#!/usr/bin/env python3
"""Exact finite checks for the capped direct-product worked example.

No floating-point arithmetic, packages, randomness, or external files are used.
This independently evaluates finite trees; it does not invoke the supplied Lean
definitions or certify the general theorem or its formalization.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import product
import json


BITS = tuple(product((0, 1), repeat=2))
PAIRS = tuple(product(BITS, repeat=2))
ANSWERS = BITS


def f(x):
    return x[0] & x[1]


def leaf(answer):
    return ("leaf", tuple(answer))


def query(h, q, left, right):
    return ("query", h, q, left, right)


def run(tree, inputs):
    counts = [0, 0]
    transcript = []
    while tree[0] == "query":
        _, h, q, left, right = tree
        b = inputs[h][q]
        counts[h] += 1
        transcript.append((h, q, b))
        tree = (left, right)[b]
    return tree[1], tuple(counts), tuple(transcript)


def correct(answer, inputs):
    return answer == tuple(map(f, inputs))


@lru_cache(None)
def capped_trees(caps):
    """All finite trees with the syntactic per-instance cap ``caps``."""
    trees = [leaf(answer) for answer in ANSWERS]
    for h, c in enumerate(caps):
        if not c:
            continue
        smaller = list(caps)
        smaller[h] -= 1
        children = capped_trees(tuple(smaller))
        for q, left, right in product(range(2), children, children):
            trees.append(query(h, q, left, right))
    return tuple(trees)


def single_input_optimum():
    """The two constants and eight one-query Boolean-output trees."""
    successes = [sum(b == f(x) for x in BITS) for b in (0, 1)]
    for q, on_zero, on_one in product(range(2), (0, 1), (0, 1)):
        successes.append(sum((on_zero, on_one)[x[q]] == f(x) for x in BITS))
    return len(successes), Fraction(max(successes), len(BITS))


def example_tree():
    """Query A0=a, then B_a=t; repeat A0 precisely when a != t."""
    stop = leaf((0, 0))
    repeat_a0 = query(0, 0, stop, stop)
    a0_branch = query(1, 0, stop, repeat_a0)
    a1_branch = query(1, 1, repeat_a0, stop)
    return query(0, 0, a0_branch, a1_branch)


def ratio(numerator, denominator):
    return str(Fraction(numerator, denominator))


def main():
    single_count, beta = single_input_optimum()
    assert single_count == 10 and beta == Fraction(3, 4)
    tree = example_tree()
    rows = [(inputs, *run(tree, inputs)) for inputs in PAIRS]
    cap = lambda counts: all(c <= 1 for c in counts)
    cap_rows = [row for row in rows if cap(row[2])]
    success_rows = [row for row in rows if correct(row[1], row[0])]
    joint_rows = [row for row in cap_rows if correct(row[1], row[0])]

    summaries = []
    for a, t in product((0, 1), repeat=2):
        selected = [row for row in rows if row[3][0][2] == a and row[3][1][2] == t]
        assert len(selected) == 4
        # Explicitly check the transcript rectangle and conditional product law.
        left_inputs = tuple(x for x in BITS if x[0] == a)
        right_inputs = tuple(y for y in BITS if y[a] == t)
        assert {row[0] for row in selected} == set(product(left_inputs, right_inputs))
        for x, y in PAIRS:
            conditional_joint = Fraction(sum(row[0] == (x, y) for row in selected), len(selected))
            conditional_product = Fraction(x in left_inputs, len(left_inputs)) * Fraction(y in right_inputs, len(right_inputs))
            assert conditional_joint == conditional_product
        successful = sum(correct(row[1], row[0]) for row in selected)
        v_a = Fraction(1) if a == 0 else Fraction(1, 2)
        v_b = Fraction(1) if t == 0 else Fraction(1, 2)
        assert Fraction(successful, len(selected)) == v_a * v_b
        assert all(cap(row[2]) == (a == t) for row in selected)
        if a != t:
            assert all(row[2] == (2, 1) for row in selected)
            assert all(row[3][2] == (0, 0, a) for row in selected)
            assert not any(row[3][2] == (0, 0, 1 - a) for row in selected)
        summaries.append({
            "first_answer_a": a,
            "second_query": f"B[{a}]",
            "second_answer_t": t,
            "history_probability": "1/4",
            "conditional_success": str(v_a * v_b),
            "per_instance_counts": [1, 1] if a == t else [2, 1],
            "cap_respected": a == t,
            "joint_success_contribution": str(Fraction(1, 4) * v_a * v_b if a == t else Fraction(0)),
        })

    p_cap = Fraction(len(cap_rows), len(rows))
    p_success = Fraction(len(success_rows), len(rows))
    p_joint = Fraction(len(joint_rows), len(rows))
    p_conditional = Fraction(len(joint_rows), len(cap_rows))
    assert (p_cap, p_success, p_joint, p_conditional) == (
        Fraction(1, 2), Fraction(9, 16), Fraction(5, 16), Fraction(5, 8)
    )
    assert p_joint <= beta**2 < p_conditional

    # Conditioning on the cap event destroys independence of the two inputs.
    p_a0 = Fraction(sum(row[0][0][0] == 0 for row in cap_rows), len(cap_rows))
    p_b0 = Fraction(sum(row[0][1][0] == 0 for row in cap_rows), len(cap_rows))
    p_both0 = Fraction(sum(row[0][0][0] == 0 and row[0][1][0] == 0 for row in cap_rows), len(cap_rows))
    assert (p_a0, p_b0, p_both0) == (Fraction(1, 2), Fraction(3, 4), Fraction(1, 2))
    assert p_both0 != p_a0 * p_b0

    # A separate exhaustive optimization over all valid capped trees.
    trees = capped_trees((1, 1))
    assert len(trees) == 5188
    best = max(Fraction(sum(correct(run(t, inputs)[0], inputs) for inputs in PAIRS), len(PAIRS)) for t in trees)
    assert best == beta**2 == Fraction(9, 16)

    # A global budget rL=2 permits concentrating both queries on one input.
    stop = leaf((0, 0))
    global_budget_tree = query(0, 0, stop, query(0, 1, stop, leaf((1, 0))))
    assert all(sum(run(global_budget_tree, inputs)[1]) <= 2 for inputs in PAIRS)
    global_success = Fraction(sum(correct(run(global_budget_tree, inputs)[0], inputs) for inputs in PAIRS), len(PAIRS))
    assert global_success == Fraction(3, 4) > beta**2

    print(json.dumps({
        "arithmetic": "fractions.Fraction (exact rational)",
        "input_law": "Two independent uniformly distributed pairs of Boolean bits",
        "function": "f(x0,x1) = x0 AND x1",
        "per_instance_cap": 1,
        "single_input_trees_checked": single_count,
        "single_input_optimum_beta": str(beta),
        "joint_inputs_checked": len(PAIRS),
        "capped_two_input_trees_checked": len(trees),
        "capped_two_input_optimum": str(best),
        "beta_squared": str(beta**2),
        "transcript_rectangle_and_conditional_product_checks": "passed for every input and all four positive two-query histories",
        "impossible_opposite_repeat_answers": "both have zero mass",
        "history_rows": summaries,
        "probability_all_correct": str(p_success),
        "probability_cap_respected": str(p_cap),
        "probability_all_correct_and_cap_respected": str(p_joint),
        "probability_all_correct_given_cap_respected": str(p_conditional),
        "conditional_dependence_witness": {
            "Pr[A0=0|E]": str(p_a0),
            "Pr[B0=0|E]": str(p_b0),
            "Pr[A0=B0=0|E]": str(p_both0),
            "product_of_conditional_marginals": str(p_a0 * p_b0),
        },
        "global_budget_rL_counterexample": {
            "total_query_cap": 2,
            "strategy": "Compute P(A) exactly, output 0 for P(B)",
            "success": str(global_success),
            "strictly_larger_than_beta_squared": True,
        },
        "scope": "Finite semantic check of this example only; no general proof or Lean-build claim",
        "all_assertions_passed": True,
    }, indent=2))


if __name__ == "__main__":
    main()
