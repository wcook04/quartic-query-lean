// The proof's architecture, from the edition's authored overview of the
// Forrelation family journey. Every stage shows its steps in place, so the
// outline reads without clicking; each step opens its walkthrough.
import { useEffect, useState } from "react";
import { href } from "../app/router";
import type { Edition } from "../app/edition";
import { inlineTex } from "../text/html";

interface Stage { id: string; title: string; after: string[]; steps: string[] }

const SIDE: Record<string, string> = { quantum: "Quantum upper bound", classical: "Classical lower bound" };

export function Architecture({ stages, edition, paper = "original" }: { stages: Stage[]; edition: Edition; paper?: string }) {
  const [titles, setTitles] = useState<Map<string, string>>(new Map());
  useEffect(() => {
    let live = true;
    edition.reader.journey("forrelation-family").then((j: any) => {
      if (live) setTitles(new Map(j.steps.map((s: any) => [s.id, s.title])));
    }).catch(() => {});
    return () => { live = false; };
  }, [edition]);

  const first = stages.filter((s) => s.after.length === 0);
  const parallel = stages.filter((s) => s.after.length === 1 && first.some((f) => f.id === s.after[0]));
  const rest = stages.filter((s) => !first.includes(s) && !parallel.includes(s));
  const order = [...first, ...parallel, ...rest];
  const num = (s: Stage) => order.indexOf(s) + 1;
  const link = (step: string) => href({ page: "read", paper, v: "journey", j: "forrelation-family", step });

  const Card = ({ s }: { s: Stage }) => (
    <section className={`arch__stage${SIDE[s.id] ? " arch__stage--side" : ""}`}>
      <p className="arch__kicker"><span className="arch__n">{num(s)}</span>{SIDE[s.id] ?? ""}</p>
      <h3 className="arch__title">{s.title}</h3>
      <ol className="arch__steps">
        {s.steps.map((id) => (
          <li key={id}>
            <a href={link(id)}>
              {titles.has(id)
                ? <span dangerouslySetInnerHTML={{ __html: inlineTex(titles.get(id)!) }} />
                : id.replace(/-/g, " ")}
            </a>
          </li>
        ))}
      </ol>
    </section>
  );

  return (
    <figure className="arch" aria-labelledby="arch-h">
      <h2 id="arch-h">How the proof fits together</h2>
      <div className="arch__flow">
        {first.map((s) => <Card key={s.id} s={s} />)}
        <div className="arch__pair">{parallel.map((s) => <Card key={s.id} s={s} />)}</div>
        {rest.map((s) => <Card key={s.id} s={s} />)}
      </div>
      <figcaption className="quiet">
        The editors’ outline of the argument, in reading order. Each step opens the Lean that carries it out. The last stage
        also uses the known universal quartic upper bound of Aaronson, Ben-David, Kothari, Rao and Tal.
      </figcaption>
    </figure>
  );
}
