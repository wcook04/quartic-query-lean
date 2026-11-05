// Validate authored declaration titles with the same KaTeX package and options
// as src/text/math.ts. A release must not depend on the reader's TeX fallback.
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import katex from "katex";

const defaultPath = fileURLToPath(new URL("../../docs/reading_declaration_titles.json", import.meta.url));
const args = process.argv.slice(2);
if (args.length > 1) {
  console.error("Usage: node scripts/check-title-math.mjs [titles.json]");
  process.exit(1);
}
const path = args.length ? resolve(args[0]) : defaultPath;
const errors = [];
let formulaCount = 0;
let titleCount = 0;

function checkTitle(name, value) {
  titleCount++;
  const paired = Array.isArray(value);
  if (!(typeof value === "string" || (paired && value.length === 2 && value.every(v => typeof v === "string")))) {
    errors.push(`${name}: expected an English string or [rich title, plain title]`);
    return;
  }
  const rich = paired ? value[0] : value;
  const plain = paired ? value[1] : value;
  if (!rich.trim() || !plain.trim()) errors.push(`${name}: titles must be nonempty`);
  if (rich.includes("`") || plain.includes("`")) errors.push(`${name}: backtick markup is not permitted`);
  if (plain.includes("$")) errors.push(`${name}: plain titles must not contain math delimiters`);
  if (!paired) return;

  // Match titleHtml's inline delimiters, while also rejecting unmatched dollars,
  // empty formulas and display delimiters that the title renderer cannot read.
  const spans = [...rich.matchAll(/\$([^$]+)\$/g)];
  if (!spans.length) errors.push(`${name}: a paired title must contain inline $…$ math`);
  if (rich.includes("$$") || rich.replace(/\$([^$]+)\$/g, "").includes("$")) {
    errors.push(`${name}: use complete, nonempty inline $…$ math spans`);
  }
  for (const [index, span] of spans.entries()) {
    const tex = span[1];
    if (!tex.trim()) {
      errors.push(`${name}: formula ${index + 1} is empty`);
      continue;
    }
    formulaCount++;
    try {
      katex.renderToString(tex, {
        displayMode: false,
        throwOnError: true,
        trust: false,
        strict: "ignore",
        output: "htmlAndMathml",
      });
    } catch (error) {
      errors.push(`${name}: formula ${index + 1} (${tex}): ${error.message}`);
    }
  }
}

try {
  const document = JSON.parse(readFileSync(path, "utf8"));
  if (!document || typeof document !== "object" || Array.isArray(document)) {
    throw new Error("expected an object containing source_snapshot_sha256 and titles");
  }
  if (!/^[a-f0-9]{64}$/.test(document.source_snapshot_sha256 ?? "")) {
    errors.push("source_snapshot_sha256: expected a 64-character lowercase hexadecimal hash");
  }
  if (!document.titles || typeof document.titles !== "object" || Array.isArray(document.titles) || !Object.keys(document.titles).length) {
    errors.push("titles: expected a nonempty object keyed by declaration name");
  } else {
    for (const [name, value] of Object.entries(document.titles)) checkTitle(name, value);
  }
} catch (error) {
  errors.push(`${path}: ${error.message}`);
}

if (errors.length) {
  console.error(`Declaration title validation failed (${errors.length} errors):\n${errors.map(error => `- ${error}`).join("\n")}`);
  process.exitCode = 1;
} else {
  console.log(`Validated ${titleCount} declaration titles and ${formulaCount} inline formulas with KaTeX ${katex.version}.`);
}
