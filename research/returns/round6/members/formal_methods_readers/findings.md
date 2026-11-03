# Located findings — round six formal-methods reader panel

The authoritative machine-readable version is `findings.json`. Quotations and Markdown line numbers refer to the supplied, hash-bound source files. Evidence paths are relative to the original input packet; the return ZIP does not duplicate that packet.

**Reading order:** `verdict.md` gives the decision and five priorities; `questions.md` ranks twenty author questions. This register retains both actionable findings and explicit keeps. High severity describes an evidence-presentation obstacle, not a claimed failure of the theorem.

## Register

| ID | Document | Kind | Severity | Location |
| --- | --- | --- | --- | --- |
| [FX001](#fx001) | exposition | evidence_presentation | high | §7, final sentence |
| [FX002](#fx002) | expert_companion | evidence_presentation | high | Appendix A, Reproducing the check |
| [FX003](#fx003) | expert_companion | evidence_presentation | medium | Appendix A, model bridge after the object table |
| [FX004](#fx004) | exposition | underweighted | medium | §7, model overview |
| [FX005](#fx005) | expert_companion | question | medium | Appendix A, Five things to check |
| [FX006](#fx006) | exposition | question | medium | §7, definition of Q |
| [FX007](#fx007) | expert_companion | evidence_presentation | high | §4.2, Proposition 3 |
| [FX008](#fx008) | exposition | unclear | medium | §7, final evidence paragraph |
| [FX009](#fx009) | expert_companion | question | medium | Appendix A, Table 2, relation legend |
| [FX010](#fx010) | expert_companion | underweighted | medium | Appendix A, What it does not establish |
| [FX011](#fx011) | expert_companion | question | medium | Appendix A, Table 2, direct product |
| [FX012](#fx012) | expert_companion | evidence_presentation | medium | Appendix A, Reproducing the check |
| [FX013](#fx013) | exposition | evidence_presentation | medium | §7, final sentence of first paragraph |
| [FX014](#fx014) | exposition | overweighted | medium | §7, opening paragraph |
| [FX015](#fx015) | expert_companion | overweighted | low | §7, growing-k remark |
| [FX016](#fx016) | exposition | question | low | §2, Transcripts |
| [FX017](#fx017) | expert_companion | question | medium | §6, Forrelation proof route |
| [FX018](#fx018) | expert_companion | keep | keep | Appendix A, Table 2, mixed-scope rows |
| [FX019](#fx019) | expert_companion | keep | keep | Appendix A, What Comparator establishes |
| [FX020](#fx020) | expert_companion | keep | keep | §1, statement and formal counterpart |
| [FX021](#fx021) | expert_companion | keep | keep | §4.3, verification |
| [FX022](#fx022) | exposition | keep | keep | §1, purpose of the small instance |
| [FX023](#fx023) | exposition | keep | keep | §5, joint event |
| [FX024](#fx024) | exposition | keep | keep | §6, quantifier order |
| [FX025](#fx025) | exposition | error | low | §6, exponent deduction |
| [FX026](#fx026) | reasoning_record | evidence_presentation | high | §6.1, Sources and formal correspondence |
| [FX027](#fx027) | reasoning_record | unclear | high | §2.9, relation/status paragraph |
| [FX028](#fx028) | reasoning_record | underweighted | medium | Reading guide |
| [FX029](#fx029) | reasoning_record | missing | medium | §2.9, second statement table |
| [FX030](#fx030) | reasoning_record | unclear | medium | §2.9, relation legend |
| [FX031](#fx031) | reasoning_record | underweighted | medium | §5.6 heading and audience route table |
| [FX032](#fx032) | reasoning_record | evidence_presentation | medium | Appendix B introduction |
| [FX033](#fx033) | reasoning_record | unclear | medium | Appendix F.1, Global verification of 2 November |
| [FX034](#fx034) | reasoning_record | question | low | Reading guide, examples |
| [FX035](#fx035) | reasoning_record | overweighted | low | §5.5, remaining physical-state specification |
| [FX036](#fx036) | reasoning_record | question | medium | §2.7, model contract |
| [FX037](#fx037) | reasoning_record | keep | keep | §2.1, promises and quantifiers |
| [FX038](#fx038) | reasoning_record | keep | keep | §2.2, minima |
| [FX039](#fx039) | reasoning_record | keep | keep | §2.6, OR2 and off-promise examples |
| [FX040](#fx040) | reasoning_record | keep | keep | §2.8, shared specifications |
| [FX041](#fx041) | reasoning_record | keep | keep | §5.1, retained state |
| [FX042](#fx042) | reasoning_record | credit | keep | §6.1, direct-product sources |
| [FX043](#fx043) | reasoning_record | keep | keep | §6.1, finite-seed endpoint |
| [FX044](#fx044) | reasoning_record | keep | keep | §6.5, capped simulator |
| [FX045](#fx045) | reasoning_record | keep | keep | §6.7, equation (19) |
| [FX046](#fx046) | reasoning_record | keep | keep | §A.6, quartic routes |
| [FX047](#fx047) | reasoning_record | keep | keep | Appendix B, construction claims |
| [FX048](#fx048) | exposition | question | medium | §7, trust conclusion |

## FX001

**exposition · evidence_presentation · high**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/exposition.md`, §7, final sentence, Markdown line 269.

> No recorded statement review yet covers the four compared theorems or these two statements

This sentence gives an obsolete evidence state. The packet contains a recorded review covering the four headline declarations and both additional endpoints, while the expert companion expressly cites it. The later report is automated and textual; its existence does not establish that a current corpus review binding covers the present record bytes.

**Why it matters.** A reviewer cannot tell whether the exposition has fallen behind the formal evidence or whether the claimed review excludes these declarations. The contradiction is visible before any proof examination.

**Direction.** Reconcile the current sentence with the supplied review and identify its automatic, nonhuman scope. Preserve the distinction between a recorded statement comparison, a proof check and independent human review. Name review existence, covered bytes, binding freshness and reviewer identity separately; do not refresh a binding by inference.

**Evidence.**

- previous_round/round5_statement_fidelity.md, “The four compared theorems” and “Other cited results”; rows uniformOpaqueAmplifier and direct_product_external_finite_realized_caps.
- repository/docs/expert_companion.md, Appendix A, paragraph after Table 2 (line 347).
- repository/docs/statement_evidence_contract.md, “Three separate facts per statement” and review-binding rules; SOURCE_STATUS.json, record.markdown_matches_accepted_review=false.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX002

**expert_companion · evidence_presentation · high**  
Perspective: `reproducibility_interface_reviewer`. Location: `repository/docs/expert_companion.md`, Appendix A, Reproducing the check, Markdown line 351.

> The first line gives the versions of the recorded runs and the commit the links point to.

The displayed commit is 659b571, but the generated Lean and passage links point to e9dfefbf11e6d1f380f122caa2349d4be78f2c1f. The packet itself is bound to 9bdd443ce9b5e2fa5a83d63e0bcb0d87fbed298a. These can be legitimate different snapshots, but the sentence says they are the same.

**Why it matters.** The first reproducibility action leaves a reader unsure which text, formal declarations and recorded run belong together. This is a version-presentation problem, not evidence that a recorded comparison failed.

**Direction.** Give one coherent snapshot map covering the paper, pinned source and recorded check. Update the explanatory commit claim to the actual link target and name any intentionally distinct provenance commits. This is edition metadata, not an allegation that the supplied acceptance receipts are false.

**Evidence.**

- repository/docs/expert_companion.md:354 and generated lean-links block (369–423).
- SOURCE_STATUS.json repository_commit; repository/docs/lean_links.json commit.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX003

**expert_companion · evidence_presentation · medium**  
Perspective: `quantum_model_reviewer`. Location: `repository/docs/expert_companion.md`, Appendix A, model bridge after the object table, Markdown line 305.

> That these models agree with the usual ones

The added bridge pointer is valuable, but its single anchor lands at §2.5, the deferred-measurement bridge, although the sentence also promises the finite-mixture argument in §2.2. A reader checking R first must search backwards.

**Why it matters.** The semantic review of R and Q starts from different mathematical questions. A single terminal anchor makes the advertised fifteen-minute route slower than it needs to be.

**Direction.** Split the existing bridge pointer into the finite-mixture argument and the quantum fixed-sequence argument, and indicate which conventional-model claim each establishes. Reuse the existing record material.

**Evidence.**

- repository/docs/reasoning_record.md §2.2, anchor R3-01-CLASSICAL, finite-behaviour argument and real-bias caveat.
- repository/docs/reasoning_record.md §2.5, anchor R3-01-BRIDGES, all-starting-vector acceptance-mass identity.

**Prior-round boundary.** Round-five ER-019 added the model-equivalence link. This finding concerns the new link’s landing and audit usability, not a repeated claim that the bridge is absent.

## FX004

**exposition · underweighted · medium**  
Perspective: `quantum_model_reviewer`. Location: `repository/docs/exposition.md`, §7, model overview, Markdown line 267.

> The five definitions above are where to answer it.

The definitions show the chosen model but do not by themselves explain its equivalence to the conventional fixed-sequence query model. The exposition has no direct route here to the record’s existing finite-mixture, probability-mass and deferred-measurement bridges.

**Why it matters.** A formal reader who does not already know the custom AdaptiveProgram representation cannot settle the intended-semantics question by accepting five names. The necessary explanation exists, but this entrance does not expose it.

**Direction.** Point this audit entrance to the existing model bridges in record §§2.2–2.5, with one short description of the semantic obligation they settle. Preserve the compact exposition.

**Evidence.**

- repository/docs/reasoning_record.md §§2.2–2.5.
- repository/lean/QuarticCorpus/Unconditional/Challenge.lean:46–74,101–140.
- literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md, “Quantum circuits” and “Projective measurement”.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX005

**expert_companion · question · medium**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/expert_companion.md`, Appendix A, Five things to check, Markdown line 321.

> *The infimum.*

The checklist checks nonemptiness for the real infimum defining alpha_tot. Where should a reader check the separate read-all witnesses that make the natural-number infima defining R and Q genuine minima?

**Why it matters.** The linked R definition itself warns that the empty natural infimum is zero. A sceptic checking for a nearby easy statement will inspect this before trusting a lower-bound endpoint.

**Direction.** Extend the existing audit route with the record’s nonempty-budget and read-all witness locators for R and Q; no additional formal work is needed.

**Evidence.**

- repository/lean/QuarticCorpus/Unconditional/Challenge.lean:71–74,139–140.
- repository/docs/reasoning_record.md §2.2 after the finite-mixture discussion; §2.4 final paragraph.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX006

**exposition · question · medium**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/exposition.md`, §7, definition of Q, Markdown line 265.

> [The budget test for $Q$][def-QLe] asks the same of one [quantum program][def-adaptive]

The linked definition has an explicit ConstantOnPromise disjunct before its program existential. Why is that branch present, and why does it not give an unintended zero-query shortcut?

**Why it matters.** This is a reasonable first objection to the actual Lean type, especially for empty promises and an empty coordinate type. The prose summary omits the branch that a sceptic is most likely to notice.

**Direction.** Link the existing explanation of the constant-on-promise branch and its empty-register purpose; present it as a representational boundary case with an existing justification.

**Evidence.**

- repository/lean/QuarticCorpus/Unconditional/Challenge.lean:128–137.
- repository/docs/reasoning_record.md §2.4, paragraph after the displayed QLe disjunction.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX007

**expert_companion · evidence_presentation · high**  
Perspective: `proof_route_reviewer`. Location: `repository/docs/expert_companion.md`, §4.2, Proposition 3, Markdown line 160.

> returns at most $T$ candidates

The prose proves a list-producing tournament, but the record says the headline Lean roots use the older measured-label/Boolean-continuation route, and the separately built list theorem is not on those roots. Appendix A does not make that route difference visible for Proposition 3.

**Why it matters.** A reader following the explanatory algorithm into the formal dependency graph can mistake a matching supporting theorem for the implementation used to establish the headline. This is exactly the distinction between proving a statement and formalising the displayed argument.

**Direction.** Add a compact pointer beside the tournament or in Appendix A to the existing two-route table and the Boolean-continuation explanation, identifying the headline-used route and the separately built list result.

**Evidence.**

- repository/docs/reasoning_record.md §5.5, table “Route / What it proves / Used by the headline proof roots”, and paragraph beginning “The supplied dependency export”.
- repository/docs/reasoning_record.md §5.6, Boolean continuation.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX008

**exposition · unclear · medium**  
Perspective: `proof_route_reviewer`. Location: `repository/docs/exposition.md`, §7, final evidence paragraph, Markdown line 269.

> The separation needs neither:

The referent of “neither” is hard to recover after two results, a stronger conclusion and three distinct limitations. The supplied explanation addresses the full-state and arbitrary-randomness extensions, but leaves the role of the separate actual-count/compliance bridge unclear.

**Why it matters.** A reader may infer either that these compared lemmas are dependencies of the headline or that their restrictions are being dismissed. The existing record distinguishes the actual proof route, so the ambiguity is avoidable.

**Direction.** Identify which extension is unnecessary for which headline proof route, and link the relevant existing route explanation rather than using one collective dismissal.

**Evidence.**

- repository/docs/exposition.md:269.
- repository/docs/reasoning_record.md §§5.5–5.6 and §6.7.
- repository/lean/QuarticQuery/LowerBound/RealizedCaps.lean, actualComplies, actualCount, compliantSuccess.

**Prior-round boundary.** Round-five fixed the finite-seed description and full-state status. This is a residual scope ambiguity in the revised paragraph, not a request to repeat those repairs.

## FX009

**expert_companion · question · medium**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/expert_companion.md`, Appendix A, Table 2, relation legend, Markdown line 327.

> accepted by Comparator in its own configuration

Do all the compared entries have the same independent-specification boundary as the 343-line Mathlib-only headline challenge? The amplifier and realised-cap challenges explicitly import maintained vocabulary and say they are not independent semantic reviews.

**Why it matters.** The shared “compared” label can be read as a uniform level of specification independence, although it records declaration agreement under different trust boundaries.

**Direction.** Expose the existing challenge boundary per class of result: Mathlib-only headline definitions versus imported maintained definitions. Keep comparison success separate from semantic independence.

**Evidence.**

- repository/lean/QuarticCorpus/Unconditional/Challenge.lean:1–7.
- repository/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean:1–8.
- repository/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean:1–8.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX010

**expert_companion · underweighted · medium**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/expert_companion.md`, Appendix A, What it does not establish, Markdown line 349.

> a modelling error shared by both would pass

The most consequential Comparator limitation is stated abstractly after the positive controls. The supplied artefacts already contain a concrete shared-bad-specification control and a separate semantic audit detecting its lack of witnesses.

**Why it matters.** A sceptic wants to see the failure mode that proof matching cannot detect, not only examples of malformed solutions that it rejects.

**Direction.** Use a short pointer to the existing shared-specification blindness example alongside this sentence, identifying it as a demonstration of the tool boundary rather than a defect in the actual theorem.

**Evidence.**

- repository/lean/QuarticCorpus/Independent/Controls/SharedAudit.lean, actual_comparison_has_witness and shared_bad_spec_has_no_witness.
- repository/corpus/receipts/comparator-round3-shared-bad-spec-blindness-2026-11-02T204814950389+0000.json, present as historical evidence; no rerun in this review.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX011

**expert_companion · question · medium**  
Perspective: `finite_probability_reviewer`. Location: `repository/docs/expert_companion.md`, Appendix A, Table 2, direct product, Markdown line 340.

> path compliance is not proved equal to the per-input caps

Which ordinary implication turns the compared recursive-compliance event into the separate per-input query-count condition of Lemma 4? The table labels the gap correctly, but its event link lands at compliantSuccess, which delegates the condition to another definition.

**Why it matters.** The finite-seed scope is already explicit; the remaining operational question is exactly what counts as compliance. Resolving it should require a local comparison of two predicates, not following a long import chain.

**Direction.** Place the existing actualComplies and actualCount definitions beside the ordinary cap-event statement, identify which interpretation is outside Lean, and label its present evidence status. Keep this an explanation of the existing interface, not a request for a new theorem or formalisation.

**Evidence.**

- repository/lean/QuarticQuery/LowerBound/RealizedCaps.lean, actualComplies, actualPath, actualCount and compliantSuccess.
- repository/docs/reasoning_record.md §6.1, cap-event corollary and formal correspondence.

**Prior-round boundary.** CM-010/ER-021 already repaired the scope claim. This asks how a reader operationally checks the now-disclosed relation.

## FX012

**expert_companion · evidence_presentation · medium**  
Perspective: `reproducibility_interface_reviewer`. Location: `repository/docs/expert_companion.md`, Appendix A, Reproducing the check, Markdown line 351.

> lists the closure the kernel checked

The dependency command traverses available types and bodies in all namespaces but displays a public QuarticQuery projection. Its hidden_paths field retains only one witness per projected edge. “The closure” is therefore a less precise description than the tool itself supplies.

**Why it matters.** A formal reader can mistake projected edges for direct proof-body dependencies or interpret the output as a complete axiom audit. A future graph must keep these distinctions visible.

**Direction.** Describe the current output as a projection, show whether an edge is direct or passes through hidden constants, and state that types as well as bodies are traversed. Point to the existing axiom evidence separately; no new tool or theorem is needed.

**Evidence.**

- repository/lean/scripts/Reach.lean.
- repository/docs/reasoning_record.md §5.5, headline-root dependency distinction.
- repository/corpus/comparator_map.json boundary and credit_vocabulary.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX013

**exposition · evidence_presentation · medium**  
Perspective: `reproducibility_interface_reviewer`. Location: `repository/docs/exposition.md`, §7, final sentence of first paragraph, Markdown line 265.

> Each link opens the exact lines.

Exact line targeting establishes the destination, but it does not state why that passage is linked to this claim. The backend already distinguishes direct configured declarations, statement dependencies and textual wrapper joins; the reader-facing link promise does not expose those different relationships. In particular, the Checked.theorem_one_one wrapper join is a proof-text reference and explicitly records no type correspondence; its nearby exact relation must not override that warning.

**Why it matters.** A future reader interface could accidentally turn a nearby source line or a curated relationship into the visual appearance of machine-checked correspondence.

**Direction.** Carry the existing relation provenance into the reader interface: text-to-type editorial mapping, configured comparison, definition dependency, and proof-root dependency should remain separate fields. Display source edition and review origin without inventing new evidence.

**Evidence.**

- repository/docs/lean_links.json boundary: line links imply no Lean or Comparator run.
- repository/corpus/comparator_map.json boundary, credit_vocabulary, and textual-join warning.
- reader_principles.md principles 5,7,8,10.
- repository/corpus/comparator_map.json, declarations["QuarticQuery.Checked.theorem_one_one"].statement_ids: a solution_proof_reference textual join carries comparison_credit="none" and explicitly records no type correspondence.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX014

**exposition · overweighted · medium**  
Perspective: `supportive_lean_reviewer`. Location: `repository/docs/exposition.md`, §7, opening paragraph, Markdown line 265.

> Five definitions carry the content.

The section compresses the audit into three unusually long paragraphs containing definitions, four theorem relations, tool behaviour, two optional endpoints and limitations. The useful material is present but is not ordered as actions a new formal reader can complete.

**Why it matters.** The supporting reader wants a feasible entry point and a clear stopping condition, not more content. After the pedagogical clarity of the four-column example, this dense final section changes mode abruptly.

**Direction.** Reorganise only the existing evidence into a short ordered audit route with optional depth: read one headline type, inspect its semantic definitions and bridges, then inspect the matching check. Preserve the full-strength restrictions and route facts.

**Evidence.**

- repository/docs/exposition.md §§2 and7.
- reader_principles.md principles3,6,11,12.
- repository/lean/QuarticCorpus/Unconditional/Challenge.lean:328–334.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX015

**expert_companion · overweighted · low**  
Perspective: `supportive_lean_reviewer`. Location: `repository/docs/expert_companion.md`, §7, growing-k remark, Markdown line 283.

> **Remark** (letting $k$ grow)**.**

The optional growing-k deduction introduces a second family regime, a large explicit constant and a detailed epsilon expression immediately before the formal audit. For this panel the more valuable distinction is that this deduction is ordinary and the needed bound is built but uncompared.

**Why it matters.** It competes with the semantics/endpoint questions without changing the fixed-k exponent theorem that the reader came to assess.

**Direction.** Keep the status and a precise route to the deduction, but reassess the space spent on the explicit epsilon expression in the short companion. Any relocation must preserve the actual deduction in the record.

**Evidence.**

- repository/docs/expert_companion.md:277–283.
- previous_round/dispositions/expert_companion.json ER-014: the prior shortened remark retained material because the full derivation was not then in the record.

**Prior-round boundary.** ER-014 already shortened this remark. This is a panel-specific weighting judgement about the resulting compact version; do not delete unique substance.

## FX016

**exposition · question · low**  
Perspective: `reproducibility_interface_reviewer`. Location: `repository/docs/exposition.md`, §2, Transcripts, Markdown line 106.

> a checker for every count on this board

When the reader opens the example checker, which facts are finite executable checks and which have a Lean theorem, and how is this reduced r=2 board related to the asymptotic r=20 log₂m family?

**Why it matters.** The text already states r=2 and says the tiny Forrelation lower bound is empty, which is good. A reader interface must preserve these scope limits when presenting a successful example as evidence.

**Direction.** At the existing checker link, label the checked finite facts and retain the reduced-address-length scope. Do not give the example an overall formal-verification badge merely because some nearby general claims are formalised.

**Evidence.**

- repository/docs/exposition.md:76,96,106,114.
- repository/research/returns/round3/members/04_addressed_construction/examples/check_example.py (present; not executed in this review).
- reader_principles.md principles10,12,14.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX017

**expert_companion · question · medium**  
Perspective: `supportive_lean_reviewer`. Location: `repository/docs/expert_companion.md`, §6, Forrelation proof route, Markdown line 271.

> No person has yet reviewed this Lean proof.

What is the smallest substantive review task being offered to a willing expert: check the independent public statement, inspect the rounded-Gaussian-to-query-bound bridge, or review the whole alternative proof? The admission is candid, but the invitation has no bounded task.

**Why it matters.** A researcher who wants the project to succeed may stop because the apparent ask is a complete audit of a large new proof route. Existing section links could support a more focused contribution.

**Direction.** Offer a bounded review route using the already available statement, proof ingredients and record locators. State the question a reader could answer in fifteen minutes, while retaining the fact that this is not full human review.

**Evidence.**

- repository/docs/expert_companion.md §6.
- repository/docs/reasoning_record.md §§3.6–3.16.
- literature/quartic-ref-06-k-forrelation-optimally-separates-quantum/extracted.md, Our Results and Overview and Techniques: source theorem, proof route and hypotheses.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX018

**expert_companion · keep · keep**  
Perspective: `finite_probability_reviewer`. Location: `repository/docs/expert_companion.md`, Appendix A, Table 2, mixed-scope rows, Markdown line 340.

> Stronger in covering uncapped trees

Keep the explicit multidirectional comparison: the direct-product endpoint strengthens the event scope while restricting seeds and leaving the count/compliance identification ordinary. This is much more trustworthy than a single global “stronger” badge.

**Why it matters.** It prevents the exact nearby-statement failure this panel is primed to investigate, while acknowledging useful formal progress without overstating it.

**Direction.** Preserve the mixed-scope detail in both prose and any reader interface; changes to layout should not collapse it to one adjective.

**Evidence.**

- repository/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean:18–25.
- repository/lean/QuarticQuery/LowerBound/RealizedCaps.lean.
- previous_round/round5_statement_fidelity.md, direct-product row.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX019

**expert_companion · keep · keep**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/expert_companion.md`, Appendix A, What Comparator establishes, Markdown line 325.

> the two are compiled separately

Keep the explanation that the challenge contains placeholders, the solution supplies proofs, and Comparator checks configured declarations against the challenge definitions. This directly answers why opening a file with sorry is compatible with a meaningful check.

**Why it matters.** A reader must not mistake a successful compilation of a placeholder statement file for a proof, or infer that seeing sorry refutes the separately checked solution.

**Direction.** Preserve the explicit challenge/solution/configuration links and the exact four-theorem scope.

**Evidence.**

- repository/lean/QuarticCorpus/Unconditional/Challenge.lean:326–340.
- repository/lean/QuarticCorpus/Unconditional/Solution.lean.
- repository/lean/QuarticCorpus/Unconditional/comparator.json.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX020

**expert_companion · keep · keep**  
Perspective: `proof_route_reviewer`. Location: `repository/docs/expert_companion.md`, §1, statement and formal counterpart, Markdown line 31.

> the explicit constants $6$ and $1/400$

Keep the immediate distinction between the compared existential logarithmic exponent and the separately built explicit-constant theorem. It lets the reader know, at the first theorem, exactly which formal endpoint supports which printed strength.

**Why it matters.** Without this local qualification the advertised explicit theorem could silently inherit the compared status of its weaker existential form.

**Direction.** Preserve both the same-circuit requirement and the separate evidence status whenever shortening the introduction or table.

**Evidence.**

- repository/lean/QuarticCorpus/Unconditional/Challenge.lean:328–334.
- repository/lean/QuarticQuery/Paper/ConstructionFamily.lean:28–40.
- previous_round/round5_statement_fidelity.md, headline and constants rows.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX021

**expert_companion · keep · keep**  
Perspective: `quantum_model_reviewer`. Location: `repository/docs/expert_companion.md`, §4.3, verification, Markdown line 180.

> No unit-cost pointer oracle is assumed.

Keep the explicit bit-query accounting for pointers and controlled access. It connects the mathematical algorithm to the formal oracle model at the place where an accidental stronger oracle would matter.

**Why it matters.** The huge addressed arrays otherwise make it easy to read one local test as a unit-cost random-access operation.

**Direction.** Preserve this point-of-use explanation and its link to the all-input cap, even if the loose logarithmic count is compressed.

**Evidence.**

- repository/lean/QuarticCorpus/Unconditional/Challenge.lean:89–94,232–260.
- repository/docs/reasoning_record.md §§4.5–4.6 and5.4.
- literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md, query-model and reversible-circuit discussion.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX022

**exposition · keep · keep**  
Perspective: `supportive_lean_reviewer`. Location: `repository/docs/exposition.md`, §1, purpose of the small instance, Markdown line 76.

> the example checks conventions only

Keep the explicit limitation on the eight-bit example, together with the negative unpromised input. It tests a real semantic distinction without pretending the tiny instance exhibits the asymptotic lower bound.

**Why it matters.** This is a strong model for presenting finite checks to sceptics: one visible object, an exact calculation and a precise limit on what follows.

**Direction.** Preserve the convention-only label and the link from the negative input to the later domain-bit counterexample.

**Evidence.**

- repository/docs/exposition.md §§1–2.
- repository/lean/QuarticCorpus/Independent/SemanticMutations.lean, absolute_high_changes_answer.
- literature/quartic-ref-06-k-forrelation-optimally-separates-quantum/extracted.md, definition of the one-sided Forrelation promise.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX023

**exposition · keep · keep**  
Perspective: `finite_probability_reviewer`. Location: `repository/docs/exposition.md`, §5, joint event, Markdown line 236.

> with lightness inside the probability

Keep the joint-event formulation, its counterexample and the simulator’s stopping rule together. The explanation exposes the exact event whose formal type must be checked.

**Why it matters.** Conditioning on a realised cap is a plausible nearby easier statement; this passage gives the reader enough structure to recognise that mutation.

**Direction.** Preserve the contrast between the joint event and conditional success and keep the independence of all free information explicit.

**Evidence.**

- repository/docs/exposition.md:214–238.
- repository/lean/QuarticQuery/LowerBound/RealizedCaps.lean, compliantSuccess.
- repository/lean/QuarticQuery/Paper/ClassicalPlanted.lean, eq_21.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX024

**exposition · keep · keep**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/exposition.md`, §6, quantifier order, Markdown line 259.

> choosing $\alpha$ first, then a single $k$, then letting $m$ grow

Keep the explicit order of quantifiers and the counterexample to substituting k=t. These are semantic checks of the headline, not dispensable asymptotic pedagogy.

**Why it matters.** A correct Lean proof of a differently ordered family statement would not settle the intended universal exponent. The exposition makes that risk intelligible.

**Direction.** Preserve this order in any compressed theorem card and in the informal-to-formal mapping.

**Evidence.**

- repository/lean/QuarticCorpus/Unconditional/Challenge.lean:328–334.
- repository/docs/expert_companion.md Appendix A, Five things to check, item5.

**Prior-round boundary.** New reader task or residual presentation issue; no rejected receipt claim.

## FX025

**exposition · error · low**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/exposition.md`, §6, exponent deduction, Markdown line 253.

> Fix $\alpha<4$

The local exponent derivation omits the restriction alpha >= 0. Replacing 1+Q by its upper bound in the denominator yields the displayed lower bound only for nonnegative alpha; when alpha < 0 the monotonicity reverses. The definition of alpha_tot already limits attention to nonnegative exponents, so this is a local missing hypothesis rather than a failure of the theorem.

**Why it matters.** The formal-to-informal comparison should preserve the domain of a quantified variable. An unnecessary extra domain makes the displayed implication stronger than the supplied argument supports.

**Direction.** Restore the existing nonnegative-exponent restriction at this local step, matching the definition and the expert companion. No new argument or formalisation is needed.

**Evidence.**

- repository/docs/exposition.md:14,253–257.
- repository/docs/expert_companion.md:277 explicitly fixes 0 <= alpha < 4.
- repository/lean/QuarticCorpus/Unconditional/Challenge.lean:311–315 includes 0 <= alpha in UniversalPower.

**Prior-round boundary.** No matching nonnegative-alpha issue found in the exposition disposition records; prior quantifier findings concerned rival indices or same-circuit order.

## FX026

**reasoning_record · evidence_presentation · high**  
Perspective: `finite_probability_reviewer`. Location: `repository/docs/reasoning_record.md`, §6.1, Sources and formal correspondence, Markdown line 3262.

> instance exceeds its cap of $L$ queries

The prose describes the compared finite-seed endpoint in per-input query counts, but its event uses recursive actualComplies. The record does not expose the unproved Lean equivalence to actualCount; the expert companion already does.

**Why it matters.** This is where a reader decides whether the formal resource event matches the prose event. The intended ordinary equivalence is credible, but the checked endpoint is not itself stated through the observable count.

**Direction.** Identify the recursive event and the ordinary count interpretation at this endpoint and the §2.9 row, reusing the existing expert caveat. This is a presentation request, not a new Lean theorem.

**Evidence.**

- repository/lean/QuarticQuery/LowerBound/RealizedCaps.lean:50–61, 101–120
- repository/docs/expert_companion.md, Appendix A, direct-product row, line 340
- repository/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean
- literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md, §1.3 and §3 (conditional values, transcript-product law, fair-algorithm remark)

**Prior-round boundary.** Round five and expert Appendix A already acknowledge the distinction. This concerns its omission from the record, not the corrected finite-seed issue.

## FX027

**reasoning_record · unclear · high**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/reasoning_record.md`, §2.9, relation/status paragraph, Markdown line 514.

> Rows without a qualification carry reviews recorded as current

The paragraph combines recorded-as-current reviews, 2 November bindings not refreshed after round-four additions, and no-current-review labels. The packet also supplies a later textual statement review. Which review authority and source scope each status denotes is unclear without reading the evidence contract.

**Why it matters.** Current execution, historical bound fidelity, and a later textual review answer different questions. Readers can over-credit old bindings or erase a real later review.

**Direction.** Separate review authority, as-of snapshot and binding state from build/Comparator status. Explain why the round-five textual review does not automatically refresh corpus bindings; do not silently upgrade statuses.

**Evidence.**

- repository/docs/statement_evidence_contract.md:56–101
- previous_round/round5_statement_fidelity.md:1–3
- repository/docs/reasoning_record.md:508–516

**Prior-round boundary.** Do not infer current corpus bindings merely from the existence of round-five review. This is a scope/authority ambiguity, not a claim that receipt facts are false.

## FX028

**reasoning_record · underweighted · medium**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/reasoning_record.md`, Reading guide, Markdown line 14.

> A reader checking the formal statement needs §2.9 and Appendix B.

The new statement-first route is useful, but its stopping condition remains unclear: §2.9 has two tables and Appendix B has 121 rows. A sceptic lacks a bounded fifteen-minute route through one headline claim and its semantic dependencies.

**Why it matters.** Exhaustiveness supports later auditing but does not make the first check of statement meaning bounded.

**Direction.** Give a minimum route through one configured target, R/Q definitions, a revealing finite control, implementation forwarding, and the relevant relation/route qualification; state what that check can conclude.

**Evidence.**

- literature/quartic-lit-buhrman-dewolf-decision-tree-survey/extracted.md, §§3.1–3.3 (printed pp. 5–8)
- repository/lean/QuarticCorpus/Unconditional/Challenge.lean
- repository/lean/QuarticCorpus/Unconditional/Solution.lean
- repository/lean/QuarticCorpus/Unconditional/comparator.json
- repository/docs/reasoning_record.md:14–23,487–516,4205–4211

**Prior-round boundary.** LR-007 was fixed by adding §2.9. Preserve it; this asks for a completion criterion, not another statement-first section.

## FX029

**reasoning_record · missing · medium**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/reasoning_record.md`, §2.9, second statement table, Markdown line 510.

> `direct_product_external_finite_realized_caps`

The headline targets have pinned statement links, while many intermediate declarations appear only as code names with ordinary-proof links. The difficult partial/stronger rows require an additional search to reach their exact types.

**Why it matters.** Type access is most needed where the formal and informal statements differ. Those rows are less directly inspectable than the headline table.

**Direction.** Extend the existing type-link pattern to intermediate compared targets and decisive shared definitions; retain ordinary-proof destinations separately.

**Evidence.**

- repository/docs/reasoning_record.md:487–512
- repository/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean
- repository/docs/lean_links.json

**Prior-round boundary.** Extends the successful LR-007 improvement; does not allege broken headline links or missing receipts.

## FX030

**reasoning_record · unclear · medium**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/reasoning_record.md`, §2.9, relation legend, Markdown line 514.

> *partial* that it proves only some clauses or keeps a hypothesis

Partial covers an equality compared with a compound row, a direct-product result broader in tree class but narrower in seed class, and a physical amplifier missing particular identifications. These are different directions of comparison.

**Why it matters.** A statement can be stronger on one axis and weaker on another. A flat completeness label hides the relevant semantic delta.

**Direction.** For exceptional rows, expose reference claim, hypothesis/domain change, conclusion clauses, and ordinary transport. Reuse the companion’s stronger-in/weaker-in account for realized caps.

**Evidence.**

- repository/docs/reasoning_record.md:491–514,2781,3257–3267
- repository/docs/expert_companion.md:340
- repository/lean/QuarticQuery/LowerBound/RealizedCaps.lean:113–120
- literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md, §1.3 and §3 (conditional values, transcript-product law, fair-algorithm remark)

**Prior-round boundary.** Preserve corrected expanded-support and compound-family explanations. Do not revive the claim that the preprint demanded the later diagnostic.

## FX031

**reasoning_record · underweighted · medium**  
Perspective: `supportive_lean_reviewer`. Location: `repository/docs/reasoning_record.md`, §5.6 heading and audience route table, Markdown line 2784.

> Optional: the Boolean continuation used by the formal headline

Optional is right for the ordinary proof, but this is the headline implementation’s route. The same audience distinction applies to the unnormalized direct-product proof and alternative zero-search estimate.

**Why it matters.** A formal reader following only the required mathematical route may inspect a proof the checked headline does not use. This is a navigation issue, not unsoundness.

**Direction.** Keep the ordinary route and add a formal dependency route indicating which optional passages matter for inspecting the implementation.

**Evidence.**

- repository/docs/reasoning_record.md:16–23,2736–2751,2784,3117–3255,3790
- literature/quartic-lit-buhrman-dewolf-decision-tree-survey/extracted.md, §§3.1–3.3 (printed pp. 5–8)
- literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md, §1.3 and §3 (conditional values, transcript-product law, fair-algorithm remark)

**Prior-round boundary.** LR-022/023 correctly moved alternatives out of the mathematical flow. Preserve those moves; add an audience route.

## FX032

**reasoning_record · evidence_presentation · medium**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/reasoning_record.md`, Appendix B introduction, Markdown line 4209.

> whose current maintained observations are in its `current_catalogue_snapshot.rows` branch

The current/historical branch distinction is now explicit, but comparing one literal claim with its type, assumptions and review scope still requires traversing a large correspondence object.

**Why it matters.** The immutable ledger is useful provenance but an inefficient first inspection surface for a semantic comparison.

**Direction.** Provide a derived per-claim view retaining the quotation and exposing exact type, delta, premises, review authority and execution scope. Do not alter or retypeset the hashed ledger.

**Evidence.**

- repository/docs/reasoning_record.md:4205–4211
- repository/docs/reasoning_record_correspondence.json: current_catalogue_snapshot.rows
- repository/docs/statement_evidence_contract.md:56–101

**Prior-round boundary.** Respect LR-012’s declined retypesetting and the fixed branch pointer. This is a separate derived view.

## FX033

**reasoning_record · unclear · medium**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/reasoning_record.md`, Appendix F.1, Global verification of 2 November, Markdown line 6094.

> Every catalogue row now has a current mathematical-fidelity review

The subsection dates this claim to 2 November, but now/current can become misleading when a search result or interface card detaches the sentence from its heading.

**Why it matters.** A historically correct statement can appear to contradict §2.9 after temporal context is lost.

**Direction.** Make snapshot dates inseparable from historical status assertions or extracted cards; direct live status to §2.9 while retaining the archival account.

**Evidence.**

- repository/docs/reasoning_record.md:6088–6096,514
- repository/docs/statement_evidence_contract.md:58–73

**Prior-round boundary.** LR-019 already moved chronology to Appendix F. This concerns local temporal wording under extraction, not another relocation.

## FX034

**reasoning_record · question · low**  
Perspective: `proof_route_reviewer`. Location: `repository/docs/reasoning_record.md`, Reading guide, examples, Markdown line 12.

> exact small examples that test each convention

Which example should a reader select for which semantic risk? Model examples, differing Forrelation sign examples, a four-column construction, a cyclic tournament and a planted XOR instance have careful local scopes but no single purpose map.

**Why it matters.** A time-limited semantic check benefits from choosing an example by the mistake it detects.

**Direction.** Add a compact risk-to-example map with expected outcome, definitions tested and limits; preserve the warnings that these are not tiny asymptotic separation instances.

**Evidence.**

- repository/docs/reasoning_record.md:334–407,477–481; §§3.5,4.3–4.4,5.2,6.2
- literature/quartic-lit-buhrman-dewolf-decision-tree-survey/extracted.md, §§3.1–3.3 (printed pp. 5–8)
- literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md, introduction and main results

**Prior-round boundary.** The examples are already corrected. This asks for selection help, not different mathematical values.

## FX035

**reasoning_record · overweighted · low**  
Perspective: `quantum_model_reviewer`. Location: `repository/docs/reasoning_record.md`, §5.5, remaining physical-state specification, Markdown line 2756.

> The remaining formal target for the complete physical reading of Lemma 3.1

The precise physical-state target is useful, but its length immediately after the route table can make its missing bridge feel central to validating Proposition 3.3, whose checked route uses measured labels.

**Why it matters.** The reader’s first decision is whether the open identification affects the headline. The correct answer is given, but separated from substantial specification detail.

**Direction.** Preserve the target while making its relevance and non-dependency visible before the full schema, or place the schema in optional detail. Do not add formalization work.

**Evidence.**

- repository/docs/reasoning_record.md:2736–2781
- literature/quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error/extracted.md, introduction and preliminaries (fixed bounded-error predicates and query model)
- repository/docs/expert_companion.md, Appendix A, amplification rows

**Prior-round boundary.** The retained-state caveat is correct. This is low-priority weighting, not a request to complete its bridge.

## FX036

**reasoning_record · question · medium**  
Perspective: `supportive_lean_reviewer`. Location: `repository/docs/reasoning_record.md`, §2.7, model contract, Markdown line 413.

> Complete source signatures, including the circuit and workspace quantifiers

Can a first-pass model view identify which bridges are definitions, proved source translations, and ordinary model-identification arguments—particularly finite distributions, empty coordinates, reindexing and deferred measurement’s acceptance-mass guarantee?

**Why it matters.** The prose explains these well, but a signature inventory alone can obscure which semantic justification must be read alongside a matching type.

**Direction.** Organize existing material by these three roles with exact endpoints and a short inspection order. Reuse the existing arguments; do not commission new equivalence proofs.

**Evidence.**

- repository/docs/reasoning_record.md:173–329,413–465
- literature/quartic-lit-buhrman-dewolf-decision-tree-survey/extracted.md, §§3.1–3.3 (printed pp. 5–8)
- repository/lean/QuarticCorpus/Unconditional/Challenge.lean
- repository/docs/statement_evidence_contract.md:18–28

**Prior-round boundary.** Keeps the explicit model discussion; no allegation that the supplied model differs from the standard intended one.

## FX037

**reasoning_record · keep · keep**  
Perspective: `supportive_lean_reviewer`. Location: `repository/docs/reasoning_record.md`, §2.1, promises and quantifiers, Markdown line 166.

> Its behavior outside $\mathcal D$ can be arbitrary, but its query cap still applies there.

The same-algorithm quantifier and all-input resource cap appear beside the partial-function convention and are reflected in RLe/QLe.

**Why it matters.** This blocks easier nearby statements selecting an algorithm after its input or bounding resources only on the promise.

**Direction.** Keep these choices near the definitions and retain their mutation controls in any shorter inspection route.

**Evidence.**

- repository/docs/reasoning_record.md:162–166,194–207,267–284,417
- literature/quartic-lit-buhrman-dewolf-decision-tree-survey/extracted.md, §§3.1–3.3 (printed pp. 5–8)
- repository/lean/QuarticCorpus/Unconditional/Challenge.lean
- repository/lean/QuarticCorpus/Independent/SemanticMutations.lean

**Prior-round boundary.** No previously fixed factual complaint is repeated.

## FX038

**reasoning_record · keep · keep**  
Perspective: `supportive_lean_reviewer`. Location: `repository/docs/reasoning_record.md`, §2.2, minima, Markdown line 217.

> The read-all witness is what makes them minima of nonempty sets

The record explains why natural-number infima are genuine minima and does not rely on an empty-infimum convention to produce a complexity value.

**Why it matters.** This is a meaningful definitional corner case for universal complexity theorems, including empty coordinates.

**Direction.** Keep nonemptiness and the constant-on-promise disjunction visible when summarizing the Lean definitions.

**Evidence.**

- repository/docs/reasoning_record.md:209–217,267–289
- repository/lean/QuarticCorpus/Unconditional/Challenge.lean
- literature/quartic-lit-buhrman-dewolf-decision-tree-survey/extracted.md, §§3.1–3.3 (printed pp. 5–8)

**Prior-round boundary.** No previously fixed factual complaint is repeated.

## FX039

**reasoning_record · keep · keep**  
Perspective: `supportive_lean_reviewer`. Location: `repository/docs/reasoning_record.md`, §2.6, OR2 and off-promise examples, Markdown line 374.

> The inclusive threshold is material.

OR2 reveals the exact inclusive threshold and arbitrary-real-weight issue; the true-only promise detects replacing undefined inputs by false.

**Why it matters.** These numerical consequences test meaning independently of two generated modules agreeing.

**Direction.** Preserve the probabilities and the explicitly finite scope of the tests; link each to the model convention it detects.

**Evidence.**

- repository/docs/reasoning_record.md:353–381
- repository/lean/QuarticCorpus/Independent/Semantics.lean
- repository/lean/QuarticCorpus/Independent/SemanticMutations.lean
- literature/quartic-lit-buhrman-dewolf-decision-tree-survey/extracted.md, §§3.1–3.3 (printed pp. 5–8)

**Prior-round boundary.** No previously fixed factual complaint is repeated.

## FX040

**reasoning_record · keep · keep**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/reasoning_record.md`, §2.8, shared specifications, Markdown line 472.

> The challenges compile separately but mechanically share the maintained definitions and theorem specifications.

The record explains shared-specification risk with an impossible-premise control and does not present acceptance of that bad specification as semantic validation.

**Why it matters.** A sceptic needs to know whether both sides can agree on the wrong question. The independently expected matrix makes that limit concrete.

**Direction.** Keep the independent expectation, finite scope and separation between mathematical detection and recorded native outcome.

**Evidence.**

- repository/docs/reasoning_record.md:469–481
- repository/lean/QuarticCorpus/Independent/Controls/SharedAudit.lean
- repository/lean/QuarticCorpus/Independent/Semantics.lean
- repository/docs/statement_evidence_contract.md:18–28
- literature/quartic-lit-buhrman-dewolf-decision-tree-survey/extracted.md, §§3.1–3.3 (printed pp. 5–8)

**Prior-round boundary.** No previously fixed factual complaint is repeated.

## FX041

**reasoning_record · keep · keep**  
Perspective: `quantum_model_reviewer`. Location: `repository/docs/reasoning_record.md`, §5.1, retained state, Markdown line 2246.

> Equality of label distributions alone would be insufficient.

The product/Bell-state counterexample explains why an output law does not identify a retained successful state; the route table connects this distinction to the actual headline proof.

**Why it matters.** Equal immediate measurement statistics do not justify substitution under later coherent operations.

**Direction.** Keep the counterexample, designated-subsystem target and statement that the remaining bridge is not a Proposition 3.3 premise; do not merge them into one amplification badge.

**Evidence.**

- repository/docs/reasoning_record.md:2246 onward,2736–2781
- repository/docs/expert_companion.md, Appendix A
- literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md, measurement/projector and deferred-measurement discussion (sampled).

**Prior-round boundary.** No previously fixed factual complaint is repeated.

## FX042

**reasoning_record · credit · keep**  
Perspective: `finite_probability_reviewer`. Location: `repository/docs/reasoning_record.md`, §6.1, direct-product sources, Markdown line 3234.

> Drucker's Theorem 1.1

The record credits Drucker’s conditional-value method while distinguishing the source’s global-budget theorem from the needed separate-cap vector-output claim. The borrowed method and the adapted statement are exposed rather than conflated.

**Why it matters.** Related theorem citations are not substituted for the precise required statement; the adaptation is exposed and proved.

**Direction.** Preserve source versions and theorem/lemma locators, and state what is borrowed in shorter views.

**Evidence.**

- repository/docs/reasoning_record.md:3228–3242
- literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md, §1.3 and §3 (conditional values, transcript-product law, fair-algorithm remark)
- Shaltiel is discussed in the record’s same source paragraph, but was not independently read in this pass; no separate attribution verdict about that paper is asserted here.

**Prior-round boundary.** No previously fixed factual complaint is repeated.

## FX043

**reasoning_record · keep · keep**  
Perspective: `finite_probability_reviewer`. Location: `repository/docs/reasoning_record.md`, §6.1, finite-seed endpoint, Markdown line 3262.

> Arbitrary measurable
> external randomness is handled by the ordinary finite-behavior reduction above

The finite weighted-seed restriction is local to the endpoint, and arbitrary measurable randomness is expressly left to an ordinary finite-behavior reduction.

**Why it matters.** The compared finite type is not falsely presented as quantifying over every external probability space.

**Direction.** Keep this caveat in §6.1 and §2.9. Add FX026’s separate compliance distinction alongside it, without erasing this useful qualification.

**Evidence.**

- repository/docs/reasoning_record.md:3257–3267
- repository/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean
- repository/lean/QuarticQuery/LowerBound/RealizedCaps.lean
- literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md, §1.3 and §3 (conditional values, transcript-product law, fair-algorithm remark)

**Prior-round boundary.** The finite-seed correction is already present: deliberately a keep, not a repeated defect.

## FX044

**reasoning_record · keep · keep**  
Perspective: `finite_probability_reviewer`. Location: `repository/docs/reasoning_record.md`, §6.5, capped simulator, Markdown line 3616.

> conditional success given nonheaviness

An exact adaptive example shows why success-and-nonheavy must remain a joint event, not success conditioned on nonheaviness.

**Why it matters.** An adaptive cap event can select easier inputs; the example prevents an incorrect conditioning step in the subsequent bound.

**Direction.** Keep the joint-event formulation, counterexample and explanation that no independence between query times is needed.

**Evidence.**

- repository/docs/reasoning_record.md, §6.1 cap-event corollary and §6.5 simulator example
- literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md, §1.3 and §3 (conditional values, transcript-product law, fair-algorithm remark)

**Prior-round boundary.** No previously fixed factual complaint is repeated.

## FX045

**reasoning_record · keep · keep**  
Perspective: `sceptical_statement_reviewer`. Location: `repository/docs/reasoning_record.md`, §6.7, equation (19), Markdown line 3790.

> Thus even a complete conjunction theorem for (19) does not formalize the early/late proof

The record separates the compound endpoint from formalization of the printed early/late route, and identifies shared primitives in the independently specified product experiment.

**Why it matters.** Matching endpoints do not certify a particular proof route, and independent specification does not imply independence of all modeling primitives.

**Direction.** Preserve endpoint, route, shared primitives and wrapper scope as separate dimensions; use this passage to guide other exceptional evidence rows.

**Evidence.**

- repository/docs/reasoning_record.md:3773–3792
- repository/docs/statement_evidence_contract.md:30–52
- previous_round/round5_statement_fidelity.md
- literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md, §1.3 and §3 (conditional values, transcript-product law, fair-algorithm remark)

**Prior-round boundary.** No previously fixed factual complaint is repeated.

## FX046

**reasoning_record · keep · keep**  
Perspective: `supportive_lean_reviewer`. Location: `repository/docs/reasoning_record.md`, §A.6, quartic routes, Markdown line 4191.

> The first route is the one used by the recorded headline proof

The imported library route, literal reconstruction and hybrid have separate constants and statuses, with the actual headline route identified.

**Why it matters.** A reconstruction’s larger constant does not undermine the headline, and a separately built alternative is not automatically its dependency.

**Direction.** Keep the route table and root identification rather than reducing all three implementations to one status.

**Evidence.**

- repository/docs/reasoning_record.md:4175–4191
- repository/docs/statement_evidence_contract.md:30–52
- literature/quartic-ref-03-degree-vs-approximate-degree-and-quantum-i/extracted.md, introduction and quartic upper-bound framing (sampled, not a fresh proof verification).

**Prior-round boundary.** No previously fixed factual complaint is repeated.

## FX047

**reasoning_record · keep · keep**  
Perspective: `proof_route_reviewer`. Location: `repository/docs/reasoning_record.md`, Appendix B, construction claims, Markdown line 4488.

> Essentiality is an additional diagnostic in the expanded maintained ledger

The record says essentiality strengthens printed Lemma 2.2 and that the older wrapper is partial against an expanded row, not deficient for omitting a preprint requirement.

**Why it matters.** Later diagnostics should not retroactively change what counts as proving the original statement or distort its authors’ contribution.

**Direction.** Preserve printed claim, expanded ledger and wrapper distinctions wherever the Lemma 2.2 relation is displayed.

**Evidence.**

- repository/docs/reasoning_record.md:4488 and §4.8
- paper/extracted.md, Lemma 2.2
- literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md, introduction and main results
- previous_round/round5_statement_fidelity.md

**Prior-round boundary.** The old support-clause confusion is fixed; preserve this correction.

## FX048

**exposition · question · medium**  
Perspective: `reproducibility_interface_reviewer`. Location: `repository/docs/exposition.md`, §7, trust conclusion, Markdown line 267.

> So a reader who accepts the definitions in that one file can trust the theorem without reading the proof.

Which execution assumptions accompany this trust conclusion? The expert companion says the recorded runs were local and unsandboxed. Logical agreement under the declared axioms, semantic adequacy and execution isolation are separate parts of the account; the exposition links the first two but leaves the third implicit.

**Why it matters.** A reader assessing AI-produced proof artifacts should be able to recover the stated check boundary without inferring that a recorded acceptance settles every aspect of its execution environment. This is not evidence of a failed check or a suspected exploit.

**Direction.** Point to the existing local-run qualification and state the intended trust boundary concisely. Retain the supplied acceptance facts; no rerun, security audit or new formal result is requested.

**Evidence.**

- repository/docs/expert_companion.md, Appendix A, “What it does not establish” and reproduction paragraph (lines 349–351).
- W01: official Lean “Validating a Lean Proof”, “What Needs to be Trusted?” and statement-meaning discussion; https://lean-lang.org/doc/reference/latest/ValidatingProofs/
- W02: official Lean Lake documentation, “Challenges and External Checkers”, comparator sandbox and external-checker options; https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/

**Prior-round boundary.** A bounded trust-communication question prompted by the current exposition and the existing companion qualification; no receipt re-verification.
