

expert_companion(2).pdf
PDF
read attached give feedback on this paper how well is it written for its intended audience give a papers worth of feedback im gonna folow this up with several "reassess again" so your initial response will not be the final one goign back so i guess plan what your subsequent go thorugh is gonna be i guess lets start high level

Worked for 6m 16s
Editorial review I: Reconstructing OpenAI’s Nearly Quartic Query Separation
First-pass assessment · 19-page manuscript · 4 November 2026

Overall verdict
This is a serious, technically sophisticated reconstruction paper that is already reasonably well written for specialists in quantum query complexity. Its main weakness is not the quality of its prose or the apparent organisation of the mathematical arguments. It is that the paper does not yet make its own intellectual contribution, explanatory hierarchy and formal verification evidence as immediately legible as they could be.

I think it is substantially closer to a publishable specialist research companion than to an informal exposition, but there is a distinction between containing a well-organised reconstruction and making a specialist immediately understand why this particular reconstruction deserves their attention.

The strongest feature is that the paper identifies two mechanisms that deserve to be understood independently:

The quantum upper bound: a weighted tournament that finds a short candidate list despite probabilistic, potentially cyclic comparisons.

The randomized lower bound: a planted-winner construction in which finding a changed certificate cell becomes a bounded-query prediction problem.

The paper gives these mechanisms substantial mathematical treatment rather than merely paraphrasing the original result. That is exactly the right direction for the stated project.

The principal editorial issue is that the reader must work fairly hard to distinguish four different things: OpenAI's mathematical result, your reconstruction of its proof, the refinements and explicit estimates introduced by that reconstruction, and what the accompanying Lean development has actually checked.

All four are addressed, and often carefully. But the distinctions are distributed across the abstract, introduction, technical sections, formal-status table and references.

I would focus the next revision on making the paper easier to evaluate, rather than simply easier to read. A sceptical theoretical computer scientist should be able to determine its mathematical contribution and evidential status within two pages, then enter the detailed proofs with a clear mental model.

Provisional assessment by audience
These are editorial judgements, not scores for the correctness of the mathematics or an independent audit of the Lean repository.

Intended reader

Writing effectiveness

Quantum query-complexity specialist

8/10

Broader theoretical computer scientist

7/10

Lean / formal-methods researcher

6/10

Mathematically strong non-specialist

4.5/10

The scores differ because the paper is already comfortable using the established language of query complexity, but it makes relatively few concessions to readers unfamiliar with Forrelation, cheat sheets, amplitude amplification and direct-product arguments.

That is not automatically a defect. A research companion should not sacrifice precision to accommodate every possible audience.

For this manuscript, I would select researchers in quantum algorithms, decision-tree/query complexity and mathematically serious formal verification as the primary readership. Adjacent theoretical computer scientists should be able to follow the principal argument, while readers seeking a first introduction should be directed to the separate examples-first exposition.

I would not attempt to turn this manuscript into a textbook. I would attempt to make its specialist explanations exceptionally clear.

1. The paper's strongest qualities
1.1 It has a genuine mathematical narrative
Many technical reconstructions fail because they reproduce a proof in the order its author discovered it, instead of the order a reader needs to understand it.

This paper largely avoids that problem.

Section 1 explains the underlying construction. Section 2 defines the function and the local certificate tests. Section 3 explains the quantum algorithm. Section 4 establishes the classical obstruction. Section 5 combines the estimates. Section 6 reports the formal endpoints.

That is a sensible structure.

More importantly, the paper makes a useful conceptual distinction between finding a plausible winner and verifying a winner. The quantum algorithm exploits cheap comparisons without pretending those comparisons establish certificate validity. The randomized argument exploits hidden addresses without pretending that simply querying a blank certificate cell is informative.

These are substantive insights that explain why the proof works, rather than just what inequalities it proves.

The abstract and §1.1 already communicate both reasonably well. 
expert_companion(2).pdf

1.2 The mathematical exposition respects subtle hypotheses
One of the manuscript's best qualities is the attention it gives to statements that sound plausible but are not justified without further conditions.

The paper explicitly distinguishes arbitrary probabilistic comparisons from noisy access to fixed tournament edges. It distinguishes worst-case branchwise caps from expected costs. It distinguishes side information independent of each input separately from side information jointly independent of the whole product. It also distinguishes an unconditional probability bound for a successful, light execution from a bound conditioned on the execution being light.

These are exactly the sorts of distinctions a careful referee would examine.

Appendix A is particularly useful because the counterexamples are not merely demonstrations of technical competence: they explain why tempting shorter proofs fail. 
expert_companion(2).pdf

I would preserve this feature even if the manuscript needs shortening. It is part of what gives the reconstruction independent explanatory value.

1.3 It is unusually careful about attribution
The paper identifies OpenAI as the source of the separation, construction and two major reductions. It distinguishes earlier pointer functions, cheat-sheet constructions and Forrelation lower bounds. It identifies the role of existing quantum search results and direct-product literature.

That is important, especially for a paper whose contribution is a reconstruction rather than a new separation theorem.

The existing attribution is much better than a vague claim to have independently discovered the mechanism.

1.4 The figures are genuinely useful
PPT - Exploring Forrelation: A Intriguing Quantum Complexity Problem PowerPoint Presentation - ID:9367583

Figure 1, page 3

The construction's winner, address blocks, certificate array and outgoing pointers

Bloom Filter

Figure 2, page 9

The coupled dummy and planted inputs underlying the classical reduction

Figure 1 is especially effective at showing that the winner's certificate address is derived from hard partial-function answers, while the selected cell contains pointers into rival columns.

Figure 2 illustrates the lower-bound coupling without overwhelming the reader with the full encoding.

Both figures use restrained colour, and the rendered mathematics is clean and legible. The presentation has the appearance of an academic paper, rather than an AI-generated report.

I would add one more figure, but I would not replace the existing two.

2. The biggest weakness: the contribution is less clear than the proof
The introduction contains an explicit contribution statement:

“Our contribution is their proof-level reconstruction with explicit query accounting and counterexamples that isolate the necessary hypotheses.”

That is a good starting point. But it leaves several significant questions unanswered.

What is independently established in this manuscript that was not already proved in the OpenAI preprint? Which arguments are alternative proofs, and which are expanded versions of the original arguments? Which quantitative constants are new calculations? Is the formalisation an independent proof development, an encoding of the reconstructed proofs, or a collection of separately verified results with partial correspondence evidence?

The paper eventually answers much of this. The difficulty is that the answers are too expensive to extract.

I would introduce a contribution-and-evidence map on page 2
Something like the following:

Component

Mathematical origin

Contribution of this work

Nearly quartic total-function separation

OpenAI

Reconstructed complete fixed-parameter argument

Probabilistic tournament

OpenAI

Explicit sampling law, proof and query accounting

Classical planted-cell reduction

OpenAI

Capped prediction proof, dependence checks and counterexamples

Numerical bounds

Reconstruction

Chosen logarithmic exponent and explicit coefficient

Lean development

Accompanying project

Formal proofs, specified comparisons and reproducible build evidence

Uniform growing-parameter consequence

Further quantitative analysis

Explicit parameter-dependent estimates, documented separately

The actual wording must be precise about originality. I would not imply the proof mechanisms are new when the manuscript expressly attributes them to OpenAI.

This table would solve several problems at once.

A theoretical computer scientist could immediately assess the mathematical work. A formal-methods researcher could identify the verification contribution. An AI researcher could understand the research workflow. A referee would be less likely to interpret the paper as claiming priority for OpenAI's theorem.

This is my highest-priority recommendation.

3. The abstract is accurate but not optimally effective
The abstract is concise and technically substantive. It announces the theorem, names the mechanisms, gives the two scales and mentions the formalisation.

The problem is one of emphasis.

Its beginning is good: the original result is identified, followed immediately by what the reconstruction explains.

Its middle is also good: the quantitative rates give an expert a fast assessment of the result's content.

But its ending emphasises the remaining correspondence boundary for a full quantum output state.

That is an important disclosure, but it leaves the reader thinking about an unresolved formalisation detail before they have been told why the main formal result does not depend on it.

There are two distinct communication goals here: declare the verified scope accurately, and convince the reader that the reconstruction deserves study. Both are legitimate. The current abstract makes them compete.

I would keep the caveat, but make the hierarchy clearer:

The main theorem and measured-label argument are the principal formal endpoints; a stronger retained-state correspondence is not being claimed as completed.

