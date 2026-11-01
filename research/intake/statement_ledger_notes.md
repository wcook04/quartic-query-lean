# Statement ledger notes: nearly quartic R versus Q separation

Paper: "A Nearly Quartic Separation Between Randomized and Quantum Query Complexity", OpenAI, 5 October 2026. Companion to `statement_ledger.json`.

## Sources and evidence status

- LaTeX was fetched from `openai/math` at pinned commit `4eaee875`. The `build` entry is a real directory holding `main.tex`, `preamble.tex`, `references.bib`, six section files and one figure file. The whole paper was read, including Sections 4 and 5 and Appendix A.
- `source_line` points to `annexes/openai-math-284-quartic-query-separation/extracted.md` in `ai_workflow`. The build script checked a text anchor at each row's line (or within two lines of it), so line numbers are machine-checked.
- The audit below is one agent's line-by-line reading plus small numeric checks. It is not a formal proof, and nobody else has reviewed it.
- Numeric checks run: `Phi=N/M`, the Grover average bound (9), the drift identity (13), the ideal-miss bound by exact tree enumeration (m=5, T=4), the error budget, `(H'_j)^2=jI`, and `deg <= lambda^2` on random 4-variable functions. All passed. These are spot checks, not evidence for the asymptotic statements.
- Bansal-Sinha was read at arXiv:2008.07003. ABKRT Conjecture 2 was read at arXiv:2010.12629.

Row kinds: `definition`, `construction`, `equation`, `lemma`, `proposition`, `theorem`, `corollary`, and `inline_claim`, the last for an unnumbered step inside a proof that a formalisation must state on its own. All 23 numbered equations have a row, with id `eq-N`, including those that act as definitions. Parts of a lemma have ids such as `lem-2.1.i`. Figure 1 and the historical survey in Section 1.1 have no rows, except `cor-cubic-refuted`.

`model_needed` uses `none` for pure real or matrix algebra, and `classical_finite` for finite combinatorics or probability with no query measure.

## Doubts about the paper

**No mathematical error was found.** Every proof step in Sections 2-5 and Appendix A held up on reading. Truth of the main theorem rests on the one unproved external input, D3. The other items are gaps in precision that a formalisation must settle.

- **D1, logarithm base (needs pinning).** Section 1.3 lets the base vary "where changing the base only changes an absolute constant". In `T = ceil(log(1000m))` the base matters: with natural log, `2m/2^T` grows without bound, reaching 64 at m=4^20. Base 2 is the reading the convention intends, and the bound then holds. Lean must use `Nat.clog 2`.
- **D2, quantum model never defined formally (largest formal risk).** The upper bound uses intermediate measurement, classical adaptivity and fresh registers. Lemma A.2 assumes a purified fixed-length sequence and dismisses the conversion in one sentence. Both are standard and compatible, but one Lean definition must serve both directions, with a proved purification lemma. Choosing a model that makes only one direction easy would weaken the meaning of `Q`.
- **D3, Forrelation lower bound (external, not reproved).** Corollary 1.4 of Bansal-Sinha does match the citation: same normal form, `delta=2^{-5k}`, same `delta/2` threshold, error 1/3, bound `Omega(k^{-29}(N/log(kN))^{1-1/k})`. Everything downstream is conditional on this published theorem. Its constant is implicit, so "sufficiently large m" has no explicit threshold.
- **D4, circuit basis unspecified (harmless).** "Fan-in at most two" leaves constant gates open, and "size" is only later said to count non-input gates. Constant gates cost one query per test, so the bounds survive. The Lean circuit type should settle this.
- **D5, verification cost display (harmless).** The display at line 488 counts only the search. The fresh polylogarithmic decoding before each search is omitted, and is dominated.
- **D6, implicit conditioning (harmless).** Line 619 says the zero's location is uniform "conditional on the full adaptive transcript"; it also needs "and the zero not yet found". Lean must state this.
- **D7, scope of "the only external lower-bound input" (wording).** True of lower bounds on `P`. The proofs still use finite minimax [27], Perron-Frobenius, and an unnamed Chernoff or Hoeffding bound in Lemma 2.1(ii). All are standard. Perron-Frobenius can be avoided: a nonnegative Rayleigh maximiser is enough.
- **D8, notation overload (readability).** `W` is the total weight, the Walsh matrix and the adversary potential. `T` is the stage count and a decision tree. `l` is `log_2 m` and the Grover iteration count. `c` is comparison cost, and also the adversary constant. `H` and `H'` are different matrices. Use separate Lean names.
- **D9, not checked.** The pointers to Drucker's Section 1.3 and Lemmas 3.1-3.2 and the rest of the Section 1.1 history were not read at source. Lemma 4.1 is proved in full in the paper, so no proof depends on these.

