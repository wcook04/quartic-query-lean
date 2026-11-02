# Exact finite checks for the model section

These checks reproduce the numerical examples and finite controls accompanying `section.md` §2.6. They use separately specified Python objects. They do not import, parse, execute or compare the Lean implementation, and their success supplies no new Lean, Lake, Comparator or external-kernel evidence.

## Run

Use Python **3.10 or newer**; only the standard library is required. The recorded execution used Python 3.12.14. Run the following from the extracted return's root directory:

```sh
python3 -E checks/check_models_exact.py > checks/classical_exact_output.json
python3 -E checks/quantum_controls.py > checks/quantum_exact_output.json
python3 -E checks/semantic_controls.py > checks/supplied_semantic_controls_output.json
```

Each command should exit with code zero and print one JSON object. The first two scripts use assertions; run without `-O` or `-OO`. The `-E` option ignores Python environment variables, including `PYTHONOPTIMIZE`, so it prevents that environment variable from disabling the assertions. No network access, package installation, Lean toolchain or external files are needed by these programs.

## Checks and outputs

| Program | Recorded output | What it checks |
| --- | --- | --- |
| `check_models_exact.py` | `classical_exact_output.json` | Exact classical success probabilities and caps; the one-bit identity and one-label/empty promises; all ten syntactic trees of depth at most one on two coordinates and their six distinct truth tables; the classical OR₂ obstruction under the uniform distribution on `00,01,10`; the XOR₂ obstruction under the uniform distribution on four inputs; exact positive/zero/negative Forrelation values for a two-layer, four-coordinate instance; small expected-query parity examples. |
| `quantum_controls.py` | `quantum_exact_output.json` | Both bit/controlled-phase Hadamard conjugacies; the idle `|+⟩` and phase-kickback `|−⟩` identities; all four inputs of the explicit OR₂ selector construction; all four inputs of one-query two-bit parity. Common square-root normalization factors are squared symbolically, leaving exact rational arithmetic. |
| `semantic_controls.py` | `supplied_semantic_controls_output.json` | The packet's independent finite controls and seven deliberately incorrect model variants. The baseline must have no mismatches and each variant must fail its designated expected answer. A deliberately shared impossible comparison specification demonstrates agreement of two finite truth tables without semantic validity. |

`exact_checks_execution.json` records the interpreter version, commands, successful exit codes, empty standard error, output parsing, and SHA-256 digests of the scripts and outputs. This is a Python-execution record, not a proof certificate.

## Custody

`semantic_controls.py` is copied byte for byte from the input packet's `repository/tools/return_checks/semantic_controls.py`. The copied quantum checker is also byte-identical to the reviewer-authored checker. The classical checker's only change is in its module docstring: the reference to the intermediate `classical_review.md` is replaced by `section.md` §2.6. Its executable code is unchanged. The custody details and original semantic-script digest are in `exact_checks_execution.json`.

## Return-package checks

Run `python3 -E checks/validate_return.py` to check required files, exact passage boundaries, all displayed equations, statement IDs, source types, bibliography keys, recorded script/output hashes and the internal manifest. When the original input packet is available, pass `--source-packet /path/to/extracted_input` to compare each source signature with its original file. The final output is saved as `return_validation.json`. This validator checks document and evidence consistency; it does not compile mathematical proofs.

## Limits

All arithmetic in these scripts uses integers or `fractions.Fraction`, with no floating-point approximation. The classical enumeration is exhaustive only for the stated two-coordinate, depth-one trees. Its distributional upper bounds apply to mixtures by linearity; the ordinary argument, including the quantifiers, is given in the section. The expected-query parity cases are finite examples through six bits, not an exhaustive search over expected-query algorithms.

The quantum checker evaluates the specified small algorithms; it does not optimize quantum success probability, and it does not claim that `2/3` is optimal quantum one-query success for OR₂. None of the scripts proves general model equivalence, verifies the separation theorem, checks the semantic correctness of the source definitions, establishes current dependency closure, or reruns a comparison. In particular, the shared-bad-specification control is a Python truth-table example and is not a Comparator execution or a prediction of a particular Comparator run. The complete mathematical proofs and the separate source-bound evidence must retain their own status.
