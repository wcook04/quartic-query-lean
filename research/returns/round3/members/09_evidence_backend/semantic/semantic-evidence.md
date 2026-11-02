# Independent finite semantic expectations

<!-- passage:SEMANTIC-SCOPE -->
The supplied definitions have the intended answers in all four requested examples
by ordinary mathematical reasoning. This return supplies new Lean tests against
those actual definitions and separate mutation controls. **The new Lean files
are proposed source, not checked theorems:** this environment has no `lean`,
`lake`, `elan`, or `lean-exposition` executable on `PATH`. Actual version-command
attempts and the stopped runner preflight are retained in `receipts/`.

The mathematical authority is the supplied OpenAI preprint, dated 5 October
2026: its abstract and §1 fix worst-case bit queries and error at most one third;
§1.3 explains the promise convention; equations (3)–(4) define Forrelation; and
equation (10) specifies complementary comparison probabilities. `Statement.lean`
is the implementation under test, not the independent authority for the expected
answers. The test code imports `QuarticQuery.Model.Classical`, and thereby the
actual `QuarticQuery.Statement`. It does not import a generated Challenge or use
the Solution-to-Challenge generator. The examples themselves were explicitly
chosen in this packet's assignment; this is independent specification of expected
answers, not a claim of independent human authorship.
<!-- /passage:SEMANTIC-SCOPE -->

## Four exact examples

<!-- passage:SEMANTIC-IDENTITY -->
Let $f(x)=x$ on one input bit. A zero-query decision tree is a constant leaf,
so a mixture of such trees has a single input-independent probability $p$ of
answering true. Correctness on input 1 requires $p\geq2/3$; correctness on input
0 requires $1-p\geq2/3$. Adding these inequalities gives $1\geq4/3$, a
contradiction. Every support tree has depth zero because the program's depth is
their maximum. Thus the actual goal is

```lean
¬ QuarticQuery.RLe QuarticQuery.SemanticReview.oneBitIdentity 0
```

The proposed proof establishes input-independence by inspecting the actual tree
constructors, then uses the actual weight normalization to show that true and
false success masses sum to one. It does not assume a finite truth table for a
different randomized model. A deliberate mutant reversing the order of
algorithm and input quantifiers succeeds by choosing the correct constant leaf
after seeing the input; `wrong_quantifier_order_changes_answer` exposes exactly
that difference. This is a model error, not a failure of the elementary
probability argument.
<!-- /passage:SEMANTIC-IDENTITY -->

<!-- passage:SEMANTIC-OR -->
For two-bit OR, choose each of the following trees with probability $1/3$:
return true; read the first bit and return it; read the second bit and return it.
Their output triples and success probabilities are:

| Input | Correct OR value | Tree outputs | Success |
| --- | --- | --- | --- |
| 00 | 0 | 1, 0, 0 | $2/3$ |
| 01 | 1 | 1, 0, 1 | $2/3$ |
| 10 | 1 | 1, 1, 0 | $2/3$ |
| 11 | 1 | 1, 1, 1 | $1$ |

The weights are strictly positive and sum to one; every tree has depth at most
one. Consequently the specified mixture witnesses `RLe orTwo 1`. Both output
labels occur, so the preceding zero-query argument also proves $R(\mathrm{OR}_2)=1$.
The inclusive threshold matters: the same mixture fails the strict condition
that its success exceed $2/3$ on every input. The proposed negative control
substitutes input 00 and uses the exact success equality, so it does not mistake
a numerical approximation for a boundary test.
<!-- /passage:SEMANTIC-OR -->

<!-- passage:SEMANTIC-PROMISE -->
Define a partial one-bit function only at input 1, where its value is true. A
constant-true leaf is correct on its entire promise and makes zero queries.
The input 0 has value `none` and imposes no correctness condition. This yields
`RLe trueOnly 0`, hence $R(\texttt{trueOnly})=0$. The explicit
`ConstantOnPromise` alternative in `QLe` gives the same result for $Q$.
These are actual witnesses to admissible budget zero; no empty-infimum argument
is involved. The mutant assigning false to the formerly undefined input becomes
the total identity and fails the zero-query test.
<!-- /passage:SEMANTIC-PROMISE -->

<!-- passage:SEMANTIC-FORRELATION -->
For $k=2,t=1,m=4$, set both sign vectors to $z=(-1,1,1,1)$. Let $W=2H$
be the unnormalized Walsh matrix. Direct multiplication gives

\[
Wz=(2,-2,-2,-2)=-2z,\qquad z^\top Wz=-8.
\]

The denominator in equation (3) is $m\sqrt m=8$, so $\Phi=-1$. The high
branch in equation (4) requires $\Phi\geq\delta=2^{-10}>0$, and the low branch
requires 
\[
|\Phi|\leq\delta/2=2^{-11}.
\]

Both inequalities fail. The expected result is `none`, not false and not true.
The proposed Lean test evaluates the actual integer numerator and denominator
with `decide +kernel` and then derives the real quotient; it separately evaluates
the actual promise classifier. The deliberately wrong classifier replacing the
high test by $|\Phi|\geq\delta$ returns true on this same input.

