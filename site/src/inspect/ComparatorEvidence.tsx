import { useState } from "react";
import type { Edition } from "../app/edition";
import { useAsync } from "../app/useAsync";
import { LeanCode } from "../lean/LeanCode";
import { SourceLine } from "./evidence";

/* The recorded Comparator runs that checked the open declaration directly. Every fact shown
   comes from the edition's comparator-evidence.json and the files it names. */

type Entry = { run: string; target: string; link: "solution_applies" | "configured_name"; challenge_lines: [number, number]; solution_lines?: [number, number] };
type Control = { configuration: string; solution: string; receipt: string };
type Run = {
  name: string; challenge: string; solution: string; receipt: string; ran_at: string; toolchain: string;
  sandboxed: boolean; paranoid: boolean; permitted_axioms: string[]; rejected_controls: Control[];
};
type Index = { runs: Record<string, Run>; declarations: Record<string, Entry[]> };

const RESOURCE = "comparator-evidence.json";

async function loadIndex(edition: Edition): Promise<Index | null> {
  // Editions built before this record existed open without the panel.
  try { return await edition.reader.resource(RESOURCE); } catch { return null; }
}

export function ComparatorEvidence({ edition, declaration }: { edition: Edition; declaration: string }) {
  const index = useAsync(() => loadIndex(edition), [edition]);
  if (index.state !== "ready" || !index.value) return null;
  const entries = Object.hasOwn(index.value.declarations, declaration) ? index.value.declarations[declaration] : [];
  if (!entries.length) return null;
  return <EvidenceFold key={declaration} edition={edition} entries={entries} runs={index.value.runs} />;
}

function EvidenceFold({ edition, entries, runs }: { edition: Edition; entries: Entry[]; runs: Record<string, Run> }) {
  const [open, setOpen] = useState(false);
  return (
    <details className="fold comparator-evidence" onToggle={(event) => setOpen(event.currentTarget.open)}>
      <summary>
        <span className="comparator-evidence__label">Comparator evidence</span>
        <span className="comparator-evidence__state">Passed</span>
      </summary>
      {open && entries.map((entry) => <EvidenceRun key={entry.run + entry.target} edition={edition} entry={entry} run={runs[entry.run]} />)}
      {open && (
        <SourceLine kind="check">
          Comparator checks that the solution proves the challenge statement with only the permitted axioms. The match to the paper is a separate review.
        </SourceLine>
      )}
    </details>
  );
}

const day = new Intl.DateTimeFormat("en-GB", { dateStyle: "long", timeZone: "UTC" });

function EvidenceRun({ edition, entry, run }: { edition: Edition; entry: Entry; run: Run }) {
  const reader = edition.reader;
  const [first, last] = entry.challenge_lines;
  const text = useAsync(async () => (await reader.readText(run.challenge)).split("\n").slice(first - 1, last).join("\n"), [reader, run.challenge, first, last]);
  const url = (path: string, lines?: [number, number]) =>
    `https://github.com/wcook04/quartic-query-lean/blob/${reader.revision}/${path}${lines ? `#L${lines[0]}-L${lines[1]}` : ""}`;
  const mode = `Local run, ${run.sandboxed ? "sandboxed" : "unsandboxed"}, ${run.paranoid ? "with the external kernel checks" : "with Lean’s default kernel"}`;
  const controls = run.rejected_controls;
  return (
    <div className="comparator-evidence__run">
      <dl className="comparator-evidence__facts">
        <div><dt>Result</dt><dd><strong>Passed</strong> on {day.format(new Date(run.ran_at))}</dd></div>
        <div><dt>Run</dt><dd>{run.name}. {mode}</dd></div>
        <div><dt>Permitted axioms</dt><dd>{run.permitted_axioms.map((a, i) => <span key={a}>{i ? ", " : ""}<code>{a}</code></span>)}</dd></div>
      </dl>
      <p className="ev">
        {entry.link === "solution_applies"
          ? "Comparator accepted the paired solution against this separately compiled challenge statement. The solution proves it by applying the Lean theorem open here."
          : "Comparator accepted the paired solution’s proof of this theorem against the separately compiled challenge statement."}
      </p>
      {text.state === "ready" ? (
        <LeanCode text={text.value} from={first} url={url(run.challenge, entry.challenge_lines)}
          label={`Challenge statement for ${entry.target}`} caption={<span>Challenge statement</span>} />
      ) : (
        <p className="quiet">{text.state === "loading" ? "Opening the challenge statement…" : "The challenge statement could not be opened."}</p>
      )}
      <ul className="plain comparator-evidence__links">
        <li><a href={url(run.solution, entry.solution_lines)} target="_blank" rel="noreferrer">Solution</a></li>
        <li><a href={url(run.receipt)} target="_blank" rel="noreferrer">Run receipt</a></li>
        <li><a href={url(entry.run)} target="_blank" rel="noreferrer">Run configuration</a></li>
      </ul>
      {controls.length > 0 && (
        <p className="ev comparator-evidence__controls">
          Comparator rejected {controls.length === 1 ? "an altered solution" : `${controls.length} altered solutions`} for this challenge:{" "}
          {controls.map((c, i) => (
            <span key={c.configuration}>
              {i ? ", " : ""}
              <a href={url(c.solution)} target="_blank" rel="noreferrer">{c.solution.split("/").pop()!.replace(/\.lean$/, "")}</a>{" "}
              (<a href={url(c.receipt)} target="_blank" rel="noreferrer">receipt</a>)
            </span>
          ))}.
        </p>
      )}
    </div>
  );
}
