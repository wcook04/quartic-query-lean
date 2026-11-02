# Review notes and authoring receipt

## Product and scope

This return supplies a self-contained replacement for §§3.1–3.5 of the long reasoning record: Forrelation's normalized product and asymmetric promise, its integer numerator and exact tests, one coherent quantum preparation with its all-input measured law, the exact modular Boolean circuit, and the smallest nontrivial examples. It is a focused section-authoring contribution, not a final integrated paper or a new proof of the randomized lower bound.

The mathematical objects remain fixed: `k ≥ 2`, `t ≥ 1`, `m = 4^t`, `δ = 2^(-5k)`, `M = 2^(t(k+1))`, and the original two thresholds. The yes condition remains positive; large negative correlation remains unpromised. The quantum and classical models continue to count ordinary bit queries with a worst-case cap. There are **zero canonical statement changes** (`STATEMENT_CHANGES.json` is empty). `NEW_STATEMENTS.json` records **three new ordinary mathematical statements**: the explicit coherent output law, the three exact examples, and the closed-form circuit-size calculation. These are explanatory additions, with no claim of newly compiled Lean declarations or mathematical priority.

The source snapshot is the packet labeled `1dd469dd0042b937b739da3bc211eeb60bdf7462`. The complete available ZIP was inventoried and its manifest checked. The pasted attachment `Pasted text(20261102-190823).txt` failed to load and was not used; the user was asked to upload it again. Its missing contents have not been guessed from its filename or from other conversations.

The original baseline `reasoning-record.md` has SHA-256 `a6d1ede97135064c2c1b54992bfe32caac76da93688e67a378eab8cca16947ff`. The frozen revised `section.md` assessed for these notes has SHA-256 `06d3a346920e61e78834b80dd55b34de7cb38dccf7bfecdfc47a6eba29cda0e2`. The return manifest binds the delivered bytes; the supplied source-read receipt records exact assessed, sampled, unavailable and unassessed source scopes.

## Ranked corrections to the baseline

| Rank | Baseline location | Correction and disposition | Reason and boundary |
| --- | --- | --- | --- |
| 1 | §3.3, quantum/coherence proof and evidence paragraph | **Incorporated:** give the retained one-trial projection state, its tensor repetitions, reversible count/output computation and exact measured binomial law. Then identify the current complete same-witness physical wrapper. | A statement about probabilities alone does not identify the retained physical resource. `construction_lemma_2_1_ii_complete` now binds the same isometry, law and continuation. The literal new tensor representation is an ordinary proof, not a new formal state-identity theorem. |
| 2 | §3.3, sharp query-count display and evidence | **Incorporated:** preserve the ordinary `qk` phase-query proof while separately stating the generic compiled `2qk` cap. | A local phase identity does not provide a full `Runs k` implementation. The complete wrapper leaves `n` and the law existential; its proof chooses the explicit repetition count. Both constants yield Lemma 2.1(ii)'s fixed-`k` asymptotic bound. |
| 3 | §3.4, integer/circuit correspondence | **Incorporated:** distinguish ideal intermediate integers from words representing residues. Prove signed recovery only for the three final comparisons. | The ideal walk/prefix/butterfly bounds do not establish a signed interpretation of every actual register. The modular invariant and final range bounds already suffice for the exact endpoint. |
| 4 | §§3.1–3.2, normalization/promise and source notes | **Incorporated:** explicitly fix the power-of-four specialization and source the exact asymmetric thresholds to Bansal–Sinha. Update the normalization/numerator support to the current complete wrappers. | AA's inspected arXiv thresholds differ; the earlier quantum construction and the exact current promise have distinct citation roles. `construction_N_phi` now contains the full numerator bundle. |
| 5 | §3.5, worked example | **Incorporated:** show positive, zero and negative examples with the same second block, alongside bit encodings, projection probabilities and exact circuit outputs. Retain the analytic census and add an exact independent checker. | The negative example explains why the quantum proposal is insufficient for domain certification. The finite check does not supply an asymptotic lower bound or a new universal formal theorem. |
| 6 | §3.1, final evidence paragraph about `L` | **Incorporated:** remove the obsolete missing-tie claim. `construction_equation_5` has an exact current tie to `eq-5`. | This is an evidence refresh, not a new lower bound. Defining `L` does not prove `R(P)>L`. |
| 7 | §3 introductory evidence and §§3.1–3.5 source notes | **Incorporated within the replacement:** replace stale source pin and “no receipt directory” statements with the source-bound current record. | Historical candidate comments are not current execution status. Conversely, inspected prior passes are not fresh execution in this review. The retained §3 introduction outside this replacement needs the same evidence refresh at integration. |
| 8 | §3.17, final evidence paragraph; baseline `LEAN_GAPS` item 31 | **Located recommendation only:** replace the claim that no complete conjunction declaration exists. | `construction_lemma_2_1_complete` is present, built and explicitly type/axiom audited in this packet. The consumer section is outside this replacement and was not edited. Its classical component still uses the project's alternative fixed-parameter proof. |
| 9 | §3.4, long constant accounting | **Incorporated:** solve the constructor-cost recurrence into a closed form and derive the existing constant in three inequalities. | This removes several auxiliary bookkeeping quantities while retaining the actual implementation's repeated doublings and exact gate basis. The new closed-form equality remains an ordinary derivation. |

