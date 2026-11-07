// Adapted from proof-reader's MapPane.tsx at e2df888, Copyright 2026
// proof-reader contributors, Apache-2.0. Local branching uses the actual
// lean-exposition site/src/model/leanGraph.ts neighbourhood implementation
// and MapPage.tsx call site: keep the centres, their immediate users and inputs,
// and every original edge between them. Context attachments are layout only.
// Unlinked prose retains the last valid neighbourhood and highlights. Manual
// movement freezes that neighbourhood and camera until following resumes.
// Fit / Around this step controls adapt lean-exposition's MapStrip.tsx.
import { memo, useCallback, useEffect, useMemo, useRef, useState } from "react";
import { ArgumentTree, type Insets, type MapViewHandle } from "./ArgumentTree";
import type { ArgEdge, ArgGraph } from "../model/graph";
import { GOAL, isType, type ProofMap } from "./fromProofMap";
import { Title } from "../text/title";
import { reach } from "./treeModel";
import "./tokens.css";
import "./graph.css";

const INSETS: Insets = { top: 10, right: 12, bottom: 10, left: 12 };
// Wide enough for a three-line title and the short Lean name beneath it.
const TILE_W = 196;
const TILE_H = 86;

/** SK's actual Lean neighbourhood, adapted to Quartic's ArgGraph.
 * Context edges attach retained roots to the paper claim for layout only;
 * their keys and semanticClass keep them separate from recorded dependencies. */
export function neighbourhood(graph: ArgGraph, goal: string, focus: readonly string[]): ArgGraph {
  const inGraph = focus.filter((id) => graph.nodes.has(id));
  const centre = inGraph.length ? inGraph : [goal];
  const keep = new Set([goal, ...centre]);
  for (const id of centre) {
    for (const e of graph.out.get(id) ?? []) keep.add(e.to);
    for (const e of graph.in.get(id) ?? []) keep.add(e.from);
  }
  if (centre[0] === goal)
    for (const e of graph.out.get(goal) ?? [])
      for (const u of graph.out.get(e.to) ?? []) keep.add(u.to);
  const edges: (ArgEdge & { note?: string })[] = graph.edges.filter((e) => keep.has(e.from) && keep.has(e.to)
    && (e.from !== goal || !graph.in.get(e.to)?.some((u) => u.from !== goal && keep.has(u.from))));
  const held = new Set(edges.map((e) => e.to));
  for (const id of keep) {
    if (id === goal || held.has(id)) continue;
    edges.push({ key: `context:${goal}→${id}`, from: goal, to: id,
      kind: "formalizes", linkIds: [], scoped: false, semanticClass: "neighbourhood_context",
      note: "Context only: what uses this result is outside this neighbourhood. Whole proof shows the complete graph." });
  }
  const members = graph.order.filter((id) => keep.has(id));
  const out = new Map(members.map((id) => [id, [] as ArgEdge[]]));
  const into = new Map(members.map((id) => [id, [] as ArgEdge[]]));
  for (const e of edges) { out.get(e.from)!.push(e); into.get(e.to)!.push(e); }
  return { ...graph, nodes: new Map(members.map((id) => [id, graph.nodes.get(id)!])),
    order: members, edges, out, in: into,
    regions: [{ id: goal, title: graph.regions[0]?.title ?? "", goal, members }],
    regionOf: new Map(members.map((id) => [id, goal])) };
}

interface Props {
  map: ProofMap;
  graph: ArgGraph;
  lit: readonly string[];
  selected: string | null;
  onSelect(name: string): void;
  selectedEdge: string | null;
  onEdge(key: string): void;
  progress: { total: number; visited: { count: number; cards: string[] }; cards: string[] } | null;
  paperName: string;
  selectionKey?: string;
  onFollow(): void;
}

