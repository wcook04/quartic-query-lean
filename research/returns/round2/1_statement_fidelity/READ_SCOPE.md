# Reading and verification scope

This is a collective source-level audit of statement meaning, supported by independent finite computations and selected primary-literature comparisons. All proposed Lean statements and the regression fixture are **unelaborated**. We did not run Lean, Lake, Comparator or the external kernels. Historical successful-run reports remain evidence of reported runs, subject to the provenance and staleness qualifications in the audit.

Paths below refer to the supplied archive root. `source_read_scope.json` lists exact reviewed filenames, scopes and source hashes. Hashes identify the reviewed bytes; they do not certify the mathematics.

## Read in full

The team read the complete `paper/extracted.md`, `READ_ME_FIRST.md`, `BUILD_STATUS.md`, `repository/README.md`, `repository/docs/statement_evidence_contract.md`, `repository/corpus/README.md`, the earlier `repository/docs/statement_fidelity_review.md`, both readable adjudication-note files, and `repository/research/adjudication/bansal_sinha_section54_second_reading.md`.

The core source review covered all of `repository/lean/QuarticQuery/Statement.lean`, its public model definitions, and these complete modules:

- `Model/Classical.lean` and `Model/Quantum.lean`;
- `Bridge/DecisionTree.lean`, `Bridge/Oracle.lean`, `Bridge/Deferred.lean`, and `Appendix/TheoremA1.lean`;
- `Construction/Winner.lean`, `Construction/Transcript.lean`, and `Construction/LocalTests.lean`;
- `Forrelation/Walsh.lean`, `Product.lean`, `Promise.lean`, `Sanity.lean`, `Builder.lean`, `Arithmetic.lean`, `Circuit.lean`, and `Repetition.lean`;
- `LowerBound/Minimax.lean`, `LowerBound/Planted/Inputs.lean`, `Tournament/Drift.lean`, and `Tournament/Ideal.lean`;
- all four `Results/` modules and `Paper/Section2.lean`.

These module paths share the prefix `repository/lean/QuarticQuery/`. Reading `Paper/Section2.lean` does not alter its recorded uncompiled status.

The root import file `repository/lean/QuarticQuery.lean`, toolchain and Lake configuration/manifest, and `repository/lean/scripts/Reach.lean` were read. The supplied complexitylib `Quantum/Search.lean`, `Quantum/Polynomial.lean`, and `Quantum/Adversary.lean` were read in full under `complexitylib/Complexity/Computability/QueryComplexity/`.

All five positive Comparator bundles' solutions and configurations and all five negative controls were reviewed. The complete copied definition blocks in the five `Challenge.lean` files were mechanically diffed against the fully read public statement file, and the theorem statements were inspected. This is source comparison; acceptance was not rerun.

All four supplied writing guides were read across the team: `writing/the-deliverable.md`, `writing/mathematical-writing-mechanics.md`, `writing/full-exposition-guide.md`, and `writing/register-from-literature.md`. The full exposition guide was read through physical line 1597. The three prose exemplars were sampled for form only.

## Selected source and literature review

`ForrelationLower/Main.lean` was inspected collectively over physical lines 1–240 and 340–end, including the endpoint and hypotheses. `ForrelationLower/Uniform.lean` was inspected over lines 1–90 and 295–end. These were not complete renewed audits of their analytic proofs. Selected `ForrelationLower/Promise.lean` passages checked the Phi correspondence and moment statements. Selected passages of `Upper/Tournament.lean`, `Upper/Columns.lean`, `Upper/Verify.lean`, and `Paper/Section3.lean` checked the explicit probability-range assumptions and their actual use.

The corpus JSON was parsed and selected records were read closely for definitions, construction, bridges, exponent quantifiers, Appendix correspondence and provenance. The evidence graph and stored dependency graph were inspected for relevant status, edge and traversal claims. We do not claim a renewed proof of every corpus row or examination of every dependency.

The primary-literature checks were targeted: Buhrman–de Wolf §§3.1–3.3 for the query models; Bansal–Sinha definitions and Theorem 1.3/Corollary 1.4 from the supplied TeX, plus the disputed Section 5.4 display; selected cheat-sheet construction context; the ABKRT degree/query theorem chain; Beals et al.'s two-bit parity passage and its expected-query convention; selected de Wolf lecture-note passages on measurement, oracle access and deferred measurement; and Špalek–Szegedy's definition and Theorem 3.1. Exact ranges and archive members appear in the JSON. Complete proofs of these external papers were not audited. The publisher PDF was visually checked at the adversary-bound denominator; no page-by-page visual audit of the preprint PDF is claimed.

## Context, computations and archive integrity

The separately attached historical transcript `Pasted text(20261102-145932).txt` was covered across the team: physical lines 1–1800 and 2437–end by the lead reviewer, and 1801–2436 by the quantum reviewer. This was a **historical contextual skim**, not a proof audit. Its embedded commands and historical reports did not authorize execution or replace current source evidence. The earlier returns were consulted selectively through the current adjudications; no full rereading of all first-round material is claimed.

The independent Python checks cover small classical complexities, exact Forrelation/promise examples, toy board mutations, and the static private-helper reachability defect. Their scripts and outputs are in `checks/`. Finite computations and source inspection do not establish elaboration of the proposed Lean signatures.

All **356 manifest entries**, representing **356 distinct listed paths**, were independently checked for presence, byte size and SHA-256. All passed: zero missing files, zero size mismatches and zero hash mismatches. There are **358 extracted files**; only `READ_ME_FIRST.md` and `manifest.json` are unlisted. This is archive-integrity verification. It is not a claim to have read all 358 files.

## Unavailable evidence and explicit limits

The supplied archive lacks raw `repository/corpus/receipts/` material and compiled `.olean` objects. Lean and Lake were unavailable on the audit environment's PATH. We did not reproduce a clean source checkout, inspect Git history, run a build, replay Comparator or rerun an external kernel.

Two relevant imported files were absent: `complexitylib/Complexity/Foundations/Quantum/Measurement.lean` and `complexitylib/Complexity/Computability/DecisionTree/Basic.lean`. Attempts to retrieve both at pinned revision `62ca5c21461b2482e8bd12b7cb9b4937d887a33a` failed through the available public retrieval routes. Their complete implementations were therefore not read.

There is no claim of a full Mathlib, CSLib or complexitylib source-closure audit; a complete tactic-by-tactic proof review; or examination of every implementation file in `Upper/`, `LowerBound/` and `ForrelationLower/`. Negative reachability labels affected by the private-helper traversal defect are not evidence that a declaration is unused. These limits are separate from the mathematical statement-fidelity conclusions reached on the inspected source.
