# Website reading data

Run `make reading-api` in a full Git checkout with Python 3.10 or newer.
Serve the resulting `build/reading-api/` directory from any static host.
For a local client, run `python3 -m http.server 8000 --directory build/reading-api`
and fetch `/v1/index.json`. The build needs the historical commits cited by the papers.
Use `python3 tools/build_reading_api.py --check` to validate draft edits before committing.
The export accepts inputs matching the captured commit.

To include the accepted PDFs, pass the release render directory to
`python3 tools/build_reading_api.py --output build/reading-api/v1 --pdf-directory /path/to/final`.
Its expert, exposition and record subdirectories hold the native renderer outputs.
The exporter checks all three PDF hashes against the print edition, verifies its
adjudication and compares the paper sources with the pinned print revision.
A Markdown-only build returns an empty `downloads` object. A build with PDFs
returns the three download resources in `reading.json`.

## Open a paper on a question

Load the manifest once and resolve each logical resource through its `href`,
relative to the manifest URL. Each entry gives its byte length and SHA-256.
The compiler installs content-addressed files before replacing the manifest
atomically. A reader holding the old manifest can finish that edition.
Keep its objects when updating an existing host.

Start with `reading.json`. Its `entrances` are keyed by paper. Each names an audience,
asks the question that brings that reader here, gives a short preview, and lists
the first stops in order. The general mathematical reader starts with a board,
the specialist with the improvement over the cubic separation, and the reader
checking the proof with the quantifiers. Keep each opening short enough to
speak in roughly 20–30 seconds. Give the reader a reason to care and a concrete
step they can take immediately.

The `video` field is currently null. Once the video exists, set it in
[the route source](reading_routes.json) to an object with `youtube_id` and
`chapters`. A chapter has a nonnegative integer `start_seconds` and a stable
`route` ID. The compiler verifies increasing timestamps and route membership.
The video and the papers can then open on the same mathematical question.

## Follow one argument across the accounts

For example, find the `erased-zero` route in `reading.json`. Its two
`locations` identify the exact expert and exposition paragraphs. Resolve their
document paths through `papers`. Its `reconstruction` key opens
`CL-erased-zero-identity` in `passages.json`. Follow its `lean` labels through
`docs/lean_links.json` to compare the bound with coefficient four with the
sharper bound with coefficient two. The registry supplies the reader's name
and pinned source URL for each target. For a Lean file, `formal-sources.json`
also gives a downloadable source and, for named declarations, separate line
ranges for the statement and the whole declaration. A Challenge file can
contain a specification placeholder. Use the named Solution and its recorded
comparison to inspect the proof supplied against that specification.

All line ranges are one-based and inclusive. The shorter-paper locators also
hash the exact paragraph bytes, excluding the blank-line delimiters. In the
reconstruction and verification supplement, passage hashes bind the original
body **between** the named passage markers, including its surrounding newlines.
Use those markers for byte-exact extraction. `papers` gives each document's
outline, formal citations, reconstruction links, local images and bibliography.
Authored Markdown bytes and figure paths are preserved. Look up relative assets
against the logical document path before resolving their content-addressed URLs.
A paper can cite an older reconstruction. A citation gains an `edition_passage`
only when the cited passage body matches this edition's body.

Open `reverse.json` from the other direction. A declaration has its registry
labels, tied statement IDs, and Comparator passage references with the original
join kind. From a label, `routes_by_target` points to the cross-paper routes
and `citations_by_target` to the actual citation lines. From a passage,
`routes_by_passage` and `record_citations_by_passage` lead back to the shorter
accounts. The routes select major arguments. Other statements and passages
remain accessible even when they have no editorial route.

## Ask what was checked

`provenance.json` identifies the producer of each kind of information.
Use the paper's original words beside the Lean source. Label the AI-authored
reading connections as editorial. The native dependency export follows
constants in Lean's elaborated types and bodies and records its traversal
scope. The separate evidence graph describes the informal statement ledger.

1. From a reconstruction passage, follow `statement_ids` into the `fidelity`
   resource map in `reading.json`. A fidelity record carries the corpus wording,
   links back to the paper passages, and individual declaration ties. Each tie
   preserves its review, freshness, assumptions, proof route, and separate build
   and comparison evidence. The corpus wording is a ledger statement. For a
   quotation from a paper, use the manuscript location.
2. Follow a tie's file and declaration range, or its recorded line when the
   source parser supplies no range. Inspect its definition, quantifiers and
   premises. An effective partial relation or an old review remains visible
   beside a successful build. The [evidence contract](statement_evidence_contract.md)
   defines the individual judgments.
3. `checks.json` identifies configured theorem names, actual Challenge and
   Solution sources, allowed axioms, receipts and negative controls. The
   shared-bad-specification fixture records acceptance of an impossible
   premise on both sides. The receipt describes that outcome. Keep it separate
   from positive comparisons and from a counterexample to a mathematical claim.
4. `axiom-audits.json` supplies recorded transitive axiom lists for the named
   declarations covered by the round-three inspectors. The list of axioms a
   configuration permits answers a different question. Each audit retains its
   log hash and snapshot freshness. Missing entries mean no indexed observation.
