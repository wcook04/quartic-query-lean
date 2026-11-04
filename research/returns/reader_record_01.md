# Detailed assessment of the revised reasoning record

Paper reviewed: A nearly quartic separation between randomized and quantum queries: a complete reasoning record — 141 pages, 4 November 2026 edition.

## Overall verdict

This is now a serious, carefully constructed mathematical proof record. It is considerably stronger as technical writing than a typical AI-generated mathematical manuscript. But it is not yet an excellent standalone mathematical paper.

The distinction matters. There is real mathematical substance, coherent proof organization, unusually explicit treatment of hidden assumptions, and a commendable separation between what is proved mathematically and what is formally checked.

The remaining weaknesses are predominantly editorial and architectural rather than problems of grammatical fluency. The document frequently becomes too concerned with explaining its own verification history, recording qualifications and enumerating evidence. That obscures the mathematical ideas that deserve the reader's attention.

My subjective assessment is:

| Dimension                                                   | Assessment |
| ----------------------------------------------------------- | ---------- |
| Mathematical precision of exposition                        | 9/10       |
| Local proof explanations                                    | 8/10       |
| Organization of the principal argument                      | 8/10       |
| Accessibility to a specialist encountering the construction | 7/10       |
| Concision and editorial discipline                          | 5.5/10     |
| Presentation as an independent research paper               | 6.5/10     |
| Quality as a comprehensive proof and verification record    | 8.5/10     |

These are writing assessments, not independently established correctness scores. I inspected the mathematical arguments and their presentation, but I have not independently certified every derivation or rerun the Lean development.

The principal improvement now needed is not another round of expanding proofs. It is deciding what the reader needs to see, in what order, and at what level of detail.

## 1. What is genuinely good now

### The mathematical mechanism is understandable

The opening succeeds at something difficult: it communicates how the nearly quartic separation arises without simply announcing asymptotic bounds.

It introduces the columns, the hidden certificate, the partial-function answers, the quantum comparisons and the planted classical lower-bound argument. Crucially, it gives the relationship between the costs:

\\[ Q(F\_{k,m})\lesssim \sqrt m\\,\operatorname{polylog}(m), \qquad R(F\_{k,m})\gtrsim \frac{m^{2-1/k}}{(\log m)^2}. \\]

From there, the exponent \\(4-2/k\\) is intelligible.

This is much better than beginning with 10 pages of formal definitions and expecting the reader to infer why they matter. The authorial attribution to OpenAI is also explicit, rather than presenting the original separation as a new theorem of this reconstruction.&#x20;

reasoning_record(4).pdf



### The proof has a recognizable logical spine

The sequence is effective:

§3 — The supplier

Establish the partial-function contract: classical hardness, quantum decoding and exact circuit certification.

§4 — The construction

Build one total function from the addressed certificates, with winner uniqueness and exact local tests.

§5 — Quantum upper bound

Comparisons, weighted tournament, bounded sampling and verification.

§6 — Classical lower bound

Hard product distribution, planted winner and capped simulator.

§7 — Exponent comparison

Combine the bounds for the same function; then §8 discharges the deferred supplier proof.

The document knows where its assumptions enter and when they are discharged. That is an important virtue, particularly in a long formal-mathematics account.

### The local writing is often excellent

Three passages stand out.

Section 4.7, pp. 22–23: The argument explaining why a genuine winner defeats an opponent with an unpromised address is particularly effective. It isolates two deterministic facts, explains which decoder must be correct, and explicitly avoids making any assumption about the other decoder. This is precise and intuitive.&#x20;

reasoning_record(4).pdf



Section 5.2, pp. 26–31: The fractional-weight tournament is presented with the required comparison interface, the exact expectation calculation, a cyclic four-candidate example, the sampling law and the coupling argument. The reader can distinguish the ideal process from the implemented bounded sampler. That is difficult material, and the presentation does not simply hide its central step behind an invocation of amplification.

Section 6.5, pp. 54–56: The capped simulator is one of the strongest pieces of writing. It distinguishes the original tree clock from the charged target-query counter, explains why truncation happens before the excess query, and proves a joint event rather than an invalid conditional probability bound. The worked example actually tests the delicate part of the argument.&#x20;

reasoning_record(4).pdf



These passages read like mathematical arguments with deliberate structure, not generic prose filling the spaces between equations.

### The document is careful about what formal verification does and does not establish

Appendix G is a genuine strength.

