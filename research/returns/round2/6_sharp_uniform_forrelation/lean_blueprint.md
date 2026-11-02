**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

# Lean blueprint for the uniform Forrelation bounds

All proposed declarations below are **unelaborated**. No Lean compiler or Lake executable was available in this environment, and no new kernel, build, or Comparator result is claimed. Mathematical proofs appear here at the level of the implementation steps and in `note.md`. The machine-readable statement records additionally spell out proposed types for the paper's displays.

The supplied build-status table reports eight `ForrelationLower` modules compiled and `Uniform.lean` uncompiled. The root build receipt also has the source-pin inconsistency recorded in the supplied adjudication: the build was run on an uncommitted tree. These are supplied records, not verification performed here. The later Comparator evidence has its own pin and remains a separate evidence object.

The proposed namespace is `QuarticQuery.ForrelationLower`, with `QuarticQuery`, `QuarticQuery.Forrelation`, `MeasureTheory`, and `Finset` open. Imports should begin with `QuarticQuery.ForrelationLower.Main`; new files should not assume that uncompiled `Uniform.lean` is already available. Use a noncomputable section and classical decidability for finite sums and indicators. The code blocks are declarations to implement, not files claimed to compile as written.

## 1. Existing vocabulary and normalization

<!-- passage:bp-vocabulary -->
All names in this table are copied from the provided files.

| Mathematics | Existing declaration |
| --- | --- |
| A bit encodes the sign $+1$ at `false`, $-1$ at `true` | `QuarticQuery.ForrelationLower.sg` |
| Multi-affine extension | `QuarticQuery.ForrelationLower.ext` |
| One discrete derivative | `QuarticQuery.ForrelationLower.D` |
| Derivatives along a list | `QuarticQuery.ForrelationLower.Dl` |
| Truncation functions | `qf`, `psiS`, `phiS`, `dphi` in `QuarticQuery.ForrelationLower` |
| Hidden Gaussian coordinates | `PC l n = Fin l × n` |
| Input coordinates | `BC l n = Fin (l+1) × n` |
| Bias vector at interpolation parameter $s$ | `wv H s u` |
| Gaussian product law | `gP (PC l n)` |
| Path coefficient and coordinate list | `cf H s e j a q u`, `Lpath l p` |
| Walsh matrix | `QuarticQuery.Forrelation.H t` |
| Promise threshold | `dl k = ((2:ℝ)^(5*k))⁻¹` |
| Forrelation polynomial | `PhiF t`, equal to `QuarticQuery.Phi (l+1) t` |
| Promise and fixed error $1/3$ complexity | `QuarticQuery.P k t`, `QuarticQuery.R`, `QuarticQuery.RLe` |
| Classical algorithms | `QuarticQuery.QueryTree`, `QuarticQuery.RandomizedProgram` |

The source writes $l=k-1$. For Walsh dimensions, $\sqrt m=2^t$. Proposed declarations below can live in `QuarticQuery.ForrelationLower`, with `open MeasureTheory Finset QuarticQuery.Forrelation`.
<!-- /passage:bp-vocabulary -->

## 2. Sharp scalar kernel

<!-- passage:bp-kernel -->
### Statement

For every $x,y\in\mathbb R$,

\[
0<\psiS(x)\,dphi(y)\le\frac3{16},
\qquad \psiS(0)dphi(0)=\frac3{16}.
\]

Thus $3/16$ is the best uniform pointwise constant for these two fixed scalar functions. This does not assert that the resulting query-complexity constant is optimal.

### Complete proof

Write $q_x=\sqrt{2+x^2}$ and $q_y=\sqrt{2+y^2}$. Their squares are at least $2$, and both are positive. Therefore $(q_xq_y)^2\ge4$, so $q_xq_y\ge2$. Also $q_y^4=(2+y^2)^2\ge4$. Hence $q_xq_y^5=(q_xq_y)q_y^4\ge8$. The exact definitions give

\[
\psiS(x)dphi(y)=\frac3{2q_xq_y^5}\le\frac3{16}.
\]

Positivity follows from the positive denominator. At $x=y=0$, $q_x=q_y=\sqrt2$, so $2q_xq_y^5=2(\sqrt2)^6=16$, proving equality. This proof uses only square identities and rational inequalities; it need not formalise a separate numerical bound involving $\sqrt2$.

### Signatures, unelaborated

```lean
theorem psi_dphi_le_sharp (x y : ℝ) :
    psiS x * dphi y ≤ (3 / 16 : ℝ)

theorem psi_dphi_eq_sharp_at_zero :
    psiS 0 * dphi 0 = (3 / 16 : ℝ)
```

Dependencies: `Stein.lean:31` `qf_pos`, `Stein.lean:33` `qf_sq`, `psiS_pos`, `dphi_pos`; unfold `psiS` and `dphi`. `positivity`, `nlinarith`, `rw [div_le_iff₀ ...]`, and `field_simp` are used throughout the existing source. A useful intermediate exact statement is $2\le qf(x)qf(y)$, proved by comparing nonnegative squares.
<!-- /passage:bp-kernel -->

## 3. Interior-block bias

<!-- passage:bp-bias -->
### Statement and proof

If $0<r<l$, then

\[
|wv(H,s,u,(r,a))|\le\frac14.
\]

This is independent of $s$: on an interior block `Sf s c = 1`, `Yf` is $\phiS(V_{r-1}(a))$, and `Xf` is $\phiS(U_r(a))$. Each has absolute value at most $1/2$, by `abs_phiS_le`; their product is at most $1/4$. The existing `abs_wv_le_half` already treats both endpoints and all interior blocks with a common bound $1/2$.

### Signature, unelaborated

```lean
theorem abs_wv_le_quarter
    {n : Type} [Fintype n] [DecidableEq n] {l : ℕ}
    (H : Matrix n n ℝ) (s : ℝ) (u : PC l n → ℝ)
    (c : BC l n) (h0 : 0 < c.1.val) (hl : c.1.val < l) :
    |wv H s u c| ≤ (1 / 4 : ℝ)
```

Dependencies: `wv`, `Sf`, `Yf`, `Xf`, `abs_phiS_le`. Unlike the endpoint estimate, this signature needs no hypothesis on `s`. The distinction is useful for the coordinate-dependent restriction transfer.
<!-- /passage:bp-bias -->

## 4. Sharp path coefficient

<!-- passage:bp-coefficient -->
### Statement

If every matrix entry has absolute value at most $h\ge0$, then every path of $e$ edges satisfies

\[
|cf(H,s,e,j,a,q,u)|\le\bigl((3/16)h\bigr)^e.
\]

### Complete proof

Induct on $e$. At zero, `cf` is $1$. At the successor, its definition is one matrix entry, one scalar kernel product, and the shorter path coefficient. Taking absolute values gives the product of their absolute values. The first is bounded by $h$, the second by $3/16$, and the third by the induction hypothesis. All comparison factors are nonnegative. Multiplying gives the claimed successor power.

### Signature, unelaborated

```lean
theorem abs_cf_le_sharp
    {n : Type} [Fintype n] [DecidableEq n] {l : ℕ}
    (H : Matrix n n ℝ) (s : ℝ) {ε : ℝ}
    (hε : 0 ≤ ε) (hH : ∀ a b, |H a b| ≤ ε) (e : ℕ) :
    ∀ (j : ℕ) (a : n) (q : Fin e → n) (u : PC l n → ℝ),
      |cf H s e j a q u| ≤ ((3 / 16 : ℝ) * ε) ^ e
```

Dependencies: new `psi_dphi_le_sharp`; `cf`, `psiS_pos`, `dphi_pos`. This is a local strengthening of `Walk.lean:556` `abs_cf_le`. Reuse its induction after grouping `psiS * dphi` before applying the scalar bound. No orthogonality or bias assumption is needed here.
<!-- /passage:bp-coefficient -->

## 5. Elementary Fourier growth

<!-- passage:bp-growth -->
### Exact residual identity

