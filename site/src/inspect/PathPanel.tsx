// The helpers behind one arrow of the Lean graph, in order, from the edition's
// recorded dependency chains. Each hop says how Lean used the next declaration.
import { useState } from "react";
import { useAsync } from "../app/useAsync";
import type { Edition } from "../app/edition";
import { LeanCode } from "../lean/LeanCode";
import { Loaded, shortName } from "./common";
import { useNav } from "./Nav";

/** A title with `code` spans, as the edition writes them. */
function Title({ text }: { text: string }) {
  return <>{text.split("`").map((part, i) => (i % 2 ? <code key={i}>{part}</code> : part))}</>;
}

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
        <h2 id="pt-h" className="panel__title">How <code>{shortName(from).split(".").pop()}</code> reaches <code>{shortName(to).split(".").pop()}</code></h2>
        <p className="panel__where">
          The graph draws one arrow. Lean records the chain of declarations behind it. Each line says where the
          declaration above uses the one below.
        </p>
      </header>
      {variants.map((v: any) => (
        <section key={v.firstKind} className="chain">
          <h3>{VARIANT[v.firstKind] ?? v.firstKind} <span className="quiet">· {v.helperCount === 0 ? "a direct use" : `${v.helperCount} ${v.helperCount === 1 ? "helper" : "helpers"} not drawn on the graph`}</span></h3>
          <ol className="chain__list">
            <li><Step reader={reader} decl={p.declarations[from]} name={from} card /></li>
            {v.hops.map((h: any, i: number) => (
              <li key={i}>
                <p className="chain__usage">uses it {USAGE[h.usage] ?? h.usage}</p>
                <Step reader={reader} decl={p.declarations[h.to]} name={h.to} card={h.to === to} />
              </li>
            ))}
          </ol>
        </section>
      ))}
      <p className="quiet">These chains are Lean’s recorded dependencies between whole declarations. The exact line where each use happens needs the separate application evidence, shown in the walkthroughs.</p>
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
        <strong>{decl?.title ? <Title text={decl.title} /> : shortName(name)}</strong>{" "}
        <span className="quiet">{card ? "card on the graph" : "helper"}{decl?.kind ? `, ${decl.kind}` : ""}</span>
      </p>
      <p className="chain__raw"><code>{name}</code></p>
      <p className="chain__actions">
        {card ? (
          <button type="button" className="textbutton" onClick={() => nav.openLean(name)}>Open in Lean</button>
        ) : (
          <button type="button" className="textbutton" aria-expanded={!!src} onClick={show} disabled={state === "busy"}>
            {state === "failed" ? "Its Lean could not be loaded" : src ? "Hide its Lean" : state === "busy" ? "Loading…" : "Show its Lean"}
          </button>
        )}
      </p>
      {src?.text && <LeanCode text={src.text} from={src.lines?.[0] ?? 1} label={`Lean source of ${name}`} />}
      {src && !src.text && src.url && <p className="quiet">No separate excerpt is recorded for this name. <a href={src.url} target="_blank" rel="noopener noreferrer">Open its module</a></p>}
      {src?.url && src.text && <p className="quiet"><a href={src.url} target="_blank" rel="noopener noreferrer">Source on GitHub</a></p>}
    </div>
  );
}