It distinguishes the compared theorem from the explicit-constants theorem, compilation from comparison, shared definitions from independently checked semantics, and the measured-label amplification route from the stronger retained-state specification.

In particular, §G.7 explicitly identifies a remaining physical retained-state formalization bridge without treating it as an assumption in the headline measured-label proof.

This is the right attitude toward formal evidence. It is more credible than indiscriminately calling every associated claim formally verified.

The problem is that this careful evidence analysis occupies too much of the reader's attention when the document is encountered as a mathematical paper.

## 2. The biggest remaining problem: three different documents are competing for control

The document is simultaneously trying to be:

1. A self-contained mathematical proof of the nearly quartic separation.
2. A pedagogical reconstruction that explains subtle mathematical decisions and potential mistakes.
3. An audit trail of formalization, execution receipts, historical revisions and statement comparisons.

All three are legitimate. They are not, however, the same literary form.

The first needs a clear theorem–lemma–proof progression. The second benefits from examples, counterexamples and informal explanations. The third requires exhaustive evidence labels and careful provenance.

The reasoning record currently switches between these forms frequently.

For instance, §4 establishes an interesting mathematical construction. It then gives a worked four-column instance, reports finite checks, distinguishes that example from a different exposition board, and references archived checker files. The underlying proof is good, but a reader has to distinguish which sentences advance the mathematics and which document the engineering process.

Likewise, §5.4 gives a genuinely important quantum complexity bound, but its exact numerical accounting occupies several pages. This is valuable evidence of precision. Nevertheless, it interrupts the momentum between the algorithm's correctness proof and its final asymptotic conclusion.

By the time the reader reaches Appendix F, the document has changed from mathematical exposition into a history of verification receipts.

The solution is not to delete the evidence. It is to make the separation between mathematical argument and verification history much sharper.

For this specific document, I would retain the fully detailed proofs. I would move more of the computational and historical commentary into clearly identified audit subsections or linked supporting material.

That preserves the record's defining advantage without making the reader work through the history of its production to understand the theorem.

## 3. The first two pages are good, but the contribution framing still needs refinement

The abstract is competently written and far clearer than many ambitious mathematical manuscripts. It immediately attributes the theorem, explains the construction and advertises the quantitative details.

But I would change how it distinguishes the original theorem from this document's own work.

At present, the reader is told that OpenAI proved the separation, followed by the statement that this record proves the theorem in full. Later the reader encounters explicit constants, a new self-contained analytic route, a growing-parameter schedule, worked examples and a Lean formalization.

These have different intellectual statuses.

An expert wants to know, immediately:

- Which mathematical result belongs to OpenAI's original preprint?
- Which proof steps are reconstructed rather than independently conceived?
- Which explicit quantitative estimates are derived in this record?
- What exactly does the Lean development establish, and what remains an ordinary mathematical proof?

Currently, the answers are present, but scattered through §1, §8.15 and Appendix G.

I would introduce a short “Scope of this reconstruction” paragraph after the abstract. It should classify the additions rather than merely enumerate them.

There is also a title issue. Although the subtitle says a complete reasoning record, the principal title remains extremely close to the underlying mathematical result. In a standalone PDF without a cover letter, that leaves some ambiguity about whether the writer is claiming the theorem or reconstructing it.

A clearer scholarly title would be:

A Complete Reconstruction and Formal Audit of the Nearly Quartic Randomized–Quantum Query Separation.

It would distinguish the intellectual activity from the original result before the reader opens page one.

Finally, the PDF would benefit from a conventional author byline, revision date, canonical repository link and explicit version identifier. The current authorship disclosure is useful, but it is not a substitute for basic publication metadata.

## 4. The mathematical exposition: detailed section-level criticisms

### Section 2 — rigorous, but disproportionately long before the construction

Section 2 is valuable because it rules out several subtle model mismatches. In particular, the treatment of finite mixtures, the inclusive \\(2/3\\) threshold, off-promise query caps and the distinction between retained quantum states and output distributions is carefully argued.

The examples in §2.6 are also well chosen. The OR example demonstrates a genuine endpoint issue, and parity demonstrates why the query-model convention matters.

I would retain them.

However, a query-complexity specialist reading this document for the separation must get through approximately eight pages of model definitions before reaching Forrelation in §3.

The reading guide alleviates that, but there is still considerable repetition between the introductory model discussion and Appendix G.2.

