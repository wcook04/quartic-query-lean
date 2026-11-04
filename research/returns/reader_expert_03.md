# Third reading: mathematical and editorial audit

This reading has already changed one important conclusion from my previous review.

## 1. Correction: my previous Appendix E criticism was wrong

I re-examined the actual typeset formula on page 19 at higher magnification.

It says

\\[ \boxed{k=\left\lfloor\sqrt{\frac{t}{20}}\right\rfloor} \qquad(t\ge80), \\]

not \\(k=\lfloor\sqrt t/20\rfloor\\), as I interpreted it previously.

Your formula is consistent: at \\(t=80\\), it gives \\(k=2\\), exactly the required minimum. The square-root bar extends over the entire fraction.

My previous assertion that this was a definite parameter error was incorrect. Do not change that formula or its threshold on the basis of my earlier review.

That correction illustrates why checking the rendered mathematical notation matters: extracted PDF text can obscure the extent of a radical or fraction.

## 2. The fixed-\\(k\\) proof is more robust than some of my earlier comments suggested

I tested the main argument again, specifically looking for a counterexample to one of its probabilistic reductions.

Three dependencies are central.

First, the quantum tournament does not need a transitive comparison relation. Equation (8) uses only

\\[ a\_{ij}+a\_{ji}=1 \\]

for distinct candidates, allowing the expected surviving weight to contract by at least a factor of two. No hidden total-order hypothesis appears to be used.

Second, the quantum sampler implements the distribution required by the analysis. Equation (9) uses fresh comparison workspaces, so the success probability associated with candidate \\(i\\) is

\\[ \frac1m\prod_b a\_{i\rho_b}. \\]

That gives the conditional weight distribution exactly. Appendix C then establishes that amplification preserves that conditional measured-label distribution.

Crucially, the proof also explains why the amplifier's success threshold remains valid before the genuine winner is selected: the winner retains weight at least \\((1-\varepsilon)^T>1/2\\).

Third, the classical planted-cell argument avoids conditioning on an adaptive event. Section 4.4 constructs a truncated predictor whose query cap holds unconditionally, then bounds the joint event of being light and naming the correct cell. This is the right order of operations.

I rechecked the final discrepancy calculation:

\\[ \left|\Pr[\mathcal T(Y^{(1)})=1]-\Pr[\mathcal T(Y^{(0)})=1]\right| \le \frac{4G}{m^2}+\frac{G}{mL}+G(2/3)^r \le\frac6{100}. \\]

The three terms are supported by distinct mechanisms, and the inequalities follow from the declared parameter bounds.&#x20;

expert_companion(3).pdf



I found no definite gap in these central reductions on this pass.

This does not mean the whole mathematical construction is independently certified. In particular, I have not reproved the external Forrelation hardness theorem or the separate uniform analytic estimate. But the internal reasoning is substantially more disciplined than a conventional high-level reconstruction.

## 3. A real missing step: the stronger constant in Appendix E

This is the most useful additional technical editorial finding.

In Section 4.5 you obtain the explicit coefficient \\(1/400\\) using elementary floor estimates.

In Appendix E, the new allowance is

\\[ X=\frac{2m^{1-1/k}}{18225k^2\ln(4km)}, \qquad L=\lfloor X\rfloor. \\]

The paper then asserts

\\[ R(F\_{k,m})> \frac{m^{2-1/k}}{1822500k^2\ln(4km)}. \\]

At first sight, reusing the two coarse floor estimates from Section 4.5 gives only half this lower bound.

However, the displayed Appendix E constant is defensible. For \\(X\ge2\\),

\\[ \lfloor X\rfloor\ge \frac X2+\frac12. \\]

And when \\(m\ge200\\),

\\[ \begin{aligned} \left\lfloor\frac{m\lfloor X\rfloor}{100}\right\rfloor &\ge \frac{m\lfloor X\rfloor}{100}-1\\\ &\ge \frac{mX}{200}+\frac m{200}-1\\\ &\ge \frac{mX}{200}. \end{aligned} \\]

Substituting the stated \\(X\\) recovers exactly the denominator \\(1{,}822{,}500\\).

So this is not another correction to the theorem. It is a missing explanation of why the improved coefficient follows.

The calculation is short enough to include directly on page 18. I would add it because numerical constants are part of what the paper advertises, and a conscientious referee may otherwise wonder where the extra factor of two came from.&#x20;

expert_companion(3).pdf



## 4. I checked the linked Lean statements, and this exposes a more specific presentation problem

I inspected the pinned `QuarticCorpus/Unconditional/Challenge.lean` and `Solution.lean` files linked from Section 6.

The challenge file defines the mathematical statements and deliberately leaves `sorry` placeholders. The corresponding solution file contains no `sorry` placeholders; its four checked endpoints are short proof wrappers that invoke previously established declarations, including `alphaTot_eq_four_unconditional` and `theorem_1_1_unconditional`.

That architecture is entirely reasonable for a specification-and-comparison workflow.

But consider how a first-time reader encounters it:

1. They click the formal statement and see `sorry`.
2. They click the solution and find a roughly 40-line file consisting mainly of `exact` applications of imported theorems.
3. They must now determine where the substantial proofs actually reside.

The PDF does say that the statements are specifications compared with separately compiled solutions. That is accurate. But the navigation still makes the hard mathematical work difficult to inspect.

I would add a proof-dependency map rather than simply expanding the prose.

A compact diagram or table could trace the actual proof modules through the three main chains:

Quantum upper bound

Reversible comparison → exact weighted sampler → bounded amplification → certificate verification → query bound

Randomized lower bound

Hard input distribution → capped direct product → planted-cell predictor → indistinguishability → query bound

Headline theorem

Both quantitative bounds → fixed-parameter exponent argument → αₜₒₜ = 4

Each arrow should link to the relevant substantial Lean declaration, not merely the short final wrapper.

I would also link directly to the dated build, comparison, and axiom-audit evidence. The historical unelaborated comment in the named-family source is explicitly discussed in the record, but a direct evidence link would make that reconciliation easier.

This would be a meaningful improvement for formal methods reviewers, without substantially increasing the paper's length.

Evidence limitation: I inspected the pinned source files; I did not rerun Lean or independently reproduce the reported axiom audit.

## 5. The largest remaining writing problem is the allocation of explanatory effort

The manuscript spends considerable effort making subtle mathematical details auditable.

For example, the reader gets:

- A four-candidate numerical example of weighted sampling.
- Eight counterexamples to invalid simplifications.
- An induction proof of the capped direct-product bound.
- A comparison of predecessor pointer access models.
- A separate treatment of growing-\\(k\\) uniformity.

These are valuable.

Yet it devotes relatively little space to explaining the structure of the Lean proof itself, despite highlighting formalization in the subtitle.

There is also a second imbalance. The introductory contribution paragraph emphasizes the specific constants \\(6\\) and \\(1/400\\), even though those are deliberately conservative reconstruction choices. The more interesting achievement is making two technically delicate reductions understandable, checkable, and formally connected to the theorem.

I would adjust the emphasis, not invent any new claims.

One simple improvement would be to include a parameter guide near the start of Section 2:

| Parameter          | Meaning                                                   |
| ------------------ | --------------------------------------------------------- |
| \\(m\\)            | Number of columns and rows per column                     |
| \\(k\\)            | Number of Forrelation sign vectors                        |
| \\(\ell=\log_2m\\) | Pointer length                                            |
| \\(r=20\ell\\)     | Number of hard address instances                          |
| \\(S\\)            | Size of the exact certificate circuit                     |
| \\(K\\)            | Number of local certificate tests                         |
| \\(T\\)            | Maximum number of tournament pivots                       |
| \\(L,G\\)          | Supplier query allowance and total classical query budget |

That may seem elementary, but the reader has to track many interacting parameters across eleven pages. A compact reference would reduce unnecessary working-memory load.

## 6. The physical meaning of the construction deserves one more sentence

The paper does define its computational model properly. On page 2, it explicitly states that arbitrary input-independent unitary computation and workspace are free, and no gate-time or space complexity is asserted.

Likewise, page 4 establishes that the input encoding has size

\\[ N\_{k,m}=O_k(m^{22}\ell^3). \\]

These are significant qualifications.

They mean the result is a separation in oracle query complexity, not a claim that the constructed Boolean function gives a practical quantum speedup under realistic computational resource bounds.

A complexity theorist knows this. But because the paper is also intended to communicate a high-profile result outside the original authors' immediate circle, it would help to connect those two facts explicitly.

I would add a single explanatory sentence after the encoding-size calculation: the function has an enormous, although polynomial-size, representation, and the claimed separation concerns bit queries rather than feasible time or memory.

The existing mathematics supports that distinction. Making it explicit would prevent an avoidable misunderstanding.

## 7. My strongest remaining criticism of the prose

The paper is technically competent, but sometimes writes in a style better suited to a verified proof ledger than to a research article.

For example, the introduction's contribution paragraph moves rapidly from crediting OpenAI, to explicit numerical constants, to Lean comparison evidence, to the physical correspondence limitation.

Every fact is relevant, but they belong to different explanatory levels.

The ideal ordering would be:

1. What this reconstruction makes mathematically clearer.
2. What is established or derived quantitatively.
3. What the Lean development checks.
4. What formal correspondence remains outside its scope.

The current material already contains all four. It is their arrangement that could be improved.

The same issue appears in Section 6, where phrases such as configured comparison bundle, source editions, retained-state comparison, and finite-seed translations arrive in rapid succession.

These are legitimate technical terms. They are not AI jargon. But readers unfamiliar with this particular verification workflow need one sentence explaining why each distinction matters.

The writing is not too verbose. In a few places, it is too compressed at the exact points where understanding the paper's contribution requires additional context.

## Final conclusion of this pass

My view has become more specific after three readings.

I would not recommend a broad rewrite of the mathematical sections. The quantum sampling proof, the capped classical prediction argument, and the final fixed-\\(k\\) exponent deduction are coherent, carefully organized, and unusually attentive to subtle assumptions.

There are two changes I would now prioritize over everything else.

First, expose the Lean proof dependency structure in a way that makes the substantial formal arguments directly inspectable, rather than expecting a reader to reconstruct the chain from specifications and imported theorem names.

Second, make the few non-obvious quantitative transitions self-contained—particularly the exact circuit-size derivation and Appendix E's stronger floor estimate.

I would also correct the minor Appendix C citation formatting, but that is not a substantive obstacle.

The mathematical exposition is now stronger than the evidence presentation. The next revision should aim to make those equally strong.

As a specialist reconstruction, this is a credible and nearly circulation-ready paper. As a standalone formal-verification research contribution, the source-to-statement correspondence still needs to be easier to audit. That is where further work is most likely to change an expert reader's assessment, rather than another round of polishing individual sentences.