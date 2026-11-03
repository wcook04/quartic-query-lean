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
| [test_build_corpus.py](test_build_corpus.py) | Statement ties and separate evidence fields. |
| [test_review_freshness.py](test_review_freshness.py) | Source-bound relation reviews, retained graph metadata and preprint-only provenance guards. |
| [test_build_research_packets.py](test_build_research_packets.py) | Review requests, source overrides and ZIP contents. |
| [test_build_funnel_packets.py](test_build_funnel_packets.py) | Writing requests, source selection and archive compatibility. |
| [test_build_round3_packets.py](test_build_round3_packets.py) | Focused primary literature and pinned dependency closures, portable writing inputs, source-bound receipt snapshots, frozen-input consistency and exclusive archive publication. |
| [test_semantic_controls.py](test_semantic_controls.py) | Independently specified finite semantics and deliberately mutated Python models. |

Use temporary directories for test outputs. Tests of private external inputs
must identify their prerequisites; they cannot establish a portable build by
silently relying on another checkout.
