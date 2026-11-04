# Fourth review — closer to a referee's assessment

I reread the 19-page Expert Companion, concentrating this time on the exact hypotheses of the auxiliary lemmas, the parameter choices, the classical minimax argument, and how much of the claimed proof a specialist can check without opening the reasoning record.

My main conclusion is that the central proof is holding up better under repeated scrutiny than the surrounding presentation of its dependencies. I found no new definite error in the principal separation argument. But there are several more specific ways the paper could be made stronger.

## 1. The auxiliary lemmas actually fit their applications

This is important because an apparently rigorous paper can fail when a theorem is applied under slightly different conditions from those it assumes.

### Bounded amplification: Lemma 3

On pages 7 and 17, Lemma 3 guarantees an exact conditional measured-label distribution, not an exact retained quantum output state.

That distinction is precisely what the tournament needs.

The proof decomposes the initial state into successful and unsuccessful components, observes that Grover iterations change their amplitudes without changing the normalized successful component, and uses a bounded randomized schedule.

I checked the boundary cases again:

- At \\(p=0\\), no trial can report success.
- For \\(p\ge 1/2\\), the direct-measurement branch provides a constant success probability.
- For \\(\gamma\le p\le1/2\\), the randomized Grover branch gives a constant success probability.
- For \\(0\<p<\gamma\\), success is not guaranteed, but the worst-case query cap remains valid.

That is a suitable contract for both tournament pivot sampling and certificate verification.

The main result uses the measured-label law and therefore does not require the stronger retained-state claim.

I would not demand a stronger theorem for the sake of the paper's headline result. The manuscript has chosen an appropriately limited theorem and explained its boundary.&#x20;

expert_companion(3).pdf



### Direct product: Lemma 5

I also traced the inductive proof in Appendix D through its application in Section 4.4.

The induction maintains separate query allowances for each block, even though the algorithm may interleave queries adaptively. Its key property is that an adaptive transcript restricts each input factor separately, preserving the product structure of the unnormalized measure.

The simulator in Section 4.4 uses an even stronger cap: at most \\(L\\) queries to all target blocks combined.

Therefore the simulator satisfies Lemma 5's separate per-block caps.

There is no hidden need to condition on the simulator's terminal lightness. Indeed, the manuscript explicitly avoids that invalid move.

This is a genuine strength.&#x20;

expert_companion(3).pdf



## 2. A distinction the paper should state: the hard distribution is not part of the construction

This is a new editorial point that I think matters.

Section 4.2 chooses a distribution \\(\mu\\) using finite minimax. The proof then samples address instances independently from \\(\mu\\).

A reader moving quickly could wonder whether the construction of the total function is itself dependent on a nonconstructively obtained distribution.

It is not.

The function \\(F\_{k,m}\\) was defined earlier using the explicit Forrelation problem and a fixed exact circuit. The minimax distribution appears only in the proof of its randomized lower bound.

That distinction is clear once one follows the full argument, but it is not stated where the distribution first appears.

I would insert one sentence:

> The distribution \\(\mu\\) is a witness used only in the lower-bound proof; it is not part of the definition or evaluation of \\(F\_{k,m}\\).

This is the kind of tiny addition that can prevent a substantial misunderstanding.

It also strengthens the presentation of the construction's explicitness, without claiming anything about efficient computational implementation.&#x20;

expert_companion(3).pdf



## 3. The finite error accounting is correct but unnecessarily opaque

I checked the tournament and verification constants again.

With

\\[ T=\lceil\log_2(1000m)\rceil,\qquad \varepsilon=\frac1{1000T}, \\]

the ideal tournament misses the winner with probability at most

\\[ 2m2^{-T}\le 0.002. \\]

Sampling failures contribute at most

\\[ T\varepsilon=0.001. \\]

Fresh decoding during winner verification contributes at most another \\(\varepsilon\le0.001\\).

Thus the upper bound on one-input rejection is at most \\(0.004\\), considerably below the required \\(1/3\\). On zero-inputs, the false-acceptance bound is at most \\(0.001\\).

All this is consistent with Section 3.3.

But the constants are scattered across Sections 3.1–3.3, and the reader must assemble the overall error budget.

I would put the three terms together in a single displayed inequality immediately before the final correctness statement:

\\[ \Pr[\text{false rejection}] \le 2m2^{-T}+T\varepsilon+\varepsilon <\frac13. \\]

Then state the zero-input bound separately.

More importantly, explain once that these parameters were chosen for generous slack, not optimality.

A mathematically sophisticated reader is not impressed by seemingly arbitrary constants such as 1000 unless their purpose is obvious. Here they have a simple purpose: making the bounded-error argument easy to close uniformly.

The paper can communicate that more efficiently.&#x20;

expert_companion(3).pdf



## 4. The biggest self-containedness problem is not the Forrelation lower bound

On this pass I distinguished three kinds of dependencies.

The first is standard imported mathematics. Citing Bansal–Sinha for the Forrelation lower bound and the universal quartic upper bound is entirely reasonable. A reconstruction of OpenAI's separation need not reprove all prior complexity theory.

The second is proof machinery developed in this paper. The bounded amplifier and separate-cap product lemma are supplied in Appendices C–D. That is excellent: the core mechanisms are inspectable.

The third is quantitative machinery developed in the companion reasoning record but necessary to substantiate the paper's specific numerical claims.