For real $n>0$ and natural $k$,

\[
(2n)^k(4n)^k\exp[-2k\ln(4n)]=2^{-k}.
\]

Exponentiate the natural logarithm: $e^{2k\ln(4n)}=(4n)^{2k}$. The left side is $(2n)^k/(4n)^k=(1/2)^k$. Every denominator is positive.

### Signature, unelaborated

```lean
theorem growth_residual_eq (k : ℕ) {n : ℝ} (hn : 0 < n) :
    (n * 2) ^ k * ((4 * n) ^ k *
      Real.exp (-(2 * (k : ℝ) * Real.log (4 * n)))) =
    (1 / 2 : ℝ) ^ k
```

The old `QuarticQuery.ForrelationLower.tail_le` in `Uniform.lean` contains this exact identity inside its proof. It is worth exposing once, with the natural-number cast settled explicitly.

### Specialised growth statement

For a depth-$d$ tree, $d\ge1$, $n\ge1$, $k\ge1$, biases $|\mu_i|\le1/2$, and any family of distinct $k$-element coordinate sets,

\[
\sum_p\left|\operatorname{ext}(D_{L_p}(v\circ T))(\mu)\right|
\le\bigl(\sqrt{16kd\ln(4n)}\bigr)^k+2^{-k}.
\]

Here the lists $L_p$ have no repeated coordinates and are determined by their underlying sets; $|v|\le1$. The public tree type has Boolean leaves, and `v : Bool → ℝ` assigns two real output values. The source does not literally state a theorem for a new tree type with arbitrarily many real leaf values. The interface below exactly matches the existing type. It suffices for each deterministic constituent of a randomized acceptance function.

### Complete proof from the existing theorem

Take $\Lambda=2k\ln(4n)>0$ and $K=\sqrt{8d\Lambda}>0$. Then $K^2=2d\cdot2^2\Lambda$, exactly the hypothesis of `sum_abs_ext_Dl_le`. Its conclusion is $K^k+(2n)^k(4n)^ke^{-\Lambda}$. Substitute the residual identity and $K^2=16kd\ln(4n)$. This is a pure specialisation of the compiled parameterised theorem, with no new stopping-time argument.

### Signature, unelaborated

```lean
theorem sum_abs_ext_Dl_le_log
    {ι P : Type} [Fintype ι] [DecidableEq ι]
    [Fintype P] [DecidableEq P]
    (Lp : P → List ι) (hnd : ∀ p, (Lp p).Nodup)
    {k d : ℕ} (hk : 0 < k) (hlen : ∀ p, (Lp p).length = k)
    (hinj : Function.Injective fun p => (Lp p).toFinset)
    {μ : ι → ℝ} (hμ : ∀ a, |μ a| ≤ (1 / 2 : ℝ))
    (hd : 0 < d) (hn : 1 ≤ Fintype.card ι)
    (T : QueryTree ι) (hT : T.depth ≤ d)
    (v : Bool → ℝ) (hv : ∀ b, |v b| ≤ 1) :
    ∑ p, |ext (Dl (Lp p) (fun z => v (T.eval z))) μ| ≤
      (Real.sqrt (16 * (k : ℝ) * (d : ℝ) *
        Real.log (4 * (Fintype.card ι : ℝ)))) ^ k +
      (1 / 2 : ℝ) ^ k
```

Dependencies: `TreeGrowth.lean:738` `sum_abs_ext_Dl_le`; new `growth_residual_eq`; `Real.sq_sqrt`, `Real.sqrt_pos`, `Real.log_pos`. Keeping an ordinary natural power of a square root avoids a separate `Real.rpow` rewrite. The mathematical $k/2$ notation denotes the same quantity because its base is positive.
<!-- /passage:bp-growth -->

## 6. Sharp advantage from the existing identity

<!-- passage:bp-advantage -->
### Statement and complete proof

Replace the factor $3^l$ in `advantage_le` by $(3/16)^l$, preserving every other hypothesis. The existing `exists_identity` provides one $s\in(0,1)$, so the integral-in-$s$ version is unnecessary for this formalisation. `integral_ext_wv_zero` identifies its zero endpoint with the uniform expectation. `Int_eq_paths` expands its right side. Apply the new `abs_cf_le_sharp` to each path. The lists `Lpath l p` are duplicate-free, all have length $l+1$, and their underlying sets determine $p$, by `Lpath_nodup`, `plist_length`, and `Lpath_inj`. Therefore the sum over paths is exactly a permitted family for `sum_abs_ext_Dl_le`. The bias is bounded by $1/2$, by `abs_wv_le_half`. Integrating the resulting uniform bound over a probability measure leaves the same bound.

### Signature, unelaborated

```lean
theorem advantage_le_sharp
    {n : Type} [Fintype n] [DecidableEq n] {l : ℕ}
    (H : Matrix n n ℝ) (hl : 0 < l) (hH : RowsOrth H)
    {ε : ℝ} (hε : 0 ≤ ε) (hHb : ∀ a b, |H a b| ≤ ε)
    {Λ K : ℝ} {d : ℕ} (hd : 0 < d) (hK : 0 < K)
    (hKsq : K ^ 2 = 2 * (d : ℝ) * 2 ^ 2 * Λ)
    (hn : 1 ≤ Fintype.card (BC l n))
    (T : QueryTree (BC l n)) (hT : T.depth ≤ d)
    (v : Bool → ℝ) (hv : ∀ b, |v b| ≤ 1) :
    |(∫ u, ext (fun z => v (T.eval z)) (wv H 1 u)
        ∂(gP (PC l n))) - ext (fun z => v (T.eval z)) 0| ≤
      ((3 / 16 : ℝ) * ε) ^ l *
        (K ^ (l + 1) + (Fintype.card (BC l n) * 2) ^ (l + 1) *
          ((4 * Fintype.card (BC l n) : ℝ) ^ (l + 1) *
            Real.exp (-Λ)))
```

This can be implemented by copying the proof of `Cascade.lean:384` and replacing its one invocation of `abs_cf_le` and the matching coefficient. Neither the mean-value identity nor the Gaussian zero-endpoint proof changes.
<!-- /passage:bp-advantage -->

## 7. Coordinate-dependent restriction identity

<!-- passage:bp-restriction -->
```lean
-- Unelaborated. Namespace QuarticQuery.ForrelationLower.
theorem restriction_identity
    {ι : Type} [Fintype ι] [DecidableEq ι]
    (g : (ι → Bool) → ℝ) (μ v : ι → ℝ)
    (L : List ι) (hL : L.Nodup) :
    (∑ ρ : ι → Option Bool,
      (∏ i, match ρ i with
        | none => v i
        | some b => (1 - v i + μ i * sg b) / 2) *
      ext (Dl L (fun z => g (fun i => (ρ i).getD (z i)))) 0) =
    (L.map v).prod * ext (Dl L g) μ
```

This algebraic equality needs no positivity assumptions. Proof route: establish finite Fourier expansion by iterating `ext_affine`, or prove the polynomial identity note.md, equation (22) by expanding `ext`, interchanging finite sums, and factoring the coordinate products with `Finset.prod_univ_sum`; extract distinct-coordinate derivatives by induction on L. `D_D`, `ext_sum`, `ext_smul`, `ext_Dl` and `Dl` are the existing tools. At μ=0, `ext (Dl L g) 0` is exactly the raw uniform Fourier coefficient; no biased normalization factors appear.
<!-- /passage:bp-restriction -->

## 8. Restriction probabilities

<!-- passage:bp-weights -->
```lean
-- Unelaborated.
theorem restriction_weight_nonneg
    {ι : Type} [Fintype ι] [DecidableEq ι]
    (μ v : ι → ℝ) (hv : ∀ i, 0 ≤ v i)
    (hμ : ∀ i, |μ i| ≤ 1 - v i)
    (ρ : ι → Option Bool) :
    0 ≤ ∏ i, match ρ i with
      | none => v i
      | some b => (1 - v i + μ i * sg b) / 2

theorem sum_restriction_weight
    {ι : Type} [Fintype ι] [DecidableEq ι]
    (μ v : ι → ℝ) :
    (∑ ρ : ι → Option Bool,
      ∏ i, match ρ i with
        | none => v i
        | some b => (1 - v i + μ i * sg b) / 2) = 1
```

