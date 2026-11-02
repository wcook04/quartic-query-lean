#!/usr/bin/env python3
"""Exact tiny-model checks for the round-three models section.

Only Python's standard library is used. This independently written program does
not import, parse, execute, or compare Lean code, and is not a kernel receipt.
The general lower bounds in section.md §2.6 are ordinary proofs; exhaustive
enumeration here is confined to depth at most one on two coordinates.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import json


@dataclass(frozen=True)
class Leaf:
    answer: int


@dataclass(frozen=True)
class Query:
    index: int
    zero: object
    one: object


def evaluate(tree, bits):
    if isinstance(tree, Leaf):
        return tree.answer
    return evaluate(tree.one if bits[tree.index] else tree.zero, bits)


def depth(tree):
    if isinstance(tree, Leaf):
        return 0
    return 1 + max(depth(tree.zero), depth(tree.one))


def probabilities(mixture, bits):
    assert mixture and all(weight > 0 for weight, _ in mixture)
    assert sum((weight for weight, _ in mixture), F(0)) == 1
    return tuple(sum((weight for weight, tree in mixture
                      if evaluate(tree, bits) == answer), F(0))
                 for answer in (0, 1))


def cap(mixture):
    return max(depth(tree) for _, tree in mixture)


def zero_query_interval(labels, threshold=F(2, 3)):
    """Allowed p=Pr[output 1]; None imposes no requirement."""
    lower, upper = F(0), F(1)
    for label in labels:
        if label == 0:
            upper = min(upper, 1 - threshold)
        elif label == 1:
            lower = max(lower, threshold)
        else:
            assert label is None
    return lower, upper


def all_depth_one_trees(coordinates):
    leaves = (Leaf(0), Leaf(1))
    return leaves + tuple(Query(i, left, right)
                          for i, left, right in product(coordinates, leaves, leaves))


def walsh_four():
    return tuple(tuple((-1) ** ((i & j).bit_count()) for j in range(4))
                 for i in range(4))


def phi_two_four(first, second):
    matrix = walsh_four()
    return F(sum(first[i] * matrix[i][j] * second[j]
                 for i, j in product(range(4), repeat=2)), 8)


def forrelation_label(phi):
    delta = F(1, 1024)
    if phi >= delta:
        return 1
    if abs(phi) <= delta / 2:
        return 0
    return None


def parity_tree(n, index=0, accumulated=0):
    if index == n:
        return Leaf(accumulated)
    return Query(index, parity_tree(n, index + 1, accumulated),
                 parity_tree(n, index + 1, accumulated ^ 1))


def main():
    inputs = tuple(product((0, 1), repeat=2))
    c0, c1 = Leaf(0), Leaf(1)
    x0, x1 = Query(0, c0, c1), Query(1, c0, c1)
    or_mixture = ((F(1, 3), c1), (F(1, 3), x0), (F(1, 3), x1))
    or_success = tuple(probabilities(or_mixture, x)[int(any(x))] for x in inputs)
    assert or_success == (F(2, 3), F(2, 3), F(2, 3), F(1))
    assert cap(or_mixture) == 1
    assert sum(weight * depth(tree) for weight, tree in or_mixture) == F(2, 3)
    trees = all_depth_one_trees(range(2))
    tables = {tuple(evaluate(tree, x) for x in inputs) for tree in trees}
    assert len(trees) == 10 and len(tables) == 6
    or_table = tuple(int(any(x)) for x in inputs)
    xor_table = tuple(x[0] ^ x[1] for x in inputs)
    assert or_table not in tables and xor_table not in tables
    hard_means = tuple(F(sum(evaluate(tree, x) == int(any(x))
                            for x in inputs[:3]), 3) for tree in trees)
    assert max(hard_means) == F(2, 3)
    optimal_tables = {tuple(evaluate(tree, x) for x in inputs)
                      for tree, mean in zip(trees, hard_means) if mean == F(2, 3)}
    assert optimal_tables == {(1, 1, 1, 1), (0, 0, 1, 1), (0, 1, 0, 1)}
    xor_means = {F(sum(evaluate(tree, x) == (x[0] ^ x[1]) for x in inputs), 4)
                 for tree in trees}
    assert xor_means == {F(1, 2)}
    identity_interval = zero_query_interval((0, 1))
    partial_interval = zero_query_interval((None, 1))
    empty_interval = zero_query_interval((None, None))
    assert identity_interval == (F(2, 3), F(1, 3))
    assert partial_interval == (F(2, 3), F(1))
    assert empty_interval == (F(0), F(1))
    identity = Query(0, c0, c1)
    assert [evaluate(identity, (x,)) for x in (0, 1)] == [0, 1]
    assert depth(identity) == 1
    off_promise_constant = ((F(1), c1),)
    assert cap(off_promise_constant) == 0
    assert [probabilities(off_promise_constant, (x,))[1] for x in (0, 1)] == [F(1), F(1)]
    # A positive-probability deep branch remains charged in full.
    depth_two = Query(0, Query(1, c0, c1), c1)
    rare_deep = ((F(99, 100), c0), (F(1, 100), depth_two))
    assert cap(rare_deep) == 2
    assert sum(weight * depth(tree) for weight, tree in rare_deep) == F(1, 50)
    # These exact signs are independent expected yes/no/off-promise examples.
    v = (-1, 1, 1, 1)
    negative = phi_two_four(v, v)
    positive = phi_two_four(tuple(-a for a in v), v)
    zero = phi_two_four((1, 1, 1, -1), v)
    assert (negative, zero, positive) == (F(-1), F(0), F(1))
    assert (forrelation_label(negative), forrelation_label(zero),
            forrelation_label(positive)) == (None, 0, 1)
    # The expected-query example reads all n bits with probability 1/3 and
    # otherwise uses one of the two constants with probability 1/3 each.
    # It succeeds with probability 2/3 and has cap n, expected cost n/3.
    parity_expected = {}
    for n in range(1, 7):
        mixture = ((F(1, 3), parity_tree(n)), (F(1, 3), c0), (F(1, 3), c1))
        successes = {probabilities(mixture, bits)[sum(bits) % 2]
                     for bits in product((0, 1), repeat=n)}
        expected_queries = sum(weight * depth(tree) for weight, tree in mixture)
        assert successes == {F(2, 3)} and cap(mixture) == n
        assert expected_queries == F(n, 3)
        parity_expected[str(n)] = {"success": str(F(2, 3)), "hard_cap": n,
                                   "expected_queries": str(expected_queries)}
    output = {
        "evidence_kind": "exact rational finite Python checks; no Lean or Comparator execution",
        "input_order": ["".join(map(str, x)) for x in inputs],
        "identity_zero_query_p_interval": list(map(str, identity_interval)),
        "identity_zero_query_feasible": identity_interval[0] <= identity_interval[1],
        "identity_one_query_exact": True,
        "or2_success": list(map(str, or_success)),
        "or2_cap": cap(or_mixture),
        "or2_expected_queries_of_this_mixture": "2/3",
        "depth_one_syntactic_trees": len(trees),
        "depth_one_distinct_truth_tables": len(tables),
        "or2_max_success_on_uniform_00_01_10": str(max(hard_means)),
        "or2_optimal_truth_tables": sorted(optimal_tables),
        "or2_strictly_above_two_thirds_with_one_query": False,
        "xor2_uniform_depth_one_success": [str(x) for x in sorted(xor_means)],
        "off_promise_one_label_zero_query_p_interval": list(map(str, partial_interval)),
        "off_promise_constant_output": 1,
        "off_promise_constant_cap": 0,
        "empty_promise_zero_query_p_interval": list(map(str, empty_interval)),
        "rare_deep_program": {"hard_cap": 2, "weighted_depth": "1/50"},
        "forrelation_k2_m4": {
            "delta": "1/1024", "delta_over_two": "1/2048",
            "first_negative": v, "first_zero": (1, 1, 1, -1),
            "first_positive": tuple(-a for a in v), "second": v,
            "phi": [str(negative), str(zero), str(positive)],
            "labels": [None, 0, 1],
        },
        "expected_query_parity_example": parity_expected,
        "all_assertions_passed": True,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
