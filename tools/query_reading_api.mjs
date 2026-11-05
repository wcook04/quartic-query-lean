// Headless access to the same captured selection API that a browser consumes.
import {readFile} from "node:fs/promises";
import {pathToFileURL, fileURLToPath} from "node:url";
import {resolve as absolute} from "node:path";
import {createHash} from "node:crypto";

export async function openLocalOrHTTP(location) {
  const url = /^https?:/.test(location) ? new URL(location) : pathToFileURL(absolute(location));
  const request = async address => address.protocol === "file:"
    ? new Response(await readFile(fileURLToPath(address))) : fetch(address);
  const manifest = await (await request(url)).json();
  const entry = manifest.resources["reader.mjs"];
  const raw = Buffer.from(await (await request(new URL(entry.href, url))).arrayBuffer());
  if (createHash("sha256").update(raw).digest("hex") !== entry.sha256)
    throw new Error("Selection client differs from the edition manifest");
  const {openReader} = await import("data:text/javascript;base64," + raw.toString("base64"));
  // Pass the immutable manifest so a concurrent export cannot switch our edition.
  return openReader(new URL(manifest.permalink, url), {fetch: request, expectedRevision: manifest.revision});
}

if (process.argv[1] && import.meta.url === pathToFileURL(absolute(process.argv[1])).href) {
  const [location, paper, selector, hash] = process.argv.slice(2);
  if (!location || !paper || !selector) {
    console.error("Usage: node tools/query_reading_api.mjs MANIFEST PAPER ID | PAPER LINE DOCUMENT_SHA256 | original PAGE PDF_SHA256 | --declaration NAME | --journey ID");
    process.exitCode = 2;
  } else {
    const reader = await openLocalOrHTTP(location);
    const result = paper === "--journey" ? await reader.journey(selector)
      : paper === "--declaration" ? await reader.fromDeclaration(selector)
      : await reader.resolve(/^\d+$/.test(selector)
        ? {paper, [reader.documents[paper]?.format === "pdf" ? "page" : "line"]: Number(selector), documentSha256: hash} : {paper, id: selector});
    console.log(JSON.stringify(result, null, 2));
  }
}
