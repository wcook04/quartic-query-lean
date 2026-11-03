# Feedback by document

This review leads with the expert companion, then examines the complete quantum thread of the current long record and the complete exposition. Its 189 exact-passage findings are in `feedback.json`: 71 for the expert companion, 54 for the record and 64 for the exposition. The three local exposition errors are QS247, QS251 and QS256. None changes the main theorem. The strongest remaining issues concern the visibility of the new fractional comparison mechanism, the promised teaching audience, and the precise interfaces between coherent states, measured laws and the formal implementation.

The prose below develops priorities and reasoning; the JSON provides the exact current quotations and individual actions. Source codes such as RR-S04 resolve in `feedback.json` under `sources_read`. Detailed comparisons and primary URLs are collected in `literature_comparison.md`. These are simulated reader perspectives, not statements attributed to the authors of the cited works.

## Order of this report

1. Expert companion: specialist reading and proof architecture.
2. Long record: quantum proof destination and cross-document consistency.
3. Exposition: operations, examples and the fixed newcomer audience.

## Expert companion

### Verdict and intended takeaway

The expert companion now earns a complete read by a query-complexity specialist. Its main quantum proof has a recognisable mathematical centre. Cheap outward-pointer comparisons protect a real winner against any rival; the comparison probabilities define product weights; a coherent trial samples those weights without calculating them; bounded amplification preserves the conditional label law; a stopped coupling transfers the ideal-process guarantee; and local verification decides the total function on all inputs. The presentation does not require comparisons among losing columns to approximate a fixed orientation.

The desired reader takeaway is that chain of ideas, together with the separate planted-input lower bound. The present takeaway is somewhat muddier: the same mechanism is surrounded by explicit constants, formal-interface qualifications, auxiliary examples and multiple Forrelation supplier results whose roles differ. Most of that material is valid and useful somewhere. The remaining revision problem is weighting and placement.

This review did not find a counterexample to the core weighted-tournament argument in the current expert text. That conclusion is scoped to the argument read here; it is not a new Lean build, Comparator run or complete independent proof of every cited supplier. The feedback contains local premise-placement and language corrections without treating them as a refutation of the theorem.

### 1. Give the main idea more of the reader's attention

The paper says that arbitrary loser-comparison probabilities are the new step, yet a substantial standard amplification calculation comes before the comparison routine. The current sketch still derives the numerical trial probabilities that round six intended to move into the record. A specialist needs the cap, exact conditional law and p=0 behaviour. They do not need to derive 9/40 before learning why the theorem uses probabilities as weights.

The exact-sampling paragraph deserves the recovered space. “The algorithm never computes the weights” is the implementation insight. It prevents an expensive interpretation involving amplitude estimation of every pair probability. The state in (9), fresh workspaces and the calculation w_i/m are already the right proof. Make their operational meaning more visible, ideally with a short numbered algorithm and a small fractional example.

The example must exhibit the hypothesis that has been weakened. A deterministic three-cycle shows the absence of transitivity, but it still belongs to fixed-tournament search. A pair of losers with probabilities strictly between zero and one gives nonbinary surviving weights and a conditional distribution different from uniform sampling of a set. Advice to add such an example is not a request for a new theorem or a new construction: it is an illustration of the abstract proposition already stated. Unless a board realisation is supplied, label it at that abstract level.

The paper's existing comparison with Ambainis–Iraids–Kokainis is valuable. Their maintained candidate set provides the natural starting point for explaining what the product weights generalise. The short text should not blur their fixed-graph setting, noisy evaluation of its edges and this paper's direct use of arbitrary comparison probabilities. The supplied v2 is enough to establish that comparison; the current v3 should be named separately when its updated discussion is used.

### 2. Explain the error budget as part of the mechanism

The winner is decoded correctly with probability at least 1−ε, and ε is only of order 1/T. A reader accustomed to approximate-oracle composition may expect much stronger error reduction because the sampler calls the comparison circuit coherently many times. That intuition is not the argument here. The a_ij are the exact output probabilities of the actual circuit. The proof does not assert that every comparison call returns a correct fixed bit. It only needs the winner's weight to survive multiplication across at most T previously measured pivots.

That point would clarify both the novelty and the accounting. It also explains why the workspaces and labels must be retained until the coherent trial is complete. After success, the pivot is measured and used as classical history for a new trial.

The stagewise coupling is already good and should be protected. Global conditioning on all stages succeeding can bias the pivot history when stage success depends on the past. The text's conditional coupling is the right argument. A failure after the winner enters the list cannot remove it.

