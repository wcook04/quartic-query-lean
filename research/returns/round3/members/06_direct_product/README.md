# Round-three return 06: the capped adaptive direct product

Prepared 2 November 2026 for the supplied packet `quartic_r3_06_direct_product.zip`.
AI agents produced this advisory return; no human mathematical review or
integration acceptance is claimed.

The assigned direct-product theorem is valid. This return supplies a complete
replacement of baseline §6.1, including the general joint-event corollary by
truncation, an exact adaptive-tree example, and updated evidence correspondence.
It preserves OpenAI's Lemma 4.1 and the original authors' attribution.

## Reading and integration

Start with `section.md`. Replace baseline §6.1 only, stopping before §6.2.
The original `CL-*` passage names are retained; additional passages have new
names. Local display labels (6.1)–(6.11) belong to this replacement and can be
renumbered by the integrating document owner without changing statement IDs.
The section expects the ordinary finite decision-tree conventions from §2.1
and supplies the capped-simulator interface needed by §6.5.

`worked_example.md` expands the exact example. Run:

```sh
python3 checks/check_adaptive_example.py
python3 checks/audit_packet.py /path/to/unpacked/quartic_r3_06_direct_product
```

Recorded successful outputs are in `checks/check_result.json` and
`checks/source_binding_result.json`. The first is finite rational arithmetic;
the second checks source bytes and supplied receipt contents. Neither invokes
Lean or Comparator.

## Return files

| File | Purpose |
|---|---|
| `section.md` | Self-contained replacement, complete proofs, stable passage anchors |
| `worked_example.md` | Adaptive example, conditional-event failure, global-budget counterexample |
| `correspondence.json` | Exact passage boundaries, claims, Lean types, premises, routes, citation roles, evidence |
| `lean_types.json` | 76 source signatures with full lexical context and 17 supplied elaborated type printouts |
| `NEW_STATEMENTS.json` | Separately registered joint-event, normalization, and example claims |
| `STATEMENT_CHANGES.json` | Empty: no canonical mathematical statement is silently changed |
| `LEAN_GAPS.md` | Remaining formal coverage boundaries and compound-row distinctions |
| `evidence_audit.json` | Source-current receipt findings, with fresh-run and missing-artifact limits |
| `references.bib` | Exact editions, locators, and source roles |
| `source_read_receipt.json` | Scoped reading, unavailable attachment, and unassessed material |
| `review_notes.md` | Ranked corrections, source comparison, authoring receipt, independent read disposition |
| `STYLE_RULES.json` | Located writing moves actually used, with scope and limits |
| `checks/` | Reproducible rational example and input-byte checks, outputs and validation |
| `manifest.json` | SHA-256 and byte counts for every other return file, plus input/source versions |

The supplied later native receipts match the current Lean source bytes. Their
existence supersedes the historical `UNELABORATED` comment for the live
conditional-value file. This review made no fresh Lean run, and no
declaration-specific Comparator pass is supplied for the direct-product
helpers. See `LEAN_GAPS.md` before promoting a prose statement to formal
coverage. No original source, adjudication, or baseline file has been changed.
