import { lazy, Suspense, useCallback, useEffect, useMemo, useRef, useState, type CSSProperties } from "react";
import { SOURCE_READER, type Edition } from "./edition";
import { excursion, go, href, switchPaper, type Route } from "./router";
import { isInitialReaderEntry, isRestoringReadingPlace, useReadingPlace, useReturnToPaper } from "./restore";
import { PAPERS, SUPPLEMENT, face } from "./papers";
import { NavContext, type Nav } from "../inspect/Nav";
import { ReaderContext } from "../inspect/ReaderContext";
import { StatementLabel } from "../inspect/common";
import { declarationHeading, NamesContext, StatementNamesContext, type DeclarationTitles, type StatementTitles } from "../inspect/Names";
import { PassagePanel } from "../inspect/PassagePanel";
import { StatementPanel } from "../inspect/StatementPanel";
import { LeanPanel } from "../inspect/LeanPanel";
import { JourneyPanel } from "../inspect/JourneyPanel";
import { PathPanel } from "../inspect/PathPanel";
import { ManuscriptPaper } from "../paper/ManuscriptPaper";
const PdfPaper = lazy(() => import("../paper/PdfPaper").then((m) => ({ default: m.PdfPaper })));
import { meaningful, type Row } from "../paper/selectRow";
const ProofPane = lazy(() => import("../map/ProofPane").then((m) => ({ default: m.ProofPane })));
import { Contents, NumberedTitle, sectionAt, type ContentsRow } from "../paper/Contents";
import { BackIcon, Chevron, CloseIcon, PaneIcon } from "./icons";
import { ReaderSplit } from "./ReaderSplit";
import { Title } from "../text/title";
import { PhraseContext, lightPhrases, phraseLayer, topicGroups, topicTone, type PhraseLayer } from "../paper/phrases";
import { useTopicColours } from "../paper/topicColours";
import { PhraseList } from "../inspect/PhraseCards";
import { CardPreview, LeanSplit, PhraseDivider, PhraseSplit } from "../inspect/PhraseSplit";
import { SubjectGraph } from "../map/SubjectGraph";
import { plainTitle, titleHtml } from "../text/title";

type PassageMode = "graph" | "lean" | "passage";
/** A paragraph tied to more steps than this shows them in the graph one at a time. */
const MANY_STEPS = 2;

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

function fitPaperMenu(menu: HTMLDetailsElement) {
  const tools = menu.closest<HTMLElement>(".paper__tools");
  const paper = menu.closest<HTMLElement>(".paper");
  const list = menu.querySelector<HTMLElement>("ul");
  if (!menu.open || !menu.getClientRects().length || menu.closest("[inert]") || !tools || !paper || !list) return;
  const anchor = tools.getBoundingClientRect(), pane = paper.getBoundingClientRect();
  const below = Math.max(0, Math.min(pane.bottom, window.innerHeight) - anchor.bottom - 12);
  const above = Math.max(0, anchor.top - Math.max(pane.top, 0) - 12);
  const opensAbove = below < 120 && above > below;
  list.dataset.placement = opensAbove ? "above" : "below";
  list.style.maxHeight = `${Math.min(window.innerHeight / 2, opensAbove ? above : below)}px`;
}

