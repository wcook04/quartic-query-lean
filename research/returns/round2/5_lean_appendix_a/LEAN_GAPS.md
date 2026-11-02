# Lean gaps and proof-route qualifications

## Status applying to every entry

All new Lean modules in this return are **unelaborated**. `lean`, `lake` and `elan` were absent from PATH. No new kernel build, Comparator run, external-kernel replay or compiled dependency extraction was performed. The supplied historical build receipts have not been replayed. Static source review and finite calculations do not establish that a proposed proof script elaborates.

The final candidate `QuarticQuery.Paper.appendixA_D_le_Q_pow_four` has a full proposed proof body. Its ingredients are the arbitrary-matrix adversary theorem, both literal adversary applications, the genuine-face/recursive-matrix Huang theorem, and the exact Midrijānis bridge. There is no deliberately assumed Perron witness, per-query bound, face transport, graph embedding or A.4 conclusion left in that final statement. The verification gap is compilation of the proposed source and its dependencies.

The entries below follow `blueprint.md`'s mathematical reading order. “Proposed exact” refers to the statement and written proof, not kernel evidence.

| Row or display | Evidence supplied | Remaining verification or qualification |
| --- | --- | --- |
| Initial quartic result / `thm-A.1` | `appendixA_D_le_Q_pow_four`, `appendixA_theoremA1`; full source assembly | Entire new dependency chain must elaborate. The literal Huang route is used, with the local multiplicity substitution below. No new compiled reach claim. |
| `def-deg` | Low-degree/Fourier equivalences, sign conversion and constant-degree theorem | New wrappers uncompiled. A separate syntactic `MvPolynomial` uniqueness theorem is not supplied; the library's function-space and polynomial-evaluation degree correspondence is the meaning used here. |
| `def-bs` | Exact sensitive-block nonemptiness equivalence and finite-supremum definition | New wrappers uncompiled. Empty families and constants are included. |
| `def-Gamma-i` | Exact mask, explicit Euclidean operator norm and finite maximum | New definitions and coercions uncompiled; positivity of the denominator is proved in source before division. |
| `claim-perron` | Compact Rayleigh maximization with absolute vectors; unconditional existence for symmetric nonnegative Γ | New proof uncompiled. Operator-norm/Rayleigh coercions and inferred finite-dimensional instances are compiler checkpoints. No irreducibility or positive-semidefinite premise is assumed. |
| `def-adv-progress` | Exact complex-valued Γ progress; initial value and gate invariance | New source uncompiled. The original private absolute-overlap progress is a different definition and is not evidence for this definition. |
| `claim-per-query` | Arbitrary-input oracle identity, full quadratic bound and operator-norm bound | New proof uncompiled. Active controlled-phase pieces have total squared norm at most one, replacing the paper's all-register equality by the sufficient inequality. Same final bound and same query cap. |
| `claim-final-overlap` | Standalone arbitrary unit-state result, algorithm-state specialization and weighted final sum | New source uncompiled. Local presentation change: use the library's squared measurement-splitting inequality, then specialize the probability thresholds. The library supplier itself uses the paper's Cauchy–Schwarz mechanism. |
| `lem-A.2` | Full general nonnegative spectral adversary, explicit coefficient one thirty-fifth | New source uncompiled. Conditional progress helpers are discharged by named proofs; they are not outstanding hypotheses of A.2. Original deferred-measurement ties remain partial. |
| `def-Sf` | Exact adjacency predicate and Euclidean norm bridge | New wrappers uncompiled. No normalized adjacency or ordinary sensitivity substitution is made. |
| `lem-A.3.bs` | Literal star construction, exact star norm, masked-edge contraction, cap and minimum bounds | New source uncompiled, especially finite Cauchy–Schwarz and Euclidean sum rewrites. The optional coefficient 16 wrapper follows the polynomial method and must keep an alternative route label. |
| `lem-A.3.lambda` | Γ equals sensitivity adjacency; explicit masked action and partial-matching norm bound | New source uncompiled. The retained coefficient 36 wrapper uses the prior specialized progress proof. |
| `lem-A.3` | Explicit uniform conjunction with coefficients 1225 and 35 | New source uncompiled. This is a stronger numerical formal statement than the original informal big-O conjunction; it is registered separately. |
| `claim-restrict-parity` | Genuine `Fin #S` face, normalized Fourier identity, every outside assignment, explicit sign/parity fiber and edge transport | New source uncompiled. `Finset.equivFin` is noncomputable and the dependent definitions are marked accordingly. The earlier ambient-only fiber wrappers no longer constitute the final supplier for the row. |
| `def-huang` | Literal recursive matrix, ordinary cube equivalence and entrywise absolute adjacency | New source uncompiled. Recursive `Fin.cases` and adjacency simplification are elaboration checkpoints. No definitional equality with complexitylib's directional operator is claimed. |
| `claim-huang-spectrum` | Symmetry, square, trace, eigenvalue classification, exact positive and negative multiplicities | **Local alternative route:** multiplicities are obtained from parity anticommutation, although trace zero is also proved. The standalone statement needs d at least one. All proposed scripts are uncompiled. |
| `claim-interlace` | Supported positive eigenvector via a dimension-kernel argument and induced unsigned Rayleigh inequality | New source uncompiled. Its spectrum premise is supplied by the exact theorem proved through the preceding local alternative. No general Cauchy interlacing theorem is asserted to have been imported. |
| `lem-A.4` | `appendixA4_paper_route`: actual face, recursive matrix, supported vector, explicit injective zero extension and norm comparison | New source uncompiled. The companion `appendixA4` is an alternative full-cube directional route and is retained separately. The final assembly calls the paper-route theorem. |
| `claim-round-block` | Separate maximum-support, fixed-original-input transport, disjointness and round-count theorems | New source uncompiled. No second execution-trace datatype for the complete pseudocode is supplied. The exact mathematical round ingredients and the imported recursive decision-tree construction are the evidence; do not claim a separately verified trace implementation. |
| `lem-A.5` | Exact library theorem transported through `D_totalise_eq_complexity` | New wrapper uncompiled. The source proof uses the same maximal-monomial mechanism, expressed in Fourier supports and induction on decreasing block sensitivity. |
| Explicit cap and minimum constants / assembly | `appendixA_degree_le_of_QLe`, `appendixA_D_le_of_QLe`, `appendixA_D_le_Q_pow_four`, `appendixA_universalPower_four` | New source uncompiled. No assertion of novelty or improvement over the numerical constant 20736. |
| Optional hybrid coefficient 19600 | `appendixA_D_le_Q_pow_four_hybrid` | New source uncompiled; **alternative block-sensitivity route** through the polynomial method. |