Prove positivity coordinatewise using `abs_le.mp`; prove normalization from the three-value sum 1 and `Finset.prod_univ_sum`. These statements parallel `bw_nonneg` and `sum_bw` in `Cube.lean`.
<!-- /passage:bp-weights -->

## 9. Restriction of a query tree

<!-- passage:bp-tree-restriction -->
```lean
-- Unelaborated. The existential form avoids adding a public definition.
theorem exists_restricted_tree {ι : Type}
    (T : QueryTree ι) (ρ : ι → Option Bool) :
    ∃ S : QueryTree ι, S.depth ≤ T.depth ∧
      ∀ z, S.eval z = T.eval (fun i => (ρ i).getD (z i))
```

Prove by induction on T. At a query, split ρ i into none, some false and some true. The none case retains the node and inductively restricts both children; the two fixed cases choose the corresponding restricted child. Existing exact constructor names are `QueryTree.leaf` and `QueryTree.query`.
<!-- /passage:bp-tree-restriction -->

## 10. Transfer of an explicit Fourier hypothesis

<!-- passage:bp-profile -->
The sharp Fourier theorem is absent from the supplied formal development. It must remain an explicit hypothesis in any result assembled before its formalization. A signature with only existing mathematical vocabulary is:

```lean
-- Unelaborated. hFourier is a genuine external obligation.
theorem sum_abs_ext_Dl_profile_le
    {ι J : Type} [Fintype ι] [DecidableEq ι]
    [Fintype J] [DecidableEq J]
    (Lp : J → List ι) (hnd : ∀ j, (Lp j).Nodup)
    {k d : ℕ} (hlen : ∀ j, (Lp j).length = k)
    (hinj : Function.Injective fun j => (Lp j).toFinset)
    (μ v : ι → ℝ) (hv : ∀ i, 0 ≤ v i)
    (hμ : ∀ i, |μ i| ≤ 1 - v i)
    {w B : ℝ} (hw : 0 < w)
    (hwprod : ∀ j, ((Lp j).map v).prod = w)
    (T : QueryTree ι) (hT : T.depth ≤ d) (val : Bool → ℝ)
    (hval : ∀ b, |val b| ≤ 1)
    (hFourier : ∀ S : QueryTree ι, S.depth ≤ d →
      (∑ j, |ext (Dl (Lp j) (fun z => val (S.eval z))) 0|) ≤ B) :
    (∑ j, |ext (Dl (Lp j) (fun z => val (T.eval z))) μ|) ≤ B / w
```

Apply Section 7 and the absolute-sum inequality, use Section 8 to average, then Section 9 and hFourier. The extra assumptions hnd, hlen, hinj serve the Fourier application; hlen and hinj are mathematically unnecessary in the purely abstract averaging implication once hFourier is granted. At the chain profile, Section 3, existing endpoint bounds and the path free-probability product in note.md, §4 give w; substitute SSW's numerical B into this theorem. Keep hFourier visible in theorem names and metadata until it has a real proof.
<!-- /passage:bp-profile -->

## 11. Conditional endpoint norm

<!-- passage:bp-endpoint-norm -->
```lean
-- Unelaborated.
theorem sum_sq_PhiF_endpoint_coeff (l t : ℕ)
    (z : BC l (Fin (mValue t)) → Bool) :
    (∑ a : Fin (mValue t),
      (D (cn 0 a)
        (PhiF t : (BC l (Fin (mValue t)) → Bool) → ℝ) z) ^ 2) =
    (mValue t : ℝ)⁻¹
```

Use `Phi_eq_PhiF` and `Forrelation.Phi_eq_matrix_product`. The first endpoint diagonal can be removed by D, leaving coefficient `(Forrelation.u t a) * y a`, with y the product of the remaining orthogonal factors applied to u. `Forrelation.isOrth_tailProd`, `Forrelation.isOrth_H`, `Forrelation.isOrth_signDiag`, `Forrelation.IsOrth.dot_self` and `Forrelation.u_dot_self` show ∑y²=1. Since u_a=2^−t, the displayed sum is 2^−2t=1/m. Alternatively prove the corresponding pointwise ℓ² recurrence for `Rs`, using `PhiF_eq_lin` and the exact Walsh row orthogonality. The already checked `ext_Rs_sq` is an averaged second moment and does not alone establish this pointwise identity.
<!-- /passage:bp-endpoint-norm -->

## 12. Rademacher exponential moment

<!-- passage:bp-linear-mgf -->
```lean
-- Unelaborated.
theorem ext_exp_linear_le
    {ι : Type} [Fintype ι] [DecidableEq ι]
    (c : ι → ℝ) (θ : ℝ) :
    ext (fun z : ι → Bool =>
      Real.exp (θ * ∑ i, c i * sg (z i))) 0 ≤
    Real.exp (θ ^ 2 / 2 * ∑ i, c i ^ 2)
```

The existing `two_point_exp_le` in `TreeGrowth.lean` already supplies the one-coordinate estimate. Factor the finite cube sum, using `Real.exp_sum`, and multiply the estimates. This avoids depending on an uncertain Mathlib Hoeffding theorem name.
<!-- /passage:bp-linear-mgf -->

## 13. Forrelation exponential moment and tail

<!-- passage:bp-forrelation-tail -->
```lean
-- Unelaborated.
theorem ext_exp_PhiF_le (l t : ℕ) (θ : ℝ) :
    ext (fun z : BC l (Fin (mValue t)) → Bool =>
      Real.exp (θ * PhiF t z)) 0 ≤
    Real.exp (θ ^ 2 / (2 * (mValue t : ℝ)))

theorem ext_PhiF_tail_le (l t : ℕ) {r : ℝ} (hr : 0 ≤ r) :
    ext (fun z : BC l (Fin (mValue t)) → Bool =>
      if r < |PhiF t z| then (1 : ℝ) else 0) 0 ≤
    2 * Real.exp (- (mValue t : ℝ) * r ^ 2 / 2)
```

Factor the cube into the first endpoint and the remaining blocks. Its linear coefficients do not depend on that endpoint, by `Rs_update_cn` and `D_lin`. Section 11 and Section 12 give the conditional MGF, then finite averaging gives the first statement. For the second, compare the indicator of Φ>r with exp(θ(Φ−r)) pointwise for θ≥0, use `ext_mono`, choose θ=mr and repeat for −Φ. Sum the two tails.
<!-- /passage:bp-forrelation-tail -->

## 14. Variable-success amplification

<!-- passage:bp-amplification -->
### Exact statement

Suppose a randomized depth-$L$ tree succeeds on every promised input with probability at least $(1+\eta)/2$, with $0<\eta\le1$. Majority of $2\tau$ independent runs has depth at most $2\tau L$, and error at most

\[
(1-\eta^2)^\tau\le e^{-\tau\eta^2}.
\]

### Complete proof

Let $r=(1-\eta)/2$. For a fixed promised input, each error indicator $W_i$ has expectation at most $r$. A majority error, with ties counted as errors, requires $\sum_i W_i\ge\tau$. If $\eta<1$, put $z=(1+\eta)/(1-\eta)>1$. Then

\[
\mathbf1_{\{\sum W_i\ge\tau\}}z^\tau
\le z^{\sum W_i},\qquad
\mathbb E z^{W_i}\le1-r+rz=1+\eta.
\]

Independence gives error at most $z^{-\tau}(1+\eta)^{2\tau}=(1-\eta^2)^\tau$. If $\eta=1$, every supported constituent is correct on the fixed promised input because all support weights are positive and the weighted success is $1$; majority is therefore correct when $\tau\ge1$. Finally $1-\eta^2\le e^{-\eta^2}$, and raising to the natural power $\tau$ proves the exponential inequality. The argument is uniform in the promised input and uses no promise on the amplified execution's off-promise behavior.

