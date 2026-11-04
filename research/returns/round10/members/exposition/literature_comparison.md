# Passage-specific literature comparison for the R10 exposition review

**Scope and status.** This is retrospective comparison after the primary chronological pass was frozen. It is advice, not a rewrite. The lead source is `repository/docs/exposition.md` in the supplied R10 archive, SHA-256 `e034aae7c7a74529656a84289b41767bcc4f06cbe1a3d2926fc8a01f918918b8`. Line references below identify that exact file. Numbered citations resolve to the primary-source entries at the end of this memo. The companion [literature_sources.json](literature_sources.json), at the root of this review ZIP, records exact source files, editions, and read/skim boundaries. Only the specified passages were read; the annex was not read in full. No uploaded script was run and no manuscript or first-pass file was modified. Comparisons paraphrase the sources; no prose is quoted verbatim.

## Recommendation in one paragraph

The remaining leverage is primarily architectural. The draft already does the difficult local work: it distinguishes probabilities from amplitudes, shows nonuniform fractional weights, retains quantum workspace, separates a joint light-visit event from conditioning on lightness, and supplies counterexamples to weak independence and pooled caps. A review should not reopen those as missing explanations. The stronger improvements are to put each component's purpose and contract before its implementation, delay constants until the mechanism gives them a role, and add one quantitative synthesis task. The sources support those teaching choices; they do not establish an empirical prediction about this draft's readers.

## 1. Put the construction's problem before the exact exponent definition

**Current location and reader task.** Lines 14–26 give useful model conventions, then introduce the infimum defining the optimal universal exponent; lines 28–34 state the fixed-parameter family with logarithmic power six and coefficient 1/400. The concrete column mechanism begins at line 36 and the board arrives later. The reader must currently track the quantifiers, two size parameters, family constants, and the algorithmic goal before seeing the object that makes the bounds plausible.

**Ambainis comparison.** The 2017 survey fixes the query model and total/partial distinction before its applications ([3], §2.1, printed pp. 3–4). Its pointer-function passage specifies the table's fields and acceptance conditions, then lets the reader derive a small certificate and understand candidate elimination ([3], §4, printed pp. 10–11). The corresponding operation here is to trace the winning column's strings, address inputs, certificate, and outgoing pointers before using them to explain the two complexity bounds. That sequence supports bringing the board and acceptance test forward. Ambainis's chained pointer function differs from this construction; its predicate and historical bounds must not be imported.

**Su comparison.** Su's distance problem explicitly preserves the assumption x > 0, uses it to select the answer, and compresses algebra its intended reader can supply ([2], pp. 1–2). The relevant distinction here is between assumptions that constrain the reader's next inference and accounting that can wait. Keep totality, the worst-case query cap, and the fixed-k interpretation visible when the bounds are introduced; defer the coefficient 1/400 and logarithmic power six until their counting argument has a role. The goal is to make a reader identify which quantities are hypotheses and which are conclusions, not simply to shorten the opening. The source preprint's expert-facing introductory theorem ([8], §1, pp. 1–3) does not by itself establish the best order for the exposition's stated prerequisites.

**Proposed change.** Keep the early definitions of a query, worst-case budget, and totality. Give the qualitative endpoint and the two mechanisms, then present the board and accepting certificate. Relocate the exact infimum/constant discussion and the explicit family accounting into a clearly identified precision layer, either after the board or at the entrance to Section 6. The exact theorem can remain readily findable. This is a change in order and emphasis, not a request to remove the theorem or its quantifiers.

**What must survive.** The distinction between the number of columns and total input length; the fact that these are an upper bound for Q and a lower bound for R; and the order “choose a target exponent, fix k, then grow m.” The existing endpoint exercise in Question 5 is particularly valuable.

**Review criterion.** Before the formal alpha calculation, a reader should be able to say what a winning column certifies, what makes its address expensive classically, and why a quantum algorithm first collects candidates and then verifies them. A shorter opening is successful only if it improves that explanation, not merely its word count.

## 2. Remove the stopped-simulator result from its premature preview

**Current location.** Line 129 introduces r = 20 log₂m, the joint event involving a correct proposed address and a query cap, the exponentially small bound, a stopped simulator, and a union over query times. At this point the draft has not yet defined the dummy run, whole-run lightness, or the fixed-time simulator.

