# Located findings: students and teachers

43 findings: 32 issues/questions and 11 keep items. IDs and text match `findings.json`.

These are modeled reading judgments unless labeled as a direct text observation. No opinions are attributed to real named researchers. Source paths refer to the supplied input packet; exact frozen source hashes are in `findings.json`.

## SX-001 · high · missing

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 26; Overview: audience. Supplied PDF p. 1.

> a graduate student who knows the query models above

The declared entry knowledge is smaller than the working prerequisite set: the crucial sampler assumes amplitude amplification, reversible computation with retained workspace, and conditional probability along an adaptive history; Section 3 also uses bounded-fan-in circuit arithmetic.

**Reader cost.** A student can satisfy the stated prerequisite and still first stall at the reversible comparison or the fixed-cap amplifier, without knowing which background to review.

**Direction.** State a short prerequisite contract and provide one precise route to the supplied lecture-note sections on amplitude amplification and probability. Distinguish assumed tools from the new tournament and planting arguments.

**Relation to round five.** The audience sentence was added after R5 ES-033; this asks whether its new prerequisite claim is operationally sufficient, not whether the audience is unnamed.

**Evidence.**

- `literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md`: Chapter 7, sections Grover’s algorithm and Amplitude amplification, lines 931–1035; Appendix 23.2, lines 3496–3536. The notes teach the geometric rotation, the need for A inverse, unknown success probability, and probabilistic tools separately; basic query-model fluency does not identify this entire package.
- `repository/docs/exposition.md`: §3, lines 124–126; §4, lines 142, 173–181; §5, lines 221–225

## SX-002 · medium · overweighted

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 26; Overview: learning outcomes. Supplied PDF p. 1.

> rederive the classical bound with its constants

Why is recovering numerical constants a headline learning outcome for this audience, while explaining how a query address becomes a simultaneous prediction is not? The rendered overview occupies about 1.76 of 14 pages, while the first numerical example begins near the bottom of page 2.

**Reader cost.** The advertised goal directs the reader toward floor arithmetic and error constants when the transferable difficulty is the capped adaptive simulation.

**Direction.** Make the reconstructable mechanism the principal learning outcome; retain constants as an optional check or secondary outcome, with the same mathematical claims and evidence.

**Relation to round five.** New audience-specific assessment; no previously fixed defect is asserted to remain.

**Evidence.**

- `repository/docs/exposition.md`: Overview line 26; §5 simulator lines 232–238; §6 line 249
- `literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md`: Chapter 7 Exercises, lines 1045–1060. The exercises ask students to reconstruct states and operations and then examine costs; this is a concrete teaching comparator, not evidence of actual reader performance.
- `repository/docs/exposition.pdf`: Physical pages 1–2; section boundaries measured in evidence/page_measurements.json. The page estimate includes title and framing; it is a space measure, not a measured reading-time estimate.

## SX-003 · medium · missing

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 26; Overview and worked-example route. Supplied PDF p. 1.

> By the end the reader should be able to build the function on a four-column board

Where can I test those learning outcomes without immediately seeing the solution? The many changed boards and probability counterexamples are already worked out for me.

**Reader cost.** Reading and recognition may look like mastery even when the student cannot choose the invariant or diagnose the changed hypothesis independently.

**Direction.** Turn a few existing changed-case examples into pause-and-predict checks or optional exercises, with answers separated from the first reading route; assess the same mechanisms already proved.

**Relation to round five.** New audience-specific assessment; no previously fixed defect is asserted to remain.

**Evidence.**

- `repository/docs/exposition.md`: Overview line 26; §2 line 108; §4 lines 146–148; §5 lines 218, 230
- `literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md`: Chapter 7 Exercises, lines 1045–1060; Preface lines 6–8. The supplied teaching comparator explicitly separates exposition and reconstruction exercises.
- `skills/record-to-expository/SKILL.md`: Workflow step 6, lines 178–186. The method already asks for a changed-case task and retrieval without repeating its worked solution.

## SX-004 · high · unclear

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 32; Overview: reason for four. Supplied PDF p. 1.

> locating it inside one column means naming an address, which costs $L$ queries there

Does this sentence assert that reaching a true cell requires paying L queries? Section 5 correctly allows a lucky address guess and bounds a joint event. The overview still sounds like a deterministic information charge in every column.

**Reader cost.** A student may carry an invalid lower-bound heuristic through the later argument and regard the simulator as technical overhead instead of the step that justifies the heuristic.

**Direction.** Qualify the first cost intuition as the aggregate consequence of the later guessing bound, and explicitly preserve the erased-zero alternative. Do not weaken the correct simulator argument.

**Relation to round five.** CM-003/ES-004 repaired the detailed true-cell paragraph. This finding concerns the surviving overview shorthand and its conflict with that repaired explanation, not the repaired paragraph itself.

**Evidence.**

- `repository/docs/exposition.md`: §5 The true cell, lines 214–238
- `paper/extracted.md`: §1.2, paragraph beginning The classical proof starts. The preprint overview separates finding the erased zero from finding the cell and describes the latter as many queries or a correct guess.

## SX-005 · medium · underweighted

**Reader:** lecturer. **Text:** `repository/docs/exposition.md`, line 38; Overview: Where this sits, final paragraph. Supplied PDF p. 2.

> The same arithmetic shows why the earlier route stops at three.

What made AND-OR composition necessary in the earlier route, and which structural cost has the new addressed-column tournament avoided? The current calculation compares exponents, but a student who has never seen a cheat sheet has not yet learned why the old construction had that certificate-verification cost.

**Reader cost.** The student can read the historical progression while still treating the improvement from three to four as a fortunate substitution of m for n. That weakens the explanation of the actual contribution.

**Direction.** Tie the existing arithmetic to the old need for cheaply verifiable domain certificates and the new separation between cheap comparison and expensive final verification. A compact mapping of roles and costs can support the existing paragraph without expanding the history.

**Relation to round five.** New audience-specific assessment of the current text; no repaired round-five issue is asserted to remain.

