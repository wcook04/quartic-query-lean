# Maintenance-tool tests

Run `make check` from the repository root. It checks layout and generated files,
then discovers every `test_*.py` module here. These are Python tooling tests;
they do not run the Lean proof build or certify mathematical statements.

Use `make check-tests` to run just these tests. The
[contributor guide](../CONTRIBUTING.md) maps other changes to their source owners
and validation commands, and explains how to audit completed packet batches.

Test modules mirror the commands they exercise:

| Test | Command or contract |
| --- | --- |
| [test_check_repository.py](test_check_repository.py) | Working-tree and staged file placement, required owners and navigation links. |
| [test_check_packets.py](test_check_packets.py) | Completed ZIP integrity, manifest coverage and batch failure reporting, using temporary fixtures. |
| [test_build_challenges.py](test_build_challenges.py) | Generated Comparator challenges. |
| [test_run_comparator.py](test_run_comparator.py) | Exact configured comparison subjects; comments, helper proofs and specializations cannot acquire comparison credit. |
| [test_build_corpus.py](test_build_corpus.py) | Statement ties and separate evidence fields, including direct versus wrapper-mediated historical comparison credit. |
| [test_build_comparator_map.py](test_build_comparator_map.py) | Challenge block parsing, verified record passages, exact quoted glosses and direct-only comparison credit in the reading map. |
| [test_build_reading_api.py](test_build_reading_api.py) | Three-account navigation, passage and declaration provenance, fidelity and atomic edition export. |
| [test_build_lean_links.py](test_build_lean_links.py) | Statement-only line ranges, used-label link blocks, unknown labels, and the generated registry and paper blocks being current. |
| [test_render_reasoning_record.py](test_render_reasoning_record.py) | PDF navigation filter: anchor destinations, reviewed directory-link targets and unchanged record bytes (Pandoc required for the filter cases). |
| [test_render_papers.py](test_render_papers.py) | Paper renderer argument handling, default and per-paper output folders, refusal of output inside the checkout and the embedded numeric citation style (no Pandoc run). |
| [test_review_freshness.py](test_review_freshness.py) | Source-bound relation reviews, retained graph metadata and preprint-only provenance guards. |
| [test_build_research_packets.py](test_build_research_packets.py) | Review requests, source overrides and ZIP contents. |
| [test_build_funnel_packets.py](test_build_funnel_packets.py) | Writing requests, source selection and archive compatibility. |
| [test_build_round3_packets.py](test_build_round3_packets.py) | Focused primary literature and pinned dependency closures, portable writing inputs, source-bound receipt snapshots, frozen-input consistency and exclusive archive publication. |
| [test_build_round5_packets.py](test_build_round5_packets.py) | Critique packets bound to exact draft bytes: draft link map, record-since-PDF diff, exclusion of private sources and named readers, fail-closed missing literature and exclusive batch output. |
| [test_semantic_controls.py](test_semantic_controls.py) | Independently specified finite semantics and deliberately mutated Python models. |

Use temporary directories for test outputs. Tests of private external inputs
must identify their prerequisites; they cannot establish a portable build by
silently relying on another checkout.

[test_build_round9_packets.py](test_build_round9_packets.py) checks all three
lead-paper requests, complete previous-round inputs, sentence-audit obligations
and rejection of stale, incomplete or changed native render receipts.

[test_build_round10_packets.py](test_build_round10_packets.py) checks complete
original-return custody (including scripts and JSONL), nested decisions and
rebased links, exact Git-pinned method and code exports, source-bound
supplementary full texts, citation coverage and immutable destinations. Temporary
Git and custody fixtures exercise these guards without private annex inputs.

[test_reading_selection.py](test_reading_selection.py) exercises edition rebinding
and the actual ES module at theorem, example, figure and proof-step selections.

[test_retained_lines.py](test_retained_lines.py) checks the source bounds of
replayed tactic evidence and exercises retained and discarded tactic branches
with `QUARTIC_NATIVE_REPLAY=1` and the pinned Lean toolchain.
