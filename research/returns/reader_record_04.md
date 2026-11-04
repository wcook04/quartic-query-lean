# Fourth reading — the remaining weaknesses are more specific than I thought

I've reread the reasoning record again, concentrating on its mathematical dependencies rather than its general presentation. I also compared the reconstruction with the original OpenAI paper and independently checked some finite calculations.

My revised judgment: the main proof reconstruction is quite strong, but there are still important problems with how the manuscript communicates what has been established, what is genuinely additional, and which steps carry the greatest mathematical risk.

This pass uncovered two issues I hadn't emphasized properly before: the distinction between the two hard distributions in the argument, and the actual strength of the growing-\\(k\\) quantitative result.

Neither is necessarily a mathematical error. Both matter a great deal to an expert evaluating this paper.

## 1. The two hard distributions deserve a much clearer explanation

This is probably my most important new criticism of the mathematical exposition.

The proof introduces two different kinds of difficult input distributions at different stages.

In §6.2, the manuscript needs a distribution \\(\mu\\) supported entirely on the promise of the Forrelation function. It obtains this through a finite minimax argument from the randomized complexity lower bound.

In §8, the manuscript constructs different distributions, \\(\nu_0\\) and \\(\nu_1\\), on the entire Boolean input cube, using the rounded Gaussian chain. These are employed to establish the underlying Forrelation lower bound.

These distributions play different roles.

First: the analytic distributions \\(\nu_0,\nu_1\\)

The Gaussian-chain construction establishes that shallow decision trees cannot distinguish the distributions sufficiently well, despite their different Forrelation statistics.

§§8.8–8.14, particularly (F16), (F33), (F39) and (F42).

Then: randomized hardness of \\(P\_{k,m}\\)

The analytic comparison proves a lower bound on \\(R(P\_{k,m})\\), taking care of the fact that the Gaussian distributions can contain unpromised inputs.

Finally: the promised hard distribution \\(\mu\\)

Finite minimax produces a distribution supported on \\(\operatorname{dom} P\_{k,m}\\). Independent samples from this law supply the addresses in the planted-winner reduction of §6.

This dependency is present and mathematically explained in the text.&#x20;

reasoning_record(4).pdf

reasoning_record(4).pdf



But because §6 appears before the complete Forrelation proof in §8, a reader first encounters \\(\mu\\), follows the classical planting argument, and only much later encounters the distributions that establish the necessary hardness.

The result is an unnecessarily demanding reading experience.

A specialist may ask: are the Gaussian samples used directly in the planted construction? Are they supported on the promise? Why does the direct-product lemma apply when the analytic distributions include unpromised inputs?

The paper answers these questions, but not together.

I would add a short paragraph in §3.2 explicitly distinguishing the analytic distributions from the eventual promise-supported hard distribution.

This would remove an important potential misunderstanding without lengthening any proof.

It would also make clear that the finite minimax step is a substantive logical bridge, not merely a technical detail.

## 2. The growing-\\(k\\) result is less novel in one sense, but stronger in another

On a deeper reading, §7.3 needs a more careful statement of what it adds.

The earlier fixed-\\(k\\) theorem already gives, for every fixed integer \\(k\\),

\\[ R(F\_{k,m})\gtrsim m^{2-1/k}/(\log m)^2, \qquad Q(F\_{k,m})\lesssim\sqrt m\\,(\log m)^6. \\]

By choosing a sequence of increasing values of \\(k\\) and, for each one, choosing \\(m\\) sufficiently large, a standard diagonal argument would already yield some sequence of functions whose exponent ratio approaches four.

That conclusion alone does not require the uniform bounds of §8.14.

The actual extra value of §7.3 is more specific:

It gives a defined schedule

\\[ k(t)=\left\lfloor\sqrt{t/20}\right\rfloor \\]

and an explicit rate

\\[ R(F_t)\geq Q(F_t)^{4-\varepsilon(\ell)}, \qquad \ell=2t, \\]

where

\\[ \varepsilon(\ell) =8\sqrt{\frac{10}{\ell}} +\frac{56\log_2\ell+508}{\ell}. \\]

That is much more informative than a nonconstructive diagonal sequence.&#x20;

reasoning_record(4).pdf



The manuscript should say this explicitly.

Otherwise an expert may reasonably think that the growing-\\(k\\) section is proving something essentially automatic from the headline theorem.

The novelty of the deduction within this reconstruction is its explicit uniformity and quantitative rate, not merely the existence of a sequence approaching exponent four.

### I also checked how informative that explicit exponent actually is

Using the formula printed in §7.3, I obtained:

