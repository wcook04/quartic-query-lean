# Phrase-tie returns, 20 November 2026

These are three returns of the reader phrase-link packets 08, 09 and 10, one for each of the
[expert companion](../../../docs/expert_companion.md), the
[exposition](../../../docs/exposition.md) and the
[reconstruction](../../../docs/reasoning_record.md). Each folder under `members/` keeps the
returned `ties.json`, `topics.json`, `titles.json`, `notes.json`, the reviewer's `REVIEW.md`
and the packet's `packet.json` unchanged. The [intake manifest](intake.json) binds their
bytes. The packets quoted the papers and the Lean at commit
`f192def14f95a3aff7da5866f35be7b565595e1d`, and each return passed the packet's mechanical
checker. [FIXES.md](FIXES.md) lists the wording and name corrections made on acceptance,
before these files were copied.

[tools/intake_phrase_returns.py](../../../tools/intake_phrase_returns.py) derived the
maintained sources in [docs/reading_phrases/](../../../docs/reading_phrases/) from these
files. Each maintained file lists its further `corrections`: Lean line ranges that ran past
the end of their declaration are cut to it (22 rows in all, none disjoint from its
declaration), eighteen titles that wrote mathematics in plain ASCII or words (such as
"one minus epsilon") are set as inline TeX with a Unicode reading, and 235 comparison notes
that wrote mathematics or Lean names as plain text are set with the mathematics in `$…$` and
the Lean names in backticks, words that stood for a formula (such as "absence" for
$\Pr[s\notin L_T]$) being replaced by it and the other words kept
([note_typesetting.json](note_typesetting.json) lists each before and after). The returns are AI work. No person has reviewed the phrase ties,
the fidelity judgements or the reading notes.
