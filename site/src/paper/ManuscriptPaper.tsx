// One manuscript, from the edition's Pandoc HTML. Its blocks carry their
// source lines; a click selects the most specific indexed selection there.
// Scrolling only observes. Selecting replaces the address; opening proof
// views pushes history, so Back returns here.
import { useEffect, useLayoutEffect, useRef, useState } from "react";
import type { Edition } from "../app/edition";
import { fitDisplayMath, sanitizeManuscript, typeset } from "../text/html";
import { linesOf, meaningful, rowFor, type Row } from "./selectRow";
import { fromOutline, type ContentsRow } from "./Contents";
import { isRestoringReadingPlace } from "../app/restore";
import { href } from "../app/router";
import { face } from "../app/papers";

const TAG_TITLE = "Linked to Lean: click the paragraph to follow its proof";

interface Props {
  edition: Edition;
  paper: string;
  selected?: string;
  anchor?: string;
  page?: number;
  onSelect(id: string): void;
  onLink(paper: string, fragment?: string): void;
  onNavigateWithin?(): void;
  onRows?(rows: Row[]): void;
  /** The source line at the reading line, as the reader scrolls. */
  onReadingLine?(line: number): void;
  onContents?(rows: ContentsRow[]): void;
  /** A selection made by following the reading line: highlight it, never scroll to it. */
  followed?: string;
}

