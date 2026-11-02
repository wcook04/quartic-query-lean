# Nearly quartic query separation: Lean and Comparator design return

Prepared 1 November 2026 for packet `3_lean_and_comparator`.

## Recommendation

Keep the attached Lean 4.36.0-rc2 / complexitylib dependency line. Make a compact,
concrete, Mathlib-only definition layer the public mathematical interface. Use
complexitylib for the classical models and the known quartic upper-bound route;
port the relevant amplitude-amplification results from
`troyjlee/quantum-query-complexity` behind explicitly proved model bridges. Prove
the new addressed-certificate construction and its classical and quantum
analyses against that interface. Keep the Bansal-Sinha lower bound as an explicit
theorem parameter until a matching formal proof is available.

This is a substantial formalisation project. It has useful, independently
checkable intermediate results. Existing source significantly reduces the
infrastructure burden, but it does not make a complete proof of the paper a
small wrapper around one imported theorem.

## Read in this order

1. `research_findings.md`: decisions, corrections to the intake, mathematical
   issues, and why they matter.
2. `model_decision.md`: comparison of the four requested quantum models,
   dependency versions, licences, and the exact bridge directions.
3. `core_definitions.lean`: concrete proposed definitions of total/partial
   Boolean functions, R, Q, bit queries, Forrelation, transcripts, and F.
4. `signature_glossary.md`, then `formalisation_plan.json`: all 118 original
   ledger IDs, with statement drafts, dependencies, source declarations, line
   ranges, difficulty and route.
5. `comparator_design.md`, then `milestones.md`: statement identity,
   conditionality, negative controls and preparation requirements.

`new_prior_art.json` retains the keys of the input quantum-prior-art format.
It includes newly found work and source-checked corrections to important
existing entries. `source_findings.md`, `tooling_findings.md`,
`ledger_audit_findings.md` and the source receipts give the underlying evidence.

## The most important corrections

- **A pointer test has small query depth, not small fixed support.** The original
  `lem-2.2.i` ledger wording is too strong. Reading an address and then its target
  takes `ell+1` queries, although every target bit can matter globally. The new
  plan repairs the statement rather than proving the wrong junta claim.
- **complexitylib supports arbitrary finite workspace.** The intake's description
  as a trivial-workspace model is incorrect. Its relevant theorems are stated
  per algorithm; a minimum-Q wrapper and its attainment/bridge proofs remain.
- **Partial quantum query semantics already have useful prior art.** Troy Lee's
  development permits a semantic input domain and read function, has native/XOR
  simulation results, and has exact conditional-law amplification. The concrete
  domain and observational determinacy still have to be instantiated correctly.
- **An imported final theorem does not verify every intermediate paper claim.**
  The known `D <= 20736 T^4` route can close the universal upper bound after
  transport. It does not by itself close the general spectral-adversary lemma
  or all of the appendix's proof steps.
- **Conditionality is not detected by the axiom list alone.** A theorem with an
  explicit mathematical premise can use only Lean's three standard axioms.
  Record its remaining mathematical premises as a separate field.
- **complexitylib is not an approved Palomar Challenge dependency at the checked
  policy revision.** The approved CSLib root is a different repository. Use the
  compact public definition layer on the Challenge side and the larger proof
  libraries on the Solution side.

## Status of this return

The research, source inspection, mathematical review, per-row plan and finite
checks were completed. The Lean file is **unbuilt**. Its definitions are
substantive drafts with an explicit list of theorem obligations; it contains
no asserted proof of the separation. The JSON statement strings are schematic
signatures, not 118 elaborated Lean declarations.

No Lean compiler, Lake or Elan executable was available in this workspace.
Consequently no new Lean build, Comparator run, independent-kernel replay or
Palomar acceptance is claimed. The historical trace ends with its last Lean
build still running; it supplies no later success receipt.

The input's 14 manifest members were checked byte-for-byte against their stated
lengths and SHA-256 hashes; all matched. Small exact finite checks cover the
Forrelation threshold conversion, tournament drift/evolution, and capped
product examples. Those computations are diagnostic checks, not proofs for all
parameters. The final validation report separately records structural checks
of this return.

## Evidence and source identity

The copied `paper/` files and `corpus/statement_ledger.json` are unchanged input
sources. The ledger is retained to preserve original IDs and provenance; its
claims are superseded where the returned plan explicitly records a correction.
The paper SHA-256 is
`a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`.
The input's OpenAI commit shorthand is `4eaee875`; full source pins for inspected
code are recorded separately. This advisory return does not upgrade any
historical claim of successful compilation or independent review.

For citations use the exact declaration and pinned URL in each `reuse` record,
the source lists in the design documents, and the page/equation/line locations
in the original paper. Search snippets and old AI summaries are leads, not
evidence of a usable theorem. Search limitations are explicit: absence from the
inspected sources is not proof that no formalisation exists anywhere.

## Intended completion criterion

The final unconditional claim is that the optimal **universal exponent** is
four. For each fixed `k >= 2`, the constructed family has the quantitative
near-quartic bounds from the manuscript. It is not a claim of an exact
fourth-power family with logarithms removed, nor permission to let `k` vary
silently with `m`. First deliver a precisely labelled conditional result;
remove each premise with a proof; retain the same frozen public definitions
and verify the statement identity after every change.

All work here is advisory preparation. The source repository, accounts and
mailboxes were not modified, and no submission or registration was made.
