# Independent review: the Forrelation lower bound in Lean

Reviewer: an adversarial reading by an agent that did not write the proof. No Lean was run and no
Lean file was edited. Every number below was computed in this review. Scripts and raw output are
in the session scratch folder (`star.py`, `star2.py`, `sim.py`, `params.py`), not in this repository.

## 1. Result

I found no error, and I found no way for the theorem to be true for a wrong reason.

The statement `BansalSinhaLower` uses the frozen definitions of `Statement.lean`, none of them is
shadowed or redefined, and `Lvalue` is large and growing. The promise is nonempty on both sides and
the proof handles inputs outside the promise correctly. The argument is correct as mathematics, and
I can reconstruct it on one page. The key identity held on every test I ran, including cases not
used before and a different truncation function.

The short route is real and it needs no extra hypothesis. It is not a fixed-`k` artefact: the core
inequality `advantage_le` holds for every `k`, every orthogonal `H` and every tree. The only thing
the fixed-`k` form loses is what the frozen statement chose not to ask for.

The result is a strictly weaker statement than the published theorem. It is the case the quartic
separation needs: each fixed `k`, `m` a power of 4, error 1/3, and a bound lower by about
`(log m)^(1+1/k)`. The proof underneath is stronger than the statement, and in its dependence on
`k` it is better than the published proof. Section 4 gives the exact relation.

Three small inaccuracies in the blueprint need correcting, and a full build of the library root is
outstanding. They are in section 7. None touches the mathematics.

## 2. The argument, reconstructed

Take `k = l+1` blocks of `m` coordinates and an orthogonal matrix `H` with entries at most `ε`.
Draw independent standard Gaussian vectors `U_0, …, U_{l-1}` and set `V_r = H U_r`. Fix an odd
bounded `φ`, and let `Ψ` satisfy `(Ψ·pdf)' = -φ·pdf`. Stein's identity then reads
`E[φ(U) G(U)] = E[Ψ(U) G'(U)]`. Write `X_r = φ(U_r)` and `Y_r = φ(V_r)`. The hard bias vector `w_s`
is `s X_0` on block 0, `Y_{r-1} X_r` on block `r`, and `Y_{l-1}` on block `l`. For a function `g` on
the cube, `ext g` is its multi-affine extension.

**Path.** Put `h(s) = E[ext g (w_s)]`. Only block 0 moves, and `ext g` is affine in each coordinate,
so `h'(s) = Σ_a E[X_0(a) · ext(D_{0,a} g)(w_s)]`.

**Walk.** Apply Stein in `U_0(a)`. The derivative falls on two kinds of term. It falls on `X_0(a)`,
but that coordinate has been removed by `D_{0,a}`, so this term is zero. It falls on each `V_0(b)`,
which appears only through `Y_0(b)` in block 1, giving `H(b,a) φ'(V_0(b)) X_1(b)` and a new derivative
at `(1,b)`. The factor `X_1(b)` sits at the coordinate just differentiated, so the same step repeats
in `U_1(b)`. The factors already produced depend only on earlier Gaussians, so later Stein steps do
not touch them. Block `l` has no `X` factor and the walk stops:

```
h(1) - h(0) = ∫₀¹ ds Σ_{p ∈ [m]^k} ∏_{r<l} H(p_{r+1},p_r)
                E[ ∏_{r<l} Ψ(U_r(p_r)) φ'(V_r(p_{r+1})) · ext(D_p g)(w_s) ].      (★)
```

**Start.** At `s = 0`, block 0 has zero bias. Then `U_0` matters only through `V_0`, whose coordinates
are independent, so reflecting one `V_0(b)` flips the sign of one bias in block 1. Since `ext` is
affine, that coordinate can be set to zero. Clearing block 1 frees `U_1` in the same way, and so on.
Hence `h(0) = ext g 0`, the uniform average.

**Advantage.** Each path weight is at most `(3ε)^l`, and the integrand is a sum over paths of
`ext(D_p g)` at a point with bias at most 1/2. For `g` a depth-`d` tree the growth bound gives
`Σ_p |ext(D_p g)(μ)| ≤ (16 k d log 4km)^(k/2) + 1`. So the advantage over uniform is at most
`(3/√m)^l ((16 k d log 4km)^(k/2) + 1)`.

