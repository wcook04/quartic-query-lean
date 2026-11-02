# Round-three return 04: the addressed construction

This return supplies a self-contained replacement for §4 of the frozen long reasoning record. The addressed construction is sound under the exact two-output circuit interface: the semantic winner predicate is total and has at most one winning pair, the local tests characterize it on every raw input, and a genuine winner defeats any opponent when its own address is decoded correctly.

The mathematical construction and separation belong to OpenAI. This is an advisory exposition and evidence review, with a new finite example and explicit interface explanations. It is not an integrated manuscript or an acceptance decision.

## Read first

- section.md: the replacement section, ordinary proofs, four-column example and references.
- review_notes.md: substantive changes, source/evidence findings, review dispositions and authoring receipt.
- LEAN_GAPS.md: exact remaining formal-correspondence limits.

The pasted-text attachment was unavailable. This return follows the instructions and sources actually readable in quartic_r3_04_addressed_construction.zip.

## Reproduce

From this directory:

~~~sh
python3 examples/check_example.py
python3 checks/validate_return.py
~~~

The first command prints deterministic JSON using the Python standard library and exact arithmetic. The second checks the package, passage boundaries and saved example output. To also verify the original source bindings:

~~~sh
python3 checks/validate_return.py --source-packet /absolute/path/to/extracted/original/packet
~~~

The example uses actual P_{2,4} and an exact 180-gate circuit checked on all 256 inputs. Its r=2 is schematic; the paper uses r=40 at m=4. It has 371 tests per candidate and a completely specified 5,936-bit base board. The sole winning pair is column 1, address 10. A second board shows that omitting domain tests falsely accepts an unpromised column. The positive Φ=1/2 and unpromised Φ=-1/2 inputs give the specified projection decoder the same Bernoulli(1/4) law.

## Evidence

The supplied root-build and selected type/axiom-audit records include the newer arbitrary-index retained-workspace theorems. All 124 recorded local Lean/config hashes match the packet bytes. This review checks those bindings and membership; it does not rerun Lean or Comparator.

The Construction Comparator covers winsAt_unique, existsUnique_gateConsistent, winner_no_incoming_zero and winner_finds_zero, plus their checked wrappers. It does not compare the complete local-test theorem.

The retained-workspace evaluator uses at most 2q physical bit queries, q=max(3,ℓ+1). A clean XOR interface is proved separately by compute-copy-uncompute, at most 4q queries. No exact Lean theorem is claimed for that clean interface.

## Contents

| File | Purpose |
|---|---|
| section.md | Complete replacement with 19 passage anchors and 19 numbered displays. |
| correspondence.json | Full Lean types, premises, source hashes and evidence per claim/display. |
| NEW_STATEMENTS.json | Four supplemental records: example, domain-test counterexample, equal projection law, clean oracle. |
| STATEMENT_CHANGES.json | Empty: no canonical statement silently changed. |
| LEAN_GAPS.md | Remaining clause/type/evidence limits, in section order. |
| references.bib | Exact inspected editions and citation roles. |
| source_read_receipt.json | Scoped reading and all 400 manifested members, with unassessed/unavailable entries. |
| STYLE_RULES.json | Source-located writing moves actually used and their limits. |
| review_notes.md | Corrections, reasoning, simplification and authoring receipt. |
| integration_map.json | Replacement boundary and old-to-new passage map. |
| examples/ | Checker, circuit, complete base board, deterministic output and explanation. |
| evidence/ | Independent AI source/type reviews and evidence bindings. |
| checks/ | Portable validator and its actual result. |
| manifest.json | Exact lengths/digests for every other return member and source versions. |

The full earlier manuscript, unrelated lower-bound/tournament proofs and future round-three returns are outside this contribution's assessment.
