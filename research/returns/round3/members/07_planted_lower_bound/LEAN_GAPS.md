# Formal and evidence boundaries, in section order

## Overall state

The ordinary planted-input proof in the assigned sections has been reconstructed without an unresolved mathematical implication. The remaining items below concern exact formal statements, proof routes, intended-statement ties, or fresh execution. They must not be described as a gap in Proposition 4.2 merely because an explanatory clause has no one-to-one formal wrapper.

The available environment has no lean or lake executable. No new compilation or Comparator execution was performed. The frozen packet does supply successful native build and transitive axiom-audit receipts. Their local source/configuration closures, audit source and log hashes were checked against the supplied bytes.

The root receipt has 124 matching local input hashes. The final axiom audit also has 124 matching local input hashes and three matching reviewed-candidate files. Focused closures match for ClassicalPlanted (16), ClassicalUniformZero (17), ClassicalAsymptotics (57), ClassicalDirectProduct (6), and Section4 (57). These counts do not cover the full external Mathlib source tree. The pinned toolchain and dependency revisions are recorded in source_read_receipt.json.

Recorded compiled-artifact hashes are available, but those binaries are not supplied. The audit confirms source binding and recorded outcomes; it is not an independent compiler reproduction.

## §6.2: minimax and address guessing

### Strict minimax margin versus weak endpoint

The source theorem QuarticQuery.exists_hard_distribution takes the ordinary premise that RLe P L fails and returns a normalized nonnegative promised distribution under which every depth-L tree succeeds with probability at most 2/3. Its complete type is in correspondence.json.

The nearest-point argument in the prose proves a uniform strict margin below 2/3. The weak source theorem does not state that margin, and its proof uses finite minimax rather than this convex-distance argument. The strict-margin strengthening is retained as the pre-existing baseline statement NCL-strict-hard-distribution with ordinary proof authority. It is not needed by the planted reduction.

### Arbitrary independent information

The supplied direct-product and randomized interfaces use finite trees and finite mixtures. The ordinary extension to arbitrary independent coins or side information groups outcomes by the finitely many capped trees they induce. No new Lean pushforward theorem from an arbitrary external probability space is supplied. This is not an extra unproved premise of the finite-model theorems.

The complete target tuple must be jointly independent of side information. Separate independence from each target alone would not justify the argument.

## §6.3: construction, supported values and coupling

The generic dummy/planted support theorem is supplied and compiled. Specializing it to the concrete Fkm definition is an ordinary definitional substitution; the current claim-Y-values row does not have a separate concrete-family conjunction wrapper. Do not equate generic component coverage with a whole-row acceptance record.

The consistency of the transcripts and the promised support are ordinary premises for the one-input value assertion. They are explicitly established by using actual evaluation transcripts and sampling from the domain. They are not unproved assumptions carried into the final proposition.

The inequalities for the output gap accept arbitrary transcript fillers; their role is to bound the change between two bit inputs. Consistency is needed when that planted input is subsequently declared an F=1 input.

The absolute-value forms of (18) and (23) strengthen the preprint's one-sided estimates. Current Paper.eq_18 and Paper.eq_23 state these stronger forms. A source relation should say stronger, not literal identity with a one-sided preprint display.

The finite XOR configuration uses the generic addressed construction with a different partial function, r=2 and G=4. It does not instantiate the Forrelation theorem or its asymptotic parameter range.

## §6.4: exact equality, endpoint bounds and proof route

### The equality is present in current evidence

QuarticQuery.Paper.erasedZero_eq_expectedZeros_div states:

~~~lean
theorem erasedZero_eq_expectedZeros_div
    {κ : Type} [Fintype κ] [DecidableEq κ] {ℓ r S : ℕ}
    (μ : BitInput κ → ℝ) (T : QueryTree (BitLoc ℓ r S κ)) :
    coupledAvg μ (fun A J I => foundZero T A J I) =
      expectedZeros μ T / ((2 ^ ℓ : ℕ) : ℝ)
~~~

This exact declaration is in the current root build receipt and in the source-bound transitive axiom audit. The latter prints only propext, Classical.choice and Quot.sound. The request and original return's unelaborated wording predate these receipts; preserving that status would be inaccurate for the current live file.

The algebraic theorem has no positivity, normalization, support or depth premise. The probability interpretation uses nonnegative normalized sampling weights and the independent uniform index built into coupledAvg.

### The complete equation-(19) conjunction remains absent

QuarticQuery.avg_foundZero_I_le and QuarticQuery.Paper.eq_19 are inequalities only. Paper.eq_19 is listed in the root declaration inventory but is not individually one of the 258 explicit axiom-audit targets. The separate equality and Paper.expectedZeros_le_four are explicitly audited.

The exact missing whole-display target is:
\[
p=\mathbb EZ/m\quad\land\quad \mathbb EZ/m\le4G/m^2,
\]
under a nonnegative normalized prior and T.depth ≤ G.

