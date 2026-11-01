# Research materials

The files in [intake/](intake/) record the initial investigation of OpenAI's
nearly quartic query-complexity separation. Start with the
[statement ledger](intake/statement_ledger.json), then read the
[ledger notes](intake/statement_ledger_notes.md) for the source locations,
interpretations, unresolved questions and proposed formalisation order.

These materials were prepared by AI agents and have not been independently
reviewed. A cited source, a proposed Lean statement and a successful proof check
are different kinds of evidence. The files record research and proposals;
they are not build receipts or proof certificates.

## Find the relevant files

| Subject | Files and role |
| --- | --- |
| Paper statements | [statement_ledger.json](intake/statement_ledger.json) contains the structured rows; [statement_ledger_notes.md](intake/statement_ledger_notes.md) explains the audit and proposed milestones. |
| References | [manuscript_references.txt](intake/manuscript_references.txt) records the bibliography; [references_resolved.json](intake/references_resolved.json) records source locations. |
| Public discussion | [commentary.json](intake/commentary.json) records discussion found during the initial research. |
| Classical Lean prior art | [prior_art_classical_lean.json](intake/prior_art_classical_lean.json) lists candidates; [prior_art_classical_lean_searches.json](intake/prior_art_classical_lean_searches.json) records the searches. |
| Quantum Lean prior art | [prior_art_quantum_lean.json](intake/prior_art_quantum_lean.json) lists candidates; [prior_art_quantum_lean_searches.json](intake/prior_art_quantum_lean_searches.json) records the searches. |
| Verification tools | [verification_tooling.md](intake/verification_tooling.md) and its [JSON companion](intake/verification_tooling.json) record researched tools, requirements and recommendations. |
| Organisation and reuse | [organisation_exemplars.md](intake/organisation_exemplars.md) surveys other Lean repositories; [internal_inheritance.md](intake/internal_inheritance.md) assesses possible reuse from related projects. |

The notes describe observations made during their research sessions. Version
recommendations, machine state and references to other checkouts may differ from
current development. Follow the cited source and pin before relying on a
recommendation. References to private or sibling checkouts do not make those
sources available in this clone.

## Build research ZIPs

[tools/build_research_packets.py](../tools/build_research_packets.py) prepares
three independent ZIPs: a paper audit, a literature review and a Lean/checking
plan. Each ZIP includes a research request, source files and a manifest of their
SHA-256 hashes. The builder checks the archived bytes against that manifest.

The original local defaults read papers and extracted text from sibling/private
checkouts, plus the current local Lean files. Those inputs are not supplied by
this repository. The [maintenance guide](../tools/README.md#build-research-packets)
lists them and shows how to supply alternative paths. With the inputs present:

```sh
python3 tools/build_research_packets.py --dest /path/to/output
```

The command builds three ZIPs and stops when a packet's required input is missing.
Producing a ZIP checks its packaging; it does not review the enclosed claims or
submit anything to an external service.

Return to the [repository overview](../README.md) for the local check command.
