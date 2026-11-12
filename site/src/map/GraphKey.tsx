// The graph's key: each line style the displayed graph uses, drawn with the
// map's own line classes and tokens (tree.css, graph.css), named in plain words.
// Styles absent from the displayed graph are left out of the key.
import type { ArgGraph } from "../model/graph";
import { STYLE_WORDS, drawnHelpers, lineStyle, type LineStyle } from "./edgeMeaning";
import { GOAL } from "./fromProofMap";

const ORDER: LineStyle[] = ["proof", "statement", "structure", "paper", "context"];
const CLASS: Record<LineStyle, string> = {
  proof: "link link--supports",
  statement: "link link--lean_type_dependency",
  structure: "link link--lean_structural_dependency",
  paper: "link link--formalizes",
  context: "link link--formalizes",
};

/** Whether the main result reaches `id` by drawn lines: the route the map draws in ink. */
function routed(graph: ArgGraph, id: string): boolean {
  const seen = new Set([GOAL]);
  const queue = [GOAL];
  while (queue.length) {
    const at = queue.shift()!;
    if (at === id) return true;
    for (const e of graph.out.get(at) ?? []) if (!seen.has(e.to)) { seen.add(e.to); queue.push(e.to); }
  }
  return false;
}

/** `badges`: the map draws "+N" helper badges (not in Whole proof). `list`: the list form
 *  is shown, which draws no arrows; its rows carry the same line samples and name helpers in words.
 *  `passage`: the paragraph's own steps (amber); `selected`: the drawn selected card (ink outline);
 *  `route`: whether the map draws the selected card's route to the main result. Each card and
 *  line state is listed only when the displayed graph contains it. */
export function GraphKey({ graph, notesRef, badges = true, list = false, passage = null, selected = null, route = true }: { graph: ArgGraph; notesRef(el: HTMLElement | null): void; badges?: boolean; list?: boolean; passage?: ReadonlySet<string> | null; selected?: string | null; route?: boolean }) {
  const present = new Set(graph.edges.map(lineStyle));
  const helpers = badges && !list && graph.edges.some((e) => (drawnHelpers(e) ?? 0) > 0);
  const cards = [...graph.nodes.keys()].filter((id) => id !== GOAL);
  const here = cards.some((id) => passage?.has(id));
  const others = cards.some((id) => !passage?.has(id) && id !== selected);
  const hereLine = !list && !!passage && graph.edges.some((e) => passage.has(e.from) && passage.has(e.to));
  const routeLine = !list && route && !!selected && routed(graph, selected);
  return (
    <div className="gkey">
      <p className="gkey__intro">{list ? "A click on a row selects it; a click on a line opens where it is used." : "Arrows point to the result that uses each step. A click on a card selects it; a click on a line opens where it is used."}</p>
      <ul className="gkey__list" aria-label={list ? "Line styles in the rows" : "Line styles"}>
        {here && <li><span className="gkey__card gkey__card--here" aria-hidden="true" />used by this paragraph</li>}
        {selected && <li><span className="gkey__card gkey__card--selected" aria-hidden="true" />selected card</li>}
        {others && <li><span className="gkey__card" aria-hidden="true" />other Lean theorems and definitions</li>}
        {hereLine && (
          <li>
            <svg className="gkey__sample" viewBox="0 0 28 8" width="28" height="8" aria-hidden="true"><path className="link link--supports link--lit" d="M1 4H27" /></svg>
            between this paragraph’s steps
          </li>
        )}
        {routeLine && (
          <li>
            <svg className="gkey__sample" viewBox="0 0 28 8" width="28" height="8" aria-hidden="true"><path className="link link--supports link--route" d="M1 4H27" /></svg>
            from the selected card to the main result
          </li>
        )}
        {ORDER.filter((s) => s === "proof" || present.has(s)).map((s) => (
          <li key={s}>
            <svg className="gkey__sample" viewBox="0 0 28 8" width="28" height="8" aria-hidden="true">
              <path className={CLASS[s]} data-context={s === "context" || undefined} d="M1 4H27" />
            </svg>
            {STYLE_WORDS[s]}
          </li>
        ))}
        {helpers && (
          <li>
            <svg className="gkey__sample" viewBox="0 0 28 16" width="28" height="16" aria-hidden="true">
              <path className="link link--supports" d="M1 8H27" />
              <g className="edge-badge" transform="translate(14 8)"><rect x={-10} y={-7} width={20} height={14} rx={7} /><text x={0} y={0.5} dominantBaseline="middle" textAnchor="middle">+2</text></g>
            </svg>
            helper lemmas between them, not drawn
          </li>
        )}
      </ul>
      <span className="gkey__notes" ref={notesRef} />
    </div>
  );
}
