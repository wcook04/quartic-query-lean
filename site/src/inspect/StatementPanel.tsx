// "Does Lean prove this?" for one maintained statement of the paper.
import { useState } from "react";
import { useAsync } from "../app/useAsync";
import type { Edition } from "../app/edition";
import { statementName } from "../app/papers";
import { LeanCode } from "../lean/LeanCode";
import { Axioms, Checks, RelationMark, Reviewer, relationSentence } from "./evidence";
import { DeclButton, DeclTitle, Elsewhere, Loaded } from "./common";
import { declarationTitle, useNames } from "./Names";
import { useNav } from "./Nav";

export function StatementPanel({ edition, id }: { edition: Edition; id: string }) {
  const review = useAsync(() => edition.reader.statementReview(id), [edition, id]);
  return (
    <Loaded value={review} what="statement comparison">
      {(r) => r.format === "archived_record" ? (
        <article className="panel">
          <h2>{statementName(r.id)}</h2>
          <p>{r.ledgerStatement}</p>
          <p>This edition records the following links to Lean. Its review predates the comparison of which theorem covers the whole statement.</p>
          <ul>{r.ties?.map((t: any) => <li key={t.file + t.declaration}>
            <a href={t.sourceURL} title={t.declaration}><DeclTitle name={t.declaration} /></a> ({t.relation})
          </li>)}</ul>
        </article>
      ) : <Statement r={r} />}
    </Loaded>
  );
}

function Statement({ r }: { r: any }) {
  const nav = useNav();
  const [lead, ...rest] = r.comparisons as any[];
  const page = r.paper?.selection?.location?.page;
  return (
    <article className="panel panel--statement" aria-labelledby="st-h">
      <header className="panel__head">
        <h2 id="st-h" className="panel__title">{statementName(r.id)}</h2>
        {page && (
          <p className="panel__where">
            Page {page} of OpenAI’s paper.{" "}
            {nav.paper !== "original" && (
              <button type="button" className="textbutton" onClick={() => nav.openSelection("original", r.paper.selection.id)}>Open it there</button>
            )}
          </p>
        )}
      </header>

      {lead ? (
        <section className="verdict" aria-label="What Lean proves">
          <p className="verdict__line">
            <RelationMark relation={lead.relation} /> <DeclButton name={lead.declaration} />
          </p>
          <p className="verdict__line">{relationSentence(lead.relation, lead.route)}
          </p>
        </section>
      ) : (
        <section className="verdict"><p className="verdict__line">No current review compares a Lean declaration with this statement.</p></section>
      )}

      <section className="where-else" aria-label="The same statement in the papers">
        <h3>Read it in the papers</h3>
        <Elsewhere rows={r.relatedSelections ?? []} here={nav.paper} />
      </section>

      <section className="ledger">
        <h3>The statement that was compared</h3>
        <p className="ledger__text">{r.ledgerStatement}</p>
        <p className="quiet">
          This is the project’s maintained reading of the paper, not a quotation.
          {r.paper?.selection ? " Open the PDF for OpenAI’s exact wording." : ""}
          {r.ledgerHistory?.wording_changed && r.ledgerHistory.earlier_ledger_wording && (
            <> Review changed this wording; the earlier description was: “{r.ledgerHistory.earlier_ledger_wording}”.</>
          )}
        </p>
      </section>

      {(() => {
        const key = (c: any) => JSON.stringify([c.inspection?.status, c.inspection?.axioms, c.build_evidence, c.comparison_evidence]);
        const shared = r.comparisons.length > 1 && r.comparisons.every((c: any) => key(c) === key(r.comparisons[0]));
        return (
          <>
            {shared && (
              <section className="sharedfacts" aria-label="Checked by Lean for every theorem below">
                <h3>Checked by Lean, for all {r.comparisons.length} theorems below</h3>
                <Axioms inspection={r.comparisons[0].inspection} />
                <Checks tie={r.comparisons[0]} />
              </section>
            )}
            {r.comparisons.map((c: any, i: number) => <Comparison key={c.declaration + c.file} c={c} leading={i === 0} shared={shared} />)}
          </>
        );
      })()}

      {r.semanticExamples?.length > 0 && (
        <section className="examples">
          <h3>Try to break the definition</h3>
          {r.semanticExamples.map((ex: any) => <Example key={ex.declaration} ex={ex} />)}
        </section>
      )}


      {(r.ledgerHistory?.adjudication_findings?.length > 0 || r.otherTies?.length > 0) && (
        <details className="more">
          <summary>Review history and older links</summary>
          {r.ledgerHistory?.adjudication_findings?.length > 0 && (
            <>
              <h4>Reviewer findings on this statement</h4>
              <ul className="findings">
                {r.ledgerHistory.adjudication_findings.map((f: any) => (
                  <li key={f.id}><p>{f.claim}</p><p className="quiet">{f.verdict === "accepted" ? "Accepted" : f.verdict}: {f.reason}</p></li>
                ))}
              </ul>
            </>
          )}
          {r.otherTies?.length > 0 && (
            <>
              <h4>Links without a current review</h4>
              <ul className="ties">
                {r.otherTies.map((t: any) => (
                  <li key={t.declaration + t.file}>
                    <DeclButton name={t.declaration} />{" "}
                    <span className="quiet">{t.review_evidence === "legacy_unbound" ? `An older review called it ${t.reviewed_relation}; that review is not bound to the current source.` : "Not reviewed."}</span>
                  </li>
                ))}
              </ul>
            </>
          )}
        </details>
      )}
    </article>
  );
}

