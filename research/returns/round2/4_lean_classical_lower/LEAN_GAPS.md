# Lean gaps and evidence limits

Every new Lean file is **unelaborated**. The source contains complete candidate proof terms, with no `sorry`, `admit`, custom axiom, or `native_decide`. Textual checks cannot establish that Lean accepts them. Every coverage entry has `compiled: false`; no existing statement evidence is promoted by this advisory return.

The reading order below matches the assigned list. A source-level claim of exact correspondence is a proposed tie for review, not a build receipt. The exact endpoint for `claim-EZ` is present by an alternative route; its compound early/late statement remains partial even if the endpoint compiles.

## Direct-product route: remaining evidence boundary

All new declarations in `lean/QuarticQuery/Paper/ClassicalDirectProduct.lean` are **unelaborated**. There is no fresh kernel, build, Comparator, or reachability receipt. The supplied compiled status of `LowerBound/DirectProduct.lean` is source evidence for the existing helper declarations, not for the new normalized route.

1. **`claim-product-law`.** Proposed proof: `classical_prefix_iff` and `classical_transcript_product_law`. Actual schedule consistency and the product event are proved in source. Await compilation and a reviewed tie.
2. **`def-value-V`.** Proposed definition `classicalTranscriptValue`, with `classicalTranscriptValue_attained` and `classicalTranscriptValue_bounds_tree`. The continuation budget is exactly `L - classicalQueriesTo τ h`, with repeated queries counted. Await compilation and a reviewed tie.
3. **`eq-16`.** Proposed theorem `classical_eq_16_transcript`, together with `classicalTranscriptValue_unchanged`. Zero-mass branches and unchanged other factors are handled in source. Await compilation and a reviewed tie.
4. **`claim-supermartingale`.** Proposed actual-prefix theorem `classical_transcript_conditional_expectation`, with local positivity derived by `classical_transcript_mass_pos`, finite iteration `classical_terminalValue_le`, and the actual algorithm bridge `classical_success_le_terminal`. This is a finite conditional-probability formalization. No claim is made to instantiate Mathlib's measure-theoretic `Supermartingale` structure. Await compilation and a reviewed tie.
5. **`claim-final-bound`.** Proposed theorem `classical_final_bound` states both inequalities. Await compilation and a reviewed tie.
6. **`eq-17`.** `Gvalue` already implements the corrected definition; `classical_eq_17_floor` proposes the exact real-floor wrapper using pinned `Nat.floor_div_eq_div`. Await compilation of the wrapper and review of the existing definitional tie.

The three additional representation statements in `NEW_STATEMENTS.json` are source-only as well. The complete deterministic and finite-mixture direct-product consequences are supplied as supplementary lemmas. The finite-mixture formal model does not itself formalize arbitrary external probability spaces or the pushforward of such a space onto finitely many possible trees; that is the remaining generality boundary for the informal word “arbitrary.”

## Lean gaps: planted-input subsection

Every new declaration in `ClassicalPlanted.lean` and `ClassicalUniformZero.lean` is unelaborated. Source inspection and mathematical derivation are not compilation evidence. The assigned rows below appear in reading order.

1. **`def-dummy`, `def-planted`.** Explicit expectation laws and their normalization/positivity wrappers are supplied. Existing `dummy` and `planted` are sample-point maps. These new wrappers need elaboration before any old partial ties can be upgraded. The arbitrary fixed blank pattern in the preprint is instantiated by all false.
2. **`claim-Y-values`.** The pair of values is assembled on the support of the product law. The generic theorem must be specialized to `P k t`, `ℓ=2t`, `r=40t` and the same correct circuit as `Fkm`. No unconditional claim about arbitrary ambient off-promise address arrays is made.
3. **`eq-18`.** The symmetric, unsplit event statement is newly supplied, with an explicit pointwise proof. The imported source statements alone did not have this type. It remains unelaborated. The absolute bars are the ledger’s packaging, not symbols printed in the preprint’s (18).
4. **`def-Z`.** An integer-valued count and its indicator-sum identity are supplied; their finite-set cast proof requires compilation. The exact `Pr(erased zero)=E Z/m` identity is also new source.
5. **`claim-uniform-zero`.** A complete finite-weight proof at the source level is supplied, including actual adaptive-prefix semantics and the positive-probability conditioning guard. It has not been elaborated. It is not a wrapper assuming the desired posterior law.
6. **`claim-EZ`.** The final bound `E Z≤4G/m` is supplied through the stronger source zero-search induction. The compound ledger row’s early/late discovery variables, `E Z_early≤2G/m`, late-count inequality and their partition/expectation combination are not formalized here. Keep the whole row partial, with alternative-route evidence for the endpoint. The task explicitly permits deriving the paper’s coefficient four from the source’s coefficient two. The sharper `2G/[m(m+1)]` result accepted for future work by adjudication is not used and is not claimed Lean-checked.
7. **`def-heavy`.** An exact named alias and its equivalence theorem are supplied. Counting repeats and using the full run are essential.
8. **`def-simulator`.** The exact concrete specialization and total cap are supplied. Query times are shifted from paper one-based times to zero-based list indices. Existing `simTree` already contains the algorithm.
9. **`eq-21`.** The exact per-time joint event is supplied and averaged under the original product law. The source previously kept this step inside the whole-run union-bound proof. It must not be converted into success conditioned on nonheaviness.
10. **`eq-22`.** The complete cell-visit event, heavy term and nonheavy union have now been assembled into one unelaborated declaration with the exact `(2/3)^r` probability.
11. **`eq-23`.** New declarations give the absolute deterministic bounds at coefficients two and four and the actual randomized-program bound at coefficient four. All are unelaborated. The original source’s one-sided `tree_gap_le` and existing contradiction were sufficient for the headline theorem; this return does not weaken a statement to obtain an exact tie.

