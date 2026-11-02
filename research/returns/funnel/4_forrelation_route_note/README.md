# Forrelation route research return

**Research date:** 2 November 2026. **Source pin:** `c7e0c9161f0ad898889bd9166e7b354acd42188d`.

The proposed improvement in the dependence on `k` is **proved as a paper deduction in the explicit regime `k >= 2`, `m >= 2^(15k+2)`**. The elementary argument gives the fully numerical constant `2/18225` with denominator `k^2 ln(4km)`. Combining the identity with Sherstov–Storozhenko–Wu's published binomial Fourier estimate removes the explicit inverse polynomial in `k`, when the bound is expressed using block size `m`. The exact constant in that consequence is `eta^2/(162 e C^2)`, where `C` is the absolute, numerically unspecified constant in their Corollary 4.14. Both the threshold and the distinction between block size and total input length remain part of the conclusion.

The existing Lean theorem is the weaker fixed-`k`, eventually-in-dimension statement. The new endpoints have not been compiled in Lean. The note supplies the complete elementary proof and a complete deduction of the sharper endpoint from the cited Fourier theorem. It does not reproduce the entire published proof of that external theorem.

## Reading order

| File | Purpose |
| --- | --- |
| `note.md` | Mathematical definitions, the single-block identity, complete elementary argument, sharp consequence, and scope. |
| `quantitative.md` | Finite inequalities, their inversions, every parameter choice, comparison of three Fourier inputs, and the conservative next formal endpoint. |
| `prior_art.json` | Ingredient-level findings: known, partly known, or not found within the documented search. |
| `references.bib` | Version-pinned primary references. |
| `correspondence.json` | Exact anchored passages and display-level mappings to statements and relevant existing Lean declarations. |
| `NEW_STATEMENTS.json` | Proposed statements and signatures, including source lemmas newly registered for this note, stronger paper results, external inputs, and arithmetic substeps. |
| `STATEMENT_CHANGES.json` | Corrections to supporting-document claims; the frozen corpus theorem statements are unchanged. |
| `LEAN_GAPS.md` | Formal evidence and missing obligations in reading order. |
| `SOURCE_AUDIT.md` | Source semantics, manifest integrity, reading coverage, historical execution evidence, and limitations. |
| `SEARCH_LOG.md` | Search queries, version checks, forward-citation coverage and reading limits. |
| `VALIDATION.md` | Mathematical review and reproducible finite checks. |

The auxiliary JSON files preserve the forward-citation inventory, contemporary abstract/body screening, declaration locations, and a proposed corpus metadata repair. `checks.py` and `checks_output.json` preserve the finite calculations.

## How to read the evidence files

The `lean` array in a correspondence entry identifies relevant existing declarations. It is not a claim that every listed declaration proves the entire passage. Exact matches, specializations, stronger statements, changed proof routes, and missing formal work are distinguished in `NEW_STATEMENTS.json` and `LEAN_GAPS.md`.

Every proposed signature is unelaborated. Its `proposed_lean_context` supplies the imports and open namespaces. Signatures that reproduce an existing declaration are labelled as such and should not be added a second time. Other signatures use existing definitions or local finite expressions; they do not silently assume a new error-parameterized complexity or restriction datatype. General powers of two in the mathematics remain broader than the public `m = 4^t` family used in the endpoint signatures.

The declaration index reports historical dependency metadata and exact source locations. It omits proof text and is not a kernel certificate. No Lean, Lake, Comparator or external-kernel replay was run in this environment. The attached source trace supplies historical executions, identified as such in `SOURCE_AUDIT.md`.

No claim of priority is made. The search found substantial antecedents and did not locate the exact matched single-block Stein chain in the sources examined. The search record identifies incomplete citation indexes and papers read only in part. This return is advisory; it makes no repository changes.
