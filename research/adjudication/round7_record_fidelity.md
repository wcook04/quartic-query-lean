# Round-seven reasoning-record fidelity reread

An independent AI reader inspected every changed passage-body diff between
`1e60214:docs/reasoning_record.md` and the final record with SHA-256
`d5d1ff5eaebc4d2f7b7a99e0ba12a6e9aac8876875a5badd50fad7b8702cb3ba`.
No concrete mathematical defect was found in the revised wording within the
scope below. This is a revision-fidelity check, not a new certification of every
proof in the record, a human review, or a novelty assessment.

The original assigned revision had 102 changed passage bodies. All 102 diffs
were read, including their added and removed mathematical text. The later
`CL-planted-interface` wording change and the final three render repairs were
then inspected. One repair concerns the already changed `forr_coherent` passage;
the other two change `history-construction-evidence` and
`history-appendix-a-evidence`. The final independent census is therefore **105
changed and 193 byte-identical passage bodies**, out of 298. The companion
[passage dispositions](round7_record_fidelity.json) give old/new body hashes and
a review disposition for every one of those 105 passages. Earlier acceptance
was not automatically transferred to reworded text.

The baseline record hash is
`41d6dae58694ff9010d417997dc40e95c3486b9133dc2a125c6843665f902d63`.
The initial revised edition, also read, was
`193f698b2a8383864b229e44df3f3fcce853aa23c9f489f2cf7c097f15f218af`;
the intermediate one-word edition was
`3298d076249aa85e15b00f8e66574d882e799647f406ee2486ab9130b18457b0`.

## What was checked directly

The read covered all actual old/new diffs. Current passages were read in full
where the new explanation required mathematical context, particularly the
analytic tree example, uniform assembly, growing-parameter calculation, model
bridges and Appendix A source correspondence.

| Revised object | Direct check and result |
| --- | --- |
| `forr_tree_growth`, `forr_tree_leaves` | For degree two and revealed set `{a,b}`, the old term is `c({a,b}) ξ_a ξ_b`; a fresh query adds exactly `ξ_q(c({a,q}) ξ_a+c({b,q}) ξ_b)`. The parenthesized coefficient is history-measurable, and the fresh centered factor has conditional mean zero. The leaf wording still denotes the terminal value of the same process, with each distinct queried coordinate counted once. |
| `forr_advantage` | The added scale explanation follows from (F33): for fixed k the main factor is proportional to `m^{-(k-1)/2} d^{k/2}`, apart from constants and logarithms. Its constant scale is `d ≈ m^{1-1/k}`. This is a scaling explanation, not an additional finite lower-bound theorem. |
| `forr_uniform_assembly` | The two k losses come from the derivative-growth factor and the amplified depth `50kD+1`. The existing finite proof and dimension premise remain intact. All seven display-math strings in this passage are unchanged. |
| `ROOT-GROWING-K` | Recomputed the explanation of the balance `40k+ℓ/k`, minimized at `sqrt(ℓ/40)`, and checked the floor identity `40(k-x)^2/k<20` for `k=floor(x)≥2`. The ensuing constant 237 gives 474 after multiplication by two; replacing 474 by 508 is conservative. All nine display-math strings in the passage are unchanged. The conclusion remains an exponent tending to four, without asserting `R=Ω(Q^4)`. |
| `R3-01-QUANTIFIERS` | For nonnegative `α<4`, an integer `k>2/(4-α)` makes `2-1/k-α/2` positive. Constants and thresholds are chosen after this fixed k. The complete quotient remains in §7.1; the overview does not claim uniformity from a fixed-k theorem. |
| `R3-01-ADAPTIVE` | `Statement.lean::QLe` explicitly disjoins `ConstantOnPromise` from one normalized state/program chosen before all promised inputs. The new empty-coordinate explanation matches that definition. The branch-norm example retains the 1/4 and 3/4 probability weights. |
| `R3-01-BRIDGES` | `Bridge/Deferred.lean::FixedSim` has separate `embed`, `embed_phase`, `entry` and an all-input/all-starting-vector mass specification. `FixedSim.query` uses the intertwining embedding and an input-independent gate extension. `exists_fixedSequence` has exactly the stated acceptance-mass guarantee. The added invariant explanation does not upgrade it to equality of returned states. |
| `forr_distribution`, `forr_path_formula`, `forr_historical_threshold` | The replacements of local `ℓ=k-1` by h, or by `k-1` in product ranges, preserve every endpoint and exponent. The path formula has one factor per Gaussian link. |
| `forr_circuit`, `forr_circuit_size` | The new residue explanation agrees with the existing modular computation and final signed-range argument. The upward coefficient rounding follows from `337a²mt²≤800a²mt²=200a²m(log₂m)²`; it does not claim optimization or a newly compiled cost identity. |
| `R3-A-HUANG`, `R3-A-FORMAL` | The signed-matrix and supported-eigenvector argument agrees with the primary sources below. The formal parity argument was moved to the formal appendix. `huangEnd_parity` supplies the anticommutation, and its involution exchanges the two eigenspaces for positive dimension. Square and trace facts are separate declarations, as stated. |
| `R3-A-MIDRIJANIS` | The maximal-monomial procedure uses only nonconstant restrictions. Each round produces a sensitive block at the same original input, inside a newly queried support; disjointness across rounds and the product bound agree with the original proof. Removing the unused Theorem 5 warning changes no attribution or bounded-error premise. |
| `forr_ssw_comparison` | The revised wording correctly limits the cancellation to the multiplicative k from amplification. It no longer suggests that every k-dependence disappears; logarithmic/input-size parameters and the unspecified external constant remain. The external Fourier theorem was not reproved here. |