That is materially more informative than simply ending with a boundary that an unfamiliar reader cannot yet interpret.

I would also use one short sentence to make the reconstruction's particular value explicit: for example, that it presents the quantum and classical mechanisms through independently checkable intermediate claims and explicit query accounting.

The objective is not to make the abstract more enthusiastic. It is to make its exact contribution easier to identify.

4. The introduction spends its attention in the wrong order
This is probably the most consequential prose-level issue.

The first page moves through the original result, contribution and scope, numerical constants, Lean statement comparisons, an unresolved physical-state correspondence, bit-query conventions, all-branch caps, coherent padding, and the formal definition of the optimal exponent.

Every item has a legitimate reason to appear somewhere.

But the reader encounters a substantial portion of the verification machinery before seeing the construction that is actually being verified.

The reader's priority at that point is more basic: What makes a column a winner? Why is comparison cheaper than verification? Why does the classical lower bound acquire an extra factor of 
m
m? What mathematical difficulty required reconstruction?

The strongest explanatory passage, §1.1, is on page 2.

I would bring a condensed version of that passage forward.

A better opening sequence
Position

Purpose

Opening paragraph

State the original problem, the conjecture and why the new exponent matters

Next paragraph

Explain the two core mechanisms in accessible specialist language

Next paragraph

State exactly what has been reconstructed or additionally established

Main theorem

Give the quantified bounds and optimal-exponent conclusion

Following paragraph

Explain the query-model conventions needed to interpret the theorem

End of introduction

Position the work relative to earlier constructions and map the formal evidence

The existing formal definitions should remain. They simply need not precede the central explanation.

The result would probably be a similar-length introduction, but much easier to absorb on first reading.

5. The mathematical architecture is good, but its dependency structure is too implicit
The proofs follow a logical sequence, yet the reader is still asked to reconstruct the dependency graph mentally.

Consider the quantum argument. To understand why the final query bound holds, the reader has to keep track of the Forrelation decoder, the exact circuit and its local tests, the comparison probabilities, the survival weights, the bounded amplifier, and the final verifier.

Similarly, the randomized argument involves a minimax hard distribution, independent address instances, dummy and planted inputs, the erased-zero event, a heavy-column split, a truncated predictor and a direct-product bound.

These are individually well explained. Their relationship could be made more explicit.

I would add a one-page proof architecture near the introduction, rather than introducing more detailed prose.

A schematic version is:

Hard partial function: 
k
k-Forrelation

Cheap quantum decoding · expensive randomized prediction

Quantum upper bound

Compare columns

Sample weighted candidates

Verify certificates

Q
(
F
k
,
m
)
=
O
~
k
(
m
)
Q(F 
k,m
​
 )= 
O
  
k
​
 ( 
m
​
 )
Randomized lower bound

Plant hidden winner

Bound zero discovery

Reduce cell discovery to prediction

R
(
F
k
,
m
)
=
Ω
~
k
(
m
2
−
1
/
k
)
R(F 
k,m
​
 )= 
Ω
  
k
​
 (m 
2−1/k
 )
Combine the bounds

α
t
o
t
=
4
α 
tot
​
 =4
The optimal exponent for total Boolean functions

This is conceptual rather than a substitute for the precise dependency graph. A paper version should also mark which results are imported, which are proved in the text and which have formal endpoints.

The value is that the reader can retain the entire proof in working memory while navigating its details.

6. The Lean formalisation is simultaneously a major strength and an underdeveloped part of the manuscript
Section 6 is one of the most important sections for differentiating this work from an ordinary exposition.

The status table on page 12 is excellent in principle. It distinguishes statements with recorded comparison checks, built and axiom-audited refinements outside the configured comparison bundle, and ordinary mathematical consequences not themselves clauses of a compared theorem. 
expert_companion(2).pdf

This is intellectually responsible. It avoids the misleading implication that every interesting claim has received an identical kind of formal check.

However, the section is quite short relative to the prominence of Lean in the subtitle and abstract.

A formal-methods specialist will probably want to know exactly what the formal theorem says, how the query model is encoded, how an oracle algorithm's query cap is represented, how the statement comparison works, and which assumptions or imported results enter the proof.

The manuscript directs them to the repository and reasoning record. Those links are useful and actually embedded in the PDF, but they cannot entirely replace an account in the paper itself.

My recommendation depends on the intended positioning.

If the primary contribution is mathematical reconstruction, Section 6 can remain compact, but the subtitle should give less equal prominence to Lean.

If the paper is intended as a mathematical-formalisation contribution, I would expand Section 6 into a more substantial account, including one or two representative Lean theorem statements and a precise trust-boundary diagram.

There is also a terminology issue. Words such as compared, built, axiom-audited, Comparator and correspondence have distinct meanings here, but they are not all self-explanatory outside the project.

A glossary or succinct definitions would help.

The strongest message would be that formal proof checking, specification comparison and manuscript-to-formal-statement correspondence are related but different evidential claims.

The manuscript already understands this distinction. It should make that distinction unmistakable to readers.

Figure clarification: The two thumbnail previews above are illustrative, not taken from the manuscript. Here are the actual extracted diagrams: Figure 1, page 3 and Figure 2, page 9.

7. The quantum upper-bound section is the paper's strongest technical exposition
Section 3 is, in my assessment, the clearest demonstration that the work is doing something useful beyond summarising the original theorem.

The progression from probabilistic comparisons to weighted survival, expected weight reduction, exact conditional sampling and final verification is well chosen.

In particular, the derivation

E
[
W
n
e
w
∣
w
]
≤
W
/
2
E[W 
new
​
 ∣w]≤W/2
is an excellent explanatory centrepiece. It shows why transitivity is unnecessary, rather than simply assuring the reader that cycles are harmless.

The construction of the sampler is also precise about the distinction between its conditional output law and its probability of succeeding. This matters because amplitude amplification is not automatically a licence to claim an arbitrary desired output distribution. 
expert_companion(2).pdf

I would nevertheless make one improvement.

The reader should know, before entering §3.2, exactly what the sampler must preserve and why.

At present, this requirement emerges through the technical development. I would promote it into the opening explanation of Section 3: the algorithm does not need to compute survival weights; it needs a procedure that samples labels in proportion to those weights, while ensuring that every run respects a predetermined query cap.

That is the essential algorithmic idea. Everything else should be organised around establishing it.

The four-candidate probability table on page 7 is useful as a check, although its pedagogical purpose could be more clearly stated. It illustrates the exact distribution being sampled rather than merely providing numerical reassurance.

I would keep the mathematical proof almost entirely intact, but give it a more explicit explanatory spine.

8. The randomized lower-bound section needs more reader guidance
Section 4 may be the harder part to understand on a first reading.

The basic coupling is excellent: construct a dummy zero-input, secretly select a column, erase its zero and fill its correct certificate cell. The chosen column supplies a factor 
m
m, while the hardness of the address problem supplies the other large factor.

But after this simple conceptual beginning, the argument becomes substantially more intricate.

In particular, the predictor in §4.4 involves two clocks, a distinction between total target queries and original-tree queries, a truncation rule, light and heavy columns, and an unconditional joint-event bound.

All of these details matter. The issue is not excessive rigour; it is that the reader lacks a compact operational picture of the simulator.

I would add a small illustrated trace in the main section, showing one original decision-tree execution alongside the truncated predictor. The separate reasoning record already contains such a trace. A carefully simplified version could be incorporated without reproducing the entire argument.

The central takeaway should be obvious before equation (12):

A query to a proposed certificate cell identifies a candidate address. If the original algorithm has not spent too many queries learning that column's address inputs, the proposed address cannot be correct with substantial probability.

Then the formal cap argument establishes that intuition.

This section could become especially persuasive with relatively little additional text, because its underlying structure is already strong. 
expert_companion(2).pdf

9. Appendix E deserves a strategic decision
The growing-parameter consequence in Appendix E is presented as optional, but the uniform Forrelation estimate supporting it is a mathematically substantial assertion.

The main theorem needs only fixed 
k
k. Appendix E changes the regime, controls the dependence on 
k
k, and uses a separate uniform estimate documented in the reasoning record.

That makes it a different kind of contribution from simply extracting explicit constants in the fixed-parameter proof.

I would decide whether the growing-parameter result is a central contribution or a supplementary consequence.

If it is central, I would give the new uniform estimate more prominence and make the proof dependencies substantially easier to audit within the manuscript.

If it is supplementary, I would keep it clearly separate from the principal reconstruction and explain why the stronger uniform analysis is included.

