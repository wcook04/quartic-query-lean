// How the site names the four papers. The edition owns their content; this
// file owns only the switcher's words and the order a newcomer meets them.
export interface PaperFace {
  id: string;
  tab: string;
  name: string;
  byline: string;
}

export const PAPERS: PaperFace[] = [
  { id: "original", tab: "Original paper", name: "A Nearly Quartic Separation Between Randomized and Quantum Query Complexity", byline: "OpenAI, 5 October 2026. The published PDF, unchanged. The Lean beside it is the Quartic project’s." },
  { id: "exposition", tab: "Learn", name: "How many bits must an algorithm read?", byline: "Will Cook, November 2026. A general mathematical exposition of OpenAI’s construction." },
  { id: "expert", tab: "Expert", name: "Reconstructing OpenAI’s nearly quartic query separation", byline: "Will Cook, November 2026. The decisive steps, for readers who know query complexity." },
  { id: "reconstruction", tab: "Full proof", name: "OpenAI’s nearly quartic query separation: a complete proof reconstruction", byline: "Will Cook, November 2026. Every step of the argument, keyed to the Lean statements." },
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
  if (/^[A-Z]?\d/.test(m[2])) return `${kind} ${m[2].replace(/\.(i{1,3}|iv|v)$/, "($1)")}`;
  return `${kind}: ${m[2].replace(/-/g, " ")}`;
}
