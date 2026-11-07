// A selected passage, answering "this step in each paper": the four papers' passages
// first, then what the Lean proves (one row per declaration with its match), then
// walkthroughs and the editors' note. Each section names its source once, at its end.
import { useAsync } from "../app/useAsync";
import type { Edition } from "../app/edition";
import { inlineTex } from "../text/html";
import { byAI, COVERAGE_SENTENCE, RelationMark, SourceLine } from "./evidence";
import { DeclButton, Elsewhere, journeyName, Loaded, StatementLabel } from "./common";
import { useNav } from "./Nav";

export function PassagePanel({ edition, query }: { edition: Edition; query: any }) {
  const key = JSON.stringify(query);
  const r = useAsync(() => edition.reader.resolve(query), [edition, key]);
  return <Loaded value={r} what="passage">{(v) => <Passage r={v} />}</Loaded>;
}

const reviewedTies = (statement: any) => (statement.lean ?? []).filter((t: any) => t.review_evidence === "current" && t.relation !== "unassessed");

interface Row { name: string; relation?: string; note?: string }

function Passage({ r }: { r: any }) {
  const nav = useNav();
  const heading = r.context?.headings?.at(-1)?.title;
  const statements: any[] = r.statements ?? [];
  const topics: any[] = r.topics ?? [];
  const elsewhere = [
    ...(r.relatedSelections ?? []).flatMap((x: any) => x.selections),
    ...topics.flatMap((t: any) => t.treatments ?? []),
  ];
  const roots: any[] = (r.proof ?? []).slice(0, 6);
  const choices: any[] = (r.matches ?? []).filter((m: any) => m.id !== r.position?.id && (m.topic || m.statements?.length));
  const ownStatement = r.paper === "original" && r.position?.id ? r.position.id.replace(/^original\//, "") : null;
  const detours = topics.flatMap((t) => t.detours ?? []).filter((d: any, i: number, all: any[]) => all.findIndex((x: any) => x.paper === d.paper && x.anchor === d.anchor) === i);

  // What the Lean proves: for each statement, its reviewed declarations (the review's
  // leading match first), then the graph's starting points tied to it; the remaining
  // starting points are the editors' links.
  const shown = new Set<string>();
  const groups = statements.map((s) => {
    const lead = s.review_scope?.leading_matches?.[0]?.declaration;
    const ties = [...reviewedTies(s)].sort((a: any, b: any) => Number(b.declaration === lead) - Number(a.declaration === lead));
    const rows: Row[] = ties.map((t: any) => ({ name: t.declaration, relation: t.relation, note: t.relation === "partial" ? t.note : undefined }));
    for (const p of roots) {
      const tie = p.basis.find((b: any) => b.basis === "statement_tie" && b.statement === s.id);
      if (tie && !rows.some((x) => x.name === p.name)) rows.push({ name: p.name, relation: tie.relation });
    }
    rows.forEach((x) => shown.add(x.name));
    return { s, rows };
  });
  const tiedRoots = roots.filter((p) => !shown.has(p.name) && p.basis.some((b: any) => b.basis === "statement_tie"));
  const editorial = roots.filter((p) => !shown.has(p.name) && !p.basis.some((b: any) => b.basis === "statement_tie"));
  const by = statements.flatMap((s) => reviewedTies(s).map((t: any) => t.reviewed_by));
  const anyReviewed = groups.some((g) => g.rows.some((x) => x.relation)) || tiedRoots.length > 0;
  const noLean = r.coverage !== "associated_targets" ? COVERAGE_SENTENCE[r.coverage] ?? COVERAGE_SENTENCE.documented_passage : null;
  const notes = topics.filter((t) => t.note);

  return (
    <article className="panel panel--passage" aria-labelledby="ps-h">
      <header className="panel__head">
        <h2 id="ps-h" className="panel__title">
          {ownStatement ? <StatementLabel id={ownStatement} /> : topics[0]?.title ?? (r.page ? `Page ${r.page}` : heading ?? "Selected passage")}
        </h2>
        {r.paper === "original"
          ? <p className="panel__where">{r.position?.id ? `Page ${r.page} of OpenAI’s paper; a margin mark shows where it begins, when the PDF records the spot.` : r.matches?.length ? `${r.matches.length} indexed statements on page ${r.page}.` : `No statement is indexed on page ${r.page}. The page reads as normal.`}</p>
          : heading && topics[0] && <p className="panel__where">In “{heading}”.</p>}
      </header>

      {r.paper === "original" && !r.position?.id && r.matches?.length > 0 && (
        <ul className="plain linklist">
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

      <section className="block block--first" aria-labelledby="ps-each">
        <h3 id="ps-each" className="block__h">This step in each paper</h3>
        <Elsewhere rows={elsewhere} here={nav.paper} selected={r.position?.id ? { paper: r.paper, id: r.position.id } : undefined} />
        {detours.length > 0 && (
          <>
          <p className="linklist__lead">Go further</p>
          <ul className="plain linklist">
            {detours.map((d: any) => (
              <li key={`${d.paper}/${d.anchor}`}><button type="button" className="textbutton" onClick={() => nav.openPassage(d.paper, d.anchor)}>{d.question}</button></li>
            ))}
          </ul>
          </>
        )}
        <SourceLine kind="editors">Passages linked by the editors, to help reading; not a proof.</SourceLine>
      </section>

      {(groups.length > 0 || tiedRoots.length > 0 || editorial.length > 0) && (
        <section className="block" aria-labelledby="ps-proves">
          <h3 id="ps-proves" className="block__h">What the Lean proves</h3>
          {groups.map(({ s, rows }) => (
            <div key={s.id} className="proves">
              <p className="proves__against">
                <span>Against {s.id === ownStatement ? "this statement" : <StatementLabel id={s.id} presentation={s.presentation} />}</span>
                <button type="button" className="textbutton proves__cmp" onClick={() => nav.openStatement(s.id)}>Compare in full</button>
              </p>
              {rows.length > 0 ? <Rows rows={rows} /> : <p className="quiet proves__none">No current review compares a Lean declaration with this statement.</p>}
            </div>
          ))}
          {tiedRoots.length > 0 && (
            <div className="proves">
              <Rows rows={tiedRoots.map((p) => ({ name: p.name, relation: p.basis.find((b: any) => b.basis === "statement_tie")?.relation }))} />
            </div>
          )}
          {editorial.length > 0 && (
            <div className="proves">
              {(groups.length > 0 || tiedRoots.length > 0) && <p className="proves__against"><span>Also linked to this passage</span></p>}
              <Rows rows={editorial.map((p) => ({ name: p.name }))} />
            </div>
          )}
          <SourceLine kind={anyReviewed ? "review" : "editors"} by={by}>
            {anyReviewed && <>Matches judged by {byAI(by) ? "AI review" : "review"} against the paper’s statement, bound to the current Lean source.</>}
            {anyReviewed && editorial.length > 0 && " "}
            {editorial.length > 0 && <>{anyReviewed ? "Unmarked rows are" : "These declarations are"} linked by the editors.</>}
          </SourceLine>
        </section>
      )}

      {groups.length === 0 && tiedRoots.length === 0 && editorial.length === 0 && noLean && (r.paper !== "original" || r.position?.id) && (
        <section className="block" aria-labelledby="ps-proves">
          <h3 id="ps-proves" className="block__h">What the Lean proves</h3>
          <p className="quiet">{noLean}</p>
        </section>
      )}

      {r.journeys?.length > 0 && (
        <section className="block" aria-labelledby="ps-why">
          <h3 id="ps-why" className="block__h">Why it works, step by step</h3>
          <ul className="plain linklist">
            {r.journeys.map((j: string) => (
              <li key={j}><button type="button" className="textbutton" onClick={() => nav.openJourney(j)}>{journeyName(j)}</button></li>
            ))}
          </ul>
          <SourceLine kind="editors">Written by the editors, to help reading; not a proof.</SourceLine>
        </section>
      )}

      {r.comparisons?.length > 0 && (
        <section className="block" aria-labelledby="ps-checks">
          <h3 id="ps-checks" className="block__h">Recorded Comparator checks</h3>
          <ul className="plain">
            {r.comparisons.map((c: any) => (
              <li key={c.path}>
                {c.role === "negative_control" || /negative/.test(c.path) ? "A deliberately broken specification" : "A check against a separately compiled specification"}:{" "}
                <strong>{c.outcome === "passed" ? "passed" : c.outcome.replace(/_/g, " ")}</strong>
                {c.currentness !== "current" ? ", recorded for an earlier version of the Lean" : ""}.
              </li>
            ))}
          </ul>
          <SourceLine kind="check">Comparator checks that the submitted Lean theorem has the specified type. This is distinct from a review of the paper’s mathematics or the meaning of those definitions.</SourceLine>
        </section>
      )}

      {notes.length > 0 && (
        <section className="block block--quiet" aria-label="Editors’ note">
          {notes.map((t) => <p key={t.id} className="editnote"><span className="editnote__k">Editors’ note.</span> <span dangerouslySetInnerHTML={{ __html: inlineTex(t.note) }} /></p>)}
        </section>
      )}
    </article>
  );
}

/** One compact row per declaration: its plain title, then its match mark when reviewed. */
function Rows({ rows }: { rows: Row[] }) {
  return (
    <ul className="plain proves__rows">
      {rows.map((x) => (
        <li key={x.name} className="proves__row">
          <span className="proves__decl"><DeclButton name={x.name} /></span>
          {x.relation && <RelationMark relation={x.relation} />}
          {x.note && <span className="proves__note">{x.note}</span>}
        </li>
      ))}
    </ul>
  );
}
