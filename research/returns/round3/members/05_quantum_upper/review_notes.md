# Review notes: replacement §5, quantum upper bound

## Outcome and exact review boundary

The return supplies a replacement for §5 of the attached long reasoning record. It reconstructs the ordinary proofs of OpenAI's Lemma 3.1 and Propositions 3.2–3.3, explains the all-input physical query budget, and corrects the correspondence with the current Lean snapshot. Within the reviewed §5 argument, **no remaining ordinary mathematical gap was identified**, using the explicitly stated incoming results from §§2–4. This is a bounded editorial and mathematical assessment of the supplied argument; it is not an endorsement of unreviewed sections, an independent human referee report, or a new formal verification run.

The strongest conclusion retained is the all-input query bound for the chosen total-function family,

\[
Q(F_{k,4^t})\le C_k\,2^t(2t)^6\qquad(t\ge1),
\]

for each fixed \(k\ge2\), with \(C_k\) depending on that fixed \(k\). The exponent six is independent of \(k\); the constant is not asserted to be uniform in \(k\). This section neither proves the randomized lower bound nor substitutes a growing-\(k\) argument for the fixed-parameter separation.

The remaining formal obligation is narrower than a missing proof of the upper bound: the packet lacks a source-bound physical implementation theorem that returns the complete original successful quantum state in a designated output subsystem, with the required uniform black-box quantifier and physical compiler correspondence. The ordinary fresh-trial/routing construction is explained. The compiled measured-label law already suffices for the headline query upper bound.

## Ranked corrections and their dispositions

The locators below are stable passage anchors in `section.md`. “Incorporated” describes the present replacement prose; it does not claim that repository Lean files or the baseline record have been edited. Exact source declarations, signatures, evidence records, and boundaries are retained in the companion correspondence and gap record.

### 1. Separate the successful state from its measured-label law

**Locators:** `upper-amplification-statement`, `upper-returned-register`, `upper-current-formal-scope`, `upper-missing-physical-state`.

**Correction and evidence.** `QuarticQuery.Amplification.bounded_amplification` proves the complete abstract `Proc` statement, including phase-invariant successful-state observables and zero wrong-state mass. `QuarticQuery.Upper.Samples.amplify` supplies the measured `Runs` law, while `QuarticQuery.Paper.quantum_amplify_samples` supplies a coherent `Samples` realization with retained workspace. The last two types do not identify a designated original output subsystem with the normalized good state. Equality of output probabilities therefore cannot be promoted to equality of full quantum states.

**Disposition: incorporated; formal theorem deferred.** The section gives both the ordinary returned-state argument and an explicit missing physical factorization statement. It distinguishes compiler correctness on arbitrary embedded vectors from amplification correctness on the specified initial vector. It also requires a program with slots for \(A,A^{-1}\) fixed before the preparation is supplied, rather than merely a separately chosen circuit for each input family. The proposed interface is explicitly uncompiled. The pure-first-qubit versus entangled-pair example shows precisely what a label law fails to control.

**Benefit and remaining check.** This preserves the full ordinary content of Lemma 3.1 while keeping the formal label exact. Closing the formal obligation requires proving output-register factorization or an equivalent instrument theorem for the same physical construction, followed by its own source-bound Lean validation. Rebuilding the existing label-law theorem would not establish the omitted clause.

### 2. Restore the current list-valued tournament theorem

**Locators:** `upper-coupling`, `upper-tournament-evidence`, `upper-continuation-induction`, `upper-current-formal-scope`.

**Correction and evidence.** The current `QuarticQuery.Paper.quantumTournament` has a finite bounded-list output law, nonnegative probabilities summing to one, coherent `Samples` and physical `Runs` witnesses, and

\[
\Pr[s\in L]\ge1-2m/2^T-T\varepsilon.
\]

Its sampler is chosen before the input and before the distinguished dominant vertex. Its substantive hypotheses are \(m\ge2\), an `IsComparison` relation on every input, and coherent pairwise `Samples` witnesses. Probability range follows from those witnesses; a perfect-verifier or extra `UnitValued` hypothesis is not silently assumed in this theorem.

