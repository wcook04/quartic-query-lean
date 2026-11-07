// Adapted from Proof Reader's proof/ProofPage.tsx and SK's MapPane dock handle,
// Apache-2.0: pointer capture, a CSS share, persisted size and keyboard resizing.
import { useLayoutEffect, useRef, useState } from "react";

const KEY = "quartic:proof-width:v1";
const DEFAULT = 0.44;
export function ReaderSplit() {
  const handle = useRef<HTMLDivElement>(null);
  const [share, setShare] = useState(() => {
    try { const n = Number(localStorage.getItem(KEY)); return n >= .25 && n <= .68 ? n : DEFAULT; } catch { return DEFAULT; }
  });
  const desk = () => handle.current?.closest<HTMLElement>(".desk");
  function clamp(value: number) {
    const width = desk()?.clientWidth || window.innerWidth;
    return Math.max(Math.max(.25, 360 / width), Math.min(Math.min(.68, 1 - 420 / width), value));
  }
  function apply(value: number, save = true) {
    const next = clamp(value);
    desk()?.style.setProperty("--proof-width", `${next * 100}%`);
    setShare(next);
    if (save) try { localStorage.setItem(KEY, String(next)); } catch { /* optional preference */ }
  }
  useLayoutEffect(() => {
    const root = desk(), paper = root?.querySelector<HTMLElement>(".paper");
    if (!root || !paper) return;
    apply(share, false);
    const measure = () => { root.toggleAttribute("data-narrow-paper", paper.clientWidth < 900); };
    const observer = new ResizeObserver(measure);
    observer.observe(paper); measure();
    return () => { observer.disconnect(); root.removeAttribute("data-narrow-paper"); };
    // The stored preference is applied once; dragging updates the same property.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  return <div ref={handle} className="reader-split" role="separator" aria-orientation="vertical"
    aria-label="Resize paper and proof panes" aria-valuemin={25} aria-valuemax={68} aria-valuenow={Math.round(share * 100)}
    aria-valuetext={`${Math.round(share * 100)} percent for the proof`} tabIndex={0}
    title="Drag to resize. Arrow keys adjust it; double-click resets it."
    onDoubleClick={() => apply(DEFAULT)}
    onKeyDown={(e) => {
      if (!["ArrowLeft", "ArrowRight", "Home", "Enter"].includes(e.key)) return;
      e.preventDefault(); e.stopPropagation();
      apply(e.key === "Home" || e.key === "Enter" ? DEFAULT : share + (e.key === "ArrowLeft" ? .025 : -.025));
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
