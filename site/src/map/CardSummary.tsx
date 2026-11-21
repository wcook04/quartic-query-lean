// A card previewed in the dock under the graph while it is under the pointer: its kind and
// Lean name, the reviewed match to a paper statement (derived as the Lean view derives it,
// LeanPanel.tsx), and the Lean statement with its proof folded (as the homepage's HeadlinePair).
import type { ClaimMatch } from "../paper/selectRow";
import { useAsync } from "../app/useAsync";
import { LeanCode } from "../lean/LeanCode";
import { RelationMark } from "../inspect/evidence";
import { StatementLabel } from "../inspect/common";

/* eslint-disable @typescript-eslint/no-explicit-any */
type Reader = any;

interface Props {
  reader: Reader;
  name: string;
  /** The card's title as the map draws it. */
  title: string;
  /** The proof map's kind for the declaration, when recorded. */
  kind?: string | null;
  claimMatch?: ClaimMatch;
}

function kindWords(kind: string | null | undefined, text: string): string {
  if (kind === "structure" || kind === "inductive" || kind === "class") return "Lean type";
  if (kind === "theorem" || kind === "lemma" || /^(private |protected )?(theorem|lemma)\s/m.test(text)) return "Lean theorem";
  if (!kind && /^(private |protected )?(structure|inductive|class)\s/m.test(text)) return "Lean type";
  return "Lean definition";
}

export function CardSummary({ reader, name, kind, claimMatch }: Props) {
  const data = useAsync<any>(() => reader.fromDeclaration(name), [reader, name]);
  const d = data.state === "ready" ? data.value : null;
  const src = d?.source ?? {};
  // The paper statements this declaration is tied to, each with its review, once (LeanPanel's derivation).
  const ties = new Map<string, { relation: string; review?: string }>();
  for (const t of d?.treatments ?? []) {
    if (!t.statement) continue;
    const prev = ties.get(t.statement);
    if (!prev || (prev.review !== "current" && t.review === "current")) ties.set(t.statement, { relation: t.relation, review: t.review });
  }
  const reviewed = [...ties].filter(([, t]) => t.review === "current" && t.relation !== "unassessed");
  const file = (src.source ?? "").replace(/^lean\//, "");
  const words = kindWords(kind, src.text ?? "");

  return (
    <div className="card-sum">
      <p className="card-sum__kind">{words} <code className="card-sum__name">{name}</code></p>
      {data.state === "loading" && <p className="edge-ev__note" role="status">Loading the card…</p>}
      {data.state === "failed" && <p className="edge-ev__note" role="alert">This card’s Lean could not be loaded.</p>}
      {claimMatch && <p className="card-sum__match"><span className="card-sum__k">{claimMatch.title}</span> <RelationMark relation={claimMatch.relation} /></p>}
      {!claimMatch && d && reviewed.map(([st, t]) => (
        <p key={st} className="card-sum__match"><span className="card-sum__k">Matches the paper</span> <RelationMark relation={t.relation as any} /> <span className="card-sum__vs">against</span> <span className="card-sum__st"><StatementLabel id={st} /></span></p>
      ))}
      {d && src.text && (
        <div className="card-sum__code">
          <LeanCode text={src.text} from={src.lines?.[0] ?? 1} self={name} label={`Lean source of ${name}`} url={src.url} foldOver={0}
            foldWord={words === "Lean theorem" ? "proof" : "definition body"}
            caption={<span className="leancode__file">{file || "Lean source"}</span>} />
        </div>
      )}
    </div>
  );
}
