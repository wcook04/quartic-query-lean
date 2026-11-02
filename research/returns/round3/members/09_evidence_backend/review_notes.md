# Located review and authoring receipt

## Ranked findings

### 1. High: semantic review can become obsolete despite fresh operation receipts

**Location:** original `repository/tools/build_corpus.py`, tie evidence/current alignment handling; `repository/corpus/ties.json`; main passage `EVID-FRESHNESS`.

**Evidence:** the reproduced definition-body edit leaves the theorem source unchanged and supplies fresh mocked build/comparison records. The original producer revives current statement credit. The returned patch keeps those operation facts but reports stale review and withholds current alignment. Actual Python regression output is in `backend/logs/patched-python-tests.log`; the supplied-corpus dry run is in `backend/logs/backend-acceptance.json`.

**Correction:** add review binding to the existing tie owner. Do not rewrite source receipts, create another registry or silently attest legacy judgments. After integration, expect 477 authored ties to be `legacy_unbound`, 840 current tie-level build facts and 19 current tie-level comparison facts to remain visible, and seven currently compared statement rows to become unassessed until review is recorded. Counts refer to this frozen corpus, not a general invariant.

**Simplification attempted:** a theorem-header hash alone would be smaller, but fails on the demonstrated implicit-definition edit. The implementation therefore reuses the existing whole-source scope. A narrower elaborated semantic closure is future work and would require trustworthy extraction. No source-text dependency heuristic was substituted.

### 2. High: the whole equation-(19) row needs its equality as well as its bound

**Location:** baseline Appendix B `eq-19`, lines 4014–4038; `Paper/ClassicalPlanted.lean`, declarations `erasedZero_eq_expectedZeros_div`, `expectedZeros_le_four`, `eq_19`; main passage `EVID-EQ19`.

**Evidence:** `eq_19` concludes only the probability inequality. A correct or even stronger inequality does not prove an omitted equality. The current maintained tie already says `partial`; the baseline's old `stronger` classification is historical and misleading if presented as current.

**Correction:** the returned `eq19_whole` joins the two existing conclusions. The independent product-law target and bridges give separate semantic obligations. Both the direct wrapper and independent target require their own native evidence; no upgrade is claimed now. `claim-EZ` remains partial because its early/late clauses are not supplied by the endpoint-only alternative proof.

**Located replacement for the baseline evidence sentence:**

> The existing `QuarticQuery.Paper.eq_19` formalizes the probability upper bound, while `QuarticQuery.Paper.erasedZero_eq_expectedZeros_div` formalizes the equality with the normalized expected zero count. The frozen source-current root-build receipt names both declarations. They have no supplied direct comparison receipt and are outside the headline roots' reached set. The proposed `eq19_whole` combines both clauses, but its new source has not yet been built or compared. The maintained relation for the old inequality-only tie is partial; the coefficient-two proof is an alternative route to the endpoint.

This is an evidence replacement proposal through the baseline owner, not an edit to the canonical paper statement.

### 3. High: the native extraction endpoint is still open

**Location:** job 09 endpoint 3; `BACKEND_INPUT_STATUS.json`; supplied consumer contracts; `EVID-EXTRACTION`.

**Evidence:** the chosen equality target has matching source-current build evidence. Actual extraction launch exited 127 with `lean-exposition: not found`. The packet contains selected implementation files, not a complete installation. No native graph exists for subsequent commands.

**Correction:** report the accepted source target and exact missing environment, preserve the launch record and run the documented re-entry when the full matching environment is available. Do not describe the existing informal reader acceptance as native extraction.

### 4. Medium: independently specified model examples must test actual definitions

**Location:** baseline §2.3 and Appendix B `def-Q`; generated challenge route; `EVID-IDENTITY` through `EVID-CONTROLS`.

**Evidence:** copying a proposition and its vocabulary into an independent challenge can check agreement while preserving a shared semantic defect. Finite toy controls do not execute Lean. The returned files state concrete expected answers, import actual definitions and distinguish mismatch rejection from shared bad-specification acceptance.

**Correction:** retain the four examples, their explicit quantifiers and query units, and the nonvacuity witness. Mark every new Lean proof uncompiled. Restrict the strict-threshold claim to failure of the specified OR mixture. The quantum zero-query example is a witness for `ConstantOnPromise`, not an audit of all quantum semantics.

### 5. Medium: historical evidence passages must identify their edition

**Location:** baseline §2.3, lines 136–145, and `Paper/ClassicalPlanted.lean` header; `EVID-SNAPSHOT`.

