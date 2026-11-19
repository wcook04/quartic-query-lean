// One argument at each level. Adapted from lean-exposition site/src/home/LevelsBand.tsx
// at origin/main (Copyright 2026 lean-exposition contributors, Apache-2.0): the rail of
// levels beside the main theorem's argument, laid out by the map's own engine and closed
// up to the steps the chosen level is linked to. Every number on it is counted from the
// edition's proof map when the page loads; the band adds no link of its own.
//
// The argument here is the Lean proof map the reader's graph pane draws: the main
// theorem's declarations, joined where one uses another in Lean. It has too many steps to
// read in one figure, so the drawing keeps the steps the two shortest accounts are linked
// to and joins two of them when a chain of undrawn steps connects them in Lean. The rail
// gives each level's count over the whole map.

import { useLayoutEffect, useMemo, useRef, useState } from "react";
import type { Edition } from "../app/edition";
import { href } from "../app/router";
import { PAPERS } from "../app/papers";
import { useAsync } from "../app/useAsync";
import { GOAL, isType, proofGraph, type ProofMap } from "../map/fromProofMap";
import type { ArgGraph } from "../model/graph";
import { reach, visibleEdges, visibleSet } from "../map/treeModel";
import { transitiveReduction } from "../map/engine/skeleton";
import { layoutScope, recordOf } from "../map/engine/occurrences";
import { layoutBounds, layoutTree } from "../map/engine/layout";
import { roundedPath, route } from "../map/engine/router";
import { METRICS_COMPACT, type EngineEdge, type Size } from "../map/engine/types";
import { Title, plainTitle } from "../text/title";
import { inlineTex } from "../text/html";
import "./levels.css";
import thumbExpert from "./levels/expert.webp";
import thumbExposition from "./levels/exposition.webp";
import thumbReconstruction from "./levels/reconstruction.webp";
import thumbOriginal from "./levels/original.webp";

/** The proof map as the edition serves it, with the per-paper links this band counts. */
interface LeveledMap extends ProofMap {
  papers: Record<string, { id: string; bindings: Record<string, string[]> }[]>;
  paper_cards?: Record<string, { cards: string[] }>;
}

type LevelId = "lean" | "original" | "reconstruction" | "expert" | "exposition";
const ACCOUNTS: Exclude<LevelId, "lean">[] = ["original", "reconstruction", "expert", "exposition"];
/** The two shortest accounts: the drawing keeps the steps either is linked to. */
const DRAWN_FROM: Exclude<LevelId, "lean">[] = ["expert", "exposition"];
const THUMBS: Record<Exclude<LevelId, "lean">, string> = {
  original: thumbOriginal, reconstruction: thumbReconstruction, expert: thumbExpert, exposition: thumbExposition,
};
/** Who each level is written for. The names come from the site's paper switcher. */
const WHO: Record<LevelId, string> = {
  lean: "The Quartic project’s proof, written for the Lean compiler.",
  original: "OpenAI’s paper, which states the theorem and gives its proof.",
  reconstruction: "Every step proved in detail, with its correspondence to OpenAI’s paper and to Lean.",
  expert: "The construction and its two proof mechanisms, for readers who know query complexity.",
  exposition: "The construction through examples, for readers who know probability and linear algebra.",
};

const TILE_W = 176;
const ROOT: Size = { w: 200, h: 86 };
const TITLE_PX = 13;
const TITLE_LINE = 1.25;
const PAD_Y = 9;
const PAD_X = 10;
const MAX_LINES = 6;
/** The map's compact spacing with no arrowheads, tight enough to read as one figure. */
const SPACING = { ...METRICS_COMPACT, arrow: 0, sepCard: 12, gapMin: 30, trackSp: 6, padTop: 10, padBottom: 8 };
/** The drawing never shrinks titles below this many screen pixels; it scrolls sideways instead. */
const MIN_TEXT_PX = 11;
/** On a wide window the drawing grows, up to this scale. */
const MAX_SCALE = 1.4;

