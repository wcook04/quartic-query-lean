# Review of the revised Expert Companion

Reconstructing OpenAI’s Nearly Quartic Query Separation · 19 pages · 4 November 2026

I read the full 19-page PDF, including the mathematical arguments in Sections 2–5, the Lean evidence in Section 6, the counterexamples, literature comparisons, and the proofs and estimates in Appendices C–E. I also inspected the rendered pages, figures, tables, equations, and hyperlinks.

## Overall assessment

This is now a serious, well-written technical reconstruction. It has a coherent mathematical narrative, precise statements, thoughtful proof organization, and a substantially more disciplined approach to identifying what is proved, borrowed, formalized, or still incomplete.

I would not dismiss it as generic AI-generated mathematical exposition. Its strongest sections demonstrate genuine attention to the places where mathematical arguments can fail: exact sampling distributions, all-branch query caps, independent side information, conditioning on adaptive events, and the distinction between formal claims and their physical interpretation.

But I would distinguish two judgments:

As an expert-facing reconstruction of an important query-complexity result, it is strong. A researcher familiar with randomized and quantum query complexity could read this productively. The writing generally respects their time and intelligence.

As a standalone research paper announcing a completed formalization, it is less convincing. Not because the prose is poor, but because the formalization occupies relatively little of the paper, several important technical dependencies live in the separate reasoning record, and the exact contribution beyond the original theorem still requires some interpretation.

My provisional ratings, assessing the document rather than independently certifying its mathematics, are:

| Dimension                              | Assessment |
| -------------------------------------- | ---------- |
| Technical prose                        | 8.5/10     |
| Organization and proof narrative       | 8.5/10     |
| Explanatory precision                  | 8/10       |
| Contribution framing                   | 8/10       |
| Standalone readability for specialists | 7.5/10     |
| Presentation of Lean evidence          | 6.5/10     |
| Typography and figures                 | 8.5/10     |

Overall: approximately 8/10 as a specialist companion paper. It needs targeted improvements rather than another wholesale rewrite.

The biggest remaining weakness is not that the mathematics is inadequately explained. It is that the reader still has to work too hard to determine exactly which achievement belongs to this paper, which belongs to OpenAI, which has been checked in Lean, and which remains supported by a separate record.

## 1. What is genuinely good now

### The introduction is doing its job

Page 1 begins by crediting OpenAI and immediately identifies the two mechanisms: the weighted quantum tournament and the classical reduction from finding a planted cell to predicting its address.

The contribution paragraph explicitly says that the separation theorem, total function, and reductions are OpenAI’s. That is important. It avoids the impression of claiming an independently discovered result.

Section 1.1 is particularly successful. Its paragraphs have a deliberate progression: first the certificate construction, then why comparisons are cheaper than verification, then the classical hidden-cell argument.

The line explaining that the losers need not form an order, because their survival probabilities supply the sampling weights, is especially effective. It identifies why the quantum algorithm is not merely applying ordinary minimum finding.

Likewise, the classical paragraph makes the lower-bound mechanism intuitive without pretending it is trivial.

I would preserve nearly all of Section 1.1. It is one of the best-written parts of the paper.&#x20;

expert_companion(3).pdf



### Section 3.2 is the technical highlight

Pages 6–7 are particularly convincing.

You define the comparison probabilities, assign the survivor weights

\\[ w_i=\prod\_{b=1}^{n}a\_{i\rho_b}, \\]

and then explain why the expected total weight halves. Equation (8) makes the essential argument visible:

\\[ \mathbb E[W\_{\mathrm{new}}\mid w]\leq \frac W2. \\]

The proof does not smuggle in transitivity. It only uses the complementarity of comparison probabilities.

The next step is equally important: Equation (9) explains how fresh comparison workspaces produce weights that genuinely multiply, giving the required conditional distribution rather than merely returning an arbitrary successful candidate.

This is where weaker explanations of such an algorithm often become hand-wavy. Your version carefully distinguishes:

- the probability of a successful state preparation;
- the distribution of labels conditional on success;
- the amplification required to achieve a fixed query cap.

The four-candidate numerical example on page 7 is also useful because it demonstrates that the two normalizations are different.

I would regard this section as a substantive strength, not an area requiring major rewriting.&#x20;

expert_companion(3).pdf



### The classical lower-bound explanation is exceptionally careful

Section 4, particularly pages 9–11, is probably the other strongest part.

Figure 2 shows the two distributions clearly: a dummy zero-input and a planted one-input differing at the erased zero and the selected certificate cell.

Section 4.4 then addresses the difficult issue: a query to a cell is effectively a prediction of an entire hidden address.

You explain why the simulator fixes a column and an original-query time, why it stops before exceeding the address-query allowance, and why it receives outside data that are jointly independent of the target instances.

