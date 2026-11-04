# Round-nine production notes

The manuscript baseline is `9c5c5a2`, with the round-eight revisions at
`b8db532`. Both were pushed before this campaign. No paper mathematics or Lean
source changed in packet preparation. The native renderers produced fresh PDFs
of the same 16-page expert companion, 21-page exposition and 132-page record.
The packet builder requires their native receipts and checks PDF bytes, current
manuscripts and renderer inputs before packaging. Visual review is separate.

The writing-method source is the merged `lean-exposition` main revision
`7edf75412ff12d72d20074252f05843e4c3aa677`, verified against its remote main.
It was exported to a task-owned directory; unrelated working checkouts were not
changed. The default sibling checkout was an older branch lacking the register
module. Selecting the verified main export fixed that prerequisite mismatch.
All five transition/register skills, their index, register-stage guide and
current generated measurements are supplied, with the directly referenced
authoring/transfer guides, critique template and sanitized rule data. The local
writing method carries round-eight refinements and the new chronological review.
Optional historical references in those guides may point outside the packet.

The new protocol makes first-encounter understanding explicit: sentence-level
coverage and reader-state logs precede thematic verification and prior-feedback
review. Findings contain specific improvement directions, not praise. Targets
of 200/250/400 findings do not excuse duplication or fabrication. The record
assignment includes all sections and appendices; reviewers must declare any
unfinished ranges. Multiple model perspectives are explicitly simulated.

Preparation caught an archive-relative protocol link that did not resolve from
its maintained request source. The protocol now has the same filename beside
the authored request and at the archive root; the request-link test covers it.
Native render-receipt tests reject stale PDF bytes, changed inputs, missing
bibliography binding for the short papers and interrupted renders. The record
uses inline references; its renderer's explicit inputs and imported layout are
checked according to its own receipt contract.

The independent packet checker, source freeze digest, embedded render bindings
and private-name checks apply to all three archives. Batch-specific archive
hashes and the source commit belong in the generated `batch-audit.json`, not in
this source note. Build outputs remain outside the repository. Preparing and
pushing the campaign does not send a packet to a reviewer or establish review,
comprehension, mathematical correctness or a new formal build.
