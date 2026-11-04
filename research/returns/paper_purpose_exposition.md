

exposition(4).pdf
PDF
Okay, so read attached. Obviously this comes with a repo and a website, whatever. This is just the PDF. We don't have to worry about, like, oh, the source and the hashes and that bullshit. It's just purely the reading experience for a mathematical reader, for the target audience for this. For that, can you please give feedback on, you know, the paper? Like, how is the paper? Can you just give it a review? Let us know, like, how good is it? Just how good is it? And please, yeah, give us feedback.


Revised all three with clearer explanations, stronger examples and cleaner navigation. Hashes, code paths and verification history now sit behind the readable theorem index.


Specialist companion — 18 pages


Exposition — 27 pages


Complete reconstruction — 94 pages, down from 141, with the mathematical proofs retained.


Rendered pages and links checked; 267 tests completed with two skips and no failures. Changes pushed, and the writing-method improvements merged upstream.

…
Review: Why OpenAI’s query separation is nearly quartic
Review of the attached 27-page exposition · November 2026

Overall assessment
8/10
Overall quality as a mathematical exposition

Strong, serious, intellectually coherent, with some remaining pedagogical weaknesses.

I've read the exposition itself, including its worked examples, diagrams, quantum algorithm, classical lower bound, exercises and appendices. I'm assessing the mathematical reading experience rather than the accompanying code, website or verification machinery.

This is a genuinely good mathematical exposition. It has a clear intellectual purpose, an unusually concrete collection of examples, and a carefully constructed path from small calculations to an important asymptotic result.

It is not merely paraphrasing a theorem or dressing mathematical claims in explanatory prose. It attempts to teach the reader how the separation works, why particular mechanisms are necessary, and how the estimates fit together.

Its biggest achievement is that it makes the nearly quartic separation feel like the consequence of two identifiable mechanisms:

Quantum: cheap pairwise comparisons identify a small collection of candidates, allowing expensive certificate verification to happen only at the end.

Classical: the planted winner and its certificate address remain inaccessible to a shallow decision tree, even when that tree adaptively guesses certificate locations.

That is exactly the understanding a good exposition should produce.

However, there is still a distinction between making an argument fully reconstructible and making its central insight easy to understand. Your paper is stronger at the former than the latter.

For the intended mathematically sophisticated reader, particularly one interested in theoretical computer science, this is a substantial achievement. For a mathematician encountering quantum query complexity for the first time, it remains quite demanding.

My central criticism is that the exposition sometimes becomes a compressed mathematical proof just when the reader most needs an intuitive explanation of what the proof is accomplishing.

That is where I would concentrate the next revision.

1. The strongest parts of the paper
The examples actually do mathematical work
This is probably the paper's greatest strength.

A common failure in mathematical exposition is to introduce a toy example, explain it, and then abandon it when the real proof begins. Here, the four-column construction returns throughout the argument.

The three eight-bit inputs on pages 2–3 establish a positive case, a zero case, and an off-promise case. Pages 4–7 then give these objects a concrete role as certificate addresses.

Figure 2 on page 5 is particularly effective. It shows an actual winning column, where its pointers go, which cells are selected, and why another column cannot also win.

The later mutations are even better.

The domain-bit example on page 6 demonstrates why validating a proposed value is insufficient without validating the promise. The false-pointer example on pages 9–10 shows why winning every comparison is not the same as possessing a valid certificate. The cycle on page 10 shows why the tournament cannot simply be sorted.

These are not arbitrary examples. Each defeats a plausible but incorrect simplification of the proof.

That makes the exposition much more convincing than one that merely presents a successful construction.

I would preserve essentially all of these examples. They are among the most valuable things in the paper.

The classical lower bound is particularly well explained
Pages 16–19 are arguably the best sustained piece of exposition.

The planted-pair construction is difficult to explain because the classical algorithm is adaptive. It might query address inputs, discover zeros, guess a cell, visit many cells, or interleave all these operations.

You give the reader a tangible pair of inputs in Figure 4, and then a table splitting the lower bound into three charges.

That is excellent mathematical organization.

The central observation on page 18 is especially good: querying a particular certificate cell already specifies a guess for the entire address, even when the algorithm has not explicitly calculated it.

That bridges the intuitive idea of a hidden certificate to the formal direct-product argument. 
exposition(4).pdf

The simulator that stops before exceeding its query cap is also explained with unusual care. The later XOR example on pages 20–21 demonstrates why a cap on the entire run is different from a cap at the instant the cell is visited.

I think a reasonably strong theoretical computer scientist could follow this argument without having previously seen this exact reduction.

That is a meaningful achievement.

The quantum argument has a good mathematical core
The best idea in Section 4 is the use of fractional comparison weights.

You explain that two losing columns need not have an underlying fixed ordering. Their comparisons can be probabilistic, and even cyclic. Nevertheless, the expected total surviving weight halves.

The identity on page 11,

E
[
∣
w
′
∣
∣
w
]
=
∣
w
∣
2
−
∑
i
w
i
2
2
∣
w
∣
≤
∣
w
∣
2
,
E[∣w 
′
 ∣∣w]= 
2∣w∣
∣w∣ 
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
∣w∣
​
 ,
is particularly satisfying.

It turns a seemingly messy stochastic comparison procedure into a clean potential argument, without assuming transitivity.

The subsequent sampling construction then makes that abstract potential argument algorithmic.

This is good exposition because the mathematics is not merely written down; the reader can see why this particular mathematical quantity was introduced.

The ending is mathematically mature
Section 6, pages 21–22, handles the order of quantifiers carefully.

The distinction between fixing 
k
k and then growing 
m
m, versus permitting 
k
k to grow with 
m
m, is essential. Likewise, the paper correctly distinguishes approaching a fourth-power separation from exhibiting one exact fourth-power lower bound.

I also appreciate the exercise showing why 
k
=
4
k=4 does not itself refute the endpoint exponent 
3.5
3.5, whereas 
k
=
5
k=5 does.

This is precisely the sort of detail that distinguishes a serious mathematical exposition from a superficial description of asymptotics.

2. Where the paper is still weaker
The opening is less examples-first than it claims
This is my first structural criticism.

The introduction promises to explain the construction starting from a four-column board. But the reader does not encounter the actual four-column board until page 5.

Instead, the sequence is an explanation of query complexity, a formal discussion of the optimal exponent, an eight-bit Forrelation example, the Walsh transform, and a quantum projection experiment.

All of this is relevant. But the order creates a slightly different learning experience from the one promised by the subtitle.

The manuscript begins with the mathematical machinery needed to understand the example, rather than first establishing the object whose behavior motivates the machinery.

Even within Section 2, Figure 1 presents the general schematic before Figure 2 presents the concrete four-column instance.

For a genuinely examples-first exposition, I would consider reversing that order.

Show the reader the literal board, tell them what victory means, and demonstrate the certificate. Then explain why the address cannot simply be read.

That immediately gives the Walsh example a purpose.

There is also a small ordering problem on page 1: 
α
t
o
t
α 
tot
​
  is introduced in terms of 
R
(
f
)
R(f) and 
Q
(
f
)
Q(f) before those two quantities have been formally explained. The subsequent paragraphs do define them clearly. They should simply come first.

None of this is fundamentally wrong, but it affects the first impression.

Section 4.3 is the largest remaining pedagogical obstacle
Pages 12–14 contain the most demanding transition in the paper.

The reader must understand that an ideal random process chooses columns according to weights, that the weights are products of comparison probabilities, that these products can be realized as successful quantum probability masses, and that amplitude amplification preserves their conditional label distribution.

This is technically impressive.

It is also a great deal to absorb in a few pages.

The paper explains the individual steps correctly at the level of its stated argument. What is missing is a sufficiently prominent statement of the whole mechanism before its implementation details.

I would want the reader to know the following before encountering the reversible registers and amplification rotations:

To sample a new column, try every column coherently and mark it successful when it beats all previous pivots. Column 
i
i is marked with probability 
w
i
w 
i
​
 . Amplification increases the probability of obtaining a successful trial without changing the relative probabilities of the successful columns. Measuring therefore samples exactly from the desired distribution.

That is the conceptual breakthrough.

Your text establishes it, particularly on pages 12–13. But the explanation is distributed among several technical paragraphs, and the reader has to assemble it into one picture.

The fractional matrix on page 13 is a good numerical example. I would retain it while adding a visual representation of the entire sampler.

Suggested conceptual diagram for Section 4.3

Uniform superposition over columns

1
m
∑
i
∣
i
⟩
m
​
 
1
​
 ∑ 
i
​
 ∣i⟩
