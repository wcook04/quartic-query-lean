# Statement fidelity of the nearly quartic separation

**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

This audit is an additional AI review. It contains source analysis, ordinary mathematical arguments, and independent finite computations. It contains no new Lean compilation, Comparator execution, or external-kernel replay. All proposed Lean signatures are **unelaborated**.

<!-- passage:verdict -->
## 1. Result and scope

The supplied source states the full unconditional conclusion of OpenAI's preprint: the optimal universal exponent relating bounded-error randomized and quantum query complexity of total Boolean functions is four. The declarations `QuarticQuery.alphaTot_eq_four_unconditional` and `QuarticQuery.theorem_1_1_unconditional` have no `BansalSinhaLower` hypothesis. They use `QuarticQuery.ForrelationLower.bansalSinhaLower`, whose source proves the precise fixed-parameter lower bound required by the construction. [OAI26, Theorem 1.1; `Results/Unconditional.lean:18–38`; `ForrelationLower/Main.lean:506–543`; IDs `thm-1.1`, `lem-2.1.i`.]

No mathematical mis-encoding was found in the inspected public definitions, finite minima, parameter quantifiers, construction, or quantum bridges on the intended range. This judgment is narrower than a new certification of the complete proof. The audit read the public statement vocabulary in full, followed the relevant defining and transport declarations, compared the statements with primary sources, and tested independent small instances. The archive lacks the compiled environment and original run receipts. Two imported foundational modules were absent and could not be retrieved at the specified pin. Those limits are recorded in `READ_SCOPE.md`.

There is a definite defect in the dependency-reporting algorithm: its namespace filter prevents traversal through Lean private declarations. Consequently, an unreached label is insufficient evidence that a public lemma is absent from the proof's dependency closure. This finding concerns the proof-use metadata. It supplies no counterexample to the theorem and no reason to believe that the kernel skipped a proof.

The important distinctions are as follows.

| Finding | Classification | Consequence |
| --- | --- | --- |
| Public query models, Forrelation promise, and addressed construction | Exact on the stated range, with harmless representations described below | Preserve the mathematical statements. |
| Private-helper traversal in `scripts/Reach.lean` | Wrong dependency-extraction algorithm | Repair and regenerate before relying on negative reachability labels. |
| Root build associated with an uncommitted working tree | Incorrect evidence description, already adjudicated | Preserve the reported historical run; do not call it a clean build of the named commit. |
| Four new modules uncompiled, with `Model/Classical.lean` newer than its reported output | Current-source verification boundary | Compile those explicit targets and bind the new receipt to their bytes. |
| Challenge vocabulary copied from `Statement.lean` | Valid mechanical comparison with shared semantic specification | Keep independent small-function tests to check intended meaning. |
| Extra square root in the Špalek–Szegedy annex digest | Wrong transcription; constants only in that digest | Correct the digest; the formal quartic constant is unaffected. |
| Expected randomized cost in the Beals et al. source | Changes the theorem if silently substituted | Use the worst-case convention and direct classical parity proof here. |
| Bansal–Sinha display locator and ABKRT theorem number | Citation errors | Correct the exact locators without changing the mathematical conclusion. |

The recommendations are advisory. No supplied source or evidence record was modified.

<!-- passage:conventions -->
## 2. Reading conventions and reference points

Paths beginning `Statement.lean`, `Model/`, `Bridge/`, `Construction/`, `Forrelation/`, `ForrelationLower/`, `Results/`, `Upper/`, `Tournament/`, or `Paper/` are relative to `repository/lean/QuarticQuery/` in the supplied archive. Other paths are stated relative to the archive root. Line numbers are physical source lines, not positions in an extracted search result. Printed theorem and page numbers take precedence when TeX extraction loses a macro.

The standard classical and quantum models are those of Buhrman and de Wolf [BDW02, §§3.1–3.3, printed pp.5–8], with unrestricted computation between queries and worst-case query count. The quantum measurement conventions are also checked against de Wolf [DW26, §§1.2.2, 2.1.2, 2.3]. Forrelation is compared with Bansal and Sinha [BS21, v3, equations (1.1)–(1.3), Theorem 1.3], as well as the preprint's equations (3)–(5). The universal quartic upper bound is ABKRT [ABKRT21, printed Theorem 2, p.2]. Full citations and stable public URLs are in `references.bib`.

“Exact” below means that no difference in the mathematical statement was found. “Harmless” means a representation or extension outside the active parameter range that preserves the stated complexity. “Constants only” is reserved for a change of convention that preserves the asymptotic conclusion. A weakened or strengthened domain or quantifier is described explicitly. “Wrong” identifies a demonstrable error, with its affected object named.

<!-- passage:classical-definitions -->
## 3. Inputs, deterministic queries, and randomization

| Definition and source | Exact ordinary meaning | Comparison and verdict |
| --- | --- | --- |
| `BitInput ι`, `TotalBool ι`, `PartialBool ι`, `Statement.lean:26–30` | An input is a function from coordinates to Boolean values. A total function returns a Boolean; a partial function returns `some b` on its domain and `none` elsewhere. | Equivalent to a Boolean function on a subset of the cube. Harmless representation. [OAI26, §1.3; BDW02, §2.] |
| `totalise`, lines 32–33 | Embed a total function by returning `some (f x)` on every input. | Exact; the total domain remains the whole cube. |
| `promised`, lines 35–36 | There exists a Boolean output at the input. | Exact domain predicate. An `Option Bool` cannot prescribe two different values at one input. |
| `reindex`, lines 38–40 | Given a coordinate bijection, precompose the queried input with that bijection before evaluating the original function. | Harmless renaming, with no aggregation of bits. Classical and quantum invariance are proved in `Model/Classical.lean:335–360` and `Model/Quantum.lean`, `Q_reindex`. |
| `QueryTree`, `QueryTree.eval`, lines 44–50 | A finite binary tree; each internal node reads one coordinate, follows the branch selected by that bit, and eventually returns a Boolean leaf. | Exact adaptive decision-tree model. [BDW02, §3.1.] |
| `QueryTree.depth`, lines 52–55 | A leaf costs zero; a query costs one plus the larger child depth. Repeated queries are charged. | Correct syntactic cap. Redundant inconsistent paths can overcharge an individual tree; they can be pruned without altering its behavior. The minimum complexity is unchanged. |
| `RandomizedProgram`, lines 57–64 | A finite mixture of trees, with strictly positive real weights summing to one. | Exact finite-support version of the standard biased-coin model. There are finitely many bounded-depth trees over a finite coordinate set; zero weights may be removed. A size-zero program cannot satisfy the sum constraint. [BDW02, §3.2; `LowerBound/Minimax.lean:88–130`.] |
| `RandomizedProgram.depth`, lines 66–67 | The maximum depth over all trees in the support. | Exact worst-case support cost. Small positive probability does not discount an expensive branch. |
| `RandomizedProgram.success`, lines 69–71 | On the specified input, sum the weights of trees returning the specified answer. | Exact probability. Weights are fixed before the input, nonnegative, and normalized. |
| `RLe f q`, lines 73–76 | One randomized program of cap at most `q` succeeds with probability at least two thirds on every promised input. | Exact pointwise bounded error. The algorithm existential precedes the input universal. Equality at two thirds is allowed. |
| `DLe f q`, lines 78–80 | One deterministic tree of depth at most `q` is exactly correct on every promised input. | Exact deterministic promise complexity. The total-function use passes through `totalise`. |
| `R`, `D`, lines 82–88 | The natural infima of their respective feasible-budget sets. | These are attained minima because read-all witnesses exist. Exact; no empty-infimum shortcut is used. |

