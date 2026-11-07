// Lean source drawn line by line, every recognised name a link. Adapted from
// proof-reader web/src/lean/code.tsx at e2df888, Copyright 2026 proof-reader
// contributors, Apache-2.0. The framed listing (caption bar, statement shown with
// the proof folded behind a count, copy and source actions) adapts Proof Reader's
// DeclBlock; continuation lines hang four characters under their own indent, as in
// lean-exposition site/src/lean/CodeView.tsx and lean.css (Apache-2.0).
import { useEffect, useMemo, useState, type CSSProperties, type ReactNode } from "react";
import { tokenizeLean } from "./leanTokens";

interface Piece { text: string; kind: string }

function lineTokens(text: string): Piece[][] {
  let inBlock = false;
  return text.split("\n").map((line) => {
    const pieces: Piece[] = [];
    let rest = line;
    while (rest) {
      if (inBlock) {
        const close = rest.indexOf("-/");
        const end = close < 0 ? rest.length : close + 2;
        pieces.push({ text: rest.slice(0, end), kind: "prose" });
        rest = rest.slice(end);
        if (close >= 0) inBlock = false;
        continue;
      }
      const block = rest.indexOf("/-");
      const dash = rest.indexOf("--");
      const start = block >= 0 && (dash < 0 || block < dash) ? block : dash;
      const code = start < 0 ? rest : rest.slice(0, start);
      if (code) for (const t of tokenizeLean(code)) pieces.push({ text: t.text, kind: t.kind });
      if (start < 0) break;
      rest = rest.slice(start);
      if (start === dash && (block < 0 || dash < block)) { pieces.push({ text: rest, kind: "comment" }); break; }
      inBlock = true;
      pieces.push({ text: rest.slice(0, 2), kind: "prose" });
      rest = rest.slice(2);
    }
    return pieces;
  });
}

const DECL = new Set(["theorem", "lemma", "def", "abbrev", "structure", "class", "instance", "example", "axiom"]);

/** Index (0-based) of the line holding the declaration's top-level `:=`, the last
 *  line of its statement; null when the source has no such separator. */