Compare each column against every previous pivot
Mark successful comparison histories

Pr
⁡
(
success and 
i
)
=
w
i
/
m
Pr(success and i)=w 
i
​
 /m
Amplitude amplification preserves relative success weights
Measure a successful column

Pr
⁡
(
i
∣
success
)
=
w
i
∑
j
w
j
Pr(i∣success)= 
∑ 
j
​
 w 
j
​
 
w 
i
​
 
​
 
A diagram like this would make the next two pages of linear algebra feel like the justification of an idea the reader already understands.

At present, those pages ask the reader to discover that idea while following the implementation.

That is the single biggest opportunity for improving the paper.

The advertised prerequisites are slightly optimistic
The introduction says the paper assumes finite-dimensional linear algebra, elementary conditional probability, and asymptotic notation.

That's a reasonable mathematical background, but the exposition also requires a reader to learn quite a lot about reversible quantum computation, measurement, randomized query trees, finite minimax, amplification, and adaptivity.

You do explain these concepts. The issue is the rate at which the reader must assimilate them.

For instance, page 3 carefully introduces quantum basis states, phase kickback, and projection probabilities. The reader then has to connect those primitives to the much more sophisticated coherent sampler on pages 12–14.

Similarly, Section 5 requires the reader to move from an elementary planted example to a direct-product lemma with adaptive interleaving and jointly independent side information.

There is a notable change in difficulty between the introductory examples and the central arguments.

I would therefore describe the audience more precisely as:

A mathematically mature reader, comfortable with probability proofs and algorithms, who is willing to learn the quantum-query formalism.

That is a perfectly respectable audience. It is just somewhat narrower than the stated prerequisites suggest.

The paper sometimes optimizes for completeness rather than understanding
There is a recurring tension between the exposition and the complete reconstruction.

In Section 3, the reader encounters exact circuit sizes, logarithmic parameters, Chernoff constants, partial-function hardness, polynomial total input length, and the headline complexity theorem in rapid succession.

These details matter mathematically. But the reader's immediate task is to understand why the construction needs three properties of the partial function: cheap quantum decoding, exact local certification, and hard classical evaluation.

That structural picture could receive greater emphasis than the constants.

Similarly, Section 4.3 gives a detailed explanation of amplitude amplification, while Appendix A.3 gives an explicit randomized amplification schedule.

I think the appendix placement is correct. But the main text could more sharply separate the conceptual fact needed for the theorem from the machinery establishing the particular fixed cap.

I would not make the paper much shorter overall. Twenty-seven pages is a reasonable length for this level of mathematics. I would instead redistribute some explanation so that the difficult ideas receive more attention than their supporting bookkeeping.

3. Section-by-section judgment
Section

My assessment

Introduction, p. 1–2

Clear and serious, but too much abstract setup before the first concrete board

1. Eight-bit inputs, p. 2–4

Strong worked calculation; the off-promise example is particularly instructive

2. Certificates, p. 4–7

Excellent. Probably the most immediately teachable section

3. General partial function, p. 7–9

Mathematically organized, but dense with parameters and imported facts

4. Quantum tournament, p. 9–15

Contains the central conceptual achievement, but Section 4.3 needs more pedagogical space

5. Classical lower bound, p. 16–21

Very strong, especially the planted-pair diagram, three-charge table and capped simulator

6. Optimal exponent, p. 21–22

Excellent handling of quantifiers and endpoint exponents

Exercises and appendices

Valuable, substantive, and generally well chosen

One additional pacing issue: Section 5's main lower-bound proof finishes on page 19, but the reader then spends two pages on counterexamples and technical tests before arriving at the exponent conclusion.

Those examples are good. I would simply mark them more visibly as optional consolidation, allowing someone following the main argument to proceed directly to Section 6.

4. The changes I would prioritize
First priority: expose the structure earlier.

Give the reader the concrete board earlier, preferably on the opening pages. Distinguish the cheap address decoder, the expensive certificate verifier, and the role of pointers before presenting all their formulas.

Second priority: make Section 4.3 visually intelligible.

Add one diagram and one concise conceptual summary that explicitly connects successful comparison histories, their probability weights, amplification, and the measured pivot law.

Third priority: clarify the simulator before its construction.

The explanation of the three budgets appears on page 19, after the simulator is introduced on page 18. Move that explanation earlier. Establish what must be bounded and which budget each algorithm is allowed before giving the four-step simulation.

Fourth priority: add short section-level conclusions.

After the quantum tournament, state in plain language exactly what the algorithm achieved and why it avoided nested verification. After the planted-pair argument, restate what the classical algorithm cannot discover and why that costs 
m
L
mL.

These would be refinements, not a wholesale rewrite. I would not disturb the core examples, mathematical statements, or general proof structure.

5. How good is it for a real mathematical reader?
I think the answer depends on the reader's background.

A theoretical computer scientist already familiar with randomized algorithms, query complexity, and elementary quantum algorithms would likely find this a useful, well-organized companion to the original construction. The paper supplies motivations, concrete counterexamples, and enough detail to follow the major mechanisms rather than merely trust a proof sketch.

A mathematician with strong linear algebra and probability but little theoretical computer science would find it more demanding. They could follow the first several pages and the planted-pair argument, but the transition to coherent quantum pivot sampling might require substantial rereading.

For a researcher already expert in quantum query complexity, the paper is not aiming to present a new theorem. Its value lies in making a difficult construction easier to teach, check conceptually, and explain to others. It succeeds at that, although an expert would still need to examine the formal arguments separately to certify mathematical correctness. This review is not such a certification.

Final verdict
My overall judgment remains 8/10 for the intended mathematical exposition.

The paper's strongest feature is the integration of concrete examples with genuinely nontrivial reasoning. Its weakest feature is that its most difficult mathematical mechanism, the quantum weighted sampler, is explained in enough detail to reconstruct but not quite enough intuitive structure to understand effortlessly on first encounter.

I would regard this as a serious, credible expository manuscript that is worth showing to mathematically sophisticated readers. It does not read like generic AI-generated mathematical prose: the examples have precise purposes, the difficult cases are acknowledged, and the arguments maintain a coherent logical direction.

The next improvement is not another general polishing pass. It is a targeted pedagogical revision of the opening and Section 4.3, with a smaller restructuring of the capped-simulator explanation.

The mathematical content is already substantial. The remaining opportunity is to make the reader see the central ideas sooner, with less work.

another pass through of rereading lets start to think about how to get it to 10/10 cuz repeated revies hover at 8 atp
Second reading: how to get the exposition from 8/10 to 10/10
I've reread the 27-page PDF, including the displayed mathematics and figures, with a stricter standard this time.

My assessment has sharpened: the remaining problem is not primarily the quality of the prose. It is the architecture of the reader's understanding.

You have already addressed many of the ordinary weaknesses of technical exposition. There are concrete examples, explicit query budgets, carefully identified assumptions, worked counterexamples, and explanations of why tempting alternative arguments fail.

But a paper can contain all those ingredients and still require too much intellectual reconstruction from its reader.

That's where this one is now.

1. Why I think repeated reviews keep landing around 8/10
I see three distinct qualities:

Dimension

Assessment

Mathematical substance and precision

9/10

Quality and relevance of worked examples

9/10

Organization of the reader's conceptual understanding

7/10

These are editorial judgments, not measurements or a certification of correctness.

The paper's most difficult ideas are explained, but their importance is sometimes established after the reader has already had to understand the machinery implementing them.

The clearest example is Section 4.3, pages 12–14.

The single most important insight there is that one can sample from a complicated distribution without knowing or computing its probabilities. The comparison experiment implicitly creates exactly the required probability weights, and amplitude amplification increases the success probability without distorting their relative proportions.

That's a beautiful idea.

But the exposition introduces reversible circuits, fresh registers, tensor products, successful workspace components, amplification rotations, and conditional measurement laws before that insight has received anything like the emphasis it deserves.

A competent mathematician can reconstruct it. An excellent expositor makes the mathematician see it.

The difference is substantial.

The same problem appears, to a lesser extent, elsewhere. On pages 2–3 the reader learns the Walsh projection experiment before seeing the certificate board that motivates it. On page 18 the reader encounters the capped simulator before page 19 explicitly distinguishes the three query budgets that explain its design.

These are not missing proofs. They are explanatory dependencies appearing in the wrong order.

That is why another round of sentence polishing might produce a somewhat cleaner 8/10 rather than a genuinely better paper.

2. The deeper issue: this is really two papers interleaved
The manuscript is trying to perform two jobs:

Job A: Develop the conceptual explanation. Why does an apparently expensive certificate problem admit an efficient quantum algorithm, and why can't a randomized algorithm defeat the construction by searching or guessing intelligently?

Job B: Reconstruct the technical argument. What are the precise quantum operations, conditional probability laws, simulation rules, error bounds, query caps, and asymptotic quantifiers?

Both jobs are legitimate. A truly excellent exposition can accomplish both.

The difficulty is that the manuscript doesn't always give them different levels of prominence.

For example, the two-dimensional amplification calculation on page 13 is mathematically useful. But a reader trying to understand the theorem's central mechanism shouldn't have to work through the reflection matrices before forming a clear picture of what amplification is being used to accomplish.

Similarly, the classical simulator on page 18 is an important rigorous argument. But the reader should first be given the conceptual strategy: turn any attempted visit to the hidden cell into an algorithm that predicts its address, and stop that algorithm before its permitted query budget is exceeded.

Only then should the four-step simulator be introduced.

The route to 10/10 is not removing rigor. It's separating conceptual discovery from technical justification.

I would make each major argument follow a consistent sequence:

Problem

What obstacle are we solving?
Idea

What makes the obstacle avoidable?
Example

What does it actually do?
Proof

Why does it always work?
The manuscript already contains nearly all four elements. The main task is to put them in that order.

3. The precise places I would change
A. Pages 1–5: make the board the first real object
The subtitle promises an examples-first explanation, but the reader must first work through the eight-bit Forrelation calculation and quantum projection experiment before encountering the actual board.

I would seriously consider introducing a simplified version of Figure 2 immediately after the initial definitions of query complexity.

Show the four columns, the all-one candidate, and the pointers to zeros. The reader should understand what a winning certificate looks like before learning how its hidden address is calculated.

Then pose the question:

How can the address of a certificate be easy to calculate quantumly but hard to discover classically?

Now Section 1 becomes the answer to a question the reader actually wants answered.

There is an important additional distinction that deserves more emphasis. Your four-column example has 
r
=
2
r=2, while the actual asymptotic construction uses 
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
 m. The small board is a pedagogical instance of the definitions, not literally the hard family specialized to 
m
=
4
m=4. You explain this, including in Appendix A.4, but I would state it prominently alongside the first diagram. 
exposition(4).pdf
 
exposition(4).pdf

This matters because there are actually three levels in the paper: the eight-bit example, the four-column board, and the asymptotically hard construction.

A perfect exposition would make the transitions between those levels unmistakable.

B. Pages 7–9: separate the three ingredients of Forrelation
Section 3 is efficient but extremely information-dense. It moves through the quantum decoder, an exact circuit, classical hardness, total input length, and the final theorem in roughly two pages.

I would introduce the section with this table:

Ingredient

What it gives us

Why we need it

Quantum decoder

O
k
(
1
)
O 
k
​
 (1) queries at constant error

Discover certificate addresses cheaply

Exact Boolean circuit

Near-linear number of local equations

Verify a proposed certificate through quantum search

Classical hardness

L
≈
m
1
−
1
/
k
L≈m 
1−1/k
 

Make hidden certificate addresses expensive to predict

Here 
O
k
(
1
)
O 
k
​
 (1) means a potentially enormous constant depending on fixed 
k
k, not a practical constant-query procedure for arbitrary parameters.

The paper already establishes these three ingredients. The table would simply tell readers why each one belongs in the proof before immersing them in its quantitative form.

I'd also distinguish more clearly between results demonstrated in the exposition and results imported from the literature. That isn't about source files or verification records. It's about helping a mathematical reader know where the argument's difficult external theorem enters.

C. Pages 9–15: give the quantum algorithm one unified mental model
This is the highest-impact revision.

On page 9 you explain why searching directly over columns would multiply the cost of locating a candidate by the cost of verifying it. Your tournament avoids that multiplication. 
exposition(4).pdf

I would make that comparison visually explicit:

Direct search

Tournament

Search operation

Expensive certificate verification

Cheap pairwise comparison

What happens repeatedly?

Full checks

Comparisons

When do full checks occur?

Throughout search

Only after the shortlist is formed

Query scale, ignoring logarithms

m
K
∼
m
m
​
  
K
​
 ∼m

m
+
K
∼
m
m
​
 + 
K
​
 ∼ 
m
​
 

Here 
K
K is the number of local certificate tests, of order 
m
m up to logarithmic factors for fixed 
k
k.

This table explains much of the construction before any probabilistic tournament analysis.

Then Section 4.2 should establish the potential-function picture, which it already does effectively.

But immediately before Section 4.3 I would insert a paragraph resembling this:

The key sampling idea. After several pivots have been chosen, assign each column the probability that fresh comparisons declare it superior to every previous pivot. These are the weights we want to sample from. We never calculate them. Instead, we prepare all candidate columns in superposition and coherently run their comparison experiments. The probability of obtaining a successful flag together with column 
i
i is proportional to its weight. Amplitude amplification increases the chance of obtaining a successful flag while preserving the relative distribution of successful column labels. Thus the quantum experiment samples from the desired weights without ever estimating them.

Then derive the formula, retain the complete workspaces, explain the inverse, and prove that amplification preserves the conditional law.

The existing linear algebra now justifies an idea the reader has already grasped. 
exposition(4).pdf

I would preserve the fractional comparison matrix on page 13. It is a particularly good example because it demonstrates that the sampler isn't merely choosing uniformly among survivors.

The proof should emphasize the two distinct miracles:

The probabilities of independent fresh comparisons multiply to produce the required weights.

Amplification changes the overall probability of success without changing the normalized distribution within the successful component.

Those are the two statements I want the reader to remember a month after reading the paper.

D. Pages 16–19: move the three budgets before the simulator
The classical argument is already excellent, but one change would make it significantly better.

On page 18 you give the capped simulator. Only on page 19 do you explicitly distinguish the global budget 
G
G, the simulator's budget 
L
L, and the separate-instance caps required by the direct-product lemma. 
exposition(4).pdf

Reverse that.

Before introducing the simulator, tell the reader exactly what the simulator must achieve:

Suppose the original algorithm visits the true certificate cell while the chosen column remains light. We want to convert this event into a prediction of all 
r
r address answers. Our predictor must be correct whenever that event occurs, but it must also obey its query cap on every other possible run. In particular, it must stop before taking a query that would exceed the cap.

Then explain the three budgets, followed by the simulator construction.

The simulator becomes an almost inevitable design rather than a clever technical trick introduced without enough warning.

I would also emphasize that the resulting probability bound concerns the joint event of being light and visiting the true cell. It is not a bound on success conditioned on being light.

You explain that correctly, and the example on page 20 is good. The key is to make it part of the reader's initial understanding rather than a subtlety they appreciate afterward.

E. Pages 19–22: protect the conclusion
There is a substantial interruption between completing the classical proof on page 19 and establishing the optimal exponent on pages 21–22.

The examples about independent planting, lightness, the two clocks, and separate caps are valuable. But for the main reading path, I'd move most of them to an appendix or a clearly marked optional section.

A reader who has just completed the planted-pair argument should be able to move immediately to:

R
(
F
k
,
m
)
≳
m
2
−
1
/
k
,
Q
(
F
k
,
m
)
≲
m
R(F 
k,m
​
 )≳m 
2−1/k
 ,Q(F 
k,m
​
 )≲ 
m
​
 
with logarithmic factors suppressed, and therefore to the exponent 
4
−
2
/
k
4−2/k.

I'd also show a little exponent ladder earlier in the manuscript:

k
k

Leading separation exponent

2

3

3

10
/
3
10/3

4

7
/
2
7/2

10

19
/
5
19/5

k
→
∞
k→∞

4

This gives the reader a concrete sense of the limiting mechanism long before the formal quantifier argument.

The quantifier discussion itself is excellent and should remain.

4. Smaller things a final editorial pass should catch
A few details stood out on this rereading that are less philosophical but still matter.

The main theorem is split across pages 8–9. Its statement starts near the bottom of page 8, and the actual complexity inequalities appear at the top of page 9. That should be a single uninterrupted displayed theorem. 
exposition(4).pdf

Section 4.4 has an awkward page break. The explanation of what a successful violation search means ends page 14 with “so it rejects the” and resumes page 15 with “candidate.” This is an easy typesetting fix, but especially distracting in a technical explanation.

The opening defines the optimal exponent before defining 
R
R and 
Q
Q. Introduce the basic complexity measures first, then the exponent. It would be a more natural progression.

The literature discussion on page 6 interrupts the certificate construction. The history of pointer functions is relevant, but placing several literature comparisons between the general board layout and the explanation of its local tests slows the mathematical story. Consider moving the historical discussion after the mechanism has been established.

