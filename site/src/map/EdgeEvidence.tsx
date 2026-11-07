// The evidence behind one line of the Lean graph, opened in place under the map.
// The use-site display adapts this site's PathPanel HopEvidence (site/src/inspect),
// which follows Proof Reader's path panel at e2df888 (Apache-2.0): the Lean lines
// come from the edition's use-site resource through reader.proofPath, and only
// recorded `sites` are highlighted. Absent evidence is said plainly.
import { useEffect, useRef, useState } from "react";
import type { ArgEdge, ArgGraph } from "../model/graph";
import { useAsync } from "../app/useAsync";
import { LeanCode } from "../lean/LeanCode";
import { Title } from "../text/title";
import type { ProofEdge } from "./fromProofMap";
import { helperWords, lineStyle, usePlace } from "./edgeMeaning";

/* eslint-disable @typescript-eslint/no-explicit-any */
type Reader = any;

const BASIS: Record<string, string> = {
  resolved_identifier: "named here",
  elaborated_application: "applied here",
  compiled_rhs: "compiled from this line",
  inherited_parameter: "parameter type",
  retained_tactic: "this tactic produced a proof using it",
  compiled_result: "in this result type",
  constructor_declaration: "constructor declared here",
};
const EXACT = new Set(["resolved_identifier", "elaborated_application", "compiled_rhs"]);

interface Props {
  reader: Reader;
  graph: ArgGraph;
  edge: ArgEdge;
  onClose(): void;
  onOpenChain(key: string): void;
  onOpenLean(name: string): void;
}

export function EdgeEvidence({ reader, graph, edge, onClose, onOpenChain, onOpenLean }: Props) {
  const e = edge as ProofEdge;
  const style = lineStyle(edge);
  const head = useRef<HTMLHeadingElement>(null);
  useEffect(() => { head.current?.focus({ preventScroll: true }); }, [edge.key]);
  const path = useAsync(async () => (style === "proof" || style === "statement" || style === "structure" ? reader.proofPath(edge.from, edge.to) : null), [reader, edge.key]);
  const name = (id: string) => graph.nodes.get(id)?.label ?? id;
  const title = (id: string) => graph.nodes.get(id)?.math ?? name(id);

  return (
    <section className="edge-ev" aria-labelledby="edge-ev-h" onKeyDown={(event) => { if (event.key === "Escape") { event.stopPropagation(); onClose(); } }}>
      <header className="edge-ev__head">
        <h3 id="edge-ev-h" ref={head} tabIndex={-1} className="edge-ev__title">
          <span className="edge-ev__from"><Title text={title(edge.from)} /></span>
          <span className="edge-ev__verb">{style === "context" ? "is placed above" : style === "paper" ? "is stated in Lean by" : "uses"}</span>
          <span className="edge-ev__to"><Title text={title(edge.to)} /></span>
        </h3>
        <button type="button" className="edge-ev__close" onClick={onClose} aria-label="Close the evidence for this line">×</button>
      </header>
      {style === "context" && (
        <p className="edge-ev__note">This line is context, not a Lean dependency. What uses this declaration lies outside the steps shown, so the map places it under the main result. Whole proof shows every recorded use.</p>
      )}
      {style === "paper" && (
        <p className="edge-ev__note">The editors link OpenAI’s Theorem 1.1 to the Lean theorem that states it. It is not a Lean dependency, so no Lean line is recorded for it. <button type="button" className="textbutton" onClick={() => onOpenLean(edge.to)}>Open its Lean</button></p>
      )}
      {path.state === "loading" && <p className="edge-ev__note" role="status">Loading the recorded evidence…</p>}
      {path.state === "failed" && <p className="edge-ev__note" role="alert">The evidence for this line could not be loaded.</p>}
      {path.state === "ready" && path.value && <Variants p={path.value} edge={e} graph={graph} reader={reader} name={name} />}
      {(style === "proof" || style === "statement" || style === "structure") && (
        <p className="edge-ev__actions">
          <button type="button" className="textbutton" onClick={() => onOpenChain(edge.key)}>Open the whole chain</button>
          <button type="button" className="textbutton" onClick={() => onOpenLean(edge.from)}>Open {short(name(edge.from))} in Lean</button>
        </p>
      )}
    </section>
  );
}

const short = (s: string) => (s.length > 42 ? `${s.slice(0, 40).replace(/\s+\S*$/, "")}…` : s);

