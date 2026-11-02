# Maintenance-tool tests

Run `make check` from the repository root. It checks layout and generated files,
then discovers every `test_*.py` module here. These are Python tooling tests;
they do not run the Lean proof build or certify mathematical statements.

Test modules mirror the commands they exercise:

| Test | Command or contract |
| --- | --- |
| [test_check_repository.py](test_check_repository.py) | Working-tree and staged file placement, required owners and README links. |
| [test_build_challenges.py](test_build_challenges.py) | Generated Comparator challenges. |
| [test_build_corpus.py](test_build_corpus.py) | Statement ties and separate evidence fields. |
| [test_build_research_packets.py](test_build_research_packets.py) | Review requests, source overrides and ZIP contents. |
| [test_build_funnel_packets.py](test_build_funnel_packets.py) | Writing requests, source selection and archive compatibility. |

Use temporary directories for test outputs. Tests of private external inputs
must identify their prerequisites; they cannot establish a portable build by
silently relying on another checkout.
