# Lean coverage, premises, and remaining boundaries

## Reading this ledger

The current source supplies the restricted fixed-parameter and sharp uniform endpoints used in the replacement section. No missing analytic hypothesis was identified in their assessed proof chain. The remaining boundaries concern exact theorem interfaces, ordinary reformulations and stronger extensions, and the scope of the supplied execution evidence.

Source locations below are relative to the packet's `repository/lean/QuarticQuery/`; a filename under `ForrelationLower/` refers to that directory. Full verbatim interfaces, namespace and ambient-variable context, source bindings, and exact membership flags are in [declaration_interfaces.json](evidence/declaration_interfaces.json). The receipt, native-input, and audit-source/log checks are in [evidence_verification.json](evidence/evidence_verification.json). [source_read_receipt.json](evidence/source_read_receipt.json) identifies the assessed source and document scopes.

**Type evidence has two levels.** When the supplied post-root audit contains a matching `#check`, the interface file reproduces that elaborated output. Otherwise it quotes the exact source header together with ambient variables, notation, and any `include` context. It does not claim to reconstruct Lean's complete minimized implicit-binder list. Unused section variables are not automatically theorem hypotheses. Conversely, an included hypothesis must not be omitted merely because it is absent from the printed source header; `sum_dw_eq` is an example.

**Paper premises are not unproved imports.** Conditions such as orthogonality, bounded bias, positive depth, and integrability are genuine premises of intermediate lemmas. The endpoint proof constructs or proves them. An external Fourier-growth theorem used only in §3.16 is a different kind of premise: it remains an external input to that comparison and is not consumed by the local endpoint.

## §3.6 — Frozen problem and endpoint

`Statement.lean:74` defines `RLe` using a finite randomized program, a worst-case depth bound, and success at least `2/3` on every promised input. `R` at line 84 is a natural minimum. The relevant minimum/attainment facts are supplied by `Model/Classical.lean`; the section's all-input query-cap convention matches this model.

The frozen family has `mValue t = 2^(2*t)` (`Statement.lean:159`), the real normalized statistic `Phi` (line 183), and the integer-defined partial promise `P` (line 188). Its yes condition is positive Forrelation; a sufficiently negative value is not a yes input. `Lvalue` (line 309) uses a natural floor and binary logarithm. `BansalSinhaLower` (line 319) is the proposition

```lean
∀ k : ℕ, 2 ≤ k → ∃ t₀ : ℕ, ∀ t : ℕ, t₀ ≤ t → Lvalue k t < R (P k t)
```

`ForrelationLower/Main.lean:525` proves `bansalSinhaLower : BansalSinhaLower` with no ordinary hypotheses. Its name does not mean that the published Bansal–Sinha theorem is assumed. The paper's discussion of the published theorem is a separate literature implication. The exact fixed-k declaration is explicitly listed in both current ordinary and paranoid Unconditional Comparator receipts.

## §3.7 — Finite extension and derivatives

The source definitions are `ext` and `D` (`Cube.lean:54,57`). `sum_bw` (65), `abs_ext_le` (90), `hasDerivAt_ext` (221), `D_D` (247), and `ext_D_eq_mul_xi` (273) support the finite biased-extension argument.

The relevant premises differ by use. The finite polynomial identity needs no bias bound. Interpreting its coefficients as probabilities needs `|μ_i| ≤ 1`. Dividing by `1−μ_i²` in the derivative character needs `|μ_i| < 1`. Later applications have `|μ_i| ≤ 1/2`, which supplies both conditions. The distinct-coordinate derivative identity is `TreeGrowth.lean:690` (`ext_Dl`); `abs_xi_le` and `xi_mean` are at lines 718 and 729.

The set-derivative notation and the explanatory polynomial examples are ordinary reformulations. No separately named source declaration is claimed for every displayed algebraic identity.

## §3.8 — Gaussian identities and truncation

`Stein.lean:22–28` defines `qf`, `psiS`, `phiS`, and `dphi`. The derivative and half-bound are at lines 76 and 98. The current source proves both `psi_dphi_le_sharp` (137) and `psi_dphi_eq_sharp_at_zero` (156): the coefficient `3/16` is already formalized, including attainment at zero.

`stein_one` (167) explicitly requires continuous bounded functions `g,g'` and the pointwise derivative law. `stein_pi` (298) carries the corresponding bounded continuous coordinate-derivative premises. The constructed integrands satisfy these through finite polynomial structure and the source's bounded-continuous-function lemmas. These premises are not left as analytic oracles.

`integral_reflect` (336) requires a unit vector and measurable integrand. `integrable_dot_sq` and `integral_dot_sq` (382,401) supply the Gaussian second-moment facts. The paper's density/Jacobian explanation is an ordinary proof presentation of reflection invariance; it does not treat the correlated pair `(U,HU)` as an independent product Gaussian.

