# Literature comparison

Primary sources were used to compare exact premises and explanatory moves. The source register conservatively marks partially read external papers as skimmed, while specifying the sections read closely. The comparison does not claim an exhaustive novelty search or independent audits of every external theorem. Source quotations are short; the input packet’s original papers are not redistributed here. Repeated specialist observations about the same source are consolidated.

## Literature comparisons for the specialist companion

These comparisons use the supplied texts at the stated scopes. They are not claims to have checked all proofs in every cited paper. The current companion and matching record §6 were read in full; the external papers were sampled at the relevant introductions, theorem statements and proof passages. Online additions are listed separately. Quoted outside passages are deliberately short.

### Drucker: show the object that tracks adaptive progress

Source: Andrew Drucker, *Improved Direct Product Theorems for Randomized Query Complexity*, arXiv:1005.0644v2, §§1.1–1.3 and §3, especially Lemmas 3.1–3.2 and the final fair-algorithm paragraph. [Primary paper](https://arxiv.org/abs/1005.0644v2). I read these passages closely in the supplied extracted text; I did not audit the later threshold, learning, search, or dynamic-interaction results.

Drucker's methodological overview gives the reader an interpretation of the potential before presenting the proof. The phrase **“winning prospects”** in §3 identifies the role of the best continuation probability; it is a prediction of achievable success with the remaining budget, not the algorithm's actual conditional success. The next key move is local: only one fortune changes at a query, while the other factors are fixed by the transcript. That ordering is useful because it explains why the product is controlled under adaptive interleaving.

The companion's unnormalized proof is shorter and, for this purpose, cleaner about zero-mass branches. It should keep that advantage. Its weaker point is the phrase “the recursion absorbs its two branches,” which hides the common-factor algebra. One explicit line would convey the same insight as Drucker's fuller discussion without importing his whole proof.

The source comparison also confirms the current credit correction. Drucker's Theorem 1.1 is a global-budget theorem, but it is not unusable here. Its specialization gives 2β^r at the simulator's total allowance L, and the companion's slack absorbs that factor. The short separate-cap proof remains a good editorial choice because it gives β^r exactly and can be explained locally. The choice is simplicity, not mathematical necessity.

### Shaltiel: precise hypotheses before the induction

Source: Ronen Shaltiel, *Towards Proving Strong Direct Product Theorems*, ECCC TR01-009, §5, Definition 4, Theorem 5 and Lemma 7, printed pp. 11–12; also the introduction's fair-algorithm discussion. [Primary report page](https://eccc.weizmann.ac.il/eccc-reports/2001/TR01-009/index.html). The fair-tree proof was read; other computational models were only sampled in the introduction.

Definition 4 states its restriction **“on every path from root to leaf.”** This is a concise model for placing the budget quantifier where no reader can miss it. The proof then strengthens the induction to separate functions and separate allowances. The companion similarly benefits from stating joint independence and per-branch caps in the lemma rather than discovering those requirements during the proof.

The current companion is more careful than some secondary descriptions of the history: it says Shaltiel's result concerns XOR advantage in the uniform-input setting. That qualification matters. The present vector-output result under μ is explained through the supplied proof and Drucker's specialization. Keep this precision; do not collapse the sources into one unnamed “standard DPT.”

### Cheat sheets: motivation before exponent arithmetic

Source: Scott Aaronson, Shalev Ben-David and Robin Kothari, *Separations in Query Complexity Using Cheat Sheets*, arXiv:1511.01937v2, §3.1 Intuition and §3.2 Implementation, including the blank-array argument. [Primary paper](https://arxiv.org/abs/1511.01937v2). These sections were read closely; the rest of the paper was not audited.

ABK motivate the construction by considering the obvious failed extension of a partial function to a total one, then identifying the difficulty of certifying the promise. Their short pivot **“hide the certificate somewhere in the input”** occurs only after the cost of evaluating and checking the composed function is understood. The array address is then a response to a concrete obstruction, rather than an object introduced for later use.

The companion's historical conversion is now mathematically informative, but it can recover one causal link from that exposition. AND–OR is useful because small certificates of all inner outputs certify the outer promise; this explains the √(nm′) verification cost. State the assumption on Q(g) before the displayed cost. The present calculation can then remain short while showing why the old recipe reaches the cube.

The blank-array comparison also explains a likely specialist pause in §4.2. ABK explicitly arrange that a blank cheat sheet is invalid. Here the dummy input is zero already because no X_i is all ones. A short local reason is enough to distinguish the two support arguments. It is unnecessary to import the old sentinel-bit device into the new construction.

### Pointer functions: distinguish the highlighted witness from arbitrary cells

Source: Andris Ambainis, Kaspars Balodis, Aleksandrs Belovs, Troy Lee, Miklos Santha and Juris Smotrovs, *Separations in Query Complexity Based on Pointer Functions*, arXiv:1506.04719v3, §1.3 and §3's definition of f_{n,m}. [Primary paper](https://arxiv.org/abs/1506.04719v3). I read the mechanism overview and the relevant function definition; I did not audit all subsequent algorithms and lower bounds.

The source repeatedly says **“each highlighted zero”** when describing the required return pointer. That adjective cannot be dropped. The highlighted leaf in each nonmarked column points back to the marked column; arbitrary other zeros can carry other destinations. The source's algorithm accordingly forms a set of candidate back-pointer destinations and reasons about that set. The companion's “each zero” sentence is a genuine local misdescription.

The supplied pointer paper also motivates a balanced tree through access cost: a distant witness on a long path is expensive to reach, while a leaf of a balanced tree can be addressed in logarithmically many steps. This is the relevant predecessor contrast for the new direct pointer fields. The current companion now correctly explains that a pairwise comparison reads only the one field aimed at its rival, while verification searches the collection of local tests. Keep that argument; merely saying that binary encoding avoids a large alphabet would not explain the cost.

### The source preprint: a cleaner end to the classical proof

Source: supplied OpenAI preprint, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, dated 5 October 2026, §§1, 4 and 5. This is packet content, not a newly retrieved public edition. I read these sections closely and used the supplied PDF/extracted text as the source boundary.

The source preprint's §4 first identifies the two discovery events and ends by naming the roles of the heavy-column estimate and the independent-answer estimate. It explicitly qualifies conditional uniformity by saying it holds before a column's zero is found. It also explains that counting every visit to the selected cell is only an upper bound on observing a changed bit. Those short qualifications survive naturally inside an otherwise compact proof.

The companion improves on the source by making several later checks explicit: one fixed circuit for both bounds, an exact direct-product proof avoiding zero-probability conditioning, a comparison with Drucker's global theorem, and concrete shortcut failures. It should not pay for those additions by deleting the source's brief qualifications at the first-difference and first-discovery steps. Those clauses are more valuable than the optional improved erased-zero constant.

### Ben-David–Blais 2025: current context, not a required substitute

Online source: Shalev Ben-David and Eric Blais, *Direct Product Theorems for Randomized Query Complexity*, FOCS 2025, [arXiv:2512.08268v1](https://arxiv.org/html/2512.08268v1). Sampled: introduction, definition preceding Theorem 1, Theorem 2 and the discussion of discounted score. Its maximum-distributional measure uses expected cost and averaged success before maximizing over input laws. This differs from the companion's fixed-law hard-cap premise. A brief related-work citation would update the context; no replacement proof is needed. The paper also motivates its potential by the different additive and multiplicative behavior of cost and success, a useful example of explaining a technical definition through the task it must perform.

### BHMT: name the cited algorithm rather than a universal limitation

Online source: Brassard, Høyer, Mosca and Tapp, *Quantum Amplitude Amplification and Estimation*, [quant-ph/0005055](https://arxiv.org/pdf/quant-ph/0005055), §2, Theorem 3 and the associated QSearch procedure, printed pp. 8–10. Sampled only. The theorem gives an expected-cost guarantee and runs indefinitely at zero success probability. The companion should attach its expectation-only description to that procedure; its own fixed-cap threshold wrapper is a different guarantee. This is a wording repair, not an objection to the amplification proof.

### What the comparison suggests about register

The best common feature of these papers is the order in which they explain a device: name the obstruction, state the desired interface, then introduce the potential or construction that meets it. This does not require every paragraph to be short. Drucker's potential and ABK's domain-certification motivation earn explanatory space. In the companion, the capped simulator and the off-promise acceptance comparison deserve that space more than unused constants. Register statistics that count words or list items will not recognize this distinction unless the drafting method first identifies the mathematical step each paragraph is supposed to carry.


### Additional comparisons: the Fourier supplier and explanatory design

#### OpenAI's source preprint and the role of the reconstruction

The supplied 5 October 2026 preprint was read through §§1–5 and Appendix A. Its §4.2 states the simulator for a fixed column and a fixed query time, aborts before query L+1 to the target tuple, and then unions over times and averages over the independent selected column. This is the standard against which the current record's opening summary was checked. The source proof says “does not condition the input distribution on a column being nonheavy” (p.13, before equation (21)). The current detailed proofs retain that distinction. The opening sentence in the record does not retain the fixed-time qualifier or the all-time G factor. That is a local misstatement in the reconstruction, not a defect discovered in the source proof. Source: supplied paper/extracted.md, §4.2, pp.12–13; [public source repository](https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026).

The source also gives a useful allocation model. It states the Forrelation contract, proves the circuit-size claim and gives the complete planted reduction. The record appropriately expands what the source imports. The companion should use that added depth to explain the delicate transitions, rather than give routine numerical bookkeeping more space than the off-promise bridge.

#### Bansal–Sinha: compare the promise before comparing the exponent

The arXiv v3 introduction, Theorem 1.3, Corollary 1.4 and the displayed substitution in §5.4 were inspected online. The source concerns the explicit Walsh k-Forrelation promise and uses a positive yes threshold. It is the appropriate published supplier for the fixed-k interface. The record's altered truncation and interpolation therefore require their own moment and derivative identities; they cannot inherit the source's distribution-specific promise-mass conclusion by name alone. The current record makes that distinction. Its version-specific logarithmic criticism is explicitly bounded and should stay bounded. Source: [arXiv:2008.07003v3](https://arxiv.org/html/2008.07003v3), equations (1.1)–(1.3), Theorem 1.3 and §5.4.

#### Girish–Tal–Wu: make the low-degree process visible

The ordinary-tree overview in §1.3 and Lemma 1.9 were read online; the parity-tree paper as a whole was not audited. Its discussion motivates degree induction through revealed-coordinate processes and explains why stopping is needed when a future good event would bias increments. This is the relevant antecedent for record §3.11. A small r=2 update would make the record's contracted-array mechanism easier to reconstruct. The record correctly supplies its own bounded-bias normalization and constants. Source: [arXiv:2103.11604v2](https://arxiv.org/html/2103.11604v2), §1.3, Lemma 1.9 and the stopping-time footnote.

#### Sherstov–Storozhenko–Wu: introduce the loss before solving it

The supplied introduction, results, Fourier-weight theorem and technique overview were sampled closely; the full combinatorial partition proof was not audited. The exposition first explains why control of all Fourier levels matters, identifies the extraneous factorial loss in the earlier method, and then describes how its partition strategy addresses that loss. Its sentence “This obstacle is the reason” (introduction, “Our results: Fourier weight of decision trees”) is followed by a concrete consequence for the achievable exponent. That is a useful writing move for the quartic record: after (F33), say which powers produce m^(1−1/k), and after (F43), say which steps cost the two powers of k.

The source's main partial-function application uses rorrelation from random orthogonal matrices. Its decision-tree Fourier-growth theorem is a separate result. The current record rightly uses the latter only in Appendix E's transfer argument and does not identify the former with its explicit Walsh promise. Source: supplied literature/quartic-ref-23-an-optimal-separation-of-randomized-and-qu/extracted.md, introduction and §1.8; [arXiv:2008.10223](https://arxiv.org/abs/2008.10223).

#### Tal: distinguish the altered problem from a changed analysis

The supplied abstract and introduction, including the definition of rorrelation and the two main query bounds, were read. The paper explicitly explains why it chooses a random orthogonal matrix: properties needed later fail for the Hadamard matrix. This is an instructive comparison because the word Forrelation alone does not identify a theorem's exact input. A related-work table should keep the problem, promise and matrix model attached to each exponent. Source: supplied literature/quartic-ref-26-towards-optimal-separations-between-quantu/extracted.md, introduction, pp.1–2; [arXiv:1912.12561](https://arxiv.org/abs/1912.12561).

#### Girish–Servedio: a nearby exact problem is still a different supplier

The supplied abstract, definitions and theorem statements were read, with the lower-bound overview and initial collision analysis sampled. Their extremal promise has values +1 and −1 and admits an exact one-query quantum algorithm. The hard-law construction uses bent functions and hidden affine structure. This is relevant recent context and a useful example of explaining why a seemingly harmless change of distribution can expose the origin. It is not a drop-in source for the record's one-sided, variable-k Walsh promise or its displayed near-linear classical bound. Source: [ITCS 2026, paper 72](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.72); supplied literature/quartic-lit-girish-forrelation-is-extremally-hard/extracted.md, definition of Extremal Forrelation and the “Main Ideas”/classical-hardness discussion.

#### A current related result checked without importing its theorem

Zhang–Shao's 30 October 2026 cyclic-Forrelation preprint was checked at abstract level only. It concerns a normalized trace, DQC1 queries and distinct adaptive/nonadaptive classical bounds. It does not replace the fixed-k one-sided promise supplier. Its recent appearance is useful context, not a reason to expand the short companion into a survey. Source: [arXiv:2610.41694v1](https://arxiv.org/abs/2610.41694v1). The supplied register already mentions this paper for disclosure practice; this return does not present it as an overlooked citation essential to the proof.

#### The supplied SK exemplars: compare moves, not subject matter

The openings and initial mathematical sections of short-paper.md, expository.md and long-reasoning-record.md were sampled. Their mathematical proofs were not audited for this task. The expository sample states what a reader should be able to reconstruct, then uses a small two-spin calculation to make the later abstraction answer a question already encountered. The long sample separates an ordinary mathematical consequence from the exact scope of the selected formal statements. Those are useful design comparisons. They do not justify transferring the length, vocabulary or proof order of a different subject to query complexity.


#### The 2026 certificate separations: identify the classical measure

Ben-David–Kothari's supplied main mathematical sections were read, including the champion construction, proposal-card checks and quantum algorithm. Their Theorem 1 simultaneously makes certificate complexity large and randomized/quantum evaluation cheap. The phrase “championship proposal form” is followed by a cumulative-sum example that explains the chosen representation. This is a useful model for teaching one gate or pointer check before presenting a large certificate. Their quartic certificate-versus-quantum separation does not itself establish the present randomized-versus-quantum lower bound. The current companion correctly keeps those measures distinct. Source: supplied literature/quartic-ref-09-randomized-query-complexity-can-beat-certi/extracted.md, §§1–3; [arXiv:2609.15063](https://arxiv.org/abs/2609.15063).

Ambainis–Iraids–Kokainis was sampled online at the abstract and §6.1. Its candidate set U(W) retains vertices pointing to every selected vertex in a fixed graph; its direction test has bounded error. This explains the comparison with the quartic construction's fractional weights, whose loser comparisons may have arbitrary probabilities. The related mechanism deserves credit, while its interface differs. Source: [arXiv:2609.11664v2](https://arxiv.org/html/2609.11664v2), §6.1, equations (3)–(4). No full proof audit is claimed.


### Göös–Pitassi–Watson: motivate the simpler grid first

I skimmed the abstract and introduction and read the motivating query construction in §2.1 of the [ECCC revision](https://eccc.weizmann.ac.il/report/2015/050/revision/1/download) of *Deterministic Communication vs. Partition Number*; I did not read its whole lifting proof.

The exposition starts from a grid whose certificates and adversarial query behavior can be understood immediately. It then adds a pointer chain to force the needed certificate structure. This is a useful model for the purpose map missing between the record's two worked boards. The reader should know which obstacle each example isolates before learning its labels. This comparison concerns exposition of a construction, not an assertion that the two lower bounds use the same reduction.



### Bibliographic precision: BSS

The [Rutgers institutional record](https://www.researchwithrutgers.org/en/publications/quantum-query-complexity-and-semi-definite-programming/) identifies the CCC 2003 article as *Quantum query complexity and semi-definite programming*, pp. 179–193. An [OSTI-hosted manuscript](https://www.osti.gov/servlets/purl/975874/) is indexed under the earlier *Quantum Decision Trees and Semidefinite Programming* title with a May 23, 2002 title-page date. I read the institutional metadata and the indexed manuscript title-page excerpt; the direct manuscript fetch failed. I did not read the full BSS article.

Appendix C should match title and edition. This is a small bibliographic repair, not evidence against the model claims.



## Exposition: literature and teaching comparison

### Scope of this comparison

The supplied cheat-sheet paper was read selectively: its technique overview, definition and discussion of critical exponents, and the construction in Section 3.1. The supplied pointer-functions paper was read through its abstract and introduction and through the construction overview, including the direct-pointer alternative. These are not claims to have read either complete paper. Online checking also inspected their arXiv metadata. The external educational comparison used selected passages of Ronald de Wolf’s revised 2026 lecture notes and its course page, not the full notes. The sources and reading scopes are identified in the source register in `feedback.json` and `review_scope.md`.

### Cheat sheets: motivate the totalisation task before advertising the address

Aaronson, Ben-David and Kothari frame the problem as converting a partial-function advantage into a total-function separation. Their overview asks what information the quantum algorithm has that a classical algorithm cannot cheaply obtain, then uses the partial-function answers to choose where a certificate is stored. The useful teaching movement is from an obstacle to a resource and then to the construction. See the supplied extracted text, overview of techniques, and Section 3.1; source: [arXiv:1511.01937v2](https://arxiv.org/abs/1511.01937).

The short phrase “it is unclear how to make these functions total” states the obstacle before the gadget. The exposition’s domain-bit board performs an even more concrete teaching service: it demonstrates why a cheap decoder can accept something a total-function certificate must reject. That example should be preserved as the local explanation of the same obstacle.

The present introduction also improves on a bare historical list by explaining why AND-OR supplies small certificates and where the older cubic accounting comes from. Its weakness is placement: it asks the newcomer to understand the whole earlier route before the first certificate-bearing board. The comparison would be easier to assess after the reader knows what certification costs in this construction.

The paper’s discussion of critical exponents is also relevant to Question 4. An infimum of universal exponents is a statement about excluding every smaller exponent; it is not identical to excluding a bound at the endpoint. The exposition already defines the correct infimum. Its exercise answer should preserve that definition’s logic rather than equate a strict parameter recipe with necessity.

### Pointer functions: credit the rejected variant and its representation cost

Ambainis, Balodis, Belovs, Lee, Santha and Smotrovs explicitly consider adding direct pointers from the special element to a zero in each other column. The next sentence identifies the cost: “the size of the alphabet becomes exponential”. The construction overview then uses a balanced pointer tree. See the supplied extracted text, construction overview, paragraph beginning “In principle”; source: [arXiv:1506.04719v3](https://arxiv.org/abs/1506.04719).

This supports the exposition’s literal statement that direct pointers appear in the earlier work. It does not support leaving the impression that the earlier Boolean construction simply used the same direct-pointer array without qualification. The prior obstacle belongs beside the credit. The present construction reads a selected pointer through bit queries and uses a different certificate and comparison organisation; its explanation should say which representation cost it pays and why that is sufficient. The critique requests that explanation, not a new novelty claim.

The supplied pointer paper is also a useful stylistic comparator because its construction overview gives reasons for changes to the gadget. The exposition does this well in its two tournament counterexamples. A dominating nonwinner explains final verification; a cycle explains why sorting or ordinary minimum finding is unavailable. These are concrete reasons, not ornamental variations of the board.

### A scoped educational comparison for the quantum subroutine

De Wolf’s *Quantum Computing: Lecture Notes*, revised 2026, develops Grover search before discussing unknown success probabilities and amplification. Selected Chapter 7 passages distinguish expected running time from a capped bounded-error procedure and explain the successful-state rotation. This supports keeping the capped contract and preserved conditional state visible while making numerical supplier details optional. I inspected Chapter 7, especially Sections 7.2–7.3, and the relevant cap discussion in Appendix B, not the whole book. [Notes, arXiv:1907.09415v6](https://arxiv.org/pdf/1907.09415); [course page](https://homepages.cwi.nl/~rdewolf/qc26.html).

### What the comparison does and does not establish

The external notes provide a model of prerequisite sequencing and a reference for a standard subroutine. They are not evidence that an actual reader understood this exposition. Likewise, the supplied research papers support construction credit and mechanism comparisons; their research-paper audience does not justify imposing the same prerequisites on a newcomer document.

The current exposition is strongest where it exceeds a research-paper overview with a small decisive counterexample: the domain bit, independent versus marginally uniform planting, and joint versus conditional lightness. Its weakest transition is the one where it falls back to a research-paper-style simulator description. A short executed trace from the existing record would bring that transition to the same teaching standard as its best examples.
