import type { ReactNode } from "react";
import type { Async } from "../app/useAsync";
import { face } from "../app/papers";
import { useNav } from "./Nav";

export function Loaded<T>({ value, children, what }: { value: Async<T>; children: (v: T) => ReactNode; what: string }) {
  if (value.state === "loading") return <p className="pending" role="status">Loading {what}…</p>;
  if (value.state === "failed")
    return (
      <div className="failed" role="alert">
        <p>The {what} could not be loaded: {value.error.message}</p>
        <p>The paper stays open on the left. Try again, or return to the passage.</p>
        <button type="button" className="textbutton" onClick={() => location.reload()}>Reload this page</button>
      </div>
    );
  return <>{children(value.value)}</>;
}

export function shortName(name: string): string {
  return name.replace(/^QuarticQuery\./, "").replace(/^QuarticCorpus\./, "");
}

export function DeclButton({ name, children }: { name: string; children?: ReactNode }) {
  const nav = useNav();
  return (
    <button type="button" className="decl" onClick={() => nav.openLean(name)} title={name}>
      {children ?? <code>{shortName(name)}</code>}
    </button>
  );
}

const ROLE: Record<string, string> = {
  general_exposition: "explains it", specialist_discussion: "discusses the decisive step", reading_route: "works through it",
  argument: "works through the argument", illustration: "illustrates it", illustrates: "illustrates it",
  worked_example: "works an example", interface: "states the interface", instantiation: "instantiates it",
};
const BY_PAPER: Record<string, string> = {
 exposition: "explains it", expert: "discusses it", reconstruction: "proves it in full",
};

function describe(r: { id: string; lines?: number[] }, i: number): string {
  if (r.id.startsWith("claim/")) return "the marked claim";
  if (r.id.startsWith("passage/")) return "the whole passage";
  if (r.lines) return `lines ${r.lines[0]}–${r.lines[1]}`;
  return `treatment ${i + 1}`;
}

/** Links to the same mathematics in the other papers, each with its role. */
export function Elsewhere({ rows, here }: { rows: { paper: string; id: string; treatment?: string; lines?: number[] }[]; here: string }) {
  const nav = useNav();
  const seen = new Set<string>();
  const order = ["original", "exposition", "expert", "reconstruction", "verification"];
  const unique = rows.filter((r) => r.paper !== here && !seen.has(r.paper + r.id) && seen.add(r.paper + r.id) && order.includes(r.paper));
  if (!unique.length) return <p className="quiet">No other paper has a linked treatment of this.</p>;
  const groups = order.map((p) => [p, unique.filter((r) => r.paper === p)] as const).filter(([, g]) => g.length);
  return (
    <ul className="elsewhere">
      {groups.map(([paper, list]) => (
        <li key={paper}>
          <span className="elsewhere__paper">{face(paper).tab}</span>
          <ul>
            {list.map((r, i) => (
              <li key={r.id}>
                <button type="button" className="elsewhere__go" onClick={() => nav.openSelection(r.paper, r.id)}>
                  {ROLE[r.treatment ?? ""] ?? BY_PAPER[r.paper] ?? "treats it"}
                  {list.length > 1 && <span className="quiet"> ({describe(r, i)})</span>}
                </button>
              </li>
            ))}
          </ul>
        </li>
      ))}
    </ul>
  );
}