**Evidence.**

- `literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md`: §3.1, extracted lines 1331–1337 and 1417–1425. The cheat-sheet overview motivates AND-OR by the difficulty of certifying domain membership and then accounts for certificate checking.
- `repository/docs/expert_companion.md`: §1.1, line 44; §1.2, line 61. The expert companion contains the certificate-size cost and explains why cheap comparisons avoid nested full verification.

## SX-006 · keep · keep

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 38; Overview: exponent mechanism. Supplied PDF p. 2.

> The same arithmetic shows why the earlier route stops at three.

Keep the comparison between the earlier cubic arithmetic and the two quadratic contributions in the new family.

**Reader cost.** It explains the title as a mechanism rather than merely simplifying exponents at the end, and it tells a student what the new construction must accomplish.

**Direction.** Preserve the argument and attribution while giving any recovered space to the sampler and simulator.

**Relation to round five.** Extends ES-033’s keep recommendation: the explicit cube-versus-four arithmetic is an audience-facing strength.

**Evidence.**

- `repository/docs/exposition.md`: Overview lines 28–38
- `paper/extracted.md`: §1.1–§1.2

## SX-007 · medium · missing

**Reader:** lecturer. **Text:** `repository/docs/exposition.md`, line 51; Overview, reading guidance. Supplied PDF p. 2.

> The boxed proof in Section 5 can be skipped;

What is the shortest assignable route for a quantum algorithms class, and what is the shortest route for a randomized lower-bounds class?

**Reader cost.** Only one skip decision is advertised. A teacher still has to infer which detailed circuit arithmetic, minimax sketch, historical paragraph and formal audit can be treated as supplied results without breaking the later proof.

**Direction.** Add a compact assignment route with retained statements and exact departure/return points. Use the existing section boundaries and name the different endpoints; do not remove the shared theorem statement.

**Relation to round five.** R5 ES-015 correctly moved the direct-product statement outside its optional box; this asks for course-level routes beyond that completed repair.

**Evidence.**

- Current exposition §§3, 4 Amplification with a fixed cap, 5 Proof of the direct product, and 7.
- skills/record-to-expository/SKILL.md, lines 147–150, requires a usable optional route with needed imported conclusions.

## SX-008 · medium · missing

**Reader:** lecturer. **Text:** `repository/docs/exposition.md`, line 51; Overview, links between the three documents. Supplied PDF p. 2.

> Full proofs of every step are in the

When should a student leave this exposition for the expert companion rather than for the complete record?

**Reader cost.** The current paper provides proof links to the record but does not explain the useful intermediate role of the expert companion. A lecturer assembling an assignment has to rediscover its concise shortcut table, method comparison and statement audit.

**Direction.** Give one concise cross-document reading choice with exact sections: exposition for construction, expert companion for comparisons or the formal audit, record for a selected proof. Avoid asking the student to read all three beginnings.

**Relation to round five.** New audience-specific assessment of the current text; no repaired round-five issue is asserted to remain.

**Evidence.**

- Current exposition Overview line 51 links the record but does not name the expert companion.
- Expert companion §1.1 and §3 are natural comparative destinations.
- Reasoning record §1.1 Reading routes already links both shorter accounts in the opposite direction.

## SX-009 · high · unclear

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 74; §1: projection experiment. Supplied PDF p. 3.

> The quantum algorithm for $P$ starts in $u$

Is this the raw projection experiment or already a bounded-error decoder for every promised input? The three chosen inputs have projection probabilities 1, 0, 1. They hide the need for repetition: in the same supplied four-bit-block universe, 1111 1000 has Phi=1/2, P=1 and one-shot acceptance 1/4.

**Reader cost.** The student can incorrectly infer that the two-query experiment itself satisfies the 2/3 correctness requirement. Section 3 later supplies the correct repeated decoder, but the interface between the two presentations is unstated.

**Direction.** Label the experiment and the amplified decoder separately, and explicitly connect the Section 1 experiment to the repetition step in Section 3. The existing full small-instance census already contains the non-extreme positive values.

**Relation to round five.** ES-017 added the correct alignment and projection explanation. This is a remaining raw-experiment versus amplified-decoder transition, not a claim that the overlap calculation is absent or wrong.

**Evidence.**

- `repository/docs/exposition.md`: §1 lines 72–76; §3 line 124
- `repository/docs/reasoning_record.md`: §3.5 #forr_small_instance, lines 909–916. The existing census has 96 inputs at numerator N=4, hence Phi=1/2.
- `checks/exact_examples_results.json`: forrelation.one_shot_diagnostic. Exact diagnostic using the existing Walsh matrix; the amplified algorithm of §3 is not contradicted.

## SX-010 · low · question

**Reader:** lecturer. **Text:** `repository/docs/exposition.md`, line 76; §1: concluding explanation of the three inputs. Supplied PDF p. 3.

> a quantum test that cannot tell $a^+$ from $a^-$

Would a short comparison with the cited sign-sensitive experiment help explain the choice of the Phi-squared decoder? The text already scopes its statement to a quantum test. Bansal–Sinha Proposition 1.2 describes acceptance probability (1+Phi)/2, so this example demonstrates the behavior of the chosen test rather than an impossibility of distinguishing the signs.

**Reader cost.** This is optional literature orientation for a lecturer, not a claim that the exposition asserts an impossible quantum task. It helps distinguish an illustrative decoder choice from the general reason a promise algorithm supplies no off-promise correctness guarantee.

**Direction.** If space and audience warrant it, briefly identify the standard source experiment and scope the sign-blindness lesson to the chosen projection test. Keep the present algorithm and examples; no optimization or new construction is requested.

**Relation to round five.** ES-017 correctly supplied the overlap interpretation. This concerns the scope of the resulting pedagogical lesson relative to the cited algorithm, not a request to undo that improvement.

**Evidence.**

