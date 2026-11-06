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
      out[p] = await Promise.all(kept.map(async ({ r, row }) => {
        if (p === "original") {
          const sid = row.statements?.[0] ?? r.id.replace(/^original\//, "");
          return { id: r.id, where: `${await statementLabel(reader, sid)}, page ${row.location?.page ?? "?"}` };
        }
        const line = row.lines?.[0];
        let sec: any = null;
        for (const c of contents) if (line != null && c.line <= line && (c.end_line == null || line <= c.end_line) && (!sec || c.level >= sec.level)) sec = c;
        const title = (sec?.title ?? "").replace(/\s*\{[^}]*\}\s*$/, "");
        const quote = row.quote ? cleanQuote(row.quote) : "";
        const where = readable(title);
        return { id: r.id, where: /^(thm|lem|prop|cor|def|eq|claim)-/.test(where) ? await statementLabel(reader, where) : where || (line ? `Line ${line}` : "Passage"), quote: isPhrase(quote) ? quote : undefined };
      }));
      // One card per section of a paper: the first (most specific) passage stands for it.
      const bySection = new Set<string>();
      out[p] = out[p].filter((pl) => !bySection.has(pl.where) && bySection.add(pl.where));
    }
    return out;
  }, [reader, key, nav.paper]);
}

/** A statement's readable name: numbered results by number; a claim by its own opening words. */
const labelCache = new Map<string, Promise<string>>();
export function statementLabel(reader: any, id: string): Promise<string> {
  if (!/^claim-/.test(id)) return Promise.resolve(statementName(id));
  if (!labelCache.has(id)) {
    labelCache.set(id, reader.resource(`fidelity/${id}.json`).then((f: any) => {
      // Prefer a typeset title when the edition has one; ASCII pseudo-maths is never shown raw.
      if (f.title) return f.title;
      const text = String(f.statement ?? "").replace(/\s+/g, " ").trim();
      if (!text || /[_{}^]|\\[a-z]|\b(sum|sqrt)_?\b/.test(text)) return "An unnumbered claim";
      const words = text.split(" ");
      return `“${words.slice(0, 9).join(" ")}${words.length > 9 ? "…" : ""}”`;
    }, () => statementName(id)));
  }
  return labelCache.get(id)!;
}

const span = (r: any) => (r.lines ? r.lines[1] - r.lines[0] : 0);
const overlaps = (a: any, b: any) => !!a.lines && !!b.lines && a.lines[0] <= b.lines[1] && b.lines[0] <= a.lines[1];
/** A quote selector as words: drop Markdown emphasis and table bars. */
/** Markdown emphasis and table bars removed outside maths; maths (with its |x|) kept intact. */
const cleanQuote = (q: string) => q.split(/(\$[^$]*\$)/).map((part, i) => (i % 2 ? part
  : part.replace(/\*\*|__/g, "").replace(/^\s*\|\s*|\s*\|\s*$/g, "").replace(/\s+\|\s+/g, " · "))).join("").trim();
/** A quote is shown only when it is a real phrase, not a short matching key. */
const isPhrase = (q: string) => q.replace(/\$[^$]*\$/g, "x").split(/\s+/).filter(Boolean).length >= 6;
/** Section titles that are bare statement IDs read as statement names. */
const readable = (t: string) => {
  const m = /^\W*((?:thm|lem|prop|cor|def|eq|claim)-[\w.-]+?)\W*$/.exec(t);
  return m ? m[1] : t;
};

const ORDER = ["original", "exposition", "expert", "reconstruction", "verification"];

const MAIN = ["original", "exposition", "expert", "reconstruction"];

/** Where the papers discuss this: one compact column per paper, always in the same order.
 *  The paper being read is marked; a place in it scrolls the paper without leaving the
 *  view. The verification details are a single link beneath. */
export function Elsewhere({ rows, here, current }: { rows: Place[]; here: string; current?: string }) {
  const nav = useNav();
  const seen = new Set<string>();
  const unique = rows.filter((r) => ORDER.includes(r.paper) && !seen.has(r.paper + r.id) && seen.add(r.paper + r.id));
  const places = usePlaces(unique);
  const mine = current ?? here;
  if (!unique.length) return <p className="quiet">No paper has a linked passage on this.</p>;
  if (places.state !== "ready") return <p className="quiet">Finding the passages…</p>;
  const supplement = places.value.verification?.[0];
  return (
    <>
      <div className="strip">
        {MAIN.map((paper) => {
          const list = places.value[paper] ?? [];
          const isHere = paper === mine;
          return (
            <div key={paper} className={`strip__col strip__col--${paper}${isHere ? " is-here" : ""}${list.length ? "" : " is-empty"}`}>
              <p className="strip__paper">{face(paper).tab}{isHere && <span className="strip__here"> · you are here</span>}</p>
              {list.length === 0 && <p className="strip__none">Not discussed</p>}
              {list.slice(0, 3).map((pl, k) => (
                <button key={pl.id} type="button" className="strip__go"
                  onClick={() => (isHere && current ? nav.showInPaper(pl.id) : isHere ? nav.showInPaper(pl.id) : nav.openSelection(paper, pl.id))}>
                  <span className="strip__where">{pl.where}</span>
                  {k === 0 && pl.quote && <span className="strip__quote">“<Title text={pl.quote} />…”</span>}
                </button>
              ))}
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
