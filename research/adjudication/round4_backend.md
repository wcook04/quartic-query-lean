# Round-four backend adjudication

This records the backend decisions taken on round-four returns
[06](../returns/round4/members/06_corpus_fidelity/quartic_r4_06_return/review_notes.md),
[07](../returns/round4/members/07_publication_backend/quartic_r4_07_publication_backend_return/review_notes.md)
and [08](../returns/round4/members/08_adversarial_audit/quartic_r4_08_return/README.md).
The returns are preserved unchanged. The [machine-readable record](round4_backend.json)
lists each decision with what was actually run. No Lean build or Comparator run
was performed for this work; every statement below about receipts reads the
recorded files.

## Comparison credit (return 06)

Return 06 found that receipts written before the producer fix listed names
scanned from `exact QuarticQuery.*` proof lines beside the configured targets.
This was checked against the receipts and configurations themselves. All 20
positive Comparator receipts predate the `declaration_scope` field. Each one
whose `source_hashes` binds its `comparator.json` still matches the current file,
so its configured names can be recovered exactly; the five unbound legacy
receipts cannot, and are not current in any case. The comparison is:

| Rows | Tied declaration | Configured target? |
| --- | --- | --- |
| `def-R`, `def-Q`, `def-D` | `QuarticQuery.R_le_iff`, `Q_le_iff`, `D_le_iff`, `R_reindex`, `Q_reindex` | No: the targets are the `Checked` wrappers |
| `thm-1.1`, `cor-cubic-refuted`, `lem-2.1.i` | `theorem_1_1_unconditional`, `cubic_bound_fails_unconditional`, `ForrelationLower.bansalSinhaLower` and their `_of_bansalSinha` forms | No |
| `cor-unique-winner`, `prop-4.2-generic` | `winsAt_unique`, `Gvalue_lt_R_addressedF` | No |
| `lem-2.2`, `lem-2.2.i`, `lem-2.2.ii` | `Paper.construction_lemma_2_2_with_support` | Yes |
| `eq-19` | `Paper.eq19_whole`, `Independent.Eq19.checked_eq19` | Yes |

Return 06's count is confirmed: of the 12 rows previously reported as compared,
8 rest only on scanned aliases and 4 on configured targets.

**Adopted.** [build_corpus.py](../../tools/build_corpus.py) now credits a tie as
`compared` only for a configured target. New receipts state their scope
(`declaration_scope: configured_theorem_names_only`); a historical receipt's
configured names are recovered only through its bound, unchanged configuration
hash. Other listed names give `comparison_credit: wrapper_mediated_historical`
on the tie and the row value `wrapper_mediated_historical`. Graph receipt
subjects use direct targets only. The corpus now reports 4 compared, 8
wrapper-mediated and 109 not run. No receipt was rewritten.

This changes no theorem and does not suggest a wrapper is wrong: each wrapper is
an ordinary restatement whose proof applies the implementation. Direct credit for
the eight rows needs either the implementation names configured as targets in a
fresh comparison, or a reviewed type correspondence for each wrapper.

Return 06's Lean additions (degree semantics, zero-query characterization,
real-valued leaves) and its proposed tie changes are not integrated here. They
need a Lean build, which this work did not run.

**Consequences for the record.** The record's §2 evidence paragraph (line 450)
says "only 12 rows have qualifying comparison evidence". That is now the 4 + 8
split above. The manuscript bytes are deliberately unchanged; the designated
author should revise that sentence. The accepted review gate for the record
binds `corpus/statements.json` by hash, so regenerating the corpus makes that
binding stale (the Lean source snapshot `43f007e0…` is unchanged). This is the
intended effect of the gate, and a new acceptance is needed before further
round-four packets are built from this checkout.

## The Comparator reading map

