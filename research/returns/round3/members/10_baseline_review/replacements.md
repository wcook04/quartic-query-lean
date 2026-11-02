# Located replacements and structural moves

All changes are proposed against the exact frozen members. Apply local replacements before moving passages. The original packet has not been edited.

## R-E01 — current-evidence correction

**Priority:** P0. **Owner:** 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage ROOT-EVIDENCE-CONVENTION, lines 142–142.

The old global commit sentence is false as a description of the current packet. Distinguish packet assembly, proof-source checkpoint and baseline history. Source hash matching is the binding evidence; commit labels alone are insufficient.

<a id="repair-R-E01"></a>
<!-- passage:repair-R-E01 -->

The baseline was written against repository commit `c7e0c9161f0ad898889bd9166e7b354acd42188d`; its historical catalogue and original evidence fields retain that provenance. The frozen review packet is at repository commit `1dd469dd0042b937b739da3bc211eeb60bdf7462`. Its current source-bound Lean and Comparator receipts identify proof-source checkpoint `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`, and their recorded local input hashes match the supplied files. The current root build, selected module runs, 258-declaration type/axiom audit, and Comparator comparisons are separate evidence records. The comparisons certify their listed declarations against the actual generated challenges; they do not independently establish the intended meaning of shared definitions. No Lean or Comparator execution was performed during this review. The versioned current concordance records exact declaration types, ordinary premises, remaining partial clauses, proof routes, and per-declaration build, comparison, and dependency status.

<!-- /passage:repair-R-E01 -->

## R-E02 — current-evidence correction

**Priority:** P0. **Owner:** 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage ROOT-RESULT, lines 46–46.

Current wrappers directly close the literal equation(2) type gap while preserving exact comparator membership and route reach.

<a id="repair-R-E02"></a>
<!-- passage:repair-R-E02 -->

**Evidence.** `QuarticQuery.alphaTot_eq_four_unconditional`, `theorem_1_1_unconditional`, and `cubic_bound_fails_unconditional` are unconditional declarations in `Results/Unconditional.lean`. The full headline theorem gives the same circuit in both complexity bounds and states the randomized bound using the integer floor `Gvalue`; `Gvalue_ge` gives the coefficient $1/400$ in equation (2). The current `Paper.construction_family_named` and `Paper.construction_equation_two` also export that literal fixed-$k$ family with $b_k=6$. The supplied source-bound root build covers these declarations; the Unconditional Comparator receipt compares the headline declarations listed in it. The two Paper wrappers have no Comparator receipt. These are reported executions with hashes checked against the frozen source, not new executions during this review. The headline proof uses the imported quartic upper-bound route. Appendix A also has a separate current formal assembly, described at its endpoint.

<!-- /passage:repair-R-E02 -->

## R01 — mathematical source attribution

**Priority:** P0. **Owner:** 03 Forrelation lower bound; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage forr_bs_translation, lines 392–407.

The inspected v3 level sum loses an unbounded logarithmic factor. Preserve theorem credit, distinguish the defective display, and retain the independent local endpoint.

<a id="repair-R01"></a>
<!-- passage:repair-R01 -->

### 3.6. The published statement and the lower-bound scale needed here

Bansal and Sinha state a randomized lower bound of
\(c k^{-29}(m/\log(km))^{1-1/k}\), for an absolute \(c>0\), for error at most \(1/3\) on the same \((2^{-5k},k)\)-Forrelation promise [BS21, arXiv:2008.07003v3, Theorem 1.3 and Corollary 1.4, p. 4]. Their \(N\) is our block length \(m\), not the total input length \(km\). The normalized product and both promise thresholds agree. Theorem 1.3 parameterizes error as \(1/2-\eta/2\); here \(\eta=1/3\). A fixed change of logarithm base is absorbed into \(c\).

The numerical implication used by the OpenAI preprint is straightforward. Fix \(k\ge2\), put \(\alpha=1-1/k\), and use base-two logarithms. For \(m\ge k\), \(\log_2(km)\le2\log_2m\). Dividing the stated lower-bound scale by the unfloored definition of \(L\) gives at least
\(c k^{-29}2^{-\alpha}(\log_2m)^{2-\alpha}\), which tends to infinity because \(2-\alpha=1+1/k>0\). Thus, for every \(c>0\) and fixed \(k\), all sufficiently large powers of four satisfy

