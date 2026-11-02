**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

# Lean correspondence and remaining formal work

This record concerns `note.md` and the supplied source at manifest pin `c7e0c9161f0ad898889bd9166e7b354acd42188d`. The mathematical proofs are in the note. This file identifies the exact boundary of the existing Lean statements and the next statements to formalize. `SOURCE_AUDIT.md` records the inspection and historical execution evidence.

**No new Lean build, kernel check or Comparator run was performed for this return.** “Existing” below means that a declaration and its proof occur in the supplied source, with historical build and dependency evidence described separately. It does not mean that the note's new formulation was compiled. Every proposed signature below is unelaborated.

## The existing endpoint

`QuarticQuery.ForrelationLower.bansalSinhaLower`, in `lean/QuarticQuery/ForrelationLower/Main.lean`, line 506, has type `QuarticQuery.BansalSinhaLower` and no mathematical premise. The definition in `Statement.lean`, lines 309–321, says that, for every fixed natural `k >= 2`, all sufficiently large `t` satisfy `Lvalue k t < R (P k t)`. Here `mValue t = 4^t`, `Lvalue` is the floor of `m^(1-1/k)/(log_2 m)^2`, and `R` fixes error at most `1/3`.

This endpoint is corpus statement `lem-2.1.i`. It uses the alternative Forrelation proof in the eight `ForrelationLower` modules. It does not provide a uniform dimension threshold, a specified universal constant, or a variable-error complexity measure. Those conclusions require new statements even when their proofs use existing intermediate lemmas.

## Displays in reading order

The table includes displays already represented in the source so that the coverage of the note is explicit. Full declaration names in the table have prefix `QuarticQuery.ForrelationLower.` unless another namespace is written. File locations are recoverable from `SOURCE_AUDIT.md` and the supplied source.