Verification supplies the all-input correctness that the tournament alone does not provide. Put the false-dominant candidate example at this transition, not only in the appendix. Name the verifier's output as a found violation or no violation detected, because the search's failure flag leads to accepting the candidate. Explain the asymmetry between zero and one inputs: on a zero-input any false acceptance is harmful; on a one-input even accepting a nonwinner gives the correct Boolean output. Only omitting the winner or failing its fresh decoder matters for the upper error bound in the latter case.

### 3. Reduce the front-loaded inventory

The theorem and the k=3 consequence make a strong first page. The subsequent contribution paragraph tries to list too much. Exact thresholds, three constants, common-circuit scope, counterexamples, direct-product observations, the uniform Forrelation estimate, the long record and Lean all appear before the construction is explained.

Move constants beside the estimates they quantify. Keep a short description of the companion's explanatory purpose. If the uniform Forrelation estimate is presented as a quantitative addition of the record, say so directly: it has a different role from the already attributed separation theorem and from the main fixed-k supplier.

The introductory overview would be stronger for this panel if it posed the quantum obstacle immediately after the input picture. Naive nested search costs about m; cheap comparisons and deferred verification recover the square-root dependence. The lower-bound heuristic can then explain why this remains classically hard. This audience-specific order need not be imposed on the lower-bound specialists' version.

The closing paragraph of the introduction should not be a contract about every link in the document. State the mathematical inputs and give a short roadmap. Put detailed document-navigation metadata in the record.

### 4. Preserve precision while repairing local wording

Several small repairs have high value because they concern the interfaces between arguments.

The earlier-separation calculation needs the polylogarithmic-Q(g) premise before the displayed simplified quantum cost. The original cheat-sheet intuition makes that assumption before suppressing the factor Q(g). The historical exponents remain valid; the problem is the order of exposition.

The total function has disjoint, unconstrained input coordinates, not “independent input bits” in the probabilistic sense. Its true address exists only when the relevant P-inputs are promised. Its decoder always returns a label, including off the promise. Keeping these three statements separate makes the reason for the exact domain circuit clearer.

State what S counts, including the output gates. Then rS transcript bits and the extra output-value tests can be read without guessing a convention. Keep the common-circuit witness, which ensures that the two bounds apply to the same total function.

The early-zero estimate should refer to first discoveries before the zero is known. Repeated queries do not discover a new zero. The planted-cell event covers possible discrepancies; it need not mean that every queried bit of the planted cell differs from a blank bit.

These are local clarity and scope issues. They do not justify rewriting the paper as an audit report.

### 5. Make the optional refinements visibly optional

The short paper needs a Forrelation supplier, the two complexity bounds and the fixed-k exponent deduction. The uniform Forrelation estimate, its explicit threshold and the growing-k family are additional results with a different dependency path. §5 should say that plainly.

The existing outline of the uniform proof names sophisticated techniques without showing the quantitative relationship that connects them. It is too dense to teach that argument and too long to serve as a simple reference. Either describe the route briefly and send the reader to the record, or show the two decisive already-proved inequalities that compare shallow-tree advantage with the advantage forced by an amplified solver. Do not compress the record into a paragraph that suggests the full proof has been reproduced.

The fixed-k proof of α_tot=4 is excellent. It chooses the target exponent first, then k, then the asymptotic variable. The optional growing-k remark should not displace that ending with a large formula whose proof is elsewhere. Its exact ε expression can remain at the linked derivation.

### 6. Formal discussion and page design

The paper has successfully removed the old hashes, commands and review-status disclaimers. Its formal section should continue to read as a normal mathematical account of what has been formalised. The measured/reset implementation and the separate retained-state result are genuinely different interfaces and should remain distinguished. Axiom inventories, alternate constants for the universal bound and the full list of linked statements are lower priority for this panel.

The PDF inspected here is legible and its counterexample table fits. The practical corrections are modest: keep Lemma 2's statement on one page; label the rows referred to by number; enlarge the essential labels in Figure 1; and place the false-dominant example where it explains verification.

### What must be kept

Keep the winner-only guarantee in the abstract; the explicit nested-search bottleneck; the restricted scope of the AND–OR cubic barrier; the domain/value distinction; outward pointers; the same-circuit witness; the local-test dichotomy and √K explanation; the shared sorted comparison circuit; retained orthogonal labels; the exact drift identity; the fresh-workspace product calculation; the stopped coupling; the two-case final error analysis; the query-position predictor; joint cap-and-success events; and the fixed-k quantifier order. These are the paper's mathematical spine. The next revision should make them easier to see.


---

# Quantum-side critique of the long reasoning record

## Scope and verdict

