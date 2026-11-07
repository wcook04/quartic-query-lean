// The displayed neighbourhood as a list: every card with its full title, and
// each line between drawn cards named in words. It is the graph's keyboard and
// narrow-screen reading, drawn from exactly the edges the map draws.
import type { ArgEdge, ArgGraph } from "../model/graph";
import { Title } from "../text/title";
import { GOAL, type ProofEdge } from "./fromProofMap";
import { drawnHelpers, edgeSentence, lineStyle, usePlace } from "./edgeMeaning";

interface Props {
  graph: ArgGraph;
  lit: ReadonlySet<string> | null;
  selected: string | null;
  selectedEdge: string | null;
  onSelect(id: string): void;
  onEdge(edge: ArgEdge): void;
}

export function GraphList({ graph, lit, selected, selectedEdge, onSelect, onEdge }: Props) {
  const name = (id: string) => graph.nodes.get(id)?.label ?? id;
  const title = (id: string) => graph.nodes.get(id)?.math ?? name(id);
  const ids = graph.order.filter((id) => id !== GOAL);
  // The passage's own steps first, then the rest in the map's order.
  ids.sort((a, b) => Number(!!lit?.has(b)) - Number(!!lit?.has(a)));
  const lineWords = (e: ArgEdge) => {
    const style = lineStyle(e);
    if (style === "context") return "context only";
    const p = e as ProofEdge;
    const where = (p.witnessKinds ?? []).map((k) => usePlace(graph, e.from, k)).join(" and ");
    const n = drawnHelpers(e);
    return `${where}${n ? ` · ${n} helper${n === 1 ? "" : "s"}` : ""}`;
  };
  return (
    <div className="glist" role="region" aria-label="The displayed steps as a list">
      <ul className="glist__cards">
        {ids.map((id) => {
          const node = graph.nodes.get(id)!;
          const uses = (graph.out.get(id) ?? []).filter((e) => e.semanticClass !== "neighbourhood_context");
          const users = (graph.in.get(id) ?? []).filter((e) => e.from !== GOAL);
          return (
            <li key={id} className={`glist__card${lit?.has(id) ? " is-here" : ""}${selected === id ? " is-selected" : ""}`} data-shape={node.shape}>
              <button type="button" className="glist__title" onClick={() => onSelect(id)} aria-pressed={selected === id} title={node.declaration}>
                <span className="glist__kind">{lit?.has(id) ? "This passage · " : ""}{node.kindLabel}</span>
                <Title text={title(id)} />
              </button>
              {(uses.length > 0 || users.length > 0) && (
                <ul className="glist__edges">
                  {users.map((e) => (
                    <li key={e.key}>
                      <button type="button" className={`glist__edge${selectedEdge === e.key ? " is-selected" : ""}`} onClick={() => onEdge(e)} aria-label={edgeSentence(graph, e, name)}>
                        <span className={`glist__sample glist__sample--${lineStyle(e)}`} aria-hidden="true" />
                        <span className="glist__dir">used by</span> <span className="glist__name"><Title text={title(e.from)} /></span> <span className="glist__how">{lineWords(e)}</span>
                      </button>
                    </li>
                  ))}
                  {uses.map((e) => (
                    <li key={e.key}>
                      <button type="button" className={`glist__edge${selectedEdge === e.key ? " is-selected" : ""}`} onClick={() => onEdge(e)} aria-label={edgeSentence(graph, e, name)}>
                        <span className={`glist__sample glist__sample--${lineStyle(e)}`} aria-hidden="true" />
                        <span className="glist__dir">uses</span> <span className="glist__name"><Title text={title(e.to)} /></span> <span className="glist__how">{lineWords(e)}</span>
                      </button>
                    </li>
                  ))}
                </ul>
              )}
            </li>
          );
        })}
      </ul>
    </div>
  );
}
