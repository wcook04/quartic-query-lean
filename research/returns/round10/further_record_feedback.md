

reasoning_record(2).pdf
PDF
read attached give feedback on this paper how well is it written for its intended audience give a papers worth of feedback im gonna folow this up with several "reassess again" so your initial response will not be the final one goign back so i guess plan what your subsequent go thorugh is gonna be i guess lets start high level

Worked for 6m 18s
Editorial review — Round 1: High-level assessment
Manuscript: A Nearly Quartic Separation Between Randomized and Quantum Queries: A Complete Reasoning Record · 140 pages · 4 November 2026

1. Overall verdict
This is a strong technical reconstruction and mathematical audit record, but it is not yet as effective a piece of mathematical communication as its underlying work deserves.

Its greatest strength is its precision. Its greatest weakness is that it gives the reader an enormous amount of information without sufficiently distinguishing what is essential, what is explanatory, what is supplementary, and what is merely evidence about the development process.

Those are different problems from whether the mathematics is correct.

The manuscript is unusually serious about making its assertions inspectable: definitions are fixed carefully, proof obligations are enumerated, small examples test subtle conventions, historical sources are distinguished, and formal verification evidence is qualified rather than presented as an undifferentiated guarantee.

But a specialist reading it for the first time must still work too hard to determine exactly what the document contributes, which portions deserve their attention, and where the deepest mathematical ideas occur.

My central editorial recommendation is to preserve the mathematical completeness while radically improving the hierarchy of information. I would not begin by cutting proofs or simplifying technical definitions. I would begin by making the existing mathematics easier to navigate, understand and independently evaluate.

2. How well does it serve its intended audience?
The title, reading guide and appendices indicate that this is primarily a reasoning record: a document for experts who want to reconstruct, scrutinize or independently check the nearly quartic randomized-versus-quantum query-complexity separation.

It is based on OpenAI's original 5 October 2026 preprint, which I located in the official OpenAI mathematical preprint repository. 

GitHub

That distinction matters enormously when grading the writing.

As a detailed mathematical reasoning record

8/10
It has substantial depth, useful proof-level explanations, explicit technical safeguards and an unusually thorough accounting of evidence.

As an exposition for query-complexity specialists

6.5/10
The mathematics is presented carefully, but the conceptual argument is often submerged beneath implementation detail, quantitative bookkeeping, and repeated qualifications.

As a first-contact paper for a busy expert

5.5/10
The opening gives the result and some intuition, but the contribution and significance of this particular reconstruction are not established sharply enough before the reader encounters considerable technical complexity.

These are provisional editorial assessments, not scores for mathematical correctness, novelty or the reliability of the Lean implementation. I have not independently checked the full proof or rerun its formal verification.

The document also serves several audiences simultaneously:

Reader

What they chiefly need

Current fit

Query-complexity researcher

Understand the separation mechanism and check the crucial proof steps

Good, but inefficient

Quantum-algorithms specialist

Understand the tournament, amplification, coherent access and query accounting

Detailed and substantially helpful

Lower-bound specialist

Inspect the hard distribution, direct product and Forrelation argument

Strong technical coverage, but demanding

Lean/formal-methods expert

Compare mathematical statements, formal types and checking evidence

Strong, though the evidence history is cumbersome

Researcher deciding whether to engage

Understand what was achieved, what's distinct from the original, and what remains unreviewed

Needs major improvement

I would judge the manuscript primarily by the first four audiences, not by its accessibility to beginners.

But even among specialists, being able to verify an argument and being able to understand it efficiently are different qualities. A mature exposition should deliver both.

3. What the paper does particularly well
A. The precision is real, not just stylistic
Sections 2, 4, 5 and 6 consistently distinguish mathematical assertions that are easy to conflate.

The distinction between the promise domain and an arbitrary off-promise output is carefully maintained. The distinction between a worst-case cap and expected query cost is also explicit. The quantum sections distinguish an output distribution from a retained coherent state. The classical lower-bound section correctly identifies why a bound on a joint event is different from a bound after conditioning on that event.

These distinctions matter because each one is a possible failure point in a proof of this kind.

The two-bit OR and parity examples in §2.6 (pp. 10–12) are especially worthwhile. They do not exist merely to make the work feel accessible. They test whether the model conventions actually mean what the document claims they mean.

This is one of the best features of the writing: the examples often explain why a particular hypothesis is necessary, rather than merely illustrating a theorem after the fact.

B. It repeatedly addresses the most natural objections
Some of the clearest passages are those that anticipate a specialist's questions.

In §4.7 (p. 22), the argument explains why a genuine winner survives comparison with an opponent whose decoded address may be meaningless.

In §5.2 (pp. 28–34), the tournament proof explains why complementary comparison probabilities suffice even when losing candidates form cycles. The fractional-weight calculation is a particularly elegant piece of the underlying argument.

In §6.1 (pp. 42–48), the direct-product discussion makes the adaptive-query issue precise and supplies examples showing what fails when independence or conditioning is handled incorrectly.

And in §8.15 (p. 85), the source attribution distinguishes the earlier Gaussian and martingale methods from the modifications used in this reconstruction.

These passages demonstrate a sophisticated understanding of what a serious reader might question. They also show that the paper has a sound basis for being genuinely explanatory, not merely exhaustive.

C. The modular proof structure is fundamentally good
The architecture is sensible:

§3 and §8

Hard partial-function ingredient

§4

Total addressed-certificate function

§5 Quantum algorithm

Q
(
F
)
≲
m
 
p
o
l
y
l
o
g
(
m
)
Q(F)≲ 
m
​
 polylog(m)
§6 Classical lower bound

R
(
F
)
≳
m
2
−
1
/
k
/
(
log
⁡
m
)
2
R(F)≳m 
2−1/k
 /(logm) 
2
 
§7 The exponent calculation

2
−
1
k
  
/
  
1
2
=
4
−
2
k
2− 
k
1
​
 / 
2
1
​
 =4− 
k
2
​
 
The central dependency structure, simplified for exposition. Appendix A supplies the previously known universal upper bound.
That is an appropriate structure for the proof. The reconstruction establishes the common function, proves each complexity bound, and then combines them. It also delays the complete proof of the Forrelation ingredient until §8, allowing a reader to understand the reduction before studying the hardest analytic prerequisite.