5. `semantic_probes` names a specific attempted variation, its Lean example and
   the historical receipt. For example, open `fidelity/def-R.json` to see the
   effect of choosing the algorithm after seeing the input. An empty array
   means there is no indexed probe for that statement. When adding a probe,
   specify which assumption, quantifier or boundary case it challenges, and
   retain the outcome and edition on which it ran.

## Maintain the data

Edit [reading_routes.json](reading_routes.json) for entrances, stable topic IDs,
unique quotation selectors and editorial cross-links. Source edits that remove
or duplicate a selector fail validation. Re-read both accounts before selecting
its replacement. Change reviewed statement relationships and bind their evidence
through [the corpus owner](../corpus/README.md). The indexes and website data
are generated. Publishing the API requires neither a database nor a separate
deploy service. It performs no Lean build or new fidelity assessment.

## Resolve a paper selection

The static export includes an ES module and prejoined selection indexes. Each
manifest includes a `permalink` alongside `index.json`. Retain the permalink
and objects to revisit a specific edition, including its optional print downloads.
The client can run in a browser or Node 18+. No service process is required.

```js
const entry = new URL("/v1/index.json", location.origin);
const initial = await (await fetch(entry)).json();
const pinned = new URL(initial.permalink, entry);
const {openReader} = await import(new URL(initial.resources["reader.mjs"].href, pinned));
const reader = await openReader(pinned, {expectedRevision: initial.revision});
const selection = await reader.resolve({paper: "reconstruction", id: "passage/upper-weight-drift"});
```

Use a stable passage or topic treatment ID from `selection/<paper>.json`, or
supply `{paper, line, endLine, documentSha256}`. The hash must be from the
manuscript the reader actually opened. The answer includes the selected words,
heading context, matches, formal roots with source ranges and excerpts, both
directions of their proof neighbourhood, other paper treatments, and scoped
comparison outcomes. A page reference for a PDF is edition-specific. The resolver
accepts Markdown selections; it does not interpret PDF screen coordinates.

`coverage` distinguishes associated targets, a documented passage without a
target, and unmapped text. A claim marker narrows the enclosing passage's
statement list. Each tie's relation and review apply to that corpus statement.
An example points to what it illustrates. An editorial constituent identifies
a step in a proof without conferring a reviewed whole-passage equivalence.
A named Solution reference links a compared wrapper to its implementation.
Each join retains its origin. An absent shorter-paper treatment stays absent.

`reader.expand(name)` returns direct references from a declaration's type, value
(including theorem proof bodies), and inductive structure. It also returns the
local declarations that use it, grouped by edge kind. Edges point from user
to dependency in **both** traversals. The compact view follows intervening
helpers until it reaches another paper-associated declaration. One shortest
witness per reached endpoint suffices for display. Depth, result and visit
bounds are explicit; use `expand` to recover direct edges beyond those limits.
`reader.fromDeclaration(name)` gives the formal source and all indexed treatments
of the declaration. Its selection IDs work with `resolve`.

The [native inspection](../tools/ReadDependencies.lean) covers declarations in
the QuarticQuery modules imported by the project root, including internal
helpers. External constants terminate traversal at their defining module;
Mathlib and complexitylib destinations use Lake's recorded dependency revisions.
A Challenge belongs to a separate compilation context. An absent declaration
or unavailable proof body is a boundary, not an empty proof.
The recorded Lean-source fingerprint excludes the manuscripts. A prose change
can move the selection while retaining the graph. A change to the inspected
formal sources leaves the previous graph marked stale and suppresses its joins.
Refresh using `python3 tools/record_reading_dependencies.py` in a built checkout
or give `--checkout` a source-identical cache-bearing checkout.

To inspect the same answers headlessly, use the release manifest or a local one:

```sh
node tools/query_reading_api.mjs build/reading-api/v1/index.json reconstruction passage/forr_three_blocks
node tools/query_reading_api.mjs build/reading-api/v1/index.json --declaration QuarticQuery.Paper.quantumDrift
```

## Revise the papers and retain earlier readings

Editorial treatments in [reading_routes.json](reading_routes.json) bind the whole
selected paragraph or marked passage to the committed manuscript at
`bindings_revision`. Moving unchanged text updates the lines automatically.
Use `python3 tools/build_reading_api.py --audit-bindings /path/to/draft-checkout` to list all affected bindings before regenerating the correspondence. It reads the drafts without editing them.
Changing the surrounding mathematics while retaining the selector fails the
build. Re-read the changed treatment, adjust its selector, statement IDs, or
role as needed, then set **that row's** `bound_at.<paper>` to the new full
manuscript revision. Keep other bindings on the edition in which they were
read. The manuscript change can be committed before this rebinding step.
Claims assembled from the current correspondence still follow its own
passage hashes and the corpus's independent review-freshness rules.

The optional `--pdf-archive PATH` accepts the same three relative paths as
`--pdf-directory`, in a portable ZIP. Supply this ZIP as a release or CI input.
The exporter verifies the approved hashes and source revision before installing
any edition. A plain clone builds the Markdown reader by itself. Publishing a
new print edition requires its accepted output bytes and adjudication.
