# Exact formal correspondence and remaining limits

## Overall disposition

No unresolved ordinary mathematical gap was found in the assigned construction under its exact circuit interface. The current source-bound root receipt includes its principal theorems. This file identifies their actual scope and the additional conclusions not promoted to checked Lean statements.

Packet pin: 1dd469dd0042b937b739da3bc211eeb60bdf7462. Root receipt commit: 31e17dee667d1d72fa621da8e7d3d8ff5fc3960a, run at 2026-11-02T18:25:39.383153+00:00. All 124 recorded local Lean/config hashes match the packet bytes. Differing commit labels alone therefore do not establish source drift. No native Lean process was executed during this return.

## 1. Circuit interface

AC-circuit uses the exact circuit premise from §3.17. CircuitRealises C P includes existence of a consistent transcript and correctness of its two output bits for every raw input. Transcript existence follows independently for every acyclic circuit; the correctness clause is (4.1) after identifying the unique transcript with evaluation.

The asymptotically efficient Forrelation circuit, its concrete circuit choice and fixed size constant are inherited inputs, not reproved here. This is an ordinary supplied premise, not an extra unresolved hardness binder. The capped, amplified decoder used in AC-comparison is likewise supplied by the preceding section.

The example's finite truth-table circuit is a separate circuit. Its exhaustive 256-input check supplies no asymptotic size theorem.

## 2. Transcripts

gateConsistent_iff_eq_circuitEval and existsUnique_gateConsistent supply the all-input equivalence and uniqueness. Actual input wires are read directly; earlier non-input values are read from the transcript.

The generic Circuit syntax does not require distinct domain and value output indices. The section adds no such generic hypothesis. Distinct output gates are a property of the example circuit.

## 3. Semantic winner and output-test definition

The source WinsAt explicitly requires P(A)=some address_bit. PaperWinsAt uses the true-address formulation. Their equivalence needs no CircuitRealises premise.

The canonical ledger's def-win-at-address uses consistent transcripts with domain output one and value output equal to the address bit. Converting that description to semantic WinsAt requires CircuitRealises C P. winsAt_iff_outputs, winsAt_iff_localTests and construction_win_at_address_outputs preserve it. The return does not silently identify these definitions before applying the circuit premise.

The type of addressedF and its finite existential predicate establish totality. Lean's noncomputable modifier does not mean partial. winsAt_unique proves both column and address uniqueness, stronger than the ledger's column-only corollary. These conclusions require no circuit correctness. Every pointer word decodes under the fixed bijection.

## 4. Count, local tests and dichotomy

The exact count is m+(m−1)+r(S+2). Its O_k(m log³m) bound additionally requires r=20ℓ and S≤A_k mℓ² with A_k fixed before m. construction_K_bound retains those hypotheses and t≥1. The count alone is insufficient.

winsAt_iff_localTests is an all-input equivalence under CircuitRealises C P. localTestTree_eval and localTestTree_depth_le provide exact adaptive evaluation without that premise or a promise. The depth max(3,ℓ+1) becomes ℓ+1 on the paper range ℓ≥2. Local dichotomy and uniqueness of the all-passing address follow. No missing construction clause remains here.

## 5. Finite examples

The example statements have lean=[] in the correspondence. The checker compares independently written semantic and local predicates on all 16 candidate pairs of the specified board, not on every possible 5,936-bit board.

The 360 transcript corruptions are single-bit mutations of the winner's selected transcripts. The general result about arbitrary corruption comes from topological induction, not this finite test.

The equal-projection-law observation uses the computed Φ values and the specified projection probability Φ². Equality for arbitrary fixed repetition count is an ordinary product-law deduction; the additional three-trial enumeration is finite. This concerns that decoder's outcome bits, not every quantum algorithm or all retained information.

The domain-omission counterexample is a new finite illustration, not a correction to the paper.

## 6. Pointer support

construction_pointer_every_physical_coordinate gives witnesses on full BitLoc inputs, with exactly one physical coordinate changed. The ℓ pointer and m possible target coordinates are distinct. The local-test definition also shows no dependence on other coordinates. Thus support is ℓ+m alongside depth ℓ+1.

The original preprint already states adaptive lookup. The erroneous fixed-support wording belonged to an earlier ledger, and the current canonical row is already corrected.

## 7. Arbitrary-index retained-workspace evaluator

construction_lemma_2_2_ii fixes (i,s), then permits arbitrary complex coefficients of the test index. Each work register starts at its fixed selected ket. The direct-sum action is preserved and every incorrect-output amplitude is zero; work remains present.

construction_controlled_compile supplies the physical 2n query cap for the same n-read controlled family, under a finite inhabited physical input type and fixed finite embedding. It preserves continuation probabilities on arbitrary embedded states. construction_lemma_2_2_complete combines these same witnesses with count, size, truth and depth at 2(ℓ+1) physical queries.

The complete type is in correspondence.json. Simultaneous superpositions of candidate pairs and test indices would require another instantiation of the generic direct-sum result; they are not literally the specialized theorem's type.

No gate-count or workspace-size bound follows. Workspace dimensions and starting states are fixed before the input; final states may depend on the input and be entangled with the label.

## 8. Clean oracle: a separately identified formal gap

Equation (4.16) is an ordinary compute-copy-uncompute corollary with arbitrary target bit, reset work, and at most 4q* physical queries. No exact Lean declaration packaging this interface was supplied. Its new record has proposed_lean=null.

The later verifier can use the retained evaluator and full inverse, so this missing formal bridge is not an open hypothesis required by the construction.

## 9. Uniform sampling

The h/K law is deduced from uniform preparation and orthogonal exact test blocks. Nearby Upper.test_samples, testLaw_pass and testLaw_fail implement related verification laws. Their existence is not used to infer arbitrary-index coherence from uniform sampling alone.

## 10. Winner domination

winner_no_incoming_zero quantifies over every rival address; winner_finds_zero uses the genuine winner's true address. quantumWinner_dominates requires k≥1, t≥1, 0<ε≤1, n≥repetitions k (ε/(40t)), a genuine WinsAt witness and a distinct opponent. It concludes 1−ε≤cmpProb n x i j. No opponent promise is required.

The prose uses 0<ε<1/2 and the same error-reduction purpose. The winner's promises justify its decoder bound by a union bound. The independence-free observation concerns the deterministic event inclusion; it does not change the implemented fresh-register algorithm.

## 11. Evidence layers

The root-build receipt includes all cited declarations. The later selected type/axiom audit includes the new Paper wrappers, not every core theorem; membership is separate for every name. The allowed axioms are propext, Quot.sound and Classical.choice. This is supplied audit evidence with freshly verified bindings, not a new kernel run.

The Construction Comparator's source membership is winsAt_unique, existsUnique_gateConsistent, winner_no_incoming_zero and winner_finds_zero, plus four Checked wrappers. It excludes construction_lemma_2_2_complete. Its independently compiled challenge shares maintained vocabulary and specifications, so a pass is not an independently authored semantic test.

The newer Paper wrappers lie outside the two recorded headline roots' reached set. That describes the dependency traversal, not compilation failure. Current source-bound evidence supersedes historical unelaborated comments for the exact matching sources.

No live state beyond the packet, human proof review, or final acceptance is inferred.
