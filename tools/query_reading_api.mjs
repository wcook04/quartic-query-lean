// Headless access to the same captured selection API that a browser consumes.
import {readFile} from "node:fs/promises";
import {pathToFileURL, fileURLToPath} from "node:url";
import {resolve as absolute} from "node:path";
import {loadEditionResources, openReader as bundledReader} from "./reader.mjs";

export async function openLocalOrHTTP(location, {bundledClient = false} = {}) {
  const url = /^https?:/.test(location) ? new URL(location) : pathToFileURL(absolute(location));
  const request = async (address, options) => address.protocol === "file:"
    ? new Response(await readFile(fileURLToPath(address))) : fetch(address, options);
  if (bundledClient) return bundledReader(url, {fetch: request});
  const {manifest, readBytes} = await loadEditionResources(url, {fetch: request});
  const raw = Buffer.from(await readBytes("reader.mjs"));
  const {openReader} = await import("data:text/javascript;base64," + raw.toString("base64"));
  // Pass the immutable manifest so a concurrent export cannot switch our edition.
  return openReader(new URL(manifest.permalink, url), {fetch: request, expectedRevision: manifest.revision});
}

// Count the same highlighted sites a reader sees. A condensed arrow is complete
// only when every hop on every displayed variant has a location.
async function proofLineCoverage(reader) {
  const map = await reader.proofMap();
  if (map.currentness !== "current") return {revision: reader.revision, status: map.currentness};
  if (!map.use_site_resource) return {revision: reader.revision, status: "unavailable_in_edition"};
  const arrows = {full: 0, partial: 0, missing: 0};
  const seen = new Set();
  const hops = {};
  for (const edge of map.edges) {
    const path = await reader.proofPath(edge.from, edge.to);
    const steps = path.variants.flatMap(v => v.hops);
    const located = steps.filter(h => h.evidence.sites.length).length;
    const category = located === 0 ? "missing" : located === steps.length ? "full" : "partial";
    arrows[category]++;
    for (const step of steps) {
      const key = JSON.stringify([step.from, step.kind, step.to]);
      if (seen.has(key)) continue;
      seen.add(key);
      const status = step.evidence.status;
      hops[status] = (hops[status] ?? 0) + 1;
    }
  }
  return {revision: reader.revision, edition: reader.permalink, arrows, distinct_hops_by_evidence: hops};
}

if (process.argv[1] && import.meta.url === pathToFileURL(absolute(process.argv[1])).href) {
  const [location, paper, selector, hash, firstKind] = process.argv.slice(2);
  const coverage = paper === "--proof-line-coverage";
  if (!location || !paper || (coverage ? selector != null : !selector) || (paper === "--proof-path" && !hash)) {
    console.error("Usage: node tools/query_reading_api.mjs MANIFEST PAPER ID | PAPER LINE DOCUMENT_SHA256 | original PAGE PDF_SHA256 | --statement ID | --declaration NAME | --journey ID | --proof-line-coverage | --proof-path FROM TO [value|type|structural]");
    process.exitCode = 2;
  } else {
    const reader = await openLocalOrHTTP(location, {bundledClient: coverage || paper === "--proof-path"});
    const result = coverage ? await proofLineCoverage(reader)
      : paper === "--proof-path" ? await reader.proofPath(selector, hash, firstKind)
      : paper === "--journey" ? await reader.journey(selector)
      : paper === "--statement" ? await reader.statementReview(selector)
      : paper === "--declaration" ? await reader.fromDeclaration(selector)
      : await reader.resolve(/^\d+$/.test(selector)
        ? {paper, [reader.documents[paper]?.format === "pdf" ? "page" : "line"]: Number(selector), documentSha256: hash} : {paper, id: selector});
    console.log(JSON.stringify(result, null, 2));
  }
}