This third category is where the presentation still needs improvement.

For example, the exact circuit-size estimate

\\[ S\le200(k+1)^2m\ell^2 \\]

is quoted with a sketch, not derived. Yet it contributes to the local-test bound \\(K\\), which determines the quantum verification cost.

Similarly, Appendix E states a uniform analytic estimate from the reasoning record and derives a growing-\\(k\\) consequence. That appendix is not a self-contained proof of the analytic estimate.

My recommendation is not to reproduce the entire reasoning record. Instead, give a precise dependency classification next to each major quantitative result:

| Result                             | What this PDF establishes                                                               |
| ---------------------------------- | --------------------------------------------------------------------------------------- |
| Forrelation hardness               | Cites an existing theorem; derives the required eventual fixed-\\(k\\) allowance        |
| Exact circuit-size bound           | States the bound and sketches the construction; full gate count is external to this PDF |
| Weighted tournament                | Gives the argument and proves the bounded amplifier                                     |
| Classical reduction                | Gives the reduction and proves the separate-cap product lemma                           |
| Explicit fixed-\\(k\\) separation  | Assembles the stated bounds                                                             |
| Uniform growing-\\(k\\) separation | Deduction conditional on the separately established estimate (16)                       |

This would make the manuscript more credible, not less. Referees generally appreciate knowing exactly which facts they are being asked to verify.

## 5. An important framing issue remains in the abstract

The abstract says that the paper proves the comparison sampler and capped prediction reduction.

That is mathematically reasonable language: the manuscript contains their proofs.

But because those reductions originate in OpenAI's construction, the wording could be read as a claim to new theorems rather than a new reconstruction of existing arguments.

The introduction subsequently supplies the correct attribution.

I would make the abstract self-sufficient by changing the emphasis from we prove to we give complete reconstructed proofs of.

The same applies to the discussion of explicit constants. The chosen exponent six and coefficient \\(1/400\\) are useful for auditing the reconstruction. They are not the central scientific novelty of the work.

The strongest accomplishment is the combination of a detailed mathematical reconstruction and formal proof artifacts with explicit scope boundaries.

That should be the abstract's hierarchy.

## 6. The parameter choices need one explanatory map

This is a recurring source of reading friction across Sections 2–5.

There are several fixed constants, each serving a different proof obligation:

| Choice                            | Why it is made                                                |
| --------------------------------- | ------------------------------------------------------------- |
| \\(r=20\ell\\)                    | Suppresses the chance of predicting the complete hard address |
| \\(G=\lfloor mL/100\rfloor\\)     | Keeps the planted/dummy distinguishing advantage small        |
| \\(T=\lceil\log_2(1000m)\rceil\\) | Makes the tournament's ideal miss probability small           |
| \\(\varepsilon=1/(1000T)\\)       | Controls accumulated sampler and verification errors          |
| \\(S\le200(k+1)^2m\ell^2\\)       | Gives the required quantitative circuit-size allowance        |

The manuscript explains each choice locally. But seeing them together would immediately reveal that the proof is driven by a few independent constraints, not by a mysterious collection of numerical constants.

I would put this near the start of the construction or at the beginning of Section 3. The resulting improvement in navigability is disproportionate to the space required.

## 7. What I think an especially skeptical expert would still ask

After a close reading, I think the difficult questions are now concentrated in three places.

First: Does the explicit exact-circuit implementation really realize the stated gate bound, including the convention for output gates and transcript bits? The manuscript supplies a plausible sketch and a record reference, but not the derivation.

Second: Does the full Lean dependency chain faithfully instantiate the measured-label algorithm described on pages 5–8? The paper distinguishes formal comparison from physical correspondence, but the reader needs to inspect more than the final theorem wrappers.

Third: Is Appendix E's uniform analytic estimate independently persuasive? Its growing-parameter deduction appears consistent, but the estimate doing the work is located in the other document.

Those are questions about inspectable proof evidence, not broad objections to the argument.

I would not represent them as demonstrated mathematical gaps. They are the places where an expert's independent checking would naturally concentrate.

## Revised overall assessment

The main proofs have now survived several close readings without an identified logical contradiction. The earlier supposed error in Appendix E's square-root parameter was my misreading of the typesetting, and I have not found a replacement mathematical counterexample.

That warrants some confidence in the quality of the reconstruction's internal exposition, but it is not the same as certifying all the mathematics or the formalization.

I would now characterize the writing as follows:

- Mathematical argument: strong, with particularly careful handling of the quantum sampling law and classical adaptive prediction.
- Proof organization: strong, although the quantitative dependencies could be mapped more explicitly.
- Technical originality and attribution: generally responsible, but the abstract could more clearly distinguish reconstructed proofs from new results.
- Formal verification presentation: accurate in its caveats, but too dependent on readers navigating separate proof artifacts.
- Self-containedness: good for the main reductions; weaker for the exact circuit estimate and uniform analytic refinement.

My rating remains approximately 8–8.5/10 as an expert-facing reconstruction.

I would avoid another general rewrite. At this point, the strongest next revision would be a short, systematic pass that makes all quantitative assumptions, theorem dependencies, and formal evidence directly traceable.

The paper no longer principally needs to sound like serious mathematics. It needs to make the serious mathematics it already contains as easy as possible to independently audit.