Most importantly, you distinguish the joint event

\\[ \Pr[\text{light and correct prediction}] \\]

from the conditional success probability given lightness. This is not pedantry; conditioning incorrectly here could invalidate the lower-bound reduction.

Appendix A.7 supplies a counterexample to precisely that mistake.

The result is a proof that is unusually explicit about why its probability manipulations are legitimate. The transition from (12) to (13), followed by the final discrepancy bound (14), is also well organized.&#x20;

expert_companion(3).pdf



### The fixed-parameter conclusion is concise and correct in shape

Page 11 properly states the quantifier order: choose the exponent being excluded, then fix \\(k\\), then take \\(m\\) large.

That is exactly the distinction needed to avoid treating a fixed-\\(k\\) asymptotic bound as automatically uniform in \\(k\\).

The optional growing-parameter analysis is separately confined to Appendix E. This is a sound structural decision.

These are all signs of a carefully constructed mathematical exposition.

## 2. The biggest remaining weakness: Section 6

This is where I would concentrate the next revision.

Page 12 is honest and careful, but it is not yet as informative as the preceding mathematical sections.

The opening says:

> The Lean development proves the headline results without open mathematical hypotheses.

You then distinguish compiled declarations, axiom audits, comparison against specifications, and correspondence with physical quantum implementations.

These distinctions are important. The table is useful. The hyperlinks genuinely lead to individual declarations, and the formal source editions are pinned rather than vaguely referenced.

Nevertheless, the reader receives a status report about the formalization rather than a sufficiently concrete explanation of the formalization itself.&#x20;

expert_companion(3).pdf



### What is missing?

A mathematician reading the paper will understand the mathematical theorem by page 11. But a formal methods researcher encountering page 12 still needs answers to several questions.

What are the precise Lean definitions of randomized and quantum query complexity? Which results about algorithms are proved from these definitions, and which enter through dependencies? What is the exact form of the main theorem? What assumptions does the axiom audit report? How does the formal representation of the comparison sampler connect to the concrete algorithm in Section 3?

You link to material that addresses these questions, but the reader has to leave the paper to understand the central formalization achievement.

That is a disproportionate weakness when the subtitle explicitly advertises the Lean formalization.

I would expand this section to approximately two pages and include an abbreviated statement of the central Lean theorem, a compact explanation of the formal query model, and an example of how one of the paper’s difficult proof obligations appears in Lean.

The most natural choice would be the exact measured-label sampling law. It is technically central, interesting in its own right, and connects the mathematical reconstruction to the formal work.

### The retained-state limitation needs a clearer explanation

The abstract says:

> ... a stronger retained-state theorem whose physical correspondence remains incomplete.

Later, Section 6 explains the distinction more precisely.

I appreciate the disclosure. It is considerably more credible than claiming complete physical correspondence without qualification.

But to a reader skimming the abstract, it can sound as though the main quantum result is incompletely formalized.

Your actual distinction appears narrower: the headline argument uses the measured-label result, while the stronger retained-state interpretation has an additional correspondence obligation.

Make that relationship unmistakable.

If the main formal theorem does not depend on the unresolved retained-state correspondence, say that explicitly, ideally beside the formal dependency map. The reader should not have to infer it.

Similarly, the table identifies the explicit-constant named-circuit theorem and the uniform Forrelation estimate as built and axiom-audited but outside the configured comparison bundle. That is a meaningful evidence distinction, not merely administrative detail.

It would help to explain what remains to be done to bring those endpoints into the same comparison regime as the headline statements.

This is the single largest remaining opportunity to strengthen the paper's academic credibility.

## 3. The contribution is properly credited, but its significance could be more explicit

You have already solved the basic attribution problem.

The contribution paragraph on page 1 clearly credits OpenAI with the theorem and construction. The literature section on page 3 identifies the antecedents. Appendix B goes beyond name-dropping references and actually distinguishes query costs, access models, and comparison contracts.

That is good scholarship.

The remaining problem is subtler.

A reader may finish the paper thinking:

I understand what OpenAI proved, but what specifically did this reconstruction establish beyond explaining it?

The answer is present, but distributed across the manuscript.

There are several different types of achievement here: reconstructed and explicitly costed proofs of OpenAI's reductions, clarified finite counterexamples to invalid shortcuts, a Lean formalization of the headline mathematical results, and additional uniform-parameter analysis supported by the reasoning record.

These are not equivalent claims of originality.

I would explicitly distinguish new exposition, independent reconstruction, formal verification, and any additional mathematical estimates.

For example, the paper's quantitative constants are labeled as reconstruction choices. That is precise. The uniform bound (16) in Appendix E is attributed to a derivation in your reasoning record rather than represented as an independently proved theorem within this PDF. Again, precise.

But an expert should not have to assemble this classification independently.

