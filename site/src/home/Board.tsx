// The exposition's opening tables, as three separate questions. The edition
// supplies the boards, the distinguishing query, the sampling rule and the
// pointer example; this file only lets a reader try them.
import { useMemo, useState } from "react";
import { href } from "../app/router";

type Bits = number[][];
interface Sel { id: string }
export interface BoardData {
  scenes: [
    { id: "known-pair"; original: Bits; alternative: Bits; distinguishing_query: { row: number; column: number }; question: string; promise: string; query_cost: number; selections: Sel[] },
    { id: "hidden-zeros"; question: string; sampling: string; yes_certificate: string; no_certificate: string; fixed_row_strategy: { rows_read: number; queries_per_board: number; difference_seen: { numerator: number; denominator: number } }[]; selections: Sel[] },
    { id: "pointer-check"; question: string; candidate: number; rivals: number[]; correct_pointer_rows: number[]; correct_target_bits: number[]; altered_pointer_rows: number[]; altered_target_bits: number[]; rival_target_bits: number[]; comparison: string; conclusion: string; selections: Sel[] },
  ];
}

const read = (s: Sel[]) => href({ page: "read", paper: "exposition", s: s[0]?.id });

export function Board({ data }: { data: BoardData }) {
  const [scene, setScene] = useState(0);
  const names = ["One known difference", "Hidden zeros", "A pointer that lies"];
  return (
    <figure className="board">
      <div className="board__steps" role="tablist" aria-label="Three questions about the table">
        {names.map((n, i) => (
          <button key={n} role="tab" type="button" id={`scene-tab-${i}`} aria-selected={scene === i} aria-controls={`scene-${i}`}
            className="board__step" onClick={() => setScene(i)}
            onKeyDown={(e) => { if (e.key === "ArrowRight" || e.key === "ArrowLeft") { const n2 = (scene + (e.key === "ArrowRight" ? 1 : 2)) % 3; setScene(n2); document.getElementById(`scene-tab-${n2}`)?.focus(); } }}
            tabIndex={scene === i ? 0 : -1}>
            <span className="board__stepno">{i + 1}</span> {n}
          </button>
        ))}
      </div>
      <div role="tabpanel" id={`scene-${scene}`} aria-labelledby={`scene-tab-${scene}`}>
        {scene === 0 && <KnownPair s={data.scenes[0]} />}
        {scene === 1 && <HiddenZeros s={data.scenes[1]} />}
        {scene === 2 && <PointerCheck s={data.scenes[2]} />}
      </div>
    </figure>
  );
}