No correction above changes the source preprint's promise or either conclusion of Lemma 2.1(ii)–(iii). Claims of new priority, author confirmation, human review, or growing-parameter hardness have not been added.

## Suggested §3.17 replacement, outside the edited scope

The following is a recommendation for the integrating editor, not an edit already applied to the frozen baseline:

> The current snapshot contains the complete conjunction as `QuarticQuery.Paper.construction_lemma_2_1_complete`. Its quantum clause relates the same coherent preparation and output law to a physical continuation with the workspace retained; its classical clause uses the project's alternative fixed-parameter proof. The supplied source-bound root-build receipt includes this declaration, and the supplied type/axiom audit records only the permitted standard axioms. No current Comparator receipt names the conjunction, and no new Lean run was performed for this revision.

The mathematical three-part display in §3.17 can remain unchanged. This paragraph updates its evidence, not its classical proof or quantifier order. The separate round-three lower-bound contributions have not been treated as integrated results.

## Concrete simplifications and their outcomes

### A single coherent state explains the measured law

The section now starts from the orthogonal components `α₁ = Πψ_z` and `α₀ = (I−Π)ψ_z`. Recording the projection in a fresh flag yields `α₀⊗|0⟩ + α₁⊗|1⟩`. Tensoring fresh trials gives orthogonal flag strings; their squared norms multiply to `p^s(1−p)^(q−s)`. A reversible count/threshold operation produces the displayed output law while retaining the same state resources.

This makes the relation between coherence and probability explicit, without introducing a second unexplained implementation. The source's own complete wrapper is described separately and faithfully. Its physical isometry need not have the identical tensor register representation for the same mathematical conclusion to hold.

### The actual gate count gives a shorter size proof

Solving the Walsh recurrence yields

\[
\operatorname{whtCost}(w,2t)=tm(12w+1).
\]

Combining numerator layers, final sum, repeated doublings, comparisons and output gates gives

\[
S=6w\bigl((k+1)m+5k+t(k+1)+4\bigr)
 +(k-1)tm(12w+1)+7.
\]

With `a = k+1`, `w ≤ 6at`, and the bracket bounded by `7amt`, the three terms are at most `252a²mt²`, `78a²mt²`, and `7a²mt²`. Hence `S ≤ 337a²mt² ≤ 800a²mt² = 200(k+1)²m(log₂m)²`, recovering the existing formal inequality.

The circuit reviewer independently reconciled all terms with the constructors. The finite reconstruction gives 3,563 gates at `k=2,t=1` and 7,275 at `k=3,t=1`, agreeing with the closed form. These computations corroborate the derivation; they are not its universal proof. No new Lean theorem for the closed form is claimed.

### Alternatives deliberately not adopted

Replacing the projection experiment by the AA/BS interference law would change its acceptance probability from `Φ²` to `(1+Φ)/2` and break the intended source correspondence. It is mentioned for attribution/comparison only. Increasing the word width to support a new signed interpretation of every intermediate register would add an unnecessary proof obligation: residue correctness plus the final three range bounds already prove the required outputs. The return therefore explains the implemented route instead of proposing a different circuit.

## Validation and evidence actually used

