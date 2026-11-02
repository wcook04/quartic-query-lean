# Reading paths and checkable intermediate results

This route is for understanding the supplied October 2026 manuscript and grounding its explanation. It separates an imported theorem, an established technique, a historical analogy, and an argument proved in the manuscript. The same labels should remain visible in a later explanation or formalization.

**Locator convention.** References [1]–[27] are the manuscript's references, resolved in `citation_audit.json`. Pages are those of the inspected version, not automatically the final journal pagination. The supplied main paper has printed and PDF pages 1–19. Paths `paper/`, `literature/`, and `corpus/` identify the original packet. Additional sources have direct links here and fuller metadata in `downloads.json`. `statement_sources.json` connects every one of the 118 ledger IDs to these routes.

## 0. A compact first pass

| Order | Read | Finish with this understanding |
|---|---|---|
| 1 | Main §1.2, pp.2–3, then §2.2, pp.5–6 | What a winner is; why the function is total and has at most one winner. |
| 2 | Main Lemma 2.1, p.4; Bansal–Sinha [6], pp.2–4 | The exact promised primitive and the one external hardness theorem. |
| 3 | Main Proposition 3.2, pp.8–9; its application §3.3, pp.9–11 | Why arbitrary behavior between nonwinners is allowed. |
| 4 | BHMT [12], pp.5–7; BBHT [11], p.3; main Lemma 3.1, pp.7–8 | Why amplification samples the same weighted distribution and has a fixed cap. |
| 5 | Drucker [13], pp.6–7 and 11–13; main §4, pp.11–14 | How adaptivity is handled, and why the capped simulator avoids conditioning bias. |
| 6 | Main §5, p.14; ABKRT [3], p.2 and pp.6–8 | What “nearly quartic” implies, and which half of the final theorem was already known. |

This first pass need not reproduce the full Bansal–Sinha interpolation proof. Mark that theorem as imported, check its assumptions and parameter translation, and return to its proof using the deeper route below.

## 1. Introduction, history and the query model — main pp.1–3

### 1.1 Establish the measures before the historical claims

The main result compares bounded-error randomized queries (R) with bounded-error quantum queries (Q). Deterministic queries (D), certificate complexity (C), exact polynomial degree, and exact quantum queries are different measures. Keep a separate line for each in working notes.

