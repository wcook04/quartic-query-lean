# Literature standard for round ten

**Open only after freezing the first reading of the lead paper.** This companion
guides subsequent comparison and revision advice. Reading it earlier supplies
expectations that must be recorded as exposure; it cannot then serve as evidence
of an unprimed encounter.

The target is exceptionally well-written mathematics by the standards of the
relevant literature. A correct, navigable account is a starting point. Ask whether
the paper makes its important idea easier to see, its difficult step easier to
reconstruct and its scope easier to use than the closest appropriate treatment.
Support that judgment with passages and reader operations. A lower detector
score, fewer pages, more examples or more findings cannot establish it.

## Compare three different kinds of paper

**Expert companion.** Its reader knows the query models and standard tools but
has not learned this construction. Assess whether the opening makes the
contribution and mechanism precise, then spends its space on the steps that
make the separation work. The reader should be able to reconstruct the upper
and lower bounds and identify the added work of this reconstruction without
being taken through an elementary quantum-computing course. Compare a proposed
change with the original preprint as well as nearby research writing. Clearer
derivations and explicit constants can be a contribution without being new
mechanisms. An ambitious improvement might reorganise the proof around the two
decisive reductions; justify it by showing which dependency becomes easier to
follow and where the displaced detail remains available.

**Exposition.** Judge the declared reader, not the expert you could imagine
instead. Can that reader execute the necessary operations, explain why they
matter and use them in the argument? A construction drawing must let the reader
locate the relevant data or follow a change. A quantum explanation must connect
the represented state to the operation performed. An example earns its space
by making a later inference available; an exercise tests the outcome actually
promised. Compare with teaching passages, not the compression of a research
abstract. A substantial replacement of a prerequisite sequence or worked
example is welcome when it removes a demonstrated obstacle. Do not append a
new example for every complaint.

**Long reasoning record.** Its reader may follow the whole argument or enter at
a cited proof. Can that reader reconstruct the precise claim, dependencies,
parameter choices and delicate cases without asking the author? Distinguish the
main derivation, useful alternative proofs, source comparisons and formal
evidence. The record can retain considerably more detail than the companion
while giving each detail a mathematical purpose and a usable destination.
Assess whether the important invariant or reduction remains visible through the
technical work. Removing repetition can improve a long record without removing
an argument; shortening it until the difficult step disappears cannot.

These are tests to apply to the supplied edition, not assertions that it fails
them. Differences in audience justify different proof routes and levels of
detail. They do not justify inconsistent mathematical statements or credit.

## Primary passages that constrain the comparison

The selections below were directly inspected on 4 November 2026. Locators name
the edition read, not an interchangeable latest version. Their use here is an
editorial judgment, not an experiment establishing better comprehension.

