// The split's half-height graph for one subject, drawn the way the Lean-neighbourhood view is:
// the cards that use the subject above, the subject (a selected card, or the steps of the
// paragraph being read), and the cards it uses below. Each band wraps into rows across the
// pane, so every direct neighbour is drawn whole at reading size; when the bands are taller than
// the graph's share, the split grows it for this subject. Whole proof keeps the full map.
import { useEffect, useLayoutEffect, useRef } from "react";
import type { ArgGraph } from "../model/graph";
import { Title } from "../text/title";

/** About 10px on screen at the smallest card type. */
const MIN_SCALE = 0.72;

function Card({ graph, id, selected, here, onSelect }: { graph: ArgGraph; id: string; selected: boolean; here: boolean; onSelect(id: string): void }) {
  const node = graph.nodes.get(id);
  if (!node) return null;
  const theorem = node.shape === "theorem";
  return (
    <button type="button" className={`lg-card tier-card${theorem ? " is-theorem" : ""}${selected ? " is-selected" : ""}${here ? " is-here" : ""}`}
      data-record={id} title={selected ? `${id}: click again to open it in the Lean tab` : id} aria-pressed={selected} onClick={() => onSelect(id)}>
      <span className="lg-card__kind">{node.kindLabel ?? (theorem ? "Theorem" : "Definition")}</span>
      <span className="lg-card__title"><Title text={node.math ?? node.label} /></span>
    </button>
  );
}

export function TierBands({ graph, goal, centre, selected, lit, onSelect }: {
  graph: ArgGraph; goal: string; centre: readonly string[]; selected: string | null; lit: ReadonlySet<string> | null; onSelect(id: string): void;
}) {
  const box = useRef<HTMLDivElement>(null);
  const middle = centre.filter((id) => graph.nodes.has(id) && id !== goal);
  const inner = new Set(middle);
  const users = [...new Set(graph.edges.filter((e) => inner.has(e.to) && e.from !== goal && !inner.has(e.from)).map((e) => e.from))];
  const uses = [...new Set(graph.edges.filter((e) => inner.has(e.from) && !inner.has(e.to) && !users.includes(e.to)).map((e) => e.to))];
  const key = [...middle, "|", ...users, "|", ...uses].join(",");
  // Report how much taller the bands are than the graph's share, so the split can give them room.
  useLayoutEffect(() => {
    const el = box.current;
    if (!el) return;
    const report = () => window.dispatchEvent(new CustomEvent("quartic:graph-need", { detail: { content: el.scrollHeight, view: el.clientHeight } }));
    report();
    const observer = new ResizeObserver(report);
    observer.observe(el);
    return () => observer.disconnect();
  }, [key]);
  useEffect(() => () => { window.dispatchEvent(new CustomEvent("quartic:graph-need", { detail: null })); }, []);
  // When the split cannot grow further, the cards' text steps down, never below 10px, until the
  // bands fit; a pane that still cannot hold them scrolls.
  useEffect(() => {
    const el = box.current;
    if (!el) return;
    let scale = 1, timer = 0;
    el.style.removeProperty("--tier-scale");
    const fit = () => {
      if (el.scrollHeight <= el.clientHeight + 1 || scale <= MIN_SCALE) return;
      scale = Math.max(MIN_SCALE, scale * Math.max(0.9, Math.sqrt(el.clientHeight / el.scrollHeight)));
      el.style.setProperty("--tier-scale", String(scale));
      timer = window.setTimeout(fit, 40);
    };
    timer = window.setTimeout(fit, 450);
    return () => window.clearTimeout(timer);
  }, [key]);
  const band = (label: string, ids: string[]) => ids.length > 0 && (
    <div className="lg-band">
      <p className="lg-band__k">{label} <span>{ids.length}</span></p>
      <ul className="lg-grid">
        {ids.map((id) => <li key={id}><Card graph={graph} id={id} selected={id === selected} here={!!lit?.has(id)} onSelect={onSelect} /></li>)}
      </ul>
    </div>
  );
  return (
    <div className="tier-bands" ref={box} aria-label="The subject, what uses it and what it uses">
      {band("Used by", users)}
      {users.length > 0 && <p className="lg-link" aria-hidden="true">uses ↓</p>}
      {band(selected && inner.has(selected) ? "Selected card" : "Steps of this paragraph", middle)}
      {uses.length > 0 && <p className="lg-link" aria-hidden="true">uses ↓</p>}
      {band("Uses", uses)}
    </div>
  );
}
