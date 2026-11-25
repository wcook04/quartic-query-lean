// Adapted from Proof Reader's proof/ProofPage.tsx and SK's MapPane dock handle,
// Apache-2.0: pointer capture, a CSS share, persisted size and keyboard resizing.
import { useLayoutEffect, useRef, useState } from "react";

const KEY = "quartic:proof-width:v1";
const DEFAULT = 0.5;
/** The grid's handle column, and the contents rail inside `.paper--contents` (216px and its 72px gap). */
const HANDLE = 10;
const OUTLINE = 216 + 72;
/** The share a reader set by dragging or the arrow keys; none means the balanced default. */
function chosenShare(): number | null {
  try {
    const kept = localStorage.getItem(KEY);
    const n = Number(kept);
    return kept != null && n >= .25 && n <= .68 ? n : null;
  } catch { return null; }
}
/** `outline`: the paper has its contents rail (`.paper--contents`). */
export function ReaderSplit({ outline = false }: { outline?: boolean }) {
  const handle = useRef<HTMLDivElement>(null);
  const chosen = useRef<number | null>(chosenShare());
  const hasOutline = useRef(outline);
  hasOutline.current = outline;
  const [share, setShare] = useState(() => chosen.current ?? DEFAULT);
  const desk = () => handle.current?.closest<HTMLElement>(".desk");
  // Balanced: the paper's reading lane and the pane get about half each. Where the contents rail
  // shows (over 1240px, and while the paper column keeps 900px) it is left out of the paper's half.
  function balanced() {
    const width = desk()?.clientWidth || window.innerWidth;
    const rail = hasOutline.current && window.matchMedia("(min-width: 1241px)").matches ? OUTLINE : 0;
    let proof = (width - HANDLE - rail) / 2;
    if (rail && width - HANDLE - proof < 900) proof = (width - HANDLE) / 2;
    return proof / width;
  }
  function clamp(value: number) {
    const width = desk()?.clientWidth || window.innerWidth;
    return Math.max(Math.max(.25, 360 / width), Math.min(Math.min(.68, 1 - 420 / width), value));
  }
  function apply(value: number, save = true) {
    const next = clamp(value);
    desk()?.style.setProperty("--proof-width", `${next * 100}%`);
    setShare(next);
    if (save) {
      chosen.current = next;
      try { localStorage.setItem(KEY, String(next)); } catch { /* optional preference */ }
    }
  }
  // Reset forgets the reader's width: the split is balanced again and follows the window.
  function reset() {
    chosen.current = null;
    try { localStorage.removeItem(KEY); } catch { /* optional preference */ }
    apply(balanced(), false);
  }
  // A paper's contents rail arrives with its manuscript and changes the balance.
  useLayoutEffect(() => {
    if (chosen.current == null) apply(balanced(), false);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [outline]);
  useLayoutEffect(() => {
    const root = desk(), paper = root?.querySelector<HTMLElement>(".paper");
    if (!root || !paper) return;
    apply(chosen.current ?? balanced(), false);
    const measure = () => { root.toggleAttribute("data-narrow-paper", paper.clientWidth < 900); };
    const observer = new ResizeObserver(measure);
    observer.observe(paper); measure();
    // Until the reader resizes, the balance follows the window.
    const follow = new ResizeObserver(() => { if (chosen.current == null) apply(balanced(), false); });
    follow.observe(root);
    return () => { observer.disconnect(); follow.disconnect(); root.removeAttribute("data-narrow-paper"); };
    // A stored preference is applied once; dragging updates the same property.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  return <div ref={handle} className="reader-split" role="separator" aria-orientation="vertical"
    aria-label="Resize paper and proof panes" aria-valuemin={25} aria-valuemax={68} aria-valuenow={Math.round(share * 100)}
    aria-valuetext={`${Math.round(share * 100)} percent for the proof`} tabIndex={0}
    title="Drag to resize. Arrow keys adjust it; double-click resets it."
    onDoubleClick={reset}
    onKeyDown={(e) => {
      if (!["ArrowLeft", "ArrowRight", "Home", "Enter"].includes(e.key)) return;
      e.preventDefault(); e.stopPropagation();
      if (e.key === "Home" || e.key === "Enter") reset();
      else apply(share + (e.key === "ArrowLeft" ? .025 : -.025));
    }}
    onPointerDown={(e) => {
      if (e.button !== 0) return;
      e.preventDefault();
      const h = e.currentTarget, root = desk();
      if (!root) return;
      h.setPointerCapture(e.pointerId);
      root.classList.add("is-resizing");
      const move = (event: PointerEvent) => {
        const box = root.getBoundingClientRect();
        apply((box.right - event.clientX) / box.width);
      };
      const end = () => {
        h.removeEventListener("pointermove", move); h.removeEventListener("pointerup", end);
        h.removeEventListener("pointercancel", end); h.removeEventListener("lostpointercapture", end);
        root.classList.remove("is-resizing");
      };
      h.addEventListener("pointermove", move); h.addEventListener("pointerup", end);
      h.addEventListener("pointercancel", end); h.addEventListener("lostpointercapture", end);
    }}><span aria-hidden="true" /></div>;
}
