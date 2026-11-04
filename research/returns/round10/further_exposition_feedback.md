

exposition(1).pdf
PDF
read attached give feedback on this paper how well is it written for its intended audience give a papers worth of feedback im gonna folow this up with several "reassess again" so your initial response will not be the final one goign back so i guess plan what your subsequent go thorugh is gonna be i guess lets start high level

Worked for 4m 1s
Editorial review — Pass 1: Is this exposition well written for its intended audience?
Review of Why OpenAI’s query separation is nearly quartic · 26 pages · November 2026

1. Overall assessment
This is a serious, unusually careful mathematical exposition with strong examples and a coherent underlying argument. Its principal weakness is not mathematical precision or sentence-level writing. It is that the reader has to work too hard to discover, retain, and connect the central ideas.

I would make an important distinction between two kinds of clarity:

Local clarity: Does an individual paragraph, definition, calculation or example explain what it is doing?

Global clarity: Does the reader understand why they are learning this particular thing, how it connects to what preceded it, and what they will eventually be able to conclude?

The paper is substantially stronger on the first than on the second.

It is also better at removing possible misunderstandings than at making the right understanding feel inevitable.

Those are different editorial achievements. The first is essential to trustworthy mathematics; the second is what can make a difficult exposition exceptionally good.

The encouraging thing is that the paper already contains much of the raw material needed for the second. I would not recommend starting again. I would recommend reorganizing the reader's experience.

Provisional editorial scores

Mathematical precision of the exposition

8.5/10

Quality of worked examples

9/10

Sentence-level clarity

8/10

Logical organization

7.5/10

Audience calibration

6/10

Conceptual accessibility

6.5/10

Pedagogical efficiency

6/10

Visual communication

7.5/10

Source and verification transparency

7.5/10

These are editorial judgments, not statistical scores. Mathematical precision here means how clearly and carefully the claims are presented, not that I have independently audited all the proofs or the original research.

My overall assessment depends on the reader:

Reader

Assessment

An advanced mathematics or theoretical CS student willing to study the paper carefully

8/10 — substantial, valuable guided exposition

A mathematically strong newcomer with exactly the advertised prerequisites

6–7/10 — understandable with considerable effort, but insufficiently scaffolded

A query-complexity specialist looking for a faithful explanation of the new construction

8/10 — precise and useful, though sometimes overexplained

A mathematically interested general reader

4/10 — much too demanding without more preliminary explanation

My central assessment: around 7/10 against the audience the introduction actually promises, with the potential to become an excellent 9/10 exposition through structural and pedagogical revision.

I would not call it poorly written. I would call it an intellectually ambitious exposition whose precision is currently ahead of its pedagogy.

2. Who is the paper actually for?
The introduction explicitly assumes finite-dimensional linear algebra, elementary conditional probability and asymptotic notation. It then promises that the reader will understand cheap comparisons replacing repeated certificate checks, and why guessing a certificate address is covered by the classical lower bound. 
exposition(1).pdf

That is a worthwhile and fairly clear educational contract.

But consider what the paper asks its reader to master after those prerequisites:

Boolean query complexity, randomized versus quantum access and worst-case error.

Promise problems, Forrelation and interference-based tests.

Addressed cheat sheets, exact circuit transcripts and local certification.

Randomized tournaments whose comparisons are neither transitive nor necessarily deterministic.

Coherent sampling, independent quantum workspaces and amplitude amplification.

Yao minimax, hard input distributions, adaptive decision trees and direct-product arguments.

Asymptotic lower bounds, parameter dependencies and the order of quantifiers.

The paper does explain many of these ideas. That is a strength. Nevertheless, these concepts interact so extensively that individually understandable explanations can still be collectively overwhelming.

I think there are really two possible intended audiences.

Audience A: a strong undergraduate or beginning graduate student who already has mathematical maturity and wants to learn a new research result. For this audience, the work is promising. It resembles a detailed set of self-study lecture notes with exercises and proof sketches developed into full arguments.

Audience B: someone who knows linear algebra, probability and asymptotic notation, but has never seriously studied quantum algorithms or theoretical computer science. For this audience, the paper is significantly harder than its introduction suggests.

I would choose Audience A as the primary audience, but make the paper genuinely traversable by Audience B.

That need not mean weakening the mathematics. It means teaching the reader what to care about before asking them to track the formal mechanisms.

3. The paper's strongest quality
The worked examples are not merely decorative.

They have been chosen to expose specific logical distinctions that matter to the theorem.

Consider the sequence:

How Do Computers Multiply Two Big Numbers So Fast? - LivePhysics

The three eight-bit inputs — pp. 2–3

A positive, zero and negative Forrelation value distinguish the promise from the quantum projection event. In particular, the negative example is accepted by the projection test but lies outside the promise.


The four-column board — pp. 4–6

A valid winning certificate, an invalid promise and an incorrect pointer are different ways a candidate can behave. The board becomes a physical object to reason about rather than an abstract function definition.


The cycled-loser example — pp. 9–11

A genuine winner beats everyone, but the losing columns can form a cycle. This destroys the tempting idea that the algorithm is simply sorting or performing ordinary minimum finding.


The dummy/planted pair — pp. 15–17

The classical lower bound becomes a question about whether an adaptive query procedure can find the few input locations where two boards differ.

The original Figures 2–4 are particularly useful because they serve the proof, rather than simply making the document look more attractive.

I especially like the dominating nonwinner on page 9. Changing one pointer makes the function evaluate to zero even though that column continues to dominate comparisons. That is an excellent way to demonstrate that comparison-based selection and exact certification are fundamentally different jobs. 
exposition(1).pdf

Likewise, the classical argument carefully distinguishes visiting the true cell from correctly computing its address, and the paper explicitly handles the possibility of guessing the address. That is an important conceptual point that a less disciplined exposition could easily gloss over.

These examples are among the paper's most valuable assets. I would preserve them.

But I would change when they appear, how often they are revisited, and how explicitly each is connected to the overall fourth-power separation.

4. The biggest structural problem: the main idea arrives too late
The introduction promises an explanation beginning with a four-column board.

But the actual sequence is:

2–3

Forrelation

Walsh matrices, sign vectors, quantum projection

3–6

The board

Cells, pointers, certificates, circuits, local tests

7–8

The large construction

Hard partial functions and the theorem

8–15

The quantum algorithm

Comparisons, weights, pivot sampling, verification

15–20

The classical lower bound

Planting, indistinguishability, capped predictions

20–21

Exponent four

The asymptotic synthesis and quantifiers

There is nothing logically wrong with this ordering.

In fact, it is quite reasonable if your primary purpose is to prove the result from the ground up.

But it creates an educational problem.

The reader encounters substantial mathematical machinery before they have an intuitive understanding of the complete construction. They cannot yet reliably distinguish what is essential from what is bookkeeping.

The theorem is formally stated on page 8. The central comparison argument develops over pages 9–14. The classical planting argument is introduced on page 15. Only on page 20 do the ingredients come together explicitly.

That is too long to defer the complete picture.

What I would change
I think the paper needs a genuinely simple, self-contained overview of its proof mechanism before the detailed mathematics starts.

It should be possible to read the first two pages and then explain the following:

There are 
m
m columns. A winning column is all ones and has a hidden certificate showing where every other column contains a zero.

Quantum computation can cheaply recover the information needed to compare columns. Comparisons reduce the candidates to a short list, and the algorithm pays to verify certificates only for that list. The resulting quantum cost is roughly 
m
m
​
 .

The classical lower bound hides a winning column in a random location. A classical algorithm can distinguish the planted board from a nonwinning board only by finding a concealed zero or visiting a correctly addressed certificate cell. Both are unlikely with a small query budget.

This produces roughly 
m
2
−
1
/
k
m 
2−1/k
  classical queries against 
m
m
​
  quantum queries. As the fixed parameter 
k
k is chosen larger, the exponent approaches four.

The paper already explains all of this. But the reader needs this conceptual model before embarking on the technical details.

I would add an early mathematical scoreboard:

Q
(
F
k
,
m
)
≲
k
m
 
polylog
⁡
(
m
)
,
R
(
F
k
,
m
)
≳
k
m
2
−
1
/
k
/
polylog
⁡
(
m
)
,
2
−
1
k
⟶
2
,
m
=
m
1
/
2
.
Q(F 
k,m
​
 )