### Signatures, unelaborated

```lean
theorem exists_amplified_eta
    {ι : Type} [Fintype ι] {f : PartialBool ι}
    (A : RandomizedProgram ι) {L τ : ℕ}
    (hdepth : A.depth ≤ L) (hτ : 0 < τ)
    {η : ℝ} (hη0 : 0 < η) (hη1 : η ≤ 1)
    (hs : ∀ x b, f x = some b → (1 + η) / 2 ≤ A.success x b) :
    ∃ (J : Type) (_ : Fintype J) (q : J → ℝ) (T : J → QueryTree ι),
      (∀ j, 0 ≤ q j) ∧ ∑ j, q j = 1 ∧
      (∀ j, (T j).depth ≤ 2 * τ * L) ∧
      ∀ x b, f x = some b →
        ∑ j, q j * (if (T j).eval x = b then 0 else 1) ≤
          (1 - η ^ 2) ^ τ

theorem amplified_error_le_exp
    {η : ℝ} (hη0 : 0 ≤ η) (hη1 : η ≤ 1) (τ : ℕ) :
    (1 - η ^ 2) ^ τ ≤ Real.exp (-((τ : ℝ) * η ^ 2))
```

Dependencies: `runAll`, `eval_runAll`, `depth_runAll_le`, `maj`, `maj_wrong`, `count_ofFn`, `RandomizedProgram.weight_pos`, `.weight_sum`; copy the finite product proof of `Amplify.lean:80` with base $z$ in place of $2$. The base-$2$ proof in the source already gives exactly $(8/9)^\tau$ at error $1/3$, so the variable-success lemma is not required by the numerical elementary endpoint. Public `RLe` fixes success $2/3$; introducing an unstated `RLeEta` definition into a signature would obscure that distinction.
<!-- /passage:bp-amplification -->

## 15. Promise gap with an explicit null-tail bound

<!-- passage:bp-gap -->
Put $a=18^{-l}$, $\delta=dl(l+1)$, $p=(a-\delta)/(1-\delta)$, and $q_M=\min\{1,4/(m\delta^2)\}$. For any acceptance function $A\in[0,1]$ with error at most $\varepsilon\in[0,1]$ on the promise,

\[
\mathbb E_{\mathcal D}A-\mathbb E_{\mathcal U}A
\ge (1-\varepsilon)p-\varepsilon-q_M.
\]

### Complete proof

The existing `mass_ge` and `ext_PhiF_zero` give $\mathbb E_{\mathcal D}\Phi\ge a$. On the positive-promise event $\Phi\ge\delta$, the bound $\Phi\le1$ applies, and outside it $\Phi<\delta$. Thus $\mathbb E\Phi\le\delta+(1-\delta)\Pr(\Phi\ge\delta)$, giving positive mass at least $p$. On that event the acceptance is at least $1-\varepsilon$, and it is nonnegative elsewhere, proving hard acceptance at least $(1-\varepsilon)p$.

Under the uniform law, `ext_PhiF_sq` gives second moment $1/m$. The exceptional event $|\Phi|>\delta/2$ has mass at most $4/(m\delta^2)$ by the pointwise bound of its indicator by $4\Phi^2/\delta^2$, and at most $1$. On its complement acceptance is at most $\varepsilon$; everywhere it is at most $1$. Uniform acceptance is therefore at most $\varepsilon+q_M$. Subtract.

An implementation can avoid introducing a probability distribution for the hard law. The pointwise inequality

\[
\frac{1-\varepsilon}{1-\delta}(\Phi(z)-\delta)\le A(z)
\]

is sufficient; integrate with `ext_mono` and then the Gaussian expectation. The denominator is positive. The source's `not_RLe_of_gap` instead uses the weaker pointwise lower bound without $1/(1-\delta)$. Both are valid, and the elementary constant survives either one.

The bound above retains the requested $p,q_M$ formula. A strictly stronger bookkeeping version follows from uniform acceptance at most $\varepsilon+(1-\varepsilon)q_M$. Its gap is $(1-\varepsilon)(p-q_M)-\varepsilon$. No endpoint here relies on that extra improvement.

### Signature for the requested formula, unelaborated

```lean
theorem promise_gap_markov
    {l t : ℕ} (hl : 0 < l)
    (acc : (BC l (Fin (mValue t)) → Bool) → ℝ)
    {ε : ℝ} (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1)
    (hacc : ∀ z, 0 ≤ acc z ∧ acc z ≤ 1)
    (hyes : ∀ z, P (l + 1) t z = some true → 1 - ε ≤ acc z)
    (hno : ∀ z, P (l + 1) t z = some false → acc z ≤ ε) :
    (1 - ε) * (((1 / 18 : ℝ) ^ l - dl (l + 1)) /
      (1 - dl (l + 1))) - ε -
      min 1 (4 / ((mValue t : ℝ) * dl (l + 1) ^ 2)) ≤
    (∫ u, ext acc (wv (H t) 1 u)
      ∂(gP (PC l (Fin (mValue t))))) - ext acc 0
```

The same proof yields the interface below with any separately established bound $q$ on the null exceptional mass. This is the useful interface for the subgaussian improvement.

```lean
theorem promise_gap_of_null_tail
    {l t : ℕ} (hl : 0 < l)
    (acc : (BC l (Fin (mValue t)) → Bool) → ℝ)
    {ε q : ℝ} (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1)
    (hacc : ∀ z, 0 ≤ acc z ∧ acc z ≤ 1)
    (hyes : ∀ z, P (l + 1) t z = some true → 1 - ε ≤ acc z)
    (hno : ∀ z, P (l + 1) t z = some false → acc z ≤ ε)
    (hq : ext (fun z : BC l (Fin (mValue t)) → Bool =>
      if dl (l + 1) / 2 < |PhiF t z| then (1 : ℝ) else 0) 0 ≤ q) :
    (1 - ε) * (((1 / 18 : ℝ) ^ l - dl (l + 1)) /
      (1 - dl (l + 1))) - ε - q ≤
    (∫ u, ext acc (wv (H t) 1 u)
      ∂(gP (PC l (Fin (mValue t))))) - ext acc 0
```

Use `open Classical in` around the second declaration or make the classical decidability of the real comparison available. The source uses this pattern for real-valued indicators and masks. Dependencies: `mass_ge`, `ext_PhiF_zero`, `ext_PhiF_sq`, `Phi_eq_PhiF`, `abs_Phi_le_one`, `P_yes`, `P_no`, `ext_mono`, `ext_const`, `ext_add`, `ext_smul`, `bcf_ext`.


### Stronger bookkeeping used in the finite sharp theorem

Uniform acceptance is at most epsilon+(1-epsilon)q. Subtracting from (1-epsilon)p gives Gamma*=(1-epsilon)(p-q)-epsilon. Its excess over Gamma is epsilon*q, nonnegative for either certified probability bound. The following compound signature records the masses and both gaps. It uses no new public definition.

