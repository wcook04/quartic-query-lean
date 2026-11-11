// OpenAI's results beside the Lean statement each was compared with. Every label
// is the one the statement comparison panel shows: the relation of the first
// current comparison, leading matches first, exactly as `statementReview` orders
// them. This page adds no mathematical claim of its own.
import { useMemo, useState } from "react";
import type { Edition } from "../app/edition";
import { href } from "../app/router";
import { useAsync } from "../app/useAsync";
import { RELATION_WORD, RelationMark } from "../inspect/evidence";
import { Title } from "../text/title";
import "./results.css";

type Rel = "exact" | "stronger" | "partial";
const RELATIONS: Rel[] = ["exact", "stronger", "partial"];

interface Row {
  id: string;
  kind: string;
  label: string;
  title: string;
  page: number | null;
  order: [number, number];
  relation: string;
  declaration: string | null;
}

interface Results {
  rows: Row[];
  counts: Record<Rel, number>;
}

/** The paper's theorems, propositions and whole lemmas: the band's rows. */
const isMajor = (r: { id: string; kind: string }) =>
  (r.kind === "theorem" || r.kind === "proposition" || r.kind === "lemma") &&
  /^(thm|prop|lem)-([A-Z]\.)?[0-9]+(\.[0-9]+)*$/.test(r.id);

const PREFIX: Record<string, string> = { thm: "Theorem", lem: "Lemma", prop: "Proposition", cor: "Corollary", eq: "Equation" };
const KIND_WORD: Record<string, string> = {
  theorem: "Theorem", proposition: "Proposition", lemma: "Lemma", corollary: "Corollary", equation: "Equation",
  definition: "Definition", construction: "Construction", inline_claim: "Claim in the text",
};

/** thm-1.1 → Theorem 1.1, lem-2.1.ii → Lemma 2.1(ii), eq-13 → Equation (13). */
export function kindLabel(id: string, kind: string): string {
  if (kind === "inline_claim") return KIND_WORD.inline_claim;
  const m = id.match(/^([a-z]+)-(.*)$/);
  const word = m && PREFIX[m[1]];
  if (m && word && /^([0-9]|[A-Z]\.[0-9])/.test(m[2])) {
    const parts = m[2].split("-")[0].split(".");
    const number: string[] = [];
    let sub = "";
    for (const p of parts) {
      if (/^[0-9]+$/.test(p) || /^[A-Z]$/.test(p)) number.push(p);
      else { if (/^(i|ii|iii|iv|v|vi)$/.test(p)) sub = `(${p})`; break; }
    }
    return m[1] === "eq" ? `Equation (${number.join(".")})` : `${word} ${number.join(".")}${sub}`;
  }
  return KIND_WORD[kind] ?? kind;
}

/** The first comparison the statement panel shows: current ties, leading matches first. */
function leadComparison(record: any): { relation: string; declaration: string } | null {
  if (!record?.review_scope) return null;
  const current = (record.lean ?? []).filter((t: any) => t.review_evidence === "current");
  const leading = (t: any) => record.review_scope.leading_matches.some((m: any) => m.declaration === t.declaration && m.file === t.file);
  const lead = [...current.filter(leading), ...current.filter((t: any) => !leading(t))][0];
  return lead ? { relation: lead.relation, declaration: lead.declaration } : null;
}

