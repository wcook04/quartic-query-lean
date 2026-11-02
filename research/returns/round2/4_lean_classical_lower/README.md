# Sections 4–5 advisory Lean development

This archive supplies proposed Lean proofs and a statement-by-statement explanation for the randomized lower bound and exponent argument in OpenAI's *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*.

**All new Lean is unelaborated.** There is no new compiler, kernel, Comparator, or dependency-closure receipt. The source contains complete candidate proofs, and every coverage record has `compiled: false`. The finite arithmetic checks and source reviews described below do not change that status.

Start with [blueprint.md](blueprint.md). It gives the mathematics, exact proposed signatures, dependencies, corrections or qualifications, and proof-route assessment for every assigned statement. [LEAN_GAPS.md](LEAN_GAPS.md) identifies what is still missing or awaits compilation.

## Files

| File | Purpose |
| --- | --- |
| `lean/QuarticQuery/Paper/ClassicalDirectProduct.lean` | Actual adaptive transcript law, conditional optimum, one-step and product expectations, finite iteration, terminal success, capped direct product, exact budget floor. |
| `lean/QuarticQuery/Paper/ClassicalPlanted.lean` | Explicit sampling laws, symmetric coupling, discovery count and expectation, heavy columns, simulator, per-time and full-run bounds, randomized-program estimate. |
| `lean/QuarticQuery/Paper/ClassicalUniformZero.lean` | Uniform hidden-zero posterior derived from an actual positive-probability adaptive transcript. |
| `lean/QuarticQuery/Paper/ClassicalAsymptotics.lean` | Exact tail exponent and limit, numerical components, explicit eventual classical lower bound, finite quotient and divergence. |
| `coverage_plan.json` | All assigned identifiers, classifications, declarations, dependencies, proposed relations, and unelaborated status. |
| `NEW_STATEMENTS.json` | Auxiliary or stronger claims, with proposed signatures using existing vocabulary. |
| `STATEMENT_CHANGES.json` | Empty array. No canonical statement is changed. |
| `correspondence.json` | Exact anchored passages in the blueprint and their statement/declaration evidence. |
| `declarations.json` | Source locations of the new declarations. These are text locations, not elaborated types. |
| `sources.md`, `references.bib` | Primary references, exact locators, immutable source pin, and attribution roles. |
| `BUILD_INSTRUCTIONS.md` | Commands and evidence needed to promote source proposals after review. |
| `checks/`, `validation.json` | Reproducible finite checks and the limits of the validation performed. |
| `source_reads/` | Assessed, sampled, and unavailable source material, with the detailed reading receipts. |
| `return_manifest.json` | File hashes for this archive. |

## Main disposition

The conditional-value argument is developed as a separate proof, with the actual algorithm's success connected to its terminal potential. The absolute coupling is proved from the first differing queried bit. The conditional uniformity theorem computes the full adaptive transcript likelihood, and the exponent calculation preserves the paper's real exponent and fixed-parameter quantifiers.

The compound `claim-EZ` entry remains partial: its exact endpoint follows from the stronger existing zero-search theorem, but the paper's early/late decomposition is not formalized here. No tightness claim is made for the coefficient two under a worst-case depth cap. The formal model uses finite mixtures; an arbitrary external probability space has no newly formalized pushforward.

The original source tree, statement ledger, adjudication, and receipts are unchanged. This is an advisory source addition for the project's own pinned compilation and review.
