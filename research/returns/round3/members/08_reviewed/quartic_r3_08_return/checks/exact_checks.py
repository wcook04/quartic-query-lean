#!/usr/bin/env python3
"""Exact semantic checks for the quartic Appendix A review.

Run: python3 exact_checks.py > exact_checks.json

All arithmetic is in integers, rational numbers, or Q(sqrt(2)).  The script
has no network access and writes only to stdout.  It is an independently
authored finite witness, not a Lean check or a proof of a general theorem.
"""

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
import json


@dataclass(frozen=True)
class K:
    """The exact real number a + b sqrt(2), with rational a and b."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __post_init__(self):
        object.__setattr__(self, "a", Fraction(self.a))
        object.__setattr__(self, "b", Fraction(self.b))

    @staticmethod
    def of(value):
        return value if isinstance(value, K) else K(value)

    def __add__(self, other):
        z = K.of(other)
        return K(self.a + z.a, self.b + z.b)

    __radd__ = __add__

    def __neg__(self):
        return K(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-K.of(other))

    def __rsub__(self, other):
        return K.of(other) - self

    def __mul__(self, other):
        z = K.of(other)
        return K(self.a * z.a + 2 * self.b * z.b,
                 self.a * z.b + self.b * z.a)

    __rmul__ = __mul__

    def rational(self):
        assert self.b == 0, (self.a, self.b)
        return self.a

    def pair(self):
        return [str(self.a), str(self.b)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def mv(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def signed_cube(d):
    # The d=0 matrix is included only as a degenerate boundary check.
    if d == 0:
        return [[0]]
    a = signed_cube(d - 1)
    n = len(a)
    return [[a[i][j] if i < n and j < n else
             -a[i-n][j-n] if i >= n and j >= n else
             int((i % n) == (j % n))
             for j in range(2*n)] for i in range(2*n)]


def main():
    inputs = list(product((0, 1), repeat=2))
    hilbert_basis = list(product((0, 1), repeat=2))  # (address, answer)
    parity = lambda x: x[0] ^ x[1]
    gamma = [[int(sum(a != b for a, b in zip(x, y)) == 1)
              for y in inputs] for x in inputs]
    masks = [[[gamma[j][k] * int(x[i] != y[i])
               for k, y in enumerate(inputs)] for j, x in enumerate(inputs)]
             for i in range(2)]
    assert gamma == transpose(gamma)
    assert all(gamma[j][k] >= 0 and
               (parity(x) != parity(y) or gamma[j][k] == 0)
               for j, x in enumerate(inputs) for k, y in enumerate(inputs))

    # The Walsh characters, normalized by 1/2, form a complete rational
    # orthonormal eigenbasis.  Thus ||Gamma||_2=2 is an exact conclusion.
    eigensystem = []
    eigenvectors = [[Fraction((-1) ** sum(a*b for a, b in zip(s, x)), 2)
                     for x in inputs] for s in inputs]
    eigenvalues = [2 - 2*sum(s) for s in inputs]
    for i, (v, eigenvalue) in enumerate(zip(eigenvectors, eigenvalues)):
        assert mv(gamma, v) == [eigenvalue*z for z in v]
        for j, w in enumerate(eigenvectors):
            assert dot(v, w) == int(i == j)
        eigensystem.append({"eigenvalue": eigenvalue,
                            "vector": [str(z) for z in v]})
    for masked in masks:
        assert mm(transpose(masked), masked) == identity(4)

    # The initial vector is |+>_address tensor |->_answer.  It has rational
    # amplitudes (1,-1,1,-1)/2.  The final H tensor I is calculated in the
    # exact quadratic field, rather than by squaring a scaled surrogate.
    initial = [K(Fraction((-1)**b, 2)) for i, b in hilbert_basis]
    h_gate = [[K(0, Fraction((-1)**(i*j), 2)) if b == c else K()
               for j, c in hilbert_basis] for i, b in hilbert_basis]
    assert mm(transpose(h_gate), h_gate) == [
        [K(z) for z in row] for row in identity(4)]
    assert dot(initial, initial) == K(1)

    runs = []
    after_query = []
    for x in inputs:
        # O_x |i,b> = |i,b XOR x_i> is exactly the ordinary bit oracle.
        oracle = [[int((i, b) == (j, c ^ x[j]))
                   for j, c in hilbert_basis] for i, b in hilbert_basis]
        assert mm(transpose(oracle), oracle) == identity(4)
        queried = mv(oracle, initial)
        final = mv(h_gate, queried)
        after_query.append(queried)
        assert dot(queried, queried) == K(1)
        assert dot(final, final) == K(1)
        probs = [sum((final[j]*final[j]).rational()
                     for j, (i, _) in enumerate(hilbert_basis) if i == bit)
                 for bit in (0, 1)]
        assert probs[parity(x)] == 1
        assert probs[1-parity(x)] == 0
        runs.append({"input": list(x), "parity": parity(x),
                     "oracle_matrix": oracle,
                     "final_amplitudes_a_plus_b_sqrt2": [z.pair() for z in final],
                     "output_probabilities_0_1": [str(p) for p in probs]})

    perron = eigenvectors[0]

    def progress(states):
        return sum(gamma[i][j]*perron[i]*perron[j]*dot(states[i], states[j])
                   for i in range(4) for j in range(4))

    w0 = progress([initial]*4).rational()
    w1 = progress(after_query).rational()
    assert w0 == 2 and w1 == 0
    assert w0-w1 == 2  # Exactly 2 max_i ||Gamma_i||.

    epsilon = Fraction(1, 100)
    epsilon_product = epsilon*(1-epsilon)
    assert epsilon_product == Fraction(99, 10000)
    # sqrt(99)<25 follows from 99<625 because both sides are nonnegative.
    assert 99 < 25**2
    c_third = K(Fraction(1, 2), Fraction(-1, 3))
    kappa_third = K(18, 12)
    assert c_third*kappa_third == K(1)
    assert 12**2*2 < 17**2  # Thus 18+12 sqrt(2)<35.

    cube_cases = []
    for d in range(5):
        a = signed_cube(d)
        cube = list(product((0, 1), repeat=d))
        n = 2**d
        assert a == transpose(a)
        assert mm(a, a) == [[d*z for z in row] for row in identity(n)]
        assert sum(a[i][i] for i in range(n)) == 0
        assert all(abs(a[i][j]) ==
                   int(sum(x != y for x, y in zip(cube[i], cube[j])) == 1)
                   for i in range(n) for j in range(n))
        signs = [(-1)**sum(x) for x in cube]
        assert [[signs[i]*a[i][j]*signs[j] for j in range(n)]
                for i in range(n)] == [[-z for z in row] for row in a]
        cube_cases.append({"dimension": d, "matrix_order": n,
                           "symmetric": True, "square_equals_d_identity": True,
                           "trace": 0, "absolute_value_is_cube_adjacency": True,
                           "parity_conjugation_negates_matrix": True,
                           "distinct_eigenvalue_split_applicable": d >= 1,
                           "multiplicity_each_if_d_positive": 2**(d-1) if d else None,
                           "zero_dimension_note": "one zero eigenvalue; no two-root split" if not d else None})

    out = {
        "status": "passed",
        "scope": "finite exact semantic witness; not Lean elaboration, universal proof, or author-confirmed erratum",
        "arithmetic": "integers, fractions.Fraction, and exact Q(sqrt(2))",
        "randomized": False,
        "lean_checked": False,
        "input_order": [list(x) for x in inputs],
        "hilbert_basis_order_address_answer": [list(x) for x in hilbert_basis],
        "gamma": gamma, "coordinate_masks": masks,
        "orthonormal_eigensystem": eigensystem,
        "gamma_norm": 2, "coordinate_mask_norms": [1, 1],
        "feasible_adversary_ratio": 2,
        "oracle_calls": 1, "algorithm_runs": runs,
        "progress": {"initial": str(w0), "after_one_query": str(w1),
                     "drop": str(w0-w1), "factor_two_saturated": True},
        "positive_error_counterexample": {
            "epsilon": str(epsilon), "epsilon_times_one_minus_epsilon": str(epsilon_product),
            "printed_lower_bound_from_witness": "2 - sqrt(99)/25",
            "strictly_greater_than": 1,
            "equivalent_strict_integer_comparison": {"left": 99, "right": 625, "holds": True},
            "exact_algorithm_upper_bound": 1,
            "contradiction_to_printed_prefactor": True,
            "corrected_lower_bound_from_witness": "1 - sqrt(99)/50",
            "corrected_coefficient_consistent": True},
        "error_one_third_constants": {
            "correct_coefficient": "1/2 - sqrt(2)/3",
            "reciprocal": "18 + 12*sqrt(2)", "reciprocal_times_coefficient": 1,
            "reciprocal_strictly_below": 35,
            "strict_integer_comparison": {"left": 288, "right": 289, "holds": True},
            "literal_35_to_four": 35**4,
            "hybrid_16_times_35_squared": 16*35**2,
            "legacy_16_times_36_squared": 16*36**2},
        "signed_cube_cases": cube_cases
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
