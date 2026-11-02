# Independent Lean/evidence review of the draft replacement section

Reviewed `/workspace/scratch/acdc3d4581d7/return/section.md` on 2 November 2026 against the focused construction source audit and the current packet's source-bound receipts. No edits to the draft and no new native Lean execution were performed. Correspondence generation was still in progress and is not covered by this review.

## Verdict

The ordinary construction proof and its intended Lean correspondences are sound within the inspected scope. In particular, the draft preserves the realization premise for the local equivalence, keeps arbitrary-index retained workspace separate from the clean XOR corollary, charges ordinary physical bit queries, and explains winner domination without assuming an opponent's promise. The following source-status and precision corrections should be made before delivery.

## Required corrections

### 1. AC-evidence: do not imply that every named core declaration was in the selected type/axiom audit

Current wording:

> The frozen packet includes a source-bound successful root-build receipt and a later type/axiom audit for these declarations.

The preceding paragraphs name both core declarations and newer Paper wrappers. The root receipt includes all of them, but the selected 258-name type/axiom audit does **not** include the core `gateConsistent_iff_eq_circuitEval`, `winsAt_unique`, `existsUnique_gateConsistent`, `winner_no_incoming_zero`, `winner_finds_zero`, or `winsAt_iff_localTests` by exact name. It includes the newer complete construction wrappers and `quantumWinner_dominates`.

Suggested replacement:

> The frozen packet's source-bound successful root-build receipt includes these declarations. A later selected type/axiom audit includes the new Paper construction wrappers, including `construction_lemma_2_2_complete` and `construction_pointer_every_physical_coordinate`; its exact declaration list is recorded separately.

Then retain the already correct statements about the 124 matching local inputs, no rerun, and exact Comparator membership. The source-bound construction Comparator separately supplies comparison for the four core mathematical statements and their wrappers; this is not the same as exact membership in the selected audit.

### 2. AC-coherent: make input independence of workspace dimensions and starting states explicit

Current wording:

> ... the workspace may depend on (y) and remains available for inversion.

The theorems choose the finite workspaces, starting kets, output functions, and circuit before the universal input quantifier. Only the **final workspace state** depends on the input. Say:

> The workspace dimensions and initial states are fixed before y. The final workspace state may depend on y and remains available for inversion.

This preserves the query-model quantifier order and removes an avoidable ambiguity.

### 3. AC-comparison: state the range of epsilon

Introduce `0<ε<1` when specifying the desired decoder error before equation (4.19). The concrete Lean wrapper uses `0<ε≤1`, `t≥1`, positive k, and the explicit repetition lower bound for `ε/(40*t)`. The paper-family address length is at least 40, so the stricter prose range safely satisfies the earlier promise decoder's requested error range. The section need not repeat the long repetition formula, but the full correspondence must retain it.

### 4. Source locator wording: the printed Lemma 2.2 has no enumerated parts

The section currently attributes `Lemma 2.2(i)` and `Lemma 2.2(ii)` to OpenAI. Those are convenient ledger subdivisions, but the supplied preprint prints a single unpartitioned Lemma 2.2. Use “the classical part of Lemma 2.2” and “the coherent part of Lemma 2.2” in mathematical citations. Keep `lem-2.2.i` and `lem-2.2.ii` as the exact sidecar statement IDs.

### 5. Rendering issues visible in the draft

Most inline mathematical expressions currently appear as bare parenthesized text such as `(P:D\to\{0,1\})`, `(m)`, and `(S=O_k(...))`; these should have valid Markdown math delimiters. Equation (4.12) has `W(y;i,s)quad` where `W(y;i,s)\quad` is intended. The tuple of rival labels near the end of AC-comparison is `(00,01,10,) or (11)`, which should be normalized to four cleanly displayed labels.

## Recommended precision improvement

In AC-coherent, “preserves all coefficients and relative phases” is easiest to justify by the explicit linear identity (4.15). A controlled unitary preserves coherence but can put branch-dependent phases into the output states `ψ_{e,y}`. It does not generally leave the reduced test-index state unchanged. Prefer “The operator acts linearly with the given complex coefficients and retains the index register” or equivalent precise wording. This is a wording refinement, not an error in (4.15).

## Checked mathematical points

* **Circuit premise:** (4.1) gives exact domain recognition on every raw input and conditional value correctness. The value bit off promise is unrestricted. The transcript induction is independent of this premise; the semantic/local bridge uses it.
* **Winner definition:** (4.5) is equivalent to `WinsAt` through the unique transcript lemma. Its semantic match to the paper requires no circuit-realization premise. Pair uniqueness and totality remain valid for arbitrary C.
* **Test list:** the circuit outputs receive both their gate equations and separate domain/value tests. The count `m+(m−1)+r(S+2)` is correct; the exact explicit size bound is the current `construction_K_bound` conclusion.
* **Pointer support:** the argument shows all `m+ℓ` physical coordinates are essential, while only `ℓ+1` are read on a path. The attribution to the old ledger is correct.
* **Retained-work coherence:** (4.15) matches the fixed-candidate, arbitrary-test-index scope of `_ii`; its workspaces and initial kets can depend on the label, but not the raw input. Unit norm of every output state follows from the unitary witness.
* **Physical cap:** retaining history with at most d abstract reads, compiled by two ordinary bit queries per read, gives at most 2d physical queries. Padding inactive branches is allowed and remains input-independent as a circuit operation.
* **Clean XOR:** compute, copy the exact output, and invert gives the separate ordinary 4d corollary. Because every index block has a certain Boolean output, copying does not disturb its work state. The draft correctly declines to assign a named checked clean-XOR theorem to this consequence.
* **Uniform evaluation:** orthogonal index blocks give h/K for failure detection, including the zero case. This is a specialization of arbitrary-index coherence, not its converse.
* **Winner domination:** a winner is never disqualified; correct decoding of its own address disqualifies every opponent. The event inclusion is valid without opponent correctness or independence. Retained orthogonal label blocks justify the same calculation in the coherent implementation.
* **Evidence:** the narrow Construction Comparator list is accurately stated. The current root/source hashes supersede stale “unelaborated” comments. No fresh native execution or human review is claimed.

## Unassessed in this review

The finite example's exact gate list, generated data files, and output counts are owned by the separate example review; the mathematical layout and failed-test reasoning in the draft are consistent with the construction. Historical-source page locators other than the unpartitioned Lemma 2.2 observation are owned by the source/literature reviewer. This review does not certify the final generated correspondence JSON or the packaging validation.
