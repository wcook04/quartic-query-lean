// The Graph view's drawing for the Quartic Reader: the shared focus graph (FocusGraph.tsx,
// specified in docs/graph-pane.md) fed from the edition. Every card and line comes from the
// edition's data: the proof map (selection/proof-map.json) gives the paper's steps, their
// reviewed statements and the lines between them; the recorded Lean dependency shards
// (proof/<module>.json, read through reader.expand) give the Lean-only declarations a step
// uses or is used by; the phrase ties give each declaration its topic colour. Nothing here
// joins two declarations that the edition does not join.
import { useCallback, useEffect, useLayoutEffect, useMemo, useState, type ReactNode } from "react";
import type { Edition } from "../app/edition";
import { FG_ROLES, FocusGraph, type FGCard, type FGEdge, type FGRole } from "./FocusGraph";
import { SOURCE_READER } from "../app/edition";
import type { ProofMap } from "./fromProofMap";
import { kindLabel } from "../results/Results";
import { Title } from "../text/title";
import { topicTone, usePhrases, type PhraseLayer } from "../paper/phrases";
import "./subject-graph.css";

/* eslint-disable @typescript-eslint/no-explicit-any */
type Reader = any;
type Titles = Record<string, { title: string; title_plain: string }>;

interface MapEdge { from: string; to: string; witnesses: Record<string, number> }
interface Base {
  map: ProofMap & { papers: Record<string, { bindings: Record<string, string[]>; lines?: [number, number] }[]> };
  modules: Record<string, string>;
  titles: Titles;
  helperKinds: Record<string, string>;
  statementKinds: Record<string, string>;
  out: Map<string, MapEdge[]>;
  inc: Map<string, MapEdge[]>;
}

/** A declaration as the graph knows it: its titles, its Lean keyword and whether the proof map draws it. */
export interface Decl { name: string; title: string; plain: string; kind: string | null; onMap: boolean; source?: string }
export interface Around { subjects: string[]; decls: Map<string, Decl>; edges: FGEdge[]; route: string[] | null }

const DEFINITION_KINDS = new Set(["def", "abbrev", "structure", "inductive", "class", "opaque", "instance"]);
// The order in which a card's reviewed statements give its printed number.
const STATEMENT_ORDER = ["thm", "prop", "lem", "cor", "eq", "claim", "construct", "def"];
const NUMBERED = new Set(["thm", "prop", "lem", "cor"]);

const witnessKind = (w: Record<string, number>): FGEdge["kind"] =>
  Object.hasOwn(w, "value") || Object.hasOwn(w, "structural") ? "proof" : Object.hasOwn(w, "type") ? "statement" : undefined;

async function loadBase(reader: Reader): Promise<Base | null> {
  const map = await reader.proofMap();
  if (map?.currentness !== "current") return null;
  const [index, titles, helpers, statements] = await Promise.all([
    reader.resource("selection/index.json"), reader.declarationTitles(),
    reader.resource("selection/proof-helpers.json").catch(() => ({ helpers: {} })),
    reader.resource("corpus/statements.json").catch(() => []),
  ]);
  const out = new Map<string, MapEdge[]>(), inc = new Map<string, MapEdge[]>();
  for (const e of map.edges as MapEdge[]) {
    out.set(e.from, [...(out.get(e.from) ?? []), e]);
    inc.set(e.to, [...(inc.get(e.to) ?? []), e]);
  }
  return {
    map, modules: index.modules, titles: titles.titles ?? {}, out, inc,
    helperKinds: Object.fromEntries(Object.entries(helpers.helpers ?? {}).map(([n, h]: [string, any]) => [n, h.kind])),
    statementKinds: Object.fromEntries((statements as any[]).map((s) => [s.id, s.kind])),
  };
}

const KEYWORD = /^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec)\s+)*(theorem|lemma|def|abbrev|structure|inductive|class|instance|axiom|opaque)\b/m;

