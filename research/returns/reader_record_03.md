# Third reading: a more demanding referee-style assessment

Paper: A nearly quartic separation between randomized and quantum queries: a complete reasoning record — 141 pages.

I have gone back through the actual PDF, concentrating on the statements and proof transitions a skeptical mathematical referee would test first. I also independently checked several of the numerical deductions and inspected the rendered pages rather than relying entirely on extracted text.

## My assessment has changed

The paper's main weakness is no longer insufficient explanation. It is that the document has not fully distinguished mathematical proof, mathematical contribution, formal verification, and historical evidence.

That is more important than cutting 20 pages or improving individual sentences.

I did not find a demonstrated contradiction in the central tournament or planted-input reductions during this pass. Several delicate steps that initially warrant suspicion are actually addressed carefully.

But I would not yet call the manuscript independently verified or publication-ready. The main mathematical exposure lies in the independently reconstructed Forrelation argument, particularly §§8.8–8.14, and in the exact relationship between the ordinary proof and its Lean implementations.

Here is what I found on this deeper reading.

## 1. I specifically tested the central mathematical dependencies

Rather than review the prose again in isolation, I followed the proof as if trying to identify a hidden assumption.

### Check A: Is the same total function used in both complexity bounds?

This is essential. Proving an efficient quantum algorithm for one encoding and a classical lower bound for a different encoding would establish nothing.

The paper makes the circuit part of the construction in §4.2, fixes that choice in the quantum analysis and returns to the same choice in §6.6 and §7.

The randomized lower bound is formulated generically for every realizing circuit, while the quantum upper bound uses the specific circuit whose size is controlled.

That is a sound way to organize this dependency. The document explains it explicitly, rather than leaving the reader to infer that the two functions are identical.&#x20;

reasoning_record(4).pdf



Assessment: I do not see an obvious mismatch in the family being bounded.

### Check B: Does the tournament really work with arbitrary losing comparisons?

The key identity in §5.2 is

\\[ \mathbb E[W\_{\mathrm{new}}\mid w] =\frac{W^2-\sum_i w_i^2}{2W}. \\]

I checked the algebra: the diagonal vanishes, and pairing ordered pairs gives the expression precisely because \\(a\_{ij}+a\_{ji}=1\\).

The proof also constructs the two orientations of each comparison from one underlying circuit. That matters: two independently implemented noisy procedures would not automatically have complementary probabilities.

The paper does not make that mistake.

The subsequent argument that a dominant vertex retains weight at least \\((1-\varepsilon)^h\\), until selected, fits the expectation estimate.

Assessment: This is one of the most persuasive parts of the paper. It should be presented as a central mathematical insight, not submerged beneath amplification bookkeeping.

### Check C: Is the planted lower-bound argument improperly conditioning on a rare event?

This is where I would expect a plausible but invalid AI-generated proof to fail.

The paper proves the joint bound

\\[ \Pr[\text{column nonheavy and query visits true cell}] \leq (2/3)^r. \\]

It does not claim that guessing remains hard after conditioning on the column being nonheavy.

The capped simulator follows the original query strategy but stops before exceeding its allowance. When the original query visits the true cell on a nonheavy run, the simulator predicts the true address.

That is an event inclusion under the original product distribution, not an unjustified conditional direct-product theorem. The paper also gives an example showing why the conditional formulation can fail.&#x20;

reasoning_record(4).pdf



Assessment: This is careful mathematics and careful writing. I would preserve it.

### Check D: Is the uniform Forrelation contradiction numerically assembled correctly?

I rechecked an important part of §8.14.

The argument obtains a lower bound on the difference of acceptance expectations of

\\[ \frac{119}{144}a_k, \qquad a_k=18^{-(k-1)}. \\]

The decision-tree indistinguishability estimate is then bounded by

\\[ \frac{a_k}{3}+\frac{a_k}{4} =\frac{7}{12}a_k. \\]

These differ by

\\[ \left(\frac{119}{144}-\frac{84}{144}\right)a_k =\frac{35}{144}a_k>0. \\]

So the final numerical contradiction has a genuine positive margin. This is not merely an asymptotic handwave where two unspecified constants are assumed to work out.

The preceding derivation of the derivative-growth estimate and Gaussian moments remains the more important part to review independently.