**Mass.** Put `g = Φ`. For the Walsh matrix each path then contributes
`m^(-1-l/2) · m^(-l/2) · ∏ Ψ φ'`, positive, so the same identity gives `E_{p₁} Φ ≥ (1/18)^l`,
which is at least `32 δ`. On the uniform measure `E Φ² = 1/m`.

**Promise.** Let `a` be the acceptance probability of a program amplified to error `ε ≤ δ`. Pointwise,
`(1-ε)(Φ-δ) ≤ a`: where `Φ ≥ δ` the input is promised, and elsewhere the left side is at most 0. Also
`a ≤ ε + 4Φ²/δ²`: where `|Φ| ≤ δ/2` the input is promised, and elsewhere the added term exceeds 1. Taking
expectations gives a gap of at least `13δ` between `p₁` and uniform. The advantage bound forbids that.

**Why it looks too good, and why it is fine.** Two facts explain it.

First, "only level `k`" means level `k` at a biased point. `ext(D_J g)(μ)` equals
`Σ_{S ⊇ J} ĝ(S) μ^(S∖J)`, so every higher uniform level is inside it. The higher levels have not
disappeared. They have been moved into the claim that level-`k` growth holds uniformly at all
biases up to 1/2. Bansal–Sinha also work at biased points, so this hides nothing from their
comparison. Their extra levels `k+1 … k(k-1)` are extra biased levels.

Second, the branching in Bansal–Sinha comes from their interpolation, which is a choice. They scale
each pair `(U_κ, V_κ)` by its own `√t_κ`, so each middle block receives an index `i` from the left and
an independent index `j` from the right. When `i ≠ j` two factors are left over, and removing them
branches. In (★) the Gaussians keep unit variance and there is one scalar parameter. Each block gets
one index, created by the Stein step on its left and consumed by the Stein step on its right. The
price of dropping `t = 0` is that `s = 0` is not the zero vector, and the reflection argument pays it.
This works because the coordinates of `V_r` are independent, which uses orthogonality of `H` and
nothing else about it.

The same route applies to the Bansal–Sinha truncation `φ = Φ_cdf - 1/2`, with
`Ψ = Φ_cdf(1-Φ_cdf)/(2γ)`. Their Owen `T` machinery exists to handle `Ψ_σ` at variance below one, and
(★) never leaves variance one. I tested this case in section 6.

## 3. Could the theorem be proved for a wrong reason?

Everything internal to the proof (the Gaussian measure, `wv`, `ext`, `Int`) is invisible in the
statement, so none of it can change what is proved. Only the statement's constants matter.

* **Frozen definitions.** `git diff HEAD -- lean/QuarticQuery/Statement.lean` is empty. Searching all
  of `lean/QuarticQuery` finds no other declaration named `P`, `R`, `Q`, `Phi`, `Lvalue`, `mValue`,
  `BansalSinhaLower`, `RLe`, `bitSign`, `walshSign`, `forrelationNumerator` or
  `forrelationDenominator`. The one clash is `ForrelationLower.D`, the discrete derivative, which
  shadows the deterministic complexity `QuarticQuery.D` inside that namespace. `D` does not occur in
  `BansalSinhaLower`, so this is harmless, though it is a readability trap. The `R` in `section Lin`
  of `Promise.lean` is a local variable and that section closes before `lt_R_of_not_RLe` is used.
* **Instances and notation.** The only instance is `IsProbabilityMeasure (gP ι)`. The only notation
  is `local notation "Nm" t => Fin (mValue t)`. Neither can change the meaning of the statement.
  There is no `axiom`, `sorry`, `unsafe`, `implemented_by`, `native_decide`, `csimp` or `opaque` in these
  files. `sorryAx` occurs 0 times in all 16 `.olean` and `.olean.private` files of the directory, and
  `Main.olean` (06:34) is newer than the sources (06:11). That is a coarse check; `#print axioms` is the
  real one, and I did not run it.