R(F 
k,m
​
 )
2− 
k
1
​
 
​
  
≲ 
k
​
  
m
​
 polylog(m),
≳ 
k
​
 m 
2−1/k
 /polylog(m),
⟶2, 
m
​
 =m 
1/2
 .
​
 
Then explicitly explain why a ratio of leading exponents near 
2
/
(
1
/
2
)
=
4
2/(1/2)=4 is the target.

These equations should not appear as a proof. They should appear as the map.

The reader can then understand that the rest of the exposition has just two large obligations: explain the surprisingly cheap quantum algorithm and explain why classical algorithms cannot emulate it cheaply.

This would probably make a bigger difference than polishing any individual paragraph.

5. Local precision is excellent, but the exposition needs stronger hierarchy
A characteristic of this paper is that it explains subtle qualifications almost as soon as they become relevant.

Examples include the distinction between signed Forrelation and its squared projection probability, the requirement that exact certification include promise membership, the fact that a comparison-dominating candidate may still be invalid, and the requirement that a hard-distribution argument control a joint event rather than condition on staying within a budget.

These distinctions are substantive. They prevent genuinely incorrect reasoning.

The problem is that they are often presented at nearly the same visual and rhetorical level as the central concepts.

Consider Section 4.

The quantum argument has a particularly elegant core:

A genuine winner beats any rival with high probability.

The algorithm samples pivots according to the probabilities of beating previous pivots.

The expected total candidate weight halves at every ideal stage.

The genuine winner retains substantial weight until selected.

Quantum sampling implements the ideal process efficiently, and exact verification eliminates false candidates.

The two most revealing facts are the expected-halving inequality on page 11 and the conditional pivot distribution derived on page 12. 
exposition(1).pdf
exposition(1).pdf

They are the conceptual center of the algorithm.

But the reader has already encountered descriptions of multiple board mutations, pair orientations, nontransitive comparisons, bounded-error comparison concerns and an ideal weighted process.

Then, after the halving argument, they must understand coherent comparison registers, tensor products, amplitude amplification, preservation of successful labels, a fixed-cap schedule, error budgets and final certificate verification.

All necessary for the full proof—but not all equally important to understanding the breakthrough.

My recommendation
Introduce a clearly stated core lemma before its derivation:

Any comparison system in which pairwise win probabilities sum to one has an ideal pivot process whose expected remaining weight falls by at least half at each stage.

Then describe the winner-preservation property in plain language.

Only after these two facts should the paper explain how the quantum computer samples the appropriate distribution.

This makes a clean division:

Mathematical insight: the weighted tournament works even with arbitrary noisy comparisons between losers.

Quantum implementation: amplitude amplification samples the desired pivots without estimating the comparison probabilities.

Correctness and cost: a short candidate list plus verification gives the required query bound.

These are three separate achievements, and each deserves its own explicit conclusion.

At present, they are woven together so tightly that a first-time reader can fail to recognize the simplicity of the underlying idea.

6. The classical lower bound is unusually careful—and unusually demanding
Section 5 is perhaps the most impressive part of the exposition as a piece of rigorous teaching.

The dummy/planted construction gives a tangible meaning to the lower bound: two boards differ only at a hidden erased zero and a hidden certificate cell.

The first-difference argument is understandable without much advanced machinery.

Then the paper identifies three possible ways an algorithm might distinguish the boards: discovering the selected zero, spending too much effort on the selected column's address inputs, or visiting its true cell while still light.

The three-charge table on page 17 is extremely useful. 
exposition(1).pdf

I would preserve it almost unchanged.

The real pedagogical bottleneck comes afterwards.

The direct-product argument on pages 17–19 is precise about adaptive interleaving and separate caps. The paper correctly draws attention to an important distinction between the event that the algorithm stays light and the joint event that it stays light and predicts correctly. The simulator's stop-before-read rule makes the reduction concrete.

However, this is the point where the exposition becomes a demanding proof text rather than an introduction.

To follow the argument, the reader has to maintain simultaneous control over global query time, forwarded queries to one column, per-instance query caps, side information, the light/heavy event, a proposed cell coordinate, and the true hidden address.

It is possible to understand every sentence and still lose the argument.

What I would do differently
I would present the classical proof in three layers.

First layer: indistinguishability. Explain what changes between the two boards and why hitting a changed coordinate is necessary to tell them apart.

Second layer: the three charges. Explain why finding the erased zero is unlikely, why only a few columns can be heavy, and why guessing an entire hard address is unlikely.

Third layer: the technical reduction. Explain why an adaptive visit to the true cell really constitutes an address prediction under the appropriate cap.

The third layer deserves its full mathematical treatment. But its role needs to be unmistakable before it starts.

The XOR trace on page 19 is helpful. I am less convinced that every reader needs to work through that trace before returning to the main separation argument.

It could become a clearly marked optional example or part of an extended appendix. Alternatively, a one-paragraph summary could appear immediately before it, telling the reader precisely what the example is demonstrating and which property is being protected.

At present, the reader may spend several pages proving a subtle technical lemma and forget what contribution that lemma makes to the fourth-power separation.

I would make the final classical takeaway almost impossible to miss:

Pr
⁡
(
distinguishing event
)
≤
4
G
m
2
⏟
zero found
+
G
m
L
⏟
heavy column
+
G
(
2
/
3
)
r
⏟
true cell guessed
.
Pr(distinguishing event)≤ 
zero found
m 
2
 
4G
​
 
​
 
​
 + 
heavy column
mL
G
​
 
​
 
​
 + 
true cell guessed
G(2/3) 
r
 
​
 
​
 .
Then interpret the inequality before doing any further algebra.

It says that with 
G
G substantially smaller than 
m
L
mL, none of the three avenues gives enough distinguishing power.

That is the reader's reward for understanding the machinery.

7. The role of each technical ingredient needs to be made more explicit
The paper uses several very different mathematical ideas.

This is not an inherent flaw. The research construction itself is an assembly of mechanisms. But the exposition needs to help the reader distinguish which parts come from previous theory, which are structural properties of the new construction, and which are technical implementations.

A dependency table near the beginning would help considerably.

Ingredient

Job in the argument

k
k-fold Forrelation

Supply partial-function instances that are quantum-easy and classically hard

Cheat-sheet addresses

Hide certificates behind many independent answers

Exact circuit transcripts

Make the winner's address and promise status locally certifiable

Directed pointers

Let a genuine winner defeat any rival

Weighted pivot sampling

Find a short candidate list without assuming comparisons form an order

Quantum defect search

Verify the remaining candidates efficiently

Planted-pair coupling

Reduce classical distinction to discovering a changed input location

Separate-cap direct product

Control adaptive guesses of hidden addresses

Universal quartic upper bound

Show that the exponent cannot exceed four

These ingredients occupy different logical positions.

For example, the lower bound on the partial function is an imported theorem. The weighted tournament is the key new algorithmic mechanism being explained. The final parameter argument turns their respective costs into the claimed optimal exponent.

The paper explains this, but not as plainly as it could.

I would specifically distinguish three types of material in the manuscript: what must be understood, what must be proved, and what can be accepted as an external theorem.

That distinction would also make it easier for a reader to choose a short route through the paper without feeling they are missing the main intellectual achievement.

8. The paper's examples need a more deliberate learning progression
I do not think the paper needs more examples overall.

It probably needs fewer examples that demand equal attention.

The current selection is rich: the positive/zero/negative Forrelation inputs, the valid four-column board, the off-promise domain-bit board, the false-pointer board, the cycle of losing columns, the fractional probability matrix, the planted pair, the conditioning counterexample, the XOR simulator and the quantifier example.

That is a considerable amount of material for 26 pages.

The examples have two distinct purposes. Some establish the main mechanism; others defend it against a plausible but incorrect simplification.

That is important.

The cycle demonstrates the core need for a tournament that does not rely on an underlying order. The false-pointer example demonstrates that comparison dominance is not a certificate. Both are central.

The fractional comparison matrix is useful, but it primarily clarifies why weighted sampling is not uniform selection. The AND and XOR examples clarify subtleties in the lower-bound proof.

I would put the first group prominently in the main exposition and treat the second group as optional deeper explorations.

There is another missed opportunity: the paper repeatedly returns to the four-column board, but it does not consistently give the reader a stable mental model of that board.

