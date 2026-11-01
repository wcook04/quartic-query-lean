# quartic-query-lean

Research notes and a developing Lean corpus for the nearly quartic separation
between randomized and quantum query complexity in
[OpenAI's preprint](https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf).

Start with the [statement ledger](research/intake/statement_ledger.json) and its
[reading notes](research/intake/statement_ledger_notes.md). The ledger indexes
statements, dependencies and proposed formalisation targets; the notes explain
its sources, limitations and proposed order of proof.

These are unreviewed research materials prepared by AI agents. They do not
establish that the paper has been formalised. The committed corpus does not yet
include Lean build evidence. The preprint and its mathematics are OpenAI's.

## Repository map

| Path | Purpose |
| --- | --- |
| [research/](research/README.md) | Statement ledger, research evidence and maintained review requests. |
| [tools/](tools/README.md) | Package research ZIPs and check repository organisation. |
| [tests/](tests/) | Regression tests for maintenance tools. |
| [Makefile](Makefile) | Local repository checks. |

## Check the repository

With Python 3.10 or newer, Git and Make installed, run from the repository root:

```sh
make check
```

This checks file placement and local README links, then runs the Python tests.
It does not build Lean or check the mathematical claims. See the
[research guide](research/README.md) for the evidence categories and the packet
builder's local dependencies.

Licensed under [Apache-2.0](LICENSE).
