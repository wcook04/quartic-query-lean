// Make the generated reading edition available to the site. In development a
// symlink serves ../build/reading-api; a build copies it next to the bundle.
import { cpSync, existsSync, lstatSync, rmSync, symlinkSync } from "node:fs";
import { resolve } from "node:path";

const source = resolve("..", "build", "reading-api");
if (!existsSync(resolve(source, "v1", "index.json"))) {
  console.error("No reading edition at ../build/reading-api. Run `make reading-api` first.");
  process.exit(1);
}
const copy = process.argv.indexOf("--copy");
if (copy >= 0) {
  const target = resolve(process.argv[copy + 1], "reading-api");
  rmSync(target, { recursive: true, force: true });
  cpSync(source, target, { recursive: true, dereference: true });
  console.log(`Copied the reading edition to ${target}`);
} else {
  const link = resolve("public", "reading-api");
  if (existsSync(link) || (() => { try { return lstatSync(link).isSymbolicLink(); } catch { return false; } })()) rmSync(link, { recursive: true, force: true });
  symlinkSync(source, link, "dir");
  console.log("Linked public/reading-api to ../build/reading-api");
}