At present it sits in an awkward middle ground: significant enough to invite serious mathematical scrutiny, but not prominent enough for a reader to recognise it as part of the contribution.

This is an editorial concern, not an assertion that the estimate is wrong.

10. The paper is reasonably self-contained, but perhaps not self-contained enough for its strongest claims
The manuscript does more than defer everything to the longer reasoning record. It includes actual arguments, quantitative calculations and the proofs of the amplifier and direct-product lemmas.

That is a major strength.

However, some of the most demanding supporting work, including parts of the explicit circuit analysis, the uniform analytic estimate and the detailed formal correspondence, lives in the external record.

That can be acceptable for a companion paper. But the paper should define precisely what kind of self-containment it promises.

A specialist reading a research article generally expects that its main mathematical assertions can be checked from the article, its stated lemmas, and cited established results. Repeated directions to a large auxiliary record can make that checking process slower, especially when the record is itself a substantial evolving research artifact.

I would draw a sharper distinction between proofs contained in this paper, standard results invoked by citation, and additional derivations supplied in the companion record.

I would not duplicate hundreds of pages of supporting material. Instead, ensure that every genuinely essential step has an intelligible statement and enough proof within this manuscript for the external reference to serve as verification support rather than the only place where the reasoning is visible.

11. Audience-specific adjustments
The paper should remain technically demanding. But a small amount of additional orientation would make it more effective across the intended research audience.

Reader

Most important change

Query-complexity expert

Emphasise the new value of the reconstruction relative to the original proof

Quantum algorithms specialist

Foreground the exact sampling-law argument and its quantum implementation

Complexity theorist outside query complexity

Explain how the partial-function hardness and totalisation interact

Lean expert

Show representative formal statements and clarify the verification boundary

AI-for-mathematics researcher

Make the relationship between AI-generated proof work, mechanical checking and mathematical correspondence auditable

I would also add a compact notation table for 
m
,
k
,
ℓ
,
r
,
L
,
K
,
T
m,k,ℓ,r,L,K,T, identifying each parameter's role.

For specialists, the benefit is not learning these symbols. It is reducing the memory burden of tracking their different roles across the two bounds.

One further clarification would be useful: the construction has an extremely large, but polynomial, encoded input length. The separation concerns bit-query complexity, with computation between queries free; it does not establish a comparable speedup in ordinary running time. The manuscript states these conventions, but connecting them directly to the encoding size would prevent misunderstanding by readers from adjacent fields.

12. Scientific credibility and presentation
There is a significant distinction between making a paper look rigorous and making its evidence genuinely inspectable.

This manuscript does well on the first and has promising foundations for the second.

Its restrained typesetting, detailed citations, carefully labelled theorems, numerical constants, explicit counterexamples and linked source editions all support a serious academic presentation.

The original OpenAI result is externally identifiable in the 5 October 2026 preprint, and the manuscript correctly attributes that underlying theorem. 

GitHub

The more important credibility questions concern the accompanying formalisation.

The note identifying AI assistance is appropriate. I would preserve it. But I would explain elsewhere, in ordinary scientific terms, how independently reproducible checking was carried out. A statement that AI systems drafted proofs and performed checks is not the same kind of evidence as a reproducible Lean build, a theorem-statement comparison or a mathematical correspondence proof.

The paper already separates some of these. I would make the distinctions more visible and use precise standard language.

I would also distinguish a successful Lean proof of a formal proposition from evidence that this proposition faithfully captures the intended mathematical theorem. Neither distinction should be used to undermine what has been established. Rather, it lets the reader know exactly what has been established.

One particular choice deserves praise: the manuscript explains that the retained-state correspondence issue does not affect the measured-label route used for the headline theorem. That is much better than either concealing the boundary or making an unnecessarily broad completeness claim.

I have not independently run the Lean development, audited its dependencies, or verified all the mathematical derivations against the original preprint. My judgement here is about the manuscript's communication and its presentation of evidence, not an independent certification of its results.

13. Revision priorities
If the next version were to be changed in only a few places, this is where I would invest the effort.

Priority

Proposed change

Expected benefit

1 — Very high

Add a contribution-and-evidence map

Makes the work's intellectual value immediately understandable

2 — Very high

Reorder the introduction around the two proof mechanisms

Improves the first two pages significantly

3 — High

Add a one-page proof architecture

Reduces cognitive load throughout the paper

4 — High

Resolve the prominence of Lean: expand its treatment or narrow the subtitle

Aligns the paper with its advertised audience

5 — High

Give the §4.4 truncated simulator a concrete trace

Makes the hardest part of the classical proof more accessible

6 — Medium

Clarify Appendix E's contribution and supporting proof status

Prevents a secondary result from clouding the main argument

7 — Medium

Add notation and query-cost summaries

Makes technical navigation faster

8 — Lower

Polish sentences, transitions, typography and references

Improves an already professional presentation

I would not prioritise shortening the proofs, changing all the notation or making the writing more conversational.

The highest-return changes are architectural.

14. How I propose to approach the subsequent reassessments
Because you intend to return with several rounds of “reassess again”, I would avoid repeatedly making the same superficial review. Each pass should deliberately change the perspective, test previous conclusions and become more exact.

Pass I — Overall contribution and readership

This review

The paper's purpose, contribution, audience, credibility, organisation and broad weaknesses. Establish a starting hypothesis about what should change.

Pass II — Cold-reader reconstruction

Re-read the manuscript without granting it the benefit of the author's intended meaning. At each section, identify what an expert actually knows, what they must infer and which explanations arrive too late.

Output: page-by-page clarity diagnosis and concrete changes.

Pass III — Mathematical exposition audit

Inspect the explanations of the upper bound, lower bound, lemma contracts, quantifier structure and accounting. Distinguish mathematically essential conditions from details that could move to appendices.

Output: proof-by-proof explanation improvements, with specific equation and paragraph references.

Pass IV — Adversarial specialist and provenance review

Compare the manuscript with OpenAI's original paper and cited mathematical antecedents. Scrutinise novelty, attribution, the scope of formal claims, source alignment and reproducibility.

Output: potential objections from a critical referee, classified by severity and evidence.

Pass V — Precise editorial rewrite

Examine the title, abstract, contribution paragraph, section openings, theorem framing, transitions, figures, captions and supporting material at sentence level.

Output: replacement passages and an actionable revision specification.

Pass VI — Final independent assessment

Reassess the revised work against the original goals, challenge earlier recommendations and determine whether remaining revisions materially improve the paper.

Output: final specialist-readiness verdict with residual limitations.

These passes should be cumulative, not repetitive. An objection from one pass should remain open until the manuscript resolves it or a later examination shows the objection was mistaken. Conversely, I would not preserve an earlier criticism merely for consistency.

15. Final judgement of this first pass
There is a meaningful difference between three possible outcomes for this paper.

As a technical explanation of OpenAI's separation, it is already strong. The mathematical organisation is substantially better than a sequence of informal explanations, and the upper/lower-bound structure is clear.

As an independently useful research reconstruction, it is promising, but it needs to present the precise contribution and the provenance of each result more forcefully. The reader should not have to investigate the repository to discover why the reconstruction represents substantial work.

As an expert-facing mathematical formalisation paper, it has potentially important material, but its current treatment of Lean is too compressed to carry the prominence it receives in the title and abstract.

The paper's most distinctive asset is not any single formula. It is the combination of careful reconstruction, explicit attention to invalid shortcuts, quantitative detail and formally inspectable endpoints.

I would preserve nearly all of the mathematical substance and substantially improve the first two pages and the formalisation section. Those changes would do more for the manuscript than polishing individual sentences throughout the 19 pages.

My provisional assessment remains 8/10 for a quantum query-complexity expert, with the largest potential improvement coming from positioning and explanatory architecture, not from simplifying the mathematics.

For the next reassessment, I would start with the cold-reader test: what exactly a competent but previously unfamiliar theoretical computer scientist understands after pages 1, 3, 5, 8 and 12, and which missing conceptual bridges most obstruct that understanding.


actual_figure_1.png
Image

actual_figure_2.png
Image
another pass read through

Worked for 4m 16s
Second review — a cold reading of the manuscript
Pass II · Reader comprehension, explanatory precision and editorial structure · 19 pages

Revised overall assessment
On a second reading, I think the paper is stronger mathematically and structurally than some of my first-pass recommendations implied, but also harder to read in several very specific places.