The supplied project already contains this concrete negative Forrelation
example in `Forrelation/Sanity.lean`, at `Phi_negativeWitness` and
`P_negativeWitness`. This return makes no novelty claim for it. The new test
imports neither theorem and fixes the expected signed answer explicitly;
its proof still needs its own native run.
<!-- /passage:SEMANTIC-FORRELATION -->

## What the two Comparator controls mean

<!-- passage:SEMANTIC-CONTROLS -->
`Controls/threshold_mutation.json` names a handwritten challenge whose premise
is $p\geq2/3$ and a solution whose same-named premise is $p>2/3$. The displayed
conclusion is unchanged and both implications are provable, but the premise's
definition has changed. The supplied Comparator implementation recursively
checks constants occurring in theorem types when `definition_names` is empty
(`Lake/Check/Compare.lean`, `compareAt` and `Compare.loop`). The predicted rejection
is therefore the definition mismatch at `Round3.ThresholdSpec.Eligible`.
This is a source-based expected result, **not an executed rejection**. The runner
requires the precise diagnostic as well as exit code 1; a missing tool or failed
build cannot satisfy this control.

`Controls/shared_blind_spot.json` deliberately gives both challenge and solution
the same impossible comparison predicate. It adds a `False` field, from which
the solution proves the conditional claim $1=0$. Comparator is expected to
accept matching definitions and a valid proof of this implication. That would
be a demonstration of the boundary of statement comparison, not semantic
acceptance of the intended comparison model. This expectation is unexecuted.

The independent semantic requirement is that a valid two-candidate comparison
exists. The concrete matrix with zero diagonal and both off-diagonal entries
$1/2$ satisfies equation (10) and the actual project's `IsComparison`.
`comparison_has_witness` constructs it. `SharedAudit.lean` separately proves
that the shared bad predicate has no witness, and rejects that same matrix.
Thus the model expectation distinguishes the two specifications even if a
comparison of the shared bad pair were to pass. There is no assertion here
that a contradiction has been proved without premises.
<!-- /passage:SEMANTIC-CONTROLS -->

## Execution and re-entry

The existing `tools/return_checks/semantic_controls.py` was executed and returned
exit code 0. Its finite Python expected answers and all seven named toy mutations
matched their expectations. This remains finite-model evidence; the script does
not execute or compare the Lean definitions. The original output and its hash
are in `receipts/existing-toy-controls.json` and its run receipt.

The new runner's real preflight returned exit code 2, with all native cases marked
`not_run`: `lake` could not be started, and no overlay was installed into the
immutable packet copy. No native build, axiom audit, or Comparator run has taken
place. `source-hashes.json` records inspected input bytes;
`receipts/preflight-final/run.json` records source hashes before and after the
attempted preflight, using the existing repository owner's
`tools/build_corpus.py::source_hashes(project.parent)`. This includes
`lean/scripts/Reach.lean` and all other local Lean owners, with exactly the
existing backend's conservative scope. A missing or failed source-hash owner
blocks the runner explicitly; it cannot fall back to a partial glob list. The
receipt records the exact runner and owner hashes and reports no source change.
The earlier `receipts/preflight/run.json` is retained as historical preflight
output from the superseded runner scope; it is not current build evidence.

To resume in a full, pinned checkout:

1. Use the packet's `leanprover/lean4:v4.36.0-rc2` toolchain and exact locked
   dependencies. The required Mathlib revision is
   `69552756cd8a2d2d48763cf7279fd814d6a1224d`.
2. Work in a disposable checkout at the frozen source bytes. Copy the returned
   `lean/QuarticCorpus/Independent/` directory into its existing
   `lean/QuarticCorpus/` library. No new library stanza or theorem registry is
   needed. The original source files and lockfile must remain byte-for-byte
   unchanged; the runner checks the relevant frozen inputs and delegates its
   before/after binding to the existing repository source-hash owner.
3. Run:

   ```sh
   python run_semantics.py --project /absolute/path/to/checkout/lean --output /absolute/path/to/new-receipts
   ```

   The runner builds the new semantic modules, runs `Inspect.lean` to print
   theorem types and axiom dependencies, and executes the two Comparator
   configurations. Its default Comparator invocation retains sandboxing. The
   explicit `--unsandboxed-local` option matches the packet's known-code local
   rehearsal style when that is the chosen environment; the receipt identifies
   this distinction.
4. Inspect the actual printed types and axiom reports. Confirm only the permitted
   foundational axioms appear. Retain every log and the before/after source
   manifest. Fix any elaboration errors before claiming a pass; these proposals
   have not been compiled here.
5. Record accepted evidence through the existing repository producer after review
   of the new modules. Do not promote the custom run summary into the corpus merely
   because it exists. The shared-bad-spec acceptance, if obtained, must remain
   labelled a blind-spot control.

The intentionally admitted proofs occur only in two Comparator Challenge
specimens. The semantic modules, mutation detection proofs, and solution
specimens contain neither `sorry` proof terms nor added axioms. Static source
inspection establishes that fact; a native axiom audit remains outstanding.
