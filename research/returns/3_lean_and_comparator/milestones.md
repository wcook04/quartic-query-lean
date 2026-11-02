# Ordered milestones and pass tests

This is an execution plan, not a record of completed formalisation. The current
return is research and design. Every gate below needs its own actual receipt.
Full source locations and fixed commits are in the model and Comparator designs.

## M0. Freeze input identity and the dependency closure

Retain the exact paper bytes, original 118 ledger IDs, corrected statement text,
source locations and all dependency SHAs. Keep Lean v4.36.0-rc2 and complexitylib
62ca5c21461b2482e8bd12b7cb9b4937d887a33a with its own resolved manifest, including
Mathlib 69552756cd8a2d2d48763cf7279fd814d6a1224d and CSLib
254e30e6d4299c51323aaeaf5f51a4763b375d4a. Do not mix in a sampled master revision.

**Pass:** a clean development build at that closure succeeds; versions, source
hashes and licence files are recorded. Reconcile the missing historical Drift
completion receipt by a new build. Hash agreement alone is not build evidence.

## M1. Freeze the public model and test declaration identity early

Elaborate the concrete definition layer, including partial and total Boolean
functions, literal bit oracle, adaptive quantum programs, tree randomization,
R/Q minima, exact Forrelation, bit locations, circuit transcripts and WinsAt.
Prove read-all witnesses, attainable minima, constant/empty-domain behavior,
R<=D<=number of bits and normalization of the quantum evaluator. Prove cost
invariance under coordinate bijections.

Before the large proof effort, compile a tiny Statement/Challenge/Solution
bundle using the real public definitions. Named public helper lemmas may be
needed for proof terms embedded in subtype constructors. Keep central
definition bodies fixed, including Q, R, P and Fkm.

**Pass:** the positive bundle accepts; a changed definition body and weakened
theorem are rejected with the intended diagnostic; source-generated common
definitions agree in exported declaration identity; feasible-set lower-bound
lemmas explicitly use proved nonemptiness. The successful model audit is
recorded separately from the Comparator receipt.

## M2. Construction, exact local tests and ideal tournament

Build the generic exact-circuit interface and physical bit layout. Prove
transcript uniqueness, the equivalence to the paper's true-address winner,
unique winner, the K local tests and their decision-tree costs. Prove the
pointer encoding is a bijection at m=4^t and counts ell physical queries.

Port/build the attached finite drift calculation. Add probability bounds,
normalized pivot laws, W=0 absorption, finite iteration, the winner weight
bound and the ideal-list guarantee. Use `Nat.clog 2 (1000*m)` for T.

**Pass:** all construction and classical tournament declarations in this
milestone compile without mathematical hypotheses beyond their explicit
parameters. In particular, the pointer test is a depth bound, not a fixed-
support bound. Comparator checks the advertised declarations and their
characterization theorems; definitions themselves stay fixed in the closure.

## M3. New randomized lower bound, conditional on hardness of P

Adapt finite minimax to a promised domain. Prove capped adaptive direct product
using transcript factorization and finite continuation values. Define dummy
and planted inputs; prove their function values; formalize the coupled run,
early/late zero discoveries, heavy-column count and the aborting address
simulator. Preserve joint events rather than conditioning on nonheaviness.

First prove a generic finite lemma under the displayed discrepancy bound.
Then specialize to m=4^t, r=40t and G=floor(mL/100). The elementary estimate
`(2/3)^(40t) <= m^(-10)` gives a discrepancy at most 6/100 when 1<=L<=m.

**Pass:** a compared theorem proves `floor(mL/100) < R(F)` for the actual
constructed function, with the explicit premise `L < R(P)` and exact-circuit
correctness. Yao/minimax and direct product are no longer hypotheses. Every
remaining premise is extracted into the result record and shown to readers.

## M4. Quantum bridges and the existing universal upper-bound route

Prove literal-bit/controlled-phase conjugation and finite coordinate/workspace
transport. Compile fixed procedures into adaptive programs. Prove that every
adaptive program can be deferred/padded into a fixed sequence at a stated
constant query overhead with the same output distribution. Handle empty input
types and constant functions explicitly.

Transport complexitylib's per-algorithm degree, block-sensitivity and quartic
bound to the public Q. The imported quartic statement is a useful independent
test of the lower-bound direction of the bridge.

**Pass:** the universal total-function upper bound is proved for the exact Q
used by this project. The proof contains no model-equivalence parameter. Any
factor from the bridge appears in the finite constant. This closes Theorem A.1
through an alternative route, not every appendix row.

