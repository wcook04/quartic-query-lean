// Load the edition's proof map once and draw the whole of it. A map from a different
// edition is never substituted: stale or absent maps say so.
import { useMemo } from "react";
import type { Edition } from "../app/edition";
import { useAsync } from "../app/useAsync";
import { GraphPane } from "./GraphPane";
import { proofGraph, type ProofMap } from "./fromProofMap";

export function ProofPane({ edition, lit, onSelect, onOpenLean, selectedEdge, onEdge, onBack }: { edition: Edition; lit: readonly string[]; onSelect(name: string): void; onOpenLean(name: string): void; selectedEdge: string | null; onEdge(key: string): void; onBack(): void }) {
  const map = useAsync(() => edition.reader.proofMap() as Promise<ProofMap>, [edition]);
  const graph = useMemo(() => (map.state === "ready" && map.value.currentness === "current" ? proofGraph(map.value) : null), [map]);
  if (map.state === "loading") return <p className="pending" role="status">Loading the Lean graph…</p>;
  if (map.state === "failed") return <div className="failed" role="alert"><p>The Lean graph could not be loaded: {map.error.message}</p></div>;
  if (!graph)
    return (
      <div className="failed">
        <p>{map.value.currentness === "stale" ? "This edition’s Lean graph was recorded for an earlier Lean source, so it is not shown." : "This edition has no Lean graph."} The evidence for each passage is still available.</p>
      </div>
    );
  return <GraphPane reader={edition.reader} map={map.value} graph={graph} lit={lit} onSelect={onSelect} onOpenLean={onOpenLean} selectedEdge={selectedEdge} onEdge={onEdge} onBack={onBack} />;
}
