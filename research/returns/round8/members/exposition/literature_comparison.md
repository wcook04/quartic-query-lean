# Literature comparison: teaching the construction and its two hard steps

## Verdict and reading boundary

The exposition is strongest when it gives the reader a small object to operate on: the three signed inputs, the false domain certificate, the dominating nonwinner, the first pivot and the capped XOR trace. It is weakest where several correct explanations have accumulated into one paragraph. The best lesson from the sources is not to imitate their sentence lengths. It is to introduce a mathematical device as the answer to a question the reader already understands, and then make its operation visible.

This comparison uses targeted primary-source reading. **Read in the relevant passages:** de Wolf's chapter 2 query model and chapter 7 Grover/amplification treatment; Buhrman–de Wolf §3.1–§3.3; Aaronson–Ambainis §3.1–§3.2; Aaronson–Ben-David–Kothari §3.1 and the opening of §3.2; BHMT §2 through the invariant-subspace calculation and Theorem 2; BBHT §§1–4; and the supplied OpenAI preprint §§3.1–§3.3. **Skimmed:** the longer introductions of the survey, Aaronson–Ambainis and the cheat-sheet paper, and Grover's opening two pages. The short IBM introductory page was read in full, but its video and slides were not opened. Neither the complete de Wolf textbook nor all proofs in these papers were read.

The supplied extractions and online text support the comparisons below. No claim about an external figure's print size, typography or visual clarity follows from reading its caption or nearby proof. This workstream did not visually inspect those PDFs. Damaged survey/Grover extraction is not silently repaired into quotations. The source-reading records provide finer passage-level scopes.

## 1. A reason to care about the model, before its limitations