export const GraphPane = memo(function GraphPane({ map, graph, lit, selected, onSelect, selectedEdge, onEdge, progress, paperName: _paperName, selectionKey, onFollow }: Props) {
  const tree = useRef<MapViewHandle>(null);
  const body = useRef<HTMLDivElement>(null);
  const [paused, setPaused] = useState(false);
  const pausedRef = useRef(false);
  // Fit follows viewport changes until the reader chooses their own camera.
  const overviewHeld = useRef(true);
  const reachable = useMemo(() => reach(graph, GOAL), [graph]);
  const currentMapped = useMemo(() => lit.filter((id) => id !== GOAL && reachable.has(id)), [lit, reachable]);
  const [scopeLit, setScopeLit] = useState<readonly string[]>(currentMapped);
  const litIds = useMemo(() => (scopeLit.length ? new Set(scopeLit) : null), [scopeLit]);
  const litKey = currentMapped.join("|");
  const litRef = useRef(currentMapped);
  litRef.current = currentMapped;
  // This paper's cards; the rest of the proof is drawn faded, as Proof Reader does.
  const coverage = useMemo(() => (progress ? new Set([GOAL, map.root, ...progress.cards]) : null), [progress, map.root]);
  // Keep SK's actual branching neighbourhood, not a compressed ancestry path.
  const [whole, setWhole] = useState(false);
  const drawnGraph = useMemo(() => whole ? graph : neighbourhood(graph, GOAL, scopeLit), [graph, whole, scopeLit]);
  const passed = useMemo(() => new Set(progress?.visited.cards ?? []), [progress]);
  const types = useMemo(() => Object.entries(map.cards).filter(([, c]) => isType(c)), [map]);

  const inView = useCallback((ids: readonly string[]) => {
    const canvas = body.current?.getBoundingClientRect();
    if (!canvas?.width) return true;
    return ids.every((id) => {
      const cards = body.current!.querySelectorAll<HTMLElement>(`.card[data-record="${CSS.escape(id)}"]`);
      if (!cards.length) return true;
      return [...cards].some((card) => {
        const r = card.getBoundingClientRect();
        return r.top >= canvas.top && r.bottom <= canvas.bottom && r.left >= canvas.left && r.right <= canvas.right;
      });
    });
  }, []);

  // Light the passage's cards on the tiles directly, so scrolling stays smooth.
  useEffect(() => {
    body.current?.querySelectorAll<HTMLElement>(".card[data-record]").forEach((card) => {
      const id = card.dataset.record!;
      const state = litIds?.has(id) ? "here" : coverage?.has(id) && !passed.has(id) && id !== GOAL && id !== map.root ? "ahead" : "";
      if ((card.dataset.trail ?? "") !== state) card.dataset.trail = state;
    });
  });

  useEffect(() => {
    if (pausedRef.current || whole || !litRef.current.length) return;
    overviewHeld.current = true;
    setScopeLit(litRef.current);
  }, [litKey, whole]);

  const setPause = useCallback((next: boolean) => {
    pausedRef.current = next;
    setPaused(next);
  }, []);

  // A deliberate passage click supersedes a held camera; ordinary scrolling
  // still leaves a manually paused map alone.
  useEffect(() => {
    if (!selectionKey || !litRef.current.length) return;
    overviewHeld.current = true;
    setScopeLit(litRef.current);
    setWhole(false);
    setPause(false);
  }, [selectionKey, litKey, setPause]);

  // A declaration deliberately opened in Lean becomes the local centre too.
  useEffect(() => {
    if (!selected || !reachable.has(selected) || selected === GOAL) return;
    overviewHeld.current = true;
    setScopeLit([selected]);
    setWhole(false);
    setPause(true);
  }, [selected, reachable, setPause]);

  // The filtered layout has its own bounds. Frame after React commits that
  // layout, and cancel if a manual move takes ownership before the next paint.
  useEffect(() => {
    const frame = window.requestAnimationFrame(() => {
      if (overviewHeld.current) tree.current?.fitAll(false);
    });
    return () => window.cancelAnimationFrame(frame);
  }, [drawnGraph]);

  // Adapted from Proof Reader's MapPane observer. It stays stable as the
  // passage changes, and never replaces a manually chosen pan or zoom.
  useEffect(() => {
    const el = body.current;
    if (!el) return;
    let timer = 0, size = "";
    const observer = new ResizeObserver(() => {
      if (!el.clientWidth || !el.clientHeight) return;
      const next = `${el.clientWidth}x${el.clientHeight}`;
      if (next === size) return;
      size = next;
      window.clearTimeout(timer);
      timer = window.setTimeout(() => {
        if (overviewHeld.current) tree.current?.fitAll(false);
        else if (!pausedRef.current && litRef.current.length && !inView(litRef.current)) tree.current?.panTo(litRef.current);
      }, 140);
    });
    observer.observe(el);
    return () => { observer.disconnect(); window.clearTimeout(timer); };
  }, [inView]);

  const fit = useCallback(() => {
    setPause(true);
    overviewHeld.current = true;
    tree.current?.fitAll();
  }, [setPause]);
  const follow = useCallback(() => {
    onFollow();
    overviewHeld.current = true;
    if (litRef.current.length) {
      setScopeLit(litRef.current);
      }
    setWhole(false);
    setPause(false);
    tree.current?.fitAll();
  }, [setPause, onFollow]);
  const toggleWhole = useCallback(() => {
    overviewHeld.current = true;
    if (whole) follow();
    else { setPause(true); setWhole(true); }
  }, [whole, follow, setPause]);
  const zoom = useCallback((factor: number) => {
    overviewHeld.current = false;
    setPause(true);
    tree.current?.zoomBy(factor);
  }, [setPause]);
  const focus = useCallback(() => {
    if (!selected || !reachable.has(selected)) { follow(); return; }
    overviewHeld.current = true;
    setPause(true);
    setScopeLit([selected]);
    setWhole(false);
  }, [selected, reachable, follow, setPause]);

  const select = useCallback((id: string | null) => {
    if (!id || id === GOAL) return;
    overviewHeld.current = true;
    setPause(true);
    setScopeLit([id]);
    setWhole(false);
    onSelect(id);
  }, [onSelect, setPause]);
  const onUserMove = useCallback(() => { overviewHeld.current = false; setPause(true); }, [setPause]);
  const noTrace = useCallback(() => undefined, []);
  const edgeSelect = useCallback((key: string | null) => {
    // The neighbourhood's goal attachments have no proofPath endpoint pair.
    if (key && graph.edges.some((edge) => edge.key === key)) onEdge(key);
  }, [onEdge, graph]);

  const view = useMemo(() => (
    <ArgumentTree
      ref={tree}
      graph={drawnGraph}
      goal={GOAL}
      insets={INSETS}
      persist={false}
      mode="overview"
      tileWidth={TILE_W}
      tileHeight={TILE_H}
      oneCardEach
      fitMax={1.8}
      selected={selected && drawnGraph.nodes.has(selected) ? selected : undefined}
      frameSelection={false}
      litIds={litIds}
      rootExcerpt={<span>OpenAI’s Theorem 1.1</span>}
      onSelect={select}
      onTrace={noTrace}
      onUserMove={onUserMove}
      selectedEdge={selectedEdge && drawnGraph.edges.some((edge) => edge.key === selectedEdge) ? selectedEdge : undefined}
      onEdgeSelect={edgeSelect}
    />
  ), [drawnGraph, selected, litIds, select, noTrace, onUserMove, selectedEdge, edgeSelect]);

  return (
    <section className="graph" aria-label="Graph of the Lean proof of Theorem 1.1">
      {paused && (
        <p className="graph__paused" role="status">
          Keeping this graph in place.
          <button type="button" onClick={follow}>Follow the paper again</button>
        </p>
      )}
      <div className="vocab" aria-label="Types the proof is written in">
        <span className="vocab__name">Types</span>
        <div className="vocab__list">
          {types.map(([name, c]) => (
            <button key={name} type="button" className={lit.includes(name) ? "is-lit" : ""} onClick={() => onSelect(name)} title={name} aria-label={c.title_plain || "Title unavailable"}><Title text={c.title || "Title unavailable"} /></button>
          ))}
        </div>
        <button type="button" className="vocab__whole" aria-pressed={whole} onClick={toggleWhole}>
          {whole ? "This passage" : "Whole proof"}
        </button>
      </div>
      {/* Adapted from Lean Exposition's MapStrip controls and map shortcuts. */}
      <div className="graph__controls" role="group" aria-label="Graph view controls" onKeyDown={(event) => {
        if (event.key === "+" || event.key === "=") { event.preventDefault(); zoom(1.25); }
        else if (event.key === "-" || event.key === "_") { event.preventDefault(); zoom(1 / 1.25); }
        else if (event.key === "0") { event.preventDefault(); fit(); }
      }}>
        <button type="button" className="map-fit" aria-label="Zoom out" title="Zoom out (−)" onClick={() => zoom(1 / 1.25)}>−</button>
        <button type="button" className="map-fit" aria-label="Zoom in" title="Zoom in (+)" onClick={() => zoom(1.25)}>+</button>
        <button type="button" className="map-fit" title="Show the whole displayed graph (0)" onClick={fit}>
          <svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M2.5 6V2.5H6M10 2.5h3.5V6M13.5 10v3.5H10M6 13.5H2.5V10" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" /></svg>
          Fit
        </button>
        <button type="button" className="map-fit" disabled={!selected && !scopeLit.length} onClick={focus}>{selected ? "Selected card" : "Around this step"}</button>
        <button type="button" className="map-fit" aria-pressed={!paused} onClick={follow}>Follow paper</button>
      </div>
      <div className="graph__canvas" ref={body}>{view}</div>
    </section>
  );
});
