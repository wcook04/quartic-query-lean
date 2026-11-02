# Forrelation lower bound: current-source and execution-evidence audit

## Finding that changes the proposed section

The current packet already contains a complete restricted sharp uniform theorem. It is no longer accurate to describe the scalar constant `3/16`, its propagated path bound, or `QuarticQuery.forrelation_lower_uniform_sharp` as proposals awaiting formalization. The theorem is present at `ForrelationLower/Uniform.lean:527`, its owning module has an accepted source-current native build, it is explicitly named in the current root-build receipt, and a supplied successful post-root audit prints its elaborated type and its three standard axioms. This audit independently recomputed all relevant local file hashes; they match the accepted records.

The theorem retains the frozen scope: natural `k ≥ 2`, `m = mValue t = 2^(2t) = 4^t`, `15k + 2 ≤ 2t`, threshold `δ = 2^(-5k)`, and randomized error at most `1/3`. It states

\[
\frac{2}{18225}\frac{m^{1-1/k}}{k^2\ln(4km)}<R(P_{k,m}).
\]

It has no advantage/error parameter `η` and no SSW premise. The improvement over the older constant `1/2332800` is exactly a factor of `256`. Scalar sharpness at zero does not establish that the final complexity constant is optimal.

The sharp uniform theorem does **not** have exact Comparator membership in this packet. The original endpoint `QuarticQuery.ForrelationLower.bansalSinhaLower : QuarticQuery.BansalSinhaLower` does, in both a current ordinary and a current paranoid Unconditional receipt. These are different evidence scopes and must remain separate.

No Lean or Lake executable was available on the review environment's PATH, and this review did not run or install Lean. All execution claims below concern supplied records whose local input hashes were checked against the supplied source. The root build's raw stdout and compiled artifacts were not independently inspected.

## Exact endpoint interfaces

The frozen definition, `Statement.lean:319`, is:

```lean
def BansalSinhaLower : Prop :=
  ∀ k : ℕ, 2 ≤ k → ∃ t₀ : ℕ, ∀ t : ℕ, t₀ ≤ t → Lvalue k t < R (P k t)
```

`Lvalue` is a natural floor of `m^(1−1/k)/(logb 2 m)^2`, and `logb_mValue` proves `logb 2 (mValue t) = 2t`. The source theorem in `Main.lean:525` has no ordinary premises:

```lean
theorem bansalSinhaLower : BansalSinhaLower
```

In particular, its theorem name does not hide an assumption of the published Bansal–Sinha result. The local source supplies its analytic proof. `RLe` is the frozen finite-mixture query model with maximum tree depth bounded by the budget and success at least `2/3` on every promised input. `R` is a natural minimum; the attainment/existence lemmas used in the proof come from `Model/Classical.lean`. The promise uses a positive yes threshold and an absolute small no threshold, leaving the middle and sufficiently negative inputs undefined. It is not an absolute-value yes promise.

The sharp theorem's verbatim source signature is:

```lean
theorem forrelation_lower_uniform_sharp
    (k t : ℕ) (hk : 2 ≤ k) (ht : 15 * k + 2 ≤ 2 * t) :
    (2 / 18225 : ℝ) *
        Real.rpow (mValue t : ℝ) (1 - 1 / (k : ℝ)) /
        ((k : ℝ) ^ 2 * Real.log (4 * (k : ℝ) * (mValue t : ℝ))) <
      (R (P k t) : ℝ)
```

The supplied audit log prints the corresponding elaborated type at lines 2303–2308 and its axiom list at line 2309. The list is exactly `[propext, Classical.choice, Quot.sound]`. The exact output is copied into `declaration_interfaces.json`; it is not reconstructed from informal notation. The audit source has the matching `#check` at line 768, `#print axioms` at 769, and includes the name in its runtime assertion list at 1037.

The same JSON contains 143 relevant declaration interfaces, exact source file hashes and locations, ambient variables/notation, available elaborated output, exact membership flags, and projected dependencies from the supplied export. For ordinary helper lemmas without supplied `#check` output, a source header plus ambient context is deliberately not claimed to be the compiler-minimized implicit binder list. For example, `sum_dw_eq` has a real `j < l` premise through its preceding `include hj in`; unused ambient section variables are not silently promoted to actual hypotheses.

## Evidence that is current

