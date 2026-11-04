# Second-pass review: a deeper, more critical reading

Paper: A nearly quartic separation between randomized and quantum queries: a complete reasoning record (141 pages).

## Revised verdict

After going back through the mathematical argument, especially §§3–8 and Appendices A, F and G, my assessment is slightly different from the previous pass.

The core mathematical exposition is stronger than I initially gave it credit for. The document's remaining problems are more specific, and some are more important, than simply being too long or too repetitive.

The paper now has a reasonably coherent chain of mathematical reasoning. It often identifies exactly what an argument needs, proves that fact, and explains why weaker-looking substitutes are insufficient. That is a real strength.

But I see four unresolved issues:

- The hierarchy between the original theorem, the reconstruction's quantitative refinements, and the formalization's achievements is not sufficiently prominent.
- The hardest and most distinctive mathematical material is often presented in the least effective order for a researcher trying to evaluate it.
- Some examples are pedagogically sound individually but do not instantiate the actual separation construction, which requires unusually careful explanation.
- The final PDF still exposes a great deal of its automated production and verification machinery rather than presenting a clean scholarly account.

There is also an important distinction in what I can conclude: I find substantial portions of the argument internally coherent on this reading, but that is not an independent certification of the complete 141-page proof. The Gaussian-chain and formal-model bridges particularly warrant independent specialist scrutiny.

## 1. The most important structural issue: what is this paper's actual contribution?

On page 1, the record clearly credits OpenAI with proving the nearly quartic separation. That is correct scholarly positioning within the document.

But the manuscript subsequently does several different things:

| Contribution in this record                               | Where it appears   | How it should be presented            |
| --------------------------------------------------------- | ------------------ | ------------------------------------- |
| Full reconstruction of the total-function separation      | §§3–7              | Principal expository contribution     |
| Complete derivation of the Forrelation ingredient         | §8                 | Major technical reconstruction        |
| Explicit supplier threshold and uniform parameter bound   | §8.14              | Quantitative refinements              |
| Growing-\\(k\\) separation schedule                       | §7.3               | Distinct quantitative consequence     |
| Alternative universal quartic proof with constants        | Appendix A         | Reconstructed known result            |
| Lean statements, compiled results and comparison evidence | Appendix G         | Formal verification and audit         |
| Original-claim catalogue and execution history            | Appendices B and F | Archival and reproducibility material |

The document knows these distinctions. Its introductory presentation does not give them appropriate relative weight.

The especially interesting material is the new-to-this-record Forrelation proof strategy using an algebraic bounded-bias transform and a decision-tree martingale, together with the explicit uniform estimate. That is substantially more intellectually interesting than the arbitrary numerical value of an eventual threshold.

Yet the abstract foregrounds \\(13669k^2\\), the logarithmic exponent six and the coefficient \\(1/400\\) almost as though these three numerical refinements are of comparable importance to the underlying methods.&#x20;

reasoning_record(4).pdf



They are not.

The first thing a specialist needs is the nature of the reconstruction, not the detailed constant accounting.

I would reorganize the opening around two primary contributions: the complete, model-explicit reconstruction and the independently developed technical derivation of its supplier bound. Then state the explicit constants, growing-parameter consequence and formal audit as distinct results.

That change would communicate the intellectual substance much more effectively without claiming priority or novelty that has not been established.

## 2. The quantum argument is better written than the document makes obvious

I went back through §§5.1–5.6 because this is where a reconstruction can sound persuasive without actually establishing the algorithm being claimed.

There are three genuinely difficult transitions, and the paper handles them relatively well.

### The comparison probabilities

The proof does not assume the comparison relation is transitive, or even that comparisons between losing columns have a well-defined correct answer.

Instead, it works with \\(a\_{ij}+a\_{ji}=1\\) and derives the expected-weight identity

\\[ \mathbb E[W\_{\mathrm{new}}\mid w] =\frac{W^2-\sum_iw_i^2}{2W} \leq\frac W2. \\]

This is excellent explanatory economy. One algebraic identity replaces what could have been several pages of informal reasoning about tournaments. The distinction between the real sampling procedure and the ideal weight process is also clear.&#x20;

reasoning_record(4).pdf



