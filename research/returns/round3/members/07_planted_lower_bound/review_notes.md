# Review and authoring receipt: planted lower bound

## Finding and disposition

The assigned ordinary argument is complete at its stated scope. The replacement reconstructs the coupling, the exact erased-zero identity, both search estimates, the capped cell simulator, the discrepancy contradiction, and the two-floor estimate. It proves Proposition 4.2 for each fixed parameter and for the same realizing circuit used by the construction and quantum upper bound. No unresolved mathematical implication was found within this assignment. This is a section-level assessment, not a review of every proof in the packet or the entire external Forrelation theorem.

The material corrections concern the precision of the explanation and the evidence attached to it. In particular, the request's description of the exact erased-zero identity as unelaborated is stale relative to the supplied current receipts. Conversely, compilation of separately stated ingredients does not establish that the corpus has accepted the entire chained equation (19), and a stronger endpoint does not formalize the paper's early/late route.

The return is advisory. The original packet, canonical statement catalogue, existing ties, source files, and repository have not been changed. No concurrent section return has been assumed. The separate uploaded `Pasted text(20261102-190839).txt` was unavailable and its contents were not inferred.

## Ranked and located corrections

### 1. Correct the exact identity's current evidence status

**Locations:** `CL-erased-zero-identity`, `CL-early-late`, `CL-formal-scope`; `LEAN_GAPS.md`, §6.4; evidence correction `erased-zero-equality-current-status`.

The mathematical identity is

\[
\Pr[\text{dummy run queries the erased zero}]=\mathbb EZ/m.
\]

Fix the entire dummy run. Exactly \(Z\) of the \(m\) independent uniform choices of the planted column select a discovered zero. Averaging proves the identity before any query-budget estimate is used. This argument prevents a nearby inequality from standing in for the equality.

`QuarticQuery.Paper.erasedZero_eq_expectedZeros_div` states that exact algebraic identity. It appears in the supplied current root-build declaration inventory and in the explicit transitive axiom audit. Its recorded axioms are `propext`, `Classical.choice`, and `Quot.sound`. The algebraic statement accepts arbitrary real finite weights; normalization and nonnegativity enter its probability interpretation, not the equality's Lean type.

The request and earlier source headers predate these receipts. Their historical status is recorded, but the replacement uses the newer source-bound evidence. No fresh compilation is claimed.

### 2. Keep the equality, the bound, and the complete row separate

**Locations:** `CL-early-late`; `lean/Eq19Complete.lean`; `NEW_STATEMENTS.json`, `r3-classical-eq19-conjunction`.

`QuarticQuery.avg_foundZero_I_le` and `QuarticQuery.Paper.eq_19` are upper bounds. Neither type contains the equality. `Paper.eq_19` is in the root inventory, but it is not individually among the 258 explicit axiom-audit targets. The equality and `Paper.expectedZeros_le_four` are explicit audit targets.

The packet has no compiled declaration conjoining both clauses of the whole display, and the current canonical row remains partially covered. The proposed wrapper proves

\[
p=\mathbb EZ/m\quad\land\quad \mathbb EZ/m\le4G/m^2
\]

from the separately evidenced ingredients. Its full declaration is supplied; it has no `sorry` or additional axiom. It is explicitly **uncompiled**. A future source-bound build, complete type/axiom inspection, and reviewed whole-row tie are required before promoting this proposal. These are integration requirements for the new wrapper, not open mathematical assumptions in Proposition 4.2.

### 3. Preserve the two search proofs and their different scope

**Locations:** `CL-early-late`, `CL-zero-worlds`, `CL-zero-average`, `CL-zero-optional`.

The ordinary paper route now exposes the positive-probability transcript argument. Before a column's zero has been found, its location is uniform among that column's unqueried rows. Early discoveries have conditional probability at most \(2/m\) per query, while every late-discovered column has consumed at least \(m/2\) queries. Hence

\[
\mathbb EZ_{\rm early}\le2G/m,\qquad
Z_{\rm late}\le2G/m,\qquad
\mathbb EZ\le4G/m.
\]

The supplied posterior declaration is exact, but the early/late counts and their separate inequalities have no supplied formalization. The formal expected-zero endpoint uses the different finite-world induction and gives \(\mathbb EZ\le2G/m\). The replacement proves this induction in ordinary mathematics and labels it as an alternative route.