| Note display | Existing evidence and exact remaining work |
| --- | --- |
| (1), Forrelation and the promise | For `m = 4^t`, the public definitions `QuarticQuery.Phi` and `QuarticQuery.P` match corpus `eq-3` and `eq-4`; `Phi_eq_PhiF` connects the internal polynomial to the public definition. The note also allows powers of two with odd logarithm. That dimension extension is outside the frozen public family and needs a new definition or transport theorem. |
| (2), sharp Fourier estimate | External input: Sherstov–Storozhenko–Wu, Corollary 4.14. No matching theorem occurs among the supplied lower-bound declarations. Its formalization is required for (3), (26)–(29). The note's explicit natural-log version is already the form of that corollary. |
| (3), sharp uniform lower bound | New paper deduction. It requires (2), restriction transfer, variable-error amplification, and the uniform parameter assembly. The existing fixed-`k` endpoint does not certify this bound. |
| (4), numerical elementary lower bound | New paper deduction. It sharpens the edge coefficient to `3/16` and makes every parameter choice uniform in `k`. The supplied code contains the underlying elementary growth argument but no theorem with this constant or threshold. |
| (5), multilinear extension and Fourier expansion | `ext`, `bw` and `piB` give the finite product-measure extension. `hasDerivAt_ext` and `D_D` supply the calculus. The displayed equality with the full uniform Fourier expansion is not an exported declaration in these modules. A finite-sum expansion proves it. |
| (6), the algebraic truncation | The definitions `qf`, `psiS`, `phiS`, `dphi` and theorem `hasDerivAt_phiS` supply this formula. A new corpus row can refer to these existing declarations; no new analytic result is needed. |
| (7), sharp kernel bounds | `abs_phiS_le` supplies the bound on `phiS`, but the source uses the coarser separate inequalities `psiS <= 1` and `dphi <= 3`. The precise separate maxima and product bound `psiS(x) * dphi(y) <= 3/16` need new statements. |
| (8), Stein identity | `stein_one` gives the one-dimensional bounded continuously differentiable test-function identity. `stein_pi` gives its coordinate version. This step has existing source evidence. |
| (9), the Gaussian-chain biases | `Uc`, `Vc`, `Xf`, `Yf`, `Sf` and `wv` define this chain; `abs_wv_le_half` bounds all biases by `1/2`. The stronger intermediate-block bound `1/4`, used for (26), is an immediate but additional specialization of the truncation bound. |
| (10), uniform zero endpoint | `integral_ext_wv_zero` proves the same expectation identity for a row-orthogonal square matrix. The source successively reflects Gaussian coordinates; the note integrates independent transformed Gaussian coordinates. The statement agrees, with a different presentation of the proof. |
| (11), path weight | The recursive definition `cf` gives the same weight, and `Int_eq_paths` gives the path expansion. The matrix index order is `H(p_(r+1),p_r)`, as in the note. A product-notation restatement is a finite induction. |
| (12), integral identity | `exists_identity` exports a mean-value identity at one `s` in `(0,1)`. `hasDerivAt_ext_s` and `integral_walk` provide the derivative calculation used in its proof. The full integral form is new: expose the averaged derivative and apply the fundamental theorem of calculus. |
| (13), three-block example | New specialization of (12), or of its pointwise derivative identity. No named three-block formula is exported. |
| (14), biased derivatives and higher uniform levels | New displayed finite-sum identity. It follows by differentiating (5). `ext_Dl` gives a related product-measure derivative formula, not this Fourier expansion. |
| (15), general advantage estimate | `abs_cf_le` and `advantage_le` use the coarser edge constant `3`; `advantage_le` also incorporates the elementary growth estimate. The note's standalone estimate with `3/16` needs a new sharp path bound and a separate assembly statement. |
| (16), moments for arbitrary orthogonal `H` | `ext_PhiF_zero` and `ext_PhiF_sq` give the corresponding exact moments for the supplied Walsh polynomial. The note's general orthogonal-matrix statement is a genuine extension. Its path-sum proof is supplied in the note. |
| (17), hard mean for arbitrary orthogonal `H` | `mass_ge` proves the Walsh specialization. The note generalizes the matrix and factors the Gaussian-layer expectations; this generalized statement needs a new declaration. |
| (18), expected kernel lower bound | `psi_dphi_ge` and the auxiliary lemmas in `Promise.lean` supply the tangent-inequality route used by `mass_ge`. The note's displayed Jensen estimate for any pair with the indicated second moments is new and takes a different route. |
| (19), promise-gap parameters | New definitions. In particular, the source's final gap uses `a-delta`; it does not use the sharper normalized yes-mass `(a-delta)/(1-delta)` or the capped exceptional mass `min(1,4/(m delta^2))`. |
| (20), distributional promise gap | `not_RLe_of_gap` contains pointwise comparisons sufficient for its weaker gap. The exact `Gamma` inequality in the note needs its own declaration. It assumes promised correctness and does not assume that the hard law is supported on the promise. |
| (21), variable-error amplification | `exists_amplified` establishes `2 tau` repetitions and error `(8/9)^tau` from initial error `1/3`. The general `(1-eta^2)^tau` statement is new. |
| (22), logarithmic biased growth | `sum_abs_ext_Dl_le` proves the parameterized bound with `K^2 = 8 d Lambda`. Choosing `Lambda = 2j ln(4n)` gives this display, including the exact residual `2^(-j)`. That specialization is not a named source theorem. The paper additionally states real leaves in `[0,1]`; the existing argument is formulated using a Boolean tree and a bounded leaf-value map. |
| (23), maximal chaos bound | `hit_azuma` and `hit_chaos_le` implement the corresponding hitting-probability induction with repeated-query handling. The source's recursive `walk` and `hit` formulation differs from the note's stopped-martingale notation. A direct restatement requires a bridge; the note supplies its mathematical argument. |
| (24), finite elementary bound | New assembly of the sharp advantage estimate, the note's exact `Gamma`, the logarithmic growth specialization, and amplification. The existing `not_RLe_of_gap` has coarser constants and pads the amplified depth by one. |
| (25), restriction transfer | New formal input. The identity is proved by a finite monomial expansion in the note. It uses coordinate-dependent free probabilities; Wu's Lemma 2.2 supplies the cited constant-probability antecedent. No matching declaration is present here. |
| (26), sharp growth on path sets | New consequence of (2) and (25), using free probability `1/2` in endpoint blocks and `3/4` in intermediate blocks. The factor `4(4/3)^(k-2)` depends on those block-specific bias bounds. |
| (27), finite sharp bound | New consequence of the path estimate, (20), amplification and (26). It requires the external Fourier theorem, but no additional external theorem about Forrelation. |
| (28), rearranged sharp bound | New algebraic consequence of (27). Positivity of the gap first forces `2 tau L >= k`, which licenses the binomial estimate. |
| (29), uniform sharp constant | New numerical specialization. Together with the stated bound on `tau`, it proves (3). It is not an unpacking of the old existential threshold. |

