#!/usr/bin/env python3
"""Exact independent finite checks for round-three Forrelation section 02.

Only the Python standard library is used.  No floating-point operations, Lean
executable, compiled Lean objects, or generated graph data are used.  The direct
path sum and dense matrix multiplication are independent references for a
separate Boolean reconstruction of the supplied gate-list constructors.

This is finite arithmetic evidence.  The Boolean reconstruction is not code
extracted from Lean and does not certify a Lean compilation or a universal
circuit theorem.  Synthetic threshold numerators need not occur on a real input.

Run: python exact_example_checker.py --json exact_example_results.json
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from math import prod
from pathlib import Path


def walsh_entry(i: int, j: int) -> int:
    return -1 if (i & j).bit_count() % 2 else 1


def sign_blocks(mask: int, k: int, t: int) -> tuple[tuple[int, ...], ...]:
    m = 4**t
    return tuple(tuple(-1 if mask >> (r * m + a) & 1 else 1
                       for a in range(m)) for r in range(k))


def mask_of(blocks: tuple[tuple[int, ...], ...]) -> int:
    m = len(blocks[0])
    return sum(1 << (r * m + a) for r, block in enumerate(blocks)
               for a, sign in enumerate(block) if sign == -1)


def direct_numerator(blocks: tuple[tuple[int, ...], ...]) -> int:
    k, m = len(blocks), len(blocks[0])
    return sum(prod(blocks[r][p[r]] for r in range(k)) *
               prod(walsh_entry(p[r], p[r + 1]) for r in range(k - 1))
               for p in product(range(m), repeat=k))


def dense_numerator(blocks: tuple[tuple[int, ...], ...]) -> int:
    m = len(blocks[0])
    v = list(blocks[-1])
    for block in reversed(blocks[:-1]):
        v = [block[i] * sum(walsh_entry(i, j) * v[j] for j in range(m))
             for i in range(m)]
    return sum(v)


def fwht(v: list[int]) -> list[int]:
    if len(v) == 1:
        return v[:]
    half = len(v) // 2
    left, right = fwht(v[:half]), fwht(v[half:])
    return [a + b for a, b in zip(left, right)] + [a - b for a, b in zip(left, right)]


def butterfly_numerator(blocks: tuple[tuple[int, ...], ...]) -> int:
    v = list(blocks[-1])
    for block in reversed(blocks[:-1]):
        v = [a * b for a, b in zip(block, fwht(v))]
    return sum(v)


def promise_from_integer(n: int, k: int, t: int) -> int | None:
    M = 2 ** (t * (k + 1))
    if 2 ** (5 * k) * n >= M:
        return 1
    if 2 ** (5 * k + 1) * abs(n) <= M:
        return 0
    return None


def promise_from_rational(n: int, k: int, t: int) -> int | None:
    phi = Fraction(n, 2 ** (t * (k + 1)))
    delta = Fraction(1, 2 ** (5 * k))
    yes, no = phi >= delta, abs(phi) <= delta / 2
    assert not (yes and no)
    return 1 if yes else 0 if no else None


class BooleanCircuit:
    """Append-only fan-in-two gate list; -1 is the constant-false wire."""

    def __init__(self, inputs: int):
        self.inputs = inputs
        self.gates: list[tuple[str, int, int]] = []

    def gate(self, op: str, a: int = -1, b: int = -1) -> int:
        assert -1 <= a < self.inputs + len(self.gates)
        assert -1 <= b < self.inputs + len(self.gates)
        wire = self.inputs + len(self.gates)
        self.gates.append((op, a, b))
        return wire

    def full_add(self, a: int, b: int, carry: int) -> tuple[int, int]:
        xor_ab = self.gate("xor", a, b)
        total = self.gate("xor", xor_ab, carry)
        ab = self.gate("and", a, b)
        xc = self.gate("and", xor_ab, carry)
        out_carry = self.gate("or", ab, xc)
        return total, out_carry

    def addsub(self, sign: int, a: list[int], b: list[int]) -> list[int]:
        assert len(a) == len(b)
        bb = [self.gate("xor", bit, sign) for bit in b]
        carry, out = sign, []
        for left, right in zip(a, bb):
            bit, carry = self.full_add(left, right, carry)
            out.append(bit)
        return out

    def add(self, a: list[int], b: list[int]) -> list[int]:
        return self.addsub(-1, a, b)

    def sub(self, a: list[int], b: list[int]) -> list[int]:
        one = self.gate("true")
        return self.addsub(one, a, b)

    def sign_mul(self, sign: int, b: list[int]) -> list[int]:
        return self.addsub(sign, [-1] * len(b), b)

    def wht(self, vectors: list[list[int]]) -> list[list[int]]:
        if len(vectors) == 1:
            return vectors
        half = len(vectors) // 2
        left = self.wht(vectors[:half])
        right = self.wht(vectors[half:])
        sums = [self.add(a, b) for a, b in zip(left, right)]
        diffs = [self.sub(a, b) for a, b in zip(left, right)]
        return sums + diffs

    def double_n(self, n: int, a: list[int]) -> list[int]:
        for _ in range(n):
            a = self.add(a, a)
        return a

    def evaluate_all(self) -> list[int]:
        """Each integer packs the wire's values on all input assignments."""
        count = 1 << self.inputs
        universe = (1 << count) - 1
        values = [sum(1 << assignment for assignment in range(count)
                      if assignment >> i & 1) for i in range(self.inputs)]

        def value(wire: int) -> int:
            return 0 if wire == -1 else values[wire]

        for op, left, right in self.gates:
            a, b = value(left), value(right)
            if op == "xor":
                v = a ^ b
            elif op == "and":
                v = a & b
            elif op == "or":
                v = a | b
            elif op == "not":
                v = universe ^ a
            elif op == "nor":
                v = universe ^ (a | b)
            elif op == "true":
                v = universe
            else:
                raise ValueError(op)
            values.append(v)
        return values


