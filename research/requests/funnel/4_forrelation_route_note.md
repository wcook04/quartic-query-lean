## Your job: the Forrelation lower-bound route (mathematical research and proof audit)

The Lean proof of the Forrelation randomized lower bound in `lean/QuarticQuery/ForrelationLower/` follows a route described in `docs/forrelation_lower_bound_blueprint.md`: one block of the Gaussian process is scaled, one Stein identity per block removes each factor, only Fourier level k appears, an elementary truncation replaces Owen's T function, and a martingale growth bound under a biased measure (after Girish, Tal and Wu) replaces Tal's theorem. `docs/forrelation_lower_bound_review.md` reconstructs it and tests the key identity numerically; `docs/forrelation_route_prior_art.md` records what was found in the literature. The Lean theorem is the weaker fixed-k statement `BansalSinhaLower` in `lean/QuarticQuery/Statement.lean`.

1. Reconstruct the argument as a self-contained mathematical note with complete proofs, independent of the Lean source, then compare it with the Lean statements line by line.
2. Determine the quantitative strength of the route. The review conjectures, from a hand derivation, that the identity combined with the sharper growth bound would improve the k-dependence of Bansal and Sinha's Theorem 1.3 from `k^(-29)` to about `k^(-1)` or `k^(-2)`. Prove or refute this. State the best bound the route gives, with every constant and logarithm.
3. Search the literature thoroughly for each ingredient and for the combination, including forward citations of Bansal and Sinha and of Girish, Tal and Wu, and work from 2024 to 2026. Report what is known, partly known and not found, with exact locators.
4. Identify the k-uniform statement, if any, that should be formalised next, and give it as a Lean signature in `NEW_STATEMENTS.json`.

## Return one ZIP containing

- `note.md`: the self-contained note, with `<!-- passage:NAME -->` anchors; `references.bib`.
- `quantitative.md`: the strength analysis with full derivations, and a verdict on the conjectured improvement (proved, refuted, or open, and why).
- `prior_art.json`: per ingredient, `status` (`known`, `partly_known`, `not_found`), `closest_work`, `locator`, `difference`.
- `correspondence.json`, `NEW_STATEMENTS.json`, `STATEMENT_CHANGES.json`, `LEAN_GAPS.md` as specified above.