async function loadResults(edition: Edition, scope: "all" | "major"): Promise<Results> {
  const { reader } = edition;
  const [statements, originals, titles, reading] = await Promise.all([
    reader.resource("corpus/statements.json"), reader.resource("selection/original.json"),
    reader.statementTitles(), reader.resource("reading.json"),
  ]);
  const selections = new Map<string, any>();
  for (const row of originals as any[]) for (const id of row.statements) if (!selections.has(id)) selections.set(id, row);
  const rows: Row[] = (statements as any[]).map((s) => {
    const sel = selections.get(s.id);
    return {
      id: s.id, kind: s.kind, label: kindLabel(s.id, s.kind),
      title: titles.titles?.[s.id]?.title ?? s.id,
      page: sel?.location?.page ?? null,
      order: [sel?.lines?.[0] ?? sel?.location?.lines?.[0] ?? Infinity, s.source_line ?? Infinity],
      // The edition's own record of the leading comparison's relation; verified to
      // agree with the comparison panel. Replaced below wherever the record is read.
      relation: s.evidence?.formal_statement ?? "unassessed",
      declaration: null,
    };
  });
  rows.sort((a, b) => a.order[0] - b.order[0] || a.order[1] - b.order[1]);
  const wanted = scope === "all" ? rows : rows.filter(isMajor);
  await Promise.all(wanted.map(async (row) => {
    const path = reading.fidelity?.[row.id];
    if (!path) return;
    const lead = leadComparison(await reader.resource(path));
    if (!lead) return;
    row.relation = lead.relation;
    row.declaration = lead.declaration;
  }));
  const counts = { exact: 0, stronger: 0, partial: 0 };
  for (const r of rows) if (r.relation in counts) counts[r.relation as Rel]++;
  return { rows, counts };
}

function useResults(edition: Edition, scope: "all" | "major") {
  return useAsync(() => loadResults(edition, scope), [edition, scope]);
}

const shortDecl = (name: string) => name.replace(/^QuarticQuery\./, "");

function ResultRow({ row, compact }: { row: Row; compact?: boolean }) {
  const to = href({ page: "read", paper: "original", s: "original/" + row.id, v: "statement", st: row.id });
  return (
    <li>
      <a className={compact ? "resultrow resultrow--compact" : "resultrow"} href={to}>
        <span className="resultrow__where">
          <span className="resultrow__kind">{row.label}</span>
          <span className="resultrow__page">{row.page != null ? `p. ${row.page}` : ""}</span>
        </span>
        <span className="resultrow__title"><Title text={row.title} /></span>
        <span className="resultrow__rel"><RelationMark relation={row.relation} /></span>
        <span className="resultrow__decl" title={row.declaration ?? undefined}>{row.declaration ? shortDecl(row.declaration) : ""}</span>
      </a>
    </li>
  );
}

function Proportion({ counts }: { counts: Record<Rel, number> }) {
  const label = RELATIONS.map((r) => `${RELATION_WORD[r]} ${counts[r]}`).join(", ");
  return (
    <div className="proportion">
      <div className="proportion__bar" role="img" aria-label={`Labels: ${label}`}>
        {RELATIONS.map((r) => counts[r] > 0 && <span key={r} className={`proportion__seg proportion__seg--${r}`} style={{ flexGrow: counts[r] }} />)}
      </div>
      <ul className="proportion__legend">
        {RELATIONS.map((r) => <li key={r}><RelationMark relation={r} /> <span className="proportion__n">{counts[r]}</span></li>)}
      </ul>
    </div>
  );
}

const KIND_FILTERS: { key: string; word: string; kinds: string[] | null }[] = [
  { key: "all", word: "All kinds", kinds: null },
  { key: "results", word: "Theorems and lemmas", kinds: ["theorem", "proposition", "lemma", "corollary"] },
  { key: "equations", word: "Equations", kinds: ["equation"] },
  { key: "definitions", word: "Definitions and constructions", kinds: ["definition", "construction"] },
  { key: "claims", word: "Claims in the text", kinds: ["inline_claim"] },
];
const LABEL_FILTERS: { key: string; word: string }[] = [
  { key: "all", word: "All" }, ...RELATIONS.map((r) => ({ key: r, word: RELATION_WORD[r] })),
];

function Failed({ quiet }: { quiet?: boolean }) {
  if (quiet) return <p className="quiet">The list of statements could not be loaded.</p>;
  return (
    <div className="failed" role="alert">
      <p>The list of statements could not be loaded from this edition.</p>
      <button type="button" className="tool" onClick={() => location.reload()}>Reload</button>
    </div>
  );
}

