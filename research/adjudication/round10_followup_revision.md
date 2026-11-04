# Follow-up editorial revision of both shorter papers

The [preserved informal assessment](../returns/round10/followup_editorial_feedback.md)
concerns the expert paper; its [intake](../returns/round10/followup_intake.json)
records the absence of an exact reviewed-edition hash and prospective reading log.
The user requested application to both the expert paper and exposition. This is
not another complete R10 return, and the exposition and record reviews remain pending.

## What changed

The expert paper's title and first paragraph identify the reconstruction and
OpenAI's theorem. The abstract introduces the search and hidden-address mechanisms
before naming the capped predictor. Its opening roadmap explains why comparisons
are cheaper than repeated certificate verification, how a proposed cell query
predicts an address, and how the two cost scales yield the fourth-power limit.
The fixed-parameter argument now leads directly to the formal correspondence in
Section 6. The complete growing-parameter refinement remains in Appendix E.
References to Appendix G visibly name the separate reasoning record.

The exposition has its own title and motivation, preserving the eight-bit and
four-column examples, taught quantum operations, questions and exact probability
conditions. The precise exponent definition is introduced at its use in Section 6.
Appendix A holds cost bookkeeping and the older recipe's arithmetic; Appendix B
holds the optional direct-product proof. Its complete contract stays on the main
route, and the simulator and planted-pair explanation remain there. It is now
25 pages; the expert remains 18. These lengths describe the delivered artifacts,
not quality targets.

The record changes only its reading-route locator from expert Section 6 to
Appendix E. Its 298 marked proof passages are byte-unchanged. The record remains
139 pages. No Lean source or theorem statement was changed; no new Lean or
Comparator execution is claimed. Historical reviews continue to describe their
original editions.

## Decisions and evidence

The [individual decisions](round10_followup_dispositions.json) distinguish the
repairs for the two audiences, retained strengths and advice not treated as a quota.
The [method application](round10_followup_method.json) adds an audience-specific
transfer check to the existing public authoring guide, with two outside transfer
cases and an exception. Early motivation and offline-readable references were
already required; this pass repairs their application rather than introducing
redundant rules. The change is published in
[lean-exposition PR 45](https://github.com/wcook04/lean-exposition/pull/45),
merged as `181651db04ad6d392db8d7b35198058067bb51c0` after hosted CI passed.

The [validation record](round10_followup_validation.json) binds the source editions,
PDFs, link checks, register comparison and rendered inspection. The register
comparison is descriptive: the teaching baseline is one lecture-note source and
has no empirical spread; damaged survey extraction was excluded. No detector
score is a writing-quality or comprehension measure. The author and receiving
editor already knew the feedback, so neither pass is described as a blind reader
study. Scores in the original assessment remain the reviewer's opinions.
