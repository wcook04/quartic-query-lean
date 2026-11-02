# Prior-art check: the Forrelation lower-bound route in `forrelation_lower_bound_blueprint.md`

Date of search: 2 Nov 2026. Scope: items (a)-(e) of the route in
`docs/forrelation_lower_bound_blueprint.md` (route D, identity (★), the Azuma growth bound, the
bound `(16 k d log 4n)^(k/2) + 1`). Read-only research; nothing was committed.

"Not found" below is a search result. It is not a claim of novelty.

## 1. Summary

| Item | Verdict | Closest prior work |
|---|---|---|
| (a) one block scaled by `s`, multi-affinity, no Gaussian time derivative | Partly known: the interpolation method is standard; the one-block-scaled path was not found | Bansal–Sinha, arXiv:2008.07003 (v3), Lemma 8 (Gaussian interpolation) and the `k-1`-parameter path of §3 |
| (b) one Stein identity per block, no branching, only level exactly `k` | Not found (the ingredient is known) | Bansal–Sinha Lemma 9 (integration by parts), the branching process of §3 and its levels `k..k(k-1)`; BS v1 for levels `k,2k,...,(k-1)k` |
| (c) elementary truncation `q(x)=sqrt(2+x^2)` in place of Owen's T | Not found; the need for a custom truncation is known | Bansal–Sinha §1.2 (`φ = Φ - 1/2`, Owen's T); Tal, arXiv:1912.12561 (uses `sgn` of Gaussians) |
| (d) level-k L1 growth for decision trees by Azuma along the tree, union bound over index sets | Known in mechanism. Only the biased-measure form is unwritten in what I found | Girish–Tal–Wu, arXiv:2103.11604, §1.3 and Lemma 1.9 (standard-decision-tree case and general case) |
| (e) bound `(16 k d log 4n)^(k/2) + 1` | Same family as known bounds; not stronger in `k`. The numerical form was not found | Sherstov–Storozhenko–Wu (SSW), main Fourier-weight theorem (label thm:MAIN-Fourier-bound; number not checked); Tal Theorem 5.1; Bansal–Sinha Corollary (biased Fourier weight, `4^ℓ w`) |

## 2. Sources actually read (all in full or in the relevant sections)

Local annexes in `/Users/willcook/src/ai_workflow/annexes/` (`extracted.md` in each):

* `quartic-ref-06-k-forrelation-optimally-separates-quantum`: Bansal–Sinha. Read §1.2 overview
  (lines 100-215 of the extract), §2 preliminaries (Gaussian interpolation Lemma 8, integration by
  parts Lemma 9, biased Fourier basis), §3-4 outline, the biased-weight section
  ("Fourier Weight under Biased Measures", Claim 27) and the proof of the main lower bound.
* `quartic-ref-23-an-optimal-separation-of-randomized-and-qu`: Sherstov–Storozhenko–Wu (SSW).
  Read the introduction (results, limitations of Tal, approach, comparison with Bansal–Sinha,
  follow-up work). The proofs of §4 were skimmed, not checked.
* `quartic-ref-26-towards-optimal-separations-between-quantu`: Tal. Read §5.1-5.3 and §7.1
  (level-1 inequality proof) and the Hadamard-matrix remark (Definition 5.5).
* `quartic-lit-girish-forrelation-is-extremally-hard`: skimmed. It concerns exact quantum algorithms
  and non-adaptive lower bounds for extremal Forrelation. It has no Fourier-growth argument. Not
  the Girish–Tal–Wu paper.
* `quartic-ref-01-forrelation-a-problem-that-optimally-separ`: Aaronson–Ambainis. Located its
  Gaussian Azuma lemma (§3.4, Lemma 8) and the Central Martingale Lemma (Lemma 16). Not read in
  full.
* `quartic-lit-bravyi-classical-algorithms-for-forrelation`: grepped only; upper bounds, not
  relevant.
* `research/returns/2_ground_in_literature/` does not exist under `/Users/willcook/src/ai_workflow`
  (`find` for a directory of that name returned nothing). No local return was available.

Fetched from the web (PDF text extracted with `pdftotext` and read):

* Girish, Tal, Wu, "Fourier Growth of Parity Decision Trees", CCC 2021, arXiv:2103.11604.
  Read the abstract, §1.1-1.4 (results, applications, proof overview, related work), Lemmas
  3.3-3.4 (adaptive Azuma), the statements of Theorems 5.5/5.12/6.3, Claim 6.1, and the proof
  outline of Lemma 5.6. Standard-decision-tree case: §1.3, "Standard Decision Trees".
