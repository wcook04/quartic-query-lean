// One Lean declaration, answering "the Lean for this step": its name, one line saying
// how it matches the paper, its source, then what it uses and what uses it. Edges are
// Lean's; matches are reviews; paper links are editorial. Rarer facts (axioms, every
// paper passage citing it) are folded at the end.
import { useEffect, useMemo, useState } from "react";
import { useAsync } from "../app/useAsync";
import type { Edition } from "../app/edition";
import { LeanCode, nameLinks } from "../lean/LeanCode";
import { Axioms, axiomSummary, RelationMark, reviewWords, SourceLine } from "./evidence";
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

export function LeanPanel({ edition, name, forStep = false }: { edition: Edition; name: string; forStep?: boolean }) {
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
    const statements = [...new Set<string>((d.treatments ?? []).filter((t: any) => t.statement && t.review === "current").map((t: any) => t.statement))];
    const reviews = await Promise.all(statements.map(async (id) => {
      const review: any = await edition.reader.statementReview(id).catch(() => null);
      return [id, review?.comparisons?.find((c: any) => c.declaration === name)] as const;
    }));
    const notes = Object.fromEntries(reviews.map(([id, c]) => [id, c?.note]));
    const by = reviews.map(([, c]) => c?.reviewed_by);
    return { d: { ...d, kind, notes, by }, linked: new Set(Object.keys(reverse)), cards, modules: graph.modules };
  }, [edition, name]);
  return <Loaded value={data} what="Lean declaration">{({ d, linked, cards, modules }) => <Declaration d={d} linked={linked} cards={cards} modules={modules} forStep={forStep} />}</Loaded>;
}

