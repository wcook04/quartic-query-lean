// OpenAI's PDF, unchanged, drawn by pdf.js from the edition's verified bytes.
// Beside each page: the statements the project indexed there, placed at the
// PDF's own named destination when it has one. No highlight is invented.
// Rendering approach adapted from proof-reader web/src/paper/PdfPane.tsx at
// e2df888, Copyright 2026 proof-reader contributors, Apache-2.0.
import { useEffect, useLayoutEffect, useMemo, useRef, useState } from "react";
import * as pdfjs from "pdfjs-dist";
import workerUrl from "pdfjs-dist/build/pdf.worker.min.mjs?url";
import type { PDFDocumentProxy } from "pdfjs-dist";
import type { Edition } from "../app/edition";
import { statementName } from "../app/papers";
import type { Row } from "./selectRow";

pdfjs.GlobalWorkerOptions.workerSrc = workerUrl;

interface Props {
  edition: Edition;
  selected?: string;
  page?: number;
  onSelect(id: string): void;
  onPage(page: number): void;
}

interface Placed { row: Row; y: number | null }

export function PdfPaper({ edition, selected, page, onSelect, onPage }: Props) {
  const [pdf, setPdf] = useState<PDFDocumentProxy | null>(null);
  const [rows, setRows] = useState<Row[]>([]);
  const [texts, setTexts] = useState<Record<string, string>>({});
  const [placed, setPlaced] = useState<Map<number, Placed[]>>(new Map());
  const [error, setError] = useState<string | null>(null);
  const [width, setWidth] = useState(0);
  const [upstream, setUpstream] = useState<string | null>(null);
  const box = useRef<HTMLDivElement>(null);
  const storeKey = `quartic:scroll:${edition.permalink}:original`;

  useEffect(() => {
    let live = true;
    let doc: PDFDocumentProxy | null = null;
    (async () => {
      const reading: any = await edition.reader.resource("reading.json");
      const meta = reading.papers.original;
      setUpstream(meta.url ?? null);
      const sel = (await edition.reader.resource("selection/original.json")) as Row[];
      if (!live) return;
      setRows(sel);
      if (!meta.resource) throw new Error("This edition does not hold a copy of the PDF.");
      const bytes = await edition.reader.readBytes(meta.resource);
      doc = await pdfjs.getDocument({ data: new Uint8Array(bytes) }).promise;
      if (!live) return;
      // Place each indexed statement at its PDF destination, when it has one.
      const map = new Map<number, Placed[]>();
      for (const row of sel) {
        let y: number | null = null;
        const dest = row.location?.destination;
        if (dest) {
          try {
            const d = await doc.getDestination(dest);
            if (d && typeof d[3] === "number") {
              const pg = await doc.getPage(row.location!.page);
              y = pg.view[3] - (d[3] as number);
            }
          } catch { /* fall back to the page */ }
        }
        const pageNo = row.location!.page;
        map.set(pageNo, [...(map.get(pageNo) ?? []), { row, y }]);
      }
      for (const list of map.values()) list.sort((a, b) => (a.y ?? 0) - (b.y ?? 0));
      if (!live) return;
      setPlaced(map);
      setPdf(doc);
      edition.reader.resource("corpus/statements.json").then((all: any[]) => {
        if (!live) return;
        const t: Record<string, string> = {};
        for (const s of all) t[s.id] = s.statement;
        setTexts(t);
      }, () => {});
    })().catch((e) => live && setError(e instanceof Error ? e.message : String(e)));
    return () => { live = false; void doc?.destroy(); };
  }, [edition]);

  useLayoutEffect(() => {
    const el = box.current;
    if (!el) return;
    const measure = () => setWidth(Math.min(el.clientWidth, 900));
    measure();
    const ro = new ResizeObserver(measure);
    ro.observe(el);
    return () => ro.disconnect();
  }, []);

  const selRow = useMemo(() => rows.find((r) => r.id === selected), [rows, selected]);
  const target = selRow?.location?.page ?? page;

  // Go to the selected statement, or the requested page, whenever it changes.
  useEffect(() => {
    if (!pdf || !width) return;
    const scroller = box.current?.closest<HTMLElement>(".paper");
    // Page sizes arrive asynchronously; place once now and again once they have.
    const place = () => {
    const node = selRow ? (document.getElementById(`mark-${selRow.id}`) ?? document.getElementById(`pin-${selRow.id}`)) : target ? document.getElementById(`page-${target}`) : null;
    if (node) node.scrollIntoView({ block: selRow ? "center" : "start" });
    else if (scroller) { try { scroller.scrollTop = Number(sessionStorage.getItem(storeKey) ?? 0); } catch { /* none */ } }
    };
    place();
    const t = window.setTimeout(place, 450);
    return () => clearTimeout(t);
  }, [pdf, width, selRow, target, storeKey]);

  useEffect(() => {
    const scroller = box.current?.closest<HTMLElement>(".paper");
    if (!scroller) return;
    let t = 0;
    const on = () => { clearTimeout(t); t = window.setTimeout(() => { try { sessionStorage.setItem(storeKey, String(Math.round(scroller.scrollTop))); } catch { /* none */ } }, 250); };
    scroller.addEventListener("scroll", on, { passive: true });
    return () => scroller.removeEventListener("scroll", on);
  }, [storeKey, pdf]);

  if (error)
    return (
      <div className="failed" role="alert">
        <p>The PDF could not be opened here: {error}</p>
        {upstream && <p><a href={upstream} target="_blank" rel="noopener noreferrer">Open OpenAI’s published PDF</a></p>}
      </div>
    );
  return (
    <div ref={box} className="pdf">
      {!pdf && <p className="pending" role="status">Loading OpenAI’s PDF…</p>}
      {pdf && width > 0 && Array.from({ length: pdf.numPages }, (_, i) => (
        <PdfPage key={i} pdf={pdf} n={i + 1} width={width} pins={placed.get(i + 1) ?? []} texts={texts}
          selected={selected} onSelect={onSelect} onPage={onPage} />
      ))}
      {pdf && upstream && <p className="pdf__foot">OpenAI’s published copy is also <a href={upstream} target="_blank" rel="noopener noreferrer">on GitHub</a>.</p>}
    </div>
  );
}