After reading pages 4–6, I want the reader to remember three objects:

Column string → hidden address → certificate cell.

And three questions:

Is the column all ones? Is the certificate the correct one? Does it point to zeros in the other columns?

A small repeated schematic or compact legend could make subsequent arguments substantially easier.

The existing figures are clean, and Figure 2's red pointers and blue true-cell outlines are especially effective. I would build a visual language around them rather than adding decorative illustrations.

9. The title, introduction and conclusion need a more deliberate relationship
The title is technically reasonable:

Why OpenAI's query separation is nearly quartic.

But the title also creates two expectations: that the reader will learn why the separation works, and that the central conclusion concerns an exponent near four.

The paper does ultimately satisfy those expectations. It simply takes too long to reward them.

I would retain the spirit of the title, but make the subtitle more informative.

For example:

How quantum comparisons, hidden certificates and classical hardness combine to give the optimal exponent.

I would also explain very early the subtle difference between the near-quartic construction and the exactly optimal exponent.

For each fixed 
k
k, the displayed lower bound gives a leading exponent 
4
−
2
/
k
4−2/k when expressed in terms of the quantum cost. Choosing arbitrarily large fixed 
k
k rules out every universal exponent below four. The imported universal upper bound then shows that four is optimal.

This is an important logical distinction, handled carefully on page 20. 
exposition(1).pdf

I would bring a plain-language version into the introduction.

Otherwise a reader might reasonably wonder why something called nearly quartic proves an exactly optimal quartic exponent.

The conclusion is another opportunity.

At present, Section 6 finishes the quantifier argument and proceeds into the formal Lean discussion. The mathematical conclusion is precise, but it does not offer quite enough conceptual closure.

A good exposition should end its main argument by returning to the original board and showing how all the machinery changed the reader's understanding of it.

I would add a short final synthesis that answers the following question:

What feature of this construction makes a fourth-power separation possible when the earlier approach stopped at a smaller exponent?

The answer is not just Forrelation hardness, nor just cheat sheets, nor just quantum search. It is their combination with comparison-based selection and deferred certificate verification.

That deserves a memorable concluding explanation.

10. The treatment of Lean is responsible, but the evidence presentation could improve
Section 7 is careful about the distinction between formal verification of statements and mathematical interpretation.

In particular, it explains that Lean checks formal theorems, Comparator checks agreement with separately compiled challenge statements, and neither automatically proves that the definitions have the intended meaning or that every informal explanation is correct. 
exposition(1).pdf

This is good practice.

It would be easy to overclaim what a formalization establishes; the paper generally resists doing so.

Still, the evidence trail is not sufficiently convenient for an outside reader.

The manuscript repeatedly points to a reasoning record and expert companion. The final reference for the original OpenAI paper identifies a local filename rather than a persistent public bibliographic location.

These may all be perfectly accessible elsewhere in the project, but the present PDF does not make that straightforward.

For an expert, an exposition's credibility depends partly on whether its source claims and supplementary computations can be inspected without a scavenger hunt.

I would add a small, precise section identifying the original source, the exposition, the reasoning record, the expert companion, the Lean statements and the independently checked material. Each should have a stable link or an exact repository path and version.

I would also separate the evidence into three statuses:

Imported mathematical results, arguments reconstructed in the paper, and formally checked statements.

This is not merely a documentation improvement. It helps an expert understand exactly what kind of contribution the exposition makes.

The AI-assistance disclosure is appropriate. What matters most is that provenance, attribution and the verification boundaries remain independently understandable.

11. Style and typesetting
The sentence-level writing is mostly restrained and professional.

There is little empty motivational rhetoric. The paper tends to say exactly what an object is, what it costs, and why it matters. It rarely substitutes excitement for explanation.

I regard that as a major strength.

The typography is also serviceable: a conventional mathematical page, readable equations, restrained use of red and blue in figures, and sensible use of tables where they clarify structure.

I would not spend substantial effort redesigning the overall visual style.

I would, however, change the information hierarchy.

Pages 11–14 and 17–19 contain dense extended derivations with relatively few strong visual stopping points. The reader can lose track of the central claim while following the details.

Short intermediate propositions, one-paragraph recaps and explicit transitions would help.

A 26-page mathematical exposition also benefits from a compact contents or reading map, especially when it offers alternative routes.

The paper already contains five questions, a combined-explanation exercise and an answer section. These are good educational features, but they might work better with progressive hints rather than placing every answer at the end.

One particularly valuable addition would be a notation and objects table:

m
m is the number of columns and sign-block width; 
k
k is the number of Forrelation blocks; 
r
r is the number of hidden address answers; 
s
s is a cell address; 
ℓ
ℓ is the pointer length; 
L
L is the classical hardness budget; 
G
G is the planted-pair query budget; and 
T
T is the number of pivot stages.

Readers should not have to reconstruct this vocabulary while also learning the algorithm.

12. What I would change first
I would prioritize changes according to how much they are likely to improve actual reader understanding.

Priority

Revision

Why

1 — Highest

Put a complete conceptual proof overview before Section 1

Gives every subsequent calculation a purpose

2 — Highest

Clarify the primary audience and reading routes

Aligns expectations with the real difficulty

3 — Highest

Give Section 4 a three-part structure: ideal process, quantum implementation, verification

Makes the central quantum innovation visible

4 — High

Separate the core classical argument from the technical direct-product reduction

Prevents the lower-bound narrative disappearing into detail

5 — High

Establish a consistent visual model for strings, addresses, cells and pointers

Reduces recurring notation and object-tracking effort

6 — High

Make proof dependencies and imported results explicit

Improves comprehension and technical credibility

7 — Medium

Move secondary examples or exceptional cases into optional passages

Keeps the main reading route shorter

8 — Medium

Strengthen the introduction and final conceptual synthesis

Makes the exposition feel like a complete explanation

9 — Medium

Add stable source, companion and formalization links

Improves independent inspectability

10 — Later

Tighten sentences, notation and formatting

Valuable, but less important than the structural work

There is a temptation to respond to the density problem by simply shortening the paper.

I would resist that.

Many of its careful distinctions are exactly what make it useful. Deleting them indiscriminately could produce a more elegant but less reliable exposition.

The better goal is to reduce the amount of information that a reader has to hold simultaneously, not necessarily to reduce the total information available.

That is why layered explanation is more promising than blunt compression.

13. A plan for the subsequent reassessments
Since you intend to ask me to reassess this repeatedly, I would make the rounds genuinely cumulative. Each should use a different intellectual standard, and later passes should be permitted to overturn earlier judgments.

01

Current pass — High-level editorial assessment

Audience fit, core narrative, educational hierarchy, central strengths and weaknesses. The question is whether the paper succeeds as an exposition at all.

02

First-time reader simulation

Go page by page as someone with the stated prerequisites but without foreknowledge of the construction. Identify every missing intuition, unexplained motivation, premature abstraction and point of likely confusion. Produce a precise map of the reader's cognitive journey.

03

Mathematical and logical dependency audit

Reconstruct the theorem-proof dependency graph independently. Examine the subtle steps: coherent sampling, expectation halving, cap enforcement, direct-product application, heavy/light conditioning, constants and quantifiers. Distinguish correctness concerns from exposition concerns. Compare with cited primary sources where possible.

04

Pedagogical redesign

Design the ideal progression of ideas. Decide which examples must precede definitions, which technical details should be optional, where diagrams would help, and how an undergraduate could reconstruct the proof with minimal unnecessary effort.

05

Specialist and skeptical-referee reading

Test whether a quantum query-complexity researcher would regard the exposition as faithful, well attributed, technically respectable and genuinely useful. Challenge the terminology, the relationship to earlier constructions and the Lean claims.

06

Sentence-level and visual editing

Review every paragraph and important equation for concision, precision, notation consistency and unnecessary cognitive load. Evaluate figures, captions, exercises and page layout. Propose actual replacements rather than abstract advice.

07

Adversarial reassessment and final editorial specification

Reconsider every major recommendation. Check which changes would genuinely help, which would sacrifice mathematical value, and which criticisms were unfair. Produce a consolidated revision specification with exact page- and section-level instructions.

In each subsequent pass, I would try to preserve the distinction between mathematical necessity, pedagogical choice and personal stylistic preference. That prevents a review from becoming an endless collection of contradictory suggestions.

