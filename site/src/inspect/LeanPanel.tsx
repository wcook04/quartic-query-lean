// One Lean declaration: its source, what Lean says it depends on, what uses it,
// and the paper passages that cite it. Edges are Lean's; paper links are editorial.
import { useMemo, useState } from "react";
import { useAsync } from "../app/useAsync";
import type { Edition } from "../app/edition";
import { LeanCode, nameLinks } from "../lean/LeanCode";
import { Axioms, RelationMark } from "./evidence";
import { statementName } from "../app/papers";
import { DeclTitle, Elsewhere, Loaded } from "./common";
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
    return { d: { ...d, kind }, linked: new Set(Object.keys(reverse)), cards, modules: graph.modules };
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
  return (
    <article className="panel panel--lean" aria-labelledby="ln-h">
      <header className="panel__head">
        <p className="panel__kind">{kindWord} in Lean{src.url && <> · <a href={src.url} target="_blank" rel="noopener noreferrer">source on GitHub</a></>}</p>
        <h2 id="ln-h" className="panel__title"><DeclTitle name={d.name} /></h2>
      </header>

      {ties.size > 0 && (
        <section className="tie" aria-label="Its place in the papers">
          {[...ties].map(([st, t]) => (
            <p key={st} className="tie__line">
              {t.review === "current" && t.relation !== "unassessed"
                ? <><RelationMark relation={t.relation} /> The Lean form of <strong>{statementName(st)}</strong>.</>
                : <>Linked by the editors to <strong>{statementName(st)}</strong>; no current review compares them.</>}{" "}
              <button type="button" className="textbutton" onClick={() => nav.openStatement(st)}>Compare with the paper</button>
            </p>
          ))}
        </section>
      )}

      <p className="cmp__actions"><button type="button" className="button button--small" onClick={() => nav.openGraph(d.name)}>Show it in the graph</button></p>

      {src.text ? (
        <section>
          <h3>What it says in Lean</h3>
          <LeanCode text={src.text} from={src.lines?.[0] ?? 1} links={links} self={d.name} onOpen={nav.openLean} label={`Lean source of ${d.name}`} />
        </section>
      ) : (
        <p className="ev quiet">No source text is recorded for this declaration.</p>
      )}

      <Neighbours title={isTheorem ? "What its proof relies on" : "What its definition relies on"} empty="Nothing else in this project." list={steps} linked={linked} mapped={cards} modules={modules} />
      {vocabulary.length > 0 && (
        <details className="more more--inline">
          <summary>{vocabulary.length} {vocabulary.length === 1 ? "definition" : "definitions"} its statement is written in</summary>
          <StatedWith list={vocabulary} />
        </details>
      )}
      <Neighbours title="What uses it" empty="No other declaration in this project uses it." list={users} linked={linked} mapped={cards} modules={modules} />

      {d.journeys?.length > 0 && (
        <section>
          <h3>Walk through the argument it belongs to</h3>
          <ul className="plain">
            {d.journeys.map((j: string) => (
              <li key={j}><button type="button" className="textbutton" onClick={() => nav.openJourney(j)}>{JOURNEY_NAMES[j] ?? j.replace(/-/g, " ")}</button></li>
            ))}
          </ul>
        </section>
      )}

      <section>
        <h3>Where the papers discuss it</h3>
        <Elsewhere rows={treatments} here="" />
        <p className="quiet">The editors made these links; Lean does not report them.</p>
      </section>

      <section>
        <h3>Axioms</h3>
        <Axioms audit={d.axiomAudit} />
      </section>
    </article>
  );
}

const JOURNEY_NAMES: Record<string, string> = {
  "forrelation-family": "How one family gives both query bounds",
  "capped-predictor": "Why naming the true cell reveals the whole address",
  "gaussian-transport": "How the Gaussian identity enters two estimates",
  "weighted-tournament": "Why weighted comparisons halve the candidates",
  "sign-blind-decoder": "Why the decoder needs an exact domain test",
};

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
      <h3>{title}</h3>
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
              {rest.length > 0 && outside > 0 && " · "}
              {outside > 0 && `${outside} ${outside === 1 ? "fact" : "facts"} from Mathlib and other libraries`}
            </p>
          )}
          {helpers && <ul className="nb__list nb__list--helpers">{rest.map((e) => <Item key={e.name} e={e} />)}</ul>}
        </>
      )}
    </section>
  );
}