export function ResultsPage({ edition }: { edition: Edition }) {
  const data = useResults(edition, "all");
  return (
    <main id="main" className="results" tabIndex={-1}>
      <h1 className="results__title">OpenAI’s results and the Lean statements compared with them</h1>
      {data.state === "loading" && <p className="pending" role="status">Loading the statements…</p>}
      {data.state === "failed" && <Failed />}
      {data.state === "ready" && <ResultsBody results={data.value} />}
    </main>
  );
}

function ResultsBody({ results }: { results: Results }) {
  const { rows, counts } = results;
  const [label, setLabel] = useState("all");
  const [kind, setKind] = useState("all");
  const kindOf = (key: string) => KIND_FILTERS.find((k) => k.key === key)!.kinds;
  const matchKind = (r: Row, key: string) => { const ks = kindOf(key); return !ks || ks.includes(r.kind); };
  const matchLabel = (r: Row, key: string) => key === "all" || r.relation === key;
  const shown = useMemo(() => rows.filter((r) => matchKind(r, kind) && matchLabel(r, label)), [rows, kind, label]);
  return (
    <>
      <p className="results__lede">
        The {rows.length} statements of OpenAI’s paper that this project indexed, in the paper’s order. On each row is the
        Lean statement compared with it and the label from an AI review: an exact match, stronger in Lean, or a
        partial match. No expert has reviewed these labels yet.{" "}
        <a href={href({ page: "about" })}>How to read the evidence</a>
      </p>
      <Proportion counts={counts} />
      <div className="results__filters">
        <div className="filters" role="group" aria-label="Filter by label">
          {LABEL_FILTERS.map((f) => {
            const n = rows.filter((r) => matchKind(r, kind) && matchLabel(r, f.key)).length;
            return (
              <button key={f.key} type="button" className="filter" aria-pressed={label === f.key} disabled={n === 0 && label !== f.key} onClick={() => setLabel(f.key)}>
                {f.word} <span className="filter__n">{n}</span>
              </button>
            );
          })}
        </div>
        <div className="filters" role="group" aria-label="Filter by kind of statement">
          {KIND_FILTERS.map((f) => {
            const n = rows.filter((r) => matchKind(r, f.key) && matchLabel(r, label)).length;
            return (
              <button key={f.key} type="button" className="filter" aria-pressed={kind === f.key} disabled={n === 0 && kind !== f.key} onClick={() => setKind(f.key)}>
                {f.word} <span className="filter__n">{n}</span>
              </button>
            );
          })}
        </div>
      </div>
      <p className="sr-only" aria-live="polite">{shown.length} statements shown</p>
      <ol className="resultlist">
        {shown.map((r) => <ResultRow key={r.id} row={r} />)}
      </ol>
    </>
  );
}

export function ResultsBand({ edition }: { edition: Edition }) {
  const data = useResults(edition, "major");
  const ready = data.state === "ready" ? data.value : null;
  const n = ready?.rows.length;
  return (
    <section className={ready ? "resultsband" : "resultsband resultsband--pending"} aria-labelledby="resultsband-h" aria-busy={data.state === "loading"}>
      <div className="resultsband__prose">
        <h2 id="resultsband-h">Each of OpenAI’s results, with the Lean statement compared with it</h2>
        {data.state === "failed" && <Failed quiet />}
        {ready && (
          <>
            <p>
              This project indexes {n} statements of OpenAI’s paper. Each one is compared with a Lean statement and
              labelled an exact match, stronger in Lean, or a partial match. AI wrote the labels, and no expert has
              reviewed them yet.
            </p>
            <Proportion counts={ready.counts} />
            <p className="resultsband__more"><a href="#/results">All {n} statements</a></p>
          </>
        )}
      </div>
      {ready && (
        <ol className="resultlist resultlist--compact">
          {ready.rows.filter(isMajor).map((r) => <ResultRow key={r.id} row={r} compact />)}
        </ol>
      )}
    </section>
  );
}
