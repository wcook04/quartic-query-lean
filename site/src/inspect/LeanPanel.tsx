// One Lean declaration: its source, what Lean says it depends on, what uses it,
// and the paper passages that cite it. Edges are Lean's; paper links are editorial.
import { useMemo, useState } from "react";
import { useAsync } from "../app/useAsync";
import type { Edition } from "../app/edition";
import { LeanCode, nameLinks } from "../lean/LeanCode";
import { Axioms } from "./evidence";
import { Elsewhere, Loaded, shortName } from "./common";
import { useNav } from "./Nav";

const KIND_WORD: Record<string, string> = { value: "proof or body", type: "statement", structural: "structure" };
const PROJECT = /^Quartic(Query|Corpus)\./;

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
    const [d, reverse] = await Promise.all([edition.reader.fromDeclaration(name), edition.reader.resource("selection/reverse.json")]);
    return { d, linked: new Set(Object.keys(reverse)) };
  }, [edition, name]);
  return <Loaded value={data} what="Lean declaration">{({ d, linked }) => <Declaration d={d} linked={linked} />}</Loaded>;
}

function Declaration({ d, linked }: { d: any; linked: Set<string> }) {
  const nav = useNav();
  const src = d.source ?? {};
  const uses = useMemo(() => edges(src, "uses"), [src]);
  const users = useMemo(() => edges(src, "used_by"), [src]);
  const links = useMemo(() => nameLinks([...uses.map((e) => e.name), ...users.map((e) => e.name)]), [uses, users]);

  if (src.status === "external_module_boundary" || src.status === "outside_recorded_graph") {
    return (
      <article className="panel">
        <h2 className="panel__title"><code>{d.name}</code></h2>
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
        <h2 id="ln-h" className="panel__title"><code>{shortName(d.name)}</code></h2>
        <p className="panel__where">
          {src.kind ? `${src.kind} in ` : "In "}<code>{src.module}</code>, lines {src.lines?.[0]}–{src.lines?.[1]}.{" "}
          {src.url && <a href={src.url} target="_blank" rel="noopener noreferrer">Source on GitHub</a>}
        </p>
      </header>

      <p className="cmp__actions"><button type="button" className="button button--small" onClick={() => nav.openGraph(d.name)}>Show it in the graph</button></p>
      <Neighbourhood self={d.name} uses={uses} users={users} linked={linked} />

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

const SHOW = 7;

function Neighbourhood({ self, uses, users, linked }: { self: string; uses: Edge[]; users: Edge[]; linked: Set<string> }) {
  const [all, setAll] = useState(false);
  const rank = (list: Edge[]) => {
    const project = list.filter((e) => PROJECT.test(e.name));
    project.sort((a, b) => Number(linked.has(b.name)) - Number(linked.has(a.name)));
    return { project, outside: list.length - project.length };
  };
  const right = rank(uses), left = rank(users);
  const r = all ? right.project : right.project.slice(0, SHOW);
  const l = all ? left.project : left.project.slice(0, SHOW);
  const rows = Math.max(r.length, l.length, 1);
  const H = rows * 44;
  return (
    <section className="hood" aria-labelledby="hood-h">
      <h3 id="hood-h">What it uses, and what uses it</h3>
      <p className="quiet">Edges reported by Lean, nearest paper-cited declarations first. A dot marks one that a paper passage cites. A name in the Lean below is a link only when it matches exactly one of these recorded edges.</p>
      <div className="hood__map" style={{ height: H }}>
        <svg className="hood__wires" viewBox={`0 0 100 ${H}`} preserveAspectRatio="none" aria-hidden="true">
          {l.map((e, i) => <path key={"l" + e.name} d={`M34 ${(i + 0.5) * 44} C42 ${(i + 0.5) * 44}, 42 ${H / 2}, 50 ${H / 2}`} className={`wire wire--${e.kind}`} />)}
          {r.map((e, i) => <path key={"r" + e.name} d={`M50 ${H / 2} C58 ${H / 2}, 58 ${(i + 0.5) * 44}, 66 ${(i + 0.5) * 44}`} className={`wire wire--${e.kind}`} />)}
        </svg>
        <ul className="hood__col hood__col--left" aria-label="Declarations that use it">
          {l.map((e) => <Node key={e.name} e={e} linked={linked.has(e.name)} />)}
          {l.length === 0 && <li className="quiet">No project declaration uses it.</li>}
        </ul>
        <div className="hood__self" style={{ top: H / 2 }}><code>{shortName(self).split(".").pop()}</code></div>
        <ul className="hood__col hood__col--right" aria-label="Declarations it uses">
          {r.map((e) => <Node key={e.name} e={e} linked={linked.has(e.name)} />)}
          {r.length === 0 && <li className="quiet">It uses no other project declaration.</li>}
        </ul>
      </div>
      <p className="hood__foot">
        {left.project.length} project declarations use it; it uses {right.project.length}
        {right.outside ? `, plus ${right.outside} from Mathlib and other libraries` : ""}.{" "}
        {(left.project.length > SHOW || right.project.length > SHOW) && (
          <button type="button" className="textbutton" onClick={() => setAll(!all)}>{all ? "Show the nearest only" : "Show all of them"}</button>
        )}
      </p>
    </section>
  );
}

function Node({ e, linked }: { e: Edge; linked: boolean }) {
  const nav = useNav();
  return (
    <li>
      <button type="button" className={`node${linked ? " node--linked" : ""}`} onClick={() => nav.openLean(e.name)} title={`${e.name} (in the ${KIND_WORD[e.kind]})`}>
        <span className="node__name">{shortName(e.name).split(".").pop()}</span>
        <span className="sr-only">, used in the {KIND_WORD[e.kind]}{linked ? ", cited by a paper" : ""}</span>
      </button>
    </li>
  );
}
