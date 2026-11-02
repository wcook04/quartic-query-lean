# Sources and citation guide

Prepared 2 November 2026. Citations below identify the editions and passages used in this advisory. They support the specified mathematical or software claim. Formal acceptance and semantic correspondence require their own evidence.

## Primary mathematical sources

| Key | Citation and inspected edition | Precise locator and use |
|---|---|---|
| **OAI26** | OpenAI. *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*. 5 October 2026. [Official paper](https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf). The packet identifies source revision `4eaee875`. | Theorem 1.1 and equations (1)–(2): headline and quantifiers. §2.2: total construction. Lemma 2.2: local verification. Lemma 3.1: capped amplification. Proposition 3.2: weighted tournament. Proposition 3.3: quantum bound. Lemma 4.1 and Proposition 4.2: classical bound. §5: exponent conclusion. Appendix A: existing universal upper bound. |
| **AA** | Scott Aaronson and Andris Ambainis. *Forrelation: A Problem that Optimally Separates Quantum from Classical Computing*. [Author-hosted primary PDF](https://www.scottaaronson.com/papers/for.pdf), inspected by the lead agent. | §1.1.1, pp. 2–3: Forrelation definition. §1.1.3, p. 4: the k-fold version. Used for the film's mathematical background and the wording “studied by Aaronson and Ambainis.” This paper credits Aaronson's 2009 introduction. |
| **BS20** | Nikhil Bansal and Makrand Sinha. *k-Forrelation Optimally Separates Quantum and Classical Query Complexity*. [arXiv:2008.07003v3](https://arxiv.org/html/2008.07003v3), 17 November 2020; STOC 2021. | Equations (1.1)–(1.3): statistic and promise. Theorem 1.3, Corollary 1.4 and §5.4: randomized lower bound and bounded-error quantum algorithm. Corollary 1.5: earlier nearly cubic total separation. Theorem 3.2 and §5.3: biased Fourier comparison. |
| **H19** | Hao Huang. *Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture*. [arXiv:1907.00847v2](https://arxiv.org/html/1907.00847v2), inspected by the lead agent. | Theorem 1.1: hypercube theorem, named on the film's source card. Theorem 1.4: sensitivity-degree consequence. Used to credit the ingredient in ABKRT20; the universal quartic query bound itself is cited to ABKRT20 Theorem 2. |
| **ABKRT20** | Scott Aaronson, Shalev Ben-David, Robin Kothari, Shravas Rao and Avishay Tal. *Degree vs. Approximate Degree and Quantum Implications of Huang’s Sensitivity Theorem*. [arXiv:2010.12629v1](https://arxiv.org/html/2010.12629v1), 23 October 2020. | Theorem 2, printed p. 2: universal `D(f)=O(Q(f)^4)`. Theorem 3 and the following short proof explain its ingredients. §7, Conjecture 2: the proposed cubic randomized upper bound. |
| **ABK16** | Scott Aaronson, Shalev Ben-David and Robin Kothari. *Separations in query complexity using cheat sheets*. STOC 2016, pp. 863–876. [DOI:10.1145/2897518.2897644](https://doi.org/10.1145/2897518.2897644). Inspected [arXiv:1511.01937v2](https://arxiv.org/html/1511.01937v2), 9 July 2019. | Theorem 1: earlier exponent-2.5 total separation. §§3.1–3.2: certificate addresses and verification. Lemma 6: blank-array lower-bound argument. §6.1, Definition 15: general cheat-sheet construction. |
| **BHMT02** | Gilles Brassard, Peter Høyer, Michele Mosca and Alain Tapp. *Quantum Amplitude Amplification and Estimation*. Contemporary Mathematics 305 (2002), pp. 53–74. Inspected [arXiv:quant-ph/0005055v1](https://arxiv.org/html/quant-ph/0005055v1). | §2, Lemma 1 and equation (8): invariant good/bad subspace and preservation of the normalized good component. Theorem 3: unknown-success search with expected query cost. OAI26 Lemma 3.1 supplies the capped version used in the tournament. |
| **D12** | Andrew Drucker. *Improved Direct Product Theorems for Randomized Query Complexity*. Computational Complexity 21(2) (2012), pp. 197–244. Inspected [arXiv:1005.0644v2](https://arxiv.org/html/1005.0644v2), 9 May 2014. | §1.3: fair algorithms with a separate cap per instance. Lemmas 3.1–3.2 and the product argument in §3: continuation values and conditional product structure under adaptive interleaving. |
| **GTW21** | Uma Girish, Avishay Tal and Kewen Wu. *Fourier Growth of Parity Decision Trees*. CCC 2021, LIPIcs 200, Article 39, pp. 39:1–39:36. [Publisher](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2021.39); [full PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol200-ccc2021/LIPIcs.CCC.2021.39/LIPIcs.CCC.2021.39.pdf). | §1.3, “Standard Decision Trees,” pp. 39:6–39:8; **Lemma 9** and footnote 2 on p. 39:8. Prior art for the Azuma, reverse-induction and union-bound mechanism; stopping preserves the martingale when direct conditioning would not. |

The original paper was read in full from `packet:paper/extracted.md`. The official GitHub file page was retrieved, but remote PDF bytes were not independently matched to the attachment. Its attached PDF SHA-256 is:

```text
a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e
```

The other mathematical entries were retrieved as primary full text and read in the relevant sections. This bibliography does not claim that every proof in every cited paper was independently audited.

## Official Comparator documentation

| Key | Official reference | Use and version boundary |
|---|---|---|
| **LEAN-LAKE** | Lean Language Reference, [Lake, §25.1.5.8, Comparator](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/). Consulted by the lead agent on 2 November 2026. | Interpretation of Comparator configuration and comparison. `definition_names` identifies definition holes; an empty list does **not** disable comparison of definitions. |
| **LEAN-435** | Lean Language Reference, [release notes for Lean 4.35.0](https://lean-lang.org/doc/reference/latest/releases/v4.35.0/). Consulted by the lead agent on 2 November 2026. | Comparator release context. The supplied project uses **`leanprover/lean4:v4.36.0-rc2`**. Release notes and current documentation do not prove which binary executed a historical run. |

The `latest` documentation URL can change. The supplied toolchain, bundle configuration, source pin and original receipt are the appropriate execution-specific records. This advisory inspected configurations and recorded observations; it did not execute Comparator.

## How to cite a passage in this return

A `packet:` path is relative to the extracted input archive. It identifies supplied evidence and does not imply that the source file is reproduced in this return ZIP.

| Claim in the reader or film | Citation that belongs beside it |
|---|---|
| A mathematical statement from the preprint | **OAI26**, precise section/equation/theorem, and its exact `statement_id` from `packet:repository/corpus/statements.json`. Example: the drift identity is OAI26 §3.2, equation (13), `eq-13`. |
| An earlier mathematical ingredient | Its author citation and exact locator above. Cite BS20 for the imported lower-bound theorem; identify separately the weaker fixed-`k` form supplied by the new Lean route. |
| A definition used by a Lean theorem | Full declaration name and module at the packet pin, with its type and definition context. A similarly named theorem is insufficient. |
| A paper-to-Lean correspondence | The selected tie and its `formal_statement`, `route` and `reach` fields, together with the exact compared text. An authored tie is a correspondence assertion. |
| An observed build or Comparator outcome | Bundle, source commit, configuration and receipt identity when available. If only the trace or summarized graph is supplied, say that it **records** the outcome. |
| A negative control | Intended rejection, actual checker outcome and test classification. A passing rejection test does not mean the changed theorem was accepted. |
| A new displayed deduction or finite example | Its `NEW_STATEMENTS.json` identifier, assumptions and calculation/evidence. A literature citation alone does not confer a checked Lean supplier. |
| A historical development claim | Dated attached trace passage or review file, with its original scope. Keep later observations separate from earlier failures or incomplete states. |

The source of a theorem, the source of its proof route and the source of a checking observation can be different. Give the locator for the claim actually being made.

## Edition and attribution distinctions

- **ABKRT20 has five authors.** Its Theorem 2 and Conjecture 2 must not be cited with the numbering or four-author attribution of arXiv:2004.13231.
- **AA is used for background, not an introduction claim.** The film says “studied by Aaronson and Ambainis”; AA itself credits the earlier introduction to Aaronson. **H19** supplies the hypercube theorem used in the later query-complexity argument; it is not the citation for ABKRT20's quartic conclusion.
- **BS20 means version 3.** Preserve its `delta=2^(-5k)` promise and fixed-`k` scope when using the weaker consequence in the packet. A derivative of order `k` at a biased point can involve higher uniform Fourier levels.
- **GTW21’s published locator is Lemma 9.** The attached prior-art report uses the arXiv-style locator Lemma 1.9. These are edition-specific references to the relevant argument.
- **BHMT02 Theorem 3 has expected cost.** The fixed worst-case cap needed here is stated and proved in OAI26 Lemma 3.1.
- **D12’s per-instance cap matters.** An aggregate cap of rL cannot replace the separate cap of L on each of r instances.
- The mathematical construction is credited to **OpenAI**. The separate Lean development and this explanation are AI-assisted work directed by Will Cook. The attached record reports AI reviews and no human review.

The new total-function construction excludes every universal exponent below four; the quartic upper bound is earlier work. For each fixed `k`, the separation approaches exponent `4−2/k`. The alternative Forrelation proof route does not establish an improved uniform dependence on `k`. The prior-art search found antecedents and route differences; “not found” does not establish priority.

## Source pins and unavailable originals

| Record | Pin |
|---|---|
| Final supplied reader/film packet | `c7e0c9161f0ad898889bd9166e7b354acd42188d` |
| Source commit named by the recorded paranoid unconditional receipt | `d42fb67a7e060fb5386867dadf20a5903df39141` |
| Paper revision named by the packet | `openai/math 4eaee875` |

These identify different objects. The original Comparator receipts, logs and compiled exports are absent from the packet. The trace records a private repository; no public final Lean-repository pin was independently established. Use the supplied local source paths and exact commit identities without manufacturing public permalinks.

All hashed manifest members matched their supplied size and SHA-256. This establishes consistency with the attachment, not authenticated execution provenance. [READ_SCOPE.md](READ_SCOPE.md) records the team's reading and verification boundaries.
