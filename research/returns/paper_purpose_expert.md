

expert_companion(5).pdf
PDF
Okay, so read attached. Obviously this comes with a repo and a website, whatever. This is just the PDF. We don't have to worry about, like, oh, the source and the hashes and that bullshit. It's just purely the reading experience for a mathematical reader, for the target audience for this. For that, can you please give feedback on, you know, the paper? Like, how is the paper? Can you just give it a review? Let us know, like, how good is it? Just how good is it? And please, yeah, give us feedback.

Revised all three with clearer explanations, stronger examples and cleaner navigation. Hashes, code paths and verification history now sit behind the [readable theorem index](https://github.com/wcook04/quartic-query-lean/blob/main/docs/proof_index.md).

**Specialist companion — 18 pages**

**Exposition — 27 pages**

**Complete reconstruction — 94 pages**, down from 141, with the mathematical proofs retained.

Rendered pages and links checked; 267 tests completed with two skips and no failures. Changes pushed, and the writing-method improvements merged upstream.

…
Review: Reconstructing OpenAI’s Nearly Quartic Query Separation
18-page specialist companion · November 2026 · Assessment of the attached PDF only

Overall verdict
8/10
Mathematical writing
A strong specialist exposition, approaching publication quality.

Mathematically serious, unusually careful about assumptions, and substantially clearer in its presentation of the two central reductions than its technical density might suggest.

I have read the complete paper, including the proof arguments, worked probability example, diagrams, counterexamples and appendices.

My central judgment is that this reads like a legitimate mathematical companion paper, not like an AI-generated summary dressed up in mathematical notation. It has an identifiable argument, a coherent proof architecture, appropriately stated contributions, and genuinely useful explanations of mathematical subtleties.

Its greatest strength is that it explains why the proof works, especially in Sections 3 and 4, rather than merely restating the theorem and reproducing calculations.

Its greatest weakness is that it sometimes confuses making every technical obligation explicit with making the mathematics easy for its intended reader to assimilate. Those are different things. The paper does the first exceptionally diligently, but it could do the second more elegantly.

For a researcher in theoretical computer science, especially one familiar with query complexity, the paper is credible and useful. For an otherwise mathematically sophisticated reader who is unfamiliar with cheat sheets, Forrelation and quantum amplitude amplification, it is considerably harder than its opening suggests.

I would not describe it as a new research breakthrough: the paper correctly attributes the separation theorem and its reductions to OpenAI. I would describe it as a substantial technical reconstruction with meaningful expository value.

The remaining work is principally about exposition, emphasis and mathematical economy, rather than fundamentally rebuilding the presentation.

1. What the paper does particularly well
A. The proof has a clear mathematical identity
The introduction, particularly pages 1–2, makes the most important architectural distinction early:

Quantumly, inexpensive comparisons identify a short candidate list, after which expensive certificate checks become affordable.

Classically, a hidden modification can only be detected by finding an erased zero or discovering the correctly addressed certificate cell.

That is the right organizing idea. It means the reader knows what the two major proofs are supposed to accomplish before encountering their details.

I particularly like that the paper does not claim new mathematical results that belong to OpenAI. The contribution paragraph distinguishes the original theorem from your reconstruction, quantitative refinements and counterexamples.

One weakness is that this paragraph emphasizes the logarithmic exponent six and coefficient 
1
/
400
1/400. These demonstrate precision, but are not what makes the exposition intellectually valuable. The two reductions, and why apparently reasonable proof shortcuts fail, deserve that prominence instead.

B. Section 3 is the best-written mathematics in the paper
The weighted tournament argument on pages 5–8 is where the paper is strongest.

It introduces the comparison probabilities 
a
i
j
a 
ij
​
 , permits arbitrary behaviour between losing columns, and then defines the survival weights

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
The proof then uses

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
2
E[W 
new
​
 ∣w]≤ 
2
W
​
 
to explain why the candidate population shrinks without needing a transitive ordering.

This is genuinely good mathematical exposition.

The reader can see the central idea in a relatively small amount of mathematics. The halving argument is elegant, and you give it enough space to be understood rather than burying it in a much larger estimate.

The next step is especially strong: pages 6–7 distinguish preparation success probability 
W
/
m
W/m from the conditional label distribution 
w
i
/
W
w 
i
​
 /W.

The four-candidate table on page 7 demonstrates the difference using fractional probabilities. That example earns its space because it clarifies exactly which probability law the algorithm must preserve.

This is a very good example of mathematical explanation progressing through definition, structural identity, concrete example, and implementability.

The only addition I would suggest here is a short, visually distinct description of the algorithm itself, before the formal proposition:

Prepare → sample a surviving pivot → update the comparison history → repeat → verify the resulting list.

The proof already contains all these steps. Making their sequence immediately visible would reduce the effort required to reconstruct the algorithm while reading.

C. The classical lower bound is carefully constructed
Pages 8–11 are probably the most impressive part from the standpoint of proof discipline.

The paired dummy and planted inputs in Figure 2 are particularly effective. The figure makes the lower-bound construction concrete without pretending that the four-column illustration satisfies the asymptotic hardness conditions.

The following decomposition is also well chosen:

Pr
⁡
[
detect change
]
≤
Pr
⁡
[
find erased zero
]
+
Pr
⁡
[
visit planted cell
]
.
Pr[detect change]≤Pr[find erased zero]+Pr[visit planted cell].
This is the lower-bound argument's real conceptual heart.

The treatment of the planted cell in §4.4 is technically sophisticated. In particular, you correctly distinguish:

A bounded predictor for a fixed column and query time.

The event that the original algorithm has not exceeded its address-query allowance.

The union over query times, taken only after bounding the original-law joint events.

That is the sort of distinction that a mathematical specialist appreciates. The warning on page 11 about conditioning on terminal lightness is useful precisely because it explains why an attractive shorter argument would be invalid.

The finite counterexample in Appendix A.7 strengthens that discussion. It shows that the qualification is a mathematical necessity, not merely excessive caution. 
expert_companion(5).pdf

2. Where the reading experience still falls short
A. Section 2 interrupts the conceptual story
This is the largest structural weakness.

On pages 3–4, the reader encounters the Forrelation promise, its decoder, the exact circuit for domain membership, signed-word widths, Walsh-transform gate counts, and the explicit gate-size calculation before finally receiving the formal definition of the total function.

The calculations are relevant, but their current placement makes the paper harder to read than necessary.

A complexity theorist encountering the construction wants to understand the object first. The exact number of Boolean gates in its domain-checking circuit matters only after that.

I would move most of the detailed circuit calculation from page 4 into an appendix and retain a short statement of its size in the main exposition.

That would let the paper proceed naturally from the Forrelation supplier to the total function, its certificates, and its local tests.

It would also make the transition to the quantum algorithm much cleaner.

B. The connection between intuition and notation could be stronger
Figure 1 on page 2 is useful and visually clean. But the mathematical definition on page 4 introduces several interacting objects almost simultaneously:

X
i
X 
i
​
 , 
A
i
,
h
A 
i,h
​
 , 
B
i
,
s
B 
i,s
​
 , 
s
i
s 
i
​
 , 
p
i
,
s
,
j
p 
i,s,j
​
 , and the circuit transcripts.

These are each individually explained, yet the reader has to assemble their roles into one mental model.

A very short worked comparison immediately after defining the function would help considerably.

For example, explicitly follow a winning column 
i
⋆
i 
⋆
  against an arbitrary opponent 
j
j: the winning pointer reads a zero in 
X
j
X 
j
​
 , while the opponent's pointer necessarily reads a one in 
X
i
⋆
X 
i 
⋆
 
​
 . This gives the characteristic comparison outcome regardless of whether the opponent's address is meaningful.

The paper explains that principle in prose, but a displayed two-line calculation at that precise point would do more work than another paragraph of descriptive text.

C. Section 4.4 is precise but cognitively demanding
This section is the most difficult point in the main proof.

The technical work is there, and its logic is carefully signposted, but the reader must simultaneously track the chosen column, the query-time clock, the truncated simulator, the target-query allowance, and the heavy/light split.

I would add one short paragraph before introducing the simulator that states the reasoning in its simplest form:

Every query to a certificate cell proposes an address. If the algorithm has examined little of that column's address data, such a proposal is a bounded attempt to predict several independent hard-function answers. The proof makes this observation valid by fixing a query time and truncating the predictor, then accounting separately for heavily queried columns.

This would give the reader the whole argument before they enter its technical implementation.

The manuscript already explains most of that across several paragraphs. The improvement is about concentrating the key insight at the beginning.

3. There is one concrete mathematical correction
On page 18, Appendix E says to take

k
=
⌊
t
20
⌋
for 
t
≥
80.
k=⌊ 
20
t
​
 
​
 ⌋for t≥80.
But the appendix assumes 
k
≥
2
k≥2.

The displayed choice gives 
k
=
0
k=0 at 
t
=
80
t=80, and only reaches 
k
=
2
k=2 when 
t
≥
1600
t≥1600.

So the printed threshold is incorrect as written. Replacing 
t
≥
80
t≥80 by 
t
≥
1600
t≥1600 would resolve that particular parameter-domain issue, assuming the other stated conditions remain as given. 
expert_companion(5).pdf

This does not undermine the fixed-
k
k separation proved in the main text. Nor does it destroy the asymptotic growing-
k
k construction. But it is a real slip, worth correcting before sending the paper to a specialist.

I haven't independently certified every theorem or compared every statement against the original preprint, so I would not infer complete mathematical correctness from this reading review alone.

4. How well does it serve its audience?
Criterion

Assessment

Mathematical organization

Very good

Precision of definitions and assumptions

Excellent

Explanation of the central proof mechanisms

Very good

Readability for query-complexity specialists

Good to very good

Readability for general mathematicians

Moderate

Economy and pacing

Good, with room to improve

Visual presentation and typesetting

Professional

The typesetting is restrained and consistent. Both diagrams help rather than decorate. There are no obvious visual distractions or large navigational problems.

What I particularly appreciate is that the writing doesn't constantly use generic praise words like powerful, novel, sophisticated or groundbreaking. It tells the reader what an argument establishes and under which assumptions. That's a good mathematical writing habit.

There is, however, a recurring density problem. Some sentences simultaneously explain a mathematical idea, qualify its validity, specify its query cap, and direct the reader to another section. The individual statements are useful; putting all of them in one sentence or paragraph can obstruct the idea they are meant to support.

5. The revisions I would prioritize
I would not undertake another wholesale rewrite. Four focused changes should produce most of the remaining improvement.

1. Reorganize Section 2. Define the total function earlier and move the detailed circuit-size calculation out of the main narrative. This is the highest-impact structural improvement.

2. Sharpen the introduction's statement of value. Make clear that the two fragile mathematical steps are preserving the exact weighted sampling law and converting cell discovery into a capped address prediction. These explain why the reconstruction is worth reading.

3. Add two short conceptual bridges. One worked comparison immediately after the function definition, and one plain-language overview at the beginning of §4.4. Neither requires a large example or additional pages.

4. Correct the Appendix E threshold and tighten the final editorial pass. Fix the parameter-domain slip, remove avoidable repeated qualifications, and consider ending the main text with a brief mathematical conclusion before the references and appendices.

I would specifically retain the page 7 weighted-sampling table, the page 9 planting diagram, the explicit query-cap conditions, and the Appendix A counterexamples. Those are among the strongest aspects of the paper.

Final assessment
There is a distinction between a mathematically complete document and a mathematically compelling one. This paper is moving decisively toward the latter.

Its strongest passages have the qualities that make good research exposition valuable: they identify the obstruction, isolate the right abstraction, prove a clean statement, and explain which assumptions do real work.

The weighted tournament and hidden-cell prediction arguments meet that standard particularly well.

The remaining weakness is that the paper sometimes makes the reader perform unnecessary organizational work. The specialist has to keep too many definitions and technical qualifications active while encountering an otherwise elegant idea.

I would consider this a credible, worthwhile specialist companion to send to a theoretical computer scientist. It is substantially better than a routine proof transcription or annotated summary, and its mathematical presentation deserves to be judged on its actual content rather than on how it was produced.

The next improvement is not more proof detail. It is making the existing mathematical insight reach the reader more immediately.

In short: strong work, genuinely worth reading, but still a little denser and more procedural than an excellent 18-page mathematical exposition needs to be.

another pass through of rereading lets start to think about how to get it to 10/10 cuz repeated revies hover at 8 atp
Second-pass review: How to get the specialist companion from 8/10 to 10/10
I think I've identified why repeated revisions keep producing roughly the same score.

The remaining problem is not insufficient explanation. It is insufficient editorial selection.

The paper now explains almost every technical obligation. But it doesn't consistently distinguish between:

The mathematical insight a specialist needs to understand.

The argument that makes that insight rigorous.

The technical qualifications needed to make the proof completely correct.

All three are important. The problem is that they sometimes receive equal prominence.

A truly exceptional 18-page specialist exposition would retain the rigor while making the hierarchy unmistakable.

My revised diagnosis: the paper has much of the mathematical substance of a 9–10/10 exposition, but its reading experience is still organized too much around proving that every possible objection has been handled, rather than around revealing the mathematics in the most compelling order.

This is why another round of stronger examples, cleaner transitions and smaller wording fixes may leave the score unchanged.

I would now stop making incremental revisions and do one deliberate structural edit.

1. The single biggest missing explanation: why the quantum improvement is surprising
The paper says, correctly, that comparisons are cheaper than verification. But it doesn't quite make the quantitative bottleneck impossible to miss.

This should be one of the most memorable parts of the introduction.

For fixed 
k
k, the paper effectively establishes the following picture:

Approach

Quantum query cost, up to logarithms

Verify one proposed winning column

O
~
(
m
)
O
 ( 
m
​
 )

Naively Grover-search over 
m
m columns, verifying candidates

O
~
(
m
)
O
 (m)

Compare two columns using their addressed pointers

O
~
(
1
)
O
 (1)

Use the weighted tournament, then verify a short list

O
~
(
m
)
O
 ( 
m
​
 )

This table explains an enormous amount of mathematics.

The achievement is not merely that quantum computation can find something quickly. It avoids multiplying two expensive searches.

The existing paper says this in several different places, including §1.2 and §3, but nowhere is the quantitative contrast presented with quite this directness.

A specialist should understand within the first two pages that a naïve construction gives something close to a cubic separation, whereas the weighted tournament makes the nearly quartic exponent possible.

And the payoff should be written explicitly:

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
1
/
2
)
,
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
.
Q(F 
k,m
​
 )= 