I would retain this architecture.

What needs improvement is the visibility of this architecture. The manuscript explains it in prose, but it takes too much effort to hold it in mind across 140 pages.

D. The treatment of verification evidence is unusually responsible
Appendices F and G are among the document's most distinctive contributions.

In particular, the text does not simply say that Lean checked the entire paper. It distinguishes compiled statements, configured comparisons, mathematical-fidelity review, ordinary derivations, and claims without human review.

Appendix G.4 also acknowledges differences between headline checked theorems and stronger quantitative assertions, including the explicit Forrelation threshold.

That is valuable. A formal proof checker establishes that a particular statement follows from particular definitions and assumptions; establishing that those definitions correspond to the intended mathematics is a separate task.

The manuscript takes that distinction seriously.

My criticism is not that the evidence is described too carefully. It is that its most important implications are not presented compactly enough for an expert approaching the project for the first time.

This could become one of the paper's defining strengths with better editorial organization.

4. The major weaknesses
A. The contribution of this particular document needs to be much clearer
Highest editorial priority
The opening establishes that OpenAI's preprint proves the separation. It also identifies the numerical refinements, the independent Forrelation derivation and the Lean formalization.

But these are presented together rather than being distinguished according to their mathematical and scholarly roles.

A first-time reader needs immediate answers to four questions:

What was already proved? The nearly quartic separation, its construction, and its quantum and randomized analyses are attributed to OpenAI's original manuscript.

What does this reconstruction establish? The document supplies full ordinary derivations of the arguments it uses, including detailed treatment of the partial-function ingredient and the universal upper bound.

What has been added? Among the identifiable additions are explicit constants, a quantitative Forrelation hardness threshold, a particular direct analytic derivation, finite worked examples, and the formalization and statement audit. Their precise novelty relative to the wider literature is a separate question.

What was checked, and to what extent? Some statements have compiled Lean proofs and specified comparison evidence; other assertions, particularly certain quantitative refinements, rely on ordinary derivations rather than corresponding checked declarations.

The document does eventually answer these questions, especially in §8.15 and Appendices F–G.

The problem is their distribution.

A mathematician should not have to read most of the record to understand the identity of the work they are evaluating.

I would introduce a short section immediately after the opening called “Scope and contributions of this reconstruction.”

It should distinguish reconstruction, additions, formal verification, source comparison, and unreviewed material.

This would materially improve the credibility and intelligibility of the entire document without changing any mathematics.

B. It explains the argument more thoroughly than it explains why the argument works
This is the biggest pedagogical weakness.

The manuscript carefully takes the reader through each mechanism. But it does not always foreground the conceptual reason that mechanism is useful.

Consider the essential separation.

Classically, the difficulty comes from the need either to find an erased zero or to identify a planted certificate whose address encodes many hard answers.

Quantumly, the algorithm does not have to discover the winner by exhaustively finding valid certificates in all columns. Instead, its comparison procedure makes a true winner dominant, and the weighted tournament rapidly reduces the set of candidates that need expensive verification.

That asymmetry is the essential innovation of the construction.

Section 1.1 explains it, but the document needs to make it the organizing principle of the entire proof. Every major technical section should explain how its main result strengthens one side of that asymmetry.

For example, §5 should make the reader understand why a tournament with unreliable comparisons is sufficient before entering the amplification implementation and exact probability-law arguments.

Section 6 should make the reader understand the two ways a planted winner might be discovered before the direct-product and capped-simulator details.

And §8 should explain the fundamental analytic obstacle in proving the Forrelation lower bound before introducing the detailed interpolation and martingale calculations.

The existing introductions often do part of this. They should do more.

The aim is not to replace the proofs with intuition. It is to make the reader know what each proof is trying to accomplish before reading it.

C. Technical rigor and expository detail are not sufficiently separated
The paper has a habit of placing several levels of explanation into the same passage.

A passage may simultaneously establish a theorem, explain a possible misconception, account for an exact constant, identify a Lean declaration, discuss a source version, and distinguish a historical checker from a newer one.

Each of those may be relevant. Together, they make the argument difficult to read continuously.

A good example occurs in §5.4 (pp. 38–40). The section transitions from the coherent implementation and conceptual query bound into detailed integer-budget accounting, including very large parameter-dependent constants.

That accounting is valuable for reproducibility and formal verification.

But a reader following the main quantum proof has already received the central result. The exact arithmetic is now a different task.

I would establish a consistently recognizable separation between:

the essential mathematical argument;

the complete technical justification;

quantitative and implementation refinements;

checking and provenance evidence.

The technical material can remain fully available. In many cases, merely moving a derivation into a clearly named optional subsection would be enough.

There is a significant difference between a proof that is complete and a proof that requires every reader to process every detail before reaching its conclusion.

The current manuscript sometimes treats those as the same thing.

D. Repetition is becoming an obstacle
I noticed repeated explanations of the same safeguards throughout the main text.

The reader is repeatedly reminded that query caps apply on every branch, that off-promise decoding remains defined, that both complexity bounds concern the same function, that certain formal results establish only output laws, and that a particular construction does not depend on an external theorem.

These qualifications are important. Some repetition is necessary, especially in sections designed to stand alone.

But there is a point at which repeated defensive clarification starts to obscure the primary line of reasoning.

For instance, once the query-model contract is clearly established in §2 and the common-function contract is fixed in §4, later sections can often refer concisely to those contracts.

That is preferable to repeatedly restating the entire justification.

I would perform a dedicated redundancy pass, distinguishing repetitions needed for standalone readability from repetitions that simply recreate previous paragraphs.

This could substantially improve the text without removing a single mathematical claim.

E. The paper sometimes sounds like a project audit rather than a mathematical publication
This is especially visible in passages referring to retained returns, historical snapshots, earlier edits, checker receipts and other project-specific terminology.

For example, §4.4 (p. 20) refers to preserved round-three checking output. Section 5.2 (p. 29) contains an instruction to return to a section of the specialist companion within the exposition of a proof.

Appendix F contains detailed information about previous snapshots, source hashes and differences between receipt labels.

All of that has a place in the project's evidence record.

But it should not frequently interrupt the mathematical argument.

Academic prose should remain intelligible even after the development history is forgotten.

A useful editorial test is:

