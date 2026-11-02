## Your job: mathematical understanding and proof audit (proof/claim audit; no new theorems required)

Read the whole paper, then read cited papers wherever the argument depends on them.

1. Explain the proof from first principles to a reader who knows linear algebra and basic probability but no query complexity. Define R, Q, partial and total functions, Forrelation, certificates and cheat sheets before using them.
2. For every row of `corpus/statement_ledger.json`, say what it means, why it is needed and which step is hardest. Correct any row that misstates the paper.
3. Check every proof step yourself. Report gaps, hidden assumptions, constants, and places where the construction could fail, especially: behaviour outside the promise in the tournament; the planted-input lower bound; the adaptive direct-product argument; parameter choices r, l, epsilon and T.
4. Say which ideas are new compared with Aaronson, Ben-David and Kothari's cheat sheets, Bansal and Sinha, and Sherstov, Storozhenko and Wu.
5. Give hand-sized worked examples: the smallest board where the winner rule, outward pointers and tournament can be computed by hand, with exact numbers.

## Return one ZIP containing

- `understanding.md`: the first-principles explanation.
- `statement_review.json`: one row per ledger id with keys `id`, `verdict` (`correct`, `corrected`, `doubtful`), `plain_meaning`, `why_needed`, `hard_step`, `correction`, `evidence`.
- `audit_findings.json`: keys `location`, `severity`, `claim`, `reasoning`, `how_to_confirm`.
- `worked_examples.md`: computed examples.
- `further_reading.json`: keys `title`, `url`, `why`, `statement_ids`.
