// How the site names the four papers. The edition owns their content; this
// file owns only the switcher's words and the order a newcomer meets them.
export interface PaperFace {
  id: string;
  tab: string;
  name: string;
  /** Author and date, set apart from the description. */
  by?: string;
  byline: string;
}

export const PAPERS: PaperFace[] = [
  { id: "expert", tab: "Expert companion", name: "Reconstructing OpenAI’s nearly quartic query separation", by: "Will Cook, November 2026", byline: "A concise account of the construction and its two proof mechanisms. Start here if you know query complexity; no prior reading of the original is needed." },
  { id: "exposition", tab: "Worked exposition", name: "How many bits must an algorithm read?", by: "Will Cook, November 2026", byline: "The construction through examples, diagrams and intermediate calculations. Assumes probability and finite-dimensional linear algebra. Sections 1–6 are the main argument; the appendices are optional." },
  { id: "reconstruction", tab: "Full proof reconstruction", name: "OpenAI’s nearly quartic query separation: a complete proof reconstruction", by: "Will Cook, November 2026", byline: "Detailed proofs, the Forrelation lower bound and quantitative refinements, with correspondence to the original and Lean." },
  { id: "original", tab: "OpenAI original", name: "A Nearly Quartic Separation Between Randomized and Quantum Query Complexity", by: "OpenAI, 5 October 2026", byline: "The source paper. The accompanying explanations, passage links and Lean development are the Quartic project’s." },
];

export const SUPPLEMENT: PaperFace = {
  id: "verification", tab: "Verification details", name: "Verification details and statement concordance",
  byline: "The statement catalogue, checking history and formal correspondence that accompany the full proof.",
};

export function face(id: string): PaperFace {
  return PAPERS.find((p) => p.id === id) ?? (id === SUPPLEMENT.id ? SUPPLEMENT : { id, tab: id, name: id, byline: "" });
}

/** A readable name for a ledger statement ID such as thm-1.1 or eq-21. */
export function statementName(id: string): string {
  const m = /^(thm|lem|prop|cor|def|eq|claim|rem|fact|ex)-(.*)$/.exec(id);
  if (!m) return id;
  const kind = { thm: "Theorem", lem: "Lemma", prop: "Proposition", cor: "Corollary", def: "Definition", eq: "Equation", claim: "Claim", rem: "Remark", fact: "Fact", ex: "Example" }[m[1]]!;
  if (m[1] === "eq") return `Equation (${m[2]})`;
  if (/^(?:[A-Z]\.)?\d|^[A-Z]\d/.test(m[2])) return `${kind} ${m[2].replace(/\.(i{1,3}|iv|v)$/, "($1)")}`;
  return `${kind}: ${m[2].replace(/-/g, " ")}`;
}
