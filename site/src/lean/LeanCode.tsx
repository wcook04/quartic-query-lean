// Lean source drawn line by line, every recognised name a link. Adapted from
// proof-reader web/src/lean/code.tsx at e2df888, Copyright 2026 proof-reader
// contributors, Apache-2.0.
import { useMemo, type CSSProperties } from "react";
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
}

export function LeanCode({ text, from = 1, links, self, onOpen, mark, spans, label }: Props) {
  const lines = useMemo(() => lineTokens(text.replace(/\s+$/, "")), [text]);
  return (
    <pre className="lean" aria-label={label ?? "Lean source"} tabIndex={0}>
      <code>
        {lines.map((pieces, i) => {
          const n = from + i;
          const marked = (!!mark && n >= mark[0] && n <= mark[1]) || !!spans?.some((sp) => sp.line === n);
          const lineSpans = spans?.filter((sp) => sp.line === n) ?? [];
          let col = 0;
          const indent = /^ */.exec(pieces.map((p) => p.text).join(""))?.[0].length ?? 0;
          return (
            <span key={i} className={`lean__line${marked ? " is-marked" : ""}`}>
              <span className="lean__no" aria-hidden="true">{n}</span>
              <span className="lean__text" style={{ "--indent": indent } as CSSProperties}>
                {pieces.map((p, j) => {
                  const start = col;
                  col += p.text.length;
                  const hit = lineSpans.find((sp) => sp.from < col && start < sp.to);
                  if (hit) {
                    // Split the token at the span's edges so exactly the recorded text is marked.
                    const a = Math.max(0, hit.from - start), b = Math.min(p.text.length, hit.to - start);
                    return (
                      <span key={j} className={`lk lk--${p.kind}`}>
                        {p.text.slice(0, a)}<mark className="lean__hit">{p.text.slice(a, b)}</mark>{p.text.slice(b)}
                      </span>
                    );
                  }
                  const typed = p.kind === "ident" && /^[A-Z]/.test(p.text);
                  const target = p.kind === "ident" ? links?.get(p.text) : undefined;
                  if (target && target !== self && onOpen)
                    return (
                      <button key={j} type="button" className={`lean__ref lk--${typed ? "type" : "ident"}`} title={target} onClick={() => onOpen(target)}>
                        {p.text}
                      </button>
                    );
                  if (p.kind === "space" || p.kind === "punct") return p.text;
                  return <span key={j} className={`lk lk--${typed ? "type" : p.kind}`}>{p.text}</span>;
                })}
              </span>
            </span>
          );
        })}
      </code>
    </pre>
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