## Imported evidence boundary

The packet reports the existing planted modules as built. The latest adjudication says the headline root-build receipt names a commit that predates some working-tree files. This return performs no clean-pin build or Comparator run and changes no receipt. Re-record the new modules at a clean source pin before assigning `built_at_pin`, and independently adjudicate every new tie.

## Static review boundary

Pinned Mathlib source was consulted for `Finset.card_filter`, `Finset.sum_subset`, `Finset.sum_eq_single` and the finite-sum arguments they support. A compiler is still required to resolve tactic behavior, reducibility, generated `to_additive` names, implicit universe/type parameters and every module import.

## Sections 4–5: tail, numerics, Omega bound, and quotient

All new declarations listed here are **unelaborated**. No new build, Comparator acceptance, or kernel check is claimed. The submitted source contains complete candidate proofs and no proof placeholders. Exact Mathlib declarations were checked in the pinned source at `69552756cd8a2d2d48763cf7279fd814d6a1224d`.

1. **`claim-tail`.** The previous source tie is weaker: `QuarticQuery.twoThirds_pow_le` supplies $(2/3)^{40t}\leq m^{-10}$, with neither $G$ nor a limit. New `classical_twoThirds_exact`, `classical_tail_le`, and `classical_tail_envelope_tendsto` supply the exact real exponent and its limit in candidate Lean. `classical_tail_parameters` specializes both the finite inequality and the zero limit to the actual floored budget. The geometric identity, sign calculation, and actual-budget square bound are separately registered as `r2-classical-tail-identity`, `r2-classical-tail-geometric`, `r2-classical-tail-negative`, and `r2-classical-budget-square`. Every new proof still needs elaboration. Preserve the original exponent and its existing weaker tie.

2. **`claim-numeric`.** The imported `discrepancy_le` exports only the aggregate bound; its proof contains the three component estimates locally. New `classical_numeric_components` copies those steps and exposes their conjunction, the sum bound, and $6/100<1/3$. It needs elaboration. The exact-exponent tail proof is unnecessary in this finite calculation, which deliberately uses the already-existing `twoThirds_pow_le`.

3. **`cor-R-omega`.** The candidate `Paper.cor_R_omega_log2` already has the correct full type but is marked uncompiled by the packet. New `classical_cor_R_omega_log2` reconstructs that short proof using only core imports, with no import of `Paper.Section4`; the natural-log conversion is `classical_cor_R_omega_log`. The explicit constant/all-circuit strengthening is `r2-classical-omega-explicit`. Both candidate wrappers need elaboration. The threshold depends on fixed $k$, even though the coefficient $1/400$ does not.

4. **`claim-exponent-ratio`.** The original source supplies eventual strict comparison and the choice of $k$, but not the exact finite quotient inequality. New `classical_ratio_arithmetic` exports that inequality, `classical_power_log_tendsto` proves divergence of the displayed envelope, and `classical_Fkm_ratio` instantiates the actual canonical circuit in both $R$ and $Q$. Their statements are registered as `r2-classical-ratio-arithmetic`, `r2-classical-power-log-limit`, and `r2-classical-ratio-explicit`. They need elaboration. The quotient limit in `classical_ratio_tendsto` also uses the existing `eventually_gt_rpow`, so no stronger uniformity in growing $k$ is claimed.

The finite mathematical derivations were reviewed against the source and the published display. The remaining formal boundary is compiler elaboration of these exact candidate declarations, followed by any desired declaration-specific comparison. The earlier reported builds of imported modules do not constitute build evidence for this new file.

