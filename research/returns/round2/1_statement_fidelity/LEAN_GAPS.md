# Lean evidence boundaries and proposed additions

All signatures in this return are **unelaborated**. No Lean, Lake, Comparator, or external kernel was run. A proposed signature without a body is an interface for later formalization, not a checked Lean file. The separate `checks/ReachPrivateFixture.lean` is also unelaborated. The Python programs test exact finite mathematics or an algorithmic dependency pattern; they do not establish Lean proof acceptance.

This list follows the reading order of `fidelity_audit.md`. Existing declarations are identified to avoid relabeling a specialization as a missing theorem. Historical build claims are preserved as reported evidence, with the source-currentness qualifications in section13 of the audit.

## 1. Classical minima and zero-query behavior

Source already contains read-all witnesses, nonemptiness, attainment, and `R_le_iff`/`D_le_iff`. These are not gaps. The explicit support-nonemptiness, total-mass, per-support-tree depth, constant-promise, and zero-query characterization wrappers in the sanity list make the intended semantics easy to test independently.

Relevant proposals: `sanity-randomized-support-nonempty`, `sanity-randomized-mass`, `sanity-randomized-full-support-cap`, `sanity-constant-classical`, `sanity-empty-promise-classical`, `sanity-empty-coordinates-classical`, `sanity-one-label-promise-classical`, `sanity-R-zero-characterization`, `sanity-D-zero-characterization`. They depend only on the elementary public model and its existing minimum results. A local normalized-mass argument in the new `ForrelationLower/Uniform.lean` is source text with no compilation evidence in this archive.

## 2. Quantum model

`AdaptiveProgram.outputMass_true_add_false`, `bitOracle_ket`, `QLe_Q`, and the exact decision-tree compilation are already present. `sf-q-mass-conservation` and `sf-q-oracle-basis` are displayed specializations of existing results, with new unelaborated wrappers only.

The genuinely useful exposed additions are `sf-q-zero-input-independent`, `sf-q-zero-iff-constant`, `sf-q-classical-random-simulation`, and `sf-q-bitruns-representable`. The first two make the zero-query lower bound explicit. The third gives same-cost finite randomized simulation, hence the conventional `Q≤R` relation; the source already has `Q≤D`. The last is the elementary reverse encoding of fixed sequences with a final binary coordinate measurement. There is no separately defined imported minimum `Q` to which one could simply assert an existing equality.

These additions are semantic checks and useful interfaces. The already-present adaptive-to-fixed conversion suffices for the imported per-algorithm quartic bound. A theorem encompassing all POVMs would require a separate finite-dimensional dilation statement and is not asserted to be formalized here.

## 3. Forrelation normalization and all three promise statuses

The source already proves positivity of the denominator, the exact integer/real promise equivalences, orthogonality of the normalized Walsh matrix, and the matrix-product formula for positive `k`. Their absence is not a gap.

The new general statement `sf-forrelation-three-statuses` has an elementary proof in section5.1 of the audit, using all-one interior blocks, a balanced character, and the tensor product of the two-bit Walsh eigenvector. A Lean proof needs the corresponding tensor or coordinatewise Walsh identity and the conversion of sign vectors to Boolean inputs. Finite checks at several parameters do not replace that proof.

`sf-phi-zero-layers` explicitly tests the public `k=0` extension. It guards the positive-layer hypothesis of `Phi_eq_matrix_product`. `sf-phi-positive-two-one` and `sf-phi-zero-two-one` are exact named finite witnesses.

## 4. Circuit and physical-layout checks

Canonical circuit evaluation and unique consistency are already proved independently of `CircuitRealises`. The source's winner uniqueness and local-test equivalence are also present. The cardinality statement `sf-bitloc-cardinality` is new as a named regression check; its proof uses finite cardinalities of disjoint sums, products, and the opponent subtype.

`sf-Fkm-t-zero` and `sf-empty-promise-rejects` record harmless boundary behavior. They are outside the nontrivial eventual separation. `sf-Fkm-one-winner` instantiates the existing planted-input acceptance theorem at the actual `Fkm 2 1`, and `sf-Fkm-corrupt-active-transcript` uses uniqueness of the consistent transcript plus an all-zero competitor string. The corresponding proofs have not been elaborated.

## 5. The local-test coherent interface