14. Final assessment from this first pass
There is a distinctive quality to the paper that I would be careful not to lose.

It is trying to explain a hard research result without treating difficult technical details as things the reader should simply trust. It takes the off-promise cases seriously, makes query budgets explicit, shows why apparently simpler algorithms fail, and separates exact certification from probabilistic selection.

That is valuable mathematical writing.

The danger is that a reader comes away thinking, I followed many of the calculations, but I am not sure I could explain the main idea myself.

For an exposition, that is the most important failure mode.

The successful reader should be able to explain both the quantum and classical halves in a few minutes, then return to the paper for the rigorous proofs.

At the moment, I think the paper is stronger at supporting that second activity than enabling the first.

The single biggest improvement would be to reorganize it around the reader's understanding of the proof mechanism, rather than around the order in which the technical obligations are discharged.

That does not require less mathematics. It requires a clearer hierarchy: first the construction's essential idea, then the reasons it works, then the complications that make the argument rigorous.

My view after this initial reading is that the mathematical exposition already has excellent raw material. The next task is to make the intellectual journey as carefully designed as the individual arguments.

I would make the first-time-reader simulation the next reassessment. It is the best way to test whether my criticisms about audience calibration and conceptual overload are actually justified, rather than merely preferences about how a mathematical paper should be organized.

another pass read through

Worked for 6m 5s
Second reading — testing the exposition as an actual learning experience
Pass 2 of the 26-page paper · First-time-reader perspective

1. My assessment has changed in three important ways
After rereading the introduction, examples, proof structure and accompanying diagrams, I would correct part of my first review.

First, the paper already contains a conceptual overview of the entire proof. The introduction describes the winning column, quantum comparisons, hidden addresses, classical guessing difficulty and approximate fourth-power relationship. I was too strong in suggesting that this overview was absent.

The real problem is subtler: the overview uses objects that the intended newcomer cannot yet visualize. It is a fairly good summary for somebody who has finished reading the paper, but a demanding summary for somebody encountering these ideas for the first time. 
exposition(1).pdf

Second, the examples are more carefully engineered than I initially gave them credit for. The domain-bit board, false-pointer board, cycle of losers and fractional comparison matrix are not four loosely related illustrations. Each rules out a particular incorrect mental model. I would no longer recommend removing examples simply to reduce the number of them.

Third, the paper is better at anticipating sophisticated reader objections than most introductory expositions. It repeatedly identifies plausible mistakes and demonstrates why they fail. That is not incidental complexity: it is part of what makes the explanation trustworthy.

My revised overarching criticism is therefore:

The paper often teaches the correct distinction before the reader has had enough time to form the simpler idea that the distinction is correcting.

That creates a particular kind of cognitive burden. Readers are required to understand both a mechanism and its exception almost simultaneously.

The solution is not primarily more explanation, or less rigor. It is better sequencing.

2. What should a successful reader actually learn?
I would assess the paper against five concrete learning outcomes.

By the end, the reader should be able to explain:

Why Forrelation provides a computational asymmetry: a cheap quantum test versus a hard randomized decision problem.

How hidden addresses and certificates turn that partial-function asymmetry into a total Boolean function.

Why comparing columns permits a much cheaper quantum algorithm than verifying every candidate.

Why a classical algorithm cannot evade the hidden addresses simply by guessing where a certificate is stored.

How the two query bounds imply that the optimal universal exponent is exactly four.

The manuscript genuinely contains the material needed for all five. The problem is how much work the reader must do to assemble the answers.

A good test of the revision would be whether someone could explain these five ideas, without notes, after one careful reading. They should not need to reproduce the direct-product proof or amplitude-amplification analysis from memory.

That is the standard I am using below.

3. Pages 1–3: The reader understands the calculation before understanding why it matters
The introduction is substantively good. It tells the reader what a query costs, what randomized and quantum error bounds mean, what a total versus partial function is, and what the eventual separation accomplishes.

But the first sentence could be clearer for someone unfamiliar with complexity theory.

The phrase optimal power relating randomized and quantum query complexity is precise in context, but the universal quantifier is not yet explicit.

I would prefer an opening that says:

For every total Boolean function, randomized query complexity is at most a constant times the fourth power of quantum query complexity (allowing an additive constant). OpenAI showed that no smaller universal exponent works.

That immediately tells the reader what is surprising and what kind of theorem is being explained.

The much bigger issue is Section 1.

The paper starts the mathematical development with two sign vectors, a Walsh matrix, a correlation expression, a tiny promise threshold, and three specific eight-bit inputs.

Only later does the reader learn that these are the hidden address-generating inputs attached to the columns.

As a first-time reader, I would probably think:

I understand how to multiply the matrix, but why are we doing this calculation? What is this partial function going to do for us?

The manuscript says that the function provides hidden answers, but the connection is still abstract at this point.

A small change with large value
Before Section 1, I would show a miniature conceptual board with one column's address mechanism:


Suggested conceptual schematic for the paper, using its existing two-bit example. This would precede the detailed Forrelation calculation.
A simple explanation could then establish that each address bit is the answer to a hard partial-function instance. The quantum algorithm can obtain these answers cheaply; the classical algorithm has difficulty obtaining or guessing the entire address.

Now the Walsh-matrix calculation has a clear job.

I would keep the eight-bit computation itself. It demonstrates the quantum interference mechanism in an unusually concrete way. The progression from a signed correlation to a squared measurement probability is well handled, especially the observation that both positive and negative correlations may produce the same projection success.

The negative example 
a
−
a 
−
  is particularly valuable. The quantum experiment accepts it with certainty, but it is outside the function's promise. That is not an arbitrary technicality; it sets up the exact promise certification required by the total construction. 
exposition(1).pdf

My recommendation is therefore to add motivation before the example, not to shorten its mathematics.

4. Pages 3–7: Probably the best sustained teaching in the paper
On the second pass, I found the construction and local-verification explanations stronger than I remembered.

Figure 2 on page 5 gives the reader a proper object to inspect. The all-one column, addresses, colored certificate cells and pointers to zeros are all visibly connected.

The example achieves something important: the reader can determine why column 1 wins without trusting any asymptotic argument.

The subsequent changes then explain two possible false inferences:

A column cannot win just because its stored value bits agree with a proposed address; the inputs also have to satisfy the promise.

A stored transcript is evidence only if its local circuit equations are correct.

Page 6's explanation of transcript checking is especially good. The NOT-then-OR example demonstrates why changing a later gate value cannot make a false computation consistent if earlier values are also falsified. Somewhere a local equation must fail. 
exposition(1).pdf

This is a strong example of mathematical pedagogy because it turns a global property into something locally inspectable.

Where I would intervene
The real difficulty is that the reader must simultaneously understand:

The column's bit string.

Its separate address inputs.

The selected cell.

Its gate transcripts.

Its outward pointers.

The local tests used to verify all of them.

Each object is explained, but the working-memory burden is substantial.

I would add a compact labeled breakdown of a single certificate cell:

Stored component

What it claims

How a test checks it

Gate transcript

The hidden input has the claimed domain and value

Check a local gate equation

Domain and value outputs

The claimed address is meaningful and correct

Read the stored output bits

Pointer to rival 
j
j

Rival 
j
j contains a zero at the named location

Read the pointer and its destination

Then explain that the winner's own string is checked separately.

This table would make the later count of 
K
K local tests much easier to understand.

I would also relocate the optional census of the 180-gate toy circuit. The exact gate count demonstrates reproducibility, but it has little explanatory significance on a first reading. It belongs in a reproducibility note or appendix, with a short cross-reference.

One thing I would emphatically preserve is the statement that one query to a cell means one bit, not a whole certificate payload. That distinction is essential to the query accounting.

A deeper audience issue
These pages illustrate the paper's biggest tension.

They are written carefully enough that a beginner can follow them slowly, but they are also packed with implementation details that a specialist would largely take for granted.

That makes them somewhat long for an expert and somewhat demanding for a newcomer.

A more explicit learning hierarchy—first understand what a certificate says, then understand why it can be checked locally, then count its tests—would serve both audiences.

5. Pages 7–8: The theorem statement is well placed, but the reader needs a parameter map
I previously suggested that the main theorem arrives too late. On closer reading, I would retract that as a general criticism.

The theorem is stated on page 8, before either of the two major algorithmic arguments begins. That is a sensible location.

