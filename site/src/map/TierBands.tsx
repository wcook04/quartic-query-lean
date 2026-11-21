// The split's half-height graph for one subject, drawn the way the Lean-neighbourhood view is:
// the cards that use the subject above, the subject (a selected card, or the steps of the
// paragraph being read), and the cards it uses below. Each band wraps into rows across the
// pane, so every direct neighbour is drawn whole at reading size; when the bands are taller than
// the graph's share, the split grows it for this subject. Whole proof keeps the full map.
import { useEffect, useLayoutEffect, useRef, useState } from "react";
import type { ArgGraph } from "../model/graph";
import { Title } from "../text/title";

/** About 10px on screen at the smallest card type. */
const MIN_SCALE = 0.72;
/** Room under the view for the "more below" cue. */
const CUE = 30;

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
  // Beyond that the bands scroll. At rest the view ends after the last whole row, never through a
  // card, and a cue under it counts the cards below.
  const [below, setBelow] = useState(0);
  const [cut, setCut] = useState<number | null>(null); // a counter: a new cut re-counts the cards below
  const [subjectFirst, setSubjectFirst] = useState(false);
  useEffect(() => {
    const el = box.current;
    if (!el) return;
    let scale = 1, timer = 0;
    el.style.removeProperty("--tier-scale");
    delete el.dataset.subjectFirst;
    setSubjectFirst(false);
    // The pane can change size (a dragged divider, the split growing): measure the cut again.
    let again = 0;
    const wrap = el.parentElement;
    const observer = wrap ? new ResizeObserver(() => { window.clearTimeout(again); again = window.setTimeout(() => settle(), 160); }) : null;
    if (wrap) observer!.observe(wrap);
    // Measured with the view at full height: end it just above the first row that would be cut.
    const settle = () => {
      el.style.removeProperty("height");
      el.style.removeProperty("bottom");
      el.scrollTop = 0;
      if (el.scrollHeight <= el.clientHeight + 1) return;
      const view = el.getBoundingClientRect();
      const subject = el.querySelector<HTMLElement>(".tier-subject")?.getBoundingClientRect();
      // A long Used-by band would push the subject out of view: the subject then comes first.
      if (subject && subject.bottom > view.bottom - CUE && !el.dataset.subjectFirst) {
        el.dataset.subjectFirst = "1";
        setSubjectFirst(true);
        timer = window.setTimeout(settle, 120);
        return;
      }
      const limit = view.bottom - CUE;
      const first = [...el.querySelectorAll<HTMLElement>(".lg-grid > li")].map((li) => li.getBoundingClientRect())
        .filter((r) => r.bottom > limit).reduce((m, r) => Math.min(m, r.top), Infinity);
      if (Number.isFinite(first)) { el.style.bottom = "auto"; el.style.height = `${Math.max(40, first - view.top - 4)}px`; }
      setCut((n) => (n ?? 0) + 1);
    };
    const fit = () => {
      if (el.scrollHeight <= el.clientHeight + 1 || scale <= MIN_SCALE) { settle(); return; }
      scale = Math.max(MIN_SCALE, scale * Math.max(0.9, Math.sqrt(el.clientHeight / el.scrollHeight)));
      el.style.setProperty("--tier-scale", String(scale));
      timer = window.setTimeout(fit, 40);
    };
    timer = window.setTimeout(fit, 450);
    return () => { window.clearTimeout(timer); window.clearTimeout(again); observer?.disconnect(); };
  }, [key]);
  // The count under the view follows the reader's scrolling.
  useEffect(() => {
    const el = box.current;
    if (!el) return;
    const count = () => {
      const bottom = el.getBoundingClientRect().bottom;
      setBelow([...el.querySelectorAll<HTMLElement>(".lg-grid > li")].filter((li) => li.getBoundingClientRect().bottom > bottom + 1).length);
    };
    count();
    el.addEventListener("scroll", count, { passive: true });
    const observer = new ResizeObserver(count);
    observer.observe(el);
    return () => { el.removeEventListener("scroll", count); observer.disconnect(); };
  }, [key, cut, subjectFirst]);
  const band = (label: string, ids: string[], subject = false) => ids.length > 0 && (
    <div className={`lg-band${subject ? " tier-subject" : ""}`}>
      <p className="lg-band__k">{label} <span>{ids.length}</span></p>
      <ul className="lg-grid">
        {ids.map((id) => <li key={id}><Card graph={graph} id={id} selected={id === selected} here={!!lit?.has(id)} onSelect={onSelect} /></li>)}
      </ul>
    </div>
  );
  const subjectBand = band(selected && inner.has(selected) ? "Selected card" : "Steps of this paragraph", middle, true);
  return (
    <div className="tier-wrap">
      <div className="tier-bands" ref={box} aria-label="The subject, what uses it and what it uses">
        {subjectFirst && subjectBand}
        {subjectFirst && users.length > 0 && <p className="lg-link" aria-hidden="true">used by ↑</p>}
        {band("Used by", users)}
        {!subjectFirst && users.length > 0 && <p className="lg-link" aria-hidden="true">uses ↓</p>}
        {!subjectFirst && subjectBand}
        {uses.length > 0 && <p className="lg-link" aria-hidden="true">{subjectFirst ? "the selected card uses ↓" : "uses ↓"}</p>}
        {band("Uses", uses)}
      </div>
      {below > 0 && (
        <button type="button" className="tier-more" onClick={() => box.current?.scrollBy({ top: box.current.clientHeight * 0.8, behavior: "smooth" })}>
          {below} more below <span aria-hidden="true">↓</span>
        </button>
      )}
    </div>
  );
}
