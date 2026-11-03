# Round-six return: students and teachers

**Recommendation:** the exposition is assignable with a lecturer’s guide. Concentrate the next revision on the coherent sampler, the capped simulator, and the reading transitions. Preserve the mathematical and evidence qualifications added in round five.

This is an advice-only return for `quartic_r6_students_and_teachers.zip`. It contains no rewritten manuscript, new theorem, new construction, proposed stronger bound, or requested new formalisation. No source manuscript, skill or repository was changed.

## Read in this order

1. `verdict.md`: one-page decision and five priorities.
2. `questions.md`: twenty questions, in priority order.
3. `findings.md` or `findings.json`: the same 43 located findings, with evidence and round-five relations; 32 issues/questions and 11 keep items.
4. `weighting.md`: measured page shares and proposed allocations for the two 14-page papers; retention and assignment roles for the 125-page supplied record PDF.
5. `method_findings.md` or `method_findings.json`: nine proposals for improving the general writing method, distinguishing weak instructions from failures to enforce good ones.
6. `coverage.md`, `reader_principles_audit.md`, and `sources_read.md`: element-by-element purpose, all fourteen review principles, source comparisons, reading depth and limitations.

## Evidence and checks

`evidence/` records the input status, source/member hashes, exact quote inventory, page-boundary measurements and the question index. `checks/` contains the validation report and standard-library scripts for the finite examples and return structure. `MANIFEST.sha256` binds every other delivered file.

The six hashes in `findings.json.source_sha256` are copied exactly from the input `SOURCE_STATUS.json`. Every finding quotes at most 25 words from the current Markdown, with an exact line locator. Current Markdown controls all findings. Page references identify the supplied PDFs and are not a claim that the record has been freshly typeset from its current source.

High severity means a material obstacle to the promised reading outcome, not an allegation that the theorem is false. The panel consists of modeled student and lecturer perspectives. Nobody’s actual opinion is invented, and no student performance was measured.

## Reproduce the checks

From this extracted directory:

```bash
python3 checks/validate_return.py
python3 checks/exact_examples.py
```

For exact quote and input-manifest checks against the original packet:

```bash
python3 checks/validate_return.py --source-zip /absolute/path/quartic_r6_students_and_teachers.zip
```

These checks validate the return’s structure, citations to supplied files, finite illustrations and byte integrity. They do not compile Lean, run Comparator, or establish the asymptotic separation theorem. No external installation is needed for the two validation scripts.