```lean
-- Unelaborated; no Lean compiler was run.
-- Imports: QuarticQuery.ForrelationLower.Main and QuarticQuery.Forrelation.Product.
open Classical MeasureTheory ProbabilityTheory Finset QuarticQuery QuarticQuery.Forrelation QuarticQuery.ForrelationLower
open scoped BigOperators
theorem QuarticQuery.ForrelationLower.Round2.promise_gap_compound
    {l t : ℕ} (hl : 0 < l)
    (acc : (BC l (Fin (mValue t)) → Bool) → ℝ)
    {ε : ℝ} (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1)
    (hacc : ∀ z, 0 ≤ acc z ∧ acc z ≤ 1)
    (hyes : ∀ z, P (l + 1) t z = some true → 1 - ε ≤ acc z)
    (hno : ∀ z, P (l + 1) t z = some false → acc z ≤ ε) :
    let δ := dl (l + 1)
    let a := (1 / 18 : ℝ) ^ l
    let p := (a - δ) / (1 - δ)
    let qM := min 1 (4 / ((mValue t : ℝ) * δ ^ 2))
    let qstar := min qM (2 * Real.exp (-(mValue t : ℝ) * δ ^ 2 / 8))
    let nullTail := ext (fun z : BC l (Fin (mValue t)) → Bool =>
      if δ / 2 < |PhiF t z| then (1 : ℝ) else 0) 0
    let diff := (∫ u, ext acc (wv (H t) 1 u)
      ∂(gP (PC l (Fin (mValue t))))) - ext acc 0
    (p ≤ ∫ u, ext (fun z => if δ ≤ PhiF t z then (1 : ℝ) else 0)
      (wv (H t) 1 u) ∂(gP (PC l (Fin (mValue t))))) ∧
    nullTail ≤ qM ∧ nullTail ≤ qstar ∧
    (∀ q : ℝ, q = qM ∨ q = qstar →
      (1 - ε) * (p - q) - ε ≤ diff ∧
      (1 - ε) * p - ε - q ≤ (1 - ε) * (p - q) - ε)
```
<!-- /passage:bp-gap -->

## 16. Finite elementary contradiction

<!-- passage:bp-finite-elementary -->
The existing `not_RLe_of_gap` hardcodes the coefficient $3$. It cannot prove the sharp endpoint merely by changing its parameters. A new lemma must use `advantage_le_sharp`; its expectation assembly otherwise follows the old proof.

### Signature, unelaborated

```lean
theorem not_RLe_of_gap_sharp
    {l t L τ : ℕ} (hl : 0 < l) {Λ K A q : ℝ}
    (hK : 0 < K)
    (hKsq : K ^ 2 = 2 * ((2 * τ * L + 1 : ℕ) : ℝ) * 2 ^ 2 * Λ)
    (hA : ((3 / 16 : ℝ) * ((2 : ℝ) ^ t)⁻¹) ^ l *
      (K ^ (l + 1) +
        (Fintype.card (BC l (Fin (mValue t))) * 2) ^ (l + 1) *
        ((4 * Fintype.card (BC l (Fin (mValue t))) : ℝ) ^ (l + 1) *
          Real.exp (-Λ))) ≤ A)
    (hε1 : (8 / 9 : ℝ) ^ τ ≤ 1)
    (hq : ext (fun z : BC l (Fin (mValue t)) → Bool =>
      if dl (l + 1) / 2 < |PhiF t z| then (1 : ℝ) else 0) 0 ≤ q)
    (hgap : (8 / 9 : ℝ) ^ τ + q + A <
      (1 - (8 / 9 : ℝ) ^ τ) *
        (((1 / 18 : ℝ) ^ l - dl (l + 1)) / (1 - dl (l + 1)))) :
    ¬ RLe (P (l + 1) t) L
```

Complete proof: assume `RLe`; obtain the finite amplified mixture from `exists_amplified`; define its acceptance function as in `Main.lean:78–228`; apply `promise_gap_of_null_tail`; apply the sharp advantage estimate to each tree at padded depth $2\tau L+1$; average using nonnegative weights summing to $1$. The resulting advantage is simultaneously at least the positive gap and at most $A$, contradicting `hgap`. The argument still works with the source's coarser lower bound $(1-\varepsilon)(a-\delta)$ if reducing initial implementation changes is preferred.
<!-- /passage:bp-finite-elementary -->

## 17. Elementary constants and padding

<!-- passage:bp-arithmetic -->
### Amplification and promise scales

At $\tau=25k$,

\[
\varepsilon=(8/9)^{25k}\le18^{-k}=a/18,
\qquad \delta\le a/32.
\]

The first follows by raising the exact integer inequality $18\cdot8^{25}<9^{25}$ to the power $k$. The second follows from $32\delta=32^{-(k-1)}\le18^{-(k-1)}=a$. These are `QuarticQuery.ForrelationLower.eps_le` in `Uniform.lean` and `QuarticQuery.ForrelationLower.dl_le` in `Uniform.lean`, whose source proofs are present but uncompiled.

### Uniform padding bound

For every $k\ge1$,

\[
\left(1+\frac1{50k}\right)^k\le\frac{50}{49}<\frac{81}{64}.
\]

For a proof using exact rational estimates, expand with the binomial theorem. Since $\binom kj\le k^j$, each term is at most $50^{-j}$, so the finite sum is at most the infinite geometric sum $50/49$. The existing source instead proves $1+x\le e^x$, then $e^{1/50}\le50/49$ from $e^{-1/50}\ge49/50$. Both routes are correct. The strict comparison $50/49<81/64$ is the integer inequality $3200<3969$.

The existing exact statement is:

```lean
-- Existing source, uncompiled in this attachment.
theorem padding_pow_le (l : ℕ) :
    (1 + 1 / (50 * ((l + 1 : ℕ) : ℝ))) ^ (l + 1) ≤ 50 / 49
```

### Sharp main term

Assume $L\ge1$, $g>0$, $k=l+1$, $Y=m^{1-1/k}$,

\[
L\le\frac{2Y}{18225k^2g},\qquad
K^2=16k(50kL+1)g,\qquad K\ge0.
\]

Because $50kL+1\le(50k+1)L$,

\[
K^2\le\left(1+\frac1{50k}\right)\left(\frac8{27}\right)^2Y,
\]

where the exact coefficient identity is $800(2/18225)=(8/27)^2$. Raise this to $k$, use $Y^k=m^{k-1}$, and multiply by $((3/16)/\sqrt m)^{2(k-1)}$. Since $(3/16)(8/27)=1/18$, comparison of nonnegative squares gives

\[
\left(\frac{3}{16\sqrt m}\right)^{k-1}K^k
\le\frac8{27}\sqrt{\frac{50}{49}}a
<\frac8{27}\frac98a=\frac a3.
\]

The weak bound $\le a/3$ is sufficient and convenient to formalise.

### Signature, unelaborated

```lean
theorem main_term_le_sharp
    {l t : ℕ} {L lg K : ℝ} (hL1 : 1 ≤ L) (hlg : 0 < lg)
    (hL : L ≤ (2 / 18225 : ℝ) *
      Real.rpow (mValue t : ℝ) (1 - 1 / ((l + 1 : ℕ) : ℝ)) /
      (((l + 1 : ℕ) : ℝ) ^ 2 * lg))
    (hK0 : 0 ≤ K)
    (hKsq : K ^ 2 = 16 * ((l + 1 : ℕ) : ℝ) *
      (50 * ((l + 1 : ℕ) : ℝ) * L + 1) * lg) :
    ((3 / 16 : ℝ) * ((2 : ℝ) ^ t)⁻¹) ^ l * K ^ (l + 1) ≤
      (1 / 18 : ℝ) ^ l / 3
```

Dependencies: pending `padding_pow_le`, arithmetic properties of `Real.rpow`, and the identity `mValue t = 2^(2*t)`. Copy the squared comparison strategy of `QuarticQuery.ForrelationLower.main_term_le` in `Uniform.lean`, replacing its constants. No irrational approximation is needed.

### Sharp residual

For $l\ge1$ and $t\ge2$, $2^t\ge4\ge27/8$, so $(3/16)2^{-t}\le1/18$. Also $2^{-(l+1)}\le1/4$. Hence

\[
\left((3/16)2^{-t}\right)^l2^{-(l+1)}\le a/4.
\]

### Signature, unelaborated

```lean
theorem tail_le_sharp
    {l t : ℕ} (hl : 0 < l) (ht : 2 ≤ t) :
    ((3 / 16 : ℝ) * ((2 : ℝ) ^ t)⁻¹) ^ l *
      (1 / 2 : ℝ) ^ (l + 1) ≤ (1 / 18 : ℝ) ^ l / 4
```

Pair it with `growth_residual_eq` to match the unspecialised finite-contradiction expression. The older coarse proof requires $t\ge6$; the sharper edge constant reduces this local requirement to $t\ge2$.

