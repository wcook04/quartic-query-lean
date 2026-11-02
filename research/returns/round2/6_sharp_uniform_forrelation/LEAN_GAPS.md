# Exact scope of the remaining Lean work

No new declaration in this ZIP was elaborated or compiled. No new build, Comparator, independent-kernel, or human-review result is claimed. The proposed signatures are implementation targets over the supplied vocabulary. Every external Fourier hypothesis remains visible.

The supplied public model has block size \(m=4^t\), fixed error \(1/3\) in `R` and `RLe`, and Boolean leaves in `QueryTree`. The paper permits every power-of-two block size and variable error. A signature about each `RandomizedProgram` with success at least \((1+\eta)/2\) expresses the variable-error lower bound without inventing a new complexity definition. A signature using `val : Bool → ℝ` allows two real leaf values; it is not a representation of a tree with arbitrarily many distinct real leaf labels.

## 1. Supplied evidence, independently of the new work

`BUILD_STATUS.md` reports up-to-date compiled objects for `Cube`, `Stein`, `Walk`, `TreeGrowth`, `Cascade`, `Promise`, `Amplify`, and `Main`. It explicitly reports `Uniform.lean` and the new `Paper/Section2/3/4.lean` modules uncompiled. Reading their proofs does not promote that status.

The supplied adjudication also records that the root build receipt names commit `16adedc16acca1e3a8d2963d4fd5655dcd0492d7`, while some listed lower-bound files were still uncommitted at that build. A clean pinned build is therefore needed to repair that receipt. The later Comparator record is a separate piece of evidence with a later source pin. This ZIP does not edit or regenerate historical receipts.

`QuarticQuery.ForrelationLower.bansalSinhaLower` is the supplied eventual fixed-\(k\) lower bound. Its statement does not imply either new uniform numerical theorem. Likewise, the source declaration for the coarse constant \(1/2332800\) is in the uncompiled module; it is not evidence that the sharp constant \(2/18225\) has been compiled.

## 2. Reading-order map for note.md

Each row includes the unnumbered displayed steps in the named passages. Records in `NEW_STATEMENTS.json` use the prefix `r2-sharp-` followed by the passage name; `correspondence.json` gives the authoritative associations.

