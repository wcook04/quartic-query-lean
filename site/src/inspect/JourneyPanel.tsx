// An authored path through the proof: each step says why a theorem is applied
// there, then shows the Lean line and the arguments Lean recorded.
import { useState } from "react";
import { useAsync } from "../app/useAsync";
import type { Edition } from "../app/edition";
import { LeanCode } from "../lean/LeanCode";
import { inlineTex } from "../text/html";
import { useEffect } from "react";
import { DeclButton, Elsewhere, Loaded, shortName } from "./common";
import { useNav } from "./Nav";

export function JourneyPanel({ edition, id, step }: { edition: Edition; id: string; step?: string }) {
  const j = useAsync(async () => {
    const path: any = await edition.reader.journey(id);
    // An occurrence is shown as "in these lines" only when its recorded byte
    // range lies inside the lines this step displays.
    const files = new Map<string, Uint8Array>();
    for (const s of path.steps) if (!files.has(s.source)) files.set(s.source, new Uint8Array(await edition.reader.readBytes(s.source)));
    for (const s of path.steps) {
      const bytes = files.get(s.source)!;
      let line = 1, start = -1, end = bytes.length;
      for (let i = 0; i < bytes.length; i++) {
        if (line === s.lines[0] && start < 0) start = i;
        if (bytes[i] === 10) { line++; if (line === s.lines[1] + 1) { end = i; break; } }
      }
      for (const u of s.uses) u.inExcerpt = (u.occurrences ?? []).filter((o: any) => o.utf8_bytes[0] >= start && o.utf8_bytes[1] <= end);
    }
    return path;
  }, [edition, id]);
  return <Loaded value={j} what="argument walkthrough">{(v) => <Journey j={v} step={step} />}</Loaded>;
}

function Journey({ j, step }: { j: any; step?: string }) {
  useEffect(() => {
    if (step) document.getElementById(`step-${step}`)?.scrollIntoView({ block: "start" });
  }, [step]);
  const nav = useNav();
  const rows = j.treatments.flatMap((t: any) => t.selections ?? []);
  return (
    <article className="panel panel--journey" aria-labelledby="jr-h">
      <header className="panel__head">
        <h2 id="jr-h" className="panel__title">{j.title}</h2>
        <p className="panel__lede" dangerouslySetInnerHTML={{ __html: inlineTex(j.scope) }} />
        <p className="quiet">The explanations are the editors’. The Lean lines, and the arguments shown beside them, are recorded from Lean.</p>
      </header>
      <ol className="steps">
        {j.steps.map((s: any, i: number) => <Step key={s.id} s={s} n={i + 1} current={s.id === step} />)}
      </ol>
      <section>
        <h3>Read this argument in a paper</h3>
        <Elsewhere rows={rows} here={nav.paper} />
      </section>
      {j.interfaces?.length > 0 && (
        <details className="more">
          <summary>The definitions this argument relies on</summary>
          {j.interfaces.map((f: any) => (
            <div key={f.name}>
              <h4><DeclButton name={f.name} /></h4>
              <LeanCode text={f.text} from={f.lines[0]} label={`Lean source of ${f.name}`} />
            </div>
          ))}
        </details>
      )}
    </article>
  );
}

function Step({ s, n, current }: { s: any; n: number; current: boolean }) {
  const [args, setArgs] = useState(false);
  const exact = s.uses.filter((u: any) => u.inExcerpt?.length);
  return (
    <li className={`step${current ? " is-current" : ""}`} id={`step-${s.id}`}>
      <h3 className="step__title"><span className="step__n">{n}</span> <span dangerouslySetInnerHTML={{ __html: inlineTex(s.title) }} /></h3>
      <p className="step__why" dangerouslySetInnerHTML={{ __html: inlineTex(s.mechanism) }} />
      <p className="quiet">In <DeclButton name={s.caller} />, lines {s.lines[0]}–{s.lines[1]}. <a href={s.url} target="_blank" rel="noopener noreferrer">Source on GitHub</a></p>
      <LeanCode text={s.text} from={s.lines[0]} label={`Lean lines ${s.lines[0]} to ${s.lines[1]} of ${s.caller}`} />
      <ul className="uses">
        {s.uses.map((u: any) => (
          <li key={u.declaration}>
            <DeclButton name={u.declaration} />{" "}
            <span className="quiet">
              {u.inExcerpt?.length
                ? `Lean matched ${u.inExcerpt.length === 1 ? "an application" : `${u.inExcerpt.length} applications`} of it to the source text in these lines.`
                : u.attribution === "exact_source_occurrence"
                  ? "Lean matched an application of it elsewhere in this declaration, outside these lines."
                  : "These lines name it, and Lean confirms the declaration uses it. No exact source occurrence was matched."}
            </span>
          </li>
        ))}
      </ul>
      {s.obligations?.length > 0 && (
        <div className="obligations">
          <h4>Where its hypotheses come from</h4>
          <ul>
            {s.obligations.map((o: any) => (
              <li key={o.callee + o.binder}>
                <code>{o.binder}</code> for <code>{shortName(o.callee).split(".").pop()}</code>: {o.explanation}
                {o.assembly && <> It is supplied later, at the step “{o.assembly.step.replace(/-/g, " ")}”, by <DeclButton name={o.assembly.provider} />.</>}
              </li>
            ))}
          </ul>
        </div>
      )}
      {exact.length > 0 && (
        <>
          <button type="button" className="disclose" aria-expanded={args} onClick={() => setArgs(!args)}>{args ? "Hide" : "Show"} the arguments Lean recorded</button>
          {args && exact.map((u: any) => u.inExcerpt.map((o: any, k: number) => (
            <table className="args" key={u.declaration + k}>
              <caption><code>{o.text}</code></caption>
              <tbody>
                {o.term.arguments.filter((a: any) => a.explicit).map((a: any, i: number) => (
                  <tr key={i}>
                    <th scope="row"><code>{a.binder}</code></th>
                    <td>{a.proof ? <>a proof of <code className="wrap">{a.type}</code></> : <code className="wrap">{a.argument}</code>}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )))}
        </>
      )}
    </li>
  );
}
