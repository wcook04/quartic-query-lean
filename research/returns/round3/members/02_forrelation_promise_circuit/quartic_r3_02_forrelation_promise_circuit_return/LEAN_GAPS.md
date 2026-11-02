# Formal correspondence and exact remaining boundaries

This file accompanies the replacement §§3.1–3.5 in `section.md`. It records the current state of the supplied snapshot, not the submission-time state of the preserved round-two candidates. Packet source pin: `1dd469dd0042b937b739da3bc211eeb60bdf7462`; toolchain: `leanprover/lean4:v4.36.0-rc2`. Complete declaration types, ordinary premises, statement relations and evidence locators belong to `correspondence.json` and its source/evidence records.

## Evidence state governing every entry

The timestamped source-bound root receipt, `repository/corpus/receipts/lean-build-root-2026-11-02T182539383153+0000.json`, includes the relevant integrated declarations. The evidence audit freshly recomputed all 124 local Lean/configuration source bindings and found them current for this packet. Relevant helper modules also have matching supplied native-pass records. The recorded full-type/axiom audit contains the principal wrapper declarations and reports only `propext`, `Quot.sound`, and `Classical.choice`; its source and log hashes match the supplied passed verdict.

These are inspected records of prior executions. **No new Lean build, kernel computation or Comparator execution was performed in this review. No human mathematical review is claimed.** No current Comparator receipt names the Forrelation promise, projection, decoder or circuit helper declarations assessed here. Root or aggregate Comparator success does not transfer to every helper.

The packet pin differs from the commit label recorded by the current root receipt (`31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`). Currentness is established by the complete matching local source bindings, not by equating those labels. The older unbound `lean-build-root.json`, historical unsuccessful attempts, and preserved `UNELABORATED` comments must not override the later source-bound passes.

The reviewed principal wrappers have ordinary parameter premises and no additional open assumptions. Conditions such as `k ≥ 1`, `m = 4^t`, `t ≥ 1`, or `0 < η < 1/2` are their mathematical domains. A missing conclusion is recorded below as a missing conclusion; it is not an unproved binder silently accepted by the theorem.

## §3.1 — Normalization, promise and lower-bound scale

**Current complete support.** `QuarticQuery.Paper.construction_walsh_definitions`, `construction_equation_3`, and `construction_equation_4` package the normalization, exact matrix word, threshold, input count, both values, undefined case and disjointness. Their maintained ties are exact on the power-of-four family. Older component ties remain partial because each component states only part of its corresponding row.

**The old missing- L tie is resolved.** `QuarticQuery.Paper.construction_equation_5` now states the definition of `Lvalue` and has an exact reviewed tie to `eq-5`, current build membership and an explicit type/axiom printout. The baseline's assertion that this row has no tie is obsolete.

**No additional mathematical premise is introduced.** This section fixes `k ≥ 2`, `t ≥ 1`; several formal statements hold on the larger domain `k ≥ 1`. The identity `M = 2^(t*(k+1))` is used only for nonempty products, where natural subtraction in the source denominator has its intended meaning. No assertion is made about that simplified identity at the formal extension `k = 0`.

The row `eq-5` defines a scale only. The classical lower bound using that scale remains in §§3.6–3.16 and is not established by a definition or by this replacement section.

## §3.2 — Integer numerator and split comparison/output statements

`QuarticQuery.Paper.construction_N_phi` now supplies the complete numerator/denominator/scaling bundle. The old statement that no single declaration contains the entire `claim-N-phi` row is obsolete.

The remaining qualification for `claim-integer-tests` is a **conjunction/statement-tie limitation**. `QuarticQuery.Paper.construction_integer_tests` proves the comparison equivalences and promise predicates; `QuarticQuery.Paper.construction_forr_output_bits` exposes the actual circuit's all-input output equations. Both current ties are individually partial. Their ordinary conjunction supplies the section's argument, but no single exported theorem with one exact tie to the entire comparison-and-actual-output row is supplied.

In particular, the stronger conclusion `d = b = 0` off the promise follows for the concrete output pair. It must not be inferred from the generic `CircuitRealises` predicate alone: that predicate only constrains the value bit on the domain. The replacement cites the actual output equations for this stronger behavior.

