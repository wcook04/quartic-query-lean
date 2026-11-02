# Backend residuals: executed Python repair, proposed integration

The source-bound build and comparison backend remains intact. This patch adds
the missing *review* freshness check and enforces the existing decision to
withhold separately derived helper statements from the preprint-only graph.
It changes no Lean source, theorem statement, existing reviewed tie, receipt,
or dependency export. It is an advisory integration patch, not a new proof or
native-extraction receipt.

## 1. The reproduced review defect

The frozen builder selects an `exact`/`stronger` tie using its authored relation
and current build/comparison facts. It never asks whether the relation was
reviewed against the source now being built. A fresh successful build after a
definition change therefore restores statement credit to the old review.
The source locations are `repository/tools/build_corpus.py::statement_records`
and the expressly acknowledged residual in
`repository/docs/statement_evidence_contract.md`.

The replay in `logs/backend-acceptance.json` supplies two source snapshots and
explicitly mocked successful operation receipts for the *new* snapshot. The
review is bound to the *old* snapshot. The frozen code reports the row as
`exact` and `compared`; the patched code preserves current operation facts but
reports the review as `stale`, its effective relation as `unassessed`, and its
statement-level comparison as `not_run`. This is a Python state-transition
test, not a claimed Lean or Comparator execution.

The regression also edits the body of `Allowed` from `n = 0` to `n ≤ 1` while
leaving the complete theorem source `permits_zero : Allowed 0` unchanged. The
test supplies fresh mock operation receipts after the edit. Its purpose is to
ensure that comparing theorem-header text alone would be insufficient; no Lean
elaboration of this toy fixture is asserted.

## 2. The smallest conservative binding

The existing `corpus/ties.json` remains the sole owner of reviewed relations.
An optional `review_binding` on one tie has schema `quartic-tie-review-v1` and
commits to:

- the exact statement ID and statement text;
- the complete merged ledger/adjudication row, including its dependency list;
- the fully qualified declaration name;
- all authored tie fields except the binding itself, including relation, route,
  premise/open-assumption classifications, reviewer and notes;
- the existing complete local Lean/configuration path-to-hash map.

`expected_review_binding` calculates those fingerprints. It is used by the
consumer to compare a recorded binding with the current inputs. It neither
establishes review nor writes bindings into the authored corpus. The evidence
producers are unchanged, so a build or Comparator pass cannot refresh review.
The integration owner must read and approve the actual source/type relation
before adding a binding. Bulk timestamp or hash promotion would defeat the
purpose and is not part of this return.

The complete local-source digest commits to the theorem's declaration context,
implicit binders, type source, and local definitions determining its meaning.
It is deliberately broader than a semantic dependency closure: proof-only
changes and unrelated local Lean additions invalidate it too. This conservative
choice reuses the already implemented snapshot rather than depending on a new
type extractor or trusting a stale dependency graph. It also binds Lake,
toolchain and dependency configuration. It does not bind dependency checkout
bytes or tool executable bytes, authenticate a reviewer's identity, or prove a
clean reconstruction. Those are the existing source-snapshot limits.

`review_evidence` is independently `current`, `stale`, `legacy_unbound`, or
`not_reviewed`. A malformed binding raises an error. Historical judgments remain
in `reviewed_relation` and `reviewed_route`; their assumptions and notes are
retained. Only a current review supplies the effective relation/route or allows
the declaration to be selected for current statement credit. Ordinary premises
and additional open assumptions retain their existing meanings. A stale review
cannot supply selected assumption metadata, while a fresh review by itself
cannot supply compilation or comparison evidence.

The relationship enforced is:

`current statement comparison = one declaration with a current exact/stronger
review + a current build receipt + a current Comparator receipt`.

Facts from different declarations still cannot combine. Informal graph nodes
remain unverified/external, irrespective of this local metadata.

## 3. Migration consequence on the actual supplied corpus

Both frozen and patched builders were run in memory on the supplied source
snapshot and real supplied receipts. The generated files were not written back.
The original inputs and all 124 local Lean/configuration hashes were checked
unchanged. The dry-run results are stored, with byte hashes of the generated
representations, in `logs/backend-acceptance.json`.

