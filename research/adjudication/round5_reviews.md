# Round-five reviews and their integration

Five referee lenses reviewed the expert companion, the exposition and the long
reasoning record from the packet frozen at `752826a`; the long-record lens returned
twice from independent runs. The six returns are preserved under
[research/returns/round5/](../returns/round5/README.md). They contain 269 located
findings across the three documents, 68 of them points to keep. No referee found a
failure of the separation theorem; the corrections concern local mathematical
statements, attribution, explanation order and the routes from a claim to its proof
and its Lean statement.

## How the findings were handled

| Document | Findings | Fixed | Kept | Moved to the record | Already resolved | Packet only | Declined |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [Expert companion](round5_dispositions/expert_companion.json) | 115 | 77 | 31 | 3 | 0 | 4 | 0 |
| [Exposition](round5_dispositions/exposition.json) | 88 | 66 | 17 | 1 | 0 | 4 | 0 |
| [Reasoning record](round5_dispositions/reasoning_record.json) | 66 | 31 | 20 | 7 | 4 | 0 | 4 |

"Packet only" findings concern three figure sources missing from the packets; the
figures were in the repository, and the packet builder dropped them because their
captions contain square brackets. "Already resolved" findings concern the record PDF
in the packets, which predated the renderer repair of `901190e`; a fresh render has
293 working internal links and no file actions. The four declined record findings
keep the byte-matched catalogue quotations and decline new figures; the reasons are
in the disposition file.

The corrections shared by several referees:

- A deterministic three-cycle is a fixed tournament. It defeats an ordering
  shortcut; the obstruction to bounded-error access is a comparison between losers
  with probability exactly $1/2$.
- Bansal and Sinha prove hardness of the explicit Forrelation problem;
  Sherstov, Storozhenko and Wu independently obtain the optimal partial separation
  through rorrelation.
- The tournament's ideal process is absorbing at zero weight, the algorithm stops
  and returns its list on sampler failure, and the per-stage failure bound holds
  only before the winner is listed.
- Reaching the true cell may be a lucky guess; the classical bound is on the joint
  event of a light column and a correct query, never on success conditional on a
  light column.
- The Lean direct product covers finitely many weighted seeds; arbitrary
  independent randomness is an ordinary reduction.

## Orientation and statement fidelity

Outside readers of AI-produced mathematics asked for two further properties, applied
to all three documents in this round. Each document now opens with the result, why
it matters, its key idea, what is new against the cited work and a map of what
follows. Each linked Lean statement is labelled the same as, stronger than or weaker
than the claim it is cited for. An [independent review of every cited
statement](round5_statement_fidelity.md) supplies those labels; it found that the
four compared theorems state exactly the claims, that $R$ and $Q$ are the standard
bounded-error worst-case measures, and that one earlier label misdescribed four
facts about winners as parts of Lemma 2.2. The papers follow it.

## Checks on the revision

- The [reworded record passages](round5_record_passage_audit.md) were audited for
  changes of meaning. Four regressions were found (a dropped "sufficiently large
  $m$", an overstated quotation of the preprint, direct comparison credit for
  unconfigured theorems, and a claim marker moved without its record) and corrected.
- The record correspondence was rebound with
  [rebind_record_passages.py](../../tools/rebind_record_passages.py): 253 passages
  moved, 36 reworded, 6 added, one claim moved
  ([report](round5_record_rebind.json)).
- The round-three dedicated comparisons were rerun on the integrated sources and
  passed, so Lemma 2.2, its two parts and Equation (19) are directly compared again.
  A paranoid run of the four headline theorems passed the same day.
- Three Lean source files still carry authoring comments calling them uncompiled;
  the current root-build receipt covers all three. The comments will be corrected
  with the next Lean change, since editing a Lean source invalidates every receipt.

These are reviews by AI referees, not human peer review.
