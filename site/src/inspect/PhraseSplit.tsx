// The dock under the graph (docs/graph-pane.md): a clicked phrase's card with its Lean lines,
// else the subject's Lean, else a line saying no Lean is linked, scrolling on its own. The
// divider adapts the reader's paper/proof handle (app/ReaderSplit.tsx): pointer capture, a
// CSS share, a remembered size and keyboard resizing, here on the vertical axis.
import { useEffect, useLayoutEffect, useRef, useState } from "react";
import type { Edition } from "../app/edition";
import { LeanPanel } from "./LeanPanel";
import { usePhrases } from "../paper/phrases";
import { Title } from "../text/title";
import { CloseIcon } from "../app/icons";
import { DeclTitle } from "./common";
import { CardSummary } from "../map/CardSummary";

const KEY = "quartic:graph-dock:v1";
/** The graph's share of the pane; the dock under it takes 15% to 70%, about 30% at first. */
const DEFAULT = 0.7;
const MIN = 0.3;
const MAX = 0.85;

/** The draggable divider between the graph (above) and the dock (below). */
export function PhraseDivider() {
  const handle = useRef<HTMLDivElement>(null);
  const [share, setShare] = useState(() => {
    try { const n = Number(localStorage.getItem(KEY)); return n >= MIN && n <= MAX ? n : DEFAULT; } catch { return DEFAULT; }
  });
  const box = () => handle.current?.closest<HTMLElement>(".inspector__graph");
  function apply(value: number, save = true) {
    const height = box()?.clientHeight || window.innerHeight;
    const next = Math.max(Math.max(MIN, 200 / height), Math.min(Math.min(MAX, 1 - 90 / height), value));
    box()?.style.setProperty("--phrase-split", `${next * 100}%`);
    setShare(next);
    if (save) try { localStorage.setItem(KEY, String(next)); } catch { /* optional preference */ }
  }
  useLayoutEffect(() => {
    apply(share, false);
    const root = box();
    return () => { root?.style.removeProperty("--phrase-split"); };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  return (
    <div ref={handle} className="phrase-divider" role="separator" aria-orientation="horizontal"
      aria-label="Resize the graph and the part under it" aria-valuemin={MIN * 100} aria-valuemax={MAX * 100} aria-valuenow={Math.round(share * 100)}
      aria-valuetext={`${Math.round(share * 100)} percent for the graph`} tabIndex={0}
      title="Drag to resize the graph and the part under it. Arrow keys adjust it; double-click resets it."
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

/** The chosen phrase in the dock: its card and Lean, with the tied lines lit. */
export function PhraseSplit({ edition, id, name, onClose, onPick, onOpenLean }: { edition: Edition; id: string; name?: string; onClose(): void; onPick(name: string): void; onOpenLean(name: string): void }) {
  const layer = usePhrases();
  const phrase = layer?.byId.get(id);
  const declaration = name && phrase?.lean.some((r) => r.name === name) ? name : phrase?.lean[0]?.name;
  if (!layer || !phrase || !declaration) return null;
  const title = layer.titles[declaration];
  return (
    <section className="phrase-split" aria-label="The chosen phrase and its Lean">
      <header className="phrase-split__bar">
        <p className="phrase-split__k">Chosen phrase{title && phrase.lean.length === 1 && <> · <Title text={title.title} /></>}{phrase.lean.length > 1 && <> · {phrase.lean.length} declarations</>}</p>
        <button type="button" className="textbutton phrase-split__open" onClick={() => onOpenLean(declaration)}>Open its Lean</button>
        <button type="button" className="phrase-split__close" onClick={onClose} aria-label="Close the phrase and follow the paper" title="Close (Esc)">
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

/** The dock when no phrase is chosen: the subject's Lean (one tab per declaration), else a
 *  line saying that no Lean is linked to the paragraph, with the paragraph itself. */
export function LeanSplit({ edition, names, heading, passage, selectionStatements, onClose, onOpenLean }: {
  edition: Edition; names: string[]; heading: string;
  passage?: { title?: string; html?: string } | null; selectionStatements?: string[]; onClose?(): void; onOpenLean(name: string): void;
}) {
  const [pick, setPick] = useState(0);
  const key = names.join("|");
  useEffect(() => setPick(0), [key]);
  const name = names[Math.min(pick, names.length - 1)];
  return (
    <section className="phrase-split lean-split" aria-label={heading}>
      {(selectionStatements === undefined || !name) && <header className="phrase-split__bar">
        <p className="phrase-split__k">{heading}</p>
        {name && <button type="button" className="textbutton phrase-split__open" onClick={() => onOpenLean(name)}>Open its Lean</button>}
        {onClose && (
          <button type="button" className="phrase-split__close" onClick={onClose} aria-label="Close and follow the paper" title="Close (Esc)">
            <CloseIcon />
          </button>
        )}
      </header>}
      {names.length > 1 && (
        <div className="phrase-split__tabs" role="tablist" aria-label="Declarations linked to this paragraph">
          {names.map((n, i) => (
            <button key={n} type="button" role="tab" aria-selected={i === pick} onClick={() => setPick(i)}><DeclName name={n} /></button>
          ))}
        </div>
      )}
      <div className="phrase-split__body">
        {name ? <LeanPanel key={name} edition={edition} name={name} forStep selectionStatements={selectionStatements} compact={selectionStatements !== undefined} />
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

/** The dock while a card is under the pointer or holds the keyboard focus: a preview of it. */
export function CardPreview({ edition, name, title, kind, onOpenLean }: { edition: Edition; name: string; title: string; kind: string; onOpenLean(name: string): void }) {
  return (
    <section className="phrase-split card-preview" aria-label="The card under the pointer">
      <header className="phrase-split__bar">
        <p className="phrase-split__k">{kind} · <Title text={title} /></p>
        <button type="button" className="textbutton phrase-split__open" onClick={() => onOpenLean(name)}>Open its Lean</button>
      </header>
      <div className="phrase-split__body">
        <CardSummary reader={edition.reader} name={name} title={title} />
      </div>
    </section>
  );
}

function DeclName({ name }: { name: string }) {
  const own = usePhrases()?.titles[name]?.title;
  return own ? <Title text={own} /> : <DeclTitle name={name} />;
}
