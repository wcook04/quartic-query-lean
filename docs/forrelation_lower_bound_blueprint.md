# Blueprint: the Forrelation randomized lower bound in Lean

Target, frozen in `lean/QuarticQuery/Statement.lean`:

```lean
def BansalSinhaLower : Prop :=
  ∀ k : ℕ, 2 ≤ k → ∃ t₀ : ℕ, ∀ t : ℕ, t₀ ≤ t → Lvalue k t < R (P k t)
```

`Lvalue k t = ⌊m^(1-1/k) / (log₂ m)²⌋` with `m = 4^t`, so `log₂ m = 2t`. `P k t` answers
`true` when `Φ ≥ δ`, `false` when `|Φ| ≤ δ/2`, with `δ = 2^(-5k)`.

**Status: proved.** `QuarticQuery.ForrelationLower.bansalSinhaLower : BansalSinhaLower` compiles
with no `sorry`; `#print axioms` gives `propext, Classical.choice, Quot.sound`. Details are in §6.

## 1. The weakest thing needed

For fixed `k`, large `t`, depth `L = Lvalue k t`:

* no constant is tracked in `k`, and `t₀` may depend on `k`;
* the depth bound has a full `(log m)²` to spare, so a growth bound
  `wt_k(T) ≤ C_k (d log n)^(k/2)` with `n = km` is enough: it costs
  `(log m)^(k/2)` against the `(log m)^k` the depth gives away;
* the promise is the exact `δ = 2^(-5k)`. This is the one thing that cannot be relaxed. A
  hard distribution with `E Φ = 1/polylog` proves nothing about `P`, so the first version of
  Bansal–Sinha (variance `1/log N`) does not apply, and rounding must keep constant bias.

## 2. Routes compared

**A. Bansal–Sinha v3 (Gaussian interpolation).** `k-1` independent interpolation parameters,
hence `k-1` generators, with an index `i_r` and an index `j_r` in each middle block. When
`i_r ≠ j_r` two leftover factors remain. Removing them is the branching process of Lemmas
18–26, which yields levels `k … k(k-1)`. Lean needs: differentiation of Gaussian expectations
under `√t`, Lemma 13 with Owen's `T`, the branching process with its counting, the biased
restriction Theorem `fwt`, and Tal's Theorem 10 as an outside input. Estimate: more than
5000 lines; the branching process alone is the largest item.

**B. Sherstov–Storozhenko–Wu / Tal (moments plus sharp Fourier growth).** Bound
`Σ_S |f̂(S)| |E χ_S|`. Needs moment bounds through all levels and the sharper
`√(C(d,ℓ) (log n)^(ℓ-1))`. It needs operator-norm control of submatrices of the orthogonal
matrix. The Hadamard matrix has large constant submatrices, so this is proved for random
orthogonal matrices and, by Bansal–Sinha's own remark, does not apply to the exact `P` here.
Rejected: it does not reach the target.

**C. Discrete or simplified variants.** (i) Density `1 + Φ`: valid, level `k` only, but
`E Φ ≈ 1/m`, so it misses the promise. (ii) Rademacher hidden vector with `y = clamp(Hx)`:
no exact chain rule in `U_i`, and the coordinates of `Hx` are not independent. (iii) Fixing the
middle blocks and correlating only `z_1, z_k` by the matrix `A(z_mid)`: gives constant
`Φ`, but has nonzero 4-point moments on blocks 1 and `k`, which need more than level-`k`
`ℓ₁` growth. (iv) Maiorana–McFarland bent pairs: `Φ = 1` but broken by three queries.
All rejected. Hybrid over coordinates in a fixed order works algebraically but evaluates at a
different bias per coordinate, so no single `μ` carries the growth bound.

**D. Selected: one bias-scaling path and a single Stein walk.** Same hard distribution shape as
A, with an elementary truncation. Scale only block 0 by `s ∈ [0,1]`. Multi-affinity gives
`d/ds = Σ_a X_0(a) ∂_{(0,a)}`, with no Gaussian time derivative. Each `X_j(a)` is removed by
one Stein identity in coordinate `U_j(a)`, which yields one `H` and moves one block to the
right. Because the same index that entered a block leaves it, no mismatch `i_r ≠ j_r` ever
appears, so there is no branching and only level `k` occurs:

