# Round-two integration record

## Storage incident override — 2 November 2026

The operator has instructed that HDD-stalled work must stop and that available
SSD storage should be used for recovery. This overrides the earlier HDD-default
continuation below. Do not restart either original job against the HDD cache.

`cf_952e3e2332e04112bbcd` exhausted its seat budget with exit 117 and no
compiler diagnostics. `cf_bf3d0271e57c43479b86` was cancelled through its owner
with process-group cleanup; its observed child PIDs are absent. These are not
theorem failures or proof evidence. These old jobs have been superseded by the bounded SSD validation below.

The canonical project's `.lake` is now a real directory on the internal SSD.
Its old HDD symlink is preserved, without changing the HDD contents, at
`/Users/willcook/src/_builds/quartic-r2-ssd/original-hdd-lake-link`. An existing
SSD recovery workspace at `/Users/willcook/src/_builds/quartic-ssd/lean` occupies
about 7.3 GiB and has the same toolchain and package manifest. Mathlib and
complexitylib Git revisions match the pins, and the Mathlib compiled-artifact
directory is on the internal filesystem. The SSD had about 16.4 GiB free after attachment; the validation runner
enforces an 8 GiB reserve. This older workspace is a cache donor, not current proof-source authority.
Do not overwrite its source or copy the HDD wholesale. The governed Mathlib
import diagnostic `cf_ab1718082ee24aaea8ee` completed with exit 0 and
`Nat.add_comm` output in 66.9 seconds of recorded child execution. This proves
usable import artifacts, not the quartic candidates or restored HDD health.
The requested 60-second budget was not a strict millisecond deadline. Current
sources have been copied separately to
`/Users/willcook/src/_builds/quartic-r2-ssd/lean`, with their hashes in
`/Users/willcook/src/_builds/quartic-r2-ssd/source_snapshot.json`. The existing
`lean_build_cache.py workspace-attach` owner attached independent APFS
copy-on-write package clones to the source snapshot and canonical project.
The canonical receipt at `lean/.lake/workspace_cache_attachment_receipt.json`
records matching package revisions and semantic locks, clean package checkouts,
and a stable donor generation. This preserves warm artifacts without allocating
a second full dependency copy or sharing a mutable symlink.

The prior host-incident receipt already documented the hot-cache migration
mistake and the SSD recovery at
`ai_workflow/state/storage_doctor/hdd_throughput_20261102/MITIGATION.json`.
This task should have consumed that receipt before queueing more HDD builds.
Small changes in open import files did not establish acceptable completion
time. Keep both the storage health question and actual theorem validation open
until their respective bounded checks succeed.

The objective is a mathematically faithful statement corpus with separate Lean,
Comparator and literature evidence, from which the long reasoning record, short
expert paper, examples-first exposition and interactive reader can be derived.
The current task assimilates all seven supplied returns before selecting and
building a successor packet batch. Seven is a suggested batch size, not a
coverage target. No publication or correspondence is part of this intake.

## Inputs and decisions

The [intake manifest](../returns/round2/intake.json) binds all seven original
archives and their 178 file members. Both the working-tree and staged-view
snapshot validators were checked against the original ZIPs. Returned source is
immutable advisory evidence; repaired Lean lives in the Lean project.

| Review | Owner and scope |
| --- | --- |
| [Fidelity](round2_fidelity.md) | Definitions, statements, negative controls and cross-return conflicts. |
| [Construction and quantum](round2_construction_quantum.md) | Sections 2 and 3, coherent state and physical-query boundaries. |
| [Classical and Appendix](round2_classical_appendix.md) | Conditional potentials, planted transcripts, spectral and degree routes. |
| [Forrelation and exponents](round2_forrelation_exponent.md) | Sharp constants, uniform thresholds and the proposed single-family schedule. |
| [Literature](round2_literature.md) | All thirteen supplied sources, distinct editions and exact theorem locators. |
| [Evidence backend](round2_backend.md) | Source-bound receipts, traversal through hidden helpers and same-declaration evidence. |

The private literature annex work is committed in ai_workflow at
`57d4732df88aef3c3bd00cf7b347c0ec53624d1d`. That commit does not establish
any Lean theorem. Source variants retained locally are not licensed for
redistribution merely because they were supplied for review.

## Accepted source and evidence boundaries

The proof-source checkpoint is `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`.
All 45 inventory targets now have source-current native passes: 39 Paper modules
(including one print-only audit) and six Forrelation/upper-bound modules. The
initial inventory and nine bounded retries preserve diagnostics and exact
transitive input hashes under
`/Users/willcook/src/_builds/quartic-r2-ssd/`. Failed or superseded attempts remain
historical records; `current_native_acceptance.json` selects current passes.
Compiler repairs and the Boolean-expression grouping review are documented in
the individual adjudications, with original returns preserved unchanged.

Eight accepted imports join the non-audit Paper modules and uniform Forrelation
module to `QuarticQuery`. The combined root passed `lake --no-cache build
+QuarticQuery:olean` in 32.8 seconds. The source-bound ordinary root build and
actual dependency export then passed in 79.11 seconds. The root export records
2,652 projected declaration names, 1,354 reached from the headline, 61,138
traversed constants and no unresolved constants. Its 584 nonempty hidden-path
witnesses were checked against the projected graph. A separate traversal
reproduced the reached set; the earlier native fixture remains a scoped
regression, not a substitute for this actual export.