The mathematical reference for this whole table is [BDW02, §§3.1–3.2]; the preprint fixes the error and worst-case convention in §1. The corpus associations are `def-partial-query`, `def-R`, and `def-D`.

<!-- passage:classical-minima -->
### 3.1 Feasibility, mass, and zero queries

The read-all tree is built at `Model/Classical.lean:231–241`, and its randomized version at lines 244–248. Nonemptiness and attainment follow at lines 256–269, with the feasibility/minimum equivalences at lines 278–283. The default output `(f x).getD false` is used only after reading the whole input; promised correctness follows from `f x = some b`. It does not turn an off-promise value into an obligation.

A distribution fixed before the input cannot distinguish two labels with zero queries. If its probability of returning true is `p`, correctness on a true input requires `p ≥ 2/3`; correctness on a false input requires `1-p ≥ 2/3`. These requirements are incompatible. Empty promises and promises with only one output label correctly have zero cost. Thus proposed checks `sanity-R-zero-characterization` and `sanity-D-zero-characterization` ask for exact equivalence with `ConstantOnPromise`, including the empty case. The elementary proof is independent of the separation.

The positive-weight convention does not require a common positive lower bound on weights. It only ensures that the support maximum charges every listed tree. The finite-support and arbitrary-real-weight conventions match the cited biased-coin model. A model restricted to a finite string of fair coins would require an additional convention about exact probabilities and boundary error; that convention is not imposed by this preprint.

The source also uses `LowerBound.Minimax` to obtain a hard distribution on the promise. Its construction explicitly excludes an empty domain, makes the distribution sum to one, and quantifies over every bounded-depth deterministic tree (`LowerBound/Minimax.lean:138–175`). This distributional step does not replace the pointwise definition of randomized correctness.

<!-- passage:quantum-definitions -->
## 4. Quantum algorithms

| Definition and source | Exact ordinary meaning | Comparison and verdict |
| --- | --- | --- |
| `Basis ι w`, `State ι w`, `Statement.lean:95–98` | Basis labels are an input coordinate, a response bit, and one of `w+1` workspace labels; states form the complex Euclidean space on those labels. | Faithful finite workspace. Arbitrary finite dimension embeds in a qubit space with unused coordinates at no query cost. The workspace is unrestricted. [BDW02, §3.3.] |
| `bitOracle`, lines 102–105 | The output amplitude at `(i,b,z)` is the previous amplitude at `(i,b XOR xᵢ,z)`. | Exact XOR oracle. Pullback and basis-vector action agree because this permutation is an involution. The index and workspace do not change. |
| `project S`, lines 108–110 | Orthogonal projection onto the coordinate subspace indexed by `S`. | Exact binary projective measurement with complementary component `ψ-project S ψ`. Other bases use input-independent unitary conjugation. [DW26, §1.2.2.] |
| `AdaptiveProgram`, lines 114–118 | A finite syntax tree of Boolean outputs, complex linear isometric endomorphisms, oracle calls, and binary measurements with classical branching. | Faithful finite quantum query program. In finite equal dimension a linear isometry is unitary. No runtime or gate-count restriction is asserted. |
| `AdaptiveProgram.queryCap`, lines 122–127 | Unitaries and output add no query; each oracle adds one; a measurement takes the maximum of both branch caps. | Exact syntactic worst-case cap. Even an unreachable branch contributes to this cap; equivalent pruned programs remain available. |
| `AdaptiveProgram.outputMass`, lines 130–137 | A leaf contributes the squared norm to its label. Transform states through unitary/oracle steps. Add the masses of the two unnormalized measurement branches. | Exact unconditional Born probabilities. Branches are neither discarded nor separately normalized to unit probability. |
| `ConstantOnPromise`, lines 141–142 | There is one Boolean equal to every defined output. | Correct zero-query case, including an empty promise. |
| `QLe f q`, lines 144–148 | Either the promise is constant, or there exist one finite workspace, one unit initial state and one program, of cap at most `q`, whose correct-label mass is at least two thirds for every promised input. | Exact quantifier order. The program, gates, measurement sets, state, and labels are chosen before the input. |
| `Q`, lines 150–151 | Natural infimum of feasible quantum budgets. | Attained minimum. A read-all tree compiles into a quantum program with the same query cap. |

These definitions match the preprint's §1 oracle and query conventions, and [BDW02, §3.3; DW26, §§2.1.2, 2.3]. Their corpus IDs are `def-query-oracle` and `def-Q`. General finite POVMs can be represented on a larger space using projective measurements [DW26, §1.2.2, footnote 5]; the source does not expose one separate theorem for every such alternative formalism.

<!-- passage:quantum-failure-modes -->
### 4.1 Normalization, hidden input access, and the empty register

`AdaptiveProgram.outputMass_true_add_false` proves that the two final masses sum to the initial squared norm (`Model/Quantum.lean:146–165`). Nonnegativity and the upper bound by that norm appear nearby. With a unit initial state this is an ordinary normalized output distribution. Zero-norm branches contribute zero. The mathematics rules out postselection and probability creation.

The free gates may act on a query index conditioned on previously obtained answers. That is ordinary adaptive computation. New information about the input enters only at a `.query` constructor, which contributes one to the cap. Arbitrarily large workspace and query-free ancilla operations are permitted in the standard model and in the imported per-algorithm bound.

The constant disjunct in `QLe` handles a genuine boundary: when the coordinate type is empty, its query basis is empty and contains no unit vector. There is then only one bit input, so any partial Boolean function is constant on its domain. `constantOnPromise_of_isEmpty` establishes exactly that fact. The disjunct cannot certify a two-label promise.