The independent evidence audit verified all 453 manifest-member records and 448 `input_sha256` entries. All 124 local Lean/configuration files bound by the timestamped current root receipt match, with no missing or extra local files relative to the bound set. The dependency export and its source binding match. All 258 expected unique type/axiom printouts are present, their declarations appear in the current root declaration inventory, and the audit source/log hashes match the passed verdict and its allowlist.

Decisive packet-relative records are:

- `repository/corpus/receipts/lean-build-root-2026-11-02T182539383153+0000.json`;
- `native_results/final-evidence/current_native_acceptance.json`;
- `native_sources/final-evidence/reviewed_axiom_audit.lean`;
- `native_logs/final-evidence/reviewed-type-axiom-audit.log`;
- `native_results/final-evidence/reviewed_axiom_audit_verdict.json`;
- `repository/research/adjudication/round2_construction_quantum.md` and its tie JSON;
- the current `repository/corpus/ties.json` and dependency export.

The timestamped receipt's commit label differs from the packet label, but every bound local file matches. This is why the return uses source hashes rather than treating a commit label or a historical `UNELABORATED` comment as the entire evidence test.

The exact finite checker uses arbitrary-precision integers and rational arithmetic. It compares direct path summation, dense Walsh multiplication, butterfly multiplication, promise thresholds, and reconstructed Boolean outputs for all 256 inputs of `k=2,t=1` and all 4,096 inputs of `k=3,t=1`. It verifies the residues/signs of the final comparison words and constructor gate counts. Its separate boundary probes are explicitly synthetic integer numerators, with no assertion of input realizability.

No fresh Lean/kernel/Comparator run was performed. The complete-wrapper principals are not themselves in the dependency closure of the two exported headline roots, even where underlying components are reached. No current Comparator receipt names the section's Forrelation helpers. No compiled `.olean` was supplied for local replay; full dependency checkout/compiler bytes are outside the 124-file binding. No human reviewer or source author has confirmed this return.

## AI peer-reader dispositions

Two delegated AI readers assessed the ordinary proof and the source correspondence; these are not human peer reviews. The quantum reader read the entire section, with focused comparison against the quantum model, sampler, compiler, current wrappers and native type output. The circuit reader read the whole section and rechecked the revised constructor count, final signs, examples and evidence wording.

| Finding | Disposition in the frozen revised section |
| --- | --- |
| Inline formulas initially had bare parentheses and several missing command backslashes. | **Incorporated:** restored math delimiters/commands and inspected the rendered equations/tables. |
| The complete wrapper's type did not explicitly identify `n=q` or expand the binomial law. | **Incorporated:** distinguish existential theorem statement from the proof's choice; locate the explicit count/law in repetition and decoder theorems. |
| `Q_η` was insufficiently defined by reference to §2.2's `Q=Q_(1/3)`. | **Incorporated:** give its minimum worst-case query-budget meaning and promise/all-input conventions. |
| The literal tensor display needed a fixed register-order permutation. | **Incorporated:** explicitly group address registers before flags by a query-free permutation. |
| The high-bit predicate `neg(T)` appeared before an explicit definition. | **Incorporated:** define it immediately before the signed-range argument. |
| Transcript predecessor description omitted constants. | **Incorporated:** say input wires, constants or earlier gates. |
| “The no promise” could be misread as absence of a promise. | **Incorporated:** use “the zero case of the promise.” |
| Bibliographic issue number and equation-number formatting were affected by the initial delimiter repair. | **Incorporated:** restore ordinary journal issue and equation-label punctuation. |
| The closed-form size calculation might have omitted shifts, constants or output gates. | **Checked and retained:** the independent constructor reconciliation accounts for all terms and the coefficient `337`. |

The nine-page PDF was generated with Pandoc/XeLaTeX, and the AI author visually inspected all nine pages. A table collision, an isolated bold paragraph opening, and an overflowing source hash were corrected; affected regions were inspected again. The completed review in `evidence/pdf_review.json` records no remaining observed clipping, overlap, unresolved TeX, or unreadable table content, and binds the reviewed PDF to its SHA-256. Layout filters change spacing and line breaks only; the complete source hash remains intact in `section.md`. The delivered renderer and final validation records identify the released source and PDF bytes. No original full-paper PDF or later companion manuscript was rebuilt by this section return.

## Mathematical taste rubric: concrete evidence