The original source's reference is incomplete. The bibliography ends its entry for the OpenAI paper with “Online source,” whereas other papers receive concrete identifiers or URLs. A standalone mathematical reader should be able to find the original theorem directly from the bibliography. That's an academic reading issue, not a repository issue.

The final formal-proof navigation interrupts the mathematical ending. Section 6 concludes with a strong explanation of the two access costs. Section 7 then switches to Lean correspondence. For this PDF's purpose, I would put that material in a short endnote or appendix and let the mathematical conclusion carry more weight.

5. What I would deliberately preserve
I would be very reluctant to remove the negative-Forrelation example, the domain-bit board, the dominating nonwinner, the directed cycle among losing columns, the fractional sampling matrix, or the adaptive capped-simulator example.

Each one addresses a real mathematical misunderstanding.

This is one area where the paper is already approaching excellent exposition.

The goal should not be a shorter paper with fewer examples. It should be a paper where the examples arrive at the exact moment a reader needs them.

The four-column board is especially valuable as a recurring object, provided the notation and its relation to the asymptotic family remain clear.

6. What I would actually do next
Here is the revision order I would follow.

Proposed editorial priorities

Impact on reading

Rebuild the first 5 pages around the board

Restructure weighted sampling in §4.3

Move simulator motivation and budgets earlier

Make proof-dependency and cost maps explicit

Restore a continuous conclusion after §5

Fix typography, terms and citations

Relative editorial impact, not measured quality scores.
I would keep the existing mathematical claims and proof coverage as the baseline. This revision should be a reorganization and explanatory expansion where needed, not an excuse to weaken the arguments.

Once those changes are made, I would test the paper with three kinds of mathematical reader: a quantum-query specialist, a theoretical computer science graduate student, and a mathematically mature non-specialist.

The test isn't whether they say the paper is clear. It's whether, after a first reading, they can independently explain why a true winner survives comparisons, why the total comparison weight decreases without an underlying order, why coherent sampling realizes the desired conditional distribution, why a true-cell query amounts to predicting hard answers, and why the resulting exponents approach four.

The strongest evidence that the exposition has reached its goal would be readers who can reconstruct the argument's logic without repeatedly consulting the technical derivations.

My updated conclusion
On this rereading, I am more convinced that the mathematics and the examples are already strong enough to support an exceptional exposition.

What is missing is an equally strong narrative of mathematical discovery.

The manuscript often explains how to prove something before giving the reader a sufficiently simple explanation of why that is the thing to prove.

That's a higher-level editorial problem than awkward wording, excessive notation, or insufficient examples.

I would aim for a manuscript in which a reader encounters the same rigorous mathematics but experiences the argument as a succession of natural insights:

A hidden certificate seems expensive to find. Comparisons avoid verifying everyone. A tournament handles even inconsistent comparisons. Coherent sampling implements the tournament without knowing its weights. Classical algorithms cannot find or guess the planted certificate cheaply. These two facts yield the fourth-power exponent.

The paper already proves that story. The 10/10 version would make the story almost impossible to miss.

And I would treat that as the central revision objective rather than chasing another half-point through local polishing.

another pass through of rereading lets start to think about how to get it to 10/10 cuz repeated revies hover at 8 atp 

like lets have taste and think about what makes a truly well written paper 

liek jsut reifnroce what you've been saying but think about it further read the paper properly agian
Third reading: what would actually make this a 10/10 mathematical exposition?
I've reread the attached 27-page exposition, including the equations, examples, page layouts, and the progression from the eight-bit Forrelation example through the tournament, planted-pair argument, and final exponent calculation.

I want to revise one part of my earlier advice.

I no longer think that simply adding more intuition, more examples, or more diagrams is the answer. There is already a lot of explanation here. In places, perhaps too much.

The problem is that the paper does not yet distinguish sharply enough between what the reader must understand, what they must believe because it has been proved, and what they might want to investigate afterward.

A truly exceptional mathematical exposition makes those distinctions almost effortlessly.

My assessment remains roughly 8/10, but I think we can now identify a much more specific route toward 9.5–10 than another general rewriting pass.

1. The missing quality is mathematical taste
The best mathematical writing has a quality that is difficult to quantify: the argument feels inevitable.

A new object appears exactly when it is needed. A calculation resolves a question that has already formed in the reader's mind. A lemma captures one surprising fact. An example makes that fact concrete. The next question then arises naturally.

At the end, the reader feels that the result could scarcely have been explained more economically.

Your paper has most of the necessary mathematics. But the reader is still sometimes working to discover the hierarchy of the ideas.

Consider how many distinct things appear in the exposition:

The Walsh experiment and the distinction between signed amplitude and projection probability.

Address bits, pointer bits, domain bits, value bits, gate transcripts, and local tests.

Dominating nonwinners, cycles among losers, fractional comparison probabilities, and surviving weights.

Coherent registers, amplification, conditional sampling, random iteration counts, and fixed query caps.

Independent planting, erased zeros, heavy columns, light columns, direct products, and capped simulators.

Five questions, their answers, a combined-explanation exercise, and a guided rubric.

Almost every one has a legitimate reason to be there.

But legitimate inclusion is not the same as good composition.

An exposition is not improved automatically by including every useful observation. It improves when the author chooses which observations deserve the reader's attention now.

That choice—what to explain, what to postpone, and what to omit from the main argument—is where I think the paper still falls short of exceptional writing.

A 10/10 revision would probably contain slightly less material in its main narrative, explain the most original ideas more generously, and preserve the technical details in clearly secondary locations.

2. The paper's best idea is still not sufficiently dominant
Here is what I think the central intellectual achievement of this construction is:

It separates finding a plausible winner from proving that a winner exists.

Ordinarily, that separation seems dangerous. A plausible winner might not be genuine; comparisons between bad candidates might be inconsistent; and a false certificate could look convincing.

The construction turns those problems into advantages.

A true winner has a robust comparison property. Other columns need not. The quantum algorithm can exploit the robust property without proving that every comparison is meaningful. It uses comparisons to obtain a small shortlist and pays the full certificate-verification cost only afterward.

Meanwhile, the classical algorithm cannot cheaply identify the planted winner or its hidden certificate address.

This is a striking architectural idea.

Your manuscript explains all of its components, but it often treats them as separate technical accomplishments rather than parts of one central argument.

For example, page 10 explains why the losing columns can form a cycle. Page 11 explains why the total surviving weight nevertheless decreases. Pages 12–14 explain how to realize the ideal sampling process quantumly.

These should feel like three stages in a single discovery:

Sorting cannot work because losing candidates need not have a consistent ordering.

Fortunately, a potential-function argument needs only pairwise complementary comparison probabilities.

Quantum sampling realizes precisely that potential process without explicitly calculating its weights.

The crucial observation is that the impossibility of sorting motivates the weighted tournament.

That relationship is present, but the reader has to do too much of the conceptual connecting.

An excellent exposition would make the transition from the cycle to the weighted sampler one of the most satisfying moments in the paper.

3. Where the manuscript still feels overengineered
This is the most important new criticism from my rereading.

Sometimes the paper sounds as though it is anticipating an exacting mathematical referee rather than guiding an interested mathematical reader.

Consider Section 4.1 on page 9. The comparison is introduced, but almost immediately you must explain its tie-breaking rule, ordering of unordered pairs, reverse-order interpretation, fresh calls, diagonal convention, and the identity

a
i
j
+
a
j
i
=
1.
a 
ij
​
 +a 
ji
​
 =1.
All of these details contribute to a rigorous definition. Yet the reader has scarcely had time to appreciate the comparison's beautiful central property:

A valid winner beats every rival because its pointers can find zeros in rivals, whereas rivals cannot find zeros in its all-one string.

That is the mathematics that should dominate the passage. The precise orientation convention should support it, not compete with it.

The same thing happens at the start of Section 5 on page 16. Before seeing the planted inputs, we encounter a relatively elaborate minimax discussion, including its correctness-matrix interpretation and the exact quantifier governing the hard distribution. 
exposition(4).pdf

This is mathematically responsible, but editorially I would reverse the priorities.

First introduce the two worlds:

One board has a zero in every column and blank certificate cells. The other erases one zero and fills one secretly selected certificate cell. How could an algorithm tell which world it is in?

Then explain the hard distribution needed to make the addresses difficult.

The reader now has a question to which minimax supplies the answer.

The difference is not one of rigor. It is the difference between mathematics motivated by a problem and mathematics introduced as machinery.