The retained \(m+1\) reference-path refinement is also proved. A scan until discovery attains its expectation-cost inequality. That observation does not optimize distinguishing success for every fixed worst-case budget. No new optimality or novelty claim is made.

### 4. State the simulator's cap before using direct product

**Locations:** `CL-heavy`, `CL-simulator`, `CL-simulator-example`, `CL-joint-event`, `CL-conditioning-counterexample`.

The simulator receives only data jointly independent of the target tuple. It aborts before target query \(L+1\), and stops before answering the proposed certificate-cell query. Reading the coordinate's address is free; reading the cell bit would be a different operation. Its total target cap implies each separate input cap on every branch.

The proof therefore bounds the **joint event** of a nonheavy original run and a true-cell query under the original distribution. It does not invoke hardness after conditioning the inputs on nonheaviness. The explicit promised-AND example shows that such conditioning can increase success from the one-query upper bound \(2/3\) to \(1\).

Source proposed-query index \(t\) is zero-based; prose query time \(q\) is one-based, with \(t=q-1\). The correspondence records this translation and the substitution lemmas preventing target values from being read as free outside data.

### 5. Label absolute-value statements as stronger than the target displays

**Locations:** `CL-first-difference`, `CL-discrepancy`; evidence correction `absolute-vs-one-sided`.

The baseline already used absolute output gaps. The replacement preserves those statements and explicitly calls them strengthenings of the preprint's one-sided equations (18) and (23). The current `Paper` wrappers support those absolute statements. The older core one-sided theorem remains separately identified. This is a correction to the source relation, not a silent alteration of a canonical baseline claim.

### 6. Separate exact tails, finite estimates, floors, and eventual hardness

**Locations:** `CL-tail-numeric`, `CL-forrelation-input`, `CL-floors`, `CL-concrete-lower`.

The exact paper envelope \(m^{2-20\log_2(3/2)}/100\), convergence of that envelope, convergence of the actual tail, and the elementary \(m^{-10}\) bound are distinct claims with distinct source declarations. The finite estimate gives the discrepancy upper bound \(6/100<1/3\) as soon as \(1\le L\le m\). It removes an unnecessary additional large-size condition at this numerical step.

The two floors are proved in the correct lower-bound direction. For \(k\ge2\), \(m=4^t\), and \(t\ge8\),

\[
G\ge\frac{m^{2-1/k}}{400(\log_2m)^2}.
\]

The arithmetic constant \(1/400\) and the threshold \(t\ge8\) are uniform in \(k\); the prerequisite \(L<R(P_{k,m})\) still has a threshold depending on the fixed \(k\). With natural logarithms the coefficient is \((\ln2)^2/400\).

The supplied historical floor check allowed a \(+1\) slack. The new check uses exact integer-root brackets and verifies the literal inequality without that slack. Finite checks do not replace the universal proof and do not certify the Forrelation hardness threshold at the tested sizes.

### 7. Retain exact circuit and parameter quantifiers

**Locations:** `CL-generic-statement`, `CL-concrete-lower`, `CL-formal-scope`.

The generic lower bound applies to every realizing circuit. It can therefore be applied to the circuit already selected for the quantum upper bound. The eventual `Paper.prop_4_2` wrappers discharge the fixed-\(k\) hardness prerequisite through the supplied Forrelation endpoint. The core pointwise theorem still has its explicit hardness binder; later discharge does not change that core type.

The order is: fix an integer \(k\ge2\), then take sufficiently large \(m\). Section 7 obtains exponent \(4-2/k\), up to logarithms, on the same function. The family of fixed choices approaches four. This section makes no assertion that one fixed \(k\) attains a fourth power or that an unreviewed growing-\(k\) extension is available.

## Literature roles and source comparison

