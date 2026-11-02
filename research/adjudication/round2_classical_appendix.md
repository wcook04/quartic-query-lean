# Round 2: classical lower bound and Appendix A

This review owns returns `4_lean_classical_lower` and `5_lean_appendix_a`.
Both submissions explicitly mark every new Lean declaration unelaborated.
Their coverage tables are proposed correspondences, not compilation or
Comparator receipts. The original returned files remain the advisory evidence;
repairs belong under `lean/QuarticQuery/Paper/`.

## Mathematical assessment

The classical return supplies a genuinely different proof of the capped
direct-product theorem: normalized conditional continuation values, an actual
adaptive transcript rectangle law, the one-step product inequality, finite
iteration, and the bridge from actual terminal success to the potential. It
also makes the planted distribution's expectation laws explicit and derives
the undiscovered-zero posterior from the full adaptive transcript likelihood.
The posterior requires a positive conditioning probability and includes
repeated queries. These are stronger fidelity witnesses than citing the
existing endpoint alone.

The `claim-EZ` compound entry remains partial even if `expectedZeros_le_four`
compiles: it obtains the endpoint from the existing stronger coefficient-two
search theorem. It does not prove the paper's early/late decomposition. No
optimality claim for coefficient two is justified. Finite mixtures are the
formal randomized model; a new pushforward theorem from an arbitrary external
probability space is not supplied.

The asymptotic candidate preserves the exact real exponent
`2 - 20 * Real.logb 2 (3 / 2)` and fixed-parameter quantifiers. The geometric
identity gives its zero limit without replacing that exponent. The quotient
estimate fixes `k` and the query exponent before the family parameter tends to
infinity. Its constant and threshold are not uniform in growing `k`.

The Appendix return supplies the arbitrary nonnegative symmetric matrix
adversary route, its literal star and sensitivity-graph applications, an actual
degree-dimensional face restriction, the recursive Huang matrix, and
Midrijānis's decision-tree bound. Its proposed paper-route constant is
`35^4 = 1500625`; the polynomial block-sensitivity hybrid gives `19600`.
Neither replaces the existing independently assembled bound `20736` merely
because its source is present. The Huang multiplicity proof uses parity
anticommutation rather than the paper's trace count. The degree definition
uses the pinned library's function-space/Fourier representation and has no
new syntactic `MvPolynomial` uniqueness theorem.

## Source-prefactor finding

The two-bit parity check reconstructs an exact one-query ordinary bit-oracle
algorithm. The four-cycle adjacency adversary has norm two, both coordinate
masks have norm one, and its progress drops from two to zero in that query.
The exact check therefore saturates the factor two in the per-query bound.
At error `1/100`, the coefficient printed in Špalek–Szegedy Theorem 3.1
would give a lower bound greater than one. The Høyer–Lee–Špalek Theorem 1
coefficient includes the required denominator two. The literature review
independently checked these primary-source displays.

This is a local numerical-prefactor discrepancy and a correction to the
return's cited annex transcription. It does not refute the equivalence of
adversary formulations or change the quartic asymptotics. The exact Python
witness is ordinary mathematical evidence; the proposed Lean parity witness
is not implemented by the return.

## Verification record

The pinned project toolchain is `leanprover/lean4:v4.36.0-rc2`; Mathlib is
`69552756cd8a2d2d48763cf7279fd814d6a1224d` and complexitylib is
`62ca5c21461b2482e8bd12b7cb9b4937d887a33a`.

Supplemental commands run from return 5 were:

```text
python3 checks/source_coefficient_check.py
python3 checks/adversary_checks.py
python3 checks/huang_and_restriction_checks.py
```

All reported `passed: true`. The first uses exact integer/rational arithmetic;
the second includes 1920 exact controlled-phase overlap cases and 100 floating
matrix instances; the third checks 278 functions, 434 restrictions, and
recursive matrix dimensions zero through eight. These are separate from Lean
and Comparator acceptance.

The return 4 command
`python3 -I research/returns/round2/4_lean_classical_lower/checks/check_mathematics.py`
also passed, with output retained in `/tmp/quartic-r2-classical-math-checks.json`.
It checked 7776 exact conditional-value inequalities (including 1728 zero-mass
branch encounters), six positive adaptive-transcript fibers, 90 undiscovered
zero/transcript pairs, 37 budget cases and 138 integer-power floor cases. Its
negative controls demonstrate why conditional nonheavy success alone is not
the required joint-event estimate, and why a total query cap cannot replace
the per-instance cap.

