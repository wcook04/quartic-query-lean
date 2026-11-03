# Round-five classical-mechanism return

Read `verdict.md` first, then `findings.md`. `findings.json` is the requested machine-readable return, with the source-draft hash object copied exactly from the supplied `SOURCE_STATUS.json`.

The 34 findings comprise 23 revision requests and 11 items to preserve. They are ordered by severity. Every quoted locator occurs in the current supplied Markdown and contains at most 25 words. This is advice only: the supplied manuscripts and Lean files were not edited.

## Files

| File | Purpose |
|---|---|
| `verdict.md` | One-page-scale judgement, five priorities and what to keep |
| `findings.json` | Authoritative structured findings in the requested schema |
| `findings.md` | Readable mirror of the same findings |
| `source_coverage.md` | Sources read closely, sources sampled, cited-only works, and exact limits |
| `citations.json` | Primary-source editions, URLs and locators |
| `review_notes.md` | Checks of existing examples/constants, rejected objections, and predecessor-review assessment |
| `checks/finite_examples.py` | Standard-library enumeration of the existing probability examples |
| `checks/finite_checks.json` | Results of those enumerations |
| `checks/input_integrity.json` | Input ZIP, supplied manifest and source-hash checks |
| `checks/link_checks.json` | Sampled Lean link ranges and selected statement text |
| `checks/quote_validation.json` | Exact matches and word counts for all 34 quotations |
| `checks/validation.json` | Validation of the deliverable’s structure and source binding |
| `checks/verify_return.py` | Safe archive CRC, member-hash and JSON validation; optional original-packet checks |
| `MANIFEST.json` | SHA-256 and byte length for every other file in this return |

## Recheck

With Python 3, after extracting the return:

```bash
python3 checks/finite_examples.py
python3 checks/verify_return.py /path/to/quartic_r5_classical_mechanism_return.zip
```

To recheck quotations and source binding against the original packet as well:

```bash
python3 checks/verify_return.py /path/to/quartic_r5_classical_mechanism_return.zip --source-packet /path/to/quartic_r5_classical_mechanism.zip
```

The verifier reads archive members without extracting them. It checks the complete member set, safe and unique names, CRCs, SHA-256 hashes, the findings schema and severity order. With the original packet it also rechecks all six draft hashes and every quoted locator. The return contains no copied input archive or full source packet; source paths in findings refer to the supplied packet unless explicitly identified as return checks.

## Evidence boundary

The original ZIP’s CRCs and all 72 entries in its supplied member manifest passed. Its three omitted SVGs are an input-package completeness problem, not archive corruption. The record’s Markdown is the current source; its earlier PDF was not substituted for it. Pending integration/build status was not treated as a finding. Existing draft PDF pages were rasterised for targeted visual inspection; no manuscript PDF was regenerated and no Lean or Comparator command was run.
