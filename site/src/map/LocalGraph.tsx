// A declaration that the passage's argument map does not draw, with its Lean neighbours:
// the project declarations it uses and those that use it, from the edition's recorded
// dependency graph (the same records as the Lean panel's "Uses" and "Used by"). Drawn by
// the reader's map engine with the Graph tab's tiles, spacing and styling.
import { useEffect, useMemo, useRef, useState } from "react";
import type { Edition } from "../app/edition";
import type { ArgEdge, ArgGraph, ArgNode, LinkKind, Origin } from "../model/graph";
import { ArgumentTree, type MapViewHandle } from "./ArgumentTree";
import { INSETS, PANE_METRICS, TILE_W, TITLE_SIZES, useTileHeights } from "./GraphPane";
import "./tokens.css";
import "./graph.css";

const ROOT = "local:neighbourhood";
const CAP = 8;
const LEAN: Origin = { family: "lean", label: "Lean", slot: 3, place: null, locator: null, url: null };
const EDGE_KIND: Record<string, LinkKind> = { value: "supports", type: "lean_type_dependency", structural: "lean_structural_dependency" };

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

function localGraph(local: Local, title: (n: string) => { title: string; title_plain: string } | undefined): ArgGraph {
  const nodes = new Map<string, ArgNode>();
  const blank = { papers: {}, region: ROOT, passedExtraction: true };
  nodes.set(ROOT, { ...blank, id: ROOT, ref: ROOT, kind: "goal", kindLabel: "Lean neighbourhood",
    label: local.users.length ? "Declarations that use it, and what it uses" : "What this declaration uses", status: "external", origin: LEAN });
  const card = (n: string) => {
    const kind = local.kinds[n] ?? "def";
    const t = title(n);
    const theorem = kind === "theorem" || kind === "lemma";
    nodes.set(n, { ...blank, id: n, ref: n, kind: "declaration", kindLabel: theorem ? "Theorem" : "Definition",
      label: t?.title_plain ?? n.split(".").pop()!, math: t?.title, declaration: n,
      shape: theorem ? "theorem" : "definition", leanFill: "whole", status: "kernel_checked", origin: LEAN });
  };
  [local.name, ...local.users.map((u) => u.name), ...local.uses.map((u) => u.name)].forEach(card);
  const edges: ArgEdge[] = [];
  const add = (from: string, to: string, kind: LinkKind, semanticClass: string = kind) =>
    edges.push({ key: `${from}→${to}→${kind}`, from, to, kind, linkIds: [`${from}→${to}`], scoped: false, semanticClass });
  if (local.users.length) for (const u of local.users) { add(ROOT, u.name, "formalizes", "neighbourhood_context"); add(u.name, local.name, EDGE_KIND[u.kind]); }
  else add(ROOT, local.name, "formalizes", "neighbourhood_context");
  for (const u of local.uses) add(local.name, u.name, EDGE_KIND[u.kind]);
  const out = new Map<string, ArgEdge[]>(), into = new Map<string, ArgEdge[]>();
  for (const id of nodes.keys()) { out.set(id, []); into.set(id, []); }
  for (const e of edges) { out.get(e.from)!.push(e); into.get(e.to)!.push(e); }
  const members = [...nodes.keys()];
  return {
    origins: [{ family: "lean", label: "Lean", slot: 3, count: nodes.size - 1 }], cites: [], nodes, order: members, edges, out, in: into,
    regions: [{ id: ROOT, title: "Lean neighbourhood", goal: ROOT, members }], regionOf: new Map(members.map((id) => [id, ROOT])),
    goals: [ROOT], cyclic: new Set(), boundaries: new Map(),
  };
}

export function LocalGraph({ edition, name, titles, onOpenLean, onBack }: { edition: Edition; name: string;
  titles: Record<string, { title: string; title_plain: string }>; onOpenLean(name: string): void; onBack(): void }) {
  const [local, setLocal] = useState<Local | null>(null);
  const [failed, setFailed] = useState(false);
  const [index, setIndex] = useState<Record<string, { title: string; title_plain: string }>>({});
  const tree = useRef<MapViewHandle>(null);
  const body = useRef<HTMLDivElement>(null);
  useEffect(() => {
    let live = true;
    setLocal(null); setFailed(false);
    neighbours(edition.reader as any, name).then((l) => live && setLocal(l), () => live && setFailed(true));
    (edition.reader as any).declarationTitles().then((r: any) => live && setIndex(r.titles ?? {}), () => {});
    return () => { live = false; };
  }, [edition, name]);
  const graph = useMemo(() => local && localGraph(local, (n) => titles[n] ?? index[n]), [local, titles, index]);
  const tileHeight = useTileHeights(graph ?? { nodes: new Map() } as ArgGraph);
  // Frame the whole neighbourhood once laid out, and again when the half changes size.
  useEffect(() => {
    const el = body.current;
    if (!el || !graph) return;
    let timer = window.setTimeout(() => tree.current?.fitAll(false), 120);
    const observer = new ResizeObserver(() => { window.clearTimeout(timer); timer = window.setTimeout(() => tree.current?.fitAll(false), 120); });
    observer.observe(el);
    return () => { observer.disconnect(); window.clearTimeout(timer); };
  }, [graph]);
  const more = local && [local.moreUsers ? `${local.moreUsers} more ${local.moreUsers === 1 ? "declaration uses" : "declarations use"} it` : "",
    local.moreUses ? `it uses ${local.moreUses} more` : ""].filter(Boolean).join("; ");
  return (
    <section className="graph local-graph" aria-label="This declaration and its Lean neighbours">
      <div className="local-graph__head">
        <p className="local-graph__title" role="heading" aria-level={2}>This declaration and its Lean neighbours <span>(not in the passage’s argument map)</span></p>
        <button type="button" className="gbtn" onClick={onBack}>Show the passage map</button>
      </div>
      <div className="graph__canvas local-graph__canvas" ref={body}>
        {failed ? <p className="pending">The Lean neighbours could not be loaded.</p>
          : !graph ? <p className="pending" role="status">Reading the Lean neighbours…</p>
          : <ArgumentTree ref={tree} graph={graph} goal={ROOT} insets={INSETS} persist={false} mode="overview" tileWidth={TILE_W}
              tileHeight={tileHeight} denseMetrics={PANE_METRICS} oneCardEach fitMax={1.15} rootTile={{ w: 320, h: 64 }} rootWord="Lean neighbourhood" selected={name}
              frameSelection={false} litIds={null} rootExcerpt={null}
              onSelect={(id) => { if (id && id !== ROOT && id !== name) onOpenLean(id); }} onTrace={() => {}} titleSizes={TITLE_SIZES} />}
      </div>
      {more && <p className="local-graph__more">Most specific shown first; {more}. The Lean tab lists them all.</p>}
    </section>
  );
}
