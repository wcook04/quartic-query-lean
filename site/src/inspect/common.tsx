import type { ReactNode } from "react";
import type { Async } from "../app/useAsync";
import { face, statementName } from "../app/papers";
import { useAsync } from "../app/useAsync";
import { useReader } from "./ReaderContext";
import { declarationTitle, useNames } from "./Names";
import { Title } from "../text/title";
import { useNav } from "./Nav";

export function Loaded<T>({ value, children, what }: { value: Async<T>; children: (v: T) => ReactNode; what: string }) {
  if (value.state === "loading") return <p className="pending" role="status">Loading {what}…</p>;
  if (value.state === "failed")
    return (
      <div className="failed" role="alert">
        <p>The {what} could not be loaded: {value.error.message}</p>
        <p>The paper stays open on the left. Try again, or return to the passage.</p>
        <button type="button" className="textbutton" onClick={() => location.reload()}>Reload this page</button>
      </div>
    );
  return <>{children(value.value)}</>;
}

export function shortName(name: string): string {
  return name.replace(/^QuarticQuery\./, "").replace(/^QuarticCorpus\./, "");
}

export function DeclButton({ name, children }: { name: string; children?: ReactNode }) {
  const nav = useNav();
  const names = useNames();
  const title = declarationTitle(names, name);
  return (
    <button type="button" className="decl decl--plain" onClick={() => nav.openLean(name)} title={name} aria-label={children ? undefined : title.title_plain}>
      {children ?? <Title text={title.title} />}
    </button>
  );
}

export function DeclTitle({ name }: { name: string }) {
  const title = declarationTitle(useNames(), name);
  return <span title={name} aria-label={title.title_plain}><Title text={title.title} /></span>;
}


export interface Place { paper: string; id: string; treatment?: string; lines?: number[] }

/** Name each place the way a reader would find it: the section and its opening words,
 *  or for OpenAI's PDF the statement and its page. Overlapping selections of one
 *  passage collapse into the most specific one. */
function usePlaces(rows: Place[]) {
  const nav = useNav();
  const reader = useReader();
  const key = rows.map((r) => r.paper + r.id).join("|");
  return useAsync(async () => {
    const reading: any = await reader.resource("reading.json");
    const papers = [...new Set(rows.map((r) => r.paper))];
    const tables = Object.fromEntries(await Promise.all(papers.map(async (p) => [p, await reader.resource(`selection/${p}.json`).catch(() => [])])));
    const out: Record<string, { id: string; where: string; quote?: string }[]> = {};
    for (const p of papers) {
      const contents: any[] = reading.papers[p]?.contents ?? reading.papers[p]?.outline ?? [];
      const found = rows.filter((r) => r.paper === p).map((r) => ({ r, row: (tables[p] as any[]).find((x) => x.id === r.id) ?? r }));
      // Narrowest first, then drop any selection that contains one already kept.
      found.sort((a, b) => span(a.row) - span(b.row));
      const kept: typeof found = [];
      for (const f of found) if (!kept.some((k) => overlaps(k.row, f.row))) kept.push(f);
      kept.sort((a, b) => (a.row.lines?.[0] ?? a.row.location?.page ?? 0) - (b.row.lines?.[0] ?? b.row.location?.page ?? 0));
      out[p] = kept.map(({ r, row }) => {
        if (p === "original") return { id: r.id, where: `${statementName(row.statements?.[0] ?? r.id.replace(/^original\//, ""))}, page ${row.location?.page ?? "?"}` };
        const line = row.lines?.[0];
        let sec: any = null;
        for (const c of contents) if (line != null && c.line <= line && (c.end_line == null || line <= c.end_line) && (!sec || c.level >= sec.level)) sec = c;
        const title = (sec?.title ?? "").replace(/\s*\{[^}]*\}\s*$/, "");
        return { id: r.id, where: title || (line ? `Line ${line}` : "Passage"), quote: row.quote ? cleanQuote(row.quote) : undefined };
      });
    }
    return out;
  }, [reader, key, nav.paper]);
}

const span = (r: any) => (r.lines ? r.lines[1] - r.lines[0] : 0);
const overlaps = (a: any, b: any) => !!a.lines && !!b.lines && a.lines[0] <= b.lines[1] && b.lines[0] <= a.lines[1];
/** A quote selector as words: drop Markdown emphasis and table bars. */
const cleanQuote = (q: string) => q.replace(/\*\*|__|`/g, "").replace(/^\|\s*|\s*\|$/g, "").replace(/\s*\|\s*/g, " · ").replace(/\$([^$]*)\$/g, "$1").trim();

const ORDER = ["original", "exposition", "expert", "reconstruction", "verification"];

/** Links to the same mathematics in the other papers, named by where they are. */
export function Elsewhere({ rows, here }: { rows: Place[]; here: string }) {
  const nav = useNav();
  const seen = new Set<string>();
  const unique = rows.filter((r) => r.paper !== here && ORDER.includes(r.paper) && !seen.has(r.paper + r.id) && seen.add(r.paper + r.id));
  const places = usePlaces(unique);
  if (!unique.length) return <p className="quiet">No other paper has a linked passage on this.</p>;
  if (places.state !== "ready") return <p className="quiet">Finding the passages…</p>;
  return (
    <ul className="elsewhere">
      {ORDER.filter((p) => places.value[p]?.length).map((paper) => (
        <li key={paper}>
          <span className="elsewhere__paper">{face(paper).tab}</span>
          <ul>
            {places.value[paper].map((pl) => (
              <li key={pl.id}>
                <button type="button" className="elsewhere__go" onClick={() => nav.openSelection(paper, pl.id)}>
                  <span className="elsewhere__where">{pl.where}</span>
                  {pl.quote && <span className="elsewhere__quote">“{pl.quote}…”</span>}
                </button>
              </li>
            ))}
          </ul>
        </li>
      ))}
    </ul>
  );
}
