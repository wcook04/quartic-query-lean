import { lazy, Suspense, useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { Edition } from "./edition";
import { go, href, type Route } from "./router";
import { PAPERS, SUPPLEMENT, face, statementName } from "./papers";
import { NavContext, type Nav } from "../inspect/Nav";
import { PassagePanel } from "../inspect/PassagePanel";
import { StatementPanel } from "../inspect/StatementPanel";
import { LeanPanel } from "../inspect/LeanPanel";
import { JourneyPanel } from "../inspect/JourneyPanel";
import { ManuscriptPaper } from "../paper/ManuscriptPaper";
const PdfPaper = lazy(() => import("../paper/PdfPaper").then((m) => ({ default: m.PdfPaper })));
import { meaningful, type Row } from "../paper/selectRow";

const KNOWN = [...PAPERS.map((p) => p.id), SUPPLEMENT.id];

export function ReaderPage({ edition, route }: { edition: Edition; route: Route }) {
  const paper = route.paper!;
  const reader = edition.reader;
  const [rows, setRows] = useState<Row[]>([]);
  const [downloads, setDownloads] = useState<Record<string, any>>({});
  const aside = useRef<HTMLElement>(null);
  const lastSelected = useRef<string | undefined>(route.s);
  const ed = edition.pinnedOlder ? edition.permalink : undefined;
  const base: Route = { page: "read", paper, ed };

  useEffect(() => { reader.resource("reading.json").then((r: any) => setDownloads(r.downloads ?? {}), () => {}); }, [reader]);
  if (route.s) lastSelected.current = route.s;

  const query = useMemo(() => {
    const doc = (reader.documents as any)[paper];
    if (route.s) {
      const m = /^l(\d+)-(\d+)$/.exec(route.s);
      return m ? { paper, line: Number(m[1]), endLine: Number(m[2]), documentSha256: doc?.sha256 } : { paper, id: route.s };
    }
    if (route.p) return { paper, page: route.p, documentSha256: doc?.sha256 };
    return null;
  }, [reader, paper, route.s, route.p]);

  const nav: Nav = useMemo(() => ({
    paper,
    openSelection: (p, id) => go({ page: "read", paper: p, s: id, ed }, p === paper && !route.v),
    openStatement: (id) => go({ ...base, s: route.s, p: route.p, v: "statement", st: id }),
    openLean: (name) => go({ ...base, s: route.s, p: route.p, v: "lean", d: name }),
    openJourney: (id) => go({ ...base, s: route.s, p: route.p, v: "journey", j: id }),
    backToPassage: () => go({ ...base, s: route.s, p: route.p }),
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }), [paper, route.s, route.p, route.v, ed]);

  const open = !!(route.s || route.p || route.v) && route.v !== "closed";

  const close = useCallback(() => {
    // Closing keeps the selection: the paper stays marked where the reader was.
    go({ ...base, s: route.s, p: route.p, v: route.s || route.p ? "closed" : undefined });
    requestAnimationFrame(() => {
      const block = document.querySelector<HTMLElement>(".paper .is-selected, .paper .pin.is-selected");
      const fallback = document.querySelector<HTMLElement>(".paper");
      (block ?? fallback)?.focus?.();
    });
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [paper, ed, route.s, route.p]);

  // Move focus to the new panel's heading; keep the selection in view.
  const panelKey = `${route.v}|${route.st}|${route.d}|${route.j}|${route.s}|${route.p}`;
  useEffect(() => {
    if (!open) return;
    const t = window.setTimeout(() => {
      const h = aside.current?.querySelector<HTMLElement>("h2");
      if (h) { h.tabIndex = -1; h.focus({ preventScroll: true }); }
      document.querySelector<HTMLElement>(".paper .is-selected")?.scrollIntoView({ block: "nearest" });
    }, 120);
    return () => clearTimeout(t);
  }, [panelKey, open]);

  useEffect(() => {
    const on = (e: KeyboardEvent) => { if (e.key === "Escape" && open) close(); };
    window.addEventListener("keydown", on);
    return () => window.removeEventListener("keydown", on);
  }, [open, close]);

  // Switching papers keeps the subject: open the matching treatment when one exists.
  async function switchTo(target: string, e: React.MouseEvent) {
    if (!query || e.metaKey || e.ctrlKey) return;
    e.preventDefault();
    try {
      const r: any = await reader.resolve(query as any);
      const candidates = [
        ...(r.relatedSelections ?? []).flatMap((x: any) => x.selections),
        ...(r.topics ?? []).flatMap((t: any) => t.treatments ?? []),
      ].filter((x: any) => x.paper === target);
      go({ page: "read", paper: target, s: candidates[0]?.id, ed });
    } catch {
      go({ page: "read", paper: target, ed });
    }
  }

  if (!KNOWN.includes(paper))
    return (
      <main id="main" className="notice-page">
        <h1>There is no paper called “{paper.slice(0, 40)}”.</h1>
        <p>Choose one of the four papers: {PAPERS.map((p, i) => <span key={p.id}>{i ? ", " : ""}<a href={href({ page: "read", paper: p.id })}>{p.tab}</a></span>)}.</p>
      </main>
    );

  const f = face(paper);
  const download = downloads[paper];
  const keyed = rows.filter((r) => r.topic && meaningful(r));

  let panel = null;
  if (route.v === "statement" && route.st) panel = <StatementPanel edition={edition} id={route.st} />;
  else if (route.v === "lean" && route.d) panel = <LeanPanel edition={edition} name={route.d} />;
  else if (route.v === "journey" && route.j) panel = <JourneyPanel edition={edition} id={route.j} step={route.step} />;
  else if (query && route.v !== "closed") panel = <PassagePanel edition={edition} query={query} />;

  return (
    <NavContext.Provider value={nav}>
      <div className={`desk${open ? " desk--open" : ""}`}>
        <nav className="papers" aria-label="Papers">
          <ul>
            {PAPERS.map((p) => (
              <li key={p.id}>
                <a href={href({ page: "read", paper: p.id, ed })} aria-current={p.id === paper ? "page" : undefined} onClick={(e) => p.id !== paper && switchTo(p.id, e)}>
                  {p.tab}
                </a>
              </li>
            ))}
          </ul>
        </nav>

        <main id="main" className="paper" tabIndex={-1} aria-label={f.name}>
          <header className="paper__head">
            <h1 className="paper__title">{f.name}</h1>
            <p className="paper__byline">{f.byline}</p>
            <div className="paper__tools">
              {download && <DownloadLink edition={edition} resource={download.resource} label="Download the PDF" name={`${paper}.pdf`} />}
              {keyed.length > 0 && (
                <details className="jump">
                  <summary>Linked passages</summary>
                  <ul>
                    {keyed.map((r) => (
                      <li key={r.id}><a href={href({ page: "read", paper, s: r.id, ed })}>{r.topic!.replace(/-/g, " ")}</a></li>
                    ))}
                  </ul>
                </details>
              )}
              {paper === "reconstruction" && <a href={href({ page: "read", paper: SUPPLEMENT.id, ed })}>Verification details</a>}
            </div>
          </header>
          {paper === "original" ? (
            <Suspense fallback={<p className="pending" role="status">Loading the PDF viewer…</p>}>
              <PdfPaper edition={edition} selected={route.s} page={route.p}
                onSelect={(id) => go({ ...base, s: id }, !route.v || route.v === "closed")}
                onPage={(n) => go({ ...base, p: n }, !route.v || route.v === "closed")} />
            </Suspense>
          ) : (
            <ManuscriptPaper key={paper} edition={edition} paper={paper} selected={route.s} anchor={route.a} onRows={setRows}
              onSelect={(id) => go({ ...base, s: id }, !route.v || route.v === "closed")}
              onLink={(p, fragment) => go({ page: "read", paper: p, a: fragment, ed })} />
          )}
        </main>

        {open && (
          <aside ref={aside} className="inspector" aria-label="Evidence for the selected passage">
            <div className="inspector__bar">
              <button type="button" className="inspector__close" onClick={close}>
                <span className="wide-only">Close</span><span className="narrow-only">Back to the paper</span>
              </button>
              {route.v && (route.s || route.p) && !(route.v === "statement" && route.s === `original/${route.st}`) && (
                <button type="button" className="textbutton" onClick={nav.backToPassage}>
                  Return to {route.s?.startsWith("original/") ? statementName(route.s.slice(9)) : "the passage"}
                </button>
              )}
              {route.v && <button type="button" className="textbutton" onClick={() => history.back()}>Back</button>}
            </div>
            <div className="inspector__body">{panel ?? <p className="quiet">Select a passage in the paper.</p>}</div>
          </aside>
        )}
      </div>
    </NavContext.Provider>
  );
}

function DownloadLink({ edition, resource, label, name }: { edition: Edition; resource: string; label: string; name: string }) {
  const [state, setState] = useState<"idle" | "busy" | "failed">("idle");
  async function get() {
    setState("busy");
    try {
      const bytes = await edition.reader.readBytes(resource);
      const url = URL.createObjectURL(new Blob([bytes], { type: "application/pdf" }));
      const a = document.createElement("a");
      a.href = url; a.download = name; a.click();
      setTimeout(() => URL.revokeObjectURL(url), 10000);
      setState("idle");
    } catch { setState("failed"); }
  }
  return (
    <button type="button" className="textbutton" onClick={get} disabled={state === "busy"}>
      {state === "failed" ? "The PDF is not in this edition" : state === "busy" ? "Preparing the PDF…" : label}
    </button>
  );
}
