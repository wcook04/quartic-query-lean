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
import { GOAL, drawnEdgeKey, isType, type ProofMap } from "./fromProofMap";
import { Title } from "../text/title";
import { reach } from "./treeModel";
import { drawnHelpers, edgeSentence } from "./edgeMeaning";
import { EdgeEvidence } from "./EdgeEvidence";
import { GraphKey } from "./GraphKey";
import { GraphList } from "./GraphList";
import { REF_PX, titlePieces, wrapLines } from "./canvas/representation";
import type { Metrics } from "./engine/types";
import "./tokens.css";
import "./graph.css";

const INSETS: Insets = { top: 14, right: 14, bottom: 14, left: 14 };
// Card titles here are short sentences (median about 60 characters, nine in
// ten under 90). One width per view; each tile is as tall as its own title.
const TILE_W = 204;
/** Tiles are sized for this camera scale: the pane's usual fit is about 0.85 to 1.15,
 *  and a title sized here still fits whole down to about k = 0.72. */
const DESIGN_K = 0.85;
/** On screen at DESIGN_K: a modest vertical and side padding, one 12px title size. */
const TILE_PAD_Y = 11;
const TILE_PAD_X = 6;
const TITLE_PX = 12;
const TITLE_LINE = 1.22;
const TITLE_MAX_LINES = 5;
/** The pane's spacing: ranks far enough apart that every line has a readable run (about 48px on
 *  screen at the usual fit) with room for its arrowhead and "+N" badge, and siblings far enough
 *  apart for parallel lines. Proof Reader's dense metrics are tuned for a whole map on one screen. */
const PANE_METRICS: Metrics = {
  sepCard: 28,
  sepDummy: 14,
  gapMin: 56,
  trackSp: 9,
  padTop: 18,
  padBottom: 12,
  radius: 6,
  arrow: 9,
  inset: 14,
  portSp: 12,
};
// One size for every card in a view: 12px at the usual scale, growing with
// the camera up to 14px so a closer view is not a large card of small text.
const TITLE_SIZES = (k: number) => [Math.min(14, Math.max(12, Math.round(12 * k * 2) / 2))];
const ROOT_TILE = { w: 440, h: 84 };
/** Below this pane width the map's tiles cannot hold readable titles; the list reads instead. */
const LIST_BELOW = 440;

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

export interface GraphFocus {
  cards: readonly string[];
  availableCards?: readonly string[];
  passages: readonly string[];
  paused: boolean;
  whole: boolean;
}
export interface GraphFocusRequest { nonce: number; passage: string; cards: readonly string[] }

interface Props {
  /** The edition's reading client, for the evidence behind a line. */
  reader: unknown;
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
  focusPassages?: readonly string[];
  focusRequest?: GraphFocusRequest;
  onFocusChange?(focus: GraphFocus): void;
}

/** Each card's tile height in world units: its title wrapped at TITLE_PX in the tile's width at
 *  DESIGN_K, plus padding. Words are measured with a canvas, like the engine's own title fit. */
