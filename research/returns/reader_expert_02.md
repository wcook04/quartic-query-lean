# Second, deeper review of the Expert Companion

On this pass, I concentrated on the mathematical argument itself, looking for invalid implications, hidden assumptions, inconsistent constants, and places where the paper states more than it proves.

My revised assessment is that the central fixed-\\(k\\) separation argument is better written than I initially gave it credit for, particularly the probabilistic tournament and the classical prediction reduction. But I also found a concrete parameter error in Appendix E that my first review missed.

## 1. A definite error on page 19

Appendix E states:

\\[ k=\left\lfloor\frac{\sqrt t}{20}\right\rfloor \qquad\text{for }t\ge80, \\]

and says this choice satisfies the classical conditions.

That is false for the stated range.

At \\(t=80\\), the formula gives \\(k=0\\). In fact:

- For \\(80\le t<400\\), it gives \\(k=0\\).
- For \\(400\le t<1600\\), it gives \\(k=1\\).
- Only when \\(t\ge1600\\) does it guarantee \\(k\ge2\\), as required throughout the construction.

The intended formula might instead have been \\(k=\lfloor\sqrt{t/20}\rfloor\\), which would explain the threshold \\(t\ge80\\). I cannot determine which expression was intended from this PDF alone.

Fix: Either change the threshold to \\(t\ge1600\\) while retaining \\(k=\lfloor\sqrt t/20\rfloor\\), or verify that the intended definition was \\(\lfloor\sqrt{t/20}\rfloor\\) and amend the expression consistently.

This does not invalidate the asymptotic result, since the chosen \\(k\\) eventually becomes admissible. But the paper currently asserts that a family is defined for parameter values at which its defining assumption fails.

It is particularly worth correcting because Appendix A.8 explicitly warns against unjustified growing-parameter substitutions.&#x20;

expert_companion(3).pdf



## 2. The central proof survives a fairly demanding internal audit

I went through the main logical dependencies again, rather than treating each section as independently convincing.

| Argument                                   | Second-pass assessment                                                                        |
| ------------------------------------------ | --------------------------------------------------------------------------------------------- |
| Forrelation supplier, §2                   | Clearly specified; the crucial hardness and circuit facts are cited inputs                    |
| Definition of the total function, §2       | Coherent, including off-promise inputs and invalid certificates                               |
| Winner's comparison advantage, §3.1        | The argument accounts correctly for an arbitrary rival                                        |
| Weighted tournament, §3.2                  | Particularly strong; the contraction and exact sampling law fit together                      |
| Bounded amplification, Appendix C          | Reasonable proof structure, though one numerical bound is cited rather than calculated        |
| Candidate verification, §3.3               | The false-positive and false-negative cases are correctly separated                           |
| Planted-input coupling, §4.2               | Well constructed and carefully justified                                                      |
| Erased-zero bound, §4.3                    | The early/late discovery decomposition works                                                  |
| Capped address prediction, §4.4            | The most delicate classical argument is handled convincingly                                  |
| Fixed-\\(k\\) exponent proof, §5           | Quantifier order and exponent calculation are explicit                                        |
| Uniform growing-\\(k\\) result, Appendix E | Depends on the separate reasoning record; contains the parameter-range error identified above |

I did not find another demonstrable contradiction in the core fixed-\\(k\\) proof on this pass. That is not independent verification of the external theorems or Lean source, but it is a meaningful distinction from a document that merely looks rigorous.

### The quantum comparator has an important strength I initially underemphasized

On page 5, the paper establishes

\\[ a\_{ij}+a\_{ji}=1,\qquad a\_{i^\star j}\ge1-\varepsilon. \\]

The first property is an exact symmetry of how the comparator is implemented, while the second holds for a genuine winner.

Crucially, the second property does not require the rival's address to decode correctly.

Because the winning column is all ones, any rival pointer into it reads one. If the winner's address is decoded correctly, its outgoing pointer reads zero in the rival. That already determines the result.

This makes the subsequent tournament theorem work under a substantially weaker contract than an ordinary noisy total-order comparison.

Your explanation on pages 5–6 is economical and mathematically appropriate. I would not dilute it with more introductory material.&#x20;

expert_companion(3).pdf



### The weighted sampler is an actual reconstruction, not a hand-wavy argument

The sequence from equations (8) to (9), then Lemma 3 and the coupling argument, is well chosen.

Equation (8) proves contraction of expected surviving weight. Equation (9) constructs the quantum preparation whose successful-label masses are proportional to those weights.

The crucial relationship is

\\[ \Pr[\text{success and label }i]=\frac{w_i}{m}, \\]

and hence

\\[ \Pr[i\mid\text{success}]=\frac{w_i}{W}. \\]

Without the second equality, the expected-weight calculation could not automatically be applied to the implemented algorithm.

You make the link explicit, then explain how the bounded amplifier preserves the conditional label distribution and why the winner ensures a sufficiently large success probability before it is selected.

