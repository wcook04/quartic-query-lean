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

## Browser edition

Run `make reading-web` with Pandoc on PATH to package the three manuscripts
and verification supplement as HTML. To include accepted PDFs in the same
export, pass `--web-manuscripts` alongside the existing print options.
The source-only export remains available. Record the Pandoc version when
comparing editions; HTML is content-addressed alongside its source.

Bundle [the reader module](../tools/reader.mjs) with the app. Pass a trusted
deployment directory ending in a slash to `openEdition`; only its optional
`edition` filename comes from a shared link. The loader validates the manifest
against its permalink, constrains object paths, rejects redirects, and checks
byte length and SHA-256. Use `reader.resource(path)` for JSON, `readText(path)`
for text and `readBytes(path)` for PDF or SVG bytes. Present bundled PDFs and
images using typed Blob URLs created from those bytes; revoke them when done.
The optional upstream PDF link opens the publisher's copy separately.

Call `reader.home()` for the opening board, each available paper’s first selection,
and the family overview and scaling examples. A new edition packages this with its
document index in `selection/start.json`. The full graph and proof inputs load
when a consumer opens the corresponding evidence. On older editions the client
reads the available opening material from the pinned edition.

`reader.manuscript(paper)` returns the paper descriptor and its HTML fragment
when available. A source-only manuscript returns null HTML and the verified Markdown
in `source`. Display that string as literal text, using one-based source lines for
passage selection. The original PDF uses its PDF descriptor. Render the
descriptor title, the fragment, and its complete TeX math spans. Images carry
`data-resource`; pass each path to `await reader.figure(paper, path)` for a verified SVG Blob scoped to that manuscript. Set an image’s source to `URL.createObjectURL(blob)` and revoke the URL when the image is removed. Route local links marked
`data-paper` and optional `data-fragment` within the reader. Fragment-only
links target existing IDs in the same paper. Preserve external revision pins.
Pandoc resolves citations against that manuscript’s packaged bibliography. Numbered footnotes and their return links use the IDs in the fragment. The export rejects duplicate IDs, unresolved citations and dangling internal destinations. Render each paper in its own document or scope anchor lookup to the active paper: different papers can both use `fn1`. Its
`data-l0` and `data-l1` describe inclusive source line groups. A group can
contain multiple selections; present the applicable choices. Resolve the
chosen selection for exact passage text. Keep paper markup intact when
opening or closing evidence.

`resolve()` returns a serializable `position`. `reader.restore(position)`
requires the same immutable edition and document digest. Keep focus, viewport
offset and proof-pane mode as UI state alongside that position. Passive
scrolling should not replace an explicitly pinned selection or push history.

Read `reading.json.board_example` via `reader.resource` for the three worked
scenes. Each scene includes selections in the current exposition. Arrays are in
printed row order and coordinates start at one. The known pair supplies both
boards and their one distinguishing query. The hidden-zero probabilities apply
to querying the first h complete rows of the coupled boards. Yes/no certificates
apply to an unknown board. The pointer example supplies the correct and altered
targets and the rival replies, with the comparison rule and outcome. Its scope
is an illustration. The exposition entrance's `first_selection` starts with
the question above the table.

## Look up a declaration title

Use the exact declaration ID for navigation and the edition’s title for display.

```js
const {status, titles} = await reader.declarationTitles()
const label = await reader.declarationTitle("QuarticQuery.Gvalue_lt_R_Fkm")
if (label.title !== null) {
  renderInlineMath(label.title)
  button.setAttribute("aria-label", label.title_plain)
}
```

The first lookup fetches one hash-verified resource. A current edition covers every project
node, including generated declarations, plus the named comparison targets and semantic examples.
Cards and path helpers already carry both fields from the same index. Use them directly to draw the
map. Titles are editorial descriptions. A statement’s correspondence record and each arrow’s Lean
witness provide the evidence.

