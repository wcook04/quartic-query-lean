#!/usr/bin/env python3
"""Supplemental finite checks. These do not compile Lean or prove a theorem.

Run from any directory with Python 3 and NumPy:
    python checks/huang_and_restriction_checks.py
The JSON result is written beside this script.
"""

import itertools
import json
from pathlib import Path

import numpy as np


def signed_cube(d):
    h = np.zeros((1, 1), dtype=np.int64)
    for _ in range(d):
        eye = np.eye(len(h), dtype=np.int64)
        h = np.block([[h, eye], [eye, -h]])
    return h


def adjacency(n, values=None):
    a = np.zeros((1 << n, 1 << n), dtype=np.int64)
    for x in range(1 << n):
        for i in range(n):
            y = x ^ (1 << i)
            if values is None or values[x] != values[y]:
                a[x, y] = 1
    return a


def sign_fourier_numerators(n, values):
    return [sum((1 - 2 * values[x]) * (-1 if (x & s).bit_count() % 2 else 1)
                for x in range(1 << n)) for s in range(1 << n)]


matrix_tests = []
for d in range(9):
    h = signed_cube(d)
    assert np.array_equal(h.T, h)
    assert np.array_equal(h @ h, d * np.eye(1 << d, dtype=np.int64))
    assert np.trace(h) == 0
    assert np.array_equal(np.abs(h), adjacency(d))
    numerical_multiplicities = None
    if d > 0:
        eigen = np.linalg.eigvalsh(h.astype(float))
        plus = int(np.count_nonzero(np.isclose(eigen, np.sqrt(d), atol=1e-10, rtol=0)))
        minus = int(np.count_nonzero(np.isclose(eigen, -np.sqrt(d), atol=1e-10, rtol=0)))
        assert plus == minus == 1 << (d - 1)
        numerical_multiplicities = {"positive": plus, "negative": minus}
    matrix_tests.append({"d": d, "size": 1 << d,
                         "exact_integer_square_trace_symmetry_absolute_adjacency": True,
                         "numerical_eigenvalue_counts": numerical_multiplicities})

restriction_tests = []
total_restrictions = 0
for n in range(4):
    positive_degree_functions = 0
    faces = 0
    for table in range(1 << (1 << n)):
        values = [(table >> x) & 1 for x in range(1 << n)]
        coeff = sign_fourier_numerators(n, values)
        degree = max((s.bit_count() for s, c in enumerate(coeff) if c), default=0)
        a = adjacency(n, values)
        lam = max(abs(np.linalg.eigvalsh(a.astype(float))))
        assert degree <= lam * lam + 1e-10
        if degree == 0:
            assert len(set(values)) == 1
            continue
        positive_degree_functions += 1
        for s, cs in enumerate(coeff):
            if not cs or s.bit_count() != degree:
                continue
            inside = [i for i in range(n) if (s >> i) & 1]
            outside = [i for i in range(n) if not (s >> i) & 1]
            for z in range(1 << len(outside)):
                base = sum(((z >> k) & 1) << i for k, i in enumerate(outside))
                embed = [base | sum(((y >> k) & 1) << i for k, i in enumerate(inside))
                         for y in range(1 << degree)]
                face = [values[x] for x in embed]
                face_num = sign_fourier_numerators(degree, face)[(1 << degree) - 1]
                assert face_num * (1 << n) == cs * (1 << degree)
                assert face_num != 0
                sigma = 1 if face_num > 0 else -1
                u = [y for y in range(1 << degree)
                     if (1 - 2 * face[y]) == sigma * (-1 if y.bit_count() % 2 else 1)]
                assert 2 * len(u) > 1 << degree
                for y in u:
                    for i in range(degree):
                        yy = y ^ (1 << i)
                        if yy in u:
                            assert face[y] != face[yy]
                            assert a[embed[y], embed[yy]] == 1
                faces += 1
    total_restrictions += faces
    restriction_tests.append({"n": n, "functions": 1 << (1 << n),
                              "positive_degree_functions": positive_degree_functions,
                              "maximal_support_outside_assignment_pairs": faces,
                              "exact_coefficient_survival_and_majority_edges": True,
                              "numerical_degree_le_spectral_norm_squared": True})

large_subsets = []
for d in range(1, 4):
    h = signed_cube(d).astype(float)
    count = 0
    for k in range((1 << (d - 1)) + 1, (1 << d) + 1):
        for u in itertools.combinations(range(1 << d), k):
            principal = h[np.ix_(u, u)]
            assert np.linalg.eigvalsh(principal)[-1] >= np.sqrt(d) - 1e-10
            count += 1
    large_subsets.append({"d": d, "large_subsets": count,
                          "numerical_principal_largest_eigenvalue_bound": True})

# An inclusion-maximal support is essential for the coefficient-survival claim.
and2 = [0, 0, 0, 1]
assert sign_fourier_numerators(2, and2)[1] == 2  # coefficient 1/2
assert sign_fourier_numerators(1, [and2[0], and2[1]])[1] == 0

result = {
    "lean_compiled": False,
    "comparator_run": False,
    "scope": "Finite exact arithmetic and supplemental numerical checks only",
    "numpy_version": np.__version__,
    "numeric_tolerance": 1e-10,
    "matrix_tests": matrix_tests,
    "restriction_tests": restriction_tests,
    "total_restrictions": total_restrictions,
    "large_subset_tests": large_subsets,
    "boundary_checks": [
        "d=0 has the 1-by-1 zero matrix; the two distinct half-dimensional eigenspaces assertion requires d>0",
        "AND on two bits has nonzero singleton Fourier coefficient that vanishes after fixing the other bit to zero; maximality cannot be dropped",
    ],
    "passed": True,
}
path = Path(__file__).with_name("huang_and_restriction_checks.json")
path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"passed": True, "functions": 278, "restrictions": total_restrictions,
                  "matrix_dimensions": list(range(9)), "output": path.name}))