| Item | Exact record | Scope independently confirmed |
| --- | --- | --- |
| Root build | `lean-build-root-2026-11-02T182539383153+0000.json` | Passed; all 124 local source/config hashes match; 2,652 exact declared names. Both endpoints are listed. |
| Ordinary Comparator | `comparator-Unconditional-2026-11-02T183450037875+0000.json` | Passed; all 124 hashes match; fixed-k endpoint explicitly listed. |
| Paranoid Comparator | `comparator-Unconditional-2026-11-02T184546477430+0000.json` | Passed, exit zero, paranoid true, source unchanged; all 124 hashes match; same eight exact names. |
| Focused Uniform native build | `native_results/native-retry-3/results.json`, target `QuarticQuery.ForrelationLower.Uniform` | Passed, exit zero, inputs unchanged; all 16 recorded input hashes match; supplied log ends `Build completed successfully (18202 jobs).` |
| Reviewed type/axiom audit | `reviewed_axiom_audit_verdict.json` and supplied source/log | Passed, exit zero, all recorded integrity checks true, all 124 source hashes match; exact marker `R2_AXIOM_AUDIT_OK declarations=258`. |
| Dependency export | `repository/corpus/lean_dependencies.json` | Source-current 124-file binding; 2,652 declared names, 1,354 names reached from the two headline roots. |

The root command is `lake build QuarticQuery`. The inspection command invokes `scripts/Reach.lean` on `QuarticQuery.theorem_1_1_unconditional` and `QuarticQuery.cubic_bound_fails_unconditional`. The receipt toolchain is `leanprover/lean4:v4.36.0-rc2`, source pin `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`. The packet manifest has a later repository commit, but exact byte matches establish currentness for the recorded inputs; the difference in commit names alone is not evidence of stale source.

The root receipt lists `bansalSinhaLower` at line 1005; the coarse uniform theorem at 2586; the sharp uniform theorem at 2587; the sharp scalar inequality at 1200; its equality-at-zero result at 1198; and `lvalue_lt_R_explicit` at 2643. These are exact-name membership checks, not a string-based inference from an imported module's name.

The sharp uniform theorem, coarse uniform theorem, and `uniform_budget_floor_bounds` are individually listed in the 258-name axiom audit. `bansalSinhaLower` is not in that particular new-name audit; its separate Comparator receipt is the relevant acceptance evidence. The two sharp scalar declarations print the same three standard axioms at log lines 2312 and 2315.

Important independently verified hashes are:

| Supplied object | SHA-256 |
| --- | --- |
| Root receipt | `bc11e3fec8581f89ce56b110bf76db2469abea4b7be00fa476f9d2cee9455c2e` |
| Audit Lean source | `78da4e0b0d875eedd3898a46f4e885a8fa7e89c2d5fbf2d3205012ff4f640513` |
| Audit log | `f87b4e78aaa99fb069acc358fd90c6b95a1fd09bb337d4b49b6851ae714d8ae1` |
| Current `Uniform.lean` | `d6bc1f4399394810fca63abdaadd67a420616371c501ab978841898f2bda049c` |
| Current `Stein.lean` | `6238d7e6f8ade6044eb623899069f35d0a5b860699c722e7007fd71046ffff9e` |

`reviewed_axiom_audit.json` describes an **unexecuted preparation** and is insufficient by itself. The successful verdict and matching execution log are the actual acceptance evidence. Similarly, the older native inventory marked Uniform blocked, and retry 1 and retry 2 failed on different Uniform hashes. They are historical records; retry 3 matches the accepted source. The round-two prose adjudication's statement that aggregate validation and recomputed reach remain pending is superseded by the later final records. Its statement that new-endpoint Comparator acceptance is absent remains accurate.

## Proof-route audit and real hypothesis boundaries

### Gaussian analysis and one-path elimination

`Cube.lean` supplies finite biased product weights, their normalization, multilinear extension, the finite chain rule, the derivative-character identity, coordinate affinity, and the vanishing repeated derivative `D_D`. The probabilistic use of product weights needs biases in `[-1,1]`; division by `1−μ_i²` needs strict interior bias. `abs_wv_le_half` proves the stronger half-bias condition needed by the growth argument when the chain has positive length and `|s|≤1`.

`Stein.lean` defines `q(x)=sqrt(2+x²)`, `Ψ(x)=1/(2q(x))`, `φ(x)=x(3+x²)/(2q(x)^3)`, and `φ'(x)=3/q(x)^5`. It proves the derivative, boundedness and oddness facts and both the sharp upper product bound and equality at zero. Its one-variable and product-Gaussian Stein lemmas explicitly require continuous bounded functions/derivatives and the appropriate derivative law. Those premises are proved for the constructed finite polynomial integrands; they are not axioms or unresolved assumptions.

`Walk.lean` proves the Stein elimination with an `EarlyOnly` condition on previously accumulated weights. That condition says that changing a current or later Gaussian coordinate cannot change the earlier weight. The inductive construction establishes it. A potentially unwanted same-block derivative vanishes because differentiating a multilinear polynomial twice in one coordinate gives zero. The remaining derivative moves to the next block, so the proof does not generate the higher derivative levels of the Bansal–Sinha interpolation.

The exact source endpoint `exists_identity` is a mean-value statement: for each finite-cube test function there exists a single common `s∈(0,1)` at which the full summed path derivative equals the endpoint difference. It does not state a literal integral in `s`. A paper may explain an integrated identity with its own regularity argument, but its formal-source claim should quote the mean-value version. Neither this identity nor `abs_cf_le_sharp` requires matrix orthogonality. Orthogonality enters the null-endpoint proof.