* Tal, EPFL Winter School 2026, "Lectures 3,4" slides (61 pages). Only text-matched. It covers
  2-fold Forrelation and the CHHL random-walk view (slide text around "Viewing z~G as a result of
  a random walk"). No Azuma proof of Fourier growth in it.
* Abstracts only (not read in full): arXiv:2609.07060 ("2-Fold Forrelation is in QAC^0"),
  arXiv:2609.11830 (Mantri, oracle separations in the Fourier hierarchy), arXiv:2602.07503 (extremal
  Forrelation, non-adaptive), arXiv:2610.41694 (cyclic Forrelation), arXiv:2007.03631 (Girish–Raz–Zhan,
  XOR of Forrelations), CHHL, arXiv/ECCC TR18-015. None claims a new proof of the k-fold bound.
  I did not read their bodies, so a technique buried inside one of them is not excluded.

## 3. Item by item

### (a) Gaussian process with one block scaled by `s`; multi-affinity; no time derivative

* Bansal–Sinha interpolate with `G(t) = sqrt(t) G`, `k-1` independent parameters
  `t in (0,1)^(k-1)` (extract line 139 and Lemma 8, extract line 311); the derivative is the
  second-order term `1/2 Σ_ij E[G_i G_j] E[∂_ij f]`. Their proof of Theorem `level` integrates over all
  `k-1` parameters (extract line 602 area, with `θ_J(t,u,v)` bounded by `(4k)^(14|J|)`).
* They remark the same formula follows from Itô calculus (extract line 311, after Lemma 8), and
  they cite the stochastic-calculus route of Raz–Tal and Wu as the other Gaussian approach
  (extract line 137). Talagrand's "smart path" is the general idea: the choice of path is free.
* I found no source that scales a single block and uses affine dependence of the cube extension
  on the scaled coordinates to avoid differentiating `sqrt(s)`. Search receipts: §5, rows S1, S2, S8.
* Verdict: partly known. The interpolation method and the freedom to choose the path are
  standard. The particular path of route D was not found. How different it is from BS Lemma 8 in
  effect depends on identity (★), which I did not re-derive; the blueprint itself notes that
  it has not had an independent reading.

### (b) Stein identity once per block, no branching, level exactly `k`

* The tool is known: BS Lemma 9 is multivariate Gaussian integration by parts, and BS also prove a
  version for the truncated variable (`E[φ(U) f(...)]`, extract line 454). Stein's identity
  is the same fact.
* The structure is not what BS do. BS (final version) report a branching process because of the
  mismatch between the index entering and leaving a block; the result is Fourier weight at all
  levels `k..k(k-1)` (extract line 194 and the display near it for v1: levels `k,2k,...,(k-1)k`
  with `δ = 1/polylog^k N`; v2/v3 with `δ = 2^(-O(k))` levels `k..k(k-1)`, Theorem `level`).
  For `k=2` BS need only level 2 (extract line 145).
* SSW and Tal do not run a walk. They expand in Fourier characters and need all levels `ℓ >= k` of
  the tree, with moment bounds `|D̂(S)| <= (c|S| log N / N)^(|S|(1-1/k)/2)` (Tal Lemma 5.7) and
  `D̂(S) = 0` for `|S| < k`. So "only level exactly `k`" is not a feature of theirs either.
  Tal's route also needs a "good" orthogonal matrix, and Tal states that the Hadamard matrix is
  not good (Definition 5.5 remark), which the blueprint §2B uses against route B.
* I found nothing using one Stein application per block with matched indices to reach level `k`
  only, for the Hadamard (Forrelation) instance with `δ = 2^(-5k)`. Search receipts: S3, S4, S8.
* Verdict: not found. The ingredient is known; the arrangement is the claim. Because a
  single-level result would be a structural simplification of BS Theorem `level`, an independent
  reading of (★) matters more here than a search, and the blueprint says that has not happened.
  The Lean proof is the evidence for correctness; it does not bear on whether it is known.

### (c) Elementary truncation `q(x) = sqrt(2+x^2)` instead of Owen's T

* BS: `φ(s) = Φ(s) - 1/2` (Gaussian cdf shifted), whose identities use Owen's T function
  (extract line 209-210, 284-294). They also say that `(1/2) sign` would be the natural choice but
  is hard to analyse directly (extract line 209). Tal uses `sgn(Z)` of Gaussians directly in the
  distribution `D_{U,k}` (Tal §4, `E[φ_U(sgn Z)] >= (2/π)^(k-1)`, extract lines 625-631). Neither
  is algebraic.
* I found no paper using an algebraic truncation of this kind with a one-line Stein identity
  (`(Ψ·pdf)' = -φ·pdf`). Search receipts: S3, S8.
* Verdict: not found. The weaker claim, that a truncation to `[-1/2,1/2]` with a usable
  integration-by-parts identity is needed, is known and stated in BS.

### (d) Level-`k` L1 growth for decision trees via Azuma along the tree

This is the item the brief asked to settle. The answer: the mechanism is in Girish–Tal–Wu.

What GTW do (arXiv:2103.11604, §1.3, "Standard Decision Trees", and Lemma 1.9):

* For a tree `T`, take a random root-to-leaf path `v_0..v_d` with partial assignments `v^(i)` in
  `{-1,0,1}^n`. With `a_S = sgn T̂(S)`, they write `Σ_|S|=ℓ |T̂(S)| = E[T(v_d) Σ a_S v_S^(d)]`
  (their (2)), so the task is to bound the walk `X^(i) = Σ_|S|=ℓ a_S v_S^(i)`.
* Increments are `x_j · Σ_{S∋j} a_S v^(i-1)_{S\{j}}`: a fair coin times a quantity fixed by the history,
  so the sequence is a martingale. The step sizes are level-`(ℓ-1)` walks of the same kind.
* For `T ⊆ [n]` with `|T| <= ℓ` they define `X_T^(i) = Σ_{S⊇T, |S|=ℓ} a_S v^(i)_{S\T}`, show it is a
  martingale whose increments are `x_j X^(i-1)_{T∪j}`, and prove by reverse induction on `|T|`
  (Lemma 1.9) that with probability `1 - ε(ℓ-t)` all `X_T^(i)` with `|T| >= t` are `<= Õ_ε(d^((ℓ-t)/2))`,
  applying Azuma and a union bound over `T` of size `t` and over `i in {0..d}`
  (`ε / (d · C(n,t))` per event). They handle the failure of the conditioned martingale property by
  truncating at the bad event (their footnote 2). Adaptive Azuma is their Lemma 3.3, a variant
  with random step bounds in Lemma 3.4.
* The final bound for standard trees falls out of the same proof; their theorem for parity trees
  (Theorems 5.5, 5.12) gives `d^(ℓ/2) · O(ℓ log n)^ℓ`, and Corollary 1.3 lifts it to randomized
  trees by convexity.
* GTW say explicitly that the proof "differs from the proofs appearing in [Tal20] and [SSW20]",
  which are tree decompositions, and that for standard trees it is "slightly simpler and more
  intuitive" (abstract and §1.4). They name the bottleneck as "a union bound on events related to
  all sets `T ⊆ [n]` of size at most `ℓ`". That bottleneck is what the blueprint's "union bound
  over one contracted index per level" addresses.

What the blueprint's item (d) adds relative to GTW:

1. The measure. GTW work under the uniform measure on `{±1}^n`, and Bansal–Sinha's Theorem
   `level` needs the bound under every bias `μ in [-1/2,1/2]^(kN)`. BS pass from uniform to biased
   by a random-restriction argument (Claim 27 in the section "Fourier Weight under Biased
   Measures"; Corollary `wt`: `wt^μ_ℓ(f) <= 4^ℓ w` where `w` bounds `wt_ℓ(f_ρ)` for all restrictions
   `ρ`). The blueprint instead runs the martingale directly under the biased measure with centered
   coordinates `ξ_a = (sgn z_a - μ_a)/(1-μ_a^2)` (lemma T1 and two-point Hoeffding T3). I found no
   written biased-measure version of GTW's argument. It looks like a direct adaptation (the
   increments remain mean-zero and bounded by 2 when `|μ| <= 1/2`), but "looks like" is my
   reading, not a source. GTW's noisy-decision-tree Claim 6.1 contains a biased mean-zero
   increment of a related kind (the posterior `v_j` of a noisy query), which shows the
   idea of biased walks along trees appears in that paper, in a different model.