Consistency check: the construction has `bs` and `deg` of order m up to logs, so `D <= bs*deg` allows order m^2, in line with the claimed `R`. This does not prove the claim.

## Design consequences

1. **Make the construction generic in `P`.** Sections 2-4 use only three facts about `P`: `L < R(P)`, a coherent decoder, and an exact circuit of size S. Define `F` over a structure bundling `P`, `C`, `m` and `r`. Forrelation then becomes one instance.
2. **Prop 4.2 is non-asymptotic.** For any m with `1 <= L <= m` and `L < R(P)`, the bound `R(F) > floor(mL/100)` holds. "Sufficiently large" only supplies those hypotheses. The circuit's size does not enter this bound, and its correctness is used only to show `F(Y1)=1`.
3. **Prop 3.2 splits cleanly.** Its ideal weight process and coupling are classical, and only exact sampling is quantum. The classical half belongs early.
4. **Prove Lemma 4.1 by Bellman recursion on a finite tree.** This avoids measurable transcripts and the martingale library altogether.
5. **The heavy-column argument bounds a joint event** and conditions on nothing. Keep it so; do not condition on nonheaviness. Query counts in `def-heavy` and `def-simulator` must both include repeats.

## Smallest definition set to fix first

1. `def-partial-query`: one `PartialBool` for partial and total functions.
2. `def-R` and `def-D`: decision trees of bounded depth, with `R` as a mixture of trees.
3. `def-transcript`: gate-level circuit type and transcripts, with settled basis (D4).
4. `def-column-layout`: a finite `BitLoc` type for input locations.
5. `eq-3` and `eq-4`: Forrelation by the exact integer form of `claim-integer-tests`, so that it is decidable.
6. `eq-6`, `def-win-at-address`, `def-F`: `m=4^t`, `r=40t`, `l=2t`; `WinsAt` is the primitive and winner is its existential.
7. `def-query-oracle` and `def-Q`: adaptive and purified algorithms with the purification lemma statement. Fix this before any quantum proof, even if proved later.

## Recommended stages

Each stage lists its exact rows. Every ledger row appears in one stage.

Six dependency edges point to a later stage on purpose, because the later result enters the earlier stage as an interface rather than a proof. `def-K`, `lem-2.2.i` and `claim-Y-values` take the specification in `lem-2.1.iii` as a structure field. `claim-coupling` takes the sampler kernel from `claim-success-prob` and `lem-3.1` as a hypothesis. `prop-4.2` takes `lem-2.1.i` as the hypothesis `L < R P`. The stage ordering is therefore a build plan, not a topological sort; the topological sort is at the end of this file.

### Stage 0: classical definitions
`def-log-convention`, `def-partial-query`, `def-R`, `def-D`, `def-transcript`, `def-eval-transcript`, `def-walsh-sign`, `eq-3`, `eq-4`, `eq-5`, `eq-6`, `def-column-layout`, `eq-7`, `eq-8`, `def-winner`, `def-win-at-address`, `def-F`, `eq-17`

### Stage 1: finite logic and the ideal tournament
`cor-unique-winner`, `lem-2.2.i`, `def-K`, `cor-local-dichotomy`, `claim-N-phi`, `claim-integer-tests`, `eq-10`, `def-T-eps`, `eq-11`, `def-ideal-process`, `eq-12`, `eq-13`, `claim-expected-WT`, `claim-weight-lb`, `eq-14`, `claim-coupling`, `claim-sin2theta`, `eq-9`

