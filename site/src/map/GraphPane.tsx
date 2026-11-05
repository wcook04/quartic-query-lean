// The Lean proof beside the paper, as Proof Reader draws it. Adapted from
// proof-reader web/src/proof/MapPane.tsx at e2df888, Copyright 2026 proof-reader
// contributors, Apache-2.0. Cards for the passage at the reading line are lit in
// amber; the camera moves only when a lit card has left the view. Moving the map
// pauses following until the reader asks for it again.
import { memo, useCallback, useEffect, useMemo, useRef, useState } from "react";
import { ArgumentTree, type Insets, type MapViewHandle } from "./ArgumentTree";
import type { ArgGraph } from "../model/graph";
import { GOAL, isType, type ProofMap } from "./fromProofMap";
import { Title } from "../text/title";
import "./tokens.css";
import "./graph.css";

const INSETS: Insets = { top: 10, right: 12, bottom: 10, left: 12 };
// Wide enough for a three-line title and the short Lean name beneath it.
const TILE_W = 196;
const TILE_H = 86;

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
}

export const GraphPane = memo(function GraphPane({ map, graph, lit, selected, onSelect, selectedEdge, onEdge, progress, paperName }: Props) {
  const tree = useRef<MapViewHandle>(null);
  const body = useRef<HTMLDivElement>(null);
  const [paused, setPaused] = useState(false);
  const pausedRef = useRef(false);
  const litIds = useMemo(() => (lit.length ? new Set(lit) : null), [lit]);
  const litKey = lit.join("|");
  const litRef = useRef(lit);
  litRef.current = lit;
  // This paper's cards; the rest of the proof is drawn faded, as Proof Reader does.
  const coverage = useMemo(() => (progress ? new Set([GOAL, map.root, ...progress.cards]) : null), [progress, map.root]);
  // Draw only this paper's cards (and the theorem they serve): a compact graph per paper.
  const [whole, setWhole] = useState(false);
  const coverKey = progress ? progress.cards.length + ":" + progress.cards[0] : "";
  // eslint-disable-next-line react-hooks/exhaustive-deps
  const within = useMemo(() => (coverage && !whole ? coverage : undefined), [coverKey, whole]);
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
    if (pausedRef.current || !lit.length) return;
    // Cards not yet drawn count as "in view"; check again after the next layout.
    const go = () => {
      const drawn = litRef.current.filter((id) => graph.nodes.has(id));
      if (!pausedRef.current && drawn.length && !inView(drawn)) tree.current?.panTo(drawn);
    };
    go();
    const t = window.setTimeout(go, 500);
    return () => window.clearTimeout(t);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [litKey]);

  const setPause = useCallback((next: boolean) => {
    pausedRef.current = next;
    setPaused(next);
  }, []);

  // Every branch drawn from the start; then frame the whole proof, or the lit cards.
  useEffect(() => {
    const open = window.setTimeout(() => tree.current?.expandAll(), 0);
    const frame = window.setTimeout(() => {
      tree.current?.fitAll(false);
      const drawn = lit.filter((id) => graph.nodes.has(id));
      if (drawn.length && !inView(drawn)) tree.current?.panTo(drawn);
    }, 80);
    // A slow first layout, or lit cards that arrive late, can frame the map after this:
    // bring the current lit cards in again once it has settled.
    const bring = () => {
      const drawn = litRef.current.filter((id) => graph.nodes.has(id));
      const ok = !drawn.length || inView(drawn);
      if (!pausedRef.current && !ok) tree.current?.panTo(drawn);
    };
    const again = [600, 1500, 2500, 4000].map((ms) => window.setTimeout(bring, ms));
    return () => { window.clearTimeout(open); window.clearTimeout(frame); again.forEach((t) => window.clearTimeout(t)); };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [graph]);

  // The room changed (the window, or the pane's width): reframe.
  useEffect(() => {
    const el = body.current;
    if (!el) return;
    let timer = 0, size = "";
    const observer = new ResizeObserver(() => {
      const next = `${el.clientWidth}x${el.clientHeight}`;
      if (next === size || !el.clientHeight) return;
      const first = !size;
      size = next;
      if (first) return;
      window.clearTimeout(timer);
      timer = window.setTimeout(() => {
        tree.current?.fitAll(false);
        if (lit.length && !inView(lit)) tree.current?.panTo(lit);
      }, 140);
    });
    observer.observe(el);
    return () => { observer.disconnect(); window.clearTimeout(timer); };
  }, [inView, lit]);

  const select = useCallback((id: string | null) => { if (id && id !== GOAL) onSelect(id); }, [onSelect]);
  const onUserMove = useCallback(() => setPause(true), [setPause]);
  const noTrace = useCallback(() => undefined, []);
  const edgeSelect = useCallback((key: string | null) => { if (key) onEdge(key); }, [onEdge]);

  const view = useMemo(() => (
    <ArgumentTree
      ref={tree}
      graph={graph}
      goal={GOAL}
      insets={INSETS}
      persist={false}
      mode="overview"
      tileWidth={TILE_W}
      tileHeight={TILE_H}
      oneCardEach
      fitMax={1.8}
      selected={selected ?? undefined}
      litIds={litIds}
      rootExcerpt={<span>OpenAI’s Theorem 1.1</span>}
      onSelect={select}
      onTrace={noTrace}
      onUserMove={onUserMove}
      selectedEdge={selectedEdge ?? undefined}
      within={within}
      onEdgeSelect={edgeSelect}
    />
  ), [graph, selected, litIds, select, noTrace, onUserMove, selectedEdge, edgeSelect, within]);

  return (
    <section className="graph" aria-label="Graph of the Lean proof of Theorem 1.1">
      {paused && (
        <p className="graph__paused" role="status">
          Paused while you move the graph.
          <button type="button" onClick={() => setPause(false)}>Follow the paper again</button>
        </p>
      )}
      <div className="vocab" aria-label="Types the proof is written in">
        <span className="vocab__name">Types</span>
        <div className="vocab__list">
          {types.map(([name, c]) => (
            <button key={name} type="button" className={lit.includes(name) ? "is-lit" : ""} onClick={() => onSelect(name)} title={name} aria-label={c.title_plain || "Title unavailable"}><Title text={c.title || "Title unavailable"} /></button>
          ))}
        </div>
        {progress && (
          <button type="button" className="vocab__whole" aria-pressed={whole} onClick={() => setWhole(!whole)}>
            {whole ? `Only ${paperName}` : "Whole proof"}
          </button>
        )}
        <span className="vocab__reached" title="Declarations linked to passages you have read in this paper. A count of what you have met, not of how much is proved.">
          {progress ? `${paperName}: met ${progress.visited.count} of ${progress.total} linked declarations` : `${graph.nodes.size - 1} declarations tied to the papers`}
        </span>
      </div>
      <div className="graph__canvas" ref={body}>{view}</div>
    </section>
  );
});