```
E[ext g(w_1)] - ext g(0)
  = ∫₀¹ ds Σ_{p ∈ [m]^k} ∏_{r<l} H(p_r, p_{r+1})
       E[ ∏_{r<l} Ψ(U_r(p_r)) φ'(V_r(p_{r+1})) · ext(D_p g)(w_s) ],     l = k-1.        (★)
```

Check before formalising: (★) was evaluated by Gauss–Hermite quadrature at `k=3, N=2` with a
random `g` (BS truncation), both sides `-6.1263979774e-4`, agreeing to 12 digits. Lean now
proves its mean-value form for every `k` (`exists_identity`, then `Int_eq_paths`). It gives the
same threshold `d ≪ m^(1-1/k)/log m` as Bansal–Sinha, using only level `k`, whereas their proof
uses levels `k … k(k-1)`. The sources read do not state (★); no wider search was made, so no
novelty is claimed. Bansal–Sinha remain the source of the hard-distribution shape and the
promise calculation.

Fourier growth is also replaced. Instead of Tal plus a random-restriction transfer, Azuma's
inequality is run directly along the tree under the biased measure, with a union bound over
one contracted index per level. This gives

```
Σ_J |ext(D_J T)(μ)| ≤ (16 k d log(4n))^(k/2) + 1    for |μ_a| ≤ 1/2.
```

It is a weaker logarithm than Tal, and enough by §1. Tal's Theorem 10 is not an input.

Truncation. Take `q(x) = √(2+x²)`, `Ψ = 1/(2q)`, `φ = xΨ - Ψ' = x(3+x²)/(2q³)`,
`φ' = 3/q⁵`. Then `|φ| ≤ ½`, `0 < Ψ ≤ ½`, `0 < φ' ≤ 1`, and Stein's identity
`E[φ(U) G(U)] = E[Ψ(U) G'(U)]` is one line, since `(Ψ·pdf)' = -φ·pdf`. No Owen `T`, no Gaussian
cdf. From `e^x ≥ 1+x`, `log y ≤ y-1`, `E U² = E V² = 1`:
`E ∏_r Ψ(U_r) φ'(V_r) ≥ (1/18)^l`, valid for correlated `U, V`, and `1/18 ≥ 1/32`.

## 3. Lemmas

`ι` is a finite coordinate type, `sgn = bitSign`, `ext g μ = Σ_z g z ∏_a (1+μ_a sgn z_a)/2`,
`D a g z = (g z[a:=false] - g z[a:=true])/2`.

Cube (`Cube.lean`, difficulty low)

* C1 `ext` is linear, `|ext g μ| ≤ B` for `|g| ≤ B`, `|μ| ≤ 1`.
* C2 chain rule: along differentiable `c`, `d/dt ext g (c t) = Σ_a c'_a ext (D a g) (c t)`.
* C3 `D a (D a g) = 0`.
* C4 `ext (D a g) μ = ext (g ξ_a) μ` for `|μ_a| < 1`, `ξ_a z = (sgn z_a - μ_a)/(1-μ_a²)`;
  so `ext (D_list p g) μ = ext (g ∏_{a∈p} ξ_a) μ` for a duplicate-free list `p`.
* C5 affine split `ext g μ = Σ_b π_a(b) ext (g[a:=b]) μ`.

Growth (`TreeGrowth.lean`, medium; the riskiest self-contained item)

* T1 `A c ℓ Q z = Σ_{J ⊆ Q, |J|=ℓ} c J ∏_{a∈J} ξ_a(z)`, with
  `A c ℓ (insert q Q) = A c ℓ Q + ξ_q A (c^q) (ℓ-1) Q`, `c^q J = c (insert q J)`.
* T2 walk expectation and hitting probability on a tree, keyed by the set of queried
  coordinates, so repeated queries need no normal form.