| Dimension | Status and located evidence |
| --- | --- |
| Mechanism and understanding | **Demonstrated:** `forr_scope` states why quantum proposal and exact certification are both needed. `forr_coherent` derives the output law from the same retained state; `forr_final_signs` identifies the precise range bound that makes modular outputs exact. |
| Elegance and proof economy | **Demonstrated:** `forr_circuit_size` replaces multiple auxiliary bounds by the exact constructor count and three inequalities. `forr_coherent` gives one orthogonal-state calculation in place of an informal transition between measured and coherent procedures. |
| Structural yield of search | **Demonstrated within the finite example:** the even/odd parity split explains the entire `k=2,t=1` census. The three examples are not isolated numerical accidents; their common Walsh image displays the asymmetry directly. No new asymptotic search result is asserted. |
| Transfer and connections | **Demonstrated at the stated interface:** the quantum law proposes address bits; the exact two-output circuit certifies promise membership and values; transcript uniqueness supplies the local verification object used later. The later total-function proof is not reproduced or assumed from an unseen return. |
| Fertility and question selection | **Partial, intentionally bounded:** assembling the tight physical `Runs k` witness is a precise formal follow-up. A universal signed-register invariant and a same-representation tensor equality are unnecessary for the current endpoint; no speculative mathematical programme is proposed. |
| Difficulty landscape and negative knowledge | **Demonstrated:** the negative example refutes replacing domain certification by thresholding `Φ²`. Same measured law alone is insufficient evidence for a retained physical witness; final integer bounds alone do not identify every modular register. These are scoped limitations, not barriers to the theorem. |
| Digestion and shared reuse | **Demonstrated:** ordinary proofs, stable passage anchors, explicit examples, an exact reproducible checker, source-version locators and full formal correspondences permit another reader to reconstruct the ingredient without a private runtime. |

## Required paper-authoring receipt

