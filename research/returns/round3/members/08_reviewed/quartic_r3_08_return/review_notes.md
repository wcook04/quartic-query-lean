# Review notes — job 08

## Disposition

The assigned exponent argument and universal quartic theorem are mathematically sound within their stated fixed-parameter and total-function scope. This return reconstructs the ordinary proofs and updates their correspondence to the current supplied formal evidence. The main baseline defect is stale evidence reporting: it describes several now-compiled intermediate claims as lacking formal ties. There are also local citation, constant, and dimension qualifications that should be carried into integration.

The input archive's exact bytes and its 472 enumerated source hashes were checked. That verifies provenance, not complete reading of every member. The source receipt distinguishes assessed passages from sampled, unavailable, and unassessed material. No source file or canonical ledger in the input packet was edited.

## Ranked and located findings

### 1. High priority — update the formal-support claims, preserving per-type limits

**Locations.** Baseline `ROOT-RATIO`, `ROOT-ADVERSARY-FINAL`, `ROOT-BS-LAMBDA`, `ROOT-HUANG-SPECTRUM`, and `ROOT-MONOMIAL-TREE` (baseline lines 2010, 2125, 2157, 2215, and 2237). Replacements: `ROOT-EXPONENT-CORRESPONDENCE` and `R3-A-FORMAL`.

The older ratio helper proves only eventual strict comparison, but the current `Paper/ClassicalAsymptotics.lean` proves the literal finite quotient and both limits. The current `Paper/ConstructionFamily.lean` carries the named circuit, realization, size and two bounds together. The Appendix modules now include the general adversary, star, matching, actual-face, recursive signed-cube and deterministic-tree statements.

The timestamped root receipt, ten focused native Appendix receipts, and reviewed type-and-axiom verdict bind these declarations to the supplied source bytes. The replacement consumes that evidence rather than asking for completed proofs again. It still distinguishes one exported type from a composition of several checked lemmas, and it does not extend Comparator scope to helpers absent from its inventory.

### 2. High priority — explain the printed adversary prefactor discrepancy with a complete witness

**Locations.** Baseline `ROOT-ADVERSARY-FINAL`; supplied return 5 coefficient check and literature adjudication. Replacement: `R3-A-PARITY-PREFACTOR`.

In Špalek–Szegedy's Theorem 3.1 (printed p. 6), the displayed query lower bound omits the factor one-half when the spectral adversary quantity is normalized as in equation (3.1). Its bit oracle is specified on p. 4 and its operator norm on p. 5. Høyer–Lee–Špalek's 29-page author PDF, Definition 1 and Theorem 1, p. 3, gives the coefficient with denominator two.

The return proves the correction independently in the progress argument and demonstrates the problem exactly on two-bit parity: one query computes parity without error, the four-cycle adversary norm is two, both mask norms are one, and one query drops the progress from two to zero. At error `1/100`, the printed bound would exceed one because `99 < 625`. This avoids depending on whether an endpoint convention includes zero error. The exact checker verifies all four inputs and all relevant matrices without floating-point arithmetic.

The older annex's extra outer square root is a separate transcription error. Correcting that transcription does not correct the printed source coefficient. The return does not claim an author-confirmed erratum, inspect the unavailable BSS original, challenge the equivalence results, or present the correction as a new adversary method.

### 3. High priority — keep the three quartic routes separate

**Locations.** Baseline `ROOT-APPENDIX-INTRO` and `ROOT-QUARTIC-UPPER`; replacement `R3-A-ASSEMBLY`.

The existing headline route uses the polynomial block-sensitivity constant 16 and spectral constant 36, giving `20736`. The literal Appendix route uses the star-adversary block-sensitivity constant `35^2` and spectral constant 35, giving `1500625`. The separate hybrid combines 16 and 35, giving `19600`. All are present with current compilation evidence, but the supplied dependency export reaches the first from the headline roots. A smaller coefficient does not make the hybrid the actual headline dependency.

The no-plus display `D <= 1500625 Q^4` uses `appendixA_D_le_Q_pow_four`; `appendixA_theoremA1` itself has a one-plus conclusion. The conjunction `R <= D` is supported separately when matching the displayed no-plus statement. The return identifies this composition explicitly.

### 4. High priority — preserve the positive-dimension scope of the spectrum claim

**Locations.** Canonical `claim-huang-spectrum`; baseline `ROOT-HUANG-SPECTRUM`; replacement `R3-A-HUANG`.

