// The paper's sections, following the reading line. Rows come from the
// edition's manuscript `contents` (older editions: its outline).
import { Title } from "../text/title";

export interface ContentsRow { title: string; level: number; line: number; end_line: number; anchor?: string; listed?: boolean }

/** A section title with its number set apart, so the words lead and the number reads grey. */
export function NumberedTitle({ text }: { text: string }) {
  const m = /^((?:Appendix\s+)?(?:[A-Z]\.)?\d+(?:\.\d+)*\.?|Appendix\s+[A-Z]\.?)\s+(\S[\s\S]*)$/.exec(text);
  if (!m) return <Title text={text} />;
  return <><span className="secno">{m[1]}</span> <Title text={m[2]} /></>;
}

export function sectionAt(rows: ContentsRow[], line: number | null): ContentsRow | null {
  if (line == null) return null;
  let best: ContentsRow | null = null;
  for (const r of rows) if (r.line <= line && line <= r.end_line && (!best || r.level >= best.level)) best = r;
  return best;
}

export function Contents({ rows, current, onGo }: { rows: ContentsRow[]; current: ContentsRow | null; onGo(row: ContentsRow): void }) {
  const top = Math.min(...rows.map((r) => r.level));
  return (
    <nav className="contents" aria-label="Contents">
      <p className="contents__title">Contents</p>
      <ol>
        {rows.filter((r) => r.level <= top + 2).map((r) => (
          <li key={`${r.line}-${r.title}`} className={`contents__item contents__item--l${r.level - top}`}>
            <a href={r.anchor ? `#${r.anchor}` : undefined} aria-current={current === r || (current && current.line >= r.line && current.end_line <= r.end_line && r.level < current.level) ? "location" : undefined}
              className={current === r ? "is-here" : ""}
              onClick={(e) => { e.preventDefault(); onGo(r); }}>
              <NumberedTitle text={r.title} />
            </a>
          </li>
        ))}
      </ol>
    </nav>
  );
}

/** Older editions give an outline of start lines; close each range at the next heading of its level or higher. */
export function fromOutline(outline: { title: string; level: number; line: number }[], lines: number): ContentsRow[] {
  return outline.map((r, i) => {
    const next = outline.slice(i + 1).find((x) => x.level <= r.level);
    return { ...r, end_line: next ? next.line - 1 : lines, listed: true };
  });
}