```yaml
mathematical_paper_review:
  object: "Replacement §§3.1–3.5: Forrelation promise, coherent quantum preparation and exact Boolean circuit."
  genre_and_target_reader: "Long reasoning-record section for a mathematically mature researcher familiar with basic query complexity."
  venue_calibration: "Ordinary proof-forward mathematical prose calibrated to the supplied preprint and primary Forrelation papers; no journal submission or author-voice imitation."
  contribution_type: "Explanatory reconstruction, exact examples, source/claim correspondence refresh and an ordinary simplification of existing constructor-cost arithmetic. No new theorem priority claimed."
  headline_claim_and_evidence_class: "For fixed k and m=4^t, a coherent all-input-capped quantum procedure has promised error eta with O_k(1+log(1/eta)) queries; an exact fan-in-two circuit recognizes the domain and value in O_k(m log^2 m) gates. Ordinary proofs plus source-matched prior Lean evidence; the sharper qk physical cap and new tensor/closed-form displays have ordinary-proof authority."
  scanability_check_title_abstract_intro_theorems_conclusion: "Section title, opening mechanism, displayed bounds and consumer interface agree. No separate abstract or whole-paper conclusion was authored."
  external_field_map: "AA arXiv v1 supplies the k-fold quantity and projection/interference constructions; BS v3 supplies the parameterized promise; OpenAI §2.1 supplies the assigned lemma and its use in the total construction."
  internal_dependency_map: "Walsh orthogonality -> normalized product/norm -> integer numerator/exact tests -> quantum projection/retained repetitions and modular circuit/final signs -> exact examples and transcript interface."
  concrete_anchor_and_example_boundary: "At k=2,t=1, one fixed second block yields Phi=1,0,-1; the negative example has projection probability one but is unpromised. Analytic census and finite checks illustrate the definitions and do not prove a growing-size lower bound."
  hard_step_and_proof_forward_decisions: "Derive the law from the same retained state, and justify integer comparison outputs using only the final signed ranges. Choose each normalization, repetition threshold and word width immediately before its purpose is proved."
  mathematical_taste_rubric_evidence_and_dispositions: "See the seven-dimension table above; the bounded formal follow-up is distinguished from a new mathematical research programme."
  concrete_simplification_attempt_and_outcome: "Closed-form constructor count yields the existing circuit bound through coefficients 252+78+7=337. Independent source reconciliation succeeded; no new Lean equality theorem claimed."
  difficulty_landscape_and_fertile_questions: "The mathematical ingredient is proved. Remaining work is exact formal packaging of the tight phase compiler, optional representation identities, and later integration. A signed interpretation of every modular register is not required and is not proposed as a blocking task."
  short_long_transfer_locators: "This is the long-record replacement only. It expects the §2.2 oracle model and supplies §§3.17 and 4's interface. The recommended §3.17 evidence paragraph is supplied above but not applied. No short paper, exposition, reader or film is created here."
  notation_definition_and_equation_grammar: "k,t,m,delta,M and thresholds fixed throughout; natural ln distinguished from base-two log; 0-based block shift disclosed; Q_eta and neg(T) explicitly defined. Displays are integrated into the proofs."
  first_time_reader_house_jargon_scan: "No unexplained project terminology on the mathematical proof path. Formal source identifiers are confined to evidence/correspondence discussion."
  one_use_symbol_scan: "U_z is a local abbreviation used to distinguish the unitary word from psi_z; retained for that explanatory role. Other auxiliary symbols have a local repeated calculation or explicit interface use."
  conditional_hypothesis_restrictiveness: "Stated: fixed k, t>=1 and m=4^t; the latter ensures an integer square-root normalization. Promise restrictions apply only to accuracy; output and cost are all-input. Inhabited choices are supplied construction data, not open hypotheses."
  citation_role_checks: "Primary source editions and equation/theorem locators explicit. AA Proposition 6's linear-interference probability is not identified with the squared-projection test. Journal metadata is distinguished from inspected arXiv pagination."
  lean_statement_correspondence_and_validation_refs: "Current source types, ordinary premises, open-assumption fields, relation/route and prior source-bound receipts are recorded in correspondence.json. Exact remaining clauses are in LEAN_GAPS.md. No new kernel/Comparator/human review claim."
  compressed_claim_occurrences_and_post_edit_scope_check: "Opening, quantum bound, circuit theorem, example explanation and current-evidence note retain the same normalization, promise, all-input cap and fixed-k scope. The old consumer evidence sentence is explicitly superseded only by a recommendation."
  bibliography_render_check: "References identify the supplied preprint and AA/BS editions, with DOI/public-source metadata separately checked. Inline math and journal issue formatting repaired and included in the nine-page rendered review."
  figure_and_reproducibility_check: "No decorative figures. Exact example and histogram tables are supported by ordinary calculations and the integer/rational checker; checker is a reconstruction, not extracted Lean."
  cold_reader_confusion_and_disposition: "Two AI readers reviewed the section. Delimiters, Q_eta, existential wrapper count, register ordering, sign notation, constants in transcript predecessors and ambiguous zero-promise wording were repaired as documented above."
  version_bound_review_coverage_and_omissions: "Baseline assigned subsections and neighboring interfaces assessed; named Forrelation/model/compiler/circuit declarations, primary §2.1/AA/BS passages and current evidence assessed at the scopes in source_read_receipt.json. Full lower-bound sections and unrelated theorem proofs not newly re-audited. Missing pasted-text attachment unavailable."
  material_transition_warrants_and_source_conflicts: "Norm gives |Phi|<=1; positive denominator gives tests; orthogonal flags give product/binomial law; fixed repetitions give all-input cap; modular identities plus final range give exact comparisons; constructor recurrence gives size; gate order gives transcript uniqueness. Historical UNELABORATED comments are superseded by matching current execution records."
  exact_open_boundary: "No full tight Runs k/qk physical theorem; no literal state-identity theorem to the new tensor representation; no signed decoding invariant for every intermediate word; split integer/output ties and bundled size ties remain partial; no fresh compilation or helper Comparator result. None is an unproved premise of Lemma 2.1(ii)-(iii)."
  rendered_release_checks: "Nine-page PDF generated with Pandoc/XeLaTeX; all nine pages visually inspected by the AI author and layout fixes rechecked. Completed evidence/pdf_review.json binds the reviewed source and PDF and records no remaining observed clipping, overlap, unresolved TeX or unreadable table content. Final validation binds rendered/source files, checks display/table correspondence coverage, and checks extracted headings and reference text; the equations themselves were visually reviewed. No human visual endorsement claimed."
  deliberate_non_changes: "No edits to canonical Lean definitions, input sources, original returns, corpus ties or receipts. No lower-bound reproving, growing-k theorem, future-return integration, public posting, merge, release or external messaging."
```

This receipt records the work and its limits. It is not a claim of mathematical novelty, human endorsement, final integration or publication approval.