This contribution concerns the current Markdown of the reasoning record, with its quantum sections read in full and with the definitions, construction, exponent calculation and selected formal-interface passages needed to understand them. The companion’s quantum section and the exposition’s quantum account were used as cross-checks. It is not a second audit of Lean receipts, and it does not claim a full rereading of the record’s classical lower bound or the long Gaussian/Fourier Forrelation proof. The associated source log distinguishes full selected-section reading from sampling. The record PDF is stale, so the findings use Markdown section and quotation locators.

The quantum argument has a sound, recognizable spine. A true addressed certificate defeats every rival on the event that its own address is decoded correctly. Complementarity of the comparison probabilities gives a short drift identity without any transitivity or correctness promise for loser comparisons. Fresh coherent preparations realize the exact weighted pivot law. A stopped coupling controls disagreement only before the wanted candidate is selected. Finally, exact local tests make verification safe on every address, including addresses output by an unpromised decoder. I did not find a counterexample to this chain, an invalid adaptive union bound, or an omitted all-input cap in the passages reviewed. The highest-priority criticisms are specifications, explanation, ordering and cross-document consistency; none is labeled a proved mathematical error.

A quantum algorithms reader could use this record as a proof destination. Reading it consecutively is less rewarding. Its most valuable novelty is interrupted by standard amplification geometry, loose scalar estimates and source-interface prose. The record should preserve the full arguments while giving the specialist a clean route through their dependencies. The present shorter companion sometimes supplies a sharper algorithmic explanation than the destination to which it sends the reader. That is a funnel problem rather than a reason to make the record shorter everywhere.

## 1. Make the actual novelty the easiest argument to find

The central fact is the identity

$$
\mathbb E[W_{\mathrm{new}}\mid w]
=\frac{W^2-\sum_iw_i^2}{2W}\leq\frac W2.
$$

For this quotient take $W>0$; the zero-weight state is handled by absorption. Its hypotheses are very weak: nonnegative weights, zero diagonal, and complementary probabilities for each unordered pair. No total order, estimated probability table or reliable Boolean orientation is needed. This is the reader’s shortest path from the theorem statement to an understanding of why the algorithm can survive arbitrary loser behavior. The text states that it is central, then postpones it until after a substantial self-contained amplification proof. A specialist should be able to read the bounded-amplification contract, jump to the drift and implementation, and return to the full amplification proof when checking the retained-state specification. This is the access-order recommendation in QS115, not a recommendation to remove the proof.

The four-candidate example is useful but undersells that novelty. Its loser triangle consists of certain wins. It establishes that sorting is impossible, but exact king-finding already permits cycles. The new difficulty is a comparison whose two outcomes can each have probability near one half, without a fixed Boolean answer separated by a correctness gap. One complementary pair at probabilities one half would turn the existing example into a demonstration of fractional survival. With the suggested pair changed, a pivot can leave weights such as $(1-\varepsilon,0,1/2,1)$; the next sample then visibly follows a nonuniform distribution that is neither a uniform set sample nor a ranking rule. The recommendation is to illustrate the theorem already proved, not to seek an extension (QS126).

The same example can carry more of the proof. A real sampler failure before the wanted candidate has entered the list can matter; a failure after it has entered merely ends the search with the useful candidate retained. Showing those two continuations would make the stopped coupling memorable (QS127). In the exposition, the later worked stage has exact decoders and deterministic comparisons too. Across the funnel, the examples now make cycles concrete while leaving the fractional case largely symbolic.

The literature comparison should use algorithmic interfaces. Dürr–Høyer draw successively smaller ordered values and analyze a decreasing rank; their paper also puts an explicit cutoff on the procedure. Mande–Paraashar–Saurabh maintain genuine candidate sets using an exact orientation oracle and exploit a tournament-density statement. Høyer–Mosca–de Wolf assume underlying Boolean answers with a bounded-error gap. The current construction instead has arbitrary comparison probabilities, a row guaranteed to be reliable whenever a semantic winner exists, and analytical multiplicative weights. These distinctions identify what is inherited and what is new more accurately than a broad phrase such as comparison-based search. Sources: RR-S04, RR-S05, RR-S06 and RR-S07.

The two 2026 certificate-complexity papers deserve similarly differentiated credit. In the supplied Ben-David–Kothari argument, exact local eliminations define an orientation before a sink/king routine and final verification are used. In the supplied Ambainis–Iraids–Kokainis quantum argument, genuine candidate sets, approximate direction/membership routines and variable-time search form the mechanism. Their bounds concern certificate complexity relative to randomized or quantum complexity; they are not themselves the randomized-versus-quantum lower bound at issue here. The record acknowledges the right papers but should say this relationship more concretely at the point of comparison (QS114; RR-S08 and RR-S10). The primary arXiv site now has AIK v3, while the packet supplies v2. Selected v3 passages were checked, not the full revision; the review’s detailed comparison rests on the supplied v2 (RR-S09).

