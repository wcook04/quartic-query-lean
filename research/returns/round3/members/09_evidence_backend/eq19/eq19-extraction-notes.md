# Equation (19) and native extraction: focused return

## Finding

The frozen sources contain a checked equality and a checked upper bound, but no
single supplied theorem in this audit states their conjunction. The name
`QuarticQuery.Paper.eq_19` denotes only the upper bound. The maintained `eq-19`
tie correctly keeps `QuarticQuery.avg_foundZero_I_le` **partial**: its coefficient
two is stronger than the paper's coefficient four, but an inequality does not
assert the equality in the compound row. The older baseline's Appendix B entry
calls that tie `stronger`; that historical evidence paragraph needs updating.

This return proposes the small actual-definition wrapper
`QuarticQuery.Paper.eq19_whole`, an independently authored experiment specification,
explicit bridges from that specification to the project definitions, and two
Comparator configurations. The wrapper and all new Lean files remain
**unelaborated here**. A real `lean-exposition extract --build` invocation was
attempted on an accepted, source-current existing declaration and failed at
process launch because `lean-exposition` is not installed. No graph, selected
goal view, or native extraction receipt was produced.

## Exact mathematical statement

Set \(m=2^\ell\). Let \(\kappa\) be a finite set of address-string coordinates,
and let \(\mu:\{0,1\}^{\kappa}\to\mathbb R\) satisfy
\(\mu(x)\geq0\) and \(\sum_x\mu(x)=1\). Independently sample every address string
\(A_{i,h}\) according to \(\mu\), every zero position \(J_i\) uniformly from
\([m]\), and one further column \(I\) uniformly from \([m]\). The dummy input has
zero exactly at \(X_i[J_i]\), the sampled address data, and fixed all-false cell
bits. A deterministic tree \(T\) has maximum depth at most the integer \(G\),
charging each bit query, including repetitions. Let \(Z\) count columns whose
unique zero appears in the complete dummy query path. Then

\[
\Pr[T(Y^{(0)})\text{ queries }X_I[J_I]]
=\frac{\mathbb E Z}{m},
\qquad
\Pr[T(Y^{(0)})\text{ queries }X_I[J_I]]\leq\frac{4G}{m^2}.
\]

The paper uses \(m=4^t\); specialize \(\ell=2t\). No hardness or promise-support
hypothesis is needed for this isolated discovery statement. Such hypotheses
enter the later planted-input and address-guessing argument. The normalization
and depth conditions are ordinary premises of this statement, not extra open
assumptions.

For each fixed pair \((A,J)\), exactly \(Z(A,J)\) of the \(m\) possible columns
\(I\) satisfy the event. Conditional averaging over the independent uniform
\(I\), followed by averaging over \((A,J)\), gives the equality. In expanded
finite sums this is simply
\[
\sum_{A,J}p_Ap_J\frac1m\sum_i\mathbf1_{\{X_i[J_i]\text{ queried}\}}
=\frac1m\sum_{A,J}p_Ap_JZ(A,J).
\]
This identity is algebraic even for non-normalized signed address weights; the
probability interpretation and inequality require the displayed distribution
premises. The supplied implementation proves the stronger inequality
\(2G/m^2\) by the finite-world search induction, then weakens the coefficient to
four. This remains an alternative proof route to the paper's early/late split.

**Authority:** OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum
Query Complexity*, 5 October 2026, §4.2, printed pp. 12–13, equation (19), frozen PDF
SHA-256 `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`.
The parsed passage is `paper/extracted.md`, lines 601–637. The baseline is
`reasoning-record.md`, §6.4 and Appendix B `eq-19`. None of these editorial
passages is itself a Lean execution receipt.

## Actual Lean interfaces

`Paper/ClassicalPlanted.lean`, lines 180–258, supplies:

| Declaration | What its complete conclusion contributes |
| --- | --- |
| `Paper.discoveredZeros` | Cardinality of the set of discovered columns. |
| `Paper.expectedZeros` | The integer-valued count averaged over address data and zero positions. |
| `Paper.erasedZero_eq_expectedZeros_div` | The equality with `expectedZeros μ T / m`. |
| `Paper.expectedZeros_le_four` | `expectedZeros μ T ≤ 4G/m`. |
| `Paper.eq_19` | Only the final erased-zero probability inequality. |
| `avg_foundZero_I_le` in `ZeroSearch.lean` | The coefficient-two inequality, with address data fixed and `J,I` averaged. |

The new theorem in `overlay/lean/QuarticQuery/Paper/Eq19Whole.lean` has the full
conjunction in its type and proof
`⟨erasedZero_eq_expectedZeros_div μ T, eq_19 hμ hμ1 T hT⟩`. This is a source-level
proposal, not an assertion that a compiler has checked it. Both underlying
declarations occur in the supplied successful source-bound root-build receipt.

The companion `Spec.lean` states the experiment independently using explicit
products and sums. Its zero test is an `if j = J i` specification; its zero count
is a cardinality, and it places the factor `1/m` for the independent column
inside the inner sum. It does not call the implementation's `dummy`, `foundZero`,
`coupledAvg`, `discoveredZeros`, or `expectedZeros`. `Bridge.lean` proves agreement
with each relevant project quantity before transporting the theorem. Thus a
change to the implementation's normalization or blank-input behavior must pass
an explicit bridge instead of being copied silently into the expected answer.

The challenge was not generated from `Solution.lean` or `Statement.lean`. It
imports the newly authored specification. The specification still shares the
project's `QueryTree`, `BitLoc`, `path`, and `depth` interfaces; it is not a
separately formalized foundation. `PathControls.lean` addresses the concrete
remaining repetition risk: asking the same bit twice must produce path
`[q,q]`, depth two, and one discovered column. This is an additional proposed
semantic test, not a witnessed pass.

The two comparisons serve distinct purposes:

- `whole-comparator.json` directly compares **the exact declaration**
  `QuarticQuery.Paper.eq19_whole` against `WholeChallenge.lean`. Its vocabulary is
  shared with the project. It supplies agreement evidence for that declaration
  only after a successful actual run.
- `comparator.json` compares `QuarticQuery.Independent.Eq19.checked_eq19` against
  the independently authored expected experiment. The solution uses the bridges.
  Neither declaration may borrow the other's comparison status.

Both keep `definition_names` empty, so the supplied Comparator traverses and
checks the bodies of non-target constants that determine the theorem types.
The allowed axioms are precisely `propext`, `Quot.sound`, and `Classical.choice`.
Only the specification-only challenge modules intentionally contain `sorry`.

`NegativeInequalityOnly.lean` proves a valid inequality but omits the equality.
The expected diagnostic for its separate negative configuration is a theorem
statement mismatch naming `QuarticQuery.Independent.Eq19.checked_eq19`. A missing
tool, bad import, build error, axiom rejection, or unrelated nonzero exit does
not satisfy that negative case. No rejection was executed here.

## Existing source-bound evidence was checked, not recreated

`accepted-target-source-check.json` independently checks the supplied successful
root receipt
`repository/corpus/receipts/lean-build-root-2026-11-02T182539383153+0000.json`.
All 124 recorded hashes match, and the complete current inventory produced by
the existing `build_corpus.source_hashes` equals the receipt inventory. The
receipt explicitly declares `QuarticQuery.Paper.erasedZero_eq_expectedZeros_div`.
All 16 source/configuration inputs in the module's separate current-native
acceptance record also match.

The source header saying “UNELABORATED” describes the submitted draft's original
environment. It does not override later source-bound successful build evidence.
Conversely, those later successes do not certify any new file in this return.
The supplied type/axiom log prints the complete equality type and the allowed
standard axioms at lines 1520–1524; `expectedZeros_le_four` appears at lines
1510–1514. Its exact source/log bindings remain part of the original packet.

