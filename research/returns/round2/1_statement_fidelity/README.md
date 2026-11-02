# Quartic statement-fidelity audit

Start with `fidelity_audit.md`. It gives the mathematical verdict, definition-by-definition comparisons, exact source locators, the dependency-extraction defect, model-transport analysis, Comparator limits, and independent small examples.

## Files

- `sanity_theorems.json`: proposed semantic checks in the existing Lean vocabulary, with known values, sources, and the errors they detect.
- `NEW_STATEMENTS.json`: registration of the new displayed claims and proposed wrappers. Every signature is unelaborated.
- `STATEMENT_CHANGES.json`: proposed corrections to evidence and documentation. No replacement of the headline mathematical theorem is proposed.
- `LEAN_GAPS.md`: evidence boundaries and next formal additions in report order.
- `correspondence.json`: exact anchored passage boundaries, statement IDs, and existing full Lean declaration names. A name here identifies a relevant existing definition or result; it does not claim a new proposed lemma is already proved.
- `references.bib`: primary sources. Its keys match the short citations in the audit.
- `negative_controls.json`: further adversarial controls; none was run through Comparator in this audit.
- `READ_SCOPE.md` and `source_read_scope.json`: what was read, what was sampled, and what was unavailable.
- `checks/`: independent executable diagnostics, their outputs, the unelaborated private-wrapper fixture, and package validation.

## Reproduce the finite checks

Run each command from this extracted directory:

```sh
python -I checks/check_classical_small.py
python -I checks/check_construction.py
python -I checks/check_reach_private.py
python -I checks/validate_return.py
```

The first two scripts use exact arithmetic and finite enumeration. The third demonstrates a name-filtering bug on a synthetic dependency graph. They require only the Python standard library and write their result JSON beside the scripts. None runs Lean or accesses the network.

`checks/check_packet_integrity.py /absolute/path/to/extracted/input` optionally checks the supplied input manifest and selected source/graph observations. It reads the original archive extraction; it does not modify it. The original papers and full source archive have not been redistributed in this return.

## Evidence status

No Lean, Lake, Comparator, or external kernel was executed. Historical execution claims remain attributed to the supplied records. The current unconditional source is present. The new source audit finds no mis-encoding of the main definitions on their intended range, and finds a definite flaw in the dependency-reporting script. The report distinguishes these conclusions.