The principal problem is not that the paper lacks a conceptual explanation. Section 1.1 already gives a good one. Nor is the problem that it needs substantially more background material. For its specialist audience, much of the assumed mathematics is appropriate.

The real problem is subtler:

The manuscript repeatedly gives the correct technical explanation before the reader has fully understood what question that explanation is answering.

This happens most noticeably in the quantum sampling argument, the construction of the total function, the capped predictor and the formal verification discussion.

After reading all 19 pages again, I would change the emphasis of my earlier recommendations:

Less additional introductory material. The existing introduction has most of the necessary ideas; it needs reordering and sharpening rather than substantial expansion.

More local explanation at difficult transitions. A few carefully placed sentences would improve comprehension more than another page of general overview.

More precision about the relationship between the reconstruction and the original proof. The distinction is stated but not always apparent in the organisation.

Greater attention to what the reader can verify from the paper itself. Particularly for numerical estimates, supporting results and Lean correspondence.

Fewer proposed diagrams than I originally suggested. The two existing figures are effective. A compact proof-dependency schematic might help, but it is not essential.

My revised provisional assessment for the intended quantum query-complexity audience is around 7.5–8/10. The manuscript is already coherent and technically purposeful. Its remaining deficiencies are concentrated in the reader's path through the arguments.

An important qualification: this pass is a close editorial reading of the supplied PDF, not an independent verification of every proof or execution of the linked Lean code. I am evaluating the explanations as written and marking claims whose supporting arguments would need separate checking.

1. What the reader actually understands, page by page
Pages

What is successfully communicated

Where comprehension becomes expensive

1–2

The original separation, its importance, the two mechanisms, the theorem and historical context

Formalisation qualifications appear before the main mechanism is explained

3–4

The certificate layout, Forrelation supplier, exact circuit and definition of the total function

Too many different roles for the address, transcript, pointer and circuit appear in quick succession

5–6

Why comparisons are cheap, why a winner is dominant, and why survival weights decrease

The connection between comparison probabilities and the actual quantum sampling procedure requires effort

7–8

Bounded amplification, candidate verification and total quantum cost

Several layers of conditional probability, coherent preparation and measured output are compressed together

8–9

The classical reduction's structure and dummy/planted coupling

The two complementary ways of discovering the planted change need stronger initial framing

10–11

The capped predictor, direct-product application, classical lower bound and final exponent argument

The predictor's mechanics are the most demanding passage in the main proof

11–12

Formal endpoints, comparison evidence and correspondence boundaries

The status vocabulary and the meaning of the different checks need clearer interpretation

14–19

Counterexamples, historical comparisons and auxiliary arguments

Several potentially substantial results are delegated to the reasoning record

The architecture is sound. The main opportunities are concentrated at the points where one section introduces a new kind of object or a new proof obligation.

2. The first two pages: good content, slightly wrong order
The paper begins with a concise account of the theorem, an explicit contribution statement and a technically complete query-model definition.

None of those is misplaced in isolation.

But, as a first-time reader, I would still be asking what the construction looks like when the text begins discussing separately compiled specifications, Comparator checks and a physical output-state correspondence boundary.

Only on page 2 do I receive the very useful explanation of the winning column, hard address and cheap comparison.

That is the first major opportunity.

I would preserve almost all the current introductory content, but move the conceptual mechanism into the first page, followed by the mathematical statement and then the verification qualifications.

A useful change in wording
The current contribution paragraph compresses the mathematical reconstruction and the formal evidence into one densely informative block. I think it would be stronger to separate their purposes.

For example:

The separation theorem and its underlying construction are due to OpenAI. We reconstruct the proof with particular attention to two interfaces: sampling candidates according to probabilistic comparison weights, and converting queries to hidden certificate cells into capped predictions of hard addresses. We make the query accounting and several necessary hypotheses explicit, including counterexamples to tempting simplifications. We then identify the corresponding formal statements and the evidence supporting their verification in Lean.

This is not proposed as a final replacement. It illustrates the hierarchy I think the paper should establish.

Notice that it does not claim the two mechanisms are newly invented. It says exactly what has been reconstructed and what the formalisation contributes.

The existing §1.1 is one of the better-written passages in the entire manuscript. I would not replace it with a more generic explanation.

I would move it forward, tighten it slightly and use it to introduce the theorem.

3. Pages 3–5: the construction is precise, but its components need a clearer hierarchy
The paper introduces the 
k
k-Forrelation promise, the quantum decoder, the exact Boolean circuit, the total function and its local tests.

This order is mathematically defensible. Nevertheless, I found myself repeatedly needing to distinguish objects with different roles.

Object

Role in the construction

X
i
X 
i
​
 

The bit strip that must be all ones for column 
i
i to win

A
i
,
h
A 
i,h
​
 

A hard partial-function input whose answer contributes to the certificate address

s
i
s 
i
​
 

The address determined by the answers to the 
r
r partial-function instances

B
i
,
s
B 
i,s
​
 

A proposed certificate cell containing pointers and circuit transcripts

C
C

The fixed exact circuit giving meaning to the proposed transcripts

The manuscript defines all of these correctly. The problem is that the reader has to hold them in memory while also learning the Forrelation promise.

I would include a compact description of these objects immediately before the formal definition on page 4, or directly beneath Figure 1.

A particular distinction worth foregrounding
The quantum decoder is not the certificate verifier.

The decoder returns an address cheaply when the relevant instances satisfy the promise. The exact Boolean circuit is needed to ensure that the alleged address and certificate are meaningful, including whether the supplied partial-function inputs lie inside the promise.

That distinction is present in the text, and Appendix A.1 provides a useful counterexample showing why the projection statistic alone cannot decide promise membership.

But this is important enough to state explicitly before presenting the detailed constructions:

The quantum algorithm can cheaply propose where a valid certificate would reside; the local tests determine whether the certificate really is valid.

That principle explains why the construction needs both an efficient quantum decoder and an exact circuit with sufficiently small size.

It also explains why the circuit transcripts are supplied as untrusted input instead of being computed by the quantum verifier.

That last point deserves slightly more emphasis. A reader unfamiliar with cheat-sheet totalisations might otherwise wonder why the certificate cell contains alleged intermediate gate values rather than just the final answers.

The reason is that locally checking proposed computation transcripts is cheaper than directly recomputing all the exact answers. The manuscript establishes this through its gate-consistency and output tests, but could communicate the motivation earlier. 
expert_companion(2).pdf

The unusual encoding size should be framed better
The encoded input length is polynomial in 
m
m, but with a large exponent. The paper explicitly states that the addressed cells dominate the count and that there are 
m
20
m 
20
  cells per column.

This is good mathematical disclosure.

For readers outside query complexity, however, it risks creating a misleading impression of an efficient practical algorithm.

I would add one sentence after the input-size calculation:

The construction is designed to establish a separation in the number of oracle queries; no corresponding bound on ordinary running time or memory usage is claimed.

Page 1 already explains that computation between queries is free. Connecting that fact to the actual encoding would improve clarity without lowering the technical level.

4. Pages 5–8: distinguish the three stages of the quantum argument
This remains the strongest mathematical exposition in the paper. But the reader has to integrate three logically separate arguments.

First, an actual winner has a high probability of defeating any particular rival:

a
i
⋆
j
≥
1
−
ε
.
a 
i 
⋆
 j
​
 ≥1−ε.
Second, the ideal tournament samples candidates with weights

w
i
=
∏
b
=
1
n
a
i
ρ
b
.
w 
i
​
 = 
b=1
∏
n
​
 a 
iρ 
b
​
 
​
 .
Third, the quantum procedure prepares and amplifies a state whose measured successful labels have the required conditional distribution.

It is the distinction between the second and third stages that makes §3.2 difficult.

The ideal process says what probability distribution would succeed mathematically. The preparation circuit realises the corresponding unnormalised label weights. Bounded amplification then increases the chance of observing success without changing the conditional label distribution.

This is the actual logical structure of the proof.

The paper demonstrates it, but mostly through a continuous stream of equations and prose. I would introduce these three stages explicitly at the beginning of §3.2.

The most valuable equation deserves more attention
The central sampling identity is

Pr
⁡
[
label
=
i
∣
success
]
=
w
i
W
,
W
=
∑
j
w
j
.
Pr[label=i∣success]= 
W
w 
i
​
 
​
 ,W= 
j
∑
​
 w 
j
​
 .
This is what connects the quantum circuit to the ideal probabilistic analysis.

The probability 
W
/
m
W/m of the preparation succeeding is a separate quantity.

