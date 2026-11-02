# Round-three job 09: independent semantics and evidence backend

This is the single advisory return for `quartic_r3_09_evidence_backend.zip`, dated 2 November 2026. Read **`evidence-path.md` first**. It contains the mathematical reasoning, evidence assessment, tested backend repair, exact limitations and integration order. The supplied repository and its canonical statement ledger were not modified.

## Status at delivery

| Work | Observed result |
|---|---|
| Input ZIP integrity | 400 payload members match the supplied manifest |
| Supplied current Lean/configuration snapshot | All 124 inputs match; 12 current receipts and 11 legacy-unbound receipts are distinguished |
| Backend repair | Patch applies cleanly; 44 Python tests passed, 2 native integrations skipped |
| Review migration | 477 historical authored judgments become explicitly unbound; build/comparison facts remain visible |
| Independent finite arithmetic | Existing seven mutation controls passed; new exact-rational independence control passed |
| New actual-definition Lean semantics | Complete proposed files, **uncompiled** |
| Full equation-(19) theorem and independent challenge | Complete proposed files/configurations, **uncompiled and un-compared** |
| Native `lean-exposition extract --build` | Actual launch attempted; exit 127, executable missing; **endpoint incomplete** |

A source-current supplied receipt is evidence about the recorded run with matching input bytes. It is not a fresh native run here. A prepared return is not acceptance of its proposed mathematics or code.

## Files and ownership

- `evidence-path.md`: main proof-forward contribution with stable passage anchors.
- `acceptance_cases.json`: unified case inventory; preserves execution type and status.
- `correspondence.json`: exact passage boundaries, statements, full proposed or supplied source types, premises, routes, citations and evidence limits.
- `NEW_STATEMENTS.json`, `STATEMENT_CHANGES.json`: seven explicitly derived semantic/sampling controls; no canonical statement edits.
- `LEAN_GAPS.md`, `review_notes.md`, `source_read_receipt.json`, `references.bib`, `STYLE_RULES.json`: open obligations, located corrections, reading scope, source editions and authoring receipt.
- `semantic/`: four requested actual-definition examples, independent witness and mutations, Comparator controls, runner and actual prerequisite/toy receipts.
- `eq19/`: full-conjunction wrapper, independently stated experiment and bridges, direct and independent Comparator configurations, repetition control and exact native extraction re-entry plan.
- `backend/`: the minimal unapplied patch, acceptance runner, before/after Python logs and actual in-memory corpus results. The patch has five owned paths; it does not introduce a second registry.
- `checks/`: reproducible source and finite-arithmetic audits, packaging checks and editorial review dispositions.
- `manifest.json`: exact sizes and SHA-256 hashes of all other payload members, plus source editions. The manifest excludes its own hash to avoid a self-reference.

Paths in retained historical receipts preserve the original execution environment. Paths in each sub-return's notes and configuration ledger are relative to that sub-return unless an explicit packet or project prefix is given. `acceptance_cases.json` records each component's base directory. Original packet members are not silently replaced by similarly named return files.

## Re-entry

1. Review and apply `backend/backend.patch` in a disposable copy of the supplied repository. Do not auto-generate review attestations for existing ties. The exact ordinary-premise and review-currentness distinctions are documented in the patch.
2. Restore Lean/Lake `leanprover/lean4:v4.36.0-rc2`, its pinned dependencies, and the complete matching `lean-exposition` distribution. Follow `eq19/reentry-plan.json` on the accepted unchanged equality target before adding new source files.
3. Copy the children of `semantic/lean/` and `eq19/overlay/lean/` into the disposable repository's `lean/` directory. Both overlays use existing libraries. Do not copy any receipt as though it certified this enlarged source snapshot.
4. Execute `semantic/run_semantics.py --project PROJECT/lean --output NEW_OUTPUT` and the equation-(19) steps in `eq19/reentry-plan.json`. The semantic runner delegates source binding to `PROJECT/tools/build_corpus.py`; it has no partial glob fallback.
5. Retain complete types, transitive axiom output, actual commands/versions/logs and before/after source hashes. A missing tool, import error or build failure does not pass a negative-control case. Record review bindings only after the complete current statement and semantic dependencies have been reviewed.

The unavailable attachment `Pasted text(20261102-190840-1).txt` was not read. This return is grounded in the supplied ZIP and the specifically identified official documentation.
