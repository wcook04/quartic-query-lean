# Recorded focused native extractions

Native reports (schema 2), raw graphs and selected graphs (schema 1.1), and the
compact actual inspection outputs are copied byte-exact. Build receipts use the
native adapter's public projection. CLI receipts are recorded projections:
they preserve executed commands, exit status and full-output hashes while
omitting verbose diagnostic text. Original local receipts remain separately
hash-bound in the [formal adjudication](../../../research/adjudication/round3_formal.json).

All three reports have `scope_complete=true` for their selected local modules.
Each overall graph has `extraction_status=partial`: dependencies outside that
scope remain explicit boundaries, including Mathlib, Init and Batteries.
The reports retain the exact defining module for each boundary. These recorded
native outputs are separate from the main informal corpus graph. They establish
local process observations, not human review, paper fidelity or a fresh-clone build.

| Case | Native report | Graph | Selected graph | Actual inspection | Build projection | CLI receipts |
| --- | --- | --- | --- | --- | --- | --- |
| eq19 | [report](eq19-report.json) | [graph](eq19-graph.json) | [selected](eq19-selected.json) | [inspection](eq19-inspection.json) | [build](eq19-build.json) | [CLI](eq19-views.json), [stored replay](eq19-stored-views.json) |
| eq19-independent | [report](eq19-independent-report.json) | [graph](eq19-independent-graph.json) | [selected](eq19-independent-selected.json) | [inspection](eq19-independent-inspection.json) | [build](eq19-independent-build.json) | [CLI](eq19-independent-views.json), [stored replay](eq19-independent-stored-views.json) |
| semantics | [report](semantics-report.json) | [graph](semantics-graph.json) | [selected](semantics-selected.json) | [inspection](semantics-inspection.json) | [build](semantics-build.json) | [CLI](semantics-views.json), [stored replay](semantics-stored-views.json) |