| Source and inspected edition | Exact use | Limit of the citation |
|---|---|---|
| OpenAI, supplied 5 October 2026 preprint, §4.2, equations (17)–(23), Proposition 4.2, pp. 12–14 | Target construction and lower-bound argument | The public pinned PDF fetch failed; the supplied local PDF/text was used. No remote/local byte identity is claimed. |
| Bansal–Sinha, arXiv:2008.07003v3, Theorem 1.3 and Corollary 1.4, p. 4 | Original Forrelation lower bound and parameter comparison | The separate §5.4 display issue is localized; this is not a complete audit of the paper or a refutation of its theorem. |
| Aaronson–Ben-David–Kothari, arXiv:1511.01937v2, §6.1, Definitions 14–15, pp. 20–21; §6.2, Lemma 17, p. 22 | Addressed-certificate construction ancestry | Lemma 17 is an upper-bound result for their cheat-sheet function, not a proof of the present planted lower bound. |
| Drucker, arXiv:1005.0644v2, §1.3, pp. 6–7; Lemmas 3.1–3.2, pp. 11–12; final paragraph of §3, p. 13 | Fair/per-input-capped direct-product antecedent and transcript product argument | The named prerequisite is the frozen baseline §6.1. The headline global-budget theorem has a different statement. Attribution of the fair case to Shaltiel is through Drucker, not a claim to have read Shaltiel's original paper. |
| Supplied QAOA long overview and expository §1 | Organization of an implication chain and a finite explanatory example | Writing specimens only; no authority for any quartic mathematical claim. |

For Bansal–Sinha, identify their block dimension \(N\) with \(m\), not with the total input length \(km\). Set their advantage parameter \(\eta=1/3\), so \(1/2-\eta/2=1/3\), and use promise threshold \(\delta=2^{-5k}\). At fixed \(k\), their stated lower bound dominates the chosen \(L\) by a logarithmic factor of order \((\log m)^{1+1/k}\).

The required §5.4 caveat is at `main.tex:1180–1181`. For a summation level \(j>k\), the compared logarithm exponents differ by \((j/k-1)/2\). The threshold at line 1184 is subsequent. Establishing the omitted displayed comparison requires additional justification. This return does not infer that the theorem is false or repair the entire parameter-uniform argument. Its proof consumes the weaker fixed-\(k\) input already established in the supplied §3 and its formal endpoint.

## Evidence record and verification

The source packet labels its repository snapshot `1dd469dd0042b937b739da3bc211eeb60bdf7462`. The successful root receipt records commit `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`. These labels differ. Binding to the supplied source is established by **124/124 matching local input hashes**, not by treating the labels as identical.

The root receipt records `lake build QuarticQuery` at `2026-11-02T18:25:39.383153+00:00`, and has a declaration inventory of 2,652. The final supplied type/axiom audit has 124/124 matching input hashes, 3/3 matching candidate files, all seven recorded guards true, and the log marker `R2_AXIOM_AUDIT_OK declarations=258`. Source and log hashes also match. Focused closures match for `ClassicalPlanted` (16), `ClassicalUniformZero` (17), `ClassicalAsymptotics` (57), `ClassicalDirectProduct` (6), and `Section4` (57).

These are audits of supplied receipts and their source binding. Neither `lean` nor `lake` is available in this environment. No new Lean build or Comparator run was performed. Compiled artifact binaries are absent, so their recorded hashes were not independently recomputed. The full external Mathlib source closure and the semantics of all 258 audited declarations were not re-audited.

The exact pinned toolchain is `leanprover/lean4:v4.36.0-rc2`; dependency revisions and complete receipt identities appear in `source_read_receipt.json` and `evidence/lean_evidence.json`. Compiler-reported types are distinguished from source-type reconstructions with explicitly restored surrounding binders. No source reconstruction is described as fresh elaboration.

### Exact finite computation

`checks/planted_example.py` independently implements the 192 physical coordinates of the four-column XOR example and its winning predicate. It enumerates 4,096 dummy configurations and 16,384 coupled choices, including 3,145,728 checks of where an input bit can change. The exact results include

\[
\mathbb EZ=3/8,\quad p_{\rm erase}=3/32=(3/8)/4,\quad
p_{\rm cell}=1/16,\quad \text{output gap}=1/16.
\]

For the fixed target column and fourth proposed query, the nonheavy true-cell event has probability \(1/8\), contained in capped-simulator success of probability \(1/4\). Exhaustive one-query XOR optimization gives \(1/2\), so the two-instance value is \((1/2)^2=1/4\). The simulator trace includes a branch that aborts before a second target query. A separate three-input promised-AND computation demonstrates the conditioning error.

The example fixes the other columns' input strings. It is a conditional-outside-data illustration, not the full theorem distribution. Its address length \(r=2\), budget \(G=4\), and XOR function differ from the asymptotic Forrelation specialization. It has no late discoveries, so the late-discovery estimate is supported by the general proof, not a nontrivial numerical test of that branch.