I would shorten the narrative portions of §2, not the definitions. The technical proofs of model equivalence can remain accessible under explicit subsection headings.

The goal should be that a specialist can obtain the exact model in approximately two pages, then skip the demonstrations without losing the argument.

### Sections 3–4 — among the best-organized material

The three-part Forrelation contract in §3.2 is excellent. It prevents the subsequent construction from importing an unspecified kind of oracle or an unquantified hardness assertion.

Section 4 then translates the contract into a total Boolean function and exact local verification tests.

The distinction between a circuit's transcript being gate-consistent and its input actually satisfying the promise is particularly well explained. The proof around (4.12) is appropriately explicit.

Section 4.6 is also unusually careful about coherent access to an arbitrarily chosen test index. It does not conflate a classical list of test procedures with a coherent quantum evaluator.

I would make only limited edits here.

One change would be to add a compact diagram immediately after §4.2 showing the selected cell in a winning column and its outward pointers. The four-column table in §4.3 is mathematically useful, but it asks the reader to visualize a structure that would be easier to understand graphically.

The diagram should depict the actual bit-query structure, not an abstract picture that conceals the pointer-reading cost.

### Section 5 — excellent central argument, excessive accounting in the main flow

The strongest mathematical writing in §5 is the explanation of the fractional-weight process.

The derivation

\\[ \mathbb E[W\_{\mathrm{new}}\mid w] =\frac{W^2-\sum_iw_i^2}{2W} \leq \frac W2 \\]

is the conceptual centre of the tournament. Its explanation is direct, and the four-candidate cyclic example reinforces the exact point: global transitivity is unnecessary.

The treatment of amplification is also stronger because it distinguishes getting a successful sample from preserving the exact conditional label distribution.

I would not simplify those arguments.

Where the section becomes harder to read is the transition to §5.4. The explicit budget, the amplification ceilings and the accumulated constant \\(C_k\\) are valuable for an audit, but they consume too much attention.

One possible reorganization is to conclude the main quantum analysis with the following hierarchy:

First: a bounded-error algorithm exists on every total input.

Second: its query complexity is \\(O_k(\sqrt m\\,\mathrm{polylog}\\,m)\\).

Third: the chosen circuit and finite accounting give the explicit logarithmic power six.

Then give the complete constant derivation in an adjacent technical subsection or appendix.

Currently the reader must process much of the third layer before being allowed to leave the quantum section.

### Section 6 — genuinely strong lower-bound exposition

The classical lower-bound section is probably the most convincing part of the document as a pedagogical proof.

The architecture is clear: an independent hard distribution, a planted winner, the first-difference event, the erased zero, the heavy columns and the guessed certificate address.

The distinction between conditioning on a light column and bounding the corresponding joint event is handled particularly well. The toy counterexample helps explain why the tempting alternative is invalid.

The alternative unnormalized direct-product proof in §6.1 is also useful because it connects the ordinary mathematical argument with the formalization.

My criticism is principally about duplication.

Section 6.2 repeats quite a lot of the construction already established in §4, and §6.3 then restates the lower-bound mechanism again. This makes each subsection independently readable, but it reduces the progression of the whole paper.

You could remove some of the repeated recap without losing a single mathematical justification.

I would also revise symbol reuse. For instance, \\(Z\\) serves as a product potential in §6.1 and then as a discovery count in §6.4. The text explicitly warns the reader, but preventing the collision is preferable to explaining it.

### Section 7 — clear mathematical conclusion, but two results deserve different emphasis

The fixed-\\(k\\) exponent deduction in §§7.1–7.2 is well written.

It correctly distinguishes excluding every exponent below four from obtaining an exact fourth-power lower bound using one fixed \\(k\\). The quantifier order is made explicit, and the treatment of the logarithmic losses is careful.

The growing-\\(k\\) calculation in §7.3 is a substantial further quantitative result. It uses the uniform Forrelation estimate and the explicit dependence of the quantum constant on \\(k\\).

This deserves more editorial prominence.

At present, it reads like another technical extension following the principal theorem. I would give it a named proposition, a brief explanation of the parameter-balancing idea, and then the existing proof.

In particular, the competition between the \\(40k\\) quantum-cost contribution and the \\(\ell/k\\) classical-cost contribution is the conceptual reason for the parameter schedule. That explanation should precede the numerical constants and remain visually distinct from them.

### Section 8 — serious mathematics, but requires a stronger conceptual map

