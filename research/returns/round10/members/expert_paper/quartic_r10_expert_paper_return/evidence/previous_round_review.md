# Retrospective R9 and transcript audit

This audit began after the lead reviewer froze the independent chronological first pass. It examines historical decisions against the current expert manuscript and selected supporting passages. It does not replace the first-pass record or present resolved historical complaints as new findings.

## Custody and coverage

The three preserved R9 return archives contain 91 files in total: 28 expert, 24 exposition and 39 reasoning-record members. Their CRC tests pass, and their extracted and compatibility copies agree byte for byte. All 538 primary manuscript findings have exactly one recorded disposition: 166 expert, 135 exposition and 237 record findings. All 48 historical method observations have matching disposition identities. These are structural coverage results, not a claim that every decision is substantively justified.

The substantive reassessment covers all 166 original XP9 findings and decisions, all 58 expert-related historical cross-document observations and decisions, and nine supporting primary findings: RR9-014, RR9-129, RR9-133, RR9-149, RR9-152, RR9-157, RR9-211, EX9116 and EX9130. Of these 175 primary findings, 173 have their bounded original concern resolved or a defensible nonadoption; two remain unresolved in the narrow senses below. The 363 uninspected supporting primary IDs are individually enumerated in `../previous_round_audit.json`. Earlier-round IDs embedded in R9 reports are separate from R9 primary findings. The expert return's 87 older audit rows are also explicitly excluded from independent reassessment; earlier rounds are context rather than an additional assignment.

The current expert source was read in full, lines 1–478, as retrospective evidence, along with its bibliography. Supporting papers were read only at the listed dependency locations. The lead reviewer's current PDF observations settle the old page-one contribution, figure labels, Section 3 opening and two-clock paragraph layout questions. This reviewer did not independently render or visually inspect the PDFs.

## Challenges to recorded decisions

### XP9-149: the dated evidence and old source header remain unreconciled at the specialist's click

The decision is recorded as applied. Expert line 399 now distinguishes recorded build/axiom evidence from comparison evidence and links the fixed-circuit family theorem. However, the linked packaged `ConstructionFamily.lean` still begins, at lines 9–11, with the undated assertion “Status: unelaborated” and says no Lean or Lake executable was available in the authoring environment. The specialist companion does not explicitly identify that header as preparation-time history. Record Appendix G.4 describes the built and audited status; exposition line 494 explicitly reconciles the old preparation-time header with later evidence. Thus the original reader-facing status conflict is only partly repaired along the expert route.

This is a documentation and navigation issue, not evidence that the theorem failed to build. A concise historical qualification next to the expert link, or a dated clarification in the source header when the authors next revise it, would satisfy the remaining reader task. The current review does not claim a new Lean or Comparator execution.

### RR9-014: the historical arithmetic still uses an unnamed comparator

The record decision retains the motivation, reasoning that it already identifies the changed classical scale and stable quantum scale. At record line 152, the immediately preceding subject is the old cheat-sheet cubic construction; the next sentences say the new construction's classical lower bound “grows” to order mL while its quantum cost “stays” near square root of m. The current expert comparison at line 67 states matched-supplier costs: old quantum m and classical m²R(P), versus new quantum square root of m and classical mR(P). Under that comparison, both costs change, and the new classical bound is smaller at fixed supplier size.

The record may intend a different comparison, but it does not name one there. State the same two cost pairs or explicitly identify the baseline for “grows” and “stays.” This challenges the disposition of the motivational comparison, not the quartic theorem or the construction's actual bound. It is a short supporting-document dependency, not a second full record review.

## Disposition locator quality

Several preserved decisions have an exact substring at the reported current location but point to a different reader task. The repair often exists elsewhere. Examples include EX9130's old-status explanation (actual exposition line 494 rather than line 98), RR9-157's return from the completion-tree example (actual record line 3725 rather than 3667), and old cross-document XP094's free-information enumeration (expert line 287 rather than 285). The JSON remaps these cases and lists seven concrete locator defects. They support a methodological lesson: validate that a cited passage performs the assigned task, in addition to checking that its quoted substring exists. Locator defects are kept separate from new manuscript criticisms.

## Historical transcript and exact-edition boundary

The attached historical snapshot contains five sessions and 954 native items. Its five user messages and the relevant completion/build/link-rebinding items were inspected. It also contains 291 omitted-evidence objects reporting 4,688,521 omitted characters; those totals may overlap. This audit cannot reconstruct the omitted outputs, prove every historical test result or certify the prior remote environment. `attached_context_review.json` identifies the inspected native items and separates reported historical outcomes from present independent checks.

The last substantive historical request was to build three R10 packets from revised papers and updated guidance, include complete R9 returns and dispositions, and demand ambitious, literature-grounded improvements with a frozen chronological first pass. Follow-up messages required referenced literature in context. The historical completion reports main at `0d977710556f304ce70fa200cbf36b9beecb78e8`, 42 annex sources plus 13 supplements, and explicit Yao/Nisan/exact-BSS edition gaps. Earlier edit/push instructions and numerical finding aspirations are historical context; they do not override the present review-only/no-quota request.

The packet declares all 41 expert-to-record links pinned to `8357f268732746d1575e05e7de8c888e20ad3793` different from the packaged record; all 12 expert-to-Lean links have no declared byte difference. The visible transcript shows that commit 8357 changed only one expert line, followed by integration-time rebinding and generation. Independently replacing all 127 occurrences of 8357 with the previous 62868 commit in the packaged record reproduces exactly the before-hash in `round9_final_rebind.json`. That final rebind is therefore a commit-string-only change, not evidence of mathematical drift.

The complete record body committed at 8357 is still unavailable in the packet or this review's fetched evidence. The transcript does not expose a full semantic diff from that committed record. Anchor availability asserted by the builder is not the same as delivery of the exact linked body. The appropriate conclusion is a scope limitation: current proof-navigation checks refer to the packaged record. No stale mathematical claim or broken anchor has been established. A hash-bound copy of the exact linked edition would remove the residual ambiguity.

## Artifacts and execution limits

- `../checks/previous_round_custody.json`: full archive custody and disposition identity coverage.
- `../previous_round_audit.json`: per-finding decisions, present locators, assessments, challenges, excluded IDs and limits.
- `attached_context_review.json`: historical request/state evidence and exact pin-rebind calculation.

Input files and prior originals were not modified. No submitted reviewer, builder, renderer, Lean or Comparator script was executed. The audit's own small parsing/hash scripts were used for structural checks. No claim is made about all three current R10 ZIPs: only the supplied expert packet was available to this session.
