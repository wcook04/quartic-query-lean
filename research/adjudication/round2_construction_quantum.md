# Round-two construction and quantum-upper adjudication

Date: 2 November 2026. Scope: returns `2_lean_construction` and
`3_lean_quantum_upper`. This review compares the returned sources with the live
Lean definitions and implementations. The returned mathematics is advisory;
submitted files under `research/returns/round2/` are preserved separately from
the integrating edits under `lean/`.

## Integration state

The returned sources are copied into the existing `QuarticQuery/Paper/` source
family for focused elaboration. At this checkpoint they remain **unelaborated
candidates**, not accepted compilation or Comparator evidence. The original
Section 2 and Section 3 declaration names are retained. No shared definition in
`Statement.lean`, reviewed tie or generated corpus record is edited by this lane.

A bounded direct Lean check was submitted, but the host guard returned exit 75
and queued a command future; this is resource deferral, not theorem failure.
The initial inventory launcher continued past that typed defer and queued
later modules before their dependencies had completed. Those 21 dependent
futures were cancelled through the owner API, then the initial one-module
future was replaced by `cf_952e3e2332e04112bbcd`, one governed serial inventory.
It reported `waiting_host_admission` / `shared_lean_host_lock_busy`, with no
Lean output. The replacement runner stops on exit 75 and skips imports of
failed modules. It excludes the four modules depending on the concurrently
changing `ForrelationLower.Main` until that dependency is rebuilt. Direct
Lean output objects do not create Lake trace evidence; the later native Lake
build must validate the integrated source and produce its own current traces.
Build evidence will be inserted below only after actual terminal compiler
results are read.

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

Compilation in the table is pending until the focused terminal results below
exist. An entry in a returned manifest establishes a proposed source target,
not type correctness, a reviewed tie, dependency reach or Comparator acceptance.

The [scoped tie candidates](round2_construction_quantum_ties.json) retain all
54 statement IDs, the original and amended texts, per-declaration relations,
ordinary premises, missing clauses and the exact reviewed source hashes. They
are a source-review handoff; they do not edit the corpus or claim a build.

### 2_lean_construction

| Statement | Candidate declaration | Compilation |
| --- | --- | --- |
| `def-log-convention` | `QuarticQuery.Paper.construction_log2_mValue` | pending |
| `def-partial-query` | `QuarticQuery.Paper.construction_correct_on_domain_iff` | pending |
| `def-query-oracle` | `QuarticQuery.Paper.construction_query_oracle` | pending |
| `eq-1` | `QuarticQuery.Paper.construction_alphaTot_eq_inf` | pending |
| `eq-2` | `QuarticQuery.Paper.construction_equation_two` | pending |
| `def-transcript` | `QuarticQuery.Paper.construction_transcript_definition` | pending |
| `def-walsh-sign` | `QuarticQuery.Paper.construction_walsh_definitions` | pending |
| `eq-3` | `QuarticQuery.Paper.construction_equation_3` | pending |
| `eq-4` | `QuarticQuery.Paper.construction_equation_4` | pending |
| `eq-5` | `QuarticQuery.Paper.construction_equation_5` | pending |
| `claim-bs-to-L` | `QuarticQuery.Paper.construction_claim_bs_to_L` | pending |
| `claim-proj-prob` | `QuarticQuery.Paper.construction_projection_test` | pending |
| `lem-2.1.ii` | `QuarticQuery.Paper.construction_lemma_2_1_ii_complete` | pending |
| `claim-N-phi` | `QuarticQuery.Paper.construction_N_phi` | pending |
| `claim-integer-tests` | `QuarticQuery.Paper.construction_integer_tests` | pending |
| `claim-circuit-size` | `QuarticQuery.Paper.construction_circuit_costs` | pending |
| `lem-2.1` | `QuarticQuery.Paper.construction_lemma_2_1_complete` | pending |
| `eq-6` | `QuarticQuery.Paper.construction_eq6` | pending |
| `def-column-layout` | `QuarticQuery.Paper.construction_column_layout` | pending |
| `eq-7` | `QuarticQuery.Paper.construction_trueAddress_iff` | pending |
| `eq-8` | `QuarticQuery.Paper.constructionOutwardPointers` | pending |
| `def-winner` | `QuarticQuery.Paper.constructionWinner` | pending |
| `cor-unique-winner` | `QuarticQuery.Paper.construction_unique_winner` | pending |
| `def-win-at-address` | `QuarticQuery.Paper.construction_winsAt_iff_winner_and_address` | pending |
| `def-K` | `QuarticQuery.Paper.construction_K_count` | pending |
| `lem-2.2.i` | `QuarticQuery.Paper.construction_lemma_2_2_i` | pending |
| `lem-2.2.ii` | `QuarticQuery.Paper.construction_lemma_2_2_ii` | pending |
| `lem-2.2` | `QuarticQuery.Paper.construction_lemma_2_2_complete` | pending |
| `cor-local-dichotomy` | `QuarticQuery.Paper.construction_local_dichotomy` | pending |