Would this sentence still be natural to a mathematician encountering the paper for the first time in two years?

If the answer is no because it refers to a particular revision, review packet or integration round, the sentence probably belongs in a dated verification appendix or provenance file.

I would not discard that historical information. I would separate the timeless mathematical exposition from the time-dependent evidence history.

F. The length is defensible, but the document needs better layering
The manuscript is approximately 67,000 words over 140 pages.

That is a substantial undertaking, but I would not call it inherently too long for a complete reconstruction and formal statement audit of a major technical result.

The issue is how those pages are distributed.

Portion

Pages

Editorial assessment

Introduction and model conventions

1–12

Thorough, but could orient specialists faster

Construction and two complexity bounds

13–59

Central material; conceptually demanding

Exponent and independent Forrelation proof

60–84

Important mathematical content

Universal quartic upper bound

85–90

Useful self-containment

Claim catalogue and references

91–115

Valuable reference material

Historical and source comparisons

116–119

Important but secondary

Execution history and formal evidence

120–140

Valuable audit, different reading task

The most obvious structural improvement would be to give the reader three layers.

The first would be a short, precise account of the complete argument, perhaps five to eight pages, designed for a specialist to understand the proof architecture.

The second would be the existing detailed mathematical reconstruction, with all important lemmas and calculations.

The third would be the formal evidence, catalogue, historical comparisons and reproducibility material.

These layers could all remain inside one PDF. The existing 98 PDF bookmarks and numerous internal links already provide useful navigation. The missing element is primarily a hierarchy of conceptual importance, not clickable navigation.

There is also a reasonable case for retaining this master record and maintaining the specialist companion and examples-first exposition as distinct entry points, as the reading guide already proposes.

I would avoid forcing all three documents into the same style.

5. Specific features I would improve before line editing
A real abstract and better front matter
The first page currently begins with the title and explanatory paragraphs rather than a conventional abstract and author/version block.

For a technical research-facing document, I would use a clear title, author and contribution statement, date, version, and an abstract that communicates the result and the reconstruction's purpose.

The opening should also distinguish the original theorem from the new explanatory and verification work.

This is a relatively small alteration with a large effect on first impressions.

A compact mathematical roadmap
The paper needs a one-page illustration of the construction.

It should show a column containing its 
X
i
X 
i
​
  string, its 
r
r partial-function instances, the address they determine, the selected certificate cell, and the outgoing pointers.

Then show what changes when a winner is planted and why the quantum and classical algorithms encounter different difficulties.

The four-column example in §4.3 is excellent raw material, but the reader reaches it only after considerable formal development.

A visual should precede the full example.

I would also add a small table of parameters, defining 
k
,
m
,
t
,
r
,
L
,
K
,
G
k,m,t,r,L,K,G, showing their orders of magnitude and identifying where they enter the proof.

Less prominence for exact constants in the opening
The threshold 
t
≥
13669
k
2
t≥13669k 
2
 , logarithmic exponent six and coefficient 
1
/
400
1/400 demonstrate quantitative completeness.

But for a first-time reader they are not the main intellectual result.

They are currently prominent on page 1. I would introduce them briefly as quantitative refinements and move the numerical details to a dedicated results paragraph or theorem after the conceptual account.

Experts will appreciate their availability. They do not need them before understanding the construction.

A more compact statement of formal evidence
The final appendices make some important distinctions: the headline comparison targets, the explicitly quantified results with separate Lean build evidence, and the ordinary-only refinements do not all have identical status.

Rather than forcing readers to reconstruct that distinction from the appendices, I would supply one compact status matrix near the front.

The matrix should give the mathematical claim, its exact formal counterpart, whether it is in the headline dependency closure, the relevant checking evidence, and any limitation.

The explicit threshold without a matching Lean statement is an example of information that should be easy to discover.

This would also help prevent readers from mistaking the intentional sorry placeholders in specification files for admitted proof gaps in the compiled solution.

More selective inclusion of source disputes
The historical analysis of Bansal–Sinha's displayed estimates and the factor-two adversary prefactor comparison are potentially interesting.

The manuscript is careful not to infer that the cited results are false merely because a displayed step appears problematic. That restraint is important.

Nevertheless, such observations draw attention and can distract from the principal theorem.

I would keep these investigations in a clearly separate source-audit section. Any externally communicated correction should receive its own especially rigorous independent review.

They should support the reconstruction's reliability, not become competing narratives.

6. What I would preserve
There is a risk in revising a document like this: making it shorter or smoother could destroy the details that make it valuable.

I would particularly protect the exact model conventions in §2, the gate-consistency and local-verification proofs in §4, the complementary-weight tournament calculation in §5.2, the adaptive direct-product and simulator arguments in §6, and the source-precise analytic derivation in §8.

I would also protect the distinctions in Appendix G between a compiled theorem, a configured comparison, a semantic interpretation and an ordinary proof.

Those are not incidental details. They are central to the purpose of a reasoning record.

The best revision would be subtractive in repetition, additive in conceptual explanation, and conservative in mathematical content.

7. The order in which I would revise it
First: resolve the document's identity

Establish exactly what the paper is, who should read it, what the original preprint established, what the reconstruction adds and what the verification evidence supports.

Second: improve the conceptual proof structure

Add a concise main-argument synopsis, one construction diagram, a parameter table and short explanations of each crucial proof mechanism.

Third: separate mathematical exposition from auditing detail

Preserve the detailed proofs, but move repetitive constants, historical process information and evidence bookkeeping into identifiable supplementary sections.

Fourth: edit at sentence and paragraph level

Only after the argument has the right hierarchy would I optimize mathematical prose, cross-references, notation, paragraph structure and typography.

Doing the sentence editing first would be inefficient. Much of it would need to be repeated after structural changes.

8. How I propose to handle your subsequent “reassess again” requests
I would treat the coming reassessments as progressively more demanding reviews, rather than simply rereading the manuscript and adjusting a score.

Here is the sequence I would use.

Round 2 — Cold-reader reconstruction. Read as a query-complexity specialist who has not participated in the project. At each important transition, ask whether the motivation, statement, assumptions and proof dependencies are clear. Identify the first point at which a competent reader is likely to lose the argument. Reassess the scores from Round 1.