export function ReaderPage({ edition, route }: { edition: Edition; route: Route }) {
  const paper = route.paper!;
  const reader = edition.reader;
  useReadingPlace(paper, edition.permalink);
  const returnTo = useReturnToPaper();
  const [rows, setRows] = useState<Row[]>([]);
  const [downloads, setDownloads] = useState<Record<string, any>>({});
  const [topicTitles, setTopicTitles] = useState<Record<string, string>>({});
  const [original, setOriginal] = useState<any>(null);
  const [showPdf, setShowPdf] = useState(false);
  const [rootDeclaration, setRootDeclaration] = useState<string | undefined>();
  const aside = useRef<HTMLElement>(null);
  const paperTools = useRef<HTMLDivElement>(null);
  const panelMove = useRef(0);
  const wide = useWide();
  const [readingLine, setReadingLine] = useState<number | null>(null);
  const [readingPage, setReadingPage] = useState<number | null>(null);
  const [following, setFollowing] = useState(() => !route.s || (!route.ed && isInitialReaderEntry()));
  const [contents, setContents] = useState<ContentsRow[]>([]);
  const [lit, setLit] = useState<string[]>([]);
  const [clickPin, setClickPin] = useState<string | null>(null);
  const [clickError, setClickError] = useState<string | null>(null);
  const clickSequence = useRef(0);
  // The first source line of the block a paragraph click landed on.
  const clickLine = useRef<number | undefined>(undefined);
  const clickPending = useRef<{ key: string } | null>(null);
  // What the pointer is over in the paper: a phrase's declarations, or a paragraph's lines.
  const [paperHover, setPaperHover] = useState<{ names?: string[]; lines?: [number, number] } | null>(null);
  // The card under the pointer in the graph, previewed in the dock.
  const [preview, setPreview] = useState<string | null>(null);
  const previewTimer = useRef(0);
  // The whole proof map, opened over the drawing from the Graph view.
  const [whole, setWhole] = useState(false);
  const [combineViews, setCombineViews] = useState(SOURCE_READER);
  const [fitHeight, setFitHeight] = useState<number | null>(null);
  // The proof map's own declarations, to say when a subject is not on it.
  const [mapCards, setMapCards] = useState<Record<string, any> | null>(null);
  // Which of a many-step paragraph's steps the graph shows, for the steps it was chosen among.
  const [stepAt, setStepAt] = useState<{ key: string; index: number }>({ key: "", index: 0 });
  // The last paragraph with Lean, kept in the drawing through paragraphs with none.
  const lastSteps = useRef<{ steps: string[]; title?: string } | null>(null);
  const [names, setNames] = useState<{ reader: typeof reader; titles: DeclarationTitles } | null>(null);
  const [phrases, setPhrases] = useState<PhraseLayer | null>(null);
  useTopicColours(phrases?.topics);
  useEffect(() => {
    let live = true;
    setPhrases(null);
    if (paper === "original" || paper === SUPPLEMENT.id) return;
    (reader as any).phrases?.(paper).then((data: any) => live && setPhrases(phraseLayer(data)), () => live && setPhrases(null));
    return () => { live = false; };
  }, [reader, paper]);
  const [statementNames, setStatementNames] = useState<{ reader: typeof reader; index: StatementTitles } | null>(null);
  const ed = edition.pinnedOlder ? edition.permalink : undefined;
  const base: Route = { page: "read", paper, ed };
  const routeNow = useRef(route);
  routeNow.current = route;
  // The tab the pane shows now. A click or the paper's reading line updates that tab; only
  // the reader's own choice of tab changes it.
  const openTab = (): PassageMode => {
    const v = routeNow.current.v;
    return v === "lean" ? "lean" : v === "passage" || v === "statement" || v === "journey" ? "passage" : "graph";
  };

  useEffect(() => { reader.resource("reading.json").then((r: any) => {
    setDownloads(r.downloads ?? {});
    setOriginal(r.papers?.original);
    setTopicTitles((titles) => ({ ...titles, ...Object.fromEntries((r.routes ?? []).map((topic: any) => [topic.id, topic.title])) }));
  }, () => {}); }, [reader]);
  useEffect(() => { reader.resource("selection/arguments.json").then((r: any) => {
    setTopicTitles((titles) => ({ ...titles, ...Object.fromEntries(Object.entries(r.topics ?? {}).map(([id, topic]: [string, any]) => [id, topic.title])) }));
  }, () => {}); }, [reader]);
  useEffect(() => { reader.proofMap().then((m: any) => { if (m.currentness === "current") { setRootDeclaration(m.root); setMapCards(m.cards); } }, () => {}); }, [reader]);
  // Adapt SimplifiedMap's dismissal: Escape belongs to the open menu before
  // the surrounding proof pane, and returns keyboard focus to its summary.
  useEffect(() => {
    const root = paperTools.current;
    if (!root) return;
    const opened = () => root.querySelector<HTMLDetailsElement>("details.jump[open]");
    const onResize = () => { const menu = opened(); if (menu) fitPaperMenu(menu); };
    const onDown = (event: PointerEvent) => {
      const menu = opened();
      if (menu && !menu.contains(event.target as Node)) menu.open = false;
    };
    const onFocus = (event: FocusEvent) => {
      const menu = opened();
      if (menu && !menu.contains(event.target as Node)) menu.open = false;
    };
    const onKey = (event: KeyboardEvent) => {
      const menu = opened();
      if (event.key !== "Escape" || event.defaultPrevented || !menu?.getClientRects().length || menu.closest("[inert]")) return;
      event.preventDefault();
      event.stopPropagation();
      menu.open = false;
      menu.querySelector<HTMLElement>("summary")?.focus({ preventScroll: true });
    };
    document.addEventListener("pointerdown", onDown);
    document.addEventListener("focusin", onFocus);
    window.addEventListener("keydown", onKey, true);
    window.addEventListener("resize", onResize);
    return () => {
      document.removeEventListener("pointerdown", onDown);
      document.removeEventListener("focusin", onFocus);
      window.removeEventListener("keydown", onKey, true);
      window.removeEventListener("resize", onResize);
    };
  }, [paper]);
  const originalHtml = paper === "original" && !!original?.rendered && !showPdf;
  const lineHit = useMemo(() => {
    if (readingLine == null) return undefined;
    let best: (typeof rows)[number] | undefined;
    let bestWidth = Infinity;
    for (const row of rows) {
      if (!row.lines || readingLine < row.lines[0] || readingLine > row.lines[1] || !meaningful(row)) continue;
      const width = row.lines[1] - row.lines[0];
      if (!best || (row.topic && !best.topic) || (!!row.topic === !!best.topic && width < bestWidth)) {
        best = row;
        bestWidth = width;
      }
    }
    return best;
  }, [rows, readingLine]);
  const lineSelection = lineHit?.id;
  const pinnedClaim = route.d ? rows.find((r) => r.id === route.s && r.claim_match?.name === route.d) : undefined;
  const currentSelection = pinnedClaim?.id ?? (following ? lineSelection ?? route.s : route.s ?? lineSelection);

  // A navigation inside the papers (a citation, a footnote, a contents entry) moves the
  // reading place, so a clicked paragraph gives way and the pane follows the paper again.
  const resumePaperFollowing = useCallback(() => {
    // A citation/footnote jump owns the paper immediately, even while the
    // previous panel's delayed focus/selection placement is still pending.
    window.clearTimeout(panelMove.current);
    if (!clickPin && !clickPending.current) return;
    clickSequence.current++;
    clickPending.current = null;
    setClickPin(null);
    setClickError(null);
    setFollowing(true);
    // A clicked paragraph's Lean was held on that paragraph; following moves it on.
    const r = routeNow.current;
    if (r.v === "lean" && r.d) go({ page: "read", paper, ed, s: r.s, v: "lean" }, true);
  }, [clickPin, paper, ed]);
  // Scrolling the paper keeps a clicked subject (docs/graph-pane.md); it only stops a pending
  // move of the pane's focus.
  const stopPanelMove = useCallback(() => window.clearTimeout(panelMove.current), []);

  async function selectPassage(id: string, line?: number) {
    clickLine.current = line;
    // A click changes the subject only. The tab stays the reader's choice, read when the
    // lookup lands, so a tab chosen while it was pending is kept.
    const key = `${paper}:${id}`;
    const pending = { key };
    clickPending.current = pending;
    const sequence = ++clickSequence.current;
    setFollowing(false);
    setClickError(null);
    try {
      let focus = await reader.proofFocus({ paper, id, line: undefined, page: undefined });
      // A whole section's selection can carry no steps of its own; the clicked block's lines then
      // give the steps, as following the paper to that block does.
      if (!focus.cards?.length && line != null && paper !== "original") focus = await (reader as any).proofFocus({ paper, line }).catch(() => focus);
      if (sequence !== clickSequence.current || clickPending.current !== pending) return;
      const cards: string[] = focus.cards ?? [];
      // Some passages reach their Lean only through their reviewed statement
      // (resolve().proof), with no graph card of their own. Lean must still
      // open that declaration rather than fall back to the main result.
      let lean = cards[0];
      if (!lean) {
        const resolved = await (reader as any).resolve({ paper, id }).catch(() => null);
        if (sequence !== clickSequence.current || clickPending.current !== pending) return;
        lean = resolved?.proof?.[0]?.name;
      }
      clickPending.current = null;
      const next = openTab();
      setClickPin(id);
      setLit(cards);
      // Clear a previous declaration/path: these views belong to this exact
      // passage and its freshly resolved Lean, not the old URL's selection.
      go({ ...base, s: id, v: next, d: next === "lean" ? lean : undefined });
    } catch (error) {
      if (sequence !== clickSequence.current) return;
      clickPending.current = null;
      setFollowing(true);
      setClickError(error instanceof Error ? error.message : String(error));
    }
  }

  // A chosen phrase whose declaration the map does not draw shows that declaration's Lean
  // neighbours, until the reader asks for the paragraph's own steps.
  const [paragraphStepsFor, setParagraphStepsFor] = useState<string | null>(null);
  // A phrase click changes the paragraph and declaration shown; the tab stays the reader's choice.
  function selectPhrase(id: string, selection: string) {
    const phrase = phrases?.byId.get(id);
    if (!phrase) return;
    const next = openTab();
    clickSequence.current++;
    clickPending.current = null;
    setFollowing(false);
    setClickError(null);
    if (!/^l\d+-\d+$/.test(selection)) setClickPin(selection);
    go({ ...base, s: selection, v: next, d: next === "passage" ? undefined : phrase.lean[0]?.name, ph: id });
  }

  // A card clicked in the graph or the whole map becomes the subject; the view stays.
  function selectCard(name: string) {
    clickSequence.current++;
    clickPending.current = null;
    setFollowing(false);
    setWhole(false);
    setPreview(null);
    const r = routeNow.current;
    go({ ...base, s: r.s ?? currentSelection, p: r.p, v: r.v === "lean" ? "lean" : "graph", d: name });
  }

  // Escape, a close button or "Follow the paper": the pane follows the reading line again.
  const followPaper = useCallback(() => {
    window.clearTimeout(panelMove.current);
    clickSequence.current++;
    clickPending.current = null;
    setClickPin(null);
    setClickError(null);
    setFollowing(true);
    setPreview(null);
    const r = routeNow.current;
    go({ ...base, s: lineSelection, v: r.v === "closed" ? undefined : r.v });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [paper, ed, lineSelection]);

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
    openSelection: (p, id) => { resumePaperFollowing(); setFollowing(false); const next: Route = { page: "read", paper: p, s: id, ed }; if (p === paper) go(next, !route.v); else excursion(next, face(paper).tab); },
    openPassage: (p, anchor) => { resumePaperFollowing(); setFollowing(false); const next: Route = { page: "read", paper: p, a: anchor, ed }; if (p === paper) go(next); else excursion(next, face(paper).tab); },
    openStatement: (id) => go({ ...base, s: route.s, p: route.p, v: "statement", st: id }),
    openLean: (name, phrase) => go({ ...base, s: currentSelection, p: route.p, v: "lean", d: name, ph: phrase }),
    // The three views share one subject: switching keeps the clicked card or phrase.
    openLeanTab: () => go({ ...base, s: currentSelection, p: route.p, v: "lean", d: route.d, ph: route.ph }),
    openGraph: (name?: string) => go({ ...base, s: route.s, p: route.p, v: "graph", d: name ?? route.d, ph: name ? undefined : route.ph }),
    openPath: (edge: string) => go({ ...base, s: route.s, p: route.p, v: "path", e: edge, d: edge.split("→")[0] }),
    openJourney: (id) => go({ ...base, s: route.s, p: route.p, v: "journey", j: id }),
    backToPassage: () => {
      if (pinnedClaim) setFollowing(false);
      go({ ...base, s: currentSelection, p: route.p, v: "passage", d: route.d, ph: route.ph });
    },
    showInPaper: (id: string) => { resumePaperFollowing(); setFollowing(false); go({ ...base, s: id, v: route.v, st: route.st, d: route.d, j: route.j, e: route.e, step: route.step }, true); },
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }), [paper, route.s, route.p, route.v, route.st, route.d, route.j, route.e, route.step, ed, currentSelection, pinnedClaim, resumePaperFollowing]);

  // SK's passage lens makes the graph a compact default; the exact Lean is one tab away.
  const open = route.v !== "closed" && (wide || !!(route.s || route.p || route.v));
  useEffect(() => {
    if (!open || wide || aside.current?.contains(document.activeElement)) return;
    aside.current?.querySelector<HTMLButtonElement>(".inspector__close")?.focus({ preventScroll: true });
  }, [open, wide]);
  // Evidence follows the reading line, as the graph does, until the reader pins a passage.
  const followed = useRef<string | undefined>(undefined);
  const followedPage = useRef<number | undefined>(undefined);
  const mode: "graph" | "path" | "lean" | "evidence" =
    route.v === "graph" ? "graph" : route.v === "path" ? "path" : route.v === "lean" ? "lean" : route.v === "statement" || route.v === "journey" ? "evidence"
      : route.v === "passage" ? "evidence" : "graph";
  useEffect(() => {
    if (!clickPin || route.s === clickPin) return;
    // Back/Forward or an independent navigation owns its saved selection.
    clickSequence.current++;
    clickPending.current = null;
    setClickPin(null);
    setFollowing(!route.s && !route.a);
  }, [route.s, route.a, clickPin]);
  // A passage whose Lean is reached through its reviewed statement has no
  // graph card; the Lean tab still opens that declaration.
  const [statementLean, setStatementLean] = useState<{ key: string; name?: string; failed?: boolean } | null>(null);
  const leanKey = currentSelection && !/^l\d+-\d+$/.test(currentSelection) && !lit.length ? currentSelection : null;
  useEffect(() => {
    if (!leanKey) return;
    let live = true;
    (reader as any).resolve({ paper, id: leanKey }).then((r: any) => live && setStatementLean({ key: leanKey, name: r?.proof?.[0]?.name }),
      () => live && setStatementLean({ key: leanKey, failed: true }));
    return () => { live = false; };
  }, [reader, paper, leanKey]);
  const passageLean = leanKey && statementLean?.key === leanKey ? statementLean.name : undefined;
  // The Lean answers the passage in hand. A passage with no linked declaration says so; the
  // main result stands in only where no linked paragraph is selected at all.
  const leanResolving = !!leanKey && statementLean?.key !== leanKey;
  const leanLookupFailed = !!leanKey && statementLean?.key === leanKey && !!statementLean.failed;
  const activeLean = route.d ?? lit[0] ?? passageLean ?? (currentSelection ? undefined : rootDeclaration);
  const claimMatch = rows.find((r) => r.id === currentSelection)?.claim_match;
  const [graphOpened, setGraphOpened] = useState(mode === "graph");
  useEffect(() => { if (mode === "graph") setGraphOpened(true); }, [mode]);

  // The graph and its paths already carry their titles. Fetch the full index
  // only when a panel may display arbitrary neighbours or statement targets.
  const needsTitles = open && (mode === "lean" || mode === "evidence" || mode === "graph");
  useEffect(() => {
    if (!needsTitles) return;
    let live = true;
    reader.declarationTitles().then((result: { titles: DeclarationTitles }) => {
      if (live) setNames({ reader, titles: result.titles });
    }, () => {});
    return () => { live = false; };
  }, [reader, needsTitles]);

  // The graph's card summary names paper statements too, so the titles load with every paper.
  const needsStatementTitles = true;
  useEffect(() => {
    if (!needsStatementTitles) return;
    let live = true;
    reader.statementTitles().then((index: StatementTitles) => {
      if (live) setStatementNames({ reader, index });
    }, () => live && setStatementNames({ reader, index: { status: "failed", titles: {} } }));
    return () => { live = false; };
  }, [reader, needsStatementTitles]);

  useEffect(() => {
    if (!following || mode === "graph" || route.a || isRestoringReadingPlace() || (route.v && route.v !== "passage" && !(route.v === "lean" && !route.d)) || (paper === "original" && !originalHtml) || readingLine == null) return;
    const hit = lineHit;
    if (!hit || hit.id === route.s) return;
    followed.current = hit.id;
    go({ ...base, s: hit.id, v: route.v }, true);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [following, mode, readingLine, rows, paper, originalHtml, route.d]);

  useEffect(() => {
    if (!following || isRestoringReadingPlace() || mode !== "evidence" || route.v !== "passage" || paper !== "original" || readingPage == null || route.p === readingPage) return;
    if (route.s && rows.find((r) => r.id === route.s)?.location?.page === readingPage) return;
    followedPage.current = readingPage;
    go({ ...base, p: readingPage, v: "passage" }, true);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [following, mode, readingPage, paper]);

  // The cards lit in the graph: the selected passage's, else the reading line's.
  useEffect(() => {
    if (clickPending.current) return;
    let live = true;
    const sequence = clickSequence.current;
    const doc = (reader.documents as any)[paper];
    let q: any = null;
    const free = route.s && /^l(\d+)-\d+$/.exec(route.s);
    if (clickPin) q = { paper, id: clickPin };
    else if (pinnedClaim) q = { paper, id: pinnedClaim.id };
    else if (!following && route.s && !free) q = { paper, id: route.s };
    else if (following && readingLine && paper !== "original") q = { paper, line: readingLine };
    else if (following && originalHtml && lineSelection) q = { paper, id: lineSelection };
    else if (following && readingPage && paper === "original" && !originalHtml) q = { paper, page: readingPage };
    else if (route.s && !free) q = { paper, id: route.s };
    else if (free) q = { paper, line: Number(free[1]) };
    else if (route.p) q = { paper, page: route.p };
    else if (doc?.format === "pdf" && !originalHtml && readingPage) q = { paper, page: readingPage };
    else if (readingLine) q = { paper, line: readingLine };
    if (!q) { setLit([]); return; }
    const line = clickPin ? clickLine.current : undefined;
    (reader as any).proofFocus(q).then((f: any) => (!f.cards?.length && line != null ? (reader as any).proofFocus({ paper, line }).catch(() => f) : f)).then((f: any) => {
      if (!live || sequence !== clickSequence.current || clickPending.current) return;
      setLit(f.cards ?? []);
    }, () => { if (live && sequence === clickSequence.current && !clickPending.current) setLit([]); });
    return () => { live = false; };
  }, [reader, paper, route.s, route.p, readingLine, readingPage, mode, originalHtml, following, clickPin, pinnedClaim, lineSelection]);

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
    // Following the paper updates the pane's content only: no focus, no paper movement.
    if (following && !clickPin && ((route.s && route.s === followed.current) || (!route.s && route.p != null && route.p === followedPage.current))) return;
    panelMove.current = window.setTimeout(() => {
      if (isRestoringReadingPlace()) return;
      const h = aside.current?.querySelector<HTMLElement>("h2");
      if (h) { h.tabIndex = -1; h.focus({ preventScroll: true }); }
      document.querySelector<HTMLElement>(".paper .is-selected")?.scrollIntoView({ block: "nearest" });
    }, 120);
    // Reuse the manuscript navigation guard: after another deliberate input,
    // delayed panel work must not pull the paper back or steal keyboard focus.
    const stop = () => window.clearTimeout(panelMove.current);
    const input = ["wheel", "touchstart", "pointerdown", "keydown"] as const;
    input.forEach((type) => window.addEventListener(type, stop, { capture: true, passive: true }));
    return () => { stop(); input.forEach((type) => window.removeEventListener(type, stop, true)); };
  }, [panelKey, open]);

  // Escape returns a held pane to following the paper; when it already follows, it closes the pane.
  const held = !!clickPin || !!route.d || !!route.ph || !following;
  useEffect(() => {
    const on = (e: KeyboardEvent) => {
      if (e.key !== "Escape" || !open || e.defaultPrevented || document.querySelector(":popover-open")) return;
      e.preventDefault();
      if (held) followPaper(); else close();
    };
    window.addEventListener("keydown", on);
    return () => window.removeEventListener("keydown", on);
  }, [open, close, held, followPaper]);

  // The tabs restore a document's own place; a passage link is a separate excursion.
  function switchTo(target: string, e: React.MouseEvent) {
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    e.preventDefault();
    switchPaper(target);
  }

  const availablePapers = PAPERS.filter(p => Object.hasOwn(reader.documents, p.id));
  if (!Object.hasOwn(reader.documents, paper))
    return (
      <main id="main" className="notice-page" tabIndex={-1}>
        <h1>This edition has no paper called “{paper.slice(0, 40)}”</h1>
        <p>The link may name a paper from another edition, or its address may have been shortened. Choose one of the papers this edition holds.</p>
        <ul className="notice-papers">
          {availablePapers.map((p) => (
            <li key={p.id}>
              <a href={href({ page: "read", paper: p.id, ed })}>
                <span className="notice-papers__tab">{p.tab}</span>
                <span className="notice-papers__name">{p.name}</span>
              </a>
            </li>
          ))}
        </ul>
        <p><a href={href({ page: "home" })}>Go to the front page</a></p>
      </main>
    );

  const f = face(paper);
  const download = downloads[paper] ?? (paper === "original" && original?.resource ? original : undefined);
  const keyed = rows.filter((r) => r.topic && meaningful(r));

  const here = sectionAt(contents, route.s && /^l(\d+)/.exec(route.s) ? Number(/^l(\d+)/.exec(route.s)![1]) : readingLine);
  // The Graph view's subject (docs/graph-pane.md): a clicked phrase's declaration, else a clicked
  // card, else the clicked or followed paragraph's steps. A paragraph with no Lean keeps the last
  // paragraph's steps in the drawing, and the main result stands in before any paragraph.
  const chosenPhrase = route.ph ? phrases?.byId.get(route.ph) : undefined;
  const phraseDeclaration = chosenPhrase?.lean.length ? (chosenPhrase.lean.some((r) => r.name === route.d) ? route.d! : chosenPhrase.lean[0].name) : undefined;
  const phraseHeld = !!phraseDeclaration && paragraphStepsFor === `${route.ph}|${phraseDeclaration}`;
  const paragraphSteps = lit.length ? lit : passageLean ? [passageLean] : [];
  const paragraphTitle = (() => {
    const row = rows.find((r) => r.id === currentSelection && r.topic);
    return row ? row.claim_match?.title ?? topicTitles[row.topic!] : here?.title;
  })();
  if (paragraphSteps.length) lastSteps.current = { steps: paragraphSteps, title: paragraphTitle };
  const pickedCard = route.d && !route.ph ? route.d : undefined;
  const offMap = (name: string) => !!mapCards && !Object.hasOwn(mapCards, name);
  let subjects: string[] = [];
  let graphLabel: React.ReactNode = null;
  let stepper: React.ReactNode = null;
  const toParagraph = () => {
    if (phraseDeclaration) setParagraphStepsFor(`${route.ph}|${phraseDeclaration}`);
    else go({ ...base, s: route.s, p: route.p, v: "graph" });
  };
  if (phraseDeclaration && !phraseHeld) {
    subjects = [phraseDeclaration];
    if (offMap(phraseDeclaration)) graphLabel = <>The Lean around this phrase’s declaration, which the proof map does not draw. <button type="button" onClick={toParagraph}>Show this paragraph’s steps</button></>;
  } else if (pickedCard) {
    subjects = [pickedCard];
    if (offMap(pickedCard)) graphLabel = <>The Lean around this declaration, which the proof map does not draw. <button type="button" onClick={toParagraph}>Show this paragraph’s steps</button></>;
  } else if (paragraphSteps.length || lastSteps.current) {
    const steps = paragraphSteps.length ? paragraphSteps : lastSteps.current!.steps;
    if (!paragraphSteps.length) graphLabel = <>No Lean is linked to this paragraph. The graph keeps the steps of {lastSteps.current!.title ? <>“<span dangerouslySetInnerHTML={{ __html: titleHtml(lastSteps.current!.title) }} />”</> : "the last linked paragraph"}.</>;
    if (steps.length > MANY_STEPS) {
      // A paragraph tied to many steps shows one at a time, its leading step first, so the drawing
      // keeps the room for their neighbourhoods; the others are a button away.
      const key = steps.join("|");
      const at = stepAt.key === key ? Math.min(stepAt.index, steps.length - 1) : 0;
      subjects = [steps[at]];
      const name = (id: string) => plainTitle(declarationHeading(id, mapCards?.[id] ?? names?.titles[id]).title);
      const move = (by: number) => setStepAt({ key, index: (at + by + steps.length) % steps.length });
      stepper = (
        <span className="graph-steps" role="group" aria-label="Steps linked to this paragraph">
          <button type="button" className="graph-acts__btn" onClick={() => move(-1)} aria-label={`Previous step: ${name(steps[(at - 1 + steps.length) % steps.length])}`}>‹</button>
          <span>Step {at + 1} of {steps.length}</span>
          <button type="button" className="graph-acts__btn" onClick={() => move(1)} aria-label={`Next step: ${name(steps[(at + 1) % steps.length])}`}>›</button>
        </span>
      );
    } else subjects = steps;
  } else if (rootDeclaration) {
    subjects = [rootDeclaration];
    graphLabel = <>No Lean is linked to this place in the paper. The graph shows the main result.</>;
  }
  const subjectLines: [number, number] | null = (() => {
    const r = rows.find((x) => x.id === currentSelection)?.lines;
    return r ? [r[0], r[1]] : readingLine != null ? [readingLine, readingLine] : null;
  })();
  const noLeanHere = !phraseDeclaration && !pickedCard && !paragraphSteps.length;
  // The paragraph itself, for the dock when no Lean is linked to it.
  const dockPassage = (() => {
    if (!noLeanHere || mode !== "graph") return null;
    const line = subjectLines?.[0];
    const block = line == null ? null : [...document.querySelectorAll<HTMLElement>(".manuscript .source-block[data-l0]")]
      .find((b) => Number(b.dataset.l0) <= line && line <= Number(b.dataset.l1));
    // The paragraph's own typeset HTML, already sanitised, without its margin marks.
    const copy = block?.cloneNode(true) as HTMLElement | undefined;
    copy?.querySelectorAll(".lean-tag, .lean-claim-link").forEach((e) => e.remove());
    return { title: here?.title, html: copy?.innerHTML };
  })();
  const onGraphHover = (name: string | null) => {
    window.clearTimeout(previewTimer.current);
    lightPhrases(phrases, name ? [name] : null);
    // Leaving a card keeps its preview a moment, so the pointer can reach the dock's button.
    if (name) setPreview(subjects.includes(name) ? null : name);
    else previewTimer.current = window.setTimeout(() => setPreview(null), 400);
  };
  const goSection = (r: ContentsRow) => { resumePaperFollowing(); setFollowing(true); go({ ...base, a: r.anchor, v: route.v }, true); };

  const selectionStatements = rows.find((row) => row.id === currentSelection)?.statements;
  const awaitingLinkedLean = SOURCE_READER && combineViews && !whole && noLeanHere && leanResolving;
  const inlineLean = SOURCE_READER && combineViews && !whole && !noLeanHere;
  const mapOnly = SOURCE_READER && (whole || (combineViews && noLeanHere && !awaitingLinkedLean));
  const graphDetail = preview && !inlineLean ? <CardPreview edition={edition} name={preview} title={phrases?.titles[preview]?.title ?? declarationHeading(preview, mapCards?.[preview] ?? names?.titles[preview]).title}
    kind={mapCards && Object.hasOwn(mapCards, preview) ? "On the proof map" : "Lean declaration outside the paper’s map"} onOpenLean={(n) => nav.openLean(n)} />
    : phraseDeclaration ? <PhraseSplit edition={edition} id={route.ph!} name={phraseDeclaration} onClose={followPaper}
      onPick={(name) => go({ ...base, s: route.s, p: route.p, v: "graph", d: name, ph: route.ph }, true)} onOpenLean={(n) => nav.openLean(n, route.ph)} />
    : <LeanSplit edition={edition} names={noLeanHere ? [] : subjects}
      heading={pickedCard ? "Selected Lean declaration" : noLeanHere ? "Selected passage" : "Lean linked to this passage"}
      passage={dockPassage} selectionStatements={SOURCE_READER ? selectionStatements ?? [] : undefined}
      onClose={held ? followPaper : undefined} onOpenLean={(n) => nav.openLean(n)} />;

  let panel = null;
  if (route.v === "statement" && route.st) panel = <StatementPanel edition={edition} id={route.st} />;
  else if (mode === "lean" && !activeLean && currentSelection) panel = (
    <article className="panel">
      {leanResolving ? <p className="pending" role="status">Finding the Lean linked to this paragraph…</p> : <>
        <p>{leanLookupFailed ? "The Lean linked to this paragraph could not be looked up." : "No Lean is linked to this paragraph."}</p>
        {rootDeclaration && <p><button type="button" className="textbutton" onClick={() => nav.openLean(rootDeclaration)}>Show the Lean of the main result</button></p>}
      </>}
    </article>
  );
  else if (mode === "lean" && activeLean) panel = <LeanPanel key={activeLean} edition={edition} name={activeLean} forStep={lit.includes(activeLean) || activeLean === passageLean} claimMatch={claimMatch} selectionStatements={SOURCE_READER ? selectionStatements ?? [] : undefined} phrase={route.d === activeLean ? route.ph : undefined} />;
  else if (route.v === "path" && route.e) panel = <PathPanel edition={edition} edge={route.e} />;
  else if (mode === "graph") panel = null;
  else if (route.v === "journey" && route.j) panel = <JourneyPanel edition={edition} id={route.j} step={route.step} />;
  else if (query && route.v !== "closed") panel = <PassagePanel edition={edition} query={query} />;

  return (
    <ReaderContext.Provider value={reader}>
    <NamesContext.Provider value={names?.reader === reader ? names.titles : {}}>
    <StatementNamesContext.Provider value={statementNames?.reader === reader ? statementNames.index : { status: "loading", titles: {} }}>
    <NavContext.Provider value={nav}>
    <PhraseContext.Provider value={phrases}>
      <div className={`desk${open ? " desk--open" : ""}${SOURCE_READER ? " desk--source" : ""}`} data-topic-count={phrases?.topics.length}>
        {!SOURCE_READER && <nav className="papers" aria-label="Papers" inert={open && !wide}>
          <div className="papers__bar">
            <ul>
              {availablePapers.map((p) => (
                <li key={p.id}><a href={href({ page: "read", paper: p.id, ed })} aria-current={p.id === paper ? "page" : undefined} onClick={(e) => p.id !== paper && switchTo(p.id, e)}>{p.tab}</a></li>
              ))}
              {paper === SUPPLEMENT.id && <li><a href={href({ page: "read", paper: SUPPLEMENT.id, ed })} aria-current={paper === SUPPLEMENT.id ? "page" : undefined}>{SUPPLEMENT.tab}</a></li>}
            </ul>
            <button type="button" className="papers__pane" aria-pressed={open} onClick={() => (open ? close() : nav.openGraph())}
              title={open ? "Hide the pane with the graph, Lean and passages" : "Open the pane with the graph, Lean and passages"}>
              <PaneIcon /><span>Lean and graph</span>
            </button>
          </div>
          {returnTo && <div className="papers__return"><button type="button" className="textbutton" onClick={returnTo.returnToOrigin}><BackIcon /> Return to {returnTo.label}</button></div>}
        </nav>}

        <main id="main" className={`paper${contents.length ? " paper--contents" : ""}`} tabIndex={-1} aria-label={f.name} inert={open && !wide}
          onWheelCapture={stopPanelMove} onTouchMoveCapture={stopPanelMove}
          onKeyDownCapture={(event) => { if (["PageDown", "PageUp", "ArrowDown", "ArrowUp", "Home", "End", " "].includes(event.key) && !(event.target as HTMLElement).closest("input,textarea,select,button,a")) stopPanelMove(); }}
          onPointerDownCapture={(event) => { const box = event.currentTarget.getBoundingClientRect(); if (event.clientX >= box.left + event.currentTarget.clientWidth) stopPanelMove(); }}>
          {contents.length > 0 && <Contents rows={contents} current={here} onGo={goSection} phrases={phrases} />}
          <header className="paper__head">
            <h1 className="paper__title">{f.name}</h1>
            {f.by && <p className="paper__by">{f.by}</p>}
            {!SOURCE_READER && <p className="paper__byline">{f.byline}</p>}
            <div className="paper__tools" ref={paperTools}>
              {SOURCE_READER && <button type="button" className="papers__pane" aria-pressed={open} onClick={() => open ? close() : nav.openGraph()}><PaneIcon />Lean and graph</button>}
              {keyed.length > 0 && (
                <details className="jump" name="paper-tools" onToggle={(event) => fitPaperMenu(event.currentTarget)}>
                  <summary>Linked passages <span className="jump__count">{keyed.length}</span><Chevron /></summary>
                  <ul>
                    {keyed.map((r) => (
                      <li key={r.id}><a href={href({ page: "read", paper, s: r.id, ed })} aria-current={r.id === route.s ? "true" : undefined} onClick={(e) => { (e.currentTarget.closest("details") as HTMLDetailsElement).open = false; }}><Title text={r.claim_match?.title ?? topicTitles[r.topic!] ?? r.topic!.replace(/-/g, " ")} /></a></li>
                    ))}
                  </ul>
                </details>
              )}
              {contents.length > 0 && (
                <details className="jump jump--contents" name="paper-tools" onToggle={(event) => fitPaperMenu(event.currentTarget)}>
                  <summary>Contents<Chevron /></summary>
                  <ul>
                    {contents.filter((r) => r.level <= Math.min(...contents.map((x) => x.level)) + 1).map((r) => (
                      <li key={r.line} className={r.level > Math.min(...contents.map((x) => x.level)) ? "jump__sub" : undefined}><a href={r.anchor ? `#${r.anchor}` : undefined} aria-current={here === r ? "location" : undefined} onClick={(e) => { e.preventDefault(); goSection(r); (e.currentTarget.closest("details") as HTMLDetailsElement).open = false; }}><NumberedTitle text={r.title} /></a></li>
                    ))}
                  </ul>
                </details>
              )}
              {phrases && (
                <details className="jump jump--topics" name="paper-tools" onToggle={(event) => fitPaperMenu(event.currentTarget)}>
                  <summary>Topic colours<Chevron /></summary>
                  <TopicKeyList layer={phrases} />
                </details>
              )}
              {paper === "original" && original?.rendered && (SOURCE_READER && !original.resource
                ? original.url && <a className="tool" href={original.url} target="_blank" rel="noopener noreferrer">Open the original PDF</a>
                : <button type="button" className="tool" onClick={() => { setShowPdf(!showPdf); setContents([]); }}>{showPdf ? "Read the text edition" : "View the original PDF"}</button>)}
              {download && <DownloadLink edition={edition} resource={download.resource} label="Download the PDF" name={`${paper}.pdf`} />}
              {paper === "reconstruction" && <a className="tool" href={href({ page: "read", paper: SUPPLEMENT.id, ed })}>Verification details</a>}
              {!SOURCE_READER && paper === "original" && <a className="tool" href={href({ page: "results" })}>All results with their Lean statements</a>}
            </div>
            {!SOURCE_READER && (paper !== "original" || originalHtml) && (
              <p className="legend"><span className="lean-tag" aria-hidden="true">Lean</span>
                {wide ? "Marked paragraphs are linked to Lean. Click one to show it in the open tab: graph, Lean or passage."
                  : "Marked paragraphs are linked to Lean. Tap one to see it in the open tab."}
              </p>
            )}
            {phrases && (
              <p className="legend legend--phrases"><span className="phrase-sample" data-tone="0" aria-hidden="true">phrase</span>
                {wide ? "The underline shows the topic colour. Click a phrase to show its Lean declaration in the open tab."
                  : "An underlined phrase states a Lean declaration; its colour names the topic. Tap it to show that declaration."}
              </p>
            )}
            {!SOURCE_READER && originalHtml && <p className="paper__edition">Reading edition rendered from OpenAI’s source. The original wording, numbering and authorship are retained; our passage links are an editorial layer.</p>}
          </header>
          {paper === "original" && !originalHtml ? (
            <Suspense fallback={<p className="pending" role="status">Loading the PDF viewer…</p>}>
              <PdfPaper edition={edition} selected={route.s} page={route.p}
                onSelect={selectPassage}
                onPage={(n) => go({ ...base, p: n }, !route.v || route.v === "closed")}
                onReadingPage={setReadingPage} />
            </Suspense>
          ) : (
            <ManuscriptPaper key={paper} edition={edition} paper={paper} selected={route.s} anchor={route.a} page={route.p} onRows={setRows}
              onReadingLine={setReadingLine} onContents={setContents} followed={followed.current}
              onSelect={selectPassage} phrases={phrases} pickedPhrase={route.ph} onPhrase={selectPhrase} onHover={setPaperHover}
              onLink={nav.openPassage} onNavigateWithin={resumePaperFollowing} />
          )}
          {SOURCE_READER && <details className="fold paper__credit">
            <summary>About this reading copy</summary>
            <p className="paper__edition">{f.byline}</p>
            {originalHtml && <p className="paper__edition">OpenAI’s original wording, numbering and authorship are retained. The Quartic project added the passage links to the reading copy.</p>}
          </details>}
        </main>

        {open && wide && <ReaderSplit />}
        {open && (
          <aside ref={aside} className={`inspector inspector--${mode}`} aria-label="The Lean proof and its evidence">
            {(() => {
              // What the pane is about, said once above its three tabs: the linked paragraph
              // that was clicked or is being read, by its title in the edition.
              const row = rows.find((r) => r.id === currentSelection && r.topic);
              const title = row?.claim_match?.title ?? (row ? topicTitles[row.topic!] : undefined);
              const chosen = route.ph && phrases?.byId.get(route.ph);
              if (chosen && route.s === currentSelection) {
                const name = chosen.lean.find((r) => r.name === route.d)?.name ?? chosen.lean[0]?.name;
                const label = name ? phrases!.titles[name]?.title : undefined;
                return (
                  <p className="inspector__about">
                    <span className="inspector__about-k">Selected phrase</span> {label ? <Title text={label} /> : null}
                  </p>
                );
              }
              const picked = route.d && !route.ph ? declarationHeading(route.d, mapCards?.[route.d] ?? names?.titles[route.d]).title : undefined;
              if (SOURCE_READER && !picked && !selectionStatements?.length && !title && !(lit.length && here)) return null;
              if (picked) return (
                <p className="inspector__about"><span className="inspector__about-k">Clicked card</span> <Title text={picked} /></p>
              );
              return (
                <p className="inspector__about">
                  {SOURCE_READER && selectionStatements?.[0]
                    ? <><span className="inspector__about-k">{clickPin || route.s === currentSelection || !following ? "Selected passage" : "Passage being read"}</span> <StatementLabel id={selectionStatements[0]} /></>
                    : title ? <><span className="inspector__about-k">{clickPin || !following || route.s === currentSelection ? "Selected paragraph" : "Paragraph being read"}</span> <Title text={title} /></>
                    : lit.length && here ? <><span className="inspector__about-k">Paragraph being read in</span> <Title text={here.title} /></>
                    : <span className="inspector__about-k">No linked paragraph at this place in the paper</span>}
                </p>
              );
            })()}
            <div className="inspector__modes" role="group" aria-label="What the pane contains">
              <button type="button" aria-pressed={mode === "graph" || mode === "path"} onClick={() => nav.openGraph()}>Graph</button>
              <button type="button" aria-pressed={mode === "lean"} disabled={!activeLean && !currentSelection} onClick={() => nav.openLeanTab!()}>Lean</button>
              <button type="button" aria-pressed={mode === "evidence"} disabled={!currentSelection && !route.p} onClick={nav.backToPassage} title="This step in each paper, and what the Lean proves">Passage</button>
              {mode === "graph" && (
                <span className="graph-acts">
                  <span className="sr-only" role="status">{phraseDeclaration && !phraseHeld ? "Held on the clicked phrase." : pickedCard ? "Held on the clicked card." : held ? "Held on the clicked paragraph." : "Following the paper."}</span>
                  {stepper}
                  {held && <button type="button" className="graph-acts__btn" onClick={followPaper} title="Follow the paper again (Esc)">Follow the paper</button>}
                  {!whole && !mapOnly && <button type="button" className="graph-acts__btn" onClick={() => setWhole(true)}>Whole proof map</button>}
                  {SOURCE_READER && !whole && !mapOnly && <button type="button" className="graph-acts__btn" onClick={() => setCombineViews(!combineViews)}>{combineViews ? "Minimise graph" : "Combine views"}</button>}
                </span>
              )}
              <button type="button" className="inspector__close" onClick={close} aria-label={wide ? "Close the Lean pane" : undefined} title={wide ? "Close (Esc)" : undefined}>
                {wide ? <CloseIcon /> : <><BackIcon /><span>Back to paper</span></>}
              </button>
            </div>
            {mode !== "graph" && (() => {
              // One quiet line: what the pane is doing, then at most two actions. The Passage
              // tab itself returns to the selected passage, so the bar does not repeat it.
              const leanFallback = mode === "lean" && !route.d && !currentSelection && activeLean === rootDeclaration;
              const pinnedLean = mode === "lean" && route.v === "lean" && !!route.d;
              const followingLean = mode === "lean" && route.v === "lean" && !route.d;
              const passageView = (mode === "lean" || mode === "evidence") && (!route.v || route.v === "passage");
              const status = leanFallback ? <>No linked paragraph at this place; showing the main result.</>
                : clickPin ? <>Held on the clicked paragraph.</>
                : pinnedLean ? <>Pinned to this declaration.</>
                : followingLean ? (following ? <>Following the paper.</> : <>Pinned to this passage.</>)
                : passageView ? (following ? <>Following the paper.</> : <>Pinned to this passage.</>)
                : null;
              const refollow = held ? followPaper : null;
              if (!status && !refollow && !route.v) return null;
              return (
                <div className="inspector__bar">
                  {status && <p className="inspector__status" role="status">{status}</p>}
                  <span className="inspector__actions">
                    {refollow && <button type="button" className="textbutton" onClick={refollow}>Follow the paper</button>}
                    {route.v && <button type="button" className="textbutton inspector__back" onClick={() => history.back()}><span aria-hidden="true">← </span>Back</button>}
                  </span>
                </div>
              );
            })()}
            {(graphOpened || mode === "graph") && (
              <div className={`inspector__graph${inlineLean ? " inspector__graph--combined" : ""}${mapOnly ? " inspector__graph--map-only" : ""}`}
                data-fit-graph={fitHeight == null ? undefined : ""}
                style={fitHeight == null ? undefined : { "--fit-graph-height": `${fitHeight}px` } as CSSProperties}
                hidden={mode !== "graph"}>
                {inlineLean && <div className="graph-dock">{graphDetail}</div>}
                <div className="inspector__map">
                  {awaitingLinkedLean ? <p className="pending" role="status">Finding the Lean linked to this passage…</p> : whole || mapOnly ? (
                    <Suspense fallback={<p className="pending" role="status">Loading the Lean graph…</p>}>
                      <ProofPane edition={edition} lit={paragraphSteps} onSelect={selectCard} onOpenLean={nav.openLean}
                        selectedEdge={route.e ?? null} onEdge={nav.openPath} onBack={whole || !mapOnly ? () => setWhole(false) : undefined} />
                    </Suspense>
                  ) : (
                    <SubjectGraph edition={edition} paper={paper} subjects={subjects} position={subjectLines} hover={paperHover}
                      held={preview} label={graphLabel} onSubject={selectCard} onHover={onGraphHover} combined={inlineLean} onFitHeight={SOURCE_READER ? setFitHeight : undefined} />
                  )}
                </div>
                {!inlineLean && !mapOnly && !awaitingLinkedLean && <>
                  <PhraseDivider />
                  <div className="graph-dock" onMouseEnter={() => window.clearTimeout(previewTimer.current)} onMouseLeave={() => preview && onGraphHover(null)}>{graphDetail}</div>
                </>}
              </div>
            )}
            {mode !== "graph" && (
              <div className="inspector__body">
                {clickError && <p className="failed" role="alert">This passage could not be opened: {clickError}</p>}
                {route.v === "passage" && phrases && <PhraseList lines={selectionLines(rows, currentSelection)} picked={route.ph} />}
                {panel ?? <p className="quiet">Scroll to a linked passage, or click one, to see its evidence.</p>}
              </div>
            )}
          </aside>
        )}
      </div>
    </PhraseContext.Provider>
    </NavContext.Provider>
    </StatementNamesContext.Provider>
    </NamesContext.Provider>
    </ReaderContext.Provider>
  );
}