- `literature/quartic-ref-06-k-forrelation-optimally-separates-quantum/extracted.md`: §1, Proposition 1.2, source PDF printed p. 2; extracted lines 32–38. The standard circuit has acceptance probability (1+forr_k)/2 and uses ceil(k/2) queries.
- `repository/docs/exposition.md`: §1, line 74; §3, line 124. The actual chosen test squares the amplitude and is correctly amplified on its promise.

## SX-011 · medium · underweighted

**Reader:** lecturer. **Text:** `repository/docs/exposition.md`, line 94; §2: attribution and address length. Supplied PDF p. 3.

> they used about $10\log n$ copies, and here $r=20\log_2m$

Why are there logarithmically many hard answers in an address, and what job does 20 do? The first explanation is a numerical comparison with cheat sheets; the design purpose only becomes visible at the very end of the lower bound.

**Reader cost.** The largest component of the input, the m^20 cell array, appears before the student understands why a long address is necessary. The direct product may then look like a theorem added afterward rather than the reason for the address length.

**Direction.** At the introduction of r, identify the existing purpose: exponentially suppress a complete guessed address enough to union bound over all G candidate queries, while keeping quantum decoding polylogarithmic and the cell array polynomial in m. Keep the exact coefficient as one convenient sufficient choice.

**Relation to round five.** New audience-specific assessment of the current text; no repaired round-five issue is asserted to remain.

**Evidence.**

- `repository/docs/exposition.md`: §5, lines 236–241. The proof uses G(2/3)^r and chooses r to make it negligible.
- `literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md`: §3.1, extracted lines 1427–1431. The cited construction motivates multiple answers as enough bits to address a large array before giving the total function.

## SX-012 · medium · question

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 96; §2: toy parameters. Supplied PDF p. 4.

> only $r=2$ address inputs per column

Which later statements may I infer from this board, and which require resetting its parameters? The paper correctly says r=2 for display and L_(2,4)=0, then resumes r=20 log_2 m in the lower-bound analysis.

**Reader cost.** The same board persists visually while its addressing multiplicity and hardness regime change. A novice can transfer the construction checks correctly but also transfer an unavailable asymptotic lower bound.

**Direction.** Provide a compact map from toy choices to theorem choices, naming the unchanged winning/local-test definitions and the unavailable hardness guarantee; reuse that map at the Section 5 reset.

**Relation to round five.** The small-size caveat and r=2 declaration are already present and must be kept. The request is to connect the two caveats to the later transfer, not to report either as missing.

**Evidence.**

- `repository/docs/exposition.md`: §1 line 76; §2 lines 94–104; §3 lines 128–134; §5 lines 193, 241

## SX-013 · keep · keep

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 108; §2: domain-bit mutation. Supplied PDF p. 5.

> A function that checked only value bits would accept this board.

Keep the changed-domain-bit board and its downstream recall during verification.

**Reader cost.** The student sees why totalizing a promise problem requires checking the promise; the raw quantum acceptance of a^- then has a concrete consequence.

**Direction.** Retain the shared input and show its connection to the nonwinner-fails-at-every-address verifier claim.

**Relation to round five.** ES-035/ES-034 are valuable and remain successful.

**Evidence.**

- `repository/docs/exposition.md`: §1 line 74; §2 line 108; §4 line 183

## SX-014 · medium · underweighted

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 114; §2: local tests. Supplied PDF p. 5.

> On the board $K=4+3+2(180+2)=371$

Can I execute one gate test and one pointer test, naming the input coordinates queried, before being asked to remember the total 371?

**Reader cost.** The board is a useful representation, but the transition from a stored certificate to the cheap test oracle is still compressed into counts. This operation later determines why quantum verification costs sqrt(K). Free computation does not make the unknown input bits free: the known circuit and the proposed gate-value bits have different roles, and S controls the number of constraints to search.

**Direction.** Use an existing gate or pointer from the supplied circuit/board to trace a local check and its bit-query cost; reduce peripheral total-bit arithmetic if space is needed. Do not reproduce the 180-gate circuit. State explicitly that the circuit is public and fixed, while proposed gate values are input bits whose consistency is queried.

**Relation to round five.** ES-018 already supplies the gate-list/checker link. This finding asks for an instructional operation before the count, not a missing circuit source.

**Evidence.**

- `repository/docs/exposition.md`: §2 lines 106–114; §4 line 183
- `repository/docs/reasoning_record.md`: §4.4 #AC-example-tests, with the supplied circuit checker and local-test families
- `repository/docs/exposition.md`: Overview line 12; §2 lines 106–114; §4 line 183. These passages provide the ingredients but distribute the resource explanation.
- `paper/extracted.md`: §1.3, extracted lines 120–123; §2.3, Lemma 2.2. Transcripts store non-input gate values; actual input bits are read when needed.
- `literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md`: §3.1, extracted lines 1331–1337. Cheaply checking a domain certificate is the motivating obstacle for cheat sheets.

## SX-015 · keep · keep

**Reader:** lecturer. **Text:** `repository/docs/exposition.md`, line 122; §3, the ingredient interface. Supplied PDF p. 5.

> The construction needs three facts about $P_{k,m}$.

Keep the three-part interface separating cheap quantum decoding, exact certification and classical hardness.

**Reader cost.** The roles tell a student what must be imported to build the total function and why a single partial-function theorem is insufficient.

**Direction.** Preserve the three roles and their destinations; make their later uses explicit when allocating space, without forcing the student through the full hardness proof. Distinguish the accepted hardness theorem from decoder and circuit details the student may check; §3 already gives a valid interface.

**Relation to round five.** New audience-specific assessment of the current text; no repaired round-five issue is asserted to remain.

**Evidence.**

- Current exposition §3 lines 122–134; §4 uses decoder and circuit size, §5 uses hardness.

## SX-016 · low · question

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 140; §4: Comparing two columns; Sampling a pivot quantumly. Supplied PDF p. 6.

> and we set $a_{ii}=0$.

When the uniform candidate register equals a previous pivot, what does the implemented circuit do? The definition sets a diagonal probability to zero, but the sampler is described as running the comparison against every pivot. A student implementing the described steps needs to connect the convention to the equality branch.