### Gap arithmetic

For $0\le\varepsilon\le a/18$, $0<\delta\le a/32$, $0<a\le1$, and $0\le q\le\delta$, use $p\ge a-\delta$, $p\le1$ to obtain

\[
(1-\varepsilon)p-\varepsilon-q
\ge a-2\delta-2\varepsilon
\ge\frac{119}{144}a>\frac7{12}a.
\]

If instead $q\le a/4$, the same calculation gives

\[
(1-\varepsilon)p-\varepsilon-q
\ge a-\delta-2\varepsilon-q
\ge\frac{175}{288}a>\frac7{12}a.
\]

For the old size hypothesis, `QuarticQuery.ForrelationLower.q_le` in `Uniform.lean` proves the first alternative. For the subgaussian threshold, $m\delta^2\ge24k$, so $q\le2e^{-3k}\le a/4$: indeed $\ln(8/a)=\ln8+(k-1)\ln18\le k\ln18<3k$. These estimates also prove a positive gap for depth zero, independently of any advantage bound.
<!-- /passage:bp-arithmetic -->

## 18. Elementary endpoints

<!-- passage:bp-elementary-endpoints -->
### Original numerical endpoint, unelaborated

```lean
theorem not_RLe_uniform_sharp
    {l t L : ℕ} (hl : 0 < l)
    (ht : 15 * (l + 1) + 2 ≤ 2 * t)
    (hL : (L : ℝ) ≤ (2 / 18225 : ℝ) *
      Real.rpow (mValue t : ℝ) (1 - 1 / ((l + 1 : ℕ) : ℝ)) /
      (((l + 1 : ℕ) : ℝ) ^ 2 *
        Real.log (4 * ((l + 1 : ℕ) : ℝ) * (mValue t : ℝ)))) :
    ¬ RLe (P (l + 1) t) L

theorem forrelation_lower_uniform_sharp
    (k t : ℕ) (hk : 2 ≤ k) (ht : 15 * k + 2 ≤ 2 * t) :
    (2 / 18225 : ℝ) *
      Real.rpow (mValue t : ℝ) (1 - 1 / (k : ℝ)) /
      ((k : ℝ) ^ 2 * Real.log (4 * (k : ℝ) * (mValue t : ℝ))) <
    (R (P k t) : ℝ)
```

Complete proof: handle $L=0$ by input-independent acceptance and the positive promise gap, or compile and use the source proposals `not_RLe_zero_of_yes_no`, `exists_P_yes`, and `exists_P_no`. For $L>0$, set $\tau=25(l+1)$, $\Lambda=2(l+1)\ln(4(l+1)m)$, $d=2\tau L+1$, $K=\sqrt{8d\Lambda}$. Apply the new finite contradiction theorem using main term $a/3$, residual $a/4$, and the gap arithmetic. To pass to $R$, use the compiled `RLe_R` at $L=R(P\,k\,t)$ and argue by contradiction; this is shorter than the current floor detour and gives strict $R>C$ directly.

### Strengthened-threshold endpoint, unelaborated

```lean
theorem forrelation_lower_uniform_sharp_subgaussian
    (k t : ℕ) (hk : 2 ≤ k)
    (hm : 24 * k * 32 ^ (2 * k) ≤ mValue t) :
    (2 / 18225 : ℝ) *
      Real.rpow (mValue t : ℝ) (1 - 1 / (k : ℝ)) /
      ((k : ℝ) ^ 2 * Real.log (4 * (k : ℝ) * (mValue t : ℝ))) <
    (R (P k t) : ℝ)
```

This theorem adds the null-tail lemma and $q\le a/4$ arithmetic to the same dependency chain. Its type uses only existing public vocabulary. The source does not contain the subgaussian tail or this statement.
<!-- /passage:bp-elementary-endpoints -->

## 19. Published sharp Fourier input

<!-- passage:bp-ssw-input -->
Fix an absolute constant $C\ge1$ such that every Boolean-valued decision tree $T$ of depth at most $d$ on $n$ sign variables satisfies
\[
 \sum_{|S|=j}|\widehat T(S)|
 \le C^j\sqrt{\binom dj}\,(1+\ln n)^{(j-1)/2},
 \qquad 1\le j\le n.                                        \tag{2}
\]
Such a constant exists by Sherstov, Storozhenko and Wu (2023), Corollary 4.14, printed p. 35 of arXiv:2008.10223v4. Their Corollary 4.15 allows arbitrary leaves in $[-1,1]$. The introductory Theorem 1.9 uses base-two logarithms; Corollary 4.14 already has the convention in (2). The statement leaves $C$ numerical but unspecified.

### Signature, unelaborated

```lean
-- Unelaborated; no Lean compiler was run.
-- Imports: QuarticQuery.ForrelationLower.Main and QuarticQuery.Forrelation.Product.
open Classical MeasureTheory ProbabilityTheory Finset QuarticQuery QuarticQuery.Forrelation QuarticQuery.ForrelationLower
open scoped BigOperators
theorem QuarticQuery.ForrelationLower.Round2.exists_ssw_constant :
  ∃ C : ℝ, 1 ≤ C ∧
    ∀ (ι : Type) [Fintype ι] [DecidableEq ι]
      (T : QueryTree ι) (val : Bool → ℝ), (∀ b, |val b| ≤ 1) →
      ∀ (j d : ℕ), 0 < j → T.depth ≤ d →
      (∑ S ∈ (Finset.univ : Finset ι).powersetCard j,
        |ext (Dl S.toList (fun z => val (T.eval z))) 0|) ≤
      C ^ j * Real.sqrt ((Nat.choose d j : ℕ) : ℝ) *
        Real.rpow (1 + Real.log (Fintype.card ι : ℝ)) (((j : ℝ) - 1) / 2)
```

External theorem, absent from supplied Lean. The signature is a universal proof obligation, not an axiom added to the project. Corollary 4.14 directly covers Boolean acceptance and {−1,0,1}; Corollary 4.15 implies the two-valued bounded-real encoding in this signature. QueryTree together with val:Bool→ℝ permits only two distinct leaf labels, so it does not encode Corollary 4.15 in full generality. That larger leaf vocabulary is not required for the acceptance-probability applications in this note.
<!-- /passage:bp-ssw-input -->

## 20. Exact path-profile consequence

<!-- passage:bp-path-profile -->
For the biases (10), choose $v_i=1/2$ in the endpoint blocks and $v_i=3/4$ in every intermediate block. Every path $S_p$ has the same free-probability product
$\frac14(\frac34)^{k-2}$.
Taking absolute values in (22), summing over these distinct path sets, and applying (2) to each restricted tree gives
\[
 \sum_p|\partial_{S_p}\widetilde T(w_s)|
 \le4(4/3)^{k-2}C^k\sqrt{\binom dk}
                (1+\ln(km))^{(k-1)/2}.                    \tag{23}
\]
Restrictions do not increase depth. The ambient dimension may remain $km$ even when some coordinates have been fixed; this avoids any empty-domain logarithm convention.

### Signature, unelaborated