The paper also responsibly identifies the classical Forrelation lower bound as an imported result, and it shows why the complete input length is polynomial in the column parameter despite the many addressed cells.

Where I think this section needs improvement is the meaning of the parameters.

The paper moves from the hand-checkable example 
m
=
4
m=4, 
k
=
2
k=2, 
r
=
2
r=2 to the asymptotic family with

m
=
4
t
,
r
=
20
log
⁡
2
m
,
2
r
=
m
20
.
m=4 
t
 ,r=20log 
2
​
 m,2 
r
 =m 
20
 .
The toy board is explicitly not an instance of the final hardness theorem. The manuscript says this, correctly.

But a first-time reader may still wonder why the construction uses so many cells, why 
r
r grows logarithmically, why the circuit must have near-linear size, and why 
k
k must eventually be fixed.

I would add a short design-rationale paragraph before the theorem:

The number of address bits must be large enough to make guessing an entire address very unlikely, but small enough that the complete input stays polynomial in the number of columns. The exact verification circuit must be efficient enough that quantum search over its local tests remains cheap. The Forrelation parameter controls how close the classical lower bound comes to 
m
m per address instance.

That explains the parameter choices as engineering constraints serving the proof, rather than numbers introduced because they happen to make the algebra work.

The theorem itself is then much easier to appreciate.

6. Pages 8–15: The quantum argument is the intellectual centerpiece
I think this section is the strongest candidate for a significant pedagogical improvement.

Not because the mathematics is badly presented, but because an exceptionally elegant argument is embedded in a long implementation narrative.

The crucial insight the reader must retain
The standard approach—searching over columns and fully checking each one—is too expensive.

The better approach is to perform cheap comparisons, retain a short list of candidates, and verify them afterwards.

The manuscript explains this very well at the beginning of Section 4. It correctly contrasts a nested cost, roughly 
m
K
m
​
  
K
​
 , with separate tournament and verification costs. That is one of the clearest explanations of why the new method is necessary. 
exposition(1).pdf

I would make that contrast the central organizing principle for the section.

The real algorithmic argument then has three conceptual steps.

Step A — The comparison structure

A true winner beats any rival with probability at least 
1
−
ε
1−ε. Losers may behave arbitrarily, including forming cycles.

Step B — The weighted tournament

Sampling pivots according to their probability of beating earlier pivots reduces expected total weight by at least half per stage, while a true winner retains substantial weight.

Step C — Quantum implementation and verification

Coherent comparisons and amplitude amplification realize that sampling process efficiently. Exact checking then distinguishes genuine winners from misleading candidates.

These steps are present in the paper. But I would make them three explicit subsections, with the essential conclusion visible before the calculations.

The cycle example is particularly effective
Page 10's diagram makes it clear that three losing columns can form a cycle, even while the genuine winner beats all three.

This shows why the problem cannot simply be reduced to sorting the columns or finding a minimum in an underlying order.

I now think this example should unquestionably remain in the main text.

The point is deeper than nontransitivity. The comparison between two losing columns may itself be probabilistic without a stable correct direction. The manuscript explains why simply repeating an unreliable comparison does not necessarily create a correct comparison bit. 
exposition(1).pdf

That is a genuinely important distinction.

The halving calculation deserves more prominence
On page 11, the paper derives

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
This is the most elegant piece of the quantum argument.

What I like about it is that the inequality needs almost nothing about the losing columns. It uses the pairwise identity 
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
 =1.

That gives the argument unusual robustness.

The reader should have a short explanation immediately after the calculation:

The tournament does not need to know which losing column is better. Even if all comparisons among losers are inconsistent, their contributions cancel pairwise in the expectation calculation.

That is the kind of insight a reader can remember and explain.

The main difficulty begins when probability becomes quantum implementation
At the bottom of page 11, the manuscript changes from an ideal stochastic process to a coherent reversible implementation.

This is probably the largest single change of mathematical perspective in the paper.

Suddenly the reader needs to reason about retained workspaces, unitary reversibility, tensor products, conditional distributions and uncomputation.

The exposition is technically careful about all of these.

In fact, the derivation on page 12 is excellent in one respect: it explicitly explains why independent fresh comparison registers cause the success probabilities to multiply, and why orthogonal column labels cause the probability masses to add.

The resulting identity

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
 
is the bridge between the hypothetical weighted tournament and the implementable algorithm. 
exposition(1).pdf

But the bridge deserves to be announced.

I would insert a paragraph saying:

So far, the weights have existed only in our analysis. The quantum algorithm does not calculate them or store them. Instead, it prepares a superposition of columns, independently performs the comparisons against the previous pivots, and selects the branches in which every comparison succeeds. Conditional on this event, the observed label automatically has exactly the desired weighted distribution.

Then derive the equation.

That one paragraph would make page 12 much easier to read.

The amplitude-amplification explanation is strong but arrives at a difficult moment
Page 13 explains the good/bad decomposition and the two-dimensional rotation, rather than treating amplitude amplification as a magical black box.

For the stated linear-algebra audience, that is a good decision.

However, the reader is now simultaneously learning the reason for amplitude amplification, its matrix representation, its behavior under unknown success probability, and its preservation of conditional label distributions.

I would explicitly distinguish two questions:

Why amplify? Because the chance of producing a successful pivot can be small.

Why is amplification safe? Because the good component is multiplied by a scalar without changing the relative distribution of labels inside it.

That second point is mathematically central. The paper gives a correct-looking, carefully developed explanation, but the reader can lose the purpose of the rotation calculation.

I would retain the calculation and place those two questions immediately before it.

7. Pages 15–20: The classical proof is clearer when approached backwards
On this reading, I found that the planted-pair argument has a stronger intuitive foundation than the quantum implementation.

The construction of 
Y
0
Y 
0
  and 
Y
1
Y 
1
  gives an excellent starting point. A nonwinning input is modified by erasing one zero and filling one hidden certificate cell. The function's answer changes, while nearly all input bits remain identical.

That is tangible.

Figure 4 is particularly successful: the changed positions are visible to the reader but hidden from the decision-tree algorithm.

This naturally gives the lower bound a physical interpretation: an algorithm must somehow query a location where the two boards differ.

The essential distinction: computing an address versus guessing one
The most important subtlety in the classical proof is that an algorithm might reach the correct certificate cell without calculating the address bits.

This is exactly the sort of gap that a rigorous exposition must address.

I would make it the main conceptual question of Section 5:

Why can't the classical algorithm simply guess the winning cell?

The answer is that a query to a certificate cell reveals, through its chosen coordinate, a proposed address for all 
r
r hidden partial-function answers. A successful true-cell visit therefore becomes an address prediction.

The proof constructs a capped simulator to exploit that observation.

The manuscript explains this carefully on pages 17–19. 
exposition(1).pdf

I would nevertheless move the informal explanation forward, closer to the planted-pair figure.

This would give the reader a clear reason to care about the later direct-product lemma.

The three-charge table is excellent
I would not replace it with a long prose explanation.

It gives a clean decomposition of the possibilities:

Pr
⁡
(
distinguish
)
≤
4
G
m
2
+
G
m
L
+
G
(
2
/
3
)
r
.
Pr(distinguish)≤ 
m 
2
 
4G
​
 + 
mL
G
​
 +G(2/3) 
r
 .
Every term corresponds to a recognizable strategy.

The first is finding the zero. The second is concentrating too many queries on the planted column's address inputs. The third is visiting its correct cell without exceeding the light-column budget.

The paper then proves these individually.

This is a good proof structure.

Where the difficulty becomes excessive for the stated audience
The simulator on page 18 has two clocks, a query counter, an abort rule, side information, a target time, a default output and a direct-product guarantee with per-instance caps.

These are all necessary to make the reduction precise.

But a reader with only introductory probability and linear algebra may find this overwhelmingly difficult, even after understanding the planted-pair idea.

My recommendation is not to suppress the simulator. Instead, explain what it accomplishes before giving its exact algorithm.

Something like:

Suppose the original algorithm reaches a true cell while having made at most 
L
L address-input queries to that column over its entire run. We can turn that event into the success of a new algorithm that predicts every hidden address bit while obeying a strict query cap. The direct-product theorem says that this cannot happen often. We now construct that algorithm carefully.

Then give the existing simulator.