The [Buhrman–de Wolf survey](https://doi.org/10.1016/S0304-3975(01)00144-X), Introduction and §3, presents decision trees as a restricted setting in which resource comparisons become tractable. Its elementary object is an adaptive sequence of bit queries; the binary tree records how earlier answers determine later choices. This makes the later measures properties of a concrete algorithmic model.

[Aaronson–Ambainis](https://arxiv.org/abs/1411.5729v1), Introduction, instead organizes its opening around “The Speedup Question”: how large a separation the model permits and what answering that question teaches about quantum advantage. Its historical examples lead to an unresolved extremal question. Those examples are statements about the paper's historical setting, not a current list of open bounds.

The [IBM Quantum Learning introduction](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/quantum-query-algorithms/introduction), opening paragraphs, calls the model “a petri dish for quantum algorithmic ideas.” The page explains its usefulness for developing and teaching algorithms while acknowledging its distance from practical computation. This is positive motivation for a simplified model; it is not evidence for a practical speedup from the present construction.

**Recommendation.** The exposition already explains one query and correctly excludes hardware/runtime conclusions. Keep both. Add the positive intellectual payoff: determining the strongest advantage compatible with answering on every input reveals what the promise assumption was buying. The reader should encounter an interesting restriction, not only a technically defined infimum. A short definition of an adaptive decision tree before its first use would also connect the elementary OR procedure to the lower-bound vocabulary.

## 2. de Wolf: operations that can be reconstructed

[de Wolf's notes, version 6](https://arxiv.org/abs/1907.09415v6), chapter 2, introduce the address register, answer register, bit oracle and phase query in direct succession. The Deutsch–Jozsa discussion then says, “Let us follow the state through these operations.” The state evolves through named transformations until a particular measurement outcome has the claimed probability. In chapter 7, the two-reflection geometry is connected to an implementable conjugation using the preparation and its inverse; the good and bad directions are identified before their rotation is analyzed.

The current exposition adopts much of this discipline. It states the bit oracle, derives phase kickback and retains all workspace in the amplified good vector. These repairs should be protected. The remaining opportunity is to finish the operational pictures already begun. In the four-dimensional example, identify $H$ with two Hadamard gates and use the final $H$ to turn projection onto $u$ into the all-zero computational-basis test. At general size, say that the position register has $2t$ qubits while $k$ counts queried sign layers.

**Recommendation.** Give the sampler a similarly reconstructible state or register picture. The new preparation is more important than another explanation that unitaries are reversible. Show where candidate, comparison workspaces and success flag reside, and where a measured pivot becomes classical data for the next stage. That uses this reader's existing circuit knowledge instead of making them translate a long verbal implementation unaided.

## 3. Grover: an immediate task, with boundaries retained

[Grover's original search paper](https://arxiv.org/abs/quant-ph/9605043), Summary and §§1–1.2, begins with “Imagine a phone directory” and a concrete retrieval task. It then introduces the transformations needed for that task. The useful writing feature is the short distance between the reader's question and an operation addressing it. The comparison here relies on the supplied opening, not a complete proof audit or a visual assessment of its figures.

The present exposition improves on a loose physical-database analogy by specifying bit-query access and explicitly excluding the cost of building an oracle. Its four-bit OR example is a better local entry for this exact theorem. It should not replace that precision with claims that a superposition reveals all entries.

**Recommendation.** Carry the same concreteness into Section 2. Before asking the reader to hold an array of transcripts in mind, tell them the task the fixed Boolean circuit performs: certify the domain claim and the address value. The later gate check and changed board are successful because they make those tasks executable. The array's full design should arrive after its certificate has a recognizable purpose.

## 4. Aaronson–Ambainis: a circuit entrance to Forrelation

[Aaronson–Ambainis](https://arxiv.org/abs/1411.5729v1), §3.2 and Figure 1's caption, gives a circuit interpretation of $k$-fold Forrelation: queried sign transformations alternate with Hadamards, and the return amplitude is the correlation quantity. Proposition 6 then supplies a controlled interference construction with its own acceptance law and query convention. The prose and caption tie the algebra to what the circuit does; this does not establish a visual-quality judgment about the supplied figure.

The current exposition's three examples do something particularly valuable for newcomers: positive, zero and negative correlation are compared explicitly, and the large negative case becomes the reason for an exact domain test. That is more directly useful to this total-function construction than merely importing a familiar Forrelation circuit diagram.

The formulations must stay distinct. The source's controlled interference probability and the exposition's squared projection probability are different operations. The present one-sided positive promise is also essential: a decoder may return any label off promise, but the certificate must reject an invalid domain claim. Familiar absolute-value or squared-correlation formulations from other notes cannot replace that promise without checking the construction's logic.

**Recommendation.** Borrow the circuit-level clarity, not a different promise or a sharper query count. Complete the existing projection circuit and keep the signed counterexample. No optimization of the decoder is needed for this teaching revision. The small $\delta$ should be labelled as an inherited promise parameter; its relevance to repetition cost is then explained where $2^{10k}$ appears.

## 5. Cheat sheets: motivate each construction choice by an obstruction

[Aaronson–Ben-David–Kothari](https://arxiv.org/abs/1511.01937v2), §3.1, has a particularly useful causal order. Extending a partial function arbitrarily does not automatically preserve a cheap quantum algorithm. Domain certification is therefore a problem. Composition supplies certificates, but appending an accessible certificate would help the classical algorithm too. The next design choice answers that problem:

> What we would like is to hide the certificate somewhere in the input where only the quantum algorithm can find it.

The address built from many hard answers then has a clear purpose. The opening of §3.2 specifies the composed inputs, certificates, addressed array and validity conditions. Figure 1 is referenced at the point where the assembled object becomes relevant; only its caption and placement in the supplied text were inspected here.

The present exposition correctly credits the addressing idea and distinguishes the pointer contribution. Its long genealogy paragraph, however, combines attribution, address length, a future direct product, union-bound arithmetic, array size and alphabet encoding before the reader has operated on the board. This is more complete locally but less causal.

**Recommendation.** Keep immediate credit, then develop the need for each component through the existing board. Move the extended predecessor comparison to the historical paragraph or expert companion. When explaining the earlier cubic scale, explicitly say that each outer input bit is supplied by a separate AND–OR instance. The current switch from $m$ to a historical $n$ should not force a newcomer to infer composition. Historical “best known” statements in the supplied paper remain dated; they should not overwrite the exposition's current attribution.

## 6. BHMT and BBHT: the contract and the operation

[BHMT](https://arxiv.org/pdf/quant-ph/0005055), §2, Lemma 1 and equation (8), identifies the invariant two-dimensional subspace and shows how amplification changes the coefficients of its good and bad components. It assumes an invertible preparation and an accessible good/bad distinction. These passages support preserving the successful direction, hence the conditional label law when the full prepared state includes retained workspace. The later amplitude-estimation development was not read for this comparison.

[BBHT](https://arxiv.org/pdf/quant-ph/9605034), §§3.1–4, supplies the quarter-success example, the randomized-iteration averaging identity in Lemma 2, and an unknown-number-of-solutions search analysis. Its zero-solution discussion explicitly uses a timeout. Thus a bounded stopping rule is an established search device, not a novel contribution of this exposition. The later counting and lower-bound sections were not read.

The current exposition makes a good division of labor: it explains the successful-direction invariant, states the capped routine's guarantee and leaves detailed trial constants in the record. It also says the cap holds below the guaranteed success threshold. That is the clause needed for a total algorithm, including on zero-inputs and after a winner has entered the list.

**Recommendation.** Keep the contract together and preserve the full-workspace convention. Add a compact conjugation formula or circuit for the prepared-state reflection. Consider presenting the existing $p=1/4$ one-iteration improvement before or alongside the $p=1/2$ example that shows no improvement. The latter is a useful warning against monotonicity, but it is a less effective first demonstration of why amplification helps. Do not replace the capped contract by an expected-cost slogan, and do not bring the record's constant accounting back into the main route.

## 7. The source preprint: restore one valuable mathematical picture

The supplied [OpenAI preprint](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf), §3.2, equation (15), displays the prepared state as a uniform candidate register tensored, conditional on that candidate, with one fresh comparison state per earlier pivot. The next steps identify the product success probability, sum over orthogonal candidates and normalize to the pivot law. The displayed state has a precise job: it explains why probabilities multiply within a candidate branch and add across candidate branches.

The exposition now states those facts correctly in prose and adds both deterministic and unequal-weight examples. Those examples exceed the source's level of concrete calculation and are worth keeping. But the register-level relation from equation (15) would complement them. The fractional matrix cannot show why a physical preparation has the stated law; it illustrates the law once established.

**Recommendation.** Use a two-pivot version of the existing preparation or an annotated register state. Explicitly separate amplitude from squared norm and distinguish the success flag's two later meanings: beating all pivots during sampling, finding a violated test during verification. This is an explanatory reuse of the source argument, not new formalization or a new theorem. Keep the abstract fractional matrix explicitly abstract; no realized board is needed.

## 8. Statements, credit and the standard of comparison

The exposition is unusually careful about three points that shorter source accounts often leave to experienced readers: one-sided promises, bounds in opposite directions, and the order of fixed-$k$ limits. Its final ratio argument and endpoint exercise should survive stylistic revision. Likewise, the domain-bit and dominating-nonwinner examples teach necessary hypotheses through failures of specific shortcuts.

The attribution should remain component-specific. OpenAI supplies the theorem, construction and separation analyses; earlier work supplies named query, certification and search ingredients; the current project supplies reconstruction, exposition and formal development. A source's existence, a successful build and a checked formal statement are different evidence claims. The closing Lean section should preserve its explicit difference between the displayed logarithmic power and the formal family's existential power, while explaining statement matching in ordinary language.

The recommendations here concern what the requested reader can reconstruct. They do not assert that every research paper ought to teach all these prerequisites, or that the exposition should copy a source's historical rhetoric. The strongest next revision would shorten the distance from an introduced object to its first use, improve the sampler's operational picture, and split the two conceptual steps in the direct-product proof. More citations alone would not do that.

Yao, Nisan and Barnum–Saks–Szegedy remain cited-only sources for this workstream; no reading of their original papers is claimed. Additional instructional comparisons and exact Bansal–Sinha parameter checks follow below.


## 9. Two additional teaching models: Jeffery and Grier

[Stacey Jeffery's Week 5 notes](https://homepages.cwi.nl/~jeffery/notes/week5.pdf), dated March 22, 2026, introduce query complexity with explicit Boolean-function and certificate examples before the Forrelation material. The passages read were pp. 1–2 and §5.4, pp. 26–27; the remaining notes were not reviewed. Their instructional advantage is a small certificate that the reader can inspect before considering general complexity measures. Forrelation is motivated by the possible size of quantum–classical separations. The historical overview predates the October preprint and is not used as the current frontier.

**Recommendation.** The exposition already has better construction-specific failure examples than an introductory survey needs. Make a reader operate on one certificate before asking them to remember the full storage specification. Borrow the teaching order, while retaining the exposition's one-sided promise: Jeffery's absolute-value formulation has different domain semantics.

[Daniel Grier's lecture notes](https://www.danielgrier.com/courses/CSE291/Fa25/lecture_notes.pdf), §4.7, pp. 49–51, explain the Forrelation procedure by following the circuit layers and then identifying the measured probability. The reading covered that section, the preamble and selected adjacent reduction context, not the full 107 pages. Claim 4.18 supplies a useful operation-to-amplitude connection; the surrounding statement separates the quantum calculation from the imported classical lower bound.

**Recommendation.** Complete the exposition's existing circuit rather than adding a second definition of Forrelation. A final basis-change gate and one tracked state would connect its algebra to an observable event. Grier's squared-correlation thresholds are not automatically interchangeable with the positive one-sided promise used in the current total-function construction.

## 10. Parameter and credit checks against primary statements

[Bansal–Sinha, arXiv:2008.07003v3](https://arxiv.org/html/2008.07003v3), introductory equations (1.1)–(1.3), Proposition 1.2, Theorem 1.3 and Corollary 1.4, gives the positive promise with threshold $\delta=2^{-5k}$ and bounded-error classical lower-bound scaling $\Omega\!\left(k^{-29}(m/\log(km))^{1-1/k}\right)$. Those passages, not the complete analytic proof, were read. For fixed $k$, this dominates $m^{1-1/k}/(\log_2m)^2$ eventually: the omitted constant and the change of logarithm base depend on fixed parameters, while the ratio grows as a positive power of $\log m$. This checks the exposition's weakened eventual scale, not its record's enormous explicit threshold. The source's $(1+\Phi)/2$ acceptance law and smaller query count use a different decoder; they do not make the exposition's $k$-query squared-projection experiment erroneous.

[Aaronson–Ben-David–Kothari–Rao–Tal, arXiv:2010.12629](https://arxiv.org/abs/2010.12629), abstract and metadata, states $D(f)=O(Q(f)^4)$ for total Boolean functions. Only that level was checked online. Combined with the ordinary $R\le D$ comparison, it supports the upper side of the exponent claim. Credit belongs to that antecedent for the universal upper bound and to the OpenAI preprint for the separation construction. This review does not independently certify either full proof.

## 11. Direct products: distinguish the resource hypothesis from the proof technique

[Drucker's author manuscript](https://people.csail.mit.edu/andyd/SDPT.pdf), §1.3 and §3, Lemmas 3.1–3.2, separately discusses the best remaining-budget success value and the product law after a fixed execution transcript. The inspected passages also distinguish the headline global-budget theorem from the fair-query argument. Its introduction and footnote credit Shaltiel's fair decision trees and explain the XOR-to-direct-product relationship. [Shaltiel's ECCC abstract](https://eccc.weizmann.ac.il/eccc-reports/2001/TR01-009/index.html) was read as an abstract, not as the full proof.

The exposition's attribution is appropriately specific. Its theorem uses separate per-instance caps; it does not simply invoke the stronger-looking headline theorem with an unexamined shared budget. The useful teaching move is to split its optional proof at the same conceptual boundary: first establish what conditioning on a transcript preserves, then analyze the remaining-budget values. Retain the counterexamples showing why a pooled cap and merely coordinatewise-independent side information are insufficient. The stopped simulator is the final application of those hypotheses, not another direct-product theorem needing to be invented.

## Source-use safeguards

Every outside source above has a URL and a passage-level reading scope. Supplied originals and extracted text were distinguished from newly opened online sources. Historical frontier statements, slide simplifications and different promises were not silently imported into the current theorem. Short quoted specimens in the comparison total at most 25 words from each external source. All recommendations remain feedback on explanation and navigation; they do not request stronger bounds, a different construction or new formalization.