`eq-13` has a file in the project already (see below).

### Stage 2: randomized lower bound, conditional on `L < R(P)` (first milestone)
`claim-product-law`, `def-value-V`, `eq-16`, `claim-supermartingale`, `claim-final-bound`, `lem-4.1`, `claim-minimax-mu`, `def-dummy`, `def-planted`, `claim-Y-values`, `eq-18`, `def-Z`, `claim-uniform-zero`, `claim-EZ`, `eq-19`, `def-heavy`, `eq-20`, `def-simulator`, `eq-21`, `eq-22`, `eq-23`, `claim-tail`, `claim-numeric`, `prop-4.2`, `cor-R-omega`, `claim-floor`

Exit criterion: `R_F_gt` compiles with no `sorry`, stated for a generic `P`, with `L < R P` as its only external hypothesis.

### Stage 3: Appendix combinatorics, no quantum
`def-deg`, `def-bs`, `def-Gamma-i`, `def-Sf`, `claim-round-block`, `lem-A.5`, `def-huang`, `claim-huang-spectrum`, `claim-restrict-parity`, `claim-interlace`, `lem-A.4`

### Stage 4: quantum model and adversary bound
`def-query-oracle`, `def-Q`, `eq-1`, `claim-perron`, `def-adv-progress`, `claim-per-query`, `claim-final-overlap`, `lem-A.2`, `lem-A.3.bs`, `lem-A.3.lambda`, `lem-A.3`, `thm-A.1`

Stage 4 settles D2, and it gives the first complete theorem on the quantum side, the quartic upper bound.

### Stage 5: quantum primitives
`def-grover-trial`, `claim-grover-state`, `lem-3.1`, `def-aij`, `construct-sampler`, `eq-15`, `claim-success-prob`, `claim-tournament-cost`, `prop-3.2`, `claim-proj-prob`, `lem-2.1.ii`, `claim-coherent-access`, `lem-2.2.ii`, `lem-2.2`

### Stage 6: circuit size and the quantum upper bound
`claim-circuit-size`, `lem-2.1.iii`, `def-decode`, `claim-decode-cost`, `def-comparison`, `claim-comparison-state`, `claim-winner-dominates`, `def-verify`, `claim-verify`, `claim-error`, `prop-3.3`

### Stage 7: assembly
`claim-bs-to-L`, `lem-2.1.i`, `lem-2.1`, `eq-2`, `claim-exponent-ratio`, `claim-no-smaller-exponent`, `thm-1.1`, `cor-cubic-refuted`

Final statement: `alphaTot = 4` under the hypothesis `forall k >= 2, BansalSinha k`.

## External results

**Enter as an explicit named hypothesis (one only):**

- `BansalSinha k`: for all large t, `Lval k t < R (Forr k t)`. This is the weakest form the proofs consume. Optionally also record the literal `BansalSinhaCor14` and derive it through `claim-bs-to-L`, so a reader can compare it directly with the source. The hypothesis is meaningful only if `R` is the standard measure, so add sanity theorems such as `R f <= D f`, `D f <= n`, and `R` of a known function.

**Prove; do not assume:**

- Finite minimax. Mathlib at the pinned commit has `Mathlib/Topology/Sion.lean` with `exists_isSaddlePointOn`; apply it on simplices. A temporary named hypothesis `YaoMinimax` is acceptable as scaffolding during Stage 2 only, and must be discharged.
- Chernoff or Hoeffding for `lem-2.1.ii`. Only a very crude bound is needed.
- Nonnegative top Rayleigh vector, replacing Perron-Frobenius (`claim-perron`). A search of mathlib for "perron" found only unrelated hits.
- Grover rotation, adversary bound, Huang's theorem and Midrijanis's inequality. The paper proves all of them. `Archive/Sensitivity.lean` exists at the pinned mathlib, but Archive is not importable, so vendor `f_squared`, `f_matrix` and `exists_eigenvalue`. Its final theorem gives max degree, so the Rayleigh conclusion of `claim-interlace` needs a modified last step.

