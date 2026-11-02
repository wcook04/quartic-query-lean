# Cold read of the replacement section

**Scope assessed:** all 875 lines of `deliverables/quartic_r3_03_forrelation_lower_bound_return/section.md`, with the formal interfaces checked against the already audited current source. No section edits, no new Lean run, and no repeated hash audit were performed.

## Verdict

The endpoint/evidence distinctions in the final two paragraphs are accurate. The section correctly separates the exact fixed-k Comparator endpoint, the current sharp uniform theorem with root/native/type-and-axiom evidence, absence of sharp Comparator membership, ordinary variable-error/SSW extensions, and absence of a fresh Lean run. The new threshold `t >= 13669 k^2` is explicitly an ordinary deduction; its comparison with the exact sharp theorem is correct. No hidden analytic assumption invalidating the main proof was found.

Three concrete corrections and two scope/notation clarifications should be made.

## Corrections

1. **State the positive thresholds in the maximal inequality.** At line 414 and the paragraph leading to (F30), add `B > 0`, `R > 0`, and an integer horizon `d >= 1`. The chosen parameter `lambda = R/(B^2 d)` divides by `B^2 d` and uses `lambda > 0` in the crossing argument. As an unrestricted statement in `R`, (F30) is false: a sufficiently negative threshold makes the event certain while the displayed exponential can be arbitrarily small. All later applications have positive `B` and `R`, so this is a local statement repair.

   Suggested start: “Let `d >= 1` be an integer, and let `B,R > 0`. For a martingale …”.

2. **Choose the positive root explicitly.** At line 431 replace “Fix `Lambda > 0` and put `K^2 = 8d Lambda`” by “Fix `Lambda > 0` and put `K = sqrt(8d Lambda) > 0`.” The positive sign is needed for the stopping thresholds `K^r` and increment bound `2K^(r-1)`. The exact source theorem has `(hK : 0 < K)`, not just the square equation. This also discharges the positive parameters in correction 1.

3. **Repair the general-k cross-reference.** At line 829, the derivation of (F58) cites (F19), which is the intermediate three-block formula and still has an unremoved Gaussian factor. Replace `(F19)` with `(F22)–(F23)`, the general path formula and common mean-value parameter.

## Scope and notation clarifications

4. **General real-valued leaves exceed the literal Lean tree interface.** Lines 353 and 502 state (F25)/(F33) for trees with arbitrary leaf labels in `[-1,1]`. The exact source types `sum_abs_ext_Dl_le`, `abs_ext_tree_chaos_le`, and `advantage_le_sharp` take

   ```lean
   (T : QueryTree I) (v : Bool → ℝ) (hv : ∀ b, |v b| ≤ 1)
   ```

   and apply to `g z = v (T.eval z)`. Thus the literal interface has Boolean leaves with a common two-value decoding, not an arbitrary independent real label at each leaf. The ordinary proof given in the section does establish the general bounded-leaf statement, so the mathematics is sound. Either narrow the lemma to this exact Boolean-tree formulation, which is enough for the endpoint, or add a sentence to the final scope paragraph identifying the bounded real-leaf version as an ordinary generalization. Also specify that `d` is an integer depth cap in the lemma.

5. **Define the zero convention for random restrictions.** Before (F57), specify that Fourier coefficients retain the original coordinate labels and that `widehat(g_rho)(S)` is defined as zero unless every coordinate of `S` is left free. Without this convention the random-domain coefficient in the expectation is undefined on some restrictions. The stated product of free probabilities is correct, and the subsequent argument already handles the no-free-variable case.

## Optional wording refinement

At line 173, “the individual functions and their derivatives are bounded as well” may be read to include `q(x)=sqrt(2+x^2)`, which is unbounded. Replace it with “Both `Psi` and `varphi`, and the derivatives needed below, are bounded.” The intended claim about the factors used by Stein is correct.

## Specific checks that passed

- (F2) preserves the one-sided yes promise, including the status of large negative values.
- (F22) uses the correct matrix orientation and one common parameter in (F23); the exact-source claim remains mean-value based.
- The stopped-chaos proof handles repeated queries and avoids conditioning on a future good event.
- The path-to-coordinate-set injection removes any multiplicity factor in (F33).
- The moment proof does not assume independence of a correlated selected `U` and `V`, and combines the hard-minus-uniform identity with the zero uniform mean.
- Amplification is exactly `2 tau` trials with cap `2 tau D`, and padded depth is positive.
- (F41) handles all unpromised inputs without assuming promise support of either distribution.
- (F43) matches the exact current theorem: initial error `1/3`, `m=4^t`, `15k+2 <= 2t`, constant `2/18225`.
- The arithmetic in (F44)–(F51), including `800*(2/18225)=(8/27)^2` and `4*13669=54676 > 54675`, is consistent with the displayed proof.
- The final paragraph does not confuse the ordinary SSW/variable-error/power-of-two deduction with either compiled endpoint.

These are presentation/interface fixes. No additional imported lower-bound assumption or unproved hard analytic step is needed for the main theorem.