The risk of excessive qualification
You are admirably careful about what each example establishes, especially the distinction between the four-column board and the asymptotic construction.

But the paper occasionally repeats such qualifications at a cost to momentum.

The tiny board is repeatedly identified as illustrative rather than asymptotically hard. Various examples are identified as mutations of the base board, not mutations of one another. Several technical passages explain precisely which properties are and are not established elsewhere.

Some of these distinctions are essential. But I would consolidate them.

For example, one short paragraph at the beginning of the construction could establish:

Throughout, the four-column board illustrates the definitions and algorithms; the lower bounds concern the larger family. Each later board modification starts from this same base example unless explicitly stated otherwise.

After that, you can trust the reader to remember the convention.

Great mathematical writing is precise, but it is also confident. It does not have to defend every choice immediately after making it.

4. Which mathematics deserves the most space?
This is where I would exercise the strongest editorial judgment.

Not all correct derivations deserve equal space in an exposition.

The paper has several calculations that are standard applications of existing methods, and others that explain the distinctive structure of this construction.

I would allocate space according to explanatory importance, not technical length.

Mathematical passage

My editorial decision

Eight-bit Walsh calculation, pp. 2–3

Keep the concrete calculation; compress surrounding normalization detail

Exact transcript certification, pp. 6–7

Give greater prominence to the local-certification equivalence

Expected halving, p. 11

Keep the full derivation; this is a central insight

Conditional weighted sampling, pp. 12–13

Expand the conceptual explanation and foreground its key identity

Two-by-two amplification matrices, p. 13

Shorten in the main text; retain the derivation in an appendix

Controlled oracle implementation, p. 15

State the required query-cost lemma; relocate low-level implementation

First-difference coupling, pp. 16–17

Keep and emphasize

Capped true-cell predictor, pp. 18–19

Keep the full argument; improve its motivation

Small technical counterexamples, pp. 20–21

Relocate most to optional material

Quantifier argument, pp. 21–22

Preserve; it is concise and important

A particularly important distinction
I would not simplify the proof of the weighted sampler by simply asserting that amplitude amplification gives the desired pivot distribution.

That would sacrifice something genuinely important.

The identity

Pr
⁡
(
success and label 
i
)
=
w
i
m
Pr(success and label i)= 
m
w 
i
​
 
​
 
is the point where the ideal stochastic tournament becomes an implementable quantum procedure.

A reader should understand why independent fresh comparisons produce the product of probabilities, why different column labels contribute orthogonal probability masses, and why amplification preserves the successful label law.

These arguments deserve space.

By contrast, deriving the reflection matrices in full is less specific to the construction. The exposition could establish the two-dimensional rotation formula succinctly and give its detailed derivation elsewhere.

This is the kind of choice an exceptionally good mathematical author makes: prove the distinctive insight in full, and handle standard supporting machinery efficiently.

I would apply the same principle to the classical section. The capped simulator is central and should remain. The many separate technical counterexamples supporting its assumptions need not all interrupt the main proof.

5. The examples need stronger selection, not multiplication
On the first review, I praised the extensive use of examples. I still do.

But I now think the examples have reached the point where selection matters more than quantity.

Consider the different examples around the classical lower bound.

Figure 4 on page 17 is indispensable. It gives an actual picture of the dummy and planted boards.

The small two-clock simulator on pages 20–21 is also valuable. It shows how an adaptive algorithm can be cut off before exceeding its allowed queries, and why the full run's query count matters.

But then there are also separate examples concerning dependent planting, conditioning on lightness, pooled query budgets, and independent side information.

Each demonstrates a real issue. Collectively, they make the section feel like a collection of defenses against possible mistakes.

For a technical reconstruction, that is excellent.

For an exposition, I would choose the central example and put it immediately after the corresponding argument. The other counterexamples would belong in an appendix called something like Why the hypotheses matter.

That would give the main proof a much stronger shape.

Likewise, I would reconsider whether the paper needs both Figure 1's general board schematic and Figure 2's concrete four-column instance in consecutive pages.

Both are useful, but perhaps one carefully designed figure could do their jobs better.

The goal is not more visual explanation. It is to give the reader a few exceptionally clear objects that remain memorable throughout the paper.

6. The opening should have more intellectual tension
Let's think about what an excellent first page actually does.

It doesn't merely establish the theorem's importance or define the objects. It creates a mathematical problem that the reader wants to see resolved.

Your opening is factual and careful. But it begins with theorem attribution, the optimal exponent, a note about formal proofs, prerequisite declarations, a four-bit OR example, the query model, and a description of the construction.

By the end of page 1, the reader has received a great deal of information. But the central difficulty hasn't been made sufficiently vivid.

I would make the first page revolve around one question:

How can finding and verifying a certificate apparently cost too much, yet a quantum algorithm still find a winner in roughly 
m
m
​
  queries?

That is an excellent problem to put in front of a reader.

Then present the obstruction and the surprising solution.

For example, the beginning of Section 4 could be made much sharper:

A certificate can be verified by searching its local consistency tests, at a cost of roughly 
m
m
​
  quantum queries. Searching over 
m
m possible winning columns using that verifier would multiply the costs, giving roughly 
m
m queries. This loses the nearly quartic separation.

The essential observation is that finding a candidate need not cost as much as verifying one. Two columns can be compared much more cheaply by following their pointers. A true winner defeats every rival with high probability, although the other comparisons may be inconsistent. We will use those comparisons to construct a short list, and verify only its members.

This is close to what page 9 already says. My suggested change is mainly one of emphasis, proportion, and rhythm.

The paragraph gives the reader a numerical obstacle, an unexpected distinction, and a plan.

That is the experience I want the whole paper to create.

7. There is a readability problem beyond the words
Looking again at the rendered pages, the typesetting is professional and readable. But it is not yet particularly expressive.

Pages 7–9, 12–15, and 18–22 contain long runs of dense prose and equations with relatively little visual differentiation between major results and technical discussion.

The document has bold lead-in phrases, but many are at similar levels of prominence.

A mathematician skimming the document should be able to recognize its few load-bearing results almost immediately.

At present, the most important mathematical statements are not always visually privileged.

In particular, I would give four results more recognizable identities: the local-certification equivalence on page 7, the expected-weight-halving identity on page 11, the exact conditional pivot law on pages 12–13, and the first-difference/capped-prediction mechanism on pages 16–19.

They do not all need colored boxes or elaborate formatting. Quite the opposite: a well-spaced proposition, a displayed equation, and a brief explanatory sentence would suffice.

The key is that the typography should reflect the logical hierarchy.

There is another issue of notation density. The same parameter 
m
m denotes both the number of columns and the width of each sign block; 
r
r controls the number of partial-function answers; 
S
S counts circuit gates; 
K
K counts local tests; 
L
L is the classical hardness budget; 
G
G is the global classical budget; 
T
T is the number of quantum pivots.

Each is necessary.

But the reader's understanding would benefit from an early, compact parameter map and consistent reminders only at major transitions.

That is better than continually reintroducing symbols in prose.

8. The ending is weaker than the mathematics deserves
This struck me particularly strongly on the third reading.

The paragraph on page 22 beginning “Return to the four-column board” is an excellent ending to the mathematical story.

It brings the reader back to the object from which the construction began, explains how the quantum and classical analyses relate, and closes with the idea that the fourth power comes from their different costs of accessing the same input. 
exposition(4).pdf

That is where I would want the exposition to end.

But instead the reader encounters a long combined-explanation exercise, a section on formal proof navigation, then pages of answers and a grading rubric.

This makes the ending feel pedagogically administrative rather than mathematically satisfying.

The questions are useful, but they belong after the main exposition as optional exercises. The same goes for the answer key and rubric.

There is also a question of genre.

The manuscript currently sits between a mathematical essay, a graduate tutorial, and a proof-reconstruction workbook. It is capable in all three forms, but the genres sometimes interfere with each other.

A great mathematical exposition can be pedagogical without continually instructing the reader to check their understanding.

I would remove the exercise prompts from the main narrative, preserve them in a consolidated exercises section, and let the mathematical argument reach its conclusion without interruption.

This one change could noticeably improve how the paper feels to read.

9. What a 10/10 structure might look like
I would consider rebuilding the main narrative around the following progression, while keeping the rigorous details in the manuscript or its appendices.

OPENING

The puzzle: verifying every candidate is too expensive.

Introduce the board and explain the cost obstacle. Give the reader a reason to care about the hidden addresses.

FOUNDATION

The certificate: hidden, but locally checkable.

Use the eight-bit examples, promise failure, and gate transcripts to explain the object precisely.

