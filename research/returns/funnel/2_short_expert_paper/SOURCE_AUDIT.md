# Source and verification audit

**Date:** 2 November 2026. **Status:** AI authoring and source review. No person has reviewed the mathematics, the Lean development or this return. No fresh Lean build or Comparator execution was performed in this environment.

## 1. What this return claims

The supplied source has the closed declarations `QuarticQuery.alphaTot_eq_four_unconditional : alphaTot = 4` and `QuarticQuery.theorem_1_1_unconditional`. The latter includes the universal quartic bound and the fixed-parameter separating families. The former external proposition `BansalSinhaLower` is proved by `QuarticQuery.ForrelationLower.bansalSinhaLower` in `repository/lean/QuarticQuery/ForrelationLower/Main.lean:506`.

The manuscript explains that result and reconstructs its mathematical proof. Its confidence rests on two distinct kinds of evidence:

- The supplied execution record reports successful kernel builds, statement comparisons, negative controls and an external-kernel replay.
- This authoring pass freshly inspected the source, checked the supplied manifest, reconstructed the mathematical arguments, reviewed the literature and checked the manuscript's correspondence.

The second item does not reproduce the first. Neither establishes independent human review. No supplied source or repository file was modified for this return.

The fixed-parameter Forrelation theorem is weaker than the full quantitative theorem stated by Bansal and Sinha. Its logarithmic denominator is squared, its threshold may depend on the fixed integer `k`, and no uniform advantage dependence is asserted. The alternative proof does not depend on verifying every step of the published Bansal–Sinha proof.

## 2. Immutable identifiers and what they establish

| Item | Supplied identifier | Interpretation |
| --- | --- | --- |
| Source snapshot | `c7e0c9161f0ad898889bd9166e7b354acd42188d` | Revision named by the packet manifest |
| Recorded paranoid replay | `d42fb67a7e060fb5386867dadf20a5903df39141` | Revision named by the replay record |
| OpenAI source | `openai/math 4eaee875` | Preprint provenance specified by the packet |
| Preprint PDF SHA-256 | `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e` | Freshly matched to the supplied PDF |
| Lean toolchain | `leanprover/lean4:v4.36.0-rc2` | `repository/lean/lean-toolchain` |
| complexitylib | `62ca5c21461b2482e8bd12b7cb9b4937d887a33a` | Lake file and manifest |
| Mathlib | `69552756cd8a2d2d48763cf7279fd814d6a1224d` | Lake dependency manifest |
| CSLib | `254e30e6d4299c51323aaeaf5f51a4763b375d4a` | Lake dependency manifest |

All 119 members enumerated by the supplied manifest matched their recorded byte lengths and SHA-256 digests. This checks the packet against its own manifest. It does not independently authenticate a remote Git commit, prove that these exact bytes were compiled, or resolve the difference between the source and replay pins.

The trace describes documentation and corpus changes after the paranoid replay and before the final source pin. The relevant command stages `README.md` and `corpus`, which is consistent with a documentation/evidence change. A complete parent-to-child Git diff is absent. We therefore do not identify the two proof trees without qualification.

