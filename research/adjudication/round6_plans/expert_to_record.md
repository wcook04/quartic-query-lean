# What the reasoning record must receive from the expert companion (round six)

The expert companion was revised on 3 November 2026. Three items have to reach `docs/reasoning_record.md`, and the companion will link to the new material once its anchors exist. Until the record agent lists new anchors at the end of `round6_plans/reasoning_record.md`, the companion keeps using existing anchors only.

## 1. Drucker's global-budget theorem also suffices (passages CL-literature-and-verification and CL-address-guess)

At present both passages say that Drucker's Theorem 1.1 "treats a global budget" or "has a different global-budget statement". That is true, but it suggests the theorem cannot be used here. It can. I checked this against Drucker, arXiv:1005.0644v2, Theorem 1.1 (restated in §3), and the remark at the end of his §1.2 that the results apply to partial functions.

Text to add, adapted to the record's notation:

> Drucker's Theorem 1.1 assumes only one global budget, and it would also serve here. Let μ be the minimax law of §6.2, so every randomized algorithm of depth L succeeds with probability at most 2/3 under μ. Take T=L, ε=1/3, k=r copies and α=3/r. Then 0<α≤3/40, and the global budget αεTk equals exactly L. The theorem bounds the all-answer success of any algorithm with total cap L on r independent inputs from μ by (2^{1/r}·2/3)^r = 2(2/3)^r. The simulator of §6.5 has total cap L, and its side information is jointly independent of the r target strings, so it is such an algorithm once that information is fixed. Using this bound replaces the guessing term Gβ^r in the discrepancy estimate by 2Gβ^r ≤ 2/(100 m^8), and the ceiling 6/100 is unchanged. We use the separate-cap form (6.1) because it gives β^r exactly and has a short proof.

## 2. New §7.4: a growing-parameter family

The record's §7.2 currently ends with "A family with a quantitative schedule k=k(t) requires additional uniform estimates and is a separate result." The companion's §7 remark proves exactly such a family, so the record should contain the derivation. Replace that sentence with a pointer to a new §7.4 containing the following.

**Inputs.**
- The uniform bound (16) of the companion, `forr_uniform_assembly`: R(P_{k,m}) > X := (2/18225)·m^{1−1/k}/(k² ln(4km)), for m=4^t and 15k+2 ≤ 2t.
- The generic lower bound (15): R(F_{k,m}) > ⌊mL/100⌋ for every integer L with 1 ≤ L ≤ m and L < R(P).
- The explicit quantum bound `Upper/Bound.lean` (src-budget-exponential): Q(F_{k,m}) ≤ 2^{53}·k·2^{10k}·√m·ℓ^6 for every t ≥ 1.

**Step 1.** If 15k+2 ≤ 2t and t ≥ 32, then X ∈ [2, m]. The upper end is immediate because 2/18225 < 1 and k² ln(4km) > 1. For the lower end, m^{1−1/k} ≥ 2^t and k ≤ 2t/15; at t=32 the inequality 2^t ≥ 18225·k²·ln(4km) holds with a large margin, and both sides are monotone in t.

**Step 2.** Put L=⌊X⌋. Then 1 ≤ L ≤ m and L ≤ X < R(P). Since R(F) is an integer exceeding ⌊mL/100⌋, it exceeds mL/100. Because X ≥ 1 gives L ≥ X/2, we get R(F_{k,m}) > mX/200 = m^{2−1/k}/(1822500·k²·ln(4km)), using 200·18225/2 = 1822500.

**Step 3.** Take k=⌊√(t/20)⌋ with t ≥ 80, so that k ≥ 2 and 15k+2 ≤ 2t. Comparing log₂ of the Step 2 lower bound with (4−ε(ℓ))·log₂ of the quantum bound, where ε(ℓ)=8√(10/ℓ)+(56 log₂ℓ+508)/ℓ and ℓ=2t, gives R(F_t) ≥ Q(F_t)^{4−ε(ℓ)} for F_t = F_{k,4^t}. Write out this comparison in full in the record.

The leading term checks out heuristically. The loss is about ℓ/k + 40k against log₂Q ≈ ℓ/2, which gives 2/k + 80k/ℓ. With k ≈ √(ℓ/40) this is 2√(40/ℓ) + 80/√(40ℓ) = 8√(10/ℓ).

I also ran a numerical sweep comparing the two bounds in logarithms, for every t from 80 to 4999 and for t = 10^4, …, 10^8. No violation appeared. This is a sample check, not a proof; the record needs the complete inequality chain.

**Boundary.** The family attains exponent 4 − O(ℓ^{−1/2}) and still gives no bound R = Ω(Q^4). The ordinary deduction uses the built theorems above. The record's §2.9 should give their status.

## 3. Record §2.9: the amplifier row, and the companion's former Appendix A

1. **Amplifier relation.** Wherever §2.9, or any statement table, describes `uniformOpaqueAmplifier` as "stronger" because it "returns the state", correct the wording. The printed Lemma 3.1 already returns the normalised successful state. What the formal statement adds:
   - it is uniform in 𝒜 (one selector gate is fixed before every opaque unitary);
   - it gives the exact success mass;
   - it returns 𝒜's successful state tensored with an auxiliary vector.

   What it restricts: the success test is a predicate on basis labels, and the reduction from a general projector is not formalised.
2. **Material that left the companion.** The companion no longer carries its fidelity table, object map, Comparator explanation or review-status paragraph. The record's §2.9 is now the only place a reader finds the statement-by-statement relation (same, stronger, weaker or mixed) for:
   - Theorem 1 (existential log exponent; floor-form lower bound);
   - the constants theorem (named circuit; its threshold is existential);
   - (5) and (16);
   - the full Lemma 2.2;
   - the amplifier, in both forms;
   - the direct-product endpoint (finite weighted seeds; recursive compliance against per-input counts);
   - (11) with its bound, the 2G/(m(m+1)) charging inequality, (12), the four winner facts, and the model sanity checks.

   Please make sure each of these has a row there.
3. **Bundle boundary.** Add one sentence per Comparator bundle saying whether its challenge definitions are Mathlib-only or import maintained `QuarticQuery` modules:
   - Mathlib-only: Unconditional, Construction.
   - Imported: UniformAmplifier, RealizedCaps, ConstructionFull, and Eq19 through its Spec.

## Already moved by the companion's owner

Reproduction metadata is now in `README.md` under "Reproducing the formal checks", with the following facts:
- the links are pinned at e9dfefb;
- the recorded Unconditional run was made at 9a0a5cd, paranoid and unsandboxed;
- `lean/` is identical from 659b571 to HEAD;
- Reach.lean prints a projection of the closure.

The record's Appendix F may point there.
