# Quantum-experts review — round six

This ZIP is the complete advice-only return for packet `quantum_experts`, dated 3 November 2026. It reviews the exact supplied working drafts. It contains **52 located findings: 37 questions or changes and 15 keep recommendations**, organized through ten source-grounded perspectives. No opinions are attributed to real researchers.

## Start here

1. **[verdict.md](verdict.md)** — one-page verdict and the five changes that matter most.
2. **[assessment.md](assessment.md)** — the technical reasoning: prior algorithms, weighted sampling, state/label contracts, the Forrelation choice and exponent history.
3. **[questions.md](questions.md)** — twenty prioritized questions with exact current-text locators.
4. **[findings.md](findings.md)** — readable findings; **[findings.json](findings.json)** is the structured authority.
5. **[weighting.md](weighting.md)** and **[component_inventory.md](component_inventory.md)** — page-share judgments and the purpose of sections, figures, tables, examples, remarks and appendices.
6. **[reader_principles.md](reader_principles.md)** — all fourteen supplied criteria assessed.
7. **[method_findings.json](method_findings.json)** — one narrow rule-priority tension, with rejected method diagnoses and local application failures kept separate.
8. **[sources_read.md](sources_read.md)** and **[reading_coverage.json](reading_coverage.json)** — exact editions and honest full-versus-sampled coverage.

## Central judgment

The weighted pivot distribution, winner-only guarantee, stopped coupling and complete query budget are the quantum center. Preserve them. The highest-priority corrections reconcile stale evidence prose, distinguish the existing opaque returned-state theorem from the sufficient physical measured-law route, align reader routes, and restore detailed recovery of the newer growing-k remark. No mathematical error in the current drafts was demonstrated by this pass; that is not an independent proof certification.

The expert companion was read first. All three current Markdown documents and the original preprint were covered in full across the review team. Of 42 supplied literature entries, three were read in full, eleven at specified passages, and twenty-eight were not independently read. The large historical trace was searched and sampled. Source-assisted editorial review is distinct from human review or fresh machine verification.

## Version and evidence boundaries

- `findings.json` copies the exact `drafts` hash object from the supplied `SOURCE_STATUS.json`; record hashes are recorded separately.
- The two short PDFs have 14 pages each. The 125-page record PDF is an older rendering, so current record findings use Markdown locators and its weighting uses an explicitly labeled proxy.
- Receipt outcomes were accepted as stipulated. No Lean compilation, Comparator run or kernel replay was performed.
- No original manuscript, skill, theorem or formalization was changed. Recommendations ask for explanation, weighting, reconciliation or recovery of existing material.
- Paths to manuscript/literature evidence are relative to the original input archive. That source corpus is not duplicated in this return.

## Integrity

`manifest.json` gives a SHA-256 digest and byte size for every payload file except the manifest itself. `checks/payload_validation.json` records the content/source checks. The finished ZIP was also CRC-tested, extracted into a fresh directory, and compared byte for byte against the manifest and source payload. These checks concern archive/document integrity, not correctness of the mathematical theorem.

After extracting the ZIP, verify it with Python 3.9 or newer (standard library only):

```bash
python checks/validate_return.py
```

To additionally recheck exact quotations and draft hashes against the original source packet:

```bash
python checks/validate_return.py --source /path/to/quartic_r6_quantum_experts.zip
```

The `--source` argument also accepts a directory containing the original extracted packet. Verification is read-only and does not execute any supplied manuscript code.