Round 3 — Adversarial mathematical exposition review. Focus on the tournament's conditional sampling law, returned-state guarantees, the capped direct-product proof, the planted-cell simulator and the quantitative Forrelation argument. Distinguish a writing problem from a potentially missing mathematical justification. Compare important claims with their cited primary sources.

Round 4 — Formalization and evidence review. Inspect the exact correspondence between paper statements, formal definitions, headline proof roots, independently checked statements and ordinary-only arguments. Where the source and receipts are accessible, examine them directly. Look for overstatements and understated limitations.

Round 5 — Section-by-section editorial review. Work through every major section at paragraph level, identifying redundancy, awkward ordering, insufficient motivation, notation overload, unnecessary qualifications and places needing worked examples. Give concrete suggested rewrites.

Round 6 — Skeptical external-review simulation. Assess what a serious specialist would regard as established, unclear, genuinely valuable, unsupported or excessively burdensome. Compare the manuscript with the conventions and standards of specialist mathematical exposition.

Round 7 — Consolidated editorial judgment. Reevaluate all earlier feedback, explicitly withdraw criticisms that fail on closer reading, distinguish essential revisions from optional improvements, and produce a definitive prioritized revision specification.

For each reassessment, I would maintain three distinctions: confirmed textual weaknesses, plausible but unconfirmed mathematical issues, and matters of editorial preference. They should never be treated as equivalent.

I would also actively challenge my previous assessments. For example, the more closely I examine the technical proofs, the more I may decide that particular repetitions or technical detours are essential. Other apparent strengths may turn out to conceal problems. The scores should be allowed to move in either direction.

9. Final judgment for Round 1
The writing is considerably stronger than a generic AI-generated technical exposition. It contains precise mathematical reasoning, carefully explained edge cases, extensive cross-references, concrete examples and unusually nuanced evidence qualifications.

Its weakness is not superficial prose quality. Most individual paragraphs are grammatically sound, professional and appropriately mathematical.

The weakness is editorial architecture.

The manuscript has been optimized much more for completeness and defensibility than for the efficient transmission of mathematical understanding.

That is understandable in a reasoning record, particularly one accompanying formal verification of an AI-produced result. But it is not inevitable. It can be both exhaustive and substantially easier to read.

I would not attempt to reduce this to an ordinary short research paper. I would preserve the complete record and build a clearer path through it.

My provisional conclusion is that the mathematical exposition has a strong foundation, and the most valuable work now is deciding what the reader needs to understand at each point, rather than adding still more detail.

The next reassessment should test this conclusion against the actual proof, not simply accept it.

another pass read through

Worked for 4m 42s
Reassessment 2 — A closer reading
My assessment has improved after this second pass. I think I was too harsh about some aspects of the paper's organization, although I've also identified more precise weaknesses that matter for its intended audience.

The manuscript is better designed as a complete mathematical reasoning record than my first review gave it credit for. Its main weakness is not a general absence of structure. It is that the structure is optimized for finding, reconstructing and verifying claims, while sometimes making the intellectual argument harder to absorb.

1. What I would change from my first assessment
Mathematical reasoning record

8/10

8.5/10
Exposition for specialists

6.5/10

7.5/10
First-contact readability

5.5/10

6.5/10
Revised provisional editorial ratings, not an independent certification of mathematical correctness or formal verification.
I would revise three of my earlier criticisms.

First, the navigation is actually quite good. Pages 1–2 establish four explicit reading routes, and page 2 identifies individual questions with direct links to their answers. There are also well-positioned local statements, explanations of which sections can be skipped, and an extensive claim catalogue. I understated how deliberately this was designed. 
reasoning_record(2).pdf

Second, the project-audit material is more contained than I suggested. Most historical receipts, source revisions and comparison details already live in Appendices F and G. There are a few distracting references in the main proof, but I would withdraw the suggestion that project history generally overwhelms the main mathematics.

Third, the opening is stronger than I initially implied. Its explanation of the hidden certificate, the winner's outward pointers, and the difference between classical and quantum discovery is relatively compact and effective. It is not simply a theorem followed by a wall of formal notation.

What survives my first critique is more specific: the paper has excellent local explanations but sometimes insufficient global synthesis. A reader can understand many individual steps without necessarily understanding, early enough, how those steps combine into the central achievement.

That is now my principal editorial diagnosis.

2. Where the manuscript is strongest on closer examination
The mathematical models are explained exceptionally carefully
Section 2 (pp. 5–12) is better than I first appreciated.

The distinctions between total and partial functions, finite random mixtures, worst-case depth, quantum output mass and coherent state preservation are not just defensive qualifications. They establish a foundation needed by the construction.

The two-bit OR example is particularly good. It shows why an inclusive success probability of 
2
/
3
2/3, arbitrary biased coins and a worst-case query cap are genuine mathematical choices, not harmless conventions. The parity and promise examples similarly expose how alternative definitions change the problem.

For a reader unfamiliar with query complexity, this section is demanding. For someone auditing an exact formalization of query complexity, it is very useful.

I would preserve virtually all of §2. My only substantial recommendation is to provide a more compact definition table for experienced readers who already know the standard model.

The quantum tournament is among the best-explained technical ideas
Section 5.2 (pp. 28–34) is probably one of the paper's strongest sections.

The central identity is unusually clean:

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
It gives the specialist a satisfying reason the procedure works. The comparison probabilities need not define a transitive ordering; complementarity is enough for expected weight to decrease.

The paper then explains why the quantum sampler produces the precise probability distribution required by this argument, not merely an arbitrary successful candidate. The cyclic tournament example strengthens that explanation.

This is good mathematical pedagogy because it works at three levels: the algebraic identity, the algorithmic interpretation and a finite counterexample to an unnecessary assumption.

The weakness is one of presentation. The reader must move between the abstract weight process, coherent preparations, amplification, coupling and physical-query accounting.

I would make the sequence clearer:

The weights are an analytical device. They are not computed. The quantum algorithm instead samples from exactly the distribution they define.

That sentence captures a central insight that deserves more prominence.

The classical lower bound is also stronger pedagogically than I first judged
Section 6.1 (pp. 42–48) is particularly impressive as an explanation of the direct-product issue.

It doesn't simply quote the claim that independent instances remain hard when queries are adaptively distributed. It follows the conditional distributions after each query, identifies why one factor changes at a time, and derives the product bound.

