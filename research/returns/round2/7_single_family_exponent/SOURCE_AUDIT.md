# Source audit and evidence boundaries

**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

This audit accompanies `single_family.md`. It records the sources received, the material actually examined, and the difference between supplied historical evidence and work performed in this review. The mathematical result is an explicit single-family refinement of OpenAI's nearly quartic construction. The amplitude-estimation decoder, its generic composition, and the growing-parameter assembly are new mathematical deductions in this submission; they are not reported as newly compiled Lean theorems.

## 1. Received files and integrity

The two user-supplied attachments were:

| Attachment | Bytes | SHA-256 |
| --- | ---: | --- |
| `quartic_r2_7_single_family_exponent.zip` | 4,279,633 | `40f82ef37e4fa1d41b5a3135a7f1af5fd28a9f5d22feeb7e88aa444876fde331` |
| `Pasted text(20261102-145930-2).txt` | 202,498 | `64b819ece1090db3f68db8853e899a241d328963c1ba70b689dee2a87b18d552` |

The transcript contains 202,050 Unicode characters and 2,586 lines. The ZIP contains 292 non-directory members, totalling 11,037,245 uncompressed bytes. Its `manifest.json` lists 290 members; `READ_ME_FIRST.md` and the manifest itself account for the two additional members. During this review, every listed member's extracted bytes were compared with its manifest byte count and SHA-256. All 290 matched; there were no missing members or mismatches.

The manifest records:

* Campaign: `round2`, job `7_single_family_exponent`.
* Repository snapshot: `4c7544f8dcdfc18d3ecf8476ebd8c1090cd46f15`.
* Preprint source: `openai/math 4eaee875`.

The manifest's 290 entries comprise two preprint files, 111 repository files, four writing guides, four exposition exemplars, 74 previous-round files, 93 literature files, one skeleton and `BUILD_STATUS.md`. These are inventory counts, not a claim that each file was read in full.

The supplied preprint PDF has SHA-256

```
a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e
```

This agrees with the prior supplied bibliography. Source locators in this submission refer to this received copy and the received Lean source, not to an assumed future state of the upstream repositories. No input file was edited.

## 2. Actual reading and verification scope

The review was divided into classical constants, quantum constants, and diagonalization/literature, followed by synthesis. The following were the sources used for the mathematical conclusions.

| Source group | Scope of examination |
| --- | --- |
| Task and evidence records | `READ_ME_FIRST.md`, `BUILD_STATUS.md`, `repository/README.md`, `repository/docs/statement_evidence_contract.md`, `repository/corpus/README.md`, and the relevant statement records, evidence graph and dependency metadata were examined. |
| Pasted transcript | All 2,586 lines were read, including the late scope changes and the final incomplete-build status. Truncated tool displays were revisited in smaller ranges. |
| OpenAI preprint | The construction, partial-function promise, quantum and planted lower arguments, and Section 5's quantifier argument were checked against `paper/extracted.md`; the received PDF supplies the pinned publication object. |
| Public definitions and exponent assembly | `Statement.lean` and `Results/Exponent.lean` were read for the function, bit locations, complexity definitions, fixed-parameter package, exponent lemmas, floors and discrepancy estimates. |
| Quantum path | The relevant declarations and proofs in `Forrelation/Repetition.lean`, `Forrelation/Circuit.lean`, and `Upper/{Circuit,Sampler,Decode,Columns,Compile,Amplify,Tournament,Verify,Bound}.lean` were examined to track the decoder, its coherent use, the circuit bound, and every factor in the total query cap. |
| Classical path | `ForrelationLower/Uniform.lean`, its finite contradiction dependencies, and the direct-product/planted interfaces were examined for amplification, the Gaussian-chain constants, the explicit regime, admissible `L`, floors and discrepancy. The mathematical check of the uniform assembly is separate from its uncompiled status. |
| Previous Forrelation-route result | `previous_round/4_forrelation_route_note/note.md` and `quantitative.md` were read in full. Its README, bibliography and evidence descriptions were used as historical context. The adopted route uses the conservative `1/2332800` constant in current source. No new verification of the sharper external-Fourier endpoint is asserted. |
| Adjudication | `funnel_adjudication_notes.md` and `bansal_sinha_section54_second_reading.md` were read. Their verdicts were checked where they affect this task; earlier returns' own claims were not treated as final adjudication. |
| BHMT | The supplied extraction and primary arXiv PDF were checked at the `Est_Amp` algorithm and Theorem 12. The measurement-free preparation, exact Grover iterate, success probability, error formula and power-of-two choice were used explicitly. |
| Bansal–Sinha | The received source archive was opened, and `main.tex` was read at the introductory parameter statements and Section 5.4. The disputed exponent was checked algebraically against the exact received TeX. |
| Other primary literature | Girish–Tal–Wu's paper and version identifiers were consulted for the martingale/Fourier context. Aaronson–Ben-David–Kothari–Rao–Tal's theorem locus and version record were checked for the universal quartic bound. The current numerical model constant was taken from the supplied formal development. Bibliographic metadata was checked against the supplied bibliographies and primary records. |

