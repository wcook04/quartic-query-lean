// One manuscript, from the edition's Pandoc HTML. Its blocks carry their
// source lines; a click selects the most specific indexed selection there.
// Scrolling only observes. Selecting replaces the address; opening proof
// views pushes history, so Back returns here.
import { useEffect, useLayoutEffect, useRef, useState } from "react";
import type { Edition } from "../app/edition";
import { sanitizeManuscript, typeset } from "../text/html";
import { linesOf, meaningful, rowFor, type Row } from "./selectRow";
import { fromOutline, type ContentsRow } from "./Contents";
import { isRestoringReadingPlace } from "../app/restore";

interface Props {
  edition: Edition;
  paper: string;
  selected?: string;
  anchor?: string;
  page?: number;
  onSelect(id: string): void;
  onLink(paper: string, fragment?: string): void;
  onRows?(rows: Row[]): void;
  /** The source line at the reading line, as the reader scrolls. */
  onReadingLine?(line: number): void;
  onContents?(rows: ContentsRow[]): void;
  /** A selection made by following the reading line: highlight it, never scroll to it. */
  followed?: string;
}

export function ManuscriptPaper({ edition, paper, selected, anchor, page, onSelect, onLink, onRows, onReadingLine, onContents, followed }: Props) {
  const root = useRef<HTMLDivElement>(null);
  const [rows, setRows] = useState<Row[] | null>(null);
  const [sourceView, setSourceView] = useState(false);
  const [ready, setReady] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const descriptor = useRef<any>(null);
  const own = useRef<string | undefined>(undefined);
  const storeKey = `quartic:scroll:${edition.permalink}:${paper}`;

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
      block.classList.toggle("is-linked", linked.some((r) => r.lines![0] <= b && a <= r.lines![1]));
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
    const target = e.target as HTMLElement;
    const a = target.closest("a");
    if (a) {
      const toPaper = a.getAttribute("data-paper");
      const hrefAttr = a.getAttribute("href") ?? "";
      if (toPaper) { e.preventDefault(); onLink(toPaper, a.getAttribute("data-fragment") ?? undefined); return; }
      if (hrefAttr.startsWith("#")) {
        e.preventDefault();
        root.current?.querySelector<HTMLElement>(`[id="${CSS.escape(hrefAttr.slice(1))}"]`)?.scrollIntoView({ block: "center" });
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
      {error && <div className="failed" role="alert"><p>This paper could not be opened: {error}</p></div>}
      {!ready && !error && <p className="pending" role="status">Loading the paper…</p>}
      {ready && sourceView && <p className="quiet">Manuscript source from this edition. Select a passage to inspect its evidence.</p>}
      <div ref={root} className={`manuscript manuscript--${paper}`} onClick={onClick} hidden={!ready} />
    </>
  );
}
