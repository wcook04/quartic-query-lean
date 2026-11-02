#!/usr/bin/env python3
"""Exact finite probability example; not Lean or Comparator evidence.

For m=4, query row zero in every column. Compare an independent uniform
erased-column index with a marginally uniform index selected from discoveries.
The latter deliberately violates the preprint's independence hypothesis.
"""
from fractions import Fraction
from itertools import product
import json


def calculate():
    m = 4
    base_mass = Fraction(1, m ** m)
    mean_zeros = Fraction(0)
    independent_hit = Fraction(0)
    dependent_hit = Fraction(0)
    dependent_marginals = [Fraction(0) for _ in range(m)]
    for zero_positions in product(range(m), repeat=m):
        discovered = [i for i, j in enumerate(zero_positions) if j == 0]
        mean_zeros += base_mass * len(discovered)
        for i in range(m):
            independent_hit += base_mass * Fraction(1, m) * (i in discovered)
        choices = discovered or list(range(m))
        for i in choices:
            mass = base_mass / len(choices)
            dependent_marginals[i] += mass
            dependent_hit += mass * (i in discovered)
    assert mean_zeros == 1
    assert independent_hit == mean_zeros / m == Fraction(1, 4)
    assert dependent_marginals == [Fraction(1, 4)] * m
    assert dependent_hit == Fraction(175, 256) != mean_zeros / m
    return {
        "scope": "exact finite Python probability model; no project Lean execution",
        "m": m, "query_cap": m, "zero_configurations": m ** m,
        "expected_distinct_discoveries": str(mean_zeros),
        "independent_uniform_index_hit_probability": str(independent_hit),
        "expected_discoveries_div_m": str(mean_zeros / m),
        "dependent_index_marginals": list(map(str, dependent_marginals)),
        "dependent_index_hit_probability": str(dependent_hit),
        "conclusion": "A uniform marginal for I does not replace independence from the dummy run.",
        "actual_preprint_counterexample": False,
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2))
