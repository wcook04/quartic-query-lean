#!/usr/bin/env python3
"""Exact finite check of the two-bit parity spectral-adversary coefficient.

Run from the return directory:
    python checks/source_coefficient_check.py > checks/source_coefficient_check.json

No random cases, floating point, external packages, or Lean elaboration are used.
The final Hadamard gate is represented by B/sqrt(2), checking B^T B=2I
and computing its output probabilities as exact rational squared masses / 2.
"""

from fractions import Fraction as F
from itertools import product
import json


def transpose(a):
    return [list(row) for row in zip(*a)]


def matvec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def dot(v, w):
    return sum(x * y for x, y in zip(v, w))


def main():
    cube = list(product((0, 1), repeat=2))
    basis = list(product((0, 1), repeat=2))  # query index, answer bit
    parity = [x[0] ^ x[1] for x in cube]
    identity = [[int(i == j) for j in range(4)] for i in range(4)]
    gamma = [[int(sum(a != b for a, b in zip(x, y)) == 1)
              for y in cube] for x in cube]
    masks = [[[gamma[j][k] * int(x[i] != y[i])
               for k, y in enumerate(cube)] for j, x in enumerate(cube)]
             for i in range(2)]
    assert gamma == transpose(gamma)
    assert all(gamma[j][k] >= 0 and
               (parity[j] != parity[k] or gamma[j][k] == 0)
               for j in range(4) for k in range(4))

    # An exact orthonormal eigenbasis proves ||Gamma||_2=2.
    eigenvectors = [[F((-1) ** (s[0] * x[0] + s[1] * x[1]), 2)
                     for x in cube] for s in cube]
    eigenvalues = [2 - 2 * sum(s) for s in cube]
    for j, (v, value) in enumerate(zip(eigenvectors, eigenvalues)):
        assert matvec(gamma, v) == [value * z for z in v]
        for k, w in enumerate(eigenvectors):
            assert dot(v, w) == int(j == k)
    assert max(abs(value) for value in eigenvalues) == 2
    # Each mask is an orthogonal permutation, so its norm is exactly 1.
    for mask in masks:
        assert matmul(transpose(mask), mask) == identity

    initial = [F((-1) ** b, 2) for i, b in basis]
    assert dot(initial, initial) == 1
    # B/sqrt(2) applies Hadamard to the query-index register.
    b_matrix = [[((-1) ** (out_i * in_i)) * int(out_b == in_b)
                 for in_i, in_b in basis] for out_i, out_b in basis]
    assert matmul(transpose(b_matrix), b_matrix) == [
        [2 * entry for entry in row] for row in identity]
    after_oracle = []
    probabilities = []
    for x in cube:
        after = [initial[basis.index((i, b ^ x[i]))] for i, b in basis]
        after_oracle.append(after)
        assert dot(after, after) == 1
        scaled_final = matvec(b_matrix, after)
        output_prob = [sum(scaled_final[j] ** 2 / 2
                           for j, (i, _) in enumerate(basis) if i == answer)
                       for answer in (0, 1)]
        assert output_prob[x[0] ^ x[1]] == 1
        assert output_prob[1 - (x[0] ^ x[1])] == 0
        probabilities.append([str(p) for p in output_prob])

    perron = eigenvectors[0]

    def progress(states):
        return sum(perron[j] * perron[k] * gamma[j][k]
                   * dot(states[j], states[k])
                   for j in range(4) for k in range(4))

    initial_progress = progress([initial] * 4)
    final_progress = progress(after_oracle)
    assert initial_progress == 2 and final_progress == 0
    assert initial_progress - final_progress == 2  # =2 max_i ||Gamma_i||.

    # At epsilon=1/100, 2(1-2sqrt(epsilon(1-epsilon)))>1 follows
    # from epsilon(1-epsilon)<1/16, with no floating-point square root.
    epsilon = F(1, 100)
    assert epsilon * (1 - epsilon) == F(99, 10000)
    assert epsilon * (1 - epsilon) < F(1, 16)
    print(json.dumps({
        "scope": "finite exact witness; no Lean proof or literature erratum certification",
        "arithmetic": "exact_integer_and_fraction",
        "seed": None,
        "randomized": False,
        "lean_compiled": False,
        "input_order": [list(x) for x in cube],
        "basis_order": [list(p) for p in basis],
        "gamma": gamma,
        "coordinate_masks": masks,
        "gamma_orthonormal_eigenvalues": eigenvalues,
        "gamma_norm": 2,
        "coordinate_mask_norms": [1, 1],
        "spectral_ratio": 2,
        "oracle_calls": 1,
        "output_probabilities_false_true": probabilities,
        "initial_progress": str(initial_progress),
        "final_progress": str(final_progress),
        "per_query_factor_two_saturated": True,
        "positive_error_witness": str(epsilon),
        "positive_error_product": str(epsilon * (1 - epsilon)),
        "positive_error_product_less_than_one_sixteenth": True,
        "printed_prefactor_incompatible_with_one_query_witness": True,
        "passed": True,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
