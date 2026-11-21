// A clicked phrase under the graph: the graph keeps the top of the pane and the phrase's
// card with its Lean lines takes the bottom, scrolling on its own. The divider adapts the
// reader's paper/proof handle (app/ReaderSplit.tsx): pointer capture, a CSS share, a
// remembered size and keyboard resizing, here on the vertical axis.
import { useEffect, useLayoutEffect, useRef, useState } from "react";
import type { Edition } from "../app/edition";
import { LeanPanel } from "./LeanPanel";
import { usePhrases } from "../paper/phrases";
import { Title } from "../text/title";
import { CloseIcon } from "../app/icons";
import { DeclTitle } from "./common";

const KEY = "quartic:phrase-split:v1";
const DEFAULT = 0.55;

/** The draggable divider between the graph (above) and the phrase (below). */
export function PhraseDivider() {
  const handle = useRef<HTMLDivElement>(null);
  const [share, setShare] = useState(() => {
    try { const n = Number(localStorage.getItem(KEY)); return n >= .2 && n <= .8 ? n : DEFAULT; } catch { return DEFAULT; }
  });
  const box = () => handle.current?.closest<HTMLElement>(".inspector__graph");
  function apply(value: number, save = true) {
    const height = box()?.clientHeight || window.innerHeight;
    const next = Math.max(Math.max(.2, 120 / height), Math.min(Math.min(.8, 1 - 160 / height), value));
    box()?.style.setProperty("--phrase-split", `${next * 100}%`);
    setShare(next);
    if (save) try { localStorage.setItem(KEY, String(next)); } catch { /* optional preference */ }
  }
  // A subject that needs more height than the graph's share has at reading size gets it, up to
  // four fifths of the pane, for as long as it is shown; the reader's own share returns after.
  useEffect(() => {
    const on = (event: Event) => {
      const need = (event as CustomEvent<{ content: number; view: number } | null>).detail;
      const root = box();
      if (!root) return;
      const total = root.clientHeight;
      const top = root.querySelector<HTMLElement>(".inspector__map")?.clientHeight ?? total * share;
      // The height the graph's share must have for the bands to show whole, from their own height.
      const wanted = need ? Math.min(0.85, Math.max(share, (top - need.view + need.content + 6) / total)) : share;
      const current = parseFloat(root.style.getPropertyValue("--phrase-split")) / 100 || share;
      if (Math.abs(wanted - current) > 0.005) root.style.setProperty("--phrase-split", `${wanted * 100}%`);
    };
    window.addEventListener("quartic:graph-need", on);
    return () => window.removeEventListener("quartic:graph-need", on);
  }, [share]);
  useLayoutEffect(() => {
    apply(share, false);
    const root = box();
    return () => { root?.style.removeProperty("--phrase-split"); };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  return (
    <div ref={handle} className="phrase-divider" role="separator" aria-orientation="horizontal"
      aria-label="Resize the graph and the phrase" aria-valuemin={20} aria-valuemax={80} aria-valuenow={Math.round(share * 100)}
      aria-valuetext={`${Math.round(share * 100)} percent for the graph`} tabIndex={0}
      title="Drag to resize the graph and the phrase. Arrow keys adjust it; double-click resets it."
      onDoubleClick={() => apply(DEFAULT)}
      onKeyDown={(e) => {
        if (!["ArrowUp", "ArrowDown", "Home", "Enter"].includes(e.key)) return;
        e.preventDefault(); e.stopPropagation();
        apply(e.key === "Home" || e.key === "Enter" ? DEFAULT : share + (e.key === "ArrowUp" ? -.05 : .05));
      }}
      onPointerDown={(e) => {
        if (e.button !== 0) return;
        e.preventDefault();
        const h = e.currentTarget, root = box();
        if (!root) return;
        h.setPointerCapture(e.pointerId);
        root.classList.add("is-resizing");
        const move = (event: PointerEvent) => {
          const r = root.getBoundingClientRect();
          apply((event.clientY - r.top) / r.height);
        };
        const end = () => {
          h.removeEventListener("pointermove", move); h.removeEventListener("pointerup", end);
          h.removeEventListener("pointercancel", end); h.removeEventListener("lostpointercapture", end);
          root.classList.remove("is-resizing");
        };
        h.addEventListener("pointermove", move); h.addEventListener("pointerup", end);
        h.addEventListener("pointercancel", end); h.addEventListener("lostpointercapture", end);
      }}><span aria-hidden="true" /></div>
  );
}

/** The phrase half: its card and Lean, with a close button; Escape closes it too. */
export function PhraseSplit({ edition, id, name, onClose, onPick }: { edition: Edition; id: string; name?: string; onClose(): void; onPick(name: string): void }) {
  const layer = usePhrases();
  const phrase = layer?.byId.get(id);
  const declaration = name && phrase?.lean.some((r) => r.name === name) ? name : phrase?.lean[0]?.name;
  useEffect(() => {
    // Escape restores the full graph before it can close the whole pane.
    const on = (e: KeyboardEvent) => {
      if (e.key !== "Escape" || e.defaultPrevented || document.querySelector(":popover-open")) return;
      e.preventDefault(); e.stopPropagation();
      onClose();
    };
    window.addEventListener("keydown", on, true);
    return () => window.removeEventListener("keydown", on, true);
  }, [onClose]);
  if (!layer || !phrase || !declaration) return null;
  const title = layer.titles[declaration];
  return (
    <section className="phrase-split" aria-label="The chosen phrase and its Lean">
      <header className="phrase-split__bar">
        <p className="phrase-split__k">Chosen phrase{title && phrase.lean.length === 1 && <> · <Title text={title.title} /></>}{phrase.lean.length > 1 && <> · {phrase.lean.length} declarations</>}</p>
        <button type="button" className="phrase-split__close" onClick={onClose} aria-label="Close the phrase and show the whole graph" title="Close (Esc)">
          <CloseIcon />
        </button>
      </header>
      {phrase.lean.length > 1 && (
        <div className="phrase-split__tabs" role="tablist" aria-label="Declarations tied to this phrase">
          {phrase.lean.map((row) => (
            <button key={row.name} type="button" role="tab" aria-selected={row.name === declaration} onClick={() => onPick(row.name)}>
              {layer.titles[row.name] ? <Title text={layer.titles[row.name].title} /> : row.name}
            </button>
          ))}
        </div>
      )}
      <div className="phrase-split__body">
        <LeanPanel key={`${id}:${declaration}`} edition={edition} name={declaration} phrase={id} />
      </div>
    </section>
  );
}

export interface GraphTarget { name: string; drawn: string | null; relation: "self" | "user" | "used" | null }

/** The card the graph centres for a phrase's declaration: the declaration itself when the map
 *  draws it, else the nearest drawn card that uses it, else the nearest drawn card it uses
 *  (fewest Lean steps in the recorded graph). */
export function useGraphTarget(edition: Edition, name: string | undefined): GraphTarget | null {
  const [target, setTarget] = useState<GraphTarget | null>(null);
  useEffect(() => {
    if (!name) { setTarget(null); return; }
    let live = true;
    (async (): Promise<GraphTarget> => {
      const reader = edition.reader as any;
      const map = await reader.proofMap();
      const cards = map?.currentness === "current" ? map.cards ?? {} : {};
      if (Object.hasOwn(cards, name)) return { name, drawn: name, relation: "self" };
      for (const relation of ["user", "used"] as const) {
        const seen = new Set([name]);
        let frontier = [name];
        while (frontier.length && seen.size < 3000) {
          const next: string[] = [];
          for (const n of frontier) {
            const node = await reader.expand(n).catch(() => null);
            const side = relation === "user" ? node?.incoming : node;
            for (const kind of ["type", "value", "structural"])
              for (const other of side?.[kind] ?? []) {
                if (seen.has(other)) continue;
                seen.add(other);
                if (Object.hasOwn(cards, other)) return { name, drawn: other, relation };
                next.push(other);
              }
          }
          frontier = next;
        }
      }
      return { name, drawn: null, relation: null };
    })().then((t) => live && setTarget(t), () => live && setTarget({ name, drawn: null, relation: null }));
    return () => { live = false; };
  }, [edition, name]);
  return target?.name === name ? target : null;
}

/** The bottom part when no phrase is chosen: a clicked card's declaration, else the Lean of the
 *  paragraph being followed (one tab per declaration), else a one-line state with the passage. */
export function LeanSplit({ edition, names, mode, passage, onClose }: {
  edition: Edition; names: string[]; mode: "card" | "follow" | "none";
  passage?: { title?: string; html?: string } | null; onClose?(): void;
}) {
  const [pick, setPick] = useState(0);
  const key = names.join("|");
  useEffect(() => setPick(0), [key]);
  useEffect(() => {
    if (!onClose) return;
    const on = (e: KeyboardEvent) => {
      if (e.key !== "Escape" || e.defaultPrevented || document.querySelector(":popover-open")) return;
      e.preventDefault(); e.stopPropagation();
      onClose();
    };
    window.addEventListener("keydown", on, true);
    return () => window.removeEventListener("keydown", on, true);
  }, [onClose]);
  const name = names[Math.min(pick, names.length - 1)];
  return (
    <section className="phrase-split lean-split" aria-label={mode === "card" ? "The selected card and its Lean" : "The Lean of the paragraph being read"}>
      <header className="phrase-split__bar">
        <p className="phrase-split__k">{mode === "card" ? "Selected card" : mode === "follow" ? "Following the paper · the Lean linked to this paragraph" : "Following the paper"}</p>
        {onClose && (
          <button type="button" className="phrase-split__close" onClick={onClose} aria-label="Close the card and follow the paper" title="Close (Esc)">
            <CloseIcon />
          </button>
        )}
      </header>
      {names.length > 1 && (
        <div className="phrase-split__tabs" role="tablist" aria-label="Declarations linked to this paragraph">
          {names.map((n, i) => (
            <button key={n} type="button" role="tab" aria-selected={i === pick} onClick={() => setPick(i)}><DeclName name={n} /></button>
          ))}
        </div>
      )}
      <div className="phrase-split__body">
        {name ? <LeanPanel key={name} edition={edition} name={name} forStep={mode === "follow"} />
          : (
            <div className="lean-split__none">
              <p className="lean-split__state">No Lean is linked to this paragraph.</p>
              {passage && (passage.title || passage.html) && (
                <div className="lean-split__passage">
                  {passage.title && <p className="lean-split__title"><Title text={passage.title} /></p>}
                  {passage.html && <div className="lean-split__text manuscript" dangerouslySetInnerHTML={{ __html: passage.html }} />}
                </div>
              )}
            </div>
          )}
      </div>
    </section>
  );
}

function DeclName({ name }: { name: string }) {
  const own = usePhrases()?.titles[name]?.title;
  return own ? <Title text={own} /> : <DeclTitle name={name} />;
}