An unknown name returns `missing_title` with null text. Show the gap. Keep raw identifiers available
in code and technical details. An older edition can supply `archived_partial` labels from its own
cards and helpers, or `unavailable_in_edition`. A stale graph withholds its index.
The [title source](reading_declaration_titles.json) is bound to the Lean snapshot. Use a string for
prose or a pair for a caption with inline `$…$` TeX and its readable plain rendering. Export checks
the declaration set and the prose around every formula. The site build renders every expression
with the reader’s pinned KaTeX.

## Open the Lean map beside the paper

The map is an optional, immutable edition resource at `selection/proof-map.json`
(advertised in `reading.json.proof_map`). The bundled client loads it on first
opening the pane. Following the paper or inspecting a collapsed edge then uses the
same object in memory. Choosing a card's Lean fetches its verified module source.

```js
const map = await reader.proofMap()
if (map.currentness === "current") {
  const focus = await reader.proofFocus({paper: "original", id: "original/thm-1.1"})
  // Or pass {paper: "reconstruction", line} or {paper: "original", page}.
  const card = map.cards[map.root]
  const raw = await reader.proofCardSource(map.root) // text, source, inclusive lines, URL
  const edge = map.edges.find(e => e.from === map.root && "value" in e.witnesses)
  const hops = await reader.proofWitness(edge.from, edge.to, "value")
}
```

The root is the declaration for the whole family theorem. Traverse the recorded
project dependencies of its type, body and structural references. Retain the root
and declarations with a qualified association to a paper selection. A statement
tie must name the same implementation file. Frozen challenge names alone do not
qualify. Some indexed associations have legacy or unassessed review status.
Read `card.statements[statementId]` for the relation, review status and proof route
of that statement only. A card title describes its declaration and the kind comes
from its source. The card’s module supplies a natural grouping for the map.

Each edge points **from the consumer to its prerequisite**. There is one witness
per recorded first-hop kind: `type` for the statement, `value` for the body
(proof for a theorem, definition body otherwise), and `structural` for a structural
dependency. A one-hop witness is a direct Lean edge. Longer witnesses pass only
through hidden declarations; later hops can have different kinds. Expand a
witness to show the actual intermediates. The map keeps a shortest witness per
first-hop kind, with deterministic ties. Internally `paths` shares prefixes
as triples of prefix index (or null), hop kind, and target declaration.

Use `card.parent` for a rooted layout tree. Its edges are a subset of the
witnessed connections. The root has a null parent. Draw additional edges on
expansion or focus. Focus returns every card associated with an exact selection.
For a line it returns the narrowest enclosing indexed ranges; for a PDF page it
returns indexed selections on that page. The `matches` include selection IDs and
`bindings` from each card name to its provenance (such as `statement:thm-1.1` or
`editorial_constituent`). An empty focus means this location has no card on
the headline map. Keep the paper location; the wider proof and raw Lean remain
available via the ordinary selection inspector. Map data from a different edition
must never be substituted. `stale` and `unavailable_in_edition` are explicit statuses.

### Count the declarations a reader has encountered

`map.paper_cards[paper]` holds the distinct declaration names for that paper, the
total `count`, and the `graph_count` on the drawn graph (excluding its separate
type shelf). A declaration can appear at many passages and still counts once.
The original indexes PDF statements by page; the manuscripts use source lines.

```js
const progress = await reader.paperCardProgress({
  paper: "original", edition: reader.permalink, visited: ["original/thm-1.1"], through: 1
})
// “Encountered X of Y linked declarations”: progress.visited.count and progress.total.
// progress.through.count describes the paper up to page 1, regardless of reading history.
```

Pass the IDs of selections actually encountered. Save them with the edition and paper.
A jump ahead adds a visited selection only when the consumer records it.
Use `surface: "all"` to include the type shelf. Counts describe navigation
among linked declarations, not the fraction of a paper certified by Lean.

### Inspect the helpers behind one arrow

Pass the consumer and prerequisite in the map's stored direction. The backend
returns one recorded path per available first-hop kind. A direct path has zero
helpers. A path with intermediates lists them in order from the selected card
to its prerequisite. For example, open the path that uses the positive budget
constant in the upper bound.