| Parameter    | Calculated \\(\varepsilon(2t)\\) | Guaranteed exponent \\(4-\varepsilon\\) |
| ------------ | -------------------------------- | --------------------------------------- |
| \\(t=80\\)   | 7.738                            | -3.738                                  |
| \\(t=184\\)  | 3.996                            | 0.004                                   |
| \\(t=1184\\) | 0.9995                           | 3.0005                                  |
| \\(t=3261\\) | 0.4999                           | 3.5001                                  |

These are evaluations of the paper's explicit bound, not measurements of the actual query complexities.

The important observation is that the growing-\\(k\\) power inequality is essentially vacuous at its advertised starting value \\(t=80\\). The paper acknowledges that possibility, but the numbers make the limitation concrete.

To obtain even an exponent greater than three from this particular bound, one reaches approximately \\(t=1184\\), with

\\[ m=4^{1184}. \\]

That is astronomically large.

There is nothing invalid about an asymptotic complexity result with loose constants. The paper deliberately sacrifices sharp constants for a self-contained argument.

But I would present §7.3 as an explicit asymptotic schedule, not as a particularly effective finite-dimensional estimate.

The fixed-\\(k\\) result already refutes the cubic conjecture. The growing-\\(k\\) calculation serves a different purpose.

## 3. The three different query budgets in the classical proof should be exposed together

Section 6 is careful locally, but its notation is harder to follow than necessary.

The lower bound uses several budget concepts:

| Quantity                      | What it controls                                                                        |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| \\(L\\)                       | The query allowance associated with the hardness of one Forrelation instance            |
| \\(G=\lfloor mL/100\rfloor\\) | The overall query cap of the deterministic tree used in the planted-input contradiction |
| \\(N_i\\)                     | The number of queries made to all address strings of column \\(i\\) on the dummy run    |
| Simulator's charged counter   | Queries to the target column's address strings, truncated before exceeding \\(L\\)      |

The distinction between \\(L\\) as a per-instance hardness parameter and \\(N_i\leq L\\) as a cap on all address-string queries in a light column is especially important.

The latter is stronger and implies that each individual instance respects the former.

That is why the direct-product theorem applies.

Section 6.5 explains this accurately.&#x20;

reasoning_record(4).pdf



But the reader has to assemble the budget hierarchy across §§6.1, 6.3 and 6.5.

I would put precisely this sort of table immediately after the generic lower-bound statement in §6.

It would explain the proof's resource accounting before the reader gets into the conditional probabilities.

This is a good example of how the manuscript can become more accessible without removing any mathematics.

## 4. I independently checked another finite mathematical claim

I enumerated all 256 eight-bit inputs for the \\(k=2,m=4\\) Forrelation example using the signed Walsh matrix and the integer numerator \\(N=z_0^TWz_1\\).

My independently computed census was:

| Numerator \\(N\\) | Number of inputs |
| ----------------- | ---------------- |
| -8                | 8                |
| -4                | 96               |
| 0                 | 48               |
| 4                 | 96               |
| 8                 | 8                |

This agrees exactly with the paper's §8.4 calculation.

Consequently the claimed promise counts also agree:

Output 1

# 104

Output 0

# 48

Undefined

# 104

This is a useful piece of independent positive evidence for the small-instance normalization and sign convention.&#x20;

reasoning_record(4).pdf



I also rechecked the numerical margin in the uniform Forrelation proof. The paper's lower acceptance-gap estimate is \\(119a_k/144\\), while its upper bound from the derivative calculation is \\(7a_k/12\\). Their difference is \\(35a_k/144>0\\).

Those particular numerical deductions are consistent.

They do not certify the full Gaussian-chain proof, whose essential difficulty lies in establishing the estimates being combined.

## 5. The original paper has a visual aid that this 141-page reconstruction lacks

I checked the original OpenAI preprint as an external source.

Its construction section includes a figure showing the winning column and the outward pointers.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



The reasoning record, despite being far longer and more pedagogical in its explanations, has no comparable figure. It relies on mathematical tables and textual descriptions.

This is a genuine missed opportunity.

The outward-pointer direction is arguably the single most important piece of geometry in the total-function construction. It simultaneously explains uniqueness, why a true winner survives comparison, and why invalid opponent addresses are harmless.

An expert can reconstruct the picture, but the reader should not have to.

The same applies to the Gaussian chain in §8.

I would regard two carefully designed figures as a higher-value improvement than another several pages of prose.

The first should show a complete selected-cell certificate, the outward pointers and the off-promise rival situation. The second should depict the progression of Gaussian variables, Walsh edges and derivatives in (F22).

Both would materially improve how quickly an expert understands the proof.

## 6. The hardest part still lacks an optimal referee-facing summary

Section 8 deserves a sharper entry point.

The manuscript gives a detailed derivation, but the real question for a referee is whether four critical assertions all hold for the same Gaussian construction and the same normalization.

