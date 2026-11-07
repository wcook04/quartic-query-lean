// One Lean declaration: its source, what Lean says it depends on, what uses it,
// and the paper passages that cite it. Edges are Lean's; paper links are editorial.
import { useEffect, useMemo, useState } from "react";
import { useAsync } from "../app/useAsync";
import type { Edition } from "../app/edition";
import { LeanCode, nameLinks } from "../lean/LeanCode";
import { Axioms, RelationMark, Who } from "./evidence";
import { DeclTitle, Elsewhere, journeyName, Loaded, StatementLabel } from "./common";
import { useNav } from "./Nav";

const KIND_WORD: Record<string, string> = { value: "proof or body", type: "statement", structural: "structure" };

interface Edge { name: string; kind: string }

function edges(node: any, side: "uses" | "used_by"): Edge[] {
  const from = side === "uses" ? node : node?.incoming ?? {};
  const out: Edge[] = [];
  const seen = new Set<string>();
  for (const kind of ["type", "value", "structural"])
    for (const name of from?.[kind] ?? []) if (!seen.has(name) && name !== node.name) { seen.add(name); out.push({ name, kind }); }
  return out;
}

export function LeanPanel({ edition, name }: { edition: Edition; name: string }) {
  const data = useAsync(async () => {
    const [d, reverse, map, graph] = await Promise.all([edition.reader.fromDeclaration(name), edition.reader.resource("selection/reverse.json"),
      edition.reader.proofMap().catch(() => null), edition.reader.resource("selection/index.json")]);
    const cards = new Set<string>();
    let kind: string | null = null;
    if (map?.currentness === "current") {
      for (const n of Object.keys(map.cards)) cards.add(n);
      kind = map.cards[name]?.kind ?? null;
    }
    if (!kind && (map as any)?.currentness === "current") {
      const path = await (edition.reader as any).proofPathSource?.(name).catch(() => null);
      kind = path?.kind ?? null;
    }
    const statements = [...new Set<string>((d.treatments ?? []).filter((t: any) => t.statement && t.review === "current" && t.relation === "partial").map((t: any) => t.statement))];
    const notes = Object.fromEntries(await Promise.all(statements.map(async (id) => {
      const review: any = await edition.reader.statementReview(id).catch(() => null);
      return [id, review?.comparisons?.find((c: any) => c.declaration === name)?.note];
    })));
    return { d: { ...d, kind, notes }, linked: new Set(Object.keys(reverse)), cards, modules: graph.modules };
  }, [edition, name]);
  return <Loaded value={data} what="Lean declaration">{({ d, linked, cards, modules }) => <Declaration d={d} linked={linked} cards={cards} modules={modules} />}</Loaded>;
}

