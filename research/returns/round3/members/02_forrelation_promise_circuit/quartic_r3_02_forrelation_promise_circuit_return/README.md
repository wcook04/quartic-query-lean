# Forrelation promise and circuit: round-three section return

This return replaces **§§3.1–3.5** of the supplied long reasoning record. It gives the normalized Forrelation definition, asymmetric promise, exact integer tests, coherent quantum preparation and output law, exact modular Boolean circuit, and a complete small-instance calculation. It uses the bit-query model of §2.2 and supplies the quantum and circuit conclusions consumed by §3.17. The classical lower bound remains outside this assignment.

Start with [section.pdf](section.pdf) for reading or [section.md](section.md) for the editable text and stable passage anchors. This is an advisory section return; it is not a final integrated paper or acceptance of its contents.

## Files

| File | Purpose |
| --- | --- |
| [section.md](section.md) | Complete replacement §§3.1–3.5, including ordinary proofs and exact citation locators. |
| [section.pdf](section.pdf) | Rendered reading copy of the section. |
| [correspondence.json](correspondence.json) | Passage boundaries, statement IDs, actual Lean types, premises, routes and evidence distinctions. |
| [NEW_STATEMENTS.json](NEW_STATEMENTS.json) | Exactly three supplemental statements: the literal coherent-state law, the matched three examples, and the closed-form circuit accounting. |
| [STATEMENT_CHANGES.json](STATEMENT_CHANGES.json) | Empty array: no canonical mathematical statement was changed. Evidence updates are recorded separately. |
| [LEAN_GAPS.md](LEAN_GAPS.md) | Exact formal correspondence and verification limits, in section order. |
| [references.bib](references.bib) | Mathematical sources with version and locator information. |
| [source_read_receipt.json](source_read_receipt.json) | Assessed, sampled, unavailable and unassessed source scope. |
| [review_notes.md](review_notes.md) | Located corrections, simplification decisions and the paper-authoring receipt. |
| [STYLE_RULES.json](STYLE_RULES.json) | Source-located writing moves used, with exemplars kept separate from mathematical authority. |
| [checks/exact_example_checker.py](checks/exact_example_checker.py) | Standalone exact arithmetic and Boolean-gate checker. |
| [checks/exact_example_results.json](checks/exact_example_results.json) | Deterministic output from the checker executed in this return directory. |
| [checks/audit_evidence.py](checks/audit_evidence.py) | Rechecks the supplied source bytes and recorded evidence bindings without running Lean. |
| [checks/validate_return.py](checks/validate_return.py) | Structural/package checker; optional `--packet` enables additional source-hash checks. |
| [checks/render_section.py](checks/render_section.py) | Pandoc/XeLaTeX rendering helper, with the supplied layout and header files. |
| [evidence/](evidence/) | Detailed source/receipt audits, recorded Lean types, scoped reading records and independent reviews. |

The archive manifest records final member sizes, hashes and source versions.

## Reproduce the finite checks

From this return directory, using Python 3.10 or newer:

```sh
python checks/exact_example_checker.py --help
python checks/exact_example_checker.py --json checks/exact_example_results.json
```

Both commands were executed successfully. The checker needs only the Python standard library. It writes the specified JSON result and prints the same result; it does not modify the section or source packet.

The checker compares direct path summation, dense Walsh multiplication, butterfly arithmetic, exact rational promise tests, and an independently written reconstruction of the supplied fan-in-two Boolean constructors. It also checks the final residue words and sign bits.

| Complete input family | Inputs | One | Zero | Undefined | Reconstructed gates |
| --- | ---: | ---: | ---: | ---: | ---: |
| $k=2,t=1$ | 256 | 104 | 48 | 104 | 3563 |
| $k=3,t=1$ | 4096 | 1472 | 1152 | 1472 | 7275 |

An additional 8193 synthetic numerators at $k=2,t=4$ check exact threshold equalities, a positive gap case and signed comparison recovery. Their realizability by actual sign inputs is not asserted. The universal claims have ordinary proofs in the section; these finite checks are independent consistency evidence.

## Recheck evidence bindings and package structure

To recompute the source/receipt audit, retain the original ZIP and its extracted input packet, then run:

```sh
python checks/audit_evidence.py --help
python checks/audit_evidence.py --packet /path/to/extracted/input_packet --archive /path/to/original.zip --output /path/to/new/audit_output
```

The help command and the audit invocation were checked successfully during preparation. Replace the example paths with the retained inputs and a new output directory **outside the preserved input packet**. The `--archive` argument is optional; it adds the original ZIP's SHA-256. This script checks file hashes, recorded receipt bindings, selected declaration membership and the recorded axiom-audit results. It writes new JSON reports and does not execute Lean, Lake or Comparator. The delivered audit details are under `evidence/`.

The return's structural/package checker can be run on its own, or with the extracted packet for source-hash checks:

```sh
python checks/validate_return.py
python checks/validate_return.py --packet /path/to/extracted/input_packet
```

These checks concern the package, references and evidence bindings. They are not mathematical proof checking or a substitute for Lean compilation.

## Regenerate the reading PDF

To regenerate the PDF where Pandoc, XeLaTeX and the fonts named by the helper are installed:

```sh
python checks/render_section.py
```

This helper takes no command-line options and writes `section.pdf`. The mathematical source remains `section.md`; the exact arithmetic checker is independent of the PDF toolchain.

## Source versions and evidence boundaries

The assigned ZIP is `quartic_r3_02_forrelation_promise_circuit.zip`, whose repository snapshot is labeled `1dd469dd0042b937b739da3bc211eeb60bdf7462`. Mathematical conventions are taken from the supplied OpenAI preprint, the inspected Aaronson–Ambainis edition and Bansal–Sinha v3, with the project specialization $m=4^t$ retained throughout.

The additional attachment **`Pasted text(20261102-190823).txt` was unavailable**. Its contents were not read, reconstructed or used. The available ZIP contains the complete scoped assignment followed here; any additional instructions in the missing text would need to be reconciled when it becomes available.

The return distinguishes current integrated Lean source and its supplied source-bound native/root receipts from historical candidate copies and old `UNELABORATED` comments. Those records were inspected; **this review did not run Lean, Comparator or a kernel census replay**. The independently written Python Boolean reconstruction is not extracted or compiled Lean code.

Three qualifications remain explicit:

- The ordinary phase construction uses $qk$ bit queries. The supplied complete formal implementation uses the generic compiler's $2qk$ cap; the local phase identity alone is not an end-to-end formal `Runs k` witness.
- The explicit tensor-register state is proved ordinarily. The supplied retained-isometry theorem is not an exact formal identification with that literal register representation.
- The circuit's `Enc` invariant is modular. Its correct final signed comparisons and Boolean outputs do not require a theorem identifying every intermediate stored word with an unrestricted signed integer.

The three new entries do not invent Lean signatures or claim newly compiled results. The first gives an ordinary state/law construction; the second combines exact examples with an already retained census; the third gives an ordinary closed-form accounting of the existing circuit. The section does not prove the later classical lower bound, settle the separate question of letting $k$ grow, or claim an exact fourth-power separation for any fixed $k$.