### 3_lean_quantum_upper

| Statement | Candidate declaration | Compilation |
| --- | --- | --- |
| `prop-3.2` | `QuarticQuery.Paper.quantumTournament` | pending |
| `claim-coupling` | `QuarticQuery.Paper.quantumList_coupling` | pending |
| `claim-tournament-cost` | `QuarticQuery.Paper.quantumTournament_cost` | pending |
| `def-grover-trial` | `QuarticQuery.Paper.quantum_grover_parameters` | pending |
| `claim-grover-state` | `QuarticQuery.Paper.quantum_grover_state` | pending |
| `claim-sin2theta` | `QuarticQuery.Paper.quantum_sin_two_angle` | pending |
| `eq-9` | `QuarticQuery.Paper.quantum_eq_9` | pending |
| `claim-coherent-access` | `QuarticQuery.Paper.quantum_controlled_bit_query` | pending |
| `def-aij` | `QuarticQuery.Paper.quantumComparison_unordered_state` | pending |
| `eq-10` | `QuarticQuery.Paper.quantumComparison_complementary` | pending |
| `def-decode` | `QuarticQuery.Paper.quantumDecode` | pending |
| `claim-decode-cost` | `QuarticQuery.Paper.quantumDecode_correct` | pending |
| `def-comparison` | `QuarticQuery.Paper.quantumComparison_sorted` | pending |
| `claim-comparison-state` | `QuarticQuery.Paper.quantumComparison_state` | pending |
| `claim-winner-dominates` | `QuarticQuery.Paper.quantumWinner_dominates` | pending |
| `def-verify` | `QuarticQuery.Paper.quantumVerify_fixedAddress` | pending |
| `claim-verify` | `QuarticQuery.Paper.quantumVerify` | pending |
| `claim-error` | `QuarticQuery.Paper.quantumError_bound` | pending |
| `construct-sampler` | `QuarticQuery.Paper.quantumTensorStage_of_samples` | pending |
| `eq-15` | `QuarticQuery.Paper.equation_15` | pending |
| `claim-success-prob` | `QuarticQuery.Paper.quantumStage_success` | pending |
| `eq-13` | `QuarticQuery.Paper.quantumDrift` | pending |
| `claim-weight-lb` | `QuarticQuery.Paper.quantumWeight_lower` | pending |
| `def-T-eps` | `QuarticQuery.Paper.quantumTournament_parameters` | pending |
| `eq-11` | `QuarticQuery.Paper.quantumDominant_iff` | pending |

## Focused validation

Pending. Source-present, build-attempted, build-passed and Comparator-accepted
states must be recorded separately against the exact integrating source.

At 16:22:13 UTC, serial future `cf_952e3e2332e04112bbcd` entered the shared host
slot after an 18.4-minute admission wait. Its first Lean child was actually
running `ConstructionDefinitions.lean` by 16:23:03. A native process sample at
16:29:03 showed `Lean_importModulesCore` and `Lean_readModuleDataPartsOfMod`;
`lsof` showed the external-drive Mathlib objects. The process had produced no
compiler diagnostics or module result. This is measured import overhead, not
a tactic failure or a successful check. Every helper imports the whole Mathlib
umbrella transitively through `Statement.lean`; no claim of a warm cache is
made from the presence of those object files.

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
source review and pending formal verification; artifact = this report and the
integrating Paper modules; human_understanding_delta = the exact state and
query interfaces are separated; verification_state = package/finite checks
passed, Lean pending; publication_or_review_state = AI integration review,
no human review; canonicalization_state = existing Paper family, old public
names preserved; unresolved_downstream_bottleneck = focused and integrated
Lean checks, reviewed ties and Comparator; next_stage_owner = root integration.

`paper_assimilation`: paper = OpenAI nearly quartic separation; section = 2–3;
canonical_mechanism_family = addressed winner tests and amplified tournament;
relation = statement-fidelity extension; understanding_delta = distinguish
retained states from output laws and logical reads from physical queries;
evidence_boundary = advisory sources plus finite checks until Lean completes;
hard_step = coherent retained-register trial/list composition and common tensor
workspace; meaningful_failed_route = identical success law does not imply the
same full state; open_remainder = tight full projection physical witness and
complete modular-register range correspondence.