The unnumbered calculation in the proof of Theorem 2 and the concluding comparison with Tal's earlier Fourier estimate are also new paper deductions. Their formal dependencies are, respectively, (24) and the earlier external Fourier theorem. The note's report on antecedent searches is bibliographic evidence, not a Lean proposition.

## Additional displays in the quantitative record

Most numbered displays in `quantitative.md` repeat the note and should reuse its statement records. The additional gaps and specializations, in that document's reading order, are as follows.

| Quantitative display or passage | Formal status and remaining work |
| --- | --- |
| Initial parameter, truncation, moment and Jensen displays | Restatements of note (1), (6)–(7), and (16)–(18), with the same dimension and general-matrix boundaries. No fresh formal support is created by repeating them. |
| (F1)–(F5) | Reuse note (19)–(22) and (24). The logarithmic growth specialization, variable-error amplification and sharper `Gamma` remain new. |
| (F6), exact elementary inversion | Additional positive-real arithmetic, recorded as `new-finite-elementary-inversion`. Positivity of the excess gap, the edge constant, the dimension and the logarithmic factor are required before taking real powers. This statement is not exported in the current source. |
| (F7)–(F10) | Reuse note (2), (25), (27), and (28). The intervening endpoint/interior free-probability product and coefficient simplification are finite calculations supporting (26)–(27); their use still depends on the new restriction transfer. |
| (E1) and its unnumbered estimates | Reuse note (4) and the elementary parameter proof. `new-elementary-arithmetic` now includes the candidate budget and small-depth hypothesis, the `K^2` bound, main and residual advantage terms, their sum, and the strict numerical gap. This is a proposed arithmetic statement, still awaiting elaboration and proof. |
| (S1) and (S2) | (S1) repeats note (3); (S2) sets `eta = 1/3`, giving the explicit coefficient `1/(1458eC^2)`. `new-eq-03` supplies the exact `C`-dependent proposed endpoint with its Fourier premise expanded, and `new-sharp-third-corollary` supplies (S2). Both specialize to `m = 4^t`. `new-sharp-public-existential` separately records the compact existential-constant consequence. None of these endpoints has been compiled. |
| Tal growth and its uniform endpoint | Two additional records: `new-tal-fourier-input` is a published external theorem, while `new-tal-consequence` is the new deduction with coefficient `eta^2/(162kC_T^2)`. The Tal premise, restriction transfer and amplification must all be formalized or supplied. This consequence is distinct from both the elementary and SSW endpoints. |
| (M1) and the intervening martingale displays | (M1) is the same crossing estimate as note (23). Detailed proposed records now cover the raw derivative formula (`new-growth-raw-formula`), chaos definition and increment (`new-growth-chaos-increment`), general centered exponential inequality (`new-growth-hoeffding`), union-bound arithmetic (`new-growth-union-arithmetic`), terminal queried-set identity (`new-growth-leaf-formula`), and parameterized growth (`new-growth-parameterized`). Several bundle existing declarations or expose a calculation inside an existing proof. The general probability-space exponential statement and standalone bridges still require formal proofs. The filtration presentation and arbitrary real-leaf formulation retain the scope qualifications described above. |
| Coarse endpoint and its parameter displays | The endpoint is `new-forrelation-uniform-coarse`. `new-coarse-arithmetic` gives the padded-depth estimate, its uniform inflation bound, the main and residual terms, and the weaker source gap. `new-padding-binomial` additionally states the finite binomial and geometric-sum calculation behind that inflation bound. These are new finite arithmetic statements whose proof uses the exact depth `50kL+1`; they have not been compiled. The zero-depth case must also be included in the final assembly. |

The proposed registry signatures were inspected for names, types and hypotheses against the supplied source. In particular, `QuarticQuery.Forrelation.H` is the normalized Walsh matrix, `sg false = 1` fixes the restriction probabilities' sign convention, and the inline general-matrix polynomial uses the same path orientation as `wv`. This was a source-level fidelity review, with no Lean elaboration.

## Recommended next endpoint using the existing constants

