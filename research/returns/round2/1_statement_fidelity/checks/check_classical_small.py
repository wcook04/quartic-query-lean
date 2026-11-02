"""Independent rational certificates for the proposed tiny classical tests.

This does not execute any supplied script and does not constitute a Lean proof.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

inputs = list(product((False, True), repeat=2))
leaf0 = tuple(False for _ in inputs)
leaf1 = tuple(True for _ in inputs)
query0 = tuple(x[0] for x in inputs)
query1 = tuple(x[1] for x in inputs)

# All syntactic trees of depth <=1 have one of these truth tables.
tables = {leaf0, leaf1}
for i, a, b in product(range(2), (False, True), (False, True)):
    tables.add(tuple(b if x[i] else a for x in inputs))

orf = tuple(x[0] or x[1] for x in inputs)
xorf = tuple(x[0] != x[1] for x in inputs)
assert orf not in tables
assert xorf not in tables
success_or = [sum((F(1, 3) for table in (leaf1, query0, query1)
                  if table[j] == orf[j]), F(0)) for j in range(4)]
assert success_or == [F(2, 3), F(2, 3), F(2, 3), F(1)]

# Any one-query tree has mean success <=2/3 on 00,01,10,
# excluding a strictly-better-than-2/3 one-query OR algorithm.
or_hard_mean = [sum((F(1, 3) for j in (0, 1, 2)
                    if table[j] == orf[j]), F(0)) for table in sorted(tables)]
assert max(or_hard_mean) == F(2, 3)

# Any one-query tree has exactly 1/2 success on uniform XOR inputs.
xor_hard_mean = [sum((F(1, 4) for j in range(4)
                     if table[j] == xorf[j]), F(0)) for table in sorted(tables)]
assert set(xor_hard_mean) == {F(1, 2)}

# A zero-query distribution is input independent. Correctness on one input
# of each label would require p>=2/3 and 1-p>=2/3, whose sum exceeds 1.
assert F(2, 3) + F(2, 3) > 1

L_2_7 = 2**7 // (4 * 7**2)
L_2_8 = 2**8 // (4 * 8**2)
G_2_8 = (4**8 * L_2_8) // 100
assert (L_2_7, L_2_8, G_2_8) == (0, 1, 655)

out = {
    "kind": "independent exact rational finite check, not Lean",
    "input_order": ["".join(str(int(b)) for b in x) for x in inputs],
    "depth_at_most_one_distinct_truth_tables": len(tables),
    "or2_equal_mixture_success": [str(s) for s in success_or],
    "or2_hard_distribution": {"00": "1/3", "01": "1/3", "10": "1/3"},
    "max_depth1_or2_hard_mean_success": str(max(or_hard_mean)),
    "xor2_uniform_depth1_success": [str(s) for s in xor_hard_mean],
    "known_complexities_from_certificates": {"OR2": {"D": 2, "R": 1}, "XOR2": {"D": 2, "R": 2}},
    "parameter_values": {"Lvalue_2_7": L_2_7, "Lvalue_2_8": L_2_8, "Gvalue_m8_L28": G_2_8},
    "all_assertions_passed": True
}
Path(__file__).with_name("classical_checks_output.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
