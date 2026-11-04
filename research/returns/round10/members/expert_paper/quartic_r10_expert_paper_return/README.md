# Quartic expert companion — round ten review

This ZIP contains an advice-only review of the exact attached R10 expert-paper packet. No manuscript, Lean source, skill, repository or historical submission was edited or executed. The main recommendation is a focused structural revision; the inspected arguments did not establish a mathematical failure of the separation. The review contains 15 actionable findings with distinct severity and priority fields, source locators and explicit coverage limits.

## Start here

| File | Purpose |
|---|---|
| [verdict.md](verdict.md) | Readiness, seven connected revision priorities and acceptance checks. |
| [feedback_by_document.md](feedback_by_document.md) | Sustained specialist critique and supporting-document dependencies. |
| [feedback.json](feedback.json) | Machine-readable findings XP10-001–XP10-015, source hashes and locators. |
| [literature_comparison.md](literature_comparison.md) | Passage-specific primary-source comparisons and their limits. |
| [sources_read.json](sources_read.json) | Exact editions, actual read scopes and portable citation IDs. |
| [previous_round_audit.json](previous_round_audit.json) | Inspected R9 findings, decisions, challenges and uninspected IDs. |
| [method_feedback.json](method_feedback.json) | Grounded improvements to applying the existing review/writing method. |

## Encounter and verification evidence

[reading_log.md](reading_log.md) separates the primary encounter from retrospective conclusions. The `first_pass/` files are immutable under [freeze.json](freeze.json). The root [sentence_audit.jsonl](sentence_audit.jsonl) adds labeled retrospective fields; [later_annotations.jsonl](later_annotations.jsonl) tracks all 38 provisional candidates. [coverage.json](coverage.json) declares the full lead source and PDF inspection, targeted specialist scopes and protocol departures.

The `evidence/` and `specialist_notes/` folders contain scoped quantum, classical, uniform, source-destination, PDF and historical checks. The `checks/` folder contains input-integrity results, eleven finite mathematical sanity checks and the return-file manifest. Repository paths in those files identify members of the input packet; the manuscripts themselves are not duplicated in this return.

## Verify the extracted return

Run with Python 3 from the extracted folder:

```sh
python3 verify_return.py
```

The verifier checks every manifested file's SHA-256 and byte count, JSON/JSONL syntax, required artifacts, finding and annotation references, and the frozen evidence hashes. To additionally match the review's quotations and source bindings against your extracted original packet, pass its root:

```sh
python3 verify_return.py --source-root /path/to/extracted/original/packet
```

To recompute the small finite checks without modifying the review, use:

```sh
python3 checks/recompute_classical_examples.py --output /tmp/quartic_finite_results.json
```

These checks use only the Python standard library. They do not run Lean, Comparator or submitted reviewer scripts. The archive was also tested for CRC errors, safe unique member paths and byte-identical extraction before delivery. [checks/validation.json](checks/validation.json) records the validation scope.

## Important reading boundaries

The primary encounter was logged in bounded source blocks, not with strict one-sentence visibility. The generated bibliography and PDF pages were inspected after the freeze. Current supplied record proof bodies were checked at named scopes; the exact historical pinned record body and live link round trips were not independently verified. Supporting manuscripts and the literature annex were not all read cover to cover. No fresh formal execution or human-reader evidence is claimed.