Section 8 is perhaps the most technically ambitious part of the record.

The algebraic truncation, Gaussian integration identity, path derivative, bounded-bias tree martingale and final moment comparison form a coherent proof strategy.

The writing is strongest when it explicitly identifies why an operation is legitimate. The discussion after (F22), for example, distinguishes the underlying independent Gaussian variables from the correlated transformed pair and avoids assigning them an incorrect product density.

Similarly, §8.10 carefully explains why one must bound derivatives at biased points rather than use only uniform degree-\\(k\\) Fourier coefficients.&#x20;

reasoning_record(4).pdf



These are the kinds of details mathematical reviewers look for.

What is still missing is a very clear conceptual picture of the Gaussian chain before the indices begin.

The three-block calculation in §8.9 helps, but an expert encountering the method for the first time has to hold the entire chain in their head while reading identities (F17)–(F22).

A small diagram showing how a derivative travels from block 0 to block \\(k-1\\), with one Walsh factor and one integration-by-parts factor per edge, would improve this significantly.

The last subsection, §8.15, does a good job attributing the antecedents and distinguishing this particular method from the literature. That material deserves to remain.

## 5. The appendices are where the document still feels least professionally edited

This is my strongest editorial criticism.

### Appendix B: exhaustive, but visibly generated

The 121-claim catalogue has a legitimate purpose. It gives a correspondence between maintained claims and their printed proofs.

However, it consumes approximately twenty pages and reads much more like a generated verification inventory than a mathematical appendix.

I found 18 catalogue entries containing duplicated identical section references in their `Argument:` fields. For example, the entry for Lemma A.2 on p. 112 lists §A.2 twice. Other entries repeat the same section three or more times.

This does not undermine a mathematical theorem, but it is exactly the sort of small mechanical defect that makes an expert think the document was automatically assembled without a final editorial pass.

I would fix these systematically in the catalogue generator.

More importantly, I would consider making the full catalogue a companion index, linked from the PDF, while retaining a compact description and perhaps the principal claim mappings in the paper itself.

### Appendix C: excellent provenance, unconventional bibliography

The edition-specific references are unusually careful. Distinguishing different versions of Beals et al., retaining exact page numbers and explaining which versions support which comparisons are all strengths.

But the bibliography often exposes raw metadata and author-name syntax that looks closer to BibTeX source than a finished journal reference.

The SHA-256 values and archive details are useful for reproducibility; they are not normally what a reader needs inside the primary bibliography.

I would separate a conventional reference list from a machine-readable edition and provenance register.

That would preserve the exact evidence while making the paper feel more scholarly and less like an internal repository report.

### Appendices D–E: mostly well handled

The earlier threshold derivation in Appendix D is explicitly historical, and the source comparisons in Appendix E are carefully qualified.

I particularly appreciate that the Bansal–Sinha displayed-step criticism is not presented as a refutation of their theorem. It identifies a specific algebraic discrepancy and gives a weaker sufficient bound without making a broader priority claim.

The issue is placement. The reading guide raises this source-display concern on page two, before the reader has understood the construction.

That is too early.

Keep the mathematical analysis in Appendix E, but avoid foregrounding a disputed literature detail in the opening reading instructions unless it is necessary to understand the proof's validity.

### Appendices F–G: technically valuable, but dominated by provenance language

Appendix F's historical receipt narrative is appropriate for a software verification archive. It is less appropriate as a central component of a mathematical publication.

Appendix G is much more useful as mathematics because it explains the models, actual theorem statements, proof dependencies and formalization boundaries.

But even here, phrases about frozen snapshots, receipts, source bindings, comparison coverage and historical reviews recur throughout.

The result is that the reader must repeatedly distinguish what was built on 2 November, what was compared on 3 November, which source commit is pinned, which theorem was merely reviewed textually, and which statements have an ordinary but not formal proof.

That information is important. Its presentation should be substantially compressed.

I would place a one-page current verification status at the beginning of Appendix G: the four headline statements, which were formally compared, which more explicit refinements were only built, and which mathematical bridges remain ordinary arguments.

Then retain the complete chronological receipt history outside the primary mathematical narrative.

One particularly important distinction to highlight is that the explicit threshold \\(t\geq13669k^2\\) is proved in the ordinary argument but is not itself a Lean theorem in the evidence described by G.4. The current text says this accurately; it simply makes the reader work too hard to discover it.

## 6. Specific publication and PDF defects

