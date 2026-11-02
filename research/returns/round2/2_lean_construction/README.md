# Lean for Sections 1 and 2

This return contains proof drafts and a statement-by-statement review of the 29 requested entries in the round-two construction task. The principal endpoints are explicit versions of Lemmas 2.1 and 2.2, including retained coherent physical implementations. The original paper and construction are OpenAI’s.

**Every new Lean file is unelaborated.** Neither `lean` nor `lake` was available, and the attachment contains no compiled dependency cache. The source review and static package checks establish no new kernel, Comparator or dependency-closure result. No person has reviewed this work.

## Read first

1. `blueprint.md` gives the mathematical statement, exact Lean signature, named proof dependencies, corrections, source locations and remaining obligations for every target. It begins with the principal lemmas.
2. `REVIEW_NOTES.md` explains the mathematical and bibliographic decisions that affect those statements.
3. `LEAN_GAPS.md` separates the universal compilation requirement from the remaining statement and proof-route qualifications.
4. `coverage_plan.json` supplies the requested machine-readable plan. Every `compiled` flag is false.

The proof sources are under `lean/QuarticQuery/Paper/Construction*.lean`, all in namespace `QuarticQuery.Paper`. `ConstructionAudit.lean` imports the delivered modules and supplies axiom-printing commands for the receiving environment. It has not been run.

`NEW_STATEMENTS.json` records supplemental finite bounds and intermediate claims. `STATEMENT_CHANGES.json` is empty because this return preserves the current adjudicated statements. Stronger companions are separate records, and older ledger errors are identified as historical corrections. No correction of the attached preprint is proposed merely because an earlier ledger was inaccurate.

`correspondence.json` maps each anchored blueprint passage to statement IDs and full declaration names. `row_details.json` retains the richer review notes and contextual binders. `source_records/target_statements.json` preserves the original selected records for comparison. `REFERENCES.md` and `references.bib` supply versioned sources and precise locators.

## Principal results in the source drafts

The complete Lemma 2.1 declaration combines the existing fixed-parameter randomized lower bound, an amplified quantum test with an all-input worst-case query cap and Boolean output law, and an exact two-output circuit of the required size. Its physical coherence clause identifies the same logical isometry with a physical program through every continuation. The older sampler/output-law conjunction remains a helper.

The complete Lemma 2.2 declaration combines the exact number of tests, an explicit cubic-logarithmic size bound, all-input winner/test equivalence, adaptive classical depth, arbitrary complex superpositions of test indices, and a physical implementation of the same coherent witnesses. Its work registers are retained. It preserves every continuation probability for each embedded logical state.

The family statement uses the specified circuit `Forrelation.forrCircuit`, with explicit constants `c = 1/400` and `b = 6`. These are wrappers around the supplied development. They are not claims of a new query-complexity separation or a new lower-bound method.

Two larger scope limits remain. The projection routine has a supplied `2k`-query implementation and a separate one-call phase identity, without a complete tight `k`-query physical witness. The exact circuit endpoint and size use modular arithmetic; the ideal integer bounds are not a full correspondence theorem for every internal register. Detailed qualifications are in `LEAN_GAPS.md`.

## Reproduce in the pinned project

The source overlay targets repository commit `4c7544f8dcdfc18d3ecf8476ebd8c1090cd46f15` from the attachment. It adds modules; it does not replace existing source files, evidence records or public statements. The receiver should review and copy the delivered `lean/QuarticQuery/Paper/Construction*.lean` files into a checkout containing that source and its pinned dependencies.

Pinned versions from the supplied configuration:

| Component | Revision |
| --- | --- |
| Lean | `leanprover/lean4:v4.36.0-rc2` |
| Mathlib | `69552756cd8a2d2d48763cf7279fd814d6a1224d` |
| complexitylib | `62ca5c21461b2482e8bd12b7cb9b4937d887a33a` |
| CSLib | `254e30e6d4299c51323aaeaf5f51a4763b375d4a` |

From the receiving project’s `lean/` directory, proposed commands are:

```sh
lake build QuarticQuery.Paper.ConstructionAudit
lake env lean QuarticQuery/Paper/ConstructionAudit.lean
```

These are instructions for a future run, not reported successful commands. Resolve any elaboration errors before recording evidence. Inspect the exact resulting types and axiom output, then add independently reviewed ties and any appropriate Comparator challenges. Record the build at a clean commit containing the source. Keep statement coverage, build status, Comparator status, proof route and dependency reach separate.

## Static validation

`checks/validate_package.py` checks the target set, required JSON fields, unique declaration names, absence of proof placeholders or custom axiom declarations, unelaborated labels, documented Ledger tags, passage anchors and local import resolution. With the original attachment extracted, run:

```sh
python3 checks/validate_package.py --base /absolute/path/to/original-extracted-packet
```

Without `--base`, the checker validates the self-contained return and identifies external imports without claiming to resolve them. `validation_report.json` records the actual static check performed here. It is not a Lean build receipt. `SOURCE_RECEIPT.json` records input hashes, the source pin, environment limits and reading scope. `manifest.json` hashes the final files.