The current contribution paragraph is good enough to preserve; I would add a brief contribution breakdown immediately after it, rather than replace it with grander claims.

Also, the main theorem and Propositions 2 and 4 are properly credited to the original work, but phrases such as reconstructed form of or adapted quantitative version of would occasionally clarify when the statements are not literal transcriptions.

This would make the paper more persuasive without overstating its novelty.

## 4. The important remaining proof-exposition issues

### Section 2: the exact circuit is somewhat too compressed

Pages 3–5 introduce the Forrelation supplier, exact circuit, certificate cells, transcript tests, and encoding length.

This section handles a large amount of material efficiently. The separation between a cheap quantum decoder and an exact circuit that recognizes domain membership is especially good.

But the exact circuit size

\\[ S\leq 200(k+1)^2m\ell^2 \\]

is a critical input into the quantum verification cost, and its derivation is primarily deferred to the reasoning record.

The paper gives a short explanation involving integer Walsh transforms, butterfly layers, and bit widths. It communicates plausibility, but does not make the bound easily checkable from this document alone.

I would add a compact derivation of the circuit-size accounting, even if the detailed gate-level construction remains in the record.

It would connect the circuit definition to the bound \\(K=O_k(m\ell^3)\\) on local tests and, ultimately, to the quantum bound in Theorem 1.

The mathematical reader should be able to check that dependency without opening another file.

### Section 3.3: make the quantum cost decomposition easier to scan

The verification error argument and final cost calculation are soundly organized, but tightly packed.

The section goes from local-test search to conditional errors, then combines the tournament and verification costs into the deliberately loose \\(O_k(\sqrt m\\,\ell^6)\\) bound.

A compact cost table would make the calculation easier to audit, separating address decoding, one comparison, tournament sampling, and verification.

This is not necessary for correctness, and I would not expand the proof much. It is simply a high-value readability improvement.

### Section 4.4: retain the proof, but front-load the target inequality

The planted-cell argument is already one of the manuscript's best sections.

One improvement would be to state the intended decomposition before constructing the simulator:

\\[ \Pr[\text{selected cell visited}] \leq \Pr[I\text{ heavy}] + \Pr[I\text{ light and selected cell visited}]. \\]

The reader could then anticipate the heavy-column estimate and the direct-product prediction estimate.

Currently, those pieces become clear during the argument. Showing the decomposition first would make the proof easier on first reading.

I would change little else in Section 4.

### Appendix E: its evidentiary status matters

Appendix E obtains a single family with

\\[ R(F_t)\geq Q(F_t)^{4-o(1)} \\]

using a uniform Forrelation estimate stated from the reasoning record.

This is a nontrivial refinement of the fixed-parameter presentation, and the distinction between fixed and growing \\(k\\) is carefully maintained.

But the uniform estimate (16) is not proved inside this PDF. The appendix describes its ingredients and points to the record for the actual analytic argument.&#x20;

expert_companion(3).pdf



That is acceptable for a companion whose scope is explicit. It would be insufficient if the paper were intended to be a self-contained publication of that uniform analytic result.

I would keep Appendix E, but make sure the introduction describes it as a deduction from the separately documented uniform estimate, not as a complete self-contained analytic proof.

## 5. The counterexamples are a real asset

Appendix A is more valuable than it may initially appear.

Most examples identify a specific hypothesis whose omission would break a proof. The particularly good ones are A.4 on independence of the planted column, A.5 on expected versus worst-case query caps, A.6 on joint independence, and A.7 on conditioning on lightness or compliance.

These are not arbitrary exercises. They are precisely related to delicate transitions in the main argument.

For an expert reviewer, this communicates that the proof has been examined adversarially, not merely paraphrased.

I would keep these examples, including the distinction in A.7 between a joint-event bound and a conditional-success bound. That distinction is easy to mishandle and difficult to explain well. Your treatment is unusually careful.

Appendix B is similarly valuable. It does not claim that every earlier cheat-sheet construction has a cubic ceiling; it explicitly limits the conclusion to the balanced AND–OR recipe being analyzed. That kind of careful restriction makes the writing more trustworthy.

The main editorial risk is one of balance. There are several pages devoted to protecting against invalid shortcuts, while Section 6 gives relatively little space to the formalization. I would increase the space for Section 6 before expanding the counterexample collection any further.

## 6. Typography, references, and research presentation

I inspected the actual rendered PDF rather than relying entirely on extracted text.

The typography is professional and consistent. Equations are readable, the margins are reasonable, the reference links are visibly distinguished, and I did not see obvious clipping or broken mathematical glyphs.

Figure 1 on page 2 and Figure 2 on page 9 are effective. The first establishes the relationships between columns, address blocks, and certificate cells. The second makes the coupling between the dummy and planted inputs concrete.