**Knuth comparison and proposed change.** Knuth, Larrabee, and Roberts ask writers to connect the next mathematical step to what the reader already knows ([1], §1, items 5 and 10–14, printed pp. 2–3). Their algorithm discussion makes the purpose of a step inspectable through the invariant attached to it, while cautioning against merely imitating a named style ([1], §10, printed pp. 20–21). Line 129 currently names a cap and a stopped simulator before a reader can identify the run or invariant involved. Leave the address-array size and the qualitative reason for logarithmically many hard answers here; move the adaptive-guess/cap explanation to the classical argument where the reader can test the stop-before-read rule on the displayed run. The attribution to cheat sheets can remain at the construction.

**Limit.** The statement at line 129 is not a newly discovered mathematical error. Later sections do supply the required joint-event argument. The issue is that the preview asks a novice to carry technical vocabulary without an available operation to perform with it.

**Review criterion.** A reader at the construction should need only understand how an address selects a cell. The first detailed occurrence of “light” and a stopped simulator should let that reader trace a particular run immediately.

## 3. Expose the comparison contract before the coherent implementation

**Current location and dependency.** Lines 217–223 explain retained registers and a reversible implementation. Lines 225–256 then establish comparison with a genuine winner, distinguish nonwinners and cycles, and define the ideal weights and halving argument. Lines 259–267 finally implement the weight distribution through fresh comparison workspaces. The current implementation discussion precedes the stochastic interface that the later algorithm actually uses.

**Childs and BHMT comparisons.** Childs makes a classical gate reversible by preserving its input and intermediate values, then explains copying an output and reversing the computation ([4], §1.4, printed pp. 2–3). Its reader can check which information an inverse needs. The corresponding operation at lines 217–223 is to identify the comparison trials, answers, flags, and other registers that the whole inverse must undo. The draft already supplies that information; placing it beside the preparation would let the reader use it immediately. BHMT then supplies the next interface: a measurement-free preparation A, its inverse, and the good/bad components ([5], §2, operator (1), Lemma 1, and equation (8), printed pp. 5–7). These sources support retained workspace here. Neither licenses an inverse acting only on the label, and Childs's separate clean-output construction is not a requirement to erase the workspace before amplification.

**Proposed change.** Present the classical comparison probabilities, winner guarantee, and ideal weighted-pivot process together. Move the detailed retained-register explanation next to the preparation that realizes those weights, with a short forward reference if needed. The result is a visible dependency: comparison law → ideal progress argument → preparation with the same law → amplification and verification.

**Beyond-annex teaching comparison.** IBM Quantum Learning's Grover lesson separates the search task, algorithm operations, and analysis ([11a–c]). The analysis defines normalized solution/non-solution states, computes the operator's action, then gives the geometry ([11c], the three named sections in the source entry). That sequence supports separating the algorithmic contract from its realization. Its uniform marked-state example cannot replace this draft's nonuniform good state with workspace.

**What must survive.** The states containing all trials, labels, query answers, and auxiliary data; the role of orthogonality; and the distinction between success probability and the conditional distribution of the label. The fractional example at lines 271–279 already provides a more appropriate local test than a generic uniform-search illustration.

## 4. Make capped amplification a usable component before giving its schedule constants

**Current location.** Lines 281–299 derive the two-dimensional rotation and preservation of the good state. Line 301 gives the exact randomized schedule, including M, N, the mixture, and the success estimate. Lines 303–313 explain why randomized iteration counts and retries preserve the conditional pivot law and how the stage guarantee fits the overall algorithm.

**BHMT and de Wolf comparisons.** The supplied de Wolf notes separate the rotation calculation from the unknown-probability and runtime-control variants ([7], §7.2, the geometric/algebraic arguments and following variants; §7.3). BHMT first makes its amplified state calculable through the operator and invariant-subspace equation, then gives a distinct stopping algorithm ([5], §2, operator (1), Lemma 1, equation (8), and Theorem 3/QSearch). For lines 281–313, these are two reader operations: derive what one iteration does to the normalized good state, and check which stopping rule achieves the required error and cost. BHMT's QSearch has expected cost when success probability is positive and runs forever at zero ([5], printed pp. 8–10). It cannot replace the draft's every-input fixed cap. The invariant-subspace calculation supports the conditional-law argument; the stopping guarantee requires its own contract.