This is probably the most successful piece of technical writing in the manuscript.

The numerical example on page 7 checks out as well: the first pivot history gives \\(W/m=23/48\\), and the second gives \\(19/60\\). It genuinely clarifies the two distinct normalizations rather than merely supplying numbers.&#x20;

expert_companion(3).pdf



## 3. The classical reduction is even stronger than it first appears

On a closer reading, Section 4 does a good job of isolating the three obstacles that often become conflated in this type of argument.

The planted column \\(I\\) must be independent of the dummy input. The total query budget must prevent too many columns from becoming heavy. And a query to a proposed certificate cell must be bounded as a prediction under the original product distribution.

You address all three separately.

The most impressive transition is on page 10, where the simulator fixes an original query time \\(\tau\\), halts before exceeding its target allowance, and outputs the address named at that query.

The simulator's success probability is bounded unconditionally, even though the event of interest includes terminal lightness.

That is the right architecture:

\\[ \Pr[\text{light and a correct prediction}] \leq \beta^r. \\]

The paper correctly warns against replacing this with a conditional success statement given lightness. Appendix A.7 makes the danger concrete.

Appendix D also deserves more credit than I gave it previously. It proves the product bound through the value recurrence \\(V_d(\nu)\\) and an induction on the interleaved query tree, rather than leaving a generic direct-product theorem as a black box.

For an expert, this is persuasive proof presentation: the algorithmic stopping rule, the independence premise, and the probabilistic event being bounded all align.&#x20;

expert_companion(3).pdf

expert_companion(3).pdf



I would preserve this argument almost exactly as written.

## 4. Where the mathematical exposition still asks too much of the reader

### The exact circuit construction remains the weakest link in the main proof's self-containedness

Section 2 quotes three properties of the Forrelation supplier. That is normal: an expert paper need not reprove Bansal–Sinha's hardness theorem.

But property (iii), concerning the exact circuit, is closer to the engineering of this particular construction.

You state

\\[ S\le200(k+1)^2m\ell^2, \\]

explain that fast Walsh transforms compute an integer numerator, and refer to the reasoning record for the gate-count derivation.

Later, that very circuit size determines the number of local tests and therefore the quantum verification complexity.

The reader can follow the asymptotic dependency, but cannot audit the particular circuit bound from the main PDF without leaving it.

This matters more than an omitted low-level implementation detail because the paper advertises explicit quantitative choices.

I would add a short derivation showing the number of transforms, the integer word-width bound, the Boolean-gate cost of a butterfly operation, and how these yield the stated \\(S\\).

A half-page calculation would be sufficient. I would not import the entire circuit construction from the record.

### The explicit quantum constant is already available later

There is a curious organizational choice.

Theorem 1 presents the quantum bound using an unspecified \\(C_k\\). But Appendix E gives the uniform estimate

\\[ Q(F\_{k,4^t}) \le 2^{53}k\\,2^{10k}\sqrt m\\,\ell^6, \\]

and explicitly says that it holds for every \\(k\ge2\\), \\(t\ge1\\).

Provided that bound has the stated provenance, you could present \\(C_k=2^{53}k2^{10k}\\) as a permissible choice in Theorem 1, referring to Appendix E for the explicit accounting.

That would make the phrase explicit quantitative bounds more compelling. Readers would no longer need to reconcile the hidden constant in the main theorem with a separate explicit constant much later in the paper.&#x20;

expert_companion(3).pdf

expert_companion(3).pdf



### Appendix C could establish its numerical constant with one more calculation

The bounded-amplification proof is fundamentally clear. But the statement that averaged Grover success is at least \\(9/20\\) is supported by a citation and the reasoning record rather than a displayed estimate.

Because the lemma is one of the two central subroutines, I would include the standard averaged-amplification probability formula and the short estimate for the chosen cutoff \\(M=\lceil10/\sqrt\gamma\rceil\\).

That would make the numerical contract directly checkable within the PDF.

There is also a small citation typo on page 17: the citation appears with a doubled opening bracket, `[[23]`.&#x20;

expert_companion(3).pdf



Neither issue threatens the overall argument, but these are easy improvements.

## 5. I would revise my previous criticism of Section 6 slightly

I previously made expanding Section 6 the dominant recommendation.

After rereading the paper as a complexity-theory companion, I think that was too categorical.

For a theoretical computer scientist primarily interested in OpenAI's separation, the paper's main value is the explicit reconstruction of the tournament and lower-bound reduction. Section 6 can legitimately function as an evidence map rather than an extended Lean tutorial.

For a formal methods researcher assessing a claimed formalization, however, Section 6 remains inadequate as a standalone technical account.

The distinction is about intended audience, not simply the amount of writing.

What I would now recommend is a more exact statement-to-formalization contract, rather than automatically expanding Section 6 by several pages.