`Paper/Section2.lean` is uncompiled. Its adaptive pointer-depth clause reflects the preprint accurately; the old ledger's fixed-support wording was wrong. Its coherent sampling clause handles a uniform index distribution, while the preprint allows supplied indices in superposition. The latter requires a stronger interface. Keep `lem-2.2.ii` partial where that exact coherent claim is intended. This does not erase the separate implemented upper-bound proof.

## 6. Tournament range assumptions

There is no omitted probability-range premise in the inspected use. `IsComparison` records equation(10); `UnitValued` supplies the range. Probability-dependent lemmas take it, and the concrete sampler proves it. The algebraic drift results need no range. No new theorem repair is requested for these facts.

## 7. Floors and literal equation(2)

The displayed asymptotic pair in section9.1 corresponds to existing ID `eq-2`, with a new literal signature `fidelity-literal-eq2`. The unconditional theorem currently packages the lower bound as `G<R`, with a natural logarithmic exponent whose positivity is not a separate field. `Gvalue_ge` supplies `c=1/400` for `t≥8`; increasing the exponent if necessary supplies positivity, and the actual witness already has exponent six. This is statement packaging around existing mathematics.

`sanity-L-zero-extension`, `sanity-L-first-positive-k2`, and `sanity-power-set-valid` expose arithmetic and infimum safeguards. The last specializes existing membership of four and the nonnegativity conjunct in `UniversalPower`. No empty-infimum proof gap was found.

## 8. Bridges and Appendix A

The displayed `D≤20736T^4` is the supplied imported theorem `Cslib.Quantum.complexity_le_mul_pow_four`, mapped to `thm-A.1`. It is an existing source result reached by an alternative route, not a new proposed theorem. The adaptive bridge preserves query count exactly. Its padding preserves output probabilities; it need not preserve the state of a finished branch.

The arbitrary-matrix adversary statement of `lem-A.2` remains partially covered. Deferred measurement addresses the model-conversion part, not the whole matrix lower bound. The two absent imported modules, `Complexity.Foundations.Quantum.Measurement` and `Complexity.Computability.DecisionTree.Basic`, prevent complete source review of the pinned imported closure. Public retrieval attempts failed; no claim is made about what those unavailable bytes contain beyond their visible uses.

## 9. Dependency extraction and Comparator

The private-helper issue is an algorithm repair, not a missing mathematical theorem. Compile the supplied fixture, import it into the exact environment used by the extractor, and require a complete path from public root through the private wrapper to public leaf. The current synthetic test reproduces the name-filter failure without executing Lean. A repaired traversal must be run before treating negative reachability labels as exhaustive.

The new controls in `negative_controls.json` are unexecuted Comparator proposals. Shared mutations require independently fixed semantic specifications; regenerating every expectation from the mutant definition would defeat the test. Existing five negative bundles and reported acceptances are not newly replayed evidence.

## 10. Literature corrections

The expected-cost convention in the Beals source, the annex's extra square root, the ABKRT numbering, and the Bansal–Sinha physical-line correction concern cited statements and evidence descriptions. They are in `STATEMENT_CHANGES.json` with that kind explicitly recorded. They are not new axioms or required replacements for the headline theorem.

The Bansal–Sinha §5.4 comparison is the already-adjudicated `claim-bs-to-L` issue. No repaired full uniform theorem is proposed here. The independent fixed-`k` proof already supplies the source endpoint.

## 11. Small exact complexities and finite diagnostics

The OR₂, XOR₂, identity and constant table is mapped to the corresponding sanity IDs. Classical upper/lower arguments are given in prose and exact-rational checks. Quantum XOR uses the standard one-query phase-kickback calculation; quantum OR uses a finite classical selector. The statements are unelaborated despite their elementary mathematical proofs.

The displayed scalar histogram is `sf-phi-two-one-histogram`. It was checked by exact rational enumeration and is proposed in existing vocabulary using `Nat.card`. The source already proves the coarser 104/48/104 promise census and the negative witness. The new conjunction wrapper `sf-existing-negative-witness` does not turn those existing facts into a missing proof.

The generic two-column board count is `sf-toy-board-census`, with a separate counting argument in section15.2. The exhaustive program checks every input and the active/inactive mutations. Its explicit Lean signature uses the two-gate circuit inline. It is distinct from the actual `Fkm 2 1` proposal, which has forty address bits.

## 12. Compilation boundary and order of work

The new signatures should first be implemented as small lemmas using the named existing declarations. Compile `Model/Classical.lean` at its supplied bytes; compile the four new targets explicitly; repair and test reachability; then regenerate the statement evidence. Preserve the reported historical results separately. There is no new compilation receipt in this return.