`DLe.toQLe`, `QLe_card`, `QLe_Q`, and `Q_le_iff` provide the read-all witness, nonemptiness, attainment, and minimum characterization (`Model/Quantum.lean:388–423`). The proposed zero-query invariance and `Q=0` characterization make the input-independence argument independently visible. An exposed exact-cost simulation of every finite randomized program would add `Q≤R`; the present source already exposes `Q≤D`. This is a useful interface addition, with no missing implication in the quartic proof.

<!-- passage:forrelation-definitions -->
## 5. Forrelation and its promise

| Definition and source | Exact ordinary meaning | Comparison and verdict |
| --- | --- | --- |
| `mValue t`, `Statement.lean:159` | The positive integer `2^(2t)=4^t`. | Exact power-of-four parameter in [OAI26, §2]. |
| `ForrelationCoord k t`, line 161 | A pair consisting of one of `k` layers and one of `m` coordinates. | Exactly `km` input bits. Bansal–Sinha's `N` is this vector length `m`, not the total `km`. |
| `bitSign`, line 164 | False denotes positive one and true denotes negative one. | Exact stated Boolean-to-sign convention. |
| `walshSign`, lines 167–169 | The sign determined by the parity of the bitwise dot product of the two `2t`-bit indices. | Exact unnormalized Walsh entry. Summing in the naturals before raising negative one preserves parity. |
| `forrelationNumerator`, lines 172–177 | Sum over paths choosing one coordinate in each layer, multiplying all input signs and the Walsh sign between each pair of consecutive layers. | Exact path expansion for positive `k`; natural `k-1` gives the correct number of transitions. |
| `forrelationDenominator`, lines 180–181 | The positive integer `m(2^t)^(k-1)`. | Exactly `m(√m)^(k-1)`; it never vanishes. |
| `Phi`, lines 183–184 | The real quotient of that integer numerator and denominator. | Exact normalized matrix expression for `k≥1`; the source states this range explicitly. |
| `P`, lines 188–193 | With `δ=2^(-5k)`, return true if `Phi≥δ`, false if `abs(Phi)≤δ/2`, and undefined otherwise. | Exact positive-high versus near-zero promise. A large negative value is excluded. Integer comparisons eliminate rounding and real comparison ambiguities. |

The references are [OAI26, §2.1, equations (3)–(5)] and [BS21, v3, `main.tex:212–229`, equations (1.1)–(1.3)]. The corresponding IDs are `def-walsh-sign`, `eq-3`, `eq-4`, and `eq-5`.

`Forrelation.Phi_eq_matrix_product` (`Forrelation/Product.lean:158–183`) proves the matrix interpretation, with at least one layer. `H_mul_H` and `H_mem_orthogonalGroup` (`Forrelation/Walsh.lean:200–212`) give Walsh normalization. `forrelationDenominator_pos`, `cases_disjoint`, and the three `P_eq_…_iff` theorems (`Forrelation/Promise.lean:28–92`) establish positivity and exact promise equivalence. These are substantive semantic bridges already present in source.

<!-- passage:forrelation-boundaries -->
### 5.1 Boundary parameters and independent nonvacuity

At `k=0`, the sum over the empty path has one term. The public definition consequently gives `Phi=1/m`. An empty alternating matrix product would give one. The existing matrix-product theorem retains the necessary positive-`k` hypothesis, and the separation uses `k≥2`. This is a harmless extension outside the intended range; `sf-phi-zero-layers` is a guard against dropping the hypothesis.

For every `k≥2` and `t≥1`, both promised labels and an excluded input occur. The following new elementary check is registered as `sf-forrelation-three-statuses`:

\[
\exists z_+,z_0,z_-:\quad
\Phi_{k,m}(z_+)=1,\qquad \Phi_{k,m}(z_0)=0,\qquad
\Phi_{k,m}(z_-)=-1.
\]

Their `P` values are respectively true, false, and undefined. Here is a proof independent of the hardness theorem. Set every interior sign vector to the all-one vector. The scalar is then the endpoint bilinear form with `k-1` copies of the normalized Walsh matrix, divided by `m`. Write `χ(x)=(-1)^(x₀)` for a balanced Walsh character. For odd `k`, the even number of Walsh factors cancels to the identity; endpoint pairs `(1,1)`, `(χ,1)`, and `(-1,1)` give the three values.

For even `k`, use the sign vector `b(x)=(-1)^(Σⱼ x₂ⱼ x₂ⱼ₊₁)`. The normalized four-dimensional Walsh matrix fixes `(1,1,1,-1)`. Tensoring this identity over the `t` coordinate pairs gives `Hb=b`. The endpoint pairs `(b,b)`, `(bχ,b)`, and `(-b,b)` give the three values because `b²=1` coordinatewise and `χ` sums to zero. The threshold lies strictly between zero and one, so the stated promise labels follow. The finite script checks these witnesses for `k=2,…,8` and `t=1,…,3`; the argument establishes the general claim. Its Lean signature remains unelaborated.

<!-- passage:circuit-definitions -->
## 6. Circuits and transcripts

| Definition and source | Exact ordinary meaning | Comparison and verdict |
| --- | --- | --- |
| `Gate ι g`, `Statement.lean:201–204` | A two-input Boolean table whose predecessors are actual input coordinates, earlier gates indexed below `g`, or a false constant. | Exact fan-in-at-most-two circuit convention. Using a fixed complete Boolean basis changes size by an absolute constant only. |
| `Circuit ι`, lines 206–210 | A finite acyclic gate list, with two gate indices designated as domain and value outputs. | Exact construction object. It is uninhabited at size zero because the outputs must be gate indices. Outputs may coincide. |
| `predecessorValue`, lines 212–217 | Read the actual input bit, the claimed earlier transcript bit, or false, according to the predecessor. | Exact. An input value is never accepted merely because a transcript claims it. |
| `GateConsistent`, lines 220–224 | Every stored gate bit equals its table applied to the specified predecessor values. | Exact local consistency, including output and unused gates. |
| `CircuitRealises`, lines 228–232 | On every input a consistent transcript exists; every consistent transcript has domain output true exactly on the promise, and on the promise its value output equals the partial function. | Exact semantic realization. There is no vacuity through absent transcripts. |

The relevant preprint statements are Lemma 2.1(iii) and §2.2; the IDs are `def-transcript`, `def-eval-transcript`, `claim-circuit-size`, and `lem-2.1.iii`. Independently of `CircuitRealises`, `circuitEval_gateConsistent` and `existsUnique_gateConsistent` prove that each acyclic circuit has a unique consistent transcript (`Construction/Transcript.lean:53–73`). The existential transcript field cannot hide a contradictory gate system.

The circuit builder uses natural-number wires internally. Missing and forward wire references evaluate as false, and conversion to the public circuit makes the same repair (`Forrelation/Builder.lean:142–153`). The proof of realization is about this actual acyclic circuit. Its modular arithmetic may overflow at intermediate steps because it preserves residues; the final comparison operands satisfy explicit signed bounds (`Forrelation/Arithmetic.lean:409–475`; `Forrelation/Circuit.lean:170–215`). An assertion that every intermediate integer fits is unnecessary and is not used.