The formalisation repository is [wcook04/quartic-query-lean](https://github.com/wcook04/quartic-query-lean). The supplied closeout says it was private and had not been submitted to Palomar. A failed public tool fetch in this authoring pass is an access failure, not independent evidence of a current 404, private status or public release.

## 3. The recorded checks

Trace locators below are physical line numbers in `Pasted text(20261102-112537).txt`, as supplied, not the capsule's internal subagent indexes.

| Evidence | Trace locator | Supported claim and limit |
| --- | --- | --- |
| Positive Comparator runs | 7437–7441 | Construction, Foundations, Separation, Tournament and Unconditional reported exit 0 |
| Four initial negative controls | 7442–7445 | ChangedDefinition, ForeignAxiom, MissingDeclaration and SorryProof rejected as intended |
| WeakenedConclusion diagnostic | 7453–7461 | Comparator rejected the mismatching theorem type; the harness initially expected the wrong diagnostic substring |
| Corrected negative-control matcher | 7475 | The intended-rejection test passed after fixing its expected diagnostic; there was no acceptance of the bad theorem |
| Unconditional paranoid replay | 8145–8146 | `Unconditional: exit 0` and `paranoid_rc=0` |
| Receipt summary | 8154; field-printing command at 9150 | Success, paranoid mode, prior revision and `sandboxed = false` |
| Forrelation axiom output | 43691 and 43740 | The lower-bound theorem uses `propext`, `Classical.choice` and `Quot.sound` |
| Composed exponent axiom output | 43741; source in the adjoining descendant record | The same axiom list for a scratch theorem proving `alphaTot = 4` by the displayed composition |
| Source closeout | 11430–11432 | Private repository; no Palomar submission or public release in that record |

The positive configurations allow exactly `propext`, `Quot.sound` and `Classical.choice`. A fresh source scan found no proof holes, extra axioms or native-evaluation escape hatches in the `QuarticQuery` proof subtree. Challenge theorem holes and deliberately invalid fixtures are separate and must not be counted as candidate proof holes.

Successful named-root `#print axioms` outputs for both final root declarations were not found in the sampled root trace: earlier attempts were deferred. The descendant outputs and Comparator's dependency checks provide the recorded evidence described above. The manuscript does not manufacture missing named-root output.

Only the Unconditional bundle has the recorded `--paranoid` replay discussed here. We do not extend that external-kernel claim to the other four bundles. Full individual kernel-checker outputs and archived receipt files are not included in the packet.

The local runs used `--inadvisably-no-sandbox`. They were unsandboxed rehearsals, not an official remote verification judgment. The dependency-reach JSON was generated from a compiled environment and is useful evidence about reachability; it is not a fresh build receipt and contains no independent source-hash authentication.

## 4. Fresh specification checks and residual risk

The five challenge files import Mathlib only. Their complete `namespace QuarticQuery … end QuarticQuery` vocabulary blocks were compared with `Statement.lean` and found byte-identical. Their solution files import the proof development and provide the named statements. This supports the claim that the candidate has to prove the frozen definition of the function and resource bounds.

The challenge vocabulary was generated from the same specification used by the solution. “Independently compiled” does not mean independently designed mathematical models. Comparator checks statement and dependency conformity; the kernel checks proofs relative to those statements. A common error in the definitions could survive both processes.

The fresh model inspection covered:

- The order of quantifiers in `QLe`: a workspace, initial state and finite program are chosen before the universal input.
- Input-independent fixed gates and measurement projectors, with input access only through the bit oracle.
- Query depth charged by the maximum over branches, including repeated queries.
- The finite randomized-mixture model and its relation to worst-case bounded-depth algorithms.
- Empty-coordinate and constant-on-promise cases.
- Explicit bit coordinates for pointers, cells and transcripts.
- Exact circuit-domain certification and transcripts containing only non-input gates.
- Deterministic-model equality, bit/phase conversion and adaptive-to-fixed-sequence conversion.
- The fixed-`k` order used to disprove every smaller universal exponent.

The local theorem `QuarticQuery.D_le_Q_pow_four` derives the numerical quartic bound through `Cslib.Quantum.complexity_le_mul_pow_four` and the model bridges. The external dependency source trees were not supplied and were not independently read in full here. The preprint's Appendix A proof is not the route implemented by this local theorem.

## 5. Statement-level records

`correspondence.json` is a list of passage-to-evidence records. Its `from` and `to` values are exact short boundary substrings of the passage, including Markdown where applicable. An opening comment of the form `<!-- passage:NAME -->` and a matching closing comment delimit each mapped passage.

A hidden `<!-- statement:ID ... -->` comment immediately before a mathematical display identifies its existing or newly proposed record. If several adjacent displays state one bundled claim, the marker applies to that bundle. Ordinary inline steps are traced through their surrounding passage.

`NEW_STATEMENTS.json` records the newly displayed intermediate claims. “New” means absent as a displayed record from the original corpus; it is not a claim of mathematical novelty. Several have exact existing Lean counterparts. Others need only a conjunction, notation conversion, finite-product unfolding or extraction of reasoning already present inside another proof. Proposed signatures contain no new assumed mathematical lemmas, but **none of those proposed wrappers has been elaborated or submitted to Comparator in this authoring environment**.

`LEAN_GAPS.md` lists displayed statements with partial correspondence, a different proof route, or an uncompiled assembly. A missing corpus tie for a definition or for an already existing exact theorem is a metadata issue. Conversely, the presence of the final closed theorem does not certify every prose derivation or displayed intermediate formula.

`STATEMENT_CHANGES.json` separates actual statement changes from metadata corrections. In particular:

- The exact adaptive-depth form of local tests corrects an earlier ledger/intake formulation; the attached preprint itself already describes reading the pointer and then its selected target.
- The improved hidden-zero bound is `2G/m²`. The final planted-gap statement is explicitly one-sided.
- The source theorem `bansalSinhaLower` proves `L<R(P)` directly. It does not prove the separate numerical comparison recorded under `claim-bs-to-L`.
- The corpus's old location and declaration-kind fields for that theorem are stale.
- Historical conditional-status prose does not override the current unconditional endpoint.

## 6. Literature checks

Primary sources were used for theorem statements and bibliographic checks. The manuscript's bibliography pins source versions where the supplied material specifies them.

| Source | Check performed |
| --- | --- |
| OpenAI preprint | Entire supplied extraction read; defining statements and proof route compared with the supplied source; outward-pointer figure inspected in the PDF |
| Aaronson–Ben-David–Kothari | Supplied introduction, initial result discussion and cheat-sheet proof/definition sections read; arXiv v2 metadata and source location checked |
| Bansal–Sinha | Entire supplied extraction and notes read by a specialist reviewer; theorem hypotheses and relevant proof sections checked against public arXiv v3 |
| Girish–Tal–Wu | Entire supplied extraction and notes read by a specialist reviewer; conference Section 1.3 and Lemma 9 checked |
| Drucker | Supplied introduction and the per-instance/product-value proof sections read; full-version Section 1.3 and Lemmas 3.1–3.2 checked |
| Brassard–Høyer–Mosca–Tapp | Rotation and amplification sections checked against the supplied material and primary PDF |
| Boyer–Brassard–Høyer–Tapp | Unknown-number-of-solutions antecedent and bibliographic metadata checked; journal page range follows the publisher |
| Aaronson–Ben-David–Kothari–Rao–Tal | Quartic upper bound and cubic conjecture checked against the primary paper |
| Comparator | Official Lean documentation checked for the meaning of statement/dependency comparison; it does not authenticate this project's execution |

The cheat-sheet arXiv identifier is **1511.01937**, not 1506.04719; the latter is a different pointer-function paper. This draft citation error was caught and corrected. Bansal–Sinha's primary arXiv class is `quant-ph`. GTW's conference theorem is Lemma 9; Lemma 1.9 is the corresponding arXiv numbering. The ABK supplied extraction renumbers some environments because it omits introductory restatable theorem numbering; the manuscript uses version-specific sections to avoid that trap.

### A narrow unresolved issue in the Bansal–Sinha exposition

The full-literature review noticed an algebraic issue in [arXiv v3, Section 5.4](https://arxiv.org/html/2008.07003v3), immediately after (5.31). Its displayed transition replaces the logarithmic factor `log(kN)^((j−1)/2)` by a constant-to-`j` factor times `log(kN)^(j(1−1/k)/2)` throughout `k ≤ j ≤ k(k−1)`. When `j>k`, their ratio is `log(kN)^((j/k−1)/2)` and is unbounded as `N` grows with `k,j` fixed. For example, `k=3,j=6` leaves `sqrt(log(3N))`. The root author independently checked the displayed formulas against the public v3 HTML.

This identifies a problem with that displayed deduction; it is **not a refutation of the theorem**. Earlier finer estimates or a corrected argument may repair it. The review did not undertake to settle the stronger quantitative theorem. In the same section, the off-promise error term in (5.31) is written as `δ²/(4N)`, while the preceding second-moment bound supplies `4/(δ²N)`. Correcting that reciprocal is harmless for fixed `k` and sufficiently large `N`.

The manuscript cites the stronger theorem as the result Bansal and Sinha state and proves its own weaker fixed-parameter input through the supplied independent route. Neither concern enters that proof. This audit makes no claim to have independently verified the entire published Bansal–Sinha argument.

### Code provenance

The headers of `repository/lean/QuarticQuery/Amplification/Geometry.lean` and `Average.lean` acknowledge adaptation from Troy Lee's `Quantum/Amplitude/Geometry.lean` and `Quantum/Amplitude/TrigSum.lean`. They are adaptations, not imports. Mathematical credit for the rotation is given to BHMT in the manuscript. The external original code files were not supplied or independently audited here.

## 7. Reading coverage and unread material

The principal source readers together read all mathematical modules assigned to them: `Statement`, `Model`, `Construction`, `Tournament`, `Upper`, `Amplification`, `LowerBound`, `Forrelation`, `ForrelationLower`, `Bridge`, `Results` and the Appendix endpoint. They read the root imports, build configuration, challenge/solution/configuration files, negative fixtures and reachability script. These are human-readable source reviews performed by AI agents, not fresh elaboration.

Read in full as text: `READ_ME_FIRST.md`; repository README; statement evidence contract; corpus README; the four writing guides; the preprint extraction; fidelity and Forrelation route/review/prior-art documents; intake/adjudication materials; all mathematical corpus row statements; the short exemplar. Manifest and corpus JSON structures were parsed completely. Thousands of dependency-graph edges were machine-read and root-checked, not individually manually audited.

The following limitations are explicit:

- The raw trace has 125,744 physical lines. It was searched throughout and read selectively. Inspected ranges include 940–1060, 3350–3585, 6940–7275, 7423–7655, 8100–8185, 9140–9155, 10950–11450 and 43660–43755, plus relevant search hits. Its remaining lines were not read sequentially.
- The long `expository.md` and `long-reasoning-record.md` exemplars were sampled for openings, section maps, source locators and verification/scope sections. Their remaining mathematical bodies were not read. They concern another theorem and supply no evidence for this result.
- The complete BS and GTW extracts and their annex notes were read. The ABK, Drucker and BHMT materials were read selectively at the parts used. Unrelated proof sections were not exhaustively audited.
- Images and algorithms absent from text extraction were not all visually inspected. No argument in this return relies on an uninspected image.
- The guides name original Halmos and Knuth annexes, but those annexes are absent from this packet. The supplied mechanics and exposition guides were read; the missing originals were not silently treated as read.
- The guides' `tools/paper_register.py` and genre profile are absent. No before/after register score is reported. `STYLE_RULES.json` records qualitative rules and actual revisions only.
- Full archived receipt/log files, `tools/`, the repository Makefile, compiled artifacts and dependency source trees are absent. The direct Lean source subtree and its manifest are present.
- No mailbox, account connection, credentials, repository integration, publication or external communication was used.

The limitations above do not erase the completed source reading. They bound it precisely.

## 8. Reproduction and validation of the return

The paper gives commands that can be run from the supplied `repository/lean` directory once the pinned toolchain and dependencies are available. Preserve `lake-manifest.json`; do not use an unqualified dependency update as a reproduction step.

A fresh check of the final source pin and a public release with full receipts remain future verification work. The uncompiled proposed wrappers are also future formal work. They are disclosed in the statement records and gaps file, not smuggled into the checked endpoint.

For this return, JSON structure, passage boundaries, statement identifiers, citation links, proposed-signature symbol references, bibliography syntax and mathematical-display coverage were checked. The manuscript was rendered for layout inspection. These are editorial and source-integrity checks. They do not claim a Lean execution.

The ZIP contains the complete manuscript and its required companion records. The PDF is a reading copy of the Markdown; the passage comments and correspondence machinery live in the Markdown and JSON files.

