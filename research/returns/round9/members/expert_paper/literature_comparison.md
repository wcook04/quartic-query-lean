# Literature comparison

## Reading scope and chronology

Literature checking followed the frozen first-pass notes. This comparison combines the three simulated perspectives and the lead reviewer's checks; it does not describe independent human referees or a complete reading of every cited paper. The sentence annotations were reconstructed after the narrative freezes. Editions and actual reading scopes below distinguish inspected arguments, introductory statements, skimmed material and unavailable full text. The search date for the newer primary papers was **4 November 2026**.

All nine reference folders supplied under `literature/` are covered below. Their local `extracted.md` files were the principal reading surfaces. Damaged macros and automatically changed theorem numbers in some extractions make them unsuitable for a numerical comparison of prose style. The comparisons instead identify specific writing operations: establishing an oracle contract, explaining why a construction component is needed, separating two resource guarantees, and showing which theorem a parameter choice invokes. No external prose is quoted verbatim.

## The source preprint: what the reconstruction should make easier to check

**OpenAI, _A Nearly Quartic Separation Between Randomized and Quantum Query Complexity_, 5 October 2026.** [Pinned source](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf); supplied `paper/source.pdf` and `paper/extracted.md`. Across perspectives, selected passages from the introduction, Lemma 2.1, §3 and §§4–5 were read. The exact remote URL was unavailable to one retrieval route; the supplied bytes remained readable. This is not a new complete proof audit.

Lemma 3.1 already gives bounded amplification with the successful-state guarantee; Proposition 3.2 already supplies the probabilistic tournament; §4.2 already uses the capped predictor's joint success event. The companion should therefore identify its added value through its existing reconstruction, quantitative choices, examples and formal correspondence, rather than making these inherited reductions sound newly supplied. A concrete comparison is especially useful: the source's §4.2, printed p.13, explicitly handles a simulation that terminates before the chosen query time. The companion's shortened fallback omits that case. Restoring it improves algorithm completeness without adding a new proof idea.

## The nine supplied references

### 1. Cheat sheets: let each construction component answer a question