`forrCircuit_realises` (`Forrelation/Circuit.lean:343–384`) supplies exact domain and value behavior. `forrCircuit_size_le` and `exists_circuit` give the required small circuit for the positive parameters (`:466–486`). The source uses an explicit implementation of the preprint's circuit-existence claim; the mathematical circuit convention is unchanged.

<!-- passage:construction-definitions -->
## 7. The addressed total function

| Definition and source | Exact ordinary meaning | Comparison and verdict |
| --- | --- | --- |
| `Column ℓ`, `Address r`, `Statement.lean:240–241` | A column is one of `2^ℓ` indices. An address is an `r`-bit word. | Exact. There is one empty address at `r=0`. |
| `BitLoc ℓ r S κ`, lines 245–249 | A disjoint union of physical `X` bits, address-instance bits, pointer bits, and circuit-transcript bits. Pointer and transcript coordinates include both the owning column and its cell address. | Exact layout. Cells are not shared across columns or addresses; the total input has no promise. |
| `readX`, `readA`, `readPointerBit`, `readTranscript`, lines 255–265 | Project to those four physical coordinate sets. The first two indices of `readX` are column and row. | Exact coordinate reads. Whole words are mathematical projections, not zero-cost operations granted to an algorithm. |
| `pointerEquiv`, lines 270–271 | One fixed bijection from `ℓ`-bit strings to rows. | Exact allowed convention. Every bit pattern is valid; the preprint permits any fixed bijection, so endianness is immaterial. |
| `WinsAt`, lines 277–283 | A candidate column is all ones; its address instances are promised and equal the chosen address bits; its active-cell transcripts are consistent; its active-cell pointers find a zero in every other column. | Exact conjunction. The pointers point outward from the candidate to its competitors. |
| `addressedF`, lines 287–289 | Boolean truth value of the existence of a winning column and its address. | Exact total Boolean function. `Classical.decide` in its mathematical definition supplies no query operation to a computing algorithm. |
| `Fkm`, lines 294–296 | Specialize to `P k t`, `ℓ=2t`, `r=40t`, and the supplied circuit `C`, chosen to realize `P` in the family theorems. | Exact specialization: `log₂m=2t` and `ceil(20 log₂m)=40t`. |

These definitions match [OAI26, §2.2, equations (6)–(8)] and IDs `eq-6`, `def-column-layout`, `eq-7`, `eq-8`, `def-winner`, and `def-F`.

The physical cardinality is a useful independent test (`sf-bitloc-cardinality`). With `m=2^ℓ`, it is

\[
\#\mathrm{BitLoc}
=m^2+mr\lvert\kappa\rvert
+m2^r(m-1)\ell+m2^rrS.
\]

The four terms count `X`, address-instance, pointer, and transcript bits. This check catches a missing owning-column or address index, which a local correctness theorem might otherwise conceal.

<!-- passage:construction-failure-modes -->
### 7.1 Witness uniqueness and circuit choice

The existential address cannot select an unrelated favorable cell: each bit is fixed by the corresponding defined value of the partial function. `winsAt_address_unique` makes this explicit (`Construction/Winner.lean:50–52`). If two different columns were winners, the first one's pointer would select a zero in the second one's all-one column. `winsAt_column_unique` proves this contradiction (`:42–47`), without assuming that any opponent address instance is promised. These are exact forms of `cor-unique-winner`.

Different realizing circuits need not give literally equal total functions. The transcript input length and gate consistency conditions can change, including when unused gates are appended. The preprint specifies a circuit construction scheme. `family_bounds` and `theorem_1_1_unconditional` select one circuit shared by the circuit-size, quantum-upper, and randomized-lower conclusions. That shared choice is what the separation requires (`Results/Conditional.lean:25–35`; `Results/Unconditional.lean:23–38`). An assertion of extensional equality for every realizing circuit would be stronger and generally ill-typed when their sizes differ.

At `t=0`, there is one column, no address instances, and no opponents. `Fkm` consequently equals its single `X` bit (`sf-Fkm-t-zero`). For a generic everywhere-undefined partial function and positive `r`, no address can satisfy the winner predicate, so the generic construction is constantly false (`sf-empty-promise-rejects`). Both are intended extensions. Neither witnesses the eventual hardness theorem.

The helper `trueAddr` defaults off-promise answers to false. The planted-input acceptance theorem explicitly assumes that every winning address instance is promised (`LowerBound/Planted/Inputs.lean:106–128`). Thus that default does not create a false certificate for an undefined instance.

<!-- passage:local-tests -->
### 7.2 Local verification is adaptive

`TestIndex` counts the local checks, and `card_testIndex` gives the preprint's value `K=m+(m-1)+r(S+2)` (`Construction/LocalTests.lean:129–134`; ID `def-K`). Each gate check reads the claimed output and its two predecessors. Each pointer check reads its `ℓ` pointer bits and then queries the selected target coordinate. Hence its query depth is at most `ℓ+1`; its possible target support over all inputs can be much larger. `localTestTree_depth_le` and `winsAt_iff_localTests` state the correct adaptive result (`:219–259`; IDs `lem-2.2.i`, `lem-2.2.ii`).

The original preprint already makes this adaptive distinction [OAI26, Lemma 2.2, printed p.6, `paper/extracted.md:274–288`]. The “Correction” comment in the new `Paper/Section2.lean:232–237` should identify the earlier ledger as the object corrected. It should not imply that the preprint asserted fixed support of size `ℓ+1`.

That new wrapper's coherent clause prepares a uniform index distribution. The preprint's clause permits supplied indices in superposition. The existing comment acknowledges the narrower interface; retain its partial status until that interface is proved. This distinction does not invalidate the separately constructed quantum upper bound. `Paper/Section2.lean` is uncompiled in the supplied build table.

<!-- passage:tournament -->
## 8. Comparison probabilities

`Tournament.IsComparison` (`Statement.lean:300–304`) states complementarity for distinct candidates and zero diagonal. It does not assert that entries lie between zero and one. This exactly records equation (10), while the probability range is represented separately by `Tournament.UnitValued` (`Tournament/Ideal.lean:28–29`).

Range-sensitive probability and expectation estimates, monotonicity, Markov bounds, and `tournament_runs` take the range hypothesis explicitly. The actual comparison sampler supplies it through `cmpProb_unit` (`Upper/Columns.lean:203–209`), and the application passes both properties (`Upper/Verify.lean:177–180`). The uncompiled `Paper.prop_3_2` derives the same range from its sampling assumption (`Paper/Section3.lean:201–208`). The drift identities without the range premise are valid stronger algebraic identities. Bare functions named `prob` or `expectFrom` should be described as probabilities or expectations only under their range hypotheses. No missing probability hypothesis was found. [OAI26, §3.2, equation (10), Proposition 3.2; IDs `eq-10`, `eq-12`, `eq-13`, `prop-3.2`.]