The source-current `Reach` export declares the equality and `eq_19`, but neither
is in the two headline roots' reached set. No direct dependency list for either
is present in that root projection. `avg_foundZero_I_le` is reached and has a
dependency list. This distinction is useful: a companion theorem can be built
without being part of the headline proof. It is also why that root projection
cannot substitute for the requested extraction of the equality itself.

## Native extraction: attempted and blocked

The chosen accepted target is:

- Module: `QuarticQuery.Paper.ClassicalPlanted`.
- Declaration: `QuarticQuery.Paper.erasedZero_eq_expectedZeros_div`.
- Module source SHA-256:
  `b86c310788efd04527ce9977e6f1cb660cd6b2b6825dcb151ab33f1b94497c2f`.
- Toolchain: `leanprover/lean4:v4.36.0-rc2`.

`native-extraction-attempt.json` retains the actual command, working directory,
exit 127, empty stdout, and `lean-exposition: not found` stderr. No native driver
ran. This record is explicitly a process-launch attempt, **not** the consumer's
native extraction receipt.

The missing prerequisites are the installed Lean/Lake toolchain, the pinned
dependency/build artifacts, and the complete installed `lean-exposition` package.
The packet includes ten contract/source files for that package, not an
installable distribution. In particular its advertised CLI imports `bundle.py`,
`intake.py`, and `prove2me.py`, which are absent, and native extraction loads
`resources/lean/Extract.lean`, which is absent. Package metadata and entry point
installation are absent. The active Python environment also lacks `jsonschema`.
`BACKEND_INPUT_STATUS.json` correctly reports the selected source group supplied;
that is a source-custody status, not an installed-tool availability assertion.

There is no supplied `lean-exposition` Git revision in the selected tool manifest.
The manifest hashes identify the reviewed source edition; the CLI's hard-coded
`0.1.0` is not a substitute for a revision. Comparator sources come from the
recorded `v4.36.0-rc2` toolchain path and are individually hashed in the packet.
No unpinned replacement tool was downloaded or used.

## Re-entry and acceptance

Use the exact commands and expected outcomes in `reentry-plan.json`. First obtain
the full tool package matching the supplied source hashes and the project's
pinned toolchain/dependencies. Re-run the accepted-target extraction on the
unmodified frozen project, retaining stdout, the driver/template/request hashes,
the build receipt, report and graph. Then run the real CLI `validate`, `select`,
and `inspect` views. The prerequisite view must come from that actual graph.

For new candidates, overlay the proposed files onto a disposable checkout. They
use the already declared `QuarticQuery` and `QuarticCorpus` libraries, so no Lake
configuration patch is needed. The independent comparison modules are nested
below `QuarticCorpus/Independent/Eq19`, outside the current one-level generated
bundle glob. Invoke their configurations directly; do not run the generator
over them or claim that the existing bundle runner discovered them.

Build the proof-bearing modules and inspect `Audit.lean` before the comparisons.
Capture source/configuration hashes with the existing corpus producer immediately
before and after each real command. Adding these modules changes the existing
conservative whole-source inventory; historical receipts do not become current
for the enlarged snapshot. Each new result needs its own successful bound
receipt, and each declaration needs its own reviewed relation. Keep the equality
and inequality ties partial until the compound theorem's actual build and
comparison exist. Do not mark any new tie checked by editing a JSON status.

The extraction contract requires version-2 native reports, type/value/structural
edges, source identities, explicit external boundaries, preserved unavailable
bodies and unexpanded declarations, and the separate successful build record.
`select` changes selected goals while keeping the graph. An empty in-scope axiom
list or successful graph-schema validation does not establish informal equation
fidelity. If external dependencies remain, the overall graph may correctly be
`partial` even when its in-scope traversal is complete.

**Still open:** native elaboration and all new comparisons; actual consumer
extraction/selection/inspection and its schema checks; a maintained semantic
review of the new compound tie. There is no completed frontend or new theorem
registry in this return.
