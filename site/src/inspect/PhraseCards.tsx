// Declaration cards for phrase ties, adapted from Proof Reader's DeclarationCard and
// PhraseQuotes (web/src/api/PhyslibMap.tsx at a7fcf2e, Apache-2.0). A card quotes the
// paper's phrase, names what the Lean row does with it, says in words how the Lean
// compares with those words, and gives the reading note. Pointing at a card lights its
// phrase in the paper; clicking the quote brings the phrase into view.
import { useLayoutEffect, useState } from "react";
import { Title } from "../text/title";
import { face } from "../app/papers";
import { fidelityLine, lightPhrases, noteHtml, phraseHtml, relationLine, showPhrase, topicTone, usePhrases, type Phrase, type PhraseLean } from "../paper/phrases";
import { useNav } from "./Nav";

function Quote({ phrase }: { phrase: Phrase }) {
  const [html, setHtml] = useState<string | null>(null);
  useLayoutEffect(() => setHtml(phraseHtml(phrase.id)), [phrase.id]);
  return (
    <button type="button" className="phrase-quote" title="Show this phrase in the paper" onClick={() => showPhrase(phrase.id)}>
      <span className="sr-only">Show in the paper: </span>
      <span dangerouslySetInnerHTML={{ __html: html ?? noteHtml(phrase.text) }} />
    </button>
  );
}

export function PhraseCard({ phrase, row, picked = false, openLean = true, showTitle = true }: { phrase: Phrase; row: PhraseLean; picked?: boolean; openLean?: boolean; showTitle?: boolean }) {
  const layer = usePhrases()!;
  const nav = useNav();
  const topic = layer.topics[layer.topicIndex.get(phrase.topic) ?? 0];
  const title = layer.titles[row.name];
  const note = layer.notes[row.name];
  const fidelity = fidelityLine(row);
  const lines = row.lines ? (row.lines[0] === row.lines[1] ? `line ${row.lines[0]}` : `lines ${row.lines[0]}–${row.lines[1]}`) : null;
  return (
    <section className={`phrase-card${picked ? " is-picked" : ""}`} data-phrase-card={phrase.id} data-lean-name={row.name} data-tone={phrase.tone}
      onMouseEnter={() => lightPhrases(layer, null, [phrase.id])} onMouseLeave={() => lightPhrases(layer, null)}
      onFocus={() => lightPhrases(layer, null, [phrase.id])} onBlur={() => lightPhrases(layer, null)}>
      <p className="phrase-card__topic"><span className="topic-swatch" data-tone={topicTone(layer, phrase.topic)} aria-hidden="true" />Topic: {topic.name}</p>
      {showTitle && <h3 className="phrase-card__title">{title ? <Title text={title.title} /> : row.name}</h3>}
      <p className="phrase-card__k">The words in the {face(layer.paper).tab.toLowerCase()}</p>
      <Quote phrase={phrase} />
      <p className="phrase-card__rel">{relationLine(row)}{lines && <>, at {lines} of</>}{!lines && <> in</>} <code className="phrase-card__name">{row.name}</code>.</p>
      {row.link_note && <p className="phrase-card__link" dangerouslySetInnerHTML={{ __html: noteHtml(row.link_note) }} />}
      <p className="phrase-card__fid">
        <span className="phrase-card__label">Compared with these words <span className="phrase-card__by">AI-assessed</span></span>
        <span className="phrase-card__fid-text"><strong>{fidelity.lead}</strong>{fidelity.note && <> <span dangerouslySetInnerHTML={{ __html: noteHtml(fidelity.note) }} /></>}</span>
      </p>
      {note && (
        <div className="phrase-card__note">
          <p className="phrase-card__label">Reading note <span className="phrase-card__by">AI-drafted</span></p>
          <p dangerouslySetInnerHTML={{ __html: noteHtml(note) }} />
        </div>
      )}
      {openLean && <p className="phrase-card__act"><button type="button" className="textbutton" onClick={() => nav.openLean(row.name, phrase.id)}>Open this declaration in the Lean tab</button></p>}
    </section>
  );
}