I also inspected the rendered PDF and its hyperlinks.

The typesetting itself is generally good. The equations and matrices are legible, mathematical symbols display correctly, and the document has 99 PDF outline/bookmark entries. The internal cross-references are real, clickable destinations.

There is, however, a concrete standalone-distribution problem.

The PDF contains 82 relative-file link actions. They refer to files such as `expert_companion.md`, `exposition.md`, `reasoning_record_correspondence.json` and paths under the research returns.

Those links depend on the PDF being opened in an environment with the corresponding directory structure. If someone receives only this PDF, many of those links will not resolve.

That matters because the document repeatedly asks the reader to consult those files.

For the externally distributed PDF, I would replace relative-file destinations with immutable public repository URLs or provide a verified accompanying archive. Internal section links can stay as they are.

The document would also benefit from an ordinary linked table of contents after the reading guide. The bookmarks help, but a reader of 141 pages should be able to see the full chapter architecture without opening the PDF outline sidebar.

## 7. How much of this is AI-like writing?

The main mathematical exposition does not exhibit the worst characteristics of AI-generated research prose.

It is not primarily a collection of vague claims followed by confident assurances. The important assertions often have actual calculations, carefully constrained hypotheses and explicit proofs.

Where it does feel AI-generated is in the amount of self-commentary.

There are many sentences explaining what a subsection is about to do, what the previous subsection did, what the formal proof does not claim, and what kind of evidence supports the next sentence.

Some of that is necessary because the paper's scope is unusually broad.

But much of it would be removed by an experienced mathematical editor on a final pass.

The writing repeatedly tells the reader that it is being precise rather than allowing its mathematical structure to establish that precision.

The catalogue-reference duplicates are another example of mechanical residue.

The next improvement should therefore reduce meta-commentary, not reduce mathematical rigor.

A strong paper can be very detailed without constantly explaining that it is detailed.

## 8. My recommended final editorial pass

In priority order:

1\. Clarify the contribution and authorship framing on page one. State plainly that the separation is OpenAI's result and identify which technical refinements, reconstructions and formal-audit work this document supplies.

2\. Establish a consistent hierarchy of explanation. For each major proof: motivation, precise statement, key idea, full argument, and optional evidence or implementation detail. The main mathematical line should never be buried inside a receipt narrative.

3\. Keep §§4–6 substantially intact. These sections contain some of the strongest writing. Reduce repeated recaps and relocate exact constants where appropriate, but do not sacrifice the event-level and coherent-state distinctions.

4\. Improve the visual explanation of the two difficult structures. Add one figure for the addressed-certificate board and one for the Gaussian derivative chain. Neither needs to be elaborate; they should convey structure unavailable from the equations alone.

5\. Separate the mathematical bibliography from the source-provenance ledger. Preserve every version-specific comparison and hash, but give the reader conventional references in Appendix C.

6\. Clean Appendix B programmatically and make Appendix G's current evidence status immediately visible. Remove duplicate references, explain the difference between ordinary and formally checked refinements in one compact summary, and move historical execution detail behind that summary.

7\. Make the PDF self-contained as a distribution artifact. Replace relative-file links, include the revision date and document identifier, and provide a conventional contents page.

## Final assessment

I would distinguish three reactions from three different expert readers.

A quantum query-complexity researcher who opens the PDF to understand the new separation should find that the core proof architecture is intelligible, that the main transitions are explained, and that several subtle points receive serious treatment. But they may find the 141-page presentation exhausting and wonder why so much of the verification process is inside the mathematical exposition.

A formal-methods researcher is more likely to appreciate Appendix G, the explicit theorem-model distinctions and the carefully limited claims about comparison and compilation. The evidence is unusually nuanced, although the central status could be exposed more efficiently.

A mathematical editor assessing the document as a publication would probably regard it as a substantial technical reconstruction that needs further editing before publication, rather than as a polished research article.

That is not a judgment that the text is mathematically invalid. It reflects the difference between a complete research record and an expertly edited paper.

I would not recommend another wholesale rewriting pass. The main proof is far enough along that aggressive rewriting risks making it less precise. I would concentrate on contribution framing, removal of process narration, appendix organization and distribution quality.

The strongest thing this revision achieves is that a reader can now trace where the central arguments come from and how the conclusions depend on them. The strongest thing it has not yet achieved is making that journey feel effortless.

For a document of this scope, that is now the central writing challenge.