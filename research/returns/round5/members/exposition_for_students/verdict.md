# Verdict: revise before assigning as a standalone exposition

The draft now has a clear frame and unusually useful counterexamples. A strong graduate student can learn the construction and see where the exponent comes from. They will still need help reconstructing the quantum sampler and the adaptive classical reduction. Recommend a focused explanatory revision, with the present scope retained.

I found one locally overbroad probability assertion, not a counterexample to the separation theorem: the per-stage failure bound needs the condition that the winner has not yet been selected (ES-008). The tested finite calculations agree with the text. The 180-gate circuit itself was not supplied for independent execution.

## Five changes that matter most

1. **Make the tournament executable in the reader’s mind.** Identify weights as analysis-only, explain the reversible preparation, and specify the absorbing zero-weight state and return-on-failure action. Keep the query cap universal while qualifying the success guarantee (ES-001, ES-002, ES-003, ES-009).
2. **Teach the classical reduction at its decisive step.** Replace the claim that visiting a cell requires knowing its address with the actual bound on guessing it. Use the existing simulator trace and show what is conditioned on in the product invariant. Complete the dependent-selection counterexample’s no-discovery branch (ES-004, ES-010, ES-011, ES-012).
3. **Repair the evidence destinations.** The arbitrary-randomness link selects a finite endpoint; the amplifier range misses its conclusion. Explain statement placeholders, link the solution, and send readers directly to existing proof anchors. Include the missing Figure 2 and Figure 4 source assets (ES-005, ES-007, ES-026, ES-027, ES-030).
4. **Make the main reading path reliable.** Essential lemma statements must survive skipping optional proofs. Explain the small Forrelation experiment’s overlap, scope Figure 1 to a winner, enlarge essential figure labels, and move peripheral arithmetic or unused refinements out of the main route (ES-015, ES-017, ES-019, ES-020, ES-024).
5. **Tighten credit and quantitative accounting.** Outward pointers have a documented antecedent; distinguish the new combination. Attribute the explicit constants to the record, explain the comparison-search model at first use, and collect tournament plus verification costs before deriving the logarithmic exponent (ES-006, ES-021, ES-022, ES-023).

**Keep:** the one-line exponent arithmetic and history; the three sign inputs and changed domain-bit board; the false-positive dominance example; the joint-versus-conditional AND example; Figure 2’s reverse pointer; the fixed-parameter quantifier warning; and the distinction between checking a formal statement and validating its meaning.

**Scope:** full exposition text and all 13 PDF pages; expert text, targeted primary-source and record checks, and exact local formal-link inspection. No fresh Lean build or Comparator run. Reading depth and reproducible checks are recorded separately.