<!-- claim:claim-bs-to-L -->
\[
c k^{-29}\left(\frac{m}{\log_2(km)}\right)^{1-1/k}
>\frac{m^{1-1/k}}{(\log_2m)^2}
\ge\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor=L.
\]

The stated theorem and the inspected derivation need separate records. In v3 §5.4, p. 38, the step between `main.tex` lines 1180–1181 replaces the logarithmic exponent \((\ell-1)/2\) by \(\ell(1-1/k)/2\) at levels \(k\le\ell\le k(k-1)\). The ratio is \(\log(km)^{(\ell/k-1)/2}\). It grows with \(m\) for every fixed \(\ell>k\); already \(k=3,\ell=6\) leaves a factor \(\sqrt{\log(3m)}\). The supplied source audit therefore does not establish that displayed implication. This finding concerns that proof step and does not refute Theorem 1.3. The ensuing depth threshold is on line 1184. Equation (5.31) also prints \(\delta^2/(4m)\) where the preceding second-moment estimate gives \(4/(m\delta^2)\); that separate correction affects the sufficient size threshold.

The separation needs only the weaker fixed-\(k\) statement \(R(P)>L\). Sections 3.7–3.15 prove it independently by the local interpolation and decision-tree argument. Even a lower-bound scale \(m^{1-1/k}/\log(km)\) would exceed \(L\) eventually, since its ratio to the unfloored \(L\) grows as \(\log m\). No claim about the exact logarithmic exponent of the published theorem is needed for that internal proof.

**Source correspondence.** The current snapshot contains the numerical comparison itself in `QuarticQuery.Paper.construction_claim_bs_to_L`; `QuarticQuery.Paper.construction_bs_comparison_chain` also states the unfloored middle inequality. Their premises are \(k\ge2\) and \(c>0\), and neither asserts a randomized lower bound. By contrast, `QuarticQuery.ForrelationLower.bansalSinhaLower` proves the eventual endpoint \(L<R(P)\) by the separate local route. A receipt for the latter endpoint cannot certify the sharp published expression; a receipt for the former arithmetic statement cannot certify the source theorem either. Current source-bound validation is recorded in the evidence appendix.

<!-- /passage:repair-R01 -->

## R02 — mathematical source attribution

**Priority:** P0. **Owner:** 03 Forrelation lower bound; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage forr_attribution, lines 822–822.

Remove the unqualified proof attribution without changing the historical ancestry or claiming novelty.

<a id="repair-R02"></a>
<!-- passage:repair-R02 -->

The problem, its alternating Walsh expression, and its small-query quantum algorithm are established Forrelation constructions [AA18]. Bansal and Sinha state a quantitatively stronger randomized lower bound, with explicit dependence on the error advantage and on \(k\), for the same small threshold [BS21, arXiv:2008.07003v3, Theorem 1.3 and Corollary 1.4, p. 4]. Section 3.6 records both its numerical implication for our target scale and the unresolved logarithmic comparison in the inspected v3 proof. The independent fixed-\(k\) proof given here establishes the weaker endpoint required by the total-function construction; it does not resolve that sharper source statement.

<!-- /passage:repair-R02 -->

## R03 — current-evidence correction

**Priority:** P0. **Owner:** 01 models/evidence; 03 Forrelation lower; 09 backend.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage forr_scope, lines 156–156.

Replace the false current-packet absence claim; make the source statement/proof boundary visible at the interface.

<a id="repair-R03"></a>
<!-- passage:repair-R03 -->

The three conclusions are a randomized lower bound, a quantum promise algorithm, and an exact Boolean circuit recognizing the promise and its value. The preprint invokes Bansal and Sinha for the first conclusion; §3.6 distinguishes the published statement from the inspected display boundary. The supplied Lean source proves the required weaker endpoint by its own Gaussian and decision-tree argument, reconstructed in full below. The historical baseline did not contain source-bound receipts. The current frozen packet does: their input hashes match the supplied files, and the versioned evidence appendix identifies each declaration's actual build, comparison and type-audit scope. No new Lean or Comparator execution was performed during this review.

<!-- /passage:repair-R03 -->

## R-E03 — current-evidence correction

**Priority:** P1. **Owner:** 05 quantum upper; 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage upper-tournament-evidence, lines 1318–1322.

An actual normalized list law and a separate literal tensor theorem now exist. The old only-Boolean limitation is stale; keep the implementation-state distinction.