The four supplied writing guides were read across the review team. The short-paper exemplar was sampled through line 355, including its first complete main proof, for organization and prose. The remaining exemplar material concerns a different theorem and was not used as mathematical evidence.

The entire literature annex and every earlier exposition were not independently re-proved. The current submission does not claim an exhaustive new citation search, a human review, or a line-by-line independent verification of all Lean declarations in the repository. The complete pasted transcript is context; it does not convert historical commands into actions performed in this environment.

All supplied source files needed for the stated deductions were readable. The unavailable items are the raw historical receipts and compiled artifacts listed below, plus a local Lean/Lake installation. No inability to access one of those items has been converted into a positive verification claim.

## 3. Compilation and comparison provenance

### What the received records say

`BUILD_STATUS.md` reports a passed root receipt at commit

```
16adedc16acca1e3a8d2963d4fd5655dcd0492d7
```

It marks the relevant older Forrelation, planted lower-bound, exponent and quantum modules as having compiled `.olean` files newer than their source. It explicitly marks the following as uncompiled:

* `QuarticQuery/ForrelationLower/Uniform.lean`.
* `QuarticQuery/Paper/Section2.lean`.
* `QuarticQuery/Paper/Section3.lean`.
* `QuarticQuery/Paper/Section4.lean`.

It also marks `QuarticQuery/Model/Classical.lean` as having an `.olean` that is **not newer than the source**. These distinctions are preserved. The existence of source text with no `sorry` is not compilation evidence.

The received `corpus/statements.json` records the old fixed-parameter endpoint `QuarticQuery.ForrelationLower.bansalSinhaLower` as built, compared, and proved by an alternative route to the preprint's imported argument. It records `QuarticQuery.theorem_1_1_unconditional` as an exact, unconditional, compared statement, with the fixed-parameter lower threshold in the theorem's established form. None of that metadata constitutes a build of a new uniform or single-family theorem.

The received evidence graph records five positive Comparator bundles, including the unconditional bundle with `--paranoid`, and five negative controls described in their details as altered solutions rejected as expected. Those are historical local runs using `--inadvisably-no-sandbox`. A `passed` field on a negative-control record means its rejection test behaved as expected; it does not mean the altered theorem was accepted.

### Commit-currentness qualification

The supplied adjudication, under “A finding the returns missed,” reports that the root build receipt names `16adedc`, while two declarations it lists, `bansalSinhaLower` and `theorem_1_1_unconditional`, only arrived in commit `06f3eb8`. It concludes that the recorded build ran on an uncommitted tree and calls for a fresh build receipt at a clean pin. The pasted transcript repeats that finding at lines 1874 and 1978.

The same supplied adjudication says the headline Comparator receipt is at `d42fb67`, which contains the source, so that separate comparison evidence is unaffected. This review did not recreate that historical repository or independently recompute those Git diffs. The qualification is reported as a finding of the received adjudication. It prevents treating the receipt's root commit identifier as a complete source-currentness certificate.

The ZIP contains the source, build-status summary, generated statement/evidence metadata, Comparator configurations and dependency graph. It does **not** contain the raw `corpus/receipts/lean-build-root.json`, the full raw Comparator receipt directory, or compiled `.olean` artifacts. Therefore this review did not inspect those underlying receipts or binaries directly. Their relevant contents are known through the supplied summaries and adjudication.

### What was run here

