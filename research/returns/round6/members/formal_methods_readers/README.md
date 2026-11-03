# Quartic round-six formal-methods reader panel

This is the requested **advice-only return**, bound to the supplied draft bytes. It contains **48 located findings**, including **18 preservation findings**, **20 ranked author questions**, and **9 proposed improvements to the general writing method**. The panel comprises six simulated expert perspectives; none represents an opinion attributed to a real person.

## Start here

1. **`verdict.md`** — one-page decision, five priorities and material to preserve.
2. **`questions.md`** — twenty questions in priority order, each with an exact current-text locator.
3. **`findings.md`** — readable register with reasons, directions, evidence and prior-round boundaries.
4. **`findings.json`** — required structured findings, panel descriptions and exact source hashes.
5. **`weighting.md`** — current versus suggested section shares for all three documents, including judgments on figures, tables, examples, remarks and appendices.
6. **`method_findings.json`** — quoted method rules, proposed changes and transfer tests.
7. **`principles.md`** — assessment against all fourteen supplied reader principles.
8. **`reader_interface.md`** — a bounded audit route and advice for displaying existing evidence and relationship provenance.
9. **`sources.md`** — exact reading scope, primary-source research and limits.

## Main result

The strongest recommendation is to make the evidence account internally coherent and usable. The current text already contains unusually helpful model bridges, negative examples and distinctions between checked endpoints and alternative ordinary proofs. The most important remaining defects concern review status, edition references and locally hidden semantic qualifications. The report does not propose a stronger theorem, a new construction or new formalisation.

One local mathematical omission is identified: exposition §6 omits the nonnegative range of alpha at a denominator-substitution step. The intended definition and expert companion already impose that range; this is not a finding that the main theorem is false. [FX025]

## Source and review boundary

- Current Markdown is authoritative. `SOURCE_STATUS.json` explicitly records that the reasoning-record PDF and accepted review do not match its current Markdown. Its 125 supplied PDF pages are only an older-layout proxy in `weighting.md`; current text shares are reported separately.
- `findings.json.source_sha256` is an exact copy of the input’s `drafts` object. Record hashes are preserved separately because the input keeps them outside `drafts`.
- Receipt acceptance is taken as supplied. No Lean compilation, Comparator run, example-checker execution or review-binding refresh was performed in this review. Reading the full record is not independent certification of every proof.
- Existing PDFs were opened and selected pages rendered for visual inspection. No new current-record PDF was produced.
- Six simulated perspectives organize the judgments. Statements about what a reader would do are reasoned predictions, not observations from human testing.
- Source paths and line numbers in citations refer to the **original input packet**, not copies inside this return. `sources.md` provides the source key and external primary links. The original papers and private context are not duplicated here.

High severity denotes a significant obstacle to interpreting the evidence presentation; no finding is marked critical. Eighteen keeps explicitly protect successful earlier corrections. Repeated themes across documents have distinct local locators because each document must work as a separate entry point.

## Integrity and machine-readable checks

`audit/source_integrity.json` records verification of all 293 input-manifest members, supplied draft/record hashes and input-archive integrity. `audit/validation_report.json` records output schema, quotation, count and manifest checks. `MANIFEST.json` and `SHA256SUMS.txt` cover every payload file except those two self-describing checksum files. `audit/validate_return.py` can check the extracted return with Python’s standard library; with `--packet /path/to/original/packet`, it also rechecks source hashes and exact quotations.

The final ZIP was tested for CRC integrity, safe unique member paths and agreement with a fresh extraction. A checksum manifest detects accidental changes; it is not a digital signature or independent authenticity guarantee.