The four-candidate cyclic example on pp. 29–30 helps because it demonstrates exactly why transitivity is unnecessary.

My criticism is that the paper should state the mathematical insight even more forcefully before the calculations:

Complementarity, not transitivity, causes the weight to halve in expectation.

That is the idea the reader should remember. It currently appears throughout the proof, but not as prominently as it deserves.

### The exact sampled-label law

The distinction between obtaining some successful sample and sampling according to the correct normalized weights is central.

The paper correctly identifies the required distribution:

\\[ \Pr[i\mid\mathrm{success}]=\frac{w_i}{W}. \\]

Its discussion of retained comparison registers and orthogonal index blocks makes clear why the output distribution is a genuine probability calculation, not merely an intuitive analogy with classical sampling.

This is one of the strongest sections.&#x20;

reasoning_record(4).pdf



I would keep almost all of it.

### The retained-state amplification claim

Section 5.6 is more complicated. It distinguishes a measurement-level sampling guarantee from preserving the normalized successful quantum state.

That distinction is mathematically real. The example contrasting a pure \\(|+\rangle\\) register with a maximally mixed register having the same computational-basis distribution is effective.

But the paper makes the reader encounter three levels of guarantee across §5.1, §5.6 and Appendix G.7.

The crucial editorial improvement is to state the logical dependencies unambiguously:

The total-function quantum upper bound uses the measured-label guarantee. The stronger retained-state result is proved in ordinary mathematics and has a separate formalization status. The full physical retained-state bridge is not presented as completed in Lean.

This is already what the document says, but a researcher should not need to reconstruct that hierarchy from several sections.

In particular, G.7 explicitly says the missing physical bridge is not an additional assumption in the proof of Proposition 3.3. That is an important reassurance and deserves a prominent reference earlier, where the bound is first proved.

My judgment: the quantum proof writing is around 8.5/10. Most of its deficiencies are navigational rather than deficiencies of mathematical explanation.

## 3. The classical lower bound is the clearest part of the paper

This was my strongest positive finding on the second reading.

The classical lower-bound argument has a particularly coherent mechanism.

A dummy input has one zero in every column. A planted input erases one zero and fills a hidden certificate cell. An algorithm distinguishing the two must encounter a changed bit.

The paper separates the two ways of encountering a change:

\\[ \Pr[\text{erased zero queried}] \leq \frac{4G}{m^2} \\]

and

\\[ \Pr[\text{planted cell queried}] \leq \frac{G}{mL}+G(2/3)^r. \\]

These are assembled in §6.6 into the discrepancy bound (23). The finite arithmetic then gives a discrepancy of at most \\(6/100\\), whereas a bounded-error algorithm would require a gap of at least \\(1/3\\).&#x20;

reasoning_record(4).pdf



The proof's most delicate point is the treatment of the nonheavy-column event.

### What I particularly like about §6.5

The capped simulator never needs to know whether the original run will eventually be nonheavy. It enforces a cap during execution.

That allows the argument to bound

\\[ \Pr[\text{nonheavy and query hits true cell}] \\]

rather than incorrectly claiming a bound on the probability of finding the cell conditioned on nonheaviness.

The explicit counterexample in §6.5 makes the distinction genuinely understandable.

This is a strong example of how to write about adaptivity: give the correct event, explain why the tempting conditional formulation is wrong, and construct a simulator whose unconditional success controls the event.

### Where this section can still improve

It uses too many overlapping demonstrations.

Section 6.1 supplies the direct-product proof and an adaptive conditioning example. Section 6.3 supplies a four-column XOR planting example. Section 6.4 gives an independence counterexample. Section 6.5 supplies a capped simulator trace and another counterexample about conditioning. Section 6.7 supplies alternative search estimates.

Every example has a reason to exist.

Together, however, they make it harder to distinguish which concepts are logically necessary and which demonstrate potential failure modes.

I would keep the capped simulator trace and the conditional-event counterexample. Those directly support the difficult proof transition.

The independence counterexample in §6.4 is also worth preserving, but it could be placed in a clearly optional example subsection.

The alternate \\(2G/m^2\\) search bound in §6.7 is useful, especially for the formalization comparison, but it need not compete with the main \\(4G/m^2\\) argument.