QUANTUM IDEA

Compare instead of verify.

Show why the true winner beats every rival and why inconsistent loser comparisons defeat ordinary sorting.

QUANTUM INSIGHT

Sample from weights that are never computed.

Derive the halving potential, successful label law, and amplification guarantee. Explain why the total cost is nearly 
m
m
​
 .

CLASSICAL INSIGHT

A query to the right hidden cell is already an address prediction.

Introduce the planted pair and prove that finding the erased zero or visiting the true cell is unlikely.

CONCLUSION

The two costs produce exponent four.

Give the fixed-
k
k quantifier argument, import the universal upper bound, and return to the board.

Notice that this structure does not require new mathematics.

It changes what is foregrounded and when.

I would aim for a main narrative of perhaps 18–21 pages, with the supporting examples, calculations, and exercises remaining accessible afterward. That is an editorial target, not a demand for arbitrary compression.

10. What I would use as the quality test
I wouldn't judge the next revision primarily by the reactions “clear,” “detailed,” or even “rigorous.” The existing paper already earns those descriptions reasonably well.

Instead, I would ask three questions of an unfamiliar mathematical reader.

After two pages: Can they explain what makes this construction interesting, what is being hidden, and why the obvious quantum search strategy is too expensive?

At the end of Section 4: Can they derive the idea behind the expected-halving identity and explain why successful quantum sampling has the right weighted distribution, without having to work backward through several pages?

At the end of the paper: Can they tell the classical lower-bound story in one coherent argument—planting, first difference, erased zero, hidden cell, capped address prediction—and connect it to the exponent calculation?

If those answers are yes, you have achieved something much more meaningful than producing a manuscript without any confusing sentences.

You have enabled someone else to possess the mathematical argument.

11. My final editorial recommendation
I would change the revision strategy quite decisively now.

Stop asking the manuscript to become more comprehensive. Stop treating every confusion as a reason to add an explanatory paragraph. Stop treating every technical subtlety as something the reader must confront at the earliest possible moment.

Instead, perform a subtractive and structural edit.

Give the entire paper one unmistakable central argument. Make the cycle of losing columns lead naturally to the weighted potential. Make that potential lead naturally to coherent sampling. Make the planted pair lead naturally to the capped predictor. Let the exponent conclusion resolve the narrative.

Preserve the complete rigor, but move standard derivations and defensive technical examples out of the main intellectual path.

I would especially protect the mathematical passages that are already excellent: the promise-failure example, the expected-weight-halving calculation, the precise successful-label law, the planted-pair figure, and the capped true-cell predictor.

Those are the paper's strongest assets.

What I think would finally move the score
These are subjective editorial targets, not guaranteed score improvements.

Revision approach

Likely outcome

Another local prose-polishing pass

Still around 8/10

Add more explanatory paragraphs and examples everywhere

Possibly worse: denser and more repetitive

Improve only the diagrams and formatting

Modest improvement

Rebuild conceptual transitions, prioritize the distinctive lemmas, and remove narrative interruptions

Credible path toward 9–9.5

Above, plus a successful fresh-reader test and a final sentence-level edit

Plausible 10/10

The final step matters because mathematical exposition isn't only about structure. Once the architecture is right, the prose should be elegant: short where the idea is simple, deliberate where it is subtle, and never more elaborate than the argument requires.

My clearest conclusion after this rereading is that the manuscript has enough mathematics and enough explanation. What it needs now is better judgment about what the reader should be thinking about at each moment.

The paper should stop feeling like a comprehensive explanation of every component of a proof and start feeling like the most natural possible route to understanding why the theorem is true.

That's the difference between a strong technical exposition and a truly memorable mathematical paper.

another pass through of rereading lets start to think about how to get it to 10/10 cuz repeated revies hover at 8 atp 

like lets have taste and think about what makes a truly well written paper 

liek jsut reifnroce what you've been saying but think about it further read the paper properly agian

like now sum up this whole thread and reread agian like you can specify the deliverables on making this a 10/10 no more 8/10 fucking rating

Worked for 3m 56s
The definitive editorial brief: making Why OpenAI’s query separation is nearly quartic an exceptional mathematical exposition
Document reviewed: the attached 27-page PDF, November 2026.

Objective: Produce the best possible standalone explanation of the mathematics for a mathematically mature reader. Not the most exhaustive reconstruction, not the most accessible popularization, and not a showcase for the surrounding project.

The goal is a paper that a serious mathematician reads and thinks:

This is a difficult argument, but I can see why its ideas work, why the construction has this shape, and why the proof could not simply have been done in the obvious way.

1. What the entire review thread has established
There has been a consistent progression through the reviews.

First reading — the mathematical content is already strong. The eight-bit Forrelation example, four-column board, off-promise counterexample, cycle among losing columns, weighted tournament, and planted-pair lower bound are substantial explanatory assets. They should not be discarded.

Second reading — the explanations appear in the wrong order. The paper frequently supplies mathematical machinery before the reader fully understands which obstacle that machinery is overcoming. This is clearest in the quantum sampler on pages 12–14 and capped simulator on pages 18–19.

Third reading — there is too much competing explanation. The manuscript sometimes reads like a proof audit or graduate workbook. Caveats, error budgets, alternative examples, references, and implementation details occupy space that ought to belong to the central ideas.

This reading — the remaining work is principally one of mathematical composition. We need to decide which ideas deserve the foreground, construct a natural sequence of discoveries, and make every displayed formula earn its place in that sequence.

The previous advice to add diagrams and intuition needs an important qualification: do not keep adding explanatory material to an already dense manuscript. A new explanation should normally replace something less effective, not accumulate beside it.

What must be preserved
The manuscript has five particularly strong mathematical moments:

The promise failure: 
a
−
a 
−
  produces the same projection probability as 
a
+
a 
+
 , yet it is outside the partial function's promise. This makes exact domain certification necessary.

The dominating nonwinner: a column can beat every rival and still fail certificate verification.

The cycle and expected-halving identity: losing columns need not form an order, yet the tournament's surviving weight decreases.

The implicit quantum sampler: the algorithm obtains the correct weighted pivot distribution without computing the weights.

The planted-pair reduction: even guessing the correct certificate cell constitutes a prediction of all its hidden address answers.

Those are not just examples or technical lemmas. They are the intellectual backbone of the exposition. 
exposition(4).pdf
exposition(4).pdf
exposition(4).pdf

2. The single governing editorial principle
Every major mathematical object should enter as the solution to an obstacle the reader already understands.

That gives the whole exposition a natural sequence:

THE PROBLEM

Finding a valid hidden certificate by repeated verification is too expensive.

FIRST INSIGHT

Comparing candidates is cheaper than verifying them.

THE DIFFICULTY

Comparisons between nonwinners are unreliable and need not form an ordering.

SECOND INSIGHT

An implicitly weighted tournament still finds the genuine winner.

THE QUANTUM MECHANISM

Coherent comparisons and amplification realize those weights without calculating them.

THE CLASSICAL OBSTRUCTION

A planted certificate cannot cheaply be found or guessed, even adaptively.

THE CONCLUSION

The different access costs force the optimal exponent to be four.

This should be the reader's experience of the argument, not merely a summary supplied after the proof.

The rigorous mathematics remains. The change is that each rigorous calculation now answers a question that the preceding passage has created.

3. The deliverables
I would commission the next revision as six tightly defined editorial deliverables. Each has a specific purpose and a test for whether it has actually succeeded.

Deliverable 1 — A rebuilt introduction and opening example
Current pages 1–5 · Highest priority

Required outcome: The reader understands the construction's central difficulty before encountering its detailed mathematical implementation.

The present introduction moves from attribution and theorem statements to model definitions, partial-function promises, the Walsh experiment, and finally the concrete board.

This means the reader encounters the apparatus of the proof before acquiring a compelling mental picture of the problem.

I would rebuild the opening around the following progression:

Define the query model and explain the randomized–quantum separation in a few precise paragraphs.

Show a simplified four-column board and explain what a winning column certifies.

Establish why checking certificates during a search is too expensive.

Announce the distinction between comparing candidates and certifying candidates.

Introduce the hidden address and pose the problem of making it quantumly accessible but classically hard to discover.

The eight-bit example should then arrive naturally as the mathematical construction supplying the hidden address.

An important restraint: Do not dump the fully defined 5,936-bit toy instance onto the first page. Introduce the board schematically and explicitly say that the precise address computation and certification conditions follow. The complete Figure 2 can then serve as the first exact instance.

The existing opening also gives the exponent 
α
t
o
t
α 
tot
​
  before defining 