* **`Lvalue` is not degenerate.** The exponent is real: `1 / (k : ℝ)`, with no natural-number division.
  `Real.logb 2 (mValue t) = 2t` is proved as `logb_mValue`. `one_le_Lvalue` gives `L ≥ 1` from `t = 8`. For
  `k = 2`, `L` is 1, 2, 7, 64, 655, 298261 at `t` = 8, 10, 12, 16, 20, 30. For `k = 3` it is 6, 25, 113, 2580,
  66580, 305419896. For `k = 5` it is 27, 163, 1045, 49667, 2684354, 78187493530. At `t = 0` the logarithm
  is 0 and Lean's division gives `L = 0`, but `t₀ ≥ 8` excludes that.
* **Division by zero.** `P` is written with integer comparisons and no division. `Phi` divides by a
  positive integer (`denom_pos`). `ξ` divides by `1-μ²`, at least 3/4 for `|μ| ≤ 1/2`. I found no
  inequality made easy by a zero denominator.
* **`R` as an infimum.** `sInf ∅ = 0` would make a lower bound false, not easy, and `lt_R_iff` uses
  `RLe_R`, the read-all witness. `lt_R_of_not_RLe` is the right direction by monotonicity.
* **`t₀` is honest and huge.** The threshold in `exists_threshold` is about 5.9e11 for `k = 2`, 1.3e16 for
  `k = 3`, 3.5e24 for `k = 5` and 5.7e45 for `k = 10`. Evaluating the actual inequalities at `L = Lvalue`, they
  start to hold near `t` = 2.7e5, 2.2e6 and 1.65e7 for `k` = 2, 3, 5. The bound therefore holds for all
  large `t`, with no special sequence, but it says nothing at any `m` that could be written out. Readers should be
  told this: the theorem is purely asymptotic.
* **Nothing is vacuous.** The conclusion itself rules this out. If one answer had no promised input, a
  constant tree would satisfy `RLe` at budget 0, so `¬ RLe (P k t) L` already forces promised inputs of
  both answers. The proof also shows it directly: `p₁(Φ ≥ δ) ≥ 31 δ`, and uniform gives `|Φ| ≤ δ/2` with
  probability at least `1 - 4/(δ²m)`. `Forrelation/Sanity.lean` confirms 104, 48 and 104 inputs at `k = 2, t = 1`.
* **The hard distribution is not supported on the promise, and that is handled.** Neither `p₁` nor uniform
  is. The same is true in Bansal–Sinha. `not_RLe_of_gap` uses correctness only through `herr`, which is
  conditional on `f x = some b`, and treats unpromised inputs through the two pointwise bounds of section 2.
  Those use only `0 ≤ a ≤ 1` and `|Φ| ≤ 1`. The blueprint is right that error 1/3 is not enough here, since
  the free mass outside the promise can absorb it. Amplification to error at most `δ` is essential, and it
  is done: `(8/9)^τ` with ties counted as wrong in `maj_wrong`.
* **All programs are covered.** `RLe` quantifies over every finite mixture of adaptive trees, and the
  proof applies `advantage_le` to each tree of the amplified mixture separately, with no assumption on
  the trees. The bound holds for repeated queries because `hit_azuma` does not count them as a fresh step.
* **Signs.** `sg` agrees with `bitSign` (`sg_eq_bitSign`), `P_yes` and `P_no` match the integer tests at
  `2^(5k)`, and `Phi_eq_PhiF` ties the internal `Φ` to the frozen numerator through the pre-existing
  `numerator_eq_walk`. The check `32 δ = (1/32)^l ≤ (1/18)^l` is exact at `δ = 2^(-5k)`, so the promise constant is
  the frozen one, and it is the only place where it could have been relaxed.

## 4. Relation to the published theorem

Bansal–Sinha (`thm:lower`; the extraction does not print the number 1.3, and I take it to be this one)
state: for `k ≥ 2`, `δ = 2^(-5k)`, every `N = 2^n` and error `1/2 - η/2`, depth
`Ω(k^(-28) (N/log kN)^(1-1/k) η²/log(1/δ))`. Corollary 3 is the case of error 1/3. The partial function is the
same as `P`, up to `N = m`. The hard distribution has the same shape as the Lean one with a different `φ`.

**What the Lean theorem says.** For each fixed `k ≥ 2` there is `t₀` such that for all `t ≥ t₀`, every error-1/3
randomized program for `P k t` needs more than `⌊m^(1-1/k)/(log₂ m)²⌋` queries, where `m = 4^t`.

