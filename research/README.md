# Research materials

The files in [intake/](intake/) record the initial investigation of OpenAI's
nearly quartic query-complexity separation. Start with the
[statement ledger](intake/statement_ledger.json), then read the
[ledger notes](intake/statement_ledger_notes.md) for the source locations,
interpretations, unresolved questions and proposed formalisation order.

The source reviews, five writing returns and seven round-two returns are in
[returns/](returns/README.md). The first reviews have verdicts in the
[adjudication](adjudication/adjudication_notes.md); the round-two
[snapshot guide](returns/round2/README.md) identifies their preserved inputs.
The intake records
were prepared by AI agents and have not been independently reviewed by a person. A cited source, a proposed Lean statement and a successful proof check
are different kinds of evidence. The intake files record research and proposals;
they are not build receipts or proof certificates.

The ten [round-three returns](returns/round3/README.md) have source-specific
[integration decisions](adjudication/round3_integration.md), including the
[foundations review](adjudication/round3_foundations.md),
[construction review](adjudication/round3_construction.md),
[evidence backend](adjudication/round3_backend.md), and
[complete claim-appendix audit](adjudication/round3_appendix_audit.md).
The maintained manuscript is now [the long reasoning record](../docs/reasoning_record.md);
returned manuscript bytes remain unchanged.

[requests/](requests/README.md) holds the maintained instructions for further reviews.
The [packet builder](../tools/build_research_packets.py) combines these
instructions with source files for reviewers. The requests describe planned
checking; they do not establish that proofs have been checked.

## Folder responsibilities

| Folder | Role |
| --- | --- |
| [intake/](intake/) | Initial research and the original statement ledger, still an input to corpus generation. |
| [returns/](returns/README.md) | Preserved reviewer submissions, with their original filenames and manifests. |
| [adjudication/](adjudication/adjudication_notes.md) | Maintained verdicts and corrections in `adjudication.json`, with explanatory notes. |
| [requests/](requests/README.md) | Source review in `review/`, explanation and writing in `funnel/`, statement/Lean coverage in `round2/`, and focused long-record sections and evidence work in [round3](requests/round3/SELECTION.md). |

For current statement evidence, begin with the [corpus guide](../corpus/README.md).
The research files explain where the inputs and decisions came from.
Adjudication notes record the development at the time of that review; their
remarks about compilation or open hypotheses are historical. Use corpus
records and their receipts for current evidence.

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
three independent ZIPs, using these authored requests:

- [Understand and audit the paper](requests/review/1_understand_the_paper.md).
- [Ground every step in the literature](requests/review/2_ground_in_literature.md).
- [Plan full Lean and Comparator checking](requests/review/3_lean_and_comparator.md).

The [common template](requests/review/common.md) and [boundaries](requests/review/boundaries.md)
combine with each request to produce its `READ_ME_FIRST.md`. Edit these source
files rather than instructions inside a generated ZIP. Each ZIP also includes
source files and a manifest of their SHA-256 hashes. The builder checks the
archived bytes against that manifest.

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

## Writing and explanation requests

The [funnel campaign](requests/funnel/) contains five maintained requests:
[long reasoning record](requests/funnel/1_long_reasoning_record.md),
[short expert paper](requests/funnel/2_short_expert_paper.md),
[examples-first exposition](requests/funnel/3_examples_first_exposition.md),
[Forrelation route note](requests/funnel/4_forrelation_route_note.md), and
[reader and film plan](requests/funnel/5_reader_and_film.md). These are requested
deliverables, not completed publications. Use the
[writing-packet command](../tools/README.md#build-writing-packets) to package them.

The five funnel returns are in [returns/funnel/](returns/README.md#funnel-returns), with their
archive names and hashes. Their audit findings have verdicts in the
[funnel adjudication](adjudication/funnel_adjudication_notes.md), whose
[JSON](adjudication/funnel_adjudication.json) also lists the tie changes and the ties
proposed for later review.

The [round-three campaign](requests/round3/SELECTION.md) develops that long-record
baseline in eight focused mathematical sections, alongside a backend assignment
and a whole-baseline review. Each packet supplies selected primary literature,
Lean evidence and reusable writing guidance. Integration follows the actual
section returns; the short paper and frontend follow the integrated record.
Use the [round-three builder](../tools/build_round3_packets.py) and its
[maintenance instructions](../tools/README.md) to freeze and package those inputs.

## Path changes

The original five `requests/*.md` files now live under `requests/review/`.
The two `returns/adjudication*` files now live under `adjudication/`, separating
maintained decisions from submitted reviews. Their contents are unchanged.
Existing packet member names are retained by the builders, so packet instructions
and historical manifests continue to refer to the same archive paths.