const WORDS = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"];
const inWords = (n: number) => WORDS[n] ?? String(n);
const plural = (n: number, one: string, many = `${one}s`) => `${n} ${n === 1 ? one : many}`;

interface Tile { id: string; lid: string; x: number; y: number; w: number; h: number; root: boolean }
interface Drawing { tiles: Map<string, Tile>; lines: string[]; x: number; y: number; w: number; h: number }

/**
 * The argument restricted to `keep`. Two kept steps stay joined when a chain of undrawn
 * steps connects them in Lean, so a level's drawing is its own narrower graph.
 * Adapted from lean-exposition's `contract`.
 */
function contract(visible: ReadonlySet<string>, edges: readonly EngineEdge[], keep: ReadonlySet<string>, assumption: (id: string) => boolean): { visible: Set<string>; edges: EngineEdge[] } {
  const out = new Map<string, string[]>();
  for (const e of edges) out.set(e.from, [...(out.get(e.from) ?? []), e.to]);
  const kept = new Set([...visible].filter((id) => keep.has(id) && !assumption(id)));
  const joined: EngineEdge[] = [];
  for (const from of kept) {
    const seen = new Set<string>();
    const stack = [...(out.get(from) ?? [])];
    while (stack.length) {
      const id = stack.pop()!;
      if (seen.has(id)) continue;
      seen.add(id);
      if (kept.has(id)) joined.push({ key: `${from}→${id}→supports`, from, to: id, kind: "supports" });
      else stack.push(...(out.get(id) ?? []));
    }
  }
  return { visible: kept, edges: joined };
}

/** Each step's tile height: its plain title wrapped in the tile's width, measured with a canvas. */
function tileHeights(graph: ArgGraph): (id: string) => number {
  const ctx = typeof document !== "undefined" ? document.createElement("canvas").getContext("2d") : null;
  const family = typeof document !== "undefined" ? getComputedStyle(document.documentElement).getPropertyValue("--sans").trim() || "sans-serif" : "sans-serif";
  if (ctx) ctx.font = `400 ${TITLE_PX}px ${family}`;
  const measure = (s: string) => (ctx ? ctx.measureText(s).width * 1.1 : s.length * TITLE_PX * 0.52);
  const width = TILE_W - 2 - 2 * PAD_X;
  const space = measure(" ");
  return (id) => {
    const words = plainTitle(graph.nodes.get(id)?.label ?? id).split(/\s+/);
    let lines = 1;
    let line = 0;
    for (const word of words) {
      const w = measure(word);
      if (line > 0 && line + space + w > width) {
        lines++;
        line = w;
      } else line += (line > 0 ? space : 0) + w;
    }
    return Math.ceil(2 + 2 * PAD_Y + Math.min(lines, MAX_LINES) * TITLE_PX * TITLE_LINE);
  };
}

const flip = <T extends { x: number; y: number }>(p: T): T => ({ ...p, x: p.y, y: p.x });

/**
 * The drawing reads from left to right: the main theorem on the left and the steps it uses
 * to its right. The engine lays a tree out from the top down, so it is given each tile with
 * width and height exchanged and its boxes and lines are reflected in the diagonal, which
 * keeps every line clear of every tile.
 */