## M5. Bounded amplification and the probabilistic tournament

Port the inspected Troy Lee amplifier to the selected dependency closure.
Establish its native/XOR/public-model transport, zero-success case,
conditional candidate law and fixed worst-case budget. Add finite repetition
to error eta. For full Lemma 3.1 coverage, prove the successful-state statement,
not only equality of measured candidate probabilities.

Construct fresh-workspace comparisons, prove the product success law and exact
weight-conditioned sampling, then prove history-dependent coupling and the
sum of all query budgets. Do not replace the process by a fixed tournament:
nonwinner comparisons need have no gap around 1/2.

**Pass:** Proposition 3.2 is proved as an implementation theorem with its
uniform constant, error bound, list length and worst-case query cap. No
amplification, exact-sampler, measurement-deferral or hidden oracle hypotheses
remain. The no-winner case still has the stated resource cap.

## M6. Forrelation upper algorithm, exact circuit and the family upper bound

Prove equality of the integer and normalized Walsh definitions. Implement the
quantum projection experiment and fixed-count error reduction. Construct the
butterfly integer circuit, track signed integer widths and translate its
arithmetic to fan-in-two gates with size O_k(m log²m). Verify local transcript
tests coherently and account for pointer reads, uncomputation and retained
garbage. Combine comparison, tournament and final verification.

**Pass:** Lemma 2.1(ii–iii), Lemma 2.2 and Proposition 3.3 are proved for a
specific exact circuit family and the same public Fkm. Correctness is on the
promise where required; query caps hold off promise. Error and cost constants
are uniform in m once k is fixed.

## M7. Conditional headline theorem and complete appendix coverage

Combine M3 and M6 with the explicit Bansal-Sinha premise. Prove floor/ceiling
and logarithm estimates, eventually-in-t family bounds, exclusion of every
alpha<4, and alphaTot=4 using M4. Give the conditional declaration a distinct
name and immutable statement identity.

In parallel finish the appendix rows not implied by the imported shortcut,
including the general nonnegative spectral adversary statement and the exact
intermediate assertions the ledger advertises. A compact alternative proof
and a line-by-line proof correspondence should have separate metadata.

**Pass:** the headline conditional theorem depends only on the named exact
Forrelation lower-bound premise; the family, models and all other arguments
are fully built. All 118 ledger IDs have honest row-to-declaration evidence,
with unresolved hypotheses and alternative-proof mappings explicit. A count
of planned rows is never reported as a count of verified claims.

## M8. Discharge the Forrelation lower bound

Either develop the Bansal-Sinha proof using the needed Fourier-growth and
Gaussian machinery, or import a newly discovered proof with an exact statement
and cost-model transport. The published paper's existence does not satisfy
this Lean milestone. First prove the literal theorem, then derive the weaker
eventual L<R(P) interface consumed by M7.

**Pass:** a separately compared unconditional theorem instantiates the M7
premise using a proof with only the permitted standard axioms. A hypothesis
inventory confirms that no replacement assumption has inherited the old
obligation. Recheck every public claim of coverage and independence.

## M9. Clean replay and Palomar preparation

Build a proof-only root, replay it through the required kernels, run each
Comparator bundle, run positive/negative controls, validate metadata and
source limits, and retain logs tied to the final commit and full dependency
closure. Challenges and negative fixtures must not contaminate the default
proof target's axiom audit. Separate semantic rejection from compile,
sandbox, export and independent-kernel failures.

The checked Palomar policy allows Challenges only from approved source
closures; complexitylib is not one. Each Challenge is limited to 102,400 UTF-8
bytes and 1,000 physical lines; the whole repository's Lean sources have
module-system and per-file rules. The full limits and exact path semantics
are in `comparator_design.md`. Measure the actual generated files before
choosing the final bundle count.

**Pass:** preparation dossier and local rehearsal receipts are complete. An
official preparation that requires a public GitHub commit remains a separate
future operation for the user's team. This task ends at preparation design;
it does not publish, submit or register anything.

## Estimates and uncertainty

The per-row line estimates are ranges of new incremental Lean work after
dependencies. They exclude copied external source, duplicated generated
Challenges, generated documentation and an independent full Bansal-Sinha proof.
Their total is an order-of-magnitude planning aid, not a schedule or a measured
implementation. Port failures, model transport and exact-circuit construction
can change it substantially. Re-estimate after M1, M3 and M5, when the main
semantic and transport risks have been resolved.
