// The Lean proof beside the paper, as Proof Reader draws it. Adapted from
// proof-reader web/src/proof/MapPane.tsx at e2df888, Copyright 2026 proof-reader
// contributors, Apache-2.0. Cards for the passage at the reading line are lit in
// amber; the camera moves only when a lit card has left the view. Moving the map
// pauses following until the reader asks for it again.
import { memo, useCallback, useEffect, useMemo, useRef, useState } from "react";
import { ArgumentTree, type Insets, type MapViewHandle } from "./ArgumentTree";
import type { ArgGraph } from "../model/graph";
import { GOAL, isType, type ProofMap } from "./fromProofMap";
import "./tokens.css";
import "./graph.css";

const INSETS: Insets = { top: 10, right: 12, bottom: 10, left: 12 };
const TILE_W = 134;
const TILE_H = 64;

interface Props {
  map: ProofMap;
  graph: ArgGraph;
  lit: readonly string[];
  selected: string | null;
  onSelect(name: string): void;
  selectedEdge: string | null;
  onEdge(key: string): void;
}

export const GraphPane = memo(function GraphPane({ map, graph, lit, selected, onSelect, selectedEdge, onEdge }: Props) {
  const tree = useRef<MapViewHandle>(null);
  const body = useRef<HTMLDivElement>(null);
  const [paused, setPaused] = useState(false);
  const pausedRef = useRef(false);
  const litIds = useMemo(() => (lit.length ? new Set(lit) : null), [lit]);
  const litKey = lit.join("|");
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
      const state = litIds?.has(card.dataset.record!) ? "here" : "";
      if ((card.dataset.trail ?? "") !== state) card.dataset.trail = state;
    });
  });

  useEffect(() => {
    if (pausedRef.current || !lit.length) return;
    const drawn = lit.filter((id) => graph.nodes.has(id));
    if (drawn.length && !inView(drawn)) tree.current?.panTo(drawn);
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
    // A slow first layout can frame the map after this: bring the lit cards in once more.
    const again = window.setTimeout(() => {
      const drawn = lit.filter((id) => graph.nodes.has(id));
      if (!pausedRef.current && drawn.length && !inView(drawn)) tree.current?.panTo(drawn);
    }, 600);
    return () => { window.clearTimeout(open); window.clearTimeout(frame); window.clearTimeout(again); };
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
      onEdgeSelect={edgeSelect}
    />
  ), [graph, selected, litIds, select, noTrace, onUserMove, selectedEdge, edgeSelect]);

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
            <button key={name} type="button" className={lit.includes(name) ? "is-lit" : ""} onClick={() => onSelect(name)} title={name}>{c.title}</button>
          ))}
        </div>
        <span className="vocab__reached">{graph.nodes.size - 1} declarations tied to the papers</span>
      </div>
      <div className="graph__canvas" ref={body}>{view}</div>
    </section>
  );
});
