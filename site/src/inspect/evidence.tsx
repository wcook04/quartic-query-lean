// Plain words for each kind of evidence. Each sentence says who produced the
// fact: Lean, a reviewer, a recorded check, or the editors' reading links.
export type Relation = "exact" | "stronger" | "partial" | "unassessed" | string;

export const RELATION_WORD: Record<string, string> = {
  exact: "Exact match", stronger: "Stronger in Lean", partial: "Partial match", unassessed: "Not assessed",
};

/** One sentence: what the review concluded about the maintained statement. */
export function relationSentence(relation: Relation, route?: string): string {
  const how = route === "alternative" ? " Its proof takes a different route from the paper’s." : route === "same" ? " Its proof follows the paper’s argument." : "";
  switch (relation) {
    case "exact": return `A review bound to the current source judged this Lean theorem to state exactly the maintained formulation.${how}`;
    case "stronger": return `A review bound to the current source judged this Lean theorem to imply the maintained formulation.${how}`;
    case "partial": return `A review bound to the current source judged this Lean theorem to cover only part of the maintained formulation; its note says which part.${how}`;
    default: return "No current review compares a Lean declaration with this statement.";
  }
}

/** Who produced a fact, in the four kinds the About page defines. */
export type Source = "lean" | "review" | "check" | "editors";
const WHO: Record<Source, string> = { lean: "Lean reports", review: "Review", check: "Recorded check", editors: "Editors" };
const WHO_TITLE: Record<Source, string> = {
  lean: "Reported by Lean from the project's source in this edition",
  review: "A review judgment bound to the current Lean source",
  check: "A recorded Lean build or Comparator run",
  editors: "An editorial reading link or explanation; it helps reading and is not a proof",
};
const AI_REVIEW = "AI review";
const AI_REVIEW_TITLE = "A review judgment, carried out with AI and bound to the current Lean source";

/** A review is labelled as carried out with AI only when every reviewer the edition
 *  records for it has an `ai:` identifier; otherwise, or with none recorded, it is a review. */
export function byAI(by?: string | readonly (string | null | undefined)[] | null): boolean {
  const ids = (Array.isArray(by) ? by : [by]).filter((id): id is string => typeof id === "string" && id.length > 0);
  return ids.length > 0 && ids.every((id) => id.startsWith("ai:"));
}

export function Who({ kind, by, children }: { kind: Source; by?: string | readonly (string | null | undefined)[] | null; children?: string }) {
  const ai = kind === "review" && byAI(by);
  return <span className={`who who--${kind}`} title={ai ? AI_REVIEW_TITLE : WHO_TITLE[kind]}>{children ?? (ai ? AI_REVIEW : WHO[kind])}</span>;
}

export function RelationMark({ relation }: { relation: Relation }) {
  return <span className={`rel rel--${relation}`}>{RELATION_WORD[relation] ?? relation}</span>;
}

const STANDARD = new Set(["propext", "Classical.choice", "Quot.sound"]);

/** Axioms are reported by Lean only when a current inspection exists. */
export function Axioms({ inspection, audit }: { inspection?: any; audit?: any }) {
  const current = inspection?.status === "current" ? inspection.axioms : audit?.snapshot_currentness === "current" ? audit.axioms : null;
  if (Array.isArray(current)) {
    if (current.length === 0) return <p className="ev"><Who kind="lean" /> that this declaration depends on no axioms.</p>;
    const extra = current.filter((a: string) => !STANDARD.has(a));
    return (
      <p className="ev">
        <Who kind="lean" /> these axioms: {current.map((a: string, i: number) => <span key={a}>{i ? ", " : ""}<code>{a}</code></span>)}.{" "}
        {extra.length === 0 ? "These are the three standard axioms of Lean’s classical mathematics." : <>Beyond the standard three: <strong>{extra.join(", ")}</strong>.</>}
      </p>
    );
  }
  if (inspection?.status === "stale" || audit?.historical_observation)
    return <p className="ev quiet">An earlier axiom check exists, but the Lean source has changed since, so it is not shown.</p>;
  return <p className="ev quiet">No axiom check is recorded for this declaration. Axioms are checked for the declarations compared with the papers.</p>;
}

export function Checks({ tie }: { tie: any }) {
  const build = tie.build_evidence === "current" ? "Lean built this declaration at the edition’s source." : "No current build record for this declaration.";
  const compared =
    tie.comparison_evidence === "current"
      ? "A recorded Comparator run checked this declaration against a separately written specification."
      : "No Comparator check targets this declaration directly.";
  return <p className="ev"><Who kind="check" /> {build} {compared}</p>;
}

export function Reviewer({ by }: { by?: string }) {
  if (!by) return null;
  return <Who kind="review" by={by} />;
}

export const COVERAGE_SENTENCE: Record<string, string> = {
  associated_targets: "This passage is linked to Lean.",
  documented_passage: "This passage is indexed, but nothing in Lean is linked to it.",
  unmapped: "No Lean is linked to this text. The paper reads on as normal.",
};