```lean
-- Unelaborated; no Lean compiler was run.
-- Imports: QuarticQuery.ForrelationLower.Main and QuarticQuery.Forrelation.Product.
open Classical MeasureTheory ProbabilityTheory Finset QuarticQuery QuarticQuery.Forrelation QuarticQuery.ForrelationLower
open scoped BigOperators
theorem QuarticQuery.ForrelationLower.Round2.path_profile_fourier_bound
    (C : ℝ) (hC : 1 ≤ C)
    (hFourier : ∀ (ι : Type) [Fintype ι] [DecidableEq ι]
      (T : QueryTree ι) (val : Bool → ℝ), (∀ b, |val b| ≤ 1) →
      ∀ j : ℕ, 0 < j →
      (∑ S ∈ (Finset.univ : Finset ι).powersetCard j,
        |ext (Dl S.toList (fun z => val (T.eval z))) 0|) ≤
      C ^ j * Real.sqrt ((Nat.choose T.depth j : ℕ) : ℝ) *
        Real.rpow (1 + Real.log (Fintype.card ι : ℝ)) (((j : ℝ) - 1) / 2))
    {n : Type} [Fintype n] [DecidableEq n] [Nonempty n]
    {l d : ℕ} (hl : 0 < l) (H : Matrix n n ℝ)
    {s : ℝ} (hs : |s| ≤ 1) (u : PC l n → ℝ)
    (T : QueryTree (BC l n)) (hT : T.depth ≤ d)
    (val : Bool → ℝ) (hval : ∀ b, |val b| ≤ 1) :
    (∑ p : n × (Fin l → n),
      |ext (Dl (Lpath l p) (fun z => val (T.eval z))) (wv H s u)|) ≤
    4 * (4 / 3 : ℝ) ^ (l - 1) * C ^ (l + 1) *
      Real.sqrt ((Nat.choose d (l + 1) : ℕ) : ℝ) *
      Real.rpow (1 + Real.log (((l + 1 : ℕ) : ℝ) * (Fintype.card n : ℝ)))
        ((l : ℝ) / 2)

theorem QuarticQuery.ForrelationLower.Round2.path_profile_product
    {n : Type} {l : ℕ} (hl : 0 < l) (p : n × (Fin l → n)) :
    let v : BC l n → ℝ := fun c =>
      if c.1.val = 0 ∨ c.1.val = l then (1 / 2 : ℝ) else (3 / 4 : ℝ)
    ((Lpath l p).map v).prod = (1 / 4 : ℝ) * (3 / 4 : ℝ) ^ (l - 1)
```

Conditional on explicit SSW Fourier hypothesis. Lpath_nodup and Lpath_inj guarantee no multiplicity factor. New restriction-depth lemma is also needed; it is elementary recursion.
<!-- /passage:bp-path-profile -->

## 21. Sharp finite comparison and inversion

<!-- passage:bp-finite-sharp -->
Using (23) in place of Lemma 11, and the identity
$b^{k-1}4(4/3)^{k-2}=3/4^{k-1}$, gives the sharper finite comparison
\[
 \boxed{\quad
 \Gamma_*(\varepsilon,q)
 \le \frac{3C^k}{4^{k-1}}
       \sqrt{\binom{2\tau L}{k}}
       \left(\frac{1+\ln(km)}m\right)^{(k-1)/2}.
 \quad}                                                    \tag{29}
\]
This inequality includes all finite parameters, before relaxing the binomial coefficient. In particular, a positive gap forces $2\tau L\ge k$.
For any positive lower bound $\gamma\le\Gamma_*(\varepsilon,q)$, the elementary estimate
$\binom dk\le(ed/k)^k$ yields
\[
 L\ge
 \frac{k}{2e\tau C^2}
 \left(\frac{\gamma4^{k-1}}3\right)^{2/k}
 \left(\frac m{1+\ln(km)}\right)^{1-1/k}.                   \tag{30}
\]
The binomial estimate follows from $\binom dk\le d^k/k!$ and
$\ln(k!)\ge\int_1^k\ln x\,dx=k\ln k-k+1$.
Equations (28)–(30), with a freely chosen integer $\tau$ and the exact defined gap, are stronger than the simplified uniform corollaries.

### Signature, unelaborated

```lean
-- Unelaborated; no Lean compiler was run.
-- Imports: QuarticQuery.ForrelationLower.Main and QuarticQuery.Forrelation.Product.
open Classical MeasureTheory ProbabilityTheory Finset QuarticQuery QuarticQuery.Forrelation QuarticQuery.ForrelationLower
open scoped BigOperators
theorem QuarticQuery.ForrelationLower.Round2.finite_sharp
    (C : ℝ) (hC : 1 ≤ C)
    (hFourier : ∀ (ι : Type) [Fintype ι] [DecidableEq ι]
      (T : QueryTree ι) (val : Bool → ℝ), (∀ b, |val b| ≤ 1) →
      ∀ j : ℕ, 0 < j →
      (∑ S ∈ (Finset.univ : Finset ι).powersetCard j,
        |ext (Dl S.toList (fun z => val (T.eval z))) 0|) ≤
      C ^ j * Real.sqrt ((Nat.choose T.depth j : ℕ) : ℝ) *
        Real.rpow (1 + Real.log (Fintype.card ι : ℝ)) (((j : ℝ) - 1) / 2))
    (k t L τ : ℕ) (hk : 2 ≤ k) (hτ : 0 < τ)
    {η ε q : ℝ} (hη0 : 0 < η) (hη1 : η ≤ 1)
    (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) (hε : (1 - η ^ 2) ^ τ ≤ ε)
    (A : RandomizedProgram (ForrelationCoord k t)) (hdepth : A.depth ≤ L)
    (hsuccess : ∀ x b, P k t x = some b → (1 + η) / 2 ≤ A.success x b)
    (hq : ext (fun z : ForrelationCoord k t → Bool =>
      if dl k / 2 < |Phi k t z| then (1 : ℝ) else 0) 0 ≤ q) :
    let δ := dl k
    let a := (1 / 18 : ℝ) ^ (k - 1)
    let gap := (1 - ε) * ((a - δ) / (1 - δ) - q) - ε
    (gap ≤ (3 * C ^ k / (4 : ℝ) ^ (k - 1)) *
      Real.sqrt ((Nat.choose (2 * τ * L) k : ℕ) : ℝ) *
      Real.rpow ((1 + Real.log ((k : ℝ) * (mValue t : ℝ))) / (mValue t : ℝ))
        (((k : ℝ) - 1) / 2)) ∧
    (0 < gap → k ≤ 2 * τ * L) ∧
    (∀ γ : ℝ, 0 < γ → γ ≤ gap →
      ((k : ℝ) / (2 * Real.exp 1 * (τ : ℝ) * C ^ 2)) *
        Real.rpow (γ * (4 : ℝ) ^ (k - 1) / 3) (2 / (k : ℝ)) *
        Real.rpow ((mValue t : ℝ) / (1 + Real.log ((k : ℝ) * (mValue t : ℝ))))
          (1 - 1 / (k : ℝ)) ≤ (L : ℝ))

theorem QuarticQuery.ForrelationLower.Round2.profile_edge_factor
    (k : ℕ) (hk : 2 ≤ k) :
    (3 / 16 : ℝ) ^ (k - 1) * 4 * (4 / 3 : ℝ) ^ (k - 2) =
      3 / (4 : ℝ) ^ (k - 1)
```

External SSW hypothesis explicit. No asymptotic threshold is hidden. The binomial inversion is a separate arithmetic proof within this target; neither SSW nor this assembly is present as compiled source.
<!-- /passage:bp-finite-sharp -->

## 22. Sharp endpoint arithmetic

<!-- passage:bp-sharp-arithmetic -->
*Proof of Theorem 1.* Set
$\tau=\lceil5k\ln2/\eta^2\rceil$.
Then $\varepsilon_\tau\le\delta$ and
$\tau\le(5\ln2+1/2)k/\eta^2<4k/\eta^2$.
Here $k\ge2$ and $\eta\le1$ absorb the rounding by $1/2$, and
$\ln2<7/10$ follows from
$\sum_{j=0}^4(7/10)^j/j!>2$.
Since $\delta\le a/32$ and $(1-\delta)p=a-\delta$, Lemma 9 gives
\[
 \Gamma(\varepsilon_\tau,q_*)
 \ge a-2\delta-a/4\ge\frac{11a}{16}.                        \tag{32}
\]
For every $\alpha\ge2/3$,
\[
 \left(\frac{\alpha a\,4^{k-1}}3\right)^{2/k}
     =\frac4{81}\left(\frac{3\alpha}{2}\right)^{2/k}
     \ge\frac4{81}.                                        \tag{33}
\]
We may use $\alpha=11/16$, since $3\alpha/2=33/32>1$. Substitute (32)–(33) and the upper bound for $\tau$ into (30). The coefficient is
$(8eC^2)^{-1}(4/81)=1/(162eC^2)$, proving (3). ∎