| Quantity | Frozen builder | Patched builder |
| --- | ---: | ---: |
| Statement rows | 121 | 121 |
| Ties including doc proposals | 840 | 840 |
| Authored reviewed ties | 477 | 477 retained as `legacy_unbound` |
| Unreviewed doc proposals | 363 | 363 |
| Current build facts on ties | 840 | 840 |
| Current comparison facts on ties | 19 | 19 |
| Rows with a current build fact | 121 | 121 |
| Statement-level `compared` rows | 7 | 0 pending renewed review |
| Current `exact`/`stronger` rows | 55 / 31 | 0 / 0 pending renewed review |
| Informal graph nodes / support edges | 121 / 225 | 121 / 225 |
| Graph node status | 120 unverified, 1 external | unchanged |
| Native extraction status | `not_run` | `not_run` |

The loss of current *alignment* credit is intentional: the old ties contain no
binding in the new format. It does not revoke the recorded Lean or Comparator
operations or infer that any theorem is false. The historical 375 partial,
62 exact, 38 stronger and 2 weaker authored tie judgments remain accessible.
No judgment was automatically re-attested. Reach classifications and the two
pre-existing missing ledger IDs (`claim-butterfly`, `def-P`) are unchanged.

## 4. Derived helper provenance

`research/adjudication/round2_forrelation_exponent_ties.json` contains seven
`new_statement_records` beginning `r2-live-`. Its `ingestion_policy` already
says to preserve these proposals there and not ingest them into the paper-only
corpus. None is present in the current 121-row ledger. Each candidate has source
information, but none currently has an authored `depends_on` field. Inferring
an empty dependency list would be unwarranted.

The patch makes that withholding enforceable. It refuses `r2-live-*` IDs even
if someone sets their source ID to the preprint. It also refuses any row with
an explicitly nonpreprint `source_id`. Both statement generation and direct
graph projection apply this check. Finally, missing prerequisite rows cause an
error instead of silently disappearing from the edge list. The frozen code's
wrong preprint attribution and silent missing-edge behavior were reproduced;
the patched code rejects both cases.

This is deliberately a withholding policy, not mixed-source ingestion. It
does not infer an unlabelled statement's provenance from its mathematical
content. Actual ingestion requires the existing source model to retain the
helper's own source identity and authored dependency relationships. No new
theorem registry, replacement graph format or frontend is introduced.

## 5. Verification actually executed

The replay script and raw logs give commands, outputs, exit codes, interpreter
version, input/output hashes and limitations. The original supplied Python
suite discovered 35 tests: 33 passed and 2 optional native integrations were
skipped. The patched suite discovered 46: 44 passed and the same 2 were skipped.
Eleven new tests cover current/legacy/stale reviews, body-only definition edits,
identity and classification edits, malformed bindings, review without proof
evidence, conservative snapshot changes, derived-row withholding and missing
dependencies. Existing positive test fixtures now explicitly carry synthetic
review bindings; no real tie was bound as part of testing.

The two skipped checks are the installed `lean-exposition` consumer journey and
the optional native Lean Reach fixture. This return does not repeat or upgrade
the supplied historical successful native Reach fixture. No Lean, Lake,
Comparator, native extraction, installed consumer or external kernel was run
in this backend subtask. Repository-wide `make check` was not claimed for the
focused packet, which intentionally omits inputs and README targets.

## 6. Applying and completing the change

`backend.patch` touches only the existing corpus builder, its positive-fixture
tests, one new regression file, and the two relevant contract guides. Apply it
against the frozen repository. Run the focused tests, then use the existing
source owners to record genuinely completed review bindings. If source files
change while integrating semantic tests or an equation-(19) wrapper, rebuild
the exact resulting source snapshot and rerun the appropriate comparisons;
bindings and old receipts must not be copied forward merely because the new
code looks similar. Regenerate the corpus and run the installed consumer's
actual schema/contract checks when that full tool is available.

The reusable acceptance condition is explicit: a semantic source edit followed
by successful new operations leaves an old review stale until that relation is
reviewed again. The unresolved native endpoints are not repaired by these
Python results.
