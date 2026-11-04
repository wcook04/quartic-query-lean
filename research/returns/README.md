# Research returns

Three independent reviews answered the requests in [review requests](../requests/review/). Each
folder holds the text records of one return. Source PDFs, copied papers and copied
ledgers were left out. The two Python checkers that came with the returns are in
[tools/return_checks/](../../tools/return_checks/).

| Folder | Original archive | SHA-256 |
| --- | --- | --- |
| [1_understand_the_paper/](1_understand_the_paper/) | `quartic_1_understand_the_paper_review.zip` | `ce44a6c1082f1b5126af35c0947cf7c5ae91bc6837b08971a587026b84322d81` |
| [2_ground_in_literature/](2_ground_in_literature/) | `quartic_literature_review_2026-11-01.zip` | `2c0d7e1e5dd0c8fb6c94b85855b5c531c3704d6dd13fdcc2d31bd0da30ed683c` |
| [3_lean_and_comparator/](3_lean_and_comparator/) | `quartic_3_lean_and_comparator_return.zip` | `6e3f8cfb1b94d108814a80f3ee337685823321fef278c237014dc24e5af421a1` |

The returns are advisory. Their findings were checked against the preprint and
the cited sources, and each finding has a verdict in
[adjudication.json](../adjudication/adjudication.json), summarised in
[adjudication_notes.md](../adjudication/adjudication_notes.md). Use those verdicts rather than the
returns' own conclusions. The Lean and Comparator return was written without a
compiler, so its signatures are drafts until a build says otherwise.

## Funnel returns

Five returns answered the writing requests in [funnel requests](../requests/funnel/).
Their text records are kept as received in [funnel/](funnel/). Their four scripts
moved to [tools/return_checks/](../../tools/return_checks/) with a `funnel<n>_` prefix
(`funnel3_examples.py`, `funnel4_checks.py`, `funnel4_validate_package.py`,
`funnel5_check_return.py`), and the worked-example figure to
[docs/figures/](../../docs/figures/). The examples script and the Forrelation checks were
rerun on 2 November 2026: the examples output matched byte for byte and every exact
constant check passed.

| Folder | Original archive | SHA-256 |
| --- | --- | --- |
| [funnel/1_long_reasoning_record/](funnel/1_long_reasoning_record/) | `quartic_long_reasoning_record.zip` | `c5af4d83d11fa5ac70c44ce10e4c3639f4c3bce5125ce213b8b75d17dd2eabc9` |
| [funnel/2_short_expert_paper/](funnel/2_short_expert_paper/) | `quartic_2_short_expert_paper_return.zip` | `e8290a347d35d2c4073161ce3f6fcbe609c4ce853d25da88dc9be74fc3fbb0f2` |
| [funnel/3_examples_first_exposition/](funnel/3_examples_first_exposition/) | `quartic_examples_first_exposition_return.zip` | `a77c7a4e0e154e075ff0154b356d9a44a2c380e363ed7b83d50f0c48d8d61472` |
| [funnel/4_forrelation_route_note/](funnel/4_forrelation_route_note/) | `quartic_4_forrelation_route_review.zip` | `19761033f55ea276788bf67f87b910e0d26fa6552b89b79efb636c0fd6e3204f` |
| [funnel/5_reader_and_film/](funnel/5_reader_and_film/) | `quartic_5_reader_and_film_return.zip` | `fb78494cb7a9c79c39c1d31153f6fda44f3af143f5b35ed70808be6be8a26413` |

These were also written without a Lean compiler. Their audit findings have verdicts in
[funnel_adjudication.json](../adjudication/funnel_adjudication.json), summarised in
[funnel_adjudication_notes.md](../adjudication/funnel_adjudication_notes.md). Their proposed
new statements are uncompiled and are not corpus rows.

## Round-two returns

The seven [round-two snapshots](round2/README.md) retain every submitted file,
including Lean and Python, as advisory evidence. Their [intake manifest](round2/intake.json)
binds the original archive hashes to the submitted member paths and bytes. The
repository checker validates those snapshots without running the submitted code;
decisions and corrections remain under [adjudication](../adjudication/).

## Round-three returns

The ten [round-three snapshots](round3/README.md) preserve original archive
members and pasted inputs as advisory evidence. Their manifest records original
archive and member hashes; decisions belong under [adjudication](../adjudication/).

## Round-four returns

The seven [round-four returns](round4/README.md) are bound by hash in their
[intake manifest](round4/intake.json); their originals and members stay local.

## Round-seven returns

Four round-seven review submissions are preserved under [round7/](round7/).
Their [intake manifest](round7/intake.json) binds archive and member hashes;
[the inventory](round7/recommendation_inventory.json) retains all structured
manuscript findings, method findings and claim journeys with their original
fields. These are advisory observations, including simulated reader perspectives,
not independent human reviews or proof verification. The original archives and
submitted scripts remain local; decisions belong under [adjudication](../adjudication/).

## Round-eight returns

The [two round-eight returns](round8/README.md) preserve 448 manuscript findings
and 40 method findings. Their [intake](round8/intake.json) binds the original
bytes; [dispositions](../adjudication/round8_synthesis.json) and
[revision notes](../adjudication/round8_revision.md) identify what changed in the
maintained papers and what was deliberately retained.

## Round-nine returns

The [three round-nine returns](round9/README.md) preserve 538 manuscript findings,
48 method findings and the reviewers' declared coverage limits. The
[intake manifest](round9/intake.json) preserves their original identities;
[the revision account](../adjudication/round9_revision.md) maps the findings to
current manuscript decisions and validation.

## Round ten

The [expert return](round10/README.md) is preserved with all 34 members and its
archive hash. The two later returns add 197 preserved files; their custody and edition limits are recorded in the same guide. Maintained
[decisions](../adjudication/round10_revision.md) are separate from submitted advice.

## Successive reader assessments

The twelve `reader_expert_*`, `reader_exposition_*` and `reader_record_*` text files preserve four successive assessments of each revised paper. The [intake record](../adjudication/reader_revision_intake.json) identifies the original bytes; the [revision](../adjudication/reader_revision.md) records decisions. Later retractions qualify earlier criticism; these are advisory readings, not independent proof certifications.

## Paper-purpose revision

The three `paper_purpose_expert.md`, `paper_purpose_exposition.md` and
`paper_purpose_record.md` files preserve the next supplied review conversations;
`paper_purpose_context.md` preserves the accompanying continuation context.
The [intake](../adjudication/paper_purpose_intake.json) binds their original bytes.
These conversations include successive reconsiderations and an extracted-formula
criticism that must be checked against the actual source. The
[revision account](../adjudication/paper_purpose_revision.md) separates the
adjudicated changes from the reviewers' proposed edits and scores.
