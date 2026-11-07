import { href } from "./router";
import { RelationMark } from "../inspect/evidence";

// The four kinds of evidence, each shown with the mark the reader uses for it.
export function About() {
  return (
    <main id="main" className="about" tabIndex={-1}>
      <h1>How to read the evidence</h1>
      <p className="about__lede">Four kinds of information appear beside the papers. Each is labelled where it appears, with the mark shown here.</p>
      <ul className="evidence-kinds">
        <li className="evidence-kind">
          <h2>What Lean reports</h2>
          <p className="evidence-kind__marks" aria-hidden="true"><span className="lean-tag">Lean</span> <span className="ev__who">Lean reports</span></p>
          <p>A declaration’s printed statement, the declarations it uses and is used by, and its axioms. These come from the Lean project of this edition. An absent axiom report means no current inspection exists; it never means “no axioms”.</p>
        </li>
        <li className="evidence-kind">
          <h2>Review judgments</h2>
          <p className="evidence-kind__marks" aria-hidden="true"><RelationMark relation="exact" /> <RelationMark relation="stronger" /> <RelationMark relation="partial" /></p>
          <p>Whether a Lean theorem states a paper statement <em>exactly</em>, <em>more strongly</em> or only <em>in part</em>. Reviews compare the project’s maintained wording of each statement, which can differ from the published sentence; the PDF has the published words. Reviews were carried out with AI and are bound to the current Lean source.</p>
        </li>
        <li className="evidence-kind">
          <h2>Recorded checks</h2>
          <p>Lean builds and Comparator runs, each with a date and the source it applies to. A successful build is a different fact from a comparison against an independent specification.</p>
        </li>
        <li className="evidence-kind">
          <h2>Editors’ links</h2>
          <p className="evidence-kind__marks" aria-hidden="true"><span className="ev__who">Editors’ note</span></p>
          <p>Which passage treats which argument, the step-by-step explanations, and the outline of the proof. These help reading; they are not proofs.</p>
        </li>
      </ul>
      <p>
        Counts of linked passages describe what you can navigate to. They do not measure how much of a paper is proved.
        The 121 indexed statements of OpenAI’s paper are those the project maintains; each carries its own judgment.
      </p>
      <p className="about__next">
        <a className="tool tool--primary" href={href({ page: "read", paper: "original", s: "original/thm-1.1", v: "statement", st: "thm-1.1" })}>See this evidence on Theorem 1.1</a>
      </p>
    </main>
  );
}
