# Independent audit: probabilistic tournament and the quantum upper bound

## Disposition

The ordinary argument of the frozen long record, §5.2–§5.4, proves the quantum upper bound with the intended all-input worst-case query cap. The crucial mechanisms are exact conditional sampling, the paired-sum drift identity, a winner's resistance to every opponent's pointer, and exact fixed-address local tests. None requires an order on the losing candidates, a correctness promise for their decoders, or independence between failures at different adaptive histories.

The main necessary editorial correction is evidentiary. The baseline's `upper-tournament-evidence` passage says the physical endpoint only returns a Boolean continuation. The current snapshot adds `QuarticQuery.Paper.quantumTournament_list` and `QuarticQuery.Paper.quantumTournament`: they exhibit a coherent `Samples` law whose measured alphabet is a list of length at most T, together with a physical `Runs` cap and the desired membership probability without verifier error. The construction/quantum adjudication records native compilation of these modules. This audit inspected their statements and proofs but did not run Lean or independently validate the compilation receipt; the dedicated evidence audit must determine the current source-bound label.

The source's older `UNELABORATED` comments are historical return text. They should neither override an authenticated current receipt nor be silently presented as current evidence. Conversely, the new list theorem does not close the retained-state Lemma 3.1 bridge. It uses the successful-label law. The literal tensor preparation and the short-circuit stage sampler have the same successful index law; they are distinct full-state implementations.

One citation locator needs correction: the baseline cites Mande–Paraashar–Saurabh as “Theorem 4.4” while linking the FSTTCS 2023 published edition. That edition's quantum king-finding theorem is **Theorem 19**, §4, printed p.30:11, with proof on pp.30:11–30:12 and Algorithm 4 on p.30:13. It assumes exact query access to the bits specifying a fixed tournament's edge directions.

## 1. Complete ordinary proof of the tournament

Fix an oracle input x and m≥2 candidates. Each unordered pair has one reversible comparison circuit, with all workspace retained. Interpreting its output as one or the other winner gives probabilities a_ij in [0,1] satisfying a_ii=0 and a_ij+a_ji=1 for i≠j. All probabilities in the proof are internal to the algorithm at this fixed x. The circuit family, not a table known numerically to the algorithm, is the input interface.

Set T=ceil(log₂(1000m)), ε=1/(1000T). Let s be any candidate satisfying a_sj≥1−ε for j≠s. The algorithm itself does not require s to exist. This condition is used solely to analyze its output when such a candidate exists.

### Ideal process and zero weight

For an ordered history L=(p₁,…,p_h), define w_i(L)=∏_(p∈L) a_ip and W(L)=∑_i w_i(L). Start from the empty history, so all weights are one. If W>0, draw p with probability w_p/W and append it, obtaining w'_i=w_i a_ip. If W=0, keep the list and all weights unchanged. This is an explicit absorbing branch, not a distribution obtained by dividing zero by zero. Because a_pp=0, a previously chosen candidate has weight zero and cannot be drawn again on a positive-weight step. All weights remain in [0,1].