The distinction is between completeness of the record and priority of presentation. You can preserve every proof without presenting them all as equally important.

## 4. The Forrelation proof is the section that most needs another editorial pass

This is the main place where my revised assessment becomes more demanding.

Section 8 contains sophisticated mathematics. It is also where I would expect the closest attention from an external researcher.

The problem is not principally that the equations are unexplained. Most are explained carefully.

The problem is that the reader learns what the technical choices accomplish before fully understanding why those choices are natural or how they fit into one strategy.

### The algebraic transform feels arbitrary on first encounter

Section 8.7 chooses

\\[ q(x)=\sqrt{2+x^2},\qquad \Psi(x)=\frac1{2q(x)},\qquad \varphi(x)=\frac{x(3+x^2)}{2q(x)^3}. \\]

It then establishes the identities and estimates required for integration by parts.

These calculations are clearly presented.&#x20;

reasoning_record(4).pdf



But a specialist's immediate question is:

Why this function?

Why the denominator \\(2+x^2\\)? Why this specific algebraic form? What other candidate functions were possible? Which property is essential, and which constant is convenient?

The text partly answers the last question, but not the first two.

One short paragraph before (F9) would substantially improve the exposition. It could explain that the construction seeks a bounded odd bias function \\(\varphi\\) and an auxiliary function \\(\Psi\\) satisfying

