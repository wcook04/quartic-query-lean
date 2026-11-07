// "Does Lean prove this?" for one maintained statement of the paper: the answer and
// one row per compared theorem first, then the statement compared, what Lean checked,
// semantic examples and the papers. Each section names its source once, at its end.
import { useState } from "react";
import { useAsync } from "../app/useAsync";
import type { Edition } from "../app/edition";
import { LeanCode } from "../lean/LeanCode";
import { Axioms, Checks, RelationMark, relationSentence, reviewWords, SourceLine } from "./evidence";
import { DeclButton, DeclTitle, Elsewhere, Loaded, StatementLabel } from "./common";
import { useStatementNames } from "./Names";
import { Title } from "../text/title";
import { useNav } from "./Nav";

export function StatementPanel({ edition, id }: { edition: Edition; id: string }) {
  const review = useAsync(() => edition.reader.statementReview(id), [edition, id]);
  return (
    <Loaded value={review} what="statement comparison">
      {(r) => r.format === "archived_record" ? (
        <article className="panel">
          <h2><StatementLabel id={r.id} /></h2>
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
  const statementNames = useStatementNames();
  const archived = statementNames.status === "unavailable_in_edition" || statementNames.status === "archived_partial";
  const comparisons: any[] = r.comparisons;
  const lead = comparisons[0];
  const page = r.paper?.selection?.location?.page;
  const by = comparisons.map((c) => c.reviewed_by);
  // Lean's axioms and the recorded checks, said once when every compared theorem shares them.
  const key = (c: any) => JSON.stringify([c.inspection?.status, c.inspection?.axioms, c.build_evidence, c.comparison_evidence]);
  const shared = comparisons.length > 1 && comparisons.every((c) => key(c) === key(comparisons[0]));
  const typed = comparisons.filter((c) => c.inspection?.status === "current" && c.inspection.type);
  return (
    <article className="panel panel--statement" aria-labelledby="st-h">
      <header className="panel__head">
        <h2 id="st-h" className="panel__title"><StatementLabel id={r.id} presentation={r.presentation} /></h2>
        {page && (
          <p className="panel__where">
            Page {page} of OpenAI’s paper.{" "}
            {nav.paper !== "original" && (
              <button type="button" className="textbutton" onClick={() => nav.openSelection("original", r.paper.selection.id)}>Open it there</button>
            )}
          </p>
        )}
      </header>

      <section className="block block--first" aria-labelledby="st-proves">
        <h3 id="st-proves" className="block__h">Does Lean prove this?</h3>
        {lead ? (
          <>
            <ul className="plain proves__rows">
              {comparisons.map((c, i) => {
                const assumptions: string[] = c.open_assumptions ?? [];
                return (
                  <li key={c.declaration + c.file} className="proves__row">
                    <span className="proves__decl"><DeclButton name={c.declaration} /></span>
                    <RelationMark relation={c.relation} />
                    {i === 0 && <span className="proves__verdict">{relationSentence(c.relation, c.route)}</span>}
                    {c.note && <span className="proves__note">{c.note}</span>}
                    {assumptions.length > 0 && <span className="proves__note proves__note--gap">Still assumes {assumptions.map((a, i) => <span key={a}>{i ? ", " : ""}<code>{a}</code></span>)} as a hypothesis.</span>}
                  </li>
                );
              })}
            </ul>
            <SourceLine kind="review" by={by}>Compared by {reviewWords(by)} against the statement below, bound to the current Lean source.</SourceLine>
          </>
        ) : (
          <p className="answer">No current review compares a Lean declaration with this statement.</p>
        )}
      </section>

      <section className="block ledger" aria-labelledby="st-ledger">
        <h3 id="st-ledger" className="block__h">The statement that was compared</h3>
        <p className="ledger__text">{r.presentation ? <span aria-label={r.presentation.body_plain}><Title text={r.presentation.body} /></span> : archived ? r.ledgerStatement : "Statement text unavailable in this edition."}</p>
        {!archived && (
          <details className="fold">
            <summary>Original ledger wording</summary>
            <p>{r.ledgerStatement}</p>
          </details>
        )}
        <p className="srcline srcline--plain">
          The project’s maintained reading of the paper, not a quotation.
          {r.paper?.selection ? " Open the PDF for OpenAI’s exact wording." : ""}
          {r.ledgerHistory?.wording_changed && r.ledgerHistory.earlier_ledger_wording && (
            <> Review changed this wording; the earlier description was: “{r.ledgerHistory.earlier_ledger_wording}”.</>
          )}
        </p>
      </section>

      {comparisons.length > 0 && (
        <section className="block" aria-labelledby="st-checked">
          <h3 id="st-checked" className="block__h">What Lean checked</h3>
          {shared ? (
            <>
              <p className="quiet">The same for all {comparisons.length} theorems above:</p>
              <Axioms inspection={comparisons[0].inspection} />
              <Checks tie={comparisons[0]} />
            </>
          ) : comparisons.length === 1 && (
            <><Axioms inspection={lead.inspection} /><Checks tie={lead} /></>
          )}
          {comparisons.length > 1 && !shared && comparisons.map((c) => (
            <details key={c.declaration + c.file} className="fold">
              <summary>Axioms and checks for <DeclTitle name={c.declaration} /></summary>
              <Axioms inspection={c.inspection} />
              <Checks tie={c} />
            </details>
          ))}
          {typed.length > 0 && (
            <details className="fold">
              <summary>The statement Lean printed {typed.length > 1 && <span className="fold__n">{typed.length} theorems</span>}</summary>
              {typed.map((c) => (
                <div key={c.declaration + c.file} className="printed">
                  {typed.length > 1 && <h4><DeclTitle name={c.declaration} /></h4>}
                  <LeanCode text={c.inspection.type} label={`Type of ${c.declaration} as printed by Lean`} from={1} caption={<span>Statement as printed by Lean</span>} />
                </div>
              ))}
            </details>
          )}
          <SourceLine kind="lean">Reported by Lean for the current source, with the recorded builds and Comparator runs.</SourceLine>
        </section>
      )}

      {r.semanticExamples?.length > 0 && (
        <section className="block examples" aria-labelledby="st-ex">
          <h3 id="st-ex" className="block__h">Try to break the definition</h3>
          {r.semanticExamples.map((ex: any) => <Example key={ex.declaration} ex={ex} />)}
          <SourceLine kind="review">Answers written by review, bound to the current Lean source; the axioms are Lean’s report.</SourceLine>
        </section>
      )}

      <section className="block" aria-labelledby="st-papers">
        <h3 id="st-papers" className="block__h">Read it in the papers</h3>
        <Elsewhere rows={r.relatedSelections ?? []} here={nav.paper} selected={r.paper?.selection ? { paper: "original", id: r.paper.selection.id } : undefined} />
        <SourceLine kind="editors">Passages linked by the editors, to help reading; not a proof.</SourceLine>
      </section>

      {(r.ledgerHistory?.adjudication_findings?.length > 0 || r.otherTies?.length > 0) && (
        <section className="block block--quiet" aria-label="Review history">
          <details className="fold">
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
        </section>
      )}
    </article>
  );
}

function Example({ ex }: { ex: any }) {
  const [open, setOpen] = useState(false);
  return (
    <div className="example">
      <p className="example__q">{ex.question}</p>
      <p className="example__a">{ex.authored_answer}</p>
      <Axioms inspection={ex.inspection} />
      {ex.receipt_currentness === "stale" && <p className="ev ev--gap">Its recorded build receipt predates the current source. Lean’s type and axioms above are from the current inspection.</p>}
      <button type="button" className="disclose" aria-expanded={open} onClick={() => setOpen(!open)}>{open ? "Hide" : "Show"} the Lean that checks this</button>
      {open && ex.rawLean && <LeanCode text={ex.rawLean} from={ex.lines?.[0] ?? 1} label={`Lean source of ${ex.declaration}`} url={ex.sourceURL}
        caption={<span>{ex.lines ? `Lean, lines ${ex.lines[0]}–${ex.lines[1] ?? ex.lines[0]}` : "Lean source"}</span>} />}
      {open && !ex.rawLean && ex.sourceURL && <p><a href={ex.sourceURL} target="_blank" rel="noopener noreferrer">Source on GitHub</a></p>}
    </div>
  );
}