The distinction between

Pr
⁡
(
success
∩
cap respected
)
Pr(success∩cap respected)
and

Pr
⁡
(
success
∣
cap respected
)
Pr(success∣cap respected)
is handled with unusual care, including examples showing why the latter cannot be substituted for the former. That distinction becomes essential in §6.5.

This is the kind of mathematical exposition that can prevent a reader from making a subtle but serious mistake.

However, the reader reaches the direct-product proof before seeing the complete planted-input construction in §6.3.

The introductory outline on p. 42 helps, but I still think the ordering could be more effective.

I would present a short, concrete account of the coupling and the two possible discoveries before proving Lemma 4.1. A specialist should be able to picture the lower-bound experiment before spending several pages on the abstract direct-product tool.

Section 8 deserves more prominence
My most important positive finding from the second reading concerns §8 (pp. 63–85).

This section is more than a routine appendix deriving an imported estimate.

It develops an independent proof of the required Forrelation hardness, using a specified bounded Gaussian transform, an interpolation through the Gaussian chain, a raw-derivative estimate along adaptive decision trees, and the moment estimates needed to obtain a promise lower bound.

The proof's structure is:

Gaussian-chain distribution
↓
Derivative path identity (F22)
↓
Decision-tree derivative bound (F25)
↓
Indistinguishability (F33)
↓
Promise-mass estimates (F36), (F39)
↓
Hardness estimate (F43).
Gaussian-chain distribution
↓
Derivative path identity (F22)
↓
Decision-tree derivative bound (F25)
↓
Indistinguishability (F33)
↓
Promise-mass estimates (F36), (F39)
↓
Hardness estimate (F43).
​
 
That is a substantial mathematical argument. Its relation to Bansal–Sinha and Girish–Tal–Wu is carefully attributed in §8.15. 
reasoning_record(2).pdf

The manuscript already gives this dependency chain in prose on p. 72. I would make it much more visible.

I would also explain the motivation for the particular functions 
φ
φ and 
Ψ
Ψ in §8.7. Their required properties are established, but a reader interested in the derivation will naturally wonder how that construction was discovered.

There is an important pedagogical distinction between proving that a cleverly chosen function works and explaining what properties led one to choose it.

Even a short paragraph describing the design constraints would add value.

3. The main weakness is now more precisely identifiable
After examining the full proof architecture, I would describe the problem as insufficient separation between the principal mathematical insight and the complete verification of that insight.

This appears differently across the manuscript.

Section

Main intellectual achievement

What obstructs a first reading

§4

A total function whose unique winner has locally checkable certificates

Too many representation and circuit details before the whole construction feels intuitive

§5

A dominant winner can be found using unreliable comparisons

Abstract sampling, amplification and physical implementation require simultaneous attention

§6

A classical algorithm rarely encounters either planted change

The direct-product machinery arrives before the complete motivating experiment

§7

The two complexity bounds force exponent four as the universal infimum

Quantitative constants and the growing-
k
k refinement compete with the short central conclusion

§8

A direct Forrelation hardness proof via a Gaussian chain and tree derivatives

Technical ingenuity is harder to appreciate than the complete derivation is to locate

Appendix G

Precise correspondence between mathematical claims and formal evidence

The reader must assemble several different evidence statuses

The common problem is not imprecise mathematics. It is that a complex mechanism is often presented in nearly the order required to prove it, rather than the order most effective for understanding it.

I do not recommend sacrificing the proof order entirely. But short conceptual introductions could do substantially more work.

4. The formal evidence section is a genuine strength — with an important limitation
This is where my assessment changed most significantly.

Appendix G is much more nuanced than a conventional statement that an AI-produced mathematical result was checked in Lean.

It distinguishes the main four configured unconditional comparisons, separately built but un-compared declarations, results established in ordinary mathematics, and mathematical-fidelity assessments of formal definitions.

It also makes clear that agreement between two modules sharing the same specification does not establish that their specification models the intended mathematical problem.

The deliberately bad shared-specification control on pp. 129–130 is especially valuable. It demonstrates that two separately compiled proofs can agree on an incorrect or vacuous specification.

That is exactly the right concern to raise when assessing formal verification.

The appendix is also explicit about genuine remaining boundaries.

For example, §G.7 distinguishes the measured-label amplification route used by the headline quantum proof from the stronger physical successful-state correspondence. The manuscript says that the latter still lacks a complete formal bridge, while explaining that this is not an extra unproved assumption of the headline Proposition 3.3 proof.

The explicit threshold 
t
≥
13669
k
2
t≥13669k 
2
  likewise has an ordinary derivation but no corresponding Lean statement. The named-family bound with logarithmic exponent six has build and axiom evidence but is not one of the four configured unconditional comparison targets. 
reasoning_record(2).pdf

This is excellent intellectual discipline.

But the evidence hierarchy is not obvious enough until the reader reaches the final pages.

I would put a compact version near the beginning:

Evidence category

What the paper reports

Configured comparisons

Four unconditional headline targets, alongside separately compared supporting statements

Built and axiom-audited

Additional quantitative and component results, with narrower comparison status

Ordinary derivation only

Certain refinements and bridges, including the explicit hardness threshold

Human mathematical review

None claimed

This would dramatically reduce the effort required to understand what “formalized” means in this particular project.

It would also protect the paper against an unfair reading in either direction: one that treats the whole argument as unverified, or one that mistakenly attributes the strongest possible Lean status to every paragraph.

5. A few concrete editorial problems I now consider worth fixing
The dual numbering convention is unnecessarily costly. The manuscript preserves theorem numbering from the original preprint while using its own section numbering. This is explained on p. 5, but seeing Lemma 4.1 discussed in §6.1 or Proposition 3.2 in §5.2 still imposes cognitive friction.

I would consistently distinguish “OpenAI's Lemma 4.1” from the record's sections, or give each theorem a local identifier while retaining the original numbering in parentheses.

Some cross-document instructions interrupt the mathematics. On p. 29, during the proof of the tournament theorem, the text directs readers back to §3.2 of the specialist companion. That is an odd instruction inside the proof of a self-contained record. It belongs in the reading guide, not in the middle of the argument. Similar navigation notes should be checked individually.