```js
const from = "QuarticQuery.Upper.familyBoundsAt_of_lower"
const to = "QuarticQuery.Forrelation.forrConstant"
const path = await reader.proofPath(from, to, "value")
if (path.status === "current") {
  const {hops, helperCount} = path.variants[0]
  const helper = path.declarations[hops[0].to] // QuarticQuery.Upper.budgetConst_pos
  const lean = await reader.proofPathSource(helper.name) // verified bytes, pinned URL
}
```

Omit the kind to inspect every variant. Each hop carries its own Lean `kind` and
display `usage` (proof, body, statement or structural_reference). A body with
unknown declaration kind is labelled body. Declarations identify whether they
are cards or helpers, their module and any available kind, title and source
range. Show a missing-title state when the edition lacks a title. A null range means the reader
can open the pinned module; it has no separate verified excerpt for that name.
On a current kernel capture, each hop also carries `evidence.compiledWitness`.
For an expression this gives the path from the compiled type or value to a
constant or projection. The region identifies the result, body, or named
parameter domain containing the occurrence. A structural witness identifies a
Lean metadata relation, such as entry 1 of an inductive type’s constructors.
`compiledCoverage` counts these witnesses per chain. A source highlight requires
a separate entry in `sites`. If the original line is unavailable,
`sourceLimitation` distinguishes a dependency found only in a parameter
domain, a caller without a separate source excerpt, and an original occurrence
whose location remains unresolved. Older editions may return a null compiled witness.
For generated helpers without a separate source range, `proofPathSource` can
return Lean’s printed type in `compiledSignature`. A `definitionSite` links the
name to its original field or constructor token when the native index provides one.

Every hop has an `evidence` response. Use `sites` to highlight its occurrences:
`resolved_identifier` marks an identifier that Lean’s own reference index resolves
to the target inside the caller, in the matching syntactic region. A reference
inside a proof body is distinct from the same name inside its statement.
`elaborated_application` adds the existing, stronger walkthrough witness for a
particular instantiated application. Several uses may have separate locations;
display the choices. Each site carries exact source text, one-based inclusive
lines, a commit-pinned link, zero-based half-open UTF-8 byte offsets in the
file and half-open UTF-16 columns within the first and last lines for browser
highlighting. `locationCoverage` counts located hops in this particular chain.

A `compiled_rhs` site covers the complete expression or tactic sequence that
produced a value on one source line. Lean reports the target constant in the
compiled body after removing the outer parameter binders. Show the whole
highlight, even when the constant was supplied implicitly. For example, the
`simpa` on line 215 of `Tournament/Ideal.lean` produces the proof that uses
`expectFrom`. The source of a particular tactic inside a multi-line or
backtracking proof requires separate evidence.

`retained_tactic` locates a dependency inside the proof term produced by a
closing tactic on one original line. During a separate elaboration, the
inspector wraps that tactic’s result in a tagged identity function. It accepts
the span only when the marker survives in the final declaration and deleting
the markers recovers the stored compiled proof. It searches the payload for
the dependency. For example, the final `rfl` in `Preparation.iterate_succ`
produces a proof containing both `Circuit.run` and `groverStep`. These uses
are visible at line 200 of `Amplification/Geometry.lean`. A tactic attempted
in a discarded branch cannot supply a location by this method. For requested value hops, `replayStatus` distinguishes
a match, a completed replay with no match, a caller without eligible single-line
tactic syntax, an uninspected module, and a caller without a verified declaration range. A null status means the edition supplies
no replay result for this hop.

`compiled_result` marks a single-line written result expression when the
target occurs in the compiled result. `constructor_declaration` marks the
constructor’s original identifier when Lean records it inside the selected
inductive declaration. Some constructor signatures also supply exact
`resolved_identifier` sites.

An `inherited_parameter` site identifies the type of a parameter declared earlier
in the same module. The pinned line can be outside the declaration's excerpt.
Show “type of inherited parameter A” with the returned `binder` text. On a
statement hop the API can use this as its location when an inline use is unavailable.
On a proof or definition hop, `parameterOrigins` can explain a dependency in a
compiled lambda parameter. These origins stay outside `sites` and the hop's
location count until an actual proof or definition use has its own evidence.
For an ordinary written parameter, an origin with `basis: written_parameter`
identifies the resolved name within its written `domain`. The parameter name
occupies the same unique slot in Lean’s compiled type and value. Its region is
`declaration_parameter`. For example, a definition that accepts a circuit can
carry the circuit type in its compiled lambda even when its implementation
never names that type.