Python's executable lookup returned no `lean` and no `lake` on this environment's `PATH`. No Lean elaboration, Lake build, Comparator run, or external-kernel replay was performed in this review. The new signatures are unelaborated proposals.

The supplied pins, recorded for a future replay, are:

| Component | Pin |
| --- | --- |
| Lean | `leanprover/lean4:v4.36.0-rc2` |
| Mathlib | `69552756cd8a2d2d48763cf7279fd814d6a1224d` |
| complexitylib | `62ca5c21461b2482e8bd12b7cb9b4937d887a33a` |
| CSLib | `254e30e6d4299c51323aaeaf5f51a4763b375d4a` |

These come from `repository/lean/lean-toolchain` and `lake-manifest.json`; they do not certify that their toolchains were installed here. Hash verification and arithmetic checks are reproducibility aids and do not replace theorem proving.

## 4. Transcript scope and final status

The transcript shows an earlier proposal to prepare three papers, followed by a change of scope to seven foundation/research jobs. The current attachment is the single-family job in that revised round. The task remains advisory: derive the theorem, preserve evidence boundaries, and return the requested files for later integration.

The final part of the transcript is particularly material:

* Lines 2283–2426 describe the change to foundation and research work and defer the full papers to a subsequent round.
* Line 2530 reports the seven ZIPs built while the new Lean checks were still pending.
* Line 2553 explicitly says the four new modules were not compiled in those ZIPs.
* Line 2564 reports that, as of 14:58, the check was still on `ForrelationLower/Uniform.lean`, had printed no errors, and had not finished.

There is no later completion receipt in the received transcript. Absence of printed errors during an unfinished process is not a passed build. Historical Mac paths, commands, background-job identifiers, plans to commit, and plans to push were read as project history. They were not executed here and did not authorize access to another machine, mailbox, account or repository.

## 5. The Bansal–Sinha display: precise local finding

The received source is `literature/quartic-ref-06-k-forrelation-optimally-separates-quantum/source.tar.gz`, corresponding to arXiv:2008.07003v3. Its archive SHA-256 is

```
f48a3225662484d12e19bf03412478cf87a388f7c2e33c69a4d7f2078202e015
```

Its `main.tex` has 1,202 lines and SHA-256

```
800119f9f12877392a92e34ac380c61a50b2a297cee0a70511058580061f835b
```

In this exact file, the display's three inequalities occupy lines **1179, 1180 and 1181**. Line **1181** is the problematic final inequality. Line 1184 is the subsequent depth-threshold display. Some supplied notes number the final inequality as 1184. This is a locator discrepancy; the mathematical expression identifies the same step.

Let `Λ=log(kN)`. The Fourier-growth term on line 1180 carries

\[
\Lambda^{(\ell-1)/2}.
\]

The proposed term on line 1181 carries

\[
\Lambda^{\ell(1-1/k)/2}.
\]

Their ratio is

\[
\Lambda^{(\ell/k-1)/2}.
\]

For every fixed `k` and any level `ℓ>k`, this ratio grows without bound as `N` grows. The level range is `k≤ℓ≤k(k−1)`, which contains such levels exactly when `k≥3`. The top-level ratio is `Λ^((k−2)/2)`. Consequently the claimed uniform-constant simplification does not follow from the preceding displayed bound in those cases. For `k=2`, the only level is `ℓ=k`, and this obstruction is absent.

A conservative local correction is to use `Λ^((ℓ−1)/2)≤Λ^(ℓ/2)` for `Λ≥1`. The resulting geometric-series argument supports a depth scale proportional to

\[
\frac{N^{1-1/k}}{k^{28}\log(kN)}
\]

for the amplified tree, and the corresponding `k⁻²⁹` scale at fixed bounded error. The supplied adjudication derives the sharper local denominator `log(kN)^(1−1/(k(k−1)))`. The present single-family proof uses the separate uniform Gaussian-chain bound and requires neither repair as an input.

The conclusion is confined to the displayed simplification and what follows from those displayed ingredients. It does **not** prove that Bansal–Sinha's Theorem 1.3 is false, nor establish that no different proof can give its stated logarithmic exponent. The slow-growth discussion and the qualitative separation consequences do not require that precise exponent. The manuscript does not rely on a presumed erratum or a presumed absence of later work.