The lowest-dependency next uniform result retains the source's edge constant `3`. Its universal constant is `1/2332800`, with the same explicit dimension threshold. It uses only the present public statement vocabulary:

```lean
-- Proposed statement only; not elaborated or compiled.
theorem QuarticQuery.forrelation_lower_uniform_existing_constants
    (k t : ℕ) (hk : 2 ≤ k) (ht : 15 * k + 2 ≤ 2 * t) :
    (1 / 2332800 : ℝ) *
        Real.rpow (QuarticQuery.mValue t : ℝ) (1 - 1 / (k : ℝ)) /
        ((k : ℝ) ^ 2 *
          Real.log (4 * (k : ℝ) * (QuarticQuery.mValue t : ℝ))) <
      (QuarticQuery.R (QuarticQuery.P k t) : ℝ)
```

Use `not_RLe_of_gap`, `advantage_le`, `sum_abs_ext_Dl_le`, `mass_ge`, `ext_PhiF_sq`, `exists_amplified`, and `QuarticQuery.lt_R_of_not_RLe`. The remaining work is finite arithmetic, the logarithmic specialization, and the zero-query case. The signature uses no new definition of query complexity.

Set `tau = 25k`. For a positive candidate query budget `L`, the existing promise lemma uses depth `50kL+1`. Bound this by `50kL(1+1/(50k))`; the resulting factor after the `k/2` power is less than `9/8`, uniformly in `k`. The coarser replacement `51kL` introduces an unnecessary factor growing with `k`. With the proposed constant, the main advantage term is at most `a/48`, the residual at most `a/4`, and the existing promise gap is at least `119a/144`, where `a = 18^(-(k-1))`. These estimates leave strict room for the contradiction. The proof for depth zero follows from existence of both promise outputs; it should precede application of a positive-depth growth lemma.

After this endpoint, formalize the sharp kernel product and repeat the explicit assembly to reach the constant `2/18225` in note (4). The mathematical derivation and the distinction between exact amplified depth and the source's padded depth are given in `quantitative.md`.

## Sharp public-vocabulary endpoint

The public definition `R` fixes error `1/3`. A variable-error statement should quantify over a randomized program and its success directly, or introduce a new error-parameter definition explicitly. The following proposed statement avoids changing the public vocabulary:

```lean
-- Proposed statement only; not elaborated or compiled.
-- Requires formalizing SSW Fourier growth and the restriction transfer.
theorem QuarticQuery.forrelation_lower_uniform_sharp :
    ∃ c : ℝ, 0 < c ∧
      ∀ (k t : ℕ), 2 ≤ k → 15 * k + 2 ≤ 2 * t →
      ∀ η : ℝ, 0 < η → η ≤ 1 →
      ∀ A : QuarticQuery.RandomizedProgram
          (QuarticQuery.ForrelationCoord k t),
        (∀ x b, QuarticQuery.P k t x = some b →
          (1 + η) / 2 ≤ A.success x b) →
        c * η ^ 2 *
          Real.rpow
            ((QuarticQuery.mValue t : ℝ) /
              (1 + Real.log
                ((k : ℝ) * (QuarticQuery.mValue t : ℝ))))
            (1 - 1 / (k : ℝ)) ≤ (A.depth : ℝ)
```

The constant is independent of `k`, `t`, `η`, and `A`. This compact signature is recorded as `new-sharp-public-existential`. The note supplies `c = 1/(162eC^2)` for an absolute Fourier-growth constant `C`; `new-eq-03` separately preserves that exact coefficient in a proposed theorem conditional on the fully expanded Fourier premise. `new-sharp-third-corollary` preserves the exact error-`1/3` coefficient. The existing source proves none of these new endpoints. A formalization must first provide the SSW theorem, the coordinate-dependent restriction identity, and variable-error amplification, then assemble (27)–(29).

## How to record the next checks

Add the new statements without changing `lem-2.1.i`; its old quantifiers and public definitions remain intact. The incorrect locator for that old record is a separate metadata repair described in `SOURCE_AUDIT.md`. Preserve the distinction between a matching statement, agreement of proof routes, and dependency reachability.

When the specified Lean toolchain and dependencies are available, elaborate the proposed signatures, prove the new declarations, inspect their axioms and dependency closure, and run the relevant independent Comparator challenge. Record actual commands, outputs and source pins. Until those executions exist, these additions remain proposed statements with paper proofs.
