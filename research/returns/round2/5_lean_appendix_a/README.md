# Appendix A review and proposed Lean implementation

The return supplies a source map and proposed Lean proofs for the requested Appendix A rows, together with a second assembly of the universal quartic bound. The main candidate is `QuarticQuery.Paper.appendixA_D_le_Q_pow_four`, with coefficient 1500625. It uses the general adversary theorem for both A.3 applications and the genuine-face/recursive-matrix route for A.4. An optional hybrid uses the stronger polynomial block bound and has coefficient 19600.

**Every new Lean file is unelaborated.** No new Lean, Lake, Comparator or external-kernel run is claimed. Full proof bodies were written and reviewed against pinned source; finite computations provide supplemental checks. The existing coefficient 20736 and its historical evidence are preserved as a separate route.

Start with `blueprint.md`. It gives the library map, mathematical statements, exact proposed Lean signatures, proof plans, normalization and model checks, constants, and citations. `LEAN_GAPS.md` separates compilation gaps from local proof-route differences.

## Contents

- `lean/QuarticQuery/Paper/AppendixA*.lean`: proposed source modules, all under `QuarticQuery.Paper`, with `Ledger:` doc comments.
- `coverage_plan.json`: one entry per requested row; `class` is statement fidelity, and `compiled` is always false.
- `NEW_STATEMENTS.json` and `STATEMENT_CHANGES.json`: explicit numerical refinements, auxiliary displays and proposed statement changes, preserving original text.
- `correspondence.json`: exact passage anchors, excerpts and declaration names for the blueprint and supplementary mathematical notes.
- `references.bib`: edition-specific primary references and immutable software pins.
- `SOURCE_CORRECTIONS.json` and `SOURCE_COEFFICIENT_CHECK.md`: precise source-note corrections and the separate adversary-prefactor check.
- `assembly_plan.json`, `declaration_index.json` and `source_manifest.json`: the proposed assembly, source declaration inventory and content hashes. They are not compiled dependency data.
- `checks/` and `validation.json`: reproducible finite arithmetic checks and a static integrity checker, with results.
- `READING_LOG.md`, `ATTRIBUTION.md` and `LICENSE`: reading scope, code attribution and upstream licensing.

## Integration

Copy the returned module paths into the existing project at the revisions specified in `source_manifest.json`. The proposed build command, from the project's Lean directory, is:

```bash
lake build QuarticQuery.Paper.AppendixA
```

This command was not run here. Successful elaboration, compiled dependency extraction, axiom inspection and any independent Comparator challenge remain the team's next steps. The return is advisory; it does not modify the original project, publish a change or update historical evidence.