**Reader cost.** Without that connection, the zero weight of an already selected candidate looks like an analytical assignment rather than a property of the successful-label circuit.

**Direction.** Name the existing query-free self-comparison branch when the sampler is introduced, and connect it to the fact that previously listed candidates cannot be sampled again.

**Relation to round five.** New audience-specific assessment of the current text; no repaired round-five issue is asserted to remain.

**Evidence.**

- `repository/docs/reasoning_record.md`: §5.2 #upper-stage-state, line 2375. The record explicitly sets the self-comparison outcome to false without querying.
- `repository/docs/reasoning_record.md`: §5.2 #upper-ideal-process, line 2318. A selected vertex gets the zero self-factor and cannot be selected again on a positive-weight step.

## SX-017 · keep · keep

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 146; §4: dominance versus winning. Supplied PDF p. 6.

> A column that dominates the comparisons is only a candidate

Keep the one-pointer mutation that produces a dominating nonwinner.

**Reader cost.** It isolates why candidate discovery is insufficient for deciding a total function, so final verification has a logical role rather than appearing as a technical extra.

**Direction.** Preserve it before the tournament analysis and reuse it for an optional prediction exercise.

**Relation to round five.** ES-036/QM-030 remain successful.

**Evidence.**

- `repository/docs/exposition.md`: §4 line 146 and verification line 183

## SX-018 · keep · keep

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 167; §4: drift identity. Supplied PDF p. 7.

> No transitivity and no margin away from $1/2$ is used.

Keep the four-pivot table directly beside the paired-term drift identity.

**Reader cost.** The finite calculation shows exactly which comparison hypothesis matters and makes the general halving argument reconstructable.

**Direction.** Preserve the separation between the cycle obstruction to sorting and the absence of margin for a fixed bounded-error predicate.

**Relation to round five.** The round-five distinction between cycles and bounded-error predicates is now correctly made and should survive.

**Evidence.**

- `repository/docs/exposition.md`: §4 lines 148–171

## SX-019 · high · underweighted

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 177; §4: quantum pivot sampling. Supplied PDF p. 8.

> Success has probability $|w|/m$

Can one row of the four-column weight table be carried through the actual coherent preparation, the probability of success, the conditional pivot distribution and amplification? The scalar equations are correct, but the promised hand-run currently stops at the ideal weights.

**Reader cost.** This is the point where a student must discover how an analysis-only weight becomes an implementable distribution. A general product formula alone is a large jump from the preceding numerical table.

**Direction.** Continue the existing cycled-board example through one sampler stage, explicitly identifying the success flag and which conditional probabilities amplification preserves. Reuse the existing numerical stage in the record.

**Relation to round five.** ES-003/ES-009 and QM-013 have repaired reversibility, conditioning, and the fractional ideal example. This is an assessment of how those correct parts connect for the stated student, not a repeat of their former omissions.

**Evidence.**

- `repository/docs/exposition.md`: §4 table lines 156–161 and sampler lines 173–179
- `repository/docs/reasoning_record.md`: #upper-cyclic-example, lines 2421–2431. The record already gives unamplified mass 23999/48000 and conditional probabilities 11999/23999 and 12000/23999; no new construction is needed.
- `literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md`: Chapter 7, Amplitude amplification; Chapter 7 Exercise 1. The teaching comparator moves from the algorithm to explicitly reconstructing states and probabilities.
- `checks/exact_examples_results.json`: tournament.after_pivot_2_*. After pivot 2, success-and-label masses are (1/4,0,0,1/4), success mass is 1/2, and the conditional pivot law is (1/2,0,0,1/2). This is a check of the supplied example, not a new general claim.

## SX-020 · medium · unclear

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 179; §4: success and failure events. Supplied PDF p. 8.

> After the winner is listed nothing is claimed

Which failure is being bounded at each layer: a promise decoder error, failure to produce a pivot, omission of the winner from the list, or false acceptance by the final verifier?

**Reader cost.** The repaired conditions are now correct, but one paragraph carries several probabilities all near epsilon. A student may wrongly transfer the pre-winner guarantee to a zero-input or to verification.

**Direction.** Make a compact event-and-scope ledger for the already stated guarantees, including what remains universally bounded on zero-inputs. Keep the stopping rule and winner-conditional qualification intact.

**Relation to round five.** ES-001/ES-008 are mathematically fixed. This is a usability assessment of the denser corrected contract, not a request to re-add its conditions.

**Evidence.**

- `repository/docs/exposition.md`: §4 lines 140, 179, 181, 183, 185
- `literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md`: Appendix 23.2, lines 3528–3536. The notes distinguish worst-case error and query cost and then explain how subroutine errors compose.

## SX-021 · keep · keep

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 179; §4: Sampling a pivot quantumly. Supplied PDF p. 8.

> but stopping cannot remove a listed column.

Keep the explanation of why sampler failure after the winner enters the list is harmless. It aligns an unconditional running-time cap with the conditional success analysis and makes the algorithm meaningful on zero-inputs.

**Reader cost.** A student trained on expected-time amplitude amplification may otherwise import a retry-until-success procedure that fails to terminate when the marked mass is zero.

**Direction.** Preserve the stop-and-verify action, empty-list output, and the pre-selection scope of the failure bound whenever the quantum argument is shortened.

**Relation to round five.** ES-001/ES-008 and QM-001/QM-002 repaired these statements. Their instructional value is high and the fixes should survive compression.

**Evidence.**

- `literature/quartic-ref-12-quantum-amplitude-amplification-and-estima/extracted.md`: §2, Theorem 3, extracted line 117. The standard unknown-success-probability QSearch theorem permits running forever when success mass is zero.
- `literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md`: Chapter 7, Grover variants, extracted lines 1004–1006. The lecture notes distinguish expected query counts and conversion to a worst-case cap.
- `paper/extracted.md`: §3.2, extracted lines 428–444. The supplied theorem stops at sampler failure and bounds every branch.

