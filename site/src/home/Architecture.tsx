// The proof's architecture, from the edition's authored overview of the
// Forrelation family journey. Stages, not Lean edges: each opens its steps.
import { href } from "../app/router";

interface Stage { id: string; title: string; after: string[]; steps: string[] }

export function Architecture({ stages, paper = "original" }: { stages: Stage[]; paper?: string }) {
  const first = stages.filter((s) => s.after.length === 0);
  const parallel = stages.filter((s) => s.after.length === 1 && first.some((f) => f.id === s.after[0]));
  const rest = stages.filter((s) => !first.includes(s) && !parallel.includes(s));
  const link = (s: Stage) => href({ page: "read", paper, v: "journey", j: "forrelation-family", step: s.steps[0] });
  const Box = ({ s }: { s: Stage }) => <a className={`arch__box arch__box--${s.id}`} href={link(s)}>{s.title}</a>;
  return (
    <figure className="arch" aria-labelledby="arch-h">
      <h2 id="arch-h">How the proof fits together</h2>
      <ol className="arch__flow">
        {first.map((s) => <li key={s.id}><Box s={s} /></li>)}
        <li className="arch__pair">
          {parallel.map((s) => <Box key={s.id} s={s} />)}
        </li>
        {rest.map((s) => <li key={s.id}><Box s={s} /></li>)}
      </ol>
      <figcaption className="quiet">
        The editors’ outline of the argument. The last stage also uses the known universal quartic upper bound of Aaronson,
        Ben-David, Kothari, Rao and Tal. Each stage opens the Lean applications behind it. This is a reading order, not
        Lean’s dependency graph.
      </figcaption>
    </figure>
  );
}