This is not an unresolved arithmetic implication. The exact comparisons and the actual Boolean outputs are proved by their respective declarations; the missing item is their complete single-statement packaging and reviewed exact tie.

## §3.3 — Projection law, coherent state and physical query count

### The exact remaining tight-query clause

`QuarticQuery.Forrelation.successProb_eq` proves the real squared-projection identity. The promise-gap lemmas supply the two probability inequalities. `QuarticQuery.Paper.construction_projection_test` combines them with `Samples k` and the generic physical `Runs (2*k)` implementation. This remains a **partial** tie to a projection claim that includes exactly one physical bit query per diagonal in the full routine.

The missing full formal statement is a physical implementation of the whole alternating-word/projection experiment, on every input, with cap `k` and law `bern (Phi k t z ^ 2)`. A measured formulation would include

```lean
Runs k (fun z b => bern (Phi k t z ^ 2) b)
```

under the ordinary finite-domain and nonempty-block conditions. A complete retained-state formulation would additionally relate the same logical operation to the physical continuation with cap `k`, before measuring or resetting the workspace. Neither complete tight formulation is supplied here.

`QuarticQuery.Paper.construction_bitOracle_phase_kickback` and `construction_bitOracle_phase_preserves` have source-matched prior compilation evidence and prove the local one-call phase action, including entangled workspace. They do not assemble that action with the entire Walsh word, projection, repeated copies and retained-register computation. Their compilation must not be promoted to a complete `Runs k` theorem.

The ordinary proof in `forr_quantum` and `forr_coherent` provides the direct `k`-query trial and `qk`-query repetition algorithm. The source's fully packaged generic route instead costs `2qk`. Both give the required fixed-`k` asymptotic conclusion of Lemma 2.1(ii); the missing exact factor-one formalization does not weaken that conclusion.

### The old same-witness coherence omission is resolved

`QuarticQuery.Paper.construction_lemma_2_1_ii_complete` opens one sampler witness and applies `QuarticQuery.Upper.compile_circ` to that same isometry. Its type includes the initial label, output labeling, all-input normalized Boolean law, promised correctness, and a physical continuation acting on every embedded logical state with cap `2*(n*k)` plus the continuation's cap. This is the current exact reviewed tie to Lemma 2.1(ii).

The shorter `construction_lemma_2_1_ii` remains a partial helper: pairing a coherent sampler with a measured/reset implementation of the same law does not by itself state one retained physical witness. Use `_complete` for the complete conclusion; do not continue listing that formerly missing conjunction as an open gap.

The `Inhabited (ForrelationCoord k t)` instance is construction machinery. The proof constructs a zero block/zero address from `k ≥ 1` and `m > 0`; it fixes the parked physical query address. It is not an unproved mathematical hypothesis. The continuation equality only asserts behavior on the chosen logical embedding, which is exactly the initialized subspace used by the construction; arbitrary states outside that embedding are not required.

### Explicit count versus existential wrapper

The complete wrapper existentially quantifies its repetition count `n` and law. Its proof selects `n = repetitions k η`, but its public type does not itself contain that equality or the expanded binomial formula. The explicit ceiling count and binomial law in the section are supported by the repetition/decoder declarations, instantiated at `q`, together with the ordinary calculation. They are not attributed to the wrapper's existential type alone.

### Literal tensor-state representation

The display `R3-FOR-COHERENT-LAW` gives a complete ordinary retained-state construction using orthogonal projected vectors, fresh flags and a reversible count/output computation. The source proves the binomial law through retained sampler composition and provides the corresponding complete physical isometry witness. It does **not** state equality of its concrete register representation to the literal tensor-factor display in the replacement.

There is no missing probability implication: the ordinary display is proved directly, and the source independently proves the required coherent law. The unprovided clause is an exact state-identification theorem between these particular representations. The return does not claim that the new display is itself a newly checked Lean theorem.

## §3.4 — Modular arithmetic, ideal bounds and the actual endpoint

### No signed interpretation of every intermediate register

The arithmetic contracts establish congruences modulo `2^w`. Addition, subtraction, sign multiplication and Walsh recursion preserve those congruences. The final comparison integers are separately proved to lie in the signed range; only there is the high bit decoded as the sign of the corresponding ordinary integer.

