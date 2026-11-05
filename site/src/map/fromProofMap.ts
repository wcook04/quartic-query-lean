// The edition's Lean proof map as the graph Proof Reader's map engine draws.
// Adapted from proof-reader web/src/model/fromEdition.ts at e2df888, Copyright
// 2026 proof-reader contributors, Apache-2.0. Every card and edge comes from the
// edition: an edge runs from a declaration to one it uses, as Lean recorded it,
// possibly through helper lemmas the map does not draw (see proofWitness).
import type { ArgEdge, ArgGraph, ArgNode, LinkKind, Origin } from "../model/graph";

export interface ProofCard {
  kind: string;
  lines: [number, number];
  module: string;
  parent: string | null;
  source: string;
  statements: Record<string, { relation: string; review: string; route: string }>;
  title: string;
}
export interface ProofMap {
  currentness: string;
  root: string;
  cards: Record<string, ProofCard>;
  edges: { from: string; to: string; witnesses: Record<string, number> }[];
}

const origin = (family: string, label: string, slot: 0 | 1 | 2 | 3): Origin => ({ family, label, slot, place: null, locator: null, url: null });
const LEAN = origin("lean", "Lean", 3);
const PAPER = origin("paper", "OpenAI’s paper", 1);
export const GOAL = "paper:thm-1.1";

const KIND_WORDS: Record<string, string> = { theorem: "Theorem", lemma: "Lemma", def: "Definition", abbrev: "Definition", instance: "Instance", axiom: "Axiom", opaque: "Definition" };
export const isType = (c: ProofCard) => ["inductive", "structure", "class"].includes(c.kind);
const shapeOf = (c: ProofCard) => (c.kind === "axiom" ? "axiom" : c.kind === "theorem" || c.kind === "lemma" ? "theorem" : "definition");
const EDGE_KIND: Record<string, LinkKind> = { value: "supports", type: "lean_type_dependency", structural: "lean_structural_dependency" };

export function proofGraph(map: ProofMap): ArgGraph {
  const nodes = new Map<string, ArgNode>();
  const blank = { papers: {}, region: GOAL, passedExtraction: true };
  nodes.set(GOAL, { ...blank, id: GOAL, ref: GOAL, kind: "goal", kindLabel: "OpenAI’s Theorem 1.1", label: "The optimal exponent is four, and a family of total functions shows it", status: "external", origin: PAPER });
  for (const [name, c] of Object.entries(map.cards)) {
    if (isType(c)) continue;
    nodes.set(name, {
      ...blank, id: name, ref: name, kind: c.kind === "axiom" ? "assumption" : "declaration",
      kindLabel: KIND_WORDS[c.kind] ?? "Definition", label: c.title.replace(/`/g, ""), rawName: name, declaration: name,
      shape: shapeOf(c), leanFill: c.kind === "axiom" ? undefined : "whole",
      status: c.kind === "axiom" ? "axiom" : "kernel_checked", origin: LEAN,
    });
  }
  const edges: ArgEdge[] = [];
  const add = (from: string, to: string, kind: LinkKind) =>
    edges.push({ key: `${from}→${to}→${kind}`, from, to, kind, linkIds: [`${from}→${to}`], scoped: false, semanticClass: kind });
  add(GOAL, map.root, "formalizes");
  for (const e of map.edges) {
    if (!nodes.has(e.from) || !nodes.has(e.to)) continue;
    for (const k of Object.keys(e.witnesses)) if (EDGE_KIND[k]) add(e.from, e.to, EDGE_KIND[k]);
  }
  const out = new Map<string, ArgEdge[]>(), into = new Map<string, ArgEdge[]>();
  for (const id of nodes.keys()) { out.set(id, []); into.set(id, []); }
  for (const edge of edges) { out.get(edge.from)!.push(edge); into.get(edge.to)!.push(edge); }
  const members = [...nodes.keys()];
  return {
    origins: [{ family: "paper", label: "OpenAI’s paper", slot: 1, count: 1 }, { family: "lean", label: "Lean", slot: 3, count: nodes.size - 1 }],
    cites: [], nodes, order: members, edges, out, in: into,
    regions: [{ id: GOAL, title: "Theorem 1.1", goal: GOAL, members }],
    regionOf: new Map(members.map((id) => [id, GOAL])),
    goals: [GOAL], cyclic: new Set(), boundaries: new Map(),
  };
}
