# Mathematical and statement-ledger audit

## Outcome

The packet contains 118 ledger rows. The delivered plan preserves all 118 IDs, gives a separate draft and incremental estimate for each, and checks that the revised dependency graph is acyclic. The strongest reuse opportunity is the existing `complexitylib` quartic upper bound; the largest genuinely external mathematical obligation remains the Bansal–Sinha Forrelation lower bound. The intervening adaptive direct-product and planted-input proof can be developed with finite decision trees and finite probability. No theorem in this audit was compiled in Lean or run through Comparator.

The paper's proof architecture survives this reading, but the intake's repeated “sound” / “no mathematical error found” labels should not be promoted to a verification result. I checked the definitions, the transitions in Sections 2–5, and the appendix against the supplied PDF text; the mathematical arguments still need the stated model, finite-probability and circuit realizability proofs. Source: `paper/extracted.md`, Sections 2–5 and Appendix A; the 118 source locators are carried in `formalisation_plan.json`.

## Corrections that change the formalization plan

### 1. Pointer tests are small decision trees, not small fixed juntas

Lemma 2.2 checks a pointer by reading its `ell` address bits, then the selected target bit of a rival X-string. The intake's `lem-2.2.i.first_lean_target` proposes that each test “depends on at most ell+1 bits.” That is false if “depends” means a fixed set of coordinates: changing the pointer can make any of m target bits relevant. The right assertion is a deterministic decision-tree depth of at most `ell+1`, with a coherent implementation of the corresponding adaptive lookup. The exact generic test-depth cap is `max 3 (ell+1)` because a binary gate check reads three bits. For the intended `t≥1`, ell≥2 and this equals ell+1.

This correction matters directly to resource accounting. A fixed-support lemma would be stronger than the paper and could not justify the actual pointer access. Sources: paper Lemma 2.2, extracted lines 266–288; ledger row `lem-2.2.i`.

### 2. The quantum model is a semantic bridge obligation

At pinned `complexitylib` commit `62ca5c21461b2482e8bd12b7cb9b4937d887a33a`, `Cslib.Quantum.State N W` has an arbitrary finite workspace W, and its oracle is controlled phase on `Fin N × Bool × W`. The intake's claim that the model has “trivial workspace” is incorrect. The source has per-algorithm statements, not a definition of the minimum Q. The core packet now defines adaptive bit-query Q and asks for purification and oracle/model transports before using those statements. Source: [Quantum/Search.lean](https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Computability/QueryComplexity/Quantum/Search.lean), declarations `State`, `phaseOracle`, `run`.

The paper uses adaptive measurements and fresh workspaces for its upper bound, but a fixed pure-state sequence in Lemma A.2. The bridge must preserve output law and give a worst-branch query bound. A constant-factor compilation is enough for the exponent, but it is not an identity of the exact Q measures. Input-dependent free gates, unit-cost cell access or expected-cost definitions would change the theorem. Source: paper conventions lines 118–123; tournament lines 409–446; Appendix A lines 750–754.

### 3. Read-all witnesses must precede minimum-complexity lower bounds

Both R and Q are often defined as natural infima. A missing algorithm witness can make the infimum of an empty feasible set equal zero. Prove finite-query read-all algorithms, nonempty feasible sets and attained minima first, including the empty-coordinate and empty-promise cases. Total-function R can then be identified with `complexitylib`'s `randomizedComplexity`; the promise-restricted variant is new work. Source: core definition draft; inspected `complexitylib` [Randomized.lean](https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Computability/QueryComplexity/Randomized.lean), especially `exists_computes_depth_eq_randomizedComplexity`.

### 4. The fixed k / growing m quantifiers must survive every shortened statement