**Disposition: incorporated.** The baseline description that only a Boolean endpoint exists is obsolete for this packet. The older `Upper.tournament_runs` is retained as a separate measured continuation theorem with verifier cost and the additional verifier error \(\varepsilon\). The indicator of membership of the distinguished vertex is identified as an analytical proof device, never an oracle supplied to the sampler.

### 3. Correct the evidence pin without overstating verification

**Locators:** `upper-current-formal-scope`; integration note below concerning baseline §2.3.

**Correction and evidence.** The current root receipt records commit `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`; the packet manifest records `1dd469dd0042b937b739da3bc211eeb60bdf7462`. Independent byte hashing in this review found that all 124 enclosed Lean/configuration inputs agree across current files, the evidence snapshot, the root receipt, the dependency export, and the final axiom verdict. This supports applicability to the exact local source closure. It does not identify the two commits or audit all files in either repository history.

**Disposition: incorporated.** Current build evidence, exact-name Comparator coverage, and headline dependency reach are stated separately. Historical “UNELABORATED” comments and failed earlier runs remain provenance, not the current compilation state. No new Lean or Comparator execution is asserted.

### 4. Bound the actual padded budget and retain the compiler factor of two

**Locators:** `upper-amplification-proof`, `upper-padded-tournament-budget`, `upper-read-compiler`, `upper-finite-budget`, `upper-explicit-log6`.

**Correction and evidence.** The charged quantity is the full padded product \(N(2M+1)\). Bounding a potentially smaller abstract `Proc.callCap` would not by itself bound that product. The replacement supplies the arithmetic

\[
N(2M+1)\le138\gamma^{-1/2}\ln(1/\eta)
\]

and then charges two ordinary bit queries for each logical read. The explicit list bound is \(6072c_{\mathrm{rd}}\sqrt m\,T^2\ln T\). The final integer budget includes both the padded tournament and the at most \(T\) fresh verifiers.

**Disposition: incorporated.** The factor of two occurs once at the compiler boundary. The constants are valid upper bounds, not optimized values. The proof explicitly applies on every branch and every input, including inputs where the amplification promise fails.

### 5. Make all conditioning and zero-weight branches legitimate

**Locators:** `upper-grover-geometry`, `upper-amplification-proof`, `upper-ideal-process`, `upper-stage-law`, `upper-quantum-tournament`, `upper-coupling`, `upper-continuation-induction`.

**Correction and evidence.** The cases \(p=0\) and \(p=1\) are handled before normalized zero components could be used. Conditional successful laws require positive successful mass. When \(W=0\), the ideal process is absorbing and the real amplification law fails with certainty; division by zero is never interpreted as conditioning. Probability range is part of the mathematical comparison assumptions, although Lean's `IsComparison` alone only gives complementarity and a zero diagonal.

**Disposition: incorporated.** The coupling charges disagreements only before the dominant vertex has entered the list. Later low-weight histories need no small-failure bound. Its union bound requires no independence among failures at different stages. The Boolean continuation induction also treats a negative intermediate lower bound explicitly, rather than multiplying inequalities with an unexamined sign.

### 6. Preserve the distinction between the literal tensor state and a short-circuit sampler

**Locators:** `upper-stage-state`, `upper-stage-law`, `upper-current-formal-scope`.

**Correction and evidence.** `QuarticQuery.Paper.equation_15` constructs the literal uniform-index tensor of all fresh comparison states. `quantumWorkspace_uniformize` supplies a common finite workspace. `Upper.stage_samples` may omit later comparisons after a failure. Their successful index masses agree, but their entire retained states are not thereby equal.

**Disposition: incorporated.** The tensor-state proof uses distinct fresh registers and orthogonality of the index slices. No independence assumption about a common deterministic orientation is introduced. The overly broad source docstring associated with `Upper.stage_samples` is reported in the audit; no source docstring was edited in this return.

### 7. Expose the one-sided reason that a true winner is dominant

**Locators:** `upper-comparison-model`, `upper-comparator`, `upper-comparison-law`, `upper-winner-dominates`.