Square and trace identities alone do not give two distinct eigenvalues in dimension zero. The extension at zero is a singleton zero matrix. For `d >= 1`, the roots `sqrt(d)` and `-sqrt(d)` are distinct and each has multiplicity `2^(d-1)`. The ordinary proof and formal multiplicity types preserve this condition. `STATEMENT_CHANGES.json` records the still-needed canonical text correction rather than silently modifying the ledger. This qualification was already proposed in the supplied prior return; the current canonical text still needs it.

### 5. Medium priority — make the fixed-parameter quantifiers visible

**Locations.** Baseline §7; replacement `ROOT-FAMILY-ASSEMBLY`, `ROOT-RATIO`, and `ROOT-NO-SMALLER`.

The proof chooses `alpha < 4`, then an integer `k > 2/(4-alpha)`, then defeats any universal constant by increasing `t` with that `k` fixed. Both complexity bounds concern the same named circuit and total function. The denominator is `1+Q`, so constants and the case `alpha=0` cause no zero-power ambiguity. A bijection from the constructed finite nonempty coordinate set to `Fin n` supplies a legitimate counterexample to the universal statement.

The replacement retains a literal quotient estimate instead of compressing everything to big-O notation. It explains why `k=2` does not by itself refute the cubic bound and why `k=3` does. It also records the failure of this estimate to force divergence at the endpoint `alpha=4-2/k`. A schedule with growing `k` is unnecessary for the theorem and remains a separate result.

### 6. Medium priority — qualify the maximal-monomial lemma and cite the actual product estimate

**Locations.** Baseline `ROOT-MONOMIAL-TREE`; replacement `R3-A-MIDRIJANIS`.

Midrijānis's Lemma 3, printed p. 3, should be used for nonconstant restrictions. A constant polynomial and its empty monomial would otherwise contradict the nonempty-sensitive-block conclusion. The decision tree in the proof of Theorem 4 only invokes the lemma while the restriction is nonconstant, so the argument survives this wording issue. The desired `D <= deg * bs` inequality appears inside that proof on p. 4; the stated theorem continues to a cubic degree estimate. Theorem 5 concerns exact quantum queries and is not the bounded-error input to this Appendix.

The reconstructed proof fixes the original input throughout the run. Each round produces a sensitive block at that same input, in coordinates not queried earlier. This is the reason block sensitivity bounds the number of rounds.

### 7. Medium priority — preserve exact editions and source roles

**Locations.** Baseline Appendix citations; replacement reference section and `references.bib`.

The supplied Huang PDF is the six-page arXiv version 2, not the seven-page Annals publication. The published edition was additionally retrieved and inspected at pp. 952–953. ABKRT theorem locators use arXiv version 1, not flattened extraction numbering. Høyer–Lee–Špalek's p. 3 is the 29-page author PDF. The supplied OpenAI bytes control the reconstruction; fetching the pinned public GitHub PDF was unavailable. The original BSS proof is historical attribution through inspected later sources, not direct evidence from an unread original.

### 8. Medium priority — avoid a false merger of the two adversary matrices

**Locations.** Replacement `R3-A-DEFINITIONS`, `R3-A-STAR`, and `R3-A-SPECTRAL`.

A block-sensitive star may have edges that flip multiple bits. Such edges need not lie in the sensitivity graph. The proof therefore bounds block sensitivity and spectral sensitivity separately. It never infers `bs <= lambda^2`. The normalized leaf vector is only used for a nonzero star. Exact star norm equality is compiled separately, while the endpoint uses its weaker cardinality-versus-norm-square consequence.

## Concrete simplification and retained detail

The Huang step is presented through an intersection of subspaces. The positive eigenspace has half the cube dimension; the subspace supported on the parity-majority set has more than half. Their intersection contains a nonzero vector. Taking coordinatewise absolute values transfers its Rayleigh quotient from the signed matrix to the ordinary induced cube graph. This makes the spectral-radius conclusion needed for query complexity immediate, with no separate interlacing theorem to state. The restriction to an actual face and zero-extension back to the full cube remain explicit.

A more aggressive compression of §7 to eventual strict comparison was rejected. It would hide the fixed positive power gap, the logarithmic loss, and the endpoint restriction. The quotient display and its short integral proof are retained because each does mathematical work.

Evidence prose is concentrated in §7.3 and A.6. This removes repeated stale status paragraphs from the proof while preserving complete per-claim details in the correspondence. The reconstruction retains full arguments for deferral, Perron normalization, per-query change, final overlap, the star norm, parity-majority restriction, signed-cube spectrum and monomial charging.