`QuarticQuery.Paper.construction_walkN_bound` and the prefix/butterfly companions bound the **ideal integer** computations. They do not identify every stored modular register with a signed intermediate integer without wraparound. No register-by-register invariant supplying that stronger interpretation is present.

That stronger invariant is **not needed** for the implemented circuit's correctness. Correct modular computation plus the final signed-range bounds prove the exact outputs. Accordingly, the section distinguishes the ideal growth proof from the actual modular implementation and does not present the absent invariant as a defect in Lemma 2.1(iii).

### Current circuit-size ties remain partial at the bundled row

`claim-circuit-size` now has more support than the old sole tie to `abs_numerator_le`: current ties include `QuarticQuery.Paper.construction_circuit_costs` and ideal walk/prefix/butterfly bounds. These remain partial ties to the full prose row. The final circuit endpoint and explicit size bound are supplied by `QuarticQuery.Forrelation.exists_circuit` and the paper-level Lemma 2.1(iii) wrapper; `exists_circuit` covers the stronger parameter range `k ≥ 1`, `t ≥ 1`.

Do not infer an exact all-clause statement tie from successful compilation of the separate pieces. Do not infer the stronger register invariant from the final numerator bound or from the endpoint realization theorem.

### New closed-form cost calculation is ordinary mathematics

`R3-FOR-CIRCUIT-SIZE` solves the source's Walsh-cost recurrence and combines the constructor costs into

\[
S=6w\bigl((k+1)m+5k+t(k+1)+4\bigr)
 +(k-1)tm(12w+1)+7.
\]

This is an ordinary derivation from the inspected constructors, independently reconciled by the circuit reviewer and checked in the finite reconstruction. It is not the type of a newly compiled Lean declaration. Its resulting bound `S ≤ 200(k+1)^2 m (log₂ m)^2` is already supported by the existing formal endpoint. The return keeps the new equality's evidence class separate from the older inequality's formal support.

The transcript uniqueness argument is ordinary induction on the acyclic gate list and has existing source support; it does not identify the new checker with extracted Lean execution.

## §3.5 — Finite examples and checks

The source has compiled-record evidence for the `k=2,t=1` census and negative witness in `Forrelation/Sanity.lean`. This review did not replay `decide +kernel`. The three displayed examples and parity count have complete ordinary calculations in the section.

The new exact checker compares several independently written arithmetic evaluations and a Boolean-gate reconstruction over all 256 inputs at `k=2,t=1` and all 4,096 inputs at `k=3,t=1`. Its separate threshold-endpoint probes use synthetic integer numerators; realizability of each probe as a Forrelation input is not asserted. These computations are finite semantic evidence, not a universal theorem, extracted Lean execution, or proof of the growing-size classical lower bound.

## §3.17 consumer — supplied conjunction, unchanged classical boundary

`QuarticQuery.Paper.construction_lemma_2_1_complete` is present in the current source, included in the source-bound root receipt, and explicitly type/axiom audited. The baseline's “no single conjunction declaration” statement is obsolete. The suggested correction is located in `review_notes.md`; the frozen consumer section itself has not been edited here.

Its classical component follows the project's alternative fixed-parameter proof. This section neither re-audits that lower-bound proof nor uses the compiled conjunction to relabel every prose step as the published Bansal–Sinha route. No result for a growing-`k` family is claimed or imported.

## Remaining evidence limits

- Relevant wrappers can have exact maintained relations while lying outside the exported headline-root dependency closure. A row-level reached flag from a different component must not be assigned to the exact wrapper.
- The 124-file current source binding includes dependency manifests, not the full dependency checkout or compiler binaries. Native `.olean` artifacts are recorded but not supplied for an independent hash replay. Before/after source hashes do not rule out a change-and-revert during the original execution.
- The current positive Comparator bundles apply only to their listed declarations and challenges. They do not provide helper-level comparison here, independently authored semantic specifications, or a human review.
- The companion attachment `Pasted text(20261102-190823).txt` was unavailable. No instruction, claim or evidence from that file has been inferred. This return follows the available ZIP request and sources.

These boundaries are preserved in the return. No canonical definition, Lean source, corpus tie or prior receipt was modified.
