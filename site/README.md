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
| `src/results` | The index of OpenAI's statements with their Lean labels, as a page and a homepage band |
| `src/family` | The header lockup, theme switch, the two videos and the footer shared with Will Cook's other sites |
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

On desktop Graph opens to the right of the paper. SK’s Lean-graph neighborhood isolates the
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

## Colours in the graph, and figures

Amber marks the paragraph being read and nothing else: a card the paragraph
relies on has an amber fill and border, and a line between two such cards is
amber. The selected card, whose Lean is open in the Lean tab, has an outline in
the text ink, and the route from it to the main result is a thicker ink line.
The key under the map lists each card and line state that is on screen. A click
on a card selects it and opens a summary under the map with its label against the
paper and its Lean statement; a second click, or the summary's button, opens the
Lean tab. The
pane names the selected paragraph above its three tabs.

Figures in the papers are drawn as dark ink on white. `styles.css` blends them
into the page: by day white multiplies into the paper, and at night lightness is
inverted with the hues kept.

## Published videos

[The short video](https://www.youtube.com/watch?v=swDOmHq8NrY) (1:50) and
[the full video](https://www.youtube.com/watch?v=u6iRqc1ToZ0) (34:02) are on YouTube.
The short video's title, address and length come from
[`src/family/family.json`](src/family/family.json), an unchanged copy of the
family registry. The full video's title, link and paper-linked chapters are in
[`docs/reading_routes.json`](../docs/reading_routes.json), and the reader exporter
includes them in the immutable edition. [`src/family/films.ts`](src/family/films.ts)
names both films and their stills: `quartic-short-thumbnail*.webp` and
`quartic-video-thumbnail*.webp` are local copies of the published thumbnails at
1280 and 640 pixels. `src/family/` owns these shared video components and their
maintained image assets. Generated `public/` and `dist/` contents remain untracked.

The homepage shows the short video three ways: a one-line link under the hero's
reading actions, the lead picture of the "Two videos" band, and the first row of
the header's Videos menu. The full video is the smaller picture in that band,
over its chapters, and the menu's second row. The Videos menu
([`src/family/VideoMenu.tsx`](src/family/VideoMenu.tsx)) is a native popover in
the site header, so both videos are one click from the reading desk without
taking room from the paper.

## Results and their Lean statements

`#/results` ([`src/results/`](src/results/)) lists every statement of OpenAI's
paper that the edition indexes, in the paper's order, with the label its leading
comparison carries (exact match, stronger in Lean or partial match), the page and
the compared Lean declaration. A row opens OpenAI's paper at that statement with
the comparison open in the pane. The homepage band shows the same counts and the
theorems, propositions and lemmas. The page reads `corpus/statements.json` and
`selection/original.json` from the edition and adds no judgment of its own.

Each chapter names a reading `route` (opening the reconstruction at that
passage), a whole reading `page` such as `verification`, or only a `title` for
a chapter with no paper counterpart. The homepage lists them as an index keyed
by time next to the video, matching the chapters in the YouTube description.

The homepage's “A paragraph and the Lean linked to it” band shows real captures of this
reader, `src/home/reader-passage-{dark,light}-{1440,2880}.webp`, adapted from
the SK site's reader still. They show
`#/read/expert?s=expert%2Fweight%2F0&v=graph` at 1440×790, captured with
Playwright at device scale 2 with `localStorage["quartic-theme"]` set to each
scheme. Recapture them when the reader's appearance changes.

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
The Lean and graph button at the end of the paper tabs opens and closes the
proof pane. On phones the pane is a sheet over the lower paper, so the selected
paragraph stays visible above it; Back to paper closes it.

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
