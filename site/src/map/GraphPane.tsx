// The whole proof map, opened from the Graph view's "Whole proof map" button. Adapted from
// proof-reader's MapPane.tsx at e2df888, Copyright 2026 proof-reader contributors,
// Apache-2.0. The map pans and zooms; the paragraph's own steps are amber; a card chosen
// here becomes the subject of the Graph view's drawing (SubjectGraph.tsx). Fit and the
// zoom controls adapt lean-exposition's MapStrip.tsx.
import { memo, useCallback, useEffect, useMemo, useRef, useState } from "react";
import { ArgumentTree, type Insets, type MapViewHandle } from "./ArgumentTree";
import type { ArgEdge, ArgGraph } from "../model/graph";
import { GOAL, drawnEdgeKey, isType, type ProofMap } from "./fromProofMap";
import { Title } from "../text/title";
import { reach } from "./treeModel";
import { edgeSentence } from "./edgeMeaning";
import { EdgeEvidence } from "./EdgeEvidence";
import { GraphKey } from "./GraphKey";
import { GraphList } from "./GraphList";
import { REF_PX, titlePieces, wrapLines } from "./canvas/representation";
import type { Metrics } from "./engine/types";
import { titleHtml } from "../text/title";
import "./tokens.css";
import "./graph.css";

export const INSETS: Insets = { top: 14, right: 14, bottom: 14, left: 14 };
// Card titles here are short sentences (median about 60 characters, nine in
// ten under 90). One width per view; each tile is as tall as its own title.
export const TILE_W = 204;
/** Tiles are sized for this camera scale: the pane's usual fit is about 0.85 to 1.15,
 *  and a title sized here still fits whole down to about k = 0.72. */
const DESIGN_K = 0.85;
/** On screen at DESIGN_K: a modest vertical and side padding, one 12px title size. */
const TILE_PAD_Y = 11;
const TILE_PAD_X = 6;
const TITLE_PX = 12;
const TITLE_LINE = 1.22;
const TITLE_MAX_LINES = 8;
/** The pane's spacing: ranks far enough apart that every line has a readable run (about 48px on
 *  screen at the usual fit) with room for its arrowhead and "+N" badge, and siblings far enough
 *  apart for parallel lines. Proof Reader's dense metrics are tuned for a whole map on one screen. */
