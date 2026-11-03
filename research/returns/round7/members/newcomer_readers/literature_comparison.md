# Literature comparison: teaching the quartic separation

## Scope and reading standard

This comparison concerns how the supplied sources explain their mathematics and what the current three documents can learn from them. It does not reassess the full proofs of the cited research results. “Read” below means the stated passages were read closely; it does not mean that every page of a long source was audited. The reader perspectives are simulations of backgrounds, not opinions attributed to any of the authors. Current-document references are to the Markdown in the packet. The supplied exposition PDF has 15 pages, the expert companion has 14, and the long record's 131-page PDF represents an earlier Markdown edition, as the packet itself explains.

The most useful comparison is a specific explanatory move at the same point in a reader's journey. A research-paper introduction is evidence for positioning a result. A lecture-note treatment is evidence for introducing an operation. Neither establishes that a novice has understood the revised text. The local recommendations here are editorial judgments grounded in those comparisons.

## 1. Establish the task before formalising its cost

### Buhrman and de Wolf: why study decision trees?

The supplied 2002 survey begins with the difficulty of proving computational lower bounds, explains the value of a simpler model, then introduces decision trees and the measures being compared. Its opening gives a reason to care about query complexity before asking the reader to master the notation. Section 3 separates deterministic, randomized and quantum models. This is especially relevant to the mathematician who has never used an oracle model and to the undergraduate whose prior notion of complexity is running time.

The exposition currently introduces the bit oracle in its first paragraph and the infimum defining the optimal exponent in its second. These are accurate mathematical objects, but they arrive before an example of the resource being counted. The phrase “we charge only for the bits it reads” can also be read as a charge for distinct positions. A beginner needs to know that an oracle call is one query, that repeated calls count again, that input-independent calculation is free in this model, and that the function being computed is fixed while its input is unknown.

A compact task such as OR on four hidden bits can support these distinctions without becoming a preliminary chapter. Show what one query returns, why an algorithm may adapt its next position, and where its random coins enter. Then state the quantum search cost as a usable input or teach its essential operation. The opportunity is to replace some of the current introductory compression, not to prepend several pages.