<a id="repair-R-E03"></a>
<!-- passage:repair-R-E03 -->

**Lean evidence for Proposition 3.2.** The older `Upper.stageLaw_some`, `sum_stageLaw_some`, and `stage_samples` implement the correct weights through a sampler that may skip later comparisons after a failure. That sampler preserves the success law without claiming equality of its complete workspace to equation (15). The current `Paper.equation_15` separately proves the literal tensor-state slice equality for supplied coherent comparison circuits.

The current `Paper.quantumTournament_list` returns a finite list-valued probability law, proves that it is normalized, supplies both a coherent `Samples` witness and a physical bit-query `Runs` witness, and proves containment of any specified dominant vertex with probability at least $1-2m/2^T-T\varepsilon$. `Paper.quantumTournament` packages the physical cap $6072c\sqrt m\,T^2\ln T$ in the source's common logical-read convention. Thus the current source includes the list-valued proposition itself. These declarations belong to the source-bound root build and recorded type audit, but are outside the two headline dependency roots and have no Comparator receipt.

The original `Upper.tournament_runs` remains the Boolean continuation used by the main proof: it verifies candidates and has an additional verifier error $\varepsilon$. The next induction explains that original route. Its narrower output type does not limit the separately exported current list theorem. Padding stage costs and the compiler's factor of two preserve the stated asymptotic cap.

<!-- /passage:repair-R-E03 -->

## R-E04 — current-evidence correction

**Priority:** P1. **Owner:** 06 direct product; 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage CL-supermartingale, lines 1608–1608.

New finite conditional theorems remove the no-declaration claim, but do not license marking every supermartingale narrative clause exact.

<a id="repair-R-E04"></a>
<!-- passage:repair-R-E04 -->

The current `Paper.classical_transcript_conditional_expectation` proves the finite positive-mass one-step product inequality, and `Paper.classical_final_bound` proves the terminal bound. `Paper.classical_transcript_product_law` and `Paper.classical_eq_16_transcript` supply the conditional factorization and one-step value estimate. Their premises require nonnegative finite product weights, a positive-mass conditioning transcript, and remaining budget for the proposed query. These are the finite conditional formulations used here; they are not a general measure-theoretic supermartingale theorem. The current corpus retains partial labels for equation (16) and the full supermartingale row. The original endpoint is also proved by the following unnormalized-weight route.

<!-- /passage:repair-R-E04 -->

## R-E05 — current-evidence correction

**Priority:** P1. **Owner:** 07 planted lower; 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage CL-first-difference, lines 1755–1755.

An explicit absolute averaged coupling theorem now exists.

<a id="repair-R-E05"></a>
<!-- passage:repair-R-E05 -->

`QuarticQuery.QueryTree.exists_mem_path_ne` proves the first-difference implication, and `eq_of_dummy_ne_planted` identifies the two classes of differing coordinates. The current `Paper.eq_18` packages the displayed absolute difference of the full dummy/planted averages with the two unsplit hit events. The older `output_gap_le` packages the one-sided indicator inequality used in the original main proof, with the cell event already split into heavy and nonheavy cases. These are distinct current declarations, not competing descriptions of one type.

<!-- /passage:repair-R-E05 -->

## R-E06 — current-evidence correction

**Priority:** P1. **Owner:** 07 planted lower; 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage CL-discrepancy, lines 1891–1891.

The precise older one-sided statement is still correct, but no longer exhausts current exported discrepancy theorems.

<a id="repair-R-E06"></a>
<!-- passage:repair-R-E06 -->

The checked erased-zero induction improves the first summand to $2G/m^2$. The current `Paper.eq_23_two` proves the absolute-value bound with this improved coefficient, and `Paper.eq_23` proves the displayed coefficient-four version. Both use normalized promise-supported weights, one-instance hardness, and a worst-case depth cap. The older `QuarticQuery.tree_gap_le`, used in the headline proof, exports the following sufficient one-sided form.

<!-- /passage:repair-R-E06 -->

## R-E07 — current-evidence correction

**Priority:** P1. **Owner:** construction/exponent section owners (numbers not supplied); 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage ROOT-FAMILY-ASSEMBLY, lines 1989–1989.

The named-circuit and quantified family wrappers are now available; no change to the fixed-k theorem is authorized.

<a id="repair-R-E07"></a>
<!-- passage:repair-R-E07 -->