## §3.9 — Bias chain and uniform endpoint

The chain is defined by `Uc`, `Vc`, `Xf`, `Yf`, `Sf`, and `wv` (`Walk.lean:33–51`). The source's packaged bound `abs_wv_le_half` (152) requires a positive chain length and `|s|≤1`. The stronger interior-coordinate bound `1/4` in the prose follows directly from multiplying two half-bounded factors; no separately compiled wrapper for that sharper coordinate bound is claimed.

The null endpoint is `integral_ext_wv_zero` (`Cascade.lean:256`). Its ordinary matrix premise is `RowsOrth H`, defined at line 25 and used in the reflection-clearing lemma `integral_mw_insert` (192). For the concrete normalized Walsh matrix, `rowsOrth_H` (`Promise.lean:129`) discharges it. The argument identifies expectations for every test function, hence the entire finite distribution. It does not replace dependent chain coordinates by independent ones.

## §3.10 — One-path Stein elimination

`sum_dw_eq` (`Walk.lean:272`) has an included `j<l` premise through `include hj in` at line 270. Its vanishing same-block term is supplied by the repeated-derivative identity. `EarlyOnly` (317) and `integral_walk` (364) encode the fact that accumulated weights depend only on earlier Gaussian layers. The induction proves the required boundedness and update invariance.

The exact endpoint identity `exists_identity` (461) supplies **one common** `s∈(0,1)` for the whole sum. `Int_eq_paths` (541) expands the nested walk. The source does not supply a literal integrated-in-`s` theorem under that name.

The section's finite-polynomial argument for differentiating the Gaussian average, its three-block calculation, and its every-`s` path formula are ordinary explanations/combinations of these ingredients. Their regularity is justified in the section, but no new compiled wrapper for these formulations is claimed. The mean-value parameter may depend on the test function; it is shared by all paths.

## §3.11 — Stopped-process growth

The source implements exposure by finite tree recursion, including repeated queries. The relevant declarations are `walk_eq_ext` and `walk_chaos` (`TreeGrowth.lean:121,215`), `two_point_exp_le` (376), `hit_azuma` (414), `hit_chaos_le` (514), and `abs_ext_tree_chaos_le` (658). The abstract step law, centered bounded increments, positive depth and threshold, and the exact quadratic threshold equation are explicit intermediate premises. The section discharges them; it does not condition on a future good event.

The final source interface `sum_abs_ext_Dl_le` (738) requires derivative lists with no repetitions, common length, and an injective map to coordinate sets; half-bias; positive `d,K`; `K²=8dΛ`; nonempty coordinate space; and a bounded tree output. All these premises matter. The paper explicitly chooses the positive square root for `K`.

**Numerical specialization.** The source retains the parameterized bound

\[
K^r+(2n)^r(4n)^r e^{-\Lambda}.
\]

The paper sets `Λ=2r ln(4n)` and `K=sqrt(16rd ln(4n))`. Since `n,r,d≥1`, these parameters are positive, and the residual is exactly `2^(-r)`. The compact display (F25) is this ordinary numerical specialization, not a separately named source theorem.

**Leaf-value scope.** The literal Lean interface takes `T : QueryTree I` and `v : Bool → ℝ`, with `|v b|≤1`, and applies to `g=v∘T.eval`. The section proves the broader statement for arbitrary bounded real labels at individual leaves. That generalization is ordinary mathematics; the local two-value interface already suffices for acceptance probabilities. It is not accurate to present the source type as an unrestricted real-leaf tree type.

## §3.12 — Advantage estimate

`Lpath_nodup` and `Lpath_inj` (`Cascade.lean:354,362`) discharge the derivative-list conditions without a path-multiplicity factor. `abs_cf_le_sharp` (`Walk.lean:574`) needs only a nonnegative entry bound and does not require orthogonality. Orthogonality is needed elsewhere, for the null endpoint.

`advantage_le_sharp` (`Cascade.lean:384`) combines these ingredients, with explicit positive-depth/threshold, half-bias, bounded-output, and matrix premises. Equation (F33) uses the same parameter substitution as §3.11, `r=k`, and the Walsh entry magnitude `1/sqrt(m)`. Its `2^(-k)` residual is an ordinary simplification of the parameterized source expression.

The old `advantage_le` (426) is now a weaker corollary of the sharp theorem. Accordingly, the fixed-k proof closure reaches the sharp scalar helper even though it does not consume the newer uniform endpoint. Root-imported, individually audited, and headline-consumed are different statuses.

## §3.13 — Hard and uniform moments

`Phi_eq_PhiF` (`Promise.lean:482`) connects the internal nested expression to the frozen statistic. `qf_le_exp` and `psi_dphi_ge` (254,271) give the tangent-exponential bound. `integral_Uc_sq` and `integral_Vc_sq` (401,413) justify the marginal moments without assuming independence of correlated selected coordinates.

