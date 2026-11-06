import { href } from "./router";

export function About() {
  return (
    <main id="main" className="about" tabIndex={-1}>
      <h1>How to read the evidence</h1>
      <p>Four kinds of information appear beside the papers. Each is labelled where it appears.</p>
      <dl>
        <dt>What Lean reports</dt>
        <dd>A declaration’s printed statement, the declarations it uses and is used by, and its axioms. These come from the Lean project of this edition. An absent axiom report means no current inspection exists; it never means “no axioms”.</dd>
        <dt>Review judgments</dt>
        <dd>Whether a Lean theorem states a paper statement <em>exactly</em>, <em>more strongly</em> or only <em>in part</em>. Reviews compare the project’s maintained wording of each statement, which can differ from the published sentence; the PDF has the published words. Reviews were carried out with AI and are bound to the current Lean source.</dd>
        <dt>Recorded checks</dt>
        <dd>Lean builds and Comparator runs, each with a date and the source it applies to. A successful build is a different fact from a comparison against an independent specification.</dd>
        <dt>Editors’ links</dt>
        <dd>Which passage treats which argument, the step-by-step explanations, and the outline of the proof. These help reading; they are not proofs.</dd>
      </dl>
      <p>
        Counts of linked passages describe what you can navigate to. They do not measure how much of a paper is proved.
        The 121 indexed statements of OpenAI’s paper are those the project maintains; each carries its own judgment.
      </p>
      <p><a href={href({ page: "read", paper: "original", s: "original/thm-1.1", v: "statement", st: "thm-1.1" })}>See this on Theorem 1.1</a></p>
    </main>
  );
}