def build_circuit(k: int, t: int) -> tuple[BooleanCircuit, int, int, dict[str, list[int]]]:
    """Reconstruct the arithmetic/output gates with the source's gate counts."""
    assert k >= 1 and t >= 0
    m, s, e = 4**t, 5 * k, t * (k + 1)
    w = s + 3 + e
    circuit = BooleanCircuit(k * m)
    one = [circuit.gate("true")] + [-1] * (w - 1)
    v = [circuit.sign_mul((k - 1) * m + a, one) for a in range(m)]
    for r in reversed(range(k - 1)):
        v = circuit.wht(v)
        v = [circuit.sign_mul(r * m + a, v[a]) for a in range(m)]
    N = [-1] * w
    for word in v:
        N = circuit.add(N, word)
    shift = circuit.double_n(s, N)
    twice_shift = circuit.add(shift, shift)
    M = circuit.double_n(e, [circuit.gate("true")] + [-1] * (w - 1))
    A = circuit.sub(shift, M)
    B = circuit.sub(M, twice_shift)
    C = circuit.add(M, twice_shift)
    b = circuit.gate("not", A[-1])
    p0 = circuit.gate("nor", B[-1], C[-1])
    d = circuit.gate("or", b, p0)
    return circuit, d, b, {"N": N, "A": A, "B": B, "C": C}


def gate_count_formula(k: int, t: int) -> int:
    m, s, e = 4**t, 5 * k, t * (k + 1)
    w = s + 3 + e
    # whtCost(w,2t) = t*m*(12w+1), by solving its exact recurrence.
    return (6 * w * ((k + 1) * m + s + e + 4)
            + (k - 1) * t * m * (12 * w + 1) + 7)


def check_family(k: int, t: int) -> dict:
    m, M = 4**t, 2 ** (t * (k + 1))
    circuit, d_wire, b_wire, words = build_circuit(k, t)
    values = circuit.evaluate_all()
    w = 5 * k + 3 + t * (k + 1)
    modulus, half = 1 << w, 1 << (w - 1)
    assert len(circuit.gates) == gate_count_formula(k, t)
    if t >= 1:
        assert len(circuit.gates) <= 200 * (k + 1) ** 2 * m * (2 * t) ** 2
    census, numerators = Counter(), Counter()

    def bit(wire: int, mask: int) -> int:
        return 0 if wire == -1 else (values[wire] >> mask) & 1

    for mask in range(1 << (k * m)):
        blocks = sign_blocks(mask, k, t)
        n = direct_numerator(blocks)
        assert n == dense_numerator(blocks) == butterfly_numerator(blocks)
        assert abs(n) <= M
        outcome = promise_from_integer(n, k, t)
        assert outcome == promise_from_rational(n, k, t)
        assert bit(d_wire, mask) == int(outcome is not None)
        assert bit(b_wire, mask) == int(2 ** (5 * k) * n >= M)
        expected = {"N": n, "A": 2 ** (5 * k) * n - M,
                    "B": M - 2 ** (5 * k + 1) * n,
                    "C": M + 2 ** (5 * k + 1) * n}
        for name, word in words.items():
            residue = sum(bit(wire, mask) << i for i, wire in enumerate(word))
            assert residue == expected[name] % modulus
            if name != "N":
                assert -half <= expected[name] < half
                assert bit(word[-1], mask) == int(expected[name] < 0)
        census[str(outcome) if outcome is not None else "undefined"] += 1
        numerators[n] += 1
    return {"k": k, "t": t, "m": m, "M": M, "word_width": w,
            "input_count": 1 << (k * m), "gate_count": len(circuit.gates),
            "census": dict(sorted(census.items())),
            "numerator_histogram": {str(n): c for n, c in sorted(numerators.items())},
            "checks": ["direct path = dense Walsh = butterfly numerator",
                       "integer thresholds = exact rational promise",
                       "every reconstructed Boolean output matches promise",
                       "N,A,B,C words encode the exact residues",
                       "A,B,C signs recover exact integer comparisons",
                       "gate count matches source-constructor recurrence"]}