That distinction is essential because the amplifier has to increase the success probability while leaving the conditional distribution over labels unchanged.

The manuscript explains this at the end of page 6 and continues into Lemma 3 on page 7. 
expert_companion(2).pdf

I would make the displayed conditional-law identity the centre of the explanation, rather than treating it as one fact among many.

The fractional-weight example is useful but poorly placed physically
The numerical four-candidate example at the end of page 6 is followed by its table at the beginning of page 7.

That is an unfortunate page break.

The reader has to turn the page to see the numbers that make the preceding paragraph concrete. The example should be kept together with its table.

I would also introduce it more deliberately: its purpose is to show that the surviving weights need not be Boolean, and that the conditional label distribution changes as pivots are added.

It is not meant to model the particular four-column instance used in the other exposition.

The manuscript explicitly acknowledges this, which is good. I would simply move that qualification into the introduction to the example.

The word "winner" has too many meanings
There is a minor but recurring terminology problem.

A column can be a genuine winning column in the definition of 
F
F. A column can win a single probabilistic comparison. A column can be dominant across comparisons without possessing a valid certificate.

The paper understands these differences, particularly in §3.3 and Appendix A.3, but the prose sometimes expects readers to supply the distinction.

I would consistently use valid winning column, defeats in a comparison and dominant candidate for these three concepts.

This would make several proofs easier to read without changing any notation.

The verification step is well justified
I would not shorten §3.3 substantially.

The observation that a dominant column need not have a valid certificate is important. The paper gives a concrete counterexample in Appendix A.3. Final verification is not a cosmetic cleanup step; it is necessary for the correctness of the algorithm.

One explanatory improvement would be to end Section 3 with a compact comparison of its costs:

Candidate selection: 
O
k
 ⁣
(
m
 
ℓ
3
(
log
⁡
ℓ
)
2
)
,
Verification: 
O
k
 ⁣
(
m
 
ℓ
7
/
2
log
⁡
ℓ
)
.
Candidate selection: 
Verification: 
​
  
O 
k
​
 ( 
m
​
 ℓ 
3
 (logℓ) 
2
 ),
O 
k
​
 ( 
m
​
 ℓ 
7/2
 logℓ).
​
 
The manuscript already contains these expressions. Giving them a clearer presentation would help readers see where the final deliberately loose 
ℓ
6
ℓ 
6
  envelope comes from.

5. Pages 8–11: the classical proof is better than it initially appears
My view of Section 4 has improved on rereading.

The structure is disciplined:

A hard distribution is obtained by minimax. Independent samples hide the address. A dummy zero-input is constructed. A single column is selected and planted. A deterministic decision tree can distinguish the two inputs only by encountering a changed coordinate. The two possible discoveries are bounded separately.

This is good mathematical exposition.

The use of the dummy run is particularly effective: it provides a fixed reference execution on which the discovery events can be evaluated.

The paper also carefully explains why the planted column must be independent of the dummy input, rather than merely marginally uniform. 
expert_companion(2).pdf

I would leave the overall proof structure unchanged.

Section 4.4 is the single most difficult passage
The issue is the simulator.

The manuscript constructs a predictor by fixing a column 
i
i, fixing an original-tree query time 
τ
τ, supplying all other dummy input data for free, and truncating the target address queries once their count reaches 
L
L.

Then it relates a visit to the correct certificate cell to successful address prediction.

Every part of this construction has a purpose. But it is not immediately obvious why these particular choices are necessary.

I would add an explanatory paragraph before the simulator is defined:

A query to a certificate cell 
B
i
,
s
B 
i,s
​
  commits the algorithm to the proposed address 
s
s, even if the cell's contents have not been read. We exploit this by simulating the original decision tree while restricting its access to the address inputs of column 
i
i. If the original run reaches the correct cell before spending too many queries on those inputs, the simulator has predicted the entire address within a capped query budget. The direct-product bound makes that event unlikely.

This is the intuition already supporting the proof. It should come before the detailed stopping rules.

Explain why the simulator fixes a query time
A specialist can reconstruct why 
τ
τ is fixed, but the explanation is compressed.

The simulator must turn one particular possible cell query into an address prediction while preserving a worst-case query cap.

Then the argument takes a union bound over the at most 
G
G original query times.

A short sentence stating that purpose would make the construction much easier to follow.

The strongest subtlety is handled correctly in the writing
The passage after equation (12) is one of the manuscript's best.

It emphasises that the probability estimate concerns the joint event of a successful prediction and a light original execution. It does not arise by conditioning on the original execution being light.

This distinction is important because such conditioning can alter the distribution of the address inputs and invalidate the direct-product premise.

Appendix A.7 supplies an explicit example.

I strongly recommend retaining this discussion. It is exactly the kind of issue that would concern a referee examining a reduction from an adaptive algorithm to a capped predictor. 
expert_companion(2).pdf

The improvement needed here is primarily pedagogical: let the reader understand the simulator before confronting the full probability calculation.

6. Page 11: the completion of the exponent proof is unusually clean
I would make comparatively few changes to Section 5.

It does something important: it separates the fixed-
k
k argument from the stronger uniform-in-
k
k claims in Appendix E.

The proof explicitly selects 
k
k after choosing an exponent 
α
<
4
α<4, then holds 
k
k fixed as 
m
m grows.

The final paragraph even spells out the quantifier order.

That is excellent practice, particularly because the statement that 
R
R behaves like 
Q
4
−
o
(
1
)
Q 
4−o(1)
  can obscure the difference between a fixed-parameter collection of families and a single growing-parameter family.

I would not add a lengthy explanation here.

The main editorial opportunity is to ensure that readers have already seen the exponent calculation informally before reaching the technical proof.

The existing end of §1.1 does this. That is another reason to preserve it.

7. Pages 11–12: the formalisation discussion needs a clearer evidential vocabulary
Section 6 is relatively short, but it has to support several distinct claims.

The paper says that the headline results are formally proved, that some statements have been compared against separately compiled specifications, and that particular numerical refinements are built and axiom-audited outside the configured comparison bundle.

It also distinguishes these from the stronger retained-output-state correspondence question.

This is careful.

But I think the reader needs an explicit explanation of what each status establishes.

Status

What it tells the reader

What it does not establish by itself

Lean proof compiled

The elaborated theorem has a proof accepted under its dependencies

That its statement matches every intended mathematical interpretation

Compared against specification

A recorded comparison checks a stated relationship between formal endpoints

Every supplementary numerical result has received the same comparison

Built and axiom-audited

A named declaration has compilation and dependency-audit evidence

That it belongs to the configured specification-comparison bundle

Mathematical deduction

A result follows in the ordinary exposition from stated results

That this exact consequence is itself a separately checked Lean declaration

Outstanding correspondence

A stronger semantic identification has not been established

That the already stated measured-label theorem necessarily depends on it

The manuscript's existing table largely contains the underlying information. What is missing is a compact explanation of the meaning of those different kinds of evidence.

I would not introduce project-specific vocabulary unnecessarily. In particular, Comparator, comparison bundle and source edition should either receive concise definitions or be explained in terms of their ordinary verification function.

I would revise one prominent sentence
Section 6 opens by saying that the Lean development proves the headline results without open mathematical hypotheses.

That may accurately describe the formal theorem, but it sits close to a discussion of an unresolved correspondence boundary.

There is no necessary contradiction. The paper says the headline proof uses measured labels and is independent of the stronger retained-state identification.

Nevertheless, the prose could be clearer:

State the exact scope of the proved formal theorem first, and then identify the stronger statement that has not been established.

This would avoid forcing a reader to resolve an apparent tension between "proved" and "remaining boundary".

An actual presentation defect
The Section 6 heading and introductory paragraph appear at the bottom of page 11, while the evidence table begins at the top of page 12.

This should be fixed in the typesetting.

The heading, introduction and table should appear together, or the section should begin on page 12.

I would make the same kind of correction to the fractional-weight example split between pages 6 and 7.

These are small layout changes with disproportionately large benefits to readability.

8. The appendices are not filler
Appendix A is unusually valuable.

The counterexamples are aligned with exact hypotheses in the main argument. They show the failure of plausible alternatives rather than simply offering supplementary exercises.

The separate independence counterexample in A.6 is particularly economical: 
S
=
X
⊕
Y
S=X⊕Y is independent of each fair bit separately while revealing information about the pair jointly.

Likewise, the expected-cap counterexample in A.5 demonstrates exactly why an expected query allowance cannot replace branchwise caps.

These examples are short, checkable and directly relevant to the proof.