Assessment: The final contradiction arithmetic I checked is consistent. This does not independently certify the underlying analytic lemmas.

## 2. The highest-risk passage is not where the paper puts the most emphasis

If I were asked to referee one part of this work, I would focus on §8.8 through §8.14, not on the headline exponent calculation.

The final exponent comparison in §7 is relatively elementary once the quantum and randomized complexity bounds have been established.

Likewise, the addressed-certificate construction is complicated but its logic can be checked locally.

The Forrelation proof is different. It makes several tightly coupled analytic claims:

The Gaussian-chain distribution has the required uniform endpoint. Differentiation moves through the successive blocks with repeated-coordinate terms vanishing. The resulting path derivatives are controlled by a biased decision-tree martingale. The rounded distribution has sufficient positive Forrelation expectation. Finally, the comparison of these two input distributions forces randomized hardness even though neither distribution is entirely supported on the promise.

The paper explains these steps. But there is a significant distinction between explaining them convincingly and independently validating them.

### The proof of the uniform endpoint

Section 8.8 argues that \\(\nu_0\\) is uniform by clearing biases through Gaussian reflections.

I followed the logic: the selected reflection changes one coordinate of the transformed Gaussian vector, while its effects on the previous block no longer matter because that block has already been cleared.

This is a clever argument.

It deserves a standalone lemma with its induction invariant displayed explicitly. Currently the proof is embedded within the construction of the Gaussian chain.

An external referee should be able to see immediately which variables are allowed to change under the reflection and why those changes do not affect uncleared blocks.

### The path derivative identity

Equation (F22) is another essential checkpoint.

The argument depends on taking a derivative in one coordinate of each block and avoiding terms where a coordinate is differentiated twice.

The three-block derivation is helpful. But the general proof follows it rather quickly.

I would make the induction invariant a formal lemma before (F22), separating the combinatorial statement about paths from the analytic integration-by-parts justification.

A reader should not have to identify both arguments simultaneously.

### The derivative-growth lemma

Equation (F25) is probably the most valuable independent review target.

It establishes a bound on the sum of absolute mixed derivatives of a bounded-depth decision tree under a biased product distribution.

The proof uses centered variables, contraction of coefficient arrays, stopping and a maximal martingale bound.

I checked the outline of the stopping argument. Importantly, it stops before an uncontrolled increment rather than conditioning on the future event that every coefficient bound holds.

That distinction is correct and explicitly discussed.

Nevertheless, I would want a specialist to review the full induction, including the treatment of repeated queries and the passage from the terminal process to the sum of absolute derivatives.

This is where another AI prose review provides diminishing returns. The next meaningful increase in confidence would come from independent mathematical scrutiny of (F16), (F22), (F25) and (F39)–(F43).

## 3. The claimed quantitative contributions are not ranked properly

This is a new, fairly important criticism of the opening.

The paper advertises three particularly concrete refinements: the threshold \\(t\geq13669k^2\\), the logarithmic exponent six and the coefficient \\(1/400\\).

Those are not equally important.

The coefficient \\(1/400\\) comes from explicit budget choices and two floor estimates. It is useful for a checkable statement but not a major conceptual contribution.

The threshold \\(13669k^2\\) is similarly a sufficient threshold obtained from the proof's inequalities. It should not be confused with a sharp hardness threshold.

The genuinely interesting additional result is the uniform Forrelation bound

\\[ R(P\_{k,m})> \frac{2m^{1-1/k}}{18225k^2\ln(4km)} \\]

in the stated dimension range.

That gives an explicit parameter dependence feeding into the growing-\\(k\\) analysis in §7.3. The paper's own comparison notes its better dependence on \\(k\\) and worse logarithmic dependence relative to the published Bansal–Sinha estimate.&#x20;

reasoning_record(4).pdf



That deserves more attention than the numerical constant \\(1/400\\).

I would reorganize the contribution statement so that the conceptual and quantitative theorems come first, with deliberately loose constants presented as evidence that the estimates are explicit rather than as primary achievements.

I also checked the growing-parameter schedule in the rendered PDF. It is

\\[ k(t)=\left\lfloor\sqrt{t/20}\right\rfloor, \\]

