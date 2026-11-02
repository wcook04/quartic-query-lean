# Round-three evidence backend adjudication

The [preserved job 09 return](../returns/round3/members/09_evidence_backend/backend/backend_notes.md)
identified a separate review-freshness boundary: changing a definition and then
rebuilding and comparing the theorem must not renew an old judgment that the
theorem says what a paper statement says. The maintained corpus builder now
enforces that boundary. The [machine-readable record](round3_backend.json)
binds the input archive and records validation and deferred work.

## Accepted implementation

An authored tie may carry `review_binding` with schema `quartic-tie-review-v1`.
The binding covers the statement ID and text, complete corrected ledger row,
declaration, every authored tie field except the binding itself, and the complete
local Lean/configuration hash map already used by operation receipts. A missing
binding is `legacy_unbound`, a differing binding is `stale`, and a malformed
binding stops generation. Only `current` reviews supply effective relation and
route. Historical judgments, assumptions and notes remain available.

This is deliberately conservative: proof edits and unrelated local Lean additions
also invalidate review. Neither a build nor Comparator can write a review binding.
The [contract](../../docs/statement_evidence_contract.md#binding-a-completed-review)
describes how a completed source review is bound. Existing ties were not bulk
attested, and a binding does not authenticate the reviewer or verify installed
dependency artifacts.

The preprint-only projection now refuses `r2-live-*` helper proposals and rows
with explicitly different source identities. It also refuses missing prerequisite
rows instead of dropping their support edges. The helpers retain their existing
adjudication provenance until mixed-source projection and authored dependency
data are available.

The returned patch was inspected against the maintained builder before its
matching changes were applied. One adaptation preserves all proposed and reviewed
ties in graph metadata receipts, including historical judgments whose freshness
is insufficient to select a current declaration. Those records remain
`semantic_review` with `not_run` status; informal graph nodes remain unverified
or external. They are metadata, not native proof or extraction receipts.

## Validation and limits

The focused suites passed 34 tests, including actual installed consumer schema
and contract validation, goal selection and inspection. The full Python suite
ran 142 tests: 141 passed and one optional native Reach fixture was skipped.
An actual temporary projection of the corpus also passed the installed
`lean-exposition validate`, `select` and `inspect` commands; its selected
argument closure contained 116 statements. The JSON record identifies that
observed graph and source snapshot. Concurrent subsequent Lean edits do not
inherit its validation.

The working layout check at this lane's validation reported only newly preserved
round-three custody members and return-local PDF links. The intake lane owns
their immutable-custody admission. A later rerun reported only the local-only
`research/returns/round3/attachments/input_10.txt` placement; integration must
rerun the gate after intake settles.
No generated corpus outputs, maintained ties or receipts were written here.
No commit was created.

Python operation receipts in regression fixtures are explicit mocks. Native
Lean extraction, axiom inspection and Comparator checks belong to their separate
implementation lane. The return's proposed native sources and expected outcomes
were not promoted by the Python results. Narrow semantic fingerprints and
mixed-source ingestion remain deferred; no second registry or frontend was added.
