# Round-four research returns

These seven submissions answer the [round-four requests](../../requests/round4/).
They are advisory evidence: neither preservation nor a reported result
establishes correctness, a build or a comparison. Decisions belong under
[adjudication](../../adjudication/).

Each return carries its full packet context (record, Lean tree, literature,
wheels), so the original archives and extracted members stay local under
`archives/` and `members/`, which Git ignores. [intake.json](intake.json)
records every original archive and member by size and SHA-256;
`python3 tools/intake_round4_returns.py --verify` checks a local copy against it.
Do not run submitted programs as part of intake.

| Return | Focus | Archive SHA-256 |
| --- | --- | --- |
| 02 | Short expert paper | `addbd3b9fe0d3e0a86c1297efb5716509b4d1c44eed6c06c350103971e033eec` |
| 03 | Examples-first exposition | `a5a179b422ab2dacfd63916ee62f272c7a8ca00499664d78d215806a82314a8b` |
| 04 | Quantum completion | `354a20dc499a05e8b64b425af2a47daa3bb5fd2bc6eb26d6eca2cc320c895549` |
| 05 | Classical completion | `64fb02ca68039d8d9279488fd78db7fedc525a98fc89d149b651ae1e0c2819de` |
| 06 | Corpus fidelity | `f121540d787c0136e4bce0466333b2fb27b1e3da236ef481a8e05c19bb333dc0` |
| 07 | Publication backend | `02522f2a3be972e93a3bf709d8a4f113a05a84413d7384e822de1f8b3c56634b` |
| 08 | Adversarial audit | `866cbf3900c6743d2155391cc9603c964c372f772ece473d1531c50cc44961e8` |

The chat summaries that accompanied the returns were not preserved separately;
their substance is in each archive's README and review notes. Returns 02, 05
and 06 ended by asking for approvals inside their own environments (a library
upload, or running Comparator without its sandbox); those requests do not apply
here.