**It is implied by the published theorem** for large `t`, because `(log m)²` eventually beats
`C k^29 (log km)^(1-1/k)` at fixed `k`.

**It does not imply the published theorem.** The losses in the statement are these:

1. `k` is fixed and `t₀` depends on it, so nothing uniform in `k` is claimed, and in particular nothing for `k`
   growing with `m`.
2. Only `m = 4^t` is covered, so odd `n` in `N = 2^n` is not.
3. Only error 1/3 is covered. There is no `η` dependence, and the case `η ≈ δ` that compares with the
   `⌈k/2⌉`-query quantum algorithm is not stated.
4. The bound has `(log m)²` where the paper has `(log kN)^(1-1/k)`, a loss of `(log m)^(1+1/k)`.
5. Only the Hadamard case is stated. The paper remarks that its proof covers orthogonal matrices with small
   entries.

**The proof gives more than the statement.** These are my derivations from Lean-checked inequalities. They are
not themselves Lean theorems.

* `advantage_le` holds for all `k`, all orthogonal `H` and all trees, with no asymptotics. Its hypothesis is
  `RowsOrth` and an entry bound.
* Combining it with `not_RLe_of_gap` gives, for every `k` and every `m = 4^t ≥ 2^(15k+2)`, about
  `R(P k t) ≥ c · m^(1-1/k) / (k² log 4km)`, with `c ≈ 1.2e-7` across `k` = 2 to 20. Against Corollary 3, this
  **improves `k^(-29)` to `k^(-2)` and loses a factor `(log kN)^(1/k)`**.
* The factor `(log)^(1/k)` comes entirely from using Azuma in place of the sharper growth bound. Feeding
  (★) with Bansal–Sinha's own Corollary `cor:wt` in place of Azuma gives advantage at most
  `3^(k-1) N^(-(k-1)/2) (4cd/3)^(k/2) (log kN)^((k-1)/2)`, and so depth
  `Ω((N/log kN)^(1-1/k) η²/log(1/δ))`. **That would be Theorem 1.3 with the factor `k^(-28)` removed**, on the
  same log factor. So (★) is a strict quantitative improvement of the published analysis, as a paper
  statement if not yet in Lean. I checked this arithmetic by hand, and it is the point an expert should look at
  first. I did no search of my own on whether a later paper has it. A separate note,
  `docs/forrelation_route_prior_art.md`, appeared during this review and reports route D as not found; I did not
  check that note.

**Relative to Tal's level-`k` growth.** The Lean file proves, as a by-product, an unconditional bound at uniform
and biased measures, `sum_abs_ext_Dl_le`. It neither implies nor needs Tal's theorem, and the Lean theorem
says nothing about Fourier growth at Tal's strength.

## 5. The growth bound

The claim is `Σ_J |ext(D_J T)(μ)| ≤ (16 k d log 4n)^(k/2) + 1` for `|μ_a| ≤ 1/2`, over any family of size-`k`
sets. Here `ext(D_J T)(μ)` is the biased Fourier coefficient of Bansal–Sinha up to a factor at most `(4/3)^(k/2)`.

**It is consistent with everything known, and it is weaker than the sharp bounds. Nothing here needs a loud flag.**

| Bound on level `ℓ` | Source in this review | Shape |
|---|---|---|
| Tal 2020 | as quoted by Bansal–Sinha, Theorem 10 and line 130 of the extraction | `(c d)^(ℓ/2) (log n)^((ℓ-1)/2)` |
| Sherstov–Storozhenko–Wu | as quoted by Bansal–Sinha | `C(d,ℓ)^(1/2) (c log n)^((ℓ-1)/2)` |
| Biased transfer, `fwt` | Bansal–Sinha | a factor `4^ℓ` at `|μ| ≤ 1/2` |
| This repository | `sum_abs_ext_Dl_le` | `(16 ℓ d log 4n)^(ℓ/2) + 1` |

Against Theorem 10 it loses a factor of about `(16ℓ/c)^(ℓ/2) √(log n)`. Against Sherstov–Storozhenko–Wu the loss
is larger, about `ℓ^ℓ √(log n)` up to `c^ℓ`. It is stronger than Theorem 10 only if `c > 16ℓ`, which is a matter of
an unspecified constant.