export function ManuscriptPaper({ edition, paper, selected, anchor, page, onSelect, onLink, onRows, onReadingLine, onContents, followed, onNavigateWithin }: Props) {
  const root = useRef<HTMLDivElement>(null);
  const [rows, setRows] = useState<Row[] | null>(null);
  const [sourceView, setSourceView] = useState(false);
  const [ready, setReady] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const descriptor = useRef<any>(null);
  const own = useRef<string | undefined>(undefined);
  const storeKey = `quartic:scroll:${edition.permalink}:${paper}`;

  // Refit wide display equations whenever the reading column changes width (pane, splitter, window).
  useEffect(() => {
    const el = root.current;
    if (!el || typeof ResizeObserver === "undefined") return;
    let width = 0, frame = 0;
    const ro = new ResizeObserver(([entry]) => {
      const w = Math.round(entry.contentRect.width);
      if (w === width) return;
      width = w;
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => fitDisplayMath(el));
    });
    ro.observe(el);
    return () => { ro.disconnect(); cancelAnimationFrame(frame); };
  }, []);

  useEffect(() => {
    let live = true;
    const blobs: string[] = [];
    setReady(false);
    setError(null);
    (async () => {
      const [manuscript, sel] = await Promise.all([edition.reader.manuscript(paper), edition.reader.resource(`selection/${paper}.json`)]);
      if (!live || !root.current) return;
      const { html, source } = manuscript;
      descriptor.current = manuscript.descriptor;
      const doc = (edition.reader.documents as any)[paper];
      const contents: ContentsRow[] = descriptor.current?.contents ?? (descriptor.current?.outline ? fromOutline(descriptor.current.outline, doc?.lines ?? 1e9) : []);
      onContents?.(contents.filter((r) => r.listed !== false && !/unlisted/.test(r.title)));
      setSourceView(html == null);
      if (html != null) {
        root.current.innerHTML = sanitizeManuscript(html);
        typeset(root.current);
        fitDisplayMath(root.current);
        // A manuscript that opens with its own title repeats the page header.
        const first = root.current.querySelector<HTMLElement>("h1, h2");
        const norm = (t: string) => t.replace(/\s+/g, " ").trim().toLowerCase();
        if (first && norm(first.textContent ?? "") === norm(face(paper).name)) first.closest<HTMLElement>(".source-block")?.classList.add("is-page-title");
        // Keep real reader destinations for copy-link, middle-click and
        // Cmd/Ctrl-click; plain clicks retain the reading-position excursion.
        const ed = edition.pinnedOlder ? edition.permalink : undefined;
        for (const link of root.current.querySelectorAll<HTMLAnchorElement>("a[href]")) {
          if (link.dataset.paper) {
            link.href = href({ page: "read", paper: link.dataset.paper, a: link.dataset.fragment, ed });
          } else if (link.getAttribute("href")?.startsWith("#")) {
            const raw = link.getAttribute("href")!.slice(1);
            let fragment = raw;
            try { fragment = decodeURIComponent(raw); } catch { /* retain a literal fragment */ }
            link.dataset.localFragment = fragment;
            link.href = href({ page: "read", paper, a: fragment, ed });
          }
        }
      } else if (source != null) {
        // Keep historical Markdown literal. Each line can still open its own evidence.
        const lines = source.split(/\r?\n/);
        if (lines.at(-1) === "") lines.pop();
        const body = document.createDocumentFragment();
        for (const [index, line] of lines.entries()) {
          const block = document.createElement("div");
          block.className = "source-block wrap";
          block.dataset.l0 = block.dataset.l1 = String(index + 1);
          block.textContent = line || "\n";
          body.append(block);
        }
        root.current.replaceChildren(body);
      } else throw new Error("This edition has no manuscript source.");
      for (const img of root.current.querySelectorAll<HTMLImageElement>("img[data-resource]")) {
        edition.reader.figure(paper, img.dataset.resource!).then((blob: Blob) => {
          if (!live) return;
          const url = URL.createObjectURL(blob);
          blobs.push(url);
          img.src = url;
        }, () => { img.alt = `Figure unavailable: ${img.alt}`; img.classList.add("is-missing"); });
      }
      setRows(sel as Row[]);
      onRows?.(sel as Row[]);
      setReady(true);
    })().catch((e) => live && setError(e instanceof Error ? e.message : String(e)));
    return () => { live = false; blobs.forEach((u) => URL.revokeObjectURL(u)); };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [edition, paper]);

  // Mark linked and selected blocks.
  useLayoutEffect(() => {
    const el = root.current;
    if (!el || !ready || !rows) return;
    const linked = rows.filter((r) => meaningful(r) && r.lines);
    const sel = linesOf(rows, selected);
    for (const block of el.querySelectorAll<HTMLElement>(".source-block[data-l0]")) {
      const a = Number(block.dataset.l0), b = Number(block.dataset.l1);
      const isLinked = linked.some((r) => r.lines![0] <= b && a <= r.lines![1]);
      block.classList.toggle("is-linked", isLinked);
      // The margin tag is a real element so it can carry its explanation.
      const tag = block.querySelector<HTMLElement>(":scope > .lean-tag");
      if (isLinked && !tag) {
        const t = document.createElement("span");
        t.className = "lean-tag lean-tag--margin";
        t.textContent = "Lean";
        t.title = TAG_TITLE;
        t.setAttribute("aria-hidden", "true");
        block.prepend(t);
      } else if (!isLinked && tag) tag.remove();
      const on = !!sel && sel[0] <= b && a <= sel[1];
      block.classList.toggle("is-selected", on);
      if (on) { block.setAttribute("aria-current", "true"); block.tabIndex = -1; }
      else { block.removeAttribute("aria-current"); block.removeAttribute("tabindex"); }
    }
  }, [ready, rows, selected]);

  // Navigation (not the reader's own click) brings its target into view, and
  // again once figures have loaded and changed the layout above it.
  useLayoutEffect(() => {
    const el = root.current;
    if (!el || !ready) return;
    const scroller = el.closest<HTMLElement>(".paper");
    let cancelled = false;
    const place = () => {
      if (cancelled || isRestoringReadingPlace()) return false;
      if (anchor) {
        const target = el.querySelector<HTMLElement>(`[id="${CSS.escape(anchor)}"]`);
        if (target) { target.scrollIntoView({ block: "start" }); return true; }
      }
      if (selected && selected !== own.current && selected !== followed) {
        const target = el.querySelector<HTMLElement>(".is-selected");
        if (target) { target.scrollIntoView({ block: "center" }); return true; }
      }
      if (page && paper === "original") {
        const location = descriptor.current?.page_locations?.find((p: any) => p.page === page);
        const anchorTarget = location?.anchor && el.querySelector<HTMLElement>(`[id="${CSS.escape(location.anchor)}"]`);
        if (anchorTarget) { anchorTarget.scrollIntoView({ block: "start" }); return true; }
        const line = location?.lines?.[0];
        const target = typeof line === "number" ? [...el.querySelectorAll<HTMLElement>(".source-block[data-l0]")].find((b) => Number(b.dataset.l0) <= line && line <= Number(b.dataset.l1)) : null;
        if (target) { target.scrollIntoView({ block: "start" }); return true; }
      }
      return false;
    };
    if (place()) {
      const images = [...el.querySelectorAll<HTMLImageElement>("img[data-resource]")].filter((i) => !i.complete || !i.naturalWidth);
      let pending = images.length;
      const again = () => { if (--pending <= 0) place(); };
      images.forEach((i) => { i.addEventListener("load", again, { once: true }); i.addEventListener("error", again, { once: true }); });
      const t = window.setTimeout(place, 700);
      const stop = () => { cancelled = true; clearTimeout(t); };
      const input = ["wheel", "touchstart", "pointerdown", "keydown"] as const;
      input.forEach((type) => window.addEventListener(type, stop, { capture: true, passive: true }));
      return () => { stop(); input.forEach((type) => window.removeEventListener(type, stop, true)); images.forEach((i) => { i.removeEventListener("load", again); i.removeEventListener("error", again); }); };
    }
    if (!isRestoringReadingPlace() && !selected && !anchor && !page && scroller) {
      try { scroller.scrollTop = Number(sessionStorage.getItem(storeKey) ?? 0); } catch { /* no storage */ }
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [ready, selected, anchor, page]);

  useEffect(() => {
    const scroller = root.current?.closest<HTMLElement>(".paper");
    if (!scroller) return;
    let t = 0;
    const on = () => {
      clearTimeout(t);
      t = window.setTimeout(() => { try { sessionStorage.setItem(storeKey, String(Math.round(scroller.scrollTop))); } catch { /* no storage */ } }, 250);
    };
    scroller.addEventListener("scroll", on, { passive: true });
    return () => scroller.removeEventListener("scroll", on);
  }, [storeKey, ready]);

  // Report the block at the reading line, a third of the way down the pane.
  useEffect(() => {
    const el = root.current;
    const scroller = el?.closest<HTMLElement>(".paper");
    if (!el || !scroller || !ready || !onReadingLine) return;
    let frame = 0, last = -1;
    const look = () => {
      frame = 0;
      const box = scroller.getBoundingClientRect();
      const x = el.getBoundingClientRect().left + Math.min(40, el.clientWidth / 2);
      const hit = document.elementFromPoint(x, box.top + box.height * 0.35)?.closest<HTMLElement>(".source-block[data-l0]");
      const line = hit ? Number(hit.dataset.l0) : -1;
      if (line > 0 && line !== last) { last = line; onReadingLine(line); }
    };
    // A short timer, not an animation frame: frames pause in background tabs.
    const on = () => { if (!frame) frame = window.setTimeout(look, 80); };
    scroller.addEventListener("scroll", on, { passive: true });
    const t = window.setTimeout(look, 300);
    return () => { scroller.removeEventListener("scroll", on); clearTimeout(frame); clearTimeout(t); };
  }, [ready, onReadingLine]);

  function onClick(e: React.MouseEvent) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    const target = e.target as HTMLElement;
    const a = target.closest("a");
    if (a) {
      const toPaper = a.getAttribute("data-paper");
      if (toPaper) { e.preventDefault(); onLink(toPaper, a.getAttribute("data-fragment") ?? undefined); return; }
      const fragment = a.getAttribute("data-local-fragment");
      if (fragment != null) {
        e.preventDefault();
        onNavigateWithin?.();
        root.current?.querySelector<HTMLElement>(`[id="${CSS.escape(fragment)}"]`)?.scrollIntoView({ block: "center" });
      }
      return;
    }
    if (target.closest("button") || window.getSelection()?.toString()) return;
    const block = target.closest<HTMLElement>(".source-block[data-l0]");
    if (!block || !rows) return;
    const id = rowFor(rows, Number(block.dataset.l0), Number(block.dataset.l1));
    // Plain prose has nothing to show: a click there leaves the panel on the last linked passage.
    if (/^l\d+-\d+$/.test(id)) return;
    own.current = id;
    onSelect(id);
  }

  return (
    <>
      {error && (
        <div className="failed" role="alert">
          <p><strong>This paper could not be opened.</strong> {error}</p>
          <p><button type="button" className="tool" onClick={() => location.reload()}>Reload the page</button></p>
        </div>
      )}
      {!ready && !error && (
        <div className="paper-skeleton" role="status">
          <span className="sr-only">Loading the paper…</span>
          {[92, 100, 96, 88, 100, 64, 0, 100, 94, 98, 72].map((w, i) => <span key={i} className="paper-skeleton__line" style={{ width: `${w}%` }} aria-hidden="true" />)}
        </div>
      )}
      {ready && sourceView && <p className="quiet">Manuscript source from this edition. Select a passage to inspect its evidence.</p>}
      <div ref={root} className={`manuscript manuscript--${paper}`} onClick={onClick} hidden={!ready} />
    </>
  );
}
