# Quartic reader website

A paper-first reader for OpenAI’s nearly quartic separation, the project’s three
accounts of its proof, and the Lean development. All mathematics, links and
evidence come from one immutable reading edition built by
`make reading-web`; this site adds presentation only.

```sh
npm install
npm run dev          # links ../build/reading-api into public/ and serves it
VITE_BASE_PATH=/quartic/ npm run build   # dist/ plus a copy of the edition
```

The site bundles [the reading client](../tools/reader.mjs) and opens the edition
under `<base>/reading-api/v1/`. A shared link may name only an
`edition-<sha256>.json` file; every byte the site shows is checked against the
edition manifest. Figures and PDFs are displayed from verified Blob URLs.

| Directory | Owns |
| --- | --- |
| `src/app` | Edition loading, hash routes, the reading desk and paper switcher |
| `src/home` | The three board scenes, the exponent control and the proof outline |
| `src/paper` | The manuscript pane (edition HTML) and the original PDF pane (pdf.js) |
| `src/inspect` | Passage, statement comparison, Lean declaration and journey panels |
| `src/lean`, `src/text` | Lean listings and KaTeX typesetting |

Adapted code carries its upstream notice: KaTeX handling from
[lean-exposition](https://github.com/wcook04/lean-exposition) and the Lean tokenizer
and PDF approach from [proof-reader](https://github.com/wcook04/proof-reader), both Apache-2.0.

## Published video

[Watch the explanation on YouTube](https://www.youtube.com/watch?v=3hZaKK0-leY) (27:13).
The title, link and paper-linked chapters are in [`docs/reading_routes.json`](../docs/reading_routes.json).
The reader exporter includes them in the immutable edition. The homepage uses
[`src/family/quartic-video-thumbnail.webp`](src/family/quartic-video-thumbnail.webp),
a local copy of the published thumbnail; `src/family/` owns these shared video
components and their maintained image assets. Generated `public/` and `dist/`
contents remain untracked.