The exact quantitative accounting sometimes outlives its immediate purpose. Section 5.4 establishes the essential 
m
m
​
 -scale quantum bound and then continues with substantial numerical accounting on pp. 39–40. That material is justified by the record's verification goals, but would read better as an explicitly optional quantitative derivation.

The growing-parameter refinement deserves a stronger introduction. Section 7.3 establishes a family with 
k
k growing and an exponent tending to four. This is a meaningful refinement of the fixed-
k
k formulation, not merely another constant calculation. Its conclusion should be given prominence before the long arithmetic supporting it.

The front matter should identify the document more formally. The first page is already a competent summary of the mathematical argument. I would not replace it wholesale. But a conventional author/date/version block, clearer distinction between the original preprint and the contributions of this reconstruction, and a concise statement of verification scope would improve its reception.

6. What I would not do
I would now argue against several tempting edits.

I would not remove the detailed query-model section. I would not eliminate the worked examples simply because experts already know some of the general phenomena. I would not compress the direct-product proof to a citation. And I would not discard the extensive formal-evidence appendices.

Nor would I try to make every page accessible to someone with no background in quantum query complexity.

The intended reader is mathematically sophisticated. That reader can handle serious notation and long arguments.

The goal should be to make that sophistication productive rather than requiring the reader to reconstruct the overall motivation repeatedly.

I would also be cautious about cutting material solely to make the paper resemble a conventional journal article. This manuscript serves a distinct purpose: preserving a complete mathematical account and the limits of its verification.

7. Revised conclusion
My view is now that the paper is very well written for an expert who explicitly wants a complete reasoning and verification record, and reasonably well written for a specialist who wants to learn the result.

It is less successful for a busy mathematician deciding whether to invest that much effort in it.

Importantly, the latter weakness can be addressed without compromising the former strength.

I see three changes offering the greatest return: a precise one-page contribution-and-evidence summary; a short, genuinely conceptual proof synopsis that distinguishes the quantum and classical mechanisms; and better signposting at the beginning of the difficult sections, especially §§5, 6 and 8.

I would now put far less emphasis on shortening the manuscript overall.

My updated diagnosis is that the problem is not excessive detail, but insufficient prioritization of detail.

For Round 3, the most valuable next step is an adversarial mathematical reading of §§5–8. I would specifically test whether the tournament's successful-label law is explained at the right level, whether the capped simulator's event inclusion is clear and justified, whether the Forrelation derivation can be followed without unexplained conceptual jumps, and whether the formal statements support exactly the claims the prose attributes to them.

That is where we can distinguish merely demanding exposition from places where even an expert could reasonably get confused about the argument itself.

again another pass

Worked for 6m 33s
Reassessment 3 — An adversarial reading of the mathematics and its exposition
My overall assessment remains positive, but this pass has identified a more important structural weakness than either of my previous reviews.

The mathematical reasoning is often exceptionally careful. The problem is that the manuscript occasionally gives its most detailed treatment to a statement stronger than the main theorem actually needs, before giving the reader the simpler statement that drives the main proof.

That distinction matters for expert readers. They are trying to determine not only whether each argument is justified, but also which arguments are indispensable.

1. The clearest example: quantum amplification
§5.1, pp. 25–28; Appendix G.7, pp. 134–137

Section 5.1 proves a detailed bounded-amplification result with an exact successful-state guarantee. It considers a unitary preparation 
A
A, a success projector 
Π
Π, and the normalized success component

g
=
Π
A
∣
0
⟩
p
,
p
=
∥
Π
A
∣
0
⟩
∥
2
.
g= 
p
​
 
ΠA∣0⟩
​
 ,p=∥ΠA∣0⟩∥ 
2
 .
The argument establishes that when amplification succeeds, the designated original register returns in state 
g
g, up to a global phase. This is stronger than merely preserving the probability distribution of a subsequent measurement.

The presentation is mathematically purposeful: it treats the two-dimensional Grover geometry, random iteration counts, the predetermined worst-case cap, and the retained workspace.

But Appendix G.7 makes an important distinction. The headline quantum upper bound uses the measured-label amplification route. The stronger returned-state result is separately developed; its complete physical formalization has a remaining bridge concerning the designated output subsystem.

The manuscript is transparent about this. That is a strength.

However, the main exposition makes the specialist read through substantial returned-state machinery before reaching the tournament, even though the theorem's essential operational requirement is an exact conditional distribution over successful labels.

I would reorganize the presentation into three layers:

State the bounded-amplification contract and the conditional successful-label law needed by the tournament.

Prove the tournament and the quantum upper bound using that law.

Give the full successful-state construction as an independently valuable strengthening, with its precise formal status.

This is not a suggestion to remove §5.1. Its derivation is valuable.

It is a suggestion to stop making the reader treat a stronger auxiliary result as the conceptual gateway to the central theorem.

The same problem occurs elsewhere in the manuscript, though usually less dramatically.

2. The classical lower bound survives the main conceptual checks
§§6.1–6.6, pp. 42–57

I looked more closely at the point where the lower-bound proof is most vulnerable to an illegitimate probabilistic shortcut.

The planted input differs from the dummy input only in two places: the erased zero and the newly filled certificate cell. The first-difference argument reduces the lower bound to showing that a short classical computation rarely encounters either location.

The erased-zero argument is relatively intuitive. The certificate-cell argument is subtler because the algorithm's decision to query a particular cell may depend on information already gathered about the hard address inputs.

The key step is equation (21):

Pr
⁡
[
column 
i
 is nonheavy
  
∧
  
query 
q
 visits 
B
i
,
s
i
]
≤
(
2
/
3
)
r
.
Pr[column i is nonheavy∧query q visits B 
i,s 
i
​
 
​
 ]≤(2/3) 
r
 .
What matters here is the joint event. The proof does not assume that the inputs remain independent after conditioning on the algorithm's entire run being nonheavy.

Instead, it constructs a simulator that enforces the query allowance before an excess query would occur. The event on the left implies that the simulator outputs the correct address, so it is contained in the simulator-success event, whose unconditional probability is bounded by the direct-product lemma.

I checked the argument's logical organization against the assumptions stated in §§6.1–6.5. In particular, the simulator receives outside data jointly independent of the target address inputs, and its query cap holds for all executions rather than only selected easy ones.

I did not find an error in this event-inclusion argument.