## 6. Quantifier wording and priority

`READ_ME_FIRST.md` characterizes the preprint as remarking that growing `k` requires uniform estimates. The supplied preprint's literal Section 5 text, at `paper/extracted.md:703–704`, says that `k` remains fixed as `m` tends to infinity. No separate growing-`k` remark was located in the received preprint. Accordingly the manuscript identifies the fixed-parameter quantifier order and explains why this new quantitative assembly tracks constants uniformly; it does not attribute an invented quotation to the preprint.

A qualitative diagonal family already follows from the established fixed-parameter theorem by choosing increasing thresholds. Bansal–Sinha's discussion before Corollary 1.4 already considers slowly growing parameters for the partial problem. The new contribution claimed here is the explicit uniform parameter schedule, its quantified exponent loss, and the fully specified decoder refinement for this construction. No priority claim is made for diagonalization, slow parameter growth, or amplitude estimation.

## 7. New claims and their mathematical/formal boundary

The source one-shot theorem is `QuarticQuery.Upper.forr_samples`, `Upper/Decode.lean:309–310`. It supplies coherent success probability `Φ²` with `k` abstract reads. Its underlying `phaseRead` gives a direct phase-kickback implementation using `k` physical queries. BHMT Theorem 12 is a new input to the decoder proof in this submission; the preprint's original use of BHMT concerns amplitude amplification.

The original `Upper.Fkm_QLe` requires the old repetition-count hypothesis and constructs its laws from `decodeProb`. A smaller numerical count cannot be substituted into that theorem. The manuscript proves a generic composition argument from a normalized, reindexable coherent `Samples` decoder, retaining all phase labels and work registers. The exact controlled Grover iterate includes its minus sign. Promise correctness and a fixed cap on every input are separate properties, both established in the mathematical argument.

The proposed BHMT interface uses at most `2qM` abstract reads. The decoder therefore uses at most `128 k 2^(5k) h` abstract reads, and the existing `Samples.runs` compiler gives the physical cap `256 k 2^(5k) h`. A separate proposed `Runs` theorem records that physical conclusion. The manuscript deliberately uses the larger physical cap as a conservative abstract cap for its final upper bound, so its stated constant includes the additional slack.

The following remain new formal obligations: the BHMT decoder and its majority amplification; the generic decoder wrapper; the revised budget; the growing-parameter/floor inequalities; and the single-family theorem. The supplied uniform lower assembly is also pending compilation. `NEW_STATEMENTS.json` and `LEAN_GAPS.md` record the proposed statements and interfaces. The new bound is a mathematical result in this submission, with formal verification explicitly outstanding.

## 8. Bibliographic mapping and version conventions

`single_family.md` uses numeric references. `references.bib` covers all five:

| Manuscript number | BibTeX key | Source of version and locator |
| --- | --- | --- |
| [1] | `OpenAI2026` | Received preprint, date 5 October 2026, source revision `4eaee875` and verified PDF hash |
| [2] | `BHMT2002` | Published chapter; arXiv:quant-ph/0005055v1, Theorem 12 on printed page 19 |
| [3] | `BansalSinha2021` | STOC publication; arXiv:2008.07003v3, 17 November 2020; received original TeX |
| [4] | `GirishTalWu2021` | CCC publication, DOI `10.4230/LIPIcs.CCC.2021.39`; arXiv:2103.11604v2, 13 May 2021 |
| [5] | `ABKRT2021` | STOC publication; supplied arXiv:2010.12629v1, 23 October 2020 |

For Girish–Tal–Wu, the relevant result is Lemma 1.9 in arXiv numbering and Lemma 9 in conference numbering. For Aaronson–Ben-David–Kothari–Rao–Tal, the supplied extraction loses some degree/sensitivity macros and restatable numbering; the bibliography uses the printed Theorem 2. The constant `20736` is credited to the supplied formal model bridge, without attributing that explicit constant to the external paper.

The primary arXiv records and relevant PDFs were consulted for BHMT, Bansal–Sinha and Girish–Tal–Wu. Official OpenAI repository search results were also obtained. A later direct reopening of the official preprint folder failed in the web tool; the locally received, hash-verified preprint remained available and supplies the textual evidence. No conclusion depends on that transient web failure.