I would preserve them.

Appendix B is also valuable because it explains why the older balanced AND–OR construction gives a different exponent from the new one. The paper is careful to describe the cubic ceiling as a limitation of that particular recipe and analysis, rather than of every cheat-sheet construction. 
expert_companion(2).pdf

That is the right scholarly framing.

Appendices C and D provide important independent arguments for the bounded amplifier and separate-cap direct-product lemma. They make the paper more useful as a technical reference.

Appendix E is a different matter
The growing-parameter result is substantial enough that I would not treat it as merely another illustration.

It rests on a uniform estimate whose supporting analytic work is in the longer reasoning record.

A reader can follow the deduction made in Appendix E while still being unable to audit its most demanding input directly from these 19 pages.

There is nothing inherently improper about relying on a companion technical record. But the paper should make the dependency unmistakable.

I would either present the uniform estimate as a clearly identified additional theorem with its proof relegated to an explicitly cited companion, or maintain a narrower focus on the fixed-parameter reconstruction and demote the growing-family consequence further.

The right decision depends on whether the growing-parameter result is intended to be a independently evaluated contribution.

I would not let the secondary result make the main theorem harder to assess.

9. The relationship to the reasoning record could be more disciplined
This is the most important new concern from the second pass.

The paper repeatedly refers to numbered sections of a much longer reasoning record, sometimes for further detail and sometimes for evidence that is quite important to the argument.

The references are usually precise. That is a virtue.

But not every external reference performs the same function.

There is a difference between consulting the reasoning record for an optional numerical improvement, consulting it for a fully detailed derivation of a stated circuit-size bound, and consulting it for the evidence that a formal declaration was checked against a specification.

These should not be presented as though they were interchangeable.

For example, the exact-circuit construction in §2 is accompanied by a sketch, while the explicit gate-count derivation is assigned to record §8.3. That is more consequential than a reference that merely gives additional intuition.

Similarly, the uniform analytic estimate in Appendix E depends on substantial material in record §§8.7–8.14.

I would examine every reference to the record and classify its role before the next revision. This is an editorial audit of proof completeness and evidential clarity, not an objection to the existence of supplementary material.

An ideal expert reader should be able to distinguish immediately between an imported established theorem, an argument proved in the paper, a supporting calculation proved in the companion record and a formal-verification receipt.

That distinction matters more than adding further general explanation.

10. Stylistic quality: better than average, but somewhat compressed
The actual sentences are generally well constructed.

The prose is restrained, precise and free of excessive self-promotion. The paper does not repeatedly announce that its results are surprising or groundbreaking. It lets the mathematics carry the argument.

That is appropriate for its intended audience.

The problem is rarely a sentence that is badly written in isolation. It is usually a paragraph containing several logically distinct operations without sufficient separation.

The most compressed passages concern exact circuit representation in §2, the transition from ideal sampling to amplitude amplification in §3.2, the simulator in §4.4, and the multiple forms of formal evidence in §6.

I would therefore resist a wholesale sentence-level rewrite. It could easily make the paper longer without significantly increasing understanding.

Instead, I would insert more short purpose statements immediately before the hardest arguments.

The paper already has strong explanatory phrases such as "The decoder locates a proposed certificate; the circuit tests whether that location has a valid meaning."

That is exactly the style I would extend: short, mathematically meaningful sentences that explain why the next technical construction is necessary.

11. What I would change first, after this second reading
Revised editorial priority

Highest impact

Move the core mechanism earlier and clarify the contribution without expanding the introduction much.
Highest impact

Clarify the three stages of the weighted quantum sampler and the exact conditional label law.
Highest impact

Add a short operational explanation of the truncated predictor before its formal construction.
High impact

Explain the different formal evidence statuses and supporting-record dependencies.
High impact

Decide how prominently Appendix E should feature as a separate quantitative contribution.
Medium impact

Clarify terminology for valid winners, comparison victories and dominant candidates.
Easy improvement

Fix the two disruptive page breaks and add concise notation or cost summaries where needed.
12. What I would explicitly not change
I would not make the paper much less mathematical. It is written for people who can understand formal complexity arguments, and reducing the density of definitions or equations indiscriminately would weaken it.

I would not remove the counterexamples. They provide essential evidence of care in the reconstruction.

I would not turn the paper into a broad survey of quantum computing. Its focus is one theorem and the mechanisms behind it.

I would not replace the measured-label proof with a broader discussion of quantum state semantics unless the manuscript's actual formal objective changes. The state-correspondence boundary should be transparent, but it need not dominate a paper whose headline proof does not depend on it.

And I would not greatly expand the historical discussion. The current distinction between the older cheat-sheet recipe, earlier pointer constructions and the new comparison mechanism is already informative.

13. Where this leaves my assessment
This second pass has made me more convinced that the manuscript is a technically credible specialist companion in its organisation and style, rather than an exposition that requires wholesale restructuring.

But it has also made me less convinced that the paper's main weakness is simply its introduction. The difficult explanatory transitions are distributed throughout the main proof, and the evidential relationship between this paper and its reasoning record deserves closer scrutiny.

The positive finding is that most of the prose improvements should be surgical.

The manuscript already contains the right proof components, the relevant technical distinctions, the counterexamples and a strong mathematical narrative. The next step is to make it easier to recognise, at every stage, what the reader is trying to establish and why the current construction is the correct tool.

For an expert audience, I would now judge the mathematical exposition stronger than the presentation of the contribution and verification evidence. That is a more specific conclusion than my first review.

My next reassessment would move from editorial reading to an adversarial mathematical-exposition audit. I would scrutinise every major lemma's assumptions, the transition between ideal and implemented algorithms, the independence and cap conditions in the classical reduction, the explicit numerical estimates, and the exact scope of the formal claims. The objective would not merely be to catch mathematical mistakes; it would be to discover where the paper can be technically correct while still leaving an expert unsure that every inference has been justified.

That is where I think the next round can add the most value.

again another pass

Worked for 4m 47s
Third review — adversarial mathematical and editorial audit
Pass III · Testing proof obligations, technical precision and specialist objections

Overall judgement
This third reading has changed my assessment again, in an important way.

The main proof is more carefully constructed than its density initially suggests. Several passages I was inclined to flag as possible weaknesses on the first reading turn out, on closer examination, to contain precisely the distinctions necessary to justify their arguments.

In particular, the manuscript handles three genuinely delicate interfaces:

Turning probabilistic comparisons into an exact weighted sampling law.

Turning adaptive certificate-cell queries into capped predictions without invalid conditioning.

Distinguishing the formally proved measured-label result from the stronger retained-output-state correspondence.

These are not superficial technicalities. They are places where an apparently convincing reconstruction could fail.

I have not identified a decisive error in the principal separation argument from this reading. That is not a claim that the theorem or its Lean formalisation has been independently verified by me.

My strongest criticism has become more specific: the manuscript is good at stating and proving its lemmas, but less good at making their proof obligations and evidential dependencies immediately auditable.

For its intended audience, the next improvement should be not simply more explanation, but a sharper distinction between what is proved locally, what is imported, what is deferred to the reasoning record, and what is supported by formal checking.

1. A stress test of the quantum argument
1.1 The probabilistic tournament appears conceptually sound
The manuscript defines 
a
i
j
a 
ij
​
  as the probability that candidate 
i
i defeats candidate 
j
j. It carefully establishes

a
i
j
+
a
j
i
=
1
(
i
≠
j
)
,
a
i
i
=
0.
a 
ij
​
 +a 
ji
​
 =1(i

=j),a 
ii
​
 =0.
This matters because the comparison need not define a total order, or even a fixed directed tournament.

The subsequent weighted process uses

w
i
=
∏
b
=
1
n
a
i
ρ
b
,
W
=
∑
i
w
i
.
w 
i
​
 = 
b=1
∏
n
​
 a 
iρ 
b
​
 
​
 ,W= 
i
∑
​
 w 
i
​
 .
Sampling the next pivot proportionally to 
w
i
w 
i
​
  yields

E
[
W
n
e
w
∣
w
]
=
W
2
−
∑
i
w
i
2
2
W
≤
W
2
.
E[W 
new
​
 ∣w]= 
2W
W 
2
 −∑ 
i
​
 w 
i
2
​
 
​
 ≤ 
2
W
​
 .
I checked the algebra behind this identity. The unordered pairs combine correctly using 
a
i
j
+
a
j
i
=
1
a 
ij
​
 +a 
ji
​
 =1, and the diagonal terms vanish.