## 2. Separate the three quantum interfaces that are currently easy to conflate

The record has three distinct objects: an invertible preparation with retained workspace, a state-returning amplifier, and a measured-label sampler that resets work between continuations. All are legitimate. They do different jobs, and a source-level implication between them should not be inferred merely from a mathematical implication between their specifications.

The ordinary proof of Lemma 3.1 establishes that successful amplification preserves the direction of the whole projected state. For fixed input, every successful iteration count has the same designated output state up to global phase. Routing the first successful trial and treating history phases as auxiliary amplitudes explains why the designated returned subsystem is pure even when extra records are retained. This is worthwhile detail. The example comparing a pure plus state with one half of an entangled pair is particularly good: it shows that agreement of computational-basis label probabilities is insufficient for a retained-state theorem. It should survive any revision (QS120; compare the geometric treatment in BHMT, RR-S02).

By contrast, the implementation used for the final decision bound only needs the finite-label law. The current companion and Appendix G.7 describe a separate measured/reset route. In §5.2, the sentence saying that the compiled finite-label law follows by measuring the successful state is mathematically true, but its placement makes it sound like a statement about the derivation of the compiled implementation. Those are different assertions. The record should explicitly name the mathematical implication, then name the independent measured/reset implementation, and say that both supply the law used in the following coupling. It should not imply that the stronger physical retained-state bridge has been obtained merely because a weaker output-law theorem is available (QS130).

The sentence in §5.3 calling the result a classical mixture over decoded labels is another local source of confusion. The full prepared state remains coherent. Orthogonal label blocks make the probability calculation equal a classical sum over the label distribution. Naming the probability law as that mixture would preserve the correct argument without contradicting the surrounding insistence on retained quantum registers (QS138). Likewise, the retained decoder is a noisy output-bit preparation with an inverse, not a clean exact oracle for the partial Boolean function. Its trial records are kept so that the full preparation can be reversed. The exact local-test oracle admits a different compute–copy–uncompute argument because its output is certain in each index block. Bringing these two explanations into direct contact would teach why workspace retention is necessary instead of making it sound like administrative bookkeeping (QS108 and QS112).

Lemma 3.1 also needs a narrower access contract. The record says every designated success subspace, then uses its reflection for free. In the input-query model, a fixed known projector or a stored success bit has this property. An arbitrary unknown input-dependent subspace would not. The intended applications plainly use a computed flag, so clarifying that the success measurement/reflection is fixed as part of the register interface does not require a new theorem or new formalization. It removes an avoidable ambiguity introduced by broadening the source statement’s success-bit wording (QS116; RR-S01 and RR-S02).

One compact diagram of a stage would resolve several of these issues at once: classical pivot history; fresh coherent comparisons and retained work; reversible success flag; amplification; measured next pivot; fresh work for the next stage. The diagram should show the existing procedure and the boundaries between its operations, not add a hardware implementation or new resource model (QS128).

## 3. Preserve the all-input correctness argument and make its polarity visible

The record is strongest when it explains exactly which promise is used. Against the actual winner, every incoming rival pointer reads a one, regardless of which label the rival decoder produced. Correct decoding of the winner’s own address suffices to disqualify the rival. No correctness claim is needed for an unpromised rival, and no independence of the two decoded addresses is needed for this event inclusion. That paragraph deserves protection (QS113).

The abstract dominant row and the semantic winner should nevertheless be distinguished at the theorem entrance. A dominant comparison row need not certify the Boolean function. The shorter documents’ dominating-nonwinner example explains why verification remains necessary. The record should carry the relationship winner implies dominant, without suggesting the converse. Under complementarity and the chosen error parameter, there cannot be two dominant rows; the output list is a way of retaining uncertain candidates, not a requirement to recover several independently valid answers (QS121–QS122).

The product law is also correctly conditional on fixed input, fixed pivot history and fixed candidate index. Separate fresh comparison workspaces yield a tensor product of success projections. Orthogonality of distinct candidate indices then yields the sum over candidates. This does not assert independence of random input bits, independent unknown orientations, or fresh draws of an oracle. The record’s explicit explanation should remain near the formula. The only information from earlier stages used by the next preparation is the classical pivot list; rebuilding all its comparisons is precisely why the sum of history lengths contributes a square in the number of stages (QS124–QS125 and QS129).