/** The Lean keyword of a declaration the map does not draw: from the helper catalogue, else its first source line. */
async function keywordOf(reader: Reader, base: Base, name: string, node: any): Promise<string | null> {
  if (base.helperKinds[name]) return base.helperKinds[name];
  if (!node?.source || !node.lines) return null;
  const text: string = await reader.resource(node.source).catch(() => "");
  return KEYWORD.exec(text.split("\n").slice(node.lines[0] - 1, node.lines[1]).join("\n"))?.[1] ?? null;
}

function mapDecl(base: Base, name: string): Decl {
  const c: any = base.map.cards[name];
  return { name, title: c.short_title || c.title || name, plain: c.short_title_plain || c.title_plain || name, kind: c.kind, onMap: true, source: c.source };
}

/** The subjects, the cards next to them and the lines between, and the route to the main result. */
async function around(reader: Reader, base: Base, subjects: string[]): Promise<Around> {
  const decls = new Map<string, Decl>();
  const edges: FGEdge[] = [];
  const onMap = (n: string) => Object.hasOwn(base.map.cards, n);
  const short = (n: string) => n.replace(/^QuarticQuery\./, "");
  const remember = async (name: string, node?: any) => {
    if (decls.has(name)) return;
    if (onMap(name)) { decls.set(name, mapDecl(base, name)); return; }
    const t = base.titles[name];
    decls.set(name, { name, title: t?.title ?? short(name), plain: t?.title_plain ?? short(name), kind: await keywordOf(reader, base, name, node), onMap: false, source: node?.source });
  };
  for (const s of subjects) {
    const node = await reader.expand(s).catch(() => null);
    await remember(s, node);
    // The proof map's own lines: the paper's argument, through helpers it does not draw.
    if (onMap(s)) {
      for (const e of base.out.get(s) ?? []) { await remember(e.to); edges.push({ from: s, to: e.to, kind: witnessKind(e.witnesses) }); }
      for (const e of base.inc.get(s) ?? []) { await remember(e.from); edges.push({ from: e.from, to: s, kind: witnessKind(e.witnesses) }); }
    }
    if (node?.status !== "recorded") continue;
    // Lean's own direct uses, for declarations with their own source lines (not compiler-made
    // auxiliaries). A declaration the map draws is reached through the map's line above.
    for (const side of ["uses", "users"] as const) {
      const record = side === "uses" ? node : node.incoming ?? {};
      const kinds = new Map<string, FGEdge["kind"]>();
      for (const k of ["value", "structural", "type"])
        for (const other of record[k] ?? []) {
          if (other === s || !Object.hasOwn(base.modules, other) || kinds.has(other)) continue;
          kinds.set(other, k === "type" ? "statement" : "proof");
        }
      for (const [other, kind] of kinds) {
        if (onMap(s) && onMap(other)) continue;
        const next = onMap(other) ? null : await reader.expand(other).catch(() => null);
        if (!onMap(other) && !next?.lines) continue;
        await remember(other, next);
        edges.push(side === "uses" ? { from: s, to: other, kind } : { from: other, to: s, kind });
      }
    }
  }
  const route = await routeFrom(reader, base, subjects);
  for (const id of route ?? []) await remember(id);
  // Two subjects of one paragraph see the same line from both ends: keep it once.
  const once = new Map<string, FGEdge>();
  for (const e of edges) {
    const k = `${e.from}>${e.to}`;
    if (!once.has(k) || once.get(k)!.kind === "statement") once.set(k, e);
  }
  return { subjects, decls, edges: [...once.values()], route };
}

/** The shortest chain of "used by" from a subject to the main result: through the map, or for a
 *  declaration the map does not draw, through Lean's users to the nearest map card first. */