Searches of the pinned mathlib found no Walsh matrix, decision tree, circuit type or quantum query library. All of these are new work. Those were name searches, so absence is likely rather than certain.

## Project state observed

During this task `lean/` appeared in `quartic-query-lean`, with a pinned mathlib, Lean 4.34.1, a README, and a 79-line `lean/QuarticQuery/Tournament/Drift.lean`. It was not written, read or assessed here. It probably overlaps `eq-13`; check it before starting Stage 1.

Sibling files also appeared in this folder, including `prior_art_classical_lean.json`, `prior_art_quantum_lean.json`, `references_resolved.json` and `verification_tooling.md`. They were not used here, so the reuse statements above cover mathlib only. Consult them before starting new work on circuits, decision trees or quantum foundations.

## Dependency order

In layers: construction definitions, then local certificate logic (Lemma 2.2). From there two independent branches run to the family bounds: classical (Lemma 4.1, minimax, Prop 4.2) and quantum (Lemma 3.1, Prop 3.2, Prop 3.3). Appendix A is independent of the construction. Theorem 1.1 joins all three.

```text
eq-3, eq-4 -> Lemma 2.1 (i external; ii quantum; iii circuit) -> winner, F -> Lemma 2.2
Lemma 4.1 + minimax + Lemma 2.1(i) -> Prop 4.2 ----------------\
Lemma 3.1 -> Prop 3.2; Lemma 2.1(ii,iii) + Lemma 2.2 -> Prop 3.3 -> eq-2 -> no alpha < 4 -\
Lemma A.2 -> A.3; Huang -> A.4; A.5 -> Theorem A.1 -------------------------------------> Theorem 1.1
```

Full topological order of all rows (each row after everything it depends on):

```text
def-log-convention
def-partial-query
def-R
def-query-oracle
def-Q
eq-1
eq-10
def-ideal-process
eq-12
eq-13
claim-expected-WT
def-T-eps
eq-11
claim-weight-lb
eq-14
def-grover-trial
claim-grover-state
claim-sin2theta
eq-9
lem-3.1
def-aij
construct-sampler
eq-15
claim-success-prob
claim-coupling
claim-tournament-cost
prop-3.2
def-walsh-sign
eq-3
eq-4
claim-proj-prob
lem-2.1.ii
eq-6
def-decode
def-transcript
def-column-layout
def-comparison
claim-decode-cost
claim-coherent-access
claim-comparison-state
eq-7
eq-8
def-eval-transcript
def-winner
claim-winner-dominates
def-win-at-address
claim-N-phi
claim-integer-tests
claim-circuit-size
lem-2.1.iii
def-K
lem-2.2.i
lem-2.2.ii
def-verify
cor-local-dichotomy
claim-verify
claim-error
prop-3.3
eq-5
eq-17
claim-bs-to-L
lem-2.1.i
claim-product-law
def-value-V
eq-16
claim-supermartingale
claim-final-bound
lem-4.1
claim-minimax-mu
def-dummy
def-planted
def-F
claim-Y-values
eq-18
def-Z
claim-uniform-zero
claim-EZ
eq-19
def-heavy
eq-20
def-simulator
eq-21
eq-22
eq-23
claim-tail
claim-numeric
prop-4.2
cor-R-omega
claim-floor
eq-2
def-Gamma-i
claim-perron
def-adv-progress
claim-per-query
claim-final-overlap
lem-A.2
def-bs
lem-A.3.bs
def-Sf
lem-A.3.lambda
lem-A.3
def-deg
claim-restrict-parity
def-huang
claim-huang-spectrum
claim-interlace
lem-A.4
claim-round-block
def-D
lem-A.5
thm-A.1
claim-exponent-ratio
claim-no-smaller-exponent
thm-1.1
cor-cubic-refuted
lem-2.1
cor-unique-winner
lem-2.2
```