**Proposed change.** State the component contract explicitly at its entrance: a hard query cap on all inputs, a specified failure bound under q ≥ γ, behavior at q = 0, and the required conditional label law when successful. Keep the rotation explanation accessible. Put the precise schedule constants and trigonometric estimate in a compact technical aside or linked derivation, then return directly to the stage argument. This reduces simultaneous bookkeeping without weakening the worst-case model.

**Do not recommend redundant repairs.** The q = 1/2 counterexample and Question 2 already prevent the false intuition that every iteration improves success. The draft already explains why mixing over iteration counts and first-success attempts preserves the same normalized good state. A recommendation to “add a Grover example” would miss this existing work.

**Review criterion.** A reader should be able to use the sampler to justify a stage without re-deriving M and N, and then inspect those constants if auditing the cap. Conversely, the reader must not silently use the guarantee below its threshold or switch to expected query cost.

## 5. Organize the classical argument around three charges, then add a transfer task

**Current location.** The necessary reasoning is present across lines 369–455: the erased zero, the heavy target, and the light true-cell visit. The final gap formula appears at line 455. The optional conditional-value proof at lines 441–450 also supplies the posterior product structure and one-query inequality needed by the reduction.

**Drucker comparison.** Drucker defines W as the best success probability remaining after a partial transcript with its remaining budget, proves a one-query conditional-expectation bound, and establishes the product law after adaptive queries before bounding the product ([6], §3, definition of W, Lemmas 3.1–3.2 and subsequent argument, printed pp. 10–13). Its reader can identify what is conditioned on and which factor the next query changes. Lines 441–450 already make those operations available in the optional proof; retain them. The teaching task in the surrounding reduction is different: a reader must identify the capped predictor's event and match each bad event to its budget. A charge map would connect that task to the local proof without pretending that unconditional independence survives arbitrary conditioning. Drucker's headline global-budget theorem and the separately capped setting remain distinct ([6], end of §3).

**Proposed change.** Introduce a compact charge map near the beginning of the coupling proof and return to it at the end. The author's two changed locations lead to three bounds:

| Contribution | What is charged | Bound used by the draft | Reader must keep fixed |
|---|---|---:|---|
| Erased zero | Discoveries of hidden zeros in the complete dummy run, averaged over the independent planted column | 4G/m² | Planting column independent of that run |
| Heavy target column | More than L queries to a target tuple | G/(mL) | Whole-run total query cap G and uniform target column |
| Light true-cell visit | A complete address named by a chosen query coordinate | G(2/3)^r | One time and column for the capped predictor; then the allowed union and averaging |

This map is the reviewer's proposed navigation aid. It is not a claim that Drucker presents this construction or these charges. The direct-product event remains a joint event; dividing by the probability of lightness would change the statement.

**Quantitative transfer task.** The existing questions test the local mechanisms well. A new synthesis task could ask the reader to vary the number of address bits. Suppose the same proof gives G ≤ mL/100, L ≤ m, and r = ⌈c log₂m⌉. Show from the coarse bound G ≤ m²/100 that

G(2/3)^r ≤ (1/100) m^{2 − c log₂(3/2)}.

Then ask which strict condition on c makes this term tend to zero and why this does not alone re-prove every upper-bound or encoding estimate for a modified family. The sufficient condition from this calculation is c > 2/log₂(3/2), approximately 3.419. This is a transfer check on the role of amplification in the classical lower bound, not a proposal to optimize or change the construction's constant 20. If r must obey an additional integrality convention, use an allowed upward rounding and state it.

**Review criterion.** The reader can identify which of the three terms controls each bad event and explain why the product mL produces the classical exponent. Naming “a direct-product theorem” without the budget map is not enough.

## 6. Preserve local exercises; use the final task to test transfer, and make answer exposure deliberate

**Current state.** Question 2 already combines overshoot, fractional weights, and final verification. Questions 3–4 expose independence and whole-run lightness. Question 5 distinguishes a fixed-k threshold from excluding its endpoint. The combined explanation at line 486 asks for both mechanisms and their role in the exponent. These are substantive exercises, not merely invitations to reread a theorem.

**Comparison.** de Wolf's chapter-7 Exercise 1 asks for intermediate states and compares one and two Grover iterations; Exercise 3 tests the quarter-marked case ([7]). Question 2 already provides those kinds of operations. Hamoudi's PCMI 2023 Problem Session 1 moves from phase queries to two-bit parity and its extension, and from sensitivity to general complexity relations ([10], Problem 2, p. 1, and Problem 3, pp. 1–2). It supports testing reuse in a changed setting, not a theorem about this family.