## Source-coefficient checks

`SOURCE_CORRECTIONS.json` records the annex's extra-square-root transcription error and the separate direct check of the publisher's error prefactor against two-bit parity. The complete calculation is in `SOURCE_COEFFICIENT_CHECK.md`. The printed coefficient is not silently substituted into the new Lean theorem.

The supplementary displays below have **no implemented Lean proof in this return**. Their proposed signatures are in `NEW_STATEMENTS.json`, using the existing statement vocabulary and pinned library definitions. The finite witness is supported by an explicit mathematical calculation and exact integer/rational checks; the general-error bound is additionally stated in Høyer–Lee–Špalek, Definition 1 and Theorem 1, p. 3 of the inspected author PDF.

| New statement | Current evidence and gap |
| --- | --- |
| `new-A-parity-two-exact-query` | Explicit normalized state, one ordinary oracle call, index Hadamard and deterministic output; checked for all four inputs. Its exact-success adaptive-program signature is proposed but unimplemented. |
| `new-A-parity-two-adversary` | Explicit matrix, orthonormal character eigenbasis and permutation masks. Exact arithmetic verifies the certificates. No new Lean matrix-norm theorem for this particular finite witness is supplied. |
| `new-A-positive-error-arithmetic` | Exact comparison at error one hundredth and the resulting contradiction with the printed prefactor. The scalar proposed Lean theorem is unimplemented. |
| `new-A-progress-factor-two-saturation` | Exact calculation of the initial and final progress values for that witness; unimplemented Lean signature. |
| `new-A-general-error-adversary` | Primary-source theorem and the same mathematical progress proof for general error. The implemented new arbitrary-matrix theorem fixes error one third; an arbitrary-error fixed-sequence generalization is proposed, not implemented. No new adaptive complexity definition indexed by error is exported. |

## Work after compilation

Compile the returned module tree at the exact project and dependency pins. Record the successful command, source hashes and toolchain. Inspect the final declaration's axioms and extract its actual dependency closure. If the project wants Comparator evidence for these rows, prepare independent challenges for the exact types and run them; no such run is included here. Keep statement fidelity, proof route, build, comparison and reach as separate fields.

The static checker in `checks/validate_return.py` checks file and metadata integrity only. Its passing output must not be reported as a Lean build or a corpus-schema-validator receipt.