In fact, the manuscript does something pedagogically valuable: it supplies examples demonstrating why conditioning on nonheaviness would be invalid.

My editorial criticism is more focused than before. The proof could make its central reduction much easier to see by displaying the following implication before the simulator's detailed implementation:

Light dummy execution queries the true cell
⟹
capped simulator outputs the true address
⟹
an algorithm correctly predicts 
r
 hard answers
.
​
  
Light dummy execution queries the true cell
⟹capped simulator outputs the true address
⟹an algorithm correctly predicts r hard answers.
​
 
That is the conceptual heart of the certificate-cell lower bound.

The current proof establishes it, but the reader has to extract this structure from several paragraphs of operational detail.

This section is therefore a strong example of good mathematical reasoning that could be more immediately intelligible without being shortened.

3. A significant distinction in the parameter argument
§§6.6, 7.3 and 8.14

This is one of the most important findings of the third pass.

The paper uses two different quantitative forms of Forrelation hardness.

Fixed-
k
k route

Growing-
k
k route

Purpose

Exclude every universal exponent below four

Construct one family whose exponent tends to four

Hardness allowance

L
=
⌊
m
1
−
1
/
k
/
(
log
⁡
2
m
)
2
⌋
L=⌊m 
1−1/k
 /(log 
2
​
 m) 
2
 ⌋

L
=
⌊
X
⌋
L=⌊X⌋, using the uniform bound (F43)

Main sufficient condition

t
≥
13669
k
2
t≥13669k 
2
 

15
k
+
2
≤
2
t
15k+2≤2t, plus conditions ensuring 
L
≥
1
L≥1

Main destination

§§6.6–7.2

§7.3

This distinction is essential.

For example, the growing-parameter construction begins at 
t
=
80
t=80, where its selected 
k
k is two. That does not satisfy the fixed-
k
k sufficient threshold 
t
≥
54676
t≥54676.

But this is not a contradiction: §7.3 explicitly uses the different allowance derived from (F43), not the fixed-
k
k allowance of §6.6.

The document explains this distinction, and I checked the displayed growing-
k
k schedule against its stated conditions.

Still, a reader who encounters the explicit 
13669
k
2
13669k 
2
  threshold early and then sees the much smaller growing-
k
k regime has a legitimate reason to stop and investigate.

I would foreground these as two different applications of the supplier theorem, ideally before §7.3 begins.

There is a related issue with the growing-family inequality. The bound

R
(
F
t
)
≥
Q
(
F
t
)
4
−
ε
(
ℓ
)
R(F 
t
​
 )≥Q(F 
t
​
 ) 
4−ε(ℓ)
 
holds as stated for the indicated range, but the explicitly provided 
ε
(
ℓ
)
ε(ℓ) is initially larger than four. In that range the displayed power inequality is true but not a meaningful near-quartic separation estimate. The manuscript acknowledges the trivial case in its proof.

For instance, direct substitution gives approximately 
ε
(
160
)
=
7.74
ε(160)=7.74 at 
t
=
80
t=80; the bound becomes quantitatively informative only later.

This is not a mistake. It is another place where a formal all-range statement and the intended asymptotic interpretation should be more clearly distinguished.

The growing-
k
k result deserves a short explanatory paragraph saying what the schedule achieves asymptotically, why it uses the uniform hardness estimate, and why its early numerical bounds are deliberately loose.

4. Section 8: the hardest mathematics is not always the hardest prose
§§8.7–8.14, pp. 73–84

The analytic proof is the portion I would now prioritize for the deepest specialist editorial review.

Its architecture is coherent. The Gaussian-chain construction leads to a derivative identity; the decision-tree martingale controls the resulting derivative sum; the moment bounds produce a gap between two distributions; and the final quantitative argument converts that gap into randomized query hardness.

I followed this chain in more detail, particularly (F22), (F25), (F33), (F39), (F42) and (F43). I did not identify an obvious missing step in those transitions, but this is not yet an independent line-by-line verification of the entire analytic proof.

My main criticism concerns the explanation of why these particular mathematical devices are chosen.

The Gaussian transformation needs a design explanation
In §8.7, the paper introduces

Ψ
(
x
)
=
1
2
2
+
x
2
,
Ψ(x)= 
2 
2+x 
2
 
​
 
1
​
 ,
and the corresponding algebraic function 
φ
φ.

It then proves several carefully chosen properties, including

φ
=
x
Ψ
−
Ψ
′
,
0
<
Ψ
(
x
)
φ
′
(
y
)
≤
3
16
.
φ=xΨ−Ψ 
′
 ,0<Ψ(x)φ 
′
 (y)≤ 
16
3
​
 .
These are useful and mathematically specific requirements.

But from the reader's perspective, the functions appear suddenly. Their properties are proved, yet the underlying design problem is not fully explained.

I would introduce them by explaining the requirements the proof needs: bounded biases for a legitimate product distribution, an integration-by-parts identity that moves derivatives between Gaussian layers, and quantitative control of the resulting factors.

Then the algebraic choice would feel motivated rather than miraculous.

This does not mean claiming to know the historical discovery process. It means showing the reader how to recognize a suitable construction.

The distinction between raw derivatives and Fourier degree is crucial
A particularly sophisticated part of §8 is the observation around (F24).

The interpolation generates derivatives involving one coordinate from each of 
k
k blocks. But taking a derivative of order 
k
k at a biased point does not eliminate all Fourier components of degree greater than 
k
k.

The paper explicitly acknowledges this and proves an estimate that controls the relevant raw derivatives without discarding those contributions.

That is a valuable clarification because an incorrect degree-truncation argument could make the proof look much simpler than it actually is.

I would elevate this observation into the conceptual introduction to §8.10.

A reader should understand that the martingale estimate is needed not simply because the decision tree is adaptive, but because the proof needs quantitative control of an entire family of derivatives at biased points.

That would make the technical machinery feel necessary.

The quantitative proof could distinguish ideas from constants more effectively
The derivation of (F43) is painstaking and explicit. That is appropriate for a complete record.

However, the proof mixes the scaling argument with the precise numerical choices needed to make the final contradiction work.

I would tell the reader in advance that the essential scaling comes from balancing

m
−
(
k
−
1
)
/
2
d
k
/
2
,
m 
−(k−1)/2
 d 
k/2
 ,