not \\(\lfloor\sqrt t/20\rfloor\\), which can appear from imperfect text extraction. The radicand matters. The displayed choice is consistent with the later balancing calculation.

The schedule's numerical exponent bound is quite loose at modest \\(t\\), which the paper acknowledges. I would distinguish clearly between the interesting asymptotic statement and the fact that the conservative constants make its finite-dimensional guarantee uninformative for many initial parameters.

## 4. The ordinary proof and Lean proof do not always follow identical routes

This is the most important issue for how you present the formalization.

Appendix G makes clear that the mathematical account and the formalized development do not have a one-to-one correspondence between every proof route.

There are at least two particularly important examples.

The tournament: The ordinary presentation proves the bounded-list result and uses that to explain the upper bound. The headline Lean proof uses the measured-label and Boolean-continuation route. A separate bounded-list theorem exists, but it is not on the headline proof's dependency path.

The universal quartic bound: Appendix A reconstructs the star-adversary argument, giving coefficient \\(35^4\\). The headline Lean result uses the separate complexity-library route, with a different constant. Other formal routes are also documented.

This is not a mathematical defect. Different valid proofs of the same result are perfectly acceptable.

But it creates a presentation problem: the phrase formalization accompanies the mathematical account can easily be interpreted as meaning the exact printed proof has been formalized step by step.

That is stronger than the evidence supports.

The paper itself is appropriately careful in G.7 and G.9. The distinction needs to move much earlier.

I would use a direct correspondence table in the main introduction or at the start of Appendix G, identifying where the printed proof and formal proof share a mathematical statement but take different routes.

The reader should not discover this only after 130 pages.

A second concern is that the paper describes historical source comments saying “UNELABORATED” even though later source-bound receipts establish successful builds.

If those comments remain in the current repository, update them. It is better to make the source and paper agree than to devote paragraphs to explaining why the source comments are outdated.

## 5. Appendix E creates a reputational burden larger than its value to the main proof

I reread the source-comparison material, particularly the claimed discrepancies in Bansal–Sinha and Špalek–Szegedy.

The paper is careful not to claim that identifying a displayed-step discrepancy refutes the surrounding theorem.

That qualification is important.

But consider the situation from an outside referee's perspective.

They have received a 141-page AI-written reconstruction of a recent major result, with no human mathematical review. Before accepting its independent reconstruction, they are also being asked to consider claims about errors in established papers.

Those claims may be correct. I have not independently adjudicated them against all relevant source versions.

But they impose an additional verification burden and may distract from the paper's actual purpose.

The complete proof of the desired Forrelation bound is presented as independent of the disputed Bansal–Sinha calculation. So the source discrepancy is not required for the main mathematical argument.

I would leave the passage-specific analysis available in Appendix E but stop raising it in the opening reading guide. I would also recommend independent confirmation before promoting any disputed correction outside a narrowly qualified technical note.

This would make the paper more credible, not less transparent.

## 6. The first page still looks like an internal reconstruction, not a finished paper

I inspected the rendered page again.

The current first page has a title, several introductory paragraphs, an authorship disclosure and a reading guide.

It does not have a conventional author byline, a clearly identified abstract, a version date or a visible permanent publication identifier.

The PDF metadata also has empty title and author fields.

There is another problem in the first paragraph's citation punctuation. The references to Aaronson et al. and OpenAI are incorporated in a way that reads as unfinished prose rather than a properly punctuated citation.

These sound superficial compared with the mathematics. But an expert who has received a cold PDF will notice them before seeing any of the actual proof.

The paper is already sufficiently long and technically ambitious to create a high initial burden of trust.

The first page should reduce that burden.

It should immediately answer who wrote it, what source result is reconstructed, what its principal additional content is, whether it is peer-reviewed, where the source lives and how to reproduce its verification claims.

That can be done cleanly without weakening the AI disclosure.

## 7. The archival material should stop competing with the mathematical results

My previous advice to cut or relocate content was too broad. I would now draw a sharper distinction.

The full direct-product proof, circuit construction, finite budget, Gaussian argument and quartic upper-bound derivation belong in the record. They are the substance.

The original-claim catalogue, previous receipt history, historical threshold and external-source audit also have value.

But the current document spends considerable space narrating the sequence in which those checks were produced.