function PdfPage({ pdf, n, width, pins, texts, selected, onSelect, onPage }: {
  pdf: PDFDocumentProxy; n: number; width: number; pins: Placed[]; texts: Record<string, string>; selected?: string; onSelect(id: string): void; onPage(p: number): void;
}) {
  const canvas = useRef<HTMLCanvasElement>(null);
  const holder = useRef<HTMLDivElement>(null);
  const [size, setSize] = useState<{ w: number; h: number; scale: number } | null>(null);
  const [visible, setVisible] = useState(n <= 2);

  useEffect(() => {
    let live = true;
    pdf.getPage(n).then((p) => {
      if (!live) return;
      const base = p.getViewport({ scale: 1 });
      const scale = width / base.width;
      setSize({ w: width, h: base.height * scale, scale });
    });
    return () => { live = false; };
  }, [pdf, n, width]);

  useEffect(() => {
    const el = holder.current;
    if (!el) return;
    const io = new IntersectionObserver((es) => es.some((e) => e.isIntersecting) && setVisible(true), { rootMargin: "800px 0px" });
    io.observe(el);
    return () => io.disconnect();
  }, []);

  useEffect(() => {
    if (!visible || !size || !canvas.current) return;
    let task: ReturnType<Awaited<ReturnType<PDFDocumentProxy["getPage"]>>["render"]> | null = null;
    let live = true;
    pdf.getPage(n).then((p) => {
      if (!live || !canvas.current) return;
      const ratio = Math.min(window.devicePixelRatio || 1, 2);
      const vp = p.getViewport({ scale: size.scale * ratio });
      const c = canvas.current;
      c.width = vp.width;
      c.height = vp.height;
      task = p.render({ canvasContext: c.getContext("2d")!, viewport: vp, canvas: c } as any);
    });
    return () => { live = false; task?.cancel(); };
  }, [visible, size, pdf, n]);

  return (
    <section className="pdf__page" id={`page-${n}`} aria-label={`Page ${n}`} ref={holder}>
      <div className="pdf__sheet" style={size ? { width: size.w, height: size.h } : { width, height: width * 1.3 }}>
        <canvas ref={canvas} style={size ? { width: size.w, height: size.h } : undefined} role="img" aria-label={`Page ${n} of OpenAI’s paper`} />
        {size && pins.filter((p) => p.y != null).map((p) => (
          <span key={p.row.id} id={`mark-${p.row.id}`} className={`pdf__mark${p.row.id === selected ? " is-selected" : ""}`} style={{ top: p.y! * size.scale }} aria-hidden="true" />
        ))}
      </div>
      <aside className="pdf__rail" aria-label={`Indexed on page ${n}`}>
        <button type="button" className="pdf__pageno" onClick={() => onPage(n)}>Page {n}</button>
        {pins.length === 0 && <p className="quiet">No indexed statement on this page.</p>}
        <ul>
          {pins.map((p) => {
            const sid = p.row.statements?.[0] ?? p.row.id;
            return (
              <li key={p.row.id} id={`pin-${p.row.id}`}>
                <button type="button" className={`pin${p.row.id === selected ? " is-selected" : ""}`} aria-pressed={p.row.id === selected} onClick={() => onSelect(p.row.id)} title={texts[sid]}>
                  {statementName(sid)}
                </button>
              </li>
            );
          })}
        </ul>
      </aside>
    </section>
  );
}
