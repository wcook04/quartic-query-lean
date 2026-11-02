#!/usr/bin/env python3
"""Exact finite checks of the delicate mathematical statements in this return.

These are independent small examples, not Lean compilation or general proofs.
Run with Python 3.10+; no third-party packages are needed.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json


def conditional_value_enumeration():
    """Exhaust the indicated finite test domain for display (16).

    The Bellman recursion is evaluated independently with exact rationals.
    This is a finite calculation, not a proof for arbitrary inputs or budgets.
    """
    inputs = tuple(product((0, 1), repeat=2))

    def restricted(weights, query, answer):
        return tuple(w if x[query] == answer else 0 for x, w in zip(inputs, weights))

    @lru_cache(None)
    def value(outputs, budget, weights):
        candidates = [sum(w for w, output in zip(weights, outputs) if output == answer)
                      for answer in (0, 1)]
        if budget:
            candidates += [sum(value(outputs, budget-1, restricted(weights, q, b))
                               for b in (0, 1)) for q in (0, 1)]
        return max(candidates)

    checks = zeros = 0
    for outputs in product((0, 1), repeat=4):
        for weights in product((0, 1, 2), repeat=4):
            mass = sum(weights)
            for budget_after_query in range(3):
                for q in (0, 1):
                    left = F(0)
                    for b in (0, 1):
                        branch = restricted(weights, q, b)
                        branch_mass = sum(branch)
                        if branch_mass == 0:
                            zeros += 1
                        probability = F(branch_mass, mass) if mass else F(0)
                        optimum = F(value(outputs, budget_after_query, branch), branch_mass) if branch_mass else F(0)
                        left += probability * optimum
                    right = F(value(outputs, budget_after_query+1, weights), mass) if mass else F(0)
                    assert left <= right
                    checks += 1
    assert checks == 7776 and zeros == 1728
    return {'functions': 16, 'weight_vectors': 81, 'budgets_after_query': [0, 1, 2],
            'checks': checks, 'zero_mass_branch_encounters': zeros, 'failures': 0}


def adaptive_transcript_product():
    """The same observed transcript has a product posterior, even with repeats."""
    blocks = tuple(product((0, 1), repeat=2))
    prior0 = {blocks[0]: F(1, 3), blocks[1]: F(1, 6), blocks[2]: F(0), blocks[3]: F(1, 2)}
    prior1 = {x: F(1, 4) for x in blocks}
    groups = defaultdict(dict)
    for u, v in product(blocks, repeat=2):
        weight = prior0[u] * prior1[v]
        obs = []
        groups[tuple(obs)][u, v] = weight
        obs.append(((0, 0), u[0]))
        groups[tuple(obs)][u, v] = weight
        query = (1, 1) if u[0] == 0 else (0, 0)
        answer = (u, v)[query[0]][query[1]]
        obs.append((query, answer))
        groups[tuple(obs)][u, v] = weight
    checked = 0
    for tau, outcomes in groups.items():
        mass = sum(outcomes.values(), F(0))
        if not mass:
            continue
        marginal0 = {x: sum((w for (u, v), w in outcomes.items() if u == x), F(0)) / mass for x in blocks}
        marginal1 = {x: sum((w for (u, v), w in outcomes.items() if v == x), F(0)) / mass for x in blocks}
        for u, v in product(blocks, repeat=2):
            assert outcomes.get((u, v), F(0)) / mass == marginal0[u] * marginal1[v]
        checked += 1
    # Repeating the same queried bit gives a probability-zero incompatible branch.
    assert not any(tau == (((0, 0), 1), ((0, 0), 0)) for tau in groups)
    return {"positive_transcript_fibers": checked, "all_posteriors_factor": True,
            "incompatible_repeat_has_zero_mass": True}


def conditioning_counterexample():
    """AND_2: stopping after the first zero selects an easy conditional law."""
    inputs = tuple(product((0, 1), repeat=2))
    one_query_success = max(
        sum(max(sum(1 for x in inputs if x[q] == b and (x[0] & x[1]) == answer)
                for answer in (0, 1)) for b in (0, 1))
        for q in (0, 1))
    beta = F(one_query_success, len(inputs))
    nonheavy = [x for x in inputs if x[0] == 0]
    conditional_success = F(sum((x[0] & x[1]) == 0 for x in nonheavy), len(nonheavy))
    joint_success = F(sum(x[0] == 0 and (x[0] & x[1]) == 0 for x in inputs), len(inputs))
    assert beta == F(3, 4)
    assert conditional_success == 1 > beta
    assert joint_success == F(1, 2) <= beta
    return {"single_instance_one_query_optimum": str(beta),
            "conditional_success_given_nonheavy": str(conditional_success),
            "joint_nonheavy_and_correct": str(joint_success)}


def cap_counterexample():
    """A total budget rL does not imply a separate cap L on each input."""
    worlds = tuple(product((0, 1), repeat=4))
    def label(x):
        return (x[0] & x[1], x[2] & x[3])
    def optimal_stop(xs):
        return max(sum(label(x) == ans for x in xs) for ans in product((0, 1), repeat=2))
    def optimum(xs, remaining):
        best = optimal_stop(xs)
        for q in range(4):
            h = q // 2
            if remaining[h]:
                nxt = list(remaining)
                nxt[h] -= 1
                score = sum(optimum(tuple(x for x in xs if x[q] == b), tuple(nxt))
                            if any(x[q] == b for x in xs) else 0 for b in (0, 1))
                best = max(best, score)
        return best
    capped = F(optimum(worlds, (1, 1)), len(worlds))
    # Query the first AND completely, then always guess false for the other.
    concentrated = F(sum(label(x)[1] == 0 for x in worlds), len(worlds))
    assert capped == F(9, 16) == F(3, 4) ** 2
    assert concentrated == F(3, 4) > capped
    return {"per_instance_cap_success": str(capped),
            "same_total_budget_concentrated_success": str(concentrated)}


def hidden_zero_posterior():
    """Actual adaptive query histories with an independent side-information bit."""
    m = 4
    groups = defaultdict(list)
    for zeros in product(range(m), repeat=m):
        for advice in (0, 1):
            trace = []
            groups[tuple(trace)].append((zeros, advice))
            trace.append((("A", 0, 0), advice))
            groups[tuple(trace)].append((zeros, advice))
            col = advice
            for step in range(3):
                # A zero changes the next column; otherwise search the next row.
                row = step
                answer = int(zeros[col] != row)
                trace.append((("X", col, row), answer))
                groups[tuple(trace)].append((zeros, advice))
                if answer == 0:
                    col = (col + 1) % m
    checked = 0
    for trace, outcomes in groups.items():
        for col in range(m):
            seen = [(q[2], b) for q, b in trace if q[0] == "X" and q[1] == col]
            if any(b == 0 for row, b in seen):
                continue
            unqueried = set(range(m)) - {row for row, b in seen}
            assert unqueried
            for row in range(m):
                actual = F(sum(zeros[col] == row for zeros, advice in outcomes), len(outcomes))
                expected = F(1, len(unqueried)) if row in unqueried else F(0)
                assert actual == expected
            checked += 1
    return {"undiscovered_column_transcript_pairs": checked,
            "posterior_uniform_on_unqueried_positions": True}


def finite_numerics():
    base = 16 * F(2, 3) ** 40
    assert 0 < base < 1
    tests = 0
    for t in range(13):
        m = 4 ** t
        for L in sorted({1, max(1, m // 2), m}):
            G = m * L // 100
            first, second, third = F(4 * G, m * m), F(G, m * L), G * F(2, 3) ** (40 * t)
            assert first <= F(4, 100)
            assert second <= F(1, 100)
            assert third <= F(1, 100)
            assert third <= F(1, 100) * base ** t
            assert first + second + third <= F(6, 100) < F(1, 3)
            tests += 1
    floors = 0
    for k in range(2, 13):
        for t in range(8, 49):
            if 2 * t % k:
                continue
            m = 4 ** t
            L = 2 ** (2 * t - 2 * t // k) // (2 * t) ** 2
            G = m * L // 100
            lower = F(2 ** (4 * t - 2 * t // k), 400 * (2 * t) ** 2)
            assert lower <= G + 1
            floors += 1
    return {"budget_cases": tests, "integer_power_floor_cases": floors,
            "exact_geometric_base": str(base), "geometric_base_between_zero_and_one": True}


def main():
    result = {"status": "passed", "arithmetic": "fractions.Fraction; exact integers and rationals",
              "scope": "Finite mathematical examples only; not Lean elaboration or a proof of all cases.",
              "conditional_value_inequality": conditional_value_enumeration(),
              "adaptive_product_law": adaptive_transcript_product(),
              "conditioning_negative_control": conditioning_counterexample(),
              "per_instance_cap_negative_control": cap_counterexample(),
              "hidden_zero_posterior": hidden_zero_posterior(),
              "numerics": finite_numerics()}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