The figures are not decorative: they help explain what the surrounding proofs are doing.

The page 7 numerical table is also useful, although I would give it a caption or a clearly identified example number. It is important enough to deserve an unambiguous cross-reference.

The reference list is reasonably comprehensive, and I checked that the PDF contains actual hyperlinks to pinned source files, including the original OpenAI PDF. That is a positive feature; the provenance is not simply asserted.

Two presentation details deserve attention.

First, the manuscript currently has no obvious canonical project or artifact link in its front matter. The necessary links eventually appear in the bibliography and Section 6, but a short permanent source URL near the title would help someone receiving the PDF independently.

Second, the artifact-version story could be clearer. The paper references specific older source editions of the record and Lean implementation, while you report a newer document revision through `071ce02`. Pinning prior validated sources is completely legitimate. But state explicitly which versions constitute the validated formal evidence, and which versions are newer expository revisions.

On page 12, the sentence that the revision claims no new execution also deserves that precision. Your report of 264 passing tests does not automatically contradict it—those tests may be different from the Lean build and axiom checks—but readers should be told which checks were rerun and which were inherited from a pinned earlier validation.

Finally, the AI-assistance footnote is appropriately transparent. I would retain the disclosure, but pair it with precise reproducibility evidence rather than allowing the phrase AI systems ... performed the recorded checks to carry too much evidentiary weight by itself.

## 7. What I would change next

I would make a focused revision, not another general prose rewrite.

| Priority    | Action                                                                                            | Reason                                                                                             |
| ----------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| 1 — Highest | Expand Section 6 with actual formal statement details, model description, and proof dependencies  | The paper currently explains its mathematics more concretely than its advertised Lean contribution |
| 2 — High    | Clarify the relationship between the measured-label theorem and retained-state correspondence     | Prevents readers mistaking an auxiliary correspondence gap for an unresolved headline theorem      |
| 3 — High    | Distinguish the specific reconstruction, formalization, and additional quantitative contributions | Gives researchers a precise answer to what this work adds                                          |
| 4 — Medium  | Make the exact circuit-size accounting in Section 2 more self-contained                           | Strengthens the dependency leading to the quantum bound                                            |
| 5 — Medium  | Add a quantum-cost summary and front-load the planted-cell decomposition                          | Improves navigability without rewriting the proofs                                                 |
| 6 — Lower   | Add an example caption, artifact/version link, and clearer test provenance                        | Improves the final scholarly presentation                                                          |

I would not spend the next revision adjusting individual sentence rhythms throughout the document. Most of that work has already been done well.

## 8. How I think an expert would receive it

Imagine a theoretical computer scientist receives this as a PDF attachment and reads it without knowing you or the history of the project.

The first two pages would make a fairly good impression. The title accurately signals a reconstruction rather than a new discovery. The opening is technically competent. Figure 1 is helpful. The theorem states explicit parameters.

By Section 3.2, the reader should see that the document is more than a shallow summary. The distinction between arbitrary probabilistic comparisons and a fixed tournament orientation, and particularly the exact conditional sampling construction, supplies substantive mathematical detail.

Section 4.4 reinforces that impression. The simulator, stopping rule, independence conditions, and joint-event argument are explained at a level appropriate for someone who might actually try to check the reduction.

The main questions I expect such a reader to have are not about whether the text sounds academic. They are likely to be:

How much of this is independently reconstructed versus imported? How does the Lean development model the quantum query algorithm? And can I inspect the exact checked statement and its dependencies without navigating a large separate record?

These are reasonable questions, and the paper can answer them more efficiently.

I would distinguish that from the stronger claim that a specialist has verified the full mathematical correctness. I have assessed the internal argument, exposition, and presentation here; I have not independently reproduced the original source comparisons, rebuilt Lean, or certified the imported analytic estimates.

## Final judgment

The paper's principal strengths are now mathematical rather than cosmetic. Its narrative is coherent, the difficult probabilistic arguments are explained with real care, and the language is mostly concise and appropriate for a theoretical-computer-science audience.

The revision has reached the point where a mathematically sophisticated reader can productively engage with the actual claims instead of first having to decipher what the document is attempting to say.

Its remaining weakness is a mismatch between its strongest achievement as presented—an unusually detailed reconstruction of the randomized–quantum separation—and its advertised additional achievement, the Lean formalization, which is comparatively underexplained in the PDF itself.

If the objective is a highly credible companion to the OpenAI result, I think it is close. If the objective is a paper that makes formal-methods researchers take the verified reconstruction seriously on its own, Section 6 and the contribution-to-evidence mapping are where the next substantial gains lie.

I would preserve the core mathematical prose, especially Sections 3.2 and 4.4, and make the next revision principally about precisely exposing the formal achievement rather than rewriting an already strong exposition.