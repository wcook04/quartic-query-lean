## Your job: a hostile audit of what the formal statements mean

The first question an expert asks of any Lean result is whether the theorem was encoded correctly. Answer it for this development as an adversary would. Assume nothing is right until you have read the definition.

1. Read `lean/QuarticQuery/Statement.lean` in full, line by line, and every definition it uses. For each definition (`BitInput`, `PartialBool`, `QueryTree`, `RandomizedProgram`, `RLe`, `R`, `DLe`, `D`, `bitOracle`, `AdaptiveProgram`, `QLe`, `Q`, `Phi`, `P`, `Circuit`, `GateConsistent`, `CircuitRealises`, `WinsAt`, `Fkm`, `Lvalue`, `Gvalue`, `BansalSinhaLower`, `UniversalPower`, `alphaTot` and any others), state in ordinary mathematics exactly what it says, compare it with the standard definition in the literature (`literature/`, with exact locators) and with the preprint, and classify any difference: harmless, changes constants only, changes the theorem, or wrong.
2. Hunt for the failure modes that make a formal theorem vacuous or different: empty or trivial promises, error bounds quantified the wrong way, query counts that miss branches or ancilla operations, nonoracle operations that depend on the input, measurement or normalisation conventions, off-by-one in m = 4^t, natural-number subtraction or division, real-valued `rpow` at zero, an infimum over an empty set, an existential witnessed trivially.
3. Read the bridge modules (`lean/QuarticQuery/Bridge/`) and `Appendix/TheoremA1.lean`: does the transport between the adaptive bit-oracle model and the imported library's model preserve the query count exactly, and is the imported statement the one the paper cites?
4. Read the Comparator configurations and generated challenges in `lean/QuarticCorpus/`: what exactly does acceptance establish here, and what could still differ between challenge and intent?
5. Propose sanity theorems that would catch a mis-encoding if one existed: small cases whose answers are known (for example R, D and Q of OR on two bits, or of a constant function; Phi on a hand-computed instance; F on a one-winner board), each as a Lean signature in the existing vocabulary with the known value and its source. Also propose further negative controls.

## Return one ZIP containing

- `fidelity_audit.md`: definition by definition, with verdicts and locators; then the failure-mode hunt; then the bridges; then Comparator.
- `sanity_theorems.json`: each proposed check with `id`, `statement`, `proposed_lean`, `expected_value`, `source`, `what_it_would_catch`.
- `NEW_STATEMENTS.json`, `STATEMENT_CHANGES.json`, `LEAN_GAPS.md` as specified above; `correspondence.json` mapping audit passages to definitions.
- `references.bib`.