R
(
f
)
R(f) and 
Q
(
f
)
Q(f). Reverse that order. Move the Lean-development sentence and the description of companion documents out of the opening mathematical argument.

Here's the sort of opening paragraph I'd actually want to read:

A randomized algorithm can be much more expensive than a quantum algorithm even when both are asked to compute the same total Boolean function. The largest possible power separation is four. The difficulty in attaining it is not merely to hide a useful certificate: a quantum algorithm must still find that certificate without paying its verification cost at every candidate. The construction we study solves this problem by separating comparison from verification. A genuine certificate gives its column a reliable advantage in pairwise comparisons, even though comparisons among other columns may be inconsistent. This permits a quantum search that verifies only a short list, while a classical algorithm still has to discover the hidden location of the certificate.

I would then immediately show the board.

Notice the difference: this tells the reader what the mathematical problem is, why the construction has its particular form, and which idea to look for.

It doesn't dilute the mathematics. It makes the mathematics purposeful.

Acceptance test: By the end of the opening two pages, a reader should be able to explain the apparent 
m
×
m
m
​
 × 
m
​
  quantum cost, why this is too large, and what cheap comparisons are intended to change.

Deliverable 2 — One canonical board, followed by controlled counterexamples
Current pages 2–7 and 9–11

The board is already a major strength, but its appearances should feel like one continuing mathematical experiment.

At present there are a base board, a domain-bit board, a false-pointer board, a cycled board, and later a planted pair. Their relationships are documented, including the useful mutation table on page 11.

I would make the example architecture more deliberate.

Base board — Figure 2, page 5

Establishes what a valid certificate looks like and why there is at most one winner.

Promise failure — page 6

Shows why an apparently correct address and transcript do not suffice without domain certification.

Dominating nonwinner — pages 9–10

Shows why comparisons cannot replace exact verification.

Cycle — Figure 3, page 10

Shows why no ordering of losing columns can be assumed.

Planted pair — Figure 4, page 17

Reuses the board's geometry to explain the classical indistinguishability argument.

I would give every example the same compact explanatory discipline: what single assumption is being tested, the smallest change from the base board, what happens, and what general lesson survives.

The examples do not need extensive concluding qualifications. A single convention can explain that the four-column construction illustrates the mechanisms but not the asymptotic hardness, and that each mutation starts from the base board.

Acceptance test: A reader can describe why each counterexample is necessary without having to remember every assigned bit.

The figures should remain mathematically precise. Figure 3 already does a good job of distinguishing the actual winner from the cycle among losers; its red and grey arrows make the point immediately. I would preserve that economy rather than redesign figures merely for visual novelty.

Deliverable 3 — A complete rewrite of the exposition of the weighted quantum tournament
Current pages 9–15 · The most important mathematical edit

This is where I would spend the largest amount of editorial attention.

Not because the existing material is bad, but because the mathematical idea is unusually elegant and deserves a correspondingly elegant explanation.

I want the reader to experience four precise discoveries.

Discovery A: Reliable winners do not imply reliable comparisons
The property

a
i
⋆
j
≥
1
−
ε
a 
i 
⋆
 j
​
 ≥1−ε
is enough to protect a true winner, although comparisons between two other columns need not have an underlying correct orientation.

Introduce the winner property before discussing the full tie-breaking convention. Then establish the exact complementary probabilities

a
i
j
+
a
j
i
=
1
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
 =1,a 
ii
​
 =0.
Those are the properties used by the potential argument.

The cycle on page 10 should then make the need for something other than sorting obvious.

Discovery B: The weight halves even without an order
Retain the central identity from page 11:

E
[
∣
w
′
∣
∣
w
]
=
∣
w
∣
2
−
∑
i
w
i
2
2
∣
w
∣
≤
∣
w
∣
2
.
E[∣w 
′
 ∣∣w]= 
2∣w∣
∣w∣ 
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
∣w∣
​
 .
But explain the idea immediately before deriving it: each unordered pair contributes exactly once when the weighted pivot is averaged over both possible orientations.

Then the algebra becomes a surprisingly short explanation of why cycles do not matter.

The next argument, that the genuine winner retains substantial weight until selected, must stay close to the halving proof. Together these are the heart of the ideal tournament.

Discovery C: Quantum computation samples weights that are never calculated
The existing Section 4.3 contains the right crucial formula:

Pr
⁡
(
success and column 
i
)
=
1
m
∏
b
a
i
p
b
=
w
i
m
.
Pr(success and column i)= 
m
1
​
  
b
∏
​
 a 
ip 
b
​
 
​
 = 
m
w 
i
​
 
​
 .
The exposition should build toward this as its central result.

I would organize the derivation in the following order:

First describe the ideal sampling operation and the distribution it needs. Then construct the uniform quantum preparation with independent fresh comparison registers. Explain that their probabilities multiply, and that different column labels contribute orthogonal probability masses. Derive the displayed identity. Finally, show that conditioning on success gives 
w
i
/
∣
w
∣
w 
i
​
 /∣w∣.

Only after this should the reader confront the details of coherent implementation, retained workspaces, and reversibility.

The current page 12 instead opens its implementation discussion with reversible-circuit mechanics before reaching the probability identity. 
exposition(4).pdf

The identity should be the star; the implementation should justify it.

Discovery D: Amplification makes the sampling usable without biasing the answer
This is subtle and must not be waved away.

The original argument explains that amplitude amplification changes the coefficient of the normalized successful state 
g
g, not the relative probabilities inside it.

Keep that fact in the main exposition.

But I would move the full two-by-two reflection-matrix multiplication to an appendix, retaining a short geometric derivation of the rotation formula in the main text.

Explain explicitly the two things amplification accomplishes and does not accomplish: it raises the chance of obtaining a successful flag, and it leaves the successful column distribution unchanged. It does not guarantee a successful sample when the original success probability is zero.

Finally give the bounded, unknown-success-probability routine and the coupling argument. The worst-case query cap and the treatment of zero success probability are mathematically necessary, so these cannot simply disappear.

Acceptance test: An unfamiliar reader should be able to reconstruct the entire quantum argument in this order:

winner reliability
⇓
weighted potential decreases
⇓
coherent preparation realizes the weights
⇓
amplification samples without bias
⇓
shortlist followed by verification
.
winner reliability
⇓
weighted potential decreases
⇓
coherent preparation realizes the weights
⇓
amplification samples without bias
⇓
shortlist followed by verification.
​
 
If the reader understands those five implications, the query count becomes the final accounting step rather than the central mystery.

Deliverable 4 — A classical lower bound that reads as one inevitable argument
Current pages 16–21

Here I would make fewer substantive changes than in the quantum section.

The current proof is already well organized. The main opportunity is to strengthen its conceptual continuity.

The classical proof should have one central sentence:

An algorithm that distinguishes the planted board from the dummy board must discover the erased zero or reach the secretly selected certificate cell; reaching that cell is itself a prediction of all the hard address answers.

Everything in the proof should serve this sentence.

I would move the motivating description of the planted pair before the detailed minimax discussion, while still introducing the common hard distribution 
μ
μ before formally sampling the boards.

The first-difference argument should then occupy a prominent position:

∣
Pr
⁡
[
A
(
Y
1
)
=
1
]
−
Pr
⁡
[
A
(
Y
0
)
=
1
]
∣
≤
Pr
⁡
(
erased zero hit
)
+
Pr
⁡
(
true cell visited
)
.
​
  
​
 Pr[A(Y 
1
 )=1]−Pr[A(Y 
0
 )=1] 
​
 
≤Pr(erased zero hit)+Pr(true cell visited).
​
 
Immediately after this, explain the two possible routes by which the algorithm can distinguish the inputs.

The three-charge table on page 17 is excellent and should remain. But the reasoning should now unfold more naturally: finding the erased zero is unlikely, selecting a heavily queried column is unlikely, and visiting the true cell of a light column predicts all the hidden answers.

The main rewrite is at the simulator.

Before defining its steps, explain the three query budgets. Before introducing its default output, explain why it needs to be a valid bounded algorithm on every input, not just successful visits.

Then introduce the event inclusion:

{
light and true cell visited
}
⊆
{
capped predictor is correct
}
.
{light and true cell visited}⊆{capped predictor is correct}.
This inclusion is the conceptual core of pages 18–19. 
exposition(4).pdf

I would retain the direct-product lemma and its exact independence and separate-cap hypotheses. I would also keep its proof in Appendix B, which is already a sensible location.

But most of the additional counterexamples on pages 20–21 should move into a section of optional technical examples. The two-clock simulation is the most valuable one for the main exposition; even that could be shortened.