`checks/check_floors.py` verifies 187 cases, \(2\le k\le12\) and \(8\le t\le24\). It uses integer powers, exact integer-root brackets, and rational tail arithmetic. The literal floor bound, \(1\le L\le m\), and discrepancy threshold all pass. Generality comes from the induction and floor proof in `section.md`.

`checks/validate_return.py` checks the required return files, JSON, 26 stable passage boundaries, display inventory, complete-type fields, bibliography keys, internal file links, and final manifest hashes. Its structural checks are not a theorem prover or intended-statement comparator. The final outcomes are recorded in `validation.json`.

## Simplification attempts and decisions

Two concrete simplifications were considered. First, using only the coefficient-two search induction would shorten the lower-bound proof. The replacement retains the early/late proof because the assignment requires reconstruction of the paper's route, and retains the induction because it explains the actual formal endpoint. Neither route is advertised as a new result.

Second, replacing the logarithmic tail argument by \((2/3)^{40t}\le m^{-10}\) eliminates a numerical eventuality condition. This simplification is used for the contradiction. The exact logarithmic envelope and its limit are retained separately for fidelity to the source display. This gains a direct finite bound without erasing a requested statement.

The optional \(m+1\) argument is kept in a labeled passage because it was already a significant ordinary refinement in the baseline. It is not required for the proposition, and its presence does not suggest a larger asymptotic exponent.

## Paper-authoring receipt

The fields below record exercised authoring checks. They are not a human review, readability score, or publication acceptance.

**object:** A self-contained replacement of long-record §§6.2–6.6, plus the requested evidence and source correspondence.

**genre_and_target_reader:** Long mathematical reasoning record for researchers familiar with basic query complexity. The reader need not remember the precise cell layout, which is recalled at entry.

**venue_calibration:** Advisory research exposition and formalization handoff; no venue submission or short-paper claim.

**contribution_type:** Reconstruction, clarification, exact finite illustration, and correction of evidence descriptions. No priority or mathematical novelty claim.

**headline_claim_and_evidence_class:** Ordinary proof of the planted lower bound and its fixed-\(k\) specialization. Existing formal endpoints have supplied source-bound receipts. The proposed whole-row wrapper is uncompiled. Computations are exact finite checks.

**scanability_check_title_abstract_intro_theorems_conclusion:** The section title, replacement scope, generic theorem, and final Proposition 4.2 identify the object and conclusion. A standalone abstract is unnecessary for this section return. The final formal-correspondence paragraph states the evidence boundary once in detail.

**external_field_map:** The target OpenAI proof, Bansal–Sinha hardness input, Drucker capped direct-product antecedent, and ABK construction ancestry have separate roles, versions, and locators in the table above.

**internal_dependency_map:** §4 definition and realizing circuit; frozen §6.1 capped direct product; minimax distribution; common coupling; erased-zero identity and search; heavy counting and capped simulator; discrepancy contradiction; §3 fixed-\(k\) Forrelation hardness; two floors; same-circuit Proposition 4.2; §7 exponent consumer.

**concrete_anchor_and_example_boundary:** Four columns, explicitly listed zeros, two-bit XOR strings, complete transcripts and pointers, a four-query tree, and a simulator trace. Exact scope and the absence of late discoveries are recorded above. The separate AND example isolates selection bias.

**hard_step_and_proof_forward_decisions:** The adaptive transcript law and simulator event containment are made explicit before their estimates are used. The independent planted index is averaged only after fixing the complete dummy run. The total cap is established on every simulator branch.

**mathematical_taste_rubric_evidence_and_dispositions:** The proof reveals two distinct hiding mechanisms; the example exposes actual queried information; repeated queries and stopped branches are handled; theorem hypotheses and quantifier order are visible. A general-purpose survey or additional formal campaign would not improve this focused return. No numerical taste score is assigned.

**concrete_simplification_attempt_and_outcome:** The coefficient-two-only option was declined to preserve paper-route fidelity. The finite \(m^{-10}\) tail was adopted for the contradiction while retaining the exact-log claim separately.

