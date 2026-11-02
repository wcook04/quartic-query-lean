#!/usr/bin/env python3
"""Arithmetic and numerical checks for a growing-k quartic separation.

Python standard library only. Run:
    python3 checks.py
    python3 checks.py --json

Finite exact checks validate extracted constants, floor factors, cardinality
identities and parameter substitutions. Floating-point tables evaluate lower
bounds on log(R)/log(Q), not the unknown actual complexities. Neither finite
checks nor these tables prove a theorem or certify a quantum algorithm.

The a=10 route uses the supplied repetition decoder. The a=5 route substitutes
a separately proved amplitude-estimation decoder; this script checks only its
proposed numerical cost expression, not its circuit or formal correctness.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from typing import Any

C0 = 2_332_800
CLASSICAL_DENOMINATOR = 200 * C0
B_LINEAR = 2_972_284_080
B_QUADRATIC = 79_491_312_000
B_CONSTANT = 1_131_887_160
ROUTES = {
    10: {"name": "source repetition decoder", "r0_coefficient": 1_920_000,
         "envelope_power": 53, "coarse_constant": 524,
         "status": "budget expression from the supplied compiled source"},
    5: {"name": "amplitude-estimation decoder", "r0_coefficient": 122_880_256,
        "envelope_power": 59, "coarse_constant": 552,
        "status": "new paper derivation; circuit/formal verification not performed here"},
}
TABLE_T = [80, 100, 1_000, 10_000, 100_000, 1_000_000, 100_000_000]
LN2 = math.log(2.0)


def budget_original(k: int, a: int) -> int:
    """Literal shape of Upper.budgetConst, with the selected R0."""
    coeff = int(ROUTES[a]["r0_coefficient"])
    r0 = 1 + coeff * (1 << (a * k))
    cc = 40 * r0 * k + 4
    ck = 42 + 20 * (200 * (k + 1) ** 2)
    return 6 * (48_002 * 258 * cc) + 6 * (40 * r0 * k + 48_002 * 69 * ck)


def budget_expanded(k: int, a: int) -> int:
    coeff = int(ROUTES[a]["r0_coefficient"])
    return (B_LINEAR * k * (1 + coeff * (1 << (a * k)))
            + B_QUADRATIC * (k + 1) ** 2 + B_CONSTANT)


def schedule(t: int, a: int) -> int:
    """floor(sqrt(s/(4a))), s=2t, computed without floating point."""
    return math.isqrt(t // (2 * a))


def log_parameters(t: int, k: int, a: int) -> dict[str, float]:
    s = 2 * t
    # Never construct m=2^s for the large parameter table.
    ell = s * LN2 + math.log(4 * k)
    log2_uniform = ((1.0 - 1.0 / k) * s - math.log2(C0)
                    - 2.0 * math.log2(k) - math.log2(ell))
    A = s + log2_uniform - math.log2(200)
    D = s / 2.0 + math.log2(budget_expanded(k, a)) + 6.0 * math.log2(s)
    E = A / D
    coarse = (4.0 - 8.0 * math.sqrt(a) / math.sqrt(s)
              - (56.0 * math.log2(s) + int(ROUTES[a]["coarse_constant"])) / s)
    return {"ell_natural_log": ell, "log2_uniform_cutoff": log2_uniform,
            "A_log2_R_lower": A, "D_log2_Q_upper": D,
            "E_log_ratio_lower": E, "coarse_exponent_lower": coarse}


def wht_recurrence(width: int, n: int) -> int:
    cost = 0
    for j in range(n):
        cost = 2 * cost + (1 << j) * (6 * width) + (1 << j) * (6 * width + 1)
    return cost


def circuit_recurrence(k: int, t: int) -> int:
    width = 5 * k + 3 + t * (k + 1)
    m = 1 << (2 * t)
    layer = 1 + m * (6 * width)
    for _ in range(k - 1):
        layer += wht_recurrence(width, 2 * t) + m * (6 * width)
    return (layer + m * (6 * width) + 5 * k * (6 * width) + 6 * width + 1
            + t * (k + 1) * (6 * width)
            + (6 * width + 1) + (6 * width + 1) + 6 * width + 3)


def circuit_closed(k: int, t: int) -> int:
    width = 5 * k + 3 + t * (k + 1)
    m = 1 << (2 * t)
    return (7 + 6 * width * ((k + 1) * m + 5 * k + t * (k + 1) + 4)
            + (k - 1) * t * m * (12 * width + 1))


def exact_checks() -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    def record(name: str, cases: int, details: str) -> None:
        checks.append({"name": name, "cases": cases, "status": "passed",
                       "details": details})

    assert CLASSICAL_DENOMINATOR == 466_560_000 < 1 << 29
    assert B_LINEAR == 6 * 40 * (48_002 * 258 + 1)
    assert B_QUADRATIC == 6 * 48_002 * 69 * 4_000
    assert B_CONSTANT == 6 * 48_002 * (258 * 4 + 69 * 42)
    for a, route in ROUTES.items():
        coeff = int(route["r0_coefficient"])
        exponent = int(route["envelope_power"])
        coarse_coeff = B_LINEAR * coeff + B_LINEAR + 4 * B_QUADRATIC + B_CONSTANT
        assert coarse_coeff < 1 << exponent
        # General proof uses (k+1)^2<=4k^2<=4k*2^k<=4k*2^(ak).
        for k in range(1, 129):
            assert budget_original(k, a) == budget_expanded(k, a)
            assert budget_expanded(k, a) <= (1 << exponent) * k * (1 << (a * k))
    assert 122_880_256 == 1_024 * 120_000 + 256
    record("budget expansions and envelopes", 256,
           "Literal source-shaped expression equals expanded integer polynomial; "
           "both envelope coefficients checked exactly. No quantum semantics tested.")

    for t in range(129):
        m = 1 << (2 * t)
        ceil_log2 = (1_000 * m - 1).bit_length()
        assert ceil_log2 == 2 * t + 10
        assert 1 << (40 * t) == m ** 20
    record("tournament ceiling and cell-array cardinality", 129,
           "ceil(log2(1000*4^t))=2t+10 and 2^(40t)=m^20; integer arithmetic.")

    count = 0
    for k in range(1, 31):
        for t in range(31):
            width = 5 * k + 3 + t * (k + 1)
            m = 1 << (2 * t)
            assert wht_recurrence(width, 2 * t) == t * m * (12 * width + 1)
            assert circuit_recurrence(k, t) == circuit_closed(k, t)
            if t >= 1:
                assert circuit_closed(k, t) <= 200 * (k + 1) ** 2 * m * (2 * t) ** 2
            count += 1
    record("circuit recurrence, closed formula and size bound", count,
           "Independent recurrence evaluation checks the extracted closed size formula. "
           "The logarithmic size bound is tested only for t>=1.")

    count = 0
    for k in range(1, 9):
        for t in range(1, 11):
            s = 2 * t
            m = 1 << s
            r = 20 * s
            size = circuit_closed(k, t)
            coordinate_sum = (m * m + m * r * (k * m)
                              + m * (1 << r) * (m - 1) * s
                              + m * (1 << r) * r * size)
            closed = m * m * (1 + 20 * k * s) + m ** 21 * ((m - 1) * s + 20 * s * size)
            assert coordinate_sum == closed
            assert (m - 1) * m ** 21 * s <= closed
            assert closed <= 4_022 * (k + 1) ** 2 * m ** 22 * s ** 3
            count += 1
    record("physical input length", count,
           "Sum of the four coordinate-type cardinalities agrees with the closed formula; "
           "m is the number of columns, not the number of input bits.")

    count = 0
    for denominator in [1, 2, 3, 7, 100]:
        values = {Fraction(2), Fraction(3), Fraction(4)}
        for j in [2, 3, 4, 10]:
            for offset in [-1, 0, 1]:
                q = Fraction(j * denominator + offset, denominator)
                if q >= 2:
                    values.add(q)
        for cutoff in sorted(values):
            floor_cutoff = cutoff.numerator // cutoff.denominator
            assert floor_cutoff >= cutoff / 2
            for m in [1, 2, 3, 99, 100, 101, 1_000, 10_001]:
                G = m * floor_cutoff // 100
                least_integer_R_above_G = G + 1
                assert least_integer_R_above_G > Fraction(m * floor_cutoff, 100)
                assert least_integer_R_above_G > m * cutoff / 200
                count += 1
    # A concrete negative control rejects the unjustified denominator 100.
    cutoff = Fraction(299, 100)
    m = 1_000
    least_R = m * (cutoff.numerator // cutoff.denominator) // 100 + 1
    assert least_R == 21 < m * cutoff / 100
    record("floor transfer and wrong-factor negative control", count,
           "For U>=2, floor(U)>=U/2; G<R gives R>mU/200. "
           "Denominator100 fails at U=299/100,m=1000: the least R allowed by G<R is 21, "
           "below mU/100=29.9.")

    count = 0
    for t in range(25):
        m = 1 << (2 * t)
        tail = Fraction(2, 3) ** (40 * t)
        assert tail <= Fraction(1, m ** 10)
        L_values = {1, m, max(1, m // 2), max(1, m // 10)}
        for L in sorted(L_values):
            G = m * L // 100
            discrepancy = Fraction(4 * G, m * m) + Fraction(G, m * L) + G * tail
            assert discrepancy <= Fraction(6, 100) < Fraction(1, 3)
            count += 1
    record("generic planted discrepancy", count,
           "Source-conservative coefficient 4 and G=floor(mL/100), 1<=L<=m; "
           "the generic theorem needs no large-t hypothesis.")

    assert 18 * 8 ** 25 < 9 ** 25
    for k in range(2, 33):
        delta = Fraction(1, 1 << (5 * k))
        assert 32 * delta == Fraction(1, 32 ** (k - 1))
        assert 32 * delta <= Fraction(1, 18 ** (k - 1))
    assert (1 << 64) >= 2 * 13_996_800 * 64 ** 3
    assert (1 << 50) > 20_736
    record("classical numerical thresholds", 33,
           "18*8^25<9^25, the 32*delta identity/bound, and the t=64 base case "
           "for U>=2 are exact. The induction proving all larger t is in the paper.")

    cases = 0
    for a in ROUTES:
        for j in range(2, 257):
            for offset in [-1, 0, 1]:
                t = 2 * a * j * j + offset
                if t < 80:
                    continue
                k = schedule(t, a)
                assert 2 * a * k * k <= t < 2 * a * (k + 1) ** 2
                s = 2 * t
                assert k >= 2 and 15 * k + 2 <= s
                assert k * k <= s
                # Leading-loss AM-GM bound, squared, can be checked exactly.
                leading_loss = Fraction(2, k) + Fraction(8 * a * k, s)
                assert leading_loss ** 2 >= Fraction(64 * a, s)
                if offset == 0:
                    assert leading_loss == Fraction(4, j)
                cases += 1
        assert schedule(80, a) == 2
    assert math.isqrt(160) // 40 != schedule(80, 10)
    record("schedule discontinuities and leading coefficient", cases,
           "Checks t just below/at/above perfect-square thresholds, all parameter "
           "conditions, and exact leading-loss equality at those thresholds. "
           "The wrong expression sqrt(s)/40 is rejected.")

    no_margin = Fraction(1, 4) + Fraction(1, 8) + Fraction(1, 64)
    yes_margin = 1 - Fraction(1, 4) - Fraction(1, 64)
    assert no_margin == Fraction(25, 64) < Fraction(1, 2)
    assert yes_margin == Fraction(47, 64) > Fraction(1, 2)
    assert Fraction(1, 2) - no_margin == Fraction(7, 64)
    assert yes_margin - Fraction(1, 2) == Fraction(15, 64)
    record("amplitude-estimation rational margins", 4,
           "With M>=8*pi/delta, the BHMT good-event error bound gives 25/64 below "
           "and 47/64 above the normalized threshold 1/2. This does not verify BHMT "
           "or its coherent implementation.")
    return checks


def make_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for a in [10, 5]:
        for t in TABLE_T:
            s = 2 * t
            k = schedule(t, a)
            pars = log_parameters(t, k, a)
            assert t >= 80 and k >= 2 and 15 * k + 2 <= s
            assert pars["A_log2_R_lower"] > 0
            assert pars["D_log2_Q_upper"] > 0
            assert pars["E_log_ratio_lower"] + 1e-12 >= pars["coarse_exponent_lower"]
            assert pars["ell_natural_log"] <= 2 * s
            assert pars["log2_uniform_cutoff"] >= 1
            assert pars["log2_uniform_cutoff"] <= s
            assert pars["A_log2_R_lower"] > math.log2(20_736)
            radius = max(16, math.ceil(math.log2(s)))
            candidates = range(max(2, k - radius), min(k + radius, (s - 2) // 15) + 1)
            eligible = [(j, log_parameters(t, j, a)) for j in candidates]
            eligible = [(j, p) for j, p in eligible if p["log2_uniform_cutoff"] >= 1]
            best_k, best = max(eligible, key=lambda pair: pair[1]["E_log_ratio_lower"])
            x = math.sqrt(s / (4.0 * a))
            loss = 2.0 / k + 8.0 * a * k / s
            identity = 4.0 / x + 2.0 * (k - x) ** 2 / (k * x * x)
            assert math.isclose(loss, identity, rel_tol=1e-12, abs_tol=1e-14)
            assert loss <= 8.0 * math.sqrt(a) / math.sqrt(s) + 4.0 * a / s + 1e-12
            rows.append({"a": a, "route": ROUTES[a]["name"], "t": t, "s": s, "k": k,
                         **pars,
                         "source_threshold_15k_plus_2_le_s": 15 * k + 2 <= s,
                         "quantum_threshold_t_ge_1": t >= 1,
                         "classical_threshold_k_ge_2": k >= 2,
                         "cutoff_at_least_2_logspace_check": pars["log2_uniform_cutoff"] >= 1,
                         "cutoff_at_most_m_logspace_check": pars["log2_uniform_cutoff"] <= s,
                         "Q_gt_1_from_universal_quartic_and_R_lower": pars["A_log2_R_lower"] > math.log2(20_736),
                         "unneeded_old_Lvalue_corollary_threshold": t >= 3_499_200 * k * k,
                         "nearby_scan_radius": radius,
                         "best_nearby_k": best_k,
                         "best_nearby_E": best["E_log_ratio_lower"],
                         "scaled_deficit_sqrt_s_times_4_minus_E": math.sqrt(s) * (4.0 - pars["E_log_ratio_lower"]),
                         "limiting_leading_deficit_coefficient": 8.0 * math.sqrt(a)})
    return rows


TEXTUAL_CHECKS = [
    "Promise/sign check: yes means Phi>=delta; no means abs(Phi)<=delta/2. "
    "A large negative Phi is off-promise. A Phi^2 decoder can accept such an input; "
    "this is permitted only because total-function verification rejects invalid address certificates with its proved bounded-error guarantee. "
    "This is a textual mathematical requirement, not a numerical test.",
    "Quantum proof check still required: coherent amplitude estimation, controlled oracle signs, "
    "inverse preparation, coherent majority with retained workspace, generic sampler replacement, "
    "and worst-case branch caps are outside this script's verification scope.",
    "The nearby-k scan is bounded and is not a global optimizer or an optimality proof. "
    "It measures finite-parameter slack in the asymptotically balanced schedule.",
    "No value in the table is the actual R or Q of a Boolean function. A and D are logarithms "
    "of established/proposed complexity bounds; E is their ratio and lower-bounds log(R)/log(Q) "
    "when the mathematical hypotheses hold.",
    "The ordinary Lvalue threshold t>=3499200*k^2 is deliberately not required. "
    "The auxiliary classical cutoff L can be changed without changing F_{k,m}.",
]


def report() -> dict[str, Any]:
    checks = exact_checks()
    rows = make_rows()
    return {"description": "Finite arithmetic checks and rounded exponent-bound evaluations; not a proof or a Lean run.",
            "classical_lower_denominator": CLASSICAL_DENOMINATOR,
            "routes": ROUTES, "exact_checks": checks,
            "floating_point_rows": rows, "textual_requirements_and_limits": TEXTUAL_CHECKS,
            "validation": {"all_exact_checks_passed": True, "all_sampled_thresholds_passed": True,
                           "all_sampled_finite_exponent_inequalities_passed": True,
                           "lean_run": False, "actual_complexities_computed": False}}


def print_text(result: dict[str, Any]) -> None:
    print(result["description"])
    print("All logs marked log2 use base2; ell=ln(4km) is a natural logarithm.")
    print("No huge value of m, R, Q or a query budget is printed.")
    print()
    print("Exact arithmetic checks:")
    for item in result["exact_checks"]:
        print(f"  PASS {item['name']} ({item['cases']} finite cases)")
        print(f"       {item['details']}")
    print()
    for a in [10, 5]:
        route = ROUTES[a]
        print(f"Route a={a}: {route['name']}")
        print(f"  Status: {route['status']}")
        print(f"  k=floor(sqrt(s/{4*a})), s=2t; B<={2}^{route['envelope_power']} k 2^({a}k).")
        print(f"  Coarse lower exponent: 4-8sqrt({a})/sqrt(s)-(56log2(s)+{route['coarse_constant']})/s.")
        print("            t      k          A          D          E       coarse   nearby k  nearby E")
        for row in result["floating_point_rows"]:
            if row["a"] != a:
                continue
            print(f"  {row['t']:11d} {row['k']:6d} {row['A_log2_R_lower']:10.3f} "
                  f"{row['D_log2_Q_upper']:10.3f} {row['E_log_ratio_lower']:10.7f} "
                  f"{row['coarse_exponent_lower']:10.7f} {row['best_nearby_k']:10d} "
                  f"{row['best_nearby_E']:10.7f}")
        print("  Every displayed case has k>=2, 15k+2<=s, cutoff>=2, cutoff<=m, and R_lower>20736.")
        print("  The unnecessary old Lvalue-corollary threshold fails for every displayed case.")
        print()
    print("Textual checks and evidence limits:")
    for text in TEXTUAL_CHECKS:
        print("  " + text)
    print()
    print("PASS: all finite arithmetic checks and sampled exponent inequalities. No Lean compiler was run.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="write the complete result as JSON")
    args = parser.parse_args()
    result = report()
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print_text(result)


if __name__ == "__main__":
    main()