### Signature, unelaborated

```lean
-- Unelaborated; no Lean compiler was run.
-- Imports: QuarticQuery.ForrelationLower.Main and QuarticQuery.Forrelation.Product.
open Classical MeasureTheory ProbabilityTheory Finset QuarticQuery QuarticQuery.Forrelation QuarticQuery.ForrelationLower
open scoped BigOperators
theorem QuarticQuery.ForrelationLower.Round2.sharp_amplification_choice
    (k : ℕ) (hk : 2 ≤ k) {η : ℝ} (hη0 : 0 < η) (hη1 : η ≤ 1) :
    let τ := Nat.ceil (5 * (k : ℝ) * Real.log 2 / η ^ 2)
    0 < τ ∧ (1 - η ^ 2) ^ τ ≤ dl k ∧ (τ : ℝ) < 4 * (k : ℝ) / η ^ 2

theorem QuarticQuery.ForrelationLower.Round2.sharp_gap_arithmetic
    {a δ ε q : ℝ} (ha0 : 0 < a) (ha1 : a ≤ 1)
    (hδ0 : 0 ≤ δ) (hδ : δ ≤ a / 32)
    (hε0 : 0 ≤ ε) (hε : ε ≤ δ) (hq : q ≤ a / 4) :
    (11 / 16 : ℝ) * a ≤ (1 - ε) * ((a - δ) / (1 - δ)) - ε - q

theorem QuarticQuery.ForrelationLower.Round2.sharp_power_arithmetic
    (k : ℕ) (hk : 2 ≤ k) {α : ℝ} (hα : (2 / 3 : ℝ) ≤ α) :
    let x := Real.rpow (α * (1 / 18 : ℝ) ^ (k - 1) * (4 : ℝ) ^ (k - 1) / 3)
      (2 / (k : ℝ))
    x = (4 / 81 : ℝ) * Real.rpow (3 * α / 2) (2 / (k : ℝ)) ∧
    (4 / 81 : ℝ) ≤ x
```

New elementary parameter assembly. The ceil rounding is uniform in k and η. Source exists_amplified covers only error1/3, so it does not discharge the general-η part.
<!-- /passage:bp-sharp-arithmetic -->

## 23. Sharp uniform endpoint with explicit Fourier hypothesis

<!-- passage:bp-sharp-endpoint -->
**Theorem 1.** Let $C$ satisfy (2). For every integer $k\ge2$, every power of two $m\ge24k\,32^{2k}$, and every $0<\eta\le1$,
\[
 R_{(1-\eta)/2}(P_{k,m})\ge
 \frac{\eta^2}{162eC^2}
 \left(\frac{m}{1+\ln(km)}\right)^{1-1/k}.                    \tag{3}
\]
The conclusion also holds under the smaller, nonintegral sufficient threshold
\[
 m\ge 8\,32^{2k}\ln\!\left(8\,18^{k-1}\right).               \tag{4}
\]
The theorem is proved below using the published estimate (2). Its full quantitative statement and the new tail argument have not been compiled in Lean.

### Signature, unelaborated

```lean
-- Unelaborated; no Lean compiler was run.
-- Imports: QuarticQuery.ForrelationLower.Main and QuarticQuery.Forrelation.Product.
open Classical MeasureTheory ProbabilityTheory Finset QuarticQuery QuarticQuery.Forrelation QuarticQuery.ForrelationLower
open scoped BigOperators
theorem QuarticQuery.ForrelationLower.Round2.sharp_uniform_of_fourier
    (C : ℝ) (hC : 1 ≤ C)
    (hFourier : ∀ (ι : Type) [Fintype ι] [DecidableEq ι]
      (T : QueryTree ι) (val : Bool → ℝ), (∀ b, |val b| ≤ 1) →
      ∀ j : ℕ, 0 < j →
      (∑ S ∈ (Finset.univ : Finset ι).powersetCard j,
        |ext (Dl S.toList (fun z => val (T.eval z))) 0|) ≤
      C ^ j * Real.sqrt ((Nat.choose T.depth j : ℕ) : ℝ) *
        Real.rpow (1 + Real.log (Fintype.card ι : ℝ)) (((j : ℝ) - 1) / 2))
    (k t : ℕ) (hk : 2 ≤ k)
    (hm : 8 * (32 : ℝ) ^ (2 * k) * Real.log (8 * (18 : ℝ) ^ (k - 1))
      ≤ (mValue t : ℝ))
    {η : ℝ} (hη0 : 0 < η) (hη1 : η ≤ 1)
    (A : RandomizedProgram (ForrelationCoord k t))
    (hsuccess : ∀ x b, P k t x = some b → (1 + η) / 2 ≤ A.success x b) :
    η ^ 2 / (162 * Real.exp 1 * C ^ 2) *
      Real.rpow ((mValue t : ℝ) /
        (1 + Real.log ((k : ℝ) * (mValue t : ℝ))))
        (1 - 1 / (k : ℝ)) ≤ (A.depth : ℝ)
```

New quantitative endpoint; SSW is explicit in hFourier. The signature states the lower bound for every successful RandomizedProgram because the supplied public vocabulary defines R only at error1/3. Its equivalence to the variable-error minimum follows by taking a minimum over such programs. The exact existing coordinate vocabulary restricts the signature to m=4^t; extending public dimensions to every power of two remains a separate model generalization.

Proof: use the tail threshold, amplification choice and gap from the preceding sections in the finite comparison. Taking gamma=11a/16 gives the power factor at least4/81, while k/(2 tau) is greater than eta²/8. The resulting constant is eta²/(162eC²). No statement that SSW has been formalized is used.
<!-- /passage:bp-sharp-endpoint -->

## 24. Formal evidence and route distinctions

<!-- passage:bp-evidence -->
1. Sharp scalar kernel and equality at zero.
2. Interior bias profile and sharp path coefficient.
3. Exact logarithmic residual identity and specialisation of the existing growth theorem.
4. Sharp advantage theorem using the existing mean-value identity.
5. Exact promise gap with a parameterised null-tail bound; instantiate Markov first.
6. Variable-success amplification, required for the η-dependent sharp Fourier theorem, optional for the elementary theorem.
7. Compile or re-prove the already-written arithmetic lemmas `dl_le`, `eps_le`, `padding_pow_le`, and the zero-query helpers from `Uniform.lean`.
8. Sharp padded main and residual bounds.
9. New finite contradiction theorem with sharp coefficient and the exact promise quotient.
10. Original numerical endpoint and strengthened-threshold endpoint.

The exact identity and the fixed-$k$ endpoint are separate evidence objects. `bansalSinhaLower` proves an eventual $Lvalue<R$ assertion for each fixed $k$; it does not state either uniform numerical endpoint. `Uniform.lean` targets the coarse numerical endpoint but is explicitly uncompiled in the snapshot. Neither status substitutes for a new compiled theorem and a new comparison challenge for the sharp endpoint.

The original Forrelation mean proof in `Promise.lean` follows a recursive finite-Jensen/tangent-bound argument. The paper note presents layer independence plus Jensen. They establish the same Walsh mean lower bound, but a correspondence record should preserve this route difference. The sharp advantage argument can use the existing mean-value identity; exporting an integral-in-$s$ identity would be an additional theorem, not a necessary prerequisite.

All nine `ForrelationLower/*.lean` files were read in full. The most relevant exact locations are `Stein.lean:22–129`, `Walk.lean:152–170,461–520,529–571`, `TreeGrowth.lean:376–599,658–807`, `Cascade.lean:256–424`, `Promise.lean:254–305,499–576`, `Amplify.lean:25–174`, `Main.lean:19–228`, and the entire uncompiled `Uniform.lean`. The first-round `note.md` and `quantitative.md` were read in full. Additional governing and context files are listed in `read_receipt.json`.
<!-- /passage:bp-evidence -->
