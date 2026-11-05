// One manuscript, from the edition's Pandoc HTML. Its blocks carry their
// source lines; a click selects the most specific indexed selection there.
// Scrolling only observes. Selecting replaces the address; opening proof
// views pushes history, so Back returns here.
import { useEffect, useLayoutEffect, useRef, useState } from "react";
import type { Edition } from "../app/edition";
import { sanitizeManuscript, typeset } from "../text/html";
import { linesOf, meaningful, rowFor, type Row } from "./selectRow";

interface Props {
  edition: Edition;
  paper: string;
  selected?: string;
  anchor?: string;
  onSelect(id: string): void;
  onLink(paper: string, fragment?: string): void;
  onRows?(rows: Row[]): void;
}

export function ManuscriptPaper({ edition, paper, selected, anchor, onSelect, onLink, onRows }: Props) {
  const root = useRef<HTMLDivElement>(null);
  const [rows, setRows] = useState<Row[] | null>(null);
  const [ready, setReady] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const own = useRef<string | undefined>(undefined);
  const storeKey = `quartic:scroll:${edition.permalink}:${paper}`;

  useEffect(() => {
    let live = true;
    const blobs: string[] = [];
    setReady(false);
    setError(null);
    (async () => {
      const [{ html }, sel] = await Promise.all([edition.reader.manuscript(paper), edition.reader.resource(`selection/${paper}.json`)]);
      if (!live || !root.current) return;
      if (html == null) throw new Error("this earlier edition was published before the reader could display manuscripts. Use the banner above to open the current edition.");
      root.current.innerHTML = sanitizeManuscript(html);
      typeset(root.current);
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
    const place = () => {
      if (anchor) {
        const target = el.querySelector<HTMLElement>(`[id="${CSS.escape(anchor)}"]`);
        if (target) { target.scrollIntoView({ block: "start" }); return true; }
      }
      if (selected && selected !== own.current) {
        const target = el.querySelector<HTMLElement>(".is-selected");
        if (target) { target.scrollIntoView({ block: "center" }); return true; }
      }
      return false;
    };
    if (place()) {
      const images = [...el.querySelectorAll<HTMLImageElement>("img[data-resource]")].filter((i) => !i.complete || !i.naturalWidth);
      let pending = images.length;
      const again = () => { if (--pending <= 0) place(); };
      images.forEach((i) => { i.addEventListener("load", again, { once: true }); i.addEventListener("error", again, { once: true }); });
      const t = window.setTimeout(place, 700);
      return () => { clearTimeout(t); images.forEach((i) => { i.removeEventListener("load", again); i.removeEventListener("error", again); }); };
    }
    if (!selected && !anchor && scroller) {
      try { scroller.scrollTop = Number(sessionStorage.getItem(storeKey) ?? 0); } catch { /* no storage */ }
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [ready, selected, anchor]);

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
    own.current = id;
    onSelect(id);
  }

  return (
    <>
      {error && <div className="failed" role="alert"><p>This paper could not be opened: {error}</p></div>}
      {!ready && !error && <p className="pending" role="status">Loading the paper…</p>}
      <div ref={root} className="manuscript" onClick={onClick} hidden={!ready} />
    </>
  );
}