<!-- passage:parameters -->
## 9. Floors, powers, and the optimal exponent

| Definition and source | Exact ordinary meaning | Comparison and verdict |
| --- | --- | --- |
| `Lvalue k t`, `Statement.lean:309–311` | Natural floor of `m^(1-1/k)/(log₂m)^2`, with the exponent and division in the reals. | Exact equation (5) for `k≥2,t≥1`. The cast precedes division, so this is not natural-number `1/k`. |
| `Gvalue m L`, lines 313–314 | Natural quotient `mL/100`. | Exact floor in equation (17), with positive divisor 100. |
| `BansalSinhaLower`, lines 319–320 | For each fixed `k≥2`, eventually in `t`, `Lvalue k t < R(P k t)`. | Exact lower-bound input needed by Lemma 2.1(i). It is weaker than the full parameter-uniform Bansal–Sinha theorem and is not an axiom. |
| `UniversalPower α`, lines 323–326 | `α≥0`, and one positive constant `C` works simultaneously for all positive input lengths and all total Boolean functions, bounding `R` by `C(1+Q)^α`. | Exact equation (1), including the shift by one. The constant cannot depend on the input length or function. |
| `alphaTot`, line 329 | Real infimum of the set of universal exponents. | Exact. The proof establishes that four is the least member before evaluating the infimum. |
| `familyExponent`, `Results/Exponent.lean:131` | The real number `4-2/k`. | Exact for positive `k`; the source proves the small values and approach to four. |
| `FamilyBoundsAt`, `FamilyBounds`, `Results/Exponent.lean:170–178` | For each fixed `k`, positive constants and a threshold precede `t`; at every sufficiently large `t`, one circuit has both complexity bounds. | Correct shared witness and quantifiers. Natural `b` may be zero syntactically; increasing it on `t≥1` yields the preprint's positive logarithmic exponent, and the actual witness is six. |

The active real-power bases are positive: `m=4^t≥1` and `1+Q≥1`. For positive `t`, `log₂m=2t>0`. At `t=0`, real division by zero is totalized and `Lvalue=0`; this is outside the large-parameter estimates. Natural subtraction in the Forrelation paths occurs only as `k-1` on the active range `k≥2`. These checks exclude a floor, zero-base, or truncated-subtraction shortcut. [IDs `eq-1`, `eq-2`, `eq-5`, `eq-17`, `claim-floor`, `claim-exponent-ratio`.]

<!-- passage:headline-quantifiers -->
### 9.1 What the headline actually implies

The floor estimate `Gvalue_ge` is proved for `t≥8` (`Results/Exponent.lean:363–406`). It permits the literal lower bound with positive constant `1/400`. Registered proposal `fidelity-literal-eq2` makes the complete paper formulation explicit: for each fixed `k≥2`, positive `c_k,C_k`, a positive natural `b_k`, and a threshold can be chosen so that the same circuit at every sufficiently large `m=4^t` gives

\[
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^{b_k},
\qquad
R(F_{k,m})\ge c_k\frac{m^{2-1/k}}{(\log_2m)^2}.
\]

This is equation (2), with a proposed literal wrapper around existing source results. The wrapper remains unelaborated. It requires no new asymptotic lower-bound argument.

For a proposed universal exponent below four, choose `k` so that `2-1/k` exceeds half that exponent, and then hold `k` fixed while letting `t` grow. The resulting positive polynomial exponent dominates the fixed logarithmic factors. The source chooses `k` before the large `t`, and the two estimates use the same circuit (`Results/Exponent.lean:159–164,202–238`). Reindexing to `Fin n` preserves both complexities; the physical coordinate type is nonempty, so `n≥1` is satisfied. Each fixed-`k` family has exponent `4-2/k`. No claim that one fixed family attains a fourth power follows from this argument. [IDs `claim-exponent-ratio`, `claim-no-smaller-exponent`, `thm-1.1`.]

`alphaTot_eq_four_of` constructs an `IsLeast` proof before invoking `csInf_eq` (`Results/Exponent.lean:243–252`). Membership of four makes the defining set nonempty, and the first conjunct of `UniversalPower` bounds it below by zero. Thus the theorem uses an ordinary least exponent, not an exceptional value of an empty or unbounded infimum.

The current lower-bound theorem follows the project's own Forrelation proof and transports it to the exact public promise. This is an alternative to relying on Bansal–Sinha's quantitative display. The name `BansalSinhaLower` describes the fixed-`k` proposition required by the preprint; it should not be expanded into a claim that the full original uniform theorem has been formalized.

<!-- passage:bridges -->
## 10. Model transport and Appendix A

### 10.1 Classical trees

`QueryTree.toDecisionTree` and `QueryTree.ofDecisionTree` are inverse constructor translations. Evaluation and depth agree, and `D_totalise_eq_complexity` identifies the two deterministic minima (`Bridge/DecisionTree.lean:25–80`). The transport has no query multiplier. [ID `def-D`.]

### 10.2 XOR and controlled phase

The imported `phaseOracle` multiplies a basis vector by the sign determined jointly by the input bit and the response/control bit (`complexitylib/Complexity/Computability/QueryComplexity/Quantum/Search.lean:81–121`). It is a controlled phase oracle. A response Hadamard conjugates it to the public XOR oracle, and the converse conjugation also holds (`Bridge/Oracle.lean:100–117`). Both use one physical oracle call.

`run_phaseGates` preserves the final state of a fixed sequence with exactly the same query count, including zero (`Bridge/Oracle.lean:119–155`). The Hadamards and all changed gates are input-independent and query-free. A bare phase oracle lacking the control bit would fail the one-input-bit identity test: its two possible oracle actions differ only by global phase. The actual definition retains the control bit. [DW26, §2.3 and footnote 17; ID `def-query-oracle`.]

### 10.3 Deferred measurements

`FixedSim` records a finite workspace, an oracle-compatible embedding, an entry isometry, a gate sequence, an acceptance set, and a specification for every input and every initial vector (`Bridge/Deferred.lean:148–157`). The gates are selected before those universal arguments.

A finished branch is padded by phase queries with identity gates. These may change its state, but preserve its norm and hence its already-fixed output probability (lines 162–175). A free unitary is absorbed into the entry map. A query uses the one-call Hadamard conjugation and an input-independent extension of an isometry (`exists_gate`, lines 135–142; query case 193–224). A measurement stores its histories in orthogonal workspace summands and uses block-diagonal operations, so their acceptance masses add without interference (lines 226–265). The structural construction turns a cap of at most `T` into exactly `T` controlled phase queries (lines 268–292).