Acceptance test: The classical proof should be explainable as one coherent reduction, not as a sequence of three estimates followed by an unrelated simulation trick. The reader should see why the simulator exists before reading how it operates.

Deliverable 5 — Restore a proper mathematical ending
Current pages 19–23

This change is straightforward and, I think, disproportionately valuable.

The main proof of the classical lower bound finishes on page 19. Two pages of auxiliary examples then intervene before Section 6 derives the optimal exponent.

Move the optional examples after the main conclusion.

The reader should move directly from

R
(
F
k
,
m
)
≳
m
2
−
1
/
k
R(F 
k,m
​
 )≳m 
2−1/k
 
to the quantum bound

Q
(
F
k
,
m
)
≲
m
Q(F 
k,m
​
 )≲ 
m
​
 
with logarithmic factors suppressed, and then to the exponent 
4
−
2
/
k
4−2/k.

Keep the careful argument that one first fixes 
k
k and then increases 
m
m. This is essential, and Section 6 explains it well.

Keep the distinction between proving that every exponent strictly below four fails universally and producing one family with an exact fourth-power separation. Do not blur that distinction for a tidier conclusion.

Then end with the existing paragraph on page 22 beginning “Return to the four-column board.”

Its closing idea is excellent: the nearly fourth-power separation results from the different costs of accessing the same input. 
exposition(4).pdf

I would let that be the final paragraph of the main mathematical exposition.

The combined exercise, guided rubric, answer key, and formal-proof navigation should follow only after a clearly marked end of the main argument.

This also resolves the manuscript's genre problem. It becomes a mathematical exposition with useful supplementary exercises, rather than a mathematical exposition that turns into a workbook at the moment of its conclusion.

Acceptance test: The paper's last main-text page leaves the reader with the theorem and its mechanism, not an assignment to complete or an invitation to another document.

Deliverable 6 — A mathematical prose and typography edit
Entire PDF · Only after structural editing

This is the final stage, not the first.

The objective is not to make every sentence shorter. It is to make the mathematical argument easier to read without loss of precision.

I would address the following specific matters:

Issue

Required action

Central theorem split across pp. 8–9

Keep theorem statement and both inequalities together

Too many similarly weighted bold lead-ins

Establish a consistent hierarchy of definitions, lemmas, explanations and examples

Dense prose on pp. 12–14

Break paragraphs according to mathematical claims, not merely length

Query-count notation

Supply one compact parameter guide and use symbols consistently

Repeated explanations of fixed caps and off-promise behavior

State carefully at their first essential use; refer back concisely

References to the reasoning record and theorem index

Preserve academically useful references without making the main argument feel dependent on accompanying materials

Exercise prompts interrupting proofs

Relocate to the supplementary exercises

Bibliography entry “OpenAI 2026. Online source”

Supply a complete, identifiable bibliographic reference

Awkward equation and paragraph page breaks

Fix during final PDF pagination

I would also give each major mathematical result a recognizable typographic identity. Not colorful callouts—just clear proposition statements, well-spaced displays, and purposeful paragraphing.

Acceptance test: A mathematical reader skimming the section headings and displayed formulas can recover the structure of the proof without reading every paragraph.

4. What the revised manuscript should look like
I would not force an arbitrary page reduction. The main text may become shorter, but only because supporting material has been placed where it belongs.

Here is the proposed final architecture.

Part

Content

Purpose

Introduction

The separation, the certificate board, and the search obstruction

Establish the mathematical puzzle

1. Hidden addresses

Eight-bit Forrelation, promise, cheap quantum decoder

Explain where the addresses come from

2. The board and local certificates

Winner condition, exact transcripts, local verification

Establish what must be certified

3. Ingredients at general scale

Quantum decoding, circuit size, classical hardness

State the three input properties

4. Finding candidates without verifying them

Comparisons, cycle, weighted tournament, coherent sampling, verification

Prove the quantum upper bound

5. Why classical algorithms cannot find the certificate

Planted pair, first difference, three charges, capped predictor

Prove the classical lower bound

6. Why the exponent is four

Bound comparison, quantifiers, universal upper bound

Complete the mathematical story

Appendices

Amplification details, query accounting, separate-cap proof, additional examples and exercises

Preserve rigor and deeper study

The largest structural changes are in the introduction, Section 4, the first part of Section 5, and the placement of the conclusion.

The rest should be comparatively conservative.

5. What I would explicitly forbid in the next revision
This matters because the previous revisions seem to have responded to criticism by adding material.

I would forbid four common forms of unproductive editing.

First, no ornamental intuition. Do not add another metaphor or informal analogy unless it resolves a specific conceptual obstacle more efficiently than the existing explanation.

Second, no extra examples without replacing or consolidating an existing one. The manuscript already contains enough examples to teach the construction. Better sequencing is more valuable than increasing their number.

Third, no weakening of the technical contract. The exact successful-label law, all-input query cap, promise certification, joint light-visit event, and fixed-
k
k quantifiers are not dispensable details. They are required to make the argument correct.

Fourth, no attempt to make every paragraph understandable to every conceivable audience. Choose mathematically mature readers willing to learn the relevant quantum-query formalism. Teach that formalism well, but do not dilute the paper into a general introduction to quantum computing.

A particularly important constraint is that this is still a standalone PDF. The main mathematical transitions must be understandable from the PDF itself. A reference to a longer reasoning record is appropriate for technical expansion, but should not replace the central explanation.

6. A rigorous editorial acceptance protocol
The revised document should not be judged by another impressionistic review alone.

I would require three tests.

Test 1 — The first-reading test

Give the new paper to an unfamiliar mathematically sophisticated reader. Record the exact places where they cannot answer “Why are we doing this?” or “What is the next step trying to establish?” Do not explain the paper to them while they read it.

Success: the reader can follow the purpose of each major proof stage without editorial intervention.

Test 2 — The reconstruction test

After reading, ask them to explain the quantum and classical mechanisms independently, including why the weighted sampler has the correct conditional distribution and why a light true-cell visit becomes a capped address prediction.

Success: they can reconstruct the central proof dependencies and identify the imported results, even if they do not remember every constant.

Test 3 — The specialist objection test

Have a query-complexity specialist identify any explanation that has become technically misleading through simplification. Check the sampling law, reversibility assumptions, error accounting, all-branch query caps, classical conditioning argument, and quantifier order.

Success: the editorial improvements preserve the mathematical content and do not introduce new proof gaps or unjustified intuitions.

These tests matter more than a numerical rating. They assess whether the paper successfully transfers the mathematical argument to someone encountering it for the first time.

7. Final deliverable specification for the next writing pass
The primary output should be one revised, publication-quality exposition PDF. It should remain mathematically self-contained relative to its explicitly imported theorems, preserve the substantive arguments, and use the examples to explain the mathematics rather than simply demonstrate calculations.

For the writing process, I would also require a short editorial change ledger—not published in the paper—recording what was moved, deleted, rewritten, or preserved and why. This prevents regressions in which a later revision restores an explanation that was intentionally removed or pushes an essential proof detail into inaccessible supplementary material.

The actual writing work should happen in this order:

Set the complete narrative structure and write the opening and ending first.

Rewrite the quantum tournament as one continuous mathematical argument.

Reorganize the classical proof around the planted pair and capped predictor.

Place the examples at their exact points of explanatory necessity, moving the rest to supplementary material.

Perform the final prose, notation, figure, bibliography and pagination edit, followed by the reader tests.

I would not make further large changes to the underlying mathematical statements unless a specialist identifies a genuine issue.

My concluding judgment after the entire thread
What makes this paper promising is that the mathematical material is not inherently dull or bureaucratic. Quite the opposite.

There is something beautiful in a tournament that works without a consistent ordering. There is something beautiful in a quantum procedure that samples unknown probability weights exactly. There is something beautiful in the observation that merely choosing the location of a query can constitute a hard prediction.

And the nearly quartic exponent emerges because those mechanisms allow radically different costs for accessing the same hidden certificate.

Those are the ideas that ought to dominate the reading experience.

The current exposition contains them, but surrounds them with enough apparatus that the reader must sometimes excavate the elegance.

I don't want another revision that merely turns 27 pages into 30 pages of increasingly careful explanation.

I want the next draft to feel more direct, more selective, more mathematically inevitable.

A really well-written mathematical paper does not make difficult mathematics appear trivial. It makes the difficulty intelligible, then shows precisely which idea overcomes it.

That is the standard I would hold this revision to: preserve all the intellectual substance, remove unnecessary competition for the reader's attention, and make the central argument the clearest and most memorable thing in the paper.





