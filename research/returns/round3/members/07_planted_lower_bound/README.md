# Round 3, job 07: planted lower bound

This ZIP is an advisory return for quartic_r3_07_planted_lower_bound.zip. It contains a self-contained replacement for §§6.2–6.6 of the supplied long reasoning record, source-level correspondence, exact examples, evidence corrections, and an uncompiled proposal for the complete equation-(19) conjunction.

## Start here

1. **section.md** — the replacement mathematical section.
2. **review_notes.md** — findings, changes, citation roles, authoring receipt, and checks.
3. **LEAN_GAPS.md** — exact remaining formal/evidence boundaries, in section order.
4. **correspondence.json** — stable passage boundaries, claim IDs, full types, premises and evidence.
5. **EVIDENCE_CORRECTIONS.json** — changes to stale or incomplete evidence descriptions.

## Reproducible material

- **checks/planted_example.py** and **checks/planted_example.json**: exact XOR planted construction, all physical bits, simulator trace/cap, erased-zero identity, and a separate AND selection-bias counterexample.
- **checks/check_floors.py** and **checks/check_floors.json**: 187 exact integer/rational cases of the literal two-floor inequality, without a +1 slack.
- **checks/validate_return.py**: validate passage boundaries, JSON, types, bibliography keys, files, and final manifest hashes. Run with Python from any directory.
- **lean/Eq19Complete.lean**: proposed conjunction of separately evidenced equality and bound. It has not been compiled and does not formalize the early/late split.

The two computation scripts accept an optional output JSON path. Without it, they write next to themselves. After extracting this return, run:

~~~text
python checks/planted_example.py
python checks/check_floors.py
python checks/validate_return.py
~~~

These checks use the Python standard library. They do not run Lean or Comparator.

## Evidence and sources

**evidence/lean_declarations.json** preserves inspected source signatures and available compiler-reported types. **evidence/lean_evidence.json** records the supplied build/axiom receipts, input hash comparisons and current ties. The local source closure matches the receipts; their recorded compiled binaries are not included in the source packet and were not re-hashed here.

**source_read_receipt.json** distinguishes assessed sections, sampled papers, unassessed proofs and unavailable attachments. **references.bib** fixes the editions and citation roles. **STYLE_RULES.json** records the writing moves actually used. **NEW_STATEMENTS.json** identifies the new wrapper/example proposals; **STATEMENT_CHANGES.json** is empty because no canonical baseline mathematical statement was changed.

The original source packet remains the authority for source files and receipts. Its repository snapshot is labeled 1dd469dd0042b937b739da3bc211eeb60bdf7462. The internal manifest records the exact source versions and returned bytes. Neither this return nor a matching archive manifest constitutes mathematical acceptance, a new Lean build, Comparator acceptance, human review, publication, or a merged repository change.

The separate uploaded file Pasted text(20261102-190839).txt was unavailable. Its contents were not read or inferred. The work follows the complete assignment available inside the ZIP.