**Correction and evidence.** Each distinct unordered pair uses one designated circuit, with reversed names complementing its output interpretation. This gives \(a_{ij}+a_{ji}=1\), even on meaningless decoded addresses. A true winner cannot be disqualified because its whole \(X\)-block is one; its own correctly decoded pointers disqualify every opponent. The opponent's decoder need not satisfy any correctness promise.

**Disposition: incorporated.** The proof no longer suggests that loser–loser comparisons admit a total ordering or a fixed bounded-error orientation. The exact four-candidate cycle illustrates why those stronger assumptions are unnecessary.

### 8. Keep verification exact on all raw inputs

**Locators:** `upper-verifier`, `upper-verification-proof`, `upper-total-error`.

**Correction and evidence.** The local tests are exact Boolean computations after fixing the decoded address. Their relevant complexity is decision-tree depth, including adaptive pointer queries, rather than dependence on a fixed small coordinate set. A nonwinner has a failed test at every possible address; otherwise circuit consistency would establish a genuine winning address. The verifier bounds consequently survive arbitrary prior tournament transcripts.

**Disposition: incorporated.** The zero-input error is at most \(T\varepsilon\); the one-input error is at most \(2m/2^T+T\varepsilon+\varepsilon\). The final extra \(\varepsilon\) belongs to fresh winner verification and is absent from the list-membership theorem.

### 9. Correct citation roles and version-specific locators

**Locators:** `upper-purpose`, `upper-amplification-statement`, `upper-average-exact`, `upper-bounded-error-comparison`, references for §5.

**Correction and evidence.** BHMT §2, Lemma 1 and equation (8), supplies the rotation analysis; its Theorem 12 is amplitude estimation. BBHT's random-iteration identity is distinguished from its expected-time search theorem. Dürr–Høyer and exact-tournament king finding concern stronger orientation/order settings. Høyer–Mosca–de Wolf requires a fixed Boolean predicate with bounded-error access; it does not directly supply an oracle for arbitrary loser–loser probabilities. Its §3 search construction and §5 imperfect-verifier discussion have distinct page/section locators.

**Disposition: incorporated.** These sources supply attribution, an ingredient, or a comparison as explicitly stated. No novelty or priority claim is inferred from the literature search. Exact inspected editions and reading scope belong to `references.bib` and `source_read_receipt.json`.

### 10. State the exponent-six result only for the chosen circuit and fixed parameter

**Locators:** `upper-section-interface`, `upper-asymptotic-bound`, `upper-explicit-log6`.

**Correction and evidence.** `Upper.Fkm_forrCircuit_QLe` and `Upper.Q_Fkm_le` use the particular `forrCircuit` and discharge the ordinary circuit-realization and size premises of the intermediate bounds. The formal parameterization is \(k=l+1\), \(m=4^t\), \(t\ge1\); the section uses the source separation's \(k\ge2\) regime. The explicit logarithmic exponent is six, with a constant depending on \(k\).

**Disposition: incorporated.** A fixed \(k\) is not asserted to give an exact fourth-power separation. No growing-\(k\) uniformity, gate complexity, workspace bound, or randomized lower bound is claimed here.

## Current evidence and what was not executed

The supplied current root receipt is `repository/corpus/receipts/lean-build-root-2026-11-02T182539383153+0000.json`. It records the toolchain `leanprover/lean4:v4.36.0-rc2`, a successful build, and 2,652 declarations read from the compiled environment. The later `native_results/final-evidence/reviewed_axiom_audit_verdict.json` records a passing audit of 258 reviewed declarations; `native_logs/final-evidence/reviewed-type-axiom-audit.log` supplies exact printed types and axiom observations. The allowed reported axiom set is `propext`, `Classical.choice`, and `Quot.sound`. The relevant logs and source-audit file hashes match their recorded bindings.

These are supplied execution receipts. This return performed source reading, mathematical reconstruction, byte-hash comparison, and finite example checking through its recorded work products. **No new Lean, Lake, or Comparator run was performed.** No Lean source was modified. A matching local source closure does not amount to fresh execution of the pinned external dependencies or to whole-repository reproduction.