The specification preserves true-output probability. False-output probability follows from norm and total-mass conservation. No equivalence of postmeasurement states or stopping times is required. This exact count is stronger than the constant-factor conversion sufficient for the preprint's asymptotic application. [IDs `def-Q`, `lem-A.2`, `thm-A.1`; DW26, §2.1.2 and Chapter 2, Exercise 8.]

<!-- passage:imported-quartic -->
### 10.4 The imported quartic theorem

`Cslib.Quantum.complexity_le_mul_pow_four` applies to a normalized fixed-sequence algorithm on any finite workspace that approximates a total Boolean function on every input. Its conclusion is the following explicit form of `thm-A.1`:

\[
D(f)\le 20736\,T^4.
\]

The supplied source proves this in `complexitylib/Complexity/Computability/QueryComplexity/Quantum/Adversary.lean:303–315`, using degree at most `1296T²`, block sensitivity at most `16T²`, and the deterministic bound by their product. The explicit constant belongs to that library proof. The earlier asymptotic theorem is due to Aaronson, Ben-David, Kothari, Rao, and Tal [ABKRT21, printed Theorem 2, p.2]. The extracted Markdown's numbering is unreliable because it loses a `restatable` theorem.

`D_le_of_QLe` converts the adaptive witness, translates two-label success into the absolute-error hypothesis, and handles the constant case with a leaf tree (`Appendix/TheoremA1.lean:25–49`). Attainment then gives `D_le_Q_pow_four`; `R≤D` and the shift by one yield `universalPower_four` (lines 51–77).

This is a faithful proof of Theorem A.1 by an alternative formal route. It does not establish every intermediate Appendix statement. In particular, the arbitrary-nonnegative-matrix adversary claim of Lemma A.2 has partial coverage; deferred measurement alone does not supply that entire lemma. Retain the separate route and coverage labels. The missing imported `Measurement` and `DecisionTree.Basic` modules also prevent claiming that this audit read the entire pinned transitive dependency closure.

<!-- passage:comparator -->
## 11. What Comparator establishes