For each fixed k≥2 the construction supplies an exponent `4−2/k` up to logarithms. For each α<4, first select a sufficiently large fixed k, then let t→∞ with m=4^t. This excludes every smaller universal power. It does not give an exact fourth-power separation for a single fixed-k family. For the cubic conjecture, k=3 already suffices; k=2 does not. Sources: paper Theorem 1.1 / equation (2), Section 5 lines 693–714. Original conjecture independently checked in [ABKRT, arXiv:2010.12629v1](https://arxiv.org/pdf/2010.12629), Conjecture 2, PDF page 20.

### 5. Generic lower-bound work need not wait for the efficient circuit

The randomized construction needs an exact circuit that recognizes the promise and answer, but not its size bound. The quantum verification cost needs `S=O_k(m(log m)^2)`. Therefore the generic planted-input theorem should take `P`, an exact circuit C, `1≤L≤m` and `L<R(P)` explicitly. Specialize only after constructing the efficient Walsh-transform circuit. A truth-table circuit can test the generic branch, but cannot discharge the efficient-family upper bound. Sources: paper Lemma 2.1(iii), Lemma 2.2 and Proposition 4.2.

The circuit-size proof is a large engineering task: signed arithmetic width/overflow, butterfly wiring, circuit sharing and count of non-input gates all matter. The paper's integer thresholds are exact, and their normalization was checked against Bansal–Sinha; no floating-point test belongs in the formal P definition. Sources: paper lines 183–199; Bansal–Sinha [arXiv:2008.07003v3](https://arxiv.org/pdf/2008.07003), equations (1.1)–(1.3), PDF pages 2–3.

## Lower-bound audit

### Capped direct products

At a positive-probability deterministic transcript, the set of compatible r-tuples is a Cartesian product of per-instance constraints. Adaptive query scheduling does not break that fact because the previous answers determine the schedule. The optimal remaining-budget success function decreases in conditional expectation when a particular next query is chosen. Other coordinates are unchanged. Multiplying those nonnegative continuation values, then applying induction on the finite tree, yields the β^r success bound.

This is not the generally false claim that a total budget rL forces ideal product success β^r. The cap is separately L for every instance. The paper's simulator actually uses the stronger cap L across its target column, so it satisfies the per-instance premise. Random coins and independent side information are fixed first and averaged afterwards. Sources: paper Lemma 4.1, lines 528–568; independently checked [Drucker arXiv:1005.0644v2](https://arxiv.org/pdf/1005.0644), Lemmas 3.1–3.2, PDF pages 11–12. A finite-tree Bellman proof is the recommended implementation; a full martingale development is unnecessary.

### The nonheavy event must stay inside the probability

Equation (21) is the joint bound

`Pr[column i is nonheavy AND query t hits its true cell] ≤ (2/3)^r`.

Do not replace it by a statement conditioned on the column being nonheavy: that event depends on the input and adaptive run, and may bias the answer distribution. The simulator proof avoids this by producing an event containment into the success event of a genuinely capped algorithm with independent side data. Source: paper lines 647–660; ledger `def-simulator`, `eq-21`.

### The removed-zero argument needs distinct positions and one common run

Before a column's zero has been seen, its posterior location is uniform over unqueried positions, conditional on the full actual transcript. Early discoveries charge at most 2/m per query. Late discoveries charge at least m/2 queried positions to distinct columns. Hence E[Z]≤4G/m. Averaging independent uniform I gives the extra factor 1/m. Both heavy-column and simulator budgets count repeated queries; discovery thresholds use distinct positions. Sources: paper lines 618–644.

### A simpler exact tail estimate

With m=4^t and r=40t,

`(2/3)^(40t) = ((2/3)^2)^(20t) ≤ (1/2)^(20t) = m^(-10)`.

If `G≤mL/100` and `L≤m`, then `G(2/3)^r≤1/(100m^8)≤1/100`. The total distinguishing bound is at most `4/100+1/100+1/100=6/100<1/3`. Thus the finite lower-bound theorem needs no logarithmic asymptotic estimate for this tail. “Sufficiently large” enters later to obtain `1≤L≤m` and `L<R(P)`. This is an elementary strengthening of the proof route, not a separate published theorem. Sources: paper equations (6), (17), (23); derived calculation above.

## Quantum-side reuse and scope

The existing local `Drift.lean` gives the finite sum identity and ≤W/2 under complementarity and positive total W. It does not model a random pivot, and it does not require nonnegative weights or a∈[0,1]. Those omitted inequalities are harmless for the algebra and necessary for its probabilistic interpretation. Add a legal tournament/weights wrapper and prove that the finite sum equals the expectation. Source: attached `lean/current/Drift.lean`, declarations `IsComparison`, `expected_weight_eq`, `expected_weight_le_half`.

Troy Lee's pinned library has `AmpSetup.amplified_cond_law`, not merely a search-success probability. That is directly relevant to exact pivot-law preservation. Its result is for classical readout probabilities and constant-error amplification; the paper's full successful-state claim and arbitrary η require additional wrappers. Its exact rotation theorem `GroverSplit.grover_pow_mulVec` is a useful state-level ingredient. Source: [Amplification.lean](https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/Amplitude/Amplification.lean) and [Geometry.lean](https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/Amplitude/Geometry.lean).

## Appendix shortcut does not imply all-row coverage

`Cslib.Quantum.complexity_le_mul_pow_four` proves `D(f)≤20736 T^4` for each bounded-error T-query algorithm in the source model. Its proof combines a sensitivity-specific adversary argument with a polynomial-method bound on block sensitivity. After the model bridge it can discharge Theorem A.1 and the main theorem's upper-bound side. It does not by itself discharge the paper's general nonnegative spectral adversary Lemma A.2, the Perron eigenvector statement, or every exact signed-cube spectrum row. Those still need their own proofs if every ledger row is to be checked. Source: [Adversary.lean](https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Computability/QueryComplexity/Quantum/Adversary.lean), module overview and `complexity_le_mul_pow_four`.

## What would change these conclusions

- A compiled, axiom-audited Forrelation lower bound with the same P, standard randomized bit-query semantics and error threshold would remove the long-lived Bansal–Sinha hypothesis. A theorem about Rorrelation, a nonstandard oracle or a weaker promise is insufficient.
- A compiled query-model transport would turn the selected upstream algorithm statements into imports for the core model. Until then, their precise constants are conditional on the transport overhead.
- A verified exact butterfly circuit with the required size bound would eliminate the main construction-engineering risk on the quantum side. Merely showing P is computable does not.
- A proof of generic spectral adversary and the literal intermediate appendix statements would permit all-row coverage claims; the already available quartic endpoint alone does not.

## Read coverage and evidence boundaries

Read in full: `READ_ME_FIRST.md`, all 118 rows of `corpus/statement_ledger.json`, `corpus/statement_ledger_notes.md`, all 16 commentary records, all 27 reference records, both prior-art JSON files, and all supplied paper extracted text including references. The paper was checked through its extracted content; formulas used here were cross-checked against the corresponding visible source representations and the root paper audit. Exact upstream source snippets and declarations were opened in shared model-audit files; they were not compiled. Historical trace reading was delegated to the separate tooling audit, not represented as completed by this mathematical audit. The bibliography record's absent local PDFs and metadata-only licenses are not silently treated as read or verified.
