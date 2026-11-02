# Formal obligations for the single-family section

Every proposed signature in NEW_STATEMENTS.json is **unelaborated**. No Lean compiler or lake executable is installed in this environment. This file distinguishes ordinary mathematical proof from compilation of that proof.

The attached BUILD_STATUS.md reports existing modules and marks ForrelationLower/Uniform.lean, and Paper/Section2–4, uncompiled. It also marks Model/Classical.lean's output older than its source. The adjudication identifies a stale commit attribution in the root build receipt. These qualifications prevent a new claim of a clean-pin root build. The historical Comparator receipt is a separate source report.

## Reading-order obligations

| Passage / displays | Statement IDs | Required work |
| --- | --- | --- |
| Main theorem (1)–(3) | sf-schedule; sf-total-lower; sf-AE-budget; sf-finite-rate-5; sf-limit-and-input-size | Assemble only after the uniform lower and new decoder have their own compiled proofs. |
| Uniform bound (4) | sf-uniform-forrelation | Compile the existing Uniform.lean source or independently formalize the reproduced parameter proof. The fixed-k bansalSinhaLower type does not imply this explicit uniform rate by unpacking. |
| Uniform arithmetic (5)–(6) | sf-uniform-parameters | Padding d=50kL+1, residual cancellation, promise gap and zero-depth case; source is currently uncompiled. |
| Auxiliary budget (7)–(9) | sf-floor-budget; sf-floor-transfer; sf-planted-numerical; sf-total-lower | Use generic Gvalue_lt_R_addressedF, not the stronger fixed-L threshold. Prove X≥2, L≤m, and both floor conversions. The direct product uses the source's alternative induction. |
| Existing quantum bound (10)–(11) | sf-T-and-repetitions; sf-B10 | Q_Fkm_le is existing evidence. Exact T equality, repetition substitution, B expansion and 2^53 envelope are new arithmetic. |
| Coherent decoder (12)–(13) | sf-amplitude-estimation-interface; sf-AE-margins; sf-majority-quarter; sf-AE-decoder; sf-AE-decoder-runs | Implement/import BHMT with exact controlled minus sign, retained work registers and a fixed off-promise cap. The sharper abstract cap128 compiles to physical256; the paper uses256 conservatively as its abstract cap too. A standalone QLe theorem is not an adequate interface. |
| Assembly (14)–(16) | sf-circuit-arithmetic; sf-generic-decoder-composition; sf-AE-count-arithmetic; sf-AE-budget | Rebuild address/comparison/verifier laws from the new Samples decoder. Current decode_samples and addrLaw hardwire the old law. Numerical substitution into Fkm_QLe is invalid. Reuse source generic tournament; the printed bound includes the compiler factor two. |
| Exact exponent (17)–(18) | sf-generic-quartic; sf-exact-exponent-5 | Transport the universal bound to BitLoc, show Q>1 and A>0, then divide in the correct directions. |
| Rate (19)–(21) and limit | sf-log-bounds; sf-log-upper-and-deficit; sf-balancing; sf-finite-rate-5; sf-limit-and-input-size | Floor cancellation, real logarithms, the denominator upper bound and ratio-deficit estimate, and squeeze. The universal quartic bound combined with the growing R lower bound proves Q diverges. |
| Baseline (22) | sf-exact-exponent-10; sf-finite-rate-10 | Same lower assembly and real arithmetic with the existing repetition algorithm. No BHMT theorem required. |
| Fixed-k diagonal paragraph | sf-diagonal-from-fixed-k | Choose increasing thresholds, define a finite prefix, and prove the asymptotic ratio using only existing fixed-k premises. |
| Obstruction paragraph | sf-square-root-barrier-for-estimates | AM–GM concerns the displayed sufficient estimates. It is not a lower bound against all possible quantum algorithms. |
| Input size (23)–(24) and following logarithmic bound | sf-input-cardinality; sf-input-envelope; sf-input-log-envelope; sf-limit-and-input-size | Cardinalities of sums/products/dependent pointer subtypes; 2^(40t)=m^20; 22s≤log2 n≤22s+4log2 s+14. No padding lemma is claimed. |

## Additional exact source arithmetic

The complete k_dependence.json records the canonical circuit width, whtCost recurrence and closed circuit size. Their new exact identities are covered by sf-circuit-arithmetic. Existing local-test cardinality and cost definitions are source-supported; their specialization to s=2t is elementary but must be elaborated in a final proof.

## Suggested implementation order

1. Compile and register Uniform.lean, then sf-floor-budget and sf-total-lower.
2. Prove sf-B10, sf-schedule, exact ratio and sf-finite-rate-10. This yields an explicit single-family result while preserving the existing quantum proof.
3. Add a decoder-generic upper wrapper, independently of BHMT.
4. Formalize the BHMT Samples interface and the threshold/majority decoder, then instantiate the wrapper for sf-AE-budget and sf-finite-rate-5.
5. Add the input-cardinality and limit wrappers; record axiom, build and comparison receipts at one clean source pin.

No original statement has been rewritten. STATEMENT_CHANGES.json is intentionally empty; stronger and differently quantified conclusions have new IDs. The job description's attribution of a literal growing-k uniformity remark is qualified in SOURCE_AUDIT.md without altering any preprint statement.
