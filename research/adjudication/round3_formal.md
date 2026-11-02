# Round-three formal integration

The Lean development proves both the equality between hit probability
and expected discoveries divided by the number of columns, and the coefficient-four
bound in equation (19). The maintained inequality already follows from a stronger coefficient-two
finite-world search argument. These wrappers assemble existing ingredients; they
do not formalize the paper's early/late proof or claim optimal constants.

The source inputs are returns 07 and 09, preserved under `research/returns/round3/`.
The returned execution records are advisory: native results below come from this
checkout and its pinned Lean toolchain.

## Statement decisions

- `QuarticQuery.Paper.eq_19_complete` preserves return 07's literal chain by bounding
  `expectedZeros / m` after asserting its equality to the hit probability.
- `QuarticQuery.Paper.eq19_whole` preserves return 09's form by bounding the hit
  probability after asserting the same equality. These are different declarations;
  neither borrows the other's Comparator result.
- `QuarticQuery.Independent.Eq19.checked_eq19` uses a separately authored explicit
  product distribution and discovery predicate. Its bridges prove agreement with
  the maintained definitions before using `eq19_whole`. It shares the coordinate,
  tree, path and depth foundations; repetition controls test that shared boundary.
- The isolated discovery experiment needs nonnegative normalized address weights
  and a worst-case depth cap. It does not need a hardness or promise-support premise.
  The paper's `m = 4^t` is obtained by choosing `ℓ = 2*t`.

## Independent semantic expectations

The new tests exercise the actual Lean definitions, using expected answers authored
separately from the generated Comparator challenges. A one-bit identity cannot be
computed with zero queries; the equal mixture of constant true and two single-bit
readers computes OR with one query at the inclusive two-thirds boundary. A promise
with only a true label has zero classical and quantum query complexity. The two
Forrelation layers `(-1,1,1,1)` have value `-1`, outside the signed high promise.
A fair two-candidate comparison supplies a concrete nonvacuity witness.

The detection theorems show changed answers when one lets the program depend on
its input, makes the success threshold strict, takes the absolute value in the high
promise, or labels the off-promise input false. The shared-specification control
adds an impossible premise on both sides: Comparator agreement is expected, while
a separate theorem proves that no such comparison exists. This acceptance is a
blind-spot demonstration, never semantic success.

## Native validation

The frozen source snapshot `43f007e0916f14d513d076e8036b9bb05aa29897b5b9eb7bc4a8d6551d63c2b3`
passed the native target batch and both type/transitive-axiom audits. The audits
identify the actual compiled declarations and permit only `propext`,
`Quot.sound` and `Classical.choice`. `round3_formal.json` binds those operation
records. All six dedicated Comparator cases passed: three positive targets were
accepted, the omitted-equality and changed-threshold cases were rejected for
the intended reason, and the shared impossible-premise control was accepted as
the expected blind-spot demonstration. The root build and dependency export
also passed on the same snapshot. All five baseline positive bundles and five
baseline negative controls were refreshed successfully. The Unconditional
bundle also passed the additional paranoid check. All three focused native
consumer runs passed, including validation, goal selection, inspection and
replay from their recorded-input locations.

## Construction support completion

`QuarticQuery.Paper.construction_lemma_2_2_with_support` conjoins the full
finite-count/coherent-query conclusion of the earlier construction theorem with
`construction_pointer_every_physical_coordinate`, specialized to `ℓ = 2*t` and
`r = 40*t`. For every pointer-word or possible-target coordinate it supplies
full physical inputs that agree everywhere else and change the pointer-test
answer. No new side premise is needed. The original theorem remains unchanged
and alone is partial for the expanded corrected ledger row.

## Integration repairs

The first native semantic build exposed elaboration gaps in the returned OR
mixture proofs: simplification left the mixture's dependent projections folded
in its depth and success goals. This is a proof-script issue; the exact finite
Python model confirms the independently specified success values. The repaired
proofs passed the frozen native target batch and type/axiom inspections.

The bridge proofs also needed to establish event equivalence before transporting
indicators and finite-set membership: direct rewriting under their hidden
Decidable instances produced an invalid rewrite motive. No experiment, theorem
type or distribution normalization changed in either repair.

The completed native target batch passed. Its first inspection run exposed a
Lean module-visibility issue in the returned audit: the non-public import of
Bridge through Solution does not expose `eq19_whole` to the audit. The audit now
imports Eq19Whole explicitly; no theorem type or proof body changed.

The printed Lemma 2.2 states the count and adaptive/coherent query bounds; it does
not state the separate essential-coordinate diagnostic literally. That diagnostic
was retained in the corrected ledger to exclude a fixed-support interpretation.
The new conjunction therefore strengthens the printed lemma with that diagnostic.
Calling the old theorem partial here is relative to the expanded corrected ledger
row, not a claim that the printed lemma itself demands an extra support clause.

The registered [targeted build receipt](../../corpus/receipts/lean-build-round3-targeted-2026-11-02T204814950389+0000.json)
covers the 18 declarations actually inspected in the compiled environment.
Positive comparisons belong to the exact [support construction](../../corpus/receipts/comparator-round3-construction-support-2026-11-02T204814950389+0000.json),
[independent product-law target](../../corpus/receipts/comparator-round3-eq19-independent-2026-11-02T204814950389+0000.json),
and [probability-form Eq19 wrapper](../../corpus/receipts/comparator-round3-eq19-direct-2026-11-02T204814950389+0000.json).
The expected-count form `eq_19_complete` has build and axiom evidence, without a
standalone comparison. The shared bad-specification receipt lists no positive
theorem declarations and carries an explicit control marker.

The [current root receipt](../../corpus/receipts/lean-build-root-2026-11-02T205500674428+0000.json)
contains all three new Paper declarations. The independent semantic declarations
are recorded under the targeted build, rather than credited to the root import.

The native consumer's detailed declaration view repeats a large derived-invariant
catalogue. For packet use, the native reports and graphs remain byte-exact, while
public command receipts retain execution status and full-output digests. A compact
actual `inspect` result is retained separately; verbose local diagnostics are not
a second proof graph or an additional semantic certification.

## Recorded native consumer results

The [recorded native inputs](../../corpus/native_extractions/round3/README.md)
contain actual reports, graphs, selected graphs, compact inspection outputs and
process receipts. Native reports use schema 2; their graph format is schema 1.1.
All selected local scopes are complete, while the overall graphs correctly retain
`extraction_status=partial` because external dependencies are outside scope.
Those boundaries include Mathlib, Init and Batteries, with exact module names in
the reports.

| Case | Local declarations | External boundaries |
| --- | ---: | ---: |
| Complete Eq19 probability statement | 65 | 532 |
| Independent product-law statement | 83 | 545 |
| Actual-definition semantic expectations and mutations | 135 | 556 |

The raw report, graph and selected files are unchanged native outputs. Build
receipts use the native adapter's public projection. Compact CLI receipts preserve
actual commands, exit status, input hashes and full-output digests; the compact
inspection file is an actual consumer result. None of these graph observations
replaces source fidelity review or human mathematical review.