`declaration_only` means the typed dependency exists but no matching source use
was established. Offer the caller’s source range or module. `otherReferences`
records locations in another or unclassified region; those are inspectable as
caller references but must not be highlighted as the selected typed use.
`stale_reference_index` and `unavailable_in_edition` are separate outcomes.
The graph can include implicit arguments, generated code, and structural edges
with no corresponding written identifier.

A first path inspection loads the edition’s source-use index. Indirect paths
also load the helper catalog. Verified raw Lean loads when the reader opens
a declaration. Authored titles are bound to declaration names; generated helpers
keep that qualification in their titles. Older map editions retain the source
locations and titles they packaged. A missing or stale map returns its status. A pair outside
the recorded map returns `not_a_dependency_edge`, including the editorial
arrow from the paper headline to the formal theorem.

```sh
node tools/query_reading_api.mjs build/reading-api/v1/index.json --proof-line-coverage
node tools/query_reading_api.mjs build/reading-api/v1/index.json --proof-path QuarticQuery.Upper.familyBoundsAt_of_lower QuarticQuery.Forrelation.forrConstant value
```

The coverage command counts a fully located arrow only if every step of every
route has a verified source use. Its separate `distinct_hop_navigation`
breakdown shows how many remaining steps can open a verified parameter type.

For the section outline, use `(await reader.manuscript(paper)).descriptor.contents`
in web editions. Each row has the printed title and level, the real HTML
`anchor`, an inclusive `line` through `end_line` range (including subsections),
and `listed`. Show listed headings and follow the deepest listed range containing
the reading line. Older editions retain their original `outline` and source locations.

## The four papers and their Lean coverage

Use `reading.json.paper_ids` for the paper switcher. The verification appendix is
listed separately in `supplement_ids`. Three papers are maintained here. The
fourth, `original`, opens OpenAI’s published PDF at a pinned revision. Pass
`--original-pdf /path/to/source.pdf` to serve a local copy in the same edition.
The exporter verifies the PDF bytes and exposes its resource in `papers.original.resource`.
The pinned upstream URL is always available.

Each entry in `reading.json.coverage` identifies its exact source bytes. For the
original, the unit is a maintained ledger statement drawn from or developed
around the published argument. Review classifications concern the ledger wording.
For our three papers, the unit is a selected passage, citation or claim. The count of linked ledger statements counts explicit statement IDs, while some selections link straight to Lean. Selections
can overlap. The distinct linked-statement count describes navigation and supplies
no denominator for the proportion of a manuscript proved in Lean.

For example, resolve `{paper:"original", id:"original/eq-21"}` to open equation
(21) on page 13 alongside the same formal evidence available to the other papers.
The result exposes the real PDF destination where available, a page URL, and
`relatedSelections` in the other documents that share the indexed statement.
Unnumbered steps and local generalizations have page locations. Rows identify
amended ledger wording and statements added in review. Whole-page requests take
`{paper:"original", page:13, documentSha256:…}`. An unindexed page still opens.
PDF prose is displayed from the original file. The project supplies the Lean.

The [recorded page map](original_preprint.json) uses the published PDF’s
destinations and the physical page breaks in the same Poppler layout extraction
used by the intake ledger. Reproduce it with `python3 tools/original_preprint.py
/path/to/source.pdf` (PyMuPDF and pdftotext). Normal exports work offline.

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
4. `axiom-audits.json` gives the transitive axioms that Lean reported for the
   inspected declaration. Each observation carries its freshness. Earlier
   round-three observations retain their historical scope. An absent observation
   means unknown. The formal type displays the hypotheses a caller must supply.