async function routeFrom(reader: Reader, base: Base, subjects: string[]): Promise<string[] | null> {
  const root = base.map.root;
  if (subjects.includes(root)) return [];
  const back = new Map<string, string | null>();
  let frontier: string[] = [];
  for (const s of subjects) if (Object.hasOwn(base.map.cards, s)) { back.set(s, null); frontier.push(s); }
  // A declaration off the map climbs Lean's users until it meets the map.
  const off = subjects.filter((s) => !Object.hasOwn(base.map.cards, s));
  if (off.length && !frontier.length) {
    const seen = new Map<string, string | null>(off.map((s) => [s, null]));
    let wave = [...off], met: string | null = null;
    while (wave.length && !met && seen.size < 3000) {
      const next: string[] = [];
      for (const n of wave) {
        const node = await reader.expand(n).catch(() => null);
        for (const k of ["value", "type", "structural"]) for (const u of node?.incoming?.[k] ?? []) {
          if (seen.has(u)) continue;
          seen.set(u, n);
          if (Object.hasOwn(base.map.cards, u)) { met = u; break; }
          next.push(u);
        }
        if (met) break;
      }
      wave = next;
    }
    if (!met) return null;
    for (let at: string | null = met; at != null; at = seen.get(at) ?? null) back.set(at, seen.get(at) ?? null);
    frontier = [met];
  }
  while (frontier.length && !back.has(root)) {
    const next: string[] = [];
    for (const n of frontier) for (const e of base.inc.get(n) ?? []) if (!back.has(e.from)) { back.set(e.from, n); next.push(e.from); }
    frontier = next;
  }
  if (!back.has(root)) return null;
  const chain: string[] = [];
  for (let at: string | null = root; at != null && !subjects.includes(at); at = back.get(at) ?? null) chain.unshift(at);
  return chain;
}

/** The colour of each topic, read from the paper's own phrase rules so the card edge matches. */
function useToneColours(layer: PhraseLayer | null): (topic: string) => string | undefined {
  const [colours, setColours] = useState<Record<string, string>>({});
  useLayoutEffect(() => {
    if (!layer) { setColours({}); return; }
    const read = () => {
      const host = document.querySelector<HTMLElement>("[data-topic-count]");
      if (!host) return;
      const probe = document.createElement("span");
      probe.hidden = true;
      host.append(probe);
      const next: Record<string, string> = {};
      for (const t of layer.topics) {
        probe.dataset.tone = String(topicTone(layer, t.id));
        const v = getComputedStyle(probe).getPropertyValue("--tone").trim();
        if (v) next[t.id] = v;
      }
      probe.remove();
      setColours(next);
    };
    read();
    const watch = new MutationObserver(read);
    watch.observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
    return () => watch.disconnect();
  }, [layer]);
  return useCallback((topic: string) => colours[topic], [colours]);
}

function useNarrow(): boolean {
  const q = "(max-width: 599px)";
  const [narrow, setNarrow] = useState(() => window.matchMedia(q).matches);
  useEffect(() => {
    const m = window.matchMedia(q);
    const on = () => setNarrow(m.matches);
    m.addEventListener("change", on);
    return () => m.removeEventListener("change", on);
  }, []);
  return narrow;
}

interface Props {
  edition: Edition;
  combined?: boolean;
  paper: string;
  /** The declarations in the middle. */
  subjects: readonly string[];
  /** The source lines of the paragraph being read or clicked, for "read" and "stated later". */
  position: [number, number] | null;
  /** What the pointer is over in the paper: a phrase's declarations or a paragraph's lines. */
  hover: { names?: string[]; lines?: [number, number] } | null;
  held?: string | null;
  label?: ReactNode;
  onSubject(name: string): void;
  onHover(name: string | null): void;
}

