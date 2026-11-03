# Literature comparison: what the quantum-query literature teaches this revision

## Judgment

The three manuscripts now distinguish several mathematical objects that a quick survey can easily conflate: a total-order comparison, a noisy evaluation of a fixed edge, an arbitrary pairwise winning probability, the success probability of a preparation, its conditional label law, and its successful quantum state. That is a substantial strength. The next revision should make these distinctions easier to use while reducing the amount of standard machinery a reader must hold before reaching the weighted tournament.

The best comparison is operational. For each source, ask what the algorithm is given, what it returns, what it is allowed to assume, and what is counted. A citation list cannot do that work. Nor does a low count of fashionable words establish good writing. The supplied sources differ markedly in length and audience, but their strongest passages make the next mathematical action apparent.

This is an editorial and technical comparison by simulated reader perspectives, not a report of reactions from any named author. The reading scopes below are deliberate. A targeted passage read closely is not represented as a whole paper read. Current manuscript quotations and findings are in the accompanying feedback; quotations from outside works here remain below twenty-five words total per source.

## Sources and actual scope of reading

| Source | Status and inspected scope | Source location |
|---|---|---|
| OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, 5 October 2026 | **Read, targeted:** supplied introduction §§1.1–1.3 and quantum argument §§3.1–3.3, including the amplification, tournament and verification proofs; not the entire preprint | [Official preprint directory](https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026); supplied `paper/extracted.md` |
| Dürr–Høyer, *A Quantum Algorithm for Finding the Minimum*, arXiv v2 | **Read:** supplied two-page main paper, algorithm and proof | [arXiv:quant-ph/9607014](https://arxiv.org/abs/quant-ph/9607014) |
| Høyer–Mosca–de Wolf, *Quantum Search on Bounded-Error Inputs* | **Read:** supplied extracted main text, including §3 algorithm analysis and applications | [arXiv:quant-ph/0304052](https://arxiv.org/abs/quant-ph/0304052) |
| Brassard–Høyer–Mosca–Tapp, *Quantum Amplitude Amplification and Estimation* | **Read, targeted:** supplied §1 and §2 through Theorem 3 and its proof; not the amplitude-estimation development | [arXiv:quant-ph/0005055](https://arxiv.org/abs/quant-ph/0005055) |
| Boyer–Brassard–Høyer–Tapp, *Tight Bounds on Quantum Searching*, v1 | **Read, targeted online:** §4, Lemma 2 and Theorem 3 through the zero-solution timeout paragraph; no whole-paper claim | [arXiv:quant-ph/9605034v1](https://arxiv.org/pdf/quant-ph/9605034v1) |
| Mande–Paraashar–Saurabh, *Randomized and Quantum Query Complexities of Finding a King in a Tournament*, FSTTCS 2023 | **Read, targeted:** introduction/overview, §4 sampling and quantum search, and most of the main theorem argument; not the entire proof or lower-bound development | [Publisher record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2023.30); supplied arXiv extraction |
| Ben-David, *A Super-Grover Separation between Randomized and Quantum Query Complexities* | **Read:** supplied main text, construction and both bounds | [arXiv:1506.08106](https://arxiv.org/abs/1506.08106) |
| Aaronson–Ben-David–Kothari, *Separations in Query Complexity Using Cheat Sheets*, arXiv v2 | **Read, targeted online:** §3.1 and §3.2 opening through the randomized composition theorem statement | [arXiv:1511.01937v2](https://arxiv.org/abs/1511.01937v2); [PDF](https://arxiv.org/pdf/1511.01937) |
| Aaronson–Ambainis, *Forrelation: A Problem That Optimally Separates Quantum from Classical Computing* | **Read, targeted online:** opening and §3.1–§3.2, Figure 1 caption and Proposition 6 proof; not the randomized lower-bound proof | [Author-hosted PDF](https://www.scottaaronson.com/papers/for.pdf); [arXiv:1411.5729](https://arxiv.org/abs/1411.5729) |
| Bansal–Sinha, *k-Forrelation Optimally Separates Quantum and Classical Query Complexity* | **Read, targeted:** supplied introduction, promise, quantum proposition, lower-bound result, applications, and opening of the k=3 overview; not the entire proof or §5.4 source dispute | [arXiv:2008.07003v3](https://arxiv.org/abs/2008.07003v3); supplied extraction and STOC edition available |
| Ben-David–Kothari, *Randomized Query Complexity Can Beat Certificate Complexity*, v1 | **Read:** supplied main text including §3 and Lemma 5; online primary abstract/HTML also checked | [arXiv:2609.15063v1](https://arxiv.org/abs/2609.15063v1) |
| Ambainis–Iraids–Kokainis, *Near-optimal Separations of Certificate Complexity from Randomized and Quantum Query Complexity* | **Read, targeted v2:** introduction, main-ideas overview and §6. **Skimmed v3:** primary version history and relevant §6.1 passages; no full v2–v3 comparison | [arXiv:2609.11664](https://arxiv.org/abs/2609.11664); [v3 HTML](https://arxiv.org/html/2609.11664v3) |
| Ronald de Wolf, *Quantum Computing: Lecture Notes*, v6, 27 August 2026 | **Read, targeted online:** Chapter 2 exercise 11 and Chapter 7 §§7.1–7.2, including the two-dimensional analysis and figure captions; not the 239-page notes as a whole | [Author-hosted PDF](https://homepages.cwi.nl/~rdewolf/qcnotes.pdf); [v6 record](https://arxiv.org/abs/1907.09415v6) |
| Pragya Arora–Udit Kumar, *Quantum Query Complexity of Tournament Solutions*, 29 October 2026 | **Skimmed only:** search-indexed abstract and metadata. Primary abstract, HTML and PDF bodies could not be retrieved. No proof comparison or novelty conclusion rests on it | [arXiv:2610.39702](https://arxiv.org/abs/2610.39702) |

The supplied source text is the basis of comparisons where a packet copy exists. Online research was also used to check recent related work and editions. No claim is made to have read Yao, Nisan or Barnum–Saks–Szegedy from the identifiers alone. Figure captions and the surrounding mathematical explanations were read; this comparison does not claim a visual inspection of the externally hosted PDF figures.

## 1. The original preprint: the decisive argument already has a clear order

OpenAI's §3 first states the amplification guarantee the application needs, then defines the comparison probabilities, proves drift for an ideal process, implements one pivot, couples histories, and verifies the returned list. The short sentence “The weights only define this ideal process” does valuable work: it prevents the reader from treating unknown probabilities as algorithmic input. The paper also explains why a later sampling failure cannot remove a previously listed winner. These are mathematical transitions, not administrative framing. [OpenAI, §§3.1–3.3](https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026).

The companions preserve this order and add useful specificity: the cyclic board, an explicit conditional sampler row, circuit-size dependence, numerical budgets and the separation of formal output laws. Their explanatory contribution should be judged by whether those additions remove a genuine inference burden. A specialist does not benefit merely from seeing the same theorem repeated with more constants. The record earns its length when it exposes a proof step that the preprint compresses; the exposition earns its length when a calculation lets a newcomer perform that step.

## 2. Minimum finding: algorithm first, cost contract visible

Dürr–Høyer place the search procedure and its time-out before the rank-based analysis. The maintained threshold is an actual table item, and a successful search replaces it with a smaller one. Their proof can analyze an ideal unbounded process while the delivered algorithm has a fixed time-out. Thus expected-cost analysis and a bounded-error algorithm with a cap can coexist; it would be inaccurate to present all previous minimum or unknown-success search as intrinsically incapable of a worst-case cap. [Dürr–Høyer, Theorem 1 and algorithm, pp. 1–2](https://arxiv.org/abs/quant-ph/9607014).

The relevant contrast here is the order structure, not merely the use of Grover search. Rank makes progress meaningful there. Complementary pairwise probabilities make total weight shrink here. Expert §1.3 correctly identifies the total-order premise. Exposition §4 would benefit from the same source's economy: state the actual candidate-generation loop before asking the reader to carry its probability analysis. Preserve the precise cap requirement, but do not let the proof of a convenient constant dominate the new search mechanism.

## 3. Search with bounded-error inputs: noise does not eliminate the underlying predicate

Høyer–Mosca–de Wolf specify fixed Boolean values and routines that compute each value with bounded error. Their problem is to search efficiently while avoiding the logarithmic penalty of naively suppressing every subroutine error. The paper develops a recurrence combining amplification and error reduction, and analyzes good and bad amplitudes with the work registers still part of the computation. [Høyer–Mosca–de Wolf, §§1 and 3](https://arxiv.org/abs/quant-ph/0304052).

That is the precise reason the theorem does not directly furnish the desired comparison oracle here. For a losing pair with probability one half, there is no intended Boolean orientation that this circuit computes with the required success gap. A probability arbitrarily close to one half likewise provides no uniform amplification cost for extracting an orientation. Current record §5.2 says this more precisely than the short phrase “bounded-error comparisons.” Keep that explanation. Also keep final verification conceptually separate: once an address is fixed, the local checks really are Boolean predicates. The reader should not leave believing that every stage tolerates arbitrary unreliability.

## 4. Amplitude amplification: the successful component is an object, not just a number

BHMT define a unitary preparation and a good subspace, then reduce the analysis to their two-dimensional span. That structure explains why changing the number of iterations changes the norm of the good component while preserving its normalized direction. Their unknown-success search theorem gives an expected-cost result; the manuscript's bounded trial schedule supplies the stronger all-branch guarantee needed at this call site. [BHMT, §2, Lemma 1 and Theorem 3](https://arxiv.org/abs/quant-ph/0005055).

BBHT already discuss an appropriate timeout in the zero-solution case at the end of §4, so capping itself should not be credited as the new idea. The relevant contribution here is the precise cap and output-law interface consumed by the weighted sampler. [BBHT, §4, end of Theorem 3 discussion](https://arxiv.org/pdf/quant-ph/9605034v1).

The companions do better than a casual invocation of amplitude amplification when they state the conditional output law explicitly. The record's distinction between a designated output subsystem and the whole enlarged workspace is also useful. The exposition can keep that insight with less trigonometric arithmetic: explain the invariant direction, the trial cap and the zero-success case, then return to the pivot distribution. The source comparison supports compression of routine proof detail, not deletion of the output-law hypothesis. Equal probabilities for one measurement remain insufficient to identify a quantum state for an arbitrary later continuation.

## 5. King finding: implicit candidates are the right analogy, fixed edges are the boundary

Mande–Paraashar–Saurabh make the obstacle to a naive quantum translation explicit: the algorithm cannot afford to enumerate the current candidate set. Their quantum section supplies a membership procedure and sampling subroutine for an implicitly represented set, then explains their costs. The graph has fixed tournament edges, and the target is a king, whose two-step reachability property differs from being an accepting certificate. [Mande–Paraashar–Saurabh, introduction and §4](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2023.30).

This is a useful writing model for the current proof. First say what representation makes an exponentially or linearly large set manageable; then explain how one sample is obtained. In the present construction the corresponding object is a product of comparison probabilities, sampled without computing that product numerically. The existing exact row after pivot 2 in the exposition is a strong step in that direction. It should be retained. A statement that comparisons may cycle teaches only one boundary; it does not yet explain the additional difficulty of fractional comparisons with no reliable fixed orientation.

## 6. The first super-Grover construction: each field of the input has a job

Ben-David's early note introduces the ingredients through the roles they will play: a cheap quantum promise problem, an AND/OR gadget with small certificates, and a large array whose address hides the useful certificate. The construction sketch is followed by a literal description of the input fields. The quantum algorithm then revisits those fields in the order in which it reads them. [Ben-David, “Constructing the Function” and “Quantum Upper Bound”](https://arxiv.org/abs/1506.08106).

That field-by-field correspondence is more instructive than a general metaphor about certificates. In the current manuscripts the outward pointer has an especially clear job: it disqualifies a rival without needing a meaningful address in that rival. The transcript has a different job: it makes the total predicate checkable at every address. Keep these purposes distinct. The restored credit for the first power-5/2 separation is appropriate and should remain. The early note's compressed error handling is not a model for an all-input, all-branch contract; a style comparator need not be adopted as a standard of proof detail in every respect.

## 7. Cheat sheets: retain the source's premise before compressing its formula

ABK's §3.1 proceeds from a failed attempt at totalization to the certificate problem, then to the gadget and hidden certificate array. Its phrase “hide the certificate somewhere in the input” makes the array's purpose concrete. It first assumes the promise function has very small quantum query complexity, then derives the cost of composition and certificate verification. [ABK, §3.1, printed pp. 9–10](https://arxiv.org/pdf/1511.01937).

This order exposes a local defect in expert §1.1: a general g is introduced before a display whose first quantum term has already specialized Q(g) to a polylogarithm. Move that assumption before the display, or keep the factor Q(g). The intended comparison with the cubic AND–OR recipe remains valid. Also qualify the framework claim quantitatively: a generic totalization construction does not promise that an arbitrary separation survives unchanged. The strongest historical comparison explains the cost being paid and the resource that the new construction saves; it need not imply a barrier for every conceivable use of cheat sheets.

## 8. Forrelation: a circuit makes the formula meaningful

Aaronson–Ambainis describe k-fold Forrelation through a circuit and its return amplitude, then give a controlled interference test with acceptance probability (1+Φ)/2 in Proposition 6. Their phrase “simulating the quantum circuit shown in Figure 1” connects the multilinear expression to an operation. [Aaronson–Ambainis, §3.2, Figure 1 and Proposition 6, printed pp. 13–14](https://www.scottaaronson.com/papers/for.pdf).

The current companion correctly distinguishes that test from the projection experiment with probability Φ². Retain this distinction and the one-sided promise. The fact that the selected projection loses the sign does not prove that quantum queries cannot reveal it. In teaching, the right local task is to follow the prepared vector, the phase operations and the final projection on one small input. The exposition already has unusually concrete tiny Forrelation data; it should reconnect that calculation to the decoder's output distribution when the algorithm later uses it. A matrix or circuit caption should name the register, observable and normalization it represents, rather than merely decorate the algebra.

## 9. Bansal–Sinha: start with the difficult case that explains the general proof

Bansal–Sinha specify the normalized matrix and one-sided promise before stating the quantum acceptance formula and classical lower bound. Their overview then narrows to “The case of $k=3$.” This is a deliberate reduction of cognitive load: the small case exposes the nonlinear obstruction the proof must overcome. Their quantitative statements also keep the advantage parameter visible before specializing to bounded error. [Bansal–Sinha, introduction, results and technique overview](https://arxiv.org/abs/2008.07003v3).

The long record's independent lower-bound reconstruction has a different purpose from the companion's use of hardness as an input. Keep that purpose explicit at the point where a reader can decide whether to enter it: uniform dependence on k and the explicit threshold are reasons; merely saying that a proof is complete is not enough. Do not reopen the already settled theorem-number issue by comparing arXiv numbering with STOC numbering as though they were the same edition. This review did not re-audit the record’s Appendix E criticism of Bansal–Sinha v3 §5.4, and makes no new claim about that disputed derivation.

## 10. The two September 2026 certificate papers: compare mechanisms, not only headlines

Ben-David–Kothari turn a large family of candidate claims into a fixed tournament using exact local tests, search it, and verify the selected candidate. Their sporting description is useful because the information kept on a card has an algorithmic role; the metaphor does not replace the representation. [Ben-David–Kothari, §3, Lemma 5](https://arxiv.org/abs/2609.15063v1). The current manuscripts should follow the same standard: every object introduced in an analogy should pay for a later operation. Also define the direction of a comparison locally; source and sink conventions differ across papers.

Ambainis–Iraids–Kokainis define a fixed graph and the set U(W) of candidates beating every selected pivot. They separate approximate edge evaluation, sampling, cost and error, and cap FindSource. The supplied v2 already contains this structure; the public record now lists v3. [AIK, §§6.1–6.3](https://arxiv.org/html/2609.11664v3).

This is the closest structural comparator for the weighted tournament. Boolean survival indicators become products of pairwise winning probabilities. That comparison should be shown once with enough precision to explain it, then used rather than repeated. The novelty claim concerns the permitted comparison behavior and its application to off-promise addresses. Neither the existence of a cap nor the abstract idea of keeping candidates that beat pivots should be represented as new here. Both papers compare certificate complexity with other measures; their headline exponents are not exponents separating R from Q in this construction.

## 11. Lecture-note pedagogy: test the operation that can silently fail

De Wolf's Chapter 7 begins with the search task, the oracle, the actual iterate and the measured output before developing the good/bad-plane analysis. Chapter 2 exercise 11 compares a clean phase query with one that leaves a copy of the queried index in workspace. The reader computes the changed output distribution. That is a particularly economical example of why apparently harmless workspace can alter interference. [De Wolf, Chapter 2 exercise 11, printed p. 21; Chapter 7 §§7.1–7.2, printed pp. 53–55](https://homepages.cwi.nl/~rdewolf/qcnotes.pdf).

The lesson for these drafts is to test the next operation, not recognition of terminology. Can the reader tell what happens if a register is measured too early? Can they distinguish the normalized successful component from a marginal label distribution? Can they calculate the next pivot from a given history? The current record's two-state counterexample and the exposition's sampler row already provide material for these checks. Use those existing objects before expanding the prerequisite list or adding a general lecture on quantum mechanics.

## 12. A fresh search result that should remain a lead

The online search found Arora–Kumar's *Quantum Query Complexity of Tournament Solutions*, dated 29 October 2026. Its indexed abstract concerns several solution concepts for tournaments. The primary body was not retrievable through the available research tool, so this review has not checked the oracle model, theorem hypotheses, proofs or relation to the present probabilistic-comparison model. [Discovery record](https://arxiv.org/abs/2610.39702).

If the authors pursue it, the first question is whether it assumes a fixed orientation or permits arbitrary comparison probabilities without a uniform correctness gap. Until that question is answered from the paper, it is a related-work lead. It supplies no basis here for claiming that the present theorem was anticipated, disproved or rendered unnecessary. This is also why a newer date should not automatically displace the carefully inspected September comparisons.

## A compact comparison the specialist reader should be able to reconstruct

| Procedure | Object supplied to the search | Progress object | What must be checked after search |
|---|---|---|---|
| Minimum finding | Values in a total order | Rank of the current threshold | Whether a search outcome actually improves the threshold |
| Search on bounded-error inputs | A fixed Boolean predicate, evaluated with a guaranteed gap | Good versus bad amplitude under error reduction | A measured candidate's validity |
| Fixed-tournament methods | Fixed edge directions, evaluated exactly or with controlled error | An implicit candidate set or graph property | The required graph property or certificate, according to the application |
| The present weighted tournament | A reversible pair circuit with complementary outcome probabilities | Total fractional weight; the dominant row retains weight | The full local certificate tests at a freshly decoded address |

This is a comparison of the passages read above, not a claim that every algorithm in a broad literature fits one row. In particular, a graph-theoretic winner, a dominant probabilistic row and a winning certificate are different predicates.

## What to change in these manuscripts, and what to preserve

**For the expert companion, give more space to the nearest comparison and less to routine constants.** The most valuable short explanation is the conversion from an implicit surviving set to fractional weights, together with the exact conditional sampling law. The opening contribution paragraph currently disperses attention across many additions. Its constants can move to the point where they control the theorem. Keep the earlier-recipe cost calculation, but place its assumptions before the display and describe the scope of the cubic limitation carefully.

**For the exposition, keep one board but let it answer successive operational questions.** The current cycle, dominating nonwinner and worked sampler row have distinct, useful roles. Preserve them. Explain which feature remains untested by the deterministic board and choose one small fractional comparison calculation if needed. The numerical proof of a uniform 9/40 trial success rate is a weaker use of space than explaining what is fixed in a stage, why the conditional law survives amplification, and why verification is still required. The reader should be able to narrate the algorithm between measurements.

**For the record, keep the difficult distinctions while reducing repeated orientation.** The fixed-oracle conditional law, the common-history coupling and the designated output subsystem deserve their present care. The many local recalls can be edited according to a reader arriving at that precise proof entry. Correct the return pointers by checking where the named argument actually lives. A valid anchor with the wrong section label is not a successful reading route.

**For credit, retain the division of labor already repaired.** The theorem and the two analyses belong to the original preprint; the companions supply explanation, reconstruction, constants and formal correspondence. Earlier results deserve local attribution when their mechanism is used. The direct-product alternative, the exactness of local checks and the choice of explicit Walsh–Hadamard Forrelation are mathematical comparisons. Dates, receipt histories and declarations of review belong elsewhere unless they affect a reader's immediate inference.

The writing target is a reader who understands the mechanism well enough to identify an assumption, vary a case and recover an omitted proof. The literature provides good models for that goal, but the strongest improvements will come from testing those operations in these particular drafts.


## Supplied exemplars: useful local comparisons, not a universal house style

The three exemplars concern another theorem and serve different readers. They were sampled at their openings, not audited in full. Their value here is to test the method against a concrete alternative organization, not to infer mathematical authority from having been produced by the same workflow. The source scopes are LEAD-S04–LEAD-S06 in `feedback.json`.

The short-paper exemplar, `exemplars/short-paper.md` (opening and initial setup, approximately lines 1–145), quickly connects its result to one recurring inequality, states the normalization the argument will use, and gives local credit for the inherited formula. That is a useful comparison for the expert companion’s crowded contribution paragraph: the reader needs to know the move that drives the argument before learning every constant and ancillary result. The exemplar’s abstract is itself dense, so its mere presence is not a reason to reproduce its density. The transferable choice is to make the mechanism and the exact normalization usable before enlarging the dependency map.

The expository exemplar, `exemplars/expository.md` (opening, §1 and the early two-spin example), promises only elementary prerequisites, explains the probability objects it actually consumes, and puts a small calculation near their first use. That supports a concrete criticism of the quartic exposition: a fixed newcomer audience cannot be satisfied by adding a prerequisite paragraph that requires a quantum-query course. The relevant analogue is a short calculation of what the oracle, phase operation or success measurement does on the displayed input. It is not an instruction to import the SK paper’s subject matter or to insert a general textbook chapter.

The long-record exemplar, `exemplars/long-reasoning-record.md` (opening target map and initial setup, approximately lines 1–100), distinguishes its central theorem from neighboring consequences and gives routes according to the reader’s objective. The quartic record already does this substantially better after the previous round. Preserve that repair. Its remaining task is more specific: allow a quantum specialist to use the amplifier contract, reach the weighted drift, and recover the full state proof when needed. A route must name the current destination correctly; a technically valid link with an obsolete section number does not provide the same service.

Across all three, the useful test is local: what does this paragraph enable the reader to do next? This yields a stronger revision criterion than matching a corpus-wide frequency of first-person pronouns, semicolons, questions or negative constructions. The method findings explain how to make that criterion govern the existing rules without proliferating another checklist.