function Variants({ p, edge, graph, reader, name }: { p: any; edge: ProofEdge; graph: ArgGraph; reader: Reader; name(id: string): string }) {
  if (p.status !== "current")
    return <p className="edge-ev__note">{p.status === "not_a_dependency_edge" ? "Lean records no dependency between these two declarations." : "This edition’s Lean graph is not current, so its evidence is not shown."}</p>;
  const order = edge.witnessKinds ?? [];
  const variants = [...p.variants].sort((a: any, b: any) => order.indexOf(a.firstKind) - order.indexOf(b.firstKind));
  const titleOf = (id: string) => p.declarations?.[id]?.title ?? graph.nodes.get(id)?.math ?? name(id);
  return (
    <>
      {variants.map((v: any) => (
        <div key={v.firstKind} className="edge-ev__variant">
          <p className="edge-ev__kind">
            <span className={`edge-ev__sample edge-ev__sample--${v.firstKind}`} aria-hidden="true" />
            Used {usePlace(graph, edge.from, v.firstKind)}, {helperWords(v.helperCount)}.
          </p>
          <ol className="edge-ev__hops">
            {v.hops.map((h: any, i: number) => (
              <li key={i}>
                <p className="edge-ev__hop">
                  {i === 0 ? "Where it uses " : <>Then <Title text={titleOf(h.from)} /> uses </>}
                  <strong><Title text={titleOf(h.to)} /></strong>
                  {h.to !== edge.to && <span className="quiet"> (helper{p.declarations?.[h.to]?.kind ? `, ${p.declarations[h.to].kind}` : ""})</span>}
                </p>
                <Site reader={reader} hop={h} initiallyOpen={i === 0} />
              </li>
            ))}
          </ol>
        </div>
      ))}
    </>
  );
}

/** One hop's recorded use site: the caller's Lean lines with the exact span marked. */
function Site({ reader, hop, initiallyOpen }: { reader: Reader; hop: any; initiallyOpen: boolean }) {
  const ev = hop.evidence ?? {};
  const sites: any[] = ev.sites ?? [];
  const [open, setOpen] = useState(initiallyOpen);
  const [pick, setPick] = useState(0);
  const [whole, setWhole] = useState(false);
  const site = sites[pick];
  const range: [number, number] | null = !open ? null : site
    ? site.basis === "inherited_parameter"
      ? [Math.max(1, site.lines[0] - 1), site.lines[1] + 1]
      : [Math.max(ev.declarationLines?.[0] ?? site.lines[0], site.lines[0] - 2), Math.min(ev.declarationLines?.[1] ?? site.lines[1], site.lines[1] + 2)]
    : whole ? ev.declarationLines ?? null : null;
  const text = useAsync(async () => (range && ev.source ? (await reader.readText(ev.source)).split("\n").slice(range[0] - 1, range[1]).join("\n") : null), [ev.source, range?.[0], range?.[1]]);
  if (!hop.evidence || ev.status === "unavailable_in_edition") return <p className="edge-ev__site quiet">This edition records no source locations for this use.</p>;
  if (ev.status === "stale_reference_index") return <p className="edge-ev__site quiet">This edition’s source locations are out of date, so none are shown.</p>;
  if (!site)
    return (
      <p className="edge-ev__site quiet">
        No single line is recorded; Lean records this use for the declaration as a whole.{" "}
        {ev.declarationLines && <button type="button" className="textbutton" onClick={() => setWhole(!whole)}>{whole ? "Hide the declaration" : "Show the declaration"}</button>}
        {whole && range && text.state === "ready" && text.value && <LeanCode text={text.value} from={range[0]} label="Lean declaration" />}
      </p>
    );
  const file = String(ev.source ?? "").split("/").pop();
  return (
    <div className="edge-ev__site">
      <p className="edge-ev__where">
        <span className={`tag${EXACT.has(site.basis) ? " tag--exact" : ""}`}>{BASIS[site.basis] ?? "located"}</span>{" "}
        <button type="button" className="textbutton" aria-expanded={open} onClick={() => setOpen(!open)}>
          {open ? "Hide" : "Show"} line {site.lines[0]}{site.lines[1] !== site.lines[0] ? `–${site.lines[1]}` : ""} of {file}
        </button>
        {sites.length > 1 && (
          <span className="hop__picks" role="group" aria-label="Choose a recorded use">
            {sites.map((x: any, i: number) => (
              <button key={i} type="button" aria-pressed={i === pick} onClick={() => { setPick(i); setOpen(true); }}>line {x.lines[0]}</button>
            ))}
          </span>
        )}
      </p>
      {range && text.state === "ready" && text.value && (
        <LeanCode text={text.value} from={range[0]}
          spans={site.lines[0] === site.lines[1] && site.utf16_columns ? [{ line: site.lines[0], from: site.utf16_columns[0], to: site.utf16_columns[1] }] : undefined}
          mark={site.lines[0] !== site.lines[1] ? site.lines : null}
          label={`Lean around line ${site.lines[0]}`} />
      )}
      {open && site.basis === "inherited_parameter" && site.binder && <p className="edge-ev__site quiet">Its binder is <code>{site.binder}</code>.</p>}
      {open && site.url && <p className="edge-ev__site"><a href={site.url} target="_blank" rel="noopener noreferrer">Line {site.lines[0]} on GitHub</a></p>}
    </div>
  );
}
