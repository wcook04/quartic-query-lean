# Round-three return 01: query models and evidence

This advisory return replaces §§1–2 of the supplied long reasoning record. The mathematical claims of OpenAI's preprint retain their attribution and quantifier order. The return is not a final integrated paper or a new Lean proof campaign.

## Read first

- `section.md` is the complete replacement, with the existing ROOT anchors retained and new stable passage anchors added.
- `review_notes.md` records the substantive findings, revisions, writing decisions and authoring receipt.
- `verification_note.md` is the single central verification paragraph, extracted verbatim from the section for reuse.
- `correspondence.json` binds each passage and load-bearing display to source declarations or an explicit ordinary/finite/literature-only status.
- `model_contract.json` contains exact source signatures with their enclosing parameters, ordinary premises, additional assumptions and current supplied evidence. These are inspected source types, not a fresh elaborator printout.
- `statement_catalog.json` preserves the exact canonical statement texts referred to by this section and its proposals, without changing the source registry.
- `NEW_STATEMENTS.json` preserves prior proposed example IDs and registers additional expository claims. `STATEMENT_CHANGES.json` is empty because no canonical mathematical statement was changed.
- `LEAN_GAPS.md`, `references.bib`, `source_read_receipt.json`, and `STYLE_RULES.json` complete the requested handoff.

## Reproduce the finite checks

Use Python 3.10 or later; all checks use only the standard library.

```sh
python3 -E checks/check_models_exact.py
python3 -E checks/quantum_controls.py
python3 -E checks/semantic_controls.py
python3 -E checks/validate_return.py
```

The first two scripts independently specify small mathematical models and use exact rational arithmetic. The third is an unchanged copy of the supplied finite semantic control. Their saved outputs are under `checks/`. They neither execute Lean nor prove general model equivalence. `validate_return.py` checks the return's internal bytes, passage boundaries, type/evidence references and required files; it does not verify mathematics by compilation.

`checks/source_integrity.json` records a separate comparison of supplied manifest entries and source-bound receipts with the original packet. `source_read_receipt.json` distinguishes reading from byte inspection. Sources not assessed are marked as such, even when their hashes were checked.

`checks/return_validation.json` records the final internal checks. To recheck source excerpts when the original packet is available elsewhere, pass `--source-packet /path/to/extracted_input` to `validate_return.py`. Without that packet, the validator checks the return's internal consistency and reports that original-source checking was unavailable.

## Input boundary

The ZIP `quartic_r3_01_models_evidence.zip` was available. The separately attached `Pasted text(20261102-190821).txt` was unavailable and has not been read or inferred. If that text contains additional instructions, they still need to be reconciled with this return.

`MANIFEST.json` records exact byte counts and SHA-256 hashes for every other return member, plus the original ZIP and principal source versions. It excludes itself to avoid a circular digest. No original source, corpus tie, acceptance record or repository file has been modified.
