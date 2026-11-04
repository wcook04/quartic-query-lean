# Preserve the first encounter, then reconsider it

The first pass tests how understanding accumulates in publication order. A later
explanation may make an earlier sentence correct in retrospect while leaving a
real first-encounter cost. Conversely, a signposted question can productively
remain open. Record the encounter before deciding which case it is.

## Before reading

Read the current request and its panel instructions. Identify the lead source
and PDF from `SOURCE_STATUS.json`. Do not open the other manuscripts, prior
returns, revision notes, dispositions, writing guides, register measurements,
exemplars or bibliography sources yet. Do not inspect exercise solutions ahead
of their place in the paper. Reading the paper's own bibliography in publication
order is part of the pass; following its citations is a second-pass activity.

State the reader perspective, assumed background and your actual prior exposure.
A model's perspectives are simulations, not observations of human readers.
Perspectives in a shared context are not independent blind readers. If you have
already read this edition, say so before starting; preserve a prospective log of
this pass, but label it an informed simulation rather than a cold encounter.

## First pass: record before moving on

Read from the title through the last reference and appendix in publication
order, sentence by sentence. At their point of use include displays, theorem
statements, proofs, captions, tables, footnotes, questions and answers. Use the
numbered Markdown copy for source-line locators. Segment sentences by meaning;
a period in an abbreviation or formula does not automatically end a sentence.
Give each sentence its own row and each non-prose object an additional row.
Keep routine rows compact and spend explanation on real demands or obstacles;
record keeping must serve the reading rather than displace it.

Before moving past a unit, record what the preceding text has made available,
what the unit adds or asks the reader to infer, what remains unresolved and what
the reader expects next. Ask whether its purpose, referents and prerequisites are
available now, and whether its cognitive work is justified at this point. An
empty issue list is acceptable; it is neither praise nor a claim of perfection.

Record confusion where it first arises. Do not import a later definition into
`available_before`. Do not silently search ahead or replace the pass with thematic
sampling. If a detour is necessary, record the departure locator, reason,
destination, information imported and return point before resuming. It becomes
part of the reading cost and exposure record, not evidence of uninterrupted
first reading.

Attempt each question before opening its answer. Save the attempt, failed routes
and missing prerequisites; use honest work estimates rather than fabricated
measurements. If the answer was previously visible, mark the attempt
`answer_exposed`. A lecturer's evaluation of an exercise is separate from a
student simulation's ability to solve it.

One primary chronological pass must span the whole lead paper. Conduct subsequent
perspectives one at a time, with their actual ranges and prior exposure declared.
They can reread from specialist viewpoints; do not relabel these as fresh passes
or combine concurrent perspectives into a supposedly serial encounter history.

## Freeze before retrospective work

Write the encounter rows incrementally to `first_pass/sentence_audit.jsonl` and
the reading notes to `first_pass/reading_log.md`. Keep a compact coverage snapshot
in `first_pass/coverage.json`. At the end of the pass, or at an explicitly
incomplete stopping point, preserve those three files unchanged. Create
`freeze.json` as the first-pass manifest, with the source hashes, SHA-256 of each
frozen file, first and last
reviewed locators, completion or partial status, unreviewed ranges, prior
exposures, detours and the stage boundary. Record a timestamp if available, but
do not treat a timestamp or a hash alone as proof of chronological conduct.
Describe the actual writing and freezing procedure.

Only then open the retrospective material. Append later resolutions, revised
interpretations and new findings to `later_annotations.jsonl`, referencing the
original `unit_id` and giving the new evidence and stage. Do not replace an old
encounter row, backdate an annotation or fill an unobserved encounter from memory. Later sentence segmentation or
expanded annotations must be separately versioned and identified as retrospective;
they cannot replace the original audit under its frozen digest.
If the prescribed logging was missed, disclose it. A retrospective reconstruction
can still supply useful advice but cannot establish a prospective first pass.

## Second pass: verify, compare and prioritize

Read the supplied and online literature, the other accounts, writing method and
round-nine returns and decisions. Check candidate findings against the exact
current text and full relevant context. For a claim that something is absent,
search the likely earlier/later passages and proof destination; distinguish an
actual omission from information present too late or too difficult to find.
Validate mathematical criticisms before classifying them as errors. Keep a
question or a reader-specific obstacle distinct from a false statement.

For each relevant prior XP9, EX9 or RR9 ID, inspect the original finding and its
individual disposition. Record what the current passage does. A recorded
"applied" or "retained" status does not settle whether the decision was wise.
Challenge it when current evidence warrants, with the precise claim contested
and a reasoned alternative. Do not revive a resolved claim without new evidence.

Inspect diagrams, tables and page transitions in the supplied PDF at ordinary
reading size, declaring the pages actually viewed. Follow the literature standard
only now. Compare treatments serving similar reader tasks and genres, then ask
whether their explanatory choice transfers here. For a proposed repair, reread
its first use and downstream dependencies: a locally smoother sentence can make
the larger argument harder to follow.

## Coverage and return integrity

The frozen sentence audit uses one JSON object per unit, in source order, with
`unit_id`, `source_path`, `line_start`, `line_end`, `sentence_in_paragraph`,
`unit_type`, `quote` (at most 25 words, exact current Markdown),
`available_before`, `new_demand`, `unresolved_after`, `next_expectation`,
`issue_ids` and `later_resolution`. At initial encounter `later_resolution` is
null; any information learned afterward belongs in a later annotation. Use
`sentence_in_paragraph: null` for displays and other non-prose units. Arrays may
be empty. Provisional issue IDs can be mapped to final findings by annotation.

The returned root `sentence_audit.jsonl` may combine the encounter and subsequent
annotations for convenient reading, but each row must cite its `encounter_ref`
and identify retrospective fields. It must not overwrite or masquerade as the
frozen evidence. `reading_log.md` follows the same separation.

Return `coverage.json` with source hashes, freeze references, first/last reviewed
locators, every section and appendix range, counts of sentences and non-prose
units, PDF pages inspected, perspective-specific coverage, detours, answer
exposure, protocol departures and all unreviewed ranges. Keep source coverage,
PDF inspection and specialist rereads distinct. If the full assignment exceeds
the available budget, return useful partial work with a continuation locator.
Never infer completeness from a large finding count or conceal an unfinished
appendix behind a general claim that the paper was read.