### Null endpoint and decision-tree growth

`Cascade.lean` successively clears coordinates using reflection invariance of the finite product Gaussian and `RowsOrth H`. `rowsOrth_H` in `Promise.lean` discharges that assumption for the normalized Walsh matrix. The proof genuinely handles the dependence between neighboring blocks. It does not assert that all chain coordinates are independent.

`TreeGrowth.lean` implements finite exposure trees with a set of already revealed coordinates. Repeated queries select the known branch, avoiding duplicate independent samples. `two_point_exp_le`, `hit_azuma`, and `hit_chaos_le` prove a stopped hitting-probability estimate. The argument does not condition on a future event that would destroy the centered-increment law. Its nontrivial premises include a positive depth proxy, positive threshold, centered bounded increments, bounded coefficients, and the exact quadratic threshold equation. At application, the depth proxy is `2τL+1`, so zero-query candidates cause no division-by-zero problem.

`sum_abs_ext_Dl_le` also requires each derivative list to have distinct coordinates, every list to have length `k`, and the map to its coordinate set to be injective. `Lpath_nodup` and `Lpath_inj` supply those facts. This is what permits the sign choice defining the chaos coefficients to remain bounded by one, with no unaccounted path-multiplicity factor.

The sharp advantage theorem combines these ingredients. The old coarse `advantage_le` is now a corollary of `advantage_le_sharp`; likewise the old gap theorem is a corollary of its sharp version. Thus the original fixed-k headline proof actually reaches the sharp scalar helper, even though it does not use the new uniform endpoint. The dependency export confirms that among the 258 newly reviewed declarations only `psi_dphi_le_sharp` belongs to the two recorded headline closures. Imported/root-built and headline-consumed remain distinct statuses.

### Moments, amplification, and threshold closure

The hard first-moment proof in `Promise.lean` is organized as nested sums (`Int_Rs`, `Yy_ge`, `integral_TT`). Its path-expanded description is a valid explanatory reformulation, but the all-path constant-derivative display is not a separately named source theorem. `mass_ge` literally bounds the hard mean **minus the uniform mean**; one must combine it with `ext_PhiF_zero` before asserting the hard mean alone is at least `18^(-(k−1))`. `ext_PhiF_sq` gives the exact uniform second moment `1/m`. `Phi_eq_PhiF` ties these nested expressions to the frozen promise statistic.

Amplification uses exactly `2τ` runs, not `τ`, and yields maximum depth `2τL` and promise error `(8/9)^τ`. `not_RLe_of_gap_sharp` uses pointwise inequalities valid on the entire cube to compare expectations. Neither the hard distribution nor the uniform distribution is assumed to be supported on the promise. The exact gap retains the uniform exceptional contribution `4/(δ²m)`.

`exists_threshold` supplies the analytic estimates for all sufficiently large `t`, not just a selected subsequence. `bansalSinhaLower` closes the frozen fixed-k statement through the minimum-budget model. Current source also contains `QuarticQuery.lvalue_lt_R_explicit`, proving the same fixed-k inequality for the explicit sufficient bound `t≥3499200 k²`; it is root-built but not individually listed in the reviewed-name audit or in Comparator. The existing section can retain its original threshold derivation while recognizing this newer stronger packaging.

## Ranked remaining gaps and recommended wording

1. **Do not promote the arbitrary-error/SSW theorem.** The current sharp theorem fixes initial error `1/3`; it does not implement the proposed SSW restriction transfer, arbitrary `η`, constant `1/(162eC²)`, or a new subgaussian null-tail assembly. Those are external or ordinary mathematical extensions with explicit remaining formal obligations.
2. **Do not call the sharp theorem Comparator-checked.** Its current root/native/axiom evidence is strong and exact, but only the fixed-k endpoint has exact Comparator membership here. The configured Unconditional comparison checks four wrappers and lists eight wrapper/underlying names. No uniform sharp name occurs.
3. **Keep the dimension and family scope.** The live uniform endpoint has `m=4^t` and `15k+2≤2t`. An arbitrary-power-of-two version or a smaller improved-tail cutoff is a separate extension.
4. **Match the identity and moment packaging.** Use a common mean-value parameter for exact-source correspondence; identify the nested moment proof when presenting expanded paths.
5. **State the verification mode accurately.** This was a source/evidence audit with byte matching, not a new Lean replay. No mathematical gap in the existing fixed-k proof was identified in the assessed source. None of the boundaries above requires assuming its hard analytic step.

The machine-readable companions are `declaration_interfaces.json`, `evidence_verification.json`, `route_boundaries.json`, and `source_read_receipt.json`. The latter records full reads of all nine lower-bound modules and `Statement.lean`, scoped baseline/document reads, and subjects left to the separate literature and mathematical adversarial reviews.