2. The statement. GTW prove their bound for the sum with absolute values fixed by `sgn T̂(S)`.
   The blueprint's quantity is `Σ_J |ext(D_J T)(μ)|` at the bias `μ`, which is the biased
   Fourier weight appearing in BS Theorem `level`. Equivalent in spirit; the translation is not
   in GTW.
3. It is a proof for standard trees only, with an elementary constant; GTW's parity-tree
   machinery (cleanup, k-clean nodes) is not needed.

Other vocabularies searched and what came back:

* Polarizing random walks: CHHL (Chattopadhyay–Hatami–Hosseini–Lovett, CCC 2018 / Theory of
  Computing 15, 2019) introduce the walk framework for PRGs. BS cite the Gaussian-random-walk
  variants [RT19, Wu20]. Tal's 2026 slides use the CHHL walk to explain Forrelation
  hybrids. None of the retrieved text gives an Azuma bound for Fourier growth of trees. This is the
  same random-walk idea but on the input side, not on the tree path.
* Aaronson–Ambainis (arXiv:1411.5729) use Gaussian Azuma on a martingale in an
  adversary-like Gram-Schmidt argument for 2-fold Forrelation. It is a different object (the
  query algorithm's transcript against Gaussian vectors) and is not a Fourier growth bound.
* Tal (1912.12561), Theorem 5.1: level-1 bound by a tail bound on the path sum `s_λ`, then
  induction on the level through decomposition and contraction. The level-1 step is a Chernoff
  bound on the sum along a random path, the base case of the same idea, but his higher levels are
  by tree decomposition. SSW reduce the same problem to a partition of the tree into elementary
  families and obtain the tight `sqrt(C(d,ℓ))`.

Verdict for (d): known (Girish–Tal–Wu, §1.3 / Lemma 1.9 is the same Azuma-along-the-path,
induction-on-`|T|`, union-bound argument). The biased-measure statement proved without a
restriction is the only difference I could identify, and I could not confirm it is absent from
the literature.

### (e) The bound `(16 k d log 4n)^(k/2) + 1` at level `k`

Comparison of the level-`ℓ` L1 bounds for depth-`d` trees on `n` variables as stated in sources:

| Source | Bound | Locator |
|---|---|---|
| Tal 2020 (arXiv:1912.12561) | `O(d)^ℓ · O(log m)^(ℓ-1)` in the extract as OCR'd, i.e. `(c^ℓ) sqrt(d^ℓ (log)^(ℓ-1))` | Theorem 5.1; quoted in SSW intro as `c^ℓ sqrt(d^ℓ (1+log kn)^(ℓ-1))` |
| SSW | `c^ℓ sqrt( C(d,ℓ) (1+log n)^(ℓ-1) )` | SSW introduction, theorem labelled `thm:MAIN-Fourier-bound` (number not checked) |
| GTW | `d^(ℓ/2) · O(ℓ log n)^ℓ` (parity trees; includes standard) | Theorem 1.1 / 5.12 |
| BS, biased | `wt^μ_ℓ <= 4^ℓ w` with `w` the restricted uniform bound | Claim 27 and Corollary `wt` |
| Blueprint | `(16 k d log 4n)^(k/2) + 1` under bias `|μ_a| <= 1/2` | §2 |

Reading: at `ℓ = k` the blueprint's bound is `d^(k/2) (log)^(k/2)` times `(16k)^(k/2)`. It matches
Tal in the exponents of `d` and (up to one factor of `sqrt(log)`) of `log`, is weaker than SSW by
the `sqrt(ℓ!)` that SSW remove, and is comparable to GTW (whose loss is `ℓ^ℓ` in the base). The
`k^(k/2)` is irrelevant for fixed `k`, which is what the blueprint's §1 asks for. The `+1` comes
from the bad event in the Azuma step and is a feature of the argument, not something I
could compare with a source. So (e) is a known kind of bound, obtained by a different route, with a
specific constant not found elsewhere. It is not a new strength.

## 4. Search receipts

Tools: `WebSearch` (standard and extended), `WebFetch`, `pdftotext` on fetched PDFs, `grep` on the
annex `extracted.md` files. Date of searches: 2 Nov 2026. Quoted strings are the queries.

| # | Query or action | Result |
|---|---|---|
| S1 | "Girish Tal Wu Fourier growth of parity decision trees arXiv" | arXiv:2103.11604; read |
| S2 | "simplified proof Forrelation randomized query lower bound k-fold Forrelation without Gaussian interpolation Fourier growth" | only Bansal–Sinha, Aaronson–Ambainis, SSW; no simplified proof |
| S3 | "k-fold Forrelation randomized lower bound new proof Stein's lemma OR integration by parts OR martingale decision tree Fourier level k only, Bansal Sinha simplification" | nothing new; confirmed BS abstract (Gaussian interpolation and integration by parts; levels `k..(k-1)k`) |
| S4 | "Fourier growth decision trees biased product measure level-k martingale Azuma Forrelation lower bound 2024 2025" | GTW, BS, SSW; 2026 items 2609.07060 and Mantri 2609.11830 surfaced (abstracts show they use the bounds; no new proof) |
| S5 | "Chattopadhyay Hatami Hosseini Lovett Pseudorandom generators from polarizing random walks Fourier level-k bounds" | metadata and abstract; no level-`k` growth statement retrieved; CHHL not read in full |
| S6 | "Girish Raz Zhan Quantum versus randomized communication complexity OR Fourier growth of communication protocols Forrelation" | Girish–Raz–Tal (ITCS 2021) and Girish–Raz–Zhan (arXiv:2007.03631); different topic |
| S7 | "arXiv 2025 2026 Forrelation query complexity lower bound decision trees Fourier weight Sherstov Storozhenko Wu follow-up" | 2602.07503 (extremal Forrelation, non-adaptive), 2610.41694 (cyclic Forrelation); neither is a re-proof of the k-fold bound |
| S8 | "Raz Tal Oracle separation of BQP and PH Forrelation Gaussian random walk Fourier tails level-k bound proof technique Wu stochastic calculus" | Raz–Tal ECCC TR18-107, Wu note (Theory of Computing 18, v018a017); full texts not read |
| S9 | "Girish Servedio table Fourier growth decision trees parity decision trees AC0 Fourier growth survey bounds level-k" | GTW again; Tal's EPFL 2026 lecture slides; no comparison table found |
| S10 | local `grep -i azuma|martingale|hoeffding|stein|polarizing|biased` on annexes quartic-ref-06, -23, -26, -01, quartic-lit-girish, quartic-lit-bravyi | Azuma only in Aaronson–Ambainis (ref-01); none in BS, SSW, Tal as a Fourier-growth proof |
| S11 | `WebFetch` arXiv abs 2008.07003 | v1 16 Aug 2020, v2 11 Nov, v3 17 Nov 2020; improvement to `δ = 2^(-O(k))` and the SSW reference were added in v2/v3 |

Not done: Google Scholar and Semantic Scholar forward-citation lists of Bansal–Sinha and GTW
were not retrieved (no such tool route in this session, and the search tool returned no
citation lists). A forward-citation sweep of BS (STOC 2021) and GTW is the obvious next step and
would be the strongest additional check for (b) and (d).

## 5. What can honestly be said

* Do not claim (d) as new. The Azuma-along-the-tree argument with induction over contracted index
  sets and a union bound is the Girish–Tal–Wu proof of Fourier growth (arXiv:2103.11604, §1.3,
  Lemma 1.9), and they say it differs from the decomposition proofs of Tal and SSW. A fair
  statement is: "a version of the Girish–Tal–Wu martingale argument, run directly under the biased
  measure, so that no random-restriction transfer is needed". The explicit constant
  `(16 k d log 4n)^(k/2) + 1` is ours; its form is weaker in `k` than SSW.
* (a), (b), (c) were not found in the sources read. For (a) and (b), say what BS do and what
  differs: BS use `k-1` interpolation parameters, a `sqrt(t)` path, Gaussian integration by
  parts, a branching process and levels `k..k(k-1)`; route D uses one scaled block, one Stein
  identity per block and level `k`. For (c), BS use `Φ - 1/2` with Owen's T; route D uses an
  algebraic function. Present these as differences from the closest work, with
  "no earlier statement found" and the search receipts above, not as priority claims.
* The blueprint's own remark (§2D: "The sources read do not state (★); no wider search was
  made, so no novelty is claimed") remains accurate after this wider search. What changed: the
  wider search found that the Azuma half is previously known, and it still did not find the walk
  half.
* The Lean development itself, a machine-checked proof of the Bansal–Sinha lower bound for
  fixed `k` with `δ = 2^(-5k)`, was not searched for here; the search was about the mathematical
  route. A check of existing formalizations (Lean, Isabelle, Coq) of Forrelation or Fourier growth
  was not performed.
* Before any public claim: have a mathematician read (★) independently (the blueprint
  records that no such reading has happened), and do the forward-citation sweep listed at the end
  of §4.