For prerequisites, use [Buhrman–de Wolf, *Complexity Measures and Decision Tree Complexity*](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), §§2–5. Its definitions and proofs remain useful, but its historical open-problem tables are not a current status source. For circuits and oracle notation, [de Wolf's lecture notes](https://homepages.cwi.nl/~rdewolf/qcnotes.pdf), inspected v5, Chapter 2 pp.13–20, Chapter 7 §§7.2–7.3 pp.53–58, and Chapter 11 pp.89–97, provide a more gradual route. The unversioned URL returned conflicting cached front matter; pin the actual edition before using these pages in a permanent bibliography.

Read the manuscript's §1.3 literally: base-two logs are fixed where needed; all algorithms count worst-case bit queries, including all random choices and measurement outcomes; correctness for a partial function is demanded only on its promise, while the routines used later still have a fixed cap outside it. Ordinary computations between queries are free in this model. These conventions are part of the theorem.

### 1.2 A precise historical reading sequence

| Claim in the introduction | Source and exact reading location | Caution |
|---|---|---|
| Quadratic quantum search | Grover [16], §§3–5, pp.3–7; BBHT [11], §§3–4, pp.2–4 | Original Grover assumes a unique solution; BBHT supplies the needed extensions. |
| Matching search lower bound | BBBV [10], §3.1, Theorem 3.3 and Corollary 3.4, pp.7–8 | Read as the hybrid method yielding the search lower bound, not a separately named OR theorem. |
| General sixth-power upper bound | Beals et al. [8], Lemma 4.2 p.5, Theorem 4.13 p.7, Theorem 5.4 p.8 | These locators are for supplied arXiv v3 (1998), not journal typesetting. |
| Near-quartic (D) versus (Q) | Pointer functions [4], §3 pp.10–15; Corollary 7 p.15 | This is deterministic complexity, not the new randomized separation. |
| First power-(5/2) randomized separation | [Ben-David's 2015 note](https://arxiv.org/pdf/1506.08106v1), abstract/§1 p.1 and §3 pp.2–5; then cheat sheets [2], Theorem 1 p.2 and pp.9–12 | Add the earlier announcement for historical accuracy. The served v1 file has a later internal date. |
| Power (8/3-o(1)) | Tal [26], introduction application, printed pp.2–3 / PDF pp.4–5; Corollary 3.2 printed p.10 / PDF p.12; Theorem 5.9 printed p.16 / PDF p.18 | Random-orthogonal rorrelation, not the exact Hadamard gadget of the new paper. |
| Power (3-o(1)) | Bansal–Sinha [6], Corollary 1.5 p.4; SSW [23], Theorem 1.5 p.4 and §1.8 p.10 | The independent approaches have distinct primitives; preserve both credits. |
| Quartic universal upper bound and cubic conjecture | ABKRT [3], Theorem 2 p.2, Conjecture 2 p.20; [earlier ABKT](https://arxiv.org/pdf/2004.13231), Theorem 1 p.2 and Conjecture 4 p.9 | First four-author preprint in 2020; expanded five-author paper is the cited account. |
| Recent comparison-based certificate results | Ben-David–Kothari [9], Theorem 1 p.1, Lemmas 2–5 pp.2–5; Ambainis–Iraids–Kokainis [5], Theorems 2.1–2.2 p.4 | These compare (C) with (R,Q); they are not earlier nearly quartic (R)-(Q) results. |

For the older foundations, Nisan–Szegedy [21], §3 pp.307–310, Definition 3.6 and Lemma 3.8, gives the exact degree/block-sensitivity relationships. The original Nisan [20] text remains unread; audit [20] distinguishes indirect locators from primary verification.

**Checkable output:** a chronology with separate columns for the measures compared, whether the function is total or partial, and the inspected edition. Do not combine an (R)-(Q) exponent with a (C)-(Q) or (D)-(Q) theorem.

## 2.1 The partial function and exact circuit — main pp.3–5

### A. Match the imported theorem exactly

Read Aaronson–Ambainis [1], §1.1.3 p.4 and §3.1–§3.2 pp.12–14 for the origin and circuit. Then place main equations (3)–(4) beside Bansal–Sinha [6], v3, equations (1.1)–(1.3), pp.2–3, and Theorem 1.3 / Corollary 1.4, p.4.

| Main manuscript | Source convention | Required check |
|---|---|---|
| (m) | (N) | Length of each sign vector; total input is (km). |
| Normalized (H), unit vector (u) | Normalized Hadamard (H_N) | Expanding the two copies of (u) gives the source's factor (1/N). |
| (\delta=2^{-5k}) | Same | Literal threshold match. |
| (\Phi\ge\delta) versus ( |\Phi|\le\delta/2) | Same promise | Large negative amplitudes are not 1-inputs. |
| (m) a power of four | (N) a power of two | A permissible subsequence. |
| Error (1/3) | Error (1/2-\eta/2) | Set the source's advantage (\eta=1/3). |

The randomized bound is

\[
\Omega\!\left(k^{-29}
\left(\frac{m}{\log(km)}\right)^{1-1/k}\right).
\]

For fixed (k), divide this by (m^{1-1/k}/(\log_2m)^2). The remaining factor tends to infinity as a positive constant times ( (\log m)^{1+1/k}). This justifies (R(P)>L), including the floor, for sufficiently large (m). The threshold need not be uniform in (k).

**Checkable output:** a precise import statement with domain, normalization, error, query model, and quantifiers. Keep the source's advantage parameter distinct from the failure probability called (\eta) in the new quantum lemma.

### B. Separate the proposal circuit from the promise verifier

The manuscript's easy quantum circuit uses (k) phase queries and accepts with probability (\Phi^2). The promise separates probabilities at least (\delta^2) from at most (\delta^2/4). It need not recognize whether the promise holds. AA Proposition 6 uses a different interference circuit, obtaining ( (1+\Phi)/2) with (\lceil k/2\rceil) queries. Either is a constant number for fixed (k); do not identify the two acceptance laws. [1], pp.13–14; main p.4.

For an explicit concentration citation, use [Hoeffding 1963](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf), §2 Theorem 1 Eq.(2.3), printed p.15 / PDF p.4, or Theorem 2 Eq.(2.6), printed p.16 / PDF p.5. Choosing threshold (5\delta^2/8) leaves a gap (3\delta^2/8) from either promised mean. Additive Hoeffding gives failure at most (\exp(-9s\delta^4/32)) after (s) repetitions. This suffices for (O_k(\log(1/\eta))) queries. It is a convenient derivation, not an optimal dependence on (k). Coherence follows separately by retaining all outcome registers and reversibly computing the threshold.

For the exact classical verifier, write (W=\sqrt mH). All entries are integers, so the amplitude equals an integer numerator divided by (m(\sqrt m)^{k-1}). Powers of four make that denominator integral. Write out the two exact integer comparisons rather than substituting floating-point arithmetic. [Main Lemma 2.1(iii), p.4.]

The Walsh butterfly needs (T(m)=2T(m/2)+m=m\log_2m) additions/subtractions per transform. Intermediates have (O_k(\log m)) bits. [Wegener, *The Complexity of Boolean Functions*](https://eccc.weizmann.ac.il/resources/pdf/cobf.pdf), Chapter 3 §3.1 Theorem 1.1, printed p.40 / PDF p.51, and subtraction discussion p.50 / PDF p.61, supports linear Boolean size for these arithmetic operations. Its cyclic-DFT theorem is not literally the Walsh theorem; the short recurrence above supplies that step. The resulting Boolean size is (O_k(m\log^2m)).

**Checkable output:** three distinct contracts: hard promised function; fixed-cap coherent answer proposal; exact total circuit computing domain membership and the correct promised answer. The third contract makes totalization possible.

### C. A deeper route into Bansal–Sinha

After the preceding import is secure, read [6] §1.2 pp.5–11, then §3 pp.15–18. Focus on Figure 1 and Theorem 3.1, p.16; Theorem 3.2, p.17; Theorems 3.3–3.4 and Corollary 3.5, pp.17–18. Read §5.4 p.38 next, to see the assembly. Then return to the interpolation identities in §4 pp.18–22 and the longer §5 proofs. This avoids getting lost in machinery before knowing what each estimate must deliver.

Useful background is [O'Donnell's 2021 edition](https://arxiv.org/pdf/2105.10386v1), Chapter 1 §§1.2–1.4, pp.22–25 for characters, orthogonality and normalization. [Sinha's 2023 Simons lecture](https://simons.berkeley.edu/talks/makrand-sinha-simons-institute-2023-06-29) and the QIP 2021 slides in `downloads.json` are author-led learning resources; this audit inspected their records, not a full recording or transcript. Pei Wu's thesis, Chapter 6, is a longer companion to the SSW route; the chapter is a reading recommendation, not fully audited material.

The later [Girish–Servedio ITCS 2026 paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/LIPIcs.ITCS.2026.72/LIPIcs.ITCS.2026.72.pdf), Theorem 4 p.72:4 and §1.3 p.72:7, gives a linear-algebra viewpoint on an **extremal sign promise**. It does not replace the arbitrary-(k) theorem needed here. In particular, a (\Phi^2) test would erase the sign in that alternative problem.

## 2.2 The total function and local tests — main pp.5–6

Read the ancestors in this order:

1. GPW [15], §2.1 pp.4–5: all-one accepting column and an outward chain witnessing rival zeros. The revised ECCC version retains this construction.
2. Pointer functions [4], §3 pp.10–11: the corresponding tree/backlink construction.
3. Cheat sheets [2], §§3.1–3.2 pp.9–12, then Definitions 14–15 pp.20–21 and Lemma 17 p.22: an answer address identifies certificates that verify both promise membership and output.
4. Main §2.2: a separate array for each column, directly indexed per-rival pointers, and exact circuit transcripts.

Prove totality and uniqueness directly from the definitions. Every proposed input has a well-defined Boolean outcome, because being in the promise is checked as a predicate. If column (i) wins, its certificate names a zero in every (X_j), (j\ne i); hence no such (j) can also have an all-one string.

For a candidate address, gate tests must load actual input bits at input wires and alleged values only for non-input gates. Topological induction shows that all consistent gate values equal the true circuit computation. The domain and output tests then certify a correct address. Incorrect addresses cannot pass merely because the quantum proposal happened to output them.

**Correct the ledger here.** A pointer test reads (\ell) bits and then one adaptively selected target bit. It has depth (\ell+1), not necessarily support size (\ell+1). With two pointer bits and four target bits, all six variables can affect the test although three queries suffice. The manuscript says query cost correctly; LR1 gives the precise ledger replacement.

**Checkable output:** a single indexed family of (K=m+(m-1)+r(S+2)) exact tests; a proof that all pass iff the candidate wins at that address; adaptive query depth for each test; and coherent evaluation under the ordinary bit oracle. Do not assume a unit-cost oracle reading an entire certificate cell.

## 3.1 Bounded amplification — main pp.7–8

Read BHMT [12], §2 Lemma 1 and Eq.(8), pp.5–7, then BBHT [11], §4 Lemma 2, p.3. The state remains in the span of the same normalized good and bad vectors. A successful measurement therefore produces the same full good vector, up to a global phase, for every iteration count that succeeds. The vector includes the retained workspace. This supplies a stronger contract than “a good answer is likely.”

The expected-runtime unknown-success statements in those sources are not enough by themselves for the manuscript. Read its complete Lemma 3.1 proof and check the fixed choices of (M), trial count, and the explicit zero-iteration half of each trial. That half handles success probability close to one. The randomized-iteration identity handles the remaining promised range. At success probability zero, there is no success; the query cap still holds.

Conditioning on the first successful trial can change the distribution of trial lengths. It cannot change the conditional successful state, because each successful branch produces the same normalized vector. Randomization over such branches gives the same density matrix.

**Checkable output:** a reusable lemma asserting (i) all-input, all-branch query cap; (ii) low failure when (p\ge\gamma); and (iii) equality of the full normalized successful state. Verify (A^{-1}) is legitimate by retaining all workspace rather than discarding measurement information. Pointer-functions [4], p.9, already discusses a preserving amplification variant, so the basic preservation principle should not be called new.

## 3.2 Probabilistic tournament — main pp.8–9

### First distinguish the comparison models

| Source | What comparisons mean | Why it is not the new theorem verbatim |
|---|---|---|
| Dürr–Høyer [14], Theorem 1 and rank lemmas, pp.1–2 | Order comparisons on values | Uses ordering/rank structure. |
| Mande–Paraashar–Saurabh [18], Definition 1.1 p.2; Observation 4.1 and Lemma 4.2 pp.10–13; Theorem 4.4 p.13, proof pp.13–15 | Fixed tournament edge bits | Cycles are allowed, but edges are definite. |
| Ben-David–Kothari [9], Lemma 5 pp.3–5 | Fixed candidate-comparison tournament | Relevant witness ancestry, different model of bad comparisons. |
| Ambainis–Iraids–Kokainis [5], §4 pp.6–8; §6 Algorithm 4 pp.12–13 and Lemma 6.6 p.15 | Fixed graph defined by first-one positions | Read supplied v2; latest reported v3 was not inspected. |
| [Høyer–Mosca–de Wolf](https://arxiv.org/pdf/quant-ph/0304052v2), §§1,3 pp.1–4 | Each subroutine approximates a specified bit with uniform constant bias | Arbitrary nonwinner probabilities need not satisfy that bias promise. |

For the new proposition, (a_{ij}+a_{ji}=1) for distinct candidates and (a_{ii}=0). Only the true winner has near-certain success against every rival. Do not threshold every other (a_{ij}) at (1/2) and assume the induced graph can be queried cheaply: a probability can be arbitrarily close to the threshold.

### Then derive the new proof in five steps

1. For weights (w_i), pivot distribution (w_p/W), and update (w_i\leftarrow w_i a_{ip}), pair the ((i,p)) and ((p,i)) terms. The exact drift is

   \[
   \mathbb E[W'\mid w]=\frac{W^2-\sum_iw_i^2}{2W}\le W/2.
   \]

2. Until the winner is selected, its weight remains at least ( (1-\epsilon)^T>1/2). Markov's inequality and the drift imply the ideal pivot list misses it with probability at most (2m/2^T). Handle (W=0) separately as the manuscript does.
3. Prepare a uniform candidate and compare it with every prior pivot in fresh workspaces. Conditional on candidate (i), the joint success probability is the product defining (w_i). Orthogonal index registers give total success (W/m) and conditional sampling law (w_i/W).
4. Apply Lemma 3.1. Before the winner is found, (W/m\ge1/(2m)). Conditional on each full previous history, a sampling failure is at most (\epsilon); coupling to the ideal process adds at most (T\epsilon).
5. Count preparation and inverse calls. At stage (t), comparison cost is (O(c(t+1))). Summing under the capped amplification yields (O(c\sqrt m T^2\log T)) on every input, including ones with no winner.

**Checkable output:** the exact drift identity, the conditional index law, and a history-conditional coupling lemma. Success probability alone is not a sufficient output contract. No unproved transitivity or uniform nonwinner bias should enter the proof.

## 3.3 Comparisons and final verification — main pp.9–11

Read the candidate-comparison predecessors [5,9] first, then perform the new off-promise check without assuming anything about a rival's decoded address.

If (i^*) is a winner, its all-one (X_{i^*}) has no zero for any rival's pointer to find. If its own address is decoded correctly, its true cell supplies a zero in every rival. These two facts make it win with probability at least (1-\epsilon), even if the rival's primitive instances are outside their promise. Sorting each unordered pair before invoking the same circuit ensures exact complementarity of the two comparison probabilities. Retained address registers keep the classical outcome branches orthogonal.

For final verification, every nonwinner has a failed local test at **every** address. A quantum search for a failed exact test therefore rejects a nonwinner except with the configured search error. On a winner's correct address there is no failed test, so verified search cannot invent one. Sum the decoding, tournament and verification errors with the manuscript's (T,\epsilon), keeping the one-sided statements explicit. [Main §3.3; [2] Lemma 17 for the general certificate principle; [11,12] for search.]

**Checkable output:** the pairwise winner guarantee, exact complementarity, verifier soundness for all addresses, and the complete worst-case cost/error calculation. This is where the combination of direct outward pointers and certified hard addresses earns its role.

## 4.1 Hard distributions and capped products — main pp.11–12

### First obtain the hard distribution

The manuscript uses the strong finite minimax direction, not merely “a hard distribution implies a randomized lower bound.” Let the rows of a finite game be all depth-at-most-(L) deterministic trees, columns the promise-domain inputs, and payoff correctness. If (L<R(P)), no randomized mixture attains success (2/3) on every input. Compactness gives an attained value below (2/3), and minimax yields a promise-supported distribution (\mu) under which every such tree succeeds with probability at most (2/3).

Use [Eric Blais's CS860 minimax chapter](https://cs.uwaterloo.ca/~eblais/cs860/w25/minimax) for a short modern formulation and its distinction from the original average-cost zero-error version. Yao [27] remains the historical citation, with original full-text access unresolved. For the concrete (P_{k,m}), Lemma 2.1(i) establishes (L<R(P)). The independent-output conclusion is a later use of Lemma 4.1; LR2 recommends separating these stages.

### Then prove the product statement with its actual cap

Read Drucker [13], §1.3 pp.6–7, Lemmas 3.1–3.2 pp.11–12 and the final paragraph of §3 p.13. Read Shaltiel [22], §5 Definition 4 and Theorem 5, printed p.11 / PDF p.12, and Lemma 7, printed p.12 / PDF p.13, for the antecedent. The latter supplied version uses uniform inputs and parity advantage. Drucker is the closer arbitrary-distribution value-function source.

Fix random coins and independent auxiliary information. A transcript of an adaptive algorithm specifies separate bit constraints for each input. Every input tuple satisfying those constraints follows the same schedule; the transcript event is rectangular. Conditional inputs therefore remain independent under their respective constraints.

For each instance, let its value be the best conditional success probability with its remaining per-instance budget. A query updates only one factor, whose conditional expectation cannot increase beyond the optimum before that query. The product of values is a supermartingale. At a leaf, conditional independence bounds the success of a proposed whole answer vector by that product. Initially it is at most (\beta^r). Averaging over the fixed auxiliary information and coins completes the proof.

**Checkable output:** a theorem permitting arbitrary adaptive interleaving, independent side information, and a cap of (L) on **each input on every branch**. A total budget (rL) is a different hypothesis and does not automatically give this ideal product bound. Do not cite Drucker's headline theorem as if it said otherwise.

## 4.2 Coupling and the extra factor of (m) — main pp.12–14

Read the manuscript in the order: dummy and planted inputs; Eq.(18); hidden-zero estimate Eq.(19); heavy-column estimate Eq.(20); simulator and Eq.(21); combination Eqs.(22)–(23).

| Mechanism | Quantity to establish | Reason it matters |
|---|---|---|
| Every dummy column contains a hidden zero; all cells blank | (F(Y^{(0)})=0) | Gives a genuine total-function zero-input. |
| Uniform independent (I); erase its zero and fill its true cell | (F(Y^{(1)})=1) | Gives a winner with correctly certified promised address. |
| Identical oracle answers until a changed location is queried | Output-probability difference bounded by two hitting events | Reduces distinguishing to erased-zero or planted-cell access. |
| Early/late zero discoveries | (\mathbb E Z\le4G/m), then hit probability (\le4G/m^2) | Uses independent uniform (I); no hindsight choice of the planted column. |
| Heavy columns receive more than (L) address queries | (\Pr[I\text{ heavy}]\le G/(mL)) | Charges concentrated classical work. |
| Fixed-column, fixed-time capped simulator | Joint nonheavy-and-hit probability (\le(2/3)^r) | Applies the product theorem without conditioning away hardness. |

The simulator receives the other dummy data for free, which is independent of the target (r) inputs. It aborts before query (L+1) to those inputs in total, a cap stronger than the per-input hypothesis. If the original run is nonheavy and proposes the true cell at time (t), the simulator reaches that point and outputs the right address. This is event containment. It is not a claim that conditioning on the original run's nonheaviness preserves (\mu^{\otimes r}).

After union bounding over times and averaging over (I), the distinguishing advantage is at most

\[
\frac{4G}{m^2}+\frac{G}{mL}+G(2/3)^r.
\]

Insert (G=\lfloor mL/100\rfloor), (r=\lceil20\log_2m\rceil), and sufficiently large (m). The bound is strictly below (1/3), contradicting success at least (2/3) on both input distributions. Fixing then averaging coins covers randomized algorithms.

**Checkable output:** a generic lower-bound lemma parameterized by a partial function and hard distribution. The only Forrelation-specific input at this point is hardness plus the existence of the exact circuit used to populate a valid cell. Credit the fair-product principle to Shaltiel/Drucker; credit this particular multi-column planting, simulator, and charge to the supplied preprint, subject to the stated priority boundary.

## 5. Optimal exponent — main p.14

Keep the quantifier order explicit. For a proposed (\alpha<4), choose fixed (k\ge2) with (2-1/k>\alpha/2). The upper bound on (Q) gives a lower bound on the ratio

\[
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
\ \ge\ 
c_{k,\alpha}\frac{m^{2-1/k-\alpha/2}}
{(\log m)^{2+\alpha b_k}}\ \longrightarrow\ \infty.
\]

This rules out each smaller universal power. Appendix A supplies the admissible power four. The additive one handles constant functions in the definition. No extra asymptotic theorem beyond power-versus-log domination is needed.

**Checkable output:** quantified statements matching Theorem 1.1, including the sufficiently-large power-of-four subsequence. Do not replace this with an exact (R=\Theta(Q^4)) family or silently let (k) grow with (m).

## Appendix A. The established quartic ceiling — main pp.14–17

Start with the final chain, then read its ingredients in increasing technical order:

| Step | Direct source | Reading purpose |
|---|---|---|
| (D\le\operatorname{bs}\deg) | Midrijanis [19], Lemma 3 and proof of Theorem 4, pp.3–4 | Each maxonomial-query round contains a sensitive block at the actual input; rounds use disjoint variables. The intermediate inequality is the one needed. |
| (\operatorname{bs}=O(Q^2)) and (\lambda=O(Q)) | Main Lemmas A.2–A.3 pp.15–16; ABKRT [3], Lemma 9 p.8 | Use a sensitive-block star, then the sensitivity adjacency matrix whose coordinate restrictions are matchings. |
| (\deg\le\lambda^2) | ABKRT [3], Theorem 1 pp.6–7; Huang [17], Lemmas 2.1–2.3 pp.3–5 and spectral-radius remark p.5 | Highest-degree restriction, parity agreement on more than half a cube, and the signed-cube spectrum. |
| Assemble (R\le D=O(Q^4)) | ABKRT [3], Theorem 2 p.2; main Theorem A.1 | The old upper bound is independent of the new lower-bound construction. |

For a friendly adversary proof, read [Høyer–Špalek, *Lower Bounds on Quantum Query Complexity*](https://www.ucw.cz/~robert/papers/lowerb-survey.pdf), §§3–4 pp.5–8, particularly Theorem 2 p.7. For provenance, BSS [7] §9.2 Theorem 4 gives the exact nonnegative spectral bound; Špalek–Szegedy [24], Theorem 3.1 / Eq.(3.1), p.6, gives equivalent formulations. The latter title concerns the adversary methods studied there, not an assertion that later negative-weight and nonnegative methods have equal strength.

For formalization, the nonnegative top eigenvector can be obtained through a short Rayleigh-quotient argument: replacing a real vector by its coordinatewise absolute value cannot decrease the quadratic form of a symmetric nonnegative matrix. This is enough for the nonnegative spectral setup; the full machinery of irreducible Perron–Frobenius theory need not become an additional project. This is a proof-organization suggestion, not a newly claimed theorem.

In the Huang step, distinguish the signed cube adjacency matrix, whose square is (dI), from the normalized Walsh–Hadamard transform used in §2.1. They are different matrices serving different purposes. The proof needs the spectral norm of the sensitivity graph, not merely its maximum degree. In the Midrijanis step, Theorem 5 concerns exact quantum complexity and is not a bounded-error cubic simulation.

**Checkable output:** prove the three links separately, with the correct measures, and then compose them. A formal proof of this upper-bound branch alone would not establish the new separation.

## Corrections, explanatory resources and the next review boundary

If discussing the claimed optimal classical simulation of few-query quantum algorithms, add [Bravyi–Gosset–Grier–Schaeffer v2](https://arxiv.org/pdf/2102.06963v2), pp.3–4, Theorems 2–4, and the [ECCC correction record](https://eccc.weizmann.ac.il/report/2021/115/). The original AA variable-splitting proof had an error. That correction concerns an adjacent upper bound, not the imported Bansal–Sinha lower bound. The revision-2 correction PDF was not retrieved; its landing/revision record was inspected. Tal's ECCC revision history likewise needs its date: the supplied arXiv version postdates the recorded repair.

For comparison while drafting an explanation, consult the [Latent Seminar article](https://lowrank.github.io/latent-seminar/OpenAI-Math/284-quartic-randomized-quantum-queries) and the [six-lesson course](https://kokunoyumeto.github.io/open-math-courses-public/courses/randomized-versus-quantum-query-complexity/). Their stated review limits matter. Existing exposition means the project's value should come from clarity and checked source alignment, not a claim to be the first explanation.

The next mathematical review should concentrate on the exact contracts above and the original Forrelation proof if an independent end-to-end verification is intended. A current source-code check would additionally need a pinned commit, a reproducible build, inspection of assumptions and axioms, and a match between the formal theorem and the manuscript. None of those executable checks was performed in this literature round. All unavailable originals, unchecked revisions, and unconsumed recordings are listed in `review_receipt.json` and `downloads.json`.
