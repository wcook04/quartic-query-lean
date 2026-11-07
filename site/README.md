# Quartic reader website

A paper-first reader for OpenAI’s nearly quartic separation, the project’s three
accounts of its proof, and the Lean development. All mathematics, links and
evidence come from one immutable reading edition built by
`make reading-web`; this site adds presentation only.

```sh
npm install
npm run dev          # links ../build/reading-api into public/ and serves it
VITE_BASE_PATH=/quartic-query-lean/ npm run build   # dist/ plus a copy of the edition
```

The site bundles [the reading client](../tools/reader.mjs) and opens the edition
under `<base>/reading-api/v1/`. A shared link may name only an
`edition-<sha256>.json` file; every byte the site shows is checked against the
edition manifest. Figures and PDFs are displayed from verified Blob URLs.

| Directory | Owns |
| --- | --- |
| `src/app` | Edition loading, hash routes, the reading desk, paper switcher and history-entry scroll/focus restoration |
| `src/home` | The three board scenes, the exponent control and the proof outline |
| `src/paper` | The four papers as edition HTML, their own contents, and the original PDF pane (pdf.js) |
| `src/inspect` | Passage, statement comparison, Lean declaration and journey panels |
| `src/lean`, `src/text` | Lean listings and KaTeX typesetting |

Adapted code carries its upstream notice: KaTeX handling from
[lean-exposition](https://github.com/wcook04/lean-exposition) and the Lean tokenizer
and PDF approach from [proof-reader](https://github.com/wcook04/proof-reader), both Apache-2.0.

The expert companion is the first reading entrance. The four tabs describe the
documents' jobs: expert companion, worked exposition, full proof reconstruction
and OpenAI original. Switching a tab restores that paper's own position. Following
a matched passage keeps a visible return to the origin, including its scroll,
selection and open proof view. Restoration adapts Lean Exposition's history and
late-content handling and stops immediately when the reader takes control.

On desktop Graph opens beside the paper. SK’s Lean-graph neighborhood isolates the
linked passage’s steps and lays out that subgraph; unlinked paragraphs keep the
last valid view. Whole proof expands the full graph, and the local view retains the real branching dependencies. Lean is the second tab; Passage offers alternative
explanations and statement comparisons. The graph has explicit zoom, full-bounds
fit and selected-step controls. A manual
camera survives switching views and resizing; Follow resumes movement with the
paper. Dependencies and helper lists follow the source listing.

Scrolling advances the graph at linked passages and leaves its last valid
neighborhood in place through unlinked prose. Clicking a different passage
focuses its graph; clicking the focused passage cycles Graph → Lean → Passage
→ Graph. A passage click does not permanently stop scroll following.

OpenAI's [pinned source and conversion checks](../docs/original_source/README.md)
produce a native reading copy while retaining the unchanged PDF. The original
keeps its authorship, numbering and section structure. The three accompanying
PDFs are admitted only with their exact source revision and accepted hashes.

## Published video

[Watch the explanation on YouTube](https://www.youtube.com/watch?v=3hZaKK0-leY) (27:13).
The title, link and paper-linked chapters are in [`docs/reading_routes.json`](../docs/reading_routes.json).
The reader exporter includes them in the immutable edition. The homepage uses
[`src/family/quartic-video-thumbnail.webp`](src/family/quartic-video-thumbnail.webp),
a local copy of the published thumbnail; `src/family/` owns these shared video
components and their maintained image assets. Generated `public/` and `dist/`
contents remain untracked.

The paper–proof separator adapts Proof Reader’s dock handle. Drag it, use the
arrow keys, or double-click to reset; the chosen split is remembered. Wider
reading columns use larger manuscript text, and contents move into their menu
when the paper pane becomes narrow.

The paper heading and manuscript share one reading measure, computed from
manuscript type size, across the closed and resizable proof views. Captions
and footnotes scale with that size. Linked-passage menus use the edition's
authored route titles and stay within the reading column. The account cards
emphasize the expert entrance, matching the first reading action.

The two paper menus form one native disclosure group. Escape dismisses the
menu before the proof pane; an outside pointer click or leaving the menu by
keyboard dismisses it too. Menus start below the entire toolbar, including
when its controls wrap. On phones, the covered paper and paper tabs are inert
while the proof is open; closing it returns focus to the selected passage.
The theme owner also updates the browser colour from the current page token.

Manuscript links have actual reader URLs: copy-link, middle-click and
Cmd/Ctrl-click open the intended paper or footnote separately. Ordinary clicks
retain the reading excursion and its Return control. An explicitly selected
older edition stays pinned in those URLs. Additional passage names come from
the same edition's existing argument index, including topics outside the
shorter route list.

Menu height is bounded by the visible paper pane rather than a fixed share of
the screen. A menu opens above its toolbar when space below is insufficient,
and repositions on resize. The last choice remains scrollable and clickable
on short phone screens.
