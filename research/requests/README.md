# Review and writing requests

These are authored packet instructions, organised by the work requested.
They are plans for a reviewer or writer, not evidence that the work succeeded.

| Campaign | Requests | Builder |
| --- | --- | --- |
| [review/](review/) | Paper audit, literature review and formalisation design. The original responses are preserved under [returns/](../returns/README.md). | [build_research_packets.py](../../tools/build_research_packets.py) |
| [funnel/](funnel/) | Long reasoning record, short expert paper, examples-first exposition, Forrelation route note, reader and film plan. | [build_funnel_packets.py](../../tools/build_funnel_packets.py) |
| [round2/](round2/) | Statement-fidelity audit; Lean for Sections 1–2, Section 3, Sections 4–5 and Appendix A; sharp uniform Forrelation bound; single-family exponent. Each packet carries the first-round returns, their adjudication and the annexed literature. | [build_round2_packets.py](../../tools/build_round2_packets.py) |
| [round3/](round3/SELECTION.md) | Eight focused long-record sections, an evidence-backend task and a baseline review. Final synthesis follows the actual section returns. | [build_round3_packets.py](../../tools/build_round3_packets.py) |
| [round4/](round4/SELECTION.md) | Seven substantial jobs after the integrated-record review: short and examples-first papers, quantum and classical completion, whole-corpus fidelity, the publication backend, and adversarial mathematical/reader review. | [build_round4_packets.py](../../tools/build_round4_packets.py) |
| [round5/](round5/SELECTION.md) | Five critique jobs on the current expert companion, exposition and long record: expert referee, quantum mechanism, classical mechanism, student exposition and long-record navigation. Referees return located findings, not rewrites. | [build_round5_packets.py](../../tools/build_round5_packets.py) |

Each campaign owns its `common.md`, `boundaries.md` and numbered job files.
The numbers identify packets within that campaign; retain those names when
revising a request. `common.md` includes `{title}`, `{job}` and `{boundary}` once
each. Builders combine these sources into each ZIP's `READ_ME_FIRST.md`.

Edit the sources here and rebuild. Do not edit an already generated ZIP as if it
were the source. Commands and external-input requirements live in the
[maintenance guide](../../tools/README.md).

[Round nine](round9/SELECTION.md) has three improvement-only packets, one per
paper, with chronological sentence-level review, full round-eight feedback and
revision decisions, and fresh source-bound PDFs. Build with
[build_round9_packets.py](../../tools/build_round9_packets.py).
