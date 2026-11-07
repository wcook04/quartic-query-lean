// The helpers behind one arrow of the Lean graph, in order, from the edition's
// recorded dependency chains. Each hop says how Lean used the next declaration, in
// plain words; what those words mean is folded, and Lean is named once at the end.
import { useState } from "react";
import { useAsync } from "../app/useAsync";
import type { Edition } from "../app/edition";
import { LeanCode } from "../lean/LeanCode";
import { Title } from "../text/title";
import { Loaded } from "./common";
import { SourceLine } from "./evidence";
import { useNav } from "./Nav";

const KIND_OF: Record<string, string> = { supports: "value", lean_type_dependency: "type", lean_structural_dependency: "structural" };
const USAGE: Record<string, string> = {
  proof: "in its proof", body: "in its definition", statement: "in its statement", structural_reference: "in its structure",
};
const VARIANT: Record<string, string> = { value: "Through proofs and definitions", type: "Through the statement", structural: "Through the structure" };

export function PathPanel({ edition, edge }: { edition: Edition; edge: string }) {
  const [from, to, linkKind] = edge.split("→");
  const kind = KIND_OF[linkKind];
  const path = useAsync(async () => {
    if (!kind) return { status: "not_a_dependency_edge" };
    return (edition.reader as any).proofPath(from, to);
  }, [edition, edge]);
  return <Loaded value={path} what="dependency path">{(p: any) => <Path p={p} from={from} to={to} kind={kind} reader={edition.reader} />}</Loaded>;
}

function Path({ p, from, to, kind, reader }: { p: any; from: string; to: string; kind?: string; reader: any }) {
  const nav = useNav();
  if (p.status !== "current") {
    return (
      <article className="panel">
        <h2 className="panel__title">This arrow</h2>
        <p>
          {p.status === "not_a_dependency_edge"
            ? "This arrow is the editors’ link from OpenAI’s theorem to the Lean theorem that states it. It is not a Lean dependency, so there is no chain of declarations behind it."
            : "This edition’s Lean graph is not current, so its dependency paths are not shown."}
        </p>
      </article>
    );
  }
  const variants = [...p.variants].sort((a: any, b: any) => Number(b.firstKind === kind) - Number(a.firstKind === kind));
  return (
    <article className="panel panel--path" aria-labelledby="pt-h">
      <header className="panel__head">
        <h2 id="pt-h" className="panel__title">How one step reaches another</h2>
        <p className="panel__where">The graph draws one arrow; Lean records the chain of declarations behind it, each using the next.</p>
        <details className="fold">
          <summary>What the words beside each use mean</summary>
          <ul className="plain marklist">
            <li><span className="usemark usemark--exact">named here</span> Lean resolves the name on the highlighted text.</li>
            <li><span className="usemark usemark--exact">compiled from this line</span> The line produces the use.</li>
            <li><span className="usemark">parameter type</span> It enters through a parameter declared earlier.</li>
            <li><span className="usemark">whole declaration</span> No single line was matched.</li>
          </ul>
        </details>
      </header>
      {variants.map((v: any) => (
        <section key={v.firstKind} className="chain">
          <h3>{VARIANT[v.firstKind] ?? v.firstKind}</h3>
          <p className="quiet chain__meta">
            {v.helperCount === 0 ? "A direct use." : `${v.helperCount} ${v.helperCount === 1 ? "helper" : "helpers"} not drawn on the graph.`}{" "}
            {v.locationCoverage && (v.locationCoverage.complete
              ? "Every step has its line in the Lean."
              : `${v.locationCoverage.located} of ${v.locationCoverage.total} steps have their line in the Lean.`)}
          </p>
          <ol className="chain__list">
            <li><Step reader={reader} decl={p.declarations[from]} name={from} card /></li>
            {v.hops.map((h: any, i: number) => (
              <li key={i}>
                <p className="chain__usage">uses it {USAGE[h.usage] ?? h.usage}</p>
                {h.evidence && <HopEvidence reader={reader} hop={h} />}
                <Step reader={reader} decl={p.declarations[h.to]} name={h.to} card={h.to === to} />
              </li>
            ))}
          </ol>
        </section>
      ))}
      <SourceLine kind="lean">These chains are Lean’s recorded dependencies between whole declarations. The exact line where each use happens needs the separate application evidence, shown in the walkthroughs.</SourceLine>
      <p className="cmp__actions">
        <button type="button" className="button button--small" onClick={() => nav.openGraph(from)}>Back to the graph</button>
      </p>
    </article>
  );
}

