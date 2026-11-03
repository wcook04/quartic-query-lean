# Round-four formal integration

This records what the round-four Lean returns actually do on this machine with
the pinned toolchain (`leanprover/lean4:v4.36.0-rc2`). The returns' own claims
are advisory: return 05 says it was never compiled, return 06 says every
Comparator attempt was blocked before comparison, and the return 08 candidate is
marked uncompiled. Build success, the axiom audit, Comparator acceptance and
semantic fidelity are reported separately below. The
[machine-readable record](round4_formal.json) lists every command, log hash,
repair and receipt.

## Summary

| Return | New modules | Built | Axioms | Comparator |
| --- | ---: | --- | --- | --- |
| 05 classical completion | 5 | yes, after three proof-script repairs in one file | standard three only | finite-seed endpoint accepted; capped-premise mutant rejected |
| 06 corpus fidelity | 4 production + 10 corpus | yes, unmodified | standard three only | Degree, ModelZero, RealLeaves accepted; all three mutants rejected |
| 04 quantum completion | 23 | yes, unmodified | standard three only | `uniformOpaqueAmplifier` and `construction_decoder_sharp` accepted |
| 08 zero-search candidate | 1 | yes, unmodified | standard three only | not run |

The allowed axioms are `propext`, `Classical.choice` and `Quot.sound`. No
audited declaration depends on `sorryAx` or any other axiom. The merged root
import (`lean/QuarticQuery.lean`) builds with all four additions.

## Return 05: realized-cap truncation

The integrate patch applies cleanly and its five files equal the shipped
`lean/` copies. Four modules built unchanged. `LowerBound/RealizedCaps.lean`
failed to elaborate as submitted and was repaired:

- `clip_path_eq_of_actualComplies`: the `simp only [hbit, ite_true, ite_false]`
  call left `if false = true` unreduced. It now uses
  `simp only [hbit, Bool.false_eq_true, ↓reduceIte]`.
- `compliantSuccess`: the `if` on the proposition
  `actualComplies ∧ ∀ h, ...` had no decision procedure. The definition is now
  preceded by `open scoped Classical in`. An `if` has the same value under any
  decision procedure, so the quantity is unchanged.
- `compliantSuccess_le_clipped`, non-compliant case: `simp [hc]` left
  `0 ≤ if ... then 1 else 0`. It is now closed by
  `simp only [hc, false_and, ↓reduceIte]` and `split_ifs <;> norm_num`.

No theorem statement changed.

**The endpoint is narrower than described.** No declaration named
`direct_product_external_realized_caps` exists. The main endpoint is
`QuarticQuery.direct_product_external_finite_realized_caps`. It covers a finite
seed space with arbitrary nonnegative weights summing to one. Each seed selects
an initially uncapped output tree. The weighted joint event "every instance
answered correctly and no instance exceeded its cap of `L` queries on this
input" is then at most `β^r`. The return's own docstrings say that arbitrary
measurable external randomness is not formalized, and
`MeasurablePolicies.lean` contains no measure theory. It is a finite-fuel
compiler from history policies to capped trees.

`Paper.classical_realized_caps` routes the clipped tree through the paper-style
`classical_direct_product` under a mass-one hypothesis.

Still unproved in Lean:

- `actualComplies c x` is a recursive cap predicate on the observed path. It is
  not proved equivalent to `∀ h, actualCount T x h ≤ c h`.
- The measurable seed transfer: measurable action-table fibers, their masses
  as real probabilities, and independence from the whole input tuple.
- Equivalence of `compilePolicy` with an unrestricted full-history runtime.

The bound is on the joint success-and-compliance event, not success
conditional on compliance. The return's finite AND counterexample shows the
conditional form is false; nothing here states it.

## Return 06: degree, zero-cost models and real leaves

The tools and test part was already integrated in `9d17016` and was not
re-applied. The returned `QuarticQuery.lean` differs from HEAD only by the
`RealLeafExplicit` import; that line was merged by hand with the 05 and 04
additions. All modules built without modification.

The return's audit used `set_option pp.universes true`, which prints
`Classical.choice.{u}`. The integration runner's first classifier treated the
suffix as a foreign axiom. It now strips universe suffixes; the raw Lean
output was already within policy.

Comparator results:

- `Independent.Degree.checked_degree_conventions` was accepted. The negative
  control omits uniqueness and the exact degree characterization; it was
  rejected because the statements do not match.
- `Independent.ModelZero.checked_zero_query_characterization` was accepted.
  The classical-only mutant, which drops the quantum clause, was rejected for
  the same reason.
- `Independent.RealLeaves.Compare.growth` and `Compare.advantage` were
  accepted. The mutant that restricts to the zero leaf was rejected.

The Degree and ModelZero challenges share their authored `Spec` modules with
the solutions. The RealLeaves targets are wrapper names over the maintained
`RealQueryTree` definitions. The production theorems
`sum_abs_ext_Dl_le_real_leaves` and `advantage_le_sharp_real_leaves` are
therefore wrapper-mediated and are not configured comparison targets. The
proposed degree tie in `proposed_adjudication.json` was not applied to
`corpus/ties.json`.