The proof is what one would expect. Along a root-to-leaf walk, the degree-`ℓ` chaos in `ξ` is a martingale whose
increment at `q` is `ξ_q` times a degree-`ℓ-1` chaos. By induction every such coefficient is at most `κ^(ℓ-1)`
except with small probability, Azuma then gives `κ^ℓ`, and a union bound over `q` and two signs costs a factor
`4n` per level. The waste is visible: each level pays `√Λ`, including level 1, which needs no logarithm. That is
exactly the extra `√(log n)`. The union bound over `n` at each level forces `Λ ~ k log n`, which is the extra `k^(k/2)`.

The exponent `d^(k/2)` cannot be improved in general: a bound `d^(k/2-ε)` fed into `advantage_le` would push the
lower bound past `N^(1-1/k)` and contradict the Aaronson–Ambainis upper bound for even `k`. So the shape in `d`
is the right one.

The blueprint's phrase "a weaker logarithm than Tal" is correct against Theorem 10.

I did not test this bound numerically. At any size I could enumerate it exceeds the trivial bound: at `d = 6`,
`n = 14`, `k = 2` it reads about 770 while the number of pairs is 91, so such a test could not fail.

## 6. Checks made

Python 3.13 with numpy 2.4.6, in the scratch folder only.

**Monomial test of (★).** Since (★) is linear in `g`, it can be tested on each monomial `χ_S` separately, which gives
many independent checks in place of one number. In `w_s` the block-0 factor is `s^(|S∩B₀|-1)`, so the `s` integral
is exactly `1/|S∩B₀|`. The blueprint's earlier check was one random `g` at `k=3, N=2`. None of the cases below repeats it.
"Max |LHS|" is the largest moment. "Max error" is the worst difference over the monomials meeting every block.
"Missing a block" is the largest moment over the other monomials, which theory says is exactly 0. "Control" drops the
factor `1/|S∩B₀|`, so it should fail wherever a moment with `|S∩B₀| ≥ 2` is nonzero.

| Case | Truncation | Grid | Monomials (meeting every block) | Max \|LHS\| | Max error | Missing a block | Control |
|---|---|---|---|---|---|---|---|
| k=3, N=3, random orthogonal H | Bansal–Sinha | Gauss–Hermite 14 | 511 (343) | 5.47e-3 | 1.3e-7 | 5.2e-9 | 4.3e-5 |
| k=3, N=3, same H | Lean | trapezoid h=0.65, 17 nodes | 511 (343) | 7.78e-3 | 4.0e-6 | 2.0e-6 | 9.7e-5 |
| k=4, N=2, Hadamard | Bansal–Sinha | Gauss–Hermite 20 | 255 (81) | 1.90e-4 | 2.1e-12 | 6.9e-15 | no signal |
| k=4, N=2, Hadamard | Lean | Gauss–Hermite 20 | 255 (81) | 3.11e-4 | 1.2e-7 | 7.3e-15 | no signal |

Reading the table:

* The identity holds to the accuracy of the quadrature in every case. The residual tracks the grid. Lean's `φ` has poles at
  `±i√2`, so Gauss–Hermite converges slowly there: at `k=3, N=3` it gave 1.1e-4 and 5.6e-5 at 12 and 14 nodes. That is why I moved
  to a trapezoid grid. Its error of 4.0e-6 stays flat from 13 to 17 nodes, so it is limited by the spacing `h`.
  The Lean row is thus good to about 5 parts in 10,000 of the largest moment, and no better.
* The control has power at `k=3, N=3`, where it fails by 20 to 300 times the residual. At `k=4, N=2` it shows nothing, because the
  moments with two block-0 indices vanish there, so those rows test the path sum but not the `s` weight.
* A second control replaced `H` by a non-orthogonal perturbation (`k=3, N=3`, Lean, 12 nodes). The moments of monomials missing a
  block jumped to 0.049, about 700 times the same figure for the orthogonal run on that grid (6.8e-5). This shows that the start step really does depend on
  orthogonality, and that the test can fail.
* `k=3, N=4` with the Walsh matrix, by scrambled Sobol sampling with `2^24` points, on 9 chosen monomials, Lean truncation. The two
  transversal triples gave 0.0022093 and 0.0022094 on both sides, differing by 2.8e-8 and 9.0e-8. The other seven have moments
  below 5e-8 in size at this precision and both sides agree to within 1.4e-8, so they are weak evidence.

