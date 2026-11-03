# Round-five expert-referee return

Start with **`verdict.md`**, then read **`findings.md`** or ingest **`findings.json`**. The latter follows the requested schema and copies the complete `drafts` hash object from the supplied `SOURCE_STATUS.json`.

The return contains 41 located findings: 4 high, 23 medium, 4 low, and 10 to keep. No critical defect in the main separation was identified. Local mathematical corrections are marked `error`; literature, navigation and editorial findings have their own categories. Every locator quote is an exact substring of the current supplied Markdown and contains at most 25 words.

## Contents

| File | Purpose |
| --- | --- |
| `verdict.md` | One-page overall judgment and five priorities. |
| `findings.json` | Canonical structured findings for intake. |
| `findings.md` | Readable rendering of the same findings and their evidence. |
| `earlier_review_followup.md` | Disposition of all 14 predecessor-review topics. |
| `sources_and_scope.md` | What was read, sampled, verified online or left unread. |
| `provenance.json` | Exact input identities and source-byte bindings. |
| `checks/example_checks.json` | Five reproduced finite examples, using exact rational arithmetic. |
| `checks/check_examples.py` | Standard-library script that reproduces those calculations. |
| `checks/local_link_audit.json` | Independent local audit of 77 used destinations across both drafts. |
| `checks/pdf_review.json` | Rendering coverage and the specific visual findings. |
| `checks/validation.json` | Schema, quotation, source-hash and calculation checks performed here. |
| `checks/validate_return.py` | Standard-library validation of the return; optional checks against the original packet. |
| `MANIFEST.json` | Byte size and SHA-256 for every other file in this return. |

Source paths in findings refer to members of the **original input packet**, except `checks/...`, which refers to this return. The source packet, historical trace and third-party papers are not duplicated here. No manuscript, bibliography or Lean source was changed. The review takes the expressly exempted in-progress completion claims as stated and does not raise findings merely about their status.

## Reproduce the checks

From the extracted return directory:

```bash
python3 checks/validate_return.py
```

To additionally check every quote and supplied source hash, pass the directory containing the original packet's `READ_ME_FIRST.md`:

```bash
python3 checks/validate_return.py --source /absolute/path/to/original_packet
```

The validator checks its own return manifest and reruns the finite examples in a temporary directory. It does not run any code from the original input packet, build Lean, run Comparator or access the network. The finite calculations check only the printed examples; they are not proofs for arbitrary input sizes.