## SX-022 · medium · overweighted

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 181; §4: fixed-cap amplification. Supplied PDF p. 8.

> at least $9/40$ whenever $p\ge\gamma$

Why must a first-pass reader process the 9/40, 40/31 and randomized iteration count on the main route before seeing the algorithm finish?

**Reader cost.** The contract needed by the sampler is delicate and important, but the numerical proof of a standard primitive competes with the new use of that primitive.

**Direction.** Keep the all-input cap, thresholded failure guarantee, zero-success case and exact conditional law in the main text; make the numerical derivation an explicitly optional proof or record excursion.

**Relation to round five.** QM-033 appropriately kept the full amplifier contract. The recommendation preserves that contract and changes the reading priority of its numerical derivation.

**Evidence.**

- `repository/docs/exposition.md`: §4 line 181
- `repository/docs/reasoning_record.md`: §5.1 #upper-amplification-proof
- `skills/record-to-expository/SKILL.md`: Frame before examples, lines 78–82. The method already recommends boxing standard amplification proofs; the present contract should remain visible while the proof route becomes optional.

## SX-023 · medium · misplaced

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 193; §5: hard distribution. Supplied PDF p. 9.

> separating that hull from the orthant $[2/3,\infty)$

Why am I asked to parse a convex-separation proof sketch in the first paragraph of the planted-input section, before I have seen the pair it supplies?

**Reader cost.** For the stated background, the one-sentence parenthesis introduces a different mathematical language without enough space to learn it. It delays the concrete operation advertised by the heading.

**Direction.** Treat the finite hard-law consequence as the local interface, state what mu guarantees, and make the already linked separation argument an optional background route.

**Relation to round five.** CM-016/ES-016 replaced a longer box with this correct parenthesis. The fix reduces length but leaves a background-prerequisite detour at the section entrance; this is a different placement assessment.

**Evidence.**

- `repository/docs/exposition.md`: §5 line 193
- `repository/docs/reasoning_record.md`: §6.2 #CL-minimax

## SX-024 · medium · unclear

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 195; §5: planted-pair example reset. Supplied PDF p. 9.

> the planted input is column $1$'s part of Figure 2

Exactly what is retained from Figure 2 when the planted pair is drawn? Figure 2 has an unpromised address input in column 2, whereas every address input in the lower-bound experiment is now drawn from a distribution on promised inputs.

**Reader cost.** The current qualification about column 1 is correct, and the new figure labels use mu, but a student following the persistent board can silently carry the old loser input or old nonblank cells into the distributional proof.

**Direction.** Mark the reset explicitly: shared board layout and the displayed planted winner, resampled promised address inputs, and initially blank cells. Keep the two-change coupling claim scoped to Y0 versus Y1.

**Relation to round five.** No mathematical inconsistency in the supplied diagram is asserted; the diagram correctly uses mu. The finding concerns an unannounced example reset.

**Evidence.**

- `repository/docs/exposition.md`: §2 lines 100–106; §5 lines 193–197
- `repository/docs/figures/exposition/fig4_planted.tex`: Both boardcolumn blocks label A_(i,h) as sampled from mu

## SX-025 · low · question

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 204; §5: The pair, first-difference inequality. Supplied PDF p. 9.

> where both events refer to the run on the dummy input.

Does visiting the true cell necessarily distinguish the pair? Some bits in its filled contents can still equal the blank bits. The proof safely counts every visit, but the exposition does not say that this is an overestimate of seeing a changed bit.

**Reader cost.** A reader may think the simulator must read a nonzero certificate bit or recognize a valid transcript before outputting an address. The reduction only uses the proposed cell coordinate.

**Direction.** Explain the one-way inclusion from first differing answer to a visit to one of the two changed locations, and distinguish a cell visit from observing an actually changed cell bit.

**Relation to round five.** New audience-specific assessment of the current text; no repaired round-five issue is asserted to remain.

**Evidence.**

- `paper/extracted.md`: §4.2, extracted lines 608–616. The source says counting every cell visit is an upper bound even when the queried bit agrees with its blank value.
- `repository/docs/reasoning_record.md`: §6.3 #CL-first-difference, line 3411. The record explicitly separates full cell visits from changed-bit exposure.
- `repository/docs/exposition.md`: §5, line 232. The simulator outputs the address before reading the cell contents.

## SX-026 · medium · underweighted

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 210; §5: The erased zero. Supplied PDF p. 9.

> an undiscovered zero is uniform among its column's unread positions

Why is the zero still uniform after all the adaptive queries to other fields? The sampling independence is stated correctly, but the reader must infer that conditioning on the entire dummy transcript preserves uniformity among unread positions because the other fields are independent and every cell is blank.

**Reader cost.** This is a reusable lower-bound idea. Applying the same sentence to the planted run would be unsafe, since its filled cell contains pointers to other zeros. The reason for analyzing the dummy execution deserves to be explicit.

**Direction.** Identify the conditioning as the full dummy transcript and state the role of blank cells in preserving the residual uniform law. Tie it to the earlier decision to measure both exposure events on the dummy run.

**Relation to round five.** CM-005 fixed mutual independence in the sampling definition. This asks for the distinct conditional-law argument after adaptive observations.

**Evidence.**

- `paper/extracted.md`: §4.2, extracted lines 618–622. The source explicitly explains why the full adaptive transcript preserves residual uniformity.
- `repository/docs/reasoning_record.md`: §6.3 #CL-dummy, line 3358; §6.4 #CL-early-late. Blank cells reveal neither a zero location nor a partial-function value; the search estimate is in the dummy world.

## SX-027 · medium · unclear

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 218; §5: AND examples use different laws. Supplied PDF p. 10.

> For AND on two independent uniform two-bit inputs

Why is the one-query baseline for AND 3/4 here but 2/3 in the next example? The first law is uniform on all four inputs; the second is uniform on 01, 10 and 11.

