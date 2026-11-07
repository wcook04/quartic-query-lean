import { lazy, Suspense, useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { Edition } from "./edition";
import { excursion, go, href, switchPaper, type Route } from "./router";
import { isRestoringReadingPlace, useReadingPlace, useReturnToPaper } from "./restore";
import { PAPERS, SUPPLEMENT, face } from "./papers";
import { NavContext, type Nav } from "../inspect/Nav";
import { ReaderContext } from "../inspect/ReaderContext";
import { NamesContext, StatementNamesContext, type DeclarationTitles, type StatementTitles } from "../inspect/Names";
import { StatementLabel } from "../inspect/common";
import { PassagePanel } from "../inspect/PassagePanel";
import { StatementPanel } from "../inspect/StatementPanel";
import { LeanPanel } from "../inspect/LeanPanel";
import { JourneyPanel } from "../inspect/JourneyPanel";
import { PathPanel } from "../inspect/PathPanel";
import { ManuscriptPaper } from "../paper/ManuscriptPaper";
const PdfPaper = lazy(() => import("../paper/PdfPaper").then((m) => ({ default: m.PdfPaper })));
import { meaningful, type Row } from "../paper/selectRow";
const ProofPane = lazy(() => import("../map/ProofPane").then((m) => ({ default: m.ProofPane })));
import { Contents, sectionAt, type ContentsRow } from "../paper/Contents";

function useWide(): boolean {
  const q = "(min-width: 901px)";
  const [wide, setWide] = useState(() => window.matchMedia(q).matches);
  useEffect(() => {
    const m = window.matchMedia(q);
    const on = () => setWide(m.matches);
    m.addEventListener("change", on);
    return () => m.removeEventListener("change", on);
  }, []);
  return wide;
}

export function ReaderPage({ edition, route }: { edition: Edition; route: Route }) {
  const paper = route.paper!;
  const reader = edition.reader;
  useReadingPlace(paper, edition.permalink);
  const returnTo = useReturnToPaper();
  const [rows, setRows] = useState<Row[]>([]);
  const [downloads, setDownloads] = useState<Record<string, any>>({});
  const [original, setOriginal] = useState<any>(null);
  const [showPdf, setShowPdf] = useState(false);
  const [rootDeclaration, setRootDeclaration] = useState<string | undefined>();
  const aside = useRef<HTMLElement>(null);
  const wide = useWide();
  const [readingLine, setReadingLine] = useState<number | null>(null);
  const [readingPage, setReadingPage] = useState<number | null>(null);
  const [following, setFollowing] = useState(true);
  const [contents, setContents] = useState<ContentsRow[]>([]);
  const [lit, setLit] = useState<string[]>([]);
  const [names, setNames] = useState<{ reader: typeof reader; titles: DeclarationTitles } | null>(null);
  const [statementNames, setStatementNames] = useState<{ reader: typeof reader; index: StatementTitles } | null>(null);
  // Selections this reader has met in this edition and paper (this browser only).
  const visitKey = `quartic:visited:${edition.permalink}:${paper}`;
  const [visited, setVisited] = useState<string[]>(() => { try { return JSON.parse(localStorage.getItem(visitKey) ?? "[]"); } catch { return []; } });
  useEffect(() => { try { setVisited(JSON.parse(localStorage.getItem(visitKey) ?? "[]")); } catch { setVisited([]); } }, [visitKey]);
  const [progress, setProgress] = useState<{ total: number; visited: { count: number; cards: string[] }; cards: string[] } | null>(null);
  const ed = edition.pinnedOlder ? edition.permalink : undefined;
  const base: Route = { page: "read", paper, ed };

  useEffect(() => { reader.resource("reading.json").then((r: any) => { setDownloads(r.downloads ?? {}); setOriginal(r.papers?.original); }, () => {}); }, [reader]);
  useEffect(() => { reader.proofMap().then((m: any) => { if (m.currentness === "current") setRootDeclaration(m.root); }, () => {}); }, [reader]);
  const originalHtml = paper === "original" && !!original?.rendered && !showPdf;
  const lineSelection = rows.filter((r) => meaningful(r) && r.lines && readingLine != null && r.lines[0] <= readingLine && readingLine <= r.lines[1])
    .sort((a, b) => (a.topic ? 0 : 1) - (b.topic ? 0 : 1) || (a.lines![1] - a.lines![0]) - (b.lines![1] - b.lines![0]))[0]?.id;
  const currentSelection = following && (!route.v || route.v === "graph") ? lineSelection ?? route.s : route.s ?? lineSelection;

  const query = useMemo(() => {
    const doc = (reader.documents as any)[paper];
    if (currentSelection) {
      const m = /^l(\d+)-(\d+)$/.exec(currentSelection);
      return m ? { paper, line: Number(m[1]), endLine: Number(m[2]), documentSha256: doc?.sha256 } : { paper, id: currentSelection };
    }
    if (route.p) return { paper, page: route.p, documentSha256: doc?.sha256 };
    return null;
  }, [reader, paper, currentSelection, route.p]);

  const nav: Nav = useMemo(() => ({
    paper,
    openSelection: (p, id) => { setFollowing(false); const next: Route = { page: "read", paper: p, s: id, ed }; if (p === paper) go(next, !route.v); else excursion(next, face(paper).tab); },
    openPassage: (p, anchor) => { setFollowing(false); const next: Route = { page: "read", paper: p, a: anchor, ed }; if (p === paper) go(next); else excursion(next, face(paper).tab); },
    openStatement: (id) => go({ ...base, s: route.s, p: route.p, v: "statement", st: id }),
    openLean: (name) => go({ ...base, s: currentSelection, p: route.p, v: "lean", d: name }),
    openGraph: (name?: string) => go({ ...base, s: route.s, p: route.p, v: "graph", d: name ?? route.d }),
    openPath: (edge: string) => go({ ...base, s: route.s, p: route.p, v: "path", e: edge, d: edge.split("→")[0] }),
    openJourney: (id) => go({ ...base, s: route.s, p: route.p, v: "journey", j: id }),
    backToPassage: () => go({ ...base, s: currentSelection, p: route.p, v: "passage" }),
    showInPaper: (id: string) => { setFollowing(false); go({ ...base, s: id, v: route.v, st: route.st, d: route.d, j: route.j, e: route.e, step: route.step }, true); },
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }), [paper, route.s, route.p, route.v, route.st, route.d, route.j, route.e, route.step, ed, currentSelection]);

  // SK's passage lens makes the graph a compact default; the exact Lean is one tab away.
  const open = route.v !== "closed" && (wide || !!(route.s || route.p || route.v));
  // Evidence follows the reading line, as the graph does, until the reader pins a passage.
  const followed = useRef<string | undefined>(undefined);
  const mode: "graph" | "path" | "lean" | "evidence" =
    route.v === "graph" ? "graph" : route.v === "path" ? "path" : route.v === "lean" ? "lean" : route.v === "statement" || route.v === "journey" ? "evidence"
      : route.v === "passage" ? "evidence" : "graph";
  const activeLean = route.d ?? lit[0] ?? rootDeclaration;
  const [graphOpened, setGraphOpened] = useState(mode === "graph");
  useEffect(() => { if (mode === "graph") setGraphOpened(true); }, [mode]);

  // The graph and its paths already carry their titles. Fetch the full index
  // only when a panel may display arbitrary neighbours or statement targets.
  const needsTitles = open && (mode === "lean" || mode === "evidence");
  useEffect(() => {
    if (!needsTitles) return;
    let live = true;
    reader.declarationTitles().then((result: { titles: DeclarationTitles }) => {
      if (live) setNames({ reader, titles: result.titles });
    }, () => {});
    return () => { live = false; };
  }, [reader, needsTitles]);

  const needsStatementTitles = paper === "original" || needsTitles;
  useEffect(() => {
    if (!needsStatementTitles) return;
    let live = true;
    reader.statementTitles().then((index: StatementTitles) => {
      if (live) setStatementNames({ reader, index });
    }, () => live && setStatementNames({ reader, index: { status: "failed", titles: {} } }));
    return () => { live = false; };
  }, [reader, needsStatementTitles]);

  useEffect(() => {
    if (!following || mode === "graph" || route.a || isRestoringReadingPlace() || (route.v && route.v !== "passage") || (paper === "original" && !originalHtml) || readingLine == null) return;
    const hit = rows.filter((r) => meaningful(r) && r.lines && r.lines[0] <= readingLine && readingLine <= r.lines[1])
      .sort((x, y) => (x.topic ? 0 : 1) - (y.topic ? 0 : 1) || (x.lines![1] - x.lines![0]) - (y.lines![1] - y.lines![0]))[0];
    if (!hit || hit.id === route.s) return;
    followed.current = hit.id;
    go({ ...base, s: hit.id, v: route.v }, true);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [following, mode, readingLine, rows, paper, originalHtml]);

  useEffect(() => {
    if (!following || isRestoringReadingPlace() || mode !== "evidence" || route.v !== "passage" || paper !== "original" || readingPage == null || route.p === readingPage) return;
    if (route.s && rows.find((r) => r.id === route.s)?.location?.page === readingPage) return;
    go({ ...base, p: readingPage, v: "passage" }, true);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [following, mode, readingPage, paper]);

  // The cards lit in the graph: the selected passage's, else the reading line's.
  useEffect(() => {
    let live = true;
    const doc = (reader.documents as any)[paper];
    let q: any = null;
    const free = route.s && /^l(\d+)-\d+$/.exec(route.s);
    if (!following && route.s && !free) q = { paper, id: route.s };
    else if (mode === "graph" && readingLine && (paper !== "original" || originalHtml)) q = { paper, line: readingLine };
    else if (mode === "graph" && readingPage && paper === "original") q = { paper, page: readingPage };
    else if (route.s && !free) q = { paper, id: route.s };
    else if (free) q = { paper, line: Number(free[1]) };
    else if (route.p) q = { paper, page: route.p };
    else if (doc?.format === "pdf" && !originalHtml && readingPage) q = { paper, page: readingPage };
    else if (readingLine) q = { paper, line: readingLine };
    if (!q) { setLit([]); return; }
    (reader as any).proofFocus(q).then((f: any) => {
      if (!live) return;
      setLit(f.cards ?? []);
      const ids: string[] = (f.matches ?? []).map((m: any) => m.id);
      setVisited((old) => {
        const fresh = ids.filter((id) => !old.includes(id));
        if (!fresh.length) return old;
        const next = [...old, ...fresh];
        try { localStorage.setItem(visitKey, JSON.stringify(next)); } catch { /* storage unavailable */ }
        return next;
      });
    }, () => live && setLit([]));
    return () => { live = false; };
  }, [reader, paper, route.s, route.p, readingLine, readingPage, mode, originalHtml, following]);

  const close = useCallback(() => {
    // Closing keeps the selection: the paper stays marked where the reader was.
    go({ ...base, s: route.s, p: route.p, v: "closed" });
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
    if (!open || !route.v || isRestoringReadingPlace()) return;
    const t = window.setTimeout(() => {
      if (isRestoringReadingPlace()) return;
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

  // The tabs restore a document's own place; a passage link is a separate excursion.
  function switchTo(target: string, e: React.MouseEvent) {
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    e.preventDefault();
    switchPaper(target);
  }

  const availablePapers = PAPERS.filter(p => Object.hasOwn(reader.documents, p.id));
  if (!Object.hasOwn(reader.documents, paper))
    return (
      <main id="main" className="notice-page">
        <h1>“{paper.slice(0, 40)}” is unavailable in this edition.</h1>
        <p>Available papers include {availablePapers.map((p, i) => <span key={p.id}>{i ? ", " : ""}<a href={href({ page: "read", paper: p.id, ed })}>{p.tab}</a></span>)}.</p>
      </main>
    );

  const f = face(paper);
  const download = downloads[paper] ?? (paper === "original" && original?.resource ? original : undefined);
  const keyed = rows.filter((r) => r.topic && meaningful(r));

  useEffect(() => {
    let live = true;
    (reader as any).paperCardProgress({ paper, edition: edition.permalink, visited })
      .then((g: any) => live && setProgress(g.status === "current" ? g : null), () => live && setProgress(null));
    return () => { live = false; };
  }, [reader, paper, edition.permalink, visited]);

  const here = sectionAt(contents, route.s && /^l(\d+)/.exec(route.s) ? Number(/^l(\d+)/.exec(route.s)![1]) : readingLine);
  const goSection = (r: ContentsRow) => { setFollowing(true); go({ ...base, a: r.anchor, v: route.v }, true); };

  let panel = null;
  if (route.v === "statement" && route.st) panel = <StatementPanel edition={edition} id={route.st} />;
  else if (mode === "lean" && activeLean) panel = <LeanPanel key={activeLean} edition={edition} name={activeLean} />;
  else if (route.v === "path" && route.e) panel = <PathPanel edition={edition} edge={route.e} />;
  else if (mode === "graph") panel = null;
  else if (route.v === "journey" && route.j) panel = <JourneyPanel edition={edition} id={route.j} step={route.step} />;
  else if (query && route.v !== "closed") panel = <PassagePanel edition={edition} query={query} />;

  return (
    <ReaderContext.Provider value={reader}>
    <NamesContext.Provider value={names?.reader === reader ? names.titles : {}}>
    <StatementNamesContext.Provider value={statementNames?.reader === reader ? statementNames.index : { status: "loading", titles: {} }}>
    <NavContext.Provider value={nav}>
      <div className={`desk${open ? " desk--open" : ""}`}>
        <nav className="papers" aria-label="Papers">
          <ul>
            {availablePapers.map((p) => (
              <li key={p.id}>
                <a href={href({ page: "read", paper: p.id, ed })} aria-current={p.id === paper ? "page" : undefined} onClick={(e) => p.id !== paper && switchTo(p.id, e)}>
                  {p.tab}
                </a>
              </li>
            ))}
          </ul>
          {returnTo && <div className="papers__return"><button type="button" className="textbutton" onClick={returnTo.returnToOrigin}>Return to {returnTo.label}</button></div>}
        </nav>

        <main id="main" className={`paper${contents.length ? " paper--contents" : ""}`} tabIndex={-1} aria-label={f.name}>
          {contents.length > 0 && <Contents rows={contents} current={here} onGo={goSection} />}
          <header className="paper__head">
            <h1 className="paper__title">{f.name}</h1>
            <p className="paper__byline">{f.byline}</p>
            <div className="paper__tools">
              {(paper !== "original" || originalHtml) && <span className="legend"><span className="legend__bar" aria-hidden="true" />Select a marked paragraph to follow its proof and related explanations</span>}
              {download && <DownloadLink edition={edition} resource={download.resource} label="Download the PDF" name={`${paper}.pdf`} />}
              {paper === "original" && original?.rendered && <button type="button" className="textbutton" onClick={() => { setShowPdf(!showPdf); setContents([]); }}>{showPdf ? "Read the text edition" : "View the original PDF"}</button>}
              {keyed.length > 0 && (
                <details className="jump">
                  <summary>Linked passages</summary>
                  <ul>
                    {keyed.map((r) => (
                      <li key={r.id}><a href={href({ page: "read", paper, s: r.id, ed })} onClick={(e) => { (e.currentTarget.closest("details") as HTMLDetailsElement).open = false; }}>{r.topic!.replace(/-/g, " ")}</a></li>
                    ))}
                  </ul>
                </details>
              )}
              {contents.length > 0 && (
                <details className="jump jump--contents">
                  <summary>Contents</summary>
                  <ul>
                    {contents.filter((r) => r.level <= Math.min(...contents.map((x) => x.level)) + 1).map((r) => (
                      <li key={r.line}><a href={r.anchor ? `#${r.anchor}` : undefined} onClick={(e) => { e.preventDefault(); goSection(r); (e.currentTarget.closest("details") as HTMLDetailsElement).open = false; }}>{r.title}</a></li>
                    ))}
                  </ul>
                </details>
              )}
              {paper === "reconstruction" && <a href={href({ page: "read", paper: SUPPLEMENT.id, ed })}>Verification details</a>}
              {!wide && <button type="button" className="textbutton" onClick={() => nav.openGraph()}>Open the proof for this passage</button>}
            </div>
            {originalHtml && <p className="paper__edition">Reading edition rendered from OpenAI’s source. The original wording, numbering and authorship are retained; our passage links are an editorial layer.</p>}
          </header>
          {paper === "original" && !originalHtml ? (
            <Suspense fallback={<p className="pending" role="status">Loading the PDF viewer…</p>}>
              <PdfPaper edition={edition} selected={route.s} page={route.p}
                onSelect={(id) => { setFollowing(false); go({ ...base, s: id }, !route.v || route.v === "closed"); }}
                onPage={(n) => go({ ...base, p: n }, !route.v || route.v === "closed")}
                onReadingPage={setReadingPage} />
            </Suspense>
          ) : (
            <ManuscriptPaper key={paper} edition={edition} paper={paper} selected={route.s} anchor={route.a} page={route.p} onRows={setRows}
              onReadingLine={setReadingLine} onContents={setContents} followed={followed.current}
              onSelect={(id) => { setFollowing(false); go({ ...base, s: id }, !route.v || route.v === "closed"); }}
              onLink={nav.openPassage} />
          )}
        </main>

        {!open && wide && (
          <button type="button" className="reopen" onClick={() => nav.openGraph()}>
            <span>Open proof</span>
          </button>
        )}
        {open && (
          <aside ref={aside} className={`inspector inspector--${mode}`} aria-label="The Lean proof and its evidence">
            <div className="inspector__modes" role="group" aria-label="What to show beside the paper">
              <button type="button" aria-pressed={mode === "graph" || mode === "path"} onClick={() => nav.openGraph()}>Graph</button>
              <button type="button" aria-pressed={mode === "lean"} disabled={!activeLean} onClick={() => activeLean && nav.openLean(activeLean)}>Lean</button>
              <button type="button" aria-pressed={mode === "evidence"} disabled={!currentSelection && !route.p} onClick={nav.backToPassage}>Passage</button>
              <button type="button" className="inspector__close" onClick={close} aria-label="Close the proof pane">
                <span className="wide-only">Close</span><span className="narrow-only">Paper</span>
              </button>
            </div>
            <div className="inspector__bar">
              {route.v && route.v !== "graph" && route.v !== "path" && (route.s || route.p) && !(route.v === "statement" && route.s === `original/${route.st}`) && (
                <button type="button" className="textbutton" onClick={nav.backToPassage}>
                  Return to {route.s?.startsWith("original/") ? <StatementLabel id={route.s.slice(9)} /> : "the passage"}
                </button>
              )}
              {route.v && <button type="button" className="textbutton" onClick={() => history.back()}>Back</button>}
            </div>
            {(graphOpened || mode === "graph") && (
              <div className="inspector__graph" hidden={mode !== "graph"}>
                <Suspense fallback={<p className="pending" role="status">Loading the Lean graph…</p>}>
                  <ProofPane edition={edition} lit={lit} selected={route.d ?? null} onSelect={nav.openLean} selectedEdge={route.e ?? null} onEdge={nav.openPath}
                    progress={progress} paperName={face(paper).tab} selectionKey={following ? undefined : route.s} onFollow={() => setFollowing(true)} />
                </Suspense>
                <p className="inspector__note">
                  The highlighted steps appear with their inputs and uses. Dotted links from the main result give context; other lines are recorded dependencies. Choose a card for its Lean, or a dependency for its helpers.
                </p>
              </div>
            )}
            {mode !== "graph" && (
              <div className="inspector__body">
                {(mode === "lean" || mode === "evidence") && (!route.v || route.v === "passage") && (
                  <p className={`follow${following ? "" : " follow--pinned"}`} role="status">
                    {following ? <>Following the paper as you read. <span className="quiet">Select a paragraph to keep it here.</span></>
                      : <>Pinned to this passage. <button type="button" className="textbutton" onClick={() => setFollowing(true)}>Follow the paper again</button></>}
                  </p>
                )}
                {mode === "lean" && !route.d && !lit.length && <p className="quiet inspector__context">The main result is shown here. No declaration is linked to the current paragraph.</p>}
                {mode === "lean" && route.v === "lean" && <p className="follow follow--pinned">Keeping this declaration open. <button type="button" className="textbutton" onClick={() => { setFollowing(true); go({ ...base, s: lineSelection }); }}>Follow the paper again</button></p>}
                {panel ?? <p className="quiet">Scroll to a linked passage, or click one, to see its evidence.</p>}
              </div>
            )}
          </aside>
        )}
      </div>
    </NavContext.Provider>
    </StatementNamesContext.Provider>
    </NamesContext.Provider>
    </ReaderContext.Provider>
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