* T3 two-point Hoeffding: `Σ_b π(b) exp(t ξ(b)) ≤ exp(t²B²/2)`, for mean zero, `|ξ| ≤ B`.
* T4 one-level Azuma: `Hit (Y > R or Bad) ≤ exp(-λR + λ²β²B²d/2) + Hit Bad`.
* T5 induction on `ℓ`: `Hit(|A c ℓ| > κ^ℓ) ≤ (4n)^ℓ e^{-Λ}` with `κ² = 2 d B² Λ`.
* T6 `|ext (val∘T · A c k univ) μ| ≤ κ^k + 1`.

Gaussian (`Stein.lean`, medium)

* G1 definitions and bounds for `φ, Ψ, φ'`.
* G2 one-dimensional Stein under `gaussianReal 0 1`, via
  `integral_eq_zero_of_hasDerivAt_of_integrable`.
* G3 Stein in one coordinate of `Measure.pi`, via `measurePreserving_piEquivPiSubtypeProd`.
* G4 reflection invariance of `Measure.pi` from `stdGaussian_map`; `E⟨e,u⟩² = 1` for a unit `e`
  from `variance_dual_stdGaussian`.

Walk (`Walk.lean`, high; depends on C2, C3, G3)

* W1 derivative of `G(u) = θ(u) ext g (w s u)` in `u(j,a)`.
* W2 the recursive integrand `I`, and `E[θ X_j(a) ext g (w)] = E[θ I]` when `g = D_{(j,a)}g₀`.
* W3 (★) as `h'(s) = Σ_a E[I l 0 a (D_{(0,a)} g)]`.
* W4 `h(0) = ext g 0`: zero the coordinates block by block, by the reflection flipping one
  `V_{j-1}(a)`, using oddness of `φ`.

Promise (`Promise.lean`, medium; depends on W, Forrelation/Product)

* P1 `D_p` of `Φ` is the constant `coef p`, for `p` a full path.
* P2 `E_{p1} Φ ≥ (1/18)^l`, from (★) applied to `Φ` and the tangent bound, with `ext Φ 0 = 0`.
* P3 `E_u Φ² = 1/m` (Parseval), hence Chebyshev.

Reduction to the promise. Here is exactly where the proof meets it. `p₁` is not supported on
the promise, and neither is the uniform measure. For a mixture `a` with error `ε` on promised
inputs:

* `E_{p₁} a ≥ (1-ε) p₁(Φ ≥ δ)`, with `p₁(Φ≥δ) ≥ E_{p₁}Φ - δ`, since `|Φ| ≤ 1`; this needs no
  more than `Φ ≥ δ` and ignores `-1`-side mass;
* `E_u a ≤ ε + u(|Φ| > δ/2) ≤ ε + 4/(δ² m)`.

With `E_{p₁}Φ ≥ (1/18)^{k-1} ≥ 32 δ` the gap is at least `δ` for `ε ≤ δ` and large `m`. A
mixture of error `1/3` does not suffice: on `p₁` all the mass outside the promise is free, so
amplification to `ε ≤ δ` is essential. Rounding is `ext` itself: `E_{p₁} g` is defined as
`E_U ext g (w_1 U)`, so `p₁` is a mixture of product measures with means `w`, and `|w| ≤ ½`
is what makes `ξ` bounded by 2. Truncation to the cube is built into `φ`.

Amplify (`Amplify.lean`, low): A1 `τ`-fold run tree, depth `≤ τ L`; A2 majority error at most
`(8/9)^τ`, by exponential Markov with `λ = 2`. `Upper/` amplification is quantum and not
usable; `exists_program_of_mixture` is not needed in this direction.

Assembly (`Main.lean`, low to medium): M1 advantage `≤ H∞^l c^l [(16 k d log 4n)^{k/2}+1]`.
M2 asymptotics at `d = τ L`, `L ≤ m^{1-1/k}/(4t²)`, `H∞ = m^{-1/2}`: the bound is
`≲ (C t/t²)^{k/2} + m^{-(k-1)/2} → 0`. M3 `bansalSinhaLower`.