| Passage and displays | Existing support | Exact outstanding work |
|---|---|---|
| definition, (1) | Corpus `eq-3`, `eq-4`; `Phi`, `P`, `Phi_eq_PhiF` | The existing formal domain is \(m=4^t\). All powers of two and variable-error notation are a broader paper model. Definitions alone do not certify any new bound. |
| ssw-input, (2) | Published SSW Corollaries 4.14–4.15, PDF p. 35 | No supplied formalization of this theorem. The universal \(C\) is not assigned a numerical value. Prove the Boolean version first, or retain the exact `hFourier` assumption. |
| sharp-result and scope, (3), (4), (6) | The old fixed-\(k\) theorem is weaker | New amplification, restriction transfer, exponential tail, binomial inversion, and constant arithmetic. The program-by-program target specializes the paper to \(m=4^t\). The total-input-length substitution is elementary algebra, not a new complexity claim. |
| elementary-result, (5) | Existing coarse growth and interpolation machinery | New \(3/16\) edge bound and quantitative assembly. Both the old and improved dimension thresholds are uncompiled. No SSW assumption is needed for this theorem. |
| extension, (7), and derivative cancellation | `ext`, `D`, `Dl`, `D_D` | Export the Fourier expansion and the uniform coefficient/raw derivative bridge as exact finite identities. |
| kernel, (8), and the scalar formulas | `psiS`, `phiS`, `dphi`, `hasDerivAt_phiS`, `abs_phiS_le` | The pointwise product bound \(3/16\) and equality at zero are new. Existing separate upper bounds \(1\) and \(3\) are too coarse. |
| stein, (9) | `stein_one` | Existing statement supplies this step for bounded continuously differentiable test functions with bounded continuous derivative. Confirm the exact instantiated hypotheses in the new assembly. |
| chain, (10) | `wv`, `abs_wv_le_half` | Interior coordinates have the stronger \(1/4\) bound, which needs a new small lemma. Matrix orientation is \(H_{\text{next},\text{current}}\). |
| zero-endpoint, (11) | `integral_ext_wv_zero` | Existing orthogonal-chain statement supplies the endpoint. Preserve its orthogonality and positive-chain-length assumptions. |
| path-identity and worked-chain, (12)–(14) | `integral_walk`, `exists_identity`, `Int_eq_paths`, distinctness of `Lpath` | The source exports a mean-value statement. The paper's integral-in-\(s\) identity is a stronger presentation and requires its own regularity and interchange proof if formalized literally. The quantitative endpoints can use the already available mean-value route. The \(k=3\) expansion and derivative/Fourier identity are new wrappers. |
| advantage, (15) | Existing `advantage_le` | Replace the coarse coefficient through a new `abs_cf_le_sharp`; the current finite theorem hardcodes \(3\). Changing only parameters cannot give the sharp constant. |
| moments, (16)–(17) | Walsh `mass_ge`, `ext_PhiF_zero`, `ext_PhiF_sq`, norm bounds | General orthogonal \(H\) is broader than the Walsh moment statements. The paper's Jensen proof differs from the source tangent-exponential proof. Standard normal marginals, including centering, are needed in the Gaussian edge lemma. |
| subgaussian, (18)–(19) | Orthogonal product identities; one-coordinate exponential estimate | Pointwise conditional endpoint norm, finite-product moment-generating bound, exponential Markov, and two-sided tail are new. A global second moment alone does not imply this tail. |
| gap, (20)–(21) | `mass_ge`, second-moment and promise interfaces | Exact denominator \(1-\delta\), arbitrary null-tail bound, minimum with the exponential tail, and the stronger gap \(\Gamma_*=(1-\varepsilon)(p-q)-\varepsilon\) are new. The symbols \(p,q\) are probability bounds, not exact masses. |
| restriction, (22) | Cube finite-sum algebra | Coordinate-dependent free probabilities, probability normalization, depth preservation of a restricted tree, and the raw-derivative identity are new. The algebraic identity also holds at \(v_i=0\); division requires a positive product. |
| path-restriction, (23) | Path distinctness and endpoint \(1/2\) bias | Interior \(1/4\) bias and the profile product \(\tfrac14(3/4)^{k-2}\) are new. SSW must be explicit as a hypothesis until proved. No path multiplicity factor is allowed. |
| growth and growth-proof, (24)–(26), terminal estimate | `sum_abs_ext_Dl_le`, `ext_Dl`, `hit_chaos_le`, `abs_ext_tree_chaos_le` | The specialized choice \(\Lambda=2j\ln(4n)\), exact \(2^{-j}\) residual, and displayed wrapper are uncompiled. The stopped-process proof is represented by the existing parameterized machinery; conditioning on a favorable future event is not a substitute. |
| amplification, (27) | `exists_amplified` at error \(1/3\), `runAll`, majority lemmas | General \(\eta\), tie-as-error handling, the endpoint \(\eta=1\), and the bound \((1-\eta^2)^\tau\) are new. No undefined `RLeEta` is used. |
| finite-elementary, (28) | Coarse finite contradiction | New sharp coefficient and exact gap. Handle zero depth separately. The paper can use unpadded depth; the source-compatible endpoint proof deliberately retains \(2\tau L+1\). |
| finite-sharp, (29)–(30) | No supplied sharp Fourier assembly | New restricted derivative estimate, binomial inversion, positivity checks, and all constant factors. The exact success hypothesis and integer depth must remain visible. |
| threshold, (31) | Elementary arithmetic only | Exponential-tail threshold, \(\ln 18<3\), and comparison with \(2^{15k+2}\). The logarithmic threshold (4) is slightly stronger than the simpler integer condition. Neither is claimed necessary. |
| sharp-proof, (32)–(33) | Existing scalar inequalities may be reused | Ceiling arithmetic for \(\tau\), positive gap, cancellation of \(k\), and \(1/(162eC^2)\) assembly are new. |
| elementary-proof and original-constant, (34)–(37) | Uncompiled arithmetic in `Uniform.lean` | Prove or compile amplification scale, padding, sharp main and residual terms, then the new contradiction theorem. The margin is \(7a/288\) under the new threshold. The factor \(256\) compares numerical constants only. |
| finite-range, (38) | Algebra from the exact gap | Prove the Markov positivity equivalence with all denominators positive. It is an obstruction to this probability comparison, not a lower bound on the dimensions required by every possible argument. |
| small-dimension | Definitions, \(m=1\) lies in \(4^t\) | Empty-zero-promise examples need their own finite wrappers. The \(m=2\) example lies outside the current \(4^t\) public family. |
| comparison | External theorems and the new derived endpoint | Keep published Rorrelation applications separate from a Fourier theorem applied to Walsh Forrelation. The Tal-derived \(1/k\) endpoint has its own missing assembly. The logarithmic loss is not proved optimal for the promise problem. |
| bs-failure and bs-repair, (39)–(40) | Exact supplied TeX and algebraic audit | The surplus logarithmic exponent is a finite algebra statement. The corrected multi-level summation and its translation from BS's external estimates are new. The replacement proof establishes the stated large-dimension range; it is not a theorem covering every pair \((k,m)\). |

## 3. Companion audit and blueprint

The audit's (B1)–(B3) and (B6)–(B8) are the exponent calculation and a finite geometric-series argument. Its (B4)–(B5) describe an asymptotic counterexample to an inequality between upper-bound expressions; there is no formalized asymptotic counterexample yet. Its (B9) additionally imports BS's earlier indistinguishability and promise estimates. A formal finite-sum lemma alone does not certify all those imports.

The audit's (B10) promise estimate is a correction of the reciprocal typo in the source. Its replacement-argument displays (B11)–(B30), including the unnumbered intermediate steps, reuse the kernel, restriction, finite comparison, amplification, endpoint, and null-tail targets above. The correspondence records map them to the same statement objects; repeated exposition is not additional kernel evidence.

The blueprint contains narrower implementation lemmas in addition to the compound paper statements. Every proposed code block remains unelaborated, including restriction depth preservation, finite-sum weight normalization, the linear Rademacher MGF, the sharp path coefficient, and the padded finite contradiction theorem. Existing declaration names are full source names where listed in correspondence. Proposed theorem names are recorded separately and are never represented as existing Lean evidence.

## 4. Suggested implementation order

1. Compile the local sharp kernel and interior-bias lemmas; derive the path coefficient.
2. Expose the logarithmic specialization of the existing growth theorem and a sharp advantage theorem.
3. Prove the finite restriction identity, weight facts, and restricted-tree depth lemma.
4. Prove the conditional endpoint norm, exponential moment, and null-tail bound.
5. Prove the exact promise-gap interface and general-\(\eta\) amplification.
6. Compile the padded elementary arithmetic and sharp finite contradiction. Use `RLe_R` directly to obtain the strict lower bound, avoiding a floor detour.
7. Assemble the Fourier-dependent finite and uniform theorems with `hFourier` explicit. Formalizing SSW itself is a separate substantial task.
8. Add the dimension-general model only after the existing \(4^t\) statements compile. Record a fresh build at a clean pin and exact comparison challenges for the new endpoints.

The exact-arithmetic script checks identities, rational inequalities, and finite examples. Its successful execution does not discharge any analytic or Lean obligation above.
