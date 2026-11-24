import { readFileSync } from "node:fs";
import { defineConfig, loadEnv, type Plugin } from "vite";
import react from "@vitejs/plugin-react";

const LIBRARY_HOME = "https://wcook04.github.io/library/";

/**
 * The Library's source reader names its edition at build time. Its page carries the masthead in the
 * HTML, so the Reading library and the paper are linked before the script runs or without it; the
 * app replaces this markup with the same header when it starts.
 */
function sourceReaderMasthead(): Plugin {
  const mark = readFileSync(new URL("./src/family/quartic.svg", import.meta.url), "utf8").trim();
  const header = `<header class="site site--source"><span class="source-lockup">`
    + `<a class="source-lockup__library" href="${LIBRARY_HOME}" translate="no"><span class="source-paper-mark" aria-hidden="true">${mark}</span>`
    + `<span class="source-lockup__long">Reading library</span><span class="source-lockup__short">Library</span></a>`
    + `<span class="source-lockup__rule" aria-hidden="true"></span>`
    + `<a class="site__name" href="/library/quartic/">Quartic query separation</a></span>`
    + `<div class="source-reader-actions"><a class="fam-lockup__home source-reader-owner" href="https://wcook04.github.io/" rel="author"><span class="fam-lockup__owner" translate="no">Will Cook</span></a></div></header>`;
  return {
    name: "source-reader-masthead",
    transformIndexHtml: (html) => html.replace('<div id="root"></div>', `<div id="root">${header}</div>`),
  };
}

// VITE_BASE_PATH is the folder the site is served from, such as /quartic/.
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "VITE_");
  const base = env.VITE_BASE_PATH ?? process.env.VITE_BASE_PATH ?? "/";
  const sourceReader = !!(env.VITE_READING_EDITION ?? process.env.VITE_READING_EDITION);
  return {
    base,
    build: { assetsInlineLimit: 0, copyPublicDir: false },
    // The reading client lives in the repository's tools/ and is bundled from there.
    server: { fs: { allow: [".."] } },
    plugins: [react(), ...(sourceReader ? [sourceReaderMasthead()] : [])],
  };
});
