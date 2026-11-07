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
  title_plain: string;
}
export interface ProofMap {
  currentness: string;
  root: string;
  cards: Record<string, ProofCard>;
  edges: { from: string; to: string; witnesses: Record<string, number> }[];
  /** Witness chains: [prefix index or null, kind of this hop, declaration reached]. */
  paths?: [number | null, string, string][];
}

/** One drawn dependency. Lean may record it as several witnesses (proof, statement,
 * structure); the map draws one line for the pair and keeps every witness here. */
export interface ProofEdge extends ArgEdge {
  /** Witness kinds Lean recorded for this pair, value first. */
  witnessKinds?: string[];
  /** Helper declarations each witness passes through before reaching `to`. */
  helpers?: Record<string, number>;
  note?: string;
}

const origin = (family: string, label: string, slot: 0 | 1 | 2 | 3): Origin => ({ family, label, slot, place: null, locator: null, url: null });
const LEAN = origin("lean", "Lean", 3);
const PAPER = origin("paper", "OpenAI’s paper", 1);
export const GOAL = "paper:thm-1.1";

const KIND_WORDS: Record<string, string> = { theorem: "Theorem", lemma: "Lemma", def: "Definition", abbrev: "Definition", instance: "Instance", axiom: "Axiom", opaque: "Definition" };
export const isType = (c: ProofCard) => ["inductive", "structure", "class"].includes(c.kind);
const shapeOf = (c: ProofCard) => (c.kind === "axiom" ? "axiom" : c.kind === "theorem" || c.kind === "lemma" ? "theorem" : "definition");
const EDGE_KIND: Record<string, LinkKind> = { value: "supports", type: "lean_type_dependency", structural: "lean_structural_dependency" };

const WITNESS_ORDER = ["value", "type", "structural"] as const;

/** Declarations a recorded witness chain passes through before its endpoint. */
export function helperCount(map: ProofMap, cursor: number): number {
  if (!map.paths) return 0;
  let hops = 0;
  for (let at: number | null = cursor; at != null && hops <= map.paths.length; at = map.paths[at]?.[0] ?? null) hops++;
  return Math.max(0, hops - 1);
}

/** The edge key a route may still name with a secondary witness kind. */
export function drawnEdgeKey(graph: ArgGraph, key: string | null | undefined): string | null {
  if (!key) return null;
  if (graph.edges.some((e) => e.key === key)) return key;
  const [from, to] = key.split("→");
  return graph.edges.find((e) => e.from === from && e.to === to)?.key ?? null;
}

export function proofGraph(map: ProofMap): ArgGraph {
  const nodes = new Map<string, ArgNode>();
  const blank = { papers: {}, region: GOAL, passedExtraction: true };
  nodes.set(GOAL, { ...blank, id: GOAL, ref: GOAL, kind: "goal", kindLabel: "OpenAI’s Theorem 1.1", label: "The optimal exponent is four, and a family of total functions shows it", status: "external", origin: PAPER });
  for (const [name, c] of Object.entries(map.cards)) {
    if (isType(c)) continue;
    nodes.set(name, {
      ...blank, id: name, ref: name, kind: c.kind === "axiom" ? "assumption" : "declaration",
      kindLabel: KIND_WORDS[c.kind] ?? "Definition", label: c.title_plain || "Title unavailable", math: c.title || undefined, declaration: name,
      shape: shapeOf(c), leanFill: c.kind === "axiom" ? undefined : "whole",
      status: c.kind === "axiom" ? "axiom" : "kernel_checked", origin: LEAN,
    });
  }
  const edges: ProofEdge[] = [];
  const add = (from: string, to: string, kind: LinkKind, extra: Partial<ProofEdge> = {}) =>
    edges.push({ key: `${from}→${to}→${kind}`, from, to, kind, linkIds: [`${from}→${to}`], scoped: false, semanticClass: kind, ...extra });
  add(GOAL, map.root, "formalizes");
  for (const e of map.edges) {
    if (!nodes.has(e.from) || !nodes.has(e.to)) continue;
    // One line per pair: drawing a proof use and a statement use of the same
    // declaration as two coincident lines hid one of them. The line takes its
    // pattern from the strongest witness and records all of them.
    const kinds = WITNESS_ORDER.filter((k) => Object.hasOwn(e.witnesses, k));
    if (!kinds.length) continue;
    const helpers = Object.fromEntries(kinds.map((k) => [k, helperCount(map, e.witnesses[k])]));
    add(e.from, e.to, EDGE_KIND[kinds[0]], { witnessKinds: kinds, helpers });
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
