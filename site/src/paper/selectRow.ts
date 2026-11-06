export interface Row {
  id: string;
  lines?: [number, number];
  topic?: string;
  treatment?: string;
  statements?: string[];
  label?: string;
  location?: { page: number; destination?: string; url?: string };
}

/** Rows a reader can usefully select: topics, passages, claims and labels. */
export const meaningful = (r: Row) => !!(r.topic || r.statements?.length || r.label || /^(passage|claim)\//.test(r.id));

/** The most specific selection covering lines [a, b], or a free line range. */
export function rowFor(rows: Row[], a: number, b: number): string {
  const hits = rows.filter((r) => meaningful(r) && r.lines && r.lines[0] <= b && a <= r.lines[1]);
  const score = (r: Row) => (r.topic ? 0 : r.id.startsWith("claim/") ? 1 : 2) * 1e6 + (r.lines![1] - r.lines![0]);
  hits.sort((x, y) => score(x) - score(y));
  return hits[0]?.id ?? `l${a}-${b}`;
}

export function linesOf(rows: Row[], s: string | undefined): [number, number] | null {
  if (!s) return null;
  const m = /^l(\d+)-(\d+)$/.exec(s);
  if (m) return [Number(m[1]), Number(m[2])];
  return rows.find((r) => r.id === s)?.lines ?? null;
}
