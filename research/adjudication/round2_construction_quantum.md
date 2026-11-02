# Round-two construction and quantum-upper adjudication

Date: 2 November 2026. Scope: returns `2_lean_construction` and
`3_lean_quantum_upper`. This review compares the returned sources with the live
Lean definitions and implementations. The returned mathematics is advisory;
submitted files under `research/returns/round2/` are preserved separately from
the integrating edits under `lean/`.

## Integration state

The integrated construction and quantum helper modules, including the complete
retained-state Lemmas 2.1 and 2.2, the coherent bounded-list tournament and the
literal tensor-state construction, now pass native Lake compilation at the
pinned toolchain. `Paper.Section2` and `Paper.Section3` also pass, preserving
the original public declaration names. Their source hashes and per-module
results are retained in the tie-candidate JSON. Final source-bound root evidence,
axiom auditing, Comparator and dependency reach remain separate integration steps. No shared definition in
`Statement.lean`, reviewed tie or generated corpus record is edited by this lane.

The earlier HDD checks were deferred or exhausted their resource budget without
a mathematical verdict. The current native results come from ordinary Lake on
the operator-authorized SSD cache, with continuous 8 GiB reserve monitoring.
Only terminal passes with unchanged local source closures are recorded as
passes; failed and blocked attempts remain in the runtime history.

## Mathematical dispositions

The construction return supplies a substantive statement-fidelity extension:
`construction_lemma_2_2_ii` keeps arbitrary complex coefficients of the test
index register, applies the exact test circuit in each orthogonal block, and
proves every wrong-label amplitude is zero. The complete statement connects
that same isometry to the physical compiler on every embedded state and every
continuation. Its `2(log₂ m+1)` bit-query cap keeps the compiler's factor of two.
The earlier `lemma_2_2` remains a uniform-index sampler statement.

`construction_lemma_2_1_ii_complete` similarly packages the *same* accurate
Forrelation isometry, retained workspace and physical continuation equation.
The all-input cap and Boolean law are independent of whether the promise holds;
correctness is conditional on the promised value. The randomized lower-bound
part continues to use the repository's alternative fixed-parameter proof.

Two qualifications are retained. `construction_projection_test` proves a
`k`-read sampler and its generic `2k`-bit-query compilation. The separate local
phase-kickback identity does not package a complete physical `Runs k` witness.
`construction_walkN_bound` and its prefix/butterfly companions concern ideal
integer sums. They do not establish that every modular circuit register stores
a signed intermediate without wraparound. The existing circuit endpoint and
size guarantee remain separate from that stronger register correspondence.

For Section 3, the coherent amplification induction and list-valued tournament
are useful extensions of the earlier measured continuation theorem. A bounded
list is now an actual `Samples` output alphabet, with normalization,
nonnegativity, its membership success bound, and an explicit physical query cap.
The perfect-indicator coupling introduces no verifier error. The zero-total-
weight case requires immediate failure, which the normalization proof states.

The literal fresh-register tensor state in `equation_15` is **not identified**
with the short-circuit implementation in `Upper.stage_samples`. The tensor
construction runs every comparison and retains all fresh registers; the
short-circuit implementation can omit later work after failure. They have the
same successful index law. The returned negative control exhibits equal
successful probability and unequal full state, supporting this distinction.

`amplification_budget_le` bounds the whole padded product used by `stageCost`
and `searchCost`, rather than inferring a bound on that product from the cap of
a smaller abstract process. The tournament exposes the explicit uniform bound
`6072 cc sqrt(m) T² log(T)` in ordinary bit queries. Probability statements
require nonnegative comparison probabilities and a positive conditioning event;
arbitrary-vector tensor identities are only mass identities until instantiated
with the unitary state witness.

The decoder, comparison, verification and error declarations expose existing
procedures and their exact all-input laws. The sorted-pair circuit supplies both
ordered comparison laws by complementing only the measured output label. The
final zero-input and one-input error statements keep their existential program
outside the universal input quantifiers.

The return does not identify the abstract returned-state amplification theorem
with its physical retained-register implementation. The latter proves the exact
successful label law, while the former proves the normalized successful-state
statement. A reviewed tie for the complete physical returned-state formulation
of Lemma 3.1 needs that additional bridge; neither the new list theorem nor a
shared success probability supplies it.

