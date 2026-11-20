// A declaration that the passage's argument map does not draw, with its Lean neighbours:
// the project declarations it uses and those that use it, from the edition's recorded
// dependency graph (the same records as the Lean panel's "Uses" and "Used by"). Drawn by
// the Graph tab's card colours as a flowing layout: the declarations that use it above, the
// declaration, then those it uses, each set wrapping into rows so every title is whole.
import { useEffect, useState } from "react";
import type { Edition } from "../app/edition";
import { Title } from "../text/title";
import "./tokens.css";
import "./graph.css";

const CAP = 8;

interface Neighbour { name: string; kind: string; users: number }
interface Local { name: string; uses: Neighbour[]; users: Neighbour[]; moreUses: number; moreUsers: number; kinds: Record<string, string> }

/** The project declarations on each side of `name`, most specific first (fewest users of their own). */
async function neighbours(reader: any, name: string): Promise<Local> {
  const index = await reader.resource("selection/index.json");
  const project = (n: string) => Object.hasOwn(index.modules, n) && n !== name;
  const node = await reader.expand(name);
  const side = async (record: any) => {
    const seen = new Map<string, string>();
    for (const kind of ["value", "type", "structural"]) for (const n of record?.[kind] ?? []) if (project(n) && !seen.has(n)) seen.set(n, kind);
    const rows = await Promise.all([...seen].map(async ([n, kind]) => {
      const other = await reader.expand(n).catch(() => null);
      const users = ["type", "value", "structural"].reduce((sum, k) => sum + (other?.incoming?.[k]?.length ?? 0), 0);
      return { name: n, kind, users };
    }));
    return rows.sort((a, b) => a.users - b.users || a.name.localeCompare(b.name));
  };
  const [uses, users] = await Promise.all([side(node), side(node.incoming)]);
  const kinds: Record<string, string> = {};
  // A card's shape follows its declaration keyword on its first source line.
  await Promise.all([name, ...uses.slice(0, CAP).map((u) => u.name), ...users.slice(0, CAP).map((u) => u.name)].map(async (n) => {
    const other = n === name ? node : await reader.expand(n).catch(() => null);
    if (!other?.source || !other.lines) return;
    const text: string = await reader.resource(other.source).catch(() => "");
    const head = text.split("\n").slice(other.lines[0] - 1, other.lines[1]).join("\n");
    const m = /^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*(theorem|lemma|def|abbrev|structure|inductive|class|instance|axiom)\b/m.exec(head);
    if (m) kinds[n] = m[1];
  }));
  return { name, uses: uses.slice(0, CAP), users: users.slice(0, CAP), moreUses: Math.max(0, uses.length - CAP), moreUsers: Math.max(0, users.length - CAP), kinds };
}

type Titles = Record<string, { title: string; title_plain: string }>;

/** One declaration as a card in the graph's colours, its whole title wrapped as needed. */
function Card({ name, kind, title, selected = false, onOpen }: { name: string; kind?: string; title?: { title: string; title_plain: string }; selected?: boolean; onOpen?(): void }) {
  const theorem = kind === "theorem" || kind === "lemma";
  const body = (
    <>
      <span className="lg-card__kind">{theorem ? "Theorem" : kind === "structure" || kind === "inductive" || kind === "class" ? "Type" : "Definition"}</span>
      <span className="lg-card__title">{title ? <Title text={title.title} /> : <code>{name}</code>}</span>
    </>
  );
  return onOpen
    ? <button type="button" className={`lg-card${theorem ? " is-theorem" : ""}`} data-record={name} title={`${name} — open it in the Lean tab`} onClick={onOpen}>{body}</button>
    : <div className={`lg-card${theorem ? " is-theorem" : ""}${selected ? " is-selected" : ""}`} data-record={name} title={name}>{body}</div>;
}

export function LocalGraph({ edition, name, titles, onOpenLean, onBack }: { edition: Edition; name: string;
  titles: Titles; onOpenLean(name: string): void; onBack(): void }) {
  const [local, setLocal] = useState<Local | null>(null);
  const [failed, setFailed] = useState(false);
  const [index, setIndex] = useState<Titles>({});
  useEffect(() => {
    let live = true;
    setLocal(null); setFailed(false);
    neighbours(edition.reader as any, name).then((l) => live && setLocal(l), () => live && setFailed(true));
    (edition.reader as any).declarationTitles().then((r: any) => live && setIndex(r.titles ?? {}), () => {});
    return () => { live = false; };
  }, [edition, name]);
  const title = (n: string) => titles[n] ?? index[n];
  const band = (label: string, rows: Neighbour[], more: number) => rows.length > 0 && (
    <div className="lg-band">
      <p className="lg-band__k">{label} <span>{rows.length + more}</span></p>
      <ul className="lg-grid">
        {rows.map((r) => <li key={r.name}><Card name={r.name} kind={local!.kinds[r.name]} title={title(r.name)} onOpen={() => onOpenLean(r.name)} /></li>)}
      </ul>
      {more > 0 && <p className="lg-band__more">and {more} more, listed in the Lean tab; the most specific are shown first.</p>}
    </div>
  );
  return (
    <section className="graph local-graph" aria-label="This declaration and its Lean neighbours">
      <div className="local-graph__head">
        <p className="local-graph__title" role="heading" aria-level={2}>This declaration and its Lean neighbours <span>(not in the passage’s argument map)</span></p>
        <button type="button" className="gbtn" onClick={onBack}>Show the passage map</button>
      </div>
      <div className="local-graph__body">
        {failed ? <p className="pending">The Lean neighbours could not be loaded.</p>
          : !local ? <p className="pending" role="status">Reading the Lean neighbours…</p>
          : <>
              {band("Used by", local.users, local.moreUsers)}
              {local.users.length > 0 && <p className="lg-link" aria-hidden="true">uses ↓</p>}
              <div className="lg-focus"><Card name={name} kind={local.kinds[name]} title={title(name)} selected /></div>
              {local.uses.length > 0 && <p className="lg-link" aria-hidden="true">uses ↓</p>}
              {band("Uses", local.uses, local.moreUses)}
              {!local.users.length && !local.uses.length && <p className="lg-band__more">No other declaration of this project uses it or is used by it.</p>}
            </>}
      </div>
    </section>
  );
}