The dependency export has 1,354 reached public declarations from `QuarticQuery.theorem_1_1_unconditional` and `QuarticQuery.cubic_bound_fails_unconditional`. None has the `QuarticQuery.Paper.` prefix. The reached upper-bound route includes the older measured `Upper.Samples.amplify` and numerical `Upper.Q_Fkm_le`; the new Paper list and tensor wrappers are present in the compiled root without being dependencies of those two exported roots. Compilation membership and proof-root reach therefore answer different questions.

Exact-name Comparator coverage is narrower still. The current Tournament bundle compares `QuarticQuery.Checked.expected_weight_eq` and `QuarticQuery.Checked.expected_weight_le_half`. The Separation and Unconditional bundles compare their respective wrappers. These passes do not separately compare the new `Paper.quantumTournament`, the literal `Paper.equation_15`, or the missing physical-state assertion by exact name. An axiom audit likewise does not establish informal/formal statement fidelity.

Historical comments headed “UNELABORATED,” older failed attempts, and advisory returns are retained as historical context. They are superseded as compilation evidence where a later passing receipt binds the same current source. They are not erased, and their semantic observations still require examination on their merits.

## Concrete simplification and explanatory reconstruction

The useful simplification is to isolate the successful-label law and use it once to construct the coupling. Pairing \((i,p)\) and \((p,i)\) gives the drift identity directly; the distinguished weight supplies positivity until selection; the exact conditional pivot law then gives the real-process miss bound with one union bound. This removes any need for an order among losing candidates, an estimate of all comparison probabilities, or independence assumptions between stage failures. The Boolean continuation induction remains in the long record because it explains the different theorem used by the current headline proof and its extra verifier error.

A tempting further simplification—replacing the returned-state assertion with the label law everywhere—was rejected. The two-qubit example in `upper-returned-register` proves that the replacement loses the pure state of the designated output subsystem. The admissible simplification is therefore limited to the upper-bound consumer, which measures candidate labels. The stronger state statement remains separately visible.

The four-candidate cyclic example is exact finite arithmetic. Its weights, conditional probabilities, and first-step expected total weight can be recomputed with rational numbers. It is not a realization of a full addressed-certificate input, an execution of a physical quantum circuit, or a proof of the universal theorem. Any artificial failure law in the example's computational record is an illustration, not the actual failure probability of the amplification circuit.

## Draft-review history and final dispositions

Draft-review notes retained under `checks/` are timestamped or version-relative observations of an earlier draft. Their outstanding-sounding wording must not be read as the status of the delivered section. The final section incorporates the substantive repairs they requested: explicit successful-register routing; a scoped auxiliary-state factorization; the separation of initial-state amplification from arbitrary-state compiler correctness; the parameter-only black-box quantifier; the charged padded product; explicit \(|\pm\rangle\) notation; the elementary-reflection clarification; and the corrected HMW citation role and locator. Inline mathematical delimiters were also repaired at source level. The final authoring/metadata checks, where provided, govern the delivered bytes; an earlier draft note remains evidence of the review process rather than an unresolved mathematical objection.

No PDF of the revised section was generated or visually reviewed for this return. Source-level delimiter and link checks, even when passing, are not a rendered-page inspection. No independent human cold-reader or author confirmation was obtained. Those limitations remain after the draft fixes.

## Integration guidance

1. Replace only §5 of `repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md` with `section.md`, preserving the replacement's stable passage anchors and its incoming interfaces from §§2–4. The return is a proposed section, not an already integrated record.
2. Refresh or scope the evidence convention in baseline §2.3, passage `ROOT-EVIDENCE-CONVENTION`. Its present global statement points all packet-relative paths to historical commit `c7e0c9161f0ad898889bd9166e7b354acd42188d`. For the replacement §5, use the current manifest commit and the exact source-bound receipt mapping described above. Do not blindly assign current evidence to untouched older passages or discard their historical provenance.
3. Integrate the companion correspondence, new-statement, statement-change, gap, reference, and source-read records as a coordinated set. Recheck anchor/excerpt alignment after any further prose edit, and bind the actual delivered bytes in the return manifest.
4. Retain the open physical-state bridge and the distinction between current compiled root membership, specified headline reach, and exact-name Comparator scope. A future source proof should receive its own evidence before those labels change.

