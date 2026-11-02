#!/usr/bin/env python3
"""Check independently specified finite examples and deliberately bad models.

This program uses small Python models. It neither reads nor executes Lean,
compares the Lean source to these models, nor runs Comparator. A passing result
is an exact finite check and a mutation demonstration, not a proof receipt.
"""

from fractions import Fraction
from itertools import product
import json


TWO_THIRDS = Fraction(2, 3)


def constant_mixture_succeeds(labels, threshold):
    """Can a single input-independent mixture of constant answers meet the bound?"""
    # p is the probability of answering true. Every promised true input gives
    # p >= threshold; every promised false input gives p <= 1 - threshold.
    lower, upper = Fraction(0), Fraction(1)
    for label in labels:
        if label is True:
            lower = max(lower, threshold)
        elif label is False:
            upper = min(upper, 1 - threshold)
        elif label is not None:
            raise ValueError("labels must be True, False, or None")
    return lower <= upper


def input_dependent_constant_succeeds(labels, threshold):
    """The intentionally incorrect model may choose different coins per input."""
    return all(constant_mixture_succeeds([label], threshold) for label in labels)


def or_two_mixture_successes():
    """Success of the equal mixture of true, first-bit and second-bit trees."""
    out = {}
    for x, y in product((False, True), repeat=2):
        answers = (True, x, y)
        target = x or y
        out[f"{int(x)}{int(y)}"] = Fraction(sum(a == target for a in answers), 3)
    return out


def phi_two_four(first, second):
    """Compute two-layer Forrelation on four signs via a normalized Walsh matrix."""
    if len(first) != 4 or len(second) != 4 or any(s not in (-1, 1) for s in (*first, *second)):
        raise ValueError("expected two length-four sign vectors")
    total = sum(first[i] * (-1 if (i & j).bit_count() % 2 else 1) * second[j]
                for i, j in product(range(4), repeat=2))
    return Fraction(total, 8)


def promise_value(phi, *, absolute_high=False):
    """Classify a two-layer example with delta = 2^(-5k), k = 2."""
    delta = Fraction(1, 1024)
    high = abs(phi) if absolute_high else phi
    if high >= delta:
        return True
    if abs(phi) <= delta / 2:
        return False
    return None


def comparison_truth_table(*, impossible=False):
    """Evaluate two-candidate comparisons with zero diagonal and 0/1 entries."""
    return tuple(a + b == 1 and not impossible for a, b in product((0, 1), repeat=2))


# These answers are authored independently of the model functions above. They
# are deliberately concrete; no Lean declaration is inferred from them.
EXPECTED = {
    "identity_zero_query": False,
    "one_label_promise_zero_query": True,
    "worst_case_cap": 2,
    "or_two_inclusive_mixture": True,
    "negative_forrelation_value": "-1",
    "negative_forrelation_promise": None,
    "comparison_has_witness": True,
}

# Each named mutant must change exactly its named independently expected answer.
MUTATIONS = {
    "algorithm_per_input": "identity_zero_query",
    "half_success_threshold": "identity_zero_query",
    "off_promise_false": "one_label_promise_zero_query",
    "minimum_branch_cap": "worst_case_cap",
    "strict_success_threshold": "or_two_inclusive_mixture",
    "absolute_high_promise": "negative_forrelation_promise",
    "shared_impossible_comparison": "comparison_has_witness",
}


def observe(mutation=None):
    if mutation is not None and mutation not in MUTATIONS:
        raise ValueError(f"unknown mutation: {mutation}")
    identity = (False, True)
    promise = (None, True)
    threshold = Fraction(1, 2) if mutation == "half_success_threshold" else TWO_THIRDS
    identity_check = (input_dependent_constant_succeeds if mutation == "algorithm_per_input"
                      else constant_mixture_succeeds)
    if mutation == "off_promise_false":
        promise = tuple(False if label is None else label for label in promise)
    successes = or_two_mixture_successes()
    if mutation == "strict_success_threshold":
        or_ok = all(p > TWO_THIRDS for p in successes.values())
    else:
        or_ok = all(p >= TWO_THIRDS for p in successes.values())
    phi = phi_two_four((-1, 1, 1, 1), (-1, 1, 1, 1))
    return {
        "identity_zero_query": identity_check(identity, threshold),
        "one_label_promise_zero_query": constant_mixture_succeeds(promise, TWO_THIRDS),
        "worst_case_cap": (min if mutation == "minimum_branch_cap" else max)(0, 2),
        "or_two_inclusive_mixture": or_ok,
        "negative_forrelation_value": str(phi),
        "negative_forrelation_promise": promise_value(
            phi, absolute_high=mutation == "absolute_high_promise"),
        "comparison_has_witness": any(comparison_truth_table(
            impossible=mutation == "shared_impossible_comparison")),
    }


def mismatches(observed):
    return [name for name, expected in EXPECTED.items() if observed[name] != expected]


def report():
    baseline = observe()
    mutations = {name: mismatches(observe(name)) for name in MUTATIONS}
    # Both toy specifications use the same impossible premise. This is finite
    # truth-table agreement only; it is not a Comparator execution or prediction.
    toy_challenge = comparison_truth_table(impossible=True)
    toy_solution = comparison_truth_table(impossible=True)
    return {
        "scope": "independent finite Python models; no Lean source comparison or Comparator run",
        "expected": EXPECTED,
        "observed": baseline,
        "baseline_mismatches": mismatches(baseline),
        "mutations_detected": mutations,
        "toy_shared_bad_spec": {
            "finite_truth_tables_agree": toy_challenge == toy_solution,
            "has_valid_comparison": any(toy_challenge),
            "comparator_executed": False,
        },
    }


def main():
    result = report()
    print(json.dumps(result, indent=2, sort_keys=True))
    return int(bool(result["baseline_mismatches"]) or any(
        result["mutations_detected"][mutation] != [case]
        for mutation, case in MUTATIONS.items()))


if __name__ == "__main__":
    raise SystemExit(main())