function Table({ bits, caption, open, onRead, mark, disabled, shade = 0 }: {
  bits: Bits; caption: string; open?: Set<string>; onRead?: (r: number, c: number) => void; mark?: { row: number; column: number } | null; disabled?: boolean; shade?: number;
}) {
  return (
    <table className="bits">
      <caption>{caption}</caption>
      <thead><tr><td /><th scope="col">1</th><th scope="col">2</th><th scope="col">3</th><th scope="col">4</th></tr></thead>
      <tbody>
        {bits.map((row, r) => (
          <tr key={r} className={r < shade ? "is-shaded" : undefined}>
            <th scope="row"><span className="bits__word">Row </span>{r + 1}</th>
            {row.map((bit, c) => {
              const key = `${r}-${c}`;
              const marked = mark && mark.row === r + 1 && mark.column === c + 1;
              if (!onRead) return <td key={c} className={`bit${bit === 0 ? " bit--zero" : ""}${marked ? " bit--mark" : ""}`}>{bit}</td>;
              const shown = open?.has(key);
              return (
                <td key={c} className={`bit${shown ? " is-open" : " is-covered"}${shown && bit === 0 ? " bit--zero" : ""}`}>
                  {shown ? bit : (
                    <button type="button" disabled={disabled} onClick={() => onRead(r, c)} aria-label={`Read row ${r + 1}, column ${c + 1}`} />
                  )}
                </td>
              );
            })}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

function KnownPair({ s }: { s: BoardData["scenes"][0] }) {
  const [which] = useState(() => (Math.random() < 0.5 ? "original" : "alternative"));
  const hidden = which === "original" ? s.original : s.alternative;
  const [open, setOpen] = useState<Set<string>>(new Set());
  const [last, setLast] = useState<[number, number] | null>(null);
  const q = s.distinguishing_query;
  const decided = open.has(`${q.row - 1}-${q.column - 1}`);
  return (
    <div className="scene">
      <p className="scene__q">{s.question}</p>
      <p className="scene__promise">You are told the covered table is one of the two printed tables. Read squares until you know which.</p>
      <div className="scene__tables">
        <Table bits={s.original} caption="Table A" />
        <Table bits={s.alternative} caption="Table B" />
        <Table bits={hidden} caption="Covered table" open={open} disabled={decided}
          onRead={(r, c) => { setOpen(new Set(open).add(`${r}-${c}`)); setLast([r, c]); }} />
      </div>
      <p className="scene__status" aria-live="polite">
        {decided ? (
          <>It is table {which === "original" ? "A" : "B"}. One query decides, as long as it is row {q.row}, column {q.column}: the only square where the two tables differ. {open.size > 1 && `You used ${open.size}.`}</>
        ) : last ? (
          <>Both tables have {s.original[last[0]][last[1]]} in row {last[0] + 1}, column {last[1] + 1}, so that read cannot tell them apart.</>
        ) : (
          <>Each square you read costs one query.</>
        )}
      </p>
      {decided && (
        <p className="scene__next">Knowing where two inputs differ makes the question cheap. The next question hides that square.</p>
      )}
      <p className="scene__read"><a href={read(s.selections)}>Read this in the general reader, Section 1 →</a></p>
    </div>
  );
}

function sample(): { zeroRow: number[]; erased: number | null } {
  const zeroRow = [0, 1, 2, 3].map(() => Math.floor(Math.random() * 4));
  return { zeroRow, erased: Math.random() < 0.5 ? Math.floor(Math.random() * 4) : null };
}

function HiddenZeros({ s }: { s: BoardData["scenes"][1] }) {
  const [game, setGame] = useState(sample);
  const [open, setOpen] = useState<Set<string>>(new Set());
  const [h, setH] = useState(1);
  const bits = useMemo(() => [0, 1, 2, 3].map((r) => [0, 1, 2, 3].map((c) => (game.zeroRow[c] === r && game.erased !== c ? 0 : 1))), [game]);
  const seen = (r: number, c: number) => open.has(`${r}-${c}`);
  const zeroIn = [0, 1, 2, 3].map((c) => [0, 1, 2, 3].some((r) => seen(r, c) && bits[r][c] === 0));
  const allOnes = [0, 1, 2, 3].findIndex((c) => [0, 1, 2, 3].every((r) => seen(r, c)) && [0, 1, 2, 3].every((r) => bits[r][c] === 1));
  const answer = allOnes >= 0 ? "yes" : zeroIn.every(Boolean) ? "no" : null;
  const row = s.fixed_row_strategy.find((x) => x.rows_read === h)!;
  return (
    <div className="scene">
      <p className="scene__q">{s.question}</p>
      <p className="scene__promise">Each column has one zero in a random row. Half the time one random column’s zero has been erased. Is there a column of ones?</p>
      <div className="scene__tables">
        <Table bits={bits} caption="Covered table" open={open} shade={h} disabled={!!answer} onRead={(r, c) => setOpen(new Set(open).add(`${r}-${c}`))} />
        <div className="scene__aside">
          <dl className="scene__certs">
            <dt>To prove yes</dt><dd>{s.yes_certificate}</dd>
            <dt>To prove no</dt><dd>{s.no_certificate}</dd>
          </dl>
          <p className="scene__status" aria-live="polite">
            {answer === "yes" && <>Yes, column {allOnes + 1}. You read {open.size} squares.</>}
            {answer === "no" && <>No: every column has a zero. You read {open.size} squares.</>}
            {!answer && (open.size === 0 ? <>Click a square to read it.</> : <>{open.size} {open.size === 1 ? "square" : "squares"} read.</>)}
          </p>
          {answer && <button type="button" className="scene__again" onClick={() => { setGame(sample()); setOpen(new Set()); }}>Cover a new table</button>}
          <div className="scene__fixed">
            <label htmlFor="rows-read">Or fix the reads in advance</label>
            <div className="scene__slider">
              <input id="rows-read" type="range" min={0} max={4} value={h} onChange={(e) => setH(Number(e.target.value))} />
              <output htmlFor="rows-read">top {h} {h === 1 ? "row" : "rows"}</output>
            </div>
            <p>
              {row.queries_per_board} queries, and the erased zero is seen with probability{" "}
              <strong>{row.difference_seen.numerator}/{row.difference_seen.denominator}</strong>. On an <em>m</em>-by-<em>m</em> table, <em>h</em> rows cost <em>mh</em> queries and succeed with probability <em>h</em>/<em>m</em>.
            </p>
          </div>
        </div>
      </div>
      <p className="scene__next">This shows what reading in a fixed pattern buys. It is not yet a lower bound: an adaptive algorithm chooses each square after seeing the earlier bits, and Section 5 handles that case.</p>
      <p className="scene__read"><a href={read(s.selections)}>Read this in the general reader, Section 1 →</a></p>
    </div>
  );
}

function PointerCheck({ s }: { s: BoardData["scenes"][2] }) {
  const [altered, setAltered] = useState(false);
  const rows = altered ? s.altered_pointer_rows : s.correct_pointer_rows;
  const bits = altered ? s.altered_target_bits : s.correct_target_bits;
  const valid = bits.every((b) => b === 0);
  return (
    <div className="scene">
      <p className="scene__q">{s.question}</p>
      <p className="scene__promise">
        Column {s.candidate} is all ones. Its certificate stores, for each other column, a row that should hold a zero.
      </p>
      <table className="pointers">
        <caption>Comparing column {s.candidate} with each rival</caption>
        <thead>
          <tr><th scope="col">Rival</th><th scope="col">Column {s.candidate} points to</th><th scope="col">Bit there</th><th scope="col">Rival’s pointer finds</th><th scope="col">Winner</th></tr>
        </thead>
        <tbody>
          {s.rivals.map((rival, i) => (
            <tr key={rival} className={bits[i] !== 0 ? "is-wrong" : ""}>
              <th scope="row">Column {rival}</th>
              <td>row {rows[i]}</td>
              <td className={bits[i] === 0 ? "is-zero" : "is-one"}>{bits[i]}</td>
              <td className={s.rival_target_bits[i] === 0 ? "is-zero" : "is-one"}>{s.rival_target_bits[i]}</td>
              <td>Column {s.candidate}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <p className="scene__toggle">
        <button type="button" aria-pressed={altered} onClick={() => setAltered(!altered)}>
          {altered ? "Restore the pointer" : `Move one pointer to row ${s.altered_pointer_rows[0]}`}
        </button>
        <span className="quiet">Column {s.candidate}’s pointer for column {s.rivals[0]}, from row {s.correct_pointer_rows[0]} to row {s.altered_pointer_rows[0]}.</span>
      </p>
      <p className="scene__status" aria-live="polite">
        {valid ? "Every stored row points to a zero. The certificate is valid and column 1 wins every comparison." : <>The pointer now finds a one, so the certificate is invalid. {s.conclusion}</>}
      </p>
      <p className="scene__next">{s.comparison} Comparisons can draw up a short list cheaply, but each candidate’s certificate must still be verified.</p>
      <p className="scene__read"><a href={read(s.selections)}>Read this in the general reader, Section 2 →</a></p>
    </div>
  );
}