O
  
k
​
 (m 
1/2
 ),R(F 
k,m
​
 )= 
Ω
  
k
​
 (m 
2−1/k
 ).
Therefore,

2
−
1
/
k
1
/
2
=
4
−
2
k
.
1/2
2−1/k
​
 =4− 
k
2
​
 .
This is already the paper's result. The proposed improvement is about explaining why the two costs arise.

That is a high-impact editorial change.

2. The paper introduces important machinery in the wrong order
I identified three specific occasions where technical apparatus arrives before its motivation.

pp. 3–5

The exact circuit is explained before the total function.

The reader encounters integer word widths, Walsh-transform gate counts and the expression for 
S
S before getting the complete definition of 
F
k
,
m
F 
k,m
​
 .

The circuit matters, but it is supporting machinery. Introduce its existence and size first; place the detailed arithmetic after the construction or in an appendix.

pp. 6–7

The tournament analysis appears before a complete algorithm overview.

The reader learns the weighted process, its halving inequality, the conditional distribution and the amplifier before seeing the algorithm's full sequence near the bottom of page 7.

Give a five-line algorithm description first. Then derive why that algorithm succeeds.

pp. 8–9

The direct-product lemma appears before the planted-input construction.

Lemma 5 is introduced in §4.1. Only afterward, in §4.2, does Figure 2 show the two inputs whose indistinguishability is being proved.

