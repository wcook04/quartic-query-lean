# Corrections applied on import

Each return passed its packet checker. A stricter audit (exact namespaces, wording rules) found these, corrected here:

- 02_sk_expository: `OAI.ZeroTemperatureSK.finite_feedback_coercivity` is declared as `OAI.ZeroTemperatureSK.Heat.finite_feedback_coercivity`; renamed in 2 Lean rows, its title and its note.
- 04_erdos257_short: `Erdos249257.periodLcm` is declared as `Erdos249257.TotientTailPeriodKiller.periodLcm`; renamed in 1 Lean rows, its title and its note.
- 07_erdos257_long_III_V: note for `Erdos249257.upperOrMiddle_within_of_two_pow_deficit`: “rather than silently replacing them by a run of only $k$ transitions” → “and cannot replace them by a run of only $k$ transitions”.
- 08_quartic_expert: note for `QuarticQuery.Paper.quantumVerify_list`: “A list is verified by testing its candidates until one accepts.” → “A list is checked by testing its candidates until one accepts.”.
- 10_quartic_reconstruction: note for `QuarticQuery.D_totalise_eq_complexity`: “without silently changing the deterministic query convention” → “with the same deterministic query convention”.
- 10_quartic_reconstruction: note for `QuarticQuery.SemanticReview.trueOnly`: “must not be silently filled with false” → “must not be filled with false”.

`fidelity: different` is kept; the lean-exposition validator must accept it (it allowed same/stronger/weaker).
