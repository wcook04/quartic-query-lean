#!/usr/bin/env python3
"""Exact finite checks of the two floors, not an asymptotic proof.

For m=4^t and k>=2, L=floor(m^((k-1)/k)/(2t)^2).
All comparisons use integers or Fraction; no floating root approximation.
The real comparison G >= m^(2-1/k)/(400(2t)^2) is equivalent, for
nonnegative quantities, to (400(2t)^2 G)^k >= m^(2k-1).
"""
from fractions import Fraction
from pathlib import Path
import json
import sys


def integer_root(a, k):
    """Return floor(a^(1/k)), certified by integer inequalities."""
    assert a >= 0 and k >= 1
    lo, hi = 0, 1 << ((a.bit_length() + k - 1) // k + 1)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid ** k <= a:
            lo = mid
        else:
            hi = mid
    assert lo ** k <= a < (lo + 1) ** k
    return lo


def main():
    rows = []
    for k in range(2, 13):
        for t in range(8, 25):
            m, denom = 4 ** t, (2 * t) ** 2
            root = integer_root(m ** (k - 1), k)
            ell = root // denom
            g = m * ell // 100
            # This certifies the exact floor without a radical approximation.
            assert (ell * denom) ** k <= m ** (k - 1)
            assert ((ell + 1) * denom) ** k > m ** (k - 1)
            assert 1 <= ell <= m
            assert 4 * t * t <= 2 ** t
            assert 100 * g <= m * ell < 100 * (g + 1)
            assert (400 * denom * g) ** k >= m ** (2 * k - 1)
            zero = Fraction(4 * g, m * m)
            heavy = Fraction(g, m * ell)
            tail = g * Fraction(2, 3) ** (40 * t)
            assert Fraction(2, 3) ** (40 * t) <= Fraction(1, m ** 10)
            assert zero <= Fraction(4, 100)
            assert heavy <= Fraction(1, 100)
            assert tail <= Fraction(1, 100 * m ** 8) <= Fraction(1, 100)
            assert zero + heavy + tail <= Fraction(6, 100) < Fraction(1, 3)
            rows.append({"k": k, "t": t, "m": m, "L": ell, "G": g,
                         "literal_floor_bound_passed": True,
                         "numeric_discrepancy_passed": True})
    data = {
        "schema": "quartic_r3_exact_floor_checks_v1",
        "case_count": len(rows),
        "domain": {"k": [2, 12], "t": [8, 24], "m": "4^t"},
        "arithmetic": "Integer powers, integer-root brackets, exact rational tail",
        "checked": [
            "L is the literal natural floor of m^(1-1/k)/(2t)^2",
            "1 <= L <= m",
            "G is floor(mL/100)",
            "G >= m^(2-1/k)/(400(2t)^2), with no +1 slack",
            "(2/3)^(40t) <= m^(-10)",
            "4G/m^2 + G/(mL) + G(2/3)^(40t) <= 6/100 < 1/3"
        ],
        "limits": [
            "Finite arithmetic verification only; the universal proof is in section.md.",
            "No assertion that the Forrelation hardness threshold holds at these t.",
            "No Lean or Comparator execution."
        ],
        "cases": rows,
        "passed": True
    }
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({"passed": True, "cases": len(rows), "output": str(out)}))


if __name__ == "__main__":
    main()
