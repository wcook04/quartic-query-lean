import type { ReactNode } from "react";
import type { Async } from "../app/useAsync";
import { face } from "../app/papers";
import { useAsync } from "../app/useAsync";
import { useReader } from "./ReaderContext";
import { declarationTitle, statementTitle, useNames, useStatementNames, type DeclarationTitle } from "./Names";
import { Title } from "../text/title";
import { useNav } from "./Nav";
import "./inspect.css";

export function Loaded<T>({ value, children, what }: { value: Async<T>; children: (v: T) => ReactNode; what: string }) {
  if (value.state === "loading")
    return (
      <div className="panel-state panel-state--loading" role="status">
        <p className="panel-state__line">Loading the {what}…</p>
        <div className="panel-state__skeleton" aria-hidden="true"><span /><span /><span /><span /></div>
      </div>
    );
  if (value.state === "failed")
    return (
      <div className="panel-state panel-state--failed" role="alert">
        <p className="panel-state__title">The {what} could not be loaded.</p>
        <p className="panel-state__detail"><code>{value.error.message}</code></p>
        <p>The paper stays open beside this pane. Reload to try again, or go back to the passage.</p>
        <button type="button" className="button button--small" onClick={() => location.reload()}>Reload this page</button>
      </div>
    );
  return <>{children(value.value)}</>;
}

/** Authored names of the walkthroughs, by edition ID. */
export const JOURNEY_NAMES: Record<string, string> = {
  "forrelation-family": "How one family gives both query bounds",
  "capped-predictor": "Why naming the true cell reveals the whole address",
  "gaussian-transport": "How the Gaussian identity enters two estimates",
  "weighted-tournament": "Why weighted comparisons halve the candidates",
  "sign-blind-decoder": "Why the decoder needs an exact domain test",
};
export const journeyName = (id: string) => JOURNEY_NAMES[id] ?? id.replace(/-/g, " ");

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

export function StatementLabel({ id, presentation }: { id: string; presentation?: DeclarationTitle | null }) {
  const index = useStatementNames();
  const title = statementTitle(presentation ? { status: "current", titles: { [id]: presentation } } : index, id);
  return <span aria-label={title.title_plain}><Title text={title.title} /></span>;
}


export interface Place { paper: string; id: string; treatment?: string; lines?: number[] }

/** Name each place the way a reader would find it: the section and its opening words,
 *  or for OpenAI's PDF the statement and its page. Overlapping selections of one
 *  passage collapse into the most specific one. */
function usePlaces(rows: Place[]) {
  const nav = useNav();
  const reader = useReader();
  const titles = useStatementNames();
  const key = rows.map((r) => r.paper + r.id).join("|");
  return useAsync(async () => {
    const reading: any = await reader.resource("reading.json");
    const papers = [...new Set(rows.map((r) => r.paper))];
    const tables = Object.fromEntries(await Promise.all(papers.map(async (p) => [p, await reader.resource(`selection/${p}.json`).catch(() => [])])));
    const out: Record<string, { id: string; where: string; wherePlain?: string; quote?: string }[]> = {};
    for (const p of papers) {
      const contents: any[] = reading.papers[p]?.contents ?? reading.papers[p]?.outline ?? [];
      const found = rows.filter((r) => r.paper === p).map((r) => ({ r, row: (tables[p] as any[]).find((x) => x.id === r.id) ?? r }));
      // Narrowest first, then drop any selection that contains one already kept.
      found.sort((a, b) => span(a.row) - span(b.row));
      const kept: typeof found = [];
      for (const f of found) if (!kept.some((k) => overlaps(k.row, f.row))) kept.push(f);
      kept.sort((a, b) => (a.row.lines?.[0] ?? a.row.location?.page ?? 0) - (b.row.lines?.[0] ?? b.row.location?.page ?? 0));
      out[p] = await Promise.all(kept.map(async ({ r, row }) => {
        if (p === "original") {
          const sid = row.statements?.[0] ?? r.id.replace(/^original\//, "");
          const title = statementTitle(titles, sid);
          const page = `, page ${row.location?.page ?? "?"}`;
          return { id: r.id, where: title.title + page, wherePlain: title.title_plain + page };
        }
        const line = row.lines?.[0];
        let sec: any = null;
        for (const c of contents) if (line != null && c.line <= line && (c.end_line == null || line <= c.end_line) && (!sec || c.level >= sec.level)) sec = c;
        const title = (sec?.title ?? "").replace(/\s*\{[^}]*\}\s*$/, "");
        const quote = row.quote ? cleanQuote(row.quote) : "";
        const where = readable(title);
        const statement = Object.hasOwn(titles.titles, where) || /^(thm|lem|prop|cor|def|eq|claim|rem|fact|ex|construct)-/.test(where)
          ? statementTitle(titles, where) : null;
        return { id: r.id, where: statement?.title ?? (where || (line ? `Line ${line}` : "Passage")), wherePlain: statement?.title_plain, quote: isPhrase(quote) ? quote : undefined };
      }));
      // Distinct passages in one section can answer different questions.
    }
    return out;
  }, [reader, key, nav.paper, titles]);
}

