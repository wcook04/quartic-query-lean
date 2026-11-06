// A selected passage: what it says, what it is linked to, and where to go next.
import { useAsync } from "../app/useAsync";
import type { Edition } from "../app/edition";
import { inlineTex } from "../text/html";
import { COVERAGE_SENTENCE, RelationMark } from "./evidence";
import { DeclButton, Elsewhere, Loaded, StatementLabel } from "./common";
import { useStatementNames } from "./Names";
import { Title } from "../text/title";
import { useNav } from "./Nav";

export function PassagePanel({ edition, query }: { edition: Edition; query: any }) {
  const key = JSON.stringify(query);
  const r = useAsync(() => edition.reader.resolve(query), [edition, key]);
  return <Loaded value={r} what="passage">{(v) => <Passage r={v} />}</Loaded>;
}

function bestTie(statement: any) {
  const current = (statement.lean ?? []).filter((t: any) => t.review_evidence === "current" && t.relation !== "unassessed");
  const lead = statement.review_scope?.leading_matches?.[0];
  return current.find((t: any) => lead && t.declaration === lead.declaration) ?? current[0] ?? null;
}

function Passage({ r }: { r: any }) {
  const nav = useNav();
  const statementNames = useStatementNames();
  const heading = r.context?.headings?.at(-1)?.title;
  const statements: any[] = r.statements ?? [];
  const topics: any[] = r.topics ?? [];
  const elsewhere = [
    ...(r.relatedSelections ?? []).flatMap((x: any) => x.selections),
    ...topics.flatMap((t: any) => t.treatments ?? []),
  ];
  const roots: any[] = (r.proof ?? []).slice(0, 6);
  const choices: any[] = (r.matches ?? []).filter((m: any) => m.id !== r.position?.id && (m.topic || m.statements?.length));
  return (
    <article className="panel panel--passage" aria-labelledby="ps-h">
      <header className="panel__head">
        <h2 id="ps-h" className="panel__title">
          {r.paper === "original" && r.position?.id ? <StatementLabel id={r.position.id.replace(/^original\//, "")} /> : topics[0]?.title ?? (r.page ? `Page ${r.page}` : heading ?? "Selected passage")}
        </h2>
        {heading && topics[0] && <p className="panel__where">In “{heading}”.</p>}
      </header>

      <p className="ev">
        {r.paper === "original"
          ? r.position?.id ? `Page ${r.page} of OpenAI’s paper. A mark in the margin shows where it begins, when the PDF records the spot.` : r.matches?.length ? `${r.matches.length} indexed statements on page ${r.page}.` : `No statement is indexed on page ${r.page}. The page reads as normal.`
          : `${COVERAGE_SENTENCE[r.coverage] ?? ""} The selected text stays highlighted in the paper.`}
      </p>
      {r.paper === "original" && !r.position?.id && r.matches?.length > 0 && (
        <ul className="plain">
          {r.matches.map((m: any) => (
            <li key={m.id}><button type="button" className="textbutton" onClick={() => nav.openSelection("original", m.id)}><StatementLabel id={m.statements?.[0] ?? m.id.replace(/^original\//, "")} /></button></li>
          ))}
        </ul>
      )}
      {choices.length > 0 && (
        <p className="quiet">
          This paragraph holds other selections too:{" "}
          {choices.map((m: any, i: number) => (
            <span key={m.id}>{i ? ", " : ""}<button type="button" className="textbutton" onClick={() => nav.openSelection(r.paper, m.id)}>{m.statements?.length ? <StatementLabel id={m.statements[0]} /> : m.topic ? m.topic.replace(/-/g, " ") : m.id.split("/").pop()}</button></span>
          ))}
        </p>
      )}

      {topics.map((t) => t.note && (
        <p key={t.id} className="note"><span className="ev__who">Editors’ note</span> <span dangerouslySetInnerHTML={{ __html: inlineTex(t.note) }} /></p>
      ))}

      <section className="where-else" aria-label="The same mathematics in the other papers">
        <h3>Read it in the other papers</h3>
        <Elsewhere rows={elsewhere} here={nav.paper} />
      </section>

      {statements.length > 0 && (
        <section aria-label="What Lean proves">
          <h3>What Lean proves</h3>
          <ul className="claims">
            {statements.map((s) => {
              const tie = bestTie(s);
              return (
                <li key={s.id} className="claim">
                  <p className="claim__head">
                    <strong><StatementLabel id={s.id} presentation={s.presentation} /></strong> {tie ? <RelationMark relation={tie.relation} /> : <span className="rel rel--unassessed">Not assessed</span>}
                  </p>
                  <p className="claim__text">{s.presentation
                    ? <span aria-label={s.presentation.body_plain}><Title text={s.presentation.body} /></span>
                    : statementNames.status === "unavailable_in_edition" || statementNames.status === "archived_partial" ? s.statement : "Statement text unavailable in this edition."}</p>
                  {s.presentation && <details className="more more--inline"><summary>Original ledger wording</summary><p>{s.statement}</p></details>}
                  <p className="claim__foot">
                    {tie && <DeclButton name={tie.declaration} />}
                    <button type="button" className="textbutton" onClick={() => nav.openStatement(s.id)}>Compare</button>
                  </p>
                </li>
              );
            })}
          </ul>
        </section>
      )}

      {r.journeys?.length > 0 && (
        <section>
          <h3>Why it works, step by step</h3>
          <ul className="plain">
            {r.journeys.map((j: string) => (
              <li key={j}><button type="button" className="button button--small" onClick={() => nav.openJourney(j)}>Walk through “{j.replace(/-/g, " ")}”</button></li>
            ))}
          </ul>
        </section>
      )}


      {roots.length > 0 && (
        <section>
          <h3>Lean to start from</h3>
          {[["Reviewed against this passage", roots.filter((p) => p.basis.some((b: any) => b.basis === "statement_tie"))],
            ["Linked by the editors", roots.filter((p) => !p.basis.some((b: any) => b.basis === "statement_tie"))]]
            .filter(([, list]) => (list as any[]).length).map(([label, list]) => (
            <div key={label as string} className="rootgroup">
              <p className="rootgroup__label">{label as string}</p>
              <ul className="roots">
                {(list as any[]).map((p) => {
                  const rel = p.basis.find((b: any) => b.basis === "statement_tie")?.relation;
                  return <li key={p.name}><DeclButton name={p.name} />{rel && <> <RelationMark relation={rel} /></>}</li>;
                })}
              </ul>
            </div>
          ))}
        </section>
      )}
      {r.comparisons?.length > 0 && (
        <section>
          <h3>Recorded Comparator checks</h3>
          <ul className="plain">
            {r.comparisons.map((c: any) => (
              <li key={c.path}>
                {c.role === "negative_control" || /negative/.test(c.path) ? "A deliberately broken specification" : "A check against an independently written specification"}:{" "}
                <strong>{c.outcome === "passed" ? "passed" : c.outcome.replace(/_/g, " ")}</strong>
                {c.currentness !== "current" ? ", recorded for an earlier version of the Lean" : ""}.
              </li>
            ))}
          </ul>
        </section>
      )}
    </article>
  );
}
