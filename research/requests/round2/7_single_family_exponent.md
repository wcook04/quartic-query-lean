## Your job: can one family reach exponent 4 - o(1)?

The preprint proves, for each fixed k, a family with randomized complexity about m^(2-1/k) and quantum complexity about sqrt(m) up to logarithms, so R is about Q^(4-2/k). Its exponent argument chooses k first and lets m grow, and it remarks that letting k grow with m would need bounds uniform in k. We now have one such bound: a randomized lower bound for k-Forrelation uniform in k with only a k^2 loss (`previous_round/4_forrelation_route_note/`, `lean/QuarticQuery/ForrelationLower/Uniform.lean`). Determine whether a single family of total functions F_m, with k = k(m) growing, satisfies R(F_m) >= Q(F_m)^(4 - o(1)), and with what o(1).

1. Track every dependence on k in the construction and both bounds, exactly. Quantum side: the Forrelation quantum algorithm's success gap (delta = 2^(-5k), so repetitions about 2^(10k) log(1/eta)), the circuit size, the address length r, decoding error, the tournament and verification costs, and the constant `budgetConst k` in `lean/QuarticQuery/Upper/Bound.lean`. Classical side: the uniform Forrelation bound, L as a function of k, the direct product, the planted argument's thresholds and G. Read the Lean source for each constant and give file and line.
2. Choose k(m) to optimise the exponent. Compute R and Q as explicit functions of m, and the resulting log R / log Q. State the best single-family exponent you can prove, for example 4 - O(log log m / log m) or 4 - O(1/sqrt(log m)), with the exact choice of k(m) and every threshold.
3. If something blocks the argument (for instance a hidden k-dependence that is exponential where you need polynomial, or a threshold such as m >= 2^(15k+2) that forces k <= O(log m)), identify it exactly and say what would remove it.
4. Write the result as a short paper section: theorem, proof, and how it relates to the preprint's quantifier remark. Put every new claim in `NEW_STATEMENTS.json` with a Lean signature in the existing vocabulary, so we can check it.

## Return one ZIP containing

- `single_family.md` with `<!-- passage:NAME -->` anchors; `references.bib`.
- `k_dependence.json`: every constant of the construction with its exact k-dependence, source file and line.
- `checks.py` (standard library) and `checks_output.txt` evaluating the exponent for explicit m.
- `correspondence.json`, `NEW_STATEMENTS.json`, `STATEMENT_CHANGES.json`, `LEAN_GAPS.md` as specified above.