Source: Buhrman–de Wolf, *Complexity measures and decision tree complexity: a survey*, TCS 288 (2002), §§1 and 3; supplied author PDF and extraction. The extraction visibly loses some letters, so it should not be copied as polished prose or treated as a clean corpus sample. [DOI](https://doi.org/10.1016/S0304-3975(01)00144-X).

### Ben-David's query-complexity notes: an operational prerequisite ladder

The newly retrieved *Query Complexity Basics* begins with a black box and a known property of its unknown input, uses OR, defines decision-tree height, then introduces randomness. It explains Dirac notation before writing a quantum oracle. This sequence supplies concrete operations before the compact model. Its usefulness here is the order, not a requirement to reproduce all the preliminaries. The exposition could borrow the task-to-model sequence while keeping its main construction central.

Read scope: §§1.1–1.2 and the beginning of the quantum model, PDF pp.1–5. [Ben-David, CS867/QIC890 notes (2022)](https://cs.uwaterloo.ca/~s4bendav/files/CS867QIC890S22QueryBasics.pdf).

Hamoudi's introductory notes make a useful audience distinction: their opening assumes basic quantum computing, including the circuit model and Dirac notation, while introducing query complexity. That is close to the physicist's starting point, but above the undergraduate's and the no-quantum mathematician's. A source can be introductory in one subject while assuming another. The packet's prerequisite paragraph should be judged against its actual readers, not simply against the word “introduction” in a bibliography. Read scope: introduction and organisation, pp.1–2. [Hamoudi, *A Brief Introduction to Quantum Query Complexity*, updated 24 April 2026](https://yassine-hamoudi.github.io/files/publications/QueryComplexity.pdf).

### Why the model deserves one sentence of motivation

Aaronson's *Open Problems Related to Quantum Query Complexity* motivates the model through algorithms it captures and lower bounds it allows. The important comparison is that its opening tells readers what the model lets researchers establish. Its §4 is also a useful historical account of the gap between known exponents before the 2026 preprint. It must be read as a dated source, not as a statement that the same question is still open.

Read scope: introduction and §4. [Author PDF](https://www.scottaaronson.com/papers/open.pdf), [journal DOI](https://doi.org/10.1145/3488559).

For this exposition, one sentence explaining that query complexity isolates the information an algorithm must obtain would give the formal comparison a purpose. It should also make clear that the theorem compares input queries; it does not by itself establish a practical wall-clock speedup. That distinction matters particularly to the physicist or engineer.

## 2. Forrelation: give the transform a question to answer

### Aaronson–Ambainis: a relation between two sign patterns

The Forrelation paper's abstract describes deciding whether a function is “highly correlated with the Fourier transform of a second function.” This 10-word phrase supplies the mathematical relationship before the formula. The introduction then positions that relationship within the question of maximal quantum versus classical query separation. Later, the paper describes the circuit and distinguishes a direct amplitude calculation from more economical interference-based algorithms.

The present exposition's geometric paragraph is one of its strongest passages. The vectors $z_1/2$ and $Hz_2/2$ have an interpretable inner product, and the positive, orthogonal and negative examples make the asymmetric promise tangible. That paragraph should survive every revision. Its position could improve: a short statement that the task asks whether one sign pattern aligns with the transformed other pattern would help readers interpret the matrix at first sight.

The packet's use of a two-query projection experiment at $k=2$ is compatible with the one-query algorithm often advertised for Forrelation: they are different experiments, and optimal query use is unnecessary here. The newcomer should not have to discover this distinction by comparing bibliographic abstracts. The companion already explains the alternative acceptance law $(1+\Phi)/2$; the exposition needs only a brief clarification if it invokes the one-query literature in its history.

Source: Aaronson–Ambainis, *Forrelation: A Problem that Optimally Separates Quantum from Classical Computing*, supplied arXiv:1411.5729v1, introduction and circuit/projection discussion, especially the discussion around Proposition 6. Read scope: those passages; the full lower-bound proof was not re-audited. [arXiv](https://arxiv.org/abs/1411.5729).

### Bansal–Sinha: visually distinguish promise cases and query actions

The supplied QIP 2021 slides place the two promise cases side by side and connect the matrix expression to a circuit picture. Their comparison of total and partial functions is visually immediate. The quantum-versus-classical table shows what is being separated before the analytic proof machinery appears.

This suggests a small improvement to §1: mark the positive interval, the near-zero interval and the unpromised region together, including the large negative values. The current numerical examples already contain the necessary information, so a simple display or a more deliberately ordered explanation could do the job. The slides' circuit strip is another useful precedent for connecting “apply the signs,” “apply $H$” and “project” to a sequence of operations. The actual thresholds in the manuscript must remain its own; illustrative slide thresholds should not be imported as if identical.

The slides also make a $k=1000$ example of an exponent close to one. For the present total-function argument, a short table for $k=2,3,4,5$ would clarify what $4-2/k$ means, provided it separates a limiting critical exponent from a universal bound at the endpoint. Question 4 currently fails to keep precisely that distinction.

Source: Bansal–Sinha, QIP 2021 slides, opening model comparison, two-fold and $k$-fold Forrelation slides, result and consequence slides; supplied PDF and extraction. Read scope: opening and result sequence; later analytic slides sampled. Related paper: [arXiv:2008.07003](https://arxiv.org/abs/2008.07003).

### An additional broad-science comparison

Aaronson's 2022 Solvay account explains the difference between query access and full circuit cost and introduces Forrelation through a relation between two functions and a Fourier transform. Its value here is the entry point for a scientist who knows some quantum mechanics. It does not supply the present total-function construction or its proof. Its dated discussion of the exponent gap should remain historical.

Read scope: §2 on the query model and §6's Forrelation discussion; other portions skimmed. [*How Much Structure Is Needed for Huge Quantum Speedups?*](https://www.scottaaronson.com/papers/aarsolvay.pdf).

## 3. Totalisation: explain why the tempting simple extension fails

### Cheat sheets introduce each ingredient as a response to an obstruction

Aaronson, Ben-David and Kothari's overview and §3.1 ask how to turn a partial function into a total one. They first consider extending the value by zero outside the promise and explain the missing capability: the cheap quantum algorithm would now have to decide promise membership. They introduce certification, then the need to hide the certificate, then several hard answers to make a sufficiently long address. This is a sequence of problems and repairs, not an inventory of data fields.

The current exposition contains the ingredients and correctly credits them, but the general column layout appears before the newcomer has a firm distinction between computing a partial value and certifying that the input lies in the promise. The $a^-$ example is the ideal bridge. Its projection behaves like the positive example while its exact domain bit is zero. Make that obstruction do the explanatory work before asking the reader to hold $X_i$, $A_{i,h}$, $B_{i,s}$, transcripts and pointers at once.

The ABK overview says, “we hide a "cheat sheet" in the input”; the local point is that the certificate is part of the input, under the algorithm's query access. In this manuscript, it is especially useful to explain that storing a transcript does not give the algorithm trusted advice. All assignments to those bits are allowed, and the winning condition rejects wrong transcripts. The argument by induction along the gates explains why checking local equations certifies the full evaluation. A small two-gate illustration would be more informative to a newcomer than the unexplained provenance of the 180-gate count.

The history of the cubic construction also needs the cost of verifying the certificate. In ABK §3.1, the competing quantum costs are $\widetilde O(m'+\sqrt{nm'})$, and the chosen balance is $m'=n$. The expert companion includes this. The exposition's compressed explanation of where the cube comes from can sound as though AND-OR contributes a simple factor while the certificate's cost is irrelevant. A small comparison of the old recipe's two costs with the new tournament's costs would be more instructive than adding another paragraph of chronology.

Source: Aaronson–Ben-David–Kothari, *Separations in query complexity using cheat sheets*, supplied arXiv:1511.01937v2, introduction, “Overview of techniques,” §3.1, the opening of §3.2 and their definition of critical exponent. These passages were read closely; later separations were not reviewed in full. [arXiv](https://arxiv.org/abs/1511.01937).

### Preserve the distinction between a recipe and a framework

The companion's AND-OR calculation explains the bottleneck of that specified construction. It does not establish an impossibility theorem for everything called a cheat sheet. This is an instance where a negative historical sentence needs the same quantifier care as a positive theorem. The exposition can describe why the earlier recipe gave a cubic exponent while crediting the addressed-certificate idea that the present construction retains.

The predecessor story is now substantially better than a list of uncredited exponents. Keep the separate roles of pointer functions, cheat sheets, Forrelation hardness, comparison search and the known universal upper bound. Do not remove a three-author citation or a necessary list of three inputs because a detector flags its cadence.

## 4. Quantum search: teach the invariant before the trial constants

### Grover's original paper begins with a task

Grover opens with an unordered phone directory: “Imagine a phone directory containing N names arranged in completely random order.” The first effect is to make the search task and the classical cost recognisable. The manuscript should borrow that concreteness, without importing database language that suggests that loading an input or implementing its oracle is free in a physical machine.

In the quartic construction, the analogous first task is not “run Grover.” It is “find a column worth checking without paying to verify every column.” Section 4 already states the nested-search cost $\sqrt m\sqrt K\approx m$. Keep this failed first attempt; it motivates the tournament more efficiently than another historical aside. Then distinguish the cheap comparison from the expensive verification, and show why outgoing pointers protect a true winner against an unpromised rival.

Source: Grover, *A fast quantum mechanical algorithm for database search*, STOC 1996, summary and §§1–3; opening and algorithm description sampled. The supplied extraction is two-column text and loses mathematical layout. [arXiv:quant-ph/9605043](https://arxiv.org/abs/quant-ph/9605043).

### De Wolf: the two-dimensional geometry carries the explanation

Chapter 7 of de Wolf's supplied lecture notes starts with the search problem, identifies good and bad states, and expresses the initial state in their two-dimensional span. It then explains the two reflections, shows their effect geometrically, and derives the sine formula. The amplitude-amplification section reuses that same construction for a general preparation and explains why its inverse is needed. The sentence “The analysis is the same as for Grover” works because the necessary operation has already been taught.

The present exposition starts its amplification paragraph with $p=\sin^2\theta$ and a normalized successful state $g$, then spends much of the paragraph on $19/40$, $9/40$ and an exact trial count. A reader who does not know the geometry cannot infer the operation from those constants. Conversely, a reader who already knows amplitude amplification is unlikely to need all the arithmetic in the main teaching route.

The distinctive fact used by this paper is that amplification changes the total successful mass while preserving the relative distribution of successful column labels. The successful vector includes the label and every retained comparison workspace; the label marginal alone need not be pure. Explain that invariant with the two-dimensional picture or a small vector calculation; state the bounded-cap routine as an imported contract with an exact proof destination. Preserve its all-input cap and the $p=0$ case, because totality makes them necessary. Moving numerical derivation out of the main route does not justify dropping the contract.

The current sampler example correctly computes joint masses, their sum, the conditional label law and the next measured pivot. That is a real improvement over a formula with no worked operation. It should stay. Its $p=1/2$ stage is a case where Grover iterations do not change the success probability. Question 2 then supplies the $p=1/4$ case where one iteration succeeds certainly. Explain what each case teaches; do not let readers interpret the first as the typical speedup mechanism.

Source: de Wolf, *Quantum computing: lecture notes*, supplied arXiv:1907.09415v6, chapter 7, especially §§7.1–7.3 and Figures 7.1–7.2; those sections read closely. Elementary state, measurement and query-model passages were consulted selectively. [arXiv](https://arxiv.org/abs/1907.09415).

Watrous's IBM Quantum Learning pages provide a compact independent comparison: the query-model page separates the abstract access cost from implementing an oracle, while the Grover analysis develops the good/bad plane and reflection geometry. Both substantive page texts were read in full; videos were not watched, and diagram descriptions were read without a separate pixel inspection. [Query model](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/quantum-query-algorithms/query-model-of-computation); [Grover analysis](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/grover-algorithm/analysis).

Brassard, Høyer, Mosca and Tapp's §2 gives the standard invariant-subspace formulation behind amplitude amplification. It supports the whole-preparation-state interpretation above. It should not be used to replace the packet's specific proof of a bounded cap and exact conditional label law. Read scope: abstract/introduction and §2 around Lemma 1 and equations (1)–(8), approximately PDF pp.5–7; remainder not read in full. [arXiv:quant-ph/0005055v1](https://arxiv.org/abs/quant-ph/0005055v1).

### Physical resources and query resources

Childs's notes explicitly choose a more prepared graduate audience and organise query complexity as a later topic. Their preface is a useful reminder that a declared prerequisite is a real scope choice. They should not be cited as evidence that an untrained reader already knows the necessary operations. The present packet fixes a less prepared audience, so its exposition must supply a shorter entry or clearly identify a usable imported result.

Read scope: preface and chapter-21 model discussion sampled. [Childs, *Lecture Notes on Quantum Algorithms*, 17 April 2025](https://www.cs.umd.edu/~amchilds/qa/qa.pdf).

## 5. The lower bound: give the predictor a visible input and output

The current planted-pair figure earns its space: it isolates the two possible locations of the first difference. The early/late zero argument then has an interpretable quantity, $Z$, and an exact use of the independent uniform column $I$. The counterexample distinguishing a uniform marginal from independence is also valuable. These are places where the exposition does better for a newcomer than the compressed preprint.

The largest remaining transition is the simulator. The text correctly separates the global cap $G$, the total forwarded cap $L$, and the per-instance cap allowed by the direct product. It also correctly bounds a joint event instead of conditioning on lightness. Neither point should be reported as absent. The remaining issue is that the reader never sees a small query trace turn into a predicted address on the main route. The record has an appropriate XOR example, but the link changes the input problem and indexing. That reset is acknowledged; a short visible trace would let the reader actually use the reduction.

The direct-product proof is better motivated if the reader first knows why success means guessing every address bit. The existing AND calculation shows that the conditional product may rise on one branch but has nonincreasing expectation. Preserve it. The phrase “condition on the whole transcript” in the erased-zero paragraph should instead refer to the observed prefix at the time of the next query; the record's version already does this. This is a repair of the explanation of an existing proof, not a new lower-bound argument.

ABK's §3.2 gives a useful nearby model of explanatory practice: it defines the simulated input, identifies the queries that require real information, and relates their count back to the desired measure. The lesson is to show a reduction as an operation with a source instance, a simulated run and an output. The present manuscript can do that using its already supplied example.

The current companion §4.1 credits Drucker’s *Improved Direct Product Theorems for Randomized Query Complexity* (2012, doi:10.1007/s00037-012-0043-7) and Shaltiel’s *Towards Proving Strong Direct Product Theorems* (2003, Computational Complexity 12:1–22) for different roles. Those bibliographic details come from the supplied bibliography; neither original paper was read in this pass. This return does not claim to have read the cited-only Yao paper or to have reconstructed the full literature of direct products. Where a specialist attribution is only supported by the supplied record and its bibliography, that boundary is retained in the source register.

The two-page PCMI worksheet by Hamoudi, with teaching assistant Pelecanos, supplies a useful exercise comparison. It asks learners to establish a phase-query equivalence and construct a small parity algorithm, requiring an operation and a transfer to another case. The local lesson is to test the promised inference, not to copy its difficulty level. In the quartic exposition, one existing question could instead ask for the capped simulator's output and the event that guarantees its correctness. Read scope: entire worksheet. [PCMI 2023, Problem Session 1](https://yassine-hamoudi.github.io/files/pcmi2023/Problems1.pdf).

## 6. The exponent: distinguish an infimum from its endpoint

The definition of critical exponent in ABK's preliminaries explicitly treats an infimum of universal powers. That framing is useful here because a logarithmic loss can leave an endpoint undecided while every strictly smaller exponent is excluded.

The current exposition gets the principal order of choices right: choose the proposed universal power, choose one fixed $k$, then let $m$ grow. Its $t\ge2^k$ counterexample is a concise way to show why a fixed-parameter threshold cannot be used with an arbitrary growing schedule. Keep both.

Question 4, however, asks which $k$ shows $\alpha_{\mathrm{tot}}\ge3.5$, while the answer rejects $k=4$ because it does not yield a positive gap at $\alpha=3.5$. With $k=4$, every $\alpha<3.5$ still gives $2-1/4-\alpha/2>0$, which is enough to prove that the infimum is at least $3.5$. Choosing $k=5$ serves the stronger target of excluding the endpoint universal power $3.5$ itself. The intended exercise can be repaired by naming that stronger target. This is a narrow question-answer error; it does not refute the main theorem or its proof.

SSW's introduction distinguishes fixed-parameter constant-query statements from slow-growing-parameter statements. That is a useful precedent for separating two quantifier patterns rather than compressing them into $o(1)$ notation too early. The expert companion's growing-$k$ remark belongs as a refinement after the fixed-$k$ proof, with its source made clear; the newcomer exposition need not teach that refinement to explain the optimal exponent.

Source: Sherstov–Storozhenko–Wu, *An optimal separation of randomized and quantum query complexity*, supplied arXiv:2008.10223v4, introduction's partial-function results and total-function consequence; read in those sections; the later Fourier-growth proof was not reviewed in this pass. [arXiv](https://arxiv.org/abs/2008.10223). Their random-orthogonal Rorrelation formulation is not literally the explicit Walsh promise used by the present construction. The current companion states that distinction and should keep it.

## 7. What the other-domain exemplars actually demonstrate

The supplied SK exposition opens with a concrete optimisation problem, a two-spin example, and then the probability operations required for its later argument. It states the deeper analytic inputs where the proof consumes them. Its useful transferable move is to connect a familiar finite calculation to the eventual inference. Its exact section order, length and choice of physical story are local to that theorem.

The quartic exposition already has an analogous finite object in the four-column board. Its strongest moments are where the reader can act on that object: follow a pointer, inspect a failed domain bit, or update the candidate weights. It is weaker when it names a large general construction, a circuit-size estimate or a trial bound before giving the reader an operation that needs it. The remedy is to improve those transitions, not to imitate the SK paper's vocabulary.

The SK short paper's opening connects the result to its decisive contradiction and distinguishes the prior theorem from its reconstruction. This is a useful comparison for the companion's first section. The current companion credits OpenAI clearly, but its list of explicit constants and accompanying artifacts competes with the new comparison mechanism. The paper's contribution should be assessable without the reader first deciding how much to value $13669k^2$ or $2^{53}k2^{10k}$.

Read scope: supplied SK exposition opening and §§1–2, main proof-route headings and selected payoff sections; supplied short-paper opening and main-result section; long exemplar guide and organisation sampled. These were used as writing examples, not as independent verification of the SK mathematics. Sources are the packet's `exemplars/expository.md`, `exemplars/short-paper.md`, and `exemplars/long-reasoning-record.md`.

## 8. Implications for the register stage

The measurement correctly points toward long introductory paragraphs and concentrated numerical detail. It also produces flags that should not become edits. Three-author credits are not empty three-part rhetoric. Necessary negations explain nonexistence and counterexamples. Formal terminology in a designated audit appendix is expected. A sentence can be near the corpus median in length and still ask a newcomer to learn several concepts at once.

The 42-document reference profile mixes research papers, lecture notes and slides. Some extracted text is damaged. Those facts limit what the paragraph and cadence comparisons can establish. Keep the broad profile as context, use a genre-matched subset for a local comparison, and judge the mathematical role of every flagged sentence. The supplied rule package also contains 17 active rules while its documentation describes 26; several rule IDs referenced by the measurement have no operative text in the package, even when an ID occurs in historical metadata. That is a packaging correction for the method, with no reason to add discussion of it to the papers.

The most effective next pass would spend less space on repeated quantitative assurance and more on three operations: making one query, turning a noisy comparison history into a weighted candidate, and turning a cell query into an address predictor. The existing arguments, examples and sources already contain the material needed. The task is to make the reader's route through them work.
