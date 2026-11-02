#!/usr/bin/env python3
"""Exact finite counterexample: Z-label laws do not determine a quantum state.

Uses only the Python standard library and rational density matrices, so no
floating-point approximation or irrational amplitude is needed. This is an
ordinary calculation, not a Lean run or a verification of Samples.bind.

Run: python state_example.py
The deterministic JSON report is written next to this script.
"""

from fractions import Fraction
import json
from pathlib import Path


Q = Fraction


def density_from_integer_ray(vector):
    """Return |v><v|/<v|v> for a nonzero real integer vector."""
    norm_squared = sum(Q(value) ** 2 for value in vector)
    assert norm_squared > 0
    return [
        [Q(left) * Q(right) / norm_squared for right in vector]
        for left in vector
    ]


def matrix_product(left, right):
    assert left and right and len(left[0]) == len(right)
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Q(0))
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def trace(matrix):
    assert matrix and all(len(row) == len(matrix) for row in matrix)
    return sum((matrix[i][i] for i in range(len(matrix))), Q(0))


def tensor_product(left, right):
    return [
        [left[i][j] * right[k][ell]
         for j in range(len(left[0])) for ell in range(len(right[0]))]
        for i in range(len(left)) for k in range(len(right))
    ]


def partial_trace_second(matrix, first_dimension=2, second_dimension=2):
    size = first_dimension * second_dimension
    assert len(matrix) == size and all(len(row) == size for row in matrix)
    return [
        [sum((matrix[a * second_dimension + b][c * second_dimension + b]
              for b in range(second_dimension)), Q(0))
         for c in range(first_dimension)]
        for a in range(first_dimension)
    ]


def measurement_probability(density, projector):
    return trace(matrix_product(density, projector))


def conjugate_by_permutation(matrix, permutation):
    """Conjugate by U|i> = |permutation[i]>."""
    size = len(matrix)
    assert sorted(permutation) == list(range(size))
    result = [[Q(0) for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[permutation[i]][permutation[j]] = matrix[i][j]
    return result


def exact_json(value):
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, list):
        return [exact_json(item) for item in value]
    if isinstance(value, dict):
        return {key: exact_json(item) for key, item in value.items()}
    return value


def main():
    rho_plus = density_from_integer_ray([1, 1])
    rho_zero = density_from_integer_ray([1, 0])
    rho_product = density_from_integer_ray([1, 0, 1, 0])
    rho_bell = density_from_integer_ray([1, 0, 0, 1])
    rho_product_first = partial_trace_second(rho_product)
    rho_bell_first = partial_trace_second(rho_bell)
    rho_mixed = [[Q(1, 2), Q(0)], [Q(0), Q(1, 2)]]

    # All global states are exact positive rank-one projectors by construction.
    for density in (rho_plus, rho_zero, rho_product, rho_bell):
        assert trace(density) == 1
        assert matrix_product(density, density) == density
        assert density == [list(row) for row in zip(*density)]
    assert tensor_product(rho_plus, rho_zero) == rho_product
    assert rho_product_first == rho_plus
    assert rho_bell_first == rho_mixed
    assert trace(rho_bell_first) == trace(rho_product_first) == 1

    z_product = [rho_product_first[i][i] for i in range(2)]
    z_bell = [rho_bell_first[i][i] for i in range(2)]
    assert z_product == z_bell == [Q(1, 2), Q(1, 2)]

    plus_product = measurement_probability(rho_product_first, rho_plus)
    plus_bell = measurement_probability(rho_bell_first, rho_plus)
    assert plus_product == Q(1)
    assert plus_bell == Q(1, 2)
    assert plus_product != plus_bell
    purity_product = trace(matrix_product(rho_product_first, rho_product_first))
    purity_bell = trace(matrix_product(rho_bell_first, rho_bell_first))
    assert purity_product == 1 and purity_bell == Q(1, 2)

    # CNOT control = first qubit, target = second qubit. It copies and uncopies
    # the computational label coherently, and is its own inverse.
    cnot = [0, 1, 3, 2]
    assert [cnot[cnot[i]] for i in range(4)] == list(range(4))
    assert conjugate_by_permutation(rho_product, cnot) == rho_bell
    uncomputed = conjugate_by_permutation(rho_bell, cnot)
    assert uncomputed == rho_product
    assert partial_trace_second(uncomputed) == rho_plus

    report = {
        "schema": "exact-returned-subsystem-example/v1",
        "status": "passed",
        "arithmetic": "fractions.Fraction; exact rational density matrices",
        "basis_order": ["00", "01", "10", "11"],
        "first_register_basis": ["0", "1"],
        "states": {
            "product_plus_zero": {
                "description": "|+> tensor |0>, where |+> = (|0> + |1>)/sqrt(2)",
                "density_matrix": rho_product,
                "first_register_density_matrix": rho_product_first,
                "first_register_purity": purity_product,
            },
            "bell": {
                "description": "(|00> + |11>)/sqrt(2)",
                "density_matrix": rho_bell,
                "first_register_density_matrix": rho_bell_first,
                "first_register_purity": purity_bell,
            },
        },
        "computational_basis_measurement_on_first_register": {
            "product_probabilities": z_product,
            "bell_probabilities": z_bell,
            "laws_equal": True,
        },
        "plus_minus_measurement_on_first_register": {
            "plus_projector": rho_plus,
            "product_plus_probability": plus_product,
            "bell_plus_probability": plus_bell,
            "laws_equal": False,
        },
        "cnot_uncomputation": {
            "control": "first register",
            "target": "second register",
            "basis_index_permutation": cnot,
            "self_inverse": True,
            "product_maps_to_bell": True,
            "bell_maps_to_product": True,
            "uncomputed_density_matrix": uncomputed,
            "original_pure_state_restored": True,
        },
        "conclusion": (
            "Equal computational-label laws do not determine the returned "
            "subsystem's quantum state. A specified coherent uncomputation "
            "can restore the pure state in this example."
        ),
        "scope": {
            "new_lean_run": False,
            "verifies_samples_bind_implementation": False,
            "proves_amplification_impossible": False,
            "purpose": "Exact finite example supporting section 5.1 and LEAN_GAPS.md",
        },
    }
    output_path = Path(__file__).with_suffix(".json")
    output_path.write_text(json.dumps(exact_json(report), indent=2) + "\n", encoding="utf-8")
    print("PASS: same Z law (1/2, 1/2); plus probabilities 1 and 1/2.")
    print("PASS: CNOT uncomputation restores |+> tensor |0> exactly.")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
