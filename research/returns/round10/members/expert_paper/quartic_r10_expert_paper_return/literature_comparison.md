# Literature comparison and revision decisions

## Purpose and reading boundary

The useful comparison is between the reader's task at a particular passage and the way a primary source supplies the required object, contract, motivation or proof. The recommendations below are **source-guided editorial judgments by this review**, not opinions attributed to the named authors about the companion. A paper that proves a related theorem need not provide the right interface for this construction.

This document combines the quantum specialist's and randomized-lower-bound specialist's retrospective checks after the frozen first pass. It is not another blind reading. “Read” means that a reviewer inspected the stated passages; it does not mean that every reviewer independently read the entire source. Bibliographic inspection, search results, a theorem statement and a complete proof are distinguished below. Source IDs Q-S## follow the quantum inventory; CL- prefixes the classical inventory's source_id. The four ROOT- writing-source IDs identify the additional local passages inspected while assembling this document.

The main editorial choice is to expose each construction-specific operation before its generic implementation becomes a substantial detour. On the quantum side, the operation is the exact success-and-label mass \(w_i/m\), which connects a comparison circuit to the next-pivot law. On the classical side, it is the unconditional capped predictor for one proposed cell query. In the optional uniform section, there are two legitimate reading goals: using an explicit estimate to choose a growing parameter, and auditing the analytic proof of that estimate. A short companion should make the route between those goals explicit.

Finding links below open the portable [feedback register](feedback.json); the XP10 identifier locates the associated advice.

## 1. The supplied source preprint

### OpenAI — the actual construction and its existing mechanisms

**Source IDs:** Q-S03; CL-original-preprint. **Edition:** *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, 5 October 2026, supplied preprint; the cited repository URL names revision 4eaee875. [Primary PDF destination](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf).

**Read:** quantum §§3.1–3.3, printed pp. 7–10, extracted lines 304–516; classical §§4.1–4.2 and the opening of §5, printed pp. 11–13, lines 522–699. The title/date were checked. This is selected proof reading, not a cover-to-cover revalidation.

The quantum passages already contain the finite amplification schedule, tensor preparation, conditional-law coupling, comparison and verification. The classical passages contain the product/capped-predictor/erasure mechanism. The companion's task is to make the connections among those mechanisms and its formal interfaces easier to inspect. Reorganizing them does not create a new algorithmic contribution.

The transferable choice is a compact stage map followed by the exact local identity or event inclusion doing the work. For the companion, that favours keeping sampler, coupling and rebuilding cost contiguous, and keeping the planted input close to the predictor that reads it. The source does not dictate that generic lemmas must move to appendices: that is the present review's choice for this manuscript's length and audience. See [XP10-008](feedback.json) and [XP10-010](feedback.json).

## 2. Quantum primitives: preserve the exact contract

### Brassard–Høyer–Mosca–Tapp — rotation, good component, and stopping cost

**Source ID:** Q-S04. **Edition:** arXiv:quant-ph/0005055v1, distinct from the bibliography's 2002 publication. [Primary version](https://arxiv.org/pdf/quant-ph/0005055v1).

**Read:** §2 through Theorem 3/QSearch, extracted lines 21–155: the operator, invariant subspace, good-state formula, endpoints and unknown-probability algorithm.

This passage separates two reader tasks: understanding what amplification does to the good component, and finding a useful iteration count. The first explains why an amplified successful sample can preserve the relative probabilities of its output labels. The second introduces a cost guarantee whose form matters.

The companion should retain a local interface specifying exact conditional label law, a deterministic cap on every branch, inverse access and behaviour below the promised success threshold. The standard rotation calculation can be shortened or deferred once that interface has a concrete use. QSearch's expected-cost guarantee, including its behaviour at zero success probability, does not supply this fixed-cap interface by itself. This is the substantive limit on the relocation proposed in [XP10-008](feedback.json).

### Boyer–Brassard–Høyer–Tapp — the averaging calculation

