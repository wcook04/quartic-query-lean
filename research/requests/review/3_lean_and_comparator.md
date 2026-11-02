## Your job: formalisation design

We want to check the whole paper in Lean, with Comparator on each published statement, using as much existing work as possible. Read `lean/prior_art_*.json`, `lean/verification_tooling.md`, `lean/organisation_exemplars.md`, `lean/internal_inheritance.md` and the current Lean in `lean/current/`, which may not have compiled yet.

1. Find every further GitHub repository, Lean Zulip thread, Mathlib pull request or other formalisation we have missed, including work on Forrelation, Fourier growth, direct-product theorems, multiplicative weights, Dürr-Høyer, amplitude amplification, and Bansal-Sinha style lower bounds. Open the source before listing it, and pin a commit.
2. Compare the quantum models in `troyjlee/quantum-query-complexity`, `cslib-community/complexitylib`, `QudeLeap/Lean-QuantumAlg` and `openai/math` (`OAI.Computability.QuantumFactoring`). Recommend one model for this paper, or a bridge, and state the Lean signatures of the core definitions: total and partial Boolean functions, R, Q, the bit oracle, Forrelation P, and F_{k,m}.
3. For each row of `corpus/statement_ledger.json`, give a Lean statement draft, its dependencies, reusable declarations with exact names and commits, estimated size in lines, and difficulty.
4. Design the conditional route: which results enter first as named hypotheses, how to keep them out of Comparator's permitted axioms, and how to remove each one later. Forrelation's lower bound is the expected largest hypothesis.
5. Design the Comparator layout: Statement, Challenge and Solution modules, negative controls that must be rejected, and the exact Palomar preparation needs. We will prepare only; nothing is to be submitted.
6. Check the licences of everything recommended. Check Lean version compatibility; we are on `leanprover/lean4:v4.36.0-rc2` with complexitylib `62ca5c21`.

## Return one ZIP containing

- `new_prior_art.json`: same keys as `lean/prior_art_quantum_lean.json`.
- `model_decision.md`: the recommendation with its reasoning.
- `core_definitions.lean`: draft signatures. Mark it as unbuilt unless you built it.
- `formalisation_plan.json`: one row per ledger id with keys `id`, `lean_statement`, `depends_on`, `reuse`, `estimated_lines`, `difficulty`, `route` (`prove`, `import`, `hypothesis`).
- `comparator_design.md` and `milestones.md`: ordered milestones, each with a pass test.
