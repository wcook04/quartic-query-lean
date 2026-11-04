# {title}

This is one of **three** round-ten review packets, one lead paper per packet.
Each carries the revised expert companion, examples-first exposition and complete
reasoning record, with their source-bound PDFs. The panel below identifies your
lead paper. Review that paper completely; consult the other two after the first
pass to test its dependencies. Execute the assignment and return the review ZIP,
not merely a plan.

## The standard we are aiming for

Help make this an exceptionally well-written mathematical paper by the standards
of the best relevant literature. Passing an accuracy check, repairing the previous
round's complaints or being understandable after repeated study is not the
endpoint. We want a reader to see why the question matters, understand the design
of the argument, follow its difficult steps and retain its central ideas without
avoidable work. Precision, proportion, explanatory force and pleasure in following
a mathematical argument all matter. Judge them for this paper's stated audience
and purpose, rather than demanding the same treatment in all three genres.

Look for the most valuable improvements still possible. These may be a sentence's
referent, a better example, a sharper theorem statement or a different architecture
for several sections. Consider substantial cuts, reordered dependencies, a new
running example or a redesigned proof presentation when the evidence warrants
that ambition. Do not confine yourself to polishing the current structure. For
a large proposal, identify the passages it changes, what the reader would gain,
what dependencies must survive and how an author could test the result.

Return concrete improvement advice, not praise, "keep this", generic style rules
or a list of strengths. There is **no numerical finding target**. Do not invent
faults, split one complaint into many, multiply it across personas or turn a
preference into a mathematical error. Nor should the absence of an obvious error
end the inquiry: compare the current explanation with a demonstrably stronger
way of accomplishing the same reader task. Make the cost and benefit explicit.
Coverage and quality of judgment matter independently of the finding count.

## Read prospectively, then verify

Follow [the chronological protocol](chronological_reading.md). Record each
sentence and non-prose unit when you encounter it; preserve what the preceding
text has made available. Freeze that first-pass evidence **before** opening past
returns, dispositions, other accounts, writing guidance or comparison literature.
The minimum panel and procedural instructions are allowed before the pass; the
literature standard and methodological material are second-pass resources. Log
any necessary detour and any prior familiarity. Do not reconstruct an encounter
log afterward and label it contemporaneous.

After the freeze, inspect the PDF at normal reading size, verify proposed
mathematical criticisms, follow proof links and compare with actual literature.
Use [the literature standard](literature_standard.md) to make this comparison
specific. Read the supplied primary sources appropriate to the panel, then search
online beyond them for useful treatments and current related work. Record the
edition, date, URL, passage locator and what you actually read. The ambition is
excellent writing, not resemblance to a named author's surface mannerisms or
conformity to a corpus average. Inaccessible sources remain unread.

Every packet includes the full 42-source existing literature annex, not merely
a panel-specific selection, plus complete PDFs and extracted text for the six
primary works used by the literature standard and supplementary mathematical
editions. These provide the context around a cited passage, not only quotations
or a style summary. After the first-pass freeze, open the generated packet-root
`LITERATURE_COVERAGE.json` to distinguish the cited edition, supplied edition,
full text, alternatives and gaps. `SUPPLEMENTARY_LITERATURE.json` identifies the
added sources and their archive members, editions and hashes. Follow those
member paths to inspect the originals; use the PDFs when extraction damages
notation.

Full-text access is still incomplete for Yao (1977) and Nisan (1991). The cited
2003 Barnum–Saks–Szegedy edition is unavailable; its earlier 2002 primary version
is included and must be identified as such. An alternate edition or related
treatment is not silent evidence for the exact citation. Read the full relevant
argument around each passage used in your critique, and distinguish the scope
you read from the scope supplied. Including a whole work does not oblige a
cover-to-cover detour through every annex or establish that anyone read it.

Then audit the complete round-nine returns and their individual dispositions.
They are historical evidence, not authority over your judgment. An accepted
repair can fail, a rejected suggestion can deserve reconsideration and a change
can create a new problem. Challenge any disposition with exact current evidence
and the original finding ID. Do not recycle a complaint that the revised text
has resolved. Keep resolved regression checks separate from new improvement
advice. Earlier rounds are context, not additional current assignments.