**Hard distribution, sampled with fast Walsh transforms, Lean's truncation.**

| k | m | mean of Φ under p₁ | sd | (1/18)^l | fraction with Φ ≥ δ | rms Φ uniform | 1/√m |
|---|---|---|---|---|---|---|---|
| 2 | 2^20 | 0.09251 | 0.00100 | 0.05556 | 1.000 | 9.19e-4 | 9.77e-4 |
| 3 | 2^20 | 0.00858 | 0.00105 | 0.00309 | 1.000 | 1.11e-3 | 9.77e-4 |
| 4 | 2^20 | 0.00096 | 0.00097 | 0.00017 | 0.850 | 9.72e-4 | 9.77e-4 |
| 2 | 2^14 | 0.09180 | 0.00754 | 0.05556 | 1.000 | 8.56e-3 | 7.81e-3 |
| 3 | 2^14 | 0.00893 | 0.00829 | 0.00309 | 0.855 | 7.97e-3 | 7.81e-3 |

Runs: 40 samples at `2^20`, 200 at `2^14`. The mean matches `(E φ')^(2l)` with `E φ' = E Ψ = 0.30402`, so
`0.09243^l`, against the proved `(1/18)^l = 0.0556^l`. The proved constant is safe by a margin of 1.66 per block.
`E Ψ = E φ'` is itself a Stein identity. For the Bansal–Sinha truncation the same product is `1/(4π) = 0.0796`,
matching their exact formula and above their `1/32`.

## 7. Doubts and corrections

There is no mathematical doubt that I could turn into a concrete objection. The items below are the ones to fix or to
keep in view.

* **Stale in the blueprint.** §6 says the library root does not import these files. The working tree's
  `lean/QuarticQuery.lean` now imports `Results.Unconditional`, which imports `ForrelationLower.Main`.
* **Build state moved during this review.** `Results/Unconditional.olean` did not exist when I first looked and appeared at
  06:41. It applies `alphaTot_eq_four_of_bansalSinha` to `bansalSinhaLower`, so if that build is sound it confirms that the theorem
  has exactly the frozen type. The root `QuarticQuery.olean` still dates from 05:02, before these files, so a full
  build of the library root is still outstanding. The new `lean/QuarticCorpus/Unconditional/` Comparator bundle also appeared
  during the review and I did not read it.
* **Imprecise in the blueprint.** §2 says route D gives "the same threshold `d ≪ m^(1-1/k)/log m` as
  Bansal–Sinha". Theirs is `(N/log N)^(1-1/k)`, up to `k^(-28)`. With Azuma, route D is worse by `(log m)^(1/k)` and
  better in `k`. With Theorem 10 it matches them in the logarithm.
* **Minor.** §6 says 3700 lines; the eight files total 3846.
* **Reader warning.** The shadowing of `D` is harmless and confusing. A rename would help any human reviewer.
* **Weight of (★).** A kernel-checked proof with a clean one-page reading and passing numerics is strong evidence.
  It has still not been read by a specialist. A claim of improving the `k`-dependence of a published theorem should go to
  one, and the blueprint's statement that no novelty is claimed should stand until a literature search is done.

## 8. Not checked

* I did not run Lean, `#print axioms`, Comparator, or any build. That the kernel accepts the theorem
  rests on the build artefacts and on the blueprint. The brief assigned that check to the kernel.
* I did not read the pre-existing `Forrelation/Product.lean` proofs (`numerator_eq_walk`, `abs_Phi_le_one`), only
  their statements and uses.
* I did not line-check every tactic proof. I read the statements and proof structure of the eight files, and
  relied on the kernel for the steps.
* The Tal and Sherstov–Storozhenko–Wu bounds are taken as quoted in Bansal–Sinha. I did not open those papers.
  No network was used, and I did no literature search of my own on whether (★) is known. The separate note
  `docs/forrelation_route_prior_art.md` covers that and is unverified by me. It says the Azuma mechanism along a tree is
  known from Girish–Tal–Wu, which fits section 5.
* The Section 4 derivations (`k^(-2)`, and the removal of `k^(-28)`) are hand calculations, not Lean theorems.