function Declaration({ d, linked, cards, modules }: { d: any; linked: Set<string>; cards: Set<string>; modules: Record<string, string> }) {
  const nav = useNav();
  const src = d.source ?? {};
  const uses = useMemo(() => edges(src, "uses"), [src]);
  const users = useMemo(() => edges(src, "used_by"), [src]);
  const links = useMemo(() => nameLinks([...uses.map((e) => e.name), ...users.map((e) => e.name)]), [uses, users]);

  if (src.status === "external_module_boundary" || src.status === "outside_recorded_graph") {
    return (
      <article className="panel">
        <h2 className="panel__title">{src.status === "external_module_boundary" ? "External package reference" : <DeclTitle name={d.name} />}</h2>
        <p>
          {src.status === "external_module_boundary"
            ? <>This declaration comes from the library module <code>{src.module}</code>, outside the Quartic project. The recorded graph stops here.</>
            : <>This name is not in the recorded Lean graph of this edition.</>}
        </p>
        {src.url && <p><a href={src.url} target="_blank" rel="noopener noreferrer">Read it in its library</a></p>}
      </article>
    );
  }

  const treatments = (d.treatments ?? []).map((t: any) => ({ paper: t.paper, id: t.selection }));
  // The paper statements this declaration is tied to, each with its review, once.
  const ties = new Map<string, { relation: string; review?: string }>();
  for (const t of d.treatments ?? []) {
    if (!t.statement) continue;
    const prev = ties.get(t.statement);
    if (!prev || (prev.review !== "current" && t.review === "current")) ties.set(t.statement, { relation: t.relation, review: t.review });
  }
  const isTheorem = d.kind === "theorem" || d.kind === "lemma" || /^(private |protected )?(theorem|lemma)\s/m.test(src.text ?? "");
  const kindWord = isTheorem ? "Theorem" : d.kind === "structure" || d.kind === "inductive" ? "Type" : "Definition";
  const steps = uses.filter((e) => e.kind !== "type");
  const vocabulary = uses.filter((e) => e.kind === "type" && Object.hasOwn(modules, e.name));
  const file = (src.source ?? "").replace(/^lean\//, "");
  const range = src.lines ? (src.lines[0] === src.lines[1] ? `line ${src.lines[0]}` : `lines ${src.lines[0]}–${src.lines[1]}`) : "";
  const reviewed = [...ties].filter(([, t]) => t.review === "current" && t.relation !== "unassessed");
  const linkedOnly = [...ties].filter(([, t]) => !(t.review === "current" && t.relation !== "unassessed"));
  const statementButton = (st: string) => <button type="button" className="textbutton" onClick={() => nav.openStatement(st)}><StatementLabel id={st} /></button>;
  return (
    <article className="panel panel--lean" aria-labelledby="ln-h">
      <header className="panel__head decl-head">
        <p className="panel__kind">{kindWord} in Lean</p>
        <h2 id="ln-h" className="panel__title decl-head__title"><DeclTitle name={d.name} /></h2>
        <p className="decl-head__raw">
          <code>{d.name}</code>
          <CopyName name={d.name} />
          <button type="button" className="decl-head__act" onClick={() => nav.openGraph(d.name)}>Show in graph</button>
        </p>
      </header>

      {src.text ? (
        <LeanCode text={src.text} from={src.lines?.[0] ?? 1} links={links} self={d.name} onOpen={nav.openLean}
          label={`Lean source of ${d.name}`} url={src.url} foldOver={14} foldWord={isTheorem ? "proof" : "definition body"}
          caption={<><span className="leancode__file">{file || "Lean source"}</span>{range && <span>{range}</span>}</>} />
      ) : (
        <p className="panel-empty">No source text is recorded for this declaration.</p>
      )}

      {ties.size > 0 && (
        <section className="block tie" aria-labelledby="ln-tie">
          <h3 id="ln-tie" className="block__h">Compared with the papers{reviewed.length > 0 && <Who kind="review" />}</h3>
          {reviewed.map(([st, t]) => (
            <div key={st} className="tie__item">
              <p className="tie__line"><RelationMark relation={t.relation} /> <span className="tie__vs">against</span> {statementButton(st)}</p>
              {t.relation === "partial" && <p className="tie__note">{d.notes[st] ?? "This declaration covers only part of the statement. Open the comparison for the reviewed scope."}</p>}
            </div>
          ))}
          {linkedOnly.length > 0 && (
            <div className="tie__item">
              <p className="tie__line tie__line--linked"><Who kind="editors" /> Linked to {linkedOnly.length === 1 ? "this statement" : "these statements"}; no current review compares {linkedOnly.length === 1 ? "the two" : "it with them"}.</p>
              <ul className="plain tie__list">{linkedOnly.map(([st]) => <li key={st}>{statementButton(st)}</li>)}</ul>
            </div>
          )}
        </section>
      )}

      <section className="block" aria-labelledby="ln-lean">
        <h3 id="ln-lean" className="block__h">Dependencies <Who kind="lean" /></h3>
        <Neighbours title={isTheorem ? "Its proof relies on" : "Its definition relies on"} empty="Nothing else in this project." list={steps} linked={linked} mapped={cards} modules={modules} />
        {vocabulary.length > 0 && (
          <details className="more more--inline">
            <summary>{vocabulary.length} {vocabulary.length === 1 ? "definition" : "definitions"} its statement is written in</summary>
            <StatedWith list={vocabulary} />
          </details>
        )}
        <Neighbours title="Used by" empty="No other declaration in this project uses it." list={users} linked={linked} mapped={cards} modules={modules} />
        <div className="nbs">
          <h4 className="nbs__h">Axioms</h4>
          <Axioms audit={d.axiomAudit} />
        </div>
      </section>

      <section className="block" aria-labelledby="ln-papers">
        <h3 id="ln-papers" className="block__h">In the papers <Who kind="editors" /></h3>
        <Elsewhere rows={treatments} here="" current={nav.paper} />
        {d.journeys?.length > 0 && (
          <ul className="plain journeys">
            {d.journeys.map((j: string) => (
              <li key={j}><button type="button" className="journey-link" onClick={() => nav.openJourney(j)}><span className="journey-link__k">Walkthrough</span> {journeyName(j)}</button></li>
            ))}
          </ul>
        )}
      </section>
    </article>
  );
}

/** Adapted from Proof Reader's CopyName (web/src/proof/DeclBlock.tsx at e2df888, Apache-2.0). */
function CopyName({ name }: { name: string }) {
  const [copied, setCopied] = useState(false);
  useEffect(() => {
    if (!copied) return;
    const timer = window.setTimeout(() => setCopied(false), 1600);
    return () => window.clearTimeout(timer);
  }, [copied]);
  return (
    <button type="button" className="decl-head__act" onClick={() => void navigator.clipboard?.writeText(name).then(() => setCopied(true), () => {})}>
      <span aria-live="polite">{copied ? "Copied" : "Copy name"}</span>
    </button>
  );
}

function StatedWith({ list }: { list: Edge[] }) {
  const nav = useNav();
  if (!list.length) return null;
  return (
    <section className="nbs">
      <p className="chips">
        {list.map((e) => (
          <button key={e.name} type="button" className="chip" onClick={() => nav.openLean(e.name)} title={e.name}>
            <DeclTitle name={e.name} />
          </button>
        ))}
      </p>
    </section>
  );
}

/** What a declaration builds on, or what builds on it: paper-linked cards first, by their
 *  plain titles; helper lemmas and library facts folded into counts the reader can open. */
function Neighbours({ title, empty, list, linked, mapped, modules }: { title: string; empty: string; list: Edge[]; linked: Set<string>; mapped: Set<string>; modules: Record<string, string> }) {
  const nav = useNav();
  const [helpers, setHelpers] = useState(false);
  const project = list.filter((e) => Object.hasOwn(modules, e.name));
  const cards = project.filter((e) => mapped.has(e.name) || linked.has(e.name));
  const rest = project.filter((e) => !cards.includes(e));
  const outside = list.length - project.length;
  const Item = ({ e }: { e: Edge }) => (
    <li>
      <button type="button" className="nb" onClick={() => nav.openLean(e.name)} title={e.name}>
        <span className="nb__title"><DeclTitle name={e.name} /></span>
      </button>
    </li>
  );
  return (
    <section className="nbs">
      <h4 className="nbs__h">{title}{list.length > 0 && <span className="nbs__n">{list.length}</span>}</h4>
      {list.length === 0 ? <p className="quiet">{empty}</p> : (
        <>
          {cards.length > 0 && <ul className="nb__list">{cards.map((e) => <Item key={e.name} e={e} />)}</ul>}
          {(rest.length > 0 || outside > 0) && (
            <p className="quiet nb__more">
              {rest.length > 0 && (
                <button type="button" className="textbutton" aria-expanded={helpers} onClick={() => setHelpers(!helpers)}>
                  {helpers ? "Hide" : "Show"} {rest.length} helper {rest.length === 1 ? "lemma" : "lemmas"}
                </button>
              )}
              {rest.length > 0 && outside > 0 && <span aria-hidden="true"> · </span>}
              {outside > 0 && <span>{outside} {outside === 1 ? "fact" : "facts"} from Mathlib and other libraries</span>}
            </p>
          )}
          {helpers && <ul className="nb__list nb__list--helpers">{rest.map((e) => <Item key={e.name} e={e} />)}</ul>}
        </>
      )}
    </section>
  );
}
