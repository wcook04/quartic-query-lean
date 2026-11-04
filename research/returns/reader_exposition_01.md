# Critical review of the revised exposition

Paper reviewed: Why OpenAI’s query separation is nearly quartic — An examples-first explanation of the optimal randomized–quantum exponent · 27 pages · November 2026

## Overall assessment

This is now a genuinely substantial mathematical exposition. It has a coherent teaching strategy, a well-defined audience, carefully chosen examples, and an unusually serious attempt to explain the mechanisms that make the proof work rather than merely reproducing its calculations.

I would distinguish three judgments:

| Criterion                                                   | Assessment |
| ----------------------------------------------------------- | ---------- |
| Mathematical exposition for a technically capable reader    | 8/10       |
| Accessibility to a new reader with the stated prerequisites | 6.5–7/10   |
| Polish as a standalone, publishable expository article      | 7.5/10     |

These are editorial assessments, not scores for mathematical correctness or originality.

The strongest feature is that the paper repeatedly makes abstract proof obligations concrete. The four-column board, off-promise certificate, cyclic comparison example, fractional sampling matrix and capped simulator are not decorative examples. Each addresses something a reader might otherwise misunderstand.

The largest remaining weakness is the distance between explaining individual proof mechanisms and giving the reader a manageable understanding of the whole proof.

The manuscript explains many hard steps well. But it sometimes tries to teach every subtlety, repair every possible misunderstanding, account for every implementation detail and retain research-level precision in a single reading path. The result is more demanding than the stated prerequisites suggest.

I would describe the current paper as:

> An ambitious, technically detailed guided reconstruction of a sophisticated query-complexity proof, with exceptionally concrete examples, but still somewhat overburdened by implementation and proof-accounting details.

That is a respectable scholarly product. It is not generic AI-generated explanatory prose. The remaining editorial problems are largely problems of selection, emphasis and mathematical communication, rather than a lack of content.

The appropriate benchmark is not a popular-science article. It is an advanced exposition for mathematically mature readers, including graduate students and researchers outside quantum query complexity.

Against that benchmark, much of the paper now works very well.

## 1. Where the writing is strongest

### The first three sections establish a real teaching sequence

The progression from eight-bit examples to a four-column board is very effective.

On pages 2–3, the three inputs \\(a^+\\), \\(a^0\\) and \\(a^-\\) establish three genuinely different cases: a positive promised input, a zero promised input and an off-promise input.

This is more than illustrating a definition. The negative example becomes relevant to the certificate failure in Section 2 and to the behavior of the comparison algorithm in Section 4.

That reuse is important. It means the examples are doing explanatory work throughout the paper.

The quantum projection calculation on page 3 is particularly good. You actually show the state changing under the two input-dependent diagonal matrices, explain phase kickback, and distinguish a signed amplitude from its squared measurement probability.

Crucially, the reader sees why the negative example can pass the projection experiment even though it is outside the promise. That gives the later domain-bit certificate a reason to exist.

Section 2, pages 4–6, is probably the best piece of introductory exposition in the manuscript.

