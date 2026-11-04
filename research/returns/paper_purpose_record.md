

reasoning_record(5).pdf
PDF
Okay, so read attached. Obviously this comes with a repo and a website, whatever. This is just the PDF. We don't have to worry about, like, oh, the source and the hashes and that bullshit. It's just purely the reading experience for a mathematical reader, for the target audience for this. For that, can you please give feedback on, you know, the paper? Like, how is the paper? Can you just give it a review? Let us know, like, how good is it? Just how good is it? And please, yeah, give us feedback.


Revised all three with clearer explanations, stronger examples and cleaner navigation. Hashes, code paths and verification history now sit behind the readable theorem index.


Specialist companion — 18 pages


Exposition — 27 pages


Complete reconstruction — 94 pages, down from 141, with the mathematical proofs retained.


Rendered pages and links checked; 267 tests completed with two skips and no failures. Changes pushed, and the writing-method improvements merged upstream.

…
Review: OpenAI’s nearly quartic query separation — a complete proof reconstruction
My overall assessment: this is a good, mathematically serious reconstruction. It is substantially stronger as a technical reference than as a continuous reading experience.

The paper has a real mathematical argument, an intelligible structure, and unusually careful explanations of several difficult proof steps. It doesn't merely reproduce theorem statements and bury the actual reasoning behind citations. In particular, the quantum tournament, the planted classical lower bound, and the analytic Forrelation argument receive substantive explanations.

But I don't think it is yet an excellent piece of mathematical exposition. Its principal weakness is that it asks the reader to maintain too many definitions, technical qualifications, parameter choices, and subsidiary arguments simultaneously.

My assessment of the attached 94-page PDF

Editorial judgement, not proof certification

Technical reconstruction

8.5/10

Mathematical precision of presentation

9/10

Explanatory insight

7.5/10

Organisation and navigation

7/10

Continuous readability

6.5/10

These scores concern the quality of the mathematical writing and organisation, not an independent certification that every proof is correct.

The important distinction is that 94 pages is not inherently too long for a complete reconstruction. The length is defensible. What matters is whether those pages make the mathematics easier to follow. Some sections demonstrably do; others make the reader work harder than necessary.

I would take the document seriously as a specialist reference or companion monograph. I would not yet recommend that a new reader start on page 1 and read every page in sequence. The strongest next revision should make the existing mathematics easier to absorb, not simply remove detail.

1. What the paper does particularly well
The central arguments are actually explained
This is its greatest strength.

In §5.2, pp. 24–29, the probabilistic tournament is handled well. The paper doesn't simply announce that a quantum procedure can find the winner. It develops the weights, derives

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
,
E[W 
new
​
 ∣w]≤ 
2
W
​
 ,
then explains why a dominant candidate retains weight, how amplification reproduces the correct conditional sampling distribution, and how the real process is coupled to the ideal process.

That's good mathematical writing. The reader can see how the argument works, rather than just accepting the theorem.

The four-candidate cyclic example on p. 27 is particularly valuable. It demonstrates why the result doesn't require comparisons to produce a consistent ordering. It's an example that addresses a genuine conceptual difficulty.

The classical lower bound has comparable strengths. On pp. 49–54, the coupling between the dummy and planted inputs is presented concretely. The argument identifies the two places at which the inputs can first differ, and §6.5 explains the capped simulator rather than treating the direct-product invocation as magic.

The distinction between a joint probability bound and an invalid conditional probability bound is also handled carefully. That's exactly the kind of subtle point where a mathematical reconstruction can contribute something useful to a reader.

These are strong sections. I would preserve their mathematical substance.

The paper understands which technical distinctions really matter
The discussion of promise membership versus a quantum decoder's output is a good example.

On pp. 16–17 and again on p. 67, the negative-Forrelation examples demonstrate that a quantum projection test can give a large acceptance probability even when the input is outside the promise.

That isn't a decorative example. It explains why an exact domain certificate is necessary.

Similarly, the explanation of retained workspaces and the exact conditional label law in §5 distinguishes two notions that can easily be conflated.

The paper is good at identifying these mathematical traps and explaining how the proof avoids them.

The analytic reconstruction is a substantial piece of exposition
I particularly like the architecture of §§8.5–8.14.

The paper moves from a rounded Gaussian construction through interpolation, integration by parts, a path-derivative identity, and a decision-tree martingale estimate. It then obtains a quantitative indistinguishability estimate and finally turns that into a lower bound for the promised problem.

The three-block calculation on pp. 73–74 is a strong choice. Rather than leaping straight into the general 
k
k-block identity (F22), it shows the derivative moving through a small number of blocks.

And the degree-two example on p. 76 helps explain the contracted coefficient arrays in the martingale argument.

These examples make the technical mathematics more credible and understandable.

The major achievement of the reconstruction, as writing, is that the Forrelation lower bound is no longer an opaque black box.

2. The main weakness: too much explanation without enough hierarchy
This is the issue I would prioritise above everything else.

The document frequently gives the reader all the information needed to understand a step, but doesn't always distinguish the crucial idea from the details required to formalise or quantify it.

Consider §5.2 on p. 24.

The proposition states the comparison interface, the parameters, the dominant-vertex definition, the algorithm, and its guarantee. Then the text starts again by fixing the comparison model, describing its orientation and probabilities, explaining its relation to earlier procedures, and restating the parameters.

None of those explanations is unreasonable individually.

But the reader has effectively encountered the same setup several times before reaching the principal argument.

A stronger mathematical exposition would give the theorem once, explain the core insight, and then prove it.

The same pattern appears elsewhere: important definitions are restated, then qualified, then compared with a formal or historical version, then restated before their use.

This creates a particular kind of fatigue. The reader understands each paragraph but gradually loses sight of which statements are driving the proof.

The paper sometimes writes like a verification memorandum
There's a recurring style of sentence that explains what the preceding argument doesn't establish.

Sometimes that is essential. But there are many statements along the lines of:

This conclusion does not establish the stronger interface.

The example is not the asymptotic construction.

No optimality is claimed for the constant.

This calculation does not refute the published theorem.

The algorithm is capped even outside the promise.

Those qualifications have legitimate mathematical purposes. The problem is their frequency and placement.

A specialist doesn't need every possible misunderstanding anticipated at the point of reading. They need the main assertion, its scope, and the reason it's true.

For example, the distinction between an exact measured-label law and a retained quantum state is worth explaining carefully once. It doesn't need to keep reappearing as a warning.

The prose would become more authoritative if it trusted the reader slightly more.

That doesn't mean sacrificing precision. It means putting precision in the statements and proofs, rather than continuously surrounding them with defensive prose.

3. The opening still makes the reader work too hard
The abstract is reasonably good. It identifies the central result, the tournament, the classical hidden-certificate mechanism, and the independent analytic reconstruction.

But the introduction still enters formal machinery too quickly.

On pp. 1–2, the paper defines the optimal exponent with a full expression involving an infimum and several quantifiers, then states the theorem, its constants and thresholds, and the parameter-selection argument.

That's an appropriate formal statement. It isn't the best first explanation.

I would like to see the essential numerical mechanism displayed much more prominently:

R
(
P
k
,
m
)
≳
m
1
−
1
/
k
,
R
(
F
k
,
m
)
≳
m
R
(
P
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
.
R(P 
k,m
​
 )
R(F 
k,m
​
 )
Q(F 
k,m
​
 )
​
  
≳m 
1−1/k
 ,
≳mR(P 
k,m
​
 )≳m 
2−1/k
 ,
≲ 
m
​
 .
​
 
Ignoring polylogarithmic factors, this gives

R
(
F
k
,
m
)
≳
Q
(
F
k
,
m
)
4
−
2
/
k
.
R(F 
k,m
​
 )≳Q(F 
k,m
​
 ) 
4−2/k
 
​
 .
This is the mathematical story the reader needs to remember through the next fifty pages.

The paper does explain these relationships, but spreads them between the theorem, §1.1, the construction and §7.

I'd make the exponent arithmetic a central feature of the first two pages.

There is also a missing visual opportunity. Figure 1 on p. 16 is useful, but the reader has already encountered several pages of abstract definitions before seeing the construction.

For a 94-page treatment, I would expect at least one early diagram showing how the partial-function answers select a certificate and how the winner's pointers eliminate competing columns.

And I'd distinguish the schematic board from the numerical four-column example more clearly: the schematic shows longer bit strips than the four-row example, something the caption acknowledges but which remains a visual interruption.

4. The first ten pages are disproportionately demanding
Section 2 is mathematically conscientious, but it is not particularly inviting.

By the end of p. 10, the reader has been through deterministic trees, finite random mixtures, the oracle representation, unnormalised measurement masses, a deferred-measurement construction, and exact small examples.

A reader who already knows quantum query complexity can probably skim most of this. A reader who doesn't know it must learn a surprisingly elaborate formal model before encountering the main construction.

That is a difficult compromise.

The examples of OR, parity and one-sided promises are worth keeping. They make clear that the error threshold, query cap and promise convention have real consequences.

But much of the model-equivalence and deferred-measurement detail could be relocated to a technical appendix, with the necessary definitions retained in the main text.

The introductory mathematical reader needs to understand what a query costs and what a bounded-error algorithm is allowed to do. They do not initially need the full recursive measurement-mass semantics.

For the stated audience, the paper is self-contained in an important sense, but not necessarily easy to enter.

5. The strongest sections sometimes get interrupted by optional mathematics
This is most noticeable in the randomized lower bound.

The direct-product proof in §6.1 is important. Its central idea is elegant: conditional independence is preserved along a transcript, and a product of optimal continuation values cannot increase in expectation.

But that argument is followed by extra examples, a cap-event discussion, and an alternative proof with unnormalised weights.

The latter is valid material for a complete reconstruction, yet it changes the reader's task from understanding the central theorem to comparing two proof systems.

Likewise, §6.7, pp. 56–57, contains alternative search estimates after the main contradiction has already been proved.

The reader then has to return mentally to the main argument before §7 finally computes the optimal exponent.

I would move such alternatives into appendices while preserving them completely.

The same applies to parts of the amplification discussion and the sequential verification subsection. The retained-state result is interesting, but the abstract itself tells us that the stronger retained-state claim isn't needed for the Boolean headline theorem. It should not compete with the main proof for the reader's attention.

The problem isn't unnecessary mathematics. It's necessary-for-completeness mathematics being placed in the necessary-for-understanding path.

6. The Forrelation section needs a more memorable conceptual picture
The analytic proof is technically impressive as an exposition, but pp. 68–82 are the hardest sustained stretch of the paper.

By this point, the reader is tracking multiple Gaussian vectors, transformed vectors, block-dependent biases, interpolation parameters, discrete derivatives, derivative paths, martingale processes, and quantitative constants.

The paper provides an outline on pp. 69–70. That is helpful. But I would go further.

The entire analytic proof could be organised around three memorable questions:

Why are the two distributions different? The correlated Gaussian rounding gives a positive Forrelation mean, while the uniform distribution has mean zero.

Why can't a shallow classical decision tree distinguish them? Interpolation and integration by parts turn the difference in expectations into a controlled sum of high-order derivatives, bounded using a decision-tree martingale.

How does this imply hardness for a partial Boolean function? Error reduction and the promise-mass estimates prevent the algorithm from exploiting unpromised inputs.

These questions are all answered in the existing text. They just aren't visually or rhetorically prominent enough.

I would also add a diagram showing the Gaussian chain and the route taken by a derivative through its blocks. That would make (F22) much easier to remember.

The quantitative assembly in §8.14 is a further example of the problem. The constants 
18225
18225, 
119
/
144
119/144, and 
7
/
12
7/12 serve the proof, but their mathematical meaning isn't immediately apparent when encountered.

A short explanation of the qualitative inequality being sought, before the exact numerical calculation, would improve this passage substantially.

7. The proof's climax is not sufficiently celebrated
Section 7, pp. 58–61, is an interesting structural case.

The fixed-
k
k quotient argument in §§7.1–7.2 is clear. It correctly identifies how the positive power of 
m
m overwhelms the logarithmic losses and excludes every exponent below four.

That should feel like the mathematical conclusion of the construction.

Instead, §7.3 immediately starts a second detailed calculation with a growing 
k
k, an explicit schedule, and large constants.

This stronger result deserves inclusion, but its placement dilutes the main theorem.

I'd end §7 with an especially clear statement that, subject to the Forrelation lemma proved in §8, the optimal exponent is established. Then give the explicit uniform schedule as a corollary after the analytic estimates are available, or in a dedicated appendix.

There is another missed opportunity at the end of §8.15. Having completed the longest and most demanding part of the argument, the paper moves into the universal-bound appendix and then references and technical comparisons.

A short closing synthesis would help the reader register what was accomplished.

8. How I would revise it from here
I would not attempt another indiscriminate shortening pass. The three-document arrangement already gives readers a shorter specialist companion and an exposition; this document should remain the complete mathematical record.

I would make the following changes in priority order:

1. Strengthen the first three pages. Put the exponent arithmetic, total-function mechanism and a construction diagram ahead of the detailed formal conventions.

2. Remove repeated setup from individual proofs. In particular, tighten the start of §5.2 and the recurring definitions of query caps, promise behaviour and comparison probabilities.

3. Move genuinely optional proofs and comparisons out of the main path. Preserve the alternative direct-product proof, alternative search bounds and retained-state refinements, but make them destinations rather than interruptions.

4. Add conceptual summaries at major transitions. The starts of §§4, 5, 6 and 8 should tell the reader what mathematical obstacle is about to be overcome, not just what theorem is being reconstructed.

5. Improve mathematical visuals. An early addressed-certificate schematic, a quantum/classical cost comparison, and a Gaussian derivative-chain diagram would add disproportionate value.

6. Separate the mathematical voice from the implementation voice. Terms such as “the source”, “the formal statement” and “the Lean proof” appear throughout. These connections are useful, but the principal narrative should read as mathematics in its own right.

7. Finish with a genuine mathematical conclusion. After the completed proof, give the reader a compact synthesis of the tournament, the planted lower bound, the Forrelation hardness and the resulting exponent.

There are also a few small editorial blemishes, such as “Appendix A,.” on p. 8 and the malformed author ordering in the Göös–Pitassi–Watson reference on p. 90. They aren't important to the overall quality, but a final proofreading pass would catch them.

9. How different mathematical readers would react
A query-complexity specialist would, I think, find this useful as a detailed reconstruction. The material in the tournament, the adaptive direct-product argument and the Forrelation proof provides concrete mathematical substance worth inspecting. Its exhaustive detail is an advantage for someone trying to understand a particular technical step.

An advanced mathematician from another area would have a harder time. Even though the paper derives many of its tools, it demands sustained fluency with computational models, conditional probabilities, Fourier-style arguments and large parameter constructions. Such a reader could follow it with effort, but the introductory guidance slightly understates that effort.

An expert assessing the writing as a conventional research paper would probably view it as overlong and insufficiently selective. Not because the underlying mathematics lacks value, but because a research paper ordinarily makes much more aggressive decisions about which background results and proof variants belong in the primary narrative.

That distinction matters. The manuscript is better understood as a technical monograph or reconstruction than as an ordinary 20-page research article.

Final judgement
The paper is already past the stage where the main problem is basic clarity or grammatical competence. Its explanations generally make mathematical sense, and the major proof ideas are accessible once the reader reaches them.

Its strongest moments are genuinely good mathematical exposition: the weight-drift calculation, the cyclic tournament, the planted-input coupling, the capped direct-product argument, and the Gaussian derivative-path construction.

Its weakest moments are those where completeness becomes an end in itself, and the authorial judgement needed to guide a reader disappears behind qualifications, alternative proofs and numerical accounting.

I would be comfortable presenting this to a mathematical expert as a serious, detailed proof reconstruction. I would not yet call it exceptional mathematical writing.

To get from good to excellent, I think the next improvement should be chiefly editorial: stronger prioritisation, better conceptual transitions, and more confidence about what the reader needs at each moment.

The encouraging part is that the mathematical substance is already there. You don't need to manufacture insight or add another layer of technical apparatus. You need to make the existing insight more visible.

My overall score for its intended purpose is around 8/10, with meaningful room for improvement in the reading experience.

another pass through of rereading lets start to think about how to get it to 10/10 cuz repeated revies hover at 8 atp
Second-pass review: what would make this a 10/10 mathematical paper?
After going back through the 94-page reconstruction, I think the repeated 8/10 assessments are telling us something important.

The next improvement is not another general polish, and it is not simply reducing the page count. It is a change in how the paper communicates mathematical understanding.

The document already does a great deal of what a rigorous reconstruction should do: it supplies actual proofs, treats difficult edge cases, gives concrete examples, and carefully separates its results from those of the original authors.

What's preventing it from being exceptional is that the reader can follow individual arguments without always having an equally clear picture of the whole argument.

I would now aim for three simultaneous standards:

A specialist can see the entire proof architecture in five minutes.

A mathematically mature reader can understand why each major lemma works before working through its technical proof.

A reader checking a particular assertion can reconstruct every assumption, quantifier and calculation without leaving the PDF.

The third standard is already relatively strong. The first two need much more attention.

1. The first structural problem: the paper is organised partly around its sources, not its reader
This became much more apparent on rereading §2, §5 and §6.

On p. 4, the document explicitly explains that theorem and lemma numbers belong to OpenAI's preprint, while section numbers belong to this reconstruction. Consequently, Lemma 4.1 lives in §6.1, Proposition 3.2 lives in §5.2, and equation numbers mix source numbering with local numbering.

This has been carefully documented, but it's a real reading cost.

A mathematical reader normally expects a proposition numbered 5.2 to belong to Section 5, or to encounter a clearly indicated source citation. Here the reader must repeatedly translate between two structures.

I would change that convention.

For example, instead of

Proposition 3.2 (OpenAI; probabilistic-comparison tournament)

use something like

Theorem 5.2 (Probabilistic-comparison tournament; OpenAI, Proposition 3.2).

Then use the local identifier throughout the reconstructed proof. Keep the original paper's equation and theorem crosswalk in an appendix or the existing index.

This is more than cosmetic. A complete reconstruction should function as an independent mathematical document, even while remaining scrupulously faithful to its sources.

The PDF already has substantial electronic navigation, including bookmarks and internal links. So the missing improvement isn't merely more hyperlinks. It's a single, consistent mathematical language and numbering hierarchy.

2. A second, more important problem: the paper repeatedly delays its best mathematics
The most revealing example is the randomized lower bound.

Section 6 begins on p. 40. Its central construction is the dummy/planted input coupling. But the reader doesn't reach the detailed construction until pp. 48–49, because the complete direct-product proof comes first.

The direct-product proof is good. The order is the problem.

For someone reading the argument for the first time, the natural questions are:

What are the two distributions?

What makes the planted input different?

Why does a classical algorithm need to discover either a hidden zero or a particular certificate cell?

Why does predicting that cell require solving many hard problems?

Only then is the reader fully motivated to study the direct-product lemma.

Instead, the manuscript spends several pages proving a sophisticated lemma before the reader has seen its most concrete application.

I would reorganise §6 substantially:

PROPOSED MATHEMATICAL READING ORDER

Construct the dummy and planted distributions, ideally side by side
Explain the two possible first differences and why they are hard to find
State the capped direct-product lemma and immediately explain why it is precisely the needed tool
Prove the heavy-column and correct-cell estimates
Complete the distinguishing-probability contradiction
Supply the full direct-product proof, including its conditional-value argument, in a clearly designated technical section
This preserves the complete mathematics while making the dependency easier to understand.

The quantum argument has a related issue. By p. 33, the essential correctness analysis is essentially complete. Then the reader encounters the detailed finite query budget, sequential-verification formalism and amplification proof before reaching §6.

The amplification proof is worth having. In fact, §5.6 contains some good mathematical explanations of the Grover rotation and retained successful state. But its position causes a substantial delay between the quantum and classical halves of the separation.

For a 10/10 version, the main proofs should form an uninterrupted intellectual progression, with technical subproofs positioned where they are most useful, not merely where they first become logically available.

3. The paper needs an exceptionally clear five-equation spine
The manuscript already contains the following mathematics, but it does not make these five ideas memorable enough.

01

A winner certifies its uniqueness.

One all-one column has pointers to a zero in every rival. This establishes uniqueness and gives the quantum comparison its crucial asymmetry.

02

The tournament loses half its weight in expectation.

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
A real winner maintains substantial weight until selected.

03

Classically, guessing the entire certificate address is exponentially unlikely.

Pr
⁡
[
all 
r
 answers correct
]
≤
(
2
/
3
)
r
Pr[all r answers correct]≤(2/3) 
r
 
under the independent hard-input distribution and the specified per-input query caps.

04

Forrelation supplies the required classical hardness.

The analytic argument bounds shallow decision trees' ability to distinguish the rounded Gaussian distribution from the uniform distribution, while showing that their Forrelation statistics differ sufficiently.

05

The two query scales produce the nearly fourth-power separation.

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
1
/
2
polylog
⁡
m
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
m
.
Q(F 
k,m
​
 )
R(F 
k,m
​
 )
​
  
≲ 
k
​
 m 
1/2
 polylogm,
≳ 
k
​
 m 
2−1/k
 /polylogm.
​
 
I'd put a compact version of this proof spine immediately after the opening theorem, and revisit it at the end.

A specialist should finish reading and remember these mechanisms, rather than primarily remembering that the construction involved 
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
 m, an exact gate count and several amplification parameters.

Those quantities are necessary for the proof. They are not the intellectual identity of the result.

4. The examples are good, but some are pitched at the wrong level
This is a more specific criticism than I made previously.

The four-candidate cyclic tournament example on p. 27 is useful, but its numerical presentation makes an elegant idea appear unnecessarily complicated.

It specialises to 
ε
=
1
/
12000
ε=1/12000, then introduces weights such as 
11999
/
12000
11999/12000 and sampling probabilities such as 
11999
/
23999
11999/23999.

The specialist does not need those fractions to understand the mechanism.

After choosing pivot 
a
a, the weights could simply be written as

(
w
s
,
w
a
,
w
b
,
w
c
)
=
(
1
−
ε
,
0
,
0
,
1
)
,
(w 
s
​
 ,w 
a
​
 ,w 
b
​
 ,w 
c
​
 )=(1−ε,0,0,1),
with

Pr
⁡
(
s
∣
success
)
=
1
−
ε
2
−
ε
.
Pr(s∣success)= 
2−ε
1−ε
​
 .
That is both simpler and more general. The exact finite numbers can be retained in a supplementary calculation.

This is a recurring opportunity: use examples to expose the mechanism, and use exact numerical accounts to certify the bounds. Don't make one example perform both tasks when doing so obscures the mathematics.

The small addressed-certificate board on pp. 15–18 has a similar issue. Its 371 local tests are carefully counted, but the interesting concept is that the four different kinds of tests together certify a valid winning column. The exact figure 371 contributes comparatively little to the reader's initial understanding.

And there is an avoidable convention change. The board in §4.3 uses columns numbered from 1, whereas the XOR planting example in §6.3 uses zero-based rows and columns, with a warning explaining the translation. I would standardise the convention throughout.

There are legitimate reasons to use a different partial function for the planting example. There is little benefit in also changing the indexing.

Three mathematical diagrams would make a substantial difference
This 94-page PDF currently has one labelled figure, on p. 16. The typesetting itself is clean and the text size is reasonable. The visual shortfall is not decoration or typography; it's the absence of pictures for genuinely structural mathematical ideas.

Diagram A — the complete proof dependency

Forrelation ingredient

Classical hardness · quantum decoder · exact circuit

Total addressed-certificate function

Quantum tournament

Find and verify winner

Q
≲
m
Q≲ 
m
​
 
Classical planting

Hide the certificate

R
≳
m
2
−
1
/
k
R≳m 
2−1/k
 
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
With logarithmic factors and the universal upper bound accounted for

This should go near the beginning. It is a mental map, not a substitute for a proof.

The second diagram should show the dummy and planted boards on facing sides, highlighting only the erased zero and selected certificate cell. That belongs at the opening of §6.

The third should show the Gaussian chain in §8: the independent 
U
j
U 
j
​
 , transformed 
V
j
=
H
U
j
V 
j
​
 =HU 
j
​
 , block biases, and one differentiated coordinate in each block. That would make the central path identity (F22) far easier to visualise.

5. The paper has a hidden second centre of gravity
The reconstruction isn't only about the total-function separation.

Starting at §8.5, p. 68, it develops a substantial analytic argument for Forrelation hardness. This occupies roughly fourteen pages and involves an alternative bounded-bias Gaussian transform, a derivative-path identity, a martingale estimate, and explicit uniform constants.

That's enough mathematics to deserve much stronger structural prominence.

Yet it currently sits inside a section titled Proofs of the Forrelation ingredient, whose first seven pages concern the quantum decoder, Boolean circuit and finite census.

I would divide that material into two major sections: one for the elementary quantum and circuit ingredients, and one titled something like A self-contained analytic proof of Forrelation hardness.

The quantitative result (F43) should be a prominently stated theorem at the beginning of the analytic section. Currently its full assembly is reached on p. 80. A reader should know earlier exactly what this long argument is proving and why its strength matters.

The explicit growing-
k
k result on pp. 59–61 also deserves better placement. Its asymptotic idea is elegant: balance the exponential dependence on 
k
k in the quantum decoder against the 
m
−
1
/
k
m 
−1/k
  loss in the classical bound. The detailed constants then turn that balancing argument into an effective schedule.

But the current presentation moves into constants such as 
2
53
2 
53
  before the conceptual balance has been sufficiently emphasised.

I'd present the asymptotic balancing principle first and the exact finite schedule second. The latter is valuable evidence of quantitative control; it should confirm the idea rather than introduce it.

This is one of the changes that could genuinely elevate the document from a thorough reconstruction to excellent mathematical exposition.

6. A high-value improvement: explain the three different Forrelation interfaces once
The paper is particularly careful about what happens off the promise, and rightly so. But this distinction is explained in §3, §4, §5 and §8, sometimes in quite similar language.

A simple table near §3.2 could consolidate the conceptual issue:

Object

On promised inputs

Off promise

Purpose

Partial function 
P
P

Has a definite Boolean value

Undefined

Supplies hard address bits

Quantum decoder

Predicts 
P
P with bounded error

May output either bit

Proposes an address

Exact circuit 
(
d
,
b
)
(d,b)

d
=
1
,
 
b
=
P
d=1, b=P

d
=
0
d=0

Certifies a proposed address

This is one of the most important distinctions in the entire construction.

The explanation currently exists and is mathematically careful. But a reader should be able to internalise it once, then recognise how it is used throughout the later proofs.

That is the difference between repeatedly telling the reader what is true and giving them a mathematical model they can reuse.

7. I would rewrite the opening of the classical proof quite aggressively
Here is an example of what I mean. This is not changing the mathematics; it is changing what the reader encounters first.

Instead of starting §6 with the generic theorem, a technical recap and an extended detour through the direct-product proof, I would lead with something close to:

The classical lower bound is proved by coupling two distributions of inputs. In the first, every column contains one hidden zero and all certificate cells are blank, so the total function is zero. In the second, we choose a uniformly random column, erase its zero, and fill the certificate cell addressed by its partial-function answers. The resulting function value is one.

A deterministic query algorithm sees identical answers on the two inputs until it queries one of the changed positions. There are only two possibilities: it discovers the erased zero, or it queries the planted certificate cell.

We bound these events separately. The first requires discovering a hidden zero in an independently selected column. The second requires predicting an entire vector of hard partial-function outputs. A capped direct-product theorem makes the latter bound valid even when queries to the underlying instances are chosen adaptively.

The rest of the argument quantifies these two obstacles and shows that a classical algorithm using substantially fewer than 
m
L
mL queries cannot distinguish the distributions.

This is a more direct mathematical invitation.

A reader knows what the proof will accomplish before encountering its machinery. The complete proof of the direct-product theorem can then be given with all its current detail.

I would use the same technique at the beginning of the analytic hardness proof.

8. The technical proof of Forrelation should have an even clearer internal structure
On closer rereading, I think the mathematical writing in §§8.9–8.14 is actually among the better parts of the PDF.

It has a genuine sequence of ideas:

The interpolation starts in the first block. Gaussian integration by parts moves a derivative into successive blocks. Multilinearity removes repeated-coordinate derivatives. The resulting derivative sum is bounded by a martingale. A separate moment calculation shows that the two distributions really do differ. Error reduction turns those estimates into promised-input hardness.

That is an elegant architecture.

But the reader needs stronger signposting at two particular transitions.

First, the transition from (F22) to (F25). The paper has worked hard to manufacture one mixed derivative involving a coordinate in each labelled block. The reason for doing this should be emphasised: those derivatives are now precisely the sort of quantities the adaptive decision-tree estimate can control. A short paragraph explicitly matching the output of one lemma to the input of the next would help.

Second, the transition from (F39) to (F42). The positive mean of Forrelation under the rounded distribution does not immediately yield a hard promise problem, because both distributions can charge inputs outside the promise. This is the decisive logical obstacle in the final part of the proof.

The document handles it, but the reader could benefit from a short explanation before the acceptance-probability inequalities appear.

I would also introduce the Gaussian path calculation with the 
k
=
2
k=2 case before the existing 
k
=
3
k=3 derivation. The two-block case shows the integration-by-parts mechanism in its simplest form; the three-block case then explains how it iterates.

This is a place where an additional half-page could improve a fourteen-page proof more than two pages of general introductory commentary.

9. There are some genuine finishing defects in the PDF
These are smaller than the structural issues, but they matter for a document aspiring to be exceptionally polished.

I checked the extracted text and layout of the attached PDF, not the repository source.

The bibliography references are not consistently typeset. There are roughly fourteen visible instances of bare citation-style identifiers, including BansalSinha2021 on p. 12, GPW2018 on p. 21, BBHT1996 on p. 23 and AIK2026 on p. 30. These should become consistent author–year or numbered citations.

Appendix B contains the references on pp. 88–90, but then the paper resumes mathematical appendices C and D on pp. 90–94. I would place the bibliography after all the mathematical appendices.

There is also a small avoidable mismatch in Figure 1 on p. 16: the schematic bit strips are longer than the four-row numerical example being introduced. The caption correctly calls them schematic, but the visual could simply be made consistent with the example or explicitly presented as a general-
m
m illustration.

These aren't reasons for an 8/10 score by themselves. They are examples of things that should not survive a final professional editorial pass.

10. What I would actually change in the next revision
I would treat the next revision as a structural intervention, not a normal copy-editing pass.

Part of the PDF

Proposed intervention

Importance

Abstract and pp. 1–4

Introduce the five-step mathematical spine; move numerical details and the numbering crosswalk out of the opening

Very high

§2, pp. 4–11

Keep precise query conventions in the main text; move detailed model equivalences and optional small examples into supporting sections

High

§4, pp. 13–21

Put the certificate diagram before the formal construction; clarify the three interfaces once; standardise indexing

High

§5, pp. 22–40

Give the weighted-tournament insight before the full algorithm; move optional sequential-verification and amplification details off the main path

Very high

§6, pp. 40–58

Lead with the planted construction rather than the complete direct-product proof

Very high

§7.3, pp. 59–61

Present the growing-
k
k balancing principle before its constants; consider moving it after the analytic proof

Medium–high

§8, pp. 61–82

Split elementary Forrelation construction from analytic hardness; elevate (F43) to a central theorem; add a derivative-chain diagram

Very high

Appendices and references

Consolidate optional source comparisons, fix citation keys and give the paper a proper closing synthesis

Medium

Importantly, I would retain almost every substantive mathematical proof. There is no need to turn the 94-page reconstruction into another 18-page paper.

The main proof path might become shorter, with the complete document remaining around its current length. That would be an improvement even if the page count barely changed.

11. How to know whether we've actually reached 10/10
I wouldn't use another internal review that simply produces another score.

I'd test a revised version against specific reading outcomes.

A query-complexity specialist reading the opening four pages should be able to explain the theorem, identify the innovation in the total-function construction, and name the purpose of each major ingredient without hunting through the document.

A reader reaching the end of the quantum proof should be able to explain both why the tournament finds a genuine winner and why it remains valid when comparisons among losing candidates are arbitrarily unreliable.

A reader reaching the classical lower bound should understand the two first-difference events before encountering the complete capped direct-product proof.

And someone studying §8 should be able to explain the analytic strategy in a short paragraph before attempting any of its technical inequalities.

Finally, an independent mathematical expert should be able to check the mathematical statements and proofs without discovering that their assumptions or notation change unexpectedly. That's a separate standard from editorial quality, and I haven't independently certified every derivation in this rereading.

My updated assessment
The paper's best mathematics deserves better presentation than it currently receives. The theorem, weighted tournament, capped simulator and Gaussian-chain argument provide enough substance for an excellent reconstruction.

I think the plateau around 8/10 comes from a recurring imbalance:

The paper is written primarily to make every assertion defensible. A 10/10 version would make the central ideas unforgettable while retaining that defensibility.

Those two objectives are not opposed. Better mathematical writing often makes rigorous proofs easier to check because it reveals which assumptions are doing the work.

I would not spend the next revision adding more explanations everywhere. I would spend it deciding, paragraph by paragraph, whether a passage advances the mathematical argument, teaches an essential mechanism, or supplies technical detail that belongs on a secondary reading path.

The single highest-value intervention is the combination of a clearer proof spine, a reordered classical lower bound, and a standalone analytic Forrelation section. Those three changes would materially improve how the paper is experienced from beginning to end.

The next pass should therefore be a serious restructuring of the exposition, with proof preservation as a hard constraint—not another round of local polishing.

another pass through of rereading lets start to think about how to get it to 10/10 cuz repeated revies hover at 8 atp 

like lets have taste and think about what makes a truly well written paper 

liek jsut reifnroce what you've been saying but think about it further read the paper properly agian
Third reading: the difference between an 8/10 and a truly excellent mathematical paper
I went back through the attached 94-page reconstruction, including the opening, the tournament proof, the classical direct product, the planted construction, the explicit exponent calculation, the Gaussian-chain argument and the appendices.

I think I can now articulate the problem more precisely.

This is a paper that is extremely concerned with being correct, complete and defensible. It is less consistently concerned with giving the reader the most beautiful route to understanding why the mathematics works.

That distinction is the key to the next revision.

A 10/10 mathematical paper does not merely contain good explanations. It exhibits judgement: what to introduce, what to delay, what to prove, what to emphasise, what to leave implicit, and what the reader should remember.

The best mathematical exposition has a quality of inevitability. You encounter a problem, understand the obstacle, and then the technique that solves it feels natural—even when the technique is genuinely ingenious.

This manuscript achieves that feeling in isolated places. It doesn't yet sustain it across the whole argument.

My diagnosis is therefore more specific than “too long” or “too technical”:

The manuscript is often better at proving that a step works than at revealing why that step is the right step to take.

That is what I would make the next revision address.

1. Taste begins with mathematical proportion
A beautiful 94-page proof can absolutely be better than a compressed 30-page proof. Completeness is part of this document's purpose.

But mathematical details do not all deserve equal prominence.

Consider what the paper asks a reader to learn:

The design of a total function with a uniquely certified winner.

The probabilistic-comparison tournament and its weight-halving phenomenon.

The capped direct-product argument that hides a certificate address.

The Gaussian interpolation and derivative-martingale proof of Forrelation hardness.

Exact oracle conventions, circuit gate counts, query budgets, floors, numerical thresholds and alternative derivations.

All five belong in a complete reconstruction. They do not have equal intellectual significance.

The first four are the ideas the reader should carry away. The fifth establishes the rigour and quantitative validity of the construction.

Currently, they often receive similar narrative weight.

On p. 34, for example, the paper presents a table of seven budget parameters, followed by the exact physical-query formula. The accounting is valuable. But the quantum algorithm's conceptual correctness has effectively already been explained on pp. 30–33, and the reader is about to encounter another large arithmetic calculation on p. 35.

The result is that the paper spends a substantial portion of its momentum on accounting precisely when the reader should be enjoying the completion of the quantum argument.

I would state the quantum upper bound and its explanation first, then put the finite budget in a clearly marked quantitative verification subsection.

Not because the budget is unimportant, but because its importance is to certify the theorem, not to explain the theorem.

A great paper makes this distinction almost effortlessly.

2. The manuscript keeps introducing machinery before the question that makes it interesting
This is the strongest recurring problem I found.

Take §5.2, p. 24.

The section states the tournament proposition, introduces the comparison interface and parameters, describes dominance, states the algorithmic guarantee, discusses the proof stages, restates the comparison assumptions, gives a literature comparison, and recalls the parameters again.

Only then, on p. 25, does the reader reach the beautiful calculation:

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
That calculation is the heart of the section.

It is remarkably elegant because complementarity alone is sufficient. The losing candidates can form cycles, comparisons can be noisy, and there need not be an underlying ordering. Yet expected weight still halves.

The author should be eager to show us this.

I'd begin the section by saying, in essence:

The tournament works even when comparisons among losing candidates are arbitrary. Its key observation is that choosing a pivot proportionally to its current weight causes the total weight to fall by at least half in expectation. The reason is simply that the probabilities of the two outcomes of each pairwise comparison sum to one.

Then give the calculation.

The full proposition with coherent comparison interfaces, fixed error parameters and exact query caps can follow.

This doesn't sacrifice a single mathematical condition. It makes those conditions relevant to something the reader now wants to understand.

The reader should encounter the central insight before its complete technical packaging.

The same principle applies to the lower bound in §6 and the analytic argument in §8.

3. A great proof makes its lemmas feel necessary, not merely available
The clearest example is §6, pp. 40–54.

The manuscript begins with the classical lower-bound theorem and then devotes §§6.1–6.2 to a complete direct-product proof and hard-distribution construction. The planted-input argument finally appears in §6.3, p. 48.

But the table on p. 49, showing the dummy and planted inputs side by side, is almost exactly the object I would want to encounter at the start of §6.

The reader should first see the two inputs, recognise that they differ only in a hidden zero and an addressed certificate cell, and then ask:

How can a classical algorithm possibly discover that cell without knowing the address?

Now the direct-product lemma becomes desirable. The reader understands why we need a result about simultaneously predicting many independent hard answers, even when queries are adaptive.

The actual direct-product proof is one of the stronger parts of the reconstruction. Its central potential,

Z
(
τ
)
=
∏
h
=
1
r
V
h
(
τ
)
,
Z(τ)= 
h=1
∏
r
​
 V 
h
​
 (τ),
is elegant: only one factor changes when the algorithm queries one input, and its conditional expected value cannot increase. The product is therefore a supermartingale.

But the manuscript could expose that observation before developing all of the posterior notation. The reader would then have a picture of the proof before working through its machinery.

This is a fundamental distinction in mathematical exposition:

An adequate proof tells the reader what is being done. An excellent proof makes the reader understand why doing it is natural.

The paper has the mathematics needed to achieve this. The order of presentation often prevents it. 
reasoning_record(5).pdf

4. Some of the paper's very best writing shows what the rest should aspire to
I don't want this to become a critique that assumes everything needs rewriting.

Certain passages are close to exactly right.

The transcript lemma, pp. 13–14
The equivalence between gate consistency and the unique circuit-evaluation transcript is introduced, proved by a straightforward topological induction, and immediately used to explain how the domain and value bits certify a proposed answer.

This is compact, complete, and mathematically purposeful.

The reader sees the statement, the proof mechanism, and why the conclusion is useful. There is relatively little surrounding commentary.

The tournament drift calculation, p. 25
Once the proof reaches the weight update, the explanation is excellent.

The sum over ordered pairs is reorganised into unordered pairs. Complementarity cancels the complicated comparison probabilities. An apparently sophisticated probabilistic phenomenon follows from a simple identity.

This is the kind of mathematics that should be foregrounded.

The higher-degree warning, pp. 74–75
This is another especially good passage.

The paper explains that an order-
k
k derivative at a biased point need not depend only on the degree-
k
k Fourier coefficients. Higher-degree terms survive, as (F24) demonstrates.

That observation explains why the next lemma must control derivatives under biased product measures.

This is genuinely good expository judgement: it identifies a tempting but incorrect simplification and shows precisely why the stronger argument is required.

I would use these passages as the editorial model for the rest of the document.

They work because they advance the mathematics. They don't spend much time describing the administrative status of the mathematics.

5. The treatment of exact constants needs discrimination, not deletion
A deeper issue is deciding when numerical precision improves understanding.

The paper is admirably exact about many things. But some constants make the argument clearer, while others distract from the underlying structure.

Consider three cases.

The 
2
/
3
2/3 endpoint in the two-bit OR example on pp. 9–10 is worth retaining. The exact probability matters because the randomized query complexity changes when the success threshold becomes strict. The example exposes a genuine subtlety in the model.

The 
11999
/
12000
11999/12000 weights in the cyclic tournament example on p. 27 are less valuable. Here the interesting phenomenon is that a dominant candidate survives even though the others form a cycle. Writing 
1
−
ε
1−ε would make the same point more cleanly. The numerical substitution could be given afterwards.

The threshold 
t
≥
13669
k
2
t≥13669k 
2
  is valuable as a quantitative theorem, but not as an introductory idea. It certifies uniform control; its exact magnitude is not the reason the method works.

This is what mathematical taste looks like at a fine level.

It is not deciding that constants are ugly and should disappear. It is recognising which constants embody a mathematical phenomenon and which merely witness an inequality.

The latter should remain available to the reader without becoming the centre of the exposition.

The same concern applies to §7.3, pp. 59–61. The genuinely interesting idea is that the growing parameter 
k
k balances two competing losses: the exponential dependence of the quantum decoder on 
k
k, and the classical exponent loss 
m
−
1
/
k
m 
−1/k
 .

The paper eventually explains this. But by then it has introduced a complicated expression for 
C
k
C 
k
​
  and several large numerical bounds.

I want to understand the balance first and the constants second.

6. The construction should feel designed rather than assembled
Section 4 defines the addressed-certificate function carefully, and §1.1 already gives a decent overview. Yet there is an opportunity to make the construction much more satisfying.

Think about how a mathematician might discover it.

We want a total Boolean function with a certificate that quantum computation can find cheaply but classical computation cannot find cheaply.

A winning column must certify its validity. Requiring that its string consist entirely of ones makes it easy to identify a special structural property.

But that alone isn't sufficient. We also need the winner to eliminate every rival, so its certificate contains pointers to zeros in their strings.

Why do the pointers face outward? Because an arbitrary pointer from a rival can never find a zero in the winner's all-one string. This produces one-sided reliability even when the rival's address is meaningless.

Why hide the certificate in an addressed cell? Because the cell can be selected by a vector of partial-function values that a quantum algorithm can decode cheaply but a classical algorithm cannot reliably predict.

Why store circuit transcripts? Because merely proposing an address is not enough: the total function must certify that those partial-function inputs actually lie in their promise and have the claimed values.

That's a beautiful chain of design decisions.

The manuscript contains all these explanations, but it tends to introduce them as features of the construction rather than as responses to successive obstacles.

I would make this progression explicit.

At the end of the introduction, the reader should feel that the design almost forces itself upon us once the requirements are understood.

That feeling of mathematical inevitability is one of the most important differences between a good reconstruction and a great one.

7. The Forrelation proof is where I would invest the most editorial thought
This is the most technically distinctive part of the reconstruction, and I think it deserves the most careful writing.

On p. 69, the manuscript states the lower bound, compares it with Bansal–Sinha, presents the stronger uniform result, and then explains the Gaussian-chain argument.

The conceptual explanation is excellent material. It simply arrives too late.

Here is roughly the opening I would want for the analytic proof:

We prove classical hardness by constructing two distributions on the same Boolean input space. Under the first, the input is uniformly random. Under the second, it is obtained by rounding a chain of correlated Gaussian vectors. Their Forrelation statistics differ, but we will show that a shallow decision tree cannot reliably distinguish the two distributions.

The key step is to interpolate in the first block only. Gaussian integration by parts then propagates a derivative through the successive blocks. Multilinearity eliminates derivatives that revisit an already differentiated coordinate, leaving a sum of order-
k
k mixed derivatives. A decision-tree martingale bounds this sum.

Finally, we use moment estimates and error reduction to account for inputs outside the Forrelation promise. This turns indistinguishability into a quantitative randomized query lower bound.

That is essentially what the paper already says, but I would place it before the detailed theorem comparisons and constants.

Then I would organise the argument around its three genuine conceptual achievements.

First: why the interpolation is chosen as it is
The manuscript establishes that the zero endpoint of the first-block interpolation is uniform. That's not a routine observation, and the Gaussian-reflection argument in §8.8 is worthwhile.

The reader should understand why turning on only the first block is so helpful: it gives a uniform endpoint while letting the derivative propagate through the chain in a controlled way.

This should be presented as a central idea, not merely a definition followed by a lemma.

Second: why the derivative becomes manageable
The path identity (F22) on p. 74 is the heart of the analytic method.

The calculation for 
k
=
3
k=3 is good because it makes the propagation visible. I'd precede it with a 
k
=
2
k=2 calculation or a very small schematic, so that the reader can first see one integration-by-parts step in isolation.

Then the general identity becomes the natural iteration of something already understood.

Crucially, explain how the resulting path family matches the hypotheses of the derivative-growth lemma. That is the bridge between the Gaussian construction and the decision-tree argument.

Third: why indistinguishability proves a promise lower bound
The discussion on pp. 79–80 is logically important.

A separation between two distributions on the full sign cube does not immediately prove hardness for a partial function, because both distributions may assign probability to unpromised inputs.

The paper resolves this using moment estimates, amplified error and the pointwise inequalities in (F41).

This is not bookkeeping. It is the final conceptual obstacle.

I would give it as much rhetorical emphasis as the derivative path itself.

The ultimate contradiction in §8.14 compares a lower expectation gap of 
119
a
k
/
144
119a 
k
​
 /144 with an upper bound of 
7
a
k
/
12
7a 
k
​
 /12. Those constants are the conclusion of the quantitative work. The reader should already understand what the two bounds represent before encountering the numerical comparison. 
reasoning_record(5).pdf

8. The prose should become calmer and less self-conscious
Another feature I noticed on this pass is how often the text explains its own relationship to the original paper, the formal implementation or the other documents.

For example, there are references to readers arriving from the specialist companion, statements about which theorem an implementation exports, and repeated distinctions between what a particular calculation does and doesn't establish.

Some are essential. But in aggregate they interrupt the mathematical voice.

There's a difference between these two kinds of writing:

This step holds on every input, including inputs outside the promise.

That can be an important assertion.

And:

This step is the version used in the formal statement, while the stronger interface discussed later is not required by the Boolean theorem.

That may be useful information, but it should be placed according to what the reader is currently trying to prove.

The current paper occasionally sounds like it is documenting a collection of proof obligations rather than developing a mathematical argument.

A superb reconstruction should be able to do both, but the principal prose should remain focused on the mathematics.

I would retain the source and formal-proof comparisons in a well-organised note on proof relationships, and keep the main body as much as possible in one mathematical voice.

This is not about making the prose more casual or less precise.

It is about removing unnecessary commentary between the reader and the argument.

9. The paper needs a stronger sense of arrival
There is one final structural issue that strikes me as important.

The manuscript proves the fixed-parameter exponent conclusion in §7, develops the complete analytic Forrelation proof in §8, and then moves into a discussion of the published proofs and Appendix A.

But after this long journey, there is no strong mathematical synthesis.

On p. 82, the last substantive section before the appendices is about the relationship to published results. The final page of the PDF ends with technical comparisons and the AI-use disclosure.

Those are appropriate things to include, but the mathematical narrative needs an earlier, unmistakable conclusion.

I would add a short section immediately after the completed proof that revisits the original question.

It should explain that the total function has one uniquely certified winner; the quantum algorithm finds and verifies that winner through the weighted tournament; the classical lower bound hides its location and address; the Forrelation argument supplies the hard address bits; and the universal quartic upper bound makes the resulting exponent optimal.

Then explain, in a few sentences, which difficulties were genuinely central and which quantitative losses were merely convenient.

After that, the reader can enter the appendices knowing the mathematical journey is complete.

A 94-page proof particularly needs this sense of closure.

10. What the next revision should actually optimise
I would stop treating this as a collection of passages to improve independently.

The next edit should be governed by one question:

At every point in the document, what does the reader know, what are they trying to understand, and why is the next paragraph the best possible next paragraph?

Apply that to the whole paper.

For §1, the answer is that the reader needs to understand the separation mechanism and why exponent four appears.

For §4, they need to understand how the total function satisfies the competing requirements of verifiability and hiddenness.

For §5, they need to understand why unreliable comparisons still permit efficient quantum selection.

For §6, they need to understand why neither finding the hidden zero nor finding the correct cell is feasible within a small classical query budget.

For §8, they need to understand why a classical decision tree cannot distinguish the two Forrelation distributions.

Everything else should support those objectives.

This gives a clear editing discipline. Retain the complete proofs, but adjust when the reader encounters them. Keep the exact finite estimates, but don't let them delay the central insight. Preserve important warnings about invalid arguments, but don't surround every theorem with defensive qualifications.

I would also resist overproducing diagrams, summaries and explanatory boxes. A great mathematical paper isn't necessarily heavily illustrated. Two or three well-designed diagrams and a handful of precise conceptual transitions would probably be enough.

The existing typography is already quite good. This is primarily a problem of mathematical composition, not visual design.

One further test I would use
Give a specialist the first four pages. They should be able to describe the construction and the exponent comparison without seeing the rest.

Then give them the opening two pages of each major proof section. Before reading the technical derivations, they should understand what the key difficulty is and have some sense of why the proposed technique will solve it.

Finally, ask them to reconstruct the argument from memory the next day.

If they remember the parameter values, the theorem locations and the numerous qualifications, but cannot reconstruct the mechanism, the exposition hasn't succeeded.

If they can reproduce the chain of ideas and know exactly where to return for the rigorous details, it has.

That is a much more useful measure than another numerical rating.

Final assessment after this rereading
I still regard this as a strong technical reconstruction. It is not mathematically superficial. The detailed treatment of the tournament, the direct product, the Gaussian-chain argument and the universal bound gives it considerable substance.

But I've become more convinced that the remaining gap is not primarily grammatical, stylistic or even organisational in the ordinary sense.

The gap is in mathematical authorship: choosing how the reader should discover the mathematics.

A very good reconstruction faithfully preserves the logic of a proof.

An exceptional reconstruction makes the proof's architecture clearer than it was before, exposes its key ideas at precisely the right moments, and makes difficult arguments feel graspable without making them seem easy or trivial.

The current document already has passages that meet that standard. The task is to extend that quality throughout.

I would therefore make the next substantial revision about mathematical motivation, order of revelation, economy of emphasis and the rhythm of insight followed by proof.

Not more explanation everywhere. Not fewer technical details indiscriminately. Not another ten rounds of sentence polishing.

A deliberate, mathematically informed editorial reconstruction of the reconstruction.

That's the change I think has the best chance of moving the reading experience meaningfully beyond its current plateau.

another pass through of rereading lets start to think about how to get it to 10/10 cuz repeated revies hover at 8 atp 

like lets have taste and think about what makes a truly well written paper 

liek jsut reifnroce what you've been saying but think about it further read the paper properly agian

like now sum up this whole thread and reread agian like you can specify the deliverables on making this a 10/10 no more 8/10 fucking rating

Worked for 6m
The final editorial brief: turning the 94-page reconstruction into exceptional mathematical writing
After rereading the PDF and synthesising all our previous reviews, I think we can stop circling around the same criticisms.

The next revision needs to change the reader's experience of the mathematics, not merely improve the sentences.

A genuinely excellent reconstruction should make a difficult proof feel progressively understandable without concealing any of its difficulty. Its rigour should be complete, but the reader should encounter the mathematical insight before being asked to absorb all the machinery that certifies it.

I have one important correction to our previous feedback.

The paper already contains many of the explanations we've repeatedly asked it to add.

For example:

Page 3 already gives a good account of the winning-certificate mechanism, outward pointers, quantum tournament and planted classical lower bound.

Page 22 already identifies the weight-halving phenomenon as the central idea of the quantum algorithm.

Pages 40–41 already explain the two first-difference events and provide a four-step overview of the classical proof.

Page 69 already contains a remarkably compact explanation of the Gaussian interpolation, derivative propagation, martingale argument and promise-mass difficulty.

So the solution is emphatically not to add another explanatory paragraph at the beginning of every section.

That could make the document worse.

The deeper problem is that the best explanation often appears too late, is surrounded by repeated technical setup, or competes with another explanation of essentially the same thing.

The manuscript has accumulated multiple layers of guidance: an abstract, reading guide, introduction, dependency index, numbering key, local recaps, theorem interfaces and proof previews. Individually they're defensible. Together they create an excess of orientation.

A mathematically sophisticated reader doesn't need to be guided continuously. They need to be shown the right thing at the right time.

The editorial principle
Every page should make the central argument easier to reconstruct, not merely make the individual statements easier to verify.

This doesn't mean removing difficult proofs. It means allocating the reader's attention intelligently.

The strongest existing passages demonstrate the standard we want. The transcript lemma on pp. 13–14 makes a claim, proves it cleanly, and immediately shows why it matters. The tournament drift on p. 25 transforms a complicated probabilistic situation into one simple identity. The discussion following (F24) on pp. 74–75 exposes why an apparently simpler Fourier argument would be insufficient.

Those passages aren't good because they're short. They're good because every piece of mathematics has a purpose the reader understands.

Our goal should be to make the whole document read with that degree of judgement.

What the entire review thread has established
The repeated reviews have converged on five problems, but they are related rather than independent.

First, mathematical hierarchy. The current document sometimes gives equal prominence to the invention of the argument, its rigorous justification, exact constants, source comparisons and model implementation details. These belong at different levels of attention.

Second, order of revelation. The reader is often given definitions and technical conditions before understanding the obstacle those conditions overcome. The direct-product argument and the analytic Forrelation proof are the largest examples.

Third, competing narratives. The text alternates between being a mathematical reconstruction, an independent exposition, a proof-audit record and a commentary on formalisation. All are legitimate purposes, but the central mathematical argument should have one consistent voice.

Fourth, mathematical memory. The document establishes a large number of true and useful facts, but could do more to help readers retain the few structural ideas from which the proof can be reconstructed.

Fifth, finishing discipline. The numbering conventions, bibliography, figure placement, source-credit language and lack of a strong final synthesis prevent the PDF from feeling completely composed.

These aren't five excuses for another general polishing exercise. They tell us precisely what the rewrite must deliver.

The mathematical backbone that the rewrite must preserve
Before specifying the deliverables, I would freeze the central argument into this sequence:

1. The supplier

The partial function 
P
k
,
m
P 
k,m
​
  is quantumly cheap, classically hard, and has an exact circuit recognising its promise and value.

Q
(
P
k
,
m
)
=
O
k
(
1
)
,
R
(
P
k
,
m
)
≳
k
m
1
−
1
/
k
polylog
⁡
m
Q(P 
k,m
​
 )=O 
k
​
 (1),R(P 
k,m
​
 )≳ 
k
​
  
polylogm
m 
1−1/k
 
​
 
For fixed k, with the appropriate parameter range.
2. The construction

Build one total function 
F
k
,
m
F 
k,m
​
  with at most one winning column. Its certificate is selected by the hard address bits, and its outward pointers disqualify every rival.

3. Quantum upper bound

Weighted comparison and verification.

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
4. Classical lower bound

Hidden zero or hidden certificate cell; use the direct product to defeat address prediction.

Pr
⁡
[
predict address
]
≤
(
2
/
3
)
r
Pr[predict address]≤(2/3) 
r
 
5. The separation and its optimality

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
(
log
⁡
m
)
6
Q(F 
k,m
​
 )≲ 
k
​
  
m
​
 (logm) 
6
 
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
(
log
⁡
m
)
2
R(F 
k,m
​
 )≳ 
k
​
  
(logm) 
2
 
m 
2−1/k
 
​
 
Together with the universal fourth-power upper bound, the family excludes every universal exponent below four.

This isn't a proposal to insert five more large explanatory boxes into the actual PDF. It's an editorial test.

Every major section should have an identifiable role in this sequence. Forrelation hardness supplies the first ingredient. The tournament and planting arguments produce the two bounds. The final parameter comparison and universal bound finish the proof.

The proof shouldn't be difficult to remember merely because its narrative is buried under its quantitative details.

The actual revision deliverables
I would commission seven defined deliverables, culminating in one finished, complete PDF. Each has a specific purpose and a test for whether it has succeeded.

Deliverable 1 — Rebuild the opening four pages
HIGHEST PRIORITY · CURRENT PP. 1–4

The opening should establish the intellectual identity of the work.

At the moment, the abstract gives the main result, discusses the independent Forrelation reconstruction, states numerical refinements, and then spends its final paragraph explaining differences between the printed mathematics and the Lean proofs.

That final paragraph isn't intrinsically bad. It is misplaced in a document whose primary purpose is the mathematics.

I would make the new front matter do four things.

Establish the result. Explain precisely what the nearly quartic separation means and what it settles.

Explain the construction. Promote the good prose currently in §1.1 on p. 3 into the reader's first encounter with the mechanism. The outward-pointer idea should arrive before the formal quantifier-heavy theorem.

Distinguish contributions. State succinctly what belongs to OpenAI's original proof, what belongs to earlier Forrelation and decision-tree work, and what this reconstruction supplies. The independent uniform analytic argument deserves prominence without an unsubstantiated novelty claim.

Explain the reading routes. Tell a specialist how to follow the separation and how to reach complete derivations. Do this once, rather than spreading it across the reading guide, dependency index and numbering key.

The formal definition of 
α
t
o
t
α 
tot
​
  belongs near the beginning, but not before the reader has a useful intuitive picture of the problem.

Definition of done

A mathematician reads the first four pages and can explain what 
F
k
,
m
F 
k,m
​
  is doing, why the quantum and classical strategies differ, why the fourth power arises, and which results are reconstructed rather than originally discovered in this manuscript.

Deliverable 2 — Establish one uninterrupted route through the separation
CURRENT §§2–7 · PP. 4–61

This is the largest editorial task.

Importantly, I would not automatically move every technical proof into an appendix. Some of our earlier recommendations were too mechanical about that.

The document is a complete reconstruction, not an eighteen-page research announcement. Readers choosing it may reasonably want the full proof of the direct-product lemma or the amplification theorem.

What we should do is distinguish the essential proof path from optional extensions and duplicate explanations.

§2

Models and conventions

Keep the exact meanings of randomized and quantum query cost, promises, oracle calls and worst-case caps in the primary path. Move the most elaborate deferred-measurement machinery to a supporting proof section. Retain the illuminating OR, parity and promise examples, but do not force every reader through all of them before the construction.

§§3–4

Forrelation contract and total function

Present the three required properties of 
P
k
,
m
P 
k,m
​
  together. Then build the certificate around the obstacles it solves: uniqueness, hidden address, exact promise certification and outward-pointer dominance. Introduce the picture before the most detailed input-length accounting.

§5

Quantum algorithm

Lead with the weighted-tournament calculation. Show why the true winner is dominant, why amplification preserves the exact conditional pivot distribution, and why final verification handles all inputs. Then establish the query bound. Place the stronger retained-state proof and extended finite-budget accounting where they don't interrupt that progression.

§6

Classical lower bound

Use the dummy/planted input comparison as the motivation. The four-step summary on p. 41 already works; improve it by bringing the concrete coupling table from p. 49 closer to the beginning. Keep one complete direct-product proof prominently available, but move the alternative proof and optional search refinements out of the first reading route.

§7

Exponent conclusion

Give the fixed-
k
k argument its own clear resolution. Treat the explicit growing-
k
k schedule as a separate quantitative refinement. Explain its balancing principle before its large numerical constants.

On p. 22, for example, I would compress the repeated parameter and source descriptions before the bounded evaluator. On pp. 24–25, I would bring the drift calculation nearer the beginning. On pp. 34–35, I would make the main upper-bound result visually dominant over the table of implementation parameters.

The essential quantum mathematics stays.

Similarly, the capped simulator on pp. 51–53 is important enough to remain in the main proof. Its distinction between a joint event and an invalid conditional estimate is not peripheral bookkeeping. It's part of what makes the lower bound rigorous.

The success condition is not fewer pages. It is a main argument whose momentum survives its necessary technical details.

Deliverable 3 — Make the analytic Forrelation proof a first-class mathematical chapter
CURRENT §§8.5–8.14 · PP. 68–82

I would devote the most careful mathematical editing to this part.

It is one of the manuscript's major contributions as a reconstruction, and it currently reads partly as a chain of proof obligations.

The argument should instead have three recognisable movements.

Movement I — Construct distributions that differ in Forrelation

Introduce the uniform law and the rounded Gaussian-chain law. Explain the choice of first-block interpolation, the uniform endpoint (F16), and the positive Forrelation mean (F39).

The reader should understand the purpose of the Gaussian construction before seeing all its technical definitions.

Movement II — Show that shallow trees cannot distinguish them

Make the derivative-propagation identity (F22) the centre of the section. Show its small cases, then derive the general path formula. Explain precisely why the decision-tree derivative estimate (F25) applies, yielding the indistinguishability bound (F33).

The reader should see the connection between the geometry of the Gaussian chain and the combinatorics of an adaptive decision tree.

Movement III — Turn indistinguishability into promise hardness

Explain why neither distribution being wholly supported on the promise creates a genuine obstacle. Then give the error-reduction and acceptance inequalities, culminating in the contradictory bounds in §8.14 and the uniform conclusion (F43).

The constants should certify a contradiction the reader already understands conceptually.

One specific edit is to move the paragraph on p. 69 beginning with the construction of two distributions ahead of the detailed comparison with the Bansal–Sinha theorem.

That literature comparison is valuable. It is simply not the best way to introduce the proof.

Another is to elevate (F43), the uniform hardness estimate, to a clearly named principal theorem of the analytic chapter, with the fixed-
k
k statement as its consequence.

Finally, the 
k
=
3
k=3 derivative example on pp. 73–74 should be preceded by the simplest 
k
=
2
k=2 case, to expose the single integration-by-parts step before its iteration.

The mathematical standard here is particularly demanding: the reader should be able to explain why the derivative passes through each block, why repeated derivatives vanish, why the martingale controls the resulting sum, and why off-promise mass requires separate treatment.

If those four things become clear, the analytic section will read as a coherent proof rather than a technically accomplished sequence of estimates.

Deliverable 4 — Create a small, exceptional set of diagrams and examples
THREE CORE FIGURES, NOT A GRAPHICS OVERHAUL

The current PDF has one labelled figure, on p. 16. It is helpful, but a manuscript this structurally intricate would benefit from a few more mathematical visualisations.

I would commission exactly three central figures.

The addressed-certificate construction. Show one all-one column, its address inputs, the selected certificate cell and its outward pointers to zeros. Place it near the introduction rather than making readers wait until p. 16.

The planted coupling. Show the dummy and planted boards, indicating precisely the erased zero and the newly filled cell. The reader should instantly see why the first-difference argument has only two cases.

The Gaussian derivative chain. Show the independent Gaussian layers, Walsh transforms, block biases and one derivative passing from block to block. The diagram should help the reader reconstruct (F22), not attempt to display all its notation.

I'd also refine the examples rather than indiscriminately adding new ones.

The cyclic tournament on p. 27 should use symbolic 
ε
ε for its main explanation, with the exact numerical instantiation optional. The negative-Forrelation examples on pp. 16 and 67 should be retained because they expose the distinction between a quantum proposal and exact promise certification. The direct-product examples should be selected for their separate purposes: adaptivity, cap enforcement and the danger of conditioning on lightness.

The figures and examples must earn their space by removing conceptual work from the surrounding prose.

Deliverable 5 — Rebuild the technical and scholarly apparatus
COMPLETENESS WITHOUT NARRATIVE CLUTTER

This deliverable preserves the document's greatest existing strength: that a reader can examine the entire proof without relying solely on external theorems.

The technical material should remain in the PDF, but its placement and navigation should be more deliberate.

The first candidates for relocation or consolidation are the detailed deferred-measurement proof in §2.5, the stronger retained-state discussion in §5.6 where it exceeds the measured-label contract needed by the main algorithm, the alternative direct-product proof in §6.1, the optional search estimates in §6.7, and the extended constant calculations in §7.3.

They should not disappear. Nor should a critical proof be replaced by “standard” or “straightforward”.

The challenge is to make each supporting argument easy to find without asking every reader to study it at the moment it first becomes available.

There are also several straightforward scholarly improvements:

Adopt one local theorem and equation numbering scheme, with original preprint identifiers given as source references rather than competing labels.

Fix visible bibliography-key remnants such as BansalSinha2021, standardise citations, and correct malformed author ordering in the Göös–Pitassi–Watson reference.

Give the document a proper two-level contents page and consistently linked section references.

Put the bibliography after the mathematical appendices rather than before Appendices C–D.

Preserve the AI-use disclosure and precise credit distinctions, but let the mathematical conclusion precede the administrative end matter.

One nuance matters here: attribution should be prominent and exact, but the prose should not repeatedly remind the reader that it is a reconstruction. Once a theorem is properly attributed, the mathematical argument can be written confidently in its own voice.

Deliverable 6 — Write a genuine conclusion to the complete proof
CURRENTLY MISSING AS A UNIFIED ENDING

I would add a short mathematical conclusion after the main obligations, including the universal upper bound, have been discharged.

It should not be a generic restatement of the abstract.

It should identify what the reader has now learned about why the construction works.

The argument succeeds because the winner's outward certificate gives robust one-sided comparisons; the quantum algorithm exploits that asymmetry through a tournament with a simple weight potential; the classical lower bound turns finding the winner into discovering a hidden modification or predicting an entire hard address; and the Forrelation argument guarantees those address bits are classically difficult.

That is the mathematical story.

The conclusion should also distinguish the fixed-
k
k optimal-exponent argument from the stronger explicit growing-parameter schedule. It should make clear that the fourth power is attained as a universal upper exponent, not as an exact constant-factor 
R
=
Ω
(
Q
4
)
R=Ω(Q 
4
 ) claim from this construction.

A short conclusion of this kind would leave the reader with the essential mathematics rather than with the final technical comparison in Appendix D.

Deliverable 7 — Independent proof-integrity and reader-experience audit
THE RELEASE GATE

This final deliverable is what prevents a beautiful rewrite from accidentally becoming a less rigorous one.

The rewrite needs two genuinely different audits.

Mathematical preservation audit. Match every theorem, lemma, hypothesis and important displayed inequality against the original 94-page document. Check all quantifier orders and parameter ranges, the use of one circuit for both complexity bounds, the treatment of off-promise inputs, the distinction between exact label laws and retained quantum states, the adaptive direct-product assumptions, and the fixed versus growing 
k
k arguments.

The audit should also independently check consequential derivations, rather than assuming that preservation guarantees correctness. This rereading was an editorial and mathematical-structure review, not a line-by-line independent certification of all 94 pages.

Blind reading audit. Give the revised PDF to readers without the previous feedback. A query-complexity specialist should try the main proof route; a mathematically mature reader from a neighbouring area should test the introduction and first major proofs.

Ask them to reconstruct the argument at defined checkpoints, without prompts from the author. Record where they had to reread, chase notation or reconstruct motivation themselves.

The result should be a concrete set of remaining reading failures, not another subjective score.

What I would explicitly forbid in this revision
The editorial work should have several hard constraints.

Do not shorten the PDF to an arbitrary page count. Do not replace a genuine mathematical difficulty with motivational prose. Do not add explanatory boxes everywhere. Do not bury essential steps in an appendix simply because they are technical. Do not erase careful qualifications about promises, probability events or query caps. Do not imply that reconstructed arguments originated here.

Most importantly, do not perform another local prose-polishing sweep before deciding the structure.

Sentence polishing before the architecture is settled risks making paragraphs beautifully worded that ultimately need to be moved or removed.

The final acceptance criteria
Instead of another rating, I would use the following concrete tests.

Revision acceptance checklist

0 of 8 criteria checked


Opening

Within four pages, the reader can explain the problem, construction, principal ideas and attribution.


Construction

Each ingredient of the winning certificate has an intelligible mathematical purpose.


Quantum argument

The reader can reconstruct weight halving, winner dominance, exact pivot sampling and final verification.


Classical argument

The dummy/planted coupling and the need for a capped direct product are clear before the technical proof becomes demanding.


Forrelation

The interpolation, derivative propagation, martingale bound and promise-mass step form a coherent argument.


Completeness

All required proofs, assumptions, constants and edge cases remain available within the PDF.


Finish

Numbering, citations, diagrams, cross-references, appendix order and conclusion form one coherent document.


Independent readers

External reading tests uncover no major conceptual obstacle caused primarily by presentation.

These checks are deliberately harder to satisfy than “the prose is clearer”, because they test the reader's mathematical understanding.

The order I would execute the work
The sequence matters.

First, create the new architecture and decide which passages are retained, moved, consolidated or rewritten. Then rebuild the opening. Next, rewrite the central separation proof without sacrificing its formal guarantees. After that, give the analytic Forrelation chapter its independent, carefully designed narrative. Only then introduce the figures, consolidate the technical material, standardise the typography and references, and conduct blind reader testing.

The final product should be one integrated, mathematically complete PDF—not a collection of individually improved sections.

The deepest conclusion from all these rereadings
There's one distinction I would leave at the centre of the editorial brief.

The current paper explains an enormous number of things. A superb paper makes clear which few things explain everything else.

For this reconstruction, those few things are identifiable:

The outward certificate creates one-sided dominance. Complementary comparisons create weight contraction. The planted coupling creates two possible first differences. The capped direct product defeats adaptive address prediction. The Gaussian interpolation and martingale method supply the necessary hardness. The exponent comparison turns these ingredients into optimality.

Those ideas give the work its mathematical character.

What makes a piece of mathematical writing exceptional is not maximum concision, maximum completeness, maximum accessibility or maximum formality in isolation. It is the judgement to combine them without allowing one to destroy the others.

Some parts of the existing manuscript already have that quality.

The next revision should use those passages as its internal standard, move the best explanations to where they do the most work, remove redundant orientation, and make the exact proofs feel like the natural completion of ideas the reader already understands.

That's the mandate I would now hand to the editorial team: preserve the full mathematics, but rebuild the experience of discovering it.

Not another pass to make the existing 94 pages marginally nicer. A properly composed, final mathematical reconstruction whose clarity comes from the architecture of the argument itself.