For W>0,

    E[W' | w] = (1/W) ∑_(p,i) w_p w_i a_ip
                = (W² − ∑_i w_i²)/(2W) ≤ W/2.

The second equality pairs the terms for (i,p) and (p,i): their sum is w_i w_p, while the diagonal is zero. The identity is algebraic; nonnegative weights are needed for the pivot ratios to be probabilities. At W=0 the next total weight is zero, so the inequality still holds. Iteration yields E W_T≤m/2^T.

If s has not yet appeared, every pivot differs from s and hence

    w_s(L) ≥ (1−ε)^h ≥ 1−hε ≥ 1−Tε = 999/1000 > 1/2.

The Bernoulli bound follows by induction: multiply 1−hε by 1−ε≥0 and discard hε²≥0. Thus an absorbing zero-weight history cannot occur before s is selected. Pointwise, the indicator that the final ideal list misses s is at most 2W_T, so its expectation is at most 2m/2^T. This uses no rank, transitivity or deterministic orientation among losers.

### Quantum sampler and conditioning

At a history of length h, prepare a uniform candidate register and h fresh comparison workspaces. Conditional on candidate i, run its comparison with p_b in the b-th fresh workspace. Before computing the success flag the full state is

    m^(-1/2) ∑_i |i⟩ ⊗_(b=1)^h |φ(i,p_b)⟩.

The success flag is true exactly when all comparison output bits say i wins. For each i, the squared norm of the all-success projection is ∏_b a_i,p_b=w_i. Distinct candidate labels are orthogonal, so the joint success-and-label mass is w_i/m and total success mass is W/m. When W>0, conditioning gives w_i/W. These are probabilities because the initial basis state is normalized and the preparation unitary. The corresponding algebraic tensor identities for arbitrary vectors are only mass identities until normalized.

Bounded amplification with γ=1/(2m), η=ε preserves this successful conditional label law. More explicitly, there is f(L)∈[0,1] such that the amplified stage reports failure with probability f(L), and returns i with probability (1−f(L))w_i/W if W>0. When W=0, f(L)=1 and it returns the current list. If W/m≥1/(2m), then f(L)≤ε. Do not state a conditional law at a zero-probability conditioning event.

On success, measure the candidate label, append it, and repeat. On failure, return the present list. Stop after at most T stages. This describes one bounded algorithm for every oracle input and every comparison table satisfying the basic probability/complementarity conditions.

### Adaptive coupling

Couple the ideal and real processes while their histories agree. For a common positive-weight history, draw an ideal pivot from w_i/W and independently a failure bit with probability f(L); give both processes the pivot on nonfailure, and stop the real process on failure. This produces the correct real law because the real successful mass is exactly (1−f(L))w_i/W. The independent auxiliary failure bit is merely a construction of a coupling; it is not a hypothesis that the physical failure events are history-independent.

At every agreed history before s first appears, W>1/2. Thus f(L)≤ε there. If D_h is the event of first disagreement at stage h before s is listed, condition on the complete history and the absence of earlier disagreement. Each conditional probability of a new disagreement is at most ε, so Pr(D_h)≤ε after averaging over those histories. Summing over at most T stages bounds pre-s disagreement by Tε. If s occurs in the ideal process without an earlier disagreement, it also occurs in the real list. A later failure cannot remove it. Consequently

    Pr[real list misses s] ≤ 2m/2^T + Tε.

No failure bound is needed after s has been listed, when total weight may be arbitrarily small. A proof that charges all stages with the same ε without this qualification is unjustified.

### Query cap

Let c≥1 be the physical query cap of a coherent controlled comparison and its inverse. At history length h, state preparation/inversion uses O(c(h+1)) queries. Every amplified stage uses O(sqrt(m) ln(1/ε)) preparation/inverse calls even when its success probability is below γ. Summing h=0,…,T−1 gives O(c sqrt(m) T² ln(1/ε))=O(c sqrt(m) T² ln T), since 1/ε=1000T and T≥11. Every branch obeys this cap, whether or not a dominant candidate exists.

The current formal implementation uses cc logical reads per comparison. Set

    N = ceil(ln(1/ε)/ln(40/31)),
    M₀ = ceil(10 sqrt(2m)).

It pads each history to T comparisons. Its physical cap is

    C_tour = 2 N(2M₀+1) T² cc.

This is exactly `T * stageCost m T cc ε`. `amplification_budget_le` gives N(2M₀+1)≤138 sqrt(2m) ln(1/ε). Using sqrt(2m)≤2sqrt(m), T≥2, 1000≤2¹⁰ and ln(1000T)≤11 ln T gives

    C_tour ≤ 6072 cc sqrt(m) T² ln T.

The factor two is the ordinary bit-query compiler charge. If the supplied comparison already consists of c ordinary bit queries, `quantumBitOracle_isCirc` represents each one as one logical read, so cc=c is an admissible input bound. The factor-two compilation is deliberately loose, and remains included once in the displayed 6072 constant.

## 2. Decoding and the comparison rule

Let m=4^t, t≥1, ℓ=2t, r=40t. A coherent address decoder runs a fixed number of Forrelation repetitions on each of r instances, retains their outcomes and work, and reversibly computes the output address. It always returns an r-bit label on any input. Correctness is only promised when all r instances are in the domain. With error at most ε/r per promised instance, the union bound gives whole-address error at most ε. Independence is unnecessary for this estimate; the implementation uses fresh copies and obtains a product law.

For fixed k, the physical address cost is O_k(r ln(r/ε)). In the source, with n repetitions per instance, the logical read cost is a=rnk and the physical cap is 2a. At the least prescribed n,

    2a ≤ 2rk [1+16·2^(10k) ln(r/ε)].

Sort two distinct candidate indices so the same unordered-pair circuit is used in both orientations. Decode their addresses separately. Each candidate follows its pointer toward the other and declares that opponent disqualified exactly when the indicated target bit is zero. If exactly one disqualifies the other it wins; if both or neither do, the smaller index wins. A self-comparison has success output false without pointer access.

The retained address registers remain orthogonal, and the pointer operations and final outcome projection are block diagonal with respect to them. Thus the coherent outcome probability equals the classical mixture over decoded-address pairs. Reversing the ordered naming complements the output interpretation of the same circuit and gives a_ij+a_ji=1 exactly on every input. The deterministic tie-break's numerical order supplies only a complete rule for unresolved pairs; no order property enters the tournament proof.

A true winning column s has X_s all ones. No opponent's pointer, at any decoded address, can disqualify s. When s's own decoder returns its true address, its certified outward pointer reaches a zero in each opponent, so s defeats that opponent. The opponent's decoder may be arbitrarily unreliable. Correct own decoding is a subset of the victory event, giving a_sj≥1−ε. This one-sided implication is the complete dominance argument.

Each pointer lookup reads ℓ pointer bits and one target bit, with a cap independent of their values. Thus the logical comparison cap is cc=2a+2(ℓ+1), and the generic physical cap is 2cc. All reversals have the same read/query cost. Computing a target index from retained labels is input-independent reversible work, hence free in query complexity.

## 3. Fixed-address verification and final error

For any chosen column and address, the construction supplies

    K = m+(m−1)+r(S+2)

exact Boolean local tests. The tests check all-one X, one outward pointer per other column, S gate constraints and two output constraints for each transcript. Each is an adaptive tree of depth at most d=max{3,ℓ+1}=ℓ+1 for m≥4. This is a bound on queries along a branch, not on the set of coordinates on which a test can depend: a pointer test can depend on m+ℓ coordinates.

The test sampler chooses a uniform test index, computes the test exactly, and labels failure as success for search. If h tests fail, its success probability is h/K. For h=0, bounded amplification reports no failed test with certainty. For h≥1, γ=1/K makes its probability of not finding a failed test at most ε. Here K≥m≥4, so 0<γ≤1/2, and ε∈(0,1/2). The fixed cap applies also at h=0.

Decode each candidate afresh and measure its address, then run this search at that fixed address. A nonwinner has at least one failed test at every address by the exact circuit-to-winner equivalence. Averaging the fixed-address acceptance bound over any decoded-address law gives acceptance at most ε. A true winner has no failed tests at its true address; it is therefore accepted whenever its new decoding is correct, giving rejection at most ε. This last inequality has only one ε loss, not decoding ε plus search ε, since the search cannot falsely report a failed exact test on the true address.

Return one if any listed candidate is accepted. On a zero input all candidates are nonwinners. Condition on the full tournament transcript and list, use fresh verification work for each candidate, and apply the union bound to at most T acceptances. The false-positive probability is at most Tε. On a one input let s be the unique winner. If s is listed, earlier acceptance already gives correct output; otherwise a fresh verification of s fails with probability at most ε, conditionally on the earlier history. Hence false-negative probability is at most 2m/2^T+Tε+ε. Since 2^T≥1000m, Tε=1/1000 and ε≤1/1000, this is at most 1/250<1/3. The program and cap are fixed before the input; the case split is in its analysis.

## 4. Exact assembled physical budget and Proposition 3.3

With a=rnk, cc=2a+2(ℓ+1), d=ℓ+1, N and M₀ as above, and M₁=ceil(10 sqrt K), the source's padded cap is

    B = T[2N(2M₀+1)Tcc] + T[2a+2N(2M₁+1)d].

The first term permits T complete amplified tournament stages; the second permits T verifications with fresh decoding. The number of trials, number of Grover iterations, number of comparisons per preparation, and number of verifications are each capped before the input. No expected-time step is substituted for a branch cap. Two bit queries per logical read account for the physical implementation; reversing and retaining garbage introduces no data-dependent stopping rule.

The circuit size S=O_k(mℓ²) yields K=O_k(mℓ³), while r,T=O(ℓ). The established decoder and amplification counts are polylogarithmic in m. Therefore each of the two displayed terms is sqrt(m) times a power of log m, proving Proposition 3.3. The existing quantitative bound `Upper.budget_le` gives the separate explicit endpoint B≤budgetConst(k)·2^t(2t)^6, and `Upper.Q_Fkm_le` instantiates the chosen `forrCircuit`. No randomized Forrelation lower-bound theorem is a premise of this quantum proof.

A possible editorial simplification is to prove Proposition 3.3 directly from this finite budget and move the deliberately loose expansion of `budgetConst` into a technical paragraph. The finite budget exposes every substantive charge without making the proof depend on memorizing large constants. Do not drop the exact `log^6` arithmetic if the revised section continues to claim that stronger explicit exponent as an independently reconstructed result; the baseline provides that arithmetic and it was checked for consistency here.

## 5. Exact cyclic example and validation

`cyclic_example.md` is a ready-to-insert anchored passage. It uses m=4, T=12, ε=1/12000. The winner beats each loser with probability 1−ε, while the losers have the deterministic three-cycle a defeats b defeats c defeats a. After pivot a, weights are (11999/12000,0,0,1); successful conditional probabilities for s and c are respectively 11999/23999 and 12000/23999. If c is next, the next successful pivot is s. The exact initial expected next total weight is 3/2. The ideal list contains s within three pivots.

The independently written `tournament_example.py` uses rational arithmetic throughout and passed. It enumerates the ideal law and an explicitly declared artificial failure law, checks 23 reachable histories, normalization, no duplicate pivots, drift, survival and the conditional-history union bound. It also detects that a zero-weight branch with failure probability zero would have total mass zero under a totalized division convention. The artificial law uses f(L)=ε for positive weight and f(L)=1 at zero weight; it is not claimed to equal the physical amplifier's law. Finite checks illustrate the proof and do not replace universal proof or kernel evidence.

## 6. Historical citation roles and edition correction

* Dürr–Høyer, *A Quantum Algorithm for Finding the Minimum*, arXiv:quant-ph/9607014v2, revision 7 January 1999, Theorem 1 and Lemmas 1–2, pp.1–2. It searches an ordered table, uses the rank-dependent probability 1/r, and caps an expected-time descent. It is a precedent for repeatedly searching relative to a selected candidate; it does not prove the probabilistic tournament. The entire two-page text was read. Primary PDF: https://arxiv.org/pdf/quant-ph/9607014v2.
* Høyer–Mosca–de Wolf, *Quantum Search on Bounded-Error Inputs*, arXiv:quant-ph/0304052v2, revision 14 April 2003; §1, §3 Facts 1–2 and its final search algorithm, and §5. Its fixed Boolean tests each have correctness probability at least 9/10. The O(sqrt n) search algorithm does not directly apply to comparisons between losers whose probabilities may be arbitrarily close to 1/2. The primary PDF has the §3 algorithm on PDF/printed p.7 and §5 on pp.8–9. The packet's extracted main text was read, with §4 sampled for its stated scope. Primary PDF: https://arxiv.org/pdf/quant-ph/0304052v2. The nominal `source.tar.gz` is a gzip-compressed `.tex` file; it was decompressed successfully, not treated as an actual tar.
* Ben-David–Kothari, *Randomized query complexity can beat certificate complexity*, arXiv:2609.15063v1, 14 September 2026, §3 Lemma 5, pp.3–5. Its three-stage organization is virtual candidate list, exact tournament reduction, then local certificate checking. This is appropriate credit for organization, not a theorem invoked in the present probability proof. It defines a fixed tournament orientation by exact local checks. The §3 proof was read from the primary HTML/PDF; other parts were sampled. URLs: https://arxiv.org/html/2609.15063v1 and https://arxiv.org/pdf/2609.15063v1.
* Mande–Paraashar–Saurabh, *Randomized and Quantum Query Complexities of Finding a King in a Tournament*, FSTTCS 2023, LIPIcs 284, 30:1–30:19, Theorem 19 (§4, p.30:11), not “Theorem 4.4” in this linked edition. The theorem is Q(KING_n)=O(sqrt n polylog n), with exact edge-direction oracle for a fixed tournament. The abstract, oracle convention, theorem statement and nearby proof were sampled. This is related algorithmic context only. URL: https://drops.dagstuhl.de/storage/00lipics/lipics-vol284-fsttcs2023/LIPIcs.FSTTCS.2023.30/LIPIcs.FSTTCS.2023.30.pdf.

Do not promote any of these historical roles to a novelty claim about the present construction. OpenAI's §3 supplies the actual tournament and application being reconstructed. The full-state amplification proof remains assigned to the amplification audit, and native receipt integrity to the evidence audit.

## 7. Limits

This audit did not run Lean, Comparator, a quantum simulator, a full repository build, or a PDF rendering of revised prose. It did inspect exact source bodies, ordinary proofs, the supplied adjudication and primary literature. No supplied source was modified. All files written are scratch audit outputs for integration.
