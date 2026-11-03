# Round-five quantum mechanism return

This archive contains an independent critique of the frozen expert companion and student exposition. It contains **38 located findings: 26 corrections and 12 keeps**. No manuscript, proof or repository source has been rewritten.

## Read in this order

1. `verdict.md` — the overall judgement and five priorities, kept to a one-page-length note.
2. `findings_readable.md` — the complete critique, with exact quotations, explanations and evidence.
3. `findings.json` — the same findings in the requested integration format, bound to the supplied draft hashes.
4. `sources_and_scope.md` — primary citations, edition-specific locators, reading coverage and limits.

The other files make the return checkable:

| File | Purpose |
| --- | --- |
| `SOURCE_STATUS.json` | Unchanged copy from the input packet. |
| `validation.json` | Exact-quote checks, source line positions, input hash/CRC checks, sampled link checks and finite example checks. |
| `CHECKSUMS.sha256` | SHA-256 of each other return file. It intentionally does not hash itself. |
| `validate_return.py` | Standalone Python 3 validator using only the standard library. |

## Interpretation

Severity counts are **3 high, 19 medium, 4 low and 12 keep**. There are no critical findings. The three findings with category `error` concern local mathematical statements or an incorrectly labelled counterexample; they do not allege that the quantum upper bound fails. Other findings distinguish missing instructions, unclear explanations, credit, presentation and evidence navigation.

The review does not claim a new Lean build or Comparator run. It respects the packet's instruction to treat the newest additions as the stated working-draft condition. It does not ask for new results, new constructions or new formalisation.

## Verify after extraction

Run from this folder, or give the script's full path:

```bash
python3 validate_return.py
```

To repeat the checks against the original extracted input packet, additionally supply its root folder, containing `READ_ME_FIRST.md` and `repository/`:

```bash
python3 validate_return.py --packet /path/to/extracted/input_packet
```

The return is self-contained as a critique. The optional source check needs the original input; the source manuscripts and literature are not duplicated in this archive.
