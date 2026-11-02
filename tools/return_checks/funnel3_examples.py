#!/usr/bin/env python3
"""Exact finite calculations for the examples-first quartic-query exposition.

Run with Python 3.10 or later, using only the standard library:
    python3 examples.py
    python3 examples.py --output examples_output.txt

The output is deterministic JSON. Every rational value is emitted exactly.
The opening board is an instance of the GENERIC addressed construction with
m=4, r=2 and a deliberately easy two-bit partial function. It is not F_{2,4}.
The separate Forrelation calculations use k=2, m=4; the actual headline
parameters at that size have r=40. The script does not allocate those arrays.

Checks cover finite examples and numerical substitutions. They do not certify
the asymptotic separation, a Lean build, the unspecified hard distribution,
or the implementation of the general quantum algorithm.

Sources: OpenAI, A Nearly Quartic Separation Between Randomized and Quantum
Query Complexity (5 October 2026), Sections 2--5; the supplied worked_examples.md
and verify_examples.py; and BHMT, Quantum Amplitude Amplification and Estimation,
Section 2. The new fully explicit toy circuit and board are expository examples.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json
from pathlib import Path


ADDRESSES = ("00", "01", "10", "11")
COLUMNS = tuple(range(1, 5))
BASE_X = ("1111", "0111", "1011", "1101")
BASE_A = (((0, 0), (0, 0)), ((1, 1), (1, 1)),
          ((0, 0), (0, 0)), ((0, 0), (0, 0)))
BASE_POINTERS = ((None, 1, 2, 3), (1, None, 2, 1),
                 (1, 2, None, 3), (1, 1, 1, None))


def gadget(a):
    """f(u,v)=v when u=0, undefined when u=1."""
    u, v = a
    return v if u == 0 else None


def gate_values(a):
    """Circuit with two non-input gates, d=NOT u and b=COPY v."""
    u, v = a
    return (1 - u, v)


def pointer_word(row):
    """The paper permits a fixed bijection; use 1,2,3,4 <-> 00,01,10,11."""
    return format(row - 1, "02b")


def blank_board(x, address_instances):
    """Physical bit dictionary, with all sixteen cells initially zero."""
    bits = {}
    for i in COLUMNS:
        for j in COLUMNS:
            bits[("X", i, j)] = int(x[i - 1][j - 1])
        for h in (1, 2):
            for q in (0, 1):
                bits[("A", i, h, q)] = address_instances[i - 1][h - 1][q]
        for s in ADDRESSES:
            for j in COLUMNS:
                if i != j:
                    for b in (0, 1):
                        bits[("P", i, s, j, b)] = 0
            for h in (1, 2):
                for g in (0, 1):
                    bits[("T", i, s, h, g)] = 0
    assert len(bits) == 192
    return bits


def fill_cell(bits, i, s, pointers, transcripts):
    for j in COLUMNS:
        if j != i:
            for b, value in enumerate(pointer_word(pointers[j - 1])):
                bits[("P", i, s, j, b)] = int(value)
    for h in (1, 2):
        for g in (0, 1):
            bits[("T", i, s, h, g)] = transcripts[h - 1][g]


def read_a(bits, i, h):
    return tuple(bits[("A", i, h, q)] for q in (0, 1))


def read_x(bits, i, j):
    return bits[("X", i, j)]


def read_pointer(bits, i, s, j):
    return 1 + 2 * bits[("P", i, s, j, 0)] + bits[("P", i, s, j, 1)]


def read_transcript(bits, i, s, h):
    return tuple(bits[("T", i, s, h, g)] for g in (0, 1))


def true_address(bits, i):
    values = [gadget(read_a(bits, i, h)) for h in (1, 2)]
    return None if None in values else "".join(map(str, values))


def proposed_address(bits, i):
    # A completely specified total decoder: return v, even if u=1.
    return "".join(str(read_a(bits, i, h)[1]) for h in (1, 2))


def wins_at(bits, i, s):
    """Direct mathematical definition; kept separate from local tests."""
    return (all(read_x(bits, i, j) == 1 for j in COLUMNS)
            and true_address(bits, i) == s
            and all(read_transcript(bits, i, s, h) == gate_values(read_a(bits, i, h))
                    for h in (1, 2))
            and all(read_x(bits, j, read_pointer(bits, i, s, j)) == 0
                    for j in COLUMNS if j != i))


def local_tests(bits, i, s):
    tests = []
    for j in COLUMNS:
        tests.append((f"X_{i}[{j}]=1", read_x(bits, i, j) == 1))
    for j in COLUMNS:
        if j != i:
            tests.append((f"pointer_to_{j}_hits_zero",
                          read_x(bits, j, read_pointer(bits, i, s, j)) == 0))
    for h in (1, 2):
        u, v = read_a(bits, i, h)
        d, b = read_transcript(bits, i, s, h)
        tests.extend(((f"h{h}:d=NOT_u", d == 1 - u),
                      (f"h{h}:b=COPY_v", b == v),
                      (f"h{h}:d=1", d == 1),
                      (f"h{h}:b=address_bit", b == int(s[h - 1]))))
    assert len(tests) == 15
    return tests


def winners(bits):
    return [(i, s) for i in COLUMNS for s in ADDRESSES if wins_at(bits, i, s)]


def check_definition_and_tests(bits):
    for i in COLUMNS:
        for s in ADDRESSES:
            assert wins_at(bits, i, s) == all(value for _, value in local_tests(bits, i, s))
    assert len(winners(bits)) <= 1


def cell_word(bits, i, s):
    pointer_bits = [bits[("P", i, s, j, b)] for j in COLUMNS if j != i for b in (0, 1)]
    transcript_bits = [bits[("T", i, s, h, g)] for h in (1, 2) for g in (0, 1)]
    return "".join(map(str, pointer_bits + transcript_bits))


def comparison_matrix(bits):
    """Sort the pair, use its proposed cells, and break ties by smaller index."""
    a = [[F(0) for _ in COLUMNS] for _ in COLUMNS]
    for i in COLUMNS:
        for j in COLUMNS:
            if i >= j:
                continue
            si, sj = proposed_address(bits, i), proposed_address(bits, j)
            i_disqualifies = read_x(bits, j, read_pointer(bits, i, si, j)) == 0
            j_disqualifies = read_x(bits, i, read_pointer(bits, j, sj, i)) == 0
            victor = (i if i_disqualifies else j) if i_disqualifies != j_disqualifies else i
            loser = j if victor == i else i
            a[victor - 1][loser - 1] = F(1)
    return tuple(tuple(row) for row in a)


def opening_board():
    for a in product((0, 1), repeat=2):
        d, b = gate_values(a)
        assert bool(d) == (gadget(a) is not None)
        assert not d or b == gadget(a)
    bits = blank_board(BASE_X, BASE_A)
    for i in COLUMNS:
        transcripts = tuple(gate_values(a) for a in BASE_A[i - 1])
        for s in ADDRESSES:
            fill_cell(bits, i, s, BASE_POINTERS[i - 1], transcripts)
    check_definition_and_tests(bits)
    assert winners(bits) == [(1, "00")]
    expected_matrix = ((0, 1, 1, 1), (0, 0, 1, 0), (0, 0, 0, 1), (0, 1, 0, 0))
    assert comparison_matrix(bits) == expected_matrix
    expected_words = ("0001101010", "0001000101", "0001101010", "0000001010")
    for i in COLUMNS:
        assert all(cell_word(bits, i, s) == expected_words[i - 1] for s in ADDRESSES)
    fail_counts = [[sum(not value for _, value in local_tests(bits, i, s))
                    for s in ADDRESSES] for i in COLUMNS]
    assert fail_counts == [[0, 1, 1, 2], [7, 6, 6, 5], [3, 4, 4, 5], [3, 4, 4, 5]]

    # Every single physical-bit mutation still agrees with the total definition.
    for location in bits:
        changed = bits.copy()
        changed[location] ^= 1
        check_definition_and_tests(changed)

    # A wrong pointer leaves candidate comparisons unchanged but invalidates F.
    bad_pointer = bits.copy()
    bad_pointer[("P", 1, "00", 2, 1)] = 1   # row 1 (00) -> row 2 (01)
    assert winners(bad_pointer) == []
    assert comparison_matrix(bad_pointer) == comparison_matrix(bits)
    pointer_failures = [name for name, value in local_tests(bad_pointer, 1, "00") if not value]
    assert pointer_failures == ["pointer_to_2_hits_zero"]

    # One corrupted d bit violates BOTH its gate equation and its output test.
    bad_d = bits.copy()
    bad_d[("T", 1, "00", 1, 0)] = 0
    assert winners(bad_d) == []
    d_failures = [name for name, value in local_tests(bad_d, 1, "00") if not value]
    assert d_failures == ["h1:d=NOT_u", "h1:d=1"]

    # No decoded opponent address or pointer target can find a zero in X_1.
    incoming_checks = 0
    for opponent in (2, 3, 4):
        for s in ADDRESSES:
            for target in COLUMNS:
                assert read_x(bits, 1, target) == 1
                assert read_x(bits, opponent, BASE_POINTERS[0][opponent - 1]) == 0
                incoming_checks += 1
    assert incoming_checks == 48

    # A pointer test reads three bits adaptively, yet its Boolean function
    # depends on all six physical input bits (two pointer bits and four targets).
    def pointer_test(values):
        p0, p1, *targets = values
        return 1 - targets[2 * p0 + p1]

    witnesses = []
    pointer_inputs = tuple(product((0, 1), repeat=6))
    for q in range(6):
        for values in pointer_inputs:
            altered = list(values)
            altered[q] ^= 1
            if pointer_test(values) != pointer_test(altered):
                witnesses.append({"changed_variable": q, "input": values,
                                  "flipped_input": altered,
                                  "test_values": (pointer_test(values), pointer_test(altered))})
                break
        else:
            raise AssertionError("An alleged relevant variable had no witness.")
    assert len(pointer_inputs) == 64 and len(witnesses) == 6

    rows = []
    for i in COLUMNS:
        s = proposed_address(bits, i)
        rows.append({"column": i, "X": BASE_X[i - 1], "A": BASE_A[i - 1],
                     "true_address": true_address(bits, i), "proposed_address": s,
                     "pointers_by_destination": BASE_POINTERS[i - 1],
                     "truthful_transcripts": [gate_values(a) for a in BASE_A[i - 1]],
                     "cells": {t: cell_word(bits, i, t) for t in ADDRESSES},
                     "failed_tests_at_proposed_address": [name for name, value in local_tests(bits, i, s)
                                                          if not value]})
    result = {
        "scope": "Generic construction, easy gadget; not the hard family F_{2,4}.",
        "parameters": {"m": 4, "ell": 2, "r": 2, "gadget_input_bits": 2, "S": 2,
                       "cells_per_column": 4, "total_cells": 16,
                       "pointer_bits_per_cell": 6, "transcript_bits_per_cell": 4,
                       "cell_bits": 10, "X_bits": 16, "A_bits": 16, "all_cell_bits": 160,
                       "total_bits": len(bits), "tests": 15, "largest_classical_test_depth": 3},
        "gadget_truth_table": [{"input": a, "f": gadget(a), "circuit_d_b": gate_values(a)}
                               for a in product((0, 1), repeat=2)],
        "pointer_encoding": {str(j): pointer_word(j) for j in COLUMNS},
        "columns": rows,
        "winner_pairs": winners(bits),
        "comparison_matrix": comparison_matrix(bits),
        "address_order_for_failure_counts": ADDRESSES,
        "failed_test_counts": fail_counts,
        "single_bit_mutations_checked": len(bits),
        "incoming_pointer_scenarios_checked": incoming_checks,
        "adaptive_pointer_test": {
            "variable_order": ("pointer_bit_0", "pointer_bit_1", "target_row_1", "target_row_2",
                               "target_row_3", "target_row_4"),
            "input_assignments": len(pointer_inputs), "relevant_variables": len(witnesses),
            "queries_per_evaluation": 3, "relevance_witnesses": witnesses},
        "broken_pointer": {"from_column": 1, "to_column": 2, "old_row": 1, "new_row": 2,
                           "failed_tests": pointer_failures, "winner_pairs": [],
                           "comparison_matrix_unchanged": True},
        "corrupt_d": {"column": 1, "address": "00", "instance": 1,
                      "failed_tests": d_failures, "winner_pairs": []},
    }
    return result, comparison_matrix(bits)


def drift_at(a, w):
    W = sum(w)
    assert W > 0
    choices = []
    expectation = F(0)
    for p, wp in enumerate(w):
        if not wp:
            continue
        new = tuple(wi * a[i][p] for i, wi in enumerate(w))
        probability = wp / W
        expectation += probability * sum(new)
        choices.append({"pivot": p + 1, "probability": probability,
                        "new_weights": new, "new_total": sum(new)})
    identity = (W * W - sum(wi * wi for wi in w)) / (2 * W)
    assert expectation == identity <= W / 2
    return {"weights": w, "total": W, "choices": choices,
            "expected_new_total": expectation, "drift_identity_value": identity}


def tournament_stats(a, steps):
    m = len(a)
    for i in range(m):
        assert a[i][i] == 0
        for j in range(m):
            assert 0 <= a[i][j] <= 1
            if i != j:
                assert a[i][j] + a[j][i] == 1
    states = [(F(1), (), (F(1),) * m)]
    result = []
    for t in range(steps + 1):
        assert sum(probability for probability, _, _ in states) == 1
        result.append({"steps": t,
                       "miss_candidate_1": sum(p for p, history, _ in states if 1 not in history),
                       "expected_total_weight": sum(p * sum(w) for p, _, w in states)})
        if t == steps:
            break
        children = []
        for probability, history, w in states:
            if not sum(w):
                children.append((probability, history, w))
                continue
            for choice in drift_at(a, w)["choices"]:
                p = choice["pivot"]
                assert p not in history
                children.append((probability * choice["probability"], history + (p,), choice["new_weights"]))
        states = children
    return result


def tournaments(cycle):
    cycle_stats = tournament_stats(cycle, 3)
    assert [row["miss_candidate_1"] for row in cycle_stats] == [1, F(3, 4), F(3, 8), 0]
    fractional = tuple(tuple(F(0) if i == j or j == 0 else F(1) if i == 0 else F(1, 2)
                             for j in range(4)) for i in range(4))
    fractional_stats = tournament_stats(fractional, 4)
    assert [row["miss_candidate_1"] for row in fractional_stats] == [1, F(3, 4), F(3, 8), F(3, 40), 0]
    w2 = (F(1), F(0), F(1, 2), F(1, 2))
    w3 = tuple(w2[i] * fractional[i][2] for i in range(4))
    assert w3 == (1, 0, 0, F(1, 4))
    assert drift_at(fractional, w2)["expected_new_total"] == F(5, 8)
    return {
        "scope": "Ideal pivot laws only; bounded quantum sampling may additionally fail.",
        "cycle_with_winner": {"matrix": cycle, "first_step": drift_at(cycle, (F(1),) * 4),
                              "statistics": cycle_stats},
        "fractional_abstract_example": {
            "scope": "An abstract comparison matrix, not asserted to come from the opening board.",
            "matrix": fractional, "after_pivot_2": drift_at(fractional, w2),
            "next_pivot_law": tuple(wi / sum(w2) for wi in w2),
            "after_pivots_2_then_3": w3,
            "following_pivot_law": tuple(wi / sum(w3) for wi in w3),
            "statistics": fractional_stats,
        },
    }


@dataclass(frozen=True)
class Qsqrt3:
    """Exact field element a+b*sqrt(3), used to check both reflections."""
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Qsqrt3) else Qsqrt3(F(value))

    def __add__(self, other):
        other = self.coerce(other)
        return Qsqrt3(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Qsqrt3(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __mul__(self, other):
        other = self.coerce(other)
        return Qsqrt3(self.a * other.a + 3 * self.b * other.b,
                      self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def rational(self):
        assert self.b == 0
        return self.a

    def __str__(self):
        if self.b == 0:
            return str(self.a)
        if self.a == 0:
            return f"({self.b})*sqrt(3)"
        return f"({self.a})+({self.b})*sqrt(3)"


def qdot(a, b):
    return sum((x * y for x, y in zip(a, b)), Qsqrt3())


def amplification():
    psi = (Qsqrt3(F(3, 10)), Qsqrt3(F(2, 5)), Qsqrt3(F(0), F(1, 2)))
    assert qdot(psi, psi) == Qsqrt3(F(1))

    def grover(v):
        flipped = (-v[0], -v[1], v[2])
        overlap = qdot(psi, flipped)
        return tuple(2 * overlap * prepared - old for prepared, old in zip(psi, flipped))

    states = []
    v = psi
    for length in range(6):
        good_mass = (v[0] * v[0] + v[1] * v[1]).rational()
        assert qdot(v, v) == Qsqrt3(F(1))
        conditional = tuple((component * component).rational() / good_mass for component in v[:2])
        assert conditional == (F(9, 25), F(16, 25))
        states.append({"iterations": length, "amplitudes": v, "success_probability": good_mass,
                       "conditional_good_probabilities": conditional})
        v = grover(v)
    assert states[0]["success_probability"] == F(1, 4)
    assert states[1]["amplitudes"] == (Qsqrt3(F(3, 5)), Qsqrt3(F(4, 5)), Qsqrt3())
    assert states[1]["success_probability"] == 1
    average_lower = F(1, 2) - F(1, 2 * 10)
    mixed_lower = F(1, 2) * average_lower
    large_p_lower = F(1, 2) * F(1, 2)
    assert average_lower == F(9, 20)
    assert mixed_lower == F(9, 40) <= large_p_lower
    assert 1 - mixed_lower == F(31, 40)
    return {"basis": ("g1", "g2", "b"), "initial_state": psi,
            "initial_good_outcome_probabilities": (F(9, 100), F(16, 100)),
            "initial_success_probability": F(1, 4),
            "one_iteration_good_multiplier": 3 - 4 * F(1, 4),
            "one_iteration_bad_multiplier": 1 - 4 * F(1, 4),
            "states": states,
            "bounded_trial_constant_arithmetic": {
                "assumed_product_M_times_sin_2theta_at_least": 10,
                "average_lower_bound_from_general_formula": average_lower,
                "mixed_trial_success_lower_bound": mixed_lower,
                "success_lower_bound_when_p_at_least_half": large_p_lower,
                "trial_failure_upper_bound": 1 - mixed_lower,
                "scope": "Checks the stated rational arithmetic; the general sine bound is a cited theorem."},
            "checked_by": "Full two-reflection calculation in Q(sqrt(3)); no floating point."}


def and_conditioning():
    inputs = tuple(product((0, 1), repeat=2))
    truth = lambda u: u[0] & u[1]
    scores = [sum(F(truth(u) == answer, 4) for u in inputs) for answer in (0, 1)]
    for q in (0, 1):
        for answers in product((0, 1), repeat=2):
            scores.append(sum(F(answers[u[q]] == truth(u), 4) for u in inputs))
    assert len(scores) == 10 and max(scores) == F(3, 4)
    runs = []
    for a, b in inputs:
        output = 0 if a == 0 else b
        queries = 1 if a == 0 else 2
        runs.append({"input": f"{a}{b}", "queries": queries, "output": output,
                     "correct": output == (a & b), "within_L_1": queries <= 1,
                     "capped_output": 0, "capped_correct": (a & b) == 0})
    nonheavy = sum(F(run["within_L_1"], 4) for run in runs)
    joint = sum(F(run["within_L_1"] and run["correct"], 4) for run in runs)
    capped = sum(F(run["capped_correct"], 4) for run in runs)
    assert nonheavy == joint == F(1, 2)
    assert capped == F(3, 4)

    # Exhaustively optimize all adaptive schedules on two independent copies,
    # with at most one query per copy on every branch. At a leaf, pick a most
    # likely answer vector. This includes stopping early and all allowed queries.
    all_inputs = tuple(product((0, 1), repeat=4))

    @lru_cache(maxsize=None)
    def optimum(observed, remaining):
        compatible = tuple(u for u in all_inputs if all(bit == -1 or bit == u[q]
                                                        for q, bit in enumerate(observed)))
        outputs = Counter((u[0] & u[1], u[2] & u[3]) for u in compatible)
        best = F(max(outputs.values()), len(compatible))
        for q in range(4):
            block = q // 2
            if remaining[block] == 0:
                continue
            next_budget = list(remaining)
            next_budget[block] -= 1
            value = F(0)
            for bit in (0, 1):
                count = sum(u[q] == bit for u in compatible)
                if not count:
                    continue
                next_observed = list(observed)
                next_observed[q] = bit
                value += F(count, len(compatible)) * optimum(tuple(next_observed), tuple(next_budget))
            best = max(best, value)
        return best

    two_copy_optimum = optimum((-1,) * 4, (1, 1))
    assert two_copy_optimum == F(9, 16)
    return {"distribution": "Uniform on 00,01,10,11; independent across copies.",
            "L": 1, "single_copy_optimum": max(scores), "one_query_trees_enumerated": len(scores),
            "runs": runs, "probability_within_cap": nonheavy,
            "probability_correct_and_within_cap": joint,
            "probability_correct_given_within_cap": joint / nonheavy,
            "capped_simulator_success": capped,
            "posterior_optimum_after_a_0": F(1), "posterior_optimum_after_a_1": F(1, 2),
            "two_copy_all_nonheavy_joint_success": joint ** 2,
            "two_copy_capped_simulator_success": capped ** 2,
            "two_copy_optimal_adaptive_success_with_separate_caps": two_copy_optimum}


def planted_board(zeros, address_instances, chosen):
    x = tuple("".join("0" if j == zeros[i - 1] else "1" for j in COLUMNS) for i in COLUMNS)
    dummy = blank_board(x, address_instances)
    planted = dummy.copy()
    planted[("X", chosen, zeros[chosen - 1])] = 1
    address = true_address(planted, chosen)
    assert address is not None
    pointers = tuple(None if j == chosen else zeros[j - 1] for j in COLUMNS)
    transcripts = tuple(gate_values(read_a(planted, chosen, h)) for h in (1, 2))
    fill_cell(planted, chosen, address, pointers, transcripts)
    return dummy, planted, address


def planted_example():
    zeros = (4, 1, 2, 3)
    address_instances = (((0, 0), (0, 0)),) * 4
    dummy, planted, address = planted_board(zeros, address_instances, 1)
    differences = [loc for loc in dummy if dummy[loc] != planted[loc]]
    assert len(differences) == 5
    assert winners(dummy) == [] and winners(planted) == [(1, "00")]
    assert cell_word(dummy, 1, "00") == "0000000000"
    assert cell_word(planted, 1, "00") == "0001101010"

    # Check every zero-location tuple, every planted column, and every possible
    # true address in the planted column. Other address instances are fixed 00.
    cases = 0
    for js in product(COLUMNS, repeat=4):
        for chosen in COLUMNS:
            for s in ADDRESSES:
                a = list(address_instances)
                a[chosen - 1] = tuple((0, int(bit)) for bit in s)
                y0, y1, actual = planted_board(js, tuple(a), chosen)
                assert actual == s
                assert winners(y0) == [] and winners(y1) == [(chosen, s)]
                for loc in y0:
                    if y0[loc] != y1[loc]:
                        assert loc == ("X", chosen, js[chosen - 1]) or (
                            loc[0] in ("P", "T") and loc[1:3] == (chosen, s))
                check_definition_and_tests(y1)
                cases += 1
    assert cases == 4096
    return {"scope": "A finite illustration of planting; this easy gadget distribution is not the hard distribution.",
            "zero_rows_J": zeros, "planted_column_I": 1, "true_address": address,
            "A": address_instances,
            "dummy_X": ["".join(str(read_x(dummy, i, j)) for j in COLUMNS) for i in COLUMNS],
            "planted_X": ["".join(str(read_x(planted, i, j)) for j in COLUMNS) for i in COLUMNS],
            "all_dummy_cells": "0000000000", "filled_cell": cell_word(planted, 1, "00"),
            "all_other_planted_cells": "0000000000", "dummy_winners": [], "planted_winners": [(1, "00")],
            "changed_physical_locations": differences, "changed_bit_count": len(differences),
            "all_zero_tuples_columns_and_target_addresses_checked": cases}


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def matvec(a, x):
    return tuple(dot(row, x) for row in a)


def forrelation_examples():
    W = ((1, 1, 1, 1), (1, -1, 1, -1), (1, 1, -1, -1), (1, -1, -1, 1))
    H = tuple(tuple(F(x, 2) for x in row) for row in W)
    assert tuple(tuple(dot(row, col) for col in zip(*H)) for row in H) == tuple(
        tuple(F(i == j) for j in range(4)) for i in range(4))
    v, z0 = (1, 1, 1, -1), (1, 1, -1, 1)
    assert matvec(H, v) == v
    delta = F(1, 1024)

    def evaluate(z1, z2):
        numerator = dot(z1, matvec(W, z2))
        assert numerator.denominator == 1
        signed_dot_product = dot(z1, matvec(H, z2))
        phi = signed_dot_product / 4
        assert phi == numerator / 8
        answer = 1 if phi >= delta else 0 if abs(phi) <= delta / 2 else None
        one = 2 ** 10 * numerator >= 8
        zero = 2 ** 11 * abs(numerator) <= 8
        domain, bit = int(one or zero), int(one)
        assert bool(domain) == (answer is not None)
        assert not domain or bit == answer
        return {"z1": z1, "z2": z2, "z1_transpose_H_z2": signed_dot_product,
                "N": numerator, "Phi": phi,
                "P": answer, "projection_probability": phi ** 2, "exact_circuit_d_b": (domain, bit)}

    names = {"one": evaluate(v, v), "zero": evaluate(z0, v),
             "undefined_negative": evaluate(tuple(-x for x in v), v)}
    assert tuple(names[name]["Phi"] for name in names) == (1, 0, -1)
    counts, histogram = Counter(), Counter()
    for z1, z2 in product(tuple(product((-1, 1), repeat=4)), repeat=2):
        row = evaluate(z1, z2)
        counts["undefined" if row["P"] is None else str(row["P"])] += 1
        histogram[str(row["Phi"])] += 1
    assert counts == {"1": 104, "0": 48, "undefined": 104}
    assert sum(counts.values()) == 256
    return {"m": 4, "k": 2, "H": H, "v": v, "H_v": matvec(H, v),
            "delta": delta, "delta_over_2": delta / 2, "denominator_M": 8,
            "named_instances": names, "all_256_pair_counts": dict(counts),
            "Phi_histogram": dict(sorted(histogram.items(), key=lambda pair: F(pair[0]))),
            "scope": "Exact circuit output bits checked; no claim of enumerating the full Forrelation circuit."}


def numeric_parameters():
    m, k, ell = 4, 2, 2
    r = 20 * ell
    T = (1000 * m - 1).bit_length()
    eps = F(1, 1000 * T)
    gamma = F(1, 2 * m)
    L = 2 // (ell * ell)
    assert (r, T, L) == (40, 12, 0)
    ideal_miss = F(2 * m, 2 ** T)
    total_error = ideal_miss + T * eps + eps
    assert total_error == F(583, 192000) < F(1, 3)
    assert T * eps == F(1, 1000)
    assert 1 - T * eps == F(999, 1000) > F(1, 2)
    assert ideal_miss <= F(1, 500)
    exponent_rows = []
    for k in (2, 3, 4, 5, 10, 20, 100):
        classical = 2 - F(1, k)
        separation = classical / F(1, 2)
        assert separation == 4 - F(2, k)
        exponent_rows.append({"fixed_k": k, "power_of_m_in_R_lower_bound": classical,
                              "power_of_m_in_Q_upper_bound": F(1, 2),
                              "separation_power_ignoring_logarithms": separation,
                              "gap_to_4": 4 - separation})
    cubic_ratio_exponents = {k: 2 - F(1, k) - F(3, 2) for k in (2, 3)}
    assert cubic_ratio_exponents == {2: F(0), 3: F(1, 6)}

    # Exact replacement for a decimal evaluation of log_2(3/2).
    assert F(2, 3) ** 2 == F(4, 9) < F(1, 2)
    assert F(4, 100) + F(1, 100) + F(1, 100) == F(3, 50) < F(1, 3)
    lower_examples = []
    for t in (1, 2, 4, 8):
        mm = 4 ** t
        rr = 40 * t
        answer_guess = F(2, 3) ** rr
        bound = F(1, mm ** 10)
        assert answer_guess <= bound
        lower_examples.append({"t": t, "m": mm, "r": rr,
                               "two_thirds_to_r": answer_guess, "m_to_minus_10": bound})
    # At t=8 and k=2 the floor defining L is exactly one. This is a numerical
    # feasibility check, not a verification that this m exceeds the unspecified
    # threshold in the Forrelation lower-bound theorem.
    t, mm, ll, rr = 8, 4 ** 8, 1, 320
    assert (2 ** t) // ((2 * t) ** 2) == ll
    G = mm * ll // 100
    discrepancy = F(4 * G, mm ** 2) + F(G, mm * ll) + G * F(2, 3) ** rr
    assert discrepancy < F(1, 3)
    return {
        "actual_family_at_k2_m4": {"m": m, "k": 2, "ell": ell, "r": r,
                                   "cells_per_column": 2 ** r, "all_cells": m * 2 ** r,
                                   "X_and_A_bits": m * (m + r * 2 * m),
                                   "cell_bits_symbolic": "6 + 40*S",
                                   "total_bits_symbolic": "1296 + 2^42*(6 + 40*S)",
                                   "K_symbolic": "87 + 40*S", "L": L, "G": m * L // 100,
                                   "scope": "L=0 gives no nontrivial randomized lower bound at this size."},
        "tournament_at_m4": {"T": T, "epsilon": eps, "gamma": gamma,
                             "ideal_miss_upper_bound": ideal_miss, "T_times_epsilon": T * eps,
                             "unselected_winner_weight_lower_bound": 1 - T * eps,
                             "one_input_total_error_upper_bound": total_error,
                             "address_bit_error_target_at_r40": eps / r},
        "exponent_table": exponent_rows,
        "cubic_ratio_m_exponents_by_fixed_k": cubic_ratio_exponents,
        "lower_bound_constant_check": {"four_ninths_less_than_half": True,
                                      "uniform_coarse_discrepancy_upper_bound": F(3, 50),
                                      "exact_power_substitutions": lower_examples,
                                      "t8_k2_numeric_feasibility": {
                                          "m": mm, "r": rr, "L": ll, "G": G,
                                          "discrepancy": discrepancy,
                                          "disclaimer": "No hard-distribution or R(P)>L claim at this particular m."}},
    }


def encode(obj):
    if isinstance(obj, (F, Qsqrt3)):
        return str(obj)
    if isinstance(obj, dict):
        return {str(key): encode(value) for key, value in obj.items()}
    if isinstance(obj, (tuple, list)):
        return [encode(value) for value in obj]
    return obj


def exact_results():
    board, matrix = opening_board()
    return {"status": "All exact assertions passed.",
            "arithmetic": "Integers, Fraction, and Q(sqrt(3)); no floating-point assertions.",
            "opening_board": board,
            "tournaments": tournaments(matrix),
            "amplification": amplification(),
            "AND_conditioning": and_conditioning(),
            "planted_input": planted_example(),
            "Forrelation": forrelation_examples(),
            "parameters": numeric_parameters()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Also save the exact JSON output to this path.")
    args = parser.parse_args()
    text = json.dumps(encode(exact_results()), ensure_ascii=False, indent=2) + "\n"
    if args.output is not None:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