**Reader cost.** The examples correctly refute different shortcuts, but switching the distribution while retaining the same function name and beta notation can obscure that hardness is a property of a function together with a law and a cap.

**Direction.** Make a small hypothesis-change map for the pooled-budget, parity-information and lightness examples, including each input law, cap and baseline beta. Keep the numerical counterexamples.

**Relation to round five.** The earlier requests for pooled-budget and joint-event counterexamples were fixed. This assesses how their distinct settings are differentiated when placed close together.

**Evidence.**

- `repository/docs/exposition.md`: §5 lines 218 and 230
- `repository/docs/reasoning_record.md`: §6.1 #CL-independent-information and #CL-adaptive-example

## SX-028 · medium · underweighted

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 221; §5: product posterior. Supplied PDF p. 10.

> the tuples consistent with $\tau$ form a product

Can I see one reachable adaptive query history decomposed into its E_h sets before the product of conditional values is used? The text proves the product claim, but the only nearby numerical examples demonstrate failures after changing assumptions.

**Reader cost.** A student may remember the counterexamples and still be unable to apply the positive invariant that makes the simulator work.

**Direction.** Use one of the existing finite examples to mark an actual reachable leaf, its coordinatewise constraints and remaining allowances, then contrast that event with conditioning on cheapness. This can be a short check for the reader, not an additional proof theorem.

**Relation to round five.** ES-010 repaired the proof: factorization, remaining budget, and averaged inequality are all present. This finding concerns worked application of the repaired invariant.

**Evidence.**

- `repository/docs/exposition.md`: §5 direct-product proof, lines 221–225
- `repository/docs/reasoning_record.md`: §6.1 #CL-product-law and #CL-adaptive-example

## SX-029 · keep · keep

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 230; §5: joint-event counterexample. Supplied PDF p. 11.

> its success given that it stays light is $1$

Keep the short three-input AND example demonstrating selection bias.

**Reader cost.** It explains why the crucial probability has lightness inside the event and prevents an intuitive but invalid use of independence after adaptive selection.

**Direction.** Preserve this example next to the simulator; clarify its different input law from the pooled-budget example.

**Relation to round five.** ES-037 remains successful.

**Evidence.**

- `repository/docs/exposition.md`: §5 lines 230–236

## SX-030 · high · underweighted

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 232; §5: simulator query caps. Supplied PDF p. 11.

> stops before the $(L+1)$-st of these

Why does a shared cap of L queries over a whole column permit invoking a lemma with L queries to each of r inputs? Where is the possible r factor lost?

**Reader cost.** The implication is elementary but central: the simulation uses a stronger aggregate cap, which implies every separate cap. Without making that relation visible, a student can think the lower bound assumes an rL allowance or has dropped an r.

**Direction.** Show the three budgets side by side: whole algorithm G, target-column aggregate L, and each component cap at most L. Connect this to the heavy-column counting and the simulator abort rule.

**Relation to round five.** New audience-specific assessment; no previously fixed defect is asserted to remain.

**Evidence.**

- `repository/docs/exposition.md`: §5 lines 214, 216, 232
- `repository/docs/reasoning_record.md`: #CL-heavy, lines 3553–3554; #CL-simulator, lines 3559–3564. The record explicitly states that the shared target cap implies all separate caps.

## SX-031 · medium · unclear

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 236; §5: simulator proof excursion. Supplied PDF p. 11.

> traces the simulator on a small board, including a run where it stops

What changes when I follow the simulator link? Its destination eventually says “Return to the four-column XOR example”, with L=1 and zero-based labels. The record does identify the toy, but the incoming link does not prepare a student arriving from the one-based Forrelation board or identify the earlier XOR setup.

**Reader cost.** The student follows the link precisely because the simulation is hard. Reconstructing a second setup at that point adds avoidable work and makes the 1/4 success bound appear unrelated to the displayed (2/3)^r bound.

**Direction.** Announce the different partial function and indexing at the departure, and link the worked trace directly after the proof link. Supply a compact translation or a precise pointer to the existing XOR setup. Preserve the distinction between a generic reduction example and an asymptotic hard instance.

**Relation to round five.** ES-011 correctly added a real proof link and the trace exists. This is a handoff problem created by linking a different worked instance, not the old absence-of-trace complaint.

**Evidence.**

- `repository/docs/exposition.md`: §5 line 236
- `repository/docs/reasoning_record.md`: #CL-simulator-example, lines 3581–3608. The record explicitly returns to a four-column XOR toy, queries X_0[0], and uses beta=1/2.

## SX-032 · keep · keep

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 259; §6: order of quantifiers. Supplied PDF p. 12.

> choosing $\alpha$ first, then a single $k$, then letting $m$ grow

Keep the fixed-parameter quantifier warning and the t>=2^k example.

**Reader cost.** The title can otherwise be mistaken for a fixed-k exact fourth-power family or an unsupported growing-k schedule. This is a reusable asymptotic reasoning lesson.

**Direction.** Retain the warning and let students identify the required k for a chosen target exponent before reading the conclusion.

**Relation to round five.** ES-039 remains successful.

**Evidence.**

- `repository/docs/exposition.md`: §6 lines 253–259
- `repository/docs/reasoning_record.md`: §1 #R3-01-QUANTIFIERS; §7.1

## SX-033 · medium · evidence_presentation

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 265; §7: first formal reading. Supplied PDF p. 12.

> Five definitions carry the content.

For a first formal-proof encounter, which one linked definition should I inspect and what exact question should I answer about it? Five definitions expand into many links before the student reaches the same/weaker/stronger qualifications.

**Reader cost.** The evidence is inspectable and candid, but the reading task is still an audit rather than a learnable first step; a student may skip the whole section or mistake opening the file for checking its meaning.

**Direction.** Give one explicitly optional first inspection task using an existing definition and an already solved board, then route broader theorem-fidelity auditing to the record. Keep all scope qualifications and receipt links available.

**Relation to round five.** ES-026/ES-028 fixed the placeholder explanation and five-definition reading guide. This recommendation gives that valid guide an assessable student task.