export function statementEndLine(text: string): number | null {
  const lines = lineTokens(text);
  let started = false;
  let depth = 0;
  for (let i = 0; i < lines.length; i++)
    for (const p of lines[i]) {
      if (p.kind === "comment" || p.kind === "prose") continue;
      if (!started) { if (p.kind === "keyword" && DECL.has(p.text)) started = true; continue; }
      if (p.kind === "bracket") depth += /[({[⦃⟨]/.test(p.text) ? 1 : -1;
      else if (depth <= 0 && p.kind === "arrow" && p.text === ":=") return i;
    }
  return null;
}

const WRAP_KEY = "quartic-lean-wrap";
function readWrap(): boolean {
  try { return localStorage.getItem(WRAP_KEY) !== "scroll"; } catch { return true; }
}
/** One wrap preference for every listing on the page. */
function useWrap(): [boolean, (v: boolean) => void] {
  const [wrap, setWrap] = useState(readWrap);
  useEffect(() => {
    const on = () => setWrap(readWrap());
    window.addEventListener("quartic-lean-wrap", on);
    return () => window.removeEventListener("quartic-lean-wrap", on);
  }, []);
  return [wrap, (v) => {
    try { localStorage.setItem(WRAP_KEY, v ? "wrap" : "scroll"); } catch { /* preference is a convenience */ }
    setWrap(v);
    window.dispatchEvent(new Event("quartic-lean-wrap"));
  }];
}

function CopyButton({ text, what }: { text: string; what: string }) {
  const [done, setDone] = useState(false);
  useEffect(() => {
    if (!done) return;
    const t = window.setTimeout(() => setDone(false), 1600);
    return () => window.clearTimeout(t);
  }, [done]);
  return (
    <button type="button" className="leancode__tool" onClick={() => void navigator.clipboard?.writeText(text).then(() => setDone(true), () => {})}>
      <span aria-live="polite">{done ? "Copied" : `Copy ${what}`}</span>
    </button>
  );
}

interface Props {
  text: string;
  /** Line number of the first line shown. */
  from?: number;
  /** Short or full names that open another declaration. */
  links?: ReadonlyMap<string, string>;
  self?: string;
  onOpen?: (fullName: string) => void;
  /** Lines to mark, numbered like `from`. */
  mark?: [number, number] | null;
  /** Exact spans to highlight: a line (numbered like `from`) and UTF-16 columns within it. */
  spans?: { line: number; from: number; to: number }[];
  label?: string;
  /** Caption at the left of the bar, e.g. the file and its lines. Without it the listing is drawn bare. */
  caption?: ReactNode;
  /** Source link for the caption bar. */
  url?: string;
  /** Fold the lines after the statement when the rest is longer than this. */
  foldOver?: number;
  /** What the folded part is called. */
  foldWord?: string;
  /** Extra content at the bottom of the frame. */
  foot?: ReactNode;
}

export function LeanCode({ text, from = 1, links, self, onOpen, mark, spans, label, caption, url, foldOver, foldWord = "proof", foot }: Props) {
  const source = useMemo(() => text.replace(/\s+$/, ""), [text]);
  const lines = useMemo(() => lineTokens(source), [source]);
  const [wrap, setWrap] = useWrap();
  const split = useMemo(() => (foldOver == null ? null : statementEndLine(source)), [source, foldOver]);
  const rest = split == null ? 0 : lines.length - split - 1;
  const foldable = foldOver != null && split != null && rest > foldOver;
  const markedLater = foldable && ((!!mark && mark[1] > from + split!) || !!spans?.some((sp) => sp.line > from + split!));
  const [open, setOpen] = useState(!foldable || markedLater);
  useEffect(() => setOpen(!foldable || markedLater), [source, foldable, markedLater]);
  const shown = foldable && !open ? lines.slice(0, split! + 1) : lines;

  const listing = (
    <pre className={`leancode__pre${wrap ? "" : " is-scroll"}`} aria-label={label ?? "Lean source"} tabIndex={0}>
      <code>
        {shown.map((pieces, i) => {
          const n = from + i;
          const marked = (!!mark && n >= mark[0] && n <= mark[1]) || !!spans?.some((sp) => sp.line === n);
          const lineSpans = spans?.filter((sp) => sp.line === n) ?? [];
          let col = 0;
          const indent = /^ */.exec(pieces.map((p) => p.text).join(""))?.[0].length ?? 0;
          const proof = split != null && i > split;
          return (
            <span key={i} className={`leancode__line${marked ? " is-marked" : ""}${proof ? " is-proof" : ""}`}>
              <span className="leancode__no" aria-hidden="true">{n}</span>
              <span className="leancode__text" style={{ "--indent": indent } as CSSProperties}>
                {pieces.map((p, j) => {
                  const start = col;
                  col += p.text.length;
                  const hit = lineSpans.find((sp) => sp.from < col && start < sp.to);
                  if (hit) {
                    // Split the token at the span's edges so exactly the recorded text is marked.
                    const a = Math.max(0, hit.from - start), b = Math.min(p.text.length, hit.to - start);
                    return (
                      <span key={j} className={`lk lk--${p.kind}`}>
                        {p.text.slice(0, a)}<mark className="leancode__hit">{p.text.slice(a, b)}</mark>{p.text.slice(b)}
                      </span>
                    );
                  }
                  const typed = p.kind === "ident" && /^[A-Z]/.test(p.text);
                  const target = p.kind === "ident" ? links?.get(p.text) : undefined;
                  if (target && target !== self && onOpen)
                    return (
                      <button key={j} type="button" className={`leancode__ref lk--${typed ? "type" : "ident"}`} title={`Open ${target}`} onClick={() => onOpen(target)}>
                        {p.text}
                      </button>
                    );
                  if (p.kind === "space" || p.kind === "punct") return p.text;
                  return <span key={j} className={`lk lk--${typed ? "type" : p.kind}`}>{p.text}</span>;
                })}
                {pieces.length === 0 && "​"}
              </span>
            </span>
          );
        })}
      </code>
    </pre>
  );

  const fold = foldable && (
    <button type="button" className="leancode__fold" aria-expanded={open} onClick={() => setOpen(!open)}>
      <span aria-hidden="true">{open ? "▾" : "▸"}</span>{" "}
      {open ? `Hide the ${foldWord}` : `Show the ${foldWord}`}, {rest} {rest === 1 ? "line" : "lines"}
      {!open && <span className="leancode__foldat"> (lines {from + split! + 1}–{from + lines.length - 1})</span>}
    </button>
  );

  if (caption == null) return <div className="leancode leancode--bare">{listing}</div>;
  return (
    <figure className="leancode">
      <figcaption className="leancode__bar">
        <span className="leancode__where">{caption}</span>
        <span className="leancode__tools">
          <button type="button" className="leancode__tool" aria-pressed={!wrap} onClick={() => setWrap(!wrap)} title={wrap ? "Keep each Lean line on one row and scroll sideways" : "Wrap long Lean lines under their indent"}>
            No wrap
          </button>
          <CopyButton text={source} what="source" />
          {url && <a className="leancode__tool" href={url} target="_blank" rel="noopener noreferrer">GitHub<span className="sr-only"> (opens in a new tab)</span></a>}
        </span>
      </figcaption>
      {listing}
      {fold}
      {foot}
    </figure>
  );
}

/** Map both short and qualified spellings of each name to the full name. */
/** Map each spelling to a full name only when exactly one recorded
 *  dependency has that spelling; an ambiguous short name stays plain text. */
export function nameLinks(names: Iterable<string>): Map<string, string> {
  const owners = new Map<string, Set<string>>();
  for (const full of names) {
    const parts = full.split(".");
    for (let i = 0; i < parts.length; i++) {
      const tail = parts.slice(i).join(".");
      if (!owners.has(tail)) owners.set(tail, new Set());
      owners.get(tail)!.add(full);
    }
  }
  const map = new Map<string, string>();
  for (const [tail, set] of owners) if (set.size === 1) map.set(tail, [...set][0]);
  return map;
}