5. A semantic example has an authored question, a kind, a source location,
   a plain-language answer bound to the Lean source snapshot, and the compiled
   Lean type and axioms. Kinds distinguish changes to a
   definition, boundary examples and witnesses that assumptions can hold.
   The response explicitly identifies statements without an indexed example.

### Read or label a ledger statement

Use `await reader.statementTitles()` for links, PDF sidebars and cross-references.
This loads one edition-bound index with `titles[id].title` for inline KaTeX and
`titles[id].title_plain` for accessible text. The index includes definitions,
unnumbered claims and rows added during review. Use the PDF locator for an
actual printed destination.

```js
const review = await reader.statementReview("eq-13")
const display = review.presentation
if (display) {
  renderInlineMath(display.title)
  renderInlineMath(display.body)
}
```

Each published statement has a descriptive title, a typeset body, their plain copies
(`title_plain` and `body_plain`), and the SHA-256 of the maintained wording.
Passage selections already include the same object on each `resolve().statements` row.
The review applies to `ledgerStatement`, which remains available verbatim.
The [editorial presentations](reading_statement_presentations.json) are checked against
individual maintained statements at export. A changed statement requires revisiting its
title and body. Manuscript edits can keep the presentation when the ledger wording is unchanged.

The bundled client returns `unavailable_in_edition` and an empty title index for an earlier
edition without this resource. Its statement review has `presentation: null` and keeps
that edition’s wording.

### Compare a paper result with Lean

Use `reader.statementReview("thm-1.1")` or
`node tools/query_reading_api.mjs build/reading-api/v1/index.json --statement thm-1.1`.
Open the original PDF at the returned location. Beside it, show the ledger
wording actually assessed, the current reviewer's explanation and the formal
type that Lean printed. Each comparison carries a link to the exact source,
its relation and proof route, its hypotheses, and its own native observation.
The preferred comparisons match the corpus's strongest available built relation.
Other current comparisons remain inspectable, as do earlier or unassessed links.
For changes to ledger wording, the response includes the previous description
and the existing reviewers' findings with their dispositions.

For Theorem 1.1 the full family theorem appears first. The shorter exponent
theorem appears as a partial match. For equation (21) the leading type spells
out the hypotheses on the input law. For the definition of randomized queries
an executable example shows how changing the order of algorithm and input
can let a zero-query algorithm appear to solve the one-bit identity problem.
The formal observation, reviewer judgment and example each have their own source.

Regenerate formal types and axioms with `python3 tools/record_reading_dependencies.py
--statements --checkout /path/to/built-checkout`. Add `--compare` to independently
re-extract and compare the saved payload. The recorder builds the modules, asks
Lean to verify each defining module, and binds the results to the inspected
source and extractor. Stale observations withhold their types and axiom lists
from current comparisons.

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
// Bundle the repository client with the frontend. apiRoot is deployment configuration.
import {openEdition} from "./tools/reader.mjs";
const reader = await openEdition(apiRoot, {edition: sharedEditionFilename});
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
statement list. Each tie's relation and review apply to that corpus statement. Current reviewed ties seed the proof neighbourhood. Historical and unassessed ties stay in the returned statement records.
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

## Inspect a theorem application

The returned `forrelation-family` journey includes an authored `overview`.
Use its stage IDs and `after` lists to place the quantum and classical arguments
beside each other. The assembly stage opens the existing shared-board witness.
These edges describe the mathematical reading order. Expand a step to see its
separately recorded Lean applications and graph edges. The `scaling` examples
give exact rational leading powers for a small choice of fixed k, including
7/2 at k = 4, together with the order of the quantifiers. Display the
logarithmic qualification whenever showing these powers.


Open a journey from a selected passage, a Lean declaration, or the edition's
application index at `reading.json → applications`. The five entries cover
weighted halving, the sign-blind decoder, the common Forrelation family, the
capped predictor and Gaussian derivative transport.

```js
const {journeys} = await reader.resolve({paper: "exposition", id: "exposition/joint-event/0"})
const path = await reader.journey(journeys.find(id => id === "capped-predictor"))
const fixedTime = path.steps.find(step => step.caller.endsWith(".eq_21"))
const treatment = path.treatments.find(topic => topic.id === fixedTime.topic)
const explanation = path.steps.map(step => step.mechanism).join("\n\n")
const dependencies = await reader.expand(fixedTime.caller)
```

