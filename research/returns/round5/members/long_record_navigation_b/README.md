# Long record navigation — independent review

**Start with `verdict.md`, then read `review.md` or process `findings.json`.** This return reviews the supplied round-five drafts as an interconnected mathematical reading experience: the two short papers, the long proof record, and the exact formal statements and evidence to which they direct readers.

There are **45 located findings: 7 high, 24 medium, 5 low, and 9 keep**. The 36 actionable findings are ordered by severity. The single `error` finding concerns the label attached to a local tournament counterexample; it does not claim that the main theorem or its tournament proof fails. The remaining findings concern navigation, organization, notation, figures, register, and the correspondence between prose and formal evidence.

## Contents

| File | Purpose |
| --- | --- |
| `verdict.md` | One-page judgment, five priorities, and the mathematical explanations to preserve. |
| `findings.json` | Authoritative structured return, with the exact required source hashes, locators, quotations, severity, impact, and suggested direction. |
| `review.md` | Readable rendering of the same 45 findings, with no additional findings. |
| `predecessor_review.md` | Follow-through on all 14 issues listed in the packet's earlier editorial review. |
| `sources_read.md` | Actual reading coverage, primary-source citations and editions, PDF inspection, and limits. |
| `evidence/arrival_audit.json` | All four incoming record links, 77 independently enumerated short-draft destinations, eight unlinked exposition locators, and 78 reading-closure checks. |
| `evidence/formal_claim_trace.json` | Seventeen central claim traces, 47 Lean-link range checks, and seven checks against recorded source hashes. |
| `evidence/pdf_navigation.json` | PDF link actions, missing passage destinations, malformed headings, and exact failed remote-PDF paths. |
| `evidence/local_counterexample_checks.json` | Independent check of the cycle example and precise scope of the local observations. |
| `evidence/quote_locations.json` | Exact matches and supplementary line locators for every finding's current-source quotation. |
| `evidence/source_status.json` | Unmodified source-status object supplied with the packet. |
| `evidence/packet_integrity.json` | Input CRC and manifest/hash checks. |
| `evidence/review_checks.json` | Scope and outcome of the independent second pass. |
| `checks/verify_return.py` | Standalone Python integrity and schema checker; uses only the standard library. |
| `checks/validation.json` | Packaging preflight results. |
| `MANIFEST.json` | Byte count and SHA-256 for every return file except the manifest itself. |

## Reading the evidence

Source paths beginning with `repository/`, `paper/`, `literature/`, or `exemplars/` refer to the **original supplied packet**, not to copied manuscripts in this return. Findings use current Markdown as authoritative; the disclosed older record-PDF paragraph is not reported as a new defect. PDF page numbers count from the first page of the supplied PDF. Exact quotations and section names are the primary locators; line numbers are supplementary.

The manuscript sources were not modified. This return provides advice, not replacement passages, new proofs, or requests for new formalization. Supplied Lean/Comparator receipts were inspected as historical evidence; no fresh Lean or Comparator run is claimed. Full scope, including sampled rather than exhaustive reading, is in `sources_read.md`.

## Recheck the return

After extraction, run from the extracted return directory:

```bash
python3 checks/verify_return.py
```

To additionally check current quotations and source hashes against the extracted original packet, and compare the ZIP with the extracted return:

```bash
python3 checks/verify_return.py --packet /path/to/original/packet --archive /path/to/quartic_r5_long_record_navigation_return.zip
```

These checks verify the return's structure, byte integrity and exact source binding. They do not certify the mathematical proofs.
