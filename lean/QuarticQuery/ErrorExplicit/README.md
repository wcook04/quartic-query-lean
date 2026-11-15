# The quartic separation with the error as a parameter

The public statements in this repository fix the error of both the randomized and the quantum
algorithms at `1/3`. The Lean files in this folder restate them with the error written out, so that
the dependence on the error and the logarithmic factor can be read from the Lean statements.
`m = 4^t`, `ln` is the natural logarithm, and `F_{k,m}` is the function of the separation.

AI agents directed by Will Cook wrote these files. Lean 4 accepts all of them with no `sorry`,
and the 13 headline theorems listed in `Axioms.lean` use only `propext`, `Classical.choice` and
`Quot.sound`. No mathematician has reviewed them.

They were compiled against revision `db3feec` of this repository. The root module
`QuarticQuery.lean` does not import this folder. To compile it, run
`lake build QuarticQuery.ErrorExplicit.Axioms` from `lean/`. The evidence records of this
repository are bound to the exact contents of `lean/` and have not been regenerated for these
files, which is why they are on a branch.

## Definitions (`Defs.lean`)

`RError f e` and `QError f d` are the repository's `R f` and `Q f` with the success threshold
`2/3` replaced by `1 - e` and `1 - d`. The program classes and the way queries are counted are
unchanged. `RError_one_third` and `QError_one_third` prove that at `1/3` they equal `R` and `Q`.

## What is proved

| Statement | File | Theorem |
| --- | --- | --- |
| For every error `e ≥ 0`, `R_e(F_{k,m}) ≥ (1 − 2e) · m^(2 − 1/k) / (72900 · k² · ln(4km))`, for `k ≥ 2`, `t ≥ 41`, `15k + 2 ≤ 2t` | `Family.lean` | `RError_Fkm_lower` |
| The quantum algorithm of the separation, at its unchanged budget `A_k · √m · (log₂ m)^6`, already has error at most `1/250`, so `Q_d(F_{k,m})` is at most that budget for every `d ≥ 1/250` | `QuantumMargin.lean` | `Fkm_forrCircuit_QLeError_250`, `QError_Fkm_le` |
| Both bounds for one function | `Family.lean` | `family_bounds_error_explicit` |
| No exponent below 4 works in `R_e(f) ≤ C · Q_d(f)^α` for total `f`, for any `0 ≤ e < 1/2` and `d ≥ 1/250` | `Exponent.lean` | `not_universalPowerError_of_lt_four` |
| Exponent 4 works for `e ≥ 0` and `0 ≤ d ≤ 1/3`, with constant 20736 | `Exponent.lean` | `RError_le_D_le_QError_pow_four` |
| So for `0 ≤ e < 1/2` and `1/250 ≤ d ≤ 1/3` the exponents that work are exactly `α ≥ 4` | `Exponent.lean` | `alphaTotError_eq_four` |
| No constant `C` gives `R(f) ≤ C · (1 + Q_d(f))^4` for all total `f` and all `d < 1/2` | `OrCounterexample.lean` | `no_error_uniform_constant` |

The last row uses OR on `N` bits at quantum error `d_N = (N − 1)/(2N − 1)`. There
`Q_{d_N}(OR_N) ≤ 2` and `R(OR_N) ≥ N/3`, so the constant in the quartic relation cannot be
chosen uniformly as the quantum error tends to `1/2`.

The general lower bound behind the first row is `planted_lower_general` in `PlantedGeneral.lean`:
for a partial `f`, a circuit realising it, `m = 2^ℓ`, address length `r` and an integer
`1 ≤ L < R(f)`, the addressed function needs at least
`(1 − 2e) / (2/m² + 1/(mL) + (2/3)^r)` randomized queries at error `e`.

## What is not proved

* Amplification is not formalised. For quantum error below `1/250` there is no bound on
  `Q_d(F_{k,m})` here, and the exponent statement is not proved there.
* For `1/3 < d < 1/2` only the lower side of the exponent statement is proved. The upper side
  needs `D ≤ C · Q_d^4` at general error, and the library result used here fixes the error at `1/3`.
* The constant 72900 is what the present argument gives and is loose. The same argument should
  give a constant near 9113 for large `t`. That is not proved.
* The diagonal choice of `k` in terms of the input length is not restated with explicit error.