**Aaronson, Ben-David and Kothari, _Separations in Query Complexity Using Cheat Sheets_.** [arXiv:1511.01937v2](https://arxiv.org/abs/1511.01937v2), 9 July 2019 revision of the STOC 2016 paper. Read: technique overview, §3.1 and relevant §3.2 implementation and randomized lower-bound passages; not the full framework. Supplied folder: `quartic-ref-02-separations-in-query-complexity-using-chea`.

Section 3.1 develops the certificate-addressing construction by explaining the difficulty that each new ingredient resolves. That causal order transfers to the companion's introduction: show why direct verification is expensive, then why cheap comparisons and delayed certification help. Section 3.2 is the useful destination for the historical AND–OR cost comparison. Its totalization mechanism does not automatically supply the current construction's local-test count or bit-query cost. The old parameter calculation should expose both changed costs, rather than suggesting that only the quantum denominator improved. Its blank-array convention also differs from the present dummy input, which is already false because every column contains a zero.

### 2. The universal quartic bound: distinguish an endpoint from its implications

**Aaronson, Ben-David, Kothari, Rao and Tal, _Degree vs. approximate degree and quantum implications of Huang's sensitivity theorem_.** [arXiv:2010.12629v1](https://arxiv.org/abs/2010.12629v1), 23 October 2020; STOC 2021. Read: introductory Theorems 1–2, their implication chain, and Conjecture 2; not the complete spectral-sensitivity proof. Supplied folder: `quartic-ref-03-degree-vs-approximate-degree-and-quantum-i`.

Theorem 1 states the universal deterministic-versus-quantum quartic bound; the randomized bound follows because randomized complexity is at most deterministic complexity. The source separates this endpoint from the machinery proving it and identifies the cubic randomized conjecture separately. The companion can use that hierarchy to make its optimal-exponent conclusion primary and its optional uniform refinement secondary. This source supplies the upper side of optimality; it does not certify the new separating construction, its explicit constants or its formalization. Several mathematical macros are damaged in the extraction, so no criticism rests on those rendered symbols.

### 3. Pointer functions: attach the access model to the comparison

**Ambainis, Balodis, Belovs, Lee, Santha and Smotrovs, _Separations in Query Complexity Based on Pointer Functions_.** [arXiv:1506.04719v3](https://arxiv.org/abs/1506.04719v3), 26 October 2015; JACM 64(5), article 32, 2017. Read: introduction and §1.3, particularly the balanced-tree and direct-pointer discussion on pp.5–6. Supplied folder: `quartic-ref-04-separations-in-query-complexity-based-on-p`.

The source distinguishes pointer variants by the operation each enables and explains the large alphabet associated with storing many direct pointers. That distinction belongs beside the current pointer encoding. Reading one selected pointer field here costs logarithmically many ordinary bit queries; this is not the same operation as querying an entire symbol in a large alphabet. The historical paragraph should preserve that model boundary while avoiding a catalogue of variants before the present construction is understood. The supplied extraction loses some macros; the review uses the intact qualitative comparison, not a reconstructed theorem from corrupted typography.

### 4. Bansal–Sinha: keep the exact supplier interface visible

**Bansal and Sinha, _$k$-Forrelation Optimally Separates Quantum and Classical Query Complexity_.** [arXiv:2008.07003v3](https://arxiv.org/abs/2008.07003v3), 17 November 2020; STOC 2021. Read: introductory promise definition, Theorem 1.3 and Corollary 1.4 on printed p.4, and the opening Gaussian-chain overview. Supplied folder: `quartic-ref-06-k-forrelation-optimally-separates-quantum`.

This is the relevant hardness supplier for the explicit Walsh promise used in the companion. Its one-promise requires positive correlation, while its zero-promise bounds the absolute value. That distinction explains why the projection statistic alone does not determine domain membership. The companion should present the supplier's promise, dimension, accuracy and cost together before using it. The introductory theorem check is not an audit of the full analytic proof. Nor is the record's additional uniform estimate merely a quotation of Corollary 1.4: its reconstructed argument and different parameter dependence require a separate proof-responsibility label.

### 5. BHMT: separate preservation of the successful component from runtime

**Brassard, Høyer, Mosca and Tapp, _Quantum Amplitude Amplification and Estimation_.** [arXiv:quant-ph/0005055v1](https://arxiv.org/abs/quant-ph/0005055v1); published in _Contemporary Mathematics_ 305, 2002. Read: §2, Lemma 1, equation (8), and Theorem 3; amplitude-estimation sections were not reviewed. Supplied folder: `quartic-ref-12-quantum-amplitude-amplification-and-estima`.

The invariant-plane calculation explains why successful amplified trials retain the original good component up to phase. The expected-cost QSearch theorem answers a different question from the companion's all-input finite cap. These should be cited for their separate jobs. The companion now correctly distinguishes the two, but its reusable contract can state the fixed flag test, original conditioning event and algorithmic uniformity together. The standard geometry alone does not identify a particular physical output subsystem after a formal compiler; that additional formal correspondence is limited explicitly in the current record's Appendix G.7.

### 6. Drucker: preserve the budget and success event when transferring a theorem

**Drucker, _Improved Direct Product Theorems for Randomized Query Complexity_.** [arXiv:1005.0644v2](https://arxiv.org/pdf/1005.0644v2), 9 May 2014 revision; _Computational Complexity_ 21, 197–244, 2012. Read: introduction, Theorem 1.1, the relevant §3 proof including Lemma 3.2, and its fair-tree specialization. Supplied folder: `quartic-ref-13-improved-direct-product-theorems-for-rando`.

The useful writing model is the explicit separation of one-instance success, copy count and query budget before the product argument. Transcript-conditioned product structure is stated where it is used. The companion's unnormalized proof can similarly expose its variable-budget invariant and leaf case. The alternative application of Theorem 1.1 gives a factor-two bound sufficient for this reduction; it should not be described as literally the same numerical conclusion as the separate-cap lemma. Expected caps, separate per-input caps and success jointly with cap compliance are different contracts. The review did not inspect the full journal-length paper.

### 7. Sherstov–Storozhenko–Wu: distinguish the explicit promise from random-matrix hardness

**Sherstov, Storozhenko and Wu, _An Optimal Separation of Randomized and Quantum Query Complexity_.** [arXiv:2008.10223v4](https://arxiv.org/abs/2008.10223v4), 29 January 2023; _SIAM Journal on Computing_ 52(2), 525–567. Read during final assembly: introductory partial/total separation statements and §1.8, the comparison with Bansal–Sinha. The supplied PDF's version label was checked. Supplied folder: `quartic-ref-23-an-optimal-separation-of-randomized-and-qu`.

Section 1.8 explains that the two approaches have different strengths: this paper's random-orthogonal-matrix route and Fourier-weight theorem are distinct from explicit Walsh Forrelation hardness. The companion should retain that distinction when explaining its supplier choice. A near-optimal partial separation by itself does not provide the exact compact certificate circuit used here. The source also separates fixed-query bounded-error statements from growing-parameter questions. That is a useful presentation comparison, but the Fourier theorem and its optional transfer in the record were not independently audited in this review.

### 8. Tal: make the matrix choice and error dependence travel together

**Tal, _Towards Optimal Separations between Quantum and Randomized Query Complexities_.** [arXiv:1912.12561v1](https://arxiv.org/abs/1912.12561v1), labelled 29 December 2019; the supplied title page is dated 12 February 2020; published at FOCS 2020. Read during final assembly: abstract, §1, Definition 1.1, matrix-choice discussion and the total-function application opening. Supplied folder: `quartic-ref-26-towards-optimal-separations-between-quantu`.

The introduction says directly that its random-matrix properties need not hold for the Hadamard matrix. It also distinguishes constant and slowly growing choices of the correlation parameter, with their quantum overhead. Those distinctions transfer to the companion's historical comparison and optional uniform section. This does not justify substituting a random orthogonal matrix into the current exact circuit. The review has not verified Tal's Fourier estimates or reconstructed the later totalization proof.

### 9. Bounded-error quantum search: name the predicate being approximated

**Høyer, Mosca and de Wolf, _Quantum Search on Bounded-Error Inputs_.** [arXiv:quant-ph/0304052v2](https://arxiv.org/abs/quant-ph/0304052v2); ICALP 2003. Read: §§1–3; §§4–5 skimmed. Supplied folder: `quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error`.

The model supplies noisy access to fixed Boolean predicates. That is a useful comparator for candidate verification, where a fixed exact validity condition exists. Arbitrary loser-versus-loser probabilities need not approximate a consistent orientation, so this source does not replace the fractional-weight tournament. The companion should make that contract distinction beside its concrete comparator, rather than asking readers to retain several search taxonomies in advance. The current verification bound is conditional on the selected list and prior history; its validity comes from a fresh test of a fixed input, not from independence of the adaptively selected candidates.

## Newer primary tournament research

Three recent papers were inspected beyond the supplied reference shelf. These comparisons are deliberately narrow.

**Ben-David and Kothari, _Randomized Query Complexity Can Beat Certificate Complexity_**, [arXiv:2609.15063v1](https://arxiv.org/html/2609.15063v1), 14 September 2026: the introduction and selected construction passages were read, with close attention to §3, Lemma 5. Its stages distinguish candidate production, elimination and verification under a fixed comparison graph. That organization transfers to the companion's actual-process, ideal-process and sampling transitions. Its oracle guarantee does not transfer to arbitrary fractional comparisons.

**Ambainis, Iraids and Kokainis, _Near-Optimal Separations of Certificate Complexity from Randomized and Quantum Query Complexity_**, [arXiv:2609.11664v3](https://arxiv.org/html/2609.11664v3), 5 October 2026: selected introductory passages and §6.1, including Algorithm 4, candidate-set equations and the direction test, were read. The source makes its maintained set and stopping rule visible before charging their cost. Here the replacement is a weight product, whose exact successful sampling law should appear immediately. The technical appendices and variable-time-search analysis were not fully audited.

**Arora and Kumar, _Quantum Query Complexity of Tournament Solutions_**, [arXiv:2610.39702v1](https://arxiv.org/html/2610.39702v1), 29 October 2026: the tournament model and §6.1, Lemma 6.1/Theorem 6.2 were read, including an independent opening of that section by the lead reviewer. Fixed-edge Condorcet finding via king finding and verification is a direct task-level comparison. It does not remove the companion's need for exact weighted sampling under unrestricted loser probabilities. A concise footnote is sufficient; a larger tournament survey would dilute the main proof.

## Additional comparisons and limits

BBHT's [arXiv:quant-ph/9605034v1, §4, Lemma 2](https://arxiv.org/html/quant-ph/9605034v1) was read for the bounded random-iteration average. Dürr–Høyer's [arXiv:quant-ph/9607014v2, §§1–3](https://arxiv.org/html/quant-ph/9607014v2) was read for its ordered-table progress argument. They clarify two different ingredients: a finite amplification trial and a rank invariant unavailable to cyclic loser comparisons.

The classical perspective inspected Ben-David's [arXiv:1506.08106v1, §§5.1–5.2](https://arxiv.org/html/1506.08106v1) for marked-zero and blank-array antecedents; Shaltiel's [ECCC TR01-009, §5, Definition 4/Theorem 5](https://eccc.weizmann.ac.il/report/2001/009/download) for its specifically scoped fair-tree result; and Girish–Tal–Wu's [CCC 2021, §1.3, Lemma 9 and footnote 2](https://drops.dagstuhl.de/storage/00lipics/lipics-vol200-ccc2021/LIPIcs.CCC.2021.39/LIPIcs.CCC.2021.39.pdf) for stopping before a bad event instead of conditioning on good paths. None is silently substituted for the present arbitrary-distribution, all-answers contract.

The Aaronson–Ambainis Forrelation full text was not independently read through the attempted online route; its relevant quantum statements were checked through Bansal–Sinha and the supplied record. No allegation rests on that retrieval failure.

The highest-value transfer from these comparisons is to expose existing interfaces at the moment they are used. In particular, the growing-family argument switches to a new allowance, $L=\lfloor X\rfloor$, supplied by the uniform bound; the missing local substitution is not a false theorem. Appendix A.3 is also valid: the all-one smallest-index column wins both possible comparison cases despite decoder error. Neither should acquire an invented mathematical objection during revision. The remaining specialist gap is an independent audit of the long record's full analytic and formal development, which this literature comparison does not claim to provide.
