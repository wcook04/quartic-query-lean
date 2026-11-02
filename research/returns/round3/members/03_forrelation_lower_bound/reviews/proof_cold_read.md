# Cold reading of the completed replacement section

Read the complete 875-line replacement `section.md` end to end, including all 60 numbered displays, the stopped-martingale argument, literature comparison, padded sharp assembly, and new explicit threshold. This reading was performed while the root was making final small corrections; the dispositions below describe the latest text observed and the outstanding suggestions sent to the root.

## Mathematical verdict

No substantive mathematical error found. The section supplies an ordinary proof of the exact promise lower bound without importing a randomized Forrelation lower bound or SSW into its core argument. All probability distributions in the main proof remain consistent. The use of the independent underlying U coordinates avoids any problem from the singular joint law of (U,HU).

The three-block display correctly includes both repeated-derivative cancellations. The finite-polynomial explanation justifies the interpolation differentiation. The reflected zero endpoint is valid for arbitrary g, identifying the entire uniform distribution. The stopped-martingale induction correctly bounds all contracted coefficient arrays on the original adaptive tree; it does not condition on a future good event. Leaf conditioning and repeated queries are handled correctly.

The padded uniform proof is correct:

- D≥1 gives d=50kD+1≤50kD(1+1/(50k)).
- The assumed bound on D makes the main term at most a_k/3 by the factor 9/8 from the binomial estimate.
- The residual is at most a_k/4 under the supplied dimension threshold.
- Their sum 7a_k/12 is strictly less than 119a_k/144; the margin is 35a_k/144>0.
- The D=0 case is explicitly excluded by the positive distributional gap.

The new threshold t≥13669k² transports every premise and preserves strictness. The exact argument uses c/6=1/54675 and 4·13669=54676>54675. The smaller ceiling threshold is correctly identified as also sufficient because the numerical query bound is already strict.

The SSW comparison's revised coarse gap is valid. From ε≤δ and exceptional mass≤δ, the all-input inequality gives Γ≥a_k−4δ≥7a_k/8. Consequently

\[
(\Gamma4^{k-1}/3)^{2/k}\ge(4/81)(21/16)^{2/k}\ge4/81.
\]

Also τ=ceil(5k ln2/η²)<4k/η² follows from k≥2, η≤1 and 5 ln2+1/2<4. Combining these with the binomial estimate gives exactly η²/(162eC²), so there is no missing factor of 2 or k. The external Fourier input is clearly separated from the elementary proof.

The corrected Bansal–Sinha sum estimate checks algebraically: with h=k(k−1) and d₁ proportional to N^(1−1/k)/L^(1−1/h), the exponent remaining in its rth term is (r/h−1)/2≤0. The geometric sum with Ac≤128^(−2) is bounded by 128^(1−k)/127<32^(−k)/4 for every k≥2. The independent literature audit owns the version and locator verification; this cold reading checks the displayed mathematical comparison.

## Concrete corrections sent to root

1. **Required wording at the stopping step.** Change “one of the ... expressions exceeds K^(r−1)” to “one of the ... expressions has absolute value greater than K^(r−1).” Negative large coefficients also invalidate the increment bound. The surrounding formulas already use absolute values, so this is a local prose correction.
2. **Minor ambiguity in bounded functions.** After the sharp product estimate, “the individual functions and their derivatives are bounded” could be read to include q(x)=sqrt(2+x²), which is unbounded. Say “Both Ψ and φ, and the derivatives used below, are bounded.”
3. **Optional immediate k=2 qualification.** The first paragraph after F17 mentions an X₁ factor before explaining the k=2 endpoint case. Its absence for k=2 is explained correctly in the general-path paragraph, but can be acknowledged immediately for first-time readers.

Other issues noticed during the first reading had already been corrected by the time of the final check: B,R>0 in the maximal inequality; K chosen as the positive square root; the higher-degree discussion referring to F24; SSW using the general F22–F23 identity rather than the three-block F19; and the positive-degree/positive-dimension range of F56.

## Text and reference checks

- All 60 numbered display tags are distinct.
- Every parenthesized F-reference resolves to a present tag.
- The correct mean-vector symbol is Latin u; there is no accidental Greek nu in F1.
- TeX control sequences have the intended single backslash. No unexpected control characters or literal tab characters were found.
- There are 76 opening and 76 closing display delimiters, three matched aligned environments, and two matched cases environments. Inline dollar counts have even parity.
- No PDF/HTML rendering, fresh Lean execution, or Comparator run was performed in this cold read. The companion bibliography and historical-threshold file were still being prepared when looked for; their final checks belong to the root's packaging step.

The few suggested edits do not change the conclusion. A final targeted reread confirmed that the root applied both the absolute-value stopping correction and the bounded-functions clarification. No required mathematical correction remains from this cold read. The section is mathematically ready for the stated advisory return, with the source and formal-evidence boundaries retained.