All five Challenge files import Mathlib only and copy the public definition block from `Statement.lean`, apart from their header and introductory comment. They are independently compiled specifications with shared mathematical vocabulary. The source comparison was performed for the full blocks, not for a few printed theorem lines. [Files `repository/lean/QuarticCorpus/*/Challenge.lean`; Comparator's official README, “Internals” and “Definition Holes,” cited as `ComparatorDocs`.]

| Bundle | Selected claims |
| --- | --- |
| Tournament | Drift identity and half-total bound. |
| Foundations | Minimum/feasibility characterizations, `R≤D`, `Q≤D`, read-all bounds, and coordinate-renaming invariance. |
| Construction | Winner/address uniqueness, circuit-transcript uniqueness, and pointer consequences. |
| Separation | Conditional headline and cubic refutation, membership of four, family bounds, and generic addressed lower bound. |
| Unconditional | Optimal exponent, full conjunction theorem, cubic refutation, and the proved `BansalSinhaLower`. |

Every configuration permits only `propext`, `Quot.sound`, and `Classical.choice`. The empty `definition_names` list permits no definition holes; it does not instruct the tool to ignore definitions. Definitions in the compared statements are recursively checked. The supplied negative controls alter a conclusion, alter a definition through an impossible field, introduce `sorry`, introduce a foreign axiom, or omit a declaration. The archive reports their rejection; this audit did not rerun them.

A theorem hypothesis remains part of its type. Axiom checking does not remove it. Thus the conditional theorem in the Separation bundle stays conditional, while the separate Unconditional bundle names the source endpoint with that hypothesis discharged. The historical conditional file is not evidence that the current result is still conditional.

Acceptance protects correspondence to the Challenge. It cannot detect a shared erroneous definition copied into both sides. For example, moving an algorithm existential inside the input quantifier on both sides would let a different constant algorithm answer each input. Mechanical agreement could coexist with a zero-query definition of every function. Independent identity, parity, and nonvacuity tests must reject such a model.

No supplied configuration itself names the external kernels. Reproducing a reported paranoid run requires its actual command, versions, exports, reports, and source hashes. An unsandboxed local rehearsal is evidence of the reported proof comparison, with no sandbox-isolation attestation. These qualifications preserve the useful historical evidence while stating its exact scope.

<!-- passage:reachability -->
## 12. Defect in dependency reachability

`repository/lean/scripts/Reach.lean:13–14` accepts a displayed project name only when it has prefix `QuarticQuery` and is not internal. In `dependencies`, lines 33–39, an excluded constant is traversed only if it is internal and still has that prefix. Lean private names have the form `_private.<module_name>.0.<original_name>` [LeanPrivateNames]. Such a name fails the prefix test, so its type and body are not visited. This is a definite algorithmic incompleteness.

The minimal pattern is a public root whose proof uses a private wrapper whose proof uses a public leaf. The current extractor can retain the root and omit the leaf. `checks/check_reach_private.py` reproduces that name-filtering failure in a synthetic graph. `checks/ReachPrivateFixture.lean` provides an unelaborated Lean fixture for the real pinned environment. The Python test is an algorithmic regression demonstration, not a Lean execution.

The actual source and supplied graph contain two discrepancies consistent with this defect:

1. `QuarticQuery.norm_hadamardL` is reached. Its source uses private `norm_pair`, which uses public `QuarticQuery.norm_invSqrtTwo_sq` (`Bridge/Oracle.lean:37–40,69–85`). The latter is declared but unreached in the graph.
2. `QuarticQuery.FixedSim.query` is reached. Its source explicitly invokes `exists_gate` and `hadamard_phaseOracle_hadamard` (`Bridge/Deferred.lean:195–209`). Its reported outgoing edges omit them, and the oracle-conjugation lemma is marked unreached in the `def-query-oracle` record.

Without the matching compiled environment, the exact generated-helper path behind each discrepancy is unconfirmed, and source/graph age could be an additional cause. The definite filter failure is enough to invalidate a general inference from “unreached” to “unused.” The kernel's own checking is a separate operation and is not weakened by an incomplete reporting script.

The repair is to traverse every referenced constant's type and available body before applying display filters, including private and generated auxiliaries. Preserve actual kernel names internally. Record missing-constant diagnostics and the source, toolchain, and compiled-object hashes. If a collapsed public graph is desired, derive it after the complete traversal, with the hidden paths retained as provenance. Then regenerate the reach fields and all descriptions of declarations as outside the proof. A public-root/private-wrapper/public-leaf regression must pass before the new graph is used to remove or discount source declarations.

<!-- passage:provenance -->
## 13. Source and execution provenance

The independently checked manifest-listed files all have their stated sizes and SHA-256 hashes. This establishes local integrity relative to that manifest. It does not establish which bytes a past build used. The snapshot commit is `4c7544f8dcdfc18d3ecf8476ebd8c1090cd46f15`, while `BUILD_STATUS.md` associates the root build with `16adedc16acca1e3a8d2963d4fd5655dcd0492d7`.

The supplied adjudication already resolves the principal discrepancy: finding `F-PIN-BUILD` says that build used an uncommitted working tree. Its receipt mentions declarations in files first committed later at `06f3eb8`. Preserve the reported successful execution, and replace the clean-pin interpretation. Finding `F-PIN-REPLAY` separately records a later Comparator run at `d42fb67a7e060fb5386867dadf20a5903df39141`, where the sources exist, and reports no Lean-source changes between that commit and the earlier compared snapshot. That is a historical adjudication, not a source-equivalence certificate for every byte in this round's archive. [Files `repository/research/adjudication/funnel_adjudication.json` and `funnel_adjudication_notes.md`.]

`BUILD_STATUS.md` lists `ForrelationLower/Uniform.lean` and `Paper/Section2.lean`, `Section3.lean`, `Section4.lean` as uncompiled. It lists `Model/Classical.lean` as compiled but with an output older than source. The introductory claim that every compiled module has an up-to-date output therefore needs qualification. None of the four new modules is imported by the current `QuarticQuery.lean` root; rebuilding that root alone does not establish their compilation.

The archive contains no `.olean` files, no raw `corpus/receipts/` directory, no exported kernel reports, and no Git history sufficient to reproduce the adjudication's comparisons. Lean and Lake were unavailable. The correct present description is: historical records report build and comparison success; this audit reads and tests the supplied source semantics and does not replay those executions. The fresh receipt should identify every target, the complete dirty/clean source state, dependency pins, source hashes, commands, exit codes, and generated report hashes.

<!-- passage:literature-corrections -->
## 14. Literature and attribution corrections

### 14.1 Randomized parity convention

The supplied Beals et al. source defines its randomized measure using expected query count (`literature/quartic-ref-08-quantum-lower-bounds-by-polynomials/extracted.md:205–207`) and explicitly uses that convention in the parity discussion (`:532–533`). Its classical parity value must not be imported into this development's worst-case support measure. Its quantum two-bit parity algorithm and Proposition 6.4 are appropriate references for the quantum side. The classical two-bit lower bound below is proved directly under [BDW02, §3.2]. This is a convention difference that changes a statement when ignored.

### 14.2 Špalek–Szegedy digest

The annex `literature/quartic-ref-24-all-quantum-adversary-methods-are-equivale/annex_notes.json`, note `n003`, inserts an extra outer square root in the denominator of Theorem 3.1. The publisher PDF, printed p.6, has denominator `1-2√(ε(1-ε))`, without that outer root [SS06]. The digest's numerical coefficient about `0.239` is consequently not obtained from the printed formula. Direct substitution of error one third into the printed expression gives about `0.0571909584`.

This is a transcription and arithmetic correction to an annex digest. No sharp constant transport between that paper's conventions and this formal model has been verified here. Use its asymptotic nonnegative spectral-adversary bound for this audit; the explicit imported quartic constant is proved independently. The paper's equivalence concerns the nonnegative adversary methods then known, and its lower-bound direction is credited to earlier work in its closing proof. Neither its title nor the digest should be generalized to all later negative-weight adversary methods.

### 14.3 ABKRT theorem numbering

The cited deterministic/quantum quartic result is printed Theorem 2 on page 2 of arXiv:2010.12629v1 [ABKRT21]. The supplied extracted text loses an earlier restatable theorem and shifts numbering. The citation should use the original PDF numbering. This is a locator correction, with no mathematical change.

### 14.4 Bansal–Sinha §5.4

The previously adjudicated concern is real and specific. In the third inequality of the final aligned display in §5.4, the power of the logarithm used to bound each Fourier-level term is too small when the level exceeds `k`. The ratio between the original and replacement logarithmic factors has exponent `(level/k-1)/2`, which is positive in that case. Levels above `k` occur in the displayed range for every `k≥3`; the `k=2` case does not have this obstruction. The substitution therefore fails to follow by that termwise estimate. A weaker logarithmic denominator still supports the fixed-`k` consequence needed here; a full extra logarithmic power is already sufficient compared with the preprint's squared-logarithm denominator. [BS21, §5.4; supplied `bansal_sinha_section54_second_reading.md`; ID `claim-bs-to-L`.]

This identifies a failed inequality in that written derivation. It does not refute the published lower-bound theorem, and it does not affect the project's independent Forrelation proof. No uniform-in-`k` repair is claimed in this audit.

There is also a definite locator correction. In the exact supplied `source.tar.gz`, the disputed third inequality is physical `main.tex:1181`; physical line 1184 is the subsequent depth condition. The extracted member has SHA-256 `800119f9f12877392a92e34ac380c61a50b2a297cee0a70511058580061f835b`. Cite the section, final aligned display, third inequality, and these bytes. The line-1184 references in the packet should be corrected while preserving the adjudicated mathematical finding.

<!-- passage:small-classical -->
## 15. Independent small-function checks

The following values use error at most one third and the supplied worst-case query convention. They are elementary audit deductions, with the classical rational certificates in `checks/check_classical_small.py`; proposed formal statements are in `sanity_theorems.json`.

| Function or promise | D | R | Q | Registered checks |
| --- | ---: | ---: | ---: | --- |
| Constant function | 0 | 0 | 0 | `sanity-constant-classical`, `sf-q-zero-iff-constant` |
| Empty promise | 0 | 0 | 0 | `sanity-empty-promise-classical`, `sf-q-zero-iff-constant` |
| One-bit identity | 1 | 1 | 1 | `sanity-identity-one-bit-classical`, `sf-q-dictator` |
| OR on two bits | 2 | 1 | 1 | `sanity-or-two-classical`, `sf-q-or-two` |
| XOR on two bits | 2 | 2 | 1 | `sanity-xor-two-classical`, `sf-q-xor-two` |

For two-bit OR, choose uniformly among the constant-true tree, the tree reading the first bit, and the tree reading the second bit. Its success probabilities on `00,01,10,11` are two thirds, two thirds, two thirds, and one. Nonconstancy excludes zero queries. No depth-one deterministic tree computes OR, while a depth-two tree does. A finite quantum coin selector simulates the same randomized algorithm at one query. The randomized test also detects changing the inclusive threshold to strict success greater than two thirds: under the uniform distribution on `00,01,10`, every one-query tree succeeds with probability at most two thirds.

For XOR, every depth-one deterministic tree succeeds on exactly half of the uniformly distributed inputs, and a mixture preserves that average. Per-input success at least two thirds is impossible at that cap. Reading both bits succeeds exactly. Quantumly, prepare an equal superposition of the two indices with response state `|−⟩`; one query produces their relative phase, and a Hadamard on the index reveals parity exactly. This is the two-input instance discussed in [BBCMW01, supplied text, Proposition 6.4 and adjacent discussion]. The finite Python checks certify the classical arithmetic; this quantum construction is an ordinary mathematical argument with an unelaborated Lean proposal.

The separate floor check `sanity-L-first-positive-k2` gives `Lvalue 2 7=0`, `Lvalue 2 8=1`, and `Gvalue (mValue 8) (Lvalue 2 8)=655`. It catches the logarithm base, `m=4^t`, real division by `k`, and both floor placements. It also warns against presenting a tiny construction as already exhibiting an asymptotic separation.

<!-- passage:small-forrelation -->
### 15.1 Hand-computed Forrelation

For `k=2,t=1`, use the normalized four-dimensional Walsh matrix. Both sign vectors `(1,1,1,-1)` give `Phi=1`; replacing the first by `(1,1,-1,1)` gives zero. The existing negative witness uses `(-1,1,1,1)` in both layers and gives negative one, which is excluded from the promise. These are `sf-phi-positive-two-one`, `sf-phi-zero-two-one`, and `sf-existing-negative-witness`.

The independent exact-rational enumeration gives the following scalar histogram (`sf-phi-two-one-histogram`), consistent with the already-proved promise census:

| Phi | -1 | -1/2 | 0 | 1/2 | 1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Number of inputs | 8 | 96 | 48 | 96 | 8 |

The resulting promise counts are 104 true, 48 false, and 104 undefined. `Forrelation/Sanity.lean:20–32` already contains the promise census; lines 54–65 contain the negative-witness facts. The named positive and zero examples and general three-status check are useful additions; the census is not a newly discovered formal gap. The full scalar histogram is a finite diagnostic recorded in `checks/construction_checks_output.json`; only the already-present promise census is cited as existing Lean evidence.

<!-- passage:one-winner -->
### 15.2 A one-winner board

An understandable exhaustive model uses two columns, one address bit, the one-bit identity promise problem, and a circuit with domain output true and value output equal to its input. Its input has eighteen bits. Give the first column `X=(1,1)` and the second `X=(0,1)`. Set the first address input to true, place transcript `(true,true)` in its true cell, and point from that cell to the zero in the second column. Set every unmentioned bit to false. The first column wins. This construction is the generic addressed function, not the enormous `Fkm` instance with forty address bits at `t=1`.

The script enumerates every board. Direct winner evaluation and the circuit-local tests agree, and at most one winner occurs. Exactly 16384 boards accept (`sf-toy-board-census`). As an independent count, a specified column is all ones with probability one quarter, its selected transcript is the unique correct two-bit string with probability one quarter, and its selected opponent bit is zero with probability one half. Thus a specified column wins with probability one thirty-second. The two winning events are disjoint, giving total fraction one sixteenth. This is a finite diagnostic of `def-winner`, `def-F`, `cor-unique-winner`, and `lem-2.2`; it is not presented as a new compiled theorem.

On the displayed board, flipping a winning `X` bit, its address input, its active pointer, or either active transcript bit makes the function reject. Changing an inactive cell bit or the opponent's address input preserves acceptance. These mutations directly test dependence on the true address and active cell. The larger formal proposal `sf-Fkm-one-winner` uses the actual `Fkm 2 1` with the existing `planted`, `circuitEval`, and `forrCircuit` definitions; `sf-Fkm-corrupt-active-transcript` asks that any changed active gate bit reject. Those proposed signatures remain unelaborated.

<!-- passage:negative-controls -->
## 16. Additional adversarial controls

`negative_controls.json` specifies mutations, independent tests, and expected failures. They are proposed controls and have not been run through Comparator. The highest-value controls have distinct targets:

| Mutation | Independent fact that must fail |
| --- | --- |
| Put the algorithm existential after the input universal | One-bit identity must require a query. |
| Replace worst-case maximum by minimum or expected depth | The support-cap and two-bit deterministic checks. |
| Admit negative random weights or renormalize every measurement branch | Nonnegative unit total output mass. |
| Replace `≥2/3` by `>2/3` | The exact one-query randomized OR witness. |
| Use a bare phase oracle without a response/control bit | The one-bit quantum identity algorithm. |
| Use absolute value in the high Forrelation threshold | The existing negative-one input must stay excluded. |
| Remove owning-column or address indices from cell coordinates | Physical input cardinality and active/inactive-cell behavior. |
| Reverse pointers or remove domain-output verification | One-winner acceptance and off-promise rejection. |
| Permit arbitrary cyclic gate predecessors | Canonical consistent transcripts need no longer exist. |
| Move the universal constant after the choice of function | The fixed universal-exponent definition changes. |
| Introduce the same bad specification on both Comparator sides | Independent semantic tests must reject even if comparison accepts. |
| Hide a public leaf behind a private proof wrapper | Correct dependency traversal must still reach the leaf. |

The shared-bad-specification control deliberately tests the boundary of statement comparison. It is not an allegation of an implementation bug in Comparator. Keep its independently specified expected answers outside the generator that copies `Statement.lean`.

<!-- passage:actions -->
## 17. Required repairs and proposed formalization

The first repair is the dependency traversal, followed by regeneration against identified source and compiled objects. Until then, suspend conclusions that rely on a negative reach label. The second is current-source execution evidence: explicitly compile the changed classical file and the four new targets, then preserve exact build, Comparator, and any external-kernel receipts. A reported build of the old root does not cover new unimported modules.

Correct the source descriptions without weakening the mathematical headline: retain the unconditional endpoint; distinguish a separately compiled Challenge from an independently authored specification; correct the annex square root, the ABKRT theorem number, and the Bansal–Sinha line locator; and identify the earlier ledger as the source of the pointer-support correction. `STATEMENT_CHANGES.json` marks these as evidence, documentation, or literature-description changes. It does not propose replacing the main mathematical statement.

The first formal additions should expose zero-query characterizations, exact OR and XOR values, a cost-preserving finite randomized-to-quantum simulation, and the general three-status Forrelation witnesses. Then package the literal equation (2) and the actual one-winner/mutated-transcript examples. Existing source facts about mass, oracle action, transcript uniqueness, and the small promise census should be reused. `LEAN_GAPS.md` distinguishes these proposed checks from already-present facts, partial interfaces, alternative routes, and unavailable execution evidence.

This audit supports the intended meaning of the source theorem while identifying concrete repairs to the evidence that describes it.