export const PANE_METRICS: Metrics = {
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
export const TITLE_SIZES = (k: number) => [Math.min(14, Math.max(12, Math.round(12 * k * 2) / 2))];
export const ROOT_TILE = { w: 440, h: 84 };
/** Below this pane width the map's tiles cannot hold readable titles; the list reads instead. */
const LIST_BELOW = 440;

interface Props {
  /** The edition's reading client, for the evidence behind a line. */
  reader: unknown;
  map: ProofMap;
  graph: ArgGraph;
  /** The paragraph's own steps, marked amber. */
  lit: readonly string[];
  /** A card chosen on the map becomes the graph's subject. */
  onSelect(name: string): void;
  /** Open a declaration in the Lean view. */
  onOpenLean(name: string): void;
  selectedEdge: string | null;
  onEdge(key: string): void;
  /** Return to the drawing around the subject. */
  onBack(): void;
}

/** Each card's tile height in world units: its title wrapped at TITLE_PX in the tile's width at
 *  DESIGN_K, plus padding. Words are measured with a canvas, like the engine's own title fit. */
export function useTileHeights(graph: ArgGraph): (id: string) => number {
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
    // A title with mathematics is measured as KaTeX lays it out, so the tile holds the typeset
    // title whole; the plain-text estimate alone left typeset titles too tall for their tiles.
    // One line of slack covers the engine fitting a formula at a size between the probe's.
    const probe = typeof document !== "undefined" ? (document.getElementById("tile-title-probe") ?? document.createElement("div")) : null;
    if (probe) {
      probe.id = "tile-title-probe";
      probe.setAttribute("aria-hidden", "true");
      probe.style.cssText = `position:absolute;left:-10000px;top:0;visibility:hidden;width:${width}px;` +
        `font:400 ${TITLE_PX}px/${TITLE_LINE} ${family};overflow-wrap:normal;word-break:normal;hyphens:manual;text-wrap:balance`;
      document.body.append(probe);
    }
    const typesetLines = (math: string) => {
      if (!probe) return 0;
      probe.innerHTML = titleHtml(math);
      return Math.round(probe.offsetHeight / (TITLE_PX * TITLE_LINE));
    };
    return (id: string) => {
      let h = cache.get(id);
      if (h !== undefined) return h;
      const node = graph.nodes.get(id);
      const label = node?.label ?? id;
      const pieces = titlePieces(label, false).map((p, i) => ({ w: measure(p.text), gap: i > 0 && p.space ? space : 0, text: p.text }));
      const wrapped = wrapLines({ pieces, ellipsis: measure("…") }, TITLE_PX, width);
      const plain = Number.isFinite(wrapped) ? wrapped : 3;
      const lines = Math.min(TITLE_MAX_LINES, Math.max(plain, node?.math && node.math !== label ? typesetLines(node.math) + 1 : 0));
      h = Math.ceil((2 + 2 * TILE_PAD_Y + lines * TITLE_PX * TITLE_LINE) / DESIGN_K);
      cache.set(id, h);
      return h;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [graph, fonts]);
}

export const GraphPane = memo(function GraphPane({ reader, map, graph, lit, onSelect, onOpenLean, selectedEdge, onEdge, onBack }: Props) {
  const tree = useRef<MapViewHandle>(null);
  const body = useRef<HTMLDivElement>(null);
  // Fit follows viewport changes until the reader moves the map.
  const held = useRef(true);
  const reachable = useMemo(() => reach(graph, GOAL), [graph]);
  const litIds = useMemo(() => {
    const ids = lit.filter((id) => id !== GOAL && reachable.has(id));
    return ids.length ? new Set(ids) : null;
  }, [lit, reachable]);
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

  // Light the paragraph's own steps on the tiles directly, so scrolling stays smooth.
  useEffect(() => {
    body.current?.querySelectorAll<HTMLElement>(".card[data-record]").forEach((card) => {
      const state = litIds?.has(card.dataset.record!) ? "here" : "";
      if ((card.dataset.trail ?? "") !== state) card.dataset.trail = state;
    });
  });

  // The whole map opens framed whole, and keeps that framing through resizes until it is moved.
  useEffect(() => {
    const frame = window.requestAnimationFrame(() => tree.current?.fitAll(false));
    return () => window.cancelAnimationFrame(frame);
  }, [graph]);
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
        else if (held.current) tree.current?.fitAll(false);
      }, 140);
    });
    observer.observe(el);
    return () => { observer.disconnect(); window.clearTimeout(timer); };
  }, []);

  const fit = useCallback(() => { held.current = true; tree.current?.fitAll(); }, []);
  const zoom = useCallback((factor: number) => { held.current = false; tree.current?.zoomBy(factor); }, []);
  const select = useCallback((id: string | null) => { if (id && id !== GOAL) onSelect(id); }, [onSelect]);
  const onUserMove = useCallback(() => { held.current = false; }, []);
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
    if (graph.edges.some((edge) => edge.key === key)) { rememberOpener(); lastHit.current = key; setInspect(key); }
  }, [graph]);
  const closeEvidence = useCallback(() => {
    const key = lastHit.current;
    setInspect(null);
    // Return keyboard focus to the line that opened the evidence, when it is still drawn.
    window.requestAnimationFrame(() => {
      const shown = (el: Element | null | undefined): el is HTMLElement | SVGElement => !!el && el.isConnected && el.getClientRects().length > 0;
      const prior = opener.current;
      opener.current = null;
      if (shown(prior)) { prior.focus({ preventScroll: true }); if (document.activeElement === prior) return; }
      const hits = body.current?.querySelectorAll<SVGPathElement>(".hit[role=button]");
      const label = key && graph.edges.find((e) => e.key === key);
      if (hits && label) {
        const name = describe(label);
        const hit = [...hits].find((h) => shown(h) && h.getAttribute("aria-label")?.startsWith(name));
        if (hit) { hit.focus({ preventScroll: true }); return; }
      }
      section.current?.querySelector<HTMLElement>(".graph__bar button[aria-pressed=true]")?.focus({ preventScroll: true });
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [graph]);
  const nameOf = useCallback((id: string) => graph.nodes.get(id)?.label ?? id, [graph]);
  const describe = useCallback((edge: ArgEdge) => edgeSentence(graph, edge, nameOf), [graph, nameOf]);
  const inspected = inspect ? graph.edges.find((e) => e.key === inspect) ?? null : null;
  inspectRef.current = inspected;
  const routeEdge = drawnEdgeKey(graph, selectedEdge);

  const view = useMemo(() => (
    <ArgumentTree
      ref={tree}
      graph={graph}
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
      titleSizes={TITLE_SIZES}
    />
  ), [graph, litIds, select, noTrace, onUserMove, inspect, routeEdge, edgeSelect, notes, describe, tileHeight]);

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
    <EdgeEvidence reader={reader} graph={graph} edge={inspected} onClose={closeEvidence}
      onOpenChain={(key) => { setInspect(null); onEdge(key); }} onOpenLean={(name) => { setInspect(null); onOpenLean(name); }} />
  );
  return (
    <section ref={section} className={`graph${shownView === "list" ? " graph--list" : ""}`} aria-label="Map of the whole Lean proof of Theorem 1.1">
      <div className="graph__head">
        {/* A heading by role, not an h2: the reader moves focus to a panel's h2, and the graph keeps focus where it was. */}
        <p className="graph__title" role="heading" aria-level={2}>The whole Lean proof</p>
        <button type="button" className="gbtn" onClick={onBack}>Around this step</button>
      </div>
      {/* One toolbar, adapted from Lean Exposition's MapStrip controls and map shortcuts. */}
      <div className="graph__bar" role="toolbar" aria-label="Map controls" onKeyDown={(event) => {
        if ((event.target as HTMLElement).closest("details")) return;
        if (event.key === "+" || event.key === "=") { event.preventDefault(); zoom(1.25); }
        else if (event.key === "-" || event.key === "_") { event.preventDefault(); zoom(1 / 1.25); }
        else if (event.key === "0") { event.preventDefault(); fit(); }
      }}>
        <div className="graph__group" role="group" aria-label="Form">
          <button type="button" className="gbtn" aria-pressed={shownView === "map"} onClick={() => setForm("map")}>Map</button>
          <button type="button" className="gbtn" aria-pressed={shownView === "list"} onClick={() => setForm("list")}>List</button>
        </div>
        {shownView === "map" && (
          <div className="graph__group graph__group--zoom" role="group" aria-label="Zoom">
            <button type="button" className="gbtn gbtn--icon" aria-label="Zoom out" title="Zoom out (−)" onClick={() => zoom(1 / 1.25)}>−</button>
            <button type="button" className="gbtn gbtn--icon" aria-label="Zoom in" title="Zoom in (+)" onClick={() => zoom(1.25)}>+</button>
            <button type="button" className="gbtn" title="Show the whole map (0)" onClick={fit}>
              <svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M2.5 6V2.5H6M10 2.5h3.5V6M13.5 10v3.5H10M6 13.5H2.5V10" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" /></svg>
              Fit
            </button>
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
                <button key={name} type="button" className={lit.includes(name) ? "is-lit" : ""} onClick={(event) => { (event.currentTarget.closest("details") as HTMLDetailsElement).open = false; onOpenLean(name); }} title={name} aria-label={c.title_plain || "Title unavailable"}><Title text={c.title || "Title unavailable"} /></button>
              ))}
            </div>
          </details>
        )}
      </div>
      <div className="graph__canvas" ref={body} hidden={shownView !== "map"}>
        {view}
        <p ref={caption} className="graph__caption" hidden aria-live="polite" />
      </div>
      {shownView === "list" && (
        <div className="graph__listwrap">
          <GraphList graph={graph} lit={litIds} selected={null} selectedEdge={inspect ?? routeEdge}
            onSelect={(id) => select(id)} onEdge={(e) => { rememberOpener(); lastHit.current = e.key; setInspect(e.key); }} />
        </div>
      )}
      {evidence}
      <GraphKey graph={graph} notesRef={setNotes} badges={false} list={shownView === "list"} passage={litIds} selected={null} route={!(inspect ?? routeEdge)} />
    </section>
  );
});