/** Every phrase tied in the given source lines, each with its Lean rows. */
export function PhraseList({ lines, picked }: { lines: [number, number] | null; picked?: string }) {
  const layer = usePhrases();
  useLayoutEffect(() => {
    if (!picked) return;
    document.querySelector<HTMLElement>(`.phrase-list [data-phrase-card="${CSS.escape(picked)}"]`)?.scrollIntoView({ block: "nearest" });
  }, [picked]);
  if (!layer || !lines) return null;
  const inside = layer.phrases.filter((p) => p.lines[0] <= lines[1] && lines[0] <= p.lines[1]);
  if (!inside.length) return null;
  const tied = inside.filter((p) => p.lean.length);
  const untied = inside.length - tied.length;
  return (
    <section className="block phrase-list" aria-labelledby="pl-h">
      <h3 id="pl-h" className="block__h">Phrases tied to Lean in this paragraph <span className="fold__n">{tied.length}</span></h3>
      <p className="phrase-list__lede">Each phrase is underlined in the paper in its topic’s colour. Point at a card to light its phrase.</p>
      {tied.map((p) => p.lean.map((row) => <PhraseCard key={`${p.id}:${row.name}`} phrase={p} row={row} picked={p.id === picked} />))}
      {untied > 0 && <p className="phrase-list__lede">{untied === 1 ? "One further phrase explains" : `${untied} further phrases explain`} the argument without a Lean declaration of its own.</p>}
    </section>
  );
}

/** The chosen phrase under the graph: what it is tied to, and a way to its Lean. */
export function PhraseStrip({ id }: { id: string }) {
  const layer = usePhrases();
  const nav = useNav();
  const phrase = layer?.byId.get(id);
  if (!layer || !phrase || !phrase.lean.length) return null;
  const row = phrase.lean[0];
  const topic = layer.topics[layer.topicIndex.get(phrase.topic) ?? 0];
  const title = layer.titles[row.name];
  return (
    <div className="phrase-strip" data-tone={phrase.tone} data-phrase-card={phrase.id} data-lean-name={row.name}
      onMouseEnter={() => lightPhrases(layer, null, [phrase.id])} onMouseLeave={() => lightPhrases(layer, null)}>
      <p className="phrase-strip__k"><span className="topic-swatch" data-tone={topicTone(layer, phrase.topic)} aria-hidden="true" />Chosen phrase · {topic.name}</p>
      <p className="phrase-strip__title">{title ? <Title text={title.title} /> : row.name}{phrase.lean.length > 1 && <span className="phrase-strip__more"> and {phrase.lean.length - 1} more</span>}</p>
      <p className="phrase-strip__act"><button type="button" className="textbutton" onClick={() => nav.openLean(row.name, phrase.id)}>Open it in the Lean tab</button> <span className="phrase-strip__hint">for the reading note and the comparison with these words</span></p>
    </div>
  );
}

/** The phrases of this paper that a declaration states, for the top of its Lean panel. */
export function DeclarationPhrases({ name, picked }: { name: string; picked?: string }) {
  const layer = usePhrases();
  if (!layer) return null;
  const phrases = layer.byName.get(name) ?? [];
  if (!phrases.length) return null;
  const ordered = [...phrases].sort((a, b) => Number(b.id === picked) - Number(a.id === picked) || a.order - b.order);
  const [first, ...rest] = ordered;
  const card = (p: Phrase) => <PhraseCard key={p.id} phrase={p} row={p.lean.find((r) => r.name === name)!} picked={p.id === picked} openLean={false} showTitle={false} />;
  return (
    <section className="block phrase-list phrase-list--lean" aria-label="The phrases this declaration states">
      {card(first)}
      {rest.length > 0 && (
        <details className="fold">
          <summary>Other phrases of this paper tied to it <span className="fold__n">{rest.length}</span></summary>
          {rest.map(card)}
        </details>
      )}
    </section>
  );
}