**difficulty_landscape_and_fertile_questions:** The load-bearing difficulty is preserving the original independent input law under adaptive simulation. Remaining formal work is principally the exact conjunction and early/late trace counts. A sharp fixed-budget distinguishing curve is outside scope and is not settled by the expectation-cost refinement.

**short_long_transfer_locators:** This return changes the long record only. A later short treatment can use the generic theorem, coupling, capped-simulator argument, and final floor inequality at `CL-generic-statement`, `CL-first-difference`, `CL-joint-event`, and `CL-concrete-lower`; no such companion has been created.

**notation_definition_and_equation_grammar:** \(P,C,m,r,L,G,J,I,Z\), true addresses, heavy columns, and simulator time are defined before use. Displays are connected to their hypotheses. Base-two and natural logarithms are distinguished at the explicit constant.

**first_time_reader_house_jargon_scan:** No unresolved house jargon in the proof. Fully qualified declaration names are concentrated in formal correspondence and supporting files. The opening defines the addressed function and its cells.

**one_use_symbol_scan:** No unexplained one-use symbol. Local counting variables \(n,d,q\), the reference-path positions \(p_s\), and the floor quantity \(a\) each support a displayed calculation and remain local.

**conditional_hypothesis_restrictiveness:** Stated. \(L<R(P)\), promise support, joint independence, positive-probability transcript conditioning, and a worst-case cap are explicit. The specialization fixes \(k\) before the size threshold. Finite-example parameters are separate.

**citation_role_checks:** Completed for the three original literature sources and the supplied preprint at the stated locators. The broad source claims and local display caveat are separated. Bibliographic keys were made consistent with the section.

**lean_statement_correspondence_and_validation_refs:** `correspondence.json`, `evidence/lean_declarations.json`, `evidence/lean_evidence.json`, and `LEAN_GAPS.md`. Complete compiler types, reconstructed source types, ordinary premises, proof route, and actual receipt scope are separately labeled.

**compressed_claim_occurrences_and_post_edit_scope_check:** The opening, generic theorem, final proposition, and formal summary retain the same fixed-parameter and same-circuit scope. Absolute displays are labeled stronger than the preprint. No endpoint statement silently acquires the paper's intermediate proof route.

**bibliography_render_check:** Citation keys, primary URLs, edition dates, theorem numbers, and printed pages checked. BibTeX/Markdown sources were not rendered as a final typeset bibliography.

**figure_and_reproducibility_check:** Two exact example tables are in the Markdown. Code and resulting JSON accompany them. No generated scientific image or external figure is used. The general proof is independent of the enumeration.

**cold_reader_confusion_and_disposition:** Independent agent rereads identified the need to resume general parameters explicitly after the toy, explain the finite minimum in randomized query complexity, distinguish stronger absolute wrappers from core one-sided results, state \((\ln2)^2/400\) unambiguously, and restore missing section binders in type records. These corrections were applied. This was AI-assisted review, not human review.

**version_bound_review_coverage_and_omissions:** Complete assigned baseline sections and the named adjacent interfaces were assessed. The three literature papers were sampled at their stated locators; first four pages and relevant proof sections were read. The entire analytic Forrelation proof, unrelated manuscript sections, external library source closure, and every Comparator challenge were not audited. Detailed per-reader scope is preserved in `source_read_receipt.json`.

**material_transition_warrants_and_source_conflicts:** Every transition states the needed cap, independence, support, or threshold. Current exact-byte receipts take precedence over stale unelaborated labels for the matching live source. Different recorded commit labels are not conflated.

**exact_open_boundary:** No ordinary implication remains open within the assigned proof. The new equation-(19) conjunction requires compilation and evidence binding; the early/late subclaims, \(m+1\) refinement, arbitrary-coin pushforward, and new examples have no newly supplied formal proof. Whole-row ties are not promoted. The separate unavailable text attachment remains unread.

**rendered_release_checks:** `section.md` was successfully parsed with Pandoc's Markdown mathematics reader. No PDF or DOCX was requested or generated, and no visual PDF layout review was performed. JSON, relative file links, archive contents, and manifest hashes are checked separately. No unavailable register-profile score is fabricated.

**deliberate_non_changes:** Canonical baseline statement IDs and mathematical claims are retained; `STATEMENT_CHANGES.json` is empty. New proposals are separately registered. Original source files and existing ties remain untouched; no publication, merge, or acceptance is implied.