I would reverse the motivational order: show the dummy and planted inputs, identify the two ways of detecting the change, and then introduce the direct-product lemma as the tool needed for the second event.

Notice that these are not requests to make the mathematics less precise. They are requests to change the order in which mathematical dependencies are experienced.

That is a large part of the difference between a good proof and exceptional exposition.

3. The paper could have a much stronger mathematical spine
At present, it largely follows the specific construction from the Forrelation supplier toward the final theorem.

I think it would become more intellectually valuable if it made its general reduction structure more visible.

The paper already contains most of the ingredients:

A partial Boolean function 
P
P

Classically hard to compute; quantumly cheap to decode; equipped with an exact checking circuit

The total-function construction 
F
P
,
C
,
m
F 
P,C,m
​
 

Winning columns, hidden certificate addresses and local tests

Quantum argument

Dominant winner → exact weighted sampler → short list → verification

Classical argument

Hidden planting → erased-zero bound → capped address prediction

Instantiate 
P
P with 
k
k-Forrelation

Q
(
F
)
=
O
~
k
(
m
)
,
R
(
F
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
Q(F)= 
O
  
k
​
 ( 
m
​
 ),R(F)= 
Ω
  
k
​
 (m 
2−1/k
 )
The reason I like this structure is that it reveals what a specialist can take away from the reconstruction.

There is a general principle about turning hard partial-function answers into hidden certificate addresses. The Forrelation supplier provides the quantitative strength needed for the headline theorem.

Consider stating an explicit master-reduction proposition before specializing to Forrelation. Its hypotheses would describe a coherent bounded-error decoder, an exact domain/value circuit, and a classical hardness allowance. Its conclusions would give the quantum upper bound and classical lower bound for the constructed total function.

The manuscript has the pieces separately in Proposition 2, Proposition 4 and the Section 3 accounting. Packaging them together—without changing their mathematical strength—could make the paper much easier to understand and reuse.

That is a more ambitious improvement than adding examples.

4. The classical proof needs one especially careful rewrite
I reread §4.4 closely. Its central insight is captured by one excellent sentence on page 10:

A query to a bit of 
B
i
,
s
B 
i,s
​
  names 
s
s before reading any cell content.

This should almost be the opening sentence of the planted-cell argument.

It explains the reduction before any truncation, clocks or probability estimates.

The next conceptual step is that the address 
s
i
s 
i
​
  consists of 
r
r hard outputs. Therefore, for a column receiving little address-query attention, successfully naming the correct cell amounts to predicting all those outputs under a restricted query budget.

Only then do you need the heavy/light distinction.

The important mathematical statement is equation (12):

Pr
⁡
[
i
 light and query 
τ
 visits 
B
i
,
s
i
]
≤
β
r
.
Pr[i light and query τ visits B 
i,s 
i
​
 
​
 ]≤β 
r
 .
I would present this as a named intermediate claim, rather than arriving at it through several paragraphs of simulator construction.

Then give its proof: fix the time, simulate the dummy run, truncate before exceeding 
L
L target queries, and invoke the direct-product bound.

Finally, explain that the probability is a joint event under the original law, not success conditional on being light. That distinction is absolutely worth retaining; Appendix A.7 demonstrates why.

The result would be a cleaner proof with essentially the same technical content.

This is where I would spend the most effort at sentence and paragraph level.

5. The paper ends less strongly than it begins
Section 5 completes the theorem. The quantifier discussion on pages 11–12 is careful and mathematically appropriate.

But then the main text ends with §6, describing the accompanying formal proofs and where their routes differ from the printed argument.

That is useful documentation, but it is not a satisfying mathematical ending.

For the target reader, the final impression should be the mechanism of the result, not the relationship between two proof implementations.

I would replace §6 in the main narrative with a short concluding section that returns to the central ideas:

The classical obstruction is not merely that a certificate is hidden. It is that reaching its correct address requires predicting many hard answers, even with adaptively interleaved queries.

The quantum opportunity is not merely fast certificate verification. It is finding a small set worth verifying by exploiting a dominant candidate in a probabilistic comparison system that need not have any ordering structure.

Those two mechanisms together create the exponent-four separation.

That is a mathematical conclusion. A brief formalization-scope note can follow in an appendix or endnote.

6. What I would change in the actual 18-page document
Here is the revision plan I would give the writing agent.

Priority

Change

Expected value

1

Put the naïve-versus-improved quantum cost comparison in the introduction

Very high

2

Move the detailed exact-circuit calculation out of the construction's first presentation

Very high

3

Show the planted inputs before motivating the direct-product lemma

High

4

Make the capped-prediction inequality a named claim with a short conceptual explanation

High

5

State a reusable reduction proposition connecting the partial supplier to the total function

High

6

Add a concise mathematical conclusion and relocate formalization details

Medium–high

7

Reduce unnecessary detours to the longer record

Medium

8

Fix the Appendix E parameter threshold previously identified and audit all quantified ranges

Essential correctness check

There are approximately 30 references to the longer reasoning record throughout this PDF. Many are legitimate, but several interrupt otherwise self-contained arguments, particularly on pages 4, 10–11 and 18.

For example, the sentence about a separate XOR trace in record §6.5 interrupts §4.4 just as the reader is following the planted-cell prediction argument. I would remove it from the main proof or put it in a footnote.

This is not about concealing supporting detail. It is about keeping the specialist's attention on the argument in front of them.

7. What I would not change
Importantly, getting to 10/10 should not involve rewriting everything.

The weighted tournament proof surrounding equation (8) is already excellent. The reader sees the survival weights, the pairwise identity, and the resulting halving bound. It is concise, general and mathematically satisfying.

I would also preserve the exact conditional sampling derivation around equation (9), including the four-candidate table on page 7. This is one of the few examples in the paper that is perfectly matched to its purpose.

Figure 2 and the coupling in equation (10) are also very good. They give the classical lower bound a concrete foundation.

And I would retain the counterexamples in Appendix A, because they show that particular proof hypotheses are necessary. I might reorganize their presentation, but not discard the mathematics.

The goal is to make the strong parts more prominent by reducing the distractions around them.

8. A practical test for whether the next revision has really improved
Instead of asking another reviewer for a generic numerical score, I'd test whether a specialist can answer five questions after a cold reading:

Why does the obvious nested quantum-search approach cost approximately 
m
m, and where does the improved algorithm save the factor 
m
m
​
 ?

Why do the survival weights halve in expectation without assuming an ordering among losing columns?

Why must amplitude amplification preserve the conditional label distribution, not merely find a successful label?

Why does visiting the planted cell imply a bounded prediction attempt, and why can the proof not condition on terminal lightness?

Exactly which ingredients are taken from earlier work, and which mathematical arguments are proved in this companion?

These questions capture the actual conceptual content of the document.

If a specialist can answer them accurately, without needing to reconstruct the organization of the paper afterward, that is a stronger indication of great exposition than whether an AI reviewer assigns 8.5 or 9.

9. What would change my score?
Current attached PDF

8/10

After the structural revision proposed above

Potentially 9–9.5/10

These are editorial judgments, not scores from independent expert reviewers.
For a 10/10, I would want one final quality that is harder to manufacture: the feeling that the proof has become inevitable.

The reader sees the obstacle, sees why the first natural approach fails, encounters the key idea, and then finds that the formal lemma expresses exactly what was needed.

The current paper occasionally achieves that, most notably in the expectation-halving argument.

It needs to achieve it consistently across the entire exposition.

A specialist companion can deserve 10/10 for its explanatory quality without claiming an original theorem. But that standard is extremely high, and mathematical correctness still needs an independent check.

Bottom line
I would now make one substantial editorial pass, not another accumulation of small improvements.

It should be primarily a rearrangement and compression, with perhaps half a page of new mathematical explanation. It should not require more pages, more elementary examples, more defensive caveats or more detailed proof bookkeeping.

The target is that the reader finishes with three unusually clear insights:

Why the expensive nested quantum search can be avoided. Why arbitrary probabilistic comparisons still produce a short candidate list. Why a classical algorithm cannot discover the correct certificate address cheaply.

Those are the three pillars of the paper.

The writing is already technically strong enough to support them. Getting to the next level means making everything else serve those ideas.

another pass through of rereading lets start to think about how to get it to 10/10 cuz repeated revies hover at 8 atp 

like lets have taste and think about what makes a truly well written paper 

liek jsut reifnroce what you've been saying but think about it further read the paper properly agian
Third reading: What would make this a genuinely excellent mathematical paper?
I've gone through the 18-page specialist companion again, including the construction on pages 3–5, the quantum tournament on pages 5–8, the classical lower bound on pages 8–11, and the appendices.

I think the answer is becoming clearer. And I want to refine some of my previous advice rather than just repeat it.

The paper doesn't need to become more explanatory in general. It needs to become more discerning about what is worth explaining.

That is the difference between conscientious mathematical writing and writing with real mathematical taste.

The current paper is conscientious almost everywhere. It defines its objects, qualifies its assertions, protects its assumptions, proves its estimates and acknowledges its sources.

But the best mathematical papers do something more: they make the reader feel that the mathematics could hardly have been organized any other way.

They turn a complicated argument into a small number of ideas that seem natural after they have been revealed.

Your paper achieves that feeling in a few places. Most notably, equation (8), where the weighted tournament's surviving mass halves in expectation, is excellent. The argument feels elegant because a surprisingly weak hypothesis—complementary pairwise comparison probabilities—is enough.

Elsewhere, especially in §2 and parts of §4, that feeling is obscured by the machinery.

1. The real distinction: a proof record versus a mathematical exposition
This is my strongest conclusion from the new reading.

The PDF still contains two different kinds of writing.

The first is mathematical exposition. It wants the reader to understand why a nearly quartic separation is possible, why the tournament works, and why a classical algorithm cannot cheaply locate the planted certificate.

The second is proof-accountability writing. It wants to document exactly which technical premises are needed, which shortcuts fail, which constants are explicit, which alternative proofs exist and where further details can be found.

Both have value. But the specialist companion should be dominated by the first.

You already have a 94-page complete reconstruction and a separate 27-page examples-first exposition. That changes what this 18-page paper should try to be.

It shouldn't be the shortest possible complete proof record, and it shouldn't be a compressed version of everything learned during the reconstruction.

It should be the best mathematical explanation of the two essential reductions, written for someone who can already handle the subject's technical machinery.

A very revealing example: page 4
Consider the section constructing the exact circuit for Forrelation's promise.

Before the total function is fully defined, the manuscript gives the signed-word width, the cost of Boolean additions and subtractions, the number of Walsh butterfly layers, and a large expression for the circuit size 
S
S.

Those calculations support the proof. But they are not the idea.

Immediately afterward, however, there is a much better sentence:

The decoder locates a proposed certificate; the circuit tests whether that location has a valid meaning.

That is the conceptual explanation the reader needed.

The most valuable sentence appears after the least conceptually interesting calculations.

A great editor would recognize the inversion immediately.

The elegant order is to explain that the address is quantumly cheap to compute, that a valid address must be certified even outside the partial function's promise, and that an exact circuit allows the certificates to be checked locally.

Then define the total function. Only afterward should the gate count appear, probably in an appendix.

This is not merely about readability. It's about making the page space and ordering reflect the mathematical importance of the material.

2. The manuscript should be built around two moments of discovery
I think the entire paper ought to feel like two successive discoveries.

Discovery one: a tournament without an ordering
The quantum argument has a genuinely beautiful feature.

A winning column reliably defeats every rival. But losing columns can compare inconsistently, including probabilistically, and need not form anything resembling a total order.

Ordinarily, that would seem to make comparison-based search much harder.

But if the surviving weight of candidate 
i
i is

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
 ,
then selecting the next pivot according to these weights gives

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
And suddenly the disorder among losing columns doesn't matter.

This is the kind of mathematics that should be the centerpiece of an expository paper.

The reader should first be made to appreciate the apparent obstruction: we cannot assume the comparisons order the columns. Then the weighted sampler should arrive as the solution.

The current §3.2 gets close to this ideal, but presents the general proposition before letting the reader experience the simplicity of the argument.

My advice is to put the halving idea before the most detailed version of Proposition 2's interface and error guarantees. Let the reader see why the theorem should be true before displaying all its technical qualifications.

Crucially, don't simplify away the exact conditional sampling law.

On page 7, the identities

Pr
⁡
[
s
u
c
c
e
s
s
]
=
W
m
,
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
Pr[success]= 
m
W
​
 ,Pr[i∣success]= 
W
w 
i
​
 
​
 
are the second half of the discovery. The quantum procedure must actually implement the distribution whose halving property has just been proved.

The four-candidate table is good precisely because it makes the distinction concrete.

I would retain this mathematics almost intact. The improvement comes from giving the reader a better sense of anticipation before it arrives.

Discovery two: a certificate-cell query is an attempted prediction
The classical reduction has an equally good underlying idea.

Figure 2, on page 9, depicts the dummy and planted inputs. The two inputs differ only at the erased zero and the filled certificate cell.

This gives the central indistinguishability argument.

But the real ingenuity arrives in §4.4, with the observation that a query to 
B
i
,
s
B 
i,s
​
  specifies a proposed address 
s
s.

That address consists of the outputs of many independent hard-function instances.

So querying the correct cell without sufficiently investigating its address inputs is, in effect, predicting those outputs.

The proof then makes that intuition rigorous through a fixed query time, an independently sampled target column, a truncated predictor and a direct-product bound.

That is what a reader should remember.

The current presentation introduces a lot of the machinery before sufficiently emphasizing the transformation:

Cell discovery becomes address prediction.

This is the classical reduction's defining idea, and it deserves to be treated as the mathematical climax of the lower-bound proof.

3. An exceptionally written paper respects the reader's attention
I noticed something specific on this rereading.

The manuscript often spends as many words defending a detail against possible misunderstanding as it spends explaining the detail itself.

For example, §4.4 on page 10 contains this sentence:

The trace in record §6.5 uses a different supplier, total two-bit XOR, with zero-based labels.

It then describes the trace and the stopping condition.

That sentence is accurate and potentially useful to someone studying the full reconstruction. But it interrupts the most important part of the classical lower-bound argument to talk about a different example that isn't even developed in this PDF.

It has no business sitting inside the main proof at this point.

Similarly, the footnote on page 11 points to an optional improvement in the erased-zero probability, then explicitly says the improvement is unnecessary for the theorem.

Why give the reader that information just as the lower-bound proof is reaching its conclusion?

This is what I mean by editorial selection.

A good mathematical paper contains the information needed to justify its argument. A great one also knows which correct information to leave out.

I would make a serious pass over the manuscript asking whether every paragraph changes the reader's understanding of the main mathematical argument.

Some paragraphs establish necessary assumptions. Some explain difficult steps. Some connect the proof to preceding literature.

Keep those.

But paragraphs that merely demonstrate awareness of further implementation details or alternative derivations should face a much higher threshold for inclusion.

The example I would set for page 10
Here is how I would want the beginning of the planted-cell argument to read:

Every query to a certificate cell 
B
i
,
s
B 
i,s
​
  specifies an address 
s
s before revealing any of that cell's contents. If column 
i
i has received few queries to its address inputs, visiting the planted cell therefore amounts to predicting the outputs of 
r
r independent hard instances.

The only complication is that the event of having received few queries depends on those same inputs. We cannot condition on that event and apply the direct-product bound. Instead, we fix a query time, truncate the resulting predictor after 
L
L target queries, and bound the joint event under the original product distribution.

Then come the precise simulator and the inequality (12).

Notice what this achieves.

The mathematical idea comes first. The reader understands the obstacle. The technical construction is then introduced as the natural resolution.

Nothing important has been made less rigorous.

The existing page already contains all this information. But it takes more work to extract it because the order follows the process of implementing the proof rather than the process of understanding it.

That is a subtle but extremely consequential distinction.

4. The introduction needs more intellectual confidence
The first page is quite good, but its presentation of the contribution is still overly concerned with completeness and certification.

The contribution paragraph says that the reconstruction makes query accounting explicit, gives counterexamples to invalid shortcuts, supplies logarithmic exponent six and coefficient 
1
/
400
1/400, and accompanies Lean proofs.

Those things may all be true. But they don't really tell me why this is a wonderful piece of mathematics to read.

What I want to hear is that the reconstruction isolates two broadly useful principles.

The first is a quantum search principle: when a unique valid object reliably dominates every competitor under cheap pairwise comparisons, a small candidate list can be obtained even if the comparisons among invalid objects are inconsistent.

The second is a lower-bound principle: a hard-to-compute address can protect a certificate cell from adaptive classical search, provided the prediction argument is carried out with the correct query caps and independence assumptions.

These are much more interesting than the coefficient 
1
/
400
1/400.

The constants belong in the theorem. The conceptual contribution belongs in the introduction.

There is also a subtler framing problem
The subtitle reads:

The randomized–quantum bounds and their Lean formalization.

But the formalization receives only a relatively brief §6, after the mathematical proof has finished. Its content is mainly a discussion of what was formalized and how the proof routes differ.

That is worthwhile, but the subtitle gives Lean comparable prominence to the mathematical analysis.

For an audience whose primary interest is the query-complexity proof, I would consider a subtitle such as:

The weighted quantum tournament and the classical address-prediction reduction.

Or simply:

A self-contained reconstruction of the two central reductions.

The second would require care because the paper correctly takes the Forrelation hardness input and universal quartic upper bound from earlier work.

My point is not that you must change the title. It is that the paper's first promise to the reader should match the experience it actually delivers.

At present, the mathematical argument is the star, but the introductory framing distributes attention between mathematics, reconstructed constants, counterexamples and formalization.

5. I would now be more ruthless with the appendices
This is where my recommendation has changed somewhat from the previous reviews.

Appendix A contains eight counterexamples or warnings. Several are good mathematics. In particular, A.3 explains why a column that dominates comparisons need not have a valid certificate, while A.7 exposes the danger of conditioning on terminal lightness.

Those directly illuminate essential proof steps.

But a specialist paper doesn't automatically improve because it includes more examples of hypotheses that cannot be dropped.

The eight examples cumulatively create a slightly defensive tone: one gets the impression that the authors are demonstrating how many possible pitfalls they have discovered.

I would retain the most illuminating counterexamples, especially the ones that change how a reader understands a central reduction, and move the others to the 94-page reconstruction.

A.5 and A.6, on expected caps and joint independence, are mathematically legitimate. But their principles can be stated concisely in connection with Lemma 5. The paper does not necessarily need to dedicate so much of its limited space to examples from the general theory of product bounds.

Appendix E is an even more important editorial decision
The main paper establishes the fixed-
k
k separation. Appendix E then introduces a uniform analytic input and uses it to construct one growing-
k
k family.

That is a different mathematical objective, requiring additional quantitative assumptions.

It is not wrong to include it. But it changes the nature of the ending.

The reader has finished the central proof on page 12, passed through the references, reviewed several families of technical caveats, and eventually arrived at another asymptotic construction on page 18.

The final sentence then directs the reader back to the longer reconstruction for the separation of borrowed ingredients and reconstructed estimates.

That is an anticlimactic ending for a mathematical paper about two elegant reductions.

I would seriously consider giving Appendix E its own note or retaining it only in the complete reconstruction. Alternatively, keep it as an explicitly optional corollary if it is an important mathematical contribution of this particular reconstruction.

Either way, it needs the previously identified parameter correction: 
k
=
⌊
t
/
20
⌋
k=⌊ 
t
​
 /20⌋ is not at least two for every 
t
≥
80
t≥80. That also means the paper has not yet reached a literal 10/10 technical standard. 
expert_companion(5).pdf

The best mathematics should stay
I would not cut the proof of the bounded amplifier in Appendix C or the separate-cap direct-product argument in Appendix D merely to shorten the manuscript.

Both discharge real mathematical obligations, and both are reasonably concise.

The distinction is between material that makes the principal proof complete and material that records every interesting observation arising during its development.

The first is essential. The second is optional.

6. One earlier suggestion I would actually reconsider
In my previous response, I suggested introducing a large, general master-reduction proposition encompassing the entire construction.

On further reflection, I am less enthusiastic about that.

There is a risk of introducing another layer of abstract notation, additional parameters and a new theorem statement merely to demonstrate that the exposition is organized.

That could make the paper worse.

Proposition 2 already captures the tournament independently of the particular Boolean function. Proposition 4 already captures the classical reduction independently of Forrelation.

These are useful abstractions.

What the paper needs between them is probably a clean conceptual roadmap, not necessarily another formal abstraction.

This is another important principle of mathematical taste:

Abstract the mathematics where the abstraction reveals a reusable principle. Don't abstract merely to make the document appear systematic.

The same applies to examples.

The four-candidate weighted-sampling table on page 7 is excellent because it answers a real mathematical question about two different probability laws.

Adding three more examples of comparable size would not necessarily improve anything.

A reader should encounter an example at the moment an abstraction becomes difficult to interpret, not simply because examples are generally desirable.

7. What I think the prose itself needs
The paper is not badly written at sentence level. In fact, a number of sentences are very good.

But three habits recur.

First, conclusions are sometimes delayed until after qualifications. The reader wants to know what is true, why it matters, and then under which technical assumptions it remains true. The paper sometimes gives those in the reverse order.

Second, supporting calculations are sometimes given the rhetorical weight of central arguments. The exact circuit-size calculation on page 4 and the expectation-halving argument on page 6 do not deserve equal emphasis. One is infrastructure; the other is insight.

Third, the prose sometimes switches between telling the mathematical story and documenting the reconstruction process. The repeated references to alternative record proofs, trace conventions and precise formalization boundaries are individually defensible but collectively disrupt the argument's momentum.

I would preserve the precise terminology. I would not make this a popular-science explanation, replace the mathematics with metaphors, or add informal filler.

What I want is shorter, more confident mathematical prose.

For example, a good specialist paper often gives a paragraph three distinct functions: state the obstacle, display the idea, and explain the consequence. It then lets the proof establish the details.

The existing manuscript sometimes has several extra sentences between those functions, describing exceptions and historical or implementation qualifications.

Those sentences are the first candidates for deletion.

8. What the ideal final version would feel like
Imagine a specialist finishes reading the paper and explains it to a colleague.

They should be able to say:

"The construction hides certificates at addresses specified by hard partial-function outputs. Classically, you can't find the planted cell without effectively predicting those outputs, and there are too many columns to investigate deeply. Quantumly, you don't search over complete certificate checks. You compare columns cheaply, using a weighted tournament that works even with inconsistent comparisons among losing columns, and then verify only a logarithmic-sized list. That's where the nearly quartic separation comes from."

That is a complete conceptual account of an intricate theorem.

An excellent paper makes it easy for its reader to produce that explanation, while also providing enough rigor to reconstruct every step.

The current paper contains everything necessary for that account, but it doesn't always maintain it as the organizing thread.

Its best passages do. The paragraph introducing §3, the calculation in equation (8), the two probability normalizations on page 7, Figure 2 and the planted-cell prediction argument are all evidence of that.

The job is to make the rest of the document exhibit the same level of focus.

9. My exact prescription for the next revision
If I were directing one more serious revision, I would impose the following priorities, in order:

1. Rewrite the abstract, contribution paragraph and theorem lead-in to emphasize the two mathematical ideas and the quantitative reason the quantum tournament matters. Demote the constants and formalization metadata.

2. Rebuild Section 2 around understanding the total function. Introduce the objects, the winner condition, the address and the local tests in the order that makes their purpose obvious. Relocate detailed circuit arithmetic.

3. Give §3.2 the strongest possible narrative progression: arbitrary comparisons are an apparent obstacle; weighted sampling creates a halving law; quantum amplification implements the required conditional distribution; the winner survives; final verification establishes correctness.

4. Rewrite §4.4 almost entirely at the prose level, while retaining its proof. Present the prediction insight first, explain why naïve conditioning is invalid, and introduce the capped simulator as the solution. Give equation (12) the prominence it deserves.

5. Edit the paper by subtraction. Remove avoidable references to alternate traces and proofs, relocate peripheral counterexamples, and decide whether the growing-
k
k appendix belongs in this particular companion.

6. End the main paper mathematically. After the exponent proof, give a concise conclusion explaining what the two reductions accomplish together. Keep a short, accurate formalization note, but don't allow it to be the principal conclusion.

I would then conduct a final technical review of the exact parameter statements, including Appendix E.

These six changes would do more for the reader than another round of generic improvements to clarity, examples and transitions.

My final thought after this rereading
I still put the current version around 8/10 as a specialist mathematical exposition, although some individual proof passages are better than that.

But I would now characterize the remaining distance differently.

Previously, I described it mostly as needing stronger explanation and navigation.

I think that understates the problem.

The paper needs a stronger sense of what its own best mathematics is.

It needs the confidence to let a beautiful argument occupy the reader's attention without continuously surrounding it with justifications, qualifications, auxiliary examples and pointers elsewhere.

The real test is not whether every detail is present. It's whether the reader encounters each detail at the moment it becomes necessary and understands why it is necessary.

This is what great mathematical writing does: it makes a hard proof feel as simple as it can be, without making it any less correct.

And I would be especially careful not to equate getting more glowing reviews with reaching 10/10. A genuinely excellent finished paper should survive an independent specialist's cold reading and mathematical scrutiny, not merely another evaluation by the same model.

My strongest recommendation is therefore a subtractive, structure-first revision: preserve the proof, preserve the genuinely illuminating examples, but cut anything that competes with the central mathematical argument without advancing it.

That, more than additional explanation, is the change I think could finally break the recurring 8/10 ceiling.

another pass through of rereading lets start to think about how to get it to 10/10 cuz repeated revies hover at 8 atp 

like lets have taste and think about what makes a truly well written paper 

liek jsut reifnroce what you've been saying but think about it further read the paper properly agian

like now sum up this whole thread and reread agian like you can specify the deliverables on making this a 10/10 no more 8/10 fucking rating

Worked for 4m 21s
The definitive editorial brief: Making the specialist companion exceptional
Paper: Reconstructing OpenAI’s Nearly Quartic Query Separation
Source: The attached 18-page PDF, reread alongside all our previous reviews.
Objective: Produce a specialist mathematical paper whose clarity, elegance, proof selection and intellectual value are exceptional—not merely a correct reconstruction with better wording.

1. The conclusion of this entire review thread
Across four readings, we've repeatedly arrived at the same underlying criticism from different directions.

The paper is mathematically substantial. It reconstructs two central mechanisms behind OpenAI's separation, provides explicit quantitative estimates, carefully states hypotheses, and contains several genuinely elegant arguments.

The most successful parts are:

The weighted tournament and expectation-halving argument in §3.2.

The distinction between preparation success probability and the exact conditional sampling distribution on page 7.

The dummy/planted input coupling in §4.2.

The conversion of a certificate-cell visit into a capped address-prediction attempt in §4.4.

The concise mathematical arguments behind the bounded amplifier and separate-cap product lemma in Appendices C–D.

These are the foundations of the final paper. Do not casually rewrite or simplify them away.

The recurring weaknesses are also now clear:

The paper sometimes explains machinery before explaining why the machinery is needed.

Details of unequal mathematical importance receive approximately equal attention.

The prose frequently anticipates objections and documents edge cases at the expense of the main mathematical argument.

The most interesting mathematical ideas occasionally appear halfway through the paragraphs that should be introducing them.

The paper is not sufficiently selective about what belongs in an 18-page specialist companion, as opposed to the separate complete reconstruction.

It has no particularly satisfying mathematical ending: the main argument gives way to formalization scope, references and technical appendices.

There is also at least one concrete correction outstanding in Appendix E: the claimed range 
t
≥
80
t≥80 for 
k
=
⌊
t
/
20
⌋
k=⌊ 
t
​
 /20⌋ does not ensure 
k
≥
2
k≥2. The displayed choice only reaches 
k
=
2
k=2 when 
t
≥
1600
t≥1600. 
expert_companion(5).pdf

The overarching problem is therefore not a shortage of mathematical content, explanation, or verification.

It is a shortage of editorial hierarchy.

The manuscript still partly reads like a meticulously compressed reconstruction, rather than a paper deliberately composed to communicate a beautiful mathematical argument.

2. The standard we're actually aiming for
A truly excellent specialist paper should accomplish five things simultaneously.

I. It gives the reader a reason to care. Not just the theorem's importance, but the specific conceptual obstacle the paper resolves.

II. It makes its key ideas memorable. A reader should remember the halving law and the cell-to-prediction reduction, rather than a sequence of technical lemmas.

III. It makes the proof feel natural. Definitions and technical devices arrive because the reader has just encountered the problem they solve.

IV. It is uncompromisingly rigorous. Every restriction that matters is present, but not every restriction needs equal rhetorical prominence.

V. It exercises restraint. The paper contains what makes the argument intelligible and convincing, not everything that was established during its development.

The central editorial principle should be:

The reader should never have to work harder to understand the organization of the proof than to understand the mathematics itself.

That is what the next revision needs to achieve.

3. What the latest rereading adds
The most important refinement is that some of the technical caveats we've been calling clutter are actually the most interesting mathematics in the paper.

We should not remove them indiscriminately.

The problem is how they are introduced.

The quantum proof has three things to establish:

The winning column dominates comparisons. The weighted tournament finds it without requiring transitivity. The quantum implementation preserves the precise sampling law and has a worst-case query cap.

Each point resolves a different potential failure. Each deserves attention.

Similarly, the classical proof has three central obstacles:

An algorithm might find the erased zero. It might discover the planted cell. And the attempt to bound the second event could fail if adaptive queries or conditioning destroy the intended hard-input distribution.

These should be presented as the proof's natural progression, rather than as a long sequence of technical precautions.

The guiding principle: one controlling quantity per argument
For the quantum tournament, the reader should constantly understand the role of total surviving weight

W
=
∑
i
w
i
.
W= 
i
∑
​
 w 
i
​
 .
The argument revolves around the fact that its expectation halves at every ideal step, whereas a genuine winner retains almost all its weight.

For the classical lower bound, the controlling quantity is the probability that an algorithm distinguishes the dummy and planted inputs:

Pr
⁡
[
find erased zero
]
+
Pr
⁡
[
visit planted cell
]
.
Pr[find erased zero]+Pr[visit planted cell].
The second event is difficult because it contains a hidden address. The truncated predictor and direct-product lemma exist to bound that event.

Every substantial proof paragraph should either introduce one of these ideas, establish it, or explain why it can be implemented legitimately.

This is the sort of criterion that allows genuinely confident editing.

It tells you what to cut without weakening the mathematics.

4. A page-by-page surgical assessment
Here is the precise intervention map after returning to the actual PDF.

Current location

What I would change

Page 1: Abstract and contribution

Emphasize the two reductions and their mathematical significance. The exponent six, 
1
/
400
1/400, formalization and counterexamples should not compete with the main insight.

Page 2: Figure 1 and theorem

Give the theorem slightly more prominence. Explain that the logical columns are drawn as horizontal strips.

Page 3: Historical comparison

Move the central quantum-cost contrast earlier; compress the longer literature discussion since Appendix B already develops it.

Page 4: Forrelation circuit

Relocate the word-width, gate-count and exact 
S
S calculation to an appendix. State the existence, purpose and required size of the circuit in the main text.

Page 5: Local tests

Make the distinction between cheap comparisons and expensive verification explicit immediately after defining the test family.

Page 6: Tournament

Introduce the ideal pivot-selection algorithm before the long formal proposition. Give the expectation-halving identity its deserved prominence.

Page 7: Exact sampler

Preserve the conditional-law calculation and the four-candidate table. Clarify the progression from the ideal sampling law to its bounded quantum implementation.

Page 8: Verification

Lead with the essential fact that a dominant candidate may have an invalid certificate. Then explain why verification finishes the algorithm.

Page 9: Planting

Present the planted construction and Figure 2 before the standalone direct-product machinery, or at least motivate that machinery using the planted-cell event first.

Page 10: Capped prediction

Substantially rewrite the proof's exposition. Begin with the cell-as-prediction insight, then introduce the fixed-time simulator. Remove the digression about the unrelated XOR trace.

Page 11: Lower-bound conclusion

Put the three error terms in direct correspondence with the three discovery mechanisms. Let the contradiction finish decisively, without optional calculation detours.

Page 12: Conclusion and Lean section

Finish with a mathematical synthesis. Retain a short, accurately scoped formalization note, but do not make it the emotional or intellectual endpoint.

Pages 13–15: Counterexamples and history

Select the examples that illuminate the central proof. Move secondary cautions to the long reconstruction.

Pages 16–17: Technical lemmas

Preserve the proofs of bounded amplification and the separate-cap product bound. They make the reconstruction mathematically substantial.

Page 18: Growing-
k
k refinement

Fix the parameter-domain issue. Decide deliberately whether this refinement warrants inclusion in the specialist companion or belongs in a separate note.

The common feature is that virtually every improvement changes the emphasis or placement of existing content.

There is little need to invent additional mathematics.

5. The ideal architecture of the finished paper
I would now build the paper in five movements.

I

The obstruction and the result

Explain why nested quantum search loses the critical 
m
m
​
  factor. State the reconstructed theorem and show the exponent calculation. Identify the two mechanisms that recover the improvement.

II

The construction

Introduce 
X
i
X 
i
​
 , the address inputs 
A
i
,
h
A 
i,h
​
 , the cells 
B
i
,
s
B 
i,s
​
 , and the winning condition. Explain how the partial-function supplier and exact circuit interact. Then establish totality and local testability.

III

Why quantum search is cheap

Establish dominance, derive the weighted tournament, implement its exact conditional sampling law, and verify the resulting short list. Finish with the query bound.

IV

Why classical search is expensive

Plant the winner, couple zero- and one-inputs, bound erased-zero discovery, and reduce planted-cell discovery to capped address prediction. Finish with the indistinguishability contradiction.

V

Why the exponent is four

Instantiate the hardness supplier, explain the fixed-
k
k quantifiers, conclude the theorem, and close with a concise synthesis of the two reductions.

This architecture largely matches what you already have. The difference is that each movement would be written around its mathematical purpose rather than its implementation history.

I would not introduce another enormous master theorem. Proposition 2 already abstracts the tournament; Proposition 4 already abstracts the classical reduction. Both are useful. A further abstraction might only add notation.

6. The actual deliverables for the revision
I would specify seven concrete deliverables. They can all be produced in a single editorial revision, but each should be reviewed separately.

Deliverable

Required output

Acceptance condition

D1. New opening

Revised title/subtitle if warranted, abstract, contribution statement, first two pages

A specialist understands the theorem, the nested-search obstacle, and the two reductions before meeting the technical construction

D2. Rebuilt construction

Reordered Section 2, with circuit arithmetic moved to supporting material

The reader can explain 
X
i
X 
i
​
 , 
A
i
,
h
A 
i,h
​
 , 
B
i
,
s
B 
i,s
​
 , the winning condition and local verification without backtracking

D3. Quantum proof revision

Edited §3 with a concise algorithm overview, weighted-pivot argument, exact-law sampler, and verification

The reader can identify precisely why arbitrary loser comparisons, small sampling probabilities and false certificates do not invalidate the algorithm

D4. Classical proof revision

Reordered §4, with planting first and a substantially clearer capped-predictor argument

The reader understands why a queried cell supplies a guessed address, and why the proof bounds an original-law joint event rather than conditioning on lightness

D5. Editorial reduction

Streamlined historical discussion, cross-references, counterexamples, and conclusion

Every remaining main-text paragraph serves the central proof, a necessary hypothesis, or essential mathematical context

D6. Mathematical audit

A short audit of theorem hypotheses, parameter ranges, query accounting and appendix dependencies

No identified issue remains unresolved, including the Appendix E threshold; the edited paper makes no stronger claims than its arguments establish

D7. Final reader-facing PDF

Fully revised and visually inspected specialist companion, with a short editorial change report

The document reads coherently on its own, its figures and notation are consistent, and the mathematical argument has not been lost or weakened during editing

The final PDF is the primary deliverable. The others are production requirements ensuring that it is genuinely improved rather than merely cosmetically different.

I would not impose an arbitrary page count. If the result is 16, 18 or 20 pages because the mathematics genuinely reads better, that's fine.

What D1 should look like
The opening needs to make the quantitative contrast unmistakable.

The previous constructions and the new construction should not just be distinguished by historical statements. The reader should immediately see the cost improvement:

na
ı
¨
ve nested quantum search
:
O
~
k
(
m
)
,
weighted tournament plus verification
:
O
~
k
(
m
)
.
na 
ı
¨
 ve nested quantum search
weighted tournament plus verification
​
  
: 
O
  
k
​
 (m),
: 
O
  
k
​
 ( 
m
​
 ).
​
 
Then explain that the classical hardness remains at scale

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
.
Ω
  
k
​
 (m 
2−1/k
 ).
This immediately accounts for the exponent 
4
−
2
/
k
4−2/k.

A key editorial instruction is that this should be explained with the actual construction's costs, not as a vague slogan about quantum speedups.

What D2 should preserve
The exact circuit isn't incidental. The partial Forrelation decoder is correct on promised inputs, while the total Boolean function must reject false certificates even when their address inputs violate the promise.

That distinction explains why there are two computational objects: the cheap quantum decoder and the exact Boolean circuit that supports local verification.

This relationship must remain in the main text.

What does not have to remain in the same place is the detailed arithmetic producing the circuit-size bound.

A specialist needs the bound. They don't need every gate-count calculation before understanding what the circuit is checking.

Likewise, a tiny worked comparison would be valuable:

Suppose 
i
⋆
i 
⋆
  wins and 
j
j is any rival. With the winning address decoded correctly,

X
j
[
p
i
⋆
,
s
i
⋆
,
j
]
=
0
,
X
i
⋆
[
p
j
,
s
,
j
⋆
]
=
1
,
X 
j
​
 [p 
i 
⋆
 ,s 
i 
⋆
 
​
 ,j
​
 ]=0,X 
i 
⋆
 
​
 [p 
j,s,j 
⋆
 
​
 ]=1,
where the second pointer denotes whatever valid row the rival's decoded cell specifies. The rival's address need not be correct for the second equality: 
X
i
⋆
X 
i 
⋆
 
​
  is all ones.

In the actual paper, use fully consistent pointer indices rather than the schematic 
j
⋆
j 
⋆
  above.

That is almost the entire dominance argument in one displayed observation.

It deserves to sit directly beside the definition, not only in the later proof.

What D3 must absolutely retain
The exact sampling law is essential:

Pr
⁡
[
success
]
=
W
m
,
Pr
⁡
[
i
∣
success
]
=
w
i
W
.
Pr[success]= 
m
W
​
 ,Pr[i∣success]= 
W
w 
i
​
 
​
 .
The algorithm cannot merely find a label that wins all comparisons with previous pivots. It must sample according to the appropriate weights.

This is one of the technically important differences between the argument and a more elementary tournament-search description.

The bounded amplifier also cannot be replaced casually by an expected-cost quantum search: the paper's claimed query cap holds on every input and branch.

These aren't defensive implementation details. They are genuine mathematical requirements that should become understandable as the proof encounters them.

What D4 must absolutely retain
The classical simulator needs the fixed query time 
τ
τ, the target budget 
L
L, and outside data jointly independent of the target address inputs.

The proof cannot simply say that the selected column is lightly queried and then invoke the direct-product bound after conditioning on that fact.

Equation (12) works because it bounds the joint event under the original law:

Pr
⁡
[
i
 light and query 
τ
 visits 
B
i
,
s
i
]
≤
β
r
.
Pr[i light and query τ visits B 
i,s 
i
​
 
​
 ]≤β 
r
 .
The simulator's truncated query cap establishes that bound before the union over times.

This is an important theorem-proofing distinction. In the revision it should be explained elegantly, not hidden away.

I would retain Appendix A.7 specifically because it shows what goes wrong with the invalid conditioning shortcut. 
expert_companion(5).pdf

7. What should be deleted, relocated, or kept?
The revision should apply a strict distinction.

Keep in the main text: the construction, quantum dominance, the halving identity, conditional sampling, verification, planted-input coupling, capped prediction, the contradiction, and the exponent calculation.

Relocate: detailed circuit gate-count derivations, unnecessary alternative examples, lengthy historical optimizations, optional numerical refinements, and extended discussions of how the printed proof differs from the Lean proof.

Delete if they add no mathematical value: repeated navigation to the longer record, remarks about alternative traces that are not used in this PDF, repeated statements of already established hypotheses, and procedural descriptions that interrupt proof arguments.

One particularly useful change would be reducing the references to the reasoning record inside the main proof.

References are essential when an argument invokes an external mathematical result or deliberately delegates a proof. But a cross-reference should not repeatedly interrupt an otherwise self-contained argument merely to advertise that a related calculation exists elsewhere.

The long reconstruction is a supporting resource. It shouldn't dictate the specialist paper's rhythm.

8. The mathematical conclusion needs to be written, not just reached
The existing paper reaches the fixed-
k
k exponent result correctly in the intended proof structure.

But a reader should finish the main text with a stronger sense of what has been learned.

I would add a short mathematical conclusion, perhaps two paragraphs.

Its central message should be:

The construction separates cheap comparison from expensive verification. Quantumly, a dominant column can be located among a logarithmic-sized set even when comparisons between invalid columns have arbitrary probability laws. Classically, the certificate address remains inaccessible because attempting to visit the right cell with too few address queries amounts to solving many independent hard instances.

Both mechanisms matter. Neither alone explains the nearly quartic exponent.

Then, in one or two sentences, explain the general significance and the relationship to the formal reconstruction.

This is much better than ending the main narrative with proof-route documentation.

9. The acceptance tests: how we know the revision is finished
The next version should be evaluated through concrete reader tasks rather than by repeatedly asking for a numerical impression.

Cold-reader acceptance checklist
Revision quality gates

0 of 9 satisfied


The first two pages communicate why the theorem is interesting and why the naïve quantum algorithm loses a factor.

The reader understands the construction and winning condition before encountering detailed circuit accounting.

The weighted tournament's halving identity feels natural, and the reader knows why no order among losers is required.

The exact conditional sampling law and all-branch quantum query cap are explained and justified.

The planted-cell proof clearly identifies the address-prediction reduction and the invalid conditioning shortcut.

The paper's main mathematical argument remains understandable without consulting the 94-page reconstruction.

Every retained appendix contributes directly to completeness, understanding or a deliberately included mathematical refinement.

Every theorem statement, parameter range, numerical constant and cross-reference has been checked after revision.

The final PDF reads cleanly, uses consistent notation, and ends with a meaningful mathematical conclusion.
I'd also want a genuine cold read from at least one query-complexity specialist who has not seen the revision history.

The key questions are whether they can follow the proof on first encounter, identify any unstated assumptions, and describe the main ideas afterward without being coached.

A review from the same model after many rounds is not an independent measure of that.

10. Final editorial direction
If this were being handed to a writing or research agent, my instruction would be:

Perform a decisive mathematical editorial revision of the attached specialist companion. The aim is not to add more detail, produce more examples, or shorten the document indiscriminately. It is to make the existing mathematics maximally clear, inevitable and memorable to a specialist reader.

Rebuild the presentation around two central reductions: the weighted quantum tournament and the classical conversion of planted-cell discovery into capped address prediction.

Put conceptual obstacles before the machinery that resolves them. Give the expectation-halving identity, exact sampling law, and prediction bound the prominence they deserve. Relocate secondary circuit arithmetic, procedural notes, cross-references and peripheral counterexamples. Preserve the mathematical substance, particularly the worst-case query caps, joint independence assumptions and the direct-product reasoning.

Produce a coherent final PDF, a short description of the substantive editorial changes, and a mathematical audit listing any outstanding claims or parameter issues. Do not claim that the proof has been independently certified if it has not.

Judge success by the specialist reader's comprehension of the finished paper, not by its similarity to previous drafts or an artificial numerical score.

The final synthesis
I think this is the most important thing to carry forward from the entire thread:

The paper's next level is not achieved by making every paragraph clearer. It is achieved by making every paragraph worth reading.

The paper should not be a tour through all the engineering necessary to reconstruct a sophisticated proof. It should be an exceptionally well-chosen mathematical path through that proof.

There is a beautiful argument here:

A dominant candidate can be found without an ordering. A hidden certificate cannot be found without predicting hard answers. Those facts change the quantum and classical costs in precisely the way needed to approach exponent four.

The excellent paper is the one in which those facts emerge naturally, their proofs feel motivated, the indispensable technical subtleties are handled exactly, and everything extraneous gets out of the way.

That is the revision to make. No more generic polishing cycles. One complete structural and mathematical editorial pass, followed by a cold-reader test.





