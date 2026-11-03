# Literature comparison

## Scope and standard of comparison

This comparison distinguishes reading a selected passage closely from reading a whole work. The seven supplied literature items were sampled for their openings, theorem interfaces and relevant proof passages; the individual scopes are recorded in `feedback.json` under `sources_read`. The three current manuscripts were read in full across the panel. The exemplar papers were sampled, not independently checked as mathematics. Online sources were consulted on 3 November 2026. Quotations below are short and identified by section or page. Editorial conclusions belong to this review, not to the cited authors.

The comparison is not a vote about whose prose sounds more human. Published papers also contain long sentences, approximate-equality heuristics, dense introductions and substantial prerequisite assumptions. The useful question is what a passage enables its intended reader to do. A research paper can assume a quantum-query vocabulary that an introductory exposition has to teach. A full proof record can preserve calculations that would overwhelm either shorter document.

## 1. Aaronson–Ben-David–Kothari: make the construction's job visible

**Source and scope.** *Separations in query complexity using cheat sheets*, supplied arXiv:1511.01937v2, especially Introduction, “Randomized versus quantum query complexity,” “The cheat sheet technique,” and the composition discussion in §3.1. [Versioned source](https://arxiv.org/abs/1511.01937v2). The full paper was sampled.

> “These separations are shown using a new technique for proving separations between query measures”

**Locator:** Introduction, “The cheat sheet technique,” first sentence.

The introduction establishes the resource comparison, gives a concrete separation and then describes the transformation's purpose. Its table distinguishes a separation achieved from a known relation. These are useful models for the current expert introduction, whose table puts existential examples and a universal upper bound under an equality heading. The companion's derived AND–OR arithmetic is a real improvement over a bare historical list: the reader sees why that particular recipe stops at a cubic exponent. Keep its qualification to the named recipe. Do not turn it into a limitation of every possible use of cheat sheets.

For the exposition, borrow the clarity of the operation, not the paper's assumed background. “Certificate,” composition and the access model still need local explanations. The supplied paper's historical priority language must also be read as language of that version; it is not a reason to undo the current documents' explicit Ben-David credit.

## 2. Bansal–Sinha: introduce the promise before the machinery

**Source and scope.** *k-Forrelation optimally separates quantum and classical query complexity*, supplied arXiv:2008.07003v3; Introduction through the main results, the one-sided promise, and the final lower-bound conversion sampled closely. [Versioned source](https://arxiv.org/abs/2008.07003v3).

> “Next, we discuss some applications of our results.”

**Locator:** Introduction, transition from the main Forrelation result to applications.

The source separates the promise, the cheap quantum experiment and the randomized lower bound before discussing consequences. That ordering helps the reader know what the analytic work supplies. The exposition's three-fact interface in §3 does the same and should stay. Its exact circuit arithmetic, however, receives more local explanation than why the classical hardness input matters.

The record's Appendix E makes a suitably narrow criticism: a particular displayed logarithmic-factor conversion and a reciprocal term in the specified edition. The review preserves that boundary. A bad displayed comparison does not disprove the theorem, and a reconstructed proof with different bookkeeping does not establish novelty. Keep the exact version and equation locators in the record; let the companion state the mathematical distinction economically. This source is technical research prose, not a model for a newcomer-facing first calculation.

## 3. Sherstov–Storozhenko–Wu: separate theorem regimes visibly

**Source and scope.** *An optimal separation of randomized and quantum query complexity*, supplied arXiv:2008.10223v4; Introduction, the partial- and total-function results, and the Fourier-growth corollaries used in the record. [Versioned source](https://arxiv.org/abs/2008.10223v4). The full work was sampled.

> “Our results: separations for partial functions”

**Locator:** Introduction, subsection heading.

The organization visibly distinguishes the partial separation, its total-function consequence and further applications. The same discipline would help the current historical table: a universal relation and a family witnessing a lower separation have different directions and quantifiers. The source also separates a fixed parameter from a slowly growing one. The current fixed-$k$ argument is good precisely because it makes the order of choices explicit; the growing-parameter result should have its own clearly marked role.

The mathematical distinction already present in the companion is worth preserving. The cited main Rorrelation result uses a random orthogonal matrix; the present construction needs an explicit Walsh promise and an exact circuit. The record's optional Fourier-growth transfer is a separate use of a source theorem, not a replacement of the main construction's matrix by a random one. Do not flatten those roles into “the same result independently.”

## 4. Aaronson–Ben-David–Kothari–Rao–Tal: show what the dependencies buy

**Source and scope.** *Degree vs. approximate degree and quantum implications of Huang's sensitivity theorem*, supplied arXiv:2010.12629v1; opening results and the short deduction of the deterministic-versus-quantum upper bound, plus the conjecture locator used by the manuscripts. [Versioned source](https://arxiv.org/abs/2010.12629v1). Sampled.

> “We use this observation to prove two main results”

**Locator:** Introduction, before “Deterministic vs. quantum query complexity.”

The opening attaches the intermediate observation to the results it makes possible. The deduction of the quartic deterministic bound exposes the few inequalities being combined and credits their origins. The record's Appendix A similarly starts with a four-link chain, then proves the ingredients. That is one of its best organizational choices: the reader can locate an ingredient without losing sight of the whole argument.

The expert paper needs the universal exponent, not both numerical constants arising from different proof routes. Their formal correspondence belongs in the record. Retain the explicit distinction between the established deterministic upper bound, its randomized consequence and the randomized cubic conjecture. The extraction supplied for this source loses some macro distinctions; source display notation should be checked in the original when transcribing formulas rather than copied mechanically from the extracted text.

## 5. Ambainis–Iraids–Kokainis: compare mathematical objects, not slogans

**Source and scope.** *Near-optimal separations of certificate complexity from randomized and quantum query complexity*, supplied arXiv:2609.11664v2, Introduction and §6.1; the corresponding parts of online v3 were also sampled. [Supplied edition](https://arxiv.org/abs/2609.11664v2); [later edition sampled](https://arxiv.org/abs/2609.11664v3).

The useful comparison is between a surviving candidate set for a fixed intended comparison graph and the current weights for probabilistic loser comparisons. The companion and record now identify that distinction. This is substantially better than claiming the entire search idea has no antecedent. Conversely, the existence of an antecedent does not make the weighted argument routine: the half-drift identity and exact conditional sampling explain the adaptation.

The present exposition has the stronger finite teaching apparatus: a dominating nonwinner and a cycle show why comparison victory alone is insufficient. Its remaining weakness is that the displayed sampler has only zero-one weights. The record's existing fractional example would let a learner check the feature that distinguishes the weighted process from ordinary candidate elimination. This is a request to use an existing explanatory example, not to strengthen the theorem or add formalization.

## 6. de Wolf: stage the standard tool before its variants

**Source and scope.** Ronald de Wolf, *Quantum computing: lecture notes*, supplied arXiv:1907.09415v6, chapter 7 closely for Grover geometry, unknown marked-set size, verification and amplitude amplification. [Versioned source](https://arxiv.org/abs/1907.09415v6). The lecture-note volume was sampled, not read in full.

> “We now list (without full proofs) a number of useful variants of Grover:”

**Locator:** chapter 7, §7.2, “Algebraic argument,” paragraph before the variant list.

The chapter develops a search problem and its geometric operation before handling variations. It also distinguishes a reliable search routine from an unqualified claim that a found label or failed attempt settles the problem. This is a useful comparison for exposition §4. The document needs the amplification routine's contract: an advance cap, the success guarantee and preservation of the conditional label law. The detailed mixture of trial types and numerical denominators can be reached in the record.

The current four-column calculation is valuable because it applies the routine to a particular prepared state. Move that application nearer the general sampling display. State the fixed cap without implying that every random branch executes the same number of calls. Borrowing the organization of a textbook chapter does not mean reproducing that chapter inside the exposition; teach the few operations the construction actually uses.

## 7. The ECCC correction note: delimit an error's consequences

**Source and scope.** Scott Aaronson, Andris Ambainis, Andrej Bogdanov, Tsun Ming Cheung and Krishnamoorthy Dinesh, *On quantum versus classical query complexity*, ECCC TR21-115, revision 2; supplied abstract, opening and estimator discussion sampled. The [official report page](https://eccc.weizmann.ac.il/report/2021/115/) was read for bibliographic verification.

> “In this note we describe a flaw”

**Locator:** Supplied revision 2, printed p. 1, opening paragraph before Theorem 1.

The note identifies the challenged argument, states what is recovered and marks a subsequent update. That is the appropriate rhetorical model for the record's Bansal–Sinha comparison: a precise local defect, its consequence and its limits. It also illustrates why historical “current” statements require a date or version.

There is a packet metadata defect to repair: `READ_ME_FIRST.md` calls this source Aaronson–Ambainis–Bogdanov–Yeung. The supplied title page and official record identify Cheung and Dinesh, and no Yeung. This is not a misattribution found in the manuscripts. The source inventory in this return uses the verified author set.

## 8. General mathematical writing: the reader's next operation

### Knuth, Larrabee and Roberts

**Source and scope.** *Mathematical Writing*, Stanford CS report, §1 read closely, especially the opening technical-writing rules; the remainder was sampled. [Official PDF](https://www-cs-faculty.stanford.edu/~knuth/papers/cs1193.pdf).

> “What does the reader know so far? What does the reader expect next and why?”

**Locator:** §1, item 12.

That question is a better local test than a paragraph-length target. In exposition §3, the bit oracle has been stated but its phase action has not been shown. In §5, the reader knows that addresses are hard but has not yet executed the simulator that reads a proposed query position as an answer vector. These gaps are about the next operation, not the elegance of an isolated sentence. The review's advice is to locate those operations, supply the minimum bridge and reuse the same finite object. The report's historical writing guidance is evidence for a practice, not experimental evidence that a particular edit improves learning.

### Lamport

**Source and scope.** *How to Write a 21st Century Proof*, dated 23 November 2011 with a 15 January 2012 change; §§1–2 read closely, later sections sampled. [Author's PDF](https://lamport.org/pubs/proof.pdf).

> “structure and naming”

**Locator:** §1, printed p. 1.

The relevant idea is to make an assertion's role and dependencies inspectable. The record needs that help where the simulator, joint cap event and final probability comparison are packed together. It does not follow that every proof should carry raw catalogue identifiers in its sentences. Human-readable lemma names and stable destinations can preserve precision without making the continuous argument sound like an index. The useful hierarchy is an overview with enough detail available beneath it; the current record sometimes gives the overview, full statement and repeated setup consecutively before beginning the proof.

### Short online teaching comparisons

The instructional pages of MIT OpenCourseWare's historical [Lecture 10](https://ocw.mit.edu/courses/6-845-quantum-complexity-theory-fall-2010/cb3396e315670e7702821be854cf120e_MIT6_845F10_lec10.pdf) and [Lecture 11](https://ocw.mit.edu/courses/6-845-quantum-complexity-theory-fall-2010/e184ebc92625eef1bc12aed4875f4e01_MIT6_845F10_lec11.pdf) were read. OR and parity motivate the first method; Lecture 11, §4.2, promptly applies an adversary theorem to explicit examples. This supports returning from the simulator's general contract to one executed trace. These 2008 notes, hosted in a 2010 course, are not used for current best bounds.

The visible [IBM Quantum Learning Grover introduction](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/grover-algorithm/introduction) was read; its video and full course were not. Its distinction between an abstract algorithmic advantage and practical advantage supports a brief reminder that the quartic theorem concerns query cost when the exposition reveals its large input length.

Girish–Tal–Wu's [*Fourier Growth of Parity Decision Trees*, arXiv:2103.11604v2](https://arxiv.org/pdf/2103.11604v2), §1.3 and Lemma 1.9, were sampled. The ordinary-tree discussion introduces the signed Fourier target before its representing walk. This is a useful ordering comparison for record §3.11, not a claim that their statement already supplies its raw-derivative theorem.

## 9. Journal guidance: useful constraints with a declared scope

The [SIAM Journal on Computing author instructions](https://epubs.siam.org/journal/sicomp/instructions-for-authors) were read in the abstract and manuscript-preparation portions. They prescribe an abstract of at most 250 words, with formulas and references minimized, and discuss usable figures. The relevant issue here is not a claim that the companion violates a word limit: it is whether the abstract's undefined parameter and multiple quantitative refinements leave room for the main idea. An abstract should be independently intelligible. No target journal has been specified, so venue instructions are comparisons, not new acceptance gates.

The [Theory of Computing ToCTeX guide](https://www.theoryofcomputing.org/submit/toctexguide.html), read in full, places any appendices before the bibliography and recommends vector figures. That appendix order is a venue rule, not evidence that all mathematical manuscripts must use it. The current illustration issue is more basic: the expert paper's Figure 2 labels its instance $m=4$ while drawing eight-bit strings. No typographic convention can repair that mismatch. Several supplied PDF floats also split mathematical sentences. Review captions and layout at reading size after the prose structure settles.

## 10. The supplied cross-field exemplars: borrow a discipline, not an outline

The opening and selected first sections of `exemplars/expository.md`, `exemplars/short-paper.md` and `exemplars/long-reasoning-record.md` were sampled. They concern a different theorem and do not provide evidence for the quartic result.

The SK exposition says it assumes “algebra and elementary calculus” and names the central contradiction in terms of endpoint data and area before introducing the detailed analytic suppliers. **Locator:** opening, paragraph beginning “We follow the quantitative proof.” The useful transferable practice is choosing a small conceptual spine and stating where the deeper inputs enter. The quartic exposition has a suitable spine already: hidden addressed certificates; a true winner protected against arbitrary rivals; comparison search before verification; two possible ways to notice a planted change. Its current opening nevertheless carries a much larger prerequisite inventory before the first example.

The expert exemplar shows a limit of imitation. Its abstract includes several mathematical consequences and a separate quantum-algorithm discussion. That accumulation is not a reason to preserve every refinement in the quartic abstract. Exemplars should supply decisions about audience, credit and dependency, not a fixed number of claims per opening or a mandatory shape for every paper.

The long exemplar is useful as a comparison for giving a full destination to imported facts, but its existence does not justify repeated entry paragraphs at every linked result. A record serves two reading modes. Incoming readers need a concise recap and the full proof; continuous readers need progress. Short entry summaries with links can serve the former while leaving repeated definitions out of the latter's main route.

## 11. Editorial conclusions from the comparison

**The three tiers need different allocations of explanation.** The expert companion should spend most of its effort on what is special to this construction: unrestricted loser comparisons, the weight drift and conditional sampler, and the reduction from a cell query to a capped address prediction. The exposition should spend effort on making the reader perform those operations on small inputs, together with the minimal query-model and coherent-query bridges. The record should preserve full supplier proofs, alternatives and formal correspondence, but let a reader reach one requested argument without repeatedly restarting the entire construction.

**A good source comparison isolates the changed hypothesis.** The current discussions of weighted versus fixed-orientation search, joint versus marginal independence, and measured labels versus a retained register do this well. Retain those distinctions even if a word detector calls their vocabulary defensive. Conversely, lists of neighboring algorithms before the present algorithm is intelligible have a high reading cost. Put the long comparison where the mathematical distinction can be recognized.

**Examples should test the step that could otherwise be misunderstood.** The negative Forrelation input tests the domain condition. The dominating nonwinner tests the difference between comparison and verification. The independent-versus-dependent planted column tests the averaging hypothesis. These are strong examples. A deterministic sampler does not additionally teach fractional weights, and a picture of an addressed cell does not execute the simulator. Those remaining gaps can be filled by reusing material already in the record.

**Credit and evidence should attach to the supported claim.** The current immediate OpenAI attribution, Ben-David priority correction and explicit same-circuit sentence should survive revision. Source-specific display errors should remain versioned and narrow. Formal material should explain which statement is proved and how its definitions connect to the printed mathematics. An implementation name or a successful historical check cannot do that explanatory work by itself.

These judgments supplement the individual findings and the fifteen claim journeys. They do not ask for a replacement manuscript, a new theorem, stronger estimates or additional formalization.