No edit to the baseline record, its §2.3, the Lean repository, or any unrelated source was performed as part of this return. No publication, merge, author approval, or packet acceptance is implied.

## Paper-authoring receipt

The following fields follow the packet's `writing/mathematical-writing-mechanics.md`, “Required paper-authoring receipt.” The manuscript locators refer to `section.md`; the final return manifest identifies its exact bytes. This is an authoring/review receipt, not a readability score, human peer review, or publication permission.

### mathematical_paper_review

- **object:** Replacement §5, “Quantum evaluation on every input,” for the supplied long reasoning record, packet `05_quantum_upper`.
- **genre_and_target_reader:** A long mathematical reasoning record for a mathematically mature researcher familiar with basic query complexity. The reader should be able to follow the ordinary argument without opening Lean.
- **venue_calibration:** Advisory section contribution. No journal submission, short paper, integrated full record, or release-ready rendered manuscript is represented as completed.
- **contribution_type:** Proof reconstruction, exposition, exact finite illustration, and correction of formal correspondence. The quantum upper-bound construction and source theorem remain credited to OpenAI; classical amplification/search ingredients retain their earlier attribution.
- **headline_claim_and_evidence_class:** The ordinary all-input upper bound and the chosen-family exponent-six bound are reconstructed in §§5.1–5.4. Exact existing Lean endpoint declarations have supplied source-current build evidence. The stronger physical returned-state correspondence is an uncompiled formal target.
- **scanability_check_title_abstract_intro_theorems_conclusion:** The section title, opening interface, Lemma 3.1 statement, Proposition 3.2 conclusion, Proposition 3.3 display, exponent-six display, and §5.5 scope note were compared for parameter, cost, and state/label consistency. No full-record abstract or conclusion was revised or revalidated by this section job.
- **external_field_map:** BHMT supplies the rotation analysis; BBHT supplies the exact randomized-iteration identity and expected-time background; Dürr–Høyer and king finding are ordered/exact-orientation comparisons; HMW is bounded-error fixed-predicate comparison; Ben-David–Kothari is an antecedent for candidate generation and certificate checking. None is silently substituted for the current probabilistic-comparison proof.
- **internal_dependency_map:** Fixed-trial amplification → exact conditional index law → fractional-weight drift and dominant-weight lower bound → coupled list sampler → one-sided winner dominance → exact local verification → all-input error bound → physical compiler and integer budget → chosen-circuit logarithmic bound. The ordinary argument and actual headline Lean dependency path are identified separately.
- **concrete_anchor_and_example_boundary:** `upper-cyclic-example` gives \(s,a,b,c\), \(\varepsilon=1/12000\), a certain three-cycle among the losing candidates, exact weights after pivots \(a,c\), and first-step expectation \(3/2\). `upper-returned-register` gives equal computational-basis label laws with different first-register states. These are finite illustrations of mechanisms and a failed implication, respectively; neither establishes the whole theorem by enumeration.
- **hard_step_and_proof_forward_decisions:** The nontrivial interface is exact sampling from surviving weights without an ordering or a success-probability estimate. The proof first explains the two-dimensional rotation, then conditioning, then drift and coupling. The designated-register issue is placed beside the successful-state proof and isolated formally in §5.5.
- **mathematical_taste_rubric_evidence_and_dispositions:** See the seven-dimension table below. No aggregate score is assigned.
- **concrete_simplification_attempt_and_outcome:** Use one exact label-law interface to justify the coupling and avoid repeated state calculations downstream; this succeeds for the query upper bound. Replacing the full state assertion by a scalar law everywhere fails, as shown by the two-qubit example. The Boolean continuation proof is retained because it has a different consumer and error term.
- **difficulty_landscape_and_fertile_questions:** The ordinary finite-probability argument is exposed rather than left as an appeal to a search routine. The motivated near-term formal task is an output-subsystem-preserving compiler for the existing parameter-only amplification procedure. Its first discriminating obligation is factorization on each positive-mass first-success branch, with no retained output-label record that dephases that subsystem. No broader research programme or mathematical impossibility is claimed.
- **short_long_transfer_locators:** This return owns only the long-record §5. Its opening mechanism, theorem statements, and final fixed-parameter qualification can later support a short companion; the full constants, continuation induction, formal evidence, and failed label-to-state implication should remain recoverable here. No short companion was produced or assessed for consistency.
- **notation_definition_and_equation_grammar:** Base-two \(\log\) and natural \(\ln\) are distinguished at the section entrance. \(p,\gamma,\eta,M,N\), comparison weights, \(T,\varepsilon\), and the original/auxiliary registers are introduced before their principal uses. \(t\) as a stage length is local to the tournament subsection; the family parameter is reset at `upper-decode`. All probability divisions carry positive-denominator conditions. Source-level math syntax was reviewed; rendered equation layout was not.
- **first_time_reader_house_jargon_scan:** Ordinary mathematical descriptions carry the main proof. Stable claim identifiers and exact Lean names are retained for this long record, with the implementation/status discussion concentrated in §5.5. No reader is required to infer the mathematical mechanism from those identifiers. This is an internal source rereading, not a human comprehension test.
- **one_use_symbol_scan:** No disposable named construction was introduced merely to label one sentence. Local summation indices and intermediate variables in the arithmetic proof are used where they make the derivation recoverable. This was a qualitative manuscript scan, not a claimed exhaustive automated symbol analysis.
- **conditional_hypothesis_restrictiveness:** Stated. Dominance is required only to guarantee inclusion of a particular vertex; the algorithm and cap exist without it. Promised-input decoding correctness is separated from all-input execution. Probability range, positive conditioning, fixed success subspace, and fixed-\(k\) constants are explicit.
- **citation_role_checks:** The target preprint is identified by supplied PDF bytes and §3 locators. Earlier methods are cited with inspected edition/theorem/page roles. BHMT Theorem 12 is explicitly excluded as the amplification warrant. The HMW comparison retains its fixed-predicate premise. Writing exemplars are structural guidance and supply no quartic mathematics.
- **lean_statement_correspondence_and_validation_refs:** Principal anchors map to fully qualified declarations and complete available types in the companion correspondence. Source signatures with ambient variables are distinguished from types printed in the supplied native audit. The current root receipt, native type/axiom verdict, dependency export, and exact-name Comparator receipts are separate evidence dimensions; none was newly executed.
- **compressed_claim_occurrences_and_post_edit_scope_check:** The entrance and endpoint retain \(m=4^t\), \(t\ge1\), fixed \(k\ge2\), a chosen realizing circuit, and an all-input maximum-over-branches query cap. The list theorem has no verifier error; the Boolean endpoint does. The returned-state theorem is abstract-formally-supported and ordinarily reconstructed, while the missing full physical implementation remains explicitly open.
- **bibliography_render_check:** Bibliographic versions, source roles, and relevant theorem/page locators were checked through the recorded primary-source readings. No typeset bibliography or PDF bibliography was rendered or visually inspected in this return.
- **figure_and_reproducibility_check:** No generated scientific figure is required. The comparison table and rational example are reproducible from the supplied finite calculation artifact and are labeled as finite arithmetic. Computational success is not reported as universal proof, Lean validation, or circuit execution.
- **cold_reader_confusion_and_disposition:** Internal rereading identified possible confusion between the whole retained workspace and the original returned register, between a list theorem and a Boolean continuation, between logical reads and physical queries, and between historical comments and current evidence. The corresponding anchored repairs above were incorporated. Earlier draft math-delimiter and HMW-locator issues were also repaired. No independent human cold-reader pass occurred.
- **version_bound_review_coverage_and_omissions:** Current replacement §5 was reviewed in full. The packet's requested source and evidence scope is recorded by `source_read_receipt.json`; detailed formal-audit coverage distinguishes full proof reads from sampled declarations, metadata inspection, and extraction. The source preprint is the supplied edition with SHA-256 `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`. No separate pasted `.txt` attachment was accessible; its contents were not inferred. No whole-record, complete lower-bound, external dependency proof, or human review is claimed.
- **material_transition_warrants_and_source_conflicts:** Tensor norm multiplicativity and orthogonal slices justify the successful index masses; finite-pair symmetry gives drift; the dominant-weight lower bound legitimizes conditioning; an explicit coupling gives the miss bound; exact local-test equivalence gives sound verification; the compiler equation gives the factor of two. Current byte-bound native evidence supersedes historical compilation status without resolving the separate output-state semantics.
- **exact_open_boundary:** A parameter-only black-box procedure physically realizing the abstract amplification construction, with a fixed designated original output subsystem, successful component \(g_x\otimes\xi_x\), zero-success behavior, and the same all-input bounded oracle count under arbitrary-state compiler continuation. It is not an additional premise in Proposition 3.3's measured-label proof.
- **rendered_release_checks:** Not performed: revised-section PDF generation, visual page review, and independent human review. Source checks and finite arithmetic have their recorded scopes. This return is not a final integrated or render-approved paper.
- **deliberate_non_changes:** No source-preprint theorem was altered; no Lean source, repository docstring, baseline §2.3, other manuscript section, dependency, or original receipt was edited. No new verification status, novelty claim, author confirmation, publication, or acceptance was asserted.