The existing table is a good starting point. It distinguishes compared endpoints, built and axiom-audited endpoints, and a deduction absent from the compared family theorem.

But it still does not show the actual types of the two main Lean declarations.

It would be valuable to print the central statement signatures—or faithfully simplified versions with direct links—and identify which formal complexity definitions they use.

The paper should also clearly separate three propositions that can otherwise be confused:

- Lean accepted a theorem about its formal query model.
- That theorem was compared with an independently compiled specification and subjected to an axiom audit.
- The formal query model corresponds to the intended physical quantum algorithm.

The manuscript already understands this distinction. Its presentation could make it more inspectable.

The unresolved retained-state correspondence should be described exactly where the dependency relationship is discussed. Readers should know whether it affects the headline measured-label theorem, a stronger auxiliary theorem, or both.

On the information printed here, the paper reports it as an additional correspondence boundary rather than an open hypothesis in the ordinary mathematical proof. I would preserve that distinction and make it impossible to miss.&#x20;

expert_companion(3).pdf



## 6. One structural issue: the reasoning record is doing several different jobs

The paper repeatedly sends the reader to the reasoning record for very different purposes:

- Full derivations of imported analytic or circuit estimates.
- Extended examples and numerical constants.
- Formal correspondence evidence and historical build records.
- Alternative proofs or refinements not needed for the main theorem.

All of these are legitimate reasons to cite a companion document. But the frequency and similarity of the cross-references make it difficult to know which trips outside the PDF are necessary.

A specialist should be able to distinguish this is a standard theorem we cite, this is a straightforward detail we expand elsewhere, and this is evidence needed to substantiate our formalization claim.

I would make that hierarchy clearer, especially in Sections 2 and 6. It would strengthen the paper's apparent self-sufficiency without adding much length.

Appendix E is the sharpest example. Its uniform estimate (16) is a substantive mathematical input whose complete proof is in the reasoning record. The asymptotic deduction following it is included in this paper.

That division is honestly indicated, but the uniform estimate's status deserves a more prominent statement than simply naming it an analytic input.

## 7. A further issue of reader expectations

The paper now moves between three levels of claim: reconstructing OpenAI's mathematical proof, introducing explicit numerical choices, and establishing independently checked Lean endpoints.

It does not falsely attribute OpenAI's theorem to you. The contribution paragraph is unusually clear about that.

But it could still be more specific about what constitutes the intellectual contribution of this particular manuscript.

For example, the proof of Proposition 2 is labeled with OpenAI's proposition number, and Proposition 4 reconstructs the original reduction. Appendices A–D add detailed analysis and examples.

The question is not simply whether those reconstructions are correct. It is whether the reader can tell which arguments have been supplied as new explanations, which quantities have been independently derived, and which statements are exact restatements of the original.

I would keep the current crediting and add a concise provenance sentence identifying the form of each contribution.

That is preferable to claims such as novel framework, new proof paradigm, or first complete explanation, none of which is needed to make the work respectable.

## 8. What I would actually change before sending it to experts

My prioritized revision sequence is now:

1. Correct the Appendix E parameter range and check it against the reasoning record. This is a demonstrable textual mathematical error, not an aesthetic preference.
2. Expose the actual Lean theorem statements and dependency boundary more directly. Retain the comparison table, but make it more independently inspectable.
3. Add a compact derivation of the circuit-size bound. It is the most important quantitative input whose derivation currently lives elsewhere.
4. Bring the explicit quantum constant forward, provided the existing uniform estimate is the one you want to claim.
5. Add the short numerical amplification calculation and correct the Appendix C citation typo.
6. Reduce unnecessary dependence on the reasoning record for locally checkable steps, while preserving links to genuine external inputs and evidence.

I would not materially rewrite Sections 3.2, 4.2, 4.3, 4.4, or the fixed-\\(k\\) conclusion. They already do what a specialist proof exposition needs to do.

## Revised judgment

My first review concentrated a little too heavily on presentation of the formalization and not quite enough on the strength of the reconstructed mathematics.

After a deeper second reading, I think the paper has a particularly good balance of rigorous probability, algorithmic construction, explicit query accounting, and counterexamples to tempting invalid inferences.

The main mathematical story is now coherent from beginning to end. It does not rely on generic explanatory language to conceal difficult transitions. In several places it makes those transitions the focus of the argument.

That is a substantial achievement for a reconstruction.

The distinction I would maintain is between a strong, expert-readable mathematical companion and a completely self-contained, independently audited formalization paper. The former description is now well supported by this PDF. The latter needs more immediately inspectable formal evidence and clearer treatment of its externally documented inputs.

The Appendix E threshold error should be corrected before circulation, particularly because it sits directly beside an explicit claim about the admissibility of the growing parameter.

Bottom line: I would rate the mathematical exposition itself around 8.5/10, the overall paper around 8/10, and regard it as close to ready for serious expert feedback once that concrete error and the remaining evidence-presentation issues are addressed.