I would also preserve the paper's important warning about conditioning on the light event. The counterexample on page 18 is useful precisely because it shows that conditioning on a cheap run can make success look deceptively likely.

That is not merely defensive writing; it teaches a transferable idea about probabilistic reductions.

A change to the examples
The XOR trace on page 19 is informative, but I would introduce it as an optional fully worked simulator trace.

The essential argument already exists without it.

For a reader pursuing full mastery, the example provides an excellent check. For a reader primarily trying to understand the separation, it is another temporary change of function and notation after a very long technical development.

Making the trace clearly optional would retain its value without making it feel like another prerequisite to finishing the theorem.

8. Pages 20–24: The ending is more rigorous than emotionally satisfying
Section 6's treatment of the order of quantifiers is strong.

It explicitly fixes the target exponent 
α
<
4
α<4, chooses an appropriate fixed 
k
k, and then lets 
m
m grow.

This avoids a common asymptotic mistake: allowing a hidden constant that depends on 
k
k to be treated as if it remained uniform while 
k
k grows.

The distinction between proving that the optimal universal exponent is four and constructing a single growing-
k
k family is also handled responsibly.

I would keep that clarification.

But after this demanding calculation, I want a concise conceptual ending.

The paper needs to say, in one paragraph, that the quantum algorithm wins by replacing repeated expensive certification with cheap elimination, while the classical algorithm is obstructed by hidden certificate addresses. Forrelation supplies the strong asymmetry needed for the exponent.

That conclusion would connect the proof back to the title.

The Lean section
My first review was too negative about the source trail.

I inspected the PDF's embedded hyperlinks. It already contains commit-pinned GitHub links to the reasoning record, expert companion, Lean challenge, proof files and original OpenAI preprint. That is much better than I initially appreciated.

The issue is discoverability, not the absence of links.

A concise source map near the introduction would be useful, but this is lower priority than the mathematical teaching.

Section 7 itself is careful about verification scope, particularly its distinction between formal theorems and the informal correspondence of definitions to intended mathematical objects. I would retain that distinction. 
exposition(1).pdf

The exercises and answers are also a strength. The combined-explanation exercise is ambitious, but appropriate for a reader who has studied the proof rather than merely skimmed it.

9. The most consequential revisions after this reading
My priorities are now more specific than in the first review.

Change

Importance

Scope

Give the reader a visual model of addresses and certificate cells before introducing Forrelation

Very high

Intro / §1

Explain why the address length, circuit size and number of columns have their chosen scales

High

§2–3

Introduce the ideal tournament as a distinct mathematical insight

Very high

§4

Announce the exact weighted-sampling law before deriving its quantum implementation

Very high

§4

State that the classical problem is controlling successful address guesses, not just computing addresses

Very high

§5

Mark some technical counterexamples and simulator traces as optional

Medium

§4–5

Give the proof a short conceptual conclusion before the Lean section

High

§6

Make the existing linked evidence easier to navigate

Low–medium

Intro / §7

I would also fix a small but noticeable typesetting problem: Section 2 begins at the bottom of page 3, and its opening sentence continues onto page 4. Starting it on a new page would give the four-column construction a clearer entrance.

There are two things I would not do.

I would not turn this into a superficial popular-science explanation. The explicit query model, off-promise cases, local tests and capped algorithms are part of the paper's intellectual value.

And I would not aggressively shorten the full proof. The reader who wants all the details should be able to obtain them here. The goal is to create a more navigable main route through the details.

10. Revised judgment
My judgment is slightly more favorable than before.

As a serious, proof-oriented self-study exposition

8.3/10
Strong
For a newcomer with only the advertised prerequisites

6.5/10
I now think the paper has more pedagogical discipline than my original review recognized. Its examples are purposeful, its explanations frequently anticipate genuine pitfalls, and the central quantum and classical arguments are carefully distinguished.

But the audience mismatch remains real.

The introduction promises accessibility to someone with finite-dimensional linear algebra, elementary probability and asymptotic notation. In practice, the paper demands substantial comfort with long mathematical arguments, quantum circuit reasoning and adaptive probabilistic reductions.

It is very good at teaching individual mechanisms. It is less good at controlling the accumulation of concepts over twenty pages.

My strongest new conclusion is that this is not primarily a prose problem. It is a problem of conceptual pacing.

The paper has already solved much of the difficult problem of making the proof exact and inspectable. The remaining editorial challenge is to make the main insight stay continuously visible while the technical machinery is developed.

For the next reassessment, I would switch standards entirely: stop reading as a learner and read as a skeptical quantum query-complexity specialist. I would scrutinize whether the stated lemmas, technical reductions, cost accounting, citations and formal-verification claims are precise enough to survive expert examination, independently of how well they teach. That is where a genuinely new third pass is most likely to uncover issues this pedagogical reading has missed.

again another pass

Worked for 4m 39s

Third reading — a skeptical specialist's assessment
Pass 3 · Mathematical credibility, proof architecture, technical precision and expert presentation

1. The main verdict
The exposition is stronger technically than its accessibility problems might suggest. On this pass, I compared its principal arguments against OpenAI's original October 2026 manuscript and checked the mathematical dependencies underlying the more delicate reductions.

My provisional findings are:

The construction, probabilistic tournament and planted-pair lower bound closely follow the original result. They are not merely informal analogies.

The exposition pays unusual attention to exact worst-case query caps, off-promise behavior, coherent quantum workspaces and adaptive classical algorithms. These are precisely the details an expert would look for.

Its distinction between a formally verified statement and a mathematically faithful formalization is important and appropriate.

Nevertheless, it sometimes makes the expert reader reconstruct the theorem–lemma structure from paragraphs that should be stated as explicit propositions.

The strongest remaining concerns are about the visibility of assumptions, the traceability of quantitative bounds and the evidence supporting the formal-verification claims.

I have not found a decisive mathematical error in the main separation argument during this pass so far. That is not equivalent to a complete independent proof verification, and I would not present it as one.

Importantly, the original OpenAI manuscript really does use an addressed certificate construction, outward pointers, probabilistic comparisons, a weighted tournament and a planted-pair argument. These are not speculative reinterpretations by the exposition. 

github.com
+1

2. A specialist's first question: what exactly is the contribution?
The opening credits the theorem and construction to OpenAI, and describes this paper's contribution as explanation and accompanying Lean development. That is an appropriate distinction. 
exposition(1).pdf

But I think an expert still needs a clearer answer to a further question:

What can I obtain from this exposition that I cannot obtain from reading the original manuscript?

At present, the answer is distributed across the work.

The valuable additions include the hand-computable Forrelation inputs, concrete false certificates and cyclic loser comparisons, explicit sampling examples, a worked simulator trace, exercises, and connections to checked formal statements.

These constitute a substantial educational contribution.

I would make that contribution explicit in the introduction:

This exposition reconstructs the separation using hand-checkable examples of the mechanisms that matter most: promise certification, nontransitive comparisons, coherent weighted sampling and adaptive guesses of hidden addresses. The aim is to make the proof reproducible by a reader rather than to introduce a different construction.

That establishes a useful identity for the paper without overclaiming originality.

One more distinction matters here. The source manuscript itself contains a fairly detailed explanation of the same construction and its analyses. Consequently, an expert may regard this exposition as an expanded teaching companion rather than a substantially new proof.

That is not a weakness, provided the manuscript presents itself that way.

I would avoid suggesting that an independent reconstruction alone implies independent mathematical validation of the original result.

3. Technical audit: which arguments withstand closer scrutiny?
I concentrated on the points where a specialist would be most concerned about a hidden change of model, an unjustified probability calculation or a missing hypothesis.

Location

What I checked

Assessment

pp. 2–3

Eight-bit Forrelation examples and projection probabilities

Arithmetic checks out

pp. 4–6

Winner conditions, false certificates and local tests

Definitions and explanations consistent

pp. 7–8

Forrelation hardness, circuit-size role and family bounds

Consistent with the original manuscript; quantitative inputs depend on cited results

pp. 9–11

Noisy comparisons, loser cycles and expected weight halving

Core identities check out

pp. 11–14

Coherent weighted sampling and amplitude amplification

Mechanism consistent with the source; implementation assumptions important

pp. 15–19

Planted pair, erased-zero probability and adaptive address guessing

Reductions match the original proof structure

pp. 20–21

Floors, fixed-
k
k quantifiers and optimal exponent