## 4. Library check at the pin

Read in the pinned source: `stdGaussian_map`, `map_pi_eq_stdGaussian`,
`variance_dual_stdGaussian`, `charFun_stdGaussian` in
`Mathlib/Probability/Distributions/Gaussian/Multivariate.lean`;
`measurePreserving_piEquivPiSubtypeProd`, `measurePreserving_piUnique` in
`MeasureTheory/Constructions/Pi.lean`; `integral_eq_zero_of_hasDerivAt_of_integrable` in
`MeasureTheory/Integral/IntegralEqImproper.lean`. Repo: `abs_Phi_le_one`, `isOrth_H`,
`H_mul_H`, `exists_hard_distribution`. Complexitylib is not needed: Chernoff and Fourier
tools there do not address adaptive trees, and `QuarticQuery` keeps a Mathlib-only proof.

## 5. Hardest step and falsifiers

As planned, the hardest bookkeeping was W1–W3 (`w` on `Fin (l+1) × n` and the chain rule); it
went through once `Xf`, `Yf`, `Uc`, `Vc` were indexed by naturals. The stated falsifiers did not
occur: (★) holds in Lean; `E ∏ Ψ φ' ≥ (1/18)^l` with `1/18 ≥ 1/32`; the union bound costs
`Λ = 2k log(4n)`. The exact promise constant `δ = 2^(-5k)` is used in `P_yes`, `P_no` and
`bansalSinhaLower`, through `32 δ ≤ (1/18)^l`.

Deviations from the plan. (i) P1 was replaced by the nested form `Rs`: each `D` removes one layer,
so `Int` on `Φ` unfolds directly (`Int_Rs`) with no closed form for path products. (ii) The
moment bound is a recursion on `TT` with `∫ TT = 0`, using finite Jensen at each step. (iii)
`Λ = 2k log Y`, with `Y = 4n`. (iv) `exists_identity` is a mean-value statement at one `s ∈ (0,1)`,
which avoids any integral in `s`.

## 6. Status

All in `lean/QuarticQuery/ForrelationLower/`, 3846 lines, built in the `QuarticQuery` root and
consumed by `QuarticQuery.alphaTot_eq_four_unconditional`. No `sorry`, no new axioms,
`Statement.lean` unchanged. Comparator accepts `forrelation_lower_bound` in the
`Unconditional` bundle. The route note in section 2 is imprecise: Azuma loses a factor
`(log m)^(1/k)` against the growth bound Bansal and Sinha quote, which the slack in `L` absorbs.

| Lemmas | File | Main theorems |
|---|---|---|
| C1–C5 | `Cube.lean` | `abs_ext_le`, `hasDerivAt_ext`, `D_D`, `ext_D_eq_mul_xi`, `ext_split`, `ext_affine` |
| T1–T6 | `TreeGrowth.lean` | `chaos_insert`, `hit_azuma`, `hit_chaos_le`, `abs_ext_tree_chaos_le`, `sum_abs_ext_Dl_le` |
| G1–G4 | `Stein.lean` | `stein_one`, `stein_pi`, `integral_reflect`, `integral_dot_sq` |
| W1–W3 | `Walk.lean` | `sum_dw_eq`, `integral_walk`, `exists_identity`, `Int_eq_paths` |
| W4, M1 | `Cascade.lean` | `integral_ext_wv_zero`, `advantage_le` |
| P1–P3 | `Promise.lean` | `numerator_eq_Fz`, `Int_Rs`, `mass_ge`, `ext_PhiF_sq` |
| A1–A2 | `Amplify.lean` | `exists_amplified` |
| M2–M3 | `Main.lean` | `not_RLe_of_gap`, `exists_threshold`, `bansalSinhaLower` |

Checked in a scratch file: `alphaTot_eq_four_of_bansalSinha bansalSinhaLower` elaborates. The
library root `QuarticQuery.lean` does not yet import these files, and nothing is committed. An
independent mathematical reading of (★) has not happened; the Lean check is the evidence.
