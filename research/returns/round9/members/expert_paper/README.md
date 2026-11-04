# Round-nine expert companion: review return

**Advice only. Start with `verdict.md`, then `feedback_by_document.md`.** No manuscript, theorem or formalization was rewritten. The subject is the expert companion; the exposition and long reasoning record are supporting sources.

## Contents

| File | Purpose |
|---|---|
| `verdict.md` | Readiness, twenty ranked revision actions, revision sequence and coverage limits |
| `feedback.json` | 166 distinct, source-ordered actions with exact quotes, locators and source hashes |
| `feedback_by_document.md` | Sustained critique of the lead and supporting-document dependencies |
| `sentence_audit.jsonl` / `coverage.json` | 541 accounted units and explicit protocol/coverage limitations |
| `reading_log.md` / `first_pass/` | Unchanged frozen narratives followed by separate verification resolutions |
| `literature_comparison.md` / `sources_read.json` | Primary-source comparisons, editions, locators and actual read scopes |
| `previous_round_audit.json` | 87 scoped assessments of 83 unique prior IDs |
| `method_feedback.json` | Transferable method feedback; no skill files changed |
| `verification/` | Input checks, finite computations, receipt scope, PDF inspection and candidate adjudication |
| `verify_return.py` / `manifest.json` | Reproducible schema, reference, optional source-quote and payload-integrity checks |

The final finding count is 166 (5 high, 59 medium, 102 low), below the depth target of 200 after removing duplicates and unsupported complaints. The return does not label every suggestion a mathematical error. Panel lenses are model-emulated perspectives, not named people or independent human readers. The procedural deviations from a literal serial, per-sentence first-read protocol are stated in the reading log, coverage and verdict.

## Source identity

- Original ZIP: `quartic_r9_expert_paper.zip`
- Original ZIP SHA-256: `3c03b7d0a50753bd418a9293bdcf37ccd1b1dd0dd1d1682b55b7409c46ee5ab5`
- Lead Markdown SHA-256: `7fddfa0c37f7d038ba58adde4e7685263f3ba7733d0fd87a8a3eea4ce653f8ab`
- Supplied repository revision: `7772e4f2b98149a38ed69b88397982620f94bdac`

Line locators refer to the current supplied Markdown, not an older linked revision. Paths beginning `repository/`, `paper/`, `literature/`, `previous_round/` or `skills/` identify members of the original input packet; the source manuscripts are intentionally not duplicated in this return. The attached session transcript was used only to establish task continuity, not as proof evidence.

## Checking the return

After extracting the return ZIP, run:

```sh
python3 verify_return.py
```

To also check exact quotations and draft hashes against your extracted original packet:

```sh
python3 verify_return.py --source-packet /absolute/path/to/original_packet
```

The manifest excludes itself to avoid a self-referential hash. No archive SHA-256 is embedded inside the archive. The delivered archive was separately CRC-tested and extracted again before saving. This verifies file integrity, not the complete mathematics.