The proposed lean/Eq19Complete.lean assembles those audited ingredients, dividing the expected-zero inequality by positive m. It has no sorry or new axiom, but it has not been compiled. Before promoting the canonical row, the integration owner needs:

1. successful compilation at the pinned project/dependency state;
2. inspection of its complete elaborated type and transitive axioms;
3. a source-bound receipt naming that exact declaration;
4. a reviewed tie covering both clauses, with the alternative search route retained;
5. Comparator evidence only if the integration contract selects this wrapper for comparison.

This is the final uncompiled proposal in this return, not a claim that either mathematical clause is unproved.

### Posterior and early/late route

Paper.uniform_zero_given_transcript is supplied, compiled and explicitly audited. It refers to an actual adaptive transcript, NoZeroSeen, and strictly positive dummyTraceMass. It returns 1 divided by the number of unqueried rows on that set and zero elsewhere. Repeated coordinates are handled by a set of unqueried rows.

The early/late variables and their separate estimates remain prose-only:
\[
\mathbb EZ_{\rm early}\le2G/m,\quad
Z_{\rm late}\le2G/m,\quad
Z=Z_{\rm early}+Z_{\rm late}.
\]
The exact support needed for a paper-route formalization would define these counts on the actual trace, prove their partition of discoveredZeros, prove the adaptive per-step early bound, and prove the pathwise late count. No such complete route is supplied.

Paper.expectedZeros_le_four proves the endpoint through the existing stronger finite-world induction. It cannot certify the early/late intermediate statements. The coefficient-two endpoint and its source proof make no optimality claim.

### Optional m+1 refinement

NCL-erased-zero-mplusone has a complete ordinary reference-path proof, retained from the baseline. No supplied Lean proof states that refinement. The scan example is sharp for the expectation-cost inequality; it does not show an optimal distinguishing curve for every worst-case cap.

## §6.5: simulator and joint event

The simulator cap, substitution/no-leak lemmas and the per-column/per-time joint event are supplied. Paper.eq_21 states the event under the original law, with nonheaviness inside the event. It does not say that a conditional distribution given nonheaviness remains hard.

The source uses natural proposed-query index t starting at zero; the prose's time q starts at one. Use t=q-1. The simulator stops before answering the proposed query, so reading its address does not consume the cell bit or an extra target query.

The free outside-data branch must never read the placeholder target coordinates of the source's complete base input. The supplied dummy_update_of_aTarget_none and dummy_update_of_aTarget_some lemmas justify this source-level separation. Dropping that distinction would turn side information into illicit target advice.

The new AND counterexample is ordinary finite mathematics checked by exhaustive calculation, not a Lean semantic test.

## §6.6: discrepancy, limits, floors and final quantifiers

### Exact tail clauses

The source supplies distinct declarations for:

- the exact real-power identity;
- negativity of the logarithmic exponent;
- the finite bound with that exact exponent;
- convergence of the displayed envelope to zero;
- convergence of the actual G-tail to zero;
- the simpler m^-10 finite estimate.

Paper.classical_tail_parameters combines the exact finite bound and convergence of the actual tail. The envelope limit is Paper.classical_tail_envelope_tendsto. A row whose literal text includes both the envelope and its limit needs both components or a new compiled conjunction. The present return records the existing partial row and the additional exact component; it does not silently promote it.

### Pointwise conditional theorem versus eventual theorem

QuarticQuery.Gvalue_lt_R_Fkm has the explicit premise Lvalue k t < R(P k t). That premise is ordinary at that modular theorem's type.

QuarticQuery.Paper.prop_4_2 has no extra Forrelation lower-bound binder. Its proof calls the supplied fixed-k ForrelationLower.bansalSinhaLower and raises the threshold to at least 8. It quantifies over every realizing circuit after one threshold. Paper.prop_4_2_forrCircuit applies it to the canonical circuit. These wrappers are named in the supplied source-bound build and axiom audit.

This return checks the use and exact type of the fixed-k supplier, not the full analytic Forrelation proof or the full sharp uniform Bansal–Sinha theorem. That earlier assigned section remains the proof destination for the prerequisite. The planted proof does not require a growing-k estimate.

### Floors and finite tests

Gvalue_ge states the literal lower floor bound with coefficient 1/400 and t≥8. The earlier return-4 check used lower ≤ G+1. The new check_floors.py verifies lower ≤ G itself by integer powers and certified root brackets. It covers 187 finite cases, not all k,t; the general induction and floor proof are supplied in section.md.

The same selected circuit must define the function in both lower and upper bounds. Fixed k precedes the eventual size threshold. Neither a nearly quartic universal exponent nor these fixed-family estimates is a literal exact-fourth-power family at one fixed k.

## Execution and acceptance boundaries

No new Lean build, Comparator run, paper-author approval, external publication, repository merge, or human mathematical review is claimed. A completed section and ZIP are reviewable contributions. The only new Lean file is clearly marked uncompiled, and none of the canonical source files or ties were modified.