**Proposed change.** Prefer one quantitative transfer task of the kind above to another introductory Grover exercise or another generic request to explain the whole theorem. Keep answers separate enough that the student can make an unaided attempt. The combined rubric currently appears at line 500, before numbered Answers 1–5. A reader using an early answer may therefore encounter the final synthesis guidance. Moving that rubric after the numbered answers, or providing a clearly separate guided version, would make the intended assessment sequence easier to maintain. The text already labels rubric use as guided practice; this is an order/exposure issue, not a claim of deceptive testing.

**Limit.** Source comparisons establish plausible exercise design choices, not measured learning gains. No additional human readers were recruited or observed for this comparison.

## 7. Use source models selectively; do not import their historical claims or simplifying assumptions

Hamoudi's linked notes are updated **24 April 2026**, despite their PCMI 2023 course link ([9], title page). Section 1.1, pp. 2–5, distinguishes task and resource conventions and qualifies its memoryless notation. Use those model boundaries when assessing the introduction at lines 14–22; do not import the simplifying notation or the now-historical supercubic-open remark on p. 7.

Likewise, Childs [4] is the supplied 17 April 2025 snapshot at a mutable author URL; Drucker [6] is the 2014 arXiv v2, not the 2012 journal edition; and the supplied de Wolf material [7] identifies arXiv v6 of 27 August 2026. A versioned preprint, supplied extraction, live webpage, and journal edition are separate evidence objects. Keep them distinct when separating theorem evidence from a teaching analogy.

## Source-use boundaries

- **Theorem evidence:** the supplied source preprint [8] for the new result; BHMT [5] for the invariant good/bad subspace calculation; Drucker v2 [6] for the conditional-value proof technique and its relation to separate caps. This comparison is not an independent certification of all hypotheses or of the whole new theorem.
- **Pedagogical comparison:** Childs's operational reversible computation [4], Ambainis's task/structure/algorithm sequence [3], de Wolf's variants and exercises [7], the Knuth report [1], Su's worked explanation [2], Hamoudi's models and problem progression [9–10], and the IBM lesson's dependency order [11].
- **Not fresh verification:** no fresh Lean or Comparator execution, no live retrieval of the supplied pinned preprint, no claim that all annex sources were read, and no claim that external examples implement the exposition's exact pointer function.
- **Original mathematical pages checked:** BHMT [5] original PDF pp. 5 and 7 and Drucker [6] original PDF pp. 11–12 were visually inspected to disambiguate extracted equations. Other read scopes are recorded as text/source reads. Rendering a page without inspecting it does not count as reading it.
- **Required reading coverage:** all six selections specified in the literature standard have passage-specific applications here: Knuth in comparison 2, Su and Ambainis in comparison 1, Childs in comparison 3, BHMT in comparisons 3–4, and Drucker in comparison 5. This is selected-passage coverage, not a claim to have read those works in full. No required selection was unavailable. The de Wolf edition date relies on supplied version metadata; the preprint was read locally, not successfully retrieved live.

## Suggested integration order

Prioritize comparisons 1–5 as one coherent architecture proposal. Use comparison 6 for a small, testable exercise/answer-order recommendation. Keep comparison 7 and the source ledger as evidence discipline. Do not inflate each preservation constraint into a separate defect. In particular, retain the fractional-law example, the q = 1/2 caveat, the joint-event simulator reduction, and the endpoint-k exercise while reducing the amount of machinery the reader must hold before its purpose becomes visible.


## Primary sources and exact passages used

Entries [1]–[8] identify supplied editions. Entries [9]–[11] identify primary teaching sources read online on 4 November 2026. Page numbers are printed page numbers unless otherwise stated; section and exercise locators are used where no PDF pagination was verified. The ledger IDs connect these entries to the source inventory and its narrower read/skim declarations.