function Comparison({ c, leading, shared }: { c: any; leading: boolean; shared: boolean }) {
  const nav = useNav();
  const title = declarationTitle(useNames(), c.declaration);
  const [showType, setShowType] = useState(leading);
  const assumptions: string[] = c.open_assumptions ?? [];
  return (
    <section className={`cmp${leading ? " cmp--lead" : ""}`} aria-label={`Comparison with ${title.title_plain}`}>
      <header className="cmp__head">
        <RelationMark relation={c.relation} />
        <DeclButton name={c.declaration} />
      </header>
      {c.note && (
        <p className="cmp__note"><Reviewer by={c.reviewed_by} /> {c.note}</p>
      )}
      {assumptions.length > 0 && (
        <p className="ev ev--gap">Still assumes {assumptions.map((a, i) => <span key={a}>{i ? ", " : ""}<code>{a}</code></span>)} as a hypothesis.</p>
      )}
      {!shared && <><Axioms inspection={c.inspection} /><Checks tie={c} /></>}
      {c.inspection?.status === "current" && c.inspection.type && (
        <div className="cmp__type">
          <button type="button" className="disclose" aria-expanded={showType} onClick={() => setShowType(!showType)}>
            {showType ? "Hide" : "Show"} the statement Lean printed
          </button>
          {showType && <LeanCode text={c.inspection.type} label={`Type of ${c.declaration} as printed by Lean`} from={1} />}
        </div>
      )}
    </section>
  );
}

function Example({ ex }: { ex: any }) {
  const [open, setOpen] = useState(false);
  return (
    <div className="example">
      <p className="example__q">{ex.question}</p>
      <p><Reviewer by="ai:" /> {ex.authored_answer}</p>
      <Axioms inspection={ex.inspection} />
      {ex.receipt_currentness === "stale" && <p className="ev ev--gap">Its recorded build receipt predates the current source. Lean’s type and axioms above are from the current inspection.</p>}
      <button type="button" className="disclose" aria-expanded={open} onClick={() => setOpen(!open)}>{open ? "Hide" : "Show"} the Lean that checks this</button>
      {open && ex.rawLean && <LeanCode text={ex.rawLean} from={ex.lines?.[0] ?? 1} label={`Lean source of ${ex.declaration}`} />}
      {open && <p><a href={ex.sourceURL} target="_blank" rel="noopener noreferrer">Source on GitHub</a></p>}
    </div>
  );
}