def explicit_examples() -> list[dict]:
    second = (-1, 1, 1, 1)
    examples = [("positive", (1, -1, -1, -1), 8, 1),
                ("zero", (1, -1, 1, 1), 0, 0),
                ("negative", (-1, 1, 1, 1), -8, None)]
    answer = []
    Wsecond = [sum(walsh_entry(i, j) * second[j] for j in range(4)) for i in range(4)]
    assert Wsecond == [2, -2, -2, -2]
    for label, first, expected_n, expected_p in examples:
        blocks = (first, second)
        n = direct_numerator(blocks)
        assert n == expected_n and promise_from_integer(n, 2, 1) == expected_p
        phi = Fraction(n, 8)
        answer.append({"label": label, "z0": list(first), "z1": list(second),
                       "input_mask": mask_of(blocks), "W_z1": Wsecond,
                       "N": n, "M": 8, "Phi": str(phi),
                       "projection_probability": str(phi**2),
                       "P": expected_p, "d": int(expected_p is not None),
                       "b": int(2**10 * n >= 8)})
    return answer


def threshold_boundary_checks() -> dict:
    # Here the two equality thresholds and a positive gap contain integers.
    # These are synthetic numerator tests, not claims of realizable inputs.
    k, t = 2, 4
    M, s = 2 ** (t * (k + 1)), 5 * k
    w, count = s + 3 + t * (k + 1), 0
    for n in range(-M, M + 1):
        A, B, C = 2**s * n - M, M - 2 ** (s + 1) * n, M + 2 ** (s + 1) * n
        signs = [((v % (1 << w)) >> (w - 1)) & 1 for v in (A, B, C)]
        assert all(-2 ** (w - 1) <= v < 2 ** (w - 1) for v in (A, B, C))
        assert signs == [int(v < 0) for v in (A, B, C)]
        b = 1 - signs[0]
        d = b or ((1 - signs[1]) and (1 - signs[2]))
        outcome = promise_from_rational(n, k, t)
        assert outcome == promise_from_integer(n, k, t)
        assert d == int(outcome is not None)
        assert b == int(outcome == 1)
        count += 1
    return {"k": k, "t": t, "M": M, "numerators_checked": count,
            "status": "synthetic integer numerators; realizability not asserted",
            "boundary_examples": [{"N": n, "Phi": str(Fraction(n, M)),
                                   "P": promise_from_integer(n, k, t)}
                                  for n in (-4, -2, 0, 2, 3, 4)]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="write machine-readable result")
    args = parser.parse_args()
    families = [check_family(2, 1), check_family(3, 1)]
    assert families[0]["census"] == {"0": 48, "1": 104, "undefined": 104}
    assert families[0]["numerator_histogram"] == {"-8": 8, "-4": 96, "0": 48, "4": 96, "8": 8}
    result = {"schema": "forrelation_exact_finite_check_v1", "passed": True,
              "arithmetic": "Python arbitrary-precision integers and fractions.Fraction",
              "bit_convention": "bit 1 means sign -1; bit index = block*m+coordinate",
              "walsh_order": "natural integer index; sign = (-1)^popcount(i & j)",
              "families": families, "examples": explicit_examples(),
              "threshold_boundary_checks": threshold_boundary_checks(),
              "limitations": ["finite checks, not a proof for all k,t",
                              "Boolean reconstruction, not extracted Lean execution",
                              "no Lean build, Comparator result, or kernel replay claimed",
                              "no classical lower bound or growing-k theorem tested"]}
    output = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.json:
        args.json.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
