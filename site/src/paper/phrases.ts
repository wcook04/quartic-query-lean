// Phrase ties: the exact words of a paper that each Lean declaration states, adapted
// from Proof Reader's Physlib Gauge theory map (web/src/api/PhyslibMap.tsx at a7fcf2e,
// Apache-2.0). The edition marks each phrase in the manuscript HTML as
// <span class="phrase" data-phrase="<id>" data-tone="<n>">; a phrase set in a table
// has one span per cell. Its topic gives the colour, never its fidelity.
import { createContext, useContext } from "react";
import { renderTex } from "../text/math";

export interface PhraseLean {
  name: string;
  file: string;
  lines?: [number, number];
  declaration_lines: [number, number];
  in_graph: boolean;
  relation: "states" | "defines" | "part" | "proof" | "contains";
  fidelity: "same" | "stronger" | "weaker" | "different";
  fidelity_note?: string;
  link_note?: string;
}
export interface Phrase { id: string; order: number; lines: [number, number]; text: string; role: string; topic: string; tone: number; lean: PhraseLean[] }
export interface Topic { id: string; name: string; description: string }
export interface PhraseLayer {
  paper: string;
  topics: Topic[];
  phrases: Phrase[];
  titles: Record<string, { title: string; title_plain: string }>;
  notes: Record<string, string>;
  byId: Map<string, Phrase>;
  byName: Map<string, Phrase[]>;
  topicIndex: Map<string, number>;
}

export function phraseLayer(data: any): PhraseLayer | null {
  if (!data || data.status !== "current" || !data.phrases?.length) return null;
  const byId = new Map<string, Phrase>();
  const byName = new Map<string, Phrase[]>();
  for (const p of data.phrases as Phrase[]) {
    byId.set(p.id, p);
    for (const row of p.lean) if (!byName.get(row.name)?.includes(p)) byName.set(row.name, [...byName.get(row.name) ?? [], p]);
  }
  const topicIndex = new Map<string, number>((data.topics as Topic[]).map((t, i) => [t.id, i]));
  return { paper: data.paper, topics: data.topics, phrases: data.phrases, titles: data.titles, notes: data.notes, byId, byName, topicIndex };
}

export const PhraseContext = createContext<PhraseLayer | null>(null);
export const usePhrases = () => useContext(PhraseContext);

/** The first shade of a topic, for keys and bars. */
export const topicTone = (layer: PhraseLayer, topic: string) => 2 * (layer.topicIndex.get(topic) ?? 0);

const RELATION: Record<PhraseLean["relation"], string> = {
  states: "Lean states this phrase",
  defines: "Lean defines the object this phrase names",
  part: "Lean states one part of this phrase",
  proof: "This phrase is a step of the Lean proof",
  contains: "Lean’s statement contains this claim among others",
};
export const relationLine = (row: PhraseLean) => RELATION[row.relation];

/** The comparison with this phrase, in words. Colour never carries it. */
export function fidelityLine(row: PhraseLean): { lead: string; note?: string } {
  switch (row.fidelity) {
    case "same": return { lead: "Lean states the same as this phrase." };
    case "stronger": return { lead: "Lean states more:", note: row.fidelity_note };
    case "weaker": return { lead: "Lean states less:", note: row.fidelity_note };
    default: return { lead: "Lean states something different:", note: row.fidelity_note };
  }
}

const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

/** A reading note or comparison note: `$…$` is TeX, set with KaTeX; backticks are Lean code. */
export function noteHtml(text: string): string {
  let out = "";
  let last = 0;
  const re = /\$([^$]+)\$|`([^`]+)`/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(text))) {
    out += esc(text.slice(last, m.index));
    out += m[1] != null ? renderTex(m[1], false).html : `<code>${esc(m[2])}</code>`;
    last = m.index + m[0].length;
  }
  return out + esc(text.slice(last));
}

/** The spans of one phrase in the open paper (several when it is set in a table). */
export const phraseSpans = (id: string) =>
  [...document.querySelectorAll<HTMLElement>(`.manuscript .phrase[data-phrase="${CSS.escape(id)}"]`)];

/** Light the phrases and cards of these declarations or phrase IDs, wherever the pointer is. */
export function lightPhrases(layer: PhraseLayer | null, names: string[] | null, phraseIds: string[] = []) {
  const ids = new Set(phraseIds);
  if (layer && names) for (const name of names) for (const p of layer.byName.get(name) ?? []) ids.add(p.id);
  const lit = names ? new Set(names) : new Set<string>();
  for (const el of document.querySelectorAll<HTMLElement>(".manuscript .phrase[data-phrase]"))
    el.classList.toggle("is-lit", ids.has(el.dataset.phrase!));
  for (const el of document.querySelectorAll<HTMLElement>("[data-phrase-card]"))
    el.classList.toggle("is-lit", ids.has(el.dataset.phraseCard!) || lit.has(el.dataset.leanName ?? ""));
}

/** The phrase's own words as the paper shows them, typeset; table cells joined by a bar. */
export function phraseHtml(id: string): string | null {
  const spans = phraseSpans(id);
  if (!spans.length) return null;
  return spans.map((s) => s.innerHTML).join(" <span class=\"phrase-quote__cell\" aria-hidden=\"true\">|</span> ");
}

/** Bring a phrase into view in the paper and flash it. */
export function showPhrase(id: string) {
  const spans = phraseSpans(id);
  if (!spans.length) return;
  spans[0].scrollIntoView({ block: "center", behavior: "smooth" });
  for (const s of spans) {
    s.classList.remove("is-flash");
    void s.offsetWidth;
    s.classList.add("is-flash");
  }
}