**Evidence:** the header says `UNELABORATED`, but the later source-bound root-build receipt names the exact declarations and matches the current file. Conversely, the new overlays have no native evidence. The baseline's old evidence edition cannot be treated as the current receipt inventory.

**Located replacement direction:** retain the original evidence description as explicitly dated historical context, then state that this frozen packet has 12 current and 11 legacy-unbound receipts under its byte-binding contract. Identify build, comparison and reach separately for each declaration. State that no native extraction has been completed. Do not rewrite history to say the original authoring environment compiled a file it did not compile.

### 6. Medium: derived helpers cannot inherit preprint provenance

**Location:** `round2_forrelation_exponent_ties.json`, seven `r2-live-*` proposals; the graph producer; `EVID-PROVENANCE`.

**Evidence:** the current graph is preprint-only, the helpers are already withheld, and their proposal records lack authored `depends_on`. Original producer behavior can relabel an inserted row as preprint material or discard a missing dependency edge.

**Correction:** explicitly continue withholding; reject mislabelled helper ingestion, nonpreprint-source relabelling and missing prerequisites. A future reviewed mixed-source route must retain the helpers' own provenance and dependencies. The derived finite independence control in this return is likewise not inserted into that graph.

## Source-review dispositions

Three focused AI reviewers examined the mathematical exposition, semantic files and backend account. This is not human or author confirmation. Concrete corrections incorporated: restore inline math delimiters; condition the adaptive-search argument on positive-probability history **up to the current time**; state address multiplicity and cell parameters; distinguish the preprint's first row from implementation row zero; describe the backend as a returned unapplied patch. The equation-(19) subsection now explains why fixing a realized history fixes the adaptive query schedule and imposes only the recorded answer constraints.

The source review found no definite further mathematical or source-level defect in the reviewed candidates. That observation is not an elaboration result. Reviewer scopes and final editorial dispositions are in `checks/editorial_review.json`.

## Paper-authoring receipt

- **Target reader:** a mathematically mature researcher familiar with basic query complexity who must assess a formal correspondence and its evidence without trusting a generated status label.
- **Contribution:** a focused backend/research return, not a replacement survey or integrated paper. It gives ordinary proofs of the assigned finite examples and full eq19 target, a tested freshness/provenance patch, complete proposed Lean sources and precise native re-entry obligations.
- **Proof spine:** zero-query distributions are input-independent; a three-tree mixture meets the inclusive threshold; undefined inputs do not enlarge the promise; a Walsh eigenvector exposes the signed high branch; an independently uniform erased column converts a distinct-discovery count into hit probability; early/late accounting gives the printed bound, and a finite-world induction explains the existing stronger endpoint route.
- **Hard step:** distinguish independence from marginal uniformity and distinguish current proof/checking operations from current mathematical correspondence. The finite sampling control and source-edit regression make these distinctions falsifiable.
- **Concrete examples and limits:** four requested semantic cases, a comparison nonvacuity witness, a repeated-query count and the 256-world sampling control. They expose named failure modes, not every possible error in the model or proof.
- **Claim/Lean alignment:** exact proposed types and ordinary premises appear in `correspondence.json`. New proofs and comparisons remain unexecuted. The original inequality-only `eq_19` is partial for the compound row; the new conjunction is a proposal. Ordinary normalization/depth premises are not labelled open conjectures.
- **Citation roles:** the pinned OpenAI preprint supplies mathematical authority; local Lean sources supply implementation meaning; supplied receipts supply recorded operation facts; Comparator/consumer sources supply integration contracts; current official Lean documentation provides background corroboration. QAOA excerpts and writing guides supply structural examples only.
- **Cold-reader difficulty and disposition:** the early/late conditioning time, cell parameters, repeated-query semantics, aggregate reach versus exact declaration reach, and two separate positive comparisons could be conflated. Each now receives an explicit local explanation. Status tables follow the mathematics so they do not replace the argument.
- **Exact open boundary:** new actual-definition Lean elaboration, transitive axiom checking and Comparator controls; native extraction/validation/selection/inspection; explicit future review bindings. The unavailable text attachment was not used. Full-proof campaign, all model semantics, dependency checkout/binary authenticity and manuscript-wide coherence are outside this focused review.
- **Rendering and checks:** Markdown source and math delimiters were inspected; no PDF, document, browser or full manuscript rendering was performed. JSON, Python syntax, references, passage excerpts, source hashes and ZIP members were checked as recorded. A source scan is not Lean elaboration.
- **Novelty and attribution:** no new quartic separation, new formal verification or priority claim is made. The negative Forrelation witness already exists in the supplied Sanity file. The finite independence countermodel is an explanatory derived control with a different law. Writing exemplars were not copied.
- **Integration:** all changes are advisory. The original packet, canonical ledger and generated corpus remain unchanged. No publication, merge, external communication or frontend was performed.

