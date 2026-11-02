# Validation record

## Mathematical review

The coordinating analysis reconstructed the proof independently from its mathematical definitions. Two separate AI reviews then checked the complete note and the displayed constants. One review also read the complete lower-bound Lean source and semantic bridges; the other derived the quantitative bounds independently. This is AI review, with no human review or new formal verification asserted.

The checks concentrated on the points capable of changing the theorem: the orientation of a nonsymmetric orthogonal matrix, repeated partial derivatives in the Stein walk, dependence of accumulated weights on earlier Gaussian layers, the zero interpolation endpoint, correlated variables within a Gaussian pair, mass outside the promise, the exact amplification depth, uniformity in the bias, stopping before an unbounded increment, and the binomial factor in the sharp Fourier theorem. All are addressed in the proofs in `note.md`.

The review corrected the two-block endpoint explanation, an omitted lower bound on the number of variables, a few transcription errors, and the citation convention for natural logarithms. It also expanded the elementary maximal-supermartingale argument and the proposed arithmetic statement so their hypotheses and conclusions are explicit. Those corrections are incorporated in the delivered files.

The new sharp and elementary endpoint signatures, as well as their supporting new signatures, remain unelaborated. No successful historical run is presented as checking these additions. See `LEAN_GAPS.md` and `SOURCE_AUDIT.md`.

## Reproduction

The finite checks require Python 3 and NumPy. From this directory, run:

```bash
python checks.py > reproduced_checks.json
```

The delivered output is `checks_output.json`. Integer and rational calculations are exact. Gaussian quadrature is floating point and supplies a finite diagnostic, not a proof of the identity or a certified error estimate. Small last-digit differences across numerical environments are possible.

## Exact checks

The script checks the integer amplification inequality and rational identities used for the elementary constant, the kernel factor, the strict contradiction margin, and the conservative constant. All returned true. It also enumerates all eight derivative supports of a three-variable polynomial under coordinate-dependent random restrictions. The computed expectation and raw-derivative formula agree exactly as rational numbers in all eight cases. These are concrete instances of the proved formulas, not a substitute for their universal statements. [Source: `checks.py`, functions `restriction_check` and `main`; `checks_output.json`, fields `exact_constants` and `restriction_identity`.]

## Numerical identity checks

The script tests all 63 nonconstant Fourier characters with three blocks of size two. It uses a nonsymmetric orthogonal rotation matrix, independent standard Gaussian layers, and a tensor Gauss–Hermite grid. The integral over the scale parameter is evaluated analytically for each monomial. This choice tests matrix orientation and contributions from uniform Fourier degrees above three. [Source: `checks.py`, function `quadrature`.]

| Calculation | Maximum absolute residual |
| --- | ---: |
| Correct identity, 16 nodes per Gaussian coordinate | 0.0000162434653 |
| Correct identity, 28 nodes per Gaussian coordinate | 0.0000004627174 |
| Deliberately omit the scale integral, 28-node grid | 0.0000459879305 |
| Deliberately transpose the matrix coefficient, 28-node grid | 0.0067349823 |
| Deliberately make the matrix nonorthogonal, 20-node grid | 0.0176702561 |

The correct-identity residual decreases on the finer grid. The incorrect variants retain larger residuals. In the nonorthogonal control, a monomial missing an input block has a nonzero expectation, displaying the failure of the uniform-zero-endpoint argument. No numerical accuracy claim beyond the recorded finite evaluations is made. [Source: `checks_output.json`, fields `orthogonal_identity_checks` and `nonorthogonal_control`.]

## File and correspondence checks

`correspondence.json` indexes every display in the note and quantitative analysis, including unnumbered proof steps. The final packaging check verifies JSON parsing, unique statement IDs, required fields, existing dependency targets, exact passage boundaries, display hashes, source declaration names, bibliography keys, and the presence of every requested file. It also checks balanced TeX braces and math delimiters as a transcription aid. These are consistency checks, not Lean elaboration or mathematical verification. Their output is retained in `validation_results.json`.

`STATEMENT_CHANGES.json` records two supporting-document corrections and explicitly distinguishes them from the frozen corpus. `METADATA_CORRECTIONS.json` separately records the incorrect location/kind of the existing Forrelation theorem. No source or corpus file was modified.