### Mathematical understanding, taste, and fertility rubric

| Dimension | Disposition and concrete evidence | Reader check and limit |
|---|---|---|
| Mechanism and understanding | **Demonstrated within the revised argument.** `upper-weight-drift`, `upper-dominant-weight`, and `upper-coupling` expose why fractional comparisons suffice; `upper-returned-register` exposes what measured labels do not determine. | Reconstruct the pairwise cancellation and the event inclusion giving the miss bound; compare the two first-register density operators. This is not a human comprehension measurement. |
| Elegance and proof economy | **Demonstrated in a bounded reconstruction.** One label-law interface supplies the coupling; fixed-comparison bias amplification is unnecessary. The continuation induction remains because it explains a different endpoint. | Identify the hypotheses removed by the direct weight argument and the state information lost if the label-law simplification is used too broadly. No claim of an optimal proof is made. |
| Structural yield of search | **Not applicable as a search contribution.** No new optimized constant or searched mathematical witness is claimed. The cyclic example was chosen to reveal the absence of an ordering assumption. | The finite calculation checks the chosen example only; 138 and 6072 are deliberately loose analytical constants. |
| Transfer and connections | **Partial, precisely bounded.** The exact label law transfers to classical candidate selection and subsequent verification. Ordered minimum finding, exact tournament access, and bounded-error fixed-predicate search are related but do not automatically transfer to arbitrary comparison probabilities. | Check the common-object and hypothesis mapping at `upper-purpose` and `upper-bounded-error-comparison`. No new general transfer theorem is claimed. |
| Fertility and question selection | **Partial.** One concrete formal target is retained: the designated-output-state compiler bridge. Its first test is the branchwise factorization/routing obligation. | Either a proof or a counterexample to a proposed implementation would clarify which retained records must be uncomputed. No completed Lean proof or wider programme is claimed. |
| Difficulty landscape and negative knowledge | **Demonstrated within scope.** The text separates routine finite algebra from the exact conditional law and the retained-state interface. It records why expected-time search, a fixed-orientation assumption, and label-law equality do not substitute for the required statements. | Each rejected substitution has a named missing hypothesis or concrete state witness. Historical build failure and inaccessible material are not treated as mathematical barriers. |
| Digestion and shared reuse | **Partial.** The ordinary proof, exact finite example, source correspondence, citations, and open boundary can be reconstructed without private tools. | A reader can recompute the weights and integer budget; full publication readiness remains unestablished because no rendered revised PDF or independent human review was obtained. |
