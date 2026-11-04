# {title}

This is one of **three** round-nine packets, one lead paper per packet. Each
contains all three current manuscripts and fresh PDFs, so cross-links can be
checked: the expert companion, the examples-first exposition and the complete
reasoning record. The panel below names the lead paper. Work on that paper in
full; use the other two as supporting sources, not as substitute lead papers.
Execute the assignment and return the review ZIP, not merely a plan.

## What we want

Find concrete ways to improve the paper, from its first sentence to its last.
We do not need praise, "this is good", "keep this", or a list of strengths.
There is no obligation to balance criticism with compliments. Look for the next
layer after round eight: unclear inference, wrong ordering, missing motivation,
undefined reference, overloaded sentence, redundant explanation, weak example,
misplaced detail, unhelpful diagram, poor page transition, imprecise credit or
mathematical error. Include small improvements as well as structural ones.

Aim for **at least 200 distinct actionable findings** for the expert paper,
**250 for the exposition**, or **400 for the long record**. These are depth
prompts, not quotas that justify invented faults or repeated versions of one
complaint. Continue beyond them when there is useful feedback. Cover every
section and appendix. Every finding must explain a specific reader cost and a
concrete repair direction; "make clearer" alone is not actionable. Rank impact
separately from source order, and state uncertainty where appropriate.

## Chronological reading is mandatory

Follow [the sequential reading protocol](chronological_reading.md).
Read every sentence in publication order and preserve the reader's state at the
moment it is encountered. Later knowledge must not retroactively make an early
sentence clear. Freeze this first-pass record **before** opening round-eight
feedback, other papers or methodological advice. Log every necessary detour.

Then verify the findings, follow links, inspect the fresh PDFs at normal size,
read the literature, and consult the previous round. The packet includes both
round-eight returns in full (text/JSON), all dispositions, revision notes and
validation records, plus older round-seven audits. These are historical advice
and decisions, not instructions overriding this request or proof that a repair
worked. No rewrite is requested.

## What to test

- The opening, novelty and credit; whether the reader understands the question
  and contribution before receiving technical detail.
- Every sentence's dependence on earlier material; each paragraph transition,
  referent, symbol, definition, displayed equation and hypothesis.
- Actual proof steps and calculations, including conditionals versus joint
  events, cap conventions, parameter ranges and fixed versus uniform estimates.
- Examples and exercises as operations the intended reader can perform; attempt
  questions before viewing answers and record any prior answer exposure.
- Figures, tables, captions, footnotes and links at their point of first use.
  Does the linked passage perform the promised task, and can the reader return?
- Weighting: what to cut, relocate, split, join or expand, with reasons.
- Agreement across the three accounts and correspondence to the formal statement.
  Existing build receipts are historical; do not spend the review rerunning them.

Read the supplied primary literature appropriate to your panel, then **search
online beyond it** for relevant papers, notes and explanations. Record dates,
editions, URLs and exact locators. Compare with the best relevant writing; do
not treat a corpus average as a quality threshold. Report inaccessible sources
honestly. Do not claim sources read merely because they were included.

The full writing skills, register rules and fresh draft measurements, reader
principles and exemplar papers from other theorems are supplied. The register is
a detector, not a verdict. The local writing method includes round-eight lessons
and this chronological-review protocol. Give method feedback where a general
rule caused or failed to catch a concrete problem. State improvements in terms
that transfer to other subjects, and distinguish a new rule from better use of
an existing rule. There is no request to rewrite the manuscripts or the skills.

{job}

## Return format

Return one ZIP with:

1. `feedback.json`: `packet`, `source_sha256` (copy `drafts` from
   `SOURCE_STATUS.json`), `panel`, `sources_read`, and `feedback`. Each finding has
   `id` (prefix below plus number), `paper`, `perspective`, `locator` (`section`,
   exact `quote` of at most 25 words, `line_start`, `line_end`, optional `pdf_page`),
   `unit_id` from the sentence audit, `kind`, `severity` (`critical`, `high`,
   `medium`, `low`), `feedback`, `why_it_matters`, `advice`, `available_before`,
   `missing_bridge`, `confidence`, optional `later_resolution`, optional
   `prior_finding_ids`, and optional `outside_source`. Use precise kinds such as
   `first_encounter`, `transition`, `prerequisite`, `prose`, `example`, `structure`,
   `figure`, `funnel`, `credit`, `error`, `question` or `evidence_presentation`.
   **No `keep` kind, `keep` severity or praise-only findings.** Order by encounter;
   rank the most consequential repairs separately in the verdict.
2. `sentence_audit.jsonl` and `coverage.json`, as specified in the sequential
   protocol. Every sentence and non-prose unit must be accounted for or declared
   unreviewed. Coverage is not inferred from the number of findings.
3. `reading_log.md`: the frozen first-pass account with reader-state changes,
   detours, stuck points, exercise attempts and later resolutions appended.
4. `feedback_by_document.md`: a sustained critique of the lead paper and shorter
   notes on cross-document dependencies. Concentrate on changes, not strengths.
5. `literature_comparison.md`: specific better treatments in the supplied and
   online literature, with editions, locators and read/skimmed labels. Keep each
   quotation within 25 words and respect aggregate quotation limits per source.
6. `previous_round_audit.json`: prior XP/EX IDs inspected, present locators and
   resolved/unresolved/regressed/new-consequence decisions. Keep this separate
   from new findings and do not count resolved items as improvement advice.
7. `method_feedback.json`: rule/skill, current evidence, mechanism of failure,
   and proposed general change. Include the limits of chronological simulation.
8. `verdict.md`: readiness for the intended reader, the twenty changes with
   greatest benefit, suggested revision order and remaining coverage gaps.
   No praise or "must keep" section.

{boundary}
