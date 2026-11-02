# Cold read of replacement §3.16

Read on 2 November 2026. Scope: §3.16 in `deliverables/quartic_r3_03_forrelation_lower_bound_return/section.md`, its named earlier equations, the target/promise statement and quantitative endpoint. Sources were reused from the completed primary-source audit; no new broad search or Lean execution was undertaken.

## Required corrections

1. **Wrong Fourier reference.** The sentence “As (F8) makes explicit, this does not discard the higher uniform Fourier levels” must reference **(F24)**. Equation (F8) is the derivative-character identity under a biased measure. Equation (F24) is the expansion over all uniform Fourier supersets and directly supports the sentence.

2. **General-k comparison cites a k=3 intermediate.** The sentence introducing (F58) currently cites **(F19)**. That equation is only the first Stein-elimination step of the three-block example and does not establish the general endpoint bound. Cite **(F11), (F22)–(F23), and (F57)** together with (F56), or the resulting general path-advantage inequality. The final coefficient `3/4^(k-1)` is correct.

3. **Add the SSW level range.** State **`1 <= r <= n`** in the quantifiers preceding (F56), matching the cited corollary. As printed, `r` is unquantified and the display is false at `r=0` for the constant-one tree whenever `n>1`. The desired application is `r=k` and `n=km`, so the correction changes no intended proof.

## Useful precision improvements

4. In the first credit paragraph, replace the list **(F16), (F19), (F38)** with **(F16), (F22), (F39)** if the intended list is uniform endpoint, general path calculation, and hard-distribution mean. The current list is not false but (F19) is restricted to `k=3`, while (F38) bounds the Gaussian path coefficient rather than stating the hard mean. Either explicitly describe the narrower listed identities or use the more representative equations.

5. The sentence attributing inverse-polynomial losses in `k` to amplification alone is imprecise. The elementary route loses one factor through its growth estimate and another through amplification. Suggested replacement: “The factor `k` from `binomial(d,k) <= (ed/k)^k` cancels the order-`k/eta^2` amplification cost. The elementary martingale estimate has an additional factor `k` inside its growth bound, leading instead to the `k^-2` endpoint.”

6. Add an explicit bibliography citation to the Tal context sentence: `Tal2019v1`, §5.1 Theorem 5.1 and §5.2 Definition 5.5. The scope description is correct: the random-orthogonal distribution theorem is not automatically a theorem for Walsh.

7. Heading hierarchy: `## 3.16` should have the same heading level as §§3.6–3.15 (currently `###`); its two internal subheadings should then be one level lower. This is editorial, not a mathematical issue.

## Checks that passed

- (F9) is the stated algebraic truncation, distinct from the Gaussian-cdf truncation in Bansal–Sinha. (F16) is the uniform endpoint; (F22) is the full derivative cascade; (F38) is its coefficient mean lower bound; (F39) is the hard mean.
- Bansal–Sinha physical `main.tex:1180–1181`, threshold at1184, reciprocal display at1173, version v3 and printed p38 are correctly identified. The archive SHA-256 matches the previously checked source.
- (F52)–(F54) have the correct logarithmic exponents. The fixed-k counterexample is to the displayed comparison of bounds; the prose correctly does not claim to refute the theorem. The sufficient corrected denominator exponent `1-1/[k(k-1)]` and geometric-sum argument are sound. The subsequent fixed-k comparison with a squared logarithm is valid after the original amplification cost and sufficiently large dimension.
- (F55) correctly uses the exceptional mass `4/(N delta^2)`. `N>=4/delta^3` gives the displayed gap at least`3delta`.
- SSW v4 PDF Corollaries4.14–4.15, printed pp35–36, and corresponding HTML4.12–4.13 are correctly distinguished. `C` remains an unspecified absolute constant and an external input; the elementary endpoint is independent of it.
- (F57) includes validity conditions for the random restriction, also permitting zero free probability without division. The path product `(1/4)(3/4)^(k-2)` and coefficient identity are correct.
- The variable-error amplification estimate `(1-eta^2)^tau` is correct with ties counted as errors; the `eta=1` endpoint is explicitly handled. The ceiling choice obeys `tau<4k/eta^2` for `k>=2` and `eta<=1`.
- The conservative gap `Gamma>=a_k-4delta>=7a_k/8` suffices. It yields the factor `4/81*(21/16)^(2/k)` in (F59), hence the stated `eta^2/(162eC^2)` coefficient in (F60). The power-of-two extension is clearly ordinary mathematics and not a claim about a newly elaborated Lean type.
- Credit distinguishes Kewen Wu from Pei Wu. The bounded novelty/search statement and the absence of author-approved correction are appropriately restrained.

Formal receipt membership in the final paragraph is outside this cold read: it should be checked against the source-current evidence audit already assigned to the Lean reviewer. No statement here independently certifies those receipts.