The new local gate example reads the actual input bit and two transcript bits,
so its depth is three. The four-column check has
`4+3+360+2+2=371` local tests and
`4[4+16+4(6+360)]=5936` input bits. The verifier's newly stated unamplified
probabilities `1/371, 2/371, 1/371` follow directly from the retained failed-test
counts. These are arithmetic checks of the explanation, not a fresh execution
of the returned board checker.

## Reused audit scope, after reading the new words

The [quantum audit](round7_quantum_audit.md) was read at SHA-256
`ec3bfada3abdf57fa2ebac1af4c2d9f23affe42f10b64f2db3fb5a33f7dbfcef`;
the [classical audit](round7_classical_audit.md) at
`12b168ea3df28ff155bc06c763ac8e10c8be20eb0d77114dbf87ae3a32359153`.
Their conclusions were reused only after inspecting the corresponding revised
passage diff. The JSON distinguishes those dispositions from direct additional
source checks and edits with no new mathematical meaning.

In particular, the quantum revisions retain a fixed, accessible success
projector, an all-branch cap, successful-state versus measured-label
distinctions, exact complementary comparison probabilities, fresh comparison
workspaces, stopped coupling and all-address verification. The fractional
loser-weight example is explicitly abstract. The final factor-two wording
continues to point to the formal `2qk` physical cap and the register boundary.
The unproved physical output-subsystem transport is still explicitly unproved;
the measured/reset route is not described as a dependency on the separate
opaque state-preserving theorem.

The classical revisions retain one minimax law chosen before independent
samples, a fixed-column/fixed-time joint event, the time union, the shared
simulator cap, independent outside data and the column average. The extra
`hard distribution` to `hard law` edit changes none of those requirements.
Final history sentence splits preserve per-name audit membership and the
post-root timing and selected-declaration scope. They do not assert a new run.

## Primary sources and maintained source boundary

Targeted primary-source reads were used for the scope not supplied by the two
round-seven audits:

- [Girish–Tal–Wu, arXiv:2103.11604v2](https://arxiv.org/pdf/2103.11604v2),
  §1.3 and Lemma 1.9, printed pp. 6–8: the contraction and fresh-coordinate
  martingale mechanism are antecedents; the record's biased raw-derivative
  constants remain its own supplied argument.
- [Huang, Annals 190 (2019)](https://annals.math.princeton.edu/wp-content/uploads/annals-v190-n3-p06-s.pdf),
  Lemma 2.2, printed p. 952, and the spectral-radius remark on p. 953:
  the signed square, trace multiplicities and spectral consequence have the
  claimed locators. This was the published edition, rather than substituting
  arXiv pagination.
- ABKRT, arXiv:2010.12629v1, Theorem 1 and §3, printed pp. 6–7,
  local primary PDF SHA-256
  `445a34b0653042ad482bd95bc2c333d476df7ade6ce5d9ec45714f5b249e39ab`:
  the supported positive-eigenvector and absolute-value argument matches the
  record's use.
- Midrijānis, arXiv:quant-ph/0403168v2, Lemma 3 and the proof of Theorem 4,
  printed pp. 3–4, local primary PDF SHA-256
  `0cdb580bd48d513b33a1c65bd27faa361bd2e4ebaceff29bbf24b16586e4ab21`:
  the product bound occurs inside the proof, while the displayed theorem is
  the subsequent cubic degree bound.

Selected maintained Lean sources were read, not rebuilt:

| Source | SHA-256 as read |
| --- | --- |
| `lean/QuarticQuery/Statement.lean` | `21e9421899572827f8051a2747412792971b0415e45ade85e434219b9badaced` |
| `lean/QuarticQuery/Bridge/Deferred.lean` | `666c5741a5a19324b7229a350bc35130627da42584c751d5444231f402c45931` |
| `lean/QuarticQuery/Paper/AppendixAHuangMatrix.lean` | `a90282494f069991f80b7ec4af0cd8898a2d4b84a7a69aa180e1ed061dd9a549` |
| `lean/QuarticQuery/ForrelationLower/Uniform.lean` | `d6bc1f4399394810fca63abdaadd67a420616371c501ab978841898f2bda049c` |

## Preservation and limits

An independent parser comparison found the same 365 unique HTML anchors and
298 unique passage IDs. The claim-marker multiset is unchanged: **261 marker
occurrences representing 185 unique claim IDs**. The principal displays (F33),
(F43), the growing-k calculation and the Huang/Midrijānis displays checked
above are byte-identical within their passage bodies. The new degree-two
display is explanatory; other changed displayed formulas use dummy-index or
link-count renamings, or relocate the fuller quotient explanation to its
existing proof.

`git diff 1e60214 -- lean` was empty when inspected. No Lean build, Comparator
run or returned review program was executed, and no manuscript was edited by
this reader. This audit does not independently re-prove the entire unchanged
Gaussian interpolation, stopping estimate, external Fourier theorem, classical
direct product or quantum construction. It supplies the missing reread of the
changed words, reuses the explicitly named audits for their established scope,
and separately checks the new explanations and selected source correspondences.