[PPT - Quantum Certificate Complexity PowerPoint Presentation, free download - ID:1034990](https://images.openai.com/static-rsc-4/qK1m0TjC9y39HBOUvngy3hqTWoIK66A8R8J8Rc4hnm8qfhnEH0Je95RCM4AGPIM_Nx3Yer4rZU-sHIm2n9mRGGCS4B_NEZ8H5U78rblv3N2UvY5YI7ZvJ7NTaGURBwd4g7WQWMK8cSxbv51NThGEKXpaAnntk1kEXCiAtqRJtO0?purpose=inline)

Figure 2, page 5

The actual PDF figure is successful because it shows the winner, its outgoing pointers, the address cells and a failed rival pointer in one picture. The surrounding text then establishes why the winner is unique.

The board diagram is followed by the general formal layout, circuit transcripts and local tests. The small NOT–OR gate example on page 6 is particularly valuable: it explains why locally consistent fragments of a false transcript cannot make an entirely false transcript pass.

That is exactly the sort of detail which a conventional research paper would omit and an exposition should supply.

There is one remaining accessibility problem here: the reader is asked to move quickly from the actual four-column board to a general family involving \\(k,t,m,r,\ell,S\\). The mathematical transition is legitimate, but it comes before the reader has quite finished forming a mental picture of the small construction.

I would add a short recap of the board's components before introducing the parameters.

### The treatment of the quantum tournament is unusually good

Section 4 is where the paper becomes most distinctive as an exposition.

The introduction on page 8 makes the central algorithmic improvement clear: directly searching over columns and verifying every candidate within the search multiplies two costs, whereas comparisons allow a shortlist to be formed before paying the expensive verification cost.

That is the conceptual heart of the quantum upper bound, and the paper identifies it properly.

The progression through the different kinds of nonwinner is excellent.

The false-pointer mutation on page 9 demonstrates that a column can dominate every comparison yet still fail certification. The three-loser cycle demonstrates why those comparisons cannot simply be treated as an ordering.

These examples establish why both the tournament and final verification are necessary.

The probabilistic analysis on page 11 is also very well chosen. The weighted-halving identity,

\\[ \mathbb E[|w'|\mid w]\leq \frac{|w|}{2}, \\]

is not merely stated. You derive it from the pairwise identity \\(a\_{ij}+a\_{ji}=1\\), then relate it to the concrete cyclic board.

The reader learns something quite general: global progress can be proved without a total order and without understanding the comparisons among losing candidates.

That is an elegant mathematical idea, and it is communicated well.

The explicit sampler contract at the beginning of Section 4.3, page 12, is another major strength. You specify the conditional distribution, the fixed query cap, the success threshold and the failure behavior before presenting the reversible implementation. That is the correct pedagogical order.&#x20;

exposition(2).pdf



The fractional comparison matrix on page 13 is also useful. It demonstrates that the sampler must produce genuinely weighted labels, rather than simply choosing uniformly among columns with nonzero weights.

### The classical lower-bound section is the strongest sustained argument

I think Section 5, pages 16–21, is the paper's most impressive stretch of explanatory writing.

The planted pair creates a particularly good narrative. The dummy and planted inputs differ in only two locations: an erased zero and a filled certificate cell.

The rest of the lower bound becomes an explanation of why a limited classical algorithm is unlikely to encounter either difference.

The three-charge table on page 18 is useful because it decomposes a complicated adaptive argument into distinguishable failure mechanisms.

But the best material comes on pages 18–20, where you explain why querying a cell is itself an address prediction.

The distinction between a cell position and the bits stored at that position is easy to miss. You make it explicit: the algorithm need not read the certificate or compute the address to have guessed the address through its query coordinate.

This is an excellent explanation of the underlying reduction.

The discussion of heavy and light runs is also more careful than typical pedagogical accounts. You correctly avoid claiming that a predictor is hard conditional on remaining light. Instead, the simulator gives an unconditional bound on the joint event.

The separate-cap lemma, the stop-before-read simulator, and the two-clock XOR example work together well. They explain not just what is true but why the most tempting alternative proof would be invalid.&#x20;

exposition(2).pdf



I would preserve most of Section 5. Cutting it aggressively would remove some of the paper's real value.

### The exponent argument is precise

Section 6 succeeds at something many expositions mishandle: the order of quantifiers.

You choose the claimed universal exponent, fix a suitable \\(k\\), and then send \\(m\\) to infinity.

The discussion of why the fixed-\\(k\\) result cannot automatically be turned into a growing-\\(k\\) family is especially careful.

The final return to the board on page 22 is effective because it reconnects the abstract exponent calculation to the two mechanisms the paper has taught.

This is a good ending to the mathematical exposition.

## 2. The biggest remaining writing problem: too much information competes for attention

The paper is clearer locally than it is globally.

By that I mean individual paragraphs usually answer reasonable questions, but the reader has to remember an enormous number of definitions and proof obligations across sections.

Consider the reader's experience.

The first pages introduce partial functions, signs, Walsh transforms, projections, query oracles and the promise. The next few pages introduce addresses, pointers, circuits, transcripts, local tests and certificate verification.

Then Section 3 introduces the large asymptotic family and its parameters. Section 4 adds comparison probabilities, pivot histories, weights, coherent workspaces, amplitude amplification, error budgets and Grover search. Section 5 adds a hard distribution, two coupled inputs, heavy columns, an adaptive simulator, two query clocks and the direct-product argument.

Each object is justified. But the paper does not do enough to distinguish which objects are central ideas and which are technical machinery.

I would add a one-page proof map before Section 1.

It should show the complete construction as three components:

- A hard partial function supplies hidden certificate addresses.
- A pointer board turns those addresses into a total Boolean function and permits cheap quantum comparisons.
- A planted distribution forces classical algorithms to locate a column or predict an address.

Alongside that, show the two costs:

\\[ Q(F\_{k,m})\lesssim_k \sqrt m\\,\operatorname{polylog}m, \qquad R(F\_{k,m})\gtrsim_k \frac{m^{2-1/k}}{\operatorname{polylog}m}. \\]

Then explain that the paper will construct and justify each ingredient.

Currently, that complete picture only gradually emerges. The introduction offers the ingredients, but not quite a sufficiently explicit architecture.

A small notation table would also help enormously. In particular, distinguish \\(m\\), \\(k\\), \\(r\\), \\(\ell\\), \\(K\\), \\(L\\), \\(G\\) and \\(T\\). The manuscript is careful with them; the reader's memory is the problem.

## 3. Section 4.3 needs a more disciplined separation between algorithm and proof

Pages 12–14 are perhaps the clearest example of the manuscript's remaining limitations.

The section has to establish four things: a reversible preparation produces the required joint masses; conditioning on success yields the ideal pivot law; amplitude amplification preserves that conditional law; and a bounded schedule achieves the required success guarantee.

Those are four conceptually separate facts.

At present, they form one long sequence of explanatory prose, linear algebra, examples and implementation details.

A specialist can follow it. A reader who has only the stated prerequisites may lose track of why a particular calculation matters.

I would introduce a visibly separate sampler algorithm immediately after the contract. It should take a classical pivot history, prepare a uniform column register, run fresh comparisons against every pivot, mark success when all comparisons are won, apply bounded amplification, and return the measured label on success.

Then prove the four obligations against that displayed algorithm.

This would reduce the amount of conceptual translation readers must perform.

The fractional matrix and the amplitude-amplification calculation should remain. They are substantive. But the reversible bookkeeping could be compressed slightly, and the explicit amplification schedule is already appropriately placed in Appendix A.3.

The target is not to shorten the mathematics. It is to make the reader know which claim each paragraph is establishing.

## 4. The paper promises slightly greater accessibility than it delivers

The introduction says that the prerequisites are finite-dimensional linear algebra, elementary conditional probability and asymptotic notation.

Taken literally, this makes the paper sound accessible to a strong undergraduate without much further preparation.

The beginning substantially supports that claim. The treatment of quantum states and the oracle is approachable.

But the reader subsequently needs to understand or rapidly learn several sophisticated styles of reasoning: coherent reversible computation, quantum amplitude amplification, Yao minimax, adaptive decision trees, conditional success probabilities, direct-product arguments and probabilistic couplings.

These are not merely additional definitions. They require mathematical proof maturity.

I would describe the audience more accurately as:

> Mathematically mature readers familiar with asymptotic algorithms and probability, but not necessarily with quantum query complexity. The relevant quantum operations and problem-specific proof mechanisms are developed from first principles.

That wording preserves the ambition without making the advanced material seem unexpectedly difficult.

There is also a real difference between being self-contained enough to reconstruct a proof and being accessible on a first reading.

The paper is increasingly successful at the former, but only moderately successful at the latter.

## 5. Some of the meticulousness is beginning to undermine the prose

The paper frequently anticipates and answers possible objections.

This is sometimes excellent. The distinction between a conditional light-event bound and a joint-event bound in Section 5 absolutely deserves space.

But the cumulative result is that the manuscript occasionally reads like a combination of an exposition, a proof verification report and a response to previous reviewers.

Three examples stand out.

On page 6, the paragraph about certificate complexity and the recent Ben-David–Kothari construction interrupts the explanation of this board's certificates. It is relevant scholarly context, but it does not help the reader understand the immediately following local tests.

On page 10, the discussion of why quantum minimum finding and bounded-error search cannot be imported directly is mathematically relevant, but rather specialist. It could be a short remark outside the main teaching sequence.

On page 23, the explanation that a historical “unelaborated” source comment predates later build and axiom evidence is far too repository-specific for the main text of an exposition.

That last sentence belongs in a verification-status appendix or repository documentation, not in the mathematical reading path.

This is the paper's most noticeable residual form of overengineering: too much effort is spent demonstrating that every anticipated objection has been addressed, including objections that an ordinary reader would never have encountered.

That is different from imprecision. The solution is mostly to move material, not discard rigorous work.

## 6. The proof-status and attribution language needs another pass

The introductory attribution is commendably clear: the mathematical theorem and original construction are credited to OpenAI.

But the theorem statement on page 8 creates a subtle presentation problem.

It is labeled as OpenAI's Theorem 1.1, then gives particular quantitative bounds, including the \\(1/400\\) coefficient and sixth logarithmic power, which the text describes as explicit choices in this reconstruction.

The attribution is potentially ambiguous.

I would label the quantitative result as a bound derived here from the OpenAI construction, and separately identify the optimal-exponent theorem as the original result. That makes the scholarly contribution of the exposition clearer without overstating it.

Similarly, page 2 says three deeper results are accepted inputs, but other arguments rely on standard amplification guarantees and a near-linear exact circuit construction whose full detail is deferred to the reasoning record.

This is defensible mathematically, but it would be more precise to distinguish research-level imported theorems, standard algorithmic subroutines, proofs supplied in the exposition, and details deferred to companions.

The source reference has an embedded link to the OpenAI GitHub preprint, which is good. Its visible bibliography entry, however, ends with the local-looking filename `quartic-query-separation.pdf`. Give the reader a plainly recognizable public source address and version identifier as well.

I also inspected the PDF's embedded links. Several reasoning-record, expert-companion and Lean links point to older pinned commit hashes rather than the revision hash `071ce02` you report. That may be intentional for reproducibility; if so, label them as fixed snapshots. Otherwise, check that readers are directed to the versions corresponding to this exposition.

## 7. Section 7 is good material in the wrong location

The Lean section demonstrates commendable attention to what formal verification actually establishes.

In particular, it distinguishes Lean checking proofs of formal statements from checking whether those statements express the intended mathematics. That is an important and appropriately restrained claim.&#x20;

exposition(2).pdf



The concrete invitation to find the `f (readA x i h) = some (s h)` clause is also a useful way to connect the paper's domain-bit board with the formal source.

The issue is placement and level.

Section 6 has already provided the paper's conceptual conclusion. The reader has arrived at the fourth power and returned to the four-column example. Then Section 7 changes register into challenge-file locations, comparison bundles, named-circuit theorem scope and historical source comments.

For a Lean-interested reader, this is worthwhile. For someone reading a mathematical exposition, it weakens the ending.

I would make the Lean material an explicitly optional appendix, or move a short statement-scope table into the main body and retain the detailed directions in the reasoning record.

The mathematics should remain the emotional and intellectual conclusion of the article.

## 8. Presentation and typesetting

The diagrams are generally well designed. Figure 2 on page 5 communicates the board unusually well, Figure 3 on page 10 captures the comparison cycle, and Figure 4 on page 17 makes the planted-pair change visually immediate.

The use of color is restrained and functional.

However, the page layout still has some obvious rough edges.

Page 16 contains the start of the classical lower-bound proof and then leaves a very large blank area because Figure 4 begins on the following page. Page 10 has a similarly substantial empty lower portion; its closing sentence introduces an example table that does not appear until page 11.

These are noticeable in a relatively short paper, especially because the surrounding pages are extremely text-dense.

Page 13's matrix calculation is correct in its rendered form, but the inline matrix product is cramped. It would benefit from display treatment. More generally, several mathematical explanations would become easier to read if a key displayed equation were immediately followed by a short interpretation rather than another dense calculation.

The body font and figures look serious and appropriate for a mathematics document. The problem is not aesthetic taste. It is uneven information density and figure placement.

## 9. The highest-value edits for the next revision

I would prioritize the following, in order:

1\. Add a one-page mathematical overview. Show the partial function, addressed certificate, tournament, planted pair and final exponent before giving the construction's details. Include a compact notation legend.

2\. Reorganize Section 4.3 around four explicit proof obligations. Keep the reversible details and the fractional example, but make the sampler itself visible as an algorithm before proving it works.

3\. Move the most specialist digressions out of the main reading path. Especially repository-status discussion, tangential certificate-complexity comparisons and a few implementation-level details already covered in the reasoning record.

4\. Make the provenance and dependency claims exact. Separate OpenAI's theorem from your reconstructed quantitative bounds; clarify which ingredients are proved, quoted or deferred; and resolve the version-pinned links.

5\. Fix the layout. Reflow Figures 3 and 4, eliminate the large blank half-page in Section 5, and avoid separating table introductions from their tables.

I would not substantially rewrite Sections 2 or 5. They are among the strongest parts of the manuscript and should serve as stylistic models for the rest.

## 10. Would I consider it a good paper?

Yes, in the specific sense that matters for an expository paper: it contains enough mathematical substance, explanatory originality and deliberate pedagogy to justify reading it rather than simply reading the original theorem.

Its main contribution is not a new query-complexity result. It is a route through an existing proof that makes otherwise easily missed mechanisms visible.

The best examples are the failed promise certificate, the dominating nonwinner, the fractional sampling law and the capped address predictor. A technically serious reader may obtain real understanding from those that the original specialist presentation does not provide as directly.

But I would not call it fully finished.

The strongest criticism is that the exposition has become almost too conscientious. It includes nearly everything necessary to defend the argument and every subtlety you have identified. A polished expository article must make an additional editorial choice: which things deserve to occupy the reader's attention at each moment.

The next improvement is therefore unlikely to come from adding more mathematical details, more defensive clarifications or more literature comparisons.

It will come from making the proof's hierarchy much more visible.

My final judgment: This is a credible advanced mathematical exposition with several genuinely excellent passages, especially in Sections 2, 4.2 and 5. Its remaining weaknesses are primarily architectural and editorial. A further revision that improves the global map and removes distractions could plausibly move it from a strong technical teaching manuscript to a very polished standalone expository article.

I assessed the actual attached 27-page PDF, including its mathematical text, diagrams, appendices and rendered layout. I did not independently recheck the external source theorem, the Lean proofs or the reported test suite; those require a separate correctness audit.