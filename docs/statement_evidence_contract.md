# How statements, proofs and Lean stay in step

Lean work and written mathematics drift apart in a familiar way. A proof is
checked, a cleaner derivation is found while writing, and the published argument
no longer matches what was checked, while the checked proof sits unused. This
contract keeps the two aligned without freezing the mathematics early.

## The unit of agreement is a statement

A corpus statement is a displayed mathematical claim with a stable identifier and
a hash of its exact text. Lean is bound to statements, not to proof prose.
Comparator already works at this level: it fixes a theorem's type and everything
that type depends on, and lets the proof change. So:

1. **A proof may be replaced freely.** A shorter derivation of the same statement
   changes the Solution side only. The statement, its Challenge and its identifier
   are unchanged.
2. **A new displayed step is a new statement.** If a cleaner derivation introduces
   an intermediate claim that a reader is asked to believe, that claim gets its own
   row and its own evidence. It starts as unchecked and is shown as unchecked.
3. **A changed statement is a new record.** Strengthening or weakening a theorem
   creates a new statement and a new comparison. The old row stays in the history.

Here the challenge vocabulary and theorem statements are mechanically copied
from maintained source and compiled separately. Comparator tests agreement with
that specification; it does not establish that a specification shared by both
sides expresses the intended mathematics. Source review and independently
specified examples remain separate obligations. The finite
[semantic controls](../tools/return_checks/semantic_controls.py) demonstrate
this distinction; they do not execute Lean or Comparator.

## Three separate facts per statement

| Field | Question it answers |
| --- | --- |
| `statement` | Is this exact claim checked by the kernel for the recorded source bytes? |
| `route` | Does the Lean proof follow the written proof: `same`, `alternative` or `none`? |
| `reach` | Is the declaration in the dependency closure of a headline theorem? |

A statement can be checked by an alternative route. That is a true, useful status
and is displayed as such. It is never displayed as a check of the written argument.

A commit name alone does not bind a dirty working tree. New build and comparison
receipts retain hashes of the Lean sources, comparison configurations and pinned
dependency configuration, and refuse current-evidence credit if those inputs
change during the run. Historical receipts without that binding remain
`legacy_unbound`; bound receipts whose inputs have changed are `stale`. Neither
is evidence that the current sources pass. Refreshing a receipt requires an
actual successful run, not relabelling its date or commit.

Compilation and comparison must support the same reviewed declaration. A
compiled partial ingredient cannot borrow an exact relation or a comparison
result from another tie. The dependency export traverses private and generated
intermediates before displaying public declarations; an absent edge in an old,
unbound export does not prove that the theorem is unused.

Reviewed statement relations remain authored judgments. They have a freshness
boundary independent of build and comparison evidence. A reviewed tie in
`corpus/ties.json` may carry a `review_binding` with schema
`quartic-tie-review-v1`. The binding commits to the statement ID, exact statement
text, complete corrected row, declaration name, all authored tie fields except
the binding itself, and the complete local Lean/configuration snapshot. Thus a
change to `premises`, `open_assumptions`, relation, route or reviewer also
invalidates the old review. Missing bindings are `legacy_unbound`; mismatching
bindings are `stale`; malformed bindings stop generation.

Only a `current` review supplies the effective `relation` and `route` used for
present statement credit. The generated tie retains the historical
`reviewed_relation`, `reviewed_route`, assumptions, note and binding alongside
`review_evidence`. Build and comparison facts remain independent: both can be
current while the old statement review is stale. Such a tie supplies no current
exact/stronger statement credit, no selected assumption metadata, and no
statement-level comparison credit. A current review alone supplies no proof
or comparison evidence.

### Binding a completed review

After inspecting the complete theorem type, its implicit context, definitions,
paper row and premise classification, the reviewer may record the result of
`expected_review_binding(id, rows()[id], reviewed_tie, source_hashes())` on that
same tie. This helper calculates an expected fingerprint; it does not establish
that a review occurred. Neither corpus generation nor an evidence producer
writes or refreshes authored review bindings. Do not bulk stamp old ties. Keep
the reviewed source bytes frozen until the binding is recorded, and retain the
actual source/type reading in the existing adjudication owner.

The binding fields are `schema`, `statement_id`, `statement_sha256`,
`row_sha256`, `declaration`, `judgment_sha256`, and
`source_snapshot_sha256`. Object digests use UTF-8 JSON with sorted keys,
`ensure_ascii=False` and separators `(',', ':')`; `statement_sha256` hashes the
exact UTF-8 statement text. The snapshot digest hashes the existing complete
path-to-SHA-256 map returned by `source_hashes`. It binds theorem source and all
local definitions, rather than only the text of a theorem header: changing a
definition while keeping that header unchanged still invalidates review.

This policy is conservative. A local proof-only edit or unrelated local Lean
addition also invalidates review, as do pinned configuration changes. Prose
outside the reviewed row/tie and local source snapshot does not. Dependency
pins are bound, but installed dependency checkout bytes and executable bytes
are not; a binding does not prove a clean reconstruction or authenticate the
reviewer. Narrow semantic-closure bindings would require a separately validated
extractor and are not inferred from an old dependency graph.

### Provenance of derived helpers

The current graph is a preprint-only projection. Separately derived `r2-live-*`
proposals remain in their existing research adjudication owner, with their own
source records. The builder refuses those IDs and explicitly nonpreprint source
IDs instead of relabelling them as OpenAI preprint statements. It also refuses
missing prerequisite rows, so a dependency on a withheld helper cannot silently
disappear. Ingestion awaits a source-aware projection preserving each helper's
own provenance and authored dependencies; this change creates no second registry.

## Collapsing onto the elegant path

Keep the checked theorems whose statements are worth reading, and treat the rest
as scaffolding. Before a paper is released:

1. Every displayed claim in the paper resolves to a statement row.
2. Every statement row has a declaration, or an explicit `none` with its reason.
3. The dependency closure of the headline declarations is computed from the
   compiled environment. A declaration outside that closure is not part of the
   headline proof. It may still support an independently checked statement in
   the written argument; retain that evidence separately from headline reach.
4. Where the final derivation differs from the Lean proof of a load-bearing step,
   the step is either re-proved along the final route or marked `alternative`.

Counts of declarations or lines are not progress. The measure is whether every
claim a reader is asked to believe has a stated evidence class.
