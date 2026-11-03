# Round-five selection: five critique packets

Round five asks five independent outside referees to critique the current expert companion (`docs/expert_companion.md`) and examples-first exposition (`docs/exposition.md`), and the long record they link into. Referees return located findings and a short verdict; they do not rewrite. Each referee reads as the researchers whose papers the drafts cite would read, using the supplied literature to check credit and to learn how the field writes.

| Job | Lens |
| --- | --- |
| [expert_referee_short](expert_referee_short.md) | The short paper as a referee: main point, attention, history and credit, the statement appendix. |
| [quantum_mechanism](quantum_mechanism.md) | The quantum upper bound in both papers against amplification, search and tournament literature. |
| [classical_mechanism](classical_mechanism.md) | The randomized lower bound in both papers against direct-product, minimax and Forrelation lower-bound literature. |
| [exposition_for_students](exposition_for_students.md) | Whether a strong student could learn the result from the exposition. |
| [long_record_navigation](long_record_navigation.md) | The long record as the destination of the short paper's links, and its claims-to-Lean evidence. |

Every job also reviews the Lean-linking layer. [common.md](common.md) gives the shared reader principles, a neutral summary of the earlier editorial findings and the return format; [boundaries.md](boundaries.md) limits the work to critique of what exists.

Every packet contains the current drafts with their rendered PDFs, the long record with its PDF, the preprint, the Comparator statement, solution, configuration and map, the long-short-expository exemplars about another theorem, and job-specific literature. The long-record job also contains the record's own link targets. Packets name no individual reader and include no correspondence or transcripts; the private session attachment and the earlier editorial review file are excluded, the latter replaced by the summary in `common.md`.

The drafts are unreviewed working drafts. No acceptance gate applies: the record was edited after its accepted review and the corpus was regenerated. Instead `SOURCE_STATUS.json` binds each packet to the exact current bytes by SHA-256, and the build fails if any input changes during packaging. The rendered draft PDFs are external inputs passed by explicit path. Use [the round-five builder](../../../tools/build_round5_packets.py); output goes to a new directory outside the checkout and never overwrites an earlier batch.