function Step({ reader, decl, name, card }: { reader: any; decl: any; name: string; card?: boolean }) {
  const nav = useNav();
  const [src, setSrc] = useState<any>(null);
  const [state, setState] = useState<"idle" | "busy" | "failed">("idle");
  async function show() {
    if (src) { setSrc(null); return; }
    setState("busy");
    try {
      setSrc(await reader.proofPathSource(name));
      setState("idle");
    } catch { setState("failed"); }
  }
  return (
    <div className={`chain__step${card ? " chain__step--card" : ""}`}>
      <p className="chain__name">
        <strong title={name} aria-label={decl?.title_plain ?? "Title unavailable"}><Title text={decl?.title ?? "Title unavailable"} /></strong>{" "}
        <span className="quiet">{card ? "card on the graph" : "helper"}{decl?.kind ? `, ${decl.kind}` : ""}</span>
      </p>
      <p className="chain__actions">
        {card ? (
          <button type="button" className="textbutton" onClick={() => nav.openLean(name)}>Open in Lean</button>
        ) : (
          <button type="button" className="textbutton" aria-expanded={!!src} onClick={show} disabled={state === "busy"}>
            {state === "failed" ? "Its Lean could not be loaded" : src ? "Hide its Lean" : state === "busy" ? "Loading…" : "Show its Lean"}
          </button>
        )}
      </p>
      {src?.text && <LeanCode text={src.text} from={src.lines?.[0] ?? 1} label={`Lean source of ${name}`} url={src.url} foldOver={14}
        caption={<span>{src.lines ? `Lean, lines ${src.lines[0]}–${src.lines[1]}` : "Lean source"}</span>} />}
      {src && !src.text && src.url && <p className="quiet">No separate excerpt is recorded for this name. <a href={src.url} target="_blank" rel="noopener noreferrer">Open its module</a></p>}
    </div>
  );
}

const BASIS: Record<string, string> = {
  resolved_identifier: "named here",
  elaborated_application: "applied here",
  compiled_rhs: "compiled from this line",
  inherited_parameter: "parameter type",
};

/** Where in the caller's Lean one hop's use happens, from the edition's evidence. */
function HopEvidence({ reader, hop }: { reader: any; hop: any }) {
  const ev = hop.evidence;
  const sites: any[] = ev.sites ?? [];
  const [pick, setPick] = useState(0);
  const [whole, setWhole] = useState(false);
  const site = sites[pick];
  const range: [number, number] | null = site
    ? site.basis === "inherited_parameter"
      ? [Math.max(1, site.lines[0] - 1), site.lines[1] + 1]
      : [Math.max(ev.declarationLines?.[0] ?? site.lines[0], site.lines[0] - 2), Math.min(ev.declarationLines?.[1] ?? site.lines[1], site.lines[1] + 2)]
    : whole ? ev.declarationLines ?? null : null;
  const text = useAsync(async () => (range && ev.source ? (await reader.readText(ev.source)).split("\n").slice(range[0] - 1, range[1]).join("\n") : null), [ev.source, range?.[0], range?.[1]]);
  if (ev.status === "stale_reference_index" || ev.status === "unavailable_in_edition")
    return <p className="hop__note">Source locations are not available in this edition.</p>;
  return (
    <div className="hop">
      {site ? (
        <p className="hop__note">
          <span className={`usemark${site.basis === "inherited_parameter" ? "" : " usemark--exact"}`}>{BASIS[site.basis] ?? "located"}</span>
          {site.basis === "inherited_parameter" && site.binder && <> Its binder is <code>{site.binder}</code>.</>}
          {sites.length > 1 && (
            <span className="hop__picks" role="group" aria-label="Choose a use">
              {" "}Uses:{sites.map((x: any, i: number) => (
                <button key={i} type="button" aria-pressed={i === pick} onClick={() => setPick(i)}>line {x.lines[0]}</button>
              ))}
            </span>
          )}
        </p>
      ) : (
        <p className="hop__note">
          <span className="usemark">whole declaration</span>{" "}
          {ev.declarationLines && <button type="button" className="textbutton" onClick={() => setWhole(!whole)}>{whole ? "Hide the declaration" : "Show the declaration"}</button>}
        </p>
      )}
      {range && text.state === "ready" && text.value && (
        <LeanCode text={text.value} from={range[0]}
          spans={site && site.lines[0] === site.lines[1] ? [{ line: site.lines[0], from: site.utf16_columns[0], to: site.utf16_columns[1] }] : undefined}
          mark={site && site.lines[0] !== site.lines[1] ? site.lines : null}
          label={`Lean around line ${site?.lines[0] ?? range[0]}`} url={site?.url}
          caption={<span>Lean, lines {range[0]}–{range[1]}</span>} />
      )}
      {site?.url && !(range && text.state === "ready" && text.value) && <p className="hop__src"><a href={site.url} target="_blank" rel="noopener noreferrer">Line {site.lines[0]} on GitHub</a></p>}
      {ev.parameterOrigins?.length > 0 && (
        <p className="hop__note">Parameter type: {ev.parameterOrigins.map((o: any, i: number) => (
          <span key={i}>{i ? ", " : ""}<a href={o.url} target="_blank" rel="noopener noreferrer">{o.binder ? <code>{o.binder}</code> : `line ${o.lines?.[0]}`}</a></span>
        ))}</p>
      )}
      {ev.otherReferences?.length > 0 && (
        <p className="hop__note quiet">Also named elsewhere in this declaration, not as this use: {ev.otherReferences.map((o: any, i: number) => (
          <span key={i}>{i ? ", " : ""}<a href={o.url} target="_blank" rel="noopener noreferrer">line {o.lines[0]}</a></span>
        ))}.</p>
      )}
    </div>
  );
}
