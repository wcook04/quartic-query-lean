# Review and writing requests

These are authored packet instructions, organised by the work requested.
They are plans for a reviewer or writer, not evidence that the work succeeded.

| Campaign | Requests | Builder |
| --- | --- | --- |
| [review/](review/) | Paper audit, literature review and formalisation design. The original responses are preserved under [returns/](../returns/README.md). | [build_research_packets.py](../../tools/build_research_packets.py) |
| [funnel/](funnel/) | Long reasoning record, short expert paper, examples-first exposition, Forrelation route note, reader and film plan. | [build_funnel_packets.py](../../tools/build_funnel_packets.py) |
| [round2/](round2/) | Statement-fidelity audit; Lean for Sections 1–2, Section 3, Sections 4–5 and Appendix A; sharp uniform Forrelation bound; single-family exponent. Each packet carries the first-round returns, their adjudication and the annexed literature. | [build_round2_packets.py](../../tools/build_round2_packets.py) |
| [round3/](round3/SELECTION.md) | Eight focused long-record sections, an evidence-backend task and a baseline review. Final synthesis follows the actual section returns. | [build_round3_packets.py](../../tools/build_round3_packets.py) |

Each campaign owns its `common.md`, `boundaries.md` and numbered job files.
The numbers identify packets within that campaign; retain those names when
revising a request. `common.md` includes `{title}`, `{job}` and `{boundary}` once
each. Builders combine these sources into each ZIP's `READ_ME_FIRST.md`.

Edit the sources here and rebuild. Do not edit an already generated ZIP as if it
were the source. Commands and external-input requirements live in the
[maintenance guide](../../tools/README.md).