## Replayed package checks

- Construction: `python3 checks/validate_package.py` exited 0. This checks
  files, schema, markers and local import names; it neither elaborates Lean nor
  resolves the external base imports without its optional base packet.
- Quantum: a scratch copy's `checks/validate_bundle.py --packet
  /tmp/quartic-round2-review-packet` exited 0 with the current repository corpus
  supplied for cross-row references. Running without that packet fails the
  `statement_ids_resolve` check because the package deliberately references
  existing rows outside its assigned set; that is not a Lean failure.
- Quantum: the scratch copy's `checks/section3_checks.py` exited 0, including
  exact rational drift/list-law cases and finite floating-point geometry/budget
  probes. Both negative controls were detected. These are finite checks, not
  universal proofs or kernel receipts.

The received quantum validator writes `checks/static_validation.json` in its
own source directory. An initial in-place replay overwrote that one returned
receipt; it was restored byte-for-byte from the submitted archive
`quartic_r2_3_lean_quantum_upper_return.zip`. Subsequent runs use scratch copies.
The reusable lesson is to inspect received checkers for output side effects
before executing them, and run self-writing checks outside preserved custody.

## Per-target crosswalk

Every primary declaration below now belongs to a native-passed helper module
at the reviewed live source hash. The table records focused compilation only;
relation review, final root validation, dependency reach and Comparator
acceptance remain separate facts.

The [scoped tie candidates](round2_construction_quantum_ties.json) retain all
54 statement IDs, the original and amended texts, per-declaration relations,
ordinary premises, missing clauses and the exact reviewed source hashes. They
are a source-review handoff; they do not edit the corpus or claim a build.

### 2_lean_construction

| Statement | Candidate declaration | Compilation |
| --- | --- | --- |
| `def-log-convention` | `QuarticQuery.Paper.construction_log2_mValue` | native passed |
| `def-partial-query` | `QuarticQuery.Paper.construction_correct_on_domain_iff` | native passed |
| `def-query-oracle` | `QuarticQuery.Paper.construction_query_oracle` | native passed |
| `eq-1` | `QuarticQuery.Paper.construction_alphaTot_eq_inf` | native passed |
| `eq-2` | `QuarticQuery.Paper.construction_equation_two` | native passed |
| `def-transcript` | `QuarticQuery.Paper.construction_transcript_definition` | native passed |
| `def-walsh-sign` | `QuarticQuery.Paper.construction_walsh_definitions` | native passed |
| `eq-3` | `QuarticQuery.Paper.construction_equation_3` | native passed |
| `eq-4` | `QuarticQuery.Paper.construction_equation_4` | native passed |
| `eq-5` | `QuarticQuery.Paper.construction_equation_5` | native passed |
| `claim-bs-to-L` | `QuarticQuery.Paper.construction_claim_bs_to_L` | native passed |
| `claim-proj-prob` | `QuarticQuery.Paper.construction_projection_test` | native passed |
| `lem-2.1.ii` | `QuarticQuery.Paper.construction_lemma_2_1_ii_complete` | native passed |
| `claim-N-phi` | `QuarticQuery.Paper.construction_N_phi` | native passed |
| `claim-integer-tests` | `QuarticQuery.Paper.construction_integer_tests` | native passed |
| `claim-circuit-size` | `QuarticQuery.Paper.construction_circuit_costs` | native passed |
| `lem-2.1` | `QuarticQuery.Paper.construction_lemma_2_1_complete` | native passed |
| `eq-6` | `QuarticQuery.Paper.construction_eq6` | native passed |
| `def-column-layout` | `QuarticQuery.Paper.construction_column_layout` | native passed |
| `eq-7` | `QuarticQuery.Paper.construction_trueAddress_iff` | native passed |
| `eq-8` | `QuarticQuery.Paper.constructionOutwardPointers` | native passed |
| `def-winner` | `QuarticQuery.Paper.constructionWinner` | native passed |
| `cor-unique-winner` | `QuarticQuery.Paper.construction_unique_winner` | native passed |
| `def-win-at-address` | `QuarticQuery.Paper.construction_winsAt_iff_winner_and_address` | native passed |
| `def-K` | `QuarticQuery.Paper.construction_K_count` | native passed |
| `lem-2.2.i` | `QuarticQuery.Paper.construction_lemma_2_2_i` | native passed |
| `lem-2.2.ii` | `QuarticQuery.Paper.construction_lemma_2_2_ii` | native passed |
| `lem-2.2` | `QuarticQuery.Paper.construction_lemma_2_2_complete` | native passed |
| `cor-local-dichotomy` | `QuarticQuery.Paper.construction_local_dichotomy` | native passed |

### 3_lean_quantum_upper

| Statement | Candidate declaration | Compilation |
| --- | --- | --- |
| `prop-3.2` | `QuarticQuery.Paper.quantumTournament` | native passed |
| `claim-coupling` | `QuarticQuery.Paper.quantumList_coupling` | native passed |
| `claim-tournament-cost` | `QuarticQuery.Paper.quantumTournament_cost` | native passed |
| `def-grover-trial` | `QuarticQuery.Paper.quantum_grover_parameters` | native passed |
| `claim-grover-state` | `QuarticQuery.Paper.quantum_grover_state` | native passed |
| `claim-sin2theta` | `QuarticQuery.Paper.quantum_sin_two_angle` | native passed |
| `eq-9` | `QuarticQuery.Paper.quantum_eq_9` | native passed |
| `claim-coherent-access` | `QuarticQuery.Paper.quantum_controlled_bit_query` | native passed |
| `def-aij` | `QuarticQuery.Paper.quantumComparison_unordered_state` | native passed |
| `eq-10` | `QuarticQuery.Paper.quantumComparison_complementary` | native passed |
| `def-decode` | `QuarticQuery.Paper.quantumDecode` | native passed |
| `claim-decode-cost` | `QuarticQuery.Paper.quantumDecode_correct` | native passed |
| `def-comparison` | `QuarticQuery.Paper.quantumComparison_sorted` | native passed |
| `claim-comparison-state` | `QuarticQuery.Paper.quantumComparison_state` | native passed |
| `claim-winner-dominates` | `QuarticQuery.Paper.quantumWinner_dominates` | native passed |
| `def-verify` | `QuarticQuery.Paper.quantumVerify_fixedAddress` | native passed |
| `claim-verify` | `QuarticQuery.Paper.quantumVerify` | native passed |
| `claim-error` | `QuarticQuery.Paper.quantumError_bound` | native passed |
| `construct-sampler` | `QuarticQuery.Paper.quantumTensorStage_of_samples` | native passed |
| `eq-15` | `QuarticQuery.Paper.equation_15` | native passed |
| `claim-success-prob` | `QuarticQuery.Paper.quantumStage_success` | native passed |
| `eq-13` | `QuarticQuery.Paper.quantumDrift` | native passed |
| `claim-weight-lb` | `QuarticQuery.Paper.quantumWeight_lower` | native passed |
| `def-T-eps` | `QuarticQuery.Paper.quantumTournament_parameters` | native passed |
| `eq-11` | `QuarticQuery.Paper.quantumDominant_iff` | native passed |

## Focused validation

Focused construction/quantum module validation passed. Source-present,
build-attempted, build-passed and Comparator-accepted states remain separate
against the exact integrating source. The following records preserve the
unsuccessful setup and repair history as well as the later native passes.

At 16:22:13 UTC, serial future `cf_952e3e2332e04112bbcd` entered the shared host
slot after an 18.4-minute admission wait. Its first Lean child was actually
running `ConstructionDefinitions.lean` by 16:23:03. A native process sample at
16:29:03 showed `Lean_importModulesCore` and `Lean_readModuleDataPartsOfMod`;
`lsof` showed the external-drive Mathlib objects. The process had produced no
compiler diagnostics or module result. This is measured import overhead, not
a tactic failure or a successful check. Every helper imports the whole Mathlib
umbrella transitively through `Statement.lean`; no claim of a warm cache is
made from the presence of those object files.

The original HDD serial run was terminated with exit 117 before it supplied a
module verdict. After the operator authorized SSD recovery, the canonical
project received a verified APFS-cloned package cache. The replacement native
inventory is `cf_58aaa94feb484c52ad9e`, with runtime evidence under
`/Users/willcook/src/_builds/quartic-r2-ssd/native-inventory/`. It runs ordinary
`lake --no-cache build <module>:olean` targets sequentially, with an 8 GiB disk
reserve and an 1800-second admitted seat budget. It records per-target local
source-closure hashes before and after, compiler output and native Lake traces.

The Lean-only dependency-exporter regression passed (exit 0, 15.07 seconds),
after verifying that its exporter implementation exactly matches the current
`scripts/Reach.lean`. The first native mathematical target, `ForrelationLower.Stein`,
also passed (exit 0, 28.12 seconds): Lake rebuilt `Statement`, `Cube` and `Stein`
while reusing the rest of its 18182-job cone. This is an observation of usable
native caching after SSD recovery, not a proof verdict for the new Paper
modules. The subsequent per-target terminal results are recorded below.

That first SSD inventory ended at 17:30:25 UTC with exit 1. Its 46 records
include the exporter fixture, all 39 Paper targets and six changed Forrelation/
upper targets. Nine records passed, 13 failed elaboration and 24 were skipped
because an imported module failed. The remaining SSD reserve was 16.68 GiB.
Within this lane, `ConstructionPhase`, `QuantumAmplification`,
`QuantumComparison` and `QuantumWorkspace` passed; these are per-target results
with unchanged local source-closure hashes, not a whole-corpus success.

The released failed sources received the following repairs before retry:
the pinned `abs_add_le` name; removal of a tactic after simplification had
already closed its goal; an explicit product cardinality rewrite; a stable
true-address equality rewrite; reconstruction through the proved domain and
Option interfaces rather than dependent-if unfolding; exposed recursive tensor
register definitions and explicit finite/classical contexts; an empty-tensor
normalization proof; and beta reduction and an explicit bounded-list cap in
the tournament proof. These repairs preserve all saved candidate statement
texts. Their new source hashes are recorded in the tie-candidate JSON; all construction and quantum helper declarations subsequently passed native retries.


The accepted construction and quantum passes span the initial inventory and
retries 1–3. Every candidate declaration's current module, source hash, terminal
receipt, compiler log, object and Lake trace is bound in
`native_validation_observations` in the tie-candidate JSON. All 120 saved
candidate statement texts remain exact substrings of the reviewed live sources.
`Section2` then passed in 26.11 seconds and `Section3` in 13.06 seconds in retry 4,
with their complete local source closures unchanged. These module passes do not
assert that a row is reached by the headline theorem or that a partial tie has
become exact.

## Consequence handoff

- Canonical mathematical object: the Section 2 construction interfaces and
  Section 3 coherent amplification/list/tensor interfaces above.
- Credit and citations: OpenAI's preprint owns the construction and separation;
  BBHT/BHMT own the amplification geometry. Returned sources retain this credit.
- Lean: this lane owns focused elaboration and repairs; root owns the integrated
  library build and exact-source receipt.
- Corpus and Comparator: root reviews new ties and challenge scope only after
  successful elaboration. No return manifest is used as compilation evidence.
- Long reasoning record, expert paper, exposition/reader: root carries the
  retained-workspace distinction, literal tensor versus successful-law
  distinction, exact physical query units and the two remaining construction
  qualifications into the next packets after the seven-return batch is closed.
- External publication/review: no submission is authorized or performed by this
  lane; human review and community acceptance remain separate evidence classes.
- Continuation: no new research packet is generated here. Root owns batch
  completion and the source-current next asks.

`tao_pipeline_receipt`: input_stage = advisory proof drafts; output_stage =
source review and focused native verification; artifact = this report and the
integrating Paper modules; human_understanding_delta = the exact state and
query interfaces are separated; verification_state = package/finite checks
and focused native construction/quantum modules passed; publication_or_review_state = AI integration review,
no human review; canonicalization_state = existing Paper family, old public
names preserved; unresolved_downstream_bottleneck = integrated
source-bound root build, complete axiom audit, reviewed ties and Comparator; next_stage_owner = root integration.

`paper_assimilation`: paper = OpenAI nearly quartic separation; section = 2–3;
canonical_mechanism_family = addressed winner tests and amplified tournament;
relation = statement-fidelity extension; understanding_delta = distinguish
retained states from output laws and logical reads from physical queries;
evidence_boundary = reviewed source and focused native passes; final root/axiom/Comparator evidence is separate;
hard_step = coherent retained-register trial/list composition and common tensor
workspace; meaningful_failed_route = identical success law does not imply the
same full state; open_remainder = tight full projection physical witness and
complete modular-register range correspondence.