function drawingOf(graph: ArgGraph, keep: ReadonlySet<string>, height: (id: string) => number): Drawing {
  const all = new Set([...reach(graph, GOAL)].filter((id) => id !== GOAL));
  const whole = visibleSet(graph, GOAL, all);
  const wholeEdges = visibleEdges(graph, GOAL, whole, all);
  const isAssumption = (id: string) => graph.nodes.get(id)?.kind === "assumption";
  const { visible, edges } = contract(whole, wholeEdges, new Set([GOAL, ...keep]), isAssumption);
  const skeleton = transitiveReduction(visible, edges);
  const scope = layoutScope(GOAL, visible, skeleton.edges, isAssumption);
  // Each step is drawn once, with a line to every drawn step that uses it.
  const { layout, plan } = layoutTree({
    root: GOAL,
    nodes: scope.nodes,
    edges: scope.edges,
    size: (lid) => (lid === GOAL ? { w: ROOT.h, h: ROOT.w } : { w: height(recordOf(lid)), h: TILE_W }),
    metrics: SPACING,
  });
  const routed = route(plan, { boxes: layout.boxes, dummyX: (key) => layout.dummies.get(key)!.x });
  const lines: string[] = [];
  for (const edge of plan.edges.values()) {
    const line = routed.edges.get(edge.key);
    if (line) lines.push(roundedPath(line.points.map(flip), SPACING.radius));
  }
  for (const [, bus] of routed.buses) lines.push(roundedPath(bus.stem.map(flip), SPACING.radius));
  const tiles = new Map<string, Tile>();
  for (const [lid, box] of layout.boxes) tiles.set(lid, { id: recordOf(lid), lid, x: box.y, y: box.x, w: box.h, h: box.w, root: lid === GOAL });
  const b = layoutBounds(layout);
  return { tiles, lines, x: b.y0, y: b.x0, w: b.y1 - b.y0, h: b.x1 - b.x0 };
}

interface Facts {
  map: LeveledMap;
  graph: ArgGraph;
  /** Steps of the main theorem's Lean proof (declarations under it, not counting the paper's theorem). */
  steps: Set<string>;
  sourceFiles: number;
  cards: Record<LevelId, Set<string>>;
  passages: Record<Exclude<LevelId, "lean">, number>;
  drawn: Set<string>;
}

function factsOf(map: LeveledMap): Facts {
  const graph = proofGraph(map);
  const steps = new Set([...reach(graph, GOAL)].filter((id) => id !== GOAL));
  const linked = (paper: string) => {
    const names = map.paper_cards?.[paper]?.cards ?? (map.papers[paper] ?? []).flatMap((row) => Object.keys(row.bindings));
    return new Set(names.filter((name) => steps.has(name)));
  };
  const cards = { lean: steps } as Record<LevelId, Set<string>>;
  const passages = {} as Facts["passages"];
  for (const paper of ACCOUNTS) {
    cards[paper] = linked(paper);
    passages[paper] = (map.papers[paper] ?? []).length;
  }
  const drawn = new Set(DRAWN_FROM.flatMap((paper) => [...cards[paper]]));
  const sourceFiles = new Set(Object.entries(map.cards).filter(([name, c]) => steps.has(name) && !isType(c)).map(([, c]) => c.source)).size;
  return { map, graph, steps, sourceFiles, cards, passages, drawn };
}

export function LevelsBand({ edition }: { edition: Edition }) {
  const loaded = useAsync(() => edition.reader.proofMap() as Promise<LeveledMap>, [edition]);
  const facts = useMemo(() => (loaded.state === "ready" && loaded.value.currentness === "current" ? factsOf(loaded.value) : null), [loaded]);
  if (loaded.state === "loading") return <section className="levels levels--pending" aria-hidden="true" />;
  if (!facts) return null;
  return <Levels facts={facts} />;
}