[build_comparator_map.py](../../tools/build_comparator_map.py) generates
[comparator_map.json](../../corpus/comparator_map.json); the [corpus guide](../../corpus/README.md#reading-a-challenge)
explains its fields. It covers the 10 Challenge files named by any Comparator
configuration: 311 blocks, 87 distinct declarations.

| Measure | Blocks | Distinct declarations |
| --- | ---: | ---: |
| With at least one verified record passage | 232 | 64 |
| With a quoted primary gloss | | 36 |
| With a corpus statement ID | 22 | 22 |
| With a direct statement tie (no wrapper) | 3 | |
| Configured targets (`direct`) | 27 | |
| Definitions a configured statement depends on | 139 | |
| Displayed but used by no configured statement | 145 | |

All 289 record passages verify against their recorded hashes. The 23 explicit
gaps are mostly construction plumbing (`Circuit`, `Gate`, `BitLoc`, the `read*`
accessors, `pointerEquiv`), three Foundations wrappers without ties
(`R_le_D`, `Q_le_D`, `D_le_card`), both Tournament theorems and the two control
specifications. Of the 64 declarations with passages, 28 are reached only
through returned correspondence lists or claim lists without a claim marker, so
they have references but no quoted gloss: notably `AdaptiveProgram`, `QueryTree`,
`P` and `Fkm`. The record does not name them in backticks.

The map also shows what each Challenge actually pins. In the Unconditional
Challenge, `R`, `Q`, `totalise`, `alphaTot`, `UniversalPower`, `AdaptiveProgram`
and `QLe` are dependencies of the configured statements; `D`, `DLe`, `reindex`,
`promised`, `Phi` and `Tournament.IsComparison` are displayed but unused there.
The Tournament Challenge pins only `Tournament.IsComparison`. The three
Independent Challenges import project modules, so part of what Comparator trusts
is not displayed in those files: 70 declarations for `ConstructionFull`, 23 for
the whole equation (19) target, 5 for the independent equation (19) target, which
additionally imports `QuarticCorpus.Independent.Eq19.Spec` outside the dependency
export.

Glosses are exact excerpts of the record with passage and excerpt hashes; no
prose is authored. Backtick and wrapper proof-text joins are labelled as textual.

## PDF navigation (returns 07 and 08)

Both returns found the same defects in the accepted PDF (`40bc5c71…`): none of
the 339 authored anchors was a PDF destination, none of the 199 internal links
worked, and five directory links had become seven remote-PDF actions to
nonexistent `<dir>/.pdf` files.

Return 08 converts anchors to `\hypertarget` only, collapses anchor-only
paragraphs and maps the five directory links to named files. Return 07 adds
`\hypertarget` with `\phantomsection\label`, and offers an optional mode that
drops every local file link. Rendering this checkout with 08's filter under the
local Pandoc 3.9 left all 199 links undefined: this Pandoc emits `\hyperref[id]`,
which needs a label. One of 08's directory targets
(`checks/recheck_forrelation_circuit.py`) is its own reconstruction and does not
exist here, while the original `exact_example_checker.py` it replaced does.

**Merged.** The [renderer](../../tools/render_reasoning_record.py) uses 07's
destination macro, 08's paragraph collapse and an explicit directory-link table
whose targets must exist (the `checks/` link names `exact_example_checker.py`).
It refuses unreviewed directory links, internal links without an anchor, missing
PDF destinations and undefined LaTeX references. 07's portable-link mode and
XeLaTeX option were not adopted; Tectonic is available here and no standalone
copy is being produced.

An actual Tectonic render of the unchanged record gave 116 pages, 339 of 339
anchors as named destinations, 199 valid GoTo actions, no GoToR action, 137 URI
actions with every local target present, no word box outside a page and no
layout diagnostics. Per-page extracted text equals the accepted PDF's apart from
one glyph position on page 116, and page 3 was inspected as an image. The PDF
stays outside the checkout; `docs/reasoning_record.pdf` is unchanged because the
accepted review binds its hash. The render is not a new visual acceptance.

## Publication adapter (return 07): deferred

Return 07's adapter builds a `lean-exposition` bundle (963 nodes) from the corpus,
record and historical companions. It is deferred, for these reasons:

1. It reads `REVIEW_GATE.json` and `EVIDENCE_SNAPSHOT.json` from the round-four
   packet and refuses changed reviewed files. Against the gate preserved in
   return 08, `corpus/statements.json` no longer matches after the comparison
   reclassification. The adapter would correctly refuse until a new review.
2. It needs the external `lean-exposition` package and `jsonschema`. The tools
   here use the standard library only; adding a runtime dependency is a separate
   decision.
3. Its authored mappings are `not_reviewed` drafts, and its historical companion
   accounts concern the old funnel drafts that rounds 02 and 03 are replacing.
4. It predates the reading map and does not carry direct versus
   wrapper-mediated credit.

The adapter, wheel and tests were read but not installed or run here. Revisit
when the record is re-accepted: the adapter should then take the comparison
credit and the reading map's block-to-passage joins from the corpus rather than
from its own receipt-membership projection.
