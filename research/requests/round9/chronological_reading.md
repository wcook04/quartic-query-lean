# Read in the order the reader receives the words

A passage may be correct once the whole paper is known and still fail on first
encounter. This review tests the accumulation of understanding in publication
order. Do not assemble a fluent retrospective account by searching ahead and
silently importing later definitions into earlier sentences.

## First pass: freeze the encounter

Read the lead paper from its title to its last reference and appendix, in printed
order. Read every sentence within each paragraph in order. At its actual point
of encounter, include each display, theorem, proof, caption, table, footnote,
question and answer. The numbered Markdown copy provides original source-line
locators; it is not an automatic sentence segmentation. Segment prose by meaning,
not by every period in a citation, abbreviation or formula. Give every sentence
its own coverage row; treat a display or non-prose object as an additional unit.

Before continuing past a sentence, ask:

- What did the preceding text let this reader know? What remains unresolved?
- What does this sentence add, and what inference does it ask the reader to make?
- Are its referents, symbols, hypotheses, purpose and prerequisites available now?
- What would this reader predict or try next? Does the next sentence honour that?
- Is the cognitive work justified here, or would a different order, example,
  definition, transition, deletion or split make the argument easier to follow?

Record a confusion at the first sentence that creates it, with the reader's
current understanding and the missing bridge. If later text resolves it, append
the resolving locator; do not erase the original encounter. Distinguish a useful,
clearly signposted open question from accidental withholding. Repeated words
can support recall; brevity alone is not an improvement.

Do not read the old reviews, revision notes, other accounts, bibliography papers
or solutions in advance. A justified detour is allowed: log its starting locator,
reason, destination, information imported and return point. That detour is part
of the reading cost. Do not silently skip ahead, search for definitions, skim
appendices or replace the sequential pass with thematic sampling.

For questions, write the attempt before opening the answer. Preserve failed
attempts, time or work estimates and prerequisites that were missing. If an
answer has already been seen, label the attempt answer-exposed; do not call it
cold. A model that already knows the document must label its first pass a
simulated chronological audit, not an observed fresh human reading. Multiple
perspectives in one context are not independent blind readers.

## Second pass: verify and prioritize

Only after freezing the first-pass log, read the supplied and online literature,
other accounts, writing method and round-eight returns and revision decisions.
Check each candidate finding against the current source. Keep a chronological
failure even if a later passage supplies the answer; explain whether bringing
that information forward would help or would spoil a deliberate teaching step.

For prior feedback, identify the XP/EX ID when relevant. Classify it as resolved,
unresolved, regressed, or a new consequence of the repair, with evidence. A prior
"applied" label is a decision to inspect, not an instruction to accept. Do not
recycle an old complaint when the current passage has fixed it. Put resolved
checks only in the regression audit, never in the improvement count.

Inspect diagrams, tables and page transitions in the PDF at ordinary reading
size. Compare prose with literature of the same genre and task. A source claim
needs an actual locator and a read/skimmed label; if online access is unavailable,
say so. Validate mathematical criticisms before calling them errors. Distinguish
an error, a justified question and a reader-specific difficulty.

## Coverage and return integrity

Write `sentence_audit.jsonl` in source order, one JSON object per encountered
sentence or non-prose unit. Each object records `unit_id`, `source_path`,
`line_start`, `line_end`, `sentence_in_paragraph`, `unit_type`, `quote` (at most
25 words, exact current Markdown), `available_before`, `new_demand`,
`unresolved_after`, `next_expectation`, `issue_ids`, and `later_resolution`
(null or a precise locator). Arrays may be empty. This is a coverage and reader-
state log, not a praise list; an empty issue list makes no claim of perfection.
Use `sentence_in_paragraph: null` for displays and other non-prose units.

Return `coverage.json` with source hashes, the first and last reviewed locators,
all section and appendix ranges, counts of sentences and other units, perspective
coverage, detours, answer exposure, and every unreviewed range. Each perspective
must identify what it actually read; do not multiply the same finding across
personas. If the complete record cannot be read within the available budget,
return the useful work with explicit gaps and a continuation locator. Never
claim full coverage from a large finding count or invent defects to hit a target.
