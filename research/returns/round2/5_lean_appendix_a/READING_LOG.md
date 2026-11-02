# Reading scope and unavailable material

This log describes the work actually performed by the root agent and its three collaborating agents. Reading source text is distinct from compiling it. Hash checking a file is distinct from reading its contents.

## Task and instruction readings

The root reviewed the attached pasted conversation for task scope, including its final task steering, and read the selected Appendix A brief in full. The older conversation was contextual reading, not an independent re-audit of every historical claim. The operational reading order was followed, with full readings of `READ_ME_FIRST.md`, `BUILD_STATUS.md`, `repository/README.md`, `repository/docs/statement_evidence_contract.md`, and `repository/corpus/README.md`. The Appendix A text of the supplied preprint, extracted lines 720–864, was read in full against its statement records. The task remains confined to Appendix A; the earlier conversation's discussion of other sections did not expand the assignment.

All four named writing guides were read in full. The root read `the-deliverable.md` and `register-from-literature.md`; a collaborating agent read `mathematical-writing-mechanics.md` and `full-exposition-guide.md` in full, filling an initially truncated span. That agent also read all three Markdown exemplars in full: `short-paper.md` (1149 lines), `expository.md` (1514 lines), and `long-reasoning-record.md` (5659 lines). Those examples concern a different theorem and their verification claims were not transferred here. The additional exemplar `short-correspondence.json` was not read in full.

The review read all requested Appendix A statement objects and the relevant existing ties. The source of `lean/QuarticQuery/Appendix/TheoremA1.lean` was read in full. The project model and bridge portions used here were read, including the input/function definitions, classical and adaptive quantum costs, `QLe_Q`, `D_totalise_eq_complexity`, and the construction and contract of `exists_fixedSequence`.

## Mathematical and library sources

The agents read the query-level `Degree.lean`, `Huang.lean`, `Midrijanis.lean`, `SpectralSensitivity.lean`, `SensitivityBounds.lean`, and the pertinent `NisanSzegedy.lean`, `Relations.lean`, `Quantum/Adversary.lean`, `Quantum/Polynomial.lean` and `Quantum/Search.lean` proofs and definitions. The exact cslib `Measures.lean` definitions were inspected. In the public foundation source, the full signed-cube, maximal-support and Fourier-restriction files were read; Fourier, low-degree, expectation and measurement files were read to establish the exact used APIs and semantics.

Final reading completed the full proof bodies of `NisanSzegedy.lean` (288 lines), `SensitivityBounds.lean` (70), `Quantum/Composition.lean` (502), `Quantum/Grover.lean` (381), and `Quantum/UnknownSearch.lean` (467). Together with the already-read Adversary, Polynomial and Search files, this covers all six files in the named `Quantum/` directory. The composition and search files supply context about purification, parking and fixed-budget upper bounds; they do not replace the adaptive bridge or change the appendix proof. The range-sensitive polynomial lemma confirms why acceptance probabilities give the coefficient 16. The ordinary-sensitivity certificate bounds do not replace the required spectral inequality.

The user-supplied subset omitted several foundational imports. The public complexitylib, cslib and Mathlib repositories were obtained at the exact revisions recorded by the project. Every one of the66 packaged complexitylib Lean files agrees byte-for-byte with its counterpart at the fetched pin. This was a content comparison, not a claim to have read all thousands of fetched source files.

Pinned Mathlib source was inspected for matrix-to-Euclidean operators, Hermitian/symmetric transport, Rayleigh extrema and operator norms, finite-dimensional eigenspaces and dimension arithmetic, block multiplication, finite Cauchy–Schwarz, finite-sum reindexing, function extension and subtype equivalences. The new code was then reviewed independently across agent assignments. Every returned Lean file was read by its author and another agent; the root additionally inspected the main bridges and final assembly.

The original Huang paper was read, including its signed recursion and spectral remark. The relevant ABKRT theorem statements, Section 3 proof and Lemma 9 were checked against the supplied extracted text and original TeX, then verified against the exact-version public PDF. Midrijānis v2 was read for Lemma 3 and the full proof of Theorem 4. The Beals et al. theorem giving the bounded-error block-sensitivity coefficient 16 was checked in the supplied source and public arXiv v3. The Špalek–Szegedy formulation, oracle convention, norm convention and Theorem 3.1 were checked in the publisher PDF, including the rendered theorem page. The Nisan–Szegedy material was inspected for the alternative route's relevant degree/block-sensitivity input; no claim of a full independent rederivation of that paper is made.

## Relevant adjudication and evidence

The existing adjudication and statement evidence were used for the previously corrected constant-degree convention, the A.2 deferred-measurement partial ties, the A.4 spectral statement, and the Midrijānis locator. Prior returns were treated as proposals subject to their adjudication, not as independent proof receipts. The broad Forrelation research and its separate lower-bound verification were outside this Appendix A audit.

The input archive's manifest lists 356 members. Every listed member's SHA-256 hash was checked; there were no missing members or mismatches. `source_manifest.json` records this result. It does not imply that all 356 members were substantively reviewed.

## Not obtained, not read in full, or not performed

- The original Barnum–Saks–Szegedy 2003 full text was not obtained. The publisher DOI endpoint was inaccessible through the search service. Its attribution was checked through the primary Špalek–Szegedy paper; no exact BSS theorem locator is claimed.
- Unrelated sections, literature and previous-round papers were not exhaustively reread. The task was Appendix A, and the source map and new proofs stay within that scope.
- `exemplars/short-correspondence.json` was not read in full. Its neighboring Markdown exemplar and the binding statement-evidence contract were read.
- The build/corpus producer scripts named by the corpus README were not present at the supplied `repository/tools/` paths. No acceptance by those scripts is claimed. The returned validator is a separate local integrity checker.
- No Lean toolchain was installed or available on PATH. No new source was elaborated, no `.olean` was generated, no Comparator challenge was run, and no actual compiled dependency closure or axiom report was extracted for the new declarations.
- No email, mailbox, account connection, credentials, repository push, publication or person-directed communication was used.

The late coefficient check also inspected Høyer, Lee and Špalek's author PDF, including Definition 1 and Theorem 1 on p. 3 and the surrounding introduction, plus the primary arXiv metadata. That entire paper was not read. It corroborates the factor one half in the standard nonnegative adversary theorem. The root independently checked both the 2006 oracle conventions and the later theorem display.

The bibliography gives the exact editions and source locations actually used. `SOURCE_CORRECTIONS.json` distinguishes source transcription corrections from mathematical conclusions; the supplementary coefficient note supplies the concrete witness for its separate printed-prefactor finding.