## Validation and evidence interpretation

`checks/exact_checks.py` passed with exact arithmetic. It covers every input of the parity example; the four-cycle eigenbasis and coordinate masks; the progress drop; the positive-error contradiction; the rational coefficient 35; and signed-cube identities through dimension four, with dimension zero explicitly excluded from the two-root split. General-dimensional conclusions are proved in the section; the finite checks are independent sanity checks of specified examples and conventions.

The return validator checks JSON structure, passage boundaries, exact quoted displays, named formal-support records, references, and delivered byte hashes. With the original input supplied, it also rechecks the original input hash inventory. Its output is included. This integrity check is not a Lean semantic checker.

The root-build receipt records 2,652 declarations and 124 source/configuration hashes. The reviewed post-root audit covers 258 declarations and allows only `propext`, `Quot.sound`, and `Classical.choice`. The latest Unconditional Comparator receipt reports a paranoid successful comparison of its eight listed declarations. The dependency export records the headline and cubic roots. Different packet and execution commit labels are not used as a shortcut: the recorded source bytes were checked directly. No fresh Lean, Lake, or Comparator execution was possible or claimed in this editorial environment.

## Paper-authoring receipt

**object:** Advisory replacement of long-record §7 and Appendix A, plus exact correspondence and reproducible checks.

**genre_and_target_reader:** A long mathematical reasoning record for a researcher familiar with basic query complexity, finite-dimensional linear algebra, and elementary real analysis. It does not assume familiarity with private project names or Lean internals.

**venue_calibration:** Full ordinary proof and source correspondence are appropriate here. The short companion and final whole-record synthesis remain separate tasks.

**contribution_type:** Expository reconstruction, evidence update, exact normalization audit, and a local scope correction. The separation and upper-bound results retain their original attribution; no new quartic theorem or optimal constant is claimed.

**headline_claim_and_evidence_class:** The fixed-parameter family excludes each admissible exponent below four; the universal quartic estimate makes four admissible. The section provides ordinary proofs and uses supplied source-current formal receipts. The parity normalization check additionally has exact finite computational evidence.

**scanability_check_title_abstract_intro_theorems_conclusion:** The replacement title and opening result state the exponent and scope. Appendix A begins with its explicit inequality and proof chain. The section-level boundaries remain visible. No whole-paper abstract or conclusion was revised.

**external_field_map:** OpenAI supplies the separation construction and target Appendix; ABKRT supplies the quartic theorem and degree-versus-spectral-sensitivity connection; Huang supplies the signed cube; Midrijānis supplies the deterministic tree; BSS receives indirect historical adversary attribution; HLS supplies the correctly normalized cited bound; SS supplies equivalence context and the inspected discrepant coefficient.

**internal_dependency_map:** Same-family quantum cap plus classical floor bound imply the quotient divergence and exclusion. Independently, nonnegative adversary gives star and sensitivity estimates, the actual-face signed-cube argument bounds degree, and the monomial tree gives `D <= bs * deg`; together these make exponent four admissible.

**concrete_anchor_and_example_boundary:** Two-bit parity checks the normalization and attains the one-query progress drop. It neither tests every adversary instance nor proves the asymptotic separation. The `k=2` and `k=3` examples explain the exponent quantifiers without asserting an exact fourth power for a fixed parameter.

**hard_step_and_proof_forward_decisions:** The nontrivial bridges are actual-face degree preservation and the subspace argument, same-input charging in the deterministic tree, and preservation of query cap under coherent deferral. They are proved in the running text. Formal-status details follow the mathematical deductions.

**mathematical_taste_rubric_evidence_and_dispositions:** The proof isolates the four inequalities that produce the quartic exponent; uses a minimal exact instance to expose the normalization; keeps strict and weak comparisons distinct; and shows why the same circuit matters. The most useful simplification is the subspace-intersection form of Huang's spectral argument. The scope boundary at the fixed-parameter exponent is retained instead of hidden by asymptotic notation.

**concrete_simplification_attempt_and_outcome:** Subspace intersection replaces a separate interlacing invocation and preserves the needed spectral conclusion. Dropping the explicit ratio was considered and rejected because it obscures endpoint and logarithm behavior.

**difficulty_landscape_and_fertile_questions:** The universal exponent follows from strict gaps with fixed parameters; it does not require uniform control in a growing parameter. A quantitative growing-parameter family and sharp constants would need additional work and are outside this return. No speculative improvement is used as a premise.