**Evidence.**

- `repository/docs/exposition.md`: §7 lines 265–269
- `reader_principles.md`: Principles 7, 10 and 12

## SX-034 · keep · keep

**Reader:** student. **Text:** `repository/docs/exposition.md`, line 267; §7: semantic boundary. Supplied PDF p. 12.

> do these definitions mean $R$, $Q$ and the function intended?

Keep the explicit separation between proving a formal statement and checking that its definitions express the intended mathematics.

**Reader cost.** A student gets a precise way to read machine-checked evidence without mistaking it for independent mathematical judgment or a test of attribution.

**Direction.** Retain the same/weaker/stronger comparisons and the human-review boundary even if the first reading route through the section is shortened.

**Relation to round five.** ES-040/ES-041 remain successful.

**Evidence.**

- `repository/docs/exposition.md`: §7 lines 267–269
- `reader_principles.md`: Principles 7 and 10

## SX-035 · medium · unclear

**Reader:** lecturer. **Text:** `repository/docs/exposition.md`, line 269; §7, final helper-result paragraph. Supplied PDF p. 13.

> The separation needs neither:

Which two requirements are unnecessary for the separation, and which amplification and direct-product guarantees are still essential?

**Reader cost.** After two stronger-or-narrower helper comparisons, the pronoun can be read as saying that the separation does not use the two tools taught in §§4–5. The following clause contains the intended distinction, but the student must resolve that dependency while also learning formal evidence classes.

**Direction.** Name the two unused extensions explicitly and map the actually used label-law and finite-input direct-product facts back to their mathematical uses. Do not change the evidence status.

**Relation to round five.** New audience-specific assessment of the current text; no repaired round-five issue is asserted to remain.

**Evidence.**

- Current exposition §7 line 269; compare the actual sampler use in §4 lines 173–181 and direct-product use in §5 lines 232–236.

## SX-036 · medium · overweighted

**Reader:** lecturer. **Text:** `repository/docs/expert_companion.md`, line 73; §1.4 Plan. Supplied PDF p. 3.

> Section 2 defines the Forrelation promise and the total function,

For a lecturer assigning the expert companion as a follow-up, can the opening reach the new proof sooner without redoing the exposition's orientation?

**Reader cost.** The abstract and §1 occupy about 3.1 page-equivalents before construction starts on page 4. The mechanisms and credit are valuable, but a student who has already read the exposition meets the same story several times before the proof layer changes.

**Direction.** Keep the expert paper independently readable, but add a precise entry for readers coming from the exposition and evaluate repeated mechanism passages against the space given to the sampler and capped simulator.

**Relation to round five.** An audience-relative weighting judgment for the requested student/teacher panel, not a claim that specialist context is unnecessary.

**Evidence.**

- Supplied expert_companion.pdf: construction heading on physical p.4, y≈111/842; opening/abstract therefore about 3.13 page-equivalents.
- Current expert companion abstract and §§1.1–1.4; current exposition Overview and §2.

## SX-037 · keep · keep

**Reader:** lecturer. **Text:** `repository/docs/expert_companion.md`, line 120; §3, shortcut table. Supplied PDF p. 5.

> Each row of Table 1 is a step a reader may be tempted to simplify

Keep the shortcut table as a seminar and follow-up resource: it separates different failed simplifications instead of presenting all technical conditions as arbitrary caution.

**Reader cost.** The lecturer can ask students to diagnose which hypothesis each example breaks, then send them to an exact proof destination. The current cycle/no-margin distinction and joint-event example make this especially useful.

**Direction.** Preserve the exact shortcut-to-counterexample matching and use the table as an optional post-exposition check. Do not turn every row into prerequisite material for the first reading.

**Relation to round five.** Protects the corrected round-five table, especially the distinction between cycles and unbiased comparisons.

**Evidence.**

- `repository/docs/expert_companion.md`: §3, Table 1 and following AND calculation. Eight distinct failed shortcuts with proof destinations.
- `reader_principles.md`: Principles 4, 5, 12 and 14. Hypothesis purpose, relationship explanation, and reader performance.

## SX-038 · medium · unclear

**Reader:** lecturer. **Text:** `repository/docs/expert_companion.md`, line 196; §5.1, direct-product proof. Supplied PDF p. 8.

> zero-weight branches need no division.

Why does the companion switch from the exposition’s conditional success values to unnormalized measures and a tree induction, and where is the correspondence between the two proofs explained?

**Reader cost.** A student following the shorter companion after §5 may treat V_d and V_h as unrelated machinery, even though the record explicitly presents these as two proof routes. A lecturer needs to choose one route without implying that both are additional prerequisites.

**Direction.** Name the change of normalization and its benefit for zero-mass branches; point to the record’s existing second proof and give a clear return point. Preserve both correct proofs without reproducing either in the other document.

**Relation to round five.** New cross-document assessment of the supplied current text.

**Evidence.**

- `repository/docs/exposition.md`: §5, Proof of the direct product, lines 221–225. Conditional values with remaining allowances.
- `repository/docs/reasoning_record.md`: §6.1, “Optional: a second proof with unnormalized weights”, #CL-weighted-values; #CL-normalization, lines 3182–3202, equation (6.11). The existing destination gives the alternate proof and explicitly relates conditional values to unnormalized product values.
- `literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md`: §1.3 and §3, conditional values and the product posterior. Primary-source baseline for the conditional-value presentation.

## SX-039 · low · question

**Reader:** lecturer. **Text:** `repository/docs/expert_companion.md`, line 283; §7, remark on letting k grow. Supplied PDF p. 10.

> This needs control uniform in $k$

Would a lecturer assign the growing-k remark on the first follow-up reading, or reserve it for a later question? It already names the extra uniform controls and is clearly labeled as a remark; its remaining issue for this panel is priority within the assignment.

**Reader cost.** The fixed-k proof has already delivered the main learning outcome. The additional schedule is a legitimate second objective with more quantitative dependencies, and the course route should say whether to pursue it.

