# Round-nine exposition review

## Start here

Read **verdict.md** for readiness, the twenty ranked changes and revision order. Then read **feedback_by_document.md** for the sustained critique. The return contains feedback and advice; it does not contain rewritten manuscripts.

The machine-readable register contains **135 distinct findings**, ordered by first encounter. The suggested 250-finding target was not met: 275 candidates were reduced by 107 merged overlaps and 33 withdrawals. Coverage was checked separately: all 439 lead Markdown lines, 730 audit units and all 21 PDF pages collectively. Sentence units total 604; the other 126 rows index displays, figures and other apparatus. The count is not a measurement of reader learning.

## Contents

| File | Purpose |
|---|---|
| verdict.md | Readiness by perspective, twenty priorities, revision order and gaps |
| feedback_by_document.md | Sustained lead-paper critique and shorter supporting-file notes |
| feedback.json | Source-bound findings with exact quotations, reader costs and repairs |
| sentence_audit.jsonl | 730 source-order reader-state and non-prose rows |
| coverage.json | Ranges, counts, source hashes, perspective scope and deviations |
| reading_log.md | Four byte-preserved frozen narratives, later corrections and teach-back |
| literature_comparison.md | Task-specific comparisons with editions and read/skimmed limits |
| previous_round_audit.json | 172 prior checks: {'resolved': 140, 'unresolved': 29, 'new-consequence': 3} |
| method_feedback.json | 15 applications/refinements of existing rules; no new rule proposal |
| mathematical_verification.md | Exact example results and the limits of those checks |
| evidence/ | Source ledger, first-pass hashes, consolidation, PDF/link checks and receipts |
| checks/verify_mathematical_examples.py | Reproducible exact finite checks; Python standard library |
| checks/verify_return.py | Schema, reference, source, byte-preservation and integrity checks |
| MANIFEST.sha256 | SHA-256 of every packaged file except this manifest itself |

## Evidence boundaries

The four readers are model-emulated perspectives. Root read two method files too early; perspectives ran concurrently rather than literally one at a time; fine-grained annotations were expanded after narrative freezing. These deviations and answer exposure are explicitly recorded. No human reading study, learning gain or blind independent trial is claimed.

No source manuscript was edited. No Lean, Comparator or repository build was rerun. The source packet's build receipts are historical. Newly run checks concern exact finite mathematical examples and the integrity and internal consistency of this return. A successful verification script is not certification of the general theorem or an endorsement of every pedagogical judgment.

## Reproduce the checks

After extracting this archive, run from its top-level review directory:

```sh
python3 checks/verify_return.py .
python3 checks/verify_mathematical_examples.py
```

To also verify current-source quotations and all supplied draft hashes, point to the original attached ZIP or its extracted contents:

```sh
python3 checks/verify_return.py . --source-zip /path/to/quartic_r9_exposition.zip
python3 checks/verify_return.py . --packet-dir /path/to/extracted_packet
```

To test the outer archive's CRCs, paths and embedded checksums without extracting it:

```sh
python3 checks/verify_return.py --archive /path/to/quartic_r9_exposition_return.zip
```

The final archive was also freshly extracted and checked before delivery. The verification scripts require Python 3.8 or newer and no third-party libraries. No external source text, original manuscripts or generated PDF page images are bundled.
