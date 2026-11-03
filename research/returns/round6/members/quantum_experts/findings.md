# Located expert-panel findings

Machine-readable authority: findings.json. These are source-grounded perspectives, not reported reactions from the named authors. The primary locator always quotes current Markdown. Additional locators consolidate repeated recommendations.

## Index

| ID | Document | Kind | Priority | Location |
|---|---|---|---|---|
| [QX-001](#qx-001) | exposition | evidence_presentation | high | §7, last sentence |
| [QX-002](#qx-002) | expert_companion | evidence_presentation | medium | 4 The quantum upper bound |
| [QX-003](#qx-003) | reasoning_record | missing | high | §7.2 Excluding all smaller universal powers |
| [QX-004](#qx-004) | reasoning_record | overweighted | high | Reading guide; §1.1 Dependencies and proof recovery |
| [QX-005](#qx-005) | expert_companion | underweighted | medium | 1.3 What is new |
| [QX-006](#qx-006) | expert_companion | evidence_presentation | medium | Appendix A, Reproducing the check |
| [QX-007](#qx-007) | exposition | unclear | medium | §7, auxiliary amplifier |
| [QX-008](#qx-008) | reasoning_record | evidence_presentation | high | §2.9 The checked statements |
| [QX-009](#qx-009) | expert_companion | question | medium | 2 The construction, property (ii) |
| [QX-010](#qx-010) | exposition | unclear | medium | §4, Sampling a pivot quantumly |
| [QX-011](#qx-011) | exposition | underweighted | medium | §4, end of ideal-process example |
| [QX-012](#qx-012) | exposition | underweighted | medium | 4 The quantum algorithm: a tournament |
| [QX-013](#qx-013) | expert_companion | question | medium | 4.2 A tournament with probabilistic comparisons |
| [QX-014](#qx-014) | expert_companion | question | medium | 2 The construction, property (iii) |
| [QX-015](#qx-015) | expert_companion | underweighted | medium | 1.3 What is new |
| [QX-016](#qx-016) | expert_companion | underweighted | medium | §1.1 The history |
| [QX-017](#qx-017) | expert_companion | overweighted | medium | Abstract and §1, explicit refinements |
| [QX-018](#qx-018) | expert_companion | misplaced | medium | §3 Where a natural shortcut fails |
| [QX-019](#qx-019) | expert_companion | misplaced | medium | 4 The quantum upper bound |
| [QX-020](#qx-020) | exposition | overweighted | medium | 4 The quantum algorithm: a tournament, Amplification with a fixed cap |
| [QX-021](#qx-021) | expert_companion | overweighted | medium | 4.3 Verification and the query count |
| [QX-022](#qx-022) | exposition | unclear | medium | Overview, after one-line arithmetic |
| [QX-023](#qx-023) | exposition | unclear | medium | Overview, intended audience |
| [QX-024](#qx-024) | exposition | overweighted | medium | Overview, example map |
| [QX-025](#qx-025) | exposition | overweighted | low | §2, board size and transcripts |
| [QX-026](#qx-026) | exposition | overweighted | medium | §7, audit reading route |
| [QX-027](#qx-027) | expert_companion | overweighted | medium | Appendix A, opening audit promise |
| [QX-028](#qx-028) | reasoning_record | missing | medium | §4.2 Columns and their selected cells |
| [QX-029](#qx-029) | reasoning_record | underweighted | medium | §2.5 Renaming coordinates and deferring measurements |
| [QX-030](#qx-030) | reasoning_record | overweighted | medium | §3.4 The exact Boolean circuit |
| [QX-031](#qx-031) | reasoning_record | overweighted | low | §3.5 A complete check of the smallest nontrivial instance |
| [QX-032](#qx-032) | reasoning_record | question | medium | §3.8 Gaussian and Stein identities |
| [QX-033](#qx-033) | reasoning_record | misplaced | medium | §3.16 Literature comparison and the scope of the conclusion |
| [QX-034](#qx-034) | reasoning_record | misplaced | medium | §6.6 The discrepancy contradiction and the floors |
| [QX-035](#qx-035) | reasoning_record | overweighted | low | §3.16 Formal and evidential scopes |
| [QX-036](#qx-036) | reasoning_record | misplaced | low | 5.1 Amplification with a fixed stopping time |
| [QX-037](#qx-037) | reasoning_record | unclear | medium | §5.6 Optional: the Boolean continuation used by the formal headline |
| [QX-038](#qx-038) | expert_companion | keep | keep | §1.2 The key mechanism; developed in §4.1 Comparisons |
| [QX-039](#qx-039) | expert_companion | keep | keep | 4.2 A tournament with probabilistic comparisons, Exact sampling |
| [QX-040](#qx-040) | expert_companion | keep | keep | 4.2 A tournament with probabilistic comparisons, Coupling |
| [QX-041](#qx-041) | reasoning_record | keep | keep | 5.4 Coherent access and the query cap |
| [QX-042](#qx-042) | reasoning_record | keep | keep | 3.3 The quantum promise algorithm, including amplification and coherence |
| [QX-043](#qx-043) | exposition | keep | keep | §1, scope of small example |
| [QX-044](#qx-044) | exposition | keep | keep | §2, The domain bit is needed |
| [QX-045](#qx-045) | exposition | keep | keep | §4, Beating every rival is not winning |
| [QX-046](#qx-046) | exposition | keep | keep | §6, quantifier counterexample |
| [QX-047](#qx-047) | reasoning_record | keep | keep | §5.2 Bounded-error comparison discussion |
| [QX-048](#qx-048) | reasoning_record | keep | keep | §5.4 Coherent access and the query cap |
| [QX-049](#qx-049) | reasoning_record | keep | keep | §3.10 Moving the derivative through the blocks |
| [QX-050](#qx-050) | reasoning_record | keep | keep | §4.5 A shallow lookup can have large support |
| [QX-051](#qx-051) | reasoning_record | keep | keep | §4.2 Totality and uniqueness |
| [QX-052](#qx-052) | expert_companion | keep | keep | §1 and §7, common circuit |

## QX-001

**evidence_presentation · high · P-MODEL**

**Locator:** `repository/docs/exposition.md`, §7, last sentence, line 269.

> No recorded statement review yet covers the four compared theorems or these two statements

**Finding.** The exposition says no statement review covers the headline and two auxiliary results, but the supplied round-five statement-fidelity report explicitly reviews all of them. The expert companion now cites that report. This is a stale evidence-status sentence, not a missing proof check.

**Why it matters.** A reader deciding what still needs human scrutiny receives incompatible accounts of which comparison of statements has already been performed.

**Direction.** Reconcile this sentence with the exact supplied review and edition. Keep its machine-generated character separate from the still-absent independent human review; no fresh Lean run is needed for this correction.

**Prior-round boundary.** ES-028/029 and QM-019 addressed reading routes; this is a new inconsistency in the review status after integration.

**Evidence:**

- previous_round/round5_statement_fidelity.md, The four compared theorems and Other cited results: all four headline targets, uniformOpaqueAmplifier, Samples.amplify and the finite-seed direct-product endpoint.

- repository/docs/expert_companion.md, Appendix A, paragraph after Table 2: review of every cited statement, made without a person.

## QX-002

**evidence_presentation · medium · P-AMP**

**Locator:** `repository/docs/expert_companion.md`, 4 The quantum upper bound, line 147.

> Lean proves this label law and also the full form of the lemma

**Finding.** Which representation does “full form” mean here: the real retained-factor theorem for an opaque preparation, or a complete physical bit-oracle wrapper with a designated returned subsystem? The former is present and compared; record §5.5 expressly withholds the latter. The first compact claim needs that distinction.

**Why it matters.** The current record correctly says the remaining physical-state specification is not an assumption of the final upper bound. Delaying that role distinction can make a stronger auxiliary contract look like a gap in the sufficient measured-label route.

**Direction.** Qualify the representation at this first claim and route the reader directly to the existing abstract/physical distinction in record §5.5. State that the measured-label interface suffices for the headline theorem. Request no new formalization and do not reopen the supplied execution receipts.

**Prior-round boundary.** QM-018/019/025 repaired links and separated state and label statements. The remaining issue is abstraction-level wording at the first full-form claim, not failure of the recorded comparisons.

**Also located at:**

- `repository/docs/reasoning_record.md`, §5.5 Formal correspondence and the remaining state specification, line 2749: “the remaining full-state specification is not an extra assumption of the final upper bound.”

**Evidence:**

- Current record §5.5, #upper-current-formal-scope: bounded_amplification, Samples.amplify and quantum_amplify_samples have different interfaces.

- Current record #upper-missing-physical-state, final paragraph: uniformOpaqueAmplifier is compared but no full physical factorization theorem is claimed.

- Current expert Appendix A Table 2, Lemma 2 rows; prior statement-fidelity review.

## QX-003

**missing · high · P-SEP**

**Locator:** `repository/docs/reasoning_record.md`, §7.2 Excluding all smaller universal powers, line 3892.

> A family with a quantitative schedule \(k=k(t)\) requires additional uniform estimates and is a separate result.

**Finding.** The current companion §7 now gives a quantitative growing-k schedule using its uniform supplier and the explicit exponential quantum constant. Where is the detailed recovery of that existing remark in the document described as the complete reasoning record?

**Why it matters.** The record's fixed-k proof is correct and sufficient for α_tot=4. But a reader following the newer short-paper remark cannot recover its schedule, conditions and scope from this endpoint, which still only says that such a result is separate.

**Direction.** Cross-link and document the existing companion remark and its already-named uniform ingredients in the record's appropriate optional route. Keep the fixed-k theorem path unchanged and do not request a new theorem, stronger bound, or formalization.

**Prior-round boundary.** No matching fixed finding was reissued.

**Evidence:**

- Current record §§1 and 7, especially line 3892; current expert_companion.md §7, line 283.

- Current companion explicitly uses Q(F_{k,m})≤2^53 k·2^{10k}√mℓ^6 and k=⌊√(t/20)⌋.

- SSW Introduction §1.2 and §1.9, supplied lines 55–64 and 202, carefully distinguishes fixed query count from growing-parameter separations.

## QX-004

**overweighted · high · P-LOWER**

**Locator:** `repository/docs/reasoning_record.md`, Reading guide; §1.1 Dependencies and proof recovery, line 19.

> Forrelation ingredient: promise, decoder and circuit

**Finding.** The first route calls §§3.6–3.15 required, whereas §1.1 and the three-property preview explicitly permit accepting the hardness supplier and continuing to §4. Which route should a quantum specialist actually follow? The first guide also sends its complete-proof route through the known universal-bound reconstruction.

**Why it matters.** The opening instruction can send a reader through roughly fourteen historical PDF pages of supplier recovery before the new totalization, despite the improved skip routes farther down. It makes completeness look like a requirement to read everything.

**Direction.** Make the first guide distinguish a first pass through the new mechanism from full dependency recovery. Keep the already-present supplier preview, stable anchors, full proof, and Appendix A; reconcile rather than add another route table.

**Prior-round boundary.** R5 LR-006, LR-007 (navigation_b), LR-016 and LR-037 added useful routes/preview. This is an inconsistency between those successful additions and the unchanged 'Required' column, not a claim that routes are absent.

**Evidence:**

- Current record lines 14–23, 121–134, 518–539 and §3.17.

- Bansal–Sinha, supplied arXiv v3, Introduction / Theorem 1.3 and Corollary 1.4 (extracted lines 52–84) supplies the standard partial-function input.

- The current record explicitly permits accepting property 1 and continuing to §4.

## QX-005

**underweighted · medium · P-CERT**

**Locator:** `repository/docs/expert_companion.md`, 1.3 What is new, line 69.

> keep the candidates that beat every pivot selected so far

**Finding.** The closest antecedent is named correctly, but its mathematical relation to the new process remains implicit. A reader of AIK would ask: is the essential replacement the hard membership indicator of U(W) by the soft product of actual comparison probabilities, together with a distinguished candidate whose mass survives?

**Why it matters.** The reader must reconstruct the conceptual step from the related-work paragraph and the later weight update. This is the main reason for that expert to read the companion, and deserves more space than the amplifier constants.

**Direction.** Connect the existing AIK candidate-set invariant to the existing product-weight invariant at the introduction to Proposition 3. Explain the roles of fixed membership, fractional mass and the winner guarantee. Keep the attribution and do not assert a general new theorem beyond the supplied proposition.

**Prior-round boundary.** QM-015/016 were fixed by adding the antecedents and accurate hypotheses. This finding concerns the explanatory connection after that fix, not absence or misattribution of those antecedents.

**Evidence:**

- AIK2026 v2, §6.1, equations (3)–(4), printed p.12: U(W) consists of vertices defeating every previous pivot; §6.2, equations (8)–(10), pp.14–15: bounded point probabilities and candidate-set shrinkage.

- Current record §5.2, #upper-ideal-process and #upper-stage-law.

- Current expert §1.3 accurately distinguishes fixed intended edges from arbitrary loser probabilities.

## QX-006

**evidence_presentation · medium · P-MODEL**

**Locator:** `repository/docs/expert_companion.md`, Appendix A, Reproducing the check, line 351.

> the commit the links point to

**Finding.** The reproduction paragraph equates its first-line commit with the link revision, but the comment names 659b571 and the pinned source links use e9dfefbf11e6d1f380f122caa2349d4be78f2c1f.

**Why it matters.** A reader reproducing the stated reading route cannot tell whether the comment denotes a recorded execution, linked source or current packet snapshot. This is a local provenance inconsistency; it is not evidence that a proof or comparison failed.

**Direction.** Correct the obsolete equation of revisions and label recorded-run, linked-source and packet revisions by role. Use existing source/status information; no new receipt execution is requested.

**Prior-round boundary.** New current-text finding; not a repeated round-five defect.

**Evidence:**

- Current expert Appendix A lines 351–357 and generated link definitions from line 371 onward; the cmp-amplifier link alone establishes the different pinned revision.

- SOURCE_STATUS.json records packet repository_commit 9bdd443ce9b5e2fa5a83d63e0bcb0d87fbed298a. Different documentary revisions can legitimately coexist.

## QX-007

**unclear · medium · P-MODEL**

**Locator:** `repository/docs/exposition.md`, §7, auxiliary amplifier, line 269.

> has a stronger conclusion than Section 4 states

**Finding.** Section 4 now explicitly states that each successful outcome returns g itself and gives a p-independent finite procedure. Calling the auxiliary Lean result stronger because it returns the original good state obscures which additional precision is intended, particularly exact success mass and an explicit retained-register specification.

**Why it matters.** The headline relation is hard to assess, especially because the paragraph also states a narrower class of success projectors.

**Direction.** Compare components separately: what the current ordinary lemma already asserts, the measured-label law used downstream, exact success mass, explicit retained-register specification, and the narrower finite basis-predicate setting. No new formalisation is needed.

**Prior-round boundary.** ES-024 moved the separate returned-state remark to §7, but §4 still states the returned-state conclusion; assess the relation after integration.

**Evidence:**

- repository/docs/exposition.md §4 Amplification with a fixed cap: every successful outcome returns g itself.

- repository/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean, uniformOpaqueAmplifier.

- previous_round/round5_statement_fidelity.md Other cited results, coherent and measured amplifier rows.

## QX-008

**evidence_presentation · high · P-AMP**

**Locator:** `repository/docs/reasoning_record.md`, §2.9 The checked statements, line 508.

> no review; partial by construction

**Finding.** The current entry table calls uniformOpaqueAmplifier unreviewed/partial, labels the uniform Forrelation endpoint unreviewed against a catalogue row, and marks the constants theorem's review noncurrent. The current companion and the supplied round-five statement-fidelity review already give substantive relation judgments for these declarations. Is 'no review' only a frozen corpus field or a claim about the present packet?

**Why it matters.** This is the first formal trust checkpoint. A reader can mistake an old ledger status for an unresolved mathematical or statement-fidelity problem and then find a different verdict in Appendix A of the companion.

**Direction.** Separate execution status, frozen corpus-review status, and current independent statement-fidelity judgment in the existing table. Reconcile the existing supplied judgments and keep their dates/scopes; do not rerun receipts or promise new formalization.

**Prior-round boundary.** R5 LR-007/LR-028 successfully created the table; the issue is inconsistent time/scope labels in its present contents, not an absent index or missing receipts.

**Evidence:**

- Current record §2.9 lines 498–514, especially uniformOpaqueAmplifier, forrelation_lower_uniform_sharp and construction_family_named rows.

- Current expert_companion.md Appendix A, Table 2, lines 335–345.

- previous_round/round5_statement_fidelity.md rows for uniformOpaqueAmplifier (line 23), direct_product_external_finite_realized_caps (line 25), construction_family_named (line 27), and forrelation_lower_uniform_sharp (line 28).

## QX-009

**question · medium · P-FORR**

**Locator:** `repository/docs/expert_companion.md`, 2 The construction, property (ii), line 99.

> measures the projection onto $u$, which succeeds with probability $\Phi^2$

**Finding.** Why choose the squared projection experiment rather than the familiar sign-sensitive interference experiment with probability (1+Phi)/2 and ceil(k/2) queries? The record answers which experiment is used, but the short paper leaves a Forrelation expert to discover that explanation separately.

**Why it matters.** The negative-Phi example and the exact domain circuitry can look like an artefact of an unnecessarily sign-blind decoder. A signed promised decoder would still not certify the exact promise on all inputs; that is the useful distinction.

**Direction.** Expose the existing record comparison at the first projection experiment. Explain the role of following the preprint’s simple fixed-k decoder and preserve the independent obligation of exact domain certification. Do not propose or analyze a new decoder.

**Prior-round boundary.** New reader-value finding; does not repeat a repaired round-five mathematical defect.

**Also located at:**

- `repository/docs/exposition.md`, §1, projection experiment, line 74: “It succeeds with certainty on both $a^+$ and $a^-$.”

**Evidence:**

- Current record §3.3 final paragraph, #forr_coherent: AA Proposition 6 versus the projection experiment.

- AA2018, §3.2, Figure 1 and Proposition 6; Bansal–Sinha Proposition 1.2, read directly in the supplied extraction.

- OpenAI supplied preprint §2.1, Lemma 2.1(ii)–(iii), pp.4–5.

## QX-010

**unclear · medium · P-MODEL**

**Locator:** `repository/docs/exposition.md`, §4, Sampling a pivot quantumly, line 179.

> On success the algorithm appends that column and continues;

**Finding.** This is where the coherent preparation becomes a classical pivot history, but the exposition does not explicitly say that the successful index is measured. Retaining decoder registers within a trial and measuring pivots between trials have different roles.

**Why it matters.** The reader can confuse coherence required for A and A^-1 with a requirement to keep the whole adaptive tournament coherent, making the later measured-label theorem appear insufficient.

**Direction.** Make the existing measurement boundary explicit and explain that fresh preparations use the resulting classical pivot list. Preserve coherence inside each amplification call.

**Prior-round boundary.** QM-008/ES-003 explain retained workspace within comparisons. This identifies the distinct between-stage boundary.

**Evidence:**

- repository/docs/reasoning_record.md §5.2, upper-stage-state and upper-quantum-tournament: fixes a classical pivot list and says to measure the index on success.

- literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md Chapter 7, Amplitude amplification: the inverse requires a unitary preparation.

## QX-011

**underweighted · medium · P-AMP**

**Locator:** `repository/docs/exposition.md`, §4, end of ideal-process example, line 171.

> the next pivot is the winner with probability $(1-\varepsilon)/(2-\varepsilon)$

**Finding.** The added fractional example supplies the conditional pivot probability but omits the associated unamplified success mass. The reader must connect the example to the sampler without seeing both quantities at once.

**Why it matters.** The central distinction between obtaining any sample and the conditional distribution of that sample is stated abstractly rather than executed on the running numbers.

**Direction.** Use the record’s existing W/4=23999/48000 calculation alongside 11999/23999 and 12000/23999 to connect this example to the sampler. Identify it as an abstract comparison-table example, as the record does.

**Prior-round boundary.** QM-013 added the conditional probability. This identifies its remaining missing connection to sample availability; no new example is requested.

**Evidence:**

- repository/docs/reasoning_record.md §5.2 upper-cyclic-example: W=23999/12000, unamplified success W/4, and both conditional probabilities; explicitly not a full addressed-certificate input.

## QX-012

**underweighted · medium · P-ROBUST**

**Locator:** `repository/docs/exposition.md`, 4 The quantum algorithm: a tournament, line 171.

> If the winner wins only with probability $1-\varepsilon$

**Finding.** The current fractional variant is useful, but it changes only the winner’s comparisons; loser–loser comparisons in the displayed example remain deterministic. What should a reader look at to understand the distinct permission for an unbiased loser pair, which is the obstruction to directly using bounded-error fixed-predicate search?

**Why it matters.** The cycle demonstrates lack of an order, and the trailing variant demonstrates nonuniform weights. Neither example by itself identifies the no-margin loser case, so an expert may remember the corrected caveat without seeing how the same drift and sampler tolerate it.

**Direction.** Keep both existing examples and distinguish their jobs explicitly from the no-margin hypothesis. Tie the existing loser-probability discussion to the general product and drift formulas, which already cover probability one half; do not claim a cycle establishes the bounded-error obstruction or request a new construction.

**Prior-round boundary.** QM-013 added the fractional variant and QM-003/017 correctly separated cycles from no-margin comparisons. This is weighting of the corrected material, not a request to restore those fixes.

**Evidence:**

- Current exposition §4 ideal-process table and fractional sentence.

- Current record §5.2 #upper-cyclic-example: weights (11999/12000,0,0,1) and conditional probabilities 11999/23999,12000/23999.

- HMW2003 §1 and §3 assume bounded-error access to fixed predicates.

## QX-013

**question · medium · P-KING**

**Locator:** `repository/docs/expert_companion.md`, 4.2 A tournament with probabilistic comparisons, line 160.

> returns at most $T$ candidates

**Finding.** Why is the reusable interface a short list rather than the single source or king returned by the closest search algorithms, and what guarantee survives when no dominant candidate exists?

**Why it matters.** The reader should not equate a list-membership guarantee conditional on dominance with the total search relation KING. This also explains why terminal sampler failure is harmless after selection and why verification is a separate obligation.

**Direction.** Make the comparison of output contracts explicit beside Proposition 3 or its antecedent comparison: list length and cap are unconditional, containment is conditional, and the final exact tests decide F. Use the already proved contract rather than promise a general king finder.

**Prior-round boundary.** New reader-value finding; does not repeat a repaired round-five mathematical defect.

**Evidence:**

- MPS2023, supplied arXiv v1, Definition 1.1 and Theorem 1.2; published Theorem 19 and Algorithm 4, pp.30:11–30:13.

- AIK2026 v2, Algorithm 4 and Lemma 6.6, pp.12,15–16: last selected vertex is the source on a positive input.

- Current expert §4.3; current record #upper-tournament-statement, #upper-quantum-tournament and #upper-verification-proof.

## QX-014

**question · medium · P-FORR**

**Locator:** `repository/docs/expert_companion.md`, 2 The construction, property (iii), line 101.

> An exact fan-in-two Boolean circuit

**Finding.** Which part of the quantum speedup needs the nearly linear circuit size, as opposed to merely the existence of an exact domain-and-value circuit? This is the reason the specialist should care about the circuit construction at all.

**Why it matters.** Without connecting S to the number K of local checks and hence the verification cost, the explicit integer arithmetic and circuit size can look like formalization detail unrelated to the quantum mechanism.

**Direction.** At the circuit property or local-test count, point to the existing dependency S to K to the cost of verifying the short list. Keep the exact domain requirement separate from the quantitative size requirement; leave the gate arithmetic in the record.

**Prior-round boundary.** New reader-value finding; does not repeat a repaired round-five mathematical defect.

**Evidence:**

- Current expert §2 property (iii), K=m+(m-1)+r(S+2), and §4.3 verification.

- Current record §3.4 and §5.4 #upper-finite-budget.

- OpenAI supplied preprint Lemma 2.1(iii), Lemma 2.2 and Proposition 3.3.

## QX-015

**underweighted · medium · P-CERT**

**Locator:** `repository/docs/expert_companion.md`, 1.3 What is new, line 69.

> both separate certificate complexity $C$ from $R$ and $Q$

**Finding.** The measure distinction is correctly stated, but the comparison would be more informative if it showed why the nearby quartic C-versus-Q result did not already give the present R-versus-Q exponent. The missing ingredient is randomized address hardness across many candidate columns.

**Why it matters.** Readers need to place the new randomized lower bound against a construction that already has sqrt(n) quantum cost and n^2 certificate complexity. Naming the changed letter alone does not identify the changed obstruction.

**Direction.** Use the already published parameter comparison from BDK Theorem 1, and connect it to the existing mL charge in this construction. Do not add a new theorem or claim a general limit on the certificate-complexity approach.

**Prior-round boundary.** QM-015/016 added correct antecedent credit and identified C as the classical measure. This asks for a quantitative mechanism comparison beyond that repaired attribution.

**Evidence:**

- BDK2026 supplied text, Theorem 1: C=Omega(n^2), R=tilde O(n), Q=tilde O(sqrt n), with Lemmas 3 and 5.

- AIK2026 v2 introduction, pp.1–2, distinguishes certificate, randomized and quantum measures.

- Current expert §1.2 and §§5.2–5.4 explain the independent addressing cost.

## QX-016

**underweighted · medium · P-SEP**

**Locator:** `repository/docs/expert_companion.md`, §1.1 The history, line 44.

> Improved partial separations then gave $8/3-o(1)$ and $3-o(1)$ in this framework

**Finding.** The 5/2 and 3 calculations are explicit, but the 8/3 step is only named. Which partial-hardness exponent changes at that step, and which outer cost stays the same?

**Why it matters.** The history table otherwise looks like a sequence of improved numbers. This reader wants to see why improving the partial supplier reached the cube, whereas the new per-column addressing changes the outer bottleneck.

**Direction.** Complete the existing parameter comparison with the intermediate c=2/3-o(1) row of the cited 2+c conversion. Distinguish this particular cheat-sheet route from a universal impossibility claim about all cheat-sheet constructions.

**Prior-round boundary.** New current-text finding; not a repeated round-five defect.

**Evidence:**

- ABK supplied v2, §3.1, composition with AND–OR and certificate checking.

- Tal supplied v1, Introduction / total-function application: partial exponent c yields the cited total exponent 2+c.

- Current expert §1.1 already derives the endpoint c=1/2 and c=1 cases; preserve those repairs.

## QX-017

**overweighted · medium · P-MIN**

**Locator:** `repository/docs/expert_companion.md`, Abstract and §1, explicit refinements, line 9.

> This companion gives the argument with explicit constants

**Finding.** Are the explicit constants a primary reason this audience should read the companion? The opening advertises them and immediately lists 6, 1/400 and 13669 k², before the reader has evaluated the weighted-comparison mechanism.

**Why it matters.** These are useful quantitative recoverability facts, but they are deliberately nonoptimal and do not explain the improvement from the cubic route. Their current emphasis competes with the document’s strongest contribution as an explanation.

**Direction.** Keep the precise refinements and their built/compared distinctions in an accessible quantitative route. Rank the weighted sampler, stopped coupling and distributed classical address cost ahead of the numerical constants in the statement of reader value.

**Prior-round boundary.** New current-text finding; not a repeated round-five defect.

**Evidence:**

- Current expert abstract, §1 paragraph beginning The proofs below, §4.3 and §6.

- DH supplied v2 presents the task and algorithm before its rank/cost calculation; this is a functional comparison, not a universal page-length rule.

## QX-018

**misplaced · medium · P-MIN**

**Locator:** `repository/docs/expert_companion.md`, §3 Where a natural shortcut fails, line 120.

> Each row of Table 1 is a step a reader may be tempted to simplify

**Finding.** Does the reader need all eight counterexamples before entering the quantum proof? Rows 4–7 and the detailed conditioning example concern lower-bound objects whose role has not yet been developed.

**Why it matters.** The table contains valuable corrected material, but a quantum reader is asked to switch to planting, per-instance caps and conditional hardness at the moment they want the probabilistic comparison algorithm.

**Direction.** Keep the quantum warnings at their first use and route the classical rows to §5 or their existing record destinations. Preserve the counterexamples and their repaired hypotheses; reduce front-loaded interruption rather than delete safeguards.

**Prior-round boundary.** Round five repaired several of these examples. Their correctness is accepted here; this concerns placement of the repaired table.

**Evidence:**

- Current expert Table 1, rows 1–8, and the following sixteen-input conditioning calculation.

- Current exposition §5 places the cap and independence examples beside the simulator obligations.

## QX-019

**misplaced · medium · P-AMP**

**Locator:** `repository/docs/expert_companion.md`, 4 The quantum upper bound, line 139.

> with a fixed-cap amplifier, a comparison of two columns

**Finding.** The quantum section enters through a standard amplification lemma and its proof before exposing the comparison theorem. A specialist already knows the two-dimensional Grover analysis; their first question is what replaces a fixed comparison predicate and which sampling contract the new drift argument consumes.

**Why it matters.** The ordering makes the familiar tool appear to carry the novelty and postpones the reason to care about its exact conditional law.

**Direction.** Give the tournament interface and its need for law-preserving capped sampling before the optional geometric proof, or provide a clearly marked specialist path from the lemma contract directly to §4.2. Retain the all-input cap and exact-law clauses. In the complete record, preserve the full proof but label the standard rotation and scalar derivations as optional recovery after the precise contract.

**Prior-round boundary.** New reader-value finding; does not repeat a repaired round-five mathematical defect.

**Also located at:**

- `repository/docs/reasoning_record.md`, §5.1 Amplification with a fixed stopping time, line 2139: “We give OpenAI's bounded construction in full.”

**Evidence:**

- BHMT2000 v1, §2, Lemma 1 and equation (8), pp.5–7, supplies the standard successful-component geometry.

- MPS2023 §1.2.2 introduces the algorithm by obstacles in sampling and counting before its Grover preliminaries.

- Current expert Lemma 2 and §4.2.

## QX-020

**overweighted · medium · P-AMP**

**Locator:** `repository/docs/exposition.md`, 4 The quantum algorithm: a tournament, Amplification with a fixed cap, line 181.

> a trial succeeds with probability at least $9/40$

**Finding.** The standard amplifier’s numerical trial constants occupy more attention than their role requires in this examples-first route. The payoff is a cap for all inputs plus the unchanged conditional label law, not the number 9/40 or the logarithm of 40/31.

**Why it matters.** The reader must parse fresh constants immediately after the novel sampling/coupling mechanism and before verification, interrupting the mechanism they are trying to retain.

**Direction.** Keep the contract and the invariant good component in the main path; make numerical repetition arithmetic a clearly optional pointer to record §5.1. Reuse the freed space for the existing fractional sampling example.

**Prior-round boundary.** New reader-value finding; does not repeat a repaired round-five mathematical defect.

**Also located at:**

- `repository/docs/exposition.md`, §4, Amplification with a fixed cap, line 181: “a trial succeeds with probability at least $9/40$ whenever $p\ge\gamma$”

**Evidence:**

- Current exposition §4 amplifier paragraph.

- BHMT2000 §2 and BBHT1996 §4 give the standard geometry and averaging ingredients.

- Current record #upper-grover-trial through #upper-amplification-proof contains the exact constants.

## QX-021

**overweighted · medium · P-KING**

**Locator:** `repository/docs/expert_companion.md`, 4.3 Verification and the query count, line 182.

> Nothing below depends on the logarithmic exponent.

**Finding.** Across the three documents, the deliberately loose exponent-six arithmetic receives more first-pass attention than its role requires. The actual decoder, inverse, sampler and verification ledger matters; the expanded scalar relaxation does not drive the separation.

**Why it matters.** It obscures the relevant economy: cheap comparisons generate only logarithmically many candidates, then verification is paid only for those candidates. It can also invite unhelpful attention to an unoptimized logarithmic exponent.

**Direction.** Keep the complete finite query budget, the fixed-k independence from m and the all-input cap. Give the expansion to exponent six a clearly marked recovery destination; do not replace the stated bound or request a sharper one.

**Prior-round boundary.** QM-012 correctly completed the query count. This finding preserves that visible total while reconsidering the amount of loose numerical relaxation in a specialist route.

**Also located at:**

- `repository/docs/reasoning_record.md`, 5.4 Coherent access and the query cap, line 2719: “We give the size arithmetic to make the independence of $C_k$ from $t$ explicit.”

- `repository/docs/reasoning_record.md`, §5.4 The explicit logarithmic exponent six, line 2725: “exactly the source's deliberately loose constant”

- `repository/docs/exposition.md`, §4, The count, line 189: “The exponent six is an artefact of this deliberately loose count.”

**Evidence:**

- Current expert §4.2 cost and §4.3 two paragraphs.

- Current record §5.4 #upper-finite-budget, #upper-asymptotic-bound and #upper-explicit-log6.

## QX-022

**unclear · medium · P-SEP**

**Locator:** `repository/docs/exposition.md`, Overview, after one-line arithmetic, line 32.

> locating it inside one column means naming an address, which costs $L$ queries there.

**Finding.** This intuition can still be read as a per-run necessity to learn the address before visiting its cell. Section 5 now correctly allows a lucky guess and bounds a joint event involving a cheap run and a true-cell query.

**Why it matters.** The opening mechanism is remembered as stronger than the actual lower-bound mechanism, even though the later probability argument is correct.

**Direction.** Carry the probability-aware qualification from Section 5 into the opening intuition while retaining the m·L versus √m arithmetic.

**Prior-round boundary.** CM-003/ES-004 repaired Section 5. This is an incomplete propagation to the Overview, not an error in the corrected proof.

**Evidence:**

- repository/docs/exposition.md §5, The true cell and The simulator: guessed addresses and the joint event are explicit.

## QX-023

**unclear · medium · P-MODEL**

**Locator:** `repository/docs/exposition.md`, Overview, intended audience, line 26.

> a graduate student who knows the query models above

**Finding.** The announced prerequisite is a query-model definition, while the sampler assumes reversible computation, retained workspaces, product states and amplitude amplification. Which operations should the reader already be able to execute?

**Why it matters.** A student may understand the eight-bit arithmetic yet stall at the sampler; an expert cannot tell which tutorial material they may safely skip.

**Direction.** Give a short operational prerequisite or precise optional prerequisite route. Do not expand the article into a quantum-computing tutorial.

**Prior-round boundary.** No matching repaired finding is reissued.

**Evidence:**

- literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md, Chapter 2 Quantum circuits and Chapter 7 Grover/Amplitude amplification.

- skills/record-to-expository/SKILL.md, Preconditions and inputs: graduate level is not an operational prerequisite ladder.

## QX-024

**overweighted · medium · P-MIN**

**Locator:** `repository/docs/exposition.md`, Overview, example map, line 43.

> The four-column board (Figure 2)

**Finding.** The Overview occupies about 1.81 page equivalents including title material; the first concrete example begins late on page 2. The theorem, payoffs paragraph, mechanism, history, cheat-sheet arithmetic and eight-row example map partly duplicate route information.

**Why it matters.** The reader gets a strong reason to read but waits too long to operate on the concrete object; the additional previews buy less than a worked sampler connection.

**Direction.** Compress overlapping route descriptions while preserving the theorem, mechanism and antecedent arithmetic. Reallocate space rather than add pages.

**Prior-round boundary.** No matching repaired finding is reissued.

**Evidence:**

- repository/docs/exposition.pdf pp. 1–2; §1 heading p. 2 at y≈639.66 on an 841.89-point page, measured from PDF text geometry.

- skills/record-to-expository/SKILL.md, Model the reader and frame the result: about a page before examples.

## QX-025

**overweighted · low · P-FORR**

**Locator:** `repository/docs/exposition.md`, §2, board size and transcripts, line 104.

> The board has $4(4+16+4(6+360))=5936$ bits.

**Finding.** What explanatory work does the exact 5936-bit total do beyond the gate count 180 and test count 371? Exact certificate semantics, local-test cost and scaling carry the quantum argument.

**Why it matters.** A specialist can mistake an implementation-size audit for the central proof parameter.

**Direction.** Keep the reproducible counts and checker destination as supporting material; prioritize what the domain/value tests certify and why K has the required growth.

**Prior-round boundary.** No matching repaired finding is reissued.

**Evidence:**

- repository/docs/exposition.md §2 Transcripts and Local tests; §3 final paragraph: the general input-size formula and K scaling already serve the asymptotic purpose.

## QX-026

**overweighted · medium · P-MODEL**

**Locator:** `repository/docs/exposition.md`, §7, audit reading route, line 265.

> Five definitions carry the content.

**Finding.** The essential model audit and four target statements are packed into a long paragraph, then followed by detailed stronger auxiliary forms. The oracle, all-branch cap, success measurement and headline quantifiers are harder to find than in the expert appendix.

**Why it matters.** This is the most likely stopping point for a reader who has followed the proof and wants a quick semantic audit.

**Direction.** Give the essential route visible structure and route detailed auxiliary comparisons to the existing expert appendix or record. Preserve the shared-modelling-error warning and precise theorem links.

**Prior-round boundary.** No matching repaired finding is reissued.

**Evidence:**

- repository/docs/expert_companion.md Appendix A, Object/Meaning table and Five things to check.

- repository/docs/exposition.pdf §7 pp. 12–13, about 0.87 page equivalents.

## QX-027

**overweighted · medium · P-MODEL**

**Locator:** `repository/docs/expert_companion.md`, Appendix A, opening audit promise, line 287.

> This appendix lists everything a reader must read to answer that question.

**Finding.** Which entries are needed for a first semantic check of Theorem 1, and which describe auxiliary comparisons? The appendix occupies about 2.35 of the supplied 14 pages, more than the entire quantum upper-bound section.

**Why it matters.** The definition map and five checks are unusually useful. Presenting all auxiliary relations and reproduction detail at equal priority can make that useful short route feel as large as the new algorithm itself.

**Direction.** Preserve the oracle/cap/probability map, common-circuit quantifiers and theorem actually used. Visibly subordinate auxiliary stronger-state, refined-constant and diagnostic entries to their existing exact destinations, without hiding any restriction of a used theorem.

**Prior-round boundary.** New current-text finding; not a repeated round-five defect.

**Evidence:**

- Current expert Appendix A, object table, four targets, five checks, Table 2 and reproduction block.

- Page geometry of the supplied expert PDF: Appendix A about 2.35 page equivalents, §4 about 1.82. These are layout estimates, not human-reading measurements.

## QX-028

**missing · medium · P-FORR**

**Locator:** `repository/docs/reasoning_record.md`, §4.2 Columns and their selected cells, line 1796.

> Column $i$ contains the following disjoint blocks of input bits.

**Finding.** How many physical input bits does this total function have? This standalone definition introduces m columns and 2^r separately stored cells per column but does not give the total n at this definition, although the companion already gives n=m[m+rkm+2^r((m−1)ℓ+rS)]=O_k(m^22ℓ^3).

**Why it matters.** A query-complexity reader needs to know immediately that m is not the total input length, and that neither address space nor certificate storage is being supplied by an implicit oracle.

**Direction.** Reuse or link the existing companion §2 input-size accounting at the layout definition. Explain its role in connecting the structured function to an ordinary n-bit function; no new asymptotic result is needed.

**Prior-round boundary.** No matching fixed finding was reissued.

**Evidence:**

- Current record §4.2, lines 1785–1804; §7.2 reindexes the finite coordinate set without the count.

- Current expert_companion.md §2, line 110 contains the exact formula and polynomial size bound.

- Aaronson–Ambainis, supplied arXiv v1, Introduction pp. 1–2 (extracted lines 47–85), explicitly distinguishes oracle models and input-size conventions.

## QX-029

**underweighted · medium · P-ROBUST**

**Locator:** `repository/docs/reasoning_record.md`, §2.5 Renaming coordinates and deferring measurements, line 307.

> The deferred-measurement bridge has a more specific guarantee than a statement that measurements may be postponed.

**Finding.** Can the fast model-audit route identify the exact boundary of this bridge before its construction: all-input acceptance masses for all starting vectors, a fixed sequence of controlled phase queries, and no final-state identity?

**Why it matters.** The intended reader already knows deferred measurement. Their genuine question is whether this formal model matches the ordinary bit-query model and whether a later retained-state use asks for more. The contract is present, but scattered across a technical induction, §§2.7–2.9 and §5.5.

**Direction.** Expose the existing bridge contract and the existing bit-query conversion together in the model navigation. Leave the isometry-extension induction available as recovery. Do not imply that acceptance-law equivalence proves preservation of the physical output subsystem.

**Prior-round boundary.** No matching fixed finding was reissued.

**Evidence:**

- Current record §2.5 lines 307–330 and §5.4 coherent-access/compiler discussion.

- Høyer–Mosca–de Wolf, supplied source, §2 (extracted line 21): fixed input-independent gates, ordinary bit oracle, output obtained from a designated final subsystem.

- Current companion Appendix A already offers a compact statement-model index that can be reused.

## QX-030

**overweighted · medium · P-FORR**

**Locator:** `repository/docs/reasoning_record.md`, §3.4 The exact Boolean circuit, line 790.

> Arithmetic using fan-in-two gates.

**Finding.** Can readers accept the exact domain/value circuit contract and its size bound before deciding whether to read the ripple-carry gate accounting? The main reason this classical circuit is present is to make certificate checking local, not to provide the quantum decoder.

**Why it matters.** The arithmetic consumes several pages before the total construction is introduced. A quantum reader may confuse gate-size certification with the cost of running a circuit coherently or with the query complexity of promise recognition.

**Direction.** Keep the exact two-output contract, signed endpoint handling, and O_k(m log²m) size statement visible. Offer the butterfly and gate-level arithmetic as proof recovery, with a forward pointer to how S enters K and verification.

**Prior-round boundary.** R5 compressed the elementary amplification derivation in §3.3; this concerns remaining gate-accounting weight in §3.4, not a request to remove endpoint correctness.

**Evidence:**

- Current record §§3.2–3.4 and §5.3; §5 entry lines 2113–2115 explains the use of S in the test count.

- Aaronson–Ambainis §3.2, supplied extracted lines 659–708, concerns the quantum alternating-phase experiment; the record's exact domain circuit serves a different construction role.

## QX-031

**overweighted · low · P-FORR**

**Locator:** `repository/docs/reasoning_record.md`, §3.5 A complete check of the smallest nontrivial instance, line 909.

> We can count all $16^2=256$ inputs without relying on a computer.

**Finding.** The three-row table already demonstrates the decisive phenomenon: a negative off-promise input has projection probability one while the exact circuit rejects its domain. Does a first-pass reader also need the full 256-input census before seeing a total column?

**Why it matters.** The census is a useful semantic audit but adds little to the algorithmic reason the domain bit is necessary. The chapter-level route currently invites reading all of §§3.1–3.5.

**Direction.** Keep the three contrasting inputs in the primary route and label the full census and checker comparison as optional audit material, preserving their existing argument and locator.

**Prior-round boundary.** R5 LR-052 kept the examples. Preserve the table and the audit; change their priority, not their mathematical content.

**Evidence:**

- Current record §3.5 lines 897–926.

- Aaronson–Ambainis §3.2 and Bansal–Sinha Introduction, supplied extracted lines 25–38, separate the promise definition from the quantum acceptance statistic.

## QX-032

**question · medium · P-LOWER**

**Locator:** `repository/docs/reasoning_record.md`, §3.8 Gaussian and Stein identities, line 1128.

> Formula (F9) makes a different choice, so its resulting distribution and moment bounds are proved here.

**Finding.** Why choose the algebraic truncation in (F9) instead of the Gaussian-CDF truncation used by Bansal–Sinha? The text carefully says that the resulting distribution is different and reproves its moments, but does not explain the design benefit the reader should look for.

**Why it matters.** An expert in the source proof sees a substantial alteration and needs a reason to invest in its new kernel identities and constants. Reproving the changed object establishes validity; it does not itself explain the choice.

**Direction.** State the documented mathematical or implementation reason for this existing choice, if there is one, and identify which later estimates it simplifies. If the choice was just convenient, say so without making a priority or novelty claim.

**Prior-round boundary.** No matching fixed finding was reissued.

**Evidence:**

- Current record §3.8, line 1128, and §3.16 lines 1689–1693.

- Bansal–Sinha, §1.2 'Improving δ to 2^{-O(k)}', supplied extracted lines 203–219, explicitly motivates the truncation by constant-variance rounding and the usable transformed integration-by-parts identity.

## QX-033

**misplaced · medium · P-LOWER**

**Locator:** `repository/docs/reasoning_record.md`, §3.16 Literature comparison and the scope of the conclusion, line 1689.

> The algebraic function (F9) used here defines a different hard distribution.

**Finding.** The source-to-reconstruction comparison is excellent but arrives after the whole long supplier proof. Can a reader see at its entrance which pieces are the published theorem, which proof method is reused, and which concrete distribution/derivative route is reconstructed here?

**Why it matters.** The combination of different truncation, first-block interpolation and an ordinary-tree martingale can otherwise look like either a literal transcription or an unexplained claim to a new lower-bound method.

**Direction.** Bring a compact version of the existing comparison to the §3.6 proof spine and leave full credit/pinpoints in §3.16. Preserve the explicit statement that the review establishes neither priority nor novelty.

**Prior-round boundary.** R5 corrected BS/SSW attribution and moved comparisons to Appendix E. Those corrections should stay; this asks for an early summary of the distinction already made.

**Evidence:**

- Current record §3.6 #forr_proof_spine, §3.8 line 1128, §3.16 lines 1689–1693.

- Bansal–Sinha supplied introduction/overview, lines 104–229; Girish–Tal–Wu §1.3, lines 127–159; Sherstov–Storozhenko–Wu §1.8–1.9, lines 184–202.

## QX-034

**misplaced · medium · P-LOWER**

**Locator:** `repository/docs/reasoning_record.md`, §6.6 The discrepancy contradiction and the floors, line 3710.

> The separate source audit of Bansal–Sinha v3 §5.4 concerns the displayed comparison at source lines 1180–1181:

**Finding.** Why reopen the version-specific logarithmic defect in the final assembly of the classical lower bound? The exact source line numbers and exponent difference repeat the forensic material already isolated in Appendix E.

**Why it matters.** At this stage the proof consumes only the fixed-k supplier established in §3. Reopening a source dispute breaks the short path from the generic planting theorem to the displayed family bound and can suggest that the current assembly still depends on resolving it.

**Direction.** Keep the fixed-k hypothesis and original-source credit at this use site; route the version-specific audit to the existing Appendix E. Do not delete the audit or imply a counterexample to the published theorem.

**Prior-round boundary.** R5 LR-036/LR-028 moved the main forensic discussion out of §3.16. This is a remaining duplicate at a different current use site, not a repetition of the fixed §3.16 complaint.

**Evidence:**

- Current record §6.6 #CL-forrelation-input, lines 3697–3710; Appendix E #forr_bs_mismatch.

- Bansal–Sinha supplied v3 final proof §5.4, extracted lines 1015–1019, is the exact displayed comparison under discussion.

## QX-035

**overweighted · low · P-LOWER**

**Locator:** `repository/docs/reasoning_record.md`, §3.16 Formal and evidential scopes, line 1702.

> Older prose calling this endpoint merely proposed is superseded by those source-matched records.

**Finding.** Does the specialist need the history of proposed status, root-build receipt, focused build, elaborated-type audit, recomputed hashes and later native execution at the end of the supplier proof, after §2.9 has already promised an authoritative current index?

**Why it matters.** The current mathematical/formal boundary is useful; repeated explanations of how old descriptions were superseded require the reader to reconstruct the project's chronology.

**Direction.** Keep the current declaration, its actual mathematical relation and its comparison/build category at this endpoint. Consolidate historical reconciliation and source-byte chronology into the already-existing Appendix F and current status index.

**Prior-round boundary.** R5 LR-019 substantially improved this by moving chronology. This identifies the remaining historical sentences, rather than asserting that all history is still in the proof.

**Evidence:**

- Current record §3.16 lines 1702–1704, §2.9 and Appendix F.

- previous_round/round5_statement_fidelity.md already gives the current uniform-estimate relation.

## QX-036

**misplaced · low · P-AMP**

**Locator:** `repository/docs/reasoning_record.md`, 5.1 Amplification with a fixed stopping time, line 2139.

> BHMT's Theorem 12 concerns amplitude estimation

**Finding.** The sentence correcting a citation to BHMT Theorem 12 reads like a response to a historical referee mistake, although the surrounding current argument cites the appropriate geometry and averaging results.

**Why it matters.** A first-time reader has no reason to suspect Theorem 12 is being invoked. The corrective aside increases the sense of accumulated review history inside a mathematical proof.

**Direction.** Keep the correct pinpoint citations in the proof and reserve the rejected-citation history for the existing execution or source-comparison apparatus if it must be retained.

**Prior-round boundary.** New reader-value finding; does not repeat a repaired round-five mathematical defect.

**Evidence:**

- Current record §5.1 opening citation paragraph.

- BHMT2000 §2 Lemma 1/equation (8), and §4 Theorem 12.

- Current record Appendix C already explains the editions and relevant locators.

## QX-037

**unclear · medium · P-AMP**

**Locator:** `repository/docs/reasoning_record.md`, §5.6 Optional: the Boolean continuation used by the formal headline, line 2786.

> This subsection is not needed for Proposition 3.2 or 3.3.

**Finding.** Optional for which reader? The subsection is optional for the ordinary mathematical proof, but it explains the acceptance guarantee of the actual implementation reached by the headline roots. The opening's unqualified optional label can send a formal auditor past the one route they came to inspect.

**Why it matters.** Two valid notions of proof route coexist. A specialist verifying the theorem and a reader checking the exact compiled derivation have different stopping points.

**Direction.** Qualify the existing route labels by reading goal and link directly from the headline-route row in §5.5. Keep the induction here rather than restoring it to the middle of the list proof.

**Prior-round boundary.** R5 LR-022/LR-024 intentionally moved this induction out of §5.2. That was an improvement; this asks for audience-specific labeling, not reversal.

**Also located at:**

- `repository/docs/reasoning_record.md`, 5.6 Optional: the Boolean continuation used by the formal headline, line 2786: “This subsection is not needed for Proposition 3.2 or 3.3.”

**Evidence:**

- Current record §5.5 route table and §5.6 lines 2784–2807.

- Current record explicitly identifies tournament_runs as reached by the headline roots.

## QX-038

**keep · keep · P-ROBUST**

**Locator:** `repository/docs/expert_companion.md`, §1.2 The key mechanism; developed in §4.1 Comparisons, line 61.

> whatever the rival's address inputs

**Finding.** Preserve the winner-only correctness argument. The true winner cannot be disqualified under any decoded rival label, and its own correct address supplies the zero that disqualifies that rival.

**Why it matters.** This is the semantic bridge that makes a partial-function decoder safe inside a total-function algorithm. It explains the outward direction of the pointers in the language a quantum algorithm designer needs.

**Direction.** Keep the local two-direction argument together with the coherent comparison contract and its link; do not replace it with an assertion that all comparisons can be amplified.

**Prior-round boundary.** Preserve the successful QM-027 correction and its current exact hypotheses.

**Evidence:**

- Current expert §4.1; record #upper-winner-dominates.

- HMW2003 fixed-predicate bounded-error hypothesis is different.

## QX-039

**keep · keep · P-AMP**

**Locator:** `repository/docs/expert_companion.md`, 4.2 A tournament with probabilistic comparisons, Exact sampling, line 169.

> The algorithm never computes the weights.

**Finding.** Preserve the exact construction of the desired law from fresh comparison workspaces. The displayed success-and-label mass explains how physical queries realize the analytical weights without estimating them.

**Why it matters.** This is substantially more valuable to the target community than a generic appeal to quantum search: it exposes the input-dependent preparation, inverse availability and exact conditional law in one place.

**Direction.** Keep the tensor display and the w_i/m to w_i/W calculation visible, with fixed input and history stated. Preserve the parallel fixed-input/history explanation in the exposition and record.

**Prior-round boundary.** Preserve QM-028 and the successful clarification that weights are analytical.

**Also located at:**

- `repository/docs/exposition.md`, §4, product law, line 173: “The comparisons then act on separate fresh registers”

- `repository/docs/reasoning_record.md`, §5.2 The quantum sampler, line 2453: “This exact conditional law is essential:”

**Evidence:**

- Current expert equation (9) and surrounding paragraph.

- Current record #upper-stage-state and #upper-stage-law.

- MPS2023 §1.2.2 and In-Sample use exact membership and uniform conditional sampling, making this weighted analogue intelligible.

## QX-040

**keep · keep · P-KING**

**Locator:** `repository/docs/expert_companion.md`, 4.2 A tournament with probabilistic comparisons, Coupling, line 176.

> a failure after $i^\star$ is listed does not remove it

**Finding.** Preserve the stopped coupling exactly where it is. The proof only needs the sampler guarantee before the winner has appeared; later histories may have arbitrarily small or zero mass.

**Why it matters.** This distinguishes an unconditional query cap from a conditional per-stage success bound, and makes the behavior on zero inputs and late failure coherent.

**Direction.** Keep the conditioning on the entire past and the stopping event. Do not simplify it to independent failures with probability epsilon at every stage. Preserve its exposition and record counterparts as well.

**Prior-round boundary.** Preserve the completed QM-001/002 and QM-029 repairs rather than repeat them as open defects.

**Also located at:**

- `repository/docs/exposition.md`, §4, stopped coupling, line 179: “stopping cannot remove a listed column.”

- `repository/docs/reasoning_record.md`, §5.2 Coupling, line 2486: “This argument deliberately stops charging failures after $s$ has appeared.”

**Evidence:**

- Current expert §4.2 Coupling.

- Current record #upper-coupling.

## QX-041

**keep · keep · P-AMP**

**Locator:** `repository/docs/reasoning_record.md`, 5.4 Coherent access and the query cap, line 2674.

> It does not provide a bound on the number of elementary gates or the amount of workspace

**Finding.** Preserve the distinction between an ordinary bit-query bound and a circuit-time or space bound, together with the concrete two-query controlled-read construction.

**Why it matters.** The enormous addressed array can otherwise suggest that uncharged pointer access or QRAM is hidden in the model. The physical oracle explanation resolves a real expert objection.

**Direction.** Keep the oracle, pointer, inverse and control accounting available in one direct reading route; a brief pointer from the short papers is enough.

**Prior-round boundary.** New reader-value finding; does not repeat a repaired round-five mathematical defect.

**Evidence:**

- Current record #upper-oracle-access and #upper-read-compiler.

- HMW2003 §2 defines the same bit oracle and input-independent unitaries.

- AIK2026 v2 Lemma 6.5 and §6.4 similarly distinguish reversible implementations and all-input query caps.

## QX-042

**keep · keep · P-ROBUST**

**Locator:** `repository/docs/reasoning_record.md`, 3.3 The quantum promise algorithm, including amplification and coherence, line 732.

> Retain every address, flag, and count register.

**Finding.** Preserve the constructive retained-register account of error reduction. It shows that the classical binomial output law and the unitary used under later superposition refer to the same preparation.

**Why it matters.** For a quantum specialist, matching a convenient classical analysis to an actual reversible subroutine is a meaningful composability check, particularly on off-promise inputs.

**Direction.** Keep the state formula and its orthogonal-flag explanation available from the decoder claim. Permit specialists to skip elementary tail-bound arithmetic without hiding this interface.

**Prior-round boundary.** New reader-value finding; does not repeat a repaired round-five mathematical defect.

**Evidence:**

- Current record #forr_coherent and #forr_repetition.

- HMW2003 §3 Fact 2 constructs coherent error reduction with retained workspace; BHMT2000 §2 requires a preparation and inverse.

## QX-043

**keep · keep · P-FORR**

**Locator:** `repository/docs/exposition.md`, §1, scope of small example, line 76.

> the example checks conventions only.

**Finding.** The tiny instance is explicitly separated from asymptotic hardness, with the concrete reason L_{2,4}=0. Preserve that scope statement with the three sign patterns.

**Why it matters.** An expert can value the exact example without mistaking its census or the four-column board for evidence of the large-m lower bound.

**Direction.** Keep the scope boundary even if the exact census is shortened.

**Prior-round boundary.** No matching repaired finding is reissued.

**Evidence:**

- repository/docs/exposition.md §1 final paragraph and §6 k=2 versus k=3.

## QX-044

**keep · keep · P-FORR**

**Locator:** `repository/docs/exposition.md`, §2, The domain bit is needed, line 108.

> A function that checked only value bits would accept this board.

**Finding.** The changed board isolates the domain bit’s logical role while preserving true gate transcripts and consistent value bits. This is the best bridge from a promise problem to the total function.

**Why it matters.** The reader sees that correct local evaluations alone do not certify promise membership.

**Direction.** Keep the mutation and exact failing test, and keep this semantic lesson distinct from the chosen decoder’s sign blindness.

**Prior-round boundary.** No matching repaired finding is reissued.

**Evidence:**

- repository/docs/exposition.md §2 changed board and Local tests: the candidate fails exactly the domain test.

## QX-045

**keep · keep · P-ROBUST**

**Locator:** `repository/docs/exposition.md`, §4, Beating every rival is not winning, line 146.

> A column that dominates the comparisons is only a candidate

**Finding.** The single moved pointer proves that even perfect dominance does not imply a valid certificate. Its placement before the tournament analysis is effective.

**Why it matters.** It prevents the comparison-search output from being mistaken for a decision procedure and explains why verification survives.

**Direction.** Keep the example and return to it in verification; do not compress verification into an unexplained routine.

**Prior-round boundary.** Preserves ES-036/QM-030.

**Also located at:**

- `repository/docs/exposition.md`, 4 The quantum algorithm: a tournament, line 146: “A column that dominates the comparisons is only a candidate”

**Evidence:**

- repository/docs/exposition.md §4 moved-pointer example and Verification.

## QX-046

**keep · keep · P-SEP**

**Locator:** `repository/docs/exposition.md`, §6, quantifier counterexample, line 259.

> the condition $t\ge2^k$ holds for all large $t$

**Finding.** The quantifier warning is short, exact and connected to why every fixed k gives an exponent below four. It earns its place for specialists as well as students.

**Why it matters.** It prevents fixed-k asymptotics from silently becoming a growing-k assertion and distinguishes exponent optimality from a literal Ω(Q^4) witness.

**Direction.** Keep the choose-α, then-k, then-m order and the k=3 cubic-refutation check; optional uniform-k details elsewhere should not displace it.

**Prior-round boundary.** No matching repaired finding is reissued.

**Evidence:**

- repository/docs/expert_companion.md §7 main argument and separate growing-k remark.

## QX-047

**keep · keep · P-ROBUST**

**Locator:** `repository/docs/reasoning_record.md`, §5.2 Bounded-error comparison discussion, line 2281.

> its probability may be $1/2$, or arbitrarily close to $1/2$.

**Finding.** Preserve the precise reason bounded-error search does not immediately turn loser comparisons into a fixed tournament: there need not be any orientation computed with a uniform bias.

**Why it matters.** This is the exact objection an HMW-background reader will raise. It distinguishes an imperfect-oracle search result with different hypotheses from the different interface used here without diminishing the earlier result.

**Direction.** Keep this distinction beside the comparison model and keep the final exact-test search separate. It is a high-value explanation, not optional historical context.

**Prior-round boundary.** Comparison antecedents were already corrected in R5. This is a preserve recommendation, not a renewed missing-credit complaint.

**Evidence:**

- Current record §5.2 lines 2279–2282.

- Høyer–Mosca–de Wolf, §1 and §3 (supplied extracted lines 5, 41) assumes each underlying Boolean f_i has a bounded-error evaluator.

- Current record §5.2 allows probabilities at and arbitrarily near one half.

## QX-048

**keep · keep · P-FORR**

**Locator:** `repository/docs/reasoning_record.md`, §5.4 Coherent access and the query cap, line 2680.

> We can now state an exact finite budget before simplifying it asymptotically.

**Finding.** Preserve B_{k,t} and the interpretation of its two brackets. This is the strongest compact answer to whether every decoder, controlled comparison, inverse, padded stage, and candidate verification is being charged.

**Why it matters.** A bit-query expert can audit the actual algorithm before accepting logarithmic simplification, including malformed inputs where successful sampling or promise correctness is unavailable.

**Direction.** Keep the exact integer budget close to the algorithm and state each conversion factor once. Use it as the authoritative source for the shorter documents' resource discussion.

**Prior-round boundary.** No matching fixed finding was reissued.

**Evidence:**

- Current record §5.4 #upper-finite-budget, lines 2680–2695.

- Høyer–Mosca–de Wolf §2, supplied extracted line 21, fixes the ordinary bit-query model against which this accounting can be read.

- Current record §5.4 then states all random branches and off-promise inputs obey the same budget.

## QX-049

**keep · keep · P-FOURIER**

**Locator:** `repository/docs/reasoning_record.md`, §3.10 Moving the derivative through the blocks, line 1271.

> Order $k$ at a biased point does not mean degree $k$ under the uniform measure.

**Finding.** Keep this warning and its displayed expansion. It prevents the most likely specialist misreading of the first-block interpolation: that higher uniform Fourier levels have somehow been discarded.

**Why it matters.** This is essential to fair comparison with Bansal–Sinha's levels k through k(k−1), SSW's all-level growth bound, and GTW's coefficient-array induction.

**Direction.** Retain the exact distinction in the supplier route and in any summary of its relationship to prior methods.

**Prior-round boundary.** R5 LR-053 preserved the derivative explanation. This is a specific reason it remains valuable to this panel.

**Evidence:**

- Current record §3.10, lines 1271–1284, equation (F24).

- Bansal–Sinha overview, supplied lines 178–199, explains which biased Fourier levels arise in its different proof.

- Girish–Tal–Wu §1.3, supplied lines 127–159, develops contracted coefficient arrays; SSW Introduction lines 122–139 states its all-level theorem.

## QX-050

**keep · keep · P-ROBUST**

**Locator:** `repository/docs/reasoning_record.md`, §4.5 A shallow lookup can have large support, line 2010.

> The original preprint already describes the adaptive lookup and requires no correction at this point

**Finding.** Preserve the separation between adaptive depth and essential-coordinate support, together with this attribution sentence.

**Why it matters.** It prevents readers from treating a pointer lookup as a fixed small-support oracle, while also preventing the local formal diagnostic from being advertised as a correction to OpenAI's construction.

**Direction.** Keep the diagnostic on the model-audit route and preserve the exact statement of what the expanded formal wrapper adds. The main algorithm only needs the shallow adaptive/coherent evaluation bound.

**Prior-round boundary.** R5 statement-fidelity corrections already made this distinction. It is a feature to retain, not an unresolved mathematical objection.

**Evidence:**

- Current record §§4.5 and 4.8; especially lines 2006–2010 and 2100.

- Current record Lemma 2.2 discussion distinguishes the original count/depth clauses from the extra essential-coordinate test.

## QX-051

**keep · keep · P-FORR**

**Locator:** `repository/docs/reasoning_record.md`, §4.2 Totality and uniqueness, line 1846.

> No undefined partial-function value has to be supplied.

**Finding.** Keep the semantic definition of totality before local circuit verification, and keep the distinction that exact circuit realization is needed for the evaluator, not to make the winner predicate total or unique.

**Why it matters.** This directly answers the concern that a partial decoder smuggles a promise into the final function. It also keeps off-promise arbitrary decoder behaviour separate from the total mathematical predicate.

**Direction.** Protect this short explanation and the one-line pointer contradiction as the construction's main conceptual checkpoint, even if implementation detail is moved.

**Prior-round boundary.** This is a current strength; no claim is made that earlier totality fixes remain unresolved.

**Evidence:**

- Current record §4.2 lines 1818–1852; §5.3 winner protection and final verification.

- Bansal–Sinha supplied Introduction lines 25–30 defines a genuinely partial promise; the present totalization has to account for every other input.

## QX-052

**keep · keep · P-SEP**

**Locator:** `repository/docs/expert_companion.md`, §1 and §7, common circuit, line 31.

> with one circuit $\mathcal C$ serving both bounds

**Finding.** Preserve the explicit insistence that the upper and lower bounds use the same exact circuit and therefore the same total function.

**Why it matters.** Separately existential witnesses would not establish the claimed separation. This small qualification does more mathematical work than many of the scalar refinements and is easy to lose while shortening.

**Direction.** Keep the common-witness statement at the theorem and exponent assembly, and retain the corresponding quantified family statement in Appendix A.

**Prior-round boundary.** This is a successful current safeguard, not an unresolved prior defect.

**Evidence:**

- Current expert §1, §7 and Appendix A family theorem / fifth check.

- Current record §§4.2 and 7; current exposition §5 closing paragraph.