## Return 04: coherent quantum completion

The return ships a whole Lean tree. Compared with HEAD it differs only by 23
new files; no existing file and not the root import. Those 23 files were copied
unmodified and all built. The first build invocation was stopped by the build
guard's 1500-second seat budget after 12 modules had passed. The identical
command was then rerun, and the other 11 passed.

The authored bundles restate each type verbatim over the maintained
definitions:

- `Upper.uniformOpaqueAmplifier`: one selector gate chosen before every
  opaque unitary. For the same `finalB`, the bundle states the retained-factor
  identity and exact success mass `1 - trialFail^N`. It also states the
  zero-mass, `p/2`, `1-η` and auxiliary-support clauses, and the logical cap
  `N*((2*(M-1)+1)*n)`. Comparator accepted it.
- `Paper.construction_decoder_sharp`: one decoder isometry with its exact
  law, promise accuracy `1-η`, logical cap `n*k`, and physical continuation of
  cap `n*k + next.queryCap`. Comparator accepted it.

No negative controls were authored for these two bundles. The other public
endpoints passed the type and axiom audit but were not compared:
`finalB_physical_on_embedding`, `forr_walsh_physical`,
`forr_walsh_tensor_physical` and `P_runs_sharp`.

Still unproved in Lean, as the return's `LEAN_GAPS.md` states:

- The basis change from a general fixed projector to the coordinate predicate.
- The literal flag/Hadamard identification of `H·ψ` with `α0|0⟩+α1|1⟩`.
- Equality between the decoder's existential isometry and threshold
  postprocessing of the separately exposed tensor witness.
- The constant 126. The maintained 138 budget is unchanged, and no consumer
  is rewired to the sharper compiler.

## Return 08: zero-search successor candidate

`QuarticQuery.zero_search_sum_successor` was placed at
`LowerBound/Planted/ZeroSearchSuccessor.lean` byte-for-byte. It built on the
first attempt and depends only on the standard three axioms. It proves, for
every finite set `U` of planted indices:

`(|U| + 1) · Σ_{j∈U} [e j ∈ path(x_j)] ≤ 2 · Σ_{j∈U} #{queried coordinates in the planted block on path(x_j)}`

No probability wrapper derives `2G/[m(m+1)]` from it, and no Comparator bundle
or corpus tie was added.

## Native validation and receipts

The final run of [round4_formal.py](../../tools/return_checks/round4_formal.py)
passed every operation on one frozen source inventory. It ran one targeted
build, six type and transitive-axiom audits, and ten dedicated comparisons:
six positive and four negative. Inputs were unchanged throughout. The
registered receipts are:

- [targeted build](../../corpus/receipts/lean-build-round4-targeted-2026-11-03T023317151864+0000.json)
- [05 endpoint](../../corpus/receipts/comparator-round4-realized-caps-external-2026-11-03T023317151864+0000.json) and [capped-premise control](../../corpus/receipts/comparator-round4-realized-caps-capped-premise-2026-11-03T023317151864+0000.json)
- [Degree](../../corpus/receipts/comparator-round4-degree-conventions-2026-11-03T023317151864+0000.json) and [missing-uniqueness control](../../corpus/receipts/comparator-round4-degree-missing-uniqueness-2026-11-03T023317151864+0000.json)
- [ModelZero](../../corpus/receipts/comparator-round4-model-zero-2026-11-03T023317151864+0000.json) and [classical-only control](../../corpus/receipts/comparator-round4-model-zero-classical-only-2026-11-03T023317151864+0000.json)
- [RealLeaves](../../corpus/receipts/comparator-round4-real-leaves-2026-11-03T023317151864+0000.json) and [zero-leaf control](../../corpus/receipts/comparator-round4-real-leaves-zero-only-2026-11-03T023317151864+0000.json)
- [uniform amplifier](../../corpus/receipts/comparator-round4-uniform-amplifier-2026-11-03T023317151864+0000.json)
- [sharp decoder](../../corpus/receipts/comparator-round4-decoder-sharp-2026-11-03T023317151864+0000.json)

Positive receipts carry `declaration_scope: configured_theorem_names_only`.
Comparator ran unsandboxed, the repository's documented local norm.

Adding Lean sources changes the global source fingerprint. Earlier receipts and
statement-review bindings therefore become stale. The root build, dependency
export, five baseline bundles and five baseline negative controls were rerun on
the integrated sources and all passed. Their receipts are timestamped
`2026-11-03T0323` to `T0333`. Statement reviews were not refreshed.

Theorem 1.1 previously had wrapper-mediated credit. That credit came from
historical receipts that listed names scanned from proof text. The refreshed
Unconditional receipt lists only its configured target, so the row now reads
`comparison_credit: none`. This is the documented credit policy applied to
fresh evidence. `tests/test_build_comparator_map.py` still pins the old value
and fails until it is updated. Comparator agreement shows that two statements match under the
same definitions. It is not a review of whether those definitions model the
paper, and no human expert review is claimed.
