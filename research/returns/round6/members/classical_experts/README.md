# Round 6 return — classical expert panel

**Start with verdict.md, then questions.md.** This is an advice-only review of the three current documents in quartic_r6_classical_experts.zip, with the historical pasted trace used as sampled context. It contains **54 located findings: 32 recommendations/questions and 22 keeps**, from **11 paper-anchored perspectives**.

The most substantive comparison is in direct_product_comparison.md: the cited global-budget theorem already gives an adequate bound at the actual simulator cap. The remaining priorities concern the predecessor tradeoff, selective pointer access, the construction-specific simulator, consistent reading routes and truthful presentation of existing statement reviews. No new mathematical error is asserted in the proof chain examined.

## Files

| File | Use |
|---|---|
| verdict.md | One-page verdict, five priorities and essential keeps. |
| questions.md | Exactly twenty ranked questions with current-text locators. |
| findings.json | Required machine-readable findings, panel and exact copied draft hashes. |
| findings.md | Readable edition of the same 54 findings. |
| weighting.md | Current and recommended section allocations, with explicit measurement limits and reading-route denominators. |
| method_findings.json | Ten bounded recommendations for the supplied writing method, each tied to its existing rule and instance findings. |
| section_purpose.md | Purpose/treatment inventory for sections, figures, tables, examples and appendices; all 121 catalogue cards are covered by their ten groups. |
| reader_principles_assessment.md | Located assessment of all fourteen supplied reader principles. |
| direct_product_comparison.md | Detailed applicability and parameter check supporting CX001; preserves the exact fair lemma’s separate value. |
| research_scope.md | What was read, sampled or not read; primary source links, editions, scope and prior-fix distinctions. |
| checks/ | Source bindings, measurements and validation results. |
| verify.py | Portable standard-library checker for all contained file hashes; optionally checks quotations against the original extracted packet. |
| manifest.json | SHA-256 and byte size of every other file in this return. |

## Scope and integrity

No supplied manuscript, proof, skill or source file was modified. The review does not propose new theorems, stronger constructions or additional formalization. The named researchers’ papers anchor the perspectives; no opinion or quotation is attributed to a real researcher.

The delivered archive was tested for ZIP CRC integrity, safe member names, duplicate names, complete extraction and byte-for-byte agreement after extraction. All JSON files were parsed, all 54 exact quotation locators were matched to current Markdown and checked for the 25-word limit, the twenty-question count was checked, and the required copied draft hashes were matched to SOURCE_STATUS.json. The full validation record is in checks/validation.json. These are artifact and locator checks, not mathematical or formal-proof certification.

After extracting, run `python3 verify.py` from any working directory to verify the return’s manifest. To also recheck the original-document quotations and source bindings, run `python3 verify.py --source /absolute/path/to/extracted/original_packet`. The checker is read-only and needs only Python’s standard library; opening the archive runs no code.
