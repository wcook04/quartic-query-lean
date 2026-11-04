# Second reading: a deeper critique of the exposition

Reassessment of Why OpenAI’s query separation is nearly quartic · 27-page attached PDF

My judgment has changed slightly after following the construction and its proof obligations again.

I think the manuscript is stronger mathematically as an exposition than my previous review conveyed, but less successful at controlling the reader's attention. The difficulty is not simply excessive length. It is that the paper sometimes gives secondary technical details almost the same prominence as the central mathematical discoveries.

There is an important distinction here. I would not recommend substantially simplifying the hard arguments. The details about reversible sampling, conditional probability, adaptive queries and certificate verification are precisely what make this exposition valuable.

Instead, I would make the hierarchy of the argument more visible, so that a reader can distinguish:

1. What the algorithm actually does.
2. Why its central mechanism works.
3. What is needed to make the proof completely rigorous.
4. Which facts are imported from existing results.

The manuscript contains all four kinds of information, but their boundaries are not always clear.

## 1. The most important finding: the paper has two excellent explanations that are not yet fully connected

The central achievement is a pair of complementary ideas.

The quantum argument: A real winning column has a special property: it beats every rival with very high probability, even when comparisons between other columns are arbitrary, cyclic or noisy. A quantum algorithm can exploit this property to collect a short list, then verify the candidates.

The classical argument: A planted winner differs from the dummy input in a hidden zero and a hidden certificate cell. Finding the cell, even by a guess, amounts to predicting a collection of hard partial-function answers.

Those really are the two halves of the nearly quartic phenomenon.

The exposition explains them separately very well. But it could establish their relationship much earlier.

For example, the reader should understand before entering the technical sections that the enormous array of certificate cells is simultaneously helpful to the quantum algorithm and hostile to the classical one.

Quantumly, the cells are affordable because the algorithm follows only a small number of pointers and verifies only a shortlist. Classically, the hidden location of the correct cell makes even choosing which stored bit to read informative and therefore difficult.

This is the architectural insight that should govern the whole exposition.

At present, the reader is given many ingredients on page 1, but has to assemble that unified insight gradually over another twenty pages.

I would add a short paragraph to the introduction explicitly describing this asymmetry as the central design principle of the construction.

## 2. The quantitative story needs to arrive sooner

One reason the quantum algorithm is difficult to appreciate on first reading is that the text repeatedly calls comparisons cheap without immediately making their cost concrete.

The relevant calculation is straightforward once the earlier definitions are assembled.

The address length is \\(r=20\log_2m\\). For fixed \\(k\\), decoding each partial-function answer to sufficiently small error costs logarithmically many queries. A comparison decodes two addresses and follows two pointers, giving a polylogarithmic query cost.

By contrast, verifying one complete certificate means searching roughly

\\[ K=O_k\\!\left(m(\log m)^3\right) \\]

local tests, which costs on the order of \\(\sqrt m\\) queries, up to logarithmic factors.

This is the critical cost separation:

| Operation                                     | Query scale for fixed \\(k\\)             |
| --------------------------------------------- | ----------------------------------------- |
| Compare two columns                           | \\(\operatorname{polylog}(m)\\)           |
| Verify one candidate column                   | \\(\sqrt m\\,\operatorname{polylog}(m)\\) |
| Direct Grover search with verification inside | \\(m\\,\operatorname{polylog}(m)\\)       |
| Tournament and shortlist verification         | \\(\sqrt m\\,\operatorname{polylog}(m)\\) |

The paper eventually establishes these estimates, including the detailed accounting in Appendix A.1. But an introductory version of this table belongs at the beginning of Section 4, before the reader encounters the comparison probabilities \\(a\_{ij}\\).

Otherwise, the reader has to study a sophisticated tournament without yet having a sufficiently vivid sense of why a tournament is needed.

This would be one of my highest-priority edits.

## 3. I checked the mathematics at several of the places where a reader has to trust the exposition

I went back through the numerical examples, the quantum sampler and the classical lower-bound bookkeeping rather than treating them as illustrative prose.

The spot checks are reassuring.

