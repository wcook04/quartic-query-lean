"""Reproducible finite checks for the accompanying Forrelation note.

These calculations supplement the proofs. Gaussian quadrature is floating point
and does not certify the identity. Dependencies: Python 3 and NumPy.
Run: python checks.py > checks_output.json
"""

import itertools
import json
import math
from fractions import Fraction as Q

import numpy as np
from numpy.polynomial.hermite import hermgauss


def phi(x):
    return x * (3 + x * x) / (2 * (2 + x * x) ** 1.5)


def psi(x):
    return 1 / (2 * np.sqrt(2 + x * x))


def dphi(x):
    return 3 / (2 + x * x) ** 2.5


def quadrature(nodes, matrix):
    """All 63 nonconstant characters for k=3, m=2, dimension four."""
    x, w = hermgauss(nodes)
    x = np.sqrt(2) * x
    w = w / np.sqrt(np.pi)
    grids = np.meshgrid(x, x, x, x, indexing="ij")
    u = np.stack([g.ravel() for g in grids], axis=1).reshape(-1, 2, 2)
    weights = np.einsum("a,b,c,d->abcd", w, w, w, w).ravel()
    v = np.einsum("ab,prb->pra", matrix, u)
    xx, yy = phi(u), phi(v)
    means = np.stack([xx[:, 0], yy[:, 0] * xx[:, 1], yy[:, 1]], axis=1)
    means = means.reshape(-1, 6)
    path_weights = []
    for path in itertools.product(range(2), repeat=3):
        a, b, c = path
        gaussian = psi(u[:, 0, a]) * dphi(v[:, 0, b])
        gaussian *= psi(u[:, 1, b]) * dphi(v[:, 1, c])
        path_weights.append((
            {a, 2 + b, 4 + c},
            gaussian * matrix[b, a] * matrix[c, b],
            gaussian * matrix[a, b] * matrix[b, c],
        ))
    maximum = dict(identity=0.0, missing_block=0.0,
                   omitted_s_integral=0.0, transposed_matrix=0.0)
    witness = {}
    for mask in range(1, 64):
        chosen = {i for i in range(6) if mask >> i & 1}
        moment = float(np.dot(weights, np.prod(means[:, sorted(chosen)], axis=1)))
        first = len(chosen & {0, 1})
        rhs = np.zeros(len(weights))
        wrong = np.zeros(len(weights))
        if first:
            for support, factor, factor_wrong in path_weights:
                if support <= chosen:
                    remainder = sorted(chosen - support)
                    rest = np.prod(means[:, remainder], axis=1) if remainder else 1.0
                    rhs += factor * rest / first
                    wrong += factor_wrong * rest / first
        value = float(np.dot(weights, rhs))
        error = abs(moment - value)
        if error > maximum["identity"]:
            maximum["identity"] = error
            witness["identity"] = sorted(chosen)
        controls = {
            "omitted_s_integral": abs(moment - first * value),
            "transposed_matrix": abs(moment - float(np.dot(weights, wrong))),
        }
        for label, error in controls.items():
            if error > maximum[label]:
                maximum[label] = error
                witness[label] = sorted(chosen)
        if any(not chosen & {2 * r, 2 * r + 1} for r in range(3)):
            maximum["missing_block"] = max(maximum["missing_block"], abs(moment))
    return {"nodes_per_dimension": nodes, "grid_size": nodes ** 4,
            "matrix": matrix.tolist(), "characters": 63,
            "max_absolute_errors": maximum, "witness_supports": witness}


def restriction_check():
    """Exact rational proof instance of the nonconstant free-probability transfer."""
    mu = [Q(1, 3), Q(-1, 5), Q(1, 7)]
    free = [Q(1, 2), Q(3, 4), Q(1, 2)]
    pol = {(): Q(2, 7), (0,): Q(1, 11), (1, 2): Q(-2, 13),
           (0, 1, 2): Q(3, 17)}
    maximum = Q(0)
    for r in range(4):
        for support in itertools.combinations(range(3), r):
            support = set(support)
            expected = Q(0)
            for state in itertools.product((0, -1, 1), repeat=3):
                probability = Q(1)
                for i, s in enumerate(state):
                    probability *= free[i] if s == 0 else (1 - free[i] + s * mu[i]) / 2
                coefficient = Q(0)
                for monomial, a in pol.items():
                    remaining = {i for i in monomial if state[i] == 0}
                    if remaining == support:
                        fixed = math.prod(state[i] for i in monomial if state[i] != 0)
                        coefficient += a * fixed
                expected += probability * coefficient
            derivative = sum((a * math.prod(mu[i] for i in monomial if i not in support)
                              for monomial, a in pol.items() if support <= set(monomial)), Q(0))
            target = math.prod(free[i] for i in support) * derivative
            maximum = max(maximum, abs(expected - target))
    return {"cases": 8, "max_error": str(maximum), "arithmetic": "exact rational"}


def main():
    exact = {
        "amplification_18_times_8_pow_25_lt_9_pow_25": 18 * 8 ** 25 < 9 ** 25,
        "elementary_constant_identity": 800 * Q(2, 18225) == Q(8, 27) ** 2,
        "kernel_times_scale": Q(3, 16) * Q(8, 27) == Q(1, 18),
        "contradiction_margin": Q(59, 108) < Q(3, 4) < Q(119, 144),
        "coarse_constant": Q(2, 18225) / 256 == Q(1, 2332800),
    }
    assert all(exact.values())
    rotation = np.array([[math.cos(.41), -math.sin(.41)],
                         [math.sin(.41), math.cos(.41)]])
    checks = [quadrature(n, rotation) for n in (16, 28)]
    perturbed = rotation.copy()
    perturbed[0, 1] += .2
    controls = quadrature(20, perturbed)
    out = {
        "purpose": "Finite arithmetic and numerical falsification checks, not a proof certificate",
        "exact_constants": exact, "restriction_identity": restriction_check(),
        "orthogonal_identity_checks": checks,
        "nonorthogonal_control": controls,
        "note": "All residuals are absolute; compare grids and failing controls. Matrix orientation and the s-integral are essential.",
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