\\[ \varphi(x)=x\Psi(x)-\Psi'(x), \\]

with enough boundedness to control the product \\(\Psi(x)\varphi'(y)\\) along each Walsh edge.

Then it can introduce the displayed rational-algebraic choice as one explicit solution meeting those requirements.

That changes the reader's experience from “here is an inexplicable formula that works” to “here is the desired analytic interface and one convenient implementation.”

### Section 8.9 gets the calculations right onto the page, but not the geometry

The three-block calculation (F18)–(F21) is one of the most significant parts of the proof.

I appreciate that the document makes the repeated-coordinate derivatives vanish by multilinearity and carefully tracks which Gaussian variables each accumulated factor depends on.

The general invariant after that example is also a good way of proving the path identity.

But the reader has to follow several layers of indices simultaneously.

A diagram would have unusually high value here:

Conceptual structure of the path-derivative identity (F22), not a substitute for the proof.

The diagram itself is simple; the benefit is that it establishes the direction of the argument before the indices appear.

### Section 8.10 is remarkably detailed, but the purpose of the martingale is under-emphasized

The derivative-growth lemma (F25) is essential because the derivatives in (F22) are evaluated at biased points, not at zero.

The text explains this correctly through (F24).

It then proves a maximal estimate for a family of degree-\\(r\\) processes built along the decision tree. The induction on degree and the use of stopping before an uncontrolled increment are both worth retaining.&#x20;

reasoning_record(4).pdf



My recommended improvement is to place a short statement immediately before (F25) that describes the mechanism:

A shallow decision tree exposes few coordinates. Its adaptive choices cannot cause the total order-\\(r\\) derivative mass to grow arbitrarily, because the newly revealed centered coordinate produces a controlled martingale increment.

That is the principle.

The current proof explains every component but does not foreground that principle quite enough.

### Section 8.14 should be reorganized around its stronger theorem

This is a more substantial structural recommendation.

The paper first states the eventual fixed-\\(k\\) Forrelation hardness in §8.5 and only later proves the stronger uniform quantitative estimate (F43) in §8.14:

\\[ R(P\_{k,m})> \frac{2m^{1-1/k}}{18225k^2\ln(4km)} \\]

under the dimension condition \\(15k+2\leq 2t\\).

The latter estimate is important because §7.3 uses it to let \\(k\\) grow. It is not merely an optional strengthening.

I would state both conclusions near the start of the supplier proof, identifying (F43) as the quantitative proposition and the fixed-\\(k\\) threshold as its corollary.

Then the reader knows exactly what the long analytic proof is going to establish.

The constant calculations in §8.14 seem internally coherent in the passages I checked, including the amplification margin, the derivative estimate and the final specialization. However, those are precisely the sorts of calculations where a full independent expert proof review is valuable. The current record's explicit absence of human mathematical review remains a material limitation.

My assessment of §8: mathematically ambitious, quite carefully written, but probably the greatest opportunity for improving specialist comprehension.

## 5. There is a subtler issue with the examples

The paper uses three different kinds of examples.

Section 4.3 takes the genuine small Forrelation function \\(P\_{2,4}\\), but reduces the address length to \\(r=2\\) instead of the separation family's \\(r=40\\) at \\(m=4\\).

Section 5.2 uses an abstract four-vertex comparison table with a three-cycle among losing candidates.

Section 6.3 uses a toy XOR supplier rather than Forrelation and changes the local numbering conventions.

The text discloses all of these changes. That is good.

But a non-specialist could come away with the mistaken impression that the examples together constitute a small executable instance of the complete separation theorem.

They do not.

There is no problem using illustrative instances with altered parameters. Indeed, the actual asymptotic construction is extremely large even for the first parameters covered by the explicit estimates.

However, I would introduce all three examples under a single statement of scope:

These examples test separate logical interfaces of the construction; none is a finite numerical witness to the asymptotic separation.

That removes the need to repeat qualifications at every encounter and makes the epistemic status of the examples clear.

## 6. The paper does not foreground how enormous the input representation is

This deserves more emphasis than I gave it previously.

Section 4.2 calculates the physical Boolean input length, including the full certificate arrays.

With \\(r=20\log_2m\\), the construction stores \\(2^r=m^{20}\\) possible cells per column. The resulting input length has the bound

\\[ n=O_k\big(m^{22}(\log m)^3\big). \\]

The quantum query bound is nevertheless approximately \\(\sqrt m\\) up to logarithmic factors.&#x20;

reasoning_record(4).pdf



This is mathematically legitimate in the query model because computation between queries is free, and only actual input-bit oracle calls are charged.

The paper explains that convention, including the fact that it makes no gate-count or workspace bound.

Still, a reader evaluating the practical significance of the result should encounter this distinction earlier.

This is not an efficient physical algorithm in the ordinary time-and-memory sense merely because its query count is small.

Nor is it being claimed to be one.

A sentence in the abstract or opening could make that explicit.

It would preempt an obvious skeptical reaction: “You have hidden the difficulty in an enormous input encoding and free computation.”

The separation is a mathematical statement about query complexity. The paper should celebrate that precise achievement without leaving room for confusion about other computational resources.

## 7. Appendix G needs a stronger distinction between the proof and its formal coverage

On another reading, I think this appendix is substantially better than an ordinary automated verification report. Its status distinctions are careful and often specific.

But there is a presentation risk.

A reader could see a complete mathematical proof, a very large Lean development, four compared headline targets and dozens of other declarations, and conclude that every detailed mathematical step printed in the PDF has been independently checked in Lean.

That is stronger than what the appendix actually claims.

For example, the manuscript reports that the explicit Forrelation threshold is an ordinary mathematical specialization without its own Lean theorem. The uniform Forrelation estimate is built but not compared. The bounded-list tournament theorem is built but not compared. The retained-state amplifier has a narrower physical formalization scope than the ordinary statement in §5.6.&#x20;

reasoning_record(4).pdf

reasoning_record(4).pdf



These distinctions are crucial, and preserving them is one of the project's strongest credibility features.

The mistake would be trying to make the audit look uniformly complete when it is not.

Instead, I would provide a compact theorem-level status table at the beginning of Appendix G showing the exact mathematical claim, whether its declaration compiled, whether its particular statement was compared, whether it is on the headline dependency path, and what remains an ordinary argument.

Then a reader can use the full appendix to investigate each entry.

The current prose is precise but requires too much searching.

I also think Appendix G should distinguish the formalization's logical guarantee from the project's semantic confidence even more explicitly. Comparator acceptance of two statements sharing definitions is not independent validation that those definitions express the intended query model. The record recognizes this and includes independently specified semantic controls; that warning should accompany the initial description of the headline checks.

## 8. Specific final-editing defects I found in the rendered PDF

Here are three concrete examples beyond broad complaints about verbosity.

Page 17: The word interchangeable is broken across lines as `interchangea` / `ble.` without a hyphen. I checked the rendered page; this is not merely a text-extraction artifact. It is a small but real typesetting defect.

Pages 95 and 104: The Appendix B claim index contains mechanically duplicated proof references. For example, `lem-2.1.ii` repeats both §8.2 and §5.3, and `claim-comparison-state` lists §5.3 twice. The index is intentionally a literal claim catalogue, but the duplication still looks like generator residue.&#x20;

reasoning_record(4).pdf



Page 114: The bibliography still has forms such as “Robert Beals and Harry Buhrman and Richard Cleve and Michele Mosca and Ronald de Wolf.” That is a source-database convention, not properly edited bibliographic prose. The same appendix puts substantial provenance metadata inside references, making it more cumbersome than a standard bibliography.

I also inspected the PDF's link structure. It contains 82 relative-file launch links, alongside hundreds of internal and external links. A relative link to something like `expert_companion.md` may work in the original directory but is not a reliable way for a reader receiving only the PDF to open that resource.

Those are fixable production issues, not mathematical objections. But in a manuscript that makes such a strong claim to complete technical precision, they are worth fixing.

## 9. The manuscript needs a real conclusion

One thing I did not emphasize enough previously is the absence of a concluding synthesis.

The paper proves the exponent result in §7, then returns to prove the deferred Forrelation ingredient in §8, then enters its appendices. The document eventually ends with formalization details and the AI-use disclosure.

There is no single concluding section that tells a reader what the complete reconstruction has established and what its remaining limitations are.

For a 141-page record, that matters.

I would insert a brief conclusion immediately after §8.15, before Appendix A.

It should distinguish the completed ordinary proof of the separation, the additional uniform quantitative bounds, the formalized headline results, the more limited formalization of some stronger refinements, and the absence of external human mathematical review.

It should also identify the intended research value: a source-traceable, inspectable proof reconstruction rather than a new claim to priority for the separation.

That would give the manuscript an appropriate scholarly ending instead of ending inside its audit machinery.

## 10. What I would actually change next

I would not perform another indiscriminate rewrite of all 141 pages.

My priorities after this reading are:

| Priority   | Change                                                              | Why it matters                                                               |
| ---------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Critical   | Rewrite the first-page contribution framing                         | Experts need to know immediately what is original, reconstructed or verified |
| High       | State (F43) near the beginning of the supplier proof                | It is the real uniform theorem powering §7.3                                 |
| High       | Add a conceptual preface to the algebraic transform in §8.7         | Currently a major mathematical choice appears unexplained                    |
| High       | Add the Gaussian derivative-chain diagram                           | Makes the hardest analytic proof easier to navigate                          |
| High       | Add a formal coverage matrix to Appendix G                          | Prevents overinterpretation of the Lean evidence                             |
| Medium     | Distinguish illustrative examples collectively                      | Prevents confusion between toys and the actual family                        |
| Medium     | Separate numeric bound statements from their arithmetic derivations | Preserves rigor while improving proof flow                                   |
| Medium     | Add a conclusion after §8.15                                        | Restores the document's overall narrative                                    |
| Production | Fix references, typography, version metadata and relative links     | Makes the PDF more credible and independently usable                         |

## Final reassessment

I would now characterize the manuscript as follows:

Mathematical exposition

## 8.5/10

Proof organization

## 8/10

Technical record and audit quality

## 8.5/10

Scholarly presentation as a standalone paper

## 7/10

These ratings concern communication and organization, not the probability that every theorem is correct.

The most important conclusion from this rereading is that the main proof no longer needs wholesale explanatory expansion.

The original theorem, the Forrelation supplier, the certificate construction, the randomized lower-bound argument and the quantum tournament are now connected by intelligible mathematical explanations.

The paper is strongest when it isolates a mathematical invariant or contract and shows exactly why it suffices. It is weakest when it introduces sophisticated technical choices without motivating their design, or makes readers navigate historical evidence to determine the status of a claim.

For an expert in query complexity, I think the manuscript is now sufficiently coherent to justify a serious technical reading. I would not yet describe it as independently validated mathematics, or as fully polished for scholarly distribution.

My main change of opinion since the first pass: I would preserve considerably more of the long proof than I originally suggested cutting. The depth is often justified. The remaining task is to improve the hierarchy of ideas, explain the crucial design choices in §8, and make the verification boundaries immediately legible.

That is a much more targeted editorial task than rewriting the document from scratch.