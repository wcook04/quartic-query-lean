// The graph's key: each line style the displayed graph uses, drawn with the
// map's own line classes and tokens (tree.css, graph.css), named in plain words.
// Styles absent from the displayed graph are left out of the key.
import type { ArgGraph } from "../model/graph";
import { STYLE_WORDS, drawnHelpers, lineStyle, type LineStyle } from "./edgeMeaning";

const ORDER: LineStyle[] = ["proof", "statement", "structure", "paper", "context"];
const CLASS: Record<LineStyle, string> = {
  proof: "link link--supports",
  statement: "link link--lean_type_dependency",
  structure: "link link--lean_structural_dependency",
  paper: "link link--formalizes",
  context: "link link--formalizes",
};

/** `badges`: the map draws "+N" helper badges (not in Whole proof). `list`: the list form
 *  is shown, which draws no arrows; its rows carry the same line samples and name helpers in words. */
export function GraphKey({ graph, notesRef, badges = true, list = false }: { graph: ArgGraph; notesRef(el: HTMLElement | null): void; badges?: boolean; list?: boolean }) {
  const present = new Set(graph.edges.map(lineStyle));
  const helpers = badges && !list && graph.edges.some((e) => (drawnHelpers(e) ?? 0) > 0);
  return (
    <div className="gkey">
      {!list && <p className="gkey__intro">An arrow points from a declaration to the result that uses it. Select a line for the Lean where it is used.</p>}
      <ul className="gkey__list" aria-label={list ? "Line styles in the rows" : "Line styles"}>
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