The 258 reviewed declaration names all exist in that environment. The native
type/axiom audit and its source-binding verifier pass, with axiom dependencies
limited to `Classical.choice`, `Quot.sound` and `propext`. Only one of these
reviewed helper names lies in the headline closure; helpers outside that
closure still have native checks. Kernel acceptance and headline reach answer
different questions.

The reviewed merge adds 164 ties to existing statement rows: 37 exact, 29
stronger and 98 partial. It preserves all 313 previous reviewed ties, including
the partial status of the whole `eq-19` claim. The merge checks statement,
source, signature and current native-receipt hashes before applying anything;
all 164 names were also found in the actual root export. It withholds seven
proposed research-derived rows, unknown return-local IDs and support-only
occurrences. These decisions do not manufacture build or comparison evidence.
The proposal, application receipt, audit, verifier and raw native records are
included in the next packets.

The merged 121-row corpus has 55 exact, 31 stronger and 35 partial formal
relations. Each row has a currently compiled tied declaration, but the 35
partial relations remain incomplete matches to their paper statements. Seven
rows have a compared tied declaration; the other 114 do not. None of these
counts constitutes independent human review or establishes a new theorem's
priority. Read the row's full type, premises and relation before using it in prose.

## Meaning, literature and remaining work

The literal Appendix chain is compiled, including the `1500625` quartic bound.
The `19600` hybrid and imported complexitylib `20736` route are distinct proofs
with distinct correspondence; no new priority or sharpness claim follows.
The revised elementary Forrelation constant is compiled at its recorded
threshold. This does not establish the sharper imported Fourier theorem, a
smaller dimension threshold, the BHMT decoder, or a complete explicit
increasing-`k` family.

Further work concerns specific meaning and interface boundaries: the full
retained quantum state rather than just its measured label law; the early/late
error decomposition and arbitrary probability-space transport; a complete
single-declaration equality-and-bound statement for `eq-19` with an independent
challenge; and independently authored semantic expectations for selected
models. Existing Comparator challenges share maintained vocabulary and theorem
specifications with the solutions. Separate compilation tests agreement, not
independent mathematical authorship.

The source-bound corpus backend and hidden-helper traversal are implemented.
The installed `lean-exposition` schema and semantic consumer accept the informal
graph and goal selection reaches prerequisites. The actual regenerated
121-row corpus, after the reviewed tie merge, was also validated and selected:
its headline selection has a 116-node authored argument closure. The receipt
and exact graph bytes are under `reader-acceptance/` in the SSD evidence root.
This observation precedes the last Comparator receipts; it is a consumer
check of those identified graph bytes, not a final evidence inventory. Actual native extraction by
`lean-exposition extract --build` remains a separate endpoint. Reviewed relation
freshness also needs enforcement independently of build freshness, and any new
research-derived graph rows need their own provenance rather than attribution
to the preprint. Packet 09 targets these residuals using the existing owners.

## Final checks and packet construction

The final serial evidence run is recorded at
`/Users/willcook/src/_builds/quartic-r2-ssd/final-evidence/operations.json`.
The phase passed at 2026-11-02T18:45:46Z. All twelve appended source-bound
receipts match the source pin and frozen inputs. Five positive Comparator
bundles passed, all five deliberately wrong solutions were rejected for their
expected reasons, and the unconditional bundle passed paranoid comparison.
These were local unsandboxed runs. The successful terminal receipt is required
by the packet input setup. It preserves a single source commit across the ordinary build,
258-name audit, five positive Comparator bundles, five negative controls and
unconditional paranoid comparison. The native runner continuously enforces an
8 GiB SSD reserve. The host's wake kill switches remain present; no automatic
chat continuation or repaired HDD health is claimed.

The [round-three selection](../requests/round3/SELECTION.md) owns ten assignments:
eight mathematical sections of the existing long reasoning record, an evidence
backend assignment and an independent review of the whole baseline. The section
writers work concurrently against the same baseline. Final synthesis is later
and receives their actual returns and adjudications; the short expert paper,
examples-first exposition and frontend follow the integrated long record.

Every packet carries relevant primary literature with version/locator details,
the frozen Lean sources and toolchain, the focused pinned complexitylib/cslib
source closure where imported, original and adjudicated returns, actual receipts,
and the exposition skill with four writing guides and labelled examples.
Literature supports mathematical claims; unrelated exemplars support writing
structure only. Required reading is focused on each assignment, with the full
baseline available and an honest source-read receipt required.

`tools/build_round3_packets.py` validates inputs without producing ZIPs by default.
The explicit local setup is
`/Users/willcook/src/_builds/quartic-r2-ssd/round3-build/`.
After final evidence and corpus regeneration, refresh options, validate the
complete batch and build with that exact input digest. The user has authorized
the ZIPs; the digest is an internal consistency check. The builder rejects input
drift and preserves existing sent archives. The independent archive validator
checks every payload byte. Intended output is
`/Users/willcook/Downloads/quartic_round3_20261102`, with a new suffix if needed.
Delivery and archive hashes are recorded with the generated batch, rather than
inserting an unverified completion claim here.