**Knuth, Larrabee and Roberts, *Mathematical Writing*, Stanford report based on
the autumn 1987 course.** [Primary PDF](https://www-cs-faculty.stanford.edu/~knuth/papers/cs1193.pdf),
§1, items 5 and 10–14, printed pp. 2–3; §10, printed pp. 20–21. The selected
passages address self-contained theorem statements, connected mathematical
explanation, first-use notation and what the reader knows before the next step.
Use them to compare a draft's actual sequence: can the reader parse a newly
introduced quantity, and does the prose explain why the next display is here?
For the companion, test the theorem in isolation; for the record, test entry at
an advertised proof destination. Section 10's discussion of algorithm steps and
invariants also cautions against imitating a named style. Adopt a device for the
operation it exposes, not to make the paper resemble a famous author's page.

**Francis Edward Su, *Guidelines for Good Mathematical Writing*, updated
18 August 2020.** [Primary handout](https://math.hmc.edu/su/wp-content/uploads/sites/10/2020/08/Guidelines-for-Good-Mathematical-Writing.pdf),
pp. 1–2, audience discussion and worked distance problem. The worked solution
keeps its positive-coordinate assumption visible while leaving routine algebra
to its intended reader. Compare allocation of detail, not sentence length.
Identify what a particular reader can supply and what the passage must show.
This permits expert compression and demands an explanation when the exposition's
reader lacks the operation; it licenses neither unexplained jumps nor a full
expansion of every algebraic manipulation.

**Andris Ambainis, *Understanding Quantum Algorithms via Query Complexity*,
arXiv:1712.06349v1 (2017).** [Versioned text](https://arxiv.org/html/1712.06349v1),
§2.1 and §4, from Theorem 4 through the pointer-function definition and ensuing
certificate discussion. The survey fixes its model and presents the table's
fields and acceptance conditions before deriving useful properties. Compare
how the quartic papers establish their data, predicate and algorithmic use.
An expert can accept a compact complete interface; a learner may need to trace
one input. The source uses a different pointer construction. Do not import its
predicate into this one or treat its historical separation bounds as current.

**Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, 17 April 2025.**
[Primary notes](https://www.cs.umd.edu/~amchilds/qa/qa.pdf), §1.4, printed pp. 2–3.
The passage first makes a classical computation reversible by retaining
intermediate values, then explains a clean-output construction with an explicit
map. Use that operational progression when assessing the exposition's quantum
prerequisites. For the expert and record, inspect the interface the next argument
actually consumes. A source's clean-output construction is not a reason to
demand cleanup where retained workspace suffices. An informal analogy alone
does not show what information the implemented operation preserves.

**Brassard, Høyer, Mosca and Tapp, *Quantum Amplitude Amplification and
Estimation*, arXiv:quant-ph/0005055v1 (2000).**
[Versioned PDF](https://arxiv.org/pdf/quant-ph/0005055v1), §2, operator (1),
Lemma 1, equation (8), Theorem 3 and QSearch. The presentation identifies the
good and bad components, states the operator's action and then derives the
amplified state. Unknown success receives a separate algorithm and guarantee.
Compare the papers' explanation of the transformation with their explanation
of stopping and cost. The exposition may teach a small state calculation; the
record must retain the general inference; the companion can cite the standard
rotation while showing the construction-specific use. QSearch's expected cost
is not the fixed-cap guarantee required here. Keep that distinction when using
this source as a model of explanation.

**Andrew Drucker, *Improved Direct Product Theorems for Randomized Query
Complexity*, arXiv:1005.0644v2 (9 May 2014).**
[Versioned PDF](https://arxiv.org/pdf/1005.0644v2), §3, definition of W, Lemmas
3.1–3.2 and the subsequent product argument. The proof gives the conditional
quantity an operational interpretation, establishes the conditional product law
and identifies the factor changed by the next query before bounding the product.
Use this sequence to assess whether the reader knows what is conditioned on
and why a multiplication is valid. The record should expose that argument; an
expert treatment can compress it after stating the relevant contract. A teaching
account may supply the contract and make its application executable. Drucker's
headline global-budget theorem and the separately capped setting used here are
different statements; the proof technique does not erase that distinction.

These are selected readings, not reviews of the complete works. Follow the
source preprint and other cited primary literature when a different mechanism
needs comparison. If an extraction loses mathematical symbols, inspect the
original page before using the passage; do not calculate style statistics on
damaged text. Report unavailable sources rather than guessing their treatment.

## Turn comparison into consequential advice

After the first-pass freeze, select the closest useful passage for each major
editorial decision. Record the source edition and locator, what operation its
reader performs, the current paper's corresponding task, and the proposed
change with its reason. Explain mismatches in audience, model or purpose before
transferring a convention. Do not copy the source's prose or promote its layout
to a universal rule.

Consider structural alternatives as well as local repairs. If a different
opening, proof order, recurring example or distribution of material across the
three papers would make the argument substantially better, give a concrete
replacement outline and walk one difficult dependency through it. Identify what
moves, what disappears, what must be taught earlier and what the reader gains.
Preserve exact hypotheses and credit. A source error or a new mathematical
claim needs separate verification; it cannot be approved as a stylistic choice.

Use the existing `literature_comparison.md` and verdict outputs. Distinguish
remaining mathematical or comprehension obstacles from opportunities to make
already sound writing exceptional. Rank changes by their effect on this reader's
understanding of the result, not by the number of sentences they touch. Explain
why a low-impact preference is not being promoted to a defect. Keep coverage,
confidence, unique actions and prior resolved complaints separate. A claim that
the paper meets or exceeds a literature standard needs a bounded comparison,
not praise or an inferred quality score.

The governing authoring method is Lean Exposition at merged commit
`7bc9ef5d253d23527c6ccbd759c2eb24c0243ac7`
([PR 44](https://github.com/wcook04/lean-exposition/pull/44)). The supplied skills
and register stage provide the full procedures. This companion selects concrete
comparisons for this round and must not be read before the first-pass freeze.
