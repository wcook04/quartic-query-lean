// What one line of the Lean graph means, in words a first-time reader can use.
// Every phrase restates a field the edition records for the edge (fromProofMap):
// the witness kinds Lean found and the helper declarations each witness passes
// through. Nothing here infers a relation the edition does not hold.
import type { ArgEdge, ArgGraph } from "../model/graph";
import type { ProofEdge } from "./fromProofMap";

export type LineStyle = "proof" | "statement" | "structure" | "paper" | "context";

export function lineStyle(edge: ArgEdge): LineStyle {
  if (edge.semanticClass === "neighbourhood_context") return "context";
  if (edge.kind === "formalizes") return "paper";
  if (edge.kind === "lean_type_dependency") return "statement";
  if (edge.kind === "lean_structural_dependency") return "structure";
  return "proof";
}

/** The legend's words for each line style, shared by the key and the list view. */
export const STYLE_WORDS: Record<LineStyle, string> = {
  proof: "used in the proof",
  statement: "used only in the statement",
  structure: "a structural reference",
  paper: "the Lean theorem for the paper’s result",
  context: "context only, not a dependency",
};

const isProof = (graph: ArgGraph, id: string) => graph.nodes.get(id)?.shape === "theorem";

/** Where the caller uses the dependency, for one witness kind. */
export function usePlace(graph: ArgGraph, from: string, kind: string): string {
  if (kind === "value") return isProof(graph, from) ? "in its proof" : "in its definition";
  if (kind === "type") return "in its statement";
  return "in its structure";
}

export function helperWords(n: number): string {
  return n === 0 ? "directly" : `through ${n} helper ${n === 1 ? "lemma" : "lemmas"} not drawn`;
}

/** Helpers on the drawn line's own witness, or null for a line with no Lean witness. */
export function drawnHelpers(edge: ArgEdge): number | null {
  const e = edge as ProofEdge;
  const first = e.witnessKinds?.[0];
  return first && e.helpers ? e.helpers[first] ?? 0 : null;
}

/** One sentence for the hover caption and the line's accessible name. */
export function edgeSentence(graph: ArgGraph, edge: ArgEdge, name: (id: string) => string): string {
  const e = edge as ProofEdge;
  const style = lineStyle(edge);
  if (style === "context") return `Context only: ${name(edge.to)} sits under the main result here because what uses it is outside this neighbourhood. Not a Lean dependency.`;
  if (style === "paper") return `${name(edge.to)} is the Lean theorem for ${name(edge.from)}. This is an editorial link, not a Lean dependency.`;
  const kinds = e.witnessKinds ?? [];
  const places = kinds.map((k) => usePlace(graph, edge.from, k));
  const where = places.length ? places.join(" and ") : "";
  const helpers = drawnHelpers(edge);
  const via = helpers == null ? "" : `, ${helperWords(helpers)}`;
  return `${name(edge.from)} uses ${name(edge.to)}${where ? ` ${where}` : ""}${via}.`;
}