Algebra and logical structure check out

p. 21

Lean statement equivalence and checking scope

Claims are carefully delimited, but evidence remains separately auditable

3.1 Forrelation: the small calculations are sound
I independently recalculated the three eight-bit examples from page 2 and the projection exercise.

Input

Signed value 
Φ
Φ

Projection probability 
Φ
2
Φ 
2
 

a
+
a 
+
 

1
1

1
1

a
0
a 
0
 

0
0

0
0

a
−
a 
−
 

−
1
−1

1
1

Exercise input 1111 1000

1
/
2
1/2

1
/
4
1/4

These agree with the manuscript.

The example establishes precisely the issue it is intended to establish: measuring the squared correlation does not tell the algorithm whether the signed correlation is large and positive or large and negative.

The promise therefore matters. So does exact certification once the partial function is incorporated into the total construction.

There is a further technical detail worth making explicit to specialists: the exposition uses 
k
k queries for its straightforward Forrelation projection experiment, while the literature also discusses implementations with approximately 
k
/
2
k/2 quantum queries. This is not a problem. For fixed 
k
k, the simpler 
k
k-query implementation is sufficient.

I would add one sentence saying that the exposition chooses the simpler implementation because optimizing the constant dependence on 
k
k is unnecessary for its separation theorem.

The cited Bansal–Sinha work does establish the relevant near-
m
1
−
1
/
k
m 
1−1/k
  randomized lower-bound scale. The original OpenAI manuscript explicitly applies it to the same normalization and promise thresholds used here. 

eccc.weizmann.ac.il
+1

A complete audit of that imported analytic result is separate from checking that the exposition has stated and used it consistently.

3.2 The probabilistic tournament is the strongest expert-level component
The most mathematically interesting general statement is not merely that a genuine winner beats every rival.

It is that the tournament algorithm works even when comparisons between losing columns have arbitrary, potentially cyclic and probabilistic outcomes.

The condition

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
0
a 
ij
​
 +a 
ji
​
 =1,a 
ii
​
 =0
is remarkably weak.

The ideal weight process then gives

E
[
W
t
+
1
∣
w
t
]
=
W
t
2
−
∑
i
w
t
,
i
2
2
W
t
≤
W
t
2
.
E[W 
t+1
​
 ∣w 
t
​
 ]= 
2W 
t
​
 
W 
t
2
​
 −∑ 
i
​
 w 
t,i
2
​
 
​
 ≤ 
2
W 
t
​
 
​
 .
I checked this calculation and its consequence for the four-column cyclic example. The expected remaining weight of 
3
/
2
3/2 from an initial weight of 
4
4 is correct.

The fractional example on page 12 also checks out. After pivot 2, the conditional label distribution is

(
12
23
,
0
,
8
23
,
3
23
)
.
( 
23
12
​
 ,0, 
23
8
​
 , 
23
3
​
 ).
After additionally selecting pivot 4, it becomes

(
15
19
,
0
,
4
19
,
0
)
.
( 
19
15
​
 ,0, 
19
4
​
 ,0).
The manuscript's arithmetic is correct in both cases. 
exposition(1).pdf

Specialist recommendation: Elevate the probabilistic tournament to a named proposition.

It should have explicit hypotheses about the comparison circuit, the worst-case cost per comparison, complementarity of pairwise probabilities, the reliability of one distinguished winner, and the probability that the output list contains that winner.

The original manuscript does precisely this in its Proposition 3.2. 

github.com

Your exposition spreads those assumptions throughout the discussion. That is reasonable for teaching, but a formal proposition would make it much easier for an expert to verify that no hypothesis has silently changed between the ideal process and the quantum implementation.

3.3 Quantum sampling: one distinction must remain explicit
The critical sampling equation is

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
.
Pr(success and label i)= 
m
w 
i
​
 
​
 .
The exposition derives this from independent comparison workspaces and a uniform superposition over candidate labels.

The specialist needs three things to be true:

Each comparison against a previous pivot is prepared using fresh workspace.

The workspace is retained coherently, so the full preparation has an inverse.

Amplitude amplification preserves the relative distribution of labels in the successful component.

The manuscript addresses all three. That is a major strength.

I also checked the two-dimensional rotation on page 13. The displayed reflection matrices and the resulting 
sin
⁡
(
(
2
v
+
1
)
θ
)
sin((2v+1)θ) success amplitude are consistent.

The important distinction is that amplification does not estimate the weights and does not need to know them. It changes the total probability of observing a successful branch without changing the label law conditional on success.

I would give that fact a named lemma or an explicitly labeled consequence of amplitude amplification.

For an expert, this is the bridge from a hypothetical stochastic algorithm to an actual quantum procedure. It deserves to be directly inspectable.

3.4 Classical hardness: the separate-cap lemma is appropriately handled
The central technical risk in Section 5 is an illicit change of distribution when conditioning on a low-query event.

The manuscript avoids that by constructing a capped simulator and bounding the joint event that a column is light and its true cell is visited.

That is the right approach.

The direct-product lemma is supported by the conditional-value/supermartingale method associated with Drucker, building on Shaltiel's work. The original paper uses essentially the same argument. 

pure.ed.ac.uk
+1

I particularly approve of the paper's insistence that the side information must be jointly independent of the entire tuple of hidden inputs, rather than separately independent of each coordinate.

That is a precise and important hypothesis.

The distinction between global query time, total queries forwarded to the selected column, and per-instance caps is also genuine. It should not be simplified away.

My main criticism is presentation: the direct-product lemma on page 18 should be stated as a formal theorem-like object, independently of the simulator application that follows.

It is useful mathematical content in its own right, and doing so would make the logic easier to audit.

4. The strongest remaining concern: formal-verification evidence
I also inspected the commit-pinned Lean sources linked from Section 7, rather than relying exclusively on the PDF's description of them.

This produced an important distinction.

The challenge file contains the four formal statements with intentional sorry placeholders. The separate solution file supplies proofs referencing the maintained development. That matches the manuscript's explanation; the placeholders in the challenge are not, by themselves, evidence of unfinished verification.

The maintained source also contains the substantive result dependencies, including an unconditional Forrelation lower-bound theorem and the family construction. The project's reasoning record reports successful compilation and axiom audits.

However, I have not independently reproduced those builds or audited the complete theorem dependency closure. The available source and recorded checks are evidence, not a substitute for that final independent verification.

A concrete repository presentation problem
The linked ConstructionFamily.lean still begins with a comment saying the file was unelaborated because Lean was unavailable in the original authoring environment.

Your reasoning record explicitly explains that this is historical and was superseded by recorded builds and axiom audits. The exposition also distinguishes the named-circuit theorem from the four-theorem comparison bundle. 
exposition(1).pdf

So this is not an established contradiction in the verification claims.

It is nevertheless an avoidable credibility problem. A skeptical researcher who follows the source link may see unelaborated and conclude that the manuscript has overstated its evidence before discovering the later explanation.

I would update the source comment in a new revision to state the present verification status and link directly to the applicable build and axiom-audit receipts.

More generally, I would give Section 7 a compact verification-status table:

Claim

Evidence

Important boundary

Four headline formal statements

Compiled proofs and recorded Comparator checks

Matching statements does not establish intended semantics

Named-circuit bound with logarithmic exponent six

Recorded build and axiom audit

Not in the four-theorem comparison bundle

Small-board and circuit computations

Archived computational checks

Not a formal proof of every explanatory paragraph

Connection between Lean definitions and standard query models

Mathematical correspondence arguments

Requires separate semantic review

This is much clearer than making an expert recover the distinction through links.

The most important lesson is not to maximize the apparent number of verified claims. It is to make the precise scope of the verification almost impossible to misunderstand.

5. A genuine omission from the literature discussion
The historical discussion is mostly accurate, but it misses two particularly relevant 2026 papers.

Both are also mentioned in OpenAI's original manuscript.

They are:

Randomized query complexity can beat certificate complexity — Ben-David and Kothari, 2026. 

arxiv.org
+1

A Near-Quartic Separation Between Certificate Complexity and Quantum Query Complexity — Ambainis, Iraids and Kokainis, 2026. 

arxiv.org

These results concern certificate complexity, rather than the randomized-versus-quantum separation established in the manuscript under review.

That distinction is essential.

But the papers are closely related through their use of candidate comparisons and efficient witness identification.