**short_long_transfer_locators:** §7's first result paragraph and parameter order, and Appendix A's first result paragraph and four-inequality display, are suitable later summary sources. Their restrictions must survive transfer. No short paper was produced.

**notation_definition_and_equation_grammar:** Query caps, logarithm bases, degree, sensitive blocks, spectral sensitivity, masks and matrix norms are defined before use. The universal constant is `K`, distinct from deterministic complexity `D`. Real powers have positive bases. Constant and zero-dimensional cases are handled before divisions or normalized vectors are introduced.

**first_time_reader_house_jargon_scan:** None in the mathematical proof beyond neighboring notation explicitly identified in the opening. Project declaration names are confined to the formal correspondence paragraphs and supporting files.

**one_use_symbol_scan:** No avoidable single-use notation was found in the bounded editorial pass. Indices in explicit matrices and local decompositions are introduced where needed; no automated register score is claimed.

**conditional_hypothesis_restrictiveness:** The fixed-parameter quantifiers and arbitrary constants are stated. No extra unproved mathematical assumption remains in the final unconditional declarations. The arbitrary-error ordinary extension is clearly distinguished from exported Lean statements.

**citation_role_checks:** Each cited inequality has an edition and original PDF locator. Original theorem credit, proof ingredients, historical attribution, formal source support and a detected source discrepancy are separated. The bibliography preserves the supplied-versus-published Huang distinction and the unread BSS boundary.

**lean_statement_correspondence_and_validation_refs:** `correspondence.json` provides exact excerpts, complete types, hypotheses, relations, routes and receipt scope. `LEAN_GAPS.md` records the no-plus/one-plus composition, compound-row limits, ordinary-only general-error extension and parity witness, and differing formal proof routes. `evidence_validation.json` records source-current evidence checks.

**compressed_claim_occurrences_and_post_edit_scope_check:** The opening exponent, ratio specialization, cubic corollary, Appendix result, route table and formal paragraphs were checked against the detailed proofs. The edits preserve fixed `k`, `d >= 1` for multiplicities, nonconstant monomial restrictions, and the distinction between the three constants.

**bibliography_render_check:** Citation keys, URLs, editions and locators were inspected in the Markdown and BibTeX sources. No bibliography was typeset or rendered to PDF, and no rendered-bibliography inspection is claimed.

**figure_and_reproducibility_check:** There are no new figures. The exact check and its captured output are delivered with standard-library reproduction commands. Source PDF displays used for the prefactor and spectral comparison were visually inspected as recorded in the read receipt.

**cold_reader_confusion_and_disposition:** Likely confusion about the function witness is resolved by naming one circuit before both bounds. Confusion between exponent thresholds and endpoints is resolved by `k=2`, `k=3`, and the zero-gap boundary. Confusion about two different graph matrices is resolved before the adversary applications. A reader can reconstruct the chain without relying on declaration names. This is an AI editorial assessment, not a human blind-reading result.

**version_bound_review_coverage_and_omissions:** The targeted baseline sections and named primary passages were assessed; the remainder of the 4,766-line baseline and unrelated packet content were not given a full review. The separate pasted-text attachment and original BSS full text were unavailable. The source receipt records the exact editions, hashes and individual assessment scopes.

**material_transition_warrants_and_source_conflicts:** Each transition is proved or traced to the specified neighboring estimate. The SS/HLS prefactor conflict is resolved by the ordinary progress proof and exact parity witness. The stale evidence claims are resolved by current byte-bound receipts, not by commit labels alone. The dimension qualification is proposed explicitly in the statement-change file.

**exact_open_boundary:** This is a section return awaiting integration. The ordinary arbitrary-error extension and parity algorithm have no claimed supplied Lean theorem; compound corpus rows need multiple declarations. New helper-wide Comparator comparisons, uniform growing-parameter estimates, unavailable-source review, human review and whole-paper synthesis remain outside scope.

**rendered_release_checks:** Markdown structure, equation delimiters, anchors, links and JSON were checked programmatically. Source pages were viewed where noted. No final PDF, DOCX or typeset section was created or visually inspected. The standalone register-measurement script/profile referenced by the generic writing guide was not supplied, so no before/after tool score is asserted.

**deliberate_non_changes:** The input archive, canonical ledger and Lean sources are preserved. Historical source comments are treated as historical rather than edited in place. Prior source credit, the fixed-parameter statement and existing headline proof route are retained.

This receipt records the authoring checks and their limits. It is not mathematical acceptance, external peer review, a human endorsement, or permission to publish.
