"""Independent, finite semantic probes for the quartic statement audit.

No packet code is imported.  Forrelation uses a hand-written 4-by-4 Walsh
matrix and exact rational arithmetic.  The toy addressed function uses two
columns, one address bit and a two-gate circuit (domain=True, value=input).
These are executable mathematical checks, not Lean checks.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


W = (
    (1, 1, 1, 1),
    (1, -1, 1, -1),
    (1, 1, -1, -1),
    (1, -1, -1, 1),
)


def phi(a, b):
    return Fraction(sum(a[i] * W[i][j] * b[j] for i in range(4) for j in range(4)), 8)


def promise(v):
    if v >= Fraction(1, 1024):
        return "true"
    if abs(v) <= Fraction(1, 2048):
        return "false"
    return "none"


def bit(word, j):
    return bool((word >> j) & 1)


# Four X bits, two A bits, four pointer bits, then eight transcript bits.
def xbit(word, i, row):
    return bit(word, 2 * i + row)


def abit(word, i):
    return bit(word, 4 + i)


def pbit(word, i, s):
    return int(bit(word, 6 + 2 * i + int(s)))


def trbit(word, i, s, gate):
    return bit(word, 10 + 4 * i + 2 * int(s) + gate)


def winner_direct(word, i):
    """Definition in the paper's words; the input bit determines the address."""
    s = abit(word, i)
    return (
        xbit(word, i, 0)
        and xbit(word, i, 1)
        and trbit(word, i, s, 0)
        and trbit(word, i, s, 1) == s
        and not xbit(word, 1 - i, pbit(word, i, s))
    )


def passes_local_tests(word, i, s):
    """Circuit-local formulation: two consistency tests plus output tests."""
    tr = (trbit(word, i, s, 0), trbit(word, i, s, 1))
    consistency = tr[0] is True and tr[1] == abit(word, i)
    outputs = tr[0] is True and tr[1] == s
    return (
        all(xbit(word, i, j) for j in range(2))
        and consistency
        and outputs
        and not xbit(word, 1 - i, pbit(word, i, s))
    )


def f(word):
    return any(winner_direct(word, i) for i in range(2))


signs = list(product((-1, 1), repeat=4))
values = Counter(phi(a, b) for a in signs for b in signs)
census = Counter(promise(v) for a in signs for b in signs for v in [phi(a, b)])
assert census == {"true": 104, "false": 48, "none": 104}
positive = ((1, 1, 1, -1), (1, 1, 1, -1))
zero = ((1, 1, -1, 1), (1, 1, 1, -1))
negative = ((-1, 1, 1, 1), (-1, 1, 1, 1))
assert phi(*positive) == 1 and promise(phi(*positive)) == "true"
assert phi(*zero) == 0 and promise(phi(*zero)) == "false"
assert phi(*negative) == -1 and promise(phi(*negative)) == "none"


def walsh_transform_integer(v):
    """Unnormalized Walsh transform by direct matrix multiplication."""
    return [sum((-1 if (i & j).bit_count() % 2 else 1) * v[j] for j in range(len(v))) for i in range(len(v))]


general_witness_checks = []
for t in range(1, 4):
    m = 4**t
    sqrt_m = 2**t
    bent = [(-1) ** sum(((x >> (2 * j)) & 1) * ((x >> (2 * j + 1)) & 1) for j in range(t)) for x in range(m)]
    chi = [(-1) ** (x & 1) for x in range(m)]
    assert walsh_transform_integer(bent) == [sqrt_m * v for v in bent]
    assert sum(chi) == 0
    for k in range(2, 9):
        end = bent if k % 2 == 0 else [1] * m
        transformed_end = list(end)
        for _ in range(k - 1):
            transformed_end = walsh_transform_integer(transformed_end)
        endpoints = [end, [a * c for a, c in zip(end, chi)], [-a for a in end]]
        outputs = [Fraction(sum(a * v for a, v in zip(first, transformed_end)), m * sqrt_m ** (k - 1)) for first in endpoints]
        assert outputs == [1, 0, -1]
        general_witness_checks.append({"k": k, "t": t, "phi_values": list(map(str, outputs))})

accepted = 0
winning_columns = [0, 0]
for word in range(1 << 18):
    winners = [i for i in range(2) if winner_direct(word, i)]
    assert len(winners) <= 1
    local = [(i, s) for i in range(2) for s in (False, True) if passes_local_tests(word, i, s)]
    assert len(local) == len(winners)
    assert bool(local) == bool(winners)
    if winners:
        assert local == [(winners[0], abit(word, winners[0]))]
        accepted += 1
        winning_columns[winners[0]] += 1
assert accepted == (1 << 18) // 16 == 16384
assert winning_columns == [8192, 8192]

# X_0=(1,1), X_1=(0,1), A_0=1, A_1=0; pointer=0 at every cell;
# the active cell B_(0,1) has transcript (1,1); other cell bits are zero.
base = sum(1 << j for j in (0, 1, 3, 4, 12, 13))
assert f(base)
mutations = {
    "winner_own_X_bit": 0,
    "winner_address_input": 4,
    "winner_active_pointer": 7,
    "winner_domain_gate": 12,
    "winner_value_gate": 13,
}
mutation_results = {name: f(base ^ (1 << j)) for name, j in mutations.items()}
assert not any(mutation_results.values())
inactive_mutations = {
    "inactive_address_pointer": 6,
    "inactive_address_domain_gate": 10,
    "inactive_address_value_gate": 11,
    "other_column_address_input": 5,
    "other_column_cell_bit": 14,
}
inactive_results = {name: f(base ^ (1 << j)) for name, j in inactive_mutations.items()}
assert all(inactive_results.values())

report = {
    "status": "passed",
    "verification_kind": "independent exact finite Python probes; no Lean run",
    "forrelation": {
        "k": 2,
        "t": 1,
        "m": 4,
        "inputs": 256,
        "phi_histogram": {str(k): v for k, v in sorted(values.items())},
        "promise_census": dict(census),
        "named_witnesses": {
            "positive": {"signs": positive, "phi": "1", "P": "some true"},
            "zero": {"signs": zero, "phi": "0", "P": "some false"},
            "negative": {"signs": negative, "phi": "-1", "P": "none"},
        },
        "general_witness_finite_checks": general_witness_checks,
    },
    "toy_addressed_function": {
        "ell": 1,
        "r": 1,
        "base_function": "identity on one bit",
        "circuit_gates": ["constant true", "input bit"],
        "domain_out": 0,
        "value_out": 1,
        "input_bits": 18,
        "inputs_enumerated": 1 << 18,
        "accepted": accepted,
        "accepted_by_winning_column": winning_columns,
        "expected_count_derivation": "Each column wins with probability (1/4)*(1/4)*(1/2)=1/32. The winning-column events are disjoint; total fraction is 1/16.",
        "local_test_equivalence": "all 262144 inputs",
        "winner_uniqueness": "all 262144 inputs",
        "base_word": base,
        "active_mutation_outputs": mutation_results,
        "irrelevant_mutation_outputs": inactive_results,
    },
}
out = Path(__file__).with_name("construction_checks_output.json")
out.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