The stopped coupling is sound. The implementation’s failure probability may depend on the entire history. The exact law nevertheless permits an auxiliary construction that draws an ideal pivot and an independent failure bit conditional on that common history. Independence belongs to this coupling construction, not to an extra physical assumption about the real sampler. While the wanted candidate is absent, its weight exceeds one half, so the success-threshold promise holds and each conditional disagreement probability is at most the prescribed error. After the candidate appears, no further such guarantee is needed. Its own weight becomes zero, and even certain failure at the next stage is harmless to list inclusion. These distinctions are where the record adds genuine proof value beyond a bare union-bound sentence (QS131–QS132).

Verification closes the all-input argument because a nonwinner has a failed test at every address. The verifier measures a fresh decoded address, searches for a failed local test, and accepts only when that search reports no success. Thus amplifier failure has the opposite operational meaning here from a failed local test. On a zero-input, at most the list-length many nonwinners can be accepted in error. On a one-input, acceptance of any earlier candidate already gives the correct decision bit; the algorithm is not claiming to return a valid witness. It is enough that the actual winner is listed and its fresh decoding succeeds if it is reached. The existing error split is correct and should be kept (QS140–QS141).

Because the word failure carries several meanings, the reader currently has to reconstruct these polarities. A two-row table stating the success flag, failure symbol and caller action for pivot sampling and failed-test search would be more useful than another blanket assurance about all-input behavior (QS133). The record’s finite board already has one and two failed tests among 371 tests. Reusing those exact numbers at verification would make the probabilities zero, 1/371 and 2/371 concrete, connecting the elaborate board to the quantum procedure that consumes it (QS111).

## 4. Keep exact budgets recoverable without burying the algorithm

The all-branch cap is a real requirement, and the record does provide it. Every trial family, maximum iteration count, maximum number of stages and maximum comparison history is bounded before input-dependent outcomes are seen. Runs can stop early; their realized counts need not be equal. The proof does not rely on an expected running time on promised inputs and then forget malformed inputs. This is a substantive strength, including the branch in which the unamplified success probability is zero.

The historical comparison needs precision. BBHT’s primary paper already discusses timeout for the no-solution case, and Dürr–Høyer’s algorithm includes a cutoff. The particular fixed-budget interface used here deserves explanation; timeout or capping itself should not be presented as an invention of this paper. The record’s current sentence that the cited expected-cost results do not by themselves provide this specific cap is defensible. The strongest comparison is to say what contract is required and show how this construction delivers it (RR-S03 and RR-S04).

The exact call budget, however, changes vocabulary several times: preparation calls, inverse calls, logical reads, abstract comparison cost, concrete comparison cost and ordinary bit queries. The distinctions are legitimate, but their correspondence should be explicit once. In particular, the abstract physical comparison cap and the concrete logical-read count occupy related roles, with the compiler’s factor two added when appropriate. A small table would make it easier to audit the count than repeated prose introductions of new symbols (QS134).

Some detail earns space. The unconditional preparation and inverse construction, with only fixed reflections controlled, answers the genuine concern that an opaque unitary cannot simply be assumed controllable. The two-query load–use–unload explanation connects the logical read to the standard input oracle. The statement that no gate or workspace bound is claimed correctly locates the result in query complexity. These should remain (QS118 and QS144).

Other detail can be placed in a constant-accounting destination. The derivative used to prove a weak logarithm inequality, followed by the factors 138, 6072 and the explicit growing-parameter constant, interrupts the mathematical dependence the reader is trying to track. Preserve these calculations, but label their role. Before replacing logarithms by reciprocal errors, say that the following count deliberately chooses a convenient logarithmic exponent. The natural comparison estimate already simplifies to the expression shown in the companion; carrying that simplification into the record makes the enlargement to the final power six transparent (QS119, QS139 and QS143).

## 5. Repair the remaining funnel and register defects

The prior-round repairs matter. The record now has a growing-k calculation, so the old complaint that it merely claims the limit without recovering it should not be repeated. The quantum reading route no longer forces a specialist through the complete Forrelation lower bound before the construction. The evidence chronology has a designated appendix. The remaining problems are more local.

Visible section references have not kept up with reorganization. The opening sends readers to companion §§4–6 for material now in §§3–5. A return link from the ideal process still names companion §4.2, which is now part of the classical argument rather than the tournament. In the statement catalogue, a §5.2 label points to an anchor in §5.5. These links can resolve technically and still fail as scholarly navigation. A semantic destination check should compare the claim, the visible section number and the destination heading (QS102 and QS154).

Source identifiers still become grammatical subjects in ordinary proof prose: the text tells a reader what happens for named declarations or describes a wrapper’s isometry/continuation fields before returning to the mathematics. The identifiers are useful as a lookup layer. They are less useful when the reader must decide sentence by sentence whether a mathematical definition or a software representation is being introduced. Keep them adjacent to claims, with compact links to Appendix G, rather than removing them altogether (QS103, QS110 and QS142). The catalogue’s plain-text sums and tensor expressions similarly make a human reader translate a serialization format back into mathematics. Readable titles and rendered notation can coexist with stable machine IDs (QS153).