The result does not require transitivity, independence of input coordinates, or a fixed orientation for every comparison.

That is one of the best parts of the manuscript.

1.2 The crucial quantum obligation is stronger than merely finding a surviving candidate
The actual algorithm must reproduce the ideal pivot distribution. It is not enough for a quantum search procedure to return some candidate that passes all previous comparisons.

The preparation in equation (9) assigns successful mass 
w
i
/
m
w 
i
​
 /m to label 
i
i. Hence, conditional on success,

Pr
⁡
[
i
∣
s
u
c
c
e
s
s
]
=
w
i
W
.
Pr[i∣success]= 
W
w 
i
​
 
​
 .
The manuscript then uses a bounded amplifier intended to preserve this conditional law.

This is the right thing to prove. The text explicitly retains comparison workspaces, uses fresh registers and avoids treating the comparison outcomes as a deterministic predicate. 
expert_companion(2).pdf

My remaining concern is not an identified error. It is that several facts essential to this argument are presented together:

The successful label probabilities factor because comparison workspaces are fresh.

Orthogonal label registers prevent interference between different candidates.

Amplitude amplification preserves the normalised successful component.

The measured output of the amplified procedure therefore has the required conditional law.

The bounded schedule preserves a worst-case query cap, even for unexpectedly small success probability.

A specialist can reconstruct this chain. But the paper would become much easier to referee if these were explicitly identified as separate proof obligations.

I would retain the mathematics and make the obligations visible.

1.3 The amplification argument addresses the right edge cases
Appendix C does something valuable: it handles 
p
=
0
p=0, permits 
p
=
1
p=1, uses a fixed schedule independent of the unknown success probability, and establishes a worst-case rather than expected-cost guarantee.

The direct-measurement branch is important for high success probabilities. The randomised Grover-iteration branch handles intermediate probabilities.

The central conditional-distribution argument is also sensible: amplitude amplification changes coefficients in the successful/unsuccessful decomposition while preserving the normalised successful component.

There is no obvious missing distributional assumption in that account.

For a self-contained specialist treatment, I would nonetheless state explicitly that the lemma concerns the measured label distribution and does not assert that every implementation has an independently identified physical output register after arbitrary compilation transformations.

The paper already respects that distinction later in Section 6. Bringing it into the lemma's explanatory discussion would make the relationship clearer.

2. The randomized lower bound survives several important checks
The classical argument was the section I most wanted to challenge.

It has several opportunities for an invalid inference: minimax, conditioning, adaptivity, query-budget allocation and coupling. On closer inspection, the manuscript explicitly addresses most of them.

2.1 Minimax supplies the right hard distribution
Proposition 4 assumes 
L
<
R
(
P
)
L<R(P). The argument then invokes finite minimax to obtain a distribution 
μ
μ on the promise domain under which every deterministic decision tree of depth at most 
L
L succeeds with probability at most 
2
/
3
2/3.

This use of minimax is appropriate. The strict inequality is important, and the manuscript identifies it.

The resulting distribution need not produce unbiased answer bits. That does not matter: the hard-distribution hypothesis already includes constant-output predictors.

This is a subtle strength of the proof. A more casual reconstruction could inadvertently assume that each address bit was uniformly random, which is not established and is unnecessary.

2.2 The direct-product lemma has the necessary hypotheses
Lemma 5 permits adaptive interleaving between independent instances, subject to a separate query cap on each instance.

The essential conditions are that the side information is jointly independent of the entire product input, and that the caps hold on every execution branch.

The induction in Appendix D uses unnormalised measures and the recursion for the optimal correct mass 
V
d
V 
d
​
 . The factorisation argument is natural: querying one input restricts only its factor of the product distribution.

The step

(
∏
j
≠
h
V
L
j
(
ν
j
)
)
[
V
L
h
−
1
(
ν
h
,
y
,
0
)
+
V
L
h
−
1
(
ν
h
,
y
,
1
)
]
≤
∏
j
V
L
j
(
ν
j
)
​
  
​
  
j

=h
∏
​
 V 
L 
j
​
 
​
 (ν 
j
​
 ) 
​
 [V 
L 
h
​
 −1
​
 (ν 
h,y,0
​
 )+V 
L 
h
​
 −1
​
 (ν 
h,y,1
​
 )]
≤ 
j
∏
​
 V 
L 
j
​
 
​
 (ν 
j
​
 )
​
 
is supported by the defining optimality recurrence for 
V
L
h
V 
L 
h
​
 
​
 .

I do not see an obvious unjustified independence step in this argument.

That finding matters because the manuscript's classical lower bound rests heavily on this lemma. 
expert_companion(2).pdf

2.3 The planted-input coupling is carefully formulated
The dummy and planted inputs differ only at the selected zero and within the selected certificate cell.

The lower-bound argument bounds the probability of querying either location on the dummy execution.

This is the correct reference run: until a differing coordinate is accessed, the deterministic query tree observes the same answers in both coupled inputs.

The paper also makes the conservative choice of counting a visit to the planted cell even if the particular queried bit does not change.

That avoids an unnecessary complication and strengthens the reliability of the coupling argument.

2.4 The erased-zero calculation is consistent
Let 
G
=
⌊
m
L
/
100
⌋
G=⌊mL/100⌋.

The argument bounds the expected number of zero discoveries by separating discoveries before and after a column has received 
m
/
2
m/2 distinct row queries.

The early-discovery contribution is at most 
2
G
/
m
2G/m. The number of columns that can receive at least 
m
/
2
m/2 row queries is at most 
2
G
/
m
2G/m.

Thus

E
Z
≤
4
G
m
,
Pr
⁡
[
selected zero queried
]
≤
4
G
m
2
.
EZ≤ 
m
4G
​
 ,Pr[selected zero queried]≤ 
m 
2
 
4G
​
 .
The additional factor 
1
/
m
1/m arises from independently choosing the planted column.

That factor would not follow merely from the planted index having a uniform marginal distribution. Appendix A.4 correctly illustrates the distinction.

2.5 The truncated predictor is more robust than it first looks
This is the most valuable part of the classical proof.

For a fixed column and query time, the simulator aborts before exceeding 
L
L queries to the target address inputs. It receives the remaining dummy input data as side information.

The direct-product lemma therefore applies to the simulator on every branch, not merely when the original decision tree happens to be light.

The proof then establishes a bound on the joint event that the original run is light and that its specified query reaches the correct certificate cell.

This avoids the invalid inference

Pr
⁡
[
success
∣
light
]
≤
(
2
/
3
)
r
,
Pr[success∣light]≤(2/3) 
r
 ,
which generally does not follow because conditioning on lightness can alter the input distribution.

The paper explicitly warns against this error and supplies a counterexample.

I would not change this mathematical structure. It is a well-designed reduction, and its careful treatment is a significant strength. 
expert_companion(2).pdf

3. The quantitative constants: mostly consistent, but their provenance matters
I independently checked the elementary numerical calculations used to finish the classical reduction.

For 
r
=
20
log
⁡
2
m
r=20log 
2
​
 m,

(
2
/
3
)
r
=
m
−
20
log
⁡
2
(
3
/
2
)
≈
m
−
11.699
.
(2/3) 
r
 =m 
−20log 
2
​
 (3/2)
 ≈m 
−11.699
 .
Therefore the manuscript's bound 
(
2
/
3
)
r
≤
m
−
10
(2/3) 
r
 ≤m 
−10
  is valid.

Using 
G
≤
m
L
/
100
G≤mL/100 and 
L
≤
m
L≤m, the three contributions to the distinguishing probability satisfy

Discovery mechanism

Upper bound

Erased zero

4
G
/
m
2
≤
0.04
4G/m 
2
 ≤0.04

Selected column is heavy

G
/
(
m
L
)
≤
0.01
G/(mL)≤0.01

Correct cell reached while light

G
(
2
/
3
)
r
≤
0.01
G(2/3) 
r
 ≤0.01

Total

At most 0.06

The resulting 
6
/
100
6/100 bound is comfortably below the 
1
/
3
1/3 distinguishing advantage required by a bounded-error algorithm.

The passage from the floor-defined allowance 
L
L to the coefficient 
1
/
400
1/400 also checks out under the stated size conditions. 
expert_companion(2).pdf

An important distinction in what is explicit
The main theorem prints

Q
(
F
k
,
m
)
≤
C
k
m
 
ℓ
6
Q(F 
k,m
​
 )≤C 
k
​
  
m
​
 ℓ 