function Levels({ facts }: { facts: Facts }) {
  const { graph, map, steps, cards, passages, drawn } = facts;
  const [level, setLevel] = useState<LevelId>("expert");

  const drawings = useMemo(() => {
    const height = tileHeights(graph);
    const out = {} as Record<LevelId, Drawing>;
    for (const id of ["lean", ...ACCOUNTS] as LevelId[]) out[id] = drawingOf(graph, new Set([...drawn].filter((name) => cards[id].has(name))), height);
    return out;
  }, [graph, drawn, cards]);
  const widest = useMemo(() => Object.values(drawings).reduce((a, b) => (b.tiles.size > a.tiles.size ? b : a)), [drawings]);
  const current = drawings[level];
  const everyTile = useMemo(() => {
    const seen = new Map<string, Tile>();
    for (const d of [widest, ...Object.values(drawings)]) for (const [lid, t] of d.tiles) if (!seen.has(lid)) seen.set(lid, t);
    return [...seen.values()];
  }, [drawings, widest]);

  const stageRef = useRef<HTMLDivElement>(null);
  const [scale, setScale] = useState(1);
  const [room, setRoom] = useState(0);
  useLayoutEffect(() => {
    const el = stageRef.current?.parentElement;
    if (!el) return;
    const measure = () => {
      setRoom(el.clientWidth);
      setScale(Math.max(MIN_TEXT_PX / TITLE_PX, Math.min(MAX_SCALE, el.clientWidth / widest.w)));
    };
    measure();
    const observer = new ResizeObserver(measure);
    observer.observe(el);
    return () => observer.disconnect();
  }, [widest.w]);

  const leftover = (d: Drawing) => (widest.h - d.h) / 2;
  const offset = (t: Tile, d: Drawing) => ({ x: t.x - d.x, y: t.y - d.y + leftover(d) });

  /** Where a step opens: the chosen paper at its first passage linked to that step, with the step's Lean. */
  const open = (name: string): string => {
    if (name === GOAL) return href({ page: "read", paper: "original", s: "original/thm-1.1", v: "statement", st: "thm-1.1" });
    const paper = level === "lean" ? "reconstruction" : level;
    const row = (map.papers[paper] ?? []).find((r) => Object.hasOwn(r.bindings, name));
    return href({ page: "read", paper, s: row?.id, v: "lean", d: name });
  };

  const total = steps.size;
  const leanHref = href({ page: "read", paper: "original", s: "original/thm-1.1", v: "lean", d: map.root });
  const rows = [
    {
      id: "lean" as LevelId,
      name: "The Lean proof",
      linked: total,
      detail: `in ${plural(facts.sourceFiles, "source file")}`,
      read: leanHref,
      readWord: "Open the main theorem’s Lean",
    },
    ...ACCOUNTS.map((paper) => {
      const face = PAPERS.find((p) => p.id === paper)!;
      return {
        id: paper as LevelId,
        name: face.tab,
        linked: cards[paper].size,
        detail: `from ${paper === "original" ? plural(passages[paper], "indexed statement") : plural(passages[paper], "linked passage")}`,
        read: href({ page: "read", paper }),
        readWord: paper === "original" ? "Read OpenAI’s paper" : "Read it here",
      };
    }),
  ];
  const rootTitle = graph.nodes.get(GOAL)?.kindLabel ?? "The main theorem";
  const shownName = rows.find((r) => r.id === level)!.name;
  const drawnCount = drawn.size;
  const shownCount = [...drawn].filter((name) => cards[level].has(name)).length;
  const shortNames = DRAWN_FROM.map((paper) => PAPERS.find((p) => p.id === paper)!.tab.toLowerCase());

  return (
    <section className="levels" aria-labelledby="levels-h">
      <h2 id="levels-h">One argument at {inWords(rows.length)} levels</h2>
      <p className="levels__text">
        The main theorem’s Lean proof has {total} steps, definitions and theorems joined by which one uses which. OpenAI’s
        paper and each account on this site are linked to some of those steps.{" "}
        <span className="levels__withdrawing">Choose a level to see which of the steps drawn here it covers, and open any step in that paper beside its Lean.</span>
      </p>
      <div className="levels__body">
        <ol className="levels__rail">
          {rows.map((row) => (
            <li
              key={row.id}
              className={`levels__row${level === row.id ? " is-chosen" : ""}`}
              onPointerEnter={(event) => { if (event.pointerType === "mouse") setLevel(row.id); }}
              onFocusCapture={() => setLevel(row.id)}
              onClick={() => setLevel(row.id)}
            >
              <div className={`levels__sheet${row.id === "lean" ? " levels__sheet--lean" : ""}`} aria-hidden="true">
                {row.id === "lean" ? (
                  <span className="levels__code">theorem {map.root.replace(/^QuarticQuery\./, "")}</span>
                ) : (
                  <img src={THUMBS[row.id as Exclude<LevelId, "lean">]} alt="" width={240} height={310} loading="lazy" decoding="async" />
                )}
              </div>
              <div className="levels__words">
                <h3 className="levels__name">{row.name}</h3>
                <p className="levels__who">{WHO[row.id]}</p>
                <p className="levels__count">
                  <span className="levels__meter" aria-hidden="true"><span style={{ width: `${(100 * row.linked) / total}%` }} /></span>
                  <span>{row.id === "lean" ? <><strong>{row.linked}</strong> steps</> : <><strong>{row.linked}</strong> of the {total} steps linked</>}, {row.detail}</span>
                </p>
                <p className="levels__links">
                  <a href={row.read}>{row.readWord}<span className="sr-only">: {row.name}</span></a>
                </p>
              </div>
            </li>
          ))}
        </ol>
        <figure className="levels__figure">
          <figcaption className="levels__cap">
            <strong>{shownName}</strong>: {level === "lean" ? `all ${drawnCount} steps drawn here are Lean declarations.` : `linked to ${shownCount} of the ${drawnCount} steps drawn here.`}
          </figcaption>
          <div className="levels__scroll">
            <div ref={stageRef} className="levels__stage" style={{ height: widest.h * scale, minWidth: widest.w * scale }}>
              <div className="levels__world" style={{ width: widest.w, height: widest.h, left: Math.max(0, (room - widest.w * scale) / 2), transform: `scale(${scale})` }}>
                <svg className="levels__lines" width={widest.w} height={widest.h} aria-hidden="true">
                  {(Object.entries(drawings) as [LevelId, Drawing][]).map(([key, d]) => (
                    <g key={key} className={level === key ? "is-shown" : undefined} transform={`translate(${-d.x} ${-d.y + leftover(d)})`}>
                      {d.lines.map((path, i) => <path key={i} d={path} />)}
                    </g>
                  ))}
                </svg>
                {everyTile.map((tile) => {
                  const here = current.tiles.get(tile.lid);
                  const at = here ? offset(here, current) : offset(tile, widest.tiles.has(tile.lid) ? widest : current);
                  const node = graph.nodes.get(tile.id);
                  const label = node?.label ?? tile.id;
                  return (
                    <a
                      key={tile.lid}
                      href={open(tile.id)}
                      className={`levels__tile${tile.root ? " levels__tile--root" : ""}${here ? "" : " is-gone"}`}
                      style={{ width: here?.w ?? tile.w, height: here?.h ?? tile.h, transform: `translate(${at.x}px, ${at.y}px)` }}
                      tabIndex={here ? undefined : -1}
                      aria-hidden={here ? undefined : true}
                      aria-label={tile.root ? `${rootTitle}: ${plainTitle(label)}` : plainTitle(label)}
                      title={tile.root ? undefined : tile.id}
                    >
                      {tile.root ? (
                        <><span className="levels__tilekind">{rootTitle}</span><span dangerouslySetInnerHTML={{ __html: inlineTex(label) }} /></>
                      ) : <Title text={node?.math ?? label} />}
                    </a>
                  );
                })}
              </div>
            </div>
          </div>
          <p className="levels__source">
            Drawn here: OpenAI’s Theorem 1.1, the Lean theorem compared with it, and the {drawnCount - 1} further Lean steps that
            the {shortNames.join(" or the ")} is linked to. A line joins two steps when the one on the left uses the one on its
            right in Lean, directly or through steps not drawn. The joins come from Lean’s recorded dependencies; the links from
            papers to steps were made with AI.
          </p>
        </figure>
      </div>
    </section>
  );
}