1. **Donald E. Knuth, Tracy Larrabee, and Paul M. Roberts. _Mathematical Writing_.** Stanford report CS-TR-87-1193, based on the autumn 1987 course. [Primary PDF](https://www-cs-faculty.stanford.edu/~knuth/papers/cs1193.pdf). **Used:** §1, items 5 and 10–14, pp. 2–3; §10, pp. 20–21. Ledger: `LC-KLR`.

2. **Francis Edward Su. _Guidelines for Good Mathematical Writing_.** Updated 18 August 2020. [Primary handout](https://math.hmc.edu/su/wp-content/uploads/sites/10/2020/08/Guidelines-for-Good-Mathematical-Writing.pdf). **Used:** audience discussion and worked distance problem, pp. 1–2. Page 3's structure/examples discussion was also read. Ledger: `LC-SU`.

3. **Andris Ambainis. _Understanding Quantum Algorithms via Query Complexity_.** arXiv:1712.06349v1, 18 December 2017. [Versioned PDF](https://arxiv.org/pdf/1712.06349v1). **Used:** §2.1, pp. 3–4; §4, from Theorem 4 through the pointer-function definition, certificate properties, and candidate-elimination discussion, pp. 10–11. Ledger: `LC-AMBAINIS`.

4. **Andrew M. Childs. _Lecture Notes on Quantum Algorithms_.** Supplied title-page date: 17 April 2025. [Author's PDF URL](https://www.cs.umd.edu/~amchilds/qa/qa.pdf), which is mutable. **Used:** §1.4, pp. 2–3; the supplied snapshot, not an assumed current edition. Ledger: `LC-CHILDS`.

5. **Gilles Brassard, Peter Høyer, Michele Mosca, and Alain Tapp. _Quantum Amplitude Amplification and Estimation_.** arXiv:quant-ph/0005055v1, 15 May 2000; manuscript title-page date 2 May 2000. [Versioned PDF](https://arxiv.org/pdf/quant-ph/0005055v1). **Used:** §2, operator (1) and Lemma 1, p. 5; equation (8), p. 7; Theorem 3 and QSearch, pp. 8–10. The surrounding derivation on pp. 4–10 was read. Ledger: `LC-BHMT`.

6. **Andrew Drucker. _Improved Direct Product Theorems for Randomized Query Complexity_.** arXiv:1005.0644v2, 9 May 2014. [Versioned PDF](https://arxiv.org/pdf/1005.0644v2). **Used:** §3, pp. 10–13: definition of W, Lemmas 3.1–3.2, subsequent product argument, and the final separate-cap/fair-computation comment. This locator is for v2, not the 2012 journal edition. Ledger: `LC-DRUCKER`.

7. **Ronald de Wolf. _Quantum Computing: Lecture Notes_.** Supplied version metadata identifies arXiv:1907.09415v6, 27 August 2026. [Version-specific record](https://arxiv.org/abs/1907.09415v6). **Used:** §7.2, geometric/algebraic arguments and variants; §7.3, amplitude amplification; chapter-7 Exercises 1 and 3. Read from the supplied extraction; no PDF page locator or independently fetched edition is asserted. Ledger: `LC-DEWOLF`.

8. **OpenAI. _A Nearly Quartic Separation Between Randomized and Quantum Query Complexity_.** Supplied preprint, 5 October 2026. [Pinned primary URL](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf). **Used:** introduction, §1 and §§1.1–1.3, pp. 1–3. Read in the attachment; live retrieval did not succeed. Ledger: `LC-PREPRINT`.

9. **Yassine Hamoudi. _Query Complexity_.** PDF updated 24 April 2026. [Author's PDF](https://yassine-hamoudi.github.io/files/publications/QueryComplexity.pdf). **Used:** title page; §1.1, pp. 2–5; historical-status boundary on p. 7. Ledger: `LC-HAMOUDI`.

10. **Yassine Hamoudi and Angelos Pelecanos. _PCMI 2023, Problem Session 1: Basics of Query Complexity & The Hybrid Method_.** Instructor and teaching-assistant credits, respectively. [Primary problem set](https://yassine-hamoudi.github.io/files/pcmi2023/Problems1.pdf). **Used:** Problem 2, p. 1; Problem 3, pp. 1–2. Both pages were read. Ledger: `LC-HAMOUDI-P1`.

11. **IBM Quantum Learning. _Fundamentals of Quantum Algorithms_, Grover lesson.** Live HTML, retrieved 4 November 2026; no immutable edition date established. **Used:** (a) [Unstructured search](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/grover-algorithm/unstructured-search), task definitions; (b) [Grover algorithm description](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/grover-algorithm/grover-algorithm-description), operational steps; (c) [Analysis](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/grover-algorithm/analysis), sections on solution/non-solution states, action of the Grover operation, and geometric picture. HTML has no printed pagination. Ledger: `LC-IBM-SEARCH`, `LC-IBM-ALGORITHM`, `LC-IBM-ANALYSIS`.