The continuation proof in §5.5 is valuable and should not disappear simply because it overlaps the list argument. It proves a different output interface for the same overall decision algorithm. Calling it a different route is currently too vague; say what changes. Explain the prepend-versus-append storage convention, avoid reusing Q for a temporary scalar probability lower bound, and preserve the careful treatment of a potentially negative induction estimate. These are small edits that make a delicate proof auditable without expanding its mathematical scope (QS145–QS148).

For the exponent, the opening approximations should remain a fast heuristic, but their inequality direction should be visible. An upper bound on the quantum cost and a lower bound on the classical cost are not matching asymptotics. The rigorous later argument already handles this correctly. In the growing-k subsection, the competing contributions proportional to k and to log(m)/k explain the square-root choice better than the long constant expansion that precedes them. Preview that tradeoff, then validate the existing schedule. Describing a relaxed constant as chosen because the companion uses it is editorial history; describing it as a convenient common upper bound is mathematical explanation (QS101 and QS149–QS150).

## What should be preserved through revision

The record’s distinguishing strength is not maximal length. It is the set of precise contracts that let a reader check where each promise, inverse, conditioning event and cost conversion is used. Preserve the bit/controlled-phase/bare-phase distinction; the negative-Forrelation domain explanation; the noisy retained decoder versus exact local-test oracle; winner-only robustness; the exact drift identity; the inaccessible nature of analytical weights; the exact successful-label law; the stopped history-conditioned coupling; the universal-address verifier guarantee; the separate one-input and zero-input errors; and the fixed all-branch budget. Those are the parts a referee needs to recover the proof and a quantum specialist needs to recognize the contribution.

The review recommends rearrangement, clarification and more representative examples, with the complete existing proofs still available. It does not recommend new theorems, improved bounds, additional formalization, or a stronger output task than Boolean evaluation.


---

# Exposition: quantum-specialist teaching critique

## Verdict

This is a useful graduate quantum-query reading, but it does not yet meet the packet’s promised entrance for a mathematically literate newcomer. I would read it to the end as someone who already knows oracle algorithms, Grover search, amplitude amplification and the logic of randomized lower bounds. I would not expect the specified non-specialist reader to reconstruct the quantum algorithm unaided. The gap is concentrated in a few operations and in the choice of examples; it does not require a general quantum-computing textbook to repair.

The strongest material is already concrete. The three eight-bit strings distinguish a promise from the outcome of a particular quantum test. The four-column board turns a large artificial function into an inspectable object. The domain-bit change, the dominant nonwinner, and the loser cycle each block a different false inference. The later simulator makes the hidden-address argument precise without pretending that an algorithm must first compute an address before guessing a cell. The fixed-parameter counterexample at the end is unusually effective. Preserve all of these.

The main remaining problem is that the central quantum example removes the feature the algorithm was introduced to handle. The cycled board makes every decoder and comparison deterministic. Its weights are therefore indicator values, and its conditional sampler is uniform on an ordinary survivor set. A reader can calculate every row, answer Question 2, and still not understand the fractional-weight extension. The record contains a nearby nonuniform example, with first-step weights 11999/12000 and 1 and conditional probabilities 11999/23999 and 12000/23999. Its loser comparisons are still deterministic. Start there and change one loser pair to probabilities one half in each direction: after pivot a the weights become (1−eps,0,1/2,1). A calculation of the success mass and conditional probabilities then exposes the arbitrary-loser mechanism as well. Label this as an abstract comparison-matrix variation, without claiming a new addressed-board realization. This is the highest-value example change in this document (QS237, QS260).

## The reader promised and the reader actually served

The first page defines an oracle in ket notation, a universal exponent as an infimum, a family with k-dependent constants, and asymptotic arithmetic. Before the first matrix is visible, the reader also encounters a historical progression, a composition argument with AND-OR, a prerequisite list and a route map. The supplied PDF starts the numerical matrix on page 3. The introduction is intelligible to a query-complexity student, but it makes a stranger hold too many undefined objects at once.

The prerequisite paragraph is honest, and its honesty should stay. Its remedy is wrong for the fixed audience. A reader who can already use unknown-probability amplification, uncomputation, minimax and conditional probability along adaptive trees has done much of the specialist preparation the exposition is meant to replace. The writing skill itself distinguishes an author-chosen audience from an audience fixed by the request and says not to treat stronger prerequisites as completion. This instance needs a short operational ladder, not a longer list of prerequisites (QS201).