6
 
and

R
(
F
k
,
m
)
≥
m
2
−
1
/
k
400
ℓ
2
.
R(F 
k,m
​
 )≥ 
400ℓ 
2
 
m 
2−1/k
 
​
 .
Here the logarithmic exponent six and the lower-bound coefficient 
1
/
400
1/400 are explicit, but the main quantum prefactor 
C
k
C 
k
​
  remains unspecified.

Appendix E gives a further quantitative envelope with explicit 
k
k-dependence.

The presentation should be precise about that distinction. Calling the theorem an explicit quantitative reconstruction is reasonable, but saying that all its constants are explicit would overstate what the main displayed estimate contains.

This is a small editorial issue, but a worthwhile one because specialists pay attention to such wording.

4. The actual high-risk dependencies
After this pass, I would not prioritise the elementary inequalities or the direct-product proof for immediate rewriting.

I would prioritise the places where a substantial mathematical claim depends on material outside the paper.

Exact circuit size — §2, page 4

The estimate 
S
≤
200
(
k
+
1
)
2
m
ℓ
2
S≤200(k+1) 
2
 mℓ 
2
  is important for the claimed quantum verification cost. The paper provides a plausible architectural sketch involving Walsh transforms and exact integer comparisons, but delegates the numerical gate-count derivation to the reasoning record.

Assessment: load-bearing quantitative dependency, not an identified error.

Uniform Forrelation bound — Appendix E, pages 18–19

The uniform estimate (16) supports the growing-parameter consequence. It requires significantly more analysis than the fixed-
k
k theorem, and the underlying estimates are in the reasoning record.

Assessment: the strongest claim that cannot be fully audited from this manuscript alone.

Formal correspondence — §6, page 12

The paper reports compared theorems, built refinements and a remaining retained-state correspondence boundary. Its distinctions are responsible, but this reading has not independently tested the source declarations or their dependencies.

Assessment: verification-scope question; an external Lean audit would be needed for a stronger judgement.

The key distinction here is between a proof defect and an audit dependency.

An external derivation may be entirely correct, but a referee still needs to know exactly which claims rely on it. The paper could improve considerably just by supplying more precise proof-status information at those locations.

5. An additional check of Appendix E
I also revisited the growing-parameter construction, particularly the choice

k
=
⌊
t
/
20
⌋
,
t
≥
80.
k=⌊ 
t/20
​
 ⌋,t≥80.
The placement of the radical matters. The formula is 
t
/
20
t/20
​
 , not 
t
/
20
t
​
 /20. At 
t
=
80
t=80, it gives 
k
=
2
k=2, satisfying the stated lower restriction on 
k
k.

This is a good example of why an adversarial reading must check the typeset mathematics rather than rely on imperfect extracted text.

The conceptual purpose of the parameter choice is also sensible: increasing 
k
k improves the classical exponent while increasing the quantum decoding overhead. Choosing 
k
k on the order of 
t
t
​
  balances the two losses.

I would not label this passage erroneous.

However, there are two different mathematical obligations: establishing the uniform bound that permits 
k
k to grow, and deriving the asymptotic conclusion after selecting 
k
(
t
)
k(t).

The latter is comparatively straightforward once the uniform estimates are accepted. The former is substantial.

I would separate these obligations more prominently in Appendix E. That would make the significance of the new uniform estimate clearer, without requiring the main paper to reproduce the entire analytic development.

6. What a sceptical referee is likely to challenge
I think an expert referee would be more concerned about the scope and reproducibility of certain claims than about the ordinary quality of the prose.

Likely challenge

My current assessment

Does the tournament assume transitivity?

No; the calculation avoids it

Does the quantum sampler preserve the exact conditional label law?

The paper provides an explicit argument, although its stages could be separated more clearly

Does the classical reduction assume unbiased address bits?

No; the minimax hard law is sufficient

Are the address predictor's caps genuinely worst-case?

The truncated simulator is designed to ensure this

Is conditioning on a light original execution used incorrectly?

No; the proof takes a joint-event bound

Are the displayed numerical constants consistent?

The elementary lower-bound calculations checked here are consistent

Is the exact circuit-size constant proved in the paper?

Not fully; the detailed derivation is external

Is the uniform growing-
k
k estimate independently established within these pages?

No; it relies on the companion record

Do the formal comparison results cover every strengthened statement?

The paper expressly says they do not

Has the entire mathematical interpretation of the retained physical state been formally identified?

The paper expressly says that stronger correspondence remains unresolved

That pattern is encouraging for the main reconstruction.

The obvious places to attack are not yielding an immediate contradiction, and the paper is unusually explicit about several of its limitations.

But the table also demonstrates why I would be cautious about describing it as a completely self-contained, fully formally verified proof of every displayed quantitative refinement.

Its evidential status is more differentiated than that.

7. A proposed improvement: a compact proof-dependency register
This is the largest new editorial recommendation arising from the third pass.

I would add a short table, ideally near the end of the introduction or before the formal-status section, stating the provenance of the main mathematical ingredients.

Result

Mathematical status

Where to check

Fixed-
k
k Forrelation hardness

Imported lower bound

Bansal–Sinha and §5

Exact circuit construction

Reconstructed quantitative construction

§2 sketch and reasoning record

Weighted tournament

Reconstructed proof of OpenAI mechanism

§3.2

Bounded amplifier

Standard amplification tools with a specified finite schedule

Appendix C

Separate-cap product lemma

Proof supplied in manuscript

Appendix D

Planted-cell classical reduction

Reconstructed proof

§4

Optimal exponent

Deduction using lower family and known upper bound

§5

Growing-
k
k uniform estimate

Additional quantitative analysis

Appendix E and reasoning record

Formal separation theorems

Reported checked endpoints

§6 and versioned Lean sources

The point is not to add bureaucracy.

The point is to make the mathematical claims easier to trace. A reader should know which ingredients are standard, which are original to the source preprint, which are reconstructed, and which are separate additions.

This would also make the paper more useful to somebody who wants to reuse one of its lemmas without studying the entire project.

8. How this changes my judgement about the intended audience
I am now more confident that the mathematical density is appropriate for specialists, but less confident that the exposition is optimally arranged for independent verification.

Those are different qualities.

A quantum query-complexity expert will likely be comfortable with the definitions, the search arguments and the asymptotic calculations. They may also appreciate the explicit treatment of probabilistic comparisons and the direct-product conditions.

But such a reader is likely to ask a sharper question than a general reader:

Which part of this reconstruction would I need to check myself, and which part has already been reduced to a standard result or a formally checked statement?

The paper should answer that question almost mechanically.

This is why, after three readings, I would not advocate substantially expanding the examples-first material. The companion exposition already exists for that role.

Instead, I would make this paper a particularly clean technical reference.

9. Revised assessment
Specialist mathematical exposition

8/10
Proof organisation and local clarity

8/10
Contribution and provenance clarity

7/10
Self-contained auditability

6.5/10
Subjective editorial scores. Self-contained auditability is not a score for mathematical correctness or the validity of the Lean development.
My overall judgement remains favourable, but more precise.

The paper is not primarily suffering from weak technical writing. Many of the demanding arguments are unusually attentive to assumptions. The core proof is organised in a coherent sequence and its local reasoning is often careful.

Its greatest outstanding weakness is the difference between containing enough material for a knowledgeable reader to reconstruct the justification and presenting that justification in a readily auditable form.

I would prioritise the latter.

10. The next pass should be different again
The first review considered the paper's contribution, audience and structure. The second examined the reading experience. This third pass tested the main mathematical inferences and identified the strongest external dependencies.

For the fourth pass, I would stop treating the document in isolation and conduct a source-comparison and provenance review.

OpenAI's original paper, A Nearly Quartic Separation Between Randomized and Quantum Query Complexity, is available in its October 2026 mathematical release. 

GitHub
 The Bansal–Sinha Forrelation result is also independently identifiable in the published literature. 

arXiv

The next genuinely useful questions are whether the reconstruction preserves the original argument faithfully, whether the explicit refinements are accurately attributed, whether claims of independent reconstruction are sufficiently distinguishable from established results, and whether the Lean endpoints faithfully represent the precise manuscript statements.

That would be a more demanding exercise than another general writing critique, and it would avoid merely repeating the same recommendations.

Third-pass conclusion: I am increasingly convinced the manuscript has a sound expository design for its main theorem. The biggest opportunity now is to make its mathematical provenance and verification boundaries as rigorous in presentation as the proof arguments themselves.