**Evidence.** `QuarticQuery.family_bounds` produces one circuit with both the quantum upper bound and the implication used for the randomized lower bound. `ForrelationLower.bansalSinhaLower` discharges that implication's remaining premise, and `Gvalue_ge` supplies $1/400$. The current `Paper.construction_family_named` uses the actual `Forrelation.forrCircuit` and explicitly states both bounds, its realization, and its size estimate; `Paper.construction_equation_two` presents the quantified equation (2) form with positive constants and $b_k=6$. Their fixed-$k$ threshold is chosen before $t$ varies. They are covered by the source-bound root build and recorded type audit, but not a Comparator receipt.

<!-- /passage:repair-R-E07 -->

## R-E08 — current-evidence correction

**Priority:** P1. **Owner:** exponent section owner (number not supplied); 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage ROOT-RATIO, lines 2010–2010.

Literal ratio, its coefficient and its limits now occur in current theorem types.

<a id="repair-R-E08"></a>
<!-- passage:repair-R-E08 -->

**Evidence.** The current `Paper.classical_exponent_ratio` concludes the displayed lower envelope with the coefficient $c/(1+C)^\alpha$, proves that envelope tends to $+\infty$, and proves that the ratio itself tends to $+\infty$, under the two eventual family bounds and the stated positivity hypotheses. `Paper.classical_Fkm_ratio` instantiates it with the canonical circuit family and $b_k=6$. The older `eventually_gt_rpow` and `exists_threshold_gap` remain sufficient comparisons used in the headline proof; their narrower conclusions no longer describe the whole available source. The current ratio wrappers belong to the source-bound root build and recorded type audit, lie outside the two headline dependency roots, and have no Comparator receipt. The integral estimate above remains an elementary ordinary proof of the same limiting comparison.

<!-- /passage:repair-R-E08 -->

## R-E09 — current-evidence correction

**Priority:** P1. **Owner:** Appendix A section owner (number not supplied); 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage ROOT-APPENDIX-INTRO, lines 2043–2043.

The current Appendix A assembly is no longer prose-only, while the original headline dependency route and distinct constants remain visible.

<a id="repair-R-E09"></a>
<!-- passage:repair-R-E09 -->

The headline proof uses `QuarticQuery.R_le_D_le_one_add_Q_pow_four` in `Appendix/TheoremA1.lean`, which obtains the coefficient $20736$ through `Cslib.Quantum.complexity_le_mul_pow_four` and the query-model bridges. The current packet also contains a separately assembled `Paper.appendixA_theoremA1` following A.2–A.5 through the nonnegative matrix adversary, the star and sensitivity-graph applications, an actual restricted face with Huang's recursive matrix, and Midrijānis's decision-tree bound. Its coefficient is $35^4=1500625$. The following ordinary proofs retain the sharper symbolic adversary constant where displayed; the local evidence notes distinguish that constant from the rational wrapper constants.

<!-- /passage:repair-R-E09 -->

## R-E10 — current-evidence correction

**Priority:** P1. **Owner:** Appendix A section owner (number not supplied); 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage ROOT-ADVERSARY-FINAL, lines 2125–2125.

This resolves the stale no-formal-progress claim without falsely treating 1/35 as at least the sharper symbolic constant.

<a id="repair-R-E10"></a>
<!-- passage:repair-R-E10 -->

**Evidence.** `FixedSim.build` and `exists_fixedSequence` supply the adaptive-to-fixed-query conversion. The current `Paper.appendixA_perron` supplies the nonnegative unit eigenvector; `appendixAProgress_query_quadratic`, `appendixAProgress_query_le`, `appendixA_unit_states_final_overlap`, and `appendixAProgress_final` prove the progress and overlap estimates with their displayed normalization and support hypotheses. `appendixA_adversary_of_perron` gives the sharp factor $1-2\sqrt{(1/3)(1-1/3)}$ for a supplied correct fixed query sequence and Perron witness. The named minimum-query wrapper `appendixA_lemmaA2` instead uses the slightly smaller rational constant $1/35$. Thus it covers the original existential-constant Lemma A.2, while identifying it with the sharper constant fixed in this prose requires supplying the intermediate witnesses and the adaptive bridge. These current declarations are included in the source-bound root build; selected wrappers have recorded type/axiom audits, but none of these Appendix helpers has a Comparator receipt.

<!-- /passage:repair-R-E10 -->

## R-E11 — current-evidence correction