The ladder can be small. Explain what one oracle call does and what its measurement does not reveal. Connect the bit oracle to the phase operation used on the signs. Explain projection as a two-outcome experiment. Show how would-be measurement outcomes can be retained as flags until a reversible preparation is inverted. State bounded amplification as a usable tool, including its cap and its conditional output law. Teach one coupled stage by using the same pivot on both sides when the real sampler succeeds. The present text already contains most of the required facts, but it supplies several only after their first consequential use (QS202, QS210, QS212, QS233, QS244).

De Wolf’s notes provide a useful ordering comparator: §§2.3–2.4 distinguish an oracle state from readable answers and derive the phase query from the bit query; §§7.1–7.3 state the search task and operations before the good/bad-plane analysis. Those are local presentation moves, not a demand that this article reproduce the notes. The source was read at those sections, not cover to cover: [Quantum Computing: Lecture Notes, v6](https://homepages.cwi.nl/~rdewolf/qcnotes.pdf).

## Put the new quantum idea in the foreground

The section correctly separates candidate generation from certificate verification. This is the structural reason the naive nested Grover search is too expensive. But it could state the operational algorithm more plainly before the ideal analysis: generate a bounded list using the comparison preparation, stop on sampler failure or at the cap, and verify the list. The weights should remain analytical quantities. The sentence saying they are never computed or estimated is indispensable (QS230, QS262).

The missing fractional example is more serious than a lack of illustration. It affects the account of novelty. Minimum finding uses an order. Bounded-error search supplies reliable answers to fixed predicates. The supplied 2026 predecessors organize their algorithms around candidate sets and tournament steps. Here the algorithm uses the actual probabilities of coherent comparisons, including comparisons between losers with no margin from one half. Its success law is exact for those actual probabilities; it never replaces them by a fictitious reliable tournament.

The exposition’s final sentence about decoder errors already being part of a_ij states this crucial fact, but far too quietly. Move its explanatory force to the introduction of a_ij or to the amplified preparation. Otherwise a quantum-trained reader may expect a union bound over every coherent comparison call and infer a much stronger accuracy requirement than the proof uses (QS245). The explanation of orthogonal retained labels is also doing something stronger than making a_ij well defined: it establishes agreement with the decoded-label experiment (QS234).

The nearest comparison-based antecedents deserve one or two sentences in this section. AIK, BDK and king finding are present in the bibliography, yet the exposition body uses none of them. It instead jumps from minimum finding and bounded-error search to the new process. The supplied BDK §3 is particularly useful as a comparison: it explicitly separates a virtual candidate list, a tournament step, and verification. Keep the distinction between its certificate-complexity result and this randomized-query result. The aim is accurate credit for the borrowed architecture, followed by a clear identification of the new arbitrary-probability extension (QS235; [Ben-David–Kothari, arXiv:2609.15063](https://arxiv.org/abs/2609.15063)).

## Standard amplification is still consuming the wrong space

The amplification paragraph contains the complete M=ceil(10/sqrt(gamma)) trial recipe, the 3/4 case split, 19/40, 9/40 and the logarithm ln(40/31). It occupies the bottom of PDF page 8 and continues on page 9. This is precisely the material that round-six findings SX-022, QX-020 and CX024 planned to send to the record. The issue is therefore an accepted revision that did not land in the supplied artifact, not a demand to reopen a repaired complaint (QS243).

The main route needs four facts: every branch has a cap independent of the unknown success probability; probability at least gamma gives small reported-failure probability; probability zero gives certain failure; and a successful label has the original conditional distribution. The normalization qualifier p>0 and global-phase qualification should match the companion. Those are small corrections. The detailed constant proof should be optional or linked. The recovered space belongs to the fractional example, the coherence bridge, and the local-test verification example.

The current worked stage has a further limitation worth keeping explicit. At success probability one half, every Grover iteration count leaves that probability one half. Question 2 then chooses a case with one surviving good label and probability one quarter, where one iteration makes success certain. Both are useful special cases, but neither teaches the need to cope with an unknown general success probability while preserving unequal output weights. The examples can remain if that is their stated role; they cannot carry the whole sampler lesson.

## Carry the board into verification

The domain-bit board gives a candidate with exactly one failing test among K=371. The dominant nonwinner gives a different single pointer failure. These should be recalled when the verifier amplifies over local tests. One uniformly chosen test then finds the fault with probability 1/K, explaining the threshold the algorithm actually uses. Without this return, the board teaches the Boolean definition and the quantum verifier arrives as an unrelated black box (QS220).

The verifier also needs a brief explanation that a coherent test-index computation still uses the ordinary bit oracle. The companion says this; the exposition does not. A pointer test computes an address reversibly, reads the pointer bits, queries the selected target bit and retains enough workspace for the inverse. That prevents the reader from imagining a unit-cost pointer oracle or free inspection of the whole addressed array (QS246).

A small gate-level example would help for the same reason. The previous plan called for both a pointer test and a gate test. Only the pointer has actual values in the delivered prose. A single gate from the existing 180-gate circuit, with one falsified proposed output, would make local transcript consistency tangible. It would also justify giving less prominence to the name Shannon expansion and to the exact circuit-size calculation (QS216–QS217, QS225–QS226).

## Three local errors to correct without changing the theorem

**Actual counts versus caps (QS247).** The count paragraph says every number of trials, iterations, stages and comparisons is fixed in advance. The algorithm chooses the Grover count randomly, stops amplification after success, stops the tournament after failure, and compares against however many pivots have already been obtained. The realized counts are variable. Their upper bounds are fixed. The preprint’s §3.2 already uses the correct fixed-upper-bounds formulation. This is an operational description error; the displayed worst-case complexity need not change.

**The m=4 hard-distribution caveat (QS251).** The sentence saying there is no hard distribution at m=4 is literally false under the condition stated at the start of Section 5. Here L=0. Give probability one half each to a^+ and a^0. Every zero-query algorithm succeeds with probability at most one half, hence at most two thirds. What the board lacks is a useful positive query budget and the later hypotheses involving division by L. Replace the blanket nonexistence claim by that exact limitation. The figure remains a schematic illustration of the coupled inputs.

**Question 4’s endpoint (QS256).** The question asks for alpha_tot≥3.5. Fixed k=4 already proves that: every alpha<3.5 has positive power gap 2−1/4−alpha/2. The answer’s k=5 proves the stronger exclusion of a universal inequality at exponent exactly 3.5. The statement that k=4 does not suffice confuses these objectives. Change the question’s target or qualify the answer. This correction strengthens the exercise’s lesson about strict inequalities and an infimum. It does not challenge the proof that alpha_tot=4.

There are two further qualifications rather than substantive errors. The heuristic approximation signs in the introduction should not imply matching values for the family’s R and Q when only a lower and an upper bound are supplied. The phrase that k=2 gives exactly the cube refers only to the leading powers, with logarithmic losses still present. The rigorous ratio argument is already correctly directed (QS204, QS255).

## Prose, weighting and the register detector

The largest prose problem is density at changes of object, not a conspicuous collection of fashionable words. The opening changes from query models to partial functions to a universal exponent to addressed columns. The circuit paragraph changes from normalizations to integer arithmetic to a gate bound. The amplification paragraph changes from a state identity to a randomized procedure to a probability estimate to a stopping-time claim. Give these transitions a named local goal and the exact fact the next step consumes.

Several smaller repairs would pay for themselves. Define certificates before treating stored cells as certificates. Number the genuinely parallel winning clauses so the later reference to the second clause is usable. State the direction of the old AND-OR composition. Define blank cells as zero bits. Condition the erased-zero discovery bound on the observed history so far, not an ambiguously completed transcript. Separate the comparison-cost symbol from the earlier c=delta^2. Put the two acceptance inequalities behind the final classical gap on the page. These are local improvements, not reasons to enlarge the paper indefinitely.

The supplied register measurements partly notice the problem: the long-paragraph examples identify the amplification and direct-product passages. They also generate harmless flags. The semicolons in four winning conditions are mathematically organized parallel clauses; they should be formatted better, not mechanically deleted. The words exactly and checked can describe actual equivalences and examples. A low first-person rate is not evidence that the prose needs more we. Do not optimize the exposition toward the statistical average of specialist papers at the expense of its fixed audience.

The formal section is much improved. Keep the ordinary statement of what was proved and its material difference from the printed family bound. Its practical entry should be the changed-board check of the winning condition, followed by optional model-definition links. A new round should spend most of its space on the quantum mechanism and reading order, not on receipts, checker terminology or status declarations.

## What the revised reader should leave with

The current successful reader can identify a winning column, explain why a domain bit is needed, see why naive nested search is expensive, calculate the ideal drift, and perform the fixed-k exponent comparison. After the next revision the reader should also be able to explain why an unpromised loser does not invalidate comparisons against the winner; why fresh coherent comparisons produce products of actual probabilities; why amplification preserves unequal conditional pivot weights; why no numerical weight table is computed; why sampler failure after the winner is listed is harmless; and why final verification can accept the genuine winner while rejecting malformed candidates at every returned address.

Those are the central quantum lessons. The detailed logarithmic constants and source-checking apparatus are secondary to them. The existing record contains the necessary support; the remaining task is to make the main route carry the operations that the exposition claims to teach.
