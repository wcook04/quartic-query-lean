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
| `src/home` | The three board scenes, the levels band, the exponent control and the proof outline |
| `src/results` | The index of OpenAI's statements with their Lean labels, as a page and a homepage band |
| `src/family` | The header lockup, theme switch, the two videos and the footer shared with Will Cook's other sites |
| `src/paper` | The four papers as edition HTML, their own contents, and the original PDF pane (pdf.js) |
| `src/inspect` | Passage, statement comparison, Lean declaration and journey panels, and the Comparator evidence that opens under a directly checked declaration |
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

## Phrases, topics and reading notes

The expert companion, the exposition and the reconstruction carry the edition's
[phrase ties](../docs/reading_api.md#phrase-ties-topics-and-reading-notes), adapted from
Proof Reader's Physlib Gauge theory map ([`src/paper/phrases.ts`](src/paper/phrases.ts),
[`src/inspect/PhraseCards.tsx`](src/inspect/PhraseCards.tsx)). Each phrase that states a Lean
declaration is underlined in its topic's colour; two shades per topic alternate so
neighbouring phrases differ. The hues keep clear of amber, the cyan, violet and grey of the
statement matches, mauve and red; every two topics of a paper differ by CIEDE2000 ΔE ≥ 15 over the page in both themes (`tests/test_topic_colours.py`). Hovering a phrase names its topic and declarations and
lights their cards; hovering a card lights its phrase. Clicking a phrase selects its
paragraph and declaration and keeps the open tab: the Lean tab shows the declaration with the
tied lines lit; the Graph tab splits ([`src/inspect/PhraseSplit.tsx`](src/inspect/PhraseSplit.tsx)):
the graph stays above, framed on the declaration's card and its drawn neighbours; when the map
does not draw it, the top half draws the declaration with the project declarations it uses and
those that use it ([`src/map/LocalGraph.tsx`](src/map/LocalGraph.tsx), at most eight each,
most specific first), with a button back to the passage map. Below a draggable divider the
phrase's card and Lean, with the tied lines lit, scroll on their own, one tab per declaration
when the phrase has several. The close button or Escape restores the whole graph; on a phone the graph folds to one line above the card. The
Passage tab puts the clicked phrase's card first, then the paragraph's other phrases. A card gives the paper's own title, the quoted words, what the Lean row does with
them, the comparison with these words in plain words ("Lean states less: …", marked
AI-assessed) and the reading note (marked AI-drafted), typeset with KaTeX. The comparison
with OpenAI's statement keeps its exact, stronger and partial marks under "Matches OpenAI's
statement". The contents rail and the Topic colours menu give the key; every listed section
and subsection in the rail carries the colour dashes of the topics whose tied phrases it
contains, its subsections' included.

Whenever the graph's subject changes (a passage followed, a card or phrase chosen) the camera
moves for 250 ms (none under reduced motion) to frame the selected card with its drawn
neighbours, or the passage's graph, at a readable scale; when that cannot fit, the selected
card or the passage's own steps stay centred. A manual pan or zoom holds until the next
subject change; a resize or a dragged divider frames the subject again.

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

## One argument at five levels

The homepage band under the opening screen ([`src/home/LevelsBand.tsx`](src/home/LevelsBand.tsx),
adapted from lean-exposition's `LevelsBand.tsx`) lists five levels: the Lean proof,
OpenAI's paper, the full proof reconstruction, the expert companion and the worked
exposition. Every number in it is counted from the edition's `selection/proof-map.json`
when the page loads: the steps are the declarations the main theorem reaches in that map
(the graph the reader's Graph pane draws), a level's count is its `paper_cards` within
them, its passage count is its rows in `papers`, and the source-file count is the distinct
`source` files of those steps.

The drawing uses the map engine in `src/map/engine`, read from left to right. It keeps
OpenAI's Theorem 1.1 and the steps the expert companion or the worked exposition is
linked to, and joins two drawn steps when the left one uses the right one in Lean,
directly or through steps not drawn (lean-exposition's `contract`). Choosing a level
keeps the drawn steps that level is linked to, and a card opens that paper at its first
passage linked to the step, with the step's Lean. On phones the drawing is hidden and the
levels and links remain.

The thumbnails `src/home/levels/{expert,exposition,reconstruction,original}.webp` are
captures of this reader at `#/read/<paper>` in the light scheme: a 1000×1300 window,
the site bar, paper tabs, toolbar and byline hidden, the page at `zoom: 0.5`, cropped
from the paper title to an 8.5:11 page over the manuscript column, and resized to
240×310. Recapture them when a paper's opening changes.

## Results and their Lean statements

`#/results` ([`src/results/`](src/results/)) lists every statement of OpenAI's
paper that the edition indexes, in the paper's order, with the label its leading
comparison carries (exact match, stronger in Lean or partial match), the page and
the compared Lean declaration. A row opens OpenAI's paper at that statement with
the comparison open in the pane. The homepage band shows the same counts and the
theorems, propositions and lemmas. The page reads `corpus/statements.json` and
`selection/original.json` from the edition and adds no judgment of its own.

A partial match is a theorem Lean accepts in full that covers less than the
paper's statement. In the comparison, Lean and passage panels its mark says
which kind: "Proves part of the statement" when the theorem has no remaining
hypothesis and states fewer conclusions, "Proved with an extra hypothesis" when
the review records an open assumption. The results index and its filter keep the
one category, "Partial match". The words are chosen in
[`relationWord`](src/inspect/evidence.tsx) from the comparison's
`open_assumptions`.

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