/** The source lines of a selection: its row's, or those named by a free l<start>-<end> ID. */
function selectionLines(rows: Row[], id: string | undefined): [number, number] | null {
  if (!id) return null;
  const free = /^l(\d+)-(\d+)$/.exec(id);
  if (free) return [Number(free[1]), Number(free[2])];
  const lines = rows.find((r) => r.id === id)?.lines;
  return lines ? [lines[0], lines[1]] : null;
}

/** The topic key: one colour per topic, grouped under its family, each with its name and what it covers. */
export function TopicKeyList({ layer }: { layer: PhraseLayer }) {
  return (
    <ul className="topic-key">
      {topicGroups(layer).map(({ family, topics }, g) => (
        <li key={family?.id ?? g} className="topic-key__family">
          {family?.named && topics.length > 1 && <span className="topic-key__family-name">{family.name}</span>}
          <ul className="topic-key">
            {topics.map((t) => (
              <li key={t.id} title={t.description}>
                <span className="topic-swatch" data-tone={topicTone(layer, t.id)} aria-hidden="true" />
                <span className="topic-key__name">{t.name}</span>
                <span className="topic-key__n">{layer.phrases.filter((p) => p.topic === t.id).length} phrases</span>
              </li>
            ))}
          </ul>
        </li>
      ))}
    </ul>
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
    <button type="button" className="tool" onClick={get} disabled={state === "busy"}>
      {state === "failed" ? "The PDF is not in this edition" : state === "busy" ? "Preparing the PDF…" : label}
    </button>
  );
}