which leads to the threshold

d
≍
m
1
−
1
/
k
d≍m 
1−1/k
 
up to parameter and logarithmic losses.

Only then should the detailed constants be assembled.

The manuscript actually notes this scaling just after (F33). The issue is that the explanation is not given sufficient prominence before the most demanding calculations.

Section 8 contains substantial mathematical explanation, but its best conceptual insights are too often presented as remarks inside the proof rather than as guides to the proof.

5. The formalization needs a more explicit dependency hierarchy
Appendix G.4–G.9, pp. 130–140

This is the most consequential issue for a specialist interested in formal verification.

On a closer reading, the document distinguishes several properties that must not be conflated:

Question

Why it matters

Does the Lean declaration compile?

Establishes that a formal proof of its type exists under the recorded environment

Was its type independently compared with a configured target?

Establishes a specific statement-level comparison, not necessarily semantic independence

Does the declaration lie in the headline proof's dependency closure?

Establishes whether that particular formal result supports the headline theorem

Does the type express the intended mathematical proposition?

Requires mathematical-fidelity reasoning beyond compilation

Is the corresponding ordinary derivation fully formalized?

A checked endpoint need not mean the printed proof route was formalized

The manuscript knows these distinctions and reports them carefully. 
reasoning_record(2).pdf

What it does not yet do especially well is help the reader combine the dimensions into a single judgment.

For example, the bounded-list tournament theorem is described as built, but not one of the principal comparison targets, and it is not used by the headline proof roots. The headline upper-bound route instead uses the measured-label and Boolean-continuation machinery.

That is entirely compatible with the stated claims. But the reader needs to see these as two proof routes, rather than merely as different statuses scattered across several paragraphs.

I would add a dependency diagram with the headline route clearly distinguished from separately checked refinements.

I would also make the distinction between two kinds of completeness explicit:

Mathematical completeness: the record supplies an ordinary argument for the claimed result without leaving the main Forrelation hardness theorem as an imported assumption.

Formal completeness: particular mathematical statements have formal proofs, while individual refinements, physical-model bridges and alternative derivations have their own separately reported status.

These are not equivalent, and the manuscript does not claim they are. The front matter should make that unmistakable.

There is also a small wording issue worth checking in G.4. The section describes the optimal-exponent comparison as partial relative to the catalogue's compound Theorem 1.1 claim, then describes the separation comparison as exact while emphasizing its family inequalities. The exact formal type may resolve this completely, but the prose could specify more clearly which clauses of the compound theorem each comparison includes.

I am identifying that as a possible ambiguity in the explanation, not a demonstrated formal mismatch.

6. Independent spot checks from this reading
I also checked several smaller numerical and finite claims rather than judging the exposition alone.

Small Forrelation census, §8.4

Independently enumerating the 256 eight-bit inputs at 
k
=
2
,
m
=
4
k=2,m=4 gives numerator counts 
8
,
96
,
48
,
96
,
8
8,96,48,96,8 at 
−
8
,
−
4
,
0
,
4
,
8
−8,−4,0,4,8, matching the manuscript. This yields 104 yes-inputs, 48 zero-inputs and 104 unpromised inputs.

Classical planting tail, §6.6

The inequality 
(
2
/
3
)
40
t
≤
m
−
10
(2/3) 
40t
 ≤m 
−10
 , for 
m
=
4
t
m=4 
t
 , follows from the stated elementary estimate. The use of this decay to absorb the union over query times is consistent with the displayed bounds.

Quantum constant accounting, §5.2

The numerical factor 
6072
=
276
⋅
2
⋅
11
6072=276⋅2⋅11 matches the stated deliberately padded comparison-query budget.

Growing-parameter schedule, §7.3

The displayed schedule 
k
(
t
)
=
⌊
t
/
20
⌋
k(t)=⌊ 
t/20
​
 ⌋ satisfies 
k
≥
2
k≥2 and the uniform hardness dimension condition at 
t
≥
80
t≥80. The mathematics is consistent once the radical's scope is read from the typeset PDF.

These checks did not reveal a numerical contradiction. They also do not replace checking every inequality, reviewing external source proofs or rerunning Lean and its comparison tools.

I would resist interpreting a successful collection of spot checks as a proof-quality certificate. The manuscript itself makes essentially the same epistemic distinction.

7. Revised editorial priorities after three passes
My ranking has changed.

Priority

Revision

Expected benefit

1

Present the minimal proof obligations before their stronger formal and mathematical variants

Major improvement to expert comprehension

2

Explain the purpose and design constraints of the Gaussian-chain and martingale machinery

Makes the most demanding analytic section easier to understand

3

Display the two quantitative Forrelation regimes separately

Prevents misreadings of the fixed-
k
k and growing-
k
k arguments

4

Give the headline Lean dependency route and supplementary formal results separate summaries

Makes the verification scope much clearer

5

Move some repeated accounting and historical navigation outside the main proof flow

Improves continuity without losing completeness

I would no longer give high priority to large-scale shortening, removing examples or simplifying the mathematical notation.

The paper's detailed style is appropriate for its actual purpose.

8. Where I now stand
Complete mathematical reasoning record

8.5/10
Specialist mathematical exposition

7.5/10
First-contact expert readability

6.5/10
I am leaving the ratings unchanged from Round 2. The deeper reading has not established that the writing is fundamentally better or worse than I judged then. It has made the grounds for the judgment more precise.

I now think the manuscript has three especially strong qualities: it handles subtle probabilistic and quantum-model distinctions seriously, it gives the reader actual proofs rather than reassurance by citation, and it is unusually explicit about what its formal evidence does and does not establish.

The main editorial limitation is that a reader often learns every technical qualification before receiving the cleanest conceptual synthesis.

For a record designed to survive hostile mathematical inspection, that trade-off is understandable. But it is not optimal.

In the next reassessment I would concentrate on the self-contained Forrelation proof, especially §§8.7–8.14, and independently reconstruct its main estimates from first principles. That is the portion where a further pass is most likely to distinguish genuine mathematical difficulty, an explanation gap and a possible mathematical error.

My strongest conclusion from Round 3 is that the manuscript is technically disciplined and substantially well written for its intended expert audience. Its next major improvement should come from making the hierarchy of mathematical ideas as rigorous as the hierarchy of mathematical claims.




