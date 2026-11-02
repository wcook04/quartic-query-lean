#!/usr/bin/env python3
"""Exact finite arithmetic for the quantum examples in the model review.

This is a separately specified Python model, not an execution of Lean or
Comparator. It tests the small identities and algorithms displayed in the
review, not the equivalence of arbitrary quantum models or any main theorem.
Only Python's standard library is used. No floating-point arithmetic occurs.
"""

from fractions import Fraction
from itertools import product
import json


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def half(a):
    return tuple(tuple(Fraction(x, 2) for x in row) for row in a)


H_unscaled = ((1, 1), (1, -1))
IDENTITY = ((1, 0), (0, 1))
FLIP = ((0, 1), (1, 0))


def conjugation_checks():
    out = []
    for bit in (0, 1):
        bit_oracle = FLIP if bit else IDENTITY
        phase_oracle = ((1, 0), (0, (-1) ** bit))
        # Each product contains two Hadamards, so their two 1/sqrt(2)
        # factors multiply to the exact rational factor 1/2.
        phase_to_bit = half(mul(mul(H_unscaled, phase_oracle), H_unscaled))
        bit_to_phase = half(mul(mul(H_unscaled, bit_oracle), H_unscaled))
        assert phase_to_bit == bit_oracle
        assert bit_to_phase == phase_oracle
        plus = (1, 1)
        minus = (1, -1)
        action = lambda v: tuple(sum(bit_oracle[i][j] * v[j] for j in range(2))
                                 for i in range(2))
        assert action(plus) == plus
        assert action(minus) == tuple(((-1) ** bit) * v for v in minus)
        out.append({"input_bit": bit, "H_phase_H": phase_to_bit,
                    "H_bit_H": bit_to_phase,
                    "plus_is_idle": True, "minus_kickback": True})
    return out


def oracle(vector, bits):
    """Bit oracle on sparse basis coefficients, with common scale preserved."""
    return {(i, b ^ bits[i], z): c for (i, b, z), c in vector.items()}


def project(vector, predicate):
    return {basis: c for basis, c in vector.items() if predicate(basis)}


def norm_sq(vector, squared_denominator):
    return sum(Fraction(c * c, squared_denominator) for c in vector.values())


def or_selector_checks():
    # State coefficients have the common scale 1/sqrt(3).
    initial = {(0, 0, 0): 1, (0, 0, 1): 1, (1, 0, 2): 1}
    assert norm_sq(initial, 3) == 1
    rows = []
    for bits in product((0, 1), repeat=2):
        masses = [Fraction(0), Fraction(0)]
        record_zero = project(initial, lambda p: p[2] == 0)
        masses[1] += norm_sq(record_zero, 3)
        # Two binary record measurements implement the three-way selection.
        remaining = project(initial, lambda p: p[2] != 0)
        for record in (1, 2):
            branch = project(remaining, lambda p: p[2] == record)
            queried = oracle(branch, bits)
            for answer in (0, 1):
                masses[answer] += norm_sq(project(queried, lambda p: p[1] == answer), 3)
        expected_true = Fraction(1 + bits[0] + bits[1], 3)
        assert masses == [1 - expected_true, expected_true]
        assert sum(masses) == 1
        value = bits[0] | bits[1]
        assert masses[value] >= Fraction(2, 3)
        rows.append({"input": ''.join(map(str, bits)), "false_mass": masses[0],
                     "true_mass": masses[1], "success": masses[value],
                     "syntactic_query_cap": 1})
    assert [r["success"] for r in rows] == [Fraction(2, 3)] * 3 + [Fraction(1)]
    return rows


def parity_checks():
    # Initial |+>_index |->_answer has integer coefficients with scale 1/2.
    initial = {(0, 0, 0): 1, (0, 1, 0): -1,
               (1, 0, 0): 1, (1, 1, 0): -1}
    assert norm_sq(initial, 4) == 1
    out = []
    for bits in product((0, 1), repeat=2):
        queried = oracle(initial, bits)
        # One final index Hadamard changes the common scale to 1/(2sqrt(2)).
        final = {(i, b, 0): sum(H_unscaled[i][j] * queried[(j, b, 0)]
                                for j in (0, 1))
                 for i in (0, 1) for b in (0, 1)}
        mass = [norm_sq(project(final, lambda p: p[0] == i), 8) for i in (0, 1)]
        assert sum(mass) == 1
        assert mass[bits[0] ^ bits[1]] == 1
        out.append({"input": ''.join(map(str, bits)), "false_mass": mass[0],
                    "true_mass": mass[1], "queries": 1})
    return out


def main():
    result = {
        "scope": "exact finite rational arithmetic; no Lean or Comparator execution",
        "conjugation": conjugation_checks(),
        "or_two_selector": or_selector_checks(),
        "two_bit_parity": parity_checks(),
        "limitations": ["Does not prove general model equivalence.",
                        "Does not optimize one-query quantum success for OR2.",
                        "Does not check current Lean source against these Python objects."]
    }
    print(json.dumps(result, indent=2, default=str))


if __name__ == '__main__':
    main()
