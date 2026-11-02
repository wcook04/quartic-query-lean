"""Independent finite/arithmetic checks for the frozen baseline review.
These checks do not run Lean and do not prove an asymptotic query lower bound.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import json


def run():
    # Independently build the four-by-four Walsh matrix from binary parity.
    walsh = [[(-1) ** ((i & j).bit_count()) for j in range(4)] for i in range(4)]
    assert all(sum(walsh[i][b] * walsh[j][b] for b in range(4)) == (4 if i == j else 0)
               for i in range(4) for j in range(4))
    nums, classes = Counter(), Counter()
    delta = Fraction(1, 2 ** 10)
    for bits in product((0, 1), repeat=8):
        z = [1 - 2 * b for b in bits]
        numerator = sum(z[i] * walsh[i][j] * z[4+j] for i in range(4) for j in range(4))
        phi = Fraction(numerator, 8)
        nums[numerator] += 1
        classes['yes' if phi >= delta else 'no' if abs(phi) <= delta / 2 else 'undefined'] += 1
    assert dict(sorted(nums.items())) == {-8: 8, -4: 96, 0: 48, 4: 96, 8: 8}
    assert classes == {'yes': 104, 'no': 48, 'undefined': 104}
    negative = [-1, 1, 1, 1]
    nneg = sum(negative[i] * walsh[i][j] * negative[j] for i in range(4) for j in range(4))
    assert Fraction(nneg, 8) == -1
    # Exact exponent discrepancy; a fixed constant cannot absorb a positive
    # power of log(k*m) as m grows. This checks the display, not its theorem.
    k, level = 3, 6
    actual = Fraction(level - 1, 2)
    claimed = Fraction(level, 2) * (1 - Fraction(1, k))
    assert actual == Fraction(5, 2) and claimed == 2 and actual - claimed == Fraction(1, 2)
    # 1/35 <= (1 - 2*sqrt(2)/3)/2 iff 2 <= (99/70)^2.
    assert Fraction(2) < Fraction(99, 70) ** 2
    assert 35 ** 2 == 1225 and 35 ** 4 == 1500625
    assert 16 * 1225 == 19600
    # A finite witness for why merely returning successful labels does not
    # replace the exact conditional law in the tournament proof.
    # A permitted comparison table and unequal nonnegative weights. This is
    # an interface example, not a claim that this state occurs in a run.
    # A biased pivot choice can break expected-weight halving.
    weights = [Fraction(1), Fraction(1, 10), Fraction(1, 10)]
    comparison = [[Fraction(0), Fraction(1), Fraction(1)],
                  [Fraction(0), Fraction(0), Fraction(1, 2)],
                  [Fraction(0), Fraction(1, 2), Fraction(0)]]
    total = sum(weights)
    new_totals = [sum(weights[i] * comparison[i][p] for i in range(3)) for p in range(3)]
    weighted_mean = sum(weights[p] / total * new_totals[p] for p in range(3))
    identity = (total ** 2 - sum(w*w for w in weights)) / (2 * total)
    assert weighted_mean == identity <= total/2
    assert new_totals[1] > total/2
    return {
        'status': 'passed',
        'scope': 'Exact finite arithmetic and independently authored semantic examples; no Lean execution or asymptotic proof certification.',
        'forrelation_census': {'k': 2, 'm': 4, 'input_count': 256,
                              'numerator_multiplicities': dict(sorted(nums.items())),
                              'promise_classes': dict(classes), 'negative_witness_phi': '-1'},
        'bansal_sinha_display': {'k': k, 'level': level,
                                'actual_log_exponent': str(actual), 'claimed_log_exponent': str(claimed),
                                'ratio_log_exponent': str(actual-claimed),
                                'scope': 'Contradicts the displayed asymptotic comparison at this level, not Theorem 1.3.'},
        'adversary_constants': {'rational_coefficient': '1/35', 'rational_is_below_sharp_coefficient': True,
                               'square': 1225, 'fourth_power': 1500625, 'hybrid_product': 19600},
        'conditional_sampler_example': {'weights': list(map(str, weights)),
                                        'total_weight': str(total),
                                        'exact_weighted_pivot_mean': str(weighted_mean),
                                        'half_total_weight': str(total/2),
                                        'always_pivot_1_new_weight': str(new_totals[1]),
                                        'scope': 'Illustrates that success probability alone does not specify the pivot distribution.'}
    }

if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