**Priority:** P1. **Owner:** Appendix A section owner (number not supplied); 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage ROOT-BS-LAMBDA, lines 2157–2157.

Both routes now exist; distinguish existential-O ledger strength from the baseline sharpened numerical display.

<a id="repair-R-E11"></a>
<!-- passage:repair-R-E11 -->

**Evidence.** The current `Paper.appendixA_blockSensitivity_star_le_Q_sq` and `appendixA_spectralSensitivity_adversary_le_Q` prove the star and sensitivity-mask consequences, with coefficients $1225$ and $35$ respectively, including constant functions. `appendixA_lemmaA3_adversary` packages the two conclusions. These are the rational-$1/35$ versions of the argument. The sharper symbolic coefficients $c^{-2}$ and $c^{-1}$ displayed above follow from the sharper ordinary adversary bound; they should not be attributed verbatim to the rational wrappers. All three current declarations have source-bound build evidence and no Comparator receipt.

<!-- /passage:repair-R-E11 -->

## R-E12 — current-evidence correction

**Priority:** P1. **Owner:** Appendix A section owner (number not supplied); 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage ROOT-HUANG-SPECTRUM, lines 2215–2215.

Current restricted-face/Huang assembly supplies the intended spectral conclusion; do not replace lambda by ordinary sensitivity or flatten all component matches to exact.

<a id="repair-R-E12"></a>
<!-- passage:repair-R-E12 -->

**Evidence.** The current `Paper.appendixA_restriction_parity_face` supplies the actual face and parity-agreement set. `huangMatrix`, its square and absolute-adjacency lemmas, `huangEnd_eigenspaces_half`, and `huang_positive_rayleigh_witness` supply the recursive matrix and supported positive-eigenvalue vector. `appendixA4_paper_route` concludes $\deg(f)\leq\lambda(f)^2$, including constants, after extension by zero to the original sensitivity graph. The formal equal-multiplicity argument uses a parity involution, whereas the prose uses trace zero. Individual catalogue rows for the full spectrum chain remain partial because their displayed clauses are split across declarations. The assembled A.4 endpoint is covered by current source-bound build and type-audit evidence, outside the headline dependency roots, with no Comparator receipt.

<!-- /passage:repair-R-E12 -->

## R-E13 — current-evidence correction

**Priority:** P1. **Owner:** Appendix A section owner (number not supplied); 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage ROOT-MONOMIAL-TREE, lines 2237–2237.

The endpoint is now exact, while the full procedural round-block narrative still uses several components.

<a id="repair-R-E13"></a>
<!-- passage:repair-R-E13 -->

**Evidence.** The current `Paper.appendixA_exists_maximal_round_support` supplies the maximal-degree support with a sensitive subset at each input. Separate restriction-transport and disjoint-support counting lemmas account for the remaining clauses of `claim-round-block`, whose current tie remains partial. `Paper.appendixA_lemmaA5` exports the exact endpoint $D(f)\leq\operatorname{bs}(f)\deg(f)$ through the decision-tree bridge and the imported Midrijānis theorem. The ordinary algorithm above gives the full per-input explanation; its endpoint is no longer without a current formal tie.

<!-- /passage:repair-R-E13 -->

## R-E14 — current-evidence correction

**Priority:** P1. **Owner:** Appendix A section owner (number not supplied); 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage ROOT-QUARTIC-UPPER, lines 2254–2254.

Update the source-availability statement and separate all three valid constants and dependency routes.

<a id="repair-R-E14"></a>
<!-- passage:repair-R-E14 -->

**Evidence.** The headline dependency route remains `D_le_of_QLe`, `D_le_Q_pow_four`, `R_le_D_le_one_add_Q_pow_four`, and `universalPower_four`, using the imported coefficient $20736$. The relevant imported source is now supplied under `dependencies/complexitylib`, and its theorem type is a fixed-query algorithm bound transported to the adaptive minimum by the bridges. Separately, current `Paper.appendixA_D_le_Q_pow_four` and `appendixA_theoremA1` assemble A.2–A.5 with coefficient $1500625=35^4$; the optional polynomial-method/spectral hybrid has coefficient $19600$. These constants belong to different explicit proof routes and are not claims that the preceding sharp prose derivation gives $20736$. The current source-bound root receipt covers the original and new declarations; the new Appendix assembly is outside the two headline dependency roots and has no Comparator receipt. This review checked source hashes and exact types, without a new Lean execution.

