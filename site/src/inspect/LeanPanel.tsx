// One Lean declaration: its source, what Lean says it depends on, what uses it,
// and the paper passages that cite it. Edges are Lean's; paper links are editorial.
import { useMemo, useState } from "react";
import { useAsync } from "../app/useAsync";
import type { Edition } from "../app/edition";
import { LeanCode, nameLinks } from "../lean/LeanCode";
import { Axioms } from "./evidence";
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
  return (
    <article className="panel panel--lean" aria-labelledby="ln-h">
      <header className="panel__head">
        <h2 id="ln-h" className="panel__title"><DeclTitle name={d.name} /></h2>
        <p className="panel__where">
          {src.kind ? `${src.kind} in ` : "In "}<code>{src.module}</code>, lines {src.lines?.[0]}–{src.lines?.[1]}.{" "}
          {src.url && <a href={src.url} target="_blank" rel="noopener noreferrer">Source on GitHub</a>}
        </p>
      </header>

      <p className="cmp__actions"><button type="button" className="button button--small" onClick={() => nav.openGraph(d.name)}>Show it in the graph</button></p>
      <StatedWith list={uses.filter((e) => e.kind === "type" && Object.hasOwn(modules, e.name))} />
      <Neighbours title={d.kind === "theorem" || d.kind === "lemma" || /^(private |protected )?(theorem|lemma)\s/m.test(src.text ?? "") ? "Its proof uses" : "Its definition uses"} empty="Nothing else in this project." list={uses.filter((e) => e.kind !== "type")} linked={linked} mapped={cards} modules={modules} />
      <Neighbours title="Used by" empty="No other declaration in this project uses it." list={users} linked={linked} mapped={cards} modules={modules} />

      {src.text ? (
        <section>
          <h3>The Lean</h3>
          <LeanCode text={src.text} from={src.lines?.[0] ?? 1} links={links} self={d.name} onOpen={nav.openLean} label={`Lean source of ${d.name}`} />
        </section>
      ) : (
        <p className="ev ev--gap">No source text is recorded for this declaration.</p>
      )}

      <section>
        <h3>Axioms</h3>
        <Axioms audit={d.axiomAudit} />
      </section>

      {d.journeys?.length > 0 && (
        <section>
          <h3>How it is used in the argument</h3>
          <ul className="plain">
            {d.journeys.map((j: string) => (
              <li key={j}><button type="button" className="textbutton" onClick={() => nav.openJourney(j)}>Follow the “{j.replace(/-/g, " ")}” step by step</button></li>
            ))}
          </ul>
        </section>
      )}

      <section>
        <h3>Where the papers cite it</h3>
        <p className="quiet">These links were written by the editors, not reported by Lean.</p>
        <Elsewhere rows={treatments} here="" />
      </section>
    </article>
  );
}

/** The definitions a statement is written with: a compact row of names, not proof steps. */
function StatedWith({ list }: { list: Edge[] }) {
  const nav = useNav();
  if (!list.length) return null;
  return (
    <section className="nbs">
      <h3>Its statement is written with</h3>
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