Some supplied scripts write results beside their source. Rerunning the Huang
check and static validator initially rewrote two return JSON files. Both were
immediately restored byte-for-byte from the original ZIP; a SHA-256 comparison
against every manifest member then found zero mismatches in both returns.
Future reruns must copy the return to scratch or redirect the producer's
actual output, after inspecting its write behavior. No returned source is
repaired in place.

Lean checks and accepted source deltas are recorded below as they finish.
No full build or Comparator run is owned by this review lane.

### Initial compiler attempt

The first focused command, from `lean/`, is
`lake env lean QuarticQuery/Paper/Section4.lean` (execution session `23563`).
A process observation at elapsed `4:44` showed native Lean PID
`57759` in uninterruptible I/O state with `0:01.05` CPU time. Its open imports
were on the verified external `.lake` root under
`/Volumes/Demo Take Media/aiw-builds/lean/lean-c1aea0af31ff22dc02ee5972/`.
The later observation at elapsed `10:46` had advanced from
`Mathlib/Data/Option/Basic.olean.server` to `Aesop/Percent`,
`Batteries/Tactic/HelpCmd`, and `Mathlib/Algebra/GroupWithZero/Opposite`, with
`0:02.23` CPU time. This established cold import I/O as the observed bottleneck.

The terminal receipt was consumed once at the integration barrier. The command
exited `117`, `seat_budget_exceeded`, at the governed 1500-second seat budget.
It emitted no Lean theorem diagnostics and reports
`validation_state=not_completed` and `proof_scope=not_proof_evidence`.
The run identifier is
`cmdrun_20261102T155703Z_56201_147972000_68177a2c8c58`.
The guard sent `SIGTERM` and confirmed that child PID `56242` and its process
group exited. Native Lean PID `57759` was absent on the terminal check.
This is incomplete validation, not a proved theorem failure or build success.
No automatic UI wake is promised; the source freeze has been released and the
integration owner must choose the next admitted validation action.

The four `Classical*.lean` and ten `AppendixA*.lean` proposed modules have
been copied into the live `Paper/` source owner for repair. They retain their
unelaborated headers and are not imported by the library entry point. No
declaration in those files is accepted or eligible for corpus promotion yet.
The bounded order after the initial check is:

```text
ClassicalDirectProduct
ClassicalPlanted -> ClassicalUniformZero
ClassicalAsymptotics
AppendixAAdversary -> AppendixAPerron
AppendixASensitivity
AppendixAPerron + AppendixASensitivity -> AppendixASpectralAdversary -> AppendixAStar
AppendixAHuang -> AppendixARestriction
AppendixAHuangMatrix
AppendixAHuangMatrix + AppendixARestriction + AppendixAAdversary -> AppendixAHuangRoute
AppendixAStar + AppendixAHuangRoute -> AppendixA
```

## Consumer handoff

[The candidate tie review](round2_classical_appendix_ties.json) compares 44
primary declarations to the whole canonical statement while retaining the
original ledger text and hash. Every source reference carries its file hash,
declaration location and unelaborated signature. It records 14 exact, 14
stronger and 16 partial source correspondences; none is eligible for promotion
before compilation. Supporting declarations are recorded separately and never
lend exact credit to a primary theorem missing a clause.

This stricter check keeps `eq-16`, the supermartingale/finite iteration row,
the tail/envelope row, both per-query steps, final overlap/final progress and
the square/trace/multiplicity row partial at their primary declarations.
Their listed supporting source statements supply the missing mathematical
clauses, but an exact single-row challenge needs the corresponding conjunction
or an independently reviewed complete declaration. The generic planted-value
theorem still needs the concrete `Fkm` specialization. The degree-definition
review also distinguishes the supplied Fourier bridges from every claim in
the unique multilinear-polynomial/sign-change convention.

The candidate JSON parsed successfully, contains exactly the 44 expected unique
statement identifiers, and its 149 declaration source references matched the
current source hashes, names, signature hashes and locations. `make check-layout`
passed. Those checks validate the review artifact and its source binding, not
the candidate Lean proofs.

The parent integration owns `corpus/ties.json`, corpus regeneration, independent
challenges, compiled dependency extraction and full-build evidence. The exact
accepted declarations must be bound to successful validation before any
evidence promotion; the candidate list does not authorize it.
The existing writing requests own the long reasoning record, short expert
paper, examples-first exposition and reader plan; they should consume the
accepted proof mechanisms and their route qualifications after the entire
seven-return batch is adjudicated. New packets must not be generated from this
lane's intermediate state.

No publication or external acceptance is claimed. Source credit remains with
the preprint and the cited primary results. This review does not select a new
mathematical target or make a novelty claim.