**Direction.** Treat the existing remark as optional further reading in the assignment guide. Preserve its uniform hypotheses and its distinction between nearly fourth-power and exact fourth-power separation. No mathematical correction to the remark is asserted.

**Relation to round five.** New cross-document assessment of the supplied current text.

**Evidence.**

- `repository/docs/exposition.md`: §6, lines 253–259. Fixed-k order of choices and nonuniform-threshold warning.
- `repository/docs/expert_companion.md`: §7, line 283; uniform estimate (16) and explicit quantum bound. The remark itself supplies additional estimates; no mathematical contradiction is alleged.
- `repository/docs/reasoning_record.md`: §7.2, #ROOT-NO-SMALLER. Explicitly identifies a quantitative growing-k schedule as a separate result, unnecessary for the infimum proof.

## SX-040 · medium · evidence_presentation

**Reader:** lecturer. **Text:** `repository/docs/expert_companion.md`, line 338; Appendix A, Table 2, full amplifier row. Supplied PDF p. 12.

> Stronger conclusion (the returned state)

Stronger than which printed assertion? Lemma 2 in this same companion already states that conditional success returns the normalized successful state up to global phase. “The returned state” therefore does not explain a stronger conclusion relative to that lemma.

**Reader cost.** The comparison table is supposed to teach precise statement fidelity. A relation label whose stated reason is already present in its comparator undermines that instructional task, even if the actual formal theorem has another extra conclusion.

**Direction.** Re-evaluate the relation against the current printed Lemma 2 and name any actual extra mass, register, or scope guarantee. Keep the narrower basis-predicate setting explicit. Do not infer new build or Comparator status from this local wording issue.

**Relation to round five.** This concerns how a current same/stronger/weaker label is justified in prose, not whether the previously reviewed formal endpoint exists or was accepted.

**Evidence.**

- `repository/docs/expert_companion.md`: §4, Lemma 2, line 143; Appendix A, Table 2, amplifier row. Both local texts already mention the returned normalized successful state.
- `repository/docs/exposition.md`: §7, line 269. The comparison there is to its own §4 exposition and also mentions exact success mass; a relation label cannot be copied without fixing the comparison target.

## SX-041 · medium · evidence_presentation

**Reader:** lecturer. **Text:** `repository/docs/expert_companion.md`, line 351; Appendix A, Reproducing the check. Supplied PDF p. 13.

> the commit the links point to.

Which edition should a lecturer use for the reproduction exercise? The paragraph says the code comment gives the linked commit, but the comment says 659b571 and the generated statement links point to e9dfefbf11e6d1f380f122caa2349d4be78f2c1f.

**Reader cost.** A student can follow the instructions faithfully and compare a different checkout from the one opened by the links. This is a visible edition mismatch, independent of whether either recorded run passed.

**Direction.** Align the reproduction comment with the intended linked edition, or explicitly distinguish the historical run commit from the reading-link commit. Give one unambiguous edition for the proposed exercise; no new formal run is requested by this finding.

**Relation to round five.** The previous round updated link pins. This is the remaining comment-to-link mismatch in the current reproduction paragraph, not a renewed receipt audit.

**Evidence.**

- `repository/docs/expert_companion.md`: Appendix A, lines 351–358 and generated lean-links block. Local comparison of the stated reproduction commit and link targets.
- `SOURCE_STATUS.json`: repository_commit. The packet records its provenance commit, which does not automatically identify a reproduction checkout.
- `manifest.json`: interpretation. Member hashes bind the exact working bytes; the commit is provenance only.

## SX-042 · high · unclear

**Reader:** lecturer. **Text:** `repository/docs/reasoning_record.md`, line 118; Reading guide versus §1.1 Dependencies and proof recovery.

> The central construction can be read after §§3.1–3.5 and the precise ingredient statement in §3.17;

Must an assigned reader complete the independent Forrelation hardness proof before starting the new construction, or may they accept the ingredient and continue?

**Reader cost.** The opening table places hardness §§3.6–3.15 on the required proof path, while this later sentence explicitly allows deferral. A teacher cannot give a single unambiguous reading instruction from the current guide, and a student may enter a long Gaussian proof unnecessarily.

**Direction.** Distinguish the route proving every imported ingredient from the route learning the new separation, and make the opening table and later dependency permission agree. Preserve all full proofs and stable anchors.

**Relation to round five.** R5 added a reading guide and moved several optional discussions. This is a conflict within the repaired navigation, not a repetition of the earlier missing-guide complaint.

**Evidence.**

- Reasoning record Reading guide, table line 19, Required proof path includes hardness §§3.6–3.15.
- Reasoning record §1.1 line 118 explicitly permits §§3.1–3.5 + §3.17 before construction.
- Exposition §3 imports Bansal–Sinha hardness without teaching the Gaussian proof.

## SX-043 · keep · keep

**Reader:** lecturer. **Text:** `repository/docs/reasoning_record.md`, line 133; §1.1, Reading routes; Appendix B role.

> Each proof destination they cite opens with the statement it proves:

Keep the proof-first destinations, return links, and separate reference catalogue. They let the long record support a class reading without making its entire 125-page supplied PDF compulsory.

**Reader cost.** The new guide and destinations are a real improvement. Solving the remaining required-versus-optional ambiguity should not discard stable anchors, full proofs, claim IDs, or evidence boundaries.

**Direction.** Preserve the full record and Appendix B as reference material. Repair the route labels and example handoffs around them; separate the recommended first reading from the archival scope.

**Relation to round five.** Acknowledges the repaired navigation and retains the full record’s purpose; it is compatible with the route-consistency critique.

**Evidence.**

- `repository/docs/reasoning_record.md`: §1.1, #record-reading-routes; §5.2 opening; §6 opening and §6.6 return link; Appendix B introduction. These destinations and role statements are present in the supplied current Markdown.
- `previous_round/dispositions/reasoning_record.json`: Navigation and proof-destination dispositions. These are improvements to preserve, not absent features to request again.

