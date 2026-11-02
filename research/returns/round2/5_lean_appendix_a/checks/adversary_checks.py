#!/usr/bin/env python3
"""Supplemental checks for Appendix A; these do not compile Lean or prove claims.

Run: python checks/adversary_checks.py > checks/adversary_checks.json
Exact tests use only the Python standard library. Numerical tests require NumPy.
"""

from fractions import Fraction as F
from itertools import product
from random import Random
import json


def exact_pair_identity():
    seed = 718429
    rng = Random(seed)
    n = 3
    cube = list(product([0, 1], repeat=n))
    dimension = n * 2

    def add(z, w):
        return z[0] + w[0], z[1] + w[1]

    def sub(z, w):
        return z[0] - w[0], z[1] - w[1]

    def mul(z, w):
        return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]

    def scale(a, z):
        return a * z[0], a * z[1]

    def inner(v, w):
        value = F(0), F(0)
        for z, t in zip(v, w):
            value = add(value, mul((z[0], -z[1]), t))
        return value

    def oracle(x, v):
        return [scale((-1) ** (b * x[i]), v[2 * i + b])
                for i in range(n) for b in (0, 1)]

    def projection(i, v):
        return [z if j == 2 * i + 1 else (F(0), F(0))
                for j, z in enumerate(v)]

    count = 0
    for _ in range(30):
        psi = [(F(rng.randrange(-5, 6), 7), F(rng.randrange(-5, 6), 11))
               for _ in range(dimension)]
        phi = [(F(rng.randrange(-5, 6), 13), F(rng.randrange(-5, 6), 17))
               for _ in range(dimension)]
        for x in cube:
            for y in cube:
                rhs = inner(psi, phi)
                for i in range(n):
                    if x[i] != y[i]:
                        rhs = sub(rhs, scale(2, inner(projection(i, psi), projection(i, phi))))
                assert inner(oracle(x, psi), oracle(y, phi)) == rhs
                count += 1
    return {
        "check": "arbitrary_input_controlled_phase_overlap_identity",
        "seed": seed,
        "arithmetic": "exact_complex_rational",
        "input_bits": n,
        "state_dimension": dimension,
        "state_pairs": 30,
        "ordered_input_pairs_per_state_pair": len(cube) ** 2,
        "cases": count,
        "normalized_states_required": False,
        "passed": True,
    }


def numerical_progress():
    import numpy as np

    seed = 91372
    rng = np.random.default_rng(seed)
    n = 3
    cube = np.array(list(product([0, 1], repeat=n)))
    count_inputs = len(cube)
    dimension = n * 2
    count = 0
    largest_ratio = -1.0
    tolerance = 1e-10

    for _ in range(100):
        f = np.bitwise_xor.reduce(cube, axis=1)
        gamma = rng.random((count_inputs, count_inputs))
        gamma = (gamma + gamma.T) / 2
        gamma[f[:, None] == f[None, :]] = 0
        _, eigenvectors = np.linalg.eigh(gamma)
        v = np.abs(eigenvectors[:, -1])
        v /= np.linalg.norm(v)
        psi = (rng.normal(size=(count_inputs, dimension))
               + 1j * rng.normal(size=(count_inputs, dimension)))
        psi /= np.linalg.norm(psi, axis=1)[:, None]
        phases = np.ones((count_inputs, dimension))
        phases[:, 1::2] = 1 - 2 * cube
        after = psi * phases

        def progress(z):
            return np.sum((v[:, None] * v[None, :] * gamma) * (z.conj() @ z.T))

        delta = abs(progress(after) - progress(psi))
        masks = [gamma * (cube[:, i, None] != cube[None, :, i]) for i in range(n)]
        coordinate_max = max(np.linalg.norm(mask, 2) for mask in masks)
        weights = abs(psi[:, 1::2]) * v[:, None]
        quadratic = sum(weights[:, i] @ masks[i] @ weights[:, i] for i in range(n))
        mass = sum(np.linalg.norm(weights[:, i]) ** 2 for i in range(n))
        assert delta <= 2 * quadratic + tolerance
        assert 2 * quadratic <= 2 * coordinate_max + tolerance
        assert mass <= 1 + tolerance
        largest_ratio = max(largest_ratio, float(delta / (2 * coordinate_max)))
        count += 1

    return {
        "check": "weighted_arbitrary_matrix_progress_bound",
        "seed": seed,
        "arithmetic": "numpy_float64_complex128",
        "numpy_version": np.__version__,
        "input_bits": n,
        "instances": count,
        "absolute_tolerance": tolerance,
        "largest_change_divided_by_bound": largest_ratio,
        "passed": True,
    }


def constants():
    assert F(2, 9) <= F(33, 70) ** 2
    assert 1 - 2 * F(33, 70) == F(2, 35)
    assert 35 ** 2 == 1225
    assert 35 ** 4 == 1500625
    assert 16 * 35 ** 2 == 19600
    return {
        "check": "rational_constants",
        "arithmetic": "exact_rational_and_integer",
        "passed": True,
        "spectral_factor": 35,
        "paper_star_block_factor": 1225,
        "paper_route_quartic_factor": 1500625,
        "polynomial_block_hybrid_quartic_factor": 19600,
    }


if __name__ == "__main__":
    output = {
        "scope": "supplemental finite tests only",
        "lean_compiled": False,
        "comparator_run": False,
        "tests": [exact_pair_identity(), numerical_progress(), constants()],
    }
    print(json.dumps(output, indent=2, sort_keys=True))