An expert reading your exposition's discussion of pointer functions, cheat sheets and tournaments would reasonably expect these references to appear.

I would add a short paragraph near the historical discussion on page 5 or Appendix A.2 explaining that comparison-based witness selection also appears in these related 2026 constructions, while explicitly distinguishing the complexity measures.

This is a targeted addition, not an invitation to expand the entire literature review.

6. The quantitative proof needs a more inspectable statement hierarchy
The original research paper presents its crucial claims as named lemmas and propositions.

Your exposition often prefers descriptive paragraphs, followed by equations and detailed explanations.

For teaching, that can be effective.

For a skeptical specialist, it makes cross-checking more laborious.

I would introduce four particularly useful formal statements, without necessarily changing their proofs.

Proposition A: Local certification. Every candidate address has a fixed family of local tests, all passing exactly when that candidate wins, with the stated maximum bit-query cost per test.

Proposition B: Probabilistic tournament. A reversible comparison circuit satisfying complementarity and reliably favoring one distinguished candidate yields a short list containing that candidate with high probability.

Lemma C: Separate-cap direct product. Independent hard address instances remain exponentially difficult to solve jointly under adaptive interleaving, provided each instance has its own cap and side information is jointly independent.

Proposition D: Planted-pair indistinguishability. Any 
G
G-query classical algorithm has distinguishing advantage at most

4
G
m
2
+
G
m
L
+
G
(
2
/
3
)
r
.
m 
2
 
4G
​
 + 
mL
G
​
 +G(2/3) 
r
 .
These statements are already proved or developed in the exposition.

The purpose of naming them is to make the proof's architecture explicit.

A specialist could then inspect Proposition B without having to extract its hypotheses from six pages of pedagogical development.

The same-circuit issue deserves prominence
One particularly good feature is the insistence that the randomized lower bound and quantum upper bound apply to the same total function and the same exact circuit construction.

This is fundamental to the claim.

An upper bound for a family constructed using one circuit and a lower bound for a different family would not suffice.

Your manuscript emphasizes this near the end of the classical argument, and the formal family statement explicitly retains the circuit witness.

I would promote this to a sentence immediately following the main theorem:

Both inequalities concern the same total Boolean function, including the same exact circuit used to encode its certificates.

That is a modest change that addresses a natural expert concern.

7. Quantitative accounting: correct scale, but explain what is sharp
The stated quantum upper bound is

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
(
log
⁡
2
m
)
6
.
Q(F 
k,m
​
 )≤C 
k
​
  
m
​
 (log 
2
​
 m) 
6
 .
The paper explicitly says that the logarithmic exponent six is loose. It gives the underlying count in Appendix A.1.

I checked the leading dependencies.

With 
ℓ
=
log
⁡
2
m
ℓ=log 
2
​
 m, the manuscript has approximately

r
,
T
=
O
(
ℓ
)
,
K
=
O
k
(
m
ℓ
3
)
.
r,T=O(ℓ),K=O 
k
​
 (mℓ 
3
 ).
Consequently, the tournament and verification contributions both have leading 
m
m
​
  dependence, with additional logarithmic factors. The deliberately loosened exponent six is consistent with that accounting.

This is exactly what the proof needs.

For expert presentation, however, I would separate three statements:

The 
m
m
​
  dependence is the crucial algorithmic achievement.

The exponent six is a convenient bound from this reconstruction, not a claimed optimal logarithmic exponent.

The upper-bound construction and its cost are independent of the input's satisfying any Forrelation promise, although the decoding guarantee is only required on promised instances.

The paper says these things in different places. Consolidating them would make the quantitative claim easier to judge.

There is no need to optimize logarithmic factors unless the paper is also claiming a quantitative advance over the original result.

8. The asymptotic conclusion is rigorous, but distinguish two notions of optimality
The manuscript correctly proves that for each 
α
<
4
α<4, one can choose a fixed 
k
k for which the ratio

R
(
F
k
,
m
)
(
1
+
Q
(
F
k
,
m
)
)
α
(1+Q(F 
k,m
​
 )) 
α
 
R(F 
k,m
​
 )
​
 
diverges as 
m
m grows.

That establishes that no universal exponent smaller than four can work.

The matching universal upper bound completes the argument.

The paper also correctly notes that choosing 
k
k as a function of 
m
m is a separate quantitative question, because the constants in the fixed-
k
k estimates may depend on 
k
k. 
exposition(1).pdf

I would preserve that distinction absolutely.

In fact, this is another place where the exposition is stronger than an abbreviated research summary might be. It does not confuse a sequence of fixed-parameter separations with a uniform asymptotic family.

For an expert, the distinction is not pedantry. It is an essential part of what exactly has been proved.

9. What a skeptical referee would most likely request
After this third reading, my prioritized technical revision requests would be:

Priority

Request

Reason

Essential

State the tournament and direct-product results as named propositions with complete hypotheses

Makes the two most delicate mechanisms independently auditable

Essential

Make the exact scope of Lean compilation, Comparator checking and mathematical correspondence explicit

Prevents verification evidence being overstated or misunderstood

High

Update stale formal-source status comments

Prevents the repository from undermining its own recorded evidence

High

Cite the two closely related 2026 comparison-based papers

Improves historical and technical completeness

High

Identify which quantitative constants are reconstructed and deliberately loose

Avoids suggesting unintended optimization claims

Medium

Promote the same-circuit assertion into the theorem discussion

Makes a critical logical requirement unmistakable

Medium

Make the original preprint's persistent source location visible in the bibliography

Improves inspectability without depending on hidden PDF hyperlinks

Medium

Clearly label which sections are explanations of existing results and which contain additional worked constructions

Clarifies the exposition's scholarly contribution

I would not recommend rewriting the proof wholesale, weakening the technical details or replacing the classical simulator with a hand-waving summary.

Those would make the paper less defensible.

10. What this changes about my assessment
I now think the intended audience should be defined slightly more narrowly:

Mathematically mature undergraduates, beginning graduate students and researchers in theoretical computer science who want a detailed guided reconstruction of the result.

For that audience, this is substantially better than a 7/10 paper.

My provisional ratings after three passes are:

Dimension

Rating

Mathematical exposition for a motivated specialist reader

8.5/10

Fidelity to the original proof architecture

9/10

Technical transparency

8.5/10

Standalone inspectability

7.5/10

Accessibility at exactly the advertised prerequisites

6.5/10

Overall effectiveness for its best-fitting audience

8–8.5/10

These are not ratings of independently established theorem correctness.

The key change from the first two assessments is that I no longer regard excessive technical detail itself as one of the manuscript's main weaknesses.

Many of the details are precisely those that establish credibility for an expert audience.

I also now think the paper would benefit more from a small number of carefully chosen theorem statements and explanatory signposts than from a radical structural rewrite.

The central editorial tension
There are two different papers competing within the current manuscript.

One is an examples-first exposition intended to make a difficult result accessible to readers with relatively modest prerequisites.

The other is a mathematically detailed companion intended to let serious readers reconstruct an advanced research proof and inspect its evidence.

Both are valuable, but they demand slightly different presentation strategies.

The strongest version would retain one manuscript while making the two reading routes visibly distinct:

The main route develops the construction, central algorithmic insights and final separation.

The detailed route supplies the precise quantum implementation, direct-product reduction, quantitative bookkeeping and verification evidence.

In other words, the technical content should remain, but the reader should know which parts are conceptual milestones and which parts discharge the rigorous obligations.

11. What I would examine on the fourth pass
We have now examined the paper from three distinct perspectives: overall editorial effectiveness, first-time-reader learning, and skeptical specialist scrutiny.

The next useful pass should be a pedagogical redesign, but I would not begin by simply changing the section order.

I would first construct a dependency map of every concept, showing exactly what must be understood before another concept can be introduced.

Then I would test alternative routes through the existing examples, especially whether the four-column board should precede the first Forrelation calculation, how the tournament should be introduced, and when the classical address-guessing problem should be revealed.

The aim would be an exact revision plan: which paragraphs to move, which transitions to rewrite, which explanations to shorten, which diagrams to add, and what should remain untouched.

My conclusion from this third pass: The paper has a credible, careful technical core. Its strongest opportunity is not to become more mathematically impressive, but to make the mathematical structure and the significance of its mechanisms immediately legible to the people most qualified to appreciate them.