const span = (r: any) => (r.lines ? r.lines[1] - r.lines[0] : 0);
const overlaps = (a: any, b: any) => !!a.lines && !!b.lines && a.lines[0] <= b.lines[1] && b.lines[0] <= a.lines[1];
/** Markdown emphasis and table bars removed outside maths; maths (with its |x|) kept intact. */
const cleanQuote = (q: string) => q.split(/(\$[^$]*\$)/).map((part, i) => (i % 2 ? part
  : part.replace(/\*\*|__/g, "").replace(/(^|[^\w*])\*([^*\s][^*]*?)\*(?!\w)/g, "$1$2").replace(/(^|[^\w*])\*(?=\S)/g, "$1").replace(/^\s*\|\s*|\s*\|\s*$/g, "").replace(/\s+\|\s+/g, " · "))).join("").trim();
/** A quote is shown only when it is a real phrase, not a short matching key. */
const isPhrase = (q: string) => q.replace(/\$[^$]*\$/g, "x").split(/\s+/).filter(Boolean).length >= 6;
/** Section titles that are bare statement IDs read as statement names. */
const readable = (t: string) => {
  const m = /^\W*((?:thm|lem|prop|cor|def|eq|claim|rem|fact|ex|construct)-[\w.-]+?)\W*$/.exec(t);
  return m ? m[1] : t;
};

const ORDER = ["expert", "exposition", "reconstruction", "original", "verification"];

const MAIN = ["expert", "exposition", "reconstruction", "original"];

/** Where the papers discuss this: one row per paper, always in the same order.
 *  The paper being read is marked; a place in it scrolls the paper without leaving the
 *  view. The selected passage itself is listed in its own paper. The verification
 *  details are a single link beneath. */
export function Elsewhere({ rows, here, current, selected }: { rows: Place[]; here: string; current?: string; selected?: { paper: string; id: string } }) {
  const nav = useNav();
  const seen = new Set<string>();
  const all = selected && ORDER.includes(selected.paper) ? [...rows, { paper: selected.paper, id: selected.id }] : rows;
  const unique = all.filter((r) => ORDER.includes(r.paper) && !seen.has(r.paper + r.id) && seen.add(r.paper + r.id));
  const places = usePlaces(unique);
  const mine = current ?? here;
  if (!unique.length) return <p className="quiet">No paper has a linked passage on this.</p>;
  if (places.state !== "ready") return <p className="quiet" role="status">Finding the passages…</p>;
  const supplement = places.value.verification?.[0];
  const go = (paper: string, id: string) => (paper === mine ? nav.showInPaper(id) : nav.openSelection(paper, id));
  const Place = ({ paper, pl }: { paper: string; pl: { id: string; where: string; wherePlain?: string; quote?: string } }) => (
    <button type="button" className="strip__go" onClick={() => go(paper, pl.id)}>
      <span className="strip__where" aria-label={pl.wherePlain}><Title text={pl.where} /></span>
      {selected && pl.id === selected.id && <span className="strip__sel">Selected passage</span>}
      {pl.quote && <span className="strip__quote">“<Title text={pl.quote} />…”</span>}
    </button>
  );
  return (
    <>
      <div className="strip">
        {MAIN.map((paper) => {
          const list = places.value[paper] ?? [];
          const isHere = paper === mine;
          return (
            <div key={paper} className={`strip__row strip__row--${paper}${isHere ? " is-here" : ""}${list.length ? "" : " is-empty"}`}>
              <p className="strip__paper">{face(paper).tab}{isHere && <span className="strip__here">You are reading this</span>}</p>
              <div className="strip__places">
                {list.length === 0 && <p className="strip__none">No passage linked yet</p>}
                {list.slice(0, 3).map((pl) => <Place key={pl.id} paper={paper} pl={pl} />)}
                {list.length > 3 && (
                  <details className="strip__extra">
                    <summary>{list.length - 3} more {list.length - 3 === 1 ? "passage" : "passages"}</summary>
                    {list.slice(3).map((pl) => <Place key={pl.id} paper={paper} pl={pl} />)}
                  </details>
                )}
              </div>
            </div>
          );
        })}
      </div>
      {supplement && (
        <p className="strip__more quiet">
          Also catalogued in the <button type="button" className="textbutton" onClick={() => nav.openSelection("verification", supplement.id)}>verification details</button>.
        </p>
      )}
    </>
  );
}