The live hard-mean proof is organized through `Int_Rs`, `Yy_ge`, and `integral_TT` (228,343,456). The paper expands that calculation into paths and constant path derivatives. This is an ordinary explanatory reformulation, not an exact separately named all-path derivative theorem.

`mass_ge` (499) literally bounds the hard expectation **minus** the uniform expectation. Combining it with `ext_PhiF_zero` (559) yields the hard mean stated in (F39). `ext_PhiF_sq` (564) supplies the uniform second moment `1/m`. The moment statement is for the concrete Walsh family; an arbitrary-orthogonal hard-moment theorem is not being inferred.

## §3.14 — Amplification and the promise gap

`exists_amplified` (`Amplify.lean:80`) starts from the frozen `RLe` model, uses exactly `2τ` independent runs, and gives depth `2τL` and error `(8/9)^τ` on promised inputs. A variable initial error is not a parameter of this theorem.

`P_yes` and `P_no` (`Main.lean:34,49`) connect the internal statistic to the exact promise. `not_RLe_of_gap_sharp` (81) requires the quantitative advantage bound and the explicit strict expectation gap; it does not assume those inequalities for free. The later arithmetic proves them. Its padded depth is `2τL+1`, ensuring positivity at `L=0`.

The all-input acceptance inequalities use only promise correctness and `0≤A≤1`. No support-on-promise assumption is required for either distribution. The uniform exceptional contribution remains `4/(mδ²)`. The coarse gap theorem (222) is preserved as a corollary.

## §3.15 — Uniform endpoint and new ordinary threshold

The exact current sharp theorem is `QuarticQuery.forrelation_lower_uniform_sharp` (`Uniform.lean:527`). Its only ordinary hypotheses are natural `k,t`, `2≤k`, and `15k+2≤2t`. It proves

\[
\frac{2}{18225}\frac{m^{1-1/k}}{k^2\ln(4km)}<R(P_{k,m}),\qquad m=4^t,
\]

at error `1/3` and the frozen promise threshold. It has no SSW hypothesis or error/advantage parameter. `main_term_le_sharp` and `not_RLe_uniform_sharp` are at lines 270 and 405. The older coefficient `1/2332800` remains in `forrelation_lower_uniform_existing_constants` (508).

The section's `t≥13669k²` threshold, including the comparison using `ln(4km)≤6t`, is an **ordinary deduction** from the sharp theorem. No compiled declaration with that new threshold is claimed. The source contains `log_four_k_m_le` (539) and a different named theorem `lvalue_lt_R_explicit` (644), whose sufficient threshold is `3499200k²` and whose proof uses the older constant. The historical four-term threshold remains in `Main.lean:366` (`exists_threshold`) and the original fixed-k proof. These statements must not be conflated.

## §3.16 — External comparison and execution boundary

The SSW Fourier theorem is an explicit external premise for (F56)–(F60). The random-restriction transfer, variable-error amplification, and resulting bound with `η²/(162eC²)` are ordinary mathematics in this section. Neither local endpoint has that type. Extending the mathematical Walsh construction to every power-of-two dimension does not extend the frozen Lean family `mValue t=4^t`. The published-display audit likewise does not create a Lean theorem or refute the published lower-bound statement.

The supplied evidence distinguishes the two actual local endpoints:

| Endpoint | Current root/native evidence | Exact Comparator membership | Supplied individual type/axiom audit |
| --- | --- | --- | --- |
| `ForrelationLower.bansalSinhaLower` | Present | Yes, ordinary and paranoid Unconditional receipts | Not in the separate 258-name new-declaration audit; Comparator is its relevant acceptance evidence |
| `forrelation_lower_uniform_sharp` | Root-listed; accepted focused Uniform retry 3 | No | Yes; elaborated type and `[propext, Classical.choice, Quot.sound]` printed |

The root receipt is `repository/corpus/receipts/lean-build-root-2026-11-02T182539383153+0000.json`; it lists the fixed-k name at line 1005 and the sharp uniform name at 2587. The current Unconditional receipts end in `183450037875+0000.json` and `184546477430+0000.json`. Uniform's accepted target record is in `native_results/native-retry-3/results.json`. The successful reviewed verdict is `native_results/final-evidence/reviewed_axiom_audit_verdict.json`; the supplied log prints the sharp type at lines 2303–2308 and axioms at 2309. The similarly named preparation metadata alone is not an execution verdict.

All 124 recorded local source/configuration hashes for the relevant root, Comparator, audit, and export records matched the packet bytes; all 16 Uniform retry-3 inputs also matched. Older “proposed,” “aggregate pending,” or failed-build prose is superseded where these later exact records apply. Sharp Comparator membership is still absent. **No fresh Lean/Lake run was performed.** This return audits supplied source and source-bound execution records; it does not claim a new kernel replay or an independent inspection of the complete compiled dependency installation.