In Appendix F, for example, different paragraphs describe source snapshots, checks that were or were not rerun in different rounds, which file headers are obsolete and which receipts supersede older evidence.

These are legitimate provenance facts. They are not an efficient way to communicate the present mathematical status.

I would preserve the complete historical information in the repository and summarize the current state in the paper.

A useful editorial test is:

If a sentence would become irrelevant solely because the next review round has finished, does it belong in the mathematical exposition?

Often the answer is no. It belongs in a dated verification record.

This would also stop the paper from requiring constant synchronization with a changing audit workflow.

## 8. The release PDF still has a concrete reproducibility problem

I inspected the PDF's link structure directly.

It contains 82 relative-file links to local Markdown, JSON, Python and other resources, including paths under `../research/returns/round3/...`.

That is not a stable external distribution format.

A researcher who receives only the PDF cannot be expected to reconstruct the repository directory structure.

Because the paper explicitly relies on some of these files as finite-check evidence, unavailable links affect the document's practical auditability.

I would produce a release edition in which every external supporting file has a stable URL at a pinned commit. Internal mathematical cross-references can remain PDF destinations.

I also found that the PDF has no embedded title or author metadata, even though it contains a substantial internal bookmark structure.

The metadata and relative links are easy to fix and disproportionately important for a standalone document.

## 9. What I would ask an actual referee to verify

If this were being circulated for external mathematical review, I would not ask someone to read the entire 141 pages without direction.

I would send three sharply defined verification questions:

1\. Forrelation: Do (F16), (F22), (F25) and the moment calculation (F39) legitimately imply the uniform hardness statement (F43), with the specified one-sided promise and parameter dependence?

2\. Quantum algorithm: Do the coherent comparison, exact sampled-label law and fixed-cap amplification produce the stated worst-case ordinary bit-query bound, including on off-promise inputs?

3\. Classical reduction and formal semantics: Does the capped simulator correctly turn a true-cell query on a nonheavy run into a prediction of all hard address bits, and do the formal models faithfully represent the capped randomized and quantum complexities used in the printed theorem?

These are meaningful, bounded requests. A reviewer could provide a substantive answer without having to adjudicate every historical receipt or all 121 catalogue entries.

That would be much more valuable than another general AI assessment.

## 10. What I would change immediately

My priority order is now narrower than before:

| Priority | Change                                                            | Expected benefit                                       |
| -------- | ----------------------------------------------------------------- | ------------------------------------------------------ |
| 1        | State the mathematical contribution hierarchy clearly on page one | Fixes authorship and novelty ambiguity                 |
| 2        | Give the uniform Forrelation result (F43) greater prominence      | Exposes the main additional mathematical substance     |
| 3        | Make §8's key invariants more explicit                            | Makes the highest-risk proof easier to referee         |
| 4        | Map ordinary proof routes to actual Lean dependency paths         | Prevents overstating formal coverage                   |
| 5        | Move historical receipt narration out of the principal PDF        | Improves scholarly readability without losing evidence |
| 6        | Remove source-error discussion from the opening reading guide     | Keeps attention on the paper's own results             |
| 7        | Repair release links, metadata and bibliography formatting        | Makes the document independently usable                |

## Final judgment after this third reading

I would rate the manuscript differently depending on its intended role.

As a complete mathematical reasoning and verification record, I think it is strong: approximately 8/10 for organization and explanatory completeness.

As a standalone paper sent cold to a quantum query-complexity researcher, I would put it closer to 6.5–7/10. That is not because the mathematics is uninteresting, but because the document asks the reader to negotiate too much provenance, too many equally weighted refinements, and too many different proof and verification routes.

As an independently validated mathematical result, I cannot assign a positive verification judgment from these readings alone. The formal evidence is substantial as described, but the semantic correspondences and the analytic reconstruction still merit external expert checking.

The core sections have reached a level where I would actively discourage another wholesale AI rewrite. The construction and the quantum/classical reductions are not crying out for more words. The highest-value improvements are clearer intellectual positioning, a much more referee-friendly presentation of §8, and a cleaner distinction between current formal results and the history of their verification.

My strongest conclusion is this: the manuscript has become a credible object for serious mathematical review, but it has not yet become an especially efficient object to review. That is the remaining editorial problem worth solving.