The journey also returns source definitions for its `interfaces`. For example,
`CircuitRealises.correct` states both the domain-bit equivalence and value-bit
condition, and `FamilyBoundsAt` quantifies one circuit before both inequalities.
Each step has an exact Lean source excerpt, a revision-bound URL, and a topic
with selections in the available papers. For each quoted callee the backend
checks for a direct reference in the compiled caller's value. The adjoining
`compiled_uses_in_caller` are Lean expressions for that caller/callee pair.
They include the formal binder, instantiated type and result type. For value
arguments the inspector displays the argument. For proof arguments it gives
the obligation, the local proof variable when available, and the head constant
when the witness has one. Lean's pretty-printer can abbreviate long expressions.

Each step's `mechanism` explains why the application matters in this argument.
For the capped predictor the ordered mechanisms cover the unconditional cap,
the event inclusion at a fixed query time and the average over the original
product law. They are authored explanations. The caller and callee names can
be passed directly to `reader.expand` to inspect their formal dependencies.

**Application evidence.** `compiled_uses_in_caller` always describes the
whole declaration. An authored excerpt plus a direct compiled reference gives
`source_associated` attribution. For selected modules the inspector also
re-elaborates the original file and consults Lean's information trees. An
`exact_source_occurrence` has an original named application span whose
instantiated expression occurs structurally in that caller's re-elaborated
body under matching local binders. Each entry in `occurrences` carries its
own term and half-open UTF-8 byte range in the full source file. Render those
arguments beside the span. A declaration can use the same callee elsewhere
with different arguments. Identical expressions shared in the proof body have
no unique kernel address in this export. Tactic-generated terms and unmatched
local contexts retain declaration-level evidence. [Lean information trees](https://lean-lang.org/doc/api/Lean/Elab/InfoTree/Types.html)

**Proof obligations.** For each compiled proof argument, `basis` distinguishes
an enclosing declaration parameter, a local reference, a named proof term
and another proof expression. `project_constants` names direct Quartic
references inside the proof argument. An authored `obligations` entry
selects the matching callee, binder and term. An optional `assembly` points to
the later step, its witnessed provider and the application excerpt. For
example, follow `hLR` from `classical-instance` to `eventual-hardness`. The
first call takes the inequality as a parameter. In the latter step the
Forrelation theorem supplies a threshold and its bound is applied at the
chosen size. At that step `shared_board` records a separate native check.
Inside one existential circuit binder of the headline theorem, Lean found
structurally identical totalised board arguments to Q and R, both using that
bound circuit.

The separate
`correspondence` records carry the reviewed statement relation and proof route
for each declaration. In particular the Gaussian journey shows uses in both
the tree advantage estimate and the promise estimate. Its selected
three-block worked example still has constituent-level coverage.

```sh
node tools/query_reading_api.mjs build/reading-api/v1/index.json --journey forrelation-family
python3 tools/record_reading_dependencies.py --applications --checkout /path/to/built/checkout
```

The [journey source](reading_applications.json) owns the ordered excerpts and
reading topics. Bind changes to a reviewed Lean snapshot, refresh the graph
and the application inspection, then run `make check`. To independently
repeat the native extraction and compare all its records, append `--compare`
to the recorder command. It leaves the recorded inspection in place. Run the
native repeated-lemma regression by setting `QUARTIC_LAKE_CHECKOUT` to a
checkout with the pinned Lean environment when running the tests. The ordinary
paper build reads the captured evidence. Existing editions keep
their original client and inspection.

A topic's `context_passages` also names manuscript prerequisites and the Git
revision at which each was read. The draft audit reports
`prerequisite_changed` when a named definition or hypothesis changes, even
if the selected paragraph still resolves. Publication requires rereading the
affected association and updating that prerequisite's revision. The audit
covers declared prerequisites and reports byte changes. Independent review
of mathematical equivalence remains a separate record.
