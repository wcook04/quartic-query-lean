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

## Integration gate

Source-level review, finite computation, Lean elaboration and independent
statement comparison remain separate. The candidate tie files accompanying
the proof reviews are review proposals with source hashes, not compilation
receipts. A compound statement needs all its conjuncts; an inequality-only
ingredient cannot inherit an exact relation from a different declaration.
Ordinary premises must also be distinguished from additional open assumptions.

The initial native inventory on the canonical SSD cache
(`cf_58aaa94feb484c52ad9e`) completed. Its runner and per-target receipts live at
`/Users/willcook/src/_builds/quartic-r2-ssd/native-inventory/`. One owner
sequences 45 targets, including all 39 Paper modules and the changed Forrelation
and upper-bound modules. Each uses the ordinary guarded `lake --no-cache build
<module>:olean`, with a 300-second per-target limit, 1740-second runner limit,
1800-second outer seat budget and continuously checked 8 GiB reserve. Failed
prerequisites skip their consumers; changes to local transitive inputs invalidate
a result. The runner does not add unaccepted imports to the root library.

The first inventory produced nine scoped passes (including the exporter fixture),
13 failures and 24 prerequisite skips. Concrete parser, API, opacity and arithmetic
elaboration errors were repaired in released files without relaxing theorem
statements. Retry 1 (`cf_2953adeb61e04202bc6d`, `native-retry-1/`) checked only
37 failed or blocked targets: 11 passed, 11 failed and 15 remained blocked.
Retry 2 (`cf_5cc3fc2c5d414927bdeb`, `native-retry-2/`) now checks the remaining
26 targets under the same reserve and bounded-run policy. Completed current
passes are not rerun. Each retry preserves earlier raw receipts.

`/Users/willcook/src/_builds/quartic-r2-ssd/current_native_acceptance.json`
collects source-closure, artifact and trace hashes for scoped acceptance; it is
not a global build or Comparator receipt. The sole native owner coordinates
repairs with source owners before rechecking them. Latest native output, not
this checkpoint narrative, determines which target is now accepted.

The byte-matched native exporter fixture passed in 15.07 seconds, including
private-wrapper and other-namespace reach, hidden-path witnesses, unresolved
constants and missing-root assertions. The first native Stein target passed in
28.12 seconds using the warm dependency cache. These are scoped results; they
are not an aggregate build, Comparator acceptance, or a repaired HDD.

The host's repository and user-level Codex wake kill switches remain present.
This detached job does not promise automatic chat continuation. Its per-target
results and terminal receipt are the continuation authority. Consume actionable
results and repair their exact diagnostics; do not submit duplicate jobs or keep
a model polling unchanged state.

The Python backend is tested against the installed `lean-exposition` consumer:
both schema and semantic contracts accept the informal graph, and selecting a
goal reaches its prerequisites. This is not native Lean extraction. The
existing packaged extractor remains the owner of a later formal declaration
graph. The tested command surface is `lean-exposition extract --build` with an
explicit module, goal, module prefix and output directory; it has not been run
on this changing proof set.

## Current validation and re-entry

The source-return checkpoint is `67b4400`. Backend corrections and native
exporter validation are committed at `57f264b`; reviewed assumption boundaries
and the conservative corpus refresh at `a2ac154`; the ten focused request sources
and tested round-three builder at `5e9868a`. Proof candidate edits remain in the
working tree until their native validation and source review are complete. The working-tree `make check` passes:
layout, challenge freshness, corpus freshness and 122 Python tests (two optional
checks skipped). A separate run enabled the installed reader integration and
passed it; the native Lean exporter fixture has since passed on SSD as recorded above. The regenerated
corpus retains historical passes as `legacy_unbound` and awards no current
build or comparison credit to this changing source set.

The next actions are to consume the SSD inventory results, repair concrete
elaboration failures, and validate the remaining targets without repeating
source-current passes.
Then select the accepted imports, review the candidate ties against those exact
bytes, build the combined library, record fresh source-bound evidence, run
Comparator and its negative controls, regenerate the corpus and validate the
reader projection. Prepare successor request sources while native validation runs; freeze and
build final packets from the accepted frontier afterward. Do not repeat
an old packet assignment whose requested endpoint already follows from a
stronger accepted theorem.

| Compatible work considered | Disposition at the dependency barrier |
| --- | --- |
| Return custody and all seven source audits | Preserved, checked and committed; further proof acceptance depends on compiler outcomes. |
| Literature and attribution | All thirteen supplied sources identified, exact discrepancies checked, and annex work committed. |
| Corpus and reader backend | Implemented and Python/consumer tested; native exporter regression passed. Actual root export, new proof receipts and independent semantic specifications remain separate gates. |
| Independent finite mathematics | Return checks replayed and per-claim limits recorded; these cannot certify the pending Lean modules. |
| Manuscripts and successor packets | Up to ten focused, literature-grounded long-record and formalization scopes are being prepared in [round3](../requests/round3/SELECTION.md); final ZIP construction awaits the accepted frontier. |
| Website and film | Require the settled corpus and authored accounts; no new visual surface is warranted yet. |
| Reusable repair | Snapshot validation now enforces original bytes in both working and staged views; its guide covers checker output isolation. |

This is an active bounded validation with a recoverable manual continuation,
not a completed proof campaign. The job IDs,
terminal files and per-module logs above make continuation recoverable without
repeating the research or assuming a successful build.

The next packet topics will be chosen from that validated remainder. In
particular, the full retained quantum state, the sharper Fourier theorem,
the growing-parameter family, and the literal Appendix route must not be
advertised as checked on the strength of returned source or finite examples.
Manuscript and reader work will consume the same statement evidence rather
than copying the reviews' proposed status labels.

## Round-three construction after native freeze

The [selection](../requests/round3/SELECTION.md) now owns ten focused assignments:
eight long-record mathematical sections, an evidence-path residual and an
independent review of the existing baseline. Each carries selected primary
literature, the exact Lean snapshot, original/adjudicated returns, the exposition
skill and its four writing guides, and role-labelled writing exemplars. The
whole baseline remains available, with focused mandatory reading for section
writers; only the baseline reviewer must assess the whole record now. Final
synthesis receives actual section returns later.

`tools/build_round3_packets.py` validates inputs without producing ZIPs by default.
The existing native setup at
`/Users/willcook/src/_builds/quartic-r2-ssd/round3-build/` contains explicit
input options and `refresh_options.py` / `run.py`. After the accepted source
snapshot, adjudications and native result files settle, refresh options, validate
the batch, inspect its input digest and build with that digest. This is an
internal consistency gate; the user has already authorized the ZIPs. The builder
checks input hashes before and after, preserves existing sent archives and runs
the independent archive validator. Intended output is
`/Users/willcook/Downloads/quartic_round3_20261102`, with a new suffix if needed.
No round-three ZIPs have been generated at this checkpoint.
