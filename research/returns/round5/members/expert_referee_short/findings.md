# Located referee findings

Readable rendering of `findings.json`; the JSON is the canonical intake format. This is critique only. Source paths below refer to the original input packet unless they begin with `checks/`, which refers to this return.

## ER-001 — high / credit

**Paper:** expert_companion  
**Location:** 1.1 Where this sits; PDF p. 2

**Exact current-source locator:**

> which Bansal and Sinha and Sherstov, Storozhenko and Wu proved

The antecedent of "which" is the conjecture that the explicit k-fold Forrelation problem achieves the optimal partial separation. Bansal–Sinha proved that statement for the Walsh matrix and the specified one-sided promise. Sherstov–Storozhenko–Wu proved the same optimal separation through k-fold Rorrelation with a random orthogonal matrix. Their total-function consequence is correctly shared credit; this sentence incorrectly assigns the explicit-Walsh conjecture to both papers.

**Why it matters:** The authors of both optimal-separation papers deliberately distinguish their constructions. Conflating them obscures why the present function can use an explicit exact Walsh circuit.

**Revision direction:** Separate credit for the optimal partial-separation exponent from credit for hardness of the explicit Walsh promise used here. Keep the independent total-function result in the history table.

**Evidence:**

- [literature/quartic-ref-23-an-optimal-separation-of-randomized-and-qu/source.pdf](https://arxiv.org/abs/2008.10223v4), §1.2, Theorem 1.1, PDF p. 3; §1.8, PDF p. 10: Theorem 1.1 quantifies over a uniformly random orthogonal U. Section 1.8 explicitly distinguishes Bansal–Sinha’s explicit Forrelation/Rorrelation construction from the random choice used in SSW.
- [literature/quartic-ref-06-k-forrelation-optimally-separates-quantum/source.pdf](https://arxiv.org/abs/2008.07003v3), §1.1, Theorem 1.3 and Corollary 1.4, PDF p. 4: The theorem uses the explicit normalized Hadamard matrix and delta=2^(-5k).

## ER-002 — high / error

**Paper:** expert_companion  
**Location:** 3. Where a natural shortcut fails; Table 1, row 2; PDF p. 5

**Exact current-source locator:**

> Treat comparisons as bounded-error queries to a fixed tournament

The deterministic three-cycle offered as the first counterexample does not refute the shortcut. It is already an exact fixed tournament, and its comparison queries have zero error. Nontransitivity and failure of bounded-error access to a fixed Boolean predicate are different issues. The alternative example of a pair at probability 1/2 does illustrate the missing bias guarantee.

**Why it matters:** Tournament and bounded-error quantum-search researchers will notice that a tournament need not be transitive. A false counterexample undermines a table presented as a reliable guide to the delicate steps.

**Revision direction:** Remove the deterministic cycle as a counterexample to this particular shortcut, or distinguish its role in rejecting total-order assumptions from the no-margin obstruction. Keep the existing probability-1/2 example.

**Evidence:**

- `paper/extracted.md`, §3, introductory paragraph; §3.2, (10)–(13): The preprint distinguishes arbitrary nonwinner probabilities from ordinary bounded-error access to a fixed tournament; complementarity does not impose transitivity.
- `repository/docs/reasoning_record.md`, §5.2, upper-comparison-model and upper-ideal-process: Certain cycles are explicitly permitted by the comparison model.
- [Mande–Paraashar–Saurabh (2023), official publisher abstract](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2023.30), Abstract and definition of a tournament: The problem is posed on arbitrary orientations of complete graphs; transitivity is not a premise.

## ER-003 — high / lean_link

**Paper:** expert_companion  
**Location:** Appendix A. Checking the statement — What Comparator establishes; PDF p. 12

**Exact current-source locator:**

> and [its parts][cmp-lemma22]

The link for the parts of Lemma 2.2 points to the wrong bundle. Construction/Challenge.lean has four targets: winner uniqueness, transcript uniqueness, absence of an incoming zero, and existence of an outgoing zero. These are useful construction facts, but none states the local-test count, shallow evaluation, or coherent evaluation asserted in Lemma 2.2. The separate ConstructionFull link does state those properties. The current wording therefore assigns the wrong mathematical meaning to a real comparison target.

**Why it matters:** A reader of the pointer-function or quantum-query papers who follows the link to check coherent certificate verification will instead see four ancillary facts and cannot reconcile the assurance with the claimed lemma.

**Revision direction:** Use the actual existing target for the local-test lemma, and label the four ancillary targets by the properties they really establish. This is a link/description correction, not a request for new formalisation.

**Evidence:**

- `repository/lean/QuarticCorpus/Construction/Challenge.lean`, L326–L341: The four theorem statements are winsAt_unique, existsUnique_gateConsistent, winner_no_incoming_zero and winner_finds_zero.
- `repository/corpus/comparator_map.json`, challenges[path=lean/QuarticCorpus/Construction/Challenge.lean].configurations[0].theorem_names: Confirms that those four declarations are the configured targets.
- `paper/extracted.md`, §2.2, Lemma 2.2, printed p. 6: Lemma concerns K local tests, exact O(log m) queries and coherent evaluation with superposed test indices.
- `repository/lean/QuarticCorpus/Independent/ConstructionFull/Challenge.lean`, L14–L60: Existing target contains the relevant test count, depth and coherent-evaluation statements.

## ER-004 — high / missing

**Paper:** expert_companion  
**Location:** 6. The Forrelation lower bound; PDF p. 10

**Exact current-source locator:**

> while the derivative bound caps it

The summary moves from a solver amplified to error ε to the depth threshold in (16) without identifying the amplified tree depth. In the record, the original cap D becomes padded depth d=50kD+1. That O(k) amplification cost supplies part of the k² denominator and is essential to the advertised uniform constant. The displayed derivative estimate is a bound for depth d, not directly for the original solver cap.

**Why it matters:** Bansal–Sinha and Girish–Tal–Wu readers checking the quantitative transfer cannot reconstruct the numerical claim from the stated chain, despite the surrounding emphasis on explicit constants.

**Revision direction:** If the quantitative sketch remains, identify the original and amplified depths and point to the existing assembly at record §3.15. Otherwise move the quantitative derivation to that record and keep only the precise input/output statement here.

**Evidence:**

- `repository/docs/reasoning_record.md`, §3.15, (F43)–(F49), especially preceding (F46): Uses τ=25k, ε=(8/9)^(25k), and d=50kD+1 before bounding the derivative expression.
- `repository/docs/expert_companion.md`, §6, derivative display and acceptance-gap paragraph: Uses d in one display but never relates d to the cap of the solver being contradicted.

## ER-005 — medium / error

**Paper:** expert_companion  
**Location:** 3. Where a natural shortcut fails; Table 1, row 4; PDF p. 5

**Exact current-source locator:**

> choose $I$ uniformly among columns where a zero was found

The experiment does not define I when none of the four queries finds a zero, an event of probability (3/4)^4=81/256. Consequently the uniform-marginal assertion and unconditional 175/256 probability are not justified by the rule as printed. The supporting record includes the omitted rule: choose uniformly among all four columns in this case.

**Why it matters:** Probability and query-complexity readers cannot reproduce the claimed joint law from the table without completing the experiment themselves.

**Revision direction:** Include the existing no-discovery branch or attach an exact link to the complete experiment while making clear that a fallback is part of the rule.

**Evidence:**

- `repository/docs/reasoning_record.md`, §6.4, CL-selection-independence-example: Explicitly includes uniform selection among all four columns when no zero is discovered, then computes 1−(3/4)^4=175/256.
- `checks/example_checks.json`, uniform-marginal planting calculation: Exact enumeration gives 81/256 for the undefined branch and 175/256 after restoring the record’s uniform fallback.

## ER-006 — medium / error

**Paper:** expert_companion  
**Location:** 7. The exponent; Remark (one explicit sequence); PDF p. 10

**Exact current-source locator:**

> For $2\le k\le t$ and $t\ge32$

The ensuing inference of the randomized lower bound from (16) omits the hypothesis 15k+2≤2t. The numerical assertion 2≤X≤m can hold under the displayed assumptions, but hardness L<R(P) follows from (16) only in its stated dimension range. For instance k=t satisfies the written range and violates that hypothesis. The subsequently chosen square-root schedule does satisfy it, so this does not refute the final sequence.

**Why it matters:** Forrelation experts checking uniformity in k will distinguish bounds on the number X from the conditions under which X is a proved lower bound.

**Revision direction:** Carry the dimension hypothesis through the general intermediate inference, or apply the inference only after the displayed schedule has supplied that hypothesis. Do not present this as a failure of the final asymptotic result.

**Evidence:**

- `repository/docs/expert_companion.md`, §6, immediately before (16): The companion itself states the necessary dimension condition.
- `repository/docs/reasoning_record.md`, §3.15, Proposition (F43) and proof (F44): The condition controls the exceptional uniform mass and is used in the proof.

## ER-007 — medium / unclear

**Paper:** expert_companion  
**Location:** 4.2 A tournament with probabilistic comparisons; PDF p. 6

**Exact current-source locator:**

> cycles among losers only make the weights fall faster

The sentence asserts a monotonic benefit from cycles that the displayed identity does not establish. At a fixed weight vector, the conditional expected new weight is (W²−Σw_i²)/(2W), independently of the orientations or comparison probabilities satisfying complementarity. The argument establishes robustness to cycles; it does not specify or prove a comparison in which a cyclic process contracts faster than an acyclic one. This is an unsupported explanatory claim, not a defect in the drift identity or the theorem.

**Why it matters:** Readers of quantum minimum and king finding will parse this as a comparison between cyclic and transitive instances rather than a statement of robustness.

**Revision direction:** State the demonstrated robustness to cycles without a comparative speed claim.

**Evidence:**

- `repository/docs/expert_companion.md`, §4.2, equation (8): Its right-hand side contains no edge orientations.
- `paper/extracted.md`, §3.2, equation (13) and concluding paragraph: The source claims no order/transitivity is used and complementarity yields the drift.

## ER-008 — medium / credit

**Paper:** expert_companion  
**Location:** 6. The Forrelation lower bound; PDF p. 9

**Exact current-source locator:**

> Sherstov, Storozhenko and Wu prove a sharper bound

"A sharper bound" has no specified object or parameter regime, and its placement reads as a direct stronger lower bound for the same P_{k,m}. The record is more careful: its §3.16 uses SSW’s Fourier-growth corollary as an external ingredient and then derives a separate Walsh comparison bound through random restrictions and the record’s own Gaussian argument. That deduction is not SSW’s Rorrelation lower-bound theorem. SSW themselves describe the two original lower bounds as incomparable, because their k and logarithmic dependencies trade off.

**Why it matters:** Forrelation and Fourier-growth readers need to distinguish a theorem being cited from a new consequence derived using it; otherwise they cannot check the claimed improvement or its dependence on k.

**Revision direction:** Name the sharper Fourier-growth theorem and identify the record’s transfer as a deduction if it is worth retaining; link to #forr_ssw_comparison. Otherwise remove this unspecific comparison from the short paper. Do not turn it into a claim that the main construction is invalid.

**Evidence:**

- `repository/docs/reasoning_record.md`, §3.16, “The sharper external Fourier comparison”, anchor forr_ssw_comparison, (F56)–(F60): The record explicitly identifies the external Fourier theorem, proves its transfer, and says neither Tal’s nor SSW’s Rorrelation distribution theorem is being transferred.
- [literature/quartic-ref-23-an-optimal-separation-of-randomized-and-qu/source.pdf](https://arxiv.org/abs/2008.10223v4), §1.8, PDF p. 10; Corollaries 4.14–4.15, printed pp. 35–36: Section 1.8 compares k^-29/log^(1-1/k) with k^-1/log^(2-1/k) and states the results are incomparable; the Fourier result is the separately relevant input.

## ER-009 — medium / credit

**Paper:** expert_companion  
**Location:** 1.1 Where this sits; PDF p. 2

**Exact current-source locator:**

> comparison-based separations of certificate complexity by Ben-David and Kothari

The closest algorithmic predecessors are named but not compared at the mechanism level. Ben-David–Kothari, Lemma 5, explicitly builds a fixed tournament from locally checked candidate claims, uses sink/king finding, and then verifies the candidate; AIK’s FindSource maintains candidates that beat all previously selected pivots in a fixed directed graph. The present fractional-weight sampler’s extra task is to retain that idea when loser comparisons have arbitrary probabilities. The draft makes that distinction against HMW but does not attach it to these more immediate sources.

**Why it matters:** The certificate-complexity authors and tournament-search readers will want the exact inherited algorithmic pattern and the precise extension, not only a list of related titles. This also explains why a near-quartic C-versus-Q result did not already settle R-versus-Q.

**Revision direction:** Add exact Lemma 5 / §6 Algorithm 4 locators and one compact mechanism comparison, identifying C as the measure separated in those papers and the absence of a fixed edge predicate here. Do not add a general survey.

**Evidence:**

- [literature/quartic-ref-09-randomized-query-complexity-can-beat-certi/extracted.md](https://arxiv.org/abs/2609.15063v1), §3, “Quantum algorithm”, Lemma 5, especially the second and third stages: A fixed orientation can be queried exactly at logarithmic bit cost, followed by certificate verification.
- [literature/quartic-ref-05-near-optimal-separations-of-certificate-co/source.pdf](https://arxiv.org/abs/2609.11664v2), §6.1, Algorithm 4 and equations (3)–(4), printed p. 12; Lemma 6.1, printed p. 13: FindSource tracks vertices beating the stored list; comparisons approximate fixed graph edges, unlike arbitrary off-promise probabilities.
- `paper/extracted.md`, §3 introduction, printed p. 7: The preprint identifies the extra feature beyond fixed-tournament comparison algorithms.

## ER-010 — medium / credit

**Paper:** expert_companion  
**Location:** 1.1 Where this sits; PDF p. 2

**Exact current-source locator:**

> the direct outward pointers used here are discussed by Ambainis et al.

The source discusses the exact direct-pointer alternative but immediately explains why it is unsuitable in its large-alphabet construction: putting all m−1 outgoing pointers in one symbol makes the alphabet exponential. Leaving out that caveat makes the historical comparison sound effortless and misses the question its authors would ask about the bit-query implementation here.

**Why it matters:** Pointer-function readers need to know why their previously discussed alternative is usable in this construction. The answer is already in §2: separately stored bit fields and access to one chosen pointer cost ell+1 queries, rather than revealing one exponential-alphabet symbol.

**Revision direction:** Give the exact §1.3 “Use of a balanced tree” locator and briefly connect the old encoding caveat to the present bit-field access and local-test count. Keep this as explanation of the existing construction, not an additional result.

**Evidence:**

- [literature/quartic-ref-04-separations-in-query-complexity-based-on-p/source.pdf](https://arxiv.org/abs/1506.04719v3), §1.3, “Use of a balanced tree”, PDF/printed p. 6, final paragraph: It explicitly discusses direct pointers to every unmarked column and states the exponential-alphabet obstruction.
- `repository/docs/expert_companion.md`, §2, “The total function” and “Local tests”: Each pointer is an ell-bit field; one pointer test costs ell+1 input-bit queries.
- `paper/extracted.md`, §3.3, final paragraph, printed p. 10: The preprint explicitly explains ordinary bit queries for superposed accesses and pointers.

## ER-011 — medium / unclear

**Paper:** expert_companion  
**Location:** 1.2 The idea; PDF p. 3

**Exact current-source locator:**

> it must invest about $L$ queries

The overview presents address investment in a constant fraction of columns as compulsory for a classical distinguisher. There is another permitted route: searching X-strings for the erased zero. The actual proof excludes that route separately, at scale m², and uses L≤m to leave mL as the relevant obstruction. A distinguisher that reads all X bits need not invest anything in addresses.

**Why it matters:** Cheat-sheet and pointer-function readers will immediately ask whether the all-one column can be found from X alone. Omitting that competing route makes the informal lower-bound argument sound stronger than the one proved.

**Revision direction:** Mention both detectable changes in the overview and explain that the erased-zero route costs enough in the regime L≤m; reserve the detailed estimates for §5.

**Evidence:**

- `paper/extracted.md`, §4.2, (18)–(23): Separates erased-zero detection and filled-cell detection.
- `repository/docs/expert_companion.md`, §§5.2–5.5, (10)–(14): The companion itself proves both terms.

## ER-012 — medium / structure

**Paper:** expert_companion  
**Location:** 1. The result; Theorem 1; PDF p. 1

**Exact current-source locator:**

> for every $t\ge13669\,k^2$

The first theorem foregrounds a large nonoptimal threshold and coefficient 1/400 before the reader has seen the construction. Those constants are not the compared headline statement and are not needed for the exponent-four conclusion. This makes the central result look dependent on arithmetic refinements that later sections say are deliberately loose.

**Why it matters:** Total-function separation researchers seek the exponent and the mechanism first; formal-methods readers must then undo the initial identification with OpenAI Theorem 1.1 and distinguish the stronger built-only form.

**Revision direction:** Give the source theorem and its quantifiers priority; place the existing explicit specialization beside its derivation or in the statement appendix, preserving the honest evidence distinction.

**Evidence:**

- `paper/extracted.md`, Theorem 1.1: States c_k,C_k,b_k and sufficiently large m.
- `repository/docs/expert_companion.md`, §1, paragraph following (2); Appendix A: Explicitly distinguishes the numerical refinements from the compared theorem.

## ER-013 — medium / misplaced

**Paper:** expert_companion  
**Location:** 6. The Forrelation lower bound; PDF p. 9

**Exact current-source locator:**

> by a different and shorter route

This section shifts from the new total-function mechanism to a second technical narrative involving an unspecified Gaussian chain, reflections, integration by parts, biased derivatives, a stopped martingale and explicit constants. It is neither enough to audit that proof nor necessary to understand the total-function separation, since the section begins by saying that only the standard fixed-k consequence is needed.

**Why it matters:** The cited Forrelation authors know the external theorem; other experts are forced to parse a compressed analytic proof whose actual definitions remain elsewhere. The separation narrative stalls between the classical bound and the exponent conclusion.

**Revision direction:** Move the analytic route and constants to the already existing record; retain here the exact prerequisite, the formal proof-route distinction and a direct locator. Preserve the indication that the planted law is not promise-supported.

**Evidence:**

- `paper/extracted.md`, §2.1, Lemma 2.1(i): The preprint imports only the fixed-k consequence.
- `repository/docs/reasoning_record.md`, §§3.6–3.15: Contains the definitions and full analytic argument that the compact sketch presupposes.
- `repository/docs/reasoning_record.md`, §3.18 Sources for the Forrelation argument: Already separates the Gaussian antecedents, modified interpolation, martingale and comparison route.

## ER-014 — medium / misplaced

**Paper:** expert_companion  
**Location:** 7. The exponent; Remark (one explicit sequence); PDF p. 10

**Exact current-source locator:**

> **Remark** (one explicit sequence)**.**

The remark becomes a separate quantitative derivation with a new schedule, explicit budget 2^53 k2^(10k), a new epsilon function and several numerical thresholds. It is not needed for α_tot=4 and undercuts the preceding clean fixed-parameter argument. The packet specifically asks whether the earlier growing-k material has become a short, explicit remark; it is explicit but remains substantial.

**Why it matters:** Experts finishing the argument must decide whether these additional unformalized details are part of the claimed contribution. They dilute the already complete exponent conclusion.

**Revision direction:** Reduce this location to the existing scope statement and move its derivation to the record; do not add a new theorem or enlarge the formalization task.

**Evidence:**

- `repository/docs/expert_companion.md`, §7, first paragraph: Already proves α_tot=4 with fixed k.
- `paper/extracted.md`, §5: Uses the fixed-k quantifier order only.

## ER-015 — medium / wasted

**Paper:** expert_companion  
**Location:** 5.3 The erased zero; PDF p. 8

**Exact current-source locator:**

> The preprint's early-and-late count gives $4G/m^2$

The mechanism has been established once the exact hit identity and any adequate O(G/m²) bound are clear, but the subsection then compares three coefficients, two alternative formal proof routes and their evidence status. This draws attention away from independence of the planted index, which is the delicate condition the main proof uses.

**Why it matters:** Direct-product and lower-bound readers need to follow how the two detection events are controlled, not track every stronger local coefficient during the proof.

**Revision direction:** Keep one sufficient derivation and the exact identity in the main flow; collect the existing sharper endpoints and declaration-level distinctions in the formal appendix or long record.

**Evidence:**

- `paper/extracted.md`, §4.2, equation (19): The original 4G/m² bound suffices.
- `repository/docs/expert_companion.md`, §5.5, (14): Any displayed version leaves a large constant margin below 1/3.

## ER-016 — medium / lean_link

**Paper:** expert_companion  
**Location:** 4. The quantum upper bound — Lemma 2, proof sketch; PDF p. 5

**Exact current-source locator:**

> the amplified procedure returns the original register in the normalised successful state

The linked highlight for the full-state amplifier stops after the theorem name, hypotheses and the first let-binding (L17–L20), before any conclusion. The retained-state conclusion is at L37–L38, exact success mass at L39–L40 and high-success guarantee at L47–L48. A second occurrence of the same endpoint-selection defect is the ConstructionFull link, which stops at L41 although the coherent-evaluation conclusion continues through L60. Both line ranges exist, so the supplied link checker reports them valid, but neither highlight contains the complete statement it advertises.

**Why it matters:** Quantum-query readers are being asked to inspect a specific retained-state/coherence claim; the highlighted source omits precisely the clause they need to check.

**Revision direction:** Extend each link to the end of the complete declaration type, or give separate links to the exact relevant conjuncts. Validate semantic coverage of a highlight in addition to whether its line numbers exist.

**Evidence:**

- `repository/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean`, L17–L52: Advertised highlight is only L17–L20; substantive retained-state, cap and success conclusions follow.
- `repository/lean/QuarticCorpus/Independent/ConstructionFull/Challenge.lean`, L38–L60: Current cmp-lemma22-full highlight ends at L41, within the witness binders, before the coherent evaluator and physical-program clauses.
- `repository/docs/lean_links.json`, links.cmp-amplifier.lines and links.cmp-lemma22-full.lines: Records [17,20] and [14,41].
- `LINK_MAP.json`, corresponding line_range_valid entries: Both are syntactically valid ranges; that does not check statement coverage.

## ER-017 — medium / lean_link

**Paper:** expert_companion  
**Location:** 7. The exponent — Remark (one explicit sequence); PDF p. 10

**Exact current-source locator:**

> the [quantum budget][src-budget] it uses is built in Lean but has not been compared.

The uniform quantum estimate in the remark depends on the explicit coefficient 2^53 k 2^(10k), but the linked lines state only budget_le with an unspecified budgetConst k and a circuit-size premise. The supplied file already contains the exact claimed endpoint Q_Fkm_le_exponential. The current link obscures the dependence on k at the one place where that dependence is essential.

**Why it matters:** Forrelation readers checking the growing-k deduction need the uniform coefficient, not the fixed-k budget theorem with a hidden constant.

**Revision direction:** Point this occurrence to Q_Fkm_le_exponential (L286–L290), optionally also to budgetConst_le_exponential (L66–L68). Preserve the built-only qualification.

**Evidence:**

- `repository/lean/QuarticQuery/Upper/Bound.lean`, L86–L90: Current src-budget endpoint: budget_le with budgetConst k.
- `repository/lean/QuarticQuery/Upper/Bound.lean`, L66–L68 and L286–L290: Existing exponential-envelope and Q endpoint explicitly contain 2^53 k 2^(10k).

## ER-018 — medium / lean_link

**Paper:** expert_companion  
**Location:** Appendix A. Checking the statement — object table; PDF p. 11

**Exact current-source locator:**

> This appendix lists everything a reader must read to answer that question.

The advertised audit list skips the definition that makes quantum success a probability: AdaptiveProgram.outputMass and its projector are not linked or explained. The QLe row says that the program succeeds with probability at least 2/3, but the source expresses that through outputMass. Checking only the linked program constructors, oracle and cap cannot distinguish correct Born-rule semantics from an incorrectly renormalised branching definition.

**Why it matters:** Query-complexity experts checking the formal statement need to inspect the actual acceptance law, especially because the representation uses adaptive measurement branches and unnormalised states.

**Revision direction:** Add a compact pointer to outputMass and project, with the existing interpretation of squared norms and addition of disjoint branch masses; route further explanation to record §§2.3–2.4.

**Evidence:**

- `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, L96–L99 and L118–L126: project and AdaptiveProgram.outputMass define the measurement and output probability semantics.
- `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, L133–L137: QLe invokes A.outputMass, which the appendix reading table does not link.
- `repository/docs/reasoning_record.md`, §§2.3–2.4, anchors ROOT-ORACLE and R3-01-ADAPTIVE: Already explains unnormalised branches, squared norm and the normalization identity.

## ER-019 — medium / lean_link

**Paper:** expert_companion  
**Location:** Appendix A. Checking the statement — object table; PDF p. 11

**Exact current-source locator:**

> Unitaries fixed before the input, oracle calls, and binary measurements of sets of basis states, with classical branching.

The appendix describes the bespoke adaptive quantum representation but gives no route to the existing argument that it agrees with the usual fixed-query model at the same cap. Similarly, the finite-mixture convention and the minima defining R and Q are glossed without a link to the existing finite-behaviour and read-all arguments. These are modelling questions, which the appendix explicitly makes the reader responsible for, rather than missing Lean proofs.

**Why it matters:** Authors using the standard quantum query model need to know why the formal cost can be substituted into the known universal quartic bound. They should not have to search a long record for the bridge that the development already contains.

**Revision direction:** Give a short cross-reference to record §§2.2–2.5, especially the cap-preserving deferred-measurement statement; keep those proofs in the long record.

**Evidence:**

- `repository/docs/reasoning_record.md`, §2.2, anchor R3-01-CLASSICAL: Finite tree behaviours recover arbitrary capped randomness; a read-all tree proves the admissible budget set is nonempty.
- `repository/docs/reasoning_record.md`, §2.4, anchor R3-01-ADAPTIVE: The classical simulation gives Q ≤ D and a nonempty set of admissible caps.
- `repository/docs/reasoning_record.md`, §2.5, anchor R3-01-BRIDGES: States acceptance-mass-preserving deferred measurement at exactly T controlled phase queries and the converse.

## ER-020 — medium / lean_link

**Paper:** expert_companion  
**Location:** Appendix A. Checking the statement — object table; PDF p. 11

**Exact current-source locator:**

> [Input bits][def-bitloc], [winning][def-wins], [$F_{k,m}$][def-F]

The F link highlights only Fkm, the specialization of addressedF. The Boolean conversion that says the function is true exactly when a winning pair exists is in addressedF at L274–L278 and is not linked in the audit table. Other decisive semantic steps, including GateConsistent and the physical pointer decoder, likewise sit between the highlighted items. The table is useful as an index but is not yet the promised complete reading route.

**Why it matters:** A pointer-function reader tracing the mathematical winner predicate into a total Boolean function has to find an unlisted definition and reconstruct the last semantic step manually.

**Revision direction:** Include addressedF in the F target and provide a small number of dependency links for gate consistency and physical pointer decoding; do not expand into a separate proof exposition.

**Evidence:**

- `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, L274–L285: addressedF is the existential winner predicate converted to Bool; Fkm only specializes it.
- `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, L201–L213 and L249–L272: predecessorValue, GateConsistent, pointer-bit reading and pointerEquiv carry semantics used by WinsAt.
- `repository/docs/lean_links.json`, links.def-F.lines: Current highlight is [280,285], omitting addressedF.

## ER-021 — medium / lean_link

**Paper:** expert_companion  
**Location:** 5.1 A direct product with separate caps; PDF p. 7

**Exact current-source locator:**

> Lean proves Lemma 4 with coins and side information drawn from an arbitrary finite probability space jointly independent of the inputs

The linked target states a weighted bound on compliantSuccess, not an explicitly displayed bound on the success probability of a tree with every-branch cap hypotheses. That is compatible with, and can be stronger than, Lemma 4, but the paper does not explain how the imported compliantSuccess quantity encodes the joint success-and-cap event or how universal compliance recovers Lemma 4. The critical independence condition is represented by seed weights outside the input average rather than by a named independence hypothesis. A reader cannot see that correspondence from the linked eight-line type alone.

**Why it matters:** Readers of Shaltiel and Drucker will look directly for the cap event and the product-law/independence condition; hiding both inside an unlinked definition makes the formal assurance harder to assess than the ordinary proof.

**Revision direction:** Add a brief mathematical gloss of compliantSuccess and a direct link to its existing definition or supporting record passage. Identify how independent seed averaging and the every-branch cap specialize the displayed target to Lemma 4.

**Evidence:**

- `repository/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean`, L18–L25: Conclusion is ∑ω w ω * compliantSuccess f μ (T ω) (fun _ => L) ≤ β^r; the definition of compliantSuccess is imported at L3.
- `repository/docs/reasoning_record.md`, §6.1, anchors CL-joint-cap and CL-weighted-product: Existing discussion distinguishes success jointly with compliance from success conditional on a cheap event.

## ER-022 — medium / lean_link

**Paper:** expert_companion  
**Location:** Appendix A. Checking the statement — What Comparator establishes; PDF p. 12

**Exact current-source locator:**

> The challenge file and the solution are compiled separately.

The prose explains comparison but never links the Solution.lean side and never tells a newcomer why all four headline declarations in the linked Challenge.lean end in sorry. Those holes are intentional specification placeholders, not incomplete proofs, but a reader following the main link has to infer that distinction. The packet supplies the adjacent solution, so this is a navigation omission rather than an evidence gap.

**Why it matters:** A complexity researcher newly checking Lean may stop at the first sorry and conclude that the central theorem is unfinished, exactly when the appendix intends to make the proof certificate easy to inspect.

**Revision direction:** Briefly identify the challenge as the specification with intentional placeholders and link the proof-bearing solution at the same revision; keep implementation identifiers out of running prose.

**Evidence:**

- `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, L326–L341: The four specification declarations have intentional sorry bodies.
- `repository/lean/QuarticCorpus/Unconditional/Solution.lean`, L16–L42: The four proof wrappers refer to proof-bearing implementation declarations.
- `repository/lean/QuarticCorpus/Unconditional/comparator.json`, challenge_module, solution_module and theorem_names: Names the two modules and exact four comparison targets.

## ER-023 — medium / lean_link

**Paper:** expert_companion  
**Location:** Appendix A. Checking the statement — What Comparator establishes; PDF p. 12

**Exact current-source locator:**

> The run used Comparator's paranoid mode

The claim about an actual accepted paranoid run points readers to a target configuration and source examples, but no direct link to the recorded run supporting that execution claim. A configuration establishes what was requested; a theorem source establishes what was stated; neither is the actual run record. The supplied comparator map contains an exact receipt path for the Unconditional bundle, so the existing evidence can be made discoverable without adding internal bookkeeping to the paper.

**Why it matters:** Experts assessing a machine-checked result need to separate the type being audited from the fact that the stated checker was run on it. The current appendix states that distinction well in principle but does not complete the navigation to the execution evidence.

**Revision direction:** Attach one plain-language link to the existing source-bound run record or its human-readable evidence summary, including the recorded revision and checker mode. This asks for a link, not a new run or an objection to the exempted in-progress additions.

**Evidence:**

- `repository/corpus/comparator_map.json`, challenges[path=lean/QuarticCorpus/Unconditional/Challenge.lean].configurations[0].latest_receipt: Contains an exact recorded receipt filename, hash, time and passed status.
- `repository/lean/QuarticCorpus/Unconditional/comparator.json`, entire file: Contains modules, target names and permitted axioms, but no executed-run status or paranoid-mode evidence.
- `repository/docs/reasoning_record.md`, §2.8, paragraph Current global verification: Already links the separate paranoid check to corpus/receipts/comparator-Unconditional-2026-11-02T212245429608+0000.json.

## ER-024 — medium / structure

**Paper:** expert_companion  
**Location:** 5.4 The planted cell; also 5.2 Planting a winner; PDF p. 8

**Exact current-source locator:**

> ### 5.4 The planted cell

Two intended subsection headings render as literal Markdown inside the preceding paragraph: "### 5.2 Planting a winner" on PDF page 7 and "### 5.4 The planted cell" on page 8. In the current source neither heading has a blank line before it. The PDF therefore loses two important divisions of the classical proof even though the source section inventory looks correct.

**Why it matters:** A lower-bound reader scanning for the planted pair or the capped simulator sees raw formatting syntax and misses the intended entry point to each argument.

**Revision direction:** Restore the paragraph/heading block boundaries required by the rendering pipeline and regenerate the PDF. Check the two headings visually; do not infer success from the Markdown heading inventory.

**Evidence:**

- `repository/docs/expert_companion.md`, L181–L183 and L210–L212: Both headings immediately follow nonblank prose lines.
- `repository/docs/expert_companion.pdf`, PDF pp. 7–8: Rendered pages and extracted PDF text both contain the literal three hash signs within prose.

## ER-025 — medium / figure

**Paper:** both  
**Location:** Expert §5.2 Planting a winner, Figure 2; exposition Figures 2 and 4; PDF p. 8

**Exact current-source locator:**

> The two coupled inputs.

The supplied Markdown references three figure sources absent from the ZIP: repository/docs/figures/expert_planted.svg, repository/docs/figures/exposition/fig2_board.svg and repository/docs/figures/exposition/fig4_planted.svg. All three figures are visible in the supplied PDFs, so this is a source-package omission, not a missing rendered figure. LINK_MAP.json omits these destinations and still reports zero problems; an independent used-destination scan finds 77 links rather than its 74. All three omitted captions contain nested square brackets.

**Why it matters:** The paired-input diagram is one of the most useful aids to the argument, but a reader opening or rebuilding the supplied Markdown cannot recover it from this packet. The zero-problem link report gives false reassurance about source completeness.

**Revision direction:** Include the three existing source assets and make the link check include destinations following captions with nested brackets. Preserve the current PDF figures; no redrawing or new mathematical content is needed.

**Evidence:**

- `repository/docs/expert_companion.md`, §5.2, image destination figures/expert_planted.svg: The source reference exists, but the archive has no corresponding member.
- `repository/docs/exposition.md`, §2 Figure 2 and §5 Figure 4: The board and planted-pair SVG destinations are likewise absent.
- `LINK_MAP.json`, problem_count and all recorded destinations: Reports zero problems while excluding the three missing destinations.
- `checks/local_link_audit.json`, missing_members and omitted_by_LINK_MAP: Independent scan retained in this return; checks local supplied bytes, not live remote availability.
- `repository/docs/expert_companion.pdf`, PDF p. 8; exposition PDF pp. 4 and 9: Visual inspection confirms the three figures are already embedded in the PDFs.

## ER-026 — medium / missing

**Paper:** expert_companion  
**Location:** 2. The construction — The total function

**Exact current-source locator:**

> for each $s\in\{0,1\}^r$ a cell $B_{i,s}$

The formal headline quantifies over functions on n bits, but the construction never states its total bit length in terms of the column parameter m. The size of the separate arrays is central to both the inherited cheat-sheet idea and the pointer-encoding comparison. The exposition already gives the exact count n=m[m+rkm+2^r((m−1)ell+rS)] and the consequence O_k(m^22(log m)^3). Including that existing count would remove any ambiguity about m counting columns rather than input bits.

**Why it matters:** Cheat-sheet and pointer-function readers routinely track the size and alphabet of the totalization. They should not have to reconstruct the physical input size while checking that all accesses are bit queries.

**Revision direction:** State or directly cross-reference the existing bit-count formula alongside the layout, with m identified as the number of columns. Keep computational running time separate from query cost and do not seek a smaller construction.

**Evidence:**

- `repository/docs/exposition.md`, §3, final paragraph before §4: Contains the exact input count and the O_k(m^22(log m)^3) bound.
- `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, L232–L238, BitLoc: The four coordinate families match the terms in the already supplied count.

## ER-027 — medium / missing

**Paper:** expert_companion  
**Location:** 3. Where a natural shortcut fails; PDF p. 4

**Exact current-source locator:**

> in the companion record or in its review material

The table promises that every counterexample is checked, but gives only the section where the correct argument is used, rather than an exact source for each example or its finite calculation. "Review material" is not an actionable locator. The omitted fallback in row 4 illustrates why source-level locators matter.

**Why it matters:** Readers cannot quickly verify the numerical examples that are supposed to improve precision; they must search a long record or unspecified review material.

**Revision direction:** Add exact locators to the existing examples/checks, and distinguish a self-contained calculation printed here from one only present in review material. Do not turn the short paper into a dump of checks.

**Evidence:**

- `repository/docs/expert_companion.md`, §3, Table 1 and following paragraph: Only row 7 receives an explicit algorithm immediately below the table.
- `repository/docs/reasoning_record.md`, §6.4, CL-selection-independence-example: Provides a concrete supporting anchor for row 4.

## ER-028 — low / history

**Paper:** expert_companion  
**Location:** 1.1 Where this sits; PDF p. 2

**Exact current-source locator:**

> The cheat-sheet arithmetic shows why the earlier route stopped at the cube.

The opening sentence can suggest a broader ceiling than the following calculation establishes. The paragraph itself correctly analyzes the AND–OR instantiation and says "the same choice"; it does not explicitly assert a universal impossibility theorem. ABK’s quoted statement supplies a positive cubic construction conditional on an optimal partial separation. The useful editorial correction is to keep the scope of the opening sentence as narrow as the calculation.

**Why it matters:** Cheat-sheet authors will distinguish what this instantiation obtains by improving its partial-function input from what the framework could ever obtain. More explicit scoping would prevent a reader from inferring a general barrier.

**Revision direction:** Scope the explanation to that instantiation and to improving its partial-function ingredient. Preserve the useful m′ and certificate-cost calculation, without making it a general no-go claim.

**Evidence:**

- [literature/quartic-ref-02-separations-in-query-complexity-using-chea/source.pdf](https://arxiv.org/abs/1511.01937v2), Introduction, Theorem 1 and following paragraph; §3.1, printed pp. 9–10: ABK gives the 5/2 construction and says an optimal partial separation would boost it to cubic in a black-box manner; §3.1 analyzes AND_m′ composed with OR_m′.
- `paper/extracted.md`, §1.1 and §1.2, printed pp. 2–3: The preprint describes the historical sequence and the new per-column charging mechanism without claiming a no-go theorem for all cheat sheets.

## ER-029 — low / history

**Paper:** expert_companion  
**Location:** 1.1 Where this sits; PDF p. 2

**Exact current-source locator:**

> descends from the pointer functions of Göös, Pitassi and Watson

The pointer lineage is now credited, but the reader is never told that the pointer-function work had already achieved a nearly quartic D-versus-Q separation. This is the relevant neighboring result that helps distinguish the new randomized lower bound from the earlier deterministic one.

**Why it matters:** Authors of the pointer-function and quartic-upper-bound papers will recognize the missing distinction immediately. A single clause would place the new result more exactly without lengthening the history substantially.

**Revision direction:** Mention the existing deterministic-versus-quantum quartic separation when introducing the pointer lineage, retaining the R-versus-Q table as the main historical thread.

**Evidence:**

- [literature/quartic-ref-04-separations-in-query-complexity-based-on-p/source.pdf](https://arxiv.org/abs/1506.04719v3), Abstract; §1.1, main-results list; §3, deterministic complexity separation: The source constructs an almost fourth-power D-versus-Q separation.
- [literature/quartic-ref-03-degree-vs-approximate-degree-and-quantum-i/source.pdf](https://arxiv.org/abs/2010.12629v1), Introduction, PDF p. 2, equation (3) and Theorem 2: ABKRT explicitly says its quartic universal upper bound matches the earlier pointer-function deterministic separation.
- `paper/extracted.md`, §1.1, printed p. 2: The preprint makes this distinction explicitly.

## ER-030 — low / register

**Paper:** expert_companion  
**Location:** Abstract; PDF p. 1

**Exact current-source locator:**

> a 343-line statement file that imports only Mathlib

The abstract ends with a source-file line count and the unexplained names Comparator and Mathlib, after already stating the result and mechanism well. Those implementation details are useful in Appendix A but make the abstract finish on checking machinery. The adjacent promise to present the argument "at the level an expert will want to check" is self-assessment rather than mathematical information.

**Why it matters:** The cited-literature audience wants the contribution and the mechanism from the abstract; readers unfamiliar with the formal tooling are forced to interpret product names before the paper has introduced them.

**Revision direction:** Keep the result, prior-best comparison and separate-array/comparison mechanism in the abstract. Move the line count and checker-specific detail to Appendix A, where they already have a clear role; remove the self-assessment.

**Evidence:**

- `repository/docs/expert_companion.md`, YAML abstract; Appendix A opening and What Comparator establishes: The abstract repeats procedural details that are explained more usefully in the appendix.
- `paper/extracted.md`, Abstract and §1.2: The source preprint leads with the result and query-model scope, then develops the mechanism in the introduction.

## ER-031 — low / error

**Paper:** exposition  
**Location:** 4. The quantum algorithm: a tournament; winner-comparison paragraph; PDF p. 6

**Exact current-source locator:**

> for every $j$, whatever the rival's address inputs are

The displayed winner-comparison guarantee omits j≠i★. The preceding paragraph explicitly sets a_ii=0, so the literal claim for every j is false at j=i★ because ε<1. The intended guarantee for every rival is correct and is stated with the exclusion in the preprint and expert companion. This is a local quantifier slip, not a failure of the tournament argument.

**Why it matters:** A student following the diagonal convention or a tournament researcher checking the hypotheses encounters an immediate contradiction between consecutive paragraphs.

**Revision direction:** Restrict the quantifier to rival columns j≠i★, consistently with the already stated theorem. Treat this as a small secondary correction.

**Evidence:**

- `repository/docs/exposition.md`, §4, Comparing two columns: Explicitly sets a_ii=0.
- `paper/extracted.md`, §3.2, Proposition 3.2, equation (11): States the dominance condition only for j≠i★.
- `repository/docs/expert_companion.md`, §4.1 Comparisons: Correctly includes j≠i★.

## ER-032 — keep / keep

**Paper:** expert_companion  
**Location:** 4.1 Comparisons; PDF p. 6

**Exact current-source locator:**

> whatever the rival's address inputs

The two deterministic facts are stated cleanly: an all-one winner can never be disqualified, and its correctly decoded address disqualifies every rival. This establishes the guarantee without any correctness assumption on the rival decoder.

**Why it matters:** Pointer-function and quantum-search experts can see exactly why off-promise rivals do not compromise totality.

**Revision direction:** Preserve this argument and its location immediately before the abstract tournament lemma; avoid replacing it by a generic claim that address decoding is reliable.

**Evidence:**

- `paper/extracted.md`, §3.3: Uses the same one-sided winner argument.
- `repository/docs/reasoning_record.md`, §5.3, upper-winner-dominates: Expands the logical dependence explicitly.

## ER-033 — keep / keep

**Paper:** expert_companion  
**Location:** 5.1 A direct product with separate caps; PDF p. 7

**Exact current-source locator:**

> zero-weight branches need no division

The unnormalized value recursion provides a short complete explanation of why adaptive interleaving still admits a product bound. It avoids unnecessary conditional-probability notation and handles zero-mass branches naturally.

**Why it matters:** Drucker and Shaltiel readers can recognize the capped direct-product mechanism and verify the induction quickly.

**Revision direction:** Keep this proof, the all-branch cap and joint-independence qualification. Credit it as the proof route used here without suggesting that the cited global-budget theorems are identical statements.

**Evidence:**

- `repository/docs/reasoning_record.md`, §6.1, unnormalized product induction and CL-normalization: Explains the relation to the conditional-value proof.
- `paper/extracted.md`, §4.1, Lemma 4.1: Proves the same capped target by the conditional supermartingale route.
- [Drucker, arXiv:1005.0644v2](https://arxiv.org/pdf/1005.0644v2), §1.3, printed pp. 6–7; Lemmas 3.1–3.2, printed pp. 11–12: Explains the fair per-instance-cap proof and the product posterior/value process; this is distinct from the paper’s stronger total-budget theorem.

## ER-034 — keep / keep

**Paper:** expert_companion  
**Location:** 5.4 The planted cell; PDF p. 9

**Exact current-source locator:**

> This bounds a joint event under the original law.

The simulator fixes a column and time, stops before exceeding the cap, and uses containment of the nonheavy-hit event in simulator success. The text expressly refuses to condition the hard distribution on nonheaviness.

**Why it matters:** Adaptive-query lower-bound experts will see that the rare-event conditioning trap has been resolved rather than hidden behind a direct-product citation.

**Revision direction:** Preserve the simulator, the quantifiers i and τ, and the joint-event sentence in the main paper. They deserve more prominence than the refinements of numerical constants.

**Evidence:**

- `paper/extracted.md`, §4.2, simulator preceding (21): Gives the same joint-event reduction.
- `repository/docs/reasoning_record.md`, §6.5, capped simulator: Expands why conditioning on the cap is not legitimate.

## ER-035 — keep / keep

**Paper:** expert_companion  
**Location:** 7. The exponent; PDF p. 10

**Exact current-source locator:**

> The order of quantifiers is:

The proof specifies α, then a fixed k, then its constants and threshold, then m→∞, and correctly warns that a fixed k excludes only powers below 4−2/k. This is the necessary scope for the optimal-infimum result and avoids claiming an exact fourth-power separation.

**Why it matters:** Authors of the earlier near-cubic separations can identify precisely what has been settled and what has not.

**Revision direction:** Keep this concise argument and the explicit distinction from R=Ω(Q^4); retain it as the endpoint of the main mathematical narrative.

**Evidence:**

- `paper/extracted.md`, §5, proof of Theorem 1.1: Uses the same order of choices.
- `repository/docs/reasoning_record.md`, §§7.1–7.2: Separately explains strict exponent gaps and the infimum.

## ER-036 — keep / keep

**Paper:** expert_companion  
**Location:** 1. The result; PDF p. 1

**Exact current-source locator:**

> The upper bound $R(f)\le D(f)=O(Q(f)^4)$ for total $f$ is due to Aaronson, Ben-David, Kothari, Rao and Tal

The upper-bound attribution correctly separates ABKRT’s quantum consequence from Huang’s sensitivity theorem, and the Theorem 2 / Conjecture 2 locators are correct in the supplied PDF. This fixes the prior tendency to blur the older universal bound with the new separation.

**Why it matters:** The sensitivity and quantum-query authors receive credit for the exact result proved, and readers can verify why the new lower-bound family settles the exponent.

**Revision direction:** Keep the attribution and the theorem/conjecture distinction, even if the opening is shortened.

**Evidence:**

- [literature/quartic-ref-03-degree-vs-approximate-degree-and-quantum-i/source.pdf](https://arxiv.org/abs/2010.12629v1), Theorem 2, PDF p. 2; Conjecture 2, PDF p. 20: Theorem 2 states D=O(Q^4); Conjecture 2 states R=O(Q^3).
- [literature/quartic-ref-17-induced-subgraphs-of-hypercubes-and-a-proo/source.pdf](https://arxiv.org/abs/1907.00847v2), Theorems 1.1 and 1.4; §2: Huang proves the induced-cube and degree/sensitivity statements used in ABKRT.

## ER-037 — keep / keep

**Paper:** expert_companion  
**Location:** 1.1 Where this sits; PDF p. 2

**Exact current-source locator:**

> Improved partial separations then gave $8/3-o(1)$ and $3-o(1)$

The total-function sequence 5/2, 8/3−o(1), and 3−o(1), with independent credit to both 2021 approaches at the cubic stage, is now correct. The AND–OR/certificate-cost explanation usefully relates the numbers rather than offering a bare list.

**Why it matters:** Readers from the cheat-sheet, Tal, and optimal-partial-separation papers can see exactly how their results fit into the development and what ingredient the new construction changes.

**Revision direction:** Preserve the sequence and the cost comparison while correcting the explicit-Forrelation attribution and narrowing the cubic-barrier wording.

**Evidence:**

- [literature/quartic-ref-02-separations-in-query-complexity-using-chea/source.pdf](https://arxiv.org/abs/1511.01937v2), Theorem 1, Introduction; §3.1: Provides the 5/2 separation and black-box cubic consequence.
- [literature/quartic-ref-26-towards-optimal-separations-between-quantu/source.pdf](https://arxiv.org/abs/1912.12561v1), Introduction, “Application: Power-(2+2/3) Separations for Total Boolean Functions”, printed pp. 2–3: Derives the 8/3−o(1) total-function separation through cheat sheets.
- [literature/quartic-ref-23-an-optimal-separation-of-randomized-and-qu/source.pdf](https://arxiv.org/abs/2008.10223v4), §1.3, Theorem 1.5, PDF p. 4: States the 3−o(1) total-function consequence.
- [literature/quartic-ref-06-k-forrelation-optimally-separates-quantum/source.pdf](https://arxiv.org/abs/2008.07003v3), Corollary 1.5, PDF p. 4: States the independent explicit total-function cubic consequence.

## ER-038 — keep / keep

**Paper:** expert_companion  
**Location:** 1.1 Where this sits; PDF p. 2

**Exact current-source locator:**

> it needs every comparison to compute a fixed predicate with bounded error

The explanation of why bounded-error search cannot simply be invoked on arbitrary loser-comparison probabilities is accurate and worth keeping. It identifies a missing hypothesis instead of treating error reduction as a universal repair.

**Why it matters:** Quantum-search readers immediately understand the distinction between a noisy implementation of a fixed bit and a procedure whose off-promise acceptance probability may be arbitrary.

**Revision direction:** Keep this distinction next to the tournament mechanism, and preserve the fixed-predicate qualification when shortening the related-work discussion.

**Evidence:**

- [external primary source: Høyer–Mosca–de Wolf](https://arxiv.org/pdf/quant-ph/0304052), §1, arXiv PDF pp. 1–2: The problem is defined by fixed Boolean values f_i, each computed with bounded two-sided error.
- `paper/extracted.md`, §3 introduction, printed p. 7: The preprint says that no uniform gap from 1/2 exists for nonwinner comparisons.

## ER-039 — keep / lean_link

**Paper:** expert_companion  
**Location:** 1. The result — formalisation qualification; PDF p. 2

**Exact current-source locator:**

> that is built but has not been compared.

The companion now cleanly separates the compared family statement from the stronger explicit constants theorem. The linked headline has an existential logarithmic exponent and floor-form lower bound; the linked constants theorem has b=6 and coefficient 1/400 for the same named circuit. That distinction is important and is stated again in the appendix without suggesting that one kind of evidence substitutes for the other.

**Why it matters:** Experts can distinguish the published mathematical statement from the exact type independently compared, without being asked to understand the project's internal status vocabulary.

**Revision direction:** Keep this precise qualification when shortening the paper, and preserve the same-circuit requirement in both descriptions.

**Evidence:**

- `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, L328–L334: Compared type has existential b and Gvalue < R for one circuit C.
- `repository/lean/QuarticQuery/Paper/ConstructionFamily.lean`, L28–L40: Explicit theorem states b=6 and 1/400 for one forrCircuit.

## ER-040 — keep / lean_link

**Paper:** expert_companion  
**Location:** Appendix A. Checking the statement — What it does not establish; PDF p. 12

**Exact current-source locator:**

> both sides come from one specification, so a modelling error shared by both would pass.

This is the right limitation to put next to the Comparator assurance. The appendix does not confuse proof/type agreement with independent semantic validation of R, Q or the construction, and it names the remaining human task in mathematical terms.

**Why it matters:** Authors of the cited mathematics can judge precisely what formal agreement adds and what conceptual responsibility remains with them.

**Revision direction:** Preserve this sentence and keep it close to the description of the checker, even if the procedural detail is shortened.

**Evidence:**

- `repository/lean/QuarticCorpus/Unconditional/Solution.lean`, L3 and theorem declarations: Solution imports the maintained statement vocabulary; the challenge separately restates the specification.
- `repository/corpus/comparator_map.json`, boundary and credit_vocabulary: The map explicitly distinguishes configured targets and textual wrapper associations from semantic review.

## ER-041 — keep / lean_link

**Paper:** expert_companion  
**Location:** Appendix A. Checking the statement — Five things to check; PDF p. 11

**Exact current-source locator:**

> with one $\mathcal C$ for both bounds.

The appendix accurately translates the quantifier order and makes the common-circuit witness explicit. Its four headline links name the configured Checked wrappers, rather than merely pointing to implementation lemmas whose comparison status could be inferred incorrectly.

**Why it matters:** Query-complexity readers can rule out the serious mistake of taking the two bounds on different functions, and can locate the exact four declarations subject to comparison.

**Revision direction:** Keep the plain mathematical names, exact target links and same-circuit condition as the core of the quick audit route.

**Evidence:**

- `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, L328–L334: ∀ k ∃ S,A,b,t₀ ∀ t ∃ C, with both cost bounds inside the same existential witness.
- `repository/lean/QuarticCorpus/Unconditional/comparator.json`, theorem_names: The four displayed Checked declarations are exactly the four configured targets.

