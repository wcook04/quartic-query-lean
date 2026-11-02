# Section 3: proposed exact Lean statements

The main proposed result is `QuarticQuery.Paper.quantumTournament`: one coherent
circuit whose measured label is a list of at most the prescribed number of
candidates, with the exact success guarantee of Proposition 3.2 and an explicit
physical bit-query bound. The source also supplies the full tensor preparation
in equation (15), a common-workspace construction for the actual comparison
interface, bounded coherent amplification, and exact comparison, decoding,
verification and error statements.

**All new Lean source is UNELABORATED.** This environment has no Lean, Lake or
elan executable and no supplied compiled dependency artifacts. No new theorem
is claimed to compile, no Comparator run was performed, and no new headline
dependency or independently checked status is asserted. The original source
tree was used for reading only. This is an advisory package for integration
and review.

## Start here

Read `blueprint.md` for the mathematical explanation and the entry for each
assigned statement. It leads with Proposition 3.2, then amplification,
comparison and verification, the error bound, and the remaining displays and
definitions. Each entry gives its class, mathematical statement, unelaborated
Lean signature, exact declaration dependencies and correspondence qualifications.

`SOURCE_AUDIT.md` identifies the earlier results that need citation and the
scope of the public-source checks. `LEAN_GAPS.md` records what compilation
and statement review must still establish. No change to an original Section 3
statement is proposed; `STATEMENT_CHANGES.json` is empty. The separate
`EVIDENCE_CORRECTIONS.json` records changes to evidence mappings and interfaces.

## Source layout

| Module | Purpose |
| --- | --- |
| `QuantumAmplification` | Grover-state and trial agreements; bounded charged product; coherent amplification; controlled access and compilation wrappers. |
| `QuantumWorkspace` | One common finite workspace, origin and output map for a finite family of coherent samplers. |
| `QuantumTensor` | Literal fresh-register tensor state, product success masses, positive-event conditional law and composed sampler. |
| `QuantumTournament` | Finite bounded-list output type, probability law, perfect-indicator coupling and coherent list circuit. |
| `QuantumTournamentFacts` | Drift, surviving weight, normalized stage law, explicit cost and final Proposition 3.2 statement. |
| `QuantumComparison` | Actual decoder/comparison/verification procedures, explicit physical caps, winner dominance and final Boolean error. |
| `QuantumUpper` | Aggregate import for the proposed modules. |

All modules are under `lean/QuarticQuery/Paper/` and use namespace
`QuarticQuery.Paper`. The aggregate does not import the earlier unbuilt
`Paper.Section3` candidate. This ZIP contains no replacement dependency sources.

## Integration and validation

Use the supplied repository's pinned environment:

| Component | Required pin from the supplied manifest |
| --- | --- |
| Lean | `leanprover/lean4:v4.36.0-rc2` |
| complexitylib | `62ca5c21461b2482e8bd12b7cb9b4937d887a33a` |
| Mathlib | `69552756cd8a2d2d48763cf7279fd814d6a1224d` |
| cslib | `254e30e6d4299c51323aaeaf5f51a4763b375d4a` |

Place the proposed files at their module paths in an isolated integration
checkout. Build `QuarticQuery.Paper.QuantumUpper` through the owner's normal
guarded Lake workflow, retaining the exact source revision and command in a
fresh receipt. After the module build, `checks/lean_checks.lean` provides
targeted `#check` and `#print axioms` commands for the main interfaces. It has
not been run here. Then review the paper-to-statement ties, including output
type, quantifier order, positive conditioning events, query units and the
alternative implementation routes. Update evidence flags only after those
steps succeed.

The supplied historical build and Comparator records remain historical
evidence. `LEAN_GAPS.md` preserves the accepted warning about a dirty-tree
receipt and its source revision. This package does not silently replace that
record with a clean-build claim.

## Checks performed here

`checks/section3_checks.py` was executed using Python 3.12.14 and NumPy 2.3.5.
Its exact-rational tests cover drift and small complete list laws, including
fractional and cyclic comparisons, history-dependent failure, zero total weight,
and termination after a winner is sampled. Numerical tests cover complex-vector
Grover iteration, the displayed averaging inequality and the explicit cost.
Two expected negative controls show the role of complementarity and demonstrate
that a full tensor state can differ from a short-circuit state with the same
successful law. Results and deterministic seed are recorded in
`checks/mathematical_checks.json`.

`checks/validate_bundle.py` checks the requested statement IDs, metadata fields,
source-signature snapshots, correspondence anchors, import paths, declaration
documentation, admission tokens and the file manifest. Its receipt is
`checks/static_validation.json`. These checks detect packaging and finite-example
errors. They do not elaborate Lean or establish universal mathematical truth.

## Evidence files

| File | Contents |
| --- | --- |
| `coverage_plan.json` | One entry per assigned statement, with `compiled: false` throughout. |
| `NEW_STATEMENTS.json` | Auxiliary statements and exact proposed signatures, including required typeclass context. |
| `STATEMENT_CHANGES.json` | Empty; no manuscript theorem is changed. |
| `correspondence.json` | Passage anchors and exact text boundaries for the blueprint. |
| `EVIDENCE_CORRECTIONS.json` | Located correspondence and interface repairs. |
| `declaration_manifest.json` | Source paths and unelaborated signature snapshots. |
| `source_manifest.json` | Input hashes, source hashes, dependency pins and verification status. |
| `READ_SCOPE.json` | Complete and partial reading scopes, unavailable resources and independent source reviews. |
| `references.json` | Primary-source URLs, versions, locators and citation roles. |