| Checkpoint  | What must be verified                                                                                |
| ----------- | ---------------------------------------------------------------------------------------------------- |
| (F16)       | The zero-interpolation endpoint really gives the uniform distribution                                |
| (F22)       | The derivative traverses all \\(k\\) blocks with the claimed factors and no missing terms            |
| (F25)       | The biased decision-tree derivative bound is valid uniformly under adaptive queries                  |
| (F39)–(F43) | The moment bounds produce sufficient separation despite unpromised inputs, with the stated constants |

This is the mathematical heart of the independent supplier proof.

The text currently does a lot to establish each of these statements. For example, §8.10 correctly distinguishes stopping a process before an uncontrolled increment from conditioning on a favorable future event. That is a meaningful piece of mathematical care.&#x20;

reasoning_record(4).pdf



But there is no single front-facing statement saying these four steps are the main independent verification targets.

A concise proof-obligation map at the start of §8.5 would be more useful to a specialist referee than several of the existing historical literature comparisons.

It would allow someone to assess the analytic proof systematically instead of reading every detail with equal attention.

## 7. The greatest remaining credibility issue is the release's verification boundary

Appendix G is careful, but it is still very difficult to obtain one complete, unambiguous answer to this question:

What exactly has been formally verified for the source version accompanying this particular PDF?

The appendix describes multiple source snapshots, successful native builds, statement comparisons, additional theorem wrappers and separately recorded model-fidelity judgments.

It also correctly identifies things that have not been formalized in exactly the same form as the ordinary argument.

For example, §G.4 states that the four principal targets were checked by the configured Comparator on the 3 November sources. But it distinguishes the existential family result from the stronger named-circuit result with explicit constants.

Section G.7 identifies the full physical successful-state bridge as narrower in formal coverage than its ordinary mathematical treatment.

These qualifications increase credibility.&#x20;

reasoning_record(4).pdf



The problem is the presentation of the evidence.

A reader should be able to see one release-level statement containing the paper version, associated Lean source commit or fingerprint, exact compared theorem names, toolchain, results, and any unformalized refinements.

The historical audit can then explain how that state was reached.

Without that front-facing release record, the appendix is exhaustively detailed but surprisingly hard to use.

I would consider this the highest-priority engineering and documentation issue, separate from the mathematics.

## 8. A subtler issue: what kind of scholarly work is this?

On this fourth pass, I think the phrase complete reasoning record is doing the document a disservice.

The document is not simply recording a chronological series of research decisions.

It is an edited, retrospective, mathematically organized reconstruction. It includes complete ordinary proofs, formal statements, semantic tests and historical verification evidence.

Those are very different things from an unedited reasoning trace.

The paper would be more accurately described as a proof reconstruction and formal-verification audit.

That wording also makes clearer why an already published 19-page theorem has been expanded into 141 pages.

The central claim of this document is not that the original mathematical result needed 141 pages to prove. It is that the reconstruction makes the logic, technical interfaces, constants and checking evidence explicit.

That is a defensible scholarly purpose. I would foreground it rather than leave readers to infer it.

## What I would actually do before sending this to a specialist

I would make one further targeted editorial revision, not another general rewrite.

The priority is to improve the researcher's ability to evaluate the work:

1. Add a short explanation of the two distributions \\(\nu_0,\nu_1\\) versus \\(\mu\\), and the finite minimax bridge between them.
2. Reframe §7.3 as an explicit quantitative growing-parameter construction, distinguishing it from the simpler diagonal consequence of the fixed-\\(k\\) theorem.
3. Put a query-budget glossary at the beginning of §6 and a four-checkpoint analytic dependency map at the beginning of §8.
4. Add the outward-pointer and Gaussian-chain figures.
5. Supply a one-page release-level formal-verification status for this exact paper/source version.

## My verdict after four readings

I am more convinced of the quality of the underlying mathematical exposition than I was initially.

The small Forrelation example withstands independent enumeration. The exponent comparisons are internally consistent in the portions checked. The tournament and planted-input arguments explicitly handle several failure modes that a superficial reconstruction would probably miss.

I have not discovered a demonstrated fatal mathematical error in those checked portions.

But I am also more convinced that the document's main weakness is a failure of emphasis.

It gives meticulous explanations of many relatively straightforward technical points while requiring the reader to assemble some of the most important global relationships—particularly the two distributions, the exact significance of §7.3 and the formalization boundaries—from widely separated sections.

As a technical proof record, I would now put it around 8.5/10 for writing and organization. As a standalone paper for a query-complexity specialist, I would put it around 7/10. Those numbers do not represent mathematical-certification confidence.

The difference comes down to how efficiently the manuscript exposes its intellectual structure.

The core mathematical writing is no longer the obvious problem. It is now the hierarchy of ideas, the presentation of the distinctive technical work, and the ease with which an independent expert can check the claims that matter most.

That is where I would concentrate the next revision.