function Declaration({ d, linked, cards, modules, forStep }: { d: any; linked: Set<string>; cards: Set<string>; modules: Record<string, string>; forStep: boolean }) {
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
  const statementButton = (st: string) => <button type="button" className="textbutton match__st" onClick={() => nav.openStatement(st)}><StatementLabel id={st} /></button>;
  const places = new Set(treatments.map((t: any) => t.paper).filter((p: string) => ["expert", "exposition", "reconstruction", "original"].includes(p))).size;
  return (
    <article className="panel panel--lean" aria-labelledby="ln-h">
      <header className="panel__head decl-head">
        <p className="panel__kind">{forStep ? <>The Lean for this step <span className="panel__kindsep">·</span> {kindWord.toLowerCase()}</> : `${kindWord} in Lean`}</p>
        <h2 id="ln-h" className="panel__title decl-head__title"><DeclTitle name={d.name} /></h2>
        <p className="decl-head__raw">
          <code>{d.name}</code>
          <CopyName name={d.name} />
          <button type="button" className="decl-head__act" onClick={() => nav.openGraph(d.name)}>Show in graph</button>
        </p>
      </header>

      {ties.size > 0 && (
        <section className="block match match--lead" aria-labelledby="ln-tie">
          <h3 id="ln-tie" className="sr-only">How it matches the paper</h3>
          {reviewed.map(([st, t]) => (
            <div key={st} className="match__item">
              <p className="match__line"><span className="match__k">Matches the paper</span> <RelationMark relation={t.relation} /> <span className="match__vs">against</span> {statementButton(st)}</p>
              {t.relation === "partial" && <p className="match__note">{d.notes[st] ?? "This declaration covers only part of the statement. Open the comparison for the reviewed scope."}</p>}
            </div>
          ))}
          {linkedOnly.length > 0 && (
            <div className="match__item">
              <p className="match__line"><span className="match__k">Linked to the paper</span> {linkedOnly.map(([st], i) => <span key={st}>{i ? ", " : ""}{statementButton(st)}</span>)}</p>
              <p className="match__note match__note--plain">No current review compares {linkedOnly.length === 1 ? "the two" : "it with them"}.</p>
            </div>
          )}
          <SourceLine kind={reviewed.length ? "review" : "editors"} by={d.by}>
            {reviewed.length > 0 && <>Compared by {reviewWords(d.by)}, bound to this Lean source.</>}
            {reviewed.length > 0 && linkedOnly.length > 0 && " "}
            {linkedOnly.length > 0 && <>{reviewed.length ? "Other statement links" : "Linked"} by the editors.</>}
          </SourceLine>
        </section>
      )}

      {src.text ? (
        <LeanCode text={src.text} from={src.lines?.[0] ?? 1} links={links} self={d.name} onOpen={nav.openLean}
          label={`Lean source of ${d.name}`} url={src.url} foldOver={14} foldWord={isTheorem ? "proof" : "definition body"}
          caption={<><span className="leancode__file">{file || "Lean source"}</span>{range && <span>{range}</span>}</>} />
      ) : (
        <p className="panel-empty">No source text is recorded for this declaration.</p>
      )}

      <section className="block" aria-labelledby="ln-uses">
        <h3 id="ln-uses" className="block__h">Uses</h3>
        <Neighbours empty="Nothing else in this project." list={steps} vocabulary={vocabulary} linked={linked} mapped={cards} modules={modules} />
        <h3 className="block__h block__h--next">Used by</h3>
        <Neighbours empty="No other declaration in this project uses it." list={users} linked={linked} mapped={cards} modules={modules} />
        <SourceLine kind="lean">From Lean’s record of this source.</SourceLine>
      </section>

      <section className="block block--quiet" aria-label="More about this declaration">
        {d.journeys?.length > 0 && (
          <ul className="plain linklist">
            {d.journeys.map((j: string) => (
              <li key={j}><span className="linklist__k">Walkthrough</span> <button type="button" className="textbutton" onClick={() => nav.openJourney(j)}>{journeyName(j)}</button></li>
            ))}
          </ul>
        )}
        {treatments.length > 0 && (
          <details className="fold">
            <summary>Where the papers discuss it {places > 0 && <span className="fold__n">{places} {places === 1 ? "paper" : "papers"}</span>}</summary>
            <Elsewhere rows={treatments} here="" current={nav.paper} />
            <SourceLine kind="editors">Passages linked by the editors.</SourceLine>
          </details>
        )}
        <details className="fold">
          <summary>{axiomSummary(d.axiomAudit)}</summary>
          <Axioms audit={d.axiomAudit} />
        </details>
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

/** What a declaration builds on, or what builds on it: paper-linked results by their
 *  plain titles; helper lemmas, statement vocabulary and library facts summarised in
 *  one quiet line, each openable. */
function Neighbours({ empty, list, vocabulary = [], linked, mapped, modules }: { empty: string; list: Edge[]; vocabulary?: Edge[]; linked: Set<string>; mapped: Set<string>; modules: Record<string, string> }) {
  const nav = useNav();
  const [open, setOpen] = useState<"helpers" | "vocabulary" | null>(null);
  const project = list.filter((e) => Object.hasOwn(modules, e.name));
  const cards = project.filter((e) => mapped.has(e.name) || linked.has(e.name));
  const rest = project.filter((e) => !cards.includes(e));
  const outside = list.length - project.length;
  const Item = ({ e }: { e: Edge }) => (
    <li><button type="button" className="declink" onClick={() => nav.openLean(e.name)} title={e.name}><DeclTitle name={e.name} /></button></li>
  );
  const toggle = (which: "helpers" | "vocabulary", n: number, one: string, many: string) => (
    <button type="button" className="textbutton" aria-expanded={open === which} onClick={() => setOpen(open === which ? null : which)}>{n} {n === 1 ? one : many}</button>
  );
  const parts = [
    rest.length > 0 && toggle("helpers", rest.length, "helper lemma", "helper lemmas"),
    vocabulary.length > 0 && toggle("vocabulary", vocabulary.length, "definition in its statement", "definitions in its statement"),
    outside > 0 && <span>{outside} library {outside === 1 ? "fact" : "facts"}</span>,
  ].filter(Boolean);
  if (list.length === 0 && vocabulary.length === 0) return <p className="quiet">{empty}</p>;
  return (
    <>
      {cards.length > 0 && <ul className="plain declist">{cards.map((e) => <Item key={e.name} e={e} />)}</ul>}
      {parts.length > 0 && (
        <p className="quiet declist__more">
          {cards.length > 0 ? "plus " : ""}{parts.map((p, i) => <span key={i}>{i ? (i === parts.length - 1 ? " and " : ", ") : ""}{p}</span>)}
        </p>
      )}
      {open === "helpers" && <ul className="plain declist declist--sub">{rest.map((e) => <Item key={e.name} e={e} />)}</ul>}
      {open === "vocabulary" && <ul className="plain declist declist--sub">{vocabulary.map((e) => <Item key={e.name} e={e} />)}</ul>}
    </>
  );
}