function useTileHeights(graph: ArgGraph): (id: string) => number {
  const [fonts, setFonts] = useState(0);
  useEffect(() => {
    let live = true;
    void (document as Document & { fonts?: FontFaceSet }).fonts?.ready?.then(() => { if (live) setFonts((n) => n + 1); });
    return () => { live = false; };
  }, []);
  return useMemo(() => {
    const ctx = typeof document !== "undefined" ? document.createElement("canvas").getContext("2d") : null;
    const family = typeof document !== "undefined" ? getComputedStyle(document.documentElement).getPropertyValue("--font-sans").trim() || "sans-serif" : "sans-serif";
    const width = TILE_W * DESIGN_K - 2 - 2 * TILE_PAD_X;
    const cache = new Map<string, number>();
    const measure = (text: string) => {
      if (!ctx) return text.length * REF_PX * 0.52;
      ctx.font = `400 ${REF_PX}px ${family}`;
      return ctx.measureText(text).width * 1.06;
    };
    const space = measure(" ");
    return (id: string) => {
      let h = cache.get(id);
      if (h !== undefined) return h;
      const label = graph.nodes.get(id)?.label ?? id;
      const pieces = titlePieces(label, false).map((p, i) => ({ w: measure(p.text), gap: i > 0 && p.space ? space : 0, text: p.text }));
      const wrapped = wrapLines({ pieces, ellipsis: measure("…") }, TITLE_PX, width);
      const lines = Math.min(TITLE_MAX_LINES, Number.isFinite(wrapped) ? wrapped : 3);
      h = Math.ceil((2 + 2 * TILE_PAD_Y + lines * TITLE_PX * TITLE_LINE) / DESIGN_K);
      cache.set(id, h);
      return h;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [graph, fonts]);
}

export const GraphPane = memo(function GraphPane({ reader, map, graph, lit, selected, onSelect, selectedEdge, onEdge, progress: _progress, paperName: _paperName, selectionKey, onFollow, focusPassages = [], focusRequest, onFocusChange }: Props) {
  const tree = useRef<MapViewHandle>(null);
  const body = useRef<HTMLDivElement>(null);
  const [paused, setPaused] = useState(false);
  const pausedRef = useRef(false);
  // Fit follows viewport changes until the reader chooses their own camera.
  const overviewHeld = useRef(true);
  // The held framing is the explicit Fit (whole displayed graph) rather than the passage's steps.
  const fitHeld = useRef(false);
  const reachable = useMemo(() => reach(graph, GOAL), [graph]);
  const currentMapped = useMemo(() => lit.filter((id) => id !== GOAL && reachable.has(id)), [lit, reachable]);
  const [scopeLit, setScopeLit] = useState<readonly string[]>(currentMapped);
  const scopeLitRef = useRef(scopeLit);
  scopeLitRef.current = scopeLit;
  const [scopePassages, setScopePassages] = useState(focusPassages);
  const litIds = useMemo(() => (scopeLit.length ? new Set(scopeLit) : null), [scopeLit]);
  const litKey = currentMapped.join("|");
  const passageKey = focusPassages.join("|");
  const litRef = useRef(currentMapped);
  litRef.current = currentMapped;
  // Keep SK's actual branching neighbourhood, not a compressed ancestry path.
  const [whole, setWhole] = useState(false);
  const drawnGraph = useMemo(() => whole ? graph : neighbourhood(graph, GOAL, scopeLit), [graph, whole, scopeLit]);
  const tileHeight = useTileHeights(graph);
  const types = useMemo(() => Object.entries(map.cards).filter(([, c]) => isType(c)), [map]);
  const caption = useRef<HTMLParagraphElement>(null);
  const [notes, setNotes] = useState<HTMLElement | null>(null);
  // The line whose evidence is open under the map; Escape or the close button returns to the line.
  const [inspect, setInspect] = useState<string | null>(null);
  const [form, setForm] = useState<"map" | "list" | null>(null);
  // Phones open on the list: start from the window width so the map is not mounted and then swapped.
  const [narrow, setNarrow] = useState(() => typeof window !== "undefined" && window.innerWidth < LIST_BELOW);
  const section = useRef<HTMLElement>(null);
  useEffect(() => {
    const el = section.current;
    if (!el) return;
    const observer = new ResizeObserver(() => { if (el.clientWidth) setNarrow(el.clientWidth < LIST_BELOW); });
    observer.observe(el);
    return () => observer.disconnect();
  }, []);
  const shownView = form ?? (narrow ? "list" : "map");
  // An open line belongs to the drawn graph it came from: a new scope or passage closes it.
  useEffect(() => { setInspect(null); }, [whole, passageKey]);

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
      // Only the passage's own steps are marked. Fading every card the reader has
      // not yet passed left most of the map looking disabled before any reading.
      const state = litIds?.has(id) ? "here" : "";
      if ((card.dataset.trail ?? "") !== state) card.dataset.trail = state;
    });
  });

  useEffect(() => {
    if (pausedRef.current || whole || !litRef.current.length) return;
    overviewHeld.current = true;
    setScopeLit(litRef.current);
    setScopePassages(focusPassages);
  }, [litKey, passageKey, whole]);

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

  useEffect(() => {
    if (!focusRequest) return;
    const cards = focusRequest.cards.filter((id) => id !== GOAL && reachable.has(id));
    if (!cards.length) return;
    overviewHeld.current = true;
    setScopeLit(cards);
    setScopePassages([focusRequest.passage]);
    setWhole(false);
    setPause(false);
  }, [focusRequest, reachable, setPause]);

  useEffect(() => {
    onFocusChange?.({ cards: scopeLit, availableCards: [...reachable], passages: scopePassages, paused, whole });
  }, [scopeLit, scopePassages, paused, whole, reachable, onFocusChange]);

  // A declaration deliberately opened in Lean becomes the local centre too.
  useEffect(() => {
    if (!selected || !reachable.has(selected) || selected === GOAL || scopeLitRef.current.includes(selected)) return;
    overviewHeld.current = true;
    setScopeLit([selected]);
    setScopePassages([]);
    setWhole(false);
    setPause(true);
  }, [selected, reachable, setPause]);

  // A passage's neighbourhood is framed whole only at a scale where every title
  // is still whole; else at that scale around its own steps (and the main result).
  // Whole proof and the Fit button frame the entire displayed graph at any scale.
  const wholeRef = useRef(whole);
  wholeRef.current = whole;
  const frameHeld = useCallback((animate: boolean) => {
    if (wholeRef.current || fitHeld.current || !scopeLitRef.current.length) tree.current?.fitAll(animate);
    else tree.current?.frameFocus(scopeLitRef.current, DESIGN_K, animate);
  }, []);

  // The filtered layout has its own bounds. Frame after React commits that
  // layout, and cancel if a manual move takes ownership before the next paint.
  useEffect(() => {
    fitHeld.current = false;
    const frame = window.requestAnimationFrame(() => {
      if (overviewHeld.current) frameHeld(false);
    });
    return () => window.cancelAnimationFrame(frame);
  }, [drawnGraph, frameHeld]);

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
        const open = inspectRef.current;
        if (open) tree.current?.panTo([open.from, open.to], { centre: true });
        else if (overviewHeld.current) frameHeld(false);
        else if (!pausedRef.current && litRef.current.length && !inView(litRef.current)) tree.current?.panTo(litRef.current);
      }, 140);
    });
    observer.observe(el);
    return () => { observer.disconnect(); window.clearTimeout(timer); };
  }, [inView, frameHeld]);

  const fit = useCallback(() => {
    setPause(true);
    overviewHeld.current = true;
    fitHeld.current = true;
    tree.current?.fitAll();
  }, [setPause]);
  const follow = useCallback(() => {
    onFollow();
    overviewHeld.current = true;
    if (litRef.current.length) {
      setScopeLit(litRef.current);
      setScopePassages(focusPassages);
      }
    setWhole(false);
    setPause(false);
    fitHeld.current = false;
    frameHeld(true);
  }, [setPause, onFollow, passageKey, frameHeld]);
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
    setScopePassages([]);
    setWhole(false);
  }, [selected, reachable, follow, setPause]);

  const select = useCallback((id: string | null) => {
    if (!id || id === GOAL) return;
    overviewHeld.current = true;
    setPause(true);
    setScopeLit([id]);
    setScopePassages([]);
    setWhole(false);
    onSelect(id);
  }, [onSelect, setPause]);
  const onUserMove = useCallback(() => { overviewHeld.current = false; setPause(true); }, [setPause]);
  const noTrace = useCallback(() => undefined, []);
  const lastHit = useRef<string | null>(null);
  // The control that opened the evidence (a list row or a map line), for returning focus on close.
  const opener = useRef<HTMLElement | SVGElement | null>(null);
  const rememberOpener = () => {
    const active = document.activeElement as HTMLElement | SVGElement | null;
    opener.current = active && section.current?.contains(active) && !active.closest(".edge-ev") ? active : null;
  };
  const inspectRef = useRef<ArgEdge | null>(null);
  const edgeSelect = useCallback((key: string | null) => {
    if (!key) { setInspect(null); return; }
    // The neighbourhood's goal attachments are not Lean dependencies; they open in place and say so.
    if (drawnGraph.edges.some((edge) => edge.key === key)) { rememberOpener(); lastHit.current = key; setInspect(key); }
  }, [drawnGraph]);
  const closeEvidence = useCallback(() => {
    const key = lastHit.current;
    setInspect(null);
    // Return keyboard focus to the line that opened the evidence, when it is still drawn.
    // Prefer the remembered opener (a list row or the map line) while it is still shown;
    // otherwise the drawn line with the same name; otherwise the toolbar.
    window.requestAnimationFrame(() => {
      const shown = (el: Element | null | undefined): el is HTMLElement | SVGElement => !!el && el.isConnected && el.getClientRects().length > 0;
      const prior = opener.current;
      opener.current = null;
      if (shown(prior)) { prior.focus({ preventScroll: true }); if (document.activeElement === prior) return; }
      const hits = body.current?.querySelectorAll<SVGPathElement>(".hit[role=button]");
      const label = key && drawnGraph.edges.find((e) => e.key === key);
      if (hits && label) {
        const name = describe(label);
        const hit = [...hits].find((h) => shown(h) && h.getAttribute("aria-label")?.startsWith(name));
        if (hit) { hit.focus({ preventScroll: true }); return; }
      }
      section.current?.querySelector<HTMLElement>(".graph__bar button[aria-pressed=true]")?.focus({ preventScroll: true });
    });
  }, [drawnGraph]);
  const nameOf = useCallback((id: string) => graph.nodes.get(id)?.label ?? id, [graph]);
  const describe = useCallback((edge: ArgEdge) => edgeSentence(graph, edge, nameOf), [graph, nameOf]);
  const badge = useCallback((edge: ArgEdge) => {
    const n = drawnHelpers(edge);
    return n ? `+${n}` : null;
  }, []);
  const inspected = inspect ? drawnGraph.edges.find((e) => e.key === inspect) ?? null : null;
  inspectRef.current = inspected;
  const routeEdge = drawnEdgeKey(drawnGraph, selectedEdge);

  const view = useMemo(() => (
    <ArgumentTree
      ref={tree}
      graph={drawnGraph}
      goal={GOAL}
      insets={INSETS}
      persist={false}
      mode="overview"
      tileWidth={TILE_W}
      tileHeight={tileHeight}
      denseMetrics={PANE_METRICS}
      oneCardEach
      fitMax={1.15}
      rootTile={ROOT_TILE}
      selected={selected && drawnGraph.nodes.has(selected) ? selected : undefined}
      frameSelection={false}
      litIds={litIds}
      rootExcerpt={<span>OpenAI’s Theorem 1.1</span>}
      onSelect={select}
      onTrace={noTrace}
      onUserMove={onUserMove}
      selectedEdge={inspect ?? routeEdge ?? undefined}
      onEdgeSelect={edgeSelect}
      captionRef={caption}
      notesHost={notes}
      describeEdge={describe}
      edgeBadge={whole ? undefined : badge}
      titleSizes={TITLE_SIZES}
    />
  ), [drawnGraph, selected, litIds, select, noTrace, onUserMove, inspect, routeEdge, edgeSelect, notes, describe, badge, whole, tileHeight]);

  const following = !paused;
  // The Types popover also closes on a pointer press outside it.
  const typesRef = useRef<HTMLDetailsElement>(null);
  useEffect(() => {
    const onDown = (event: PointerEvent) => {
      const el = typesRef.current;
      if (el?.open && !el.contains(event.target as Node)) el.open = false;
    };
    document.addEventListener("pointerdown", onDown);
    return () => document.removeEventListener("pointerdown", onDown);
  }, []);
  // Under the map: the canvas shrinks and the camera keeps the line's two cards in view.
  const evidence = inspected && (
    <EdgeEvidence reader={reader} graph={drawnGraph} edge={inspected} onClose={closeEvidence}
      onOpenChain={(key) => { setInspect(null); onEdge(key); }} onOpenLean={(name) => { setInspect(null); select(name); }} />
  );
  return (
    <section ref={section} className={`graph${shownView === "list" ? " graph--list" : ""}`} aria-label="Graph of the Lean proof of Theorem 1.1">
      {/* The question the tab answers, beside whether it follows the paper. */}
      <div className="graph__head">
        {/* A heading by role, not an h2: the reader moves focus to a panel's h2, and the graph keeps focus where it was. */}
        <p className="graph__title" role="heading" aria-level={2}>{whole ? "The whole Lean proof" : scopeLit.length ? "What this paragraph relies on" : "The main result"}</p>
        {/* A stable accessible name ("Follow the paper") with aria-pressed for the state;
            the visible words change, so the state is also announced politely. */}
        <button type="button" className={`gstatus${following ? "" : " gstatus--pinned"}`} aria-pressed={following} aria-label="Follow the paper" onClick={follow}
          title={following ? "The graph moves to each linked passage as you read" : "Resume following the paper"}>
          <span className="gstatus__dot" aria-hidden="true" />
          <span aria-hidden="true">{following ? "Following the paper" : <>Pinned here · <span className="gstatus__act">Follow the paper</span></>}</span>
        </button>
      </div>
      {/* One toolbar, adapted from Lean Exposition's MapStrip controls and map shortcuts. */}
      <div className="graph__bar" role="toolbar" aria-label="Graph view controls" onKeyDown={(event) => {
        if ((event.target as HTMLElement).closest("details")) return;
        if (event.key === "+" || event.key === "=") { event.preventDefault(); zoom(1.25); }
        else if (event.key === "-" || event.key === "_") { event.preventDefault(); zoom(1 / 1.25); }
        else if (event.key === "0") { event.preventDefault(); fit(); }
      }}>
        <div className="graph__group" role="group" aria-label="Scope">
          <button type="button" className="gbtn" aria-pressed={!whole} onClick={() => whole && toggleWhole()}>This passage</button>
          <button type="button" className="gbtn" aria-pressed={whole} onClick={() => !whole && toggleWhole()}>Whole proof</button>
        </div>
        <div className="graph__group" role="group" aria-label="Form">
          <button type="button" className="gbtn" aria-pressed={shownView === "map"} onClick={() => setForm("map")}>Map</button>
          <button type="button" className="gbtn" aria-pressed={shownView === "list"} onClick={() => setForm("list")}>List</button>
        </div>
        {shownView === "map" && (
          <div className="graph__group graph__group--zoom" role="group" aria-label="Zoom">
            <button type="button" className="gbtn gbtn--icon" aria-label="Zoom out" title="Zoom out (−)" onClick={() => zoom(1 / 1.25)}>−</button>
            <button type="button" className="gbtn gbtn--icon" aria-label="Zoom in" title="Zoom in (+)" onClick={() => zoom(1.25)}>+</button>
            <button type="button" className="gbtn" title="Show the whole displayed graph (0)" onClick={fit}>
              <svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M2.5 6V2.5H6M10 2.5h3.5V6M13.5 10v3.5H10M6 13.5H2.5V10" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" /></svg>
              Fit
            </button>
            <button type="button" className="gbtn" disabled={!selected && !scopeLit.length} onClick={focus}>{selected ? "Selected card" : "This step"}</button>
          </div>
        )}
        {types.length > 0 && (
          <details className="graph__types" ref={typesRef} onKeyDown={(event) => {
            if (event.key !== "Escape" || !event.currentTarget.open) return;
            // Escape belongs to the open popover, not the proof pane around it.
            event.preventDefault();
            event.stopPropagation();
            event.currentTarget.open = false;
            event.currentTarget.querySelector<HTMLElement>("summary")?.focus();
          }}>
            <summary className="gbtn">Types <span className="graph__count">{types.length}</span></summary>
            <div className="graph__typespop" role="group" aria-label="Types the proof is written in">
              <p className="graph__typesnote">The structures the proof is written in. Choose one for its Lean.</p>
              {types.map(([name, c]) => (
                <button key={name} type="button" className={lit.includes(name) ? "is-lit" : ""} onClick={(event) => { (event.currentTarget.closest("details") as HTMLDetailsElement).open = false; onSelect(name); }} title={name} aria-label={c.title_plain || "Title unavailable"}><Title text={c.title || "Title unavailable"} /></button>
              ))}
            </div>
          </details>
        )}
      </div>
      <span className="sr-only" role="status">{following ? "The graph follows the paper." : "The graph is pinned here."}</span>
      <div className="graph__canvas" ref={body} hidden={shownView !== "map"}>
        {view}
        <p ref={caption} className="graph__caption" hidden aria-live="polite" />
      </div>
      {shownView === "list" && (
        <div className="graph__listwrap">
          <GraphList graph={drawnGraph} lit={litIds} selected={selected} selectedEdge={inspect ?? routeEdge}
            onSelect={(id) => select(id)} onEdge={(e) => { rememberOpener(); lastHit.current = e.key; setInspect(e.key); }} />
        </div>
      )}
      {evidence}
      <GraphKey graph={drawnGraph} notesRef={setNotes} badges={!whole} list={shownView === "list"} />
    </section>
  );
});