## Structured authoring receipt

```json
{
  "mathematical_paper_review": {
    "object": "evidence-path.md and accompanying focused job09 return",
    "genre_and_target_reader": "Advisory mathematical/backend contribution for query-complexity researchers assessing exact formal correspondence.",
    "venue_calibration": "No journal/venue or submission requested; not an integrated manuscript.",
    "contribution_type": "Ordinary mathematical exposition, independent proposed semantic tests, tested minimal backend repair, exact evidence audit.",
    "headline_claim_and_evidence_class": "Review freshness repaired in Python; full eq19 and semantic candidates supplied, uncompiled; native extraction blocked.",
    "scanability_check_title_abstract_intro_theorems_conclusion": "Title, opening status, mathematical subsections, evidence tables and integration order inspected; no separate abstract or final-paper conclusion created.",
    "external_field_map": "Pinned preprint is mathematical authority; Lean sources/receipts are implementation/evidence; official docs are corroboration; QAOA is structural only.",
    "internal_dependency_map": "Model definitions -> finite examples; dummy/product law -> equality; early/late or finite-tree argument -> bound; conjunction -> two separate comparison targets; source snapshot + explicit review -> current alignment.",
    "concrete_anchor_and_example_boundary": "Four semantic examples, nonvacuity, repeated query, independent-index countermodel; targeted failure modes only.",
    "hard_step_and_proof_forward_decisions": "Positive-probability adaptive history and independent uniform I made explicit; finite-world induction displayed.",
    "mathematical_taste_rubric_evidence_and_dispositions": "Exact hypotheses precede bounds; ordinary proof precedes status; stronger endpoint labelled alternative route; no novelty or human-review claim.",
    "concrete_simplification_attempt_and_outcome": "Two existing component theorems give a short conjunction proof; header-only review binding rejected because the reproduced semantic edit leaves header unchanged.",
    "difficulty_landscape_and_fertile_questions": "A finer sound semantic dependency fingerprint would reduce conservative invalidation, but needs trustworthy native extraction; no implementation promised here.",
    "short_long_transfer_locators": "No short companion authored. Main report anchors and proposed baseline §2.3/Appendix B corrections support later integration.",
    "notation_definition_and_equation_grammar": "Defined m, ℓ, r, S, μ, I, J, T, G and Z; repaired inline math delimiters; preprint versus zero-based indexing explicit.",
    "first_time_reader_house_jargon_scan": "Explained current receipt, semantic review binding, native extraction and shared-specification blind spot locally.",
    "one_use_symbol_scan": "Notation kept to finite proofs and actual source interfaces; no new acronym family.",
    "conditional_hypothesis_restrictiveness": "Finite types, μ≥0, sum μ=1, depth cap ordinary; isolated equality algebraic; no extra hardness assumption.",
    "citation_role_checks": "references.bib and source_read_receipt.json separate exact versions, mathematical authority, tool implementation, recorded operations and exemplars.",
    "lean_statement_correspondence_and_validation_refs": "correspondence.json, LEAN_GAPS.md, acceptance_cases.json; no new native pass.",
    "compressed_claim_occurrences_and_post_edit_scope_check": "Opening, tables and conclusion retain uncompiled/unrun labels; 840 counted as ties, not distinct declarations.",
    "bibliography_render_check": "BibTeX source inspected; no bibliography engine/render run. URLs/editions stated explicitly.",
    "figure_and_reproducibility_check": "No figures required. Scripts, actual logs and exact hashes provided; native re-entry unexecuted.",
    "cold_reader_confusion_and_disposition": "Clarified history up to current time, input parameters, row indexing, shared versus independent definitions and exact target identity.",
    "version_bound_review_coverage_and_omissions": "Focused passages only; see scoped read ledger. Unavailable TXT and runtime explicitly recorded.",
    "material_transition_warrants_and_source_conflicts": "Old UNELABORATED header treated historically against later matching receipt; old stronger eq19 classification corrected to maintained partial.",
    "exact_open_boundary": "New Lean elaboration/axioms/comparisons; real native extraction/schema/selection/inspection; later explicit review attestations.",
    "rendered_release_checks": "No visual PDF/browser/manuscript rendering. Actual JSON, Python syntax, anchor, hash and archive checks are recorded separately.",
    "deliberate_non_changes": "Original packet, canonical statements, generated corpus and external systems unchanged; no second registry or frontend."
  }
}
```