## What to examine

- The question, contribution and credit; whether opening and section openings
  give the reader a reason and a usable expectation for what follows.
- Each sentence's inferential demand, referents and prerequisites at first use;
  paragraph movement, notation, hypotheses and the purpose of displays.
- The proof's actual mechanisms, with the assumptions, conditioning, parameter
  regimes, accounting and termination needed for the claimed conclusion.
- Examples and exercises as tasks the intended reader can perform. Attempt a
  question before viewing its answer; disclose prior answer exposure.
- Diagrams, captions, tables, footnotes, links and page transitions where they
  are encountered. Check whether a destination performs its advertised job.
- Proportion and architecture: where detail buys understanding, where it hides
  the argument, and what deletion, relocation or reconstruction could improve.
- Consistency across the accounts and fidelity to the formal statement, while
  distinguishing mathematical explanation from historical execution evidence.

The packet includes merged writing guidance, register measurements and exemplars.
Use them after the first pass as tools for judgment, not rules that automatically
condemn a sentence. Give method feedback only where a transferable failure or
improvement is grounded in a concrete case. Distinguish improving application of
an existing rule from proposing a new rule. No manuscript or skill rewrite is
requested.

{job}

## Return format

Return one ZIP containing:

1. `feedback.json`: `packet`, `source_sha256` (copy `drafts` from
   `SOURCE_STATUS.json`), `panel`, `sources_read`, and `feedback`. Each finding has
   `id` (the panel's prefix plus a number), `paper`, `perspective`, `locator`
   (`section`, exact `quote` of at most 25 words, `line_start`, `line_end`, optional
   `pdf_page`), `unit_id` from the sentence audit, `kind`, `severity` (`critical`,
   `high`, `medium`, `low`), `feedback`, `why_it_matters`, `advice`,
   `available_before`, `missing_bridge`, `confidence`, and optional
   `later_resolution`, `prior_finding_ids` and `outside_source`. Useful kinds
   include `first_encounter`, `transition`, `prerequisite`, `prose`, `example`,
   `structure`, `figure`, `funnel`, `credit`, `error`, `question` and
   `evidence_presentation`. No `keep` kind or severity and no praise-only rows.
   Order findings by first encounter, with impact ranked separately. For a
   structural proposal, add `affected_locators`, `dependency_constraints` and
   `acceptance_check`; anchor it at the first passage affected.
2. `first_pass/`, `freeze.json`, `sentence_audit.jsonl`, `later_annotations.jsonl`
   and `coverage.json`, following the chronological protocol. Preserve immutable
   encounter evidence separately from later interpretation. Declare every
   unreviewed range; finding count is not a coverage certificate.
3. `reading_log.md`: a readable account linked to the frozen log and explicitly
   separated later annotations, including detours and exercise attempts.
4. `feedback_by_document.md`: a sustained critique of the lead paper and shorter
   notes on cross-document dependencies. Explain how the proposed changes work
   together, including alternatives to its present architecture when justified.
5. `literature_comparison.md`: passage-specific comparisons with supplied and
   online sources, stating the edition, locator, read/skimmed status, reader task
   and proposed application. Do not merely name impressive authors. Keep each
   quotation within 25 words and respect aggregate source quotation limits.
6. `previous_round_audit.json`: round-nine IDs actually inspected, their recorded
   dispositions, present locators and `resolved`, `unresolved`, `regressed` or
   `new_consequence` assessments, with evidence. Include separately identified
   challenges to dispositions and any uninspected prior IDs. Do not count a
   resolved item as a new finding.
7. `method_feedback.json`: rule/skill, current evidence, failure mechanism,
   existing-rule versus new-rule judgment and proposed general change. Report
   any limits or departures in the chronological review itself.
8. `verdict.md`: readiness for the intended reader, the changes with greatest
   expected benefit, a coherent revision order and remaining coverage gaps.
   Choose up to twenty priorities when that is useful; do not pad the list. Say
   what would distinguish a merely serviceable next edition from an excellent
   one, using the concrete findings. No praise or "must keep" section.

{boundary}