<!-- /passage:repair-R-E14 -->

## R-E15 — current-evidence correction

**Priority:** P1. **Owner:** 09 backend; later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage ROOT-CATALOGUE-INTRO, lines 2264–2264.

Preserve the historical record rather than rewriting its original evidence fields as though they were always current; give the reader one explicit current overlay.

<a id="repair-R-E15"></a>
<!-- passage:repair-R-E15 -->

This catalogue preserves the original corpus statements and the evidence fields supplied with the historical baseline. Its source version is the baseline checkpoint named in §2.3; it is not a current coverage report. The separately versioned current concordance compares all 121 rows with the frozen review packet, gives exact current types and per-declaration evidence, and records the one changed canonical statement text, `claim-bs-to-L`. Historical quotations are retained verbatim there and are not silently overwritten. A current build, a generated-challenge comparison, a dependency path, and agreement with the intended ordinary statement remain distinct judgments. The current row labels comprise 55 exact, 31 stronger and 35 partial matches; only seven rows have a recorded comparison. Those counts are corpus metadata, not a blanket claim that every displayed sentence has been independently verified.

<!-- /passage:repair-R-E15 -->

## R04 — current-evidence correction

**Priority:** P1. **Owner:** 02 Forrelation promise/circuit; 09 backend.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage forr_bundle, lines 851–851.

A complete conjunction is now supplied; preserve exact compiler and evidence boundaries.

<a id="repair-R04"></a>
<!-- passage:repair-R04 -->

The current source contains a conjunction theorem, `QuarticQuery.Paper.construction_lemma_2_1_complete`, for these three parts. Its statement retains the concrete coherent preparation and bit-query compiler premises; the quantum component has the compiled query accounting recorded beside Lemma 2.1(ii). The theorem is covered by the source-bound root build and the recorded type audit, with no individual Comparator receipt. The displayed asymptotic interface is the ordinary consequence of those components, not a claim that this review reran the kernel.

<!-- /passage:repair-R04 -->

## R05 — resource specification clarification

**Priority:** P1. **Owner:** 05 quantum upper.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage upper-amplification-statement, lines 1022–1022.

The amplitude-amplification proof uses the success reflection. The actual applications already retain the necessary flag.

<a id="repair-R05"></a>
<!-- passage:repair-R05 -->

**Lemma 3.1, with the quantifiers made explicit.** For every pair of real numbers \(0<\gamma\leq 1/2\) and \(0<\eta<1/2\), there is one procedure, depending on \(\gamma,\eta\) and using a preparation \(A\) as a black box, with the following property for every unitary \(A\), every fixed input oracle, and every designated retained success bit. Write \(p\) for the probability that measuring \(A|0\rangle\) in that subspace succeeds. The procedure returns either failure or a state. Every returned state is the normalized success component of \(A|0\rangle\), up to global phase. If \(p\geq\gamma\), its failure probability is at most \(\eta\). If \(p=0\), it fails with certainty. On every branch, for every \(p\in[0,1]\), it uses \(O(\gamma^{-1/2}\ln(1/\eta))\) calls to \(A\) and \(A^{-1}\). In particular, neither the procedure nor its stopping rule depends on knowing \(p\). This is corpus statement `lem-3.1`. The bit's one-outcome projection is denoted by \(\Pi\). Its phase flip and measurement are fixed input-independent operations and use no bit-oracle queries. More generally, the same argument applies to a success subspace when its reflection and measurement are supplied at no additional query cost; otherwise their cost must be counted.

<!-- /passage:repair-R05 -->

## R06 — worked proof explanation

**Priority:** P1. **Owner:** 03 Forrelation lower bound.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage forr_identity, lines 542–544.

Show both Stein eliminations, the vanished repeated derivatives, and independence of previously created weights.

<a id="repair-R06"></a>
<!-- passage:repair-R06 -->