**Source ID:** Q-S05. **Edition:** arXiv:quant-ph/9605034v1, submitted 23 May 1996, with a draft date of 10 May 1996; distinct from the 1998 journal citation. [Primary version](https://arxiv.org/pdf/quant-ph/9605034v1).

**Read:** §4, Lemmas 1–2 and the complete averaged-probability calculation on printed p. 3. The two-column extraction was checked against the rendered page.

The reader task here is narrower than proving the whole search procedure: verify the average success probability obtained by a random iteration count. A precise lemma locator lets the companion delegate that standard calculation while retaining its own finite schedule and cutoff.

This supports the same interface/implementation split as BHMT, without treating a source citation as a substitute for all operational clauses. The companion must still explain how its chosen trials and cutoff produce the stated all-branch cap. A page locator for the inspected arXiv draft should not be silently presented as a journal-page locator. See [XP10-008](feedback.json).

### Aaronson–Ambainis — identify the experiment before quoting its cost

**Source ID:** Q-S06. **Edition:** *Forrelation*, arXiv:1411.5729v1; the bibliography cites the 2018 SICOMP publication. [Primary version](https://arxiv.org/pdf/1411.5729v1).

**Read:** §3.2, Figure 1, the paragraph before Proposition 6, and Proposition 6 with its complete proof; printed pp. 13–14, extracted lines 646–738. Both original pages were inspected visually.

The passage distinguishes a projection experiment with probability \(\Phi^2\) from an interference experiment with probability \((1+\Phi)/2\). The reader therefore needs to know which experiment a subsequent query count describes.

The companion's explicit identification of the projection decoder should remain. It explains the \(\delta^{-2}=2^{10k}\) dependence used when \(k\) grows; it also prevents the proposition about the other experiment from being mistaken for the implemented decoder. The projection test is adequate on the stated asymmetric promise. Its inability to decide all off-promise domain membership is handled by the separate exact circuit. These checks support the brief cost bridge in [XP10-012](feedback.json), not an allegation that squaring the statistic invalidates decoding.

### Høyer–Mosca–de Wolf — noisy evaluation of a fixed predicate

**Source ID:** Q-S09. **Edition:** supplied quant-ph/0304052 source extraction, associated with the ICALP 2003 citation. [Primary record](https://arxiv.org/abs/quant-ph/0304052).

**Read:** introduction, query-model definition, §3 Facts 1–2 and the setup of the amplification/error-reduction process, extracted lines 1–60. The full optimal-search proof was not revalidated.

The source asks the reader to distinguish a Boolean predicate from the noisy procedures used to evaluate it. Those procedures still target the same fixed labels with the required bias.

That distinction should guide the companion's discussion of alternative search tools. Between two losing candidates, its comparison outcomes need not approximate a fixed predicate or fixed edge direction. A robust-search theorem for noisy evaluations therefore cannot simply replace the weighted sampler. This supports a short, precise oracle distinction at the comparator's introduction rather than an extended catalogue before the comparator exists; see [XP10-002](feedback.json).

## 3. Candidate elimination and fixed-edge comparisons

### Ambainis–Iraids–Kokainis — what the direction test is estimating

**Source ID:** Q-S07. **Edition:** arXiv:2609.11664v3, revised 5 October 2026. [Primary version record](https://arxiv.org/abs/2609.11664v3).

**Read:** §6.1 overview, candidate-set/update equations and fixed-graph direction-test contract, extracted lines 306–355; later FindSource cost/implementation discussion, lines 397–436. The complete variable-time proof was not audited. Damaged pseudocode extraction was not used for exact pseudocode claims.

The useful passage-level comparison is the relationship between an evolving candidate set and the fixed graph whose directions are being tested. A bounded-error test estimates that existing relation; its noise does not remove the relation.

The companion should compare this contract directly with complementary but otherwise unrestricted losing-pair probabilities. Its fractional weights encode a different survivor mechanism. Keeping the oracle distinction beside the new comparator makes the comparison assessable when both objects are available. It does not justify importing the source's implementation or claiming that every set-valued elimination argument fails. See [XP10-002](feedback.json).

### Mande–Paraashar–Saurabh — king finding is a distinct task

**Source ID:** Q-S08. **Edition:** published FSTTCS 2023, LIPIcs 284, article 30. [Published primary version](https://doi.org/10.4230/LIPIcs.FSTTCS.2023.30).

**Read:** introductory definition/model, §4 Theorem 19 proof on pp. 30:11–30:12, adjacent Lemma 18 interface, and Algorithm 4 visually on p. 30:13. Not all supporting sampling proofs were read.

A king reaches every other vertex by a directed path of length at most two. That target is different from a vertex defeating every other vertex directly. The passage helps a reader identify the problem being solved before comparing elimination routines.

The transferable choice is to give the task and oracle first, then identify the structural analogy. The mismatch is fixed edge access versus the companion's arbitrary probabilities between losing candidates. The source supplies context for elimination/search, not a theorem for the companion's probabilistic comparator. This is a reason to compress and localize the comparison under [XP10-002](feedback.json), not to discard its credit.

### Ben-David–Kothari — elimination and verification as separate stages

**Source ID:** Q-S12. **Edition:** arXiv:2609.15063v1. [Primary version record](https://arxiv.org/abs/2609.15063v1).

**Read:** construction, Lemmas 2–3, and §3 Lemma 5 algorithm discussion, extracted lines 11–112. Lemma 4's proof was not substantively reviewed because the displayed output was truncated.

The inspected algorithm discussion makes candidate elimination and final verification separately visible. That division helps a reader anticipate why the last verification stage remains necessary after a search has produced a plausible candidate.

A short stage map is transferable to the companion without importing the source's algorithm. The comparison relation is fixed, and the source's SINK terminology uses a reversed arrow convention. Neither should be carried into the companion without translation. The useful editorial result is clearer placement of final verification and a concrete oracle comparison, as in [XP10-002](feedback.json) and [XP10-008](feedback.json).

## 4. Construction lineage: explain the choice being inherited

### Ambainis–Balodis–Belovs–Lee–Santha–Smotrovs — pointer representation matters

**Source ID:** Q-S10. **Edition:** supplied arXiv:1506.04719 manuscript, associated with the JACM 2017 citation. [Primary record](https://arxiv.org/abs/1506.04719).

**Read:** §1.3 technique discussion, extracted lines 211–295: back pointers, totalization, balanced trees and the direct-pointer-symbol alternative. Where mathematical extraction was damaged, only intact prose/model comparisons were used.

This discussion connects pointer architecture to the separation it enables and to the cost of representing pointers. It is a better comparison target than a general assertion that both constructions use pointers.

The companion should retain the distinctions among back pointers, balanced trees and its chosen direct fields, but place the detailed representation comparison after readers have seen those fields. The source's direct-pointer-symbol alternative has an exponential alphabet in its own setting; transferring its cost conclusion requires matching the parameters and access model. This informs [XP10-002](feedback.json), while preserving the existing lineage and the Boolean-encoding distinction.

### Aaronson–Ben-David–Kothari — totalization before detailed parameters

**Source ID:** Q-S11. **Edition:** supplied arXiv:1511.01937v2, associated with the STOC 2016 citation. [Primary version record](https://arxiv.org/abs/1511.01937v2).

**Read:** introduction through the summary of results, extracted lines 1–84: promise-totalization motivation and advertised improvements. The specialist did not independently read the composition proof in §3.

The introduction gives a reader the purpose of adding certificate information to a promise problem before requiring the construction's details. The companion can similarly keep immediate cheat-sheet credit and a matched old/new cost comparison near its main result.

The transfer is organizational, not verification of every old-recipe parameter from this limited read. The companion's detailed optimization can move to a later related-work location or the record while retaining the precise claim that the cubic ceiling concerns the analyzed balanced AND–OR recipe. It is not an impossibility theorem for every cheat-sheet construction. See [XP10-002](feedback.json).

## 5. Randomized hardness and the optional analytic proof

### Bansal–Sinha — separate the promised problem, hard law and analytic engine

**Source ID:** CL-bansal-sinha. **Edition:** arXiv:2008.07003v3, the mathematical locator edition named alongside the STOC 2021 citation. [Primary version record](https://arxiv.org/abs/2008.07003v3); [publication DOI](https://doi.org/10.1145/3406325.3451040).

**Read:** definition, theorem/corollary and introductory discussion, extracted lines 1–84; §3 distribution and proof outline, lines 365–451; §4.3 integration-by-parts statement and opening, lines 490–500. Overview lines 104–155 were only partly seen and search hits skimmed. The full published lower-bound proof was not revalidated.

Section 3 first specifies the correlated Gaussian/rounding law and the statistic's promise behaviour, then states the advantage-to-Fourier-weight interface. This helps a reader identify which distribution and guarantee each analytic estimate concerns.

The companion needs the same separation of roles. Its ordinary fixed-\(k\) input comes from the cited explicit Walsh–Hadamard theorem. Its optional reconstruction uses a different algebraic bias and proves the necessary moment and derivative estimates for that law. That law is not the promised minimax law used in §4. The uniform theorem should therefore appear with its full conditions and exact proof destination before readers choose whether to follow the analytic mechanism. This supports [XP10-012](feedback.json), without implying that the cited source already contains the reconstruction's exact constants or that the reconstruction dominates its result.

### Drucker — the continuation value explains the product bound

**Source ID:** CL-drucker. **Edition:** arXiv:1005.0644v2; the supplied author text says it essentially matches *Computational Complexity* 21(2), 197–244 (2012). [Primary version record](https://arxiv.org/abs/1005.0644v2); [publication DOI](https://doi.org/10.1007/s00037-012-0043-7).

**Read:** introduction through methods, extracted lines 1–85; lines 125–200, including the §3 proof and final fair-tree remark. The source's partial-domain extension and edition note were checked. The whole paper was not read.

The §3 proof defines a continuation value, proves its one-step inequality, and establishes the transcript-conditioned product law before multiplying values. The reader can see both why adaptive interleaving is allowed and which independence survives it.

The companion's unnormalised recurrence is a concise alternative that avoids dividing by zero-mass transcripts. Its exact separate-cap statement should remain before the simulator. The full induction and optional global-budget substitution can follow the application, once the reason for each hypothesis is concrete. The inspected general theorem with \(T=L\), error \(1/3\), and \(\alpha=3/r\) gives the advertised \(2\beta^r\); it is not the exact separate-cap statement. See [XP10-010](feedback.json).

### Girish–Tal–Wu — name the controlled sum before invoking its bound

**Source ID:** CL-girish-tal-wu. **Edition:** published CCC 2021, LIPIcs 200, article 39, pp. 39:1–39:36. [Published primary version](https://doi.org/10.4230/LIPIcs.CCC.2021.39).

**Read:** §1.3's ordinary-tree overview and Lemma 9, pp. 39:6–39:8, extracted lines 351–550; footnote 2's stopping warning at lines 523–525; the opening of the parity discussion. The later complete proof was not revalidated.

The overview identifies the terminal signed coefficient sum, then its increments and the degree induction. That order makes the probabilistic estimate answer an already visible question.

For the companion, a brief description of the order-\(k\) raw-derivative sum would help if the analytic sketch remains. Its bounded-bias adaptation is proved in the record; the published lemma is methodological ancestry, not that exact statement. Alternatively, readers interested in the growing family can use the uniform interface first and follow an exact link for this analytic task. See [XP10-012](feedback.json).

## 6. Primary research beyond the supplied annex

### Hamoudi — state the query task compactly

**Source ID:** Q-S13. **Edition/read:** author-hosted PDF dated 24 April 2026; title, introduction and §1.1 through binary/phase query definitions, pp. 1–4, read via primary PDF extraction. [Author PDF](https://yassine-hamoudi.github.io/files/publications/QueryComplexity.pdf).

The passage moves from the task, input alphabet and success requirement to access and cost. That supports a compact model contract near the companion's result, with operational details at their use. It does not call for tutorial prerequisites in an expert paper. The rest of the notes was not read. This is a presentation comparison, not an additional theorem dependency.

### Arora–Kumar — a closer find-and-verify comparison

**Source ID:** Q-S14. **Edition/read:** arXiv:2610.39702v1, submitted 29 October 2026; abstract/introduction, fixed-edge definitions, and §6.1 Lemma 6.1 plus complete Theorem 6.2 proof, pp. 11–12. [Primary version](https://arxiv.org/pdf/2610.39702v1).

Theorem 6.2 finds a Condorcet winner, or reports absence, by finding a king and checking for an incoming edge. This is a close structural comparison for the companion's search followed by verification. It still assumes coherent fixed-edge access. The optional update in [XP10-004](feedback.json) should replace a less useful comparison, not lengthen the opening. This later source supplies neither a missing premise nor a priority objection; other results were not verified.

### Ben-David–Blais — an interface can precede a long embedding proof

**Source ID:** CL-bd-blais-dpt2025. **Edition/read:** author-hosted 43-page manuscript associated with FOCS 2025, arXiv:2512.08268; overview through §1.3, §3.1 interfaces, and §4's opening. [Author PDF](https://cs.uwaterloo.ca/~eblais/assets/pdf/direct_product_theorems.pdf).

Section 1.3, pp. 6–8, defines discounted score, motivates tensorization and sketches the embedding. Section 3.1, p. 17, states interfaces and derives a consequence before the longer proofs. This supports keeping the companion's product contract before its use while relocating implementation detail: [XP10-010](feedback.json). The measure differs from exact per-input caps, so this source should not replace Lemma 5's justification. The complete tensorization proof was not audited; no identity with the proceedings edition is asserted.

### Ben-David–Blais — ordinary minimax has a specific guarantee

**Source ID:** CL-bd-blais-minimax. **Edition/read:** author-hosted 59-page ACM-template manuscript dated September 2023; introduction, pp. 1–3, and opening principal interface. It retains template publication metadata. [Author PDF](https://cs.uwaterloo.ca/~eblais/assets/pdf/minimax.pdf).

The introduction separates fixed-cost hardness from stronger balanced-label and simultaneous small-bias guarantees. This clarifies why the companion may use a biased hard law chosen for one cap. No stronger minimax theorem is needed. Retain that exact guarantee when reorganizing §4 under [XP10-010](feedback.json). The remaining proof was not read; manuscript page numbers are not claimed as final journal pagination.

## 7. Writing and exposition passages inspected locally

These four comparisons were added only after reading the supplied PDF passages themselves. They support decisions about this manuscript; they are not mechanical rules requiring every expert paper to adopt the same structure.

### Knuth–Larrabee–Roberts — motivation and a self-contained interface

**Source ID:** ROOT-KLR. **Edition/read:** the Stanford course report based on autumn 1987; title page, PDF pp. 4–5 (§1 items 5–19, especially 5 and 10–14), and pp. 22–23 (§10, algorithm presentation). [Author-hosted report](https://www-cs-faculty.stanford.edu/~knuth/papers/cs1193.pdf).

These passages combine self-contained theorem statements with motivating prose, complementary explanations and modular algorithm presentation. Their useful implication here is to keep a lemma's contract available while moving its detailed implementation until the reader knows its purpose. This supports [XP10-008](feedback.json) and [XP10-010](feedback.json). The report also treats algorithm style as adaptable; it does not prescribe an appendix or a universal lemma order. The rest of the report was not read for this comparison.

### Francis Su — choose examples and details for the task

**Source ID:** ROOT-SU. **Edition/read:** *Guidelines for Good Mathematical Writing*, updated 18 August 2020, all three pages. [Author PDF](https://math.hmc.edu/su/wp-content/uploads/sites/10/2020/08/Guidelines-for-Good-Mathematical-Writing.pdf).

Sections 1–2 connect audience, complete sentences, structural signposting and examples that retain the relevant feature. For this companion, that supports an earlier construction, a compact side-by-side weight example, and an explicit choice between using and explaining the optional uniform estimate: [XP10-002](feedback.json), [XP10-009](feedback.json), [XP10-012](feedback.json). The per-block versus terminal-lightness example mismatch also matters because the explanatory feature should match the stated event: [XP10-011](feedback.json). The classroom examples do not require simplifying away the expert paper's exact hypotheses.

### Andrew Childs — explain the compute/copy/uncompute operation

**Source ID:** ROOT-CHILDS. **Edition/read:** *Lecture Notes on Quantum Algorithms*, title dated 17 April 2025; PDF pp. 10–11, particularly §1.4, printed pp. 2–3, with adjacent text also read. [Author PDF](https://www.cs.umd.edu/~amchilds/qa/qa.pdf).

Section 1.4 explains reversible evaluation by retaining intermediates, copying the answer, then reversing the computation. A similarly short operational explanation helps connect the companion's decoder to coherent calls and inverse access. Keep that model bridge near its use when applying [XP10-008](feedback.json). The tutorial argument does not establish the companion's stronger retained-state formal correspondence or its physical-subsystem transport; those require their own exact evidence. No later chapters were reviewed.

### Andris Ambainis — explain a construction before comparing its variants

**Source ID:** ROOT-AMBAINIS. **Edition/read:** query-complexity survey, arXiv:1712.06349v1; PDF/printed pp. 9–12, §4 and the opening of §5. [Primary version](https://arxiv.org/pdf/1712.06349v1).

Section 4 presents a concrete pointer function, its certificate and elimination algorithm before variants; §5 introduces cheat-sheet totalization through its purpose and interface. That order supports making the companion's predicate available before detailed architectural comparisons: [XP10-002](feedback.json). The survey's bounds and open questions describe its historical edition, not the current state of the subject. This reading is an exposition comparison, not verification of the later results it cites.

## 8. Resulting editorial choices and their limits

The sources support several concrete choices, with the mathematical contracts preserved:

| Reader task | Proposed choice | Finding |
|---|---|---|
| Understand what changed from earlier constructions | Keep immediate credit and the matched old/new cost pair; relocate detailed old-recipe optimization and model comparisons until their objects are available. | [XP10-002](feedback.json) |
| Follow the real quantum sampler | Introduce the complementary comparator, ideal weights and \(w_i/m\) mass identity; give the bounded amplifier interface at use; keep coupling and rebuilding cost contiguous. | [XP10-008](feedback.json) |
| Compare two normalization operations | Present the finite weight example in a small table, preserving its exact comparator data and its abstract-example scope. | [XP10-009](feedback.json) |
| Understand why the classical product lemma applies | Keep its precise statement before the application, then show planting, erasure and the unconditional capped predictor; retain the proof at a usable later destination. | [XP10-010](feedback.json) |
| Understand the conditioning warning | Link an example of the exact terminal-lightness event, with its hard-law premise and limited construction scope stated accurately. | [XP10-011](feedback.json) |
| Use the stronger single-family consequence | State the uniform estimate with its conditions and direct proof destination, derive the new allowance and schedule, and make the analytic route separately available. | [XP10-012](feedback.json) |

These are presentation recommendations. The technical checks do not justify replacing exact contracts with general labels such as amplitude amplification, robust search or direct product. Nor do the comparisons justify claiming that a successful destination lookup validates an entire proof.

## 9. Edition and access limits that must remain visible

The bibliography was checked for identities and locators, but inclusion in it did not count as source reading. Uninspected portions remain uninspected. In particular:

- **Yao 1977:** the exact original full text was unavailable in the supplied annex/retrieval record. It was not read in this review. The finite minimax argument was inspected in the current reasoning record and through the explicitly identified later sources; that is not a claim to have read Yao's original.
- **Nisan 1991, CREW PRAMs and decision trees:** the exact original was likewise unavailable. The supplied Nisan–Szegedy 1994 material is a different work and does not fill that reading gap.
- **BSS2003:** the packet supplies a complete earlier manuscript dated 23 May 2002, Los Alamos report LA-UR-01-6417, but not the exact 2003 conference edition. Its presence does not support an “absent source content” claim; it also does not establish edition or pagination identity with [the cited proceedings publication](https://doi.org/10.1109/CCC.2003.1214419). This comparison does not claim to have read that manuscript's full proof.
- **The reasoning record:** Q-S15 and CL-current-record concern the current packaged file, SHA-256 19a92fa5d5b2859855450074bbc840a6c0734490a0dc501be24efb8e72de5b07. The lead's links name public revision 8357f268732746d1575e05e7de8c888e20ad3793. The packet reports different bytes. The specialists' checks therefore establish support in the packaged edition, not identical support at the public pin. Before applying the exact theorem/example navigation suggestions in [XP10-011](feedback.json) and [XP10-012](feedback.json), confirm that their destination edition contains the inspected passage.

Finally, reading supplied Lean statements or local proofs is different from compiling them or repeating a configured comparison. No fresh Lean build or Comparator execution underlies this literature comparison. The separate result-to-evidence mapping recommended in [XP10-013](feedback.json), and the stale-status reconciliation in [XP10-014](feedback.json), should preserve those distinctions.