The three eight-bit Forrelation examples on pages 2–3 have signed values \\(1,0,-1\\), as stated. The additional projection exercise gives amplitude \\(1/2\\) and success probability \\(1/4\\).

The fractional comparison matrix on page 13 also behaves as advertised. After pivot 2, its weights are

\\[ (1,0,2/3,1/4), \\]

so the preparation succeeds with probability \\(23/48\\). Following pivot 4, they become

\\[ (1,0,4/15,0), \\]

giving the conditional distribution \\((15/19,0,4/19,0)\\). These calculations agree with the supplied answers.

The expected-weight calculation in Section 4.2 also checks out:

\\[ \mathbb E[|w'|\mid w] = \frac{|w|^2-\sum_i w_i^2}{2|w|} \leq \frac{|w|}{2}. \\]

The distinction between this expectation bound and a guaranteed reduction on every history is correctly maintained.&#x20;

exposition(2).pdf



The resulting error accounting is consistent with the selected \\(T\\) and \\(\varepsilon\\). For instance, at \\(m=4\\), the formula gives \\(T=12\\) and \\(\varepsilon=1/12000\\), yielding the advertised error budget.

In Section 5, the final three charges also combine in the stated way, and the exponent argument in Section 6 uses the quantifiers in the correct order.

I did not find an obvious numerical contradiction in those checked passages. That is not the same as independently proving the entire construction. In particular, I have not audited the original Forrelation lower-bound theorem, the complete exact-circuit construction, or every deferred argument in the reasoning record.

There are, however, several more subtle issues with how the mathematical claims are presented.

### The exact circuit is doing more work than its exposition suggests

On page 7, the text introduces an exact Boolean circuit satisfying

\\[ S\leq 200(k+1)^2m(\log_2m)^2. \\]

It then sketches how Walsh transforms and integer comparisons give such a circuit, with the full construction deferred to the reasoning record.

The reader needs to understand that this is not incidental background. The near-linear circuit size is necessary for the quantum verification cost.

If the transcripts were too large, checking them by quantum search could destroy the nearly square-root query bound.

I would give this a named statement, perhaps Circuit-size lemma, followed by a plain-language explanation of exactly what the upper-bound argument needs from it.

The exact constant 200 is not pedagogically important at first encounter. It belongs in the quantitative statement or an appendix. What matters is the \\(O_k(m\log^2m)\\) gate count and exact correctness on both promised and unpromised inputs.

### The amplification schedule is partly proved here and partly deferred

Pages 13–14 do a good job showing why amplitude amplification preserves the relative probabilities within the successful subspace.

But the finite schedule's quantitative guarantee is subsequently imported, with the trigonometric estimate deferred to the reasoning record.

That is acceptable in an exposition. It should simply be presented as an explicitly named subsidiary result, rather than letting the reader infer that the preceding two-dimensional rotation calculation has already proved the entire fixed-cap guarantee.

I would distinguish the statements:

Preservation: Successful amplification outputs the correct conditional pivot distribution.

Success guarantee: A specified randomized schedule achieves sufficiently high success probability whenever the preparation probability exceeds the threshold, within a bounded number of queries.

They require different arguments. The first is substantially explained in the main paper; the second is deferred.

That distinction improves mathematical transparency without adding another proof.

## 4. Section 4 contains a particularly elegant conceptual separation that deserves more emphasis

I missed the full value of this on the first reading.

The quantum tournament's analysis separates two properties that readers might assume are inseparable.

The expected-halving argument needs only

\\[ a\_{ij}+a\_{ji}=1. \\]

It does not need a genuine winning column, transitivity, deterministic comparisons or even a meaningful underlying ordering.

The additional property

\\[ a\_{i^\star j}\geq1-\varepsilon \\]

is used separately to ensure that the genuine winner retains sufficient weight until sampled.

This division is beautiful.

The first fact establishes that the search process makes global progress in an arbitrary stochastic tournament. The second establishes that a particular important vertex cannot disappear too soon.

The paper proves both, but could state the division far more prominently.

I would make them two small lemmas with descriptive names: expected mass reduction and winner preservation. Then the quantum sampling construction becomes an implementation lemma realizing the abstract process.

The reader could hold three statements in mind instead of several pages of continuously developing notation.

### The word “winner” is overloaded

There is also a small but persistent terminology problem.

The manuscript uses winner for a column possessing a valid global certificate, and winning a comparison for a pairwise outcome. Later, a dominating nonwinner defeats every rival without being a genuine winner.

The prose repeatedly explains the distinction, but that repetition is evidence that the terminology still places a burden on the reader.

I would consistently use valid column or certified winner for the global notion, and comparison victor or simply beats for the pairwise notion.

Similarly, distinguish a successful pivot-sampling flag from a successful defect-search flag. Section 4.4 explicitly warns that the two kinds of success mean opposite things. That warning is good, but clearer names could eliminate the need for part of it.

This is a small editorial change with disproportionate benefits because those terms recur throughout the hardest section.

## 5. The examples are excellent individually, but the four-column board is not always functioning as a single continuous example

The four-column board is supposed to be the reader's stable mental object.

It is introduced in Section 2, modified for domain-bit failure, modified again for false-pointer dominance, modified for a cyclic tournament, and eventually reused schematically for the planted-pair argument.

The paper carefully says that each mutation starts from the base board. The summary table on page 11 is particularly valuable.&#x20;

exposition(2).pdf



But there is an interesting pedagogical tension here.

Because the board is repeatedly modified, it becomes increasingly difficult to remember its current state. The exposition is doing what good mathematics teaching should do—changing one property at a time—but the reader lacks a consistent visual representation of those changes.

I would consider one consolidated board-state comparison diagram, showing the four configurations side by side and marking only the changed components.

This could replace some repeated verbal explanation.

There is a second distinction worth strengthening: the small board has \\(m=4\\), \\(k=2\\), \\(r=2\\), whereas the asymptotic construction uses \\(r=20\log_2m\\), which would equal 40 at \\(m=4\\).

In other words, the four-column example is a pedagogically shortened version of the construction, not literally the small-parameter instance of the theorem's full family.

The paper says this in several ways, including that the small board has no positive lower-bound budget. But one explicit statement would prevent a reader from assuming that the finite illustration establishes more than it does.

A useful accompanying explanation would be:

> The toy board preserves the logical definition of a certificate and the comparison mechanism, but deliberately shortens the hidden address. Its purpose is to make the operations visible, not to demonstrate the asymptotic separation.

That is already the manuscript's position; it just deserves more visibility.

## 6. Section 5 is excellent, but its hardest passage is presented in a slightly unnatural order

The simulator on page 19 is one of the technically strongest pieces in the article.

The problem is that the reader encounters the separate-cap direct-product lemma before the reduction has fully explained why such a lemma is needed.

The present sequence is roughly: introduce heavy/light columns, state the direct-product lemma, explain why conditioning on lightness is invalid, identify the target event, and finally construct the simulator.

I think the more intuitive sequence would be the reverse at the critical point.

Start with the precise claim that needs proving:

\\[ \Pr\bigl(i\text{ light and query }j \text{ visits }B\_{i,s_i}\bigr)\leq(2/3)^r. \\]

Then explain the desired reduction in ordinary language:

The algorithm's query position itself proposes the entire address. We will simulate its run using only a bounded number of queries to the hidden address inputs. If the original run is light and reaches the true cell, the simulator must successfully output the hidden address.

Only after that motivation should the paper introduce the lemma that bounds the simulator's success.

The caution about conditioning on lightness would then appear exactly where it is needed.

This is a substantial editorial improvement, not merely a stylistic preference. It changes the reader's experience from learning a technical tool and later discovering its purpose, to understanding a specific problem and then seeing the tool solve it.

### The three sources of randomness need a clearer conceptual map

Another issue emerges on a second reading.

The classical distribution uses three distinct random objects.

The independent address inputs sampled from \\(\mu\\) make predicting certificate locations difficult. The random zero positions \\(J_i\\) make discovering the string change difficult. The independent planted column \\(I\\) prevents the classical algorithm from directing its work toward the column that matters.

These play different roles in the three charges.

The manuscript contains all this information, but the independence conditions are distributed across the section.

I would add a short sentence when the planted pair is introduced explaining those three jobs.

Then the three-charge table has a conceptual explanation already in place.

The conditional-independence counterexample on page 18 is worthwhile. It shows something subtle: making \\(I\\) uniform marginally does not suffice if it depends on the observed run.

Similarly, the light-event example on page 19 shows why one cannot simply condition on a favorable branch and apply the original hardness distribution.

These are unusually good examples of probabilistic proof discipline. They should remain.

### The simulator pseudocode could be simpler without losing rigor

The two clocks are important: global time counts every query, whereas \\(q\\) counts queries forwarded to the hidden tuple.

But the four-step simulator has a slightly awkward control flow, especially the interaction between inspecting time \\(j\\), processing the proposed query and outputting the default.

I would express it as a bounded loop over global times \\(1,\ldots,j\\). At each time, inspect the proposed query. If it is the target cell query at time \\(j\\), output its address. Otherwise, before forwarding a hidden-tuple query, check whether the cap has been exhausted. If the loop ends without the target query, output the default.

This is logically the same intended routine, but easier to trace.

The accompanying XOR example on page 20 is good, although by then the reader has already had to understand the simulator abstractly.

Moving the little two-clock table closer to the routine could help.

## 7. There is a small but definite notation-order problem

The manuscript states the theorem involving \\(\alpha\_{\mathrm{tot}}\\) on page 8.

But the exact definition,

\\[ \alpha\_{\mathrm{tot}} = \inf\left\\{\alpha\geq0: \exists C>0\ \forall f\text{ total},\ R(f)\leq C(1+Q(f))^\alpha\right\\}, \\]

does not appear until page 21.

An experienced researcher will infer what is meant. A reader following an instructional exposition should not have to.

I would either define \\(\alpha\_{\mathrm{tot}}\\) when \\(R\\) and \\(Q\\) first appear in the introduction, or give a short informal definition there and retain the full quantified formula in Section 6.

This is a good example of a manuscript that is technically precise but occasionally precise too late.

Section 6 itself is very good. The distinction between fixing \\(k\\) and allowing \\(k\\) to grow with \\(m\\) is carefully drawn, and Question 5 directly tests the endpoint issue.&#x20;

exposition(2).pdf



I would not shorten that argument. I would improve the introduction to it.

## 8. The title and scope create one unresolved expectation

The subtitle promises an explanation of the optimal randomized–quantum exponent.

The main body provides a substantial reconstruction of the lower-bound construction, establishing why no exponent smaller than four can work.

The matching universal upper bound is cited and described as an accepted input. It is briefly discussed at the end of Section 6, with further details deferred to the reasoning record.

That is a perfectly legitimate mathematical division of labor.

But it means the paper primarily explains why the fourth power is necessary, not independently why four always suffices.

There are two reasonable editorial directions.

One is to retain the current scope but make the subtitle slightly narrower, emphasizing a guided reconstruction of the nearly quartic lower bound.

The other is to include a short, conceptual account of the universal upper-bound route. It need not reproduce Huang's theorem; it could simply outline the chain of results that makes an exponent above four unnecessary.

I slightly prefer the second option, because the existing title is appealing and the upper-bound context would give the ending more completeness.

### Another scope issue: query complexity versus computational speedup

The manuscript correctly defines the query model and notes that its total input length is enormous:

\\[ n=O_k\\!\left(m^{22}(\log m)^3\right). \\]

It also explicitly excludes intervening computation and oracle-construction time from the query count.

These caveats matter enormously, especially for a reader attracted by the phrase quantum separation who is not already a complexity theorist.

I would give the result a short interpretation near the end:

The construction proves a sharp relation between two abstract query complexity measures. It does not by itself establish an equivalent end-to-end computational speedup for a practical problem.

That would make the exposition more robust when it travels beyond the specialist audience.

## 9. Proof provenance is mostly responsible, but could be expressed more cleanly

I would separate the paper's claims into three statuses.

Established within this exposition: the board's winning condition and local certification logic, the tournament's expected-weight argument, the sampling-law calculation, the main planted-pair reduction, the separate-cap direct-product proof and the exponent quantifier argument.

Mathematical ingredients quoted or deferred: the Forrelation hardness theorem, the universal quartic upper bound, the detailed exact-circuit construction and the constant-success estimate for the amplification schedule.

Formal verification evidence: the Lean statements, their proofs and the comparison checks described in Section 7.

The paper already discloses much of this, but not through one simple map.

That matters because the introductory phrase describing the three accepted deeper results can make the paper sound more self-contained than it is in several smaller technical details.

This is not dishonesty. It is a presentation mismatch.

For a mathematical reader, a compact table of dependencies would be much more useful than scattering provenance references through prose.

The same applies to the theorem attribution. I would separate the original exponent theorem from the explicit quantitative reconstruction rather than put both under a heading identifying OpenAI's Theorem 1.1.

And the named-circuit result's exact Lean comparison status should be stated once in a clearly distinguished verification note rather than partly in the mathematical narrative.

## 10. The paper is now closer to a textbook chapter than a conventional expository article

This became clearer on rereading.

The manuscript contains carefully staged examples, questions, separated answers, guided feedback, a long optional proof and multiple explanatory routes.

This resembles graduate teaching notes or a self-study chapter much more than the ordinary form of a concise expository research article.

That is not a weakness in itself.

In fact, it may be its comparative advantage.

The problem is that the paper still has occasional features of all three genres: a theorem reconstruction, a guided textbook chapter and a formal-verification report.

The first two fit together naturally. The third can complement them, but needs a more clearly marked boundary.

I would settle deliberately on an advanced, self-contained-as-far-as-practical teaching chapter with documented external dependencies.

That gives you permission to retain the exercises and elaborate examples. It also gives you a strong reason to move implementation provenance and repository history out of the mathematical reading path.

A paper need not imitate a journal article to be taken seriously by mathematicians. It does need to make its purpose and depth clear.

## 11. What I would actually change in the next pass

I would make a relatively surgical revision, not another wholesale rewrite.

Highest priority: restructure the proof dependencies.

Move the definition of the optimal exponent earlier; insert a compact comparison-cost calculation before Section 4.1; separate the expected-weight, winner-preservation and quantum-sampling statements; and introduce the classical target event before the direct-product lemma.

These changes directly address the places where the reader is most likely to lose the mathematical thread.

Second priority: strengthen the concrete example architecture.

Make it unmistakable that the four-column board is a shortened teaching model, give one consolidated board-mutation comparison and explicitly relate the three sources of randomness to their three classical charges.

Third priority: organize the claim statuses.

Distinguish original theorem, quantitative reconstruction, imported mathematical facts, arguments deferred to the reasoning record and formal-checking evidence.

Fourth priority: tighten the ending.

Provide a short conceptual explanation of the universal upper bound, finish the mathematical argument with the construction's central insight, and put detailed Lean material in an optional, clearly delineated extension.

I would preserve the vast majority of the mathematical content.

## Final assessment after the second reading

My strongest positive judgment is that the exposition explains why particular proof devices are necessary, not just how to apply them.

The negative Forrelation input explains promise certification. The dominating nonwinner explains final verification. The cyclic tournament explains why comparison sorting is unavailable. The fractional matrix explains weighted sampling. The light-event counterexample explains why a conditional argument fails. The simulator explains how adaptive guessing is captured by a capped predictor.

That sequence is deliberate, technically meaningful and pedagogically valuable.

My strongest criticism is that the reader is still asked to perform too much organizational work. Too often, the paper introduces a precise mechanism before fully explaining which obstacle it overcomes, or presents a detailed calculation before revealing its place in the proof architecture.

I would now regard this as a strong advanced expository manuscript that needs a focused editorial restructuring, rather than a manuscript requiring another round of general explanatory expansion.

The distinction matters: adding more examples or detailed lemmas could actually make it worse.

If I were an outside mathematician reading this version, my principal concern would not be that the author had failed to engage seriously with the argument. The level of care in the worked examples and error-sensitive reductions makes that engagement evident. My concern would be whether the teaching structure is sufficiently controlled that another mathematician could reconstruct the central ideas without repeatedly returning to earlier sections.

The next revision should make the mathematics easier to retain, not merely easier to check. That is the main conclusion of this deeper pass.