First take \(k=3\), so there are two Gaussian vectors \(U_0,U_1\) and the three blocks of biases are
\[
w_s=(sX_0,\;Y_0X_1,\;Y_1).
\]
Products within a block are coordinatewise. For this calculation write \(D_{r,a}=\partial_{(r,a)}\), and keep the same bias \(w_s(U)\) in every extension below. The derivative formula just proved is
\[
h'_g(s)=\sum_a\mathbb E\!\left[X_0(a)\mathcal E_{w_s}D_{0,a}g\right].
\]
Apply the coordinate Stein identity to \(X_0(a)=\varphi(U_0(a))\). Differentiating the extension with respect to \(U_0(a)\) can affect its first or second block. The first-block contribution is
\(s\varphi'(U_0(a))\mathcal E_{w_s}D_{0,a}^{2}g=0\), because a multilinear extension has zero second derivative in the same coordinate. The second-block contribution through coordinate \(b\) is
\(H_{b,a}\varphi'(V_0(b))X_1(b)\mathcal E_{w_s}D_{0,a}D_{1,b}g\). Consequently
\[
h'_g(s)=\sum_{a,b}H_{b,a}\,
\mathbb E\!\left[
\Psi(U_0(a))\varphi'(V_0(b))X_1(b)
\mathcal E_{w_s}D_{0,a}D_{1,b}g
\right].
\]
Now eliminate \(X_1(b)=\varphi(U_1(b))\) in the same way. The factor \(\Psi(U_0(a))\varphi'(V_0(b))\) depends only on \(U_0\), so differentiation in \(U_1(b)\) leaves it unchanged. The contribution through the middle-block bias is
\(Y_0(b)\varphi'(U_1(b))\mathcal E_{w_s}D_{0,a}D_{1,b}^{2}g=0\). Differentiation through the last-block coordinate \(c\) remains and gives
\[
\begin{aligned}
h'_g(s)=\sum_{a,b,c}H_{b,a}H_{c,b}\,
\mathbb E\!\bigl[&\Psi(U_0(a))\varphi'(V_0(b))
\Psi(U_1(b))\varphi'(V_1(c))\\
&\mathcal E_{w_s}D_{0,a}D_{1,b}D_{2,c}g\bigr].
\end{aligned}
\]
There is now one cube derivative in each block and no remaining \(X\) factor to eliminate.

The general induction repeats these two steps. After choosing \(a_0,\ldots,a_j\), the term still to be eliminated has the factor
\(X_j(a_j)\mathcal E_{w_s}\partial_{(0,a_0)}\cdots\partial_{(j,a_j)}g\), multiplied by weights depending only on \(U_0,\ldots,U_{j-1}\). Stein in \(U_j(a_j)\) leaves those weights unchanged. Its effect on the current-block bias vanishes by the repeated derivative at \((j,a_j)\); its effect on bias \((j+1,b)\) contributes
\(H_{b,a_j}\varphi'(V_j(b))X_{j+1}(b)\) and a new cube derivative at \((j+1,b)\). At the last block the convention is \(X_\ell=1\), so the iteration stops after \(\ell=k-1\) eliminations. This convention also covers \(k=2\) directly.

<!-- /passage:repair-R06 -->

## R07 — proof quantifier clarification

**Priority:** P1. **Owner:** 03 Forrelation lower bound.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage forr_identity, lines 562–562.

Do not choose a different mean-value parameter for each path.

<a id="repair-R07"></a>
<!-- passage:repair-R07 -->

The mean value theorem was applied to the whole scalar function \(h_g\), so one parameter \(s_*\) serves every path; it may depend on \(g\)

<!-- /passage:repair-R07 -->

## R08 — structure and navigation

**Priority:** P1. **Owner:** later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage ROOT-ARCHITECTURE, lines 59–59.

Describe the actual branches; apply together with R09 so the named proof appendix exists.

<a id="repair-R08"></a>
<!-- passage:repair-R08 -->

The separation has two branches after the same total function is fixed. The quantum branch uses the promise decoder and exact local tests; the classical branch uses the promised hard distribution and the capped direct product. Their bounds meet in the fixed-k exponent calculation. The independent universal quartic upper bound is proved in Appendix A. The Forrelation lower-bound appendix supplies the complete internal proof of the hardness interface. The historical catalogue and current evidence concordance supply statement-level lookup at their respective source versions.

<!-- /passage:repair-R08 -->

## R09 — structural move

**Priority:** P1. **Owner:** later integrator; 02 promise/circuit; 03 lower bound.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage forr_cube through forr_attribution, lines 410–831.

Move the full internal proof while preserving its exact mathematical content. It occupies 5195 of11160 whitespace tokens before the total construction.

<a id="repair-R09"></a>
<!-- passage:repair-R09 -->

1. First apply the local mathematical and evidence repairs whose targets are inside this span.
2. Move complete §§3.7–3.16 to a named Forrelation lower-bound appendix; preserve every existing passage and claim anchor.
3. Keep §§3.1–3.6 and §3.17 in the main route. Keep the source-display caveat beside the lower-bound interface.
4. Add a direct proof link from forr_bundle to forr_cube; add a backlink from the proof appendix to forr_bundle.
5. Reletter appendices, section references and rendered links only during final integration.


The main construction uses the following three properties of the same partial function. The complete internal proof of its randomized lower bound is in the [Forrelation lower-bound appendix](#forr_cube).

<!-- /passage:repair-R09 -->

## R10 — historical provenance

**Priority:** P1. **Owner:** later integrator; 09 backend.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage ROOT-CATALOGUE-INTRO, lines 2259–2259.

The catalogue already preserves old evidence. Clarify its title rather than rewriting its original rows.

<a id="repair-R10"></a>
<!-- passage:repair-R10 -->

## Appendix B. Historical statement catalogue and source correspondence

<!-- /passage:repair-R10 -->

## R11 — current-evidence correction

**Priority:** P1. **Owner:** 07 planted lower; 09 backend.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md, passage CL-early-late, lines 1775–1775.

The exact identity exists as an additional source theorem even though the selected row remains partial.

<a id="repair-R11"></a>
<!-- passage:repair-R11 -->

The equality follows by first conditioning on the complete dummy run: exactly $Z$ choices of the independent uniform $I$ have their zero discovered. This recovers `claim-EZ` and Eq. 19 as stated. The supplied source proves a stronger estimate by the following shorter induction, without conditional probabilities. The current source proves the probability identity in `QuarticQuery.Paper.erasedZero_eq_expectedZeros_div`, the coefficient-four bound in `Paper.eq_19`, and the coefficient-two refinement in `Paper.erasedZero_le_two`. The older selected corpus ties `sum_xQueries_le` and `avg_foundZero_I_le` are only partial correspondences to the full equation; their metadata should not obscure these additional current declarations. This source support does not include the optional denominator \(m(m+1)\) proved later. All evidence is per declaration and source-bound; no new kernel run was made here.

<!-- /passage:repair-R11 -->

## R120 — cross-document navigation

**Priority:** P2. **Owner:** later integrator; later companion revision.

**Target:** repository/research/returns/funnel/2_short_expert_paper/paper.md, passage headline, lines 33–33.

Passage comments are not rendered anchors. Add actual anchors and then apply the seven-unit proof map.

<a id="repair-R120"></a>
<!-- passage:repair-R120 -->

<a id="headline"></a>
<!-- passage:headline -->

<!-- /passage:repair-R120 -->

## R121 — cross-document navigation

**Priority:** P2. **Owner:** later integrator; later companion revision.

**Target:** repository/research/returns/funnel/3_examples_first_exposition/exposition.md, passage main-theorem, lines 475–475.

Passage comments are not rendered anchors. Add actual anchors and then apply the seven-unit proof map.

<a id="repair-R121"></a>
<!-- passage:repair-R121 -->

<a id="main-theorem"></a>
<!-- passage:main-theorem -->

<!-- /passage:repair-R121 -->

## R13 — reproducibility access

**Priority:** P2. **Owner:** later integrator; packet/backend owner.

**Target:** repository/research/returns/funnel/3_examples_first_exposition/exposition.md, passage reproducibility command, lines 723–723.

The selected packet includes examples_output.txt but not examples.py. Preserve the original execution claim as historical, and supply an exact script/hash in the eventual reader bundle before claiming fresh reproduction.

<a id="repair-R13"></a>
<!-- passage:repair-R13 -->

python3 examples.py > examples_output.regenerated.txt


The original exposition reports these calculations from examples.py. That script is not included in this selected review packet; the retained output alone does not permit fresh reproduction here. The independent Forrelation census returned with this review is a separate computation.

<!-- /passage:repair-R13 -->

## R14 — edition-specific citations

**Priority:** P2. **Owner:** later integrator.

**Target:** repository/research/returns/funnel/1_long_reasoning_record/references.bib, passage bibliography, lines 1–298.

Replace the six principal mathematical entries with the edition-specific entries in this return; retain unrelated entries without implying they were independently audited.

<a id="repair-R14"></a>
<!-- passage:repair-R14 -->

1. Merge the exact edition-specific BibTeX entries identified by this repair.

<!-- /passage:repair-R14 -->