export function SubjectGraph({ edition, paper, subjects, position, hover, held, label, onSubject, onHover, combined }: Props) {
  const reader = edition.reader as Reader;
  const layer = usePhrases();
  const tone = useToneColours(layer);
  const narrow = useNarrow();
  const [unfolded, setUnfolded] = useState(false);
  const [base, setBase] = useState<Base | null | undefined>(undefined);
  useEffect(() => {
    let live = true;
    loadBase(reader).then((b) => live && setBase(b), () => live && setBase(null));
    return () => { live = false; };
  }, [reader]);
  const key = subjects.join("|");
  // The last drawing stays until the next one is ready, so the pane is never blank.
  const [shown, setShown] = useState<Around | null>(null);
  const [failed, setFailed] = useState(false);
  useEffect(() => {
    if (!base || !subjects.length) return;
    let live = true;
    setFailed(false);
    around(reader, base, [...subjects]).then((a) => live && setShown(a), () => live && setFailed(true));
    return () => { live = false; };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [reader, base, key]);

  // The reading position, kept by value so that a new array with the same lines changes nothing.
  const atKey = position ? `${position[0]}-${position[1]}` : "";
  const at = useMemo(() => (atKey ? atKey.split("-").map(Number) as [number, number] : null), [atKey]);
  const firstLine = useMemo(() => {
    const at = new Map<string, number>();
    for (const row of base?.map.papers?.[paper] ?? []) {
      if (!row.lines) continue;
      for (const name of Object.keys(row.bindings)) at.set(name, Math.min(at.get(name) ?? Infinity, row.lines[0]));
    }
    return at;
  }, [base, paper]);

  const cards = useMemo(() => {
    const out = new Map<string, FGCard>();
    if (!shown || !base) return out;
    for (const d of shown.decls.values()) {
      let role: FGRole, kicker: string | undefined;
      if (d.onMap) {
        const statements = Object.entries((base.map.cards[d.name] as any).statements ?? {}) as [string, any][];
        const reviewed = statements.filter(([, v]) => v.review === "current" && v.relation !== "unassessed").map(([id]) => id)
          .sort((a, b) => STATEMENT_ORDER.indexOf(a.split("-")[0]) - STATEMENT_ORDER.indexOf(b.split("-")[0]));
        const lead = reviewed[0];
        const definition = !!d.kind && DEFINITION_KINDS.has(d.kind);
        role = definition ? "definition" : lead && NUMBERED.has(lead.split("-")[0]) ? "result" : "step";
        // The printed number, with the reviewed relation when the Lean is not an exact match.
        const relation = lead ? (base.map.cards[d.name] as any).statements[lead].relation : null;
        kicker = lead ? kindLabel(lead, base.statementKinds[lead] ?? "") + (relation === "stronger" ? ", stronger in Lean" : relation === "partial" ? ", partial match" : "") : undefined;
      } else if (d.kind && DEFINITION_KINDS.has(d.kind)) { role = "definition"; kicker = "Lean definition"; }
      else role = "helper";
      // Grouping: the topic whose colour the declaration's phrases carry in this paper; without
      // one, the top folder of its Lean file (or the file itself at the top). A large group divides by
      // Lean file.
      const topic = layer?.byName.get(d.name)?.[0]?.topic;
      const topicName = topic ? layer?.topics.find((t) => t.id === topic)?.name : undefined;
      const file = d.source?.replace(/^lean\/(QuarticQuery|QuarticCorpus)\//, "");
      const top = file?.includes("/") ? file.slice(0, file.indexOf("/")) : undefined;
      const first = firstLine.get(d.name);
      const seen = first == null || !at ? undefined : first < at[0] ? "before" : first > at[1] ? "later" : "here";
      out.set(d.name, { id: d.name, title: d.plain, name: d.name.replace(/^QuarticQuery\./, ""), role, kicker, tone: topic ? tone(topic) : undefined, seen,
        topic: topicName ?? (top ? `${top}/` : file),
        // A large group divides by Lean file, named by its own name so that it fits a column.
        section: file?.slice(file.lastIndexOf("/") + 1) });
    }
    return out;
  }, [shown, base, layer, tone, firstLine, at]);
  const card = useCallback((id: string) => cards.get(id), [cards]);
  // Only a declaration is previewed in the dock; a group head under the pointer leaves it as it is.
  const hoverCard = useCallback((id: string | null) => onHover(id && cards.has(id) ? id : null), [cards, onHover]);
  const subjectSet = useMemo(() => new Set(key.split("|")), [key]);
  // A paragraph under the pointer lights the declarations its most specific passages bind.
  const lit = useMemo(() => {
    if (!hover) return [];
    if (hover.names) return hover.names;
    const [a, b] = hover.lines!;
    const rows = (base?.map.papers?.[paper] ?? []).filter((r) => r.lines && r.lines[0] <= b && a <= r.lines[1]);
    if (!rows.length) return [];
    const width = (r: { lines?: [number, number] }) => r.lines![1] - r.lines![0];
    const least = Math.min(...rows.map(width));
    return [...new Set(rows.filter((r) => width(r) === least).flatMap((r) => Object.keys(r.bindings)))];
  }, [hover, base, paper]);
  // A title is typeset; one whose formula is too long for a node in a column is shown in its plain
  // words, which wrap, so that no formula runs past the node.
  const renderTitle = useCallback((c: FGCard) => {
    const text = shown?.decls.get(c.id)?.title ?? c.title;
    const longest = Math.max(0, ...[...text.matchAll(/\$([^$]+)\$/g)].map((m) => m[1].length));
    return longest > 22 && !subjectSet.has(c.id) ? <>{c.title}</> : <Title text={text} />;
  }, [shown, subjectSet]);

  if (base === null) return <p className="sgraph__state">This edition’s proof map is not current, so the graph is not drawn. The Lean and passage views still answer for each paragraph.</p>;
  if (!shown) return <p className="sgraph__state" role="status">{failed ? "The graph for this place could not be loaded." : "Drawing the graph…"}</p>;

  const drawn = shown.subjects;
  const isSubject = new Set(drawn);
  const users = new Set(shown.edges.filter((e) => isSubject.has(e.to) && !isSubject.has(e.from)).map((e) => e.from));
  const uses = new Set(shown.edges.filter((e) => isSubject.has(e.from) && !isSubject.has(e.to) && !users.has(e.to)).map((e) => e.to));
  if (narrow && !combined && !unfolded) {
    const first = cards.get(drawn[0]);
    return (
      <div className="sgraph__strip">
        <p><span className="sgraph__strip-k">{drawn.length > 1 ? `${drawn.length} steps` : first?.kicker ?? (first ? FG_ROLES[first.role].one : "Graph")}</span>{" "}
          {drawn.length === 1 && first ? <Title text={shown.decls.get(drawn[0])?.title ?? first.title} /> : null}
          <span className="sgraph__strip-n"> · uses {uses.size} · used by {users.size}</span></p>
        <button type="button" className="textbutton" onClick={() => setUnfolded(true)}>Show the graph</button>
      </div>
    );
  }
  const routeNote = shown.route === null ? "No chain of uses in the proof map joins this to the main result." : shown.route.length === 0 ? "This is the main result." : undefined;
  return (
    <div className="sgraph">
      {narrow && !combined && <p className="sgraph__fold"><button type="button" className="textbutton" onClick={() => setUnfolded(false)}>Fold the graph</button></p>}
      <FocusGraph embeddedHeader={SOURCE_READER ? { title: "Dependencies", action: null } : undefined} subjects={drawn} card={card} edges={shown.edges} route={shown.route && shown.route.length ? shown.route : null} routeNote={routeNote}
        label={label} lit={lit} held={held} onSubject={onSubject} onHover={hoverCard} renderTitle={renderTitle}
        roles={{ helper: { one: "Lean helper" } }} manyLabel="Steps linked to this paragraph" />
    </div>
  );
}
