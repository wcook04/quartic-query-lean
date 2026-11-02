#!/usr/bin/env python3
"""Exact finite illustration of the planted-input argument.

This is independent of Lean and of the packet's supplied checking scripts.
It uses m=4, r=2, P(u0,u1)=u0 XOR u1 and uniform two-bit inputs.
It deliberately does not use r=40t or G=floor(mL/100), so it cannot
verify the asymptotic Proposition 4.2. All enumerated probabilities are exact.
"""

from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import sys

M = 4
R = 2
ELL = 2
L = 1
G = 4
TARGET = 1
BITS = tuple(product((0, 1), repeat=2))
TARGETS = tuple(product(BITS, repeat=R))
ZERO_POSITIONS = tuple(product(range(M), repeat=M))
ADDRESSES = tuple(product((0, 1), repeat=R))
OUTSIDE_A = (((0, 0), (0, 1)), ((0, 0), (0, 0)),
             ((1, 0), (1, 1)), ((0, 1), (1, 0)))


def frac(x):
    x = Fraction(x)
    return {"numerator": x.numerator, "denominator": x.denominator,
            "text": str(x)}


def parity(u):
    return u[0] ^ u[1]


def transcript(u):
    # Gate 0 is constant true (the domain output); gate 1 is XOR (the value).
    return (1, parity(u))


def address(U):
    return tuple(map(parity, U))


def put_target(U):
    a = list(OUTSIDE_A)
    a[TARGET] = U
    return tuple(a)


def all_coordinates():
    for i in range(M):
        for p in range(M):
            yield ("X", i, p)
        for h in range(R):
            for p in range(2):
                yield ("A", i, h, p)
        for s in ADDRESSES:
            for j in range(M):
                if j != i:
                    for p in range(ELL):
                        yield ("B", "pointer", i, s, j, p)
            for h in range(R):
                for g in range(2):
                    yield ("B", "transcript", i, s, h, g)


COORDINATES = tuple(all_coordinates())


def oracle(J, A, planted_column=None):
    def read(q):
        if q[0] == "X":
            _, i, p = q
            return int(i == planted_column or p != J[i])
        if q[0] == "A":
            _, i, h, p = q
            return A[i][h][p]
        _, kind, i, s, j, p = q
        if i != planted_column or s != address(A[i]):
            return 0
        if kind == "pointer":
            # Big-endian two-bit pointer encoding.
            return (J[j] >> (ELL - 1 - p)) & 1
        return transcript(A[i][j])[p]
    return read


def winner(read, i):
    """Evaluate the generic addressed-winner predicate on oracle bits."""
    if not all(read(("X", i, p)) for p in range(M)):
        return False
    U = tuple(tuple(read(("A", i, h, p)) for p in range(2)) for h in range(R))
    s = address(U)  # Every two-bit input is promised for this toy P.
    for h in range(R):
        if tuple(read(("B", "transcript", i, s, h, g)) for g in range(2)) != transcript(U[h]):
            return False
    for j in range(M):
        if j == i:
            continue
        pointer = sum(read(("B", "pointer", i, s, j, p)) << (ELL - 1 - p)
                      for p in range(ELL))
        if read(("X", j, pointer)):
            return False
    return True


def total_function(read):
    return int(any(winner(read, i) for i in range(M)))


def next_query(trace):
    """A deterministic four-query algorithm; tuples name physical bits."""
    step = len(trace)
    if step == 0:
        return ("X", 0, 0)
    if step == 1:
        return ("A", TARGET, 0, 0)
    b = trace[1][1]
    if step == 2:
        return (("A", TARGET, 1, 0) if b == 0 else ("X", 2, 1))
    if step == 3:
        # Query the domain-output bit at the guessed address (b,0).
        return ("B", "transcript", TARGET, (b, 0), 0, 0)
    return None


def run(read):
    trace = []
    while (q := next_query(trace)) is not None:
        trace.append((q, read(q)))
    return trace, trace[-1][1]


def simulate(J, U, proposed_time=4, cap=L):
    """Outside answers come from an independent base with placeholder A_TARGET.

    The simulator stops before answering its proposed-time query. Target
    queries are made only through U and capped on every possible input.
    """
    base = oracle(J, OUTSIDE_A)
    trace = []
    entries = []
    used = 0
    while (q := next_query(trace)) is not None:
        time = len(trace) + 1
        if time == proposed_time:
            guess = q[3] if q[0] == "B" and q[2] == TARGET else (0, 0)
            entries.append({"time": time, "coordinate": q, "action": "return proposed address",
                            "guess": guess, "target_queries_used": used, "bit_read": False})
            return {"guess": guess, "target_queries_used": used,
                    "aborted": False, "trace": entries}
        if q[0] == "A" and q[1] == TARGET:
            if used == cap:
                entries.append({"time": time, "coordinate": q, "action": "abort before target query",
                                "guess": (0, 0), "target_queries_used": used, "bit_read": False})
                return {"guess": (0, 0), "target_queries_used": used,
                        "aborted": True, "trace": entries}
            answer = U[q[2]][q[3]]
            used += 1
            origin = "target oracle (charged)"
        else:
            answer = base(q)
            origin = "independent outside data (free)"
        trace.append((q, answer))
        entries.append({"time": time, "coordinate": q, "action": origin,
                        "answer": answer, "target_queries_used": used, "bit_read": True})
    return {"guess": (0, 0), "target_queries_used": used, "aborted": False, "trace": entries}


def zero_statistics(trace, J):
    seen = [set() for _ in range(M)]
    discovered = set()
    early = late = 0
    for q, _ in trace:
        if q[0] != "X":
            continue
        _, i, p = q
        if p == J[i] and i not in discovered:
            if len(seen[i]) < Fraction(M, 2):
                early += 1
            else:
                late += 1
            discovered.add(i)
        seen[i].add(p)
    assert len(discovered) == early + late
    return discovered, early, late


def one_query_optimum(inputs, function):
    """Enumerate both constants and all one-query Boolean decision trees."""
    values = [sum(function(u) == b for u in inputs) for b in (0, 1)]
    for p in range(2):
        for leaves in product((0, 1), repeat=2):
            values.append(sum(function(u) == leaves[u[p]] for u in inputs))
    return Fraction(max(values), len(inputs))


def main():
    # Named sample: after one charged target bit, the simulator guesses (1,0).
    J0 = (2, 0, 3, 1)
    U0 = ((1, 0), (1, 1))
    A0 = put_target(U0)
    y0, y1 = oracle(J0, A0), oracle(J0, A0, TARGET)
    tr0, out0 = run(y0)
    tr1, out1 = run(y1)
    sample = {
        "J": J0, "A": A0, "I": TARGET, "true_address": address(U0),
        "X_dummy": [[y0(("X", i, p)) for p in range(M)] for i in range(M)],
        "X_planted": [[y1(("X", i, p)) for p in range(M)] for i in range(M)],
        "planted_transcripts": [transcript(u) for u in U0],
        "planted_pointers": {str(j): [int(b) for b in format(J0[j], "02b")]
                             for j in range(M) if j != TARGET},
        "F_dummy": total_function(y0), "F_planted": total_function(y1),
        "algorithm_dummy_trace": [{"time": t + 1, "coordinate": q, "answer": b}
                                  for t, (q, b) in enumerate(tr0)],
        "algorithm_planted_trace": [{"time": t + 1, "coordinate": q, "answer": b}
                                    for t, (q, b) in enumerate(tr1)],
        "algorithm_outputs": [out0, out1],
        "simulator": simulate(J0, U0),
        "abort_case": {"target_inputs": ((0, 1), (0, 0)),
                       "simulation": simulate(J0, ((0, 1), (0, 0)))},
    }
    assert sample["F_dummy"] == 0 and sample["F_planted"] == 1
    assert out0 == 0 and out1 == 1
    assert sample["simulator"]["guess"] == address(U0)
    assert sample["abort_case"]["simulation"]["aborted"]

    dummy_count = len(ZERO_POSITIONS) * len(TARGETS)
    coupled_count = dummy_count * M
    counts = {name: 0 for name in ("sum_Z", "sum_early", "sum_late", "erased_zero_hits",
                                  "true_cell_hits", "output_disagreements", "signed_output_gap", "nonheavy_true_cell",
                                  "simulator_success", "heavy_target", "heavy_selected")}
    for J in ZERO_POSITIONS:
        for U in TARGETS:
            A = put_target(U)
            dummy = oracle(J, A)
            trace, out = run(dummy)
            assert total_function(dummy) == 0
            assert out == 0  # Its final query reads a blank dummy cell.
            discovered, early, late = zero_statistics(trace, J)
            counts["sum_Z"] += len(discovered)
            counts["sum_early"] += early
            counts["sum_late"] += late
            assert late <= Fraction(2 * G, M)
            q_target = sum(q[0] == "A" and q[1] == TARGET for q, _ in trace)
            is_heavy = q_target > L
            true_visit = any(q[0] == "B" and q[2] == TARGET and q[3] == address(U)
                             for q, _ in trace)
            sim = simulate(J, U)
            assert sim["target_queries_used"] <= L
            success = sim["guess"] == address(U)
            joint = not is_heavy and true_visit
            assert not joint or success
            counts["heavy_target"] += is_heavy
            counts["nonheavy_true_cell"] += joint
            counts["simulator_success"] += success
            for I in range(M):
                planted = oracle(J, A, I)
                assert total_function(planted) == 1
                # Exhaustively check the support of changed physical bits.
                for q in COORDINATES:
                    if dummy(q) != planted(q):
                        assert q == ("X", I, J[I]) or (
                            q[0] == "B" and q[2] == I and q[3] == address(A[I]))
                ptrace, pout = run(planted)
                erased_hit = I in discovered
                cell_hit = any(q[0] == "B" and q[2] == I and q[3] == address(A[I])
                               for q, _ in trace)
                if out != pout:
                    assert erased_hit or cell_hit
                counts["erased_zero_hits"] += erased_hit
                counts["true_cell_hits"] += cell_hit
                counts["output_disagreements"] += (out != pout)
                counts["signed_output_gap"] += pout - out
                counts["heavy_selected"] += (I == TARGET and is_heavy)
    ez = Fraction(counts["sum_Z"], dummy_count)
    phit = Fraction(counts["erased_zero_hits"], coupled_count)
    assert phit == ez / M
    assert ez <= Fraction(2 * G, M)
    assert Fraction(counts["sum_early"], dummy_count) <= Fraction(2 * G, M)
    xor_beta = one_query_optimum(BITS, parity)
    assert xor_beta == Fraction(1, 2)
    psim = Fraction(counts["simulator_success"], dummy_count)
    pjoint = Fraction(counts["nonheavy_true_cell"], dummy_count)
    assert pjoint <= psim <= xor_beta ** R
    signed_gap = Fraction(counts["signed_output_gap"], coupled_count)
    assert abs(signed_gap) == Fraction(counts["output_disagreements"], coupled_count)
    assert signed_gap == Fraction(counts["true_cell_hits"], coupled_count)

    # Supplemental counterexample: conditioning on nonheaviness is unsafe.
    # This uses a different toy P, explicitly labelled, because the uniform
    # XOR toy has no such bias after a one-bit target transcript.
    and_inputs = ((0, 1), (1, 0), (1, 1))
    and_function = lambda u: u[0] & u[1]
    and_beta = one_query_optimum(and_inputs, and_function)
    assert and_beta == Fraction(2, 3)
    selection_cases = []
    for u in and_inputs:
        # Full algorithm: stop after first bit if it is 0; otherwise read both.
        qcount = 1 if u[0] == 0 else 2
        nonheavy = qcount <= 1
        # Capped simulator/default output is always 0.
        success = and_function(u) == 0
        selection_cases.append({"input": u, "P": and_function(u), "full_query_count": qcount,
                                "nonheavy": nonheavy, "capped_guess": 0,
                                "capped_success": success})
    nh = sum(row["nonheavy"] for row in selection_cases)
    joint = sum(row["nonheavy"] and row["capped_success"] for row in selection_cases)
    success = sum(row["capped_success"] for row in selection_cases)
    assert Fraction(joint, nh) == 1
    assert Fraction(joint, 3) <= Fraction(success, 3) == and_beta

    data = {
        "schema": "quartic_r3_planted_toy_v1",
        "parameters": {"m": M, "ell": ELL, "r": R, "L": L, "G": G,
                       "n": 2, "S": 2, "coordinate_count": len(COORDINATES)},
        "limits": ["Finite illustration only; r=2 differs from the theorem's r=40t.",
                   "G=4 is not floor(mL/100), which is zero for these toy parameters.",
                   "P is two-bit XOR, not Forrelation.",
                   "Enumerated measure fixes other columns' A inputs, conditions appropriate for the fixed-target simulator; target inputs are independent uniform two-bit strings.",
                   "No Lean compilation, Comparator result, or asymptotic proof is certified."],
        "circuit": {"gate_0": "constant 1 (domain output)",
                    "gate_1": "XOR(input0,input1) (value output)",
                    "transcript_order": ["domain", "value"]},
        "sample": sample,
        "exact_enumeration": {
            "dummy_samples": dummy_count, "coupled_samples": coupled_count,
            "changed_coordinate_checks": coupled_count * len(COORDINATES),
            "counts": counts,
            "E_Z": frac(ez), "Pr_hit_erased_zero": frac(phit), "E_Z_over_m": frac(ez / M),
            "Pr_hit_true_cell": frac(Fraction(counts["true_cell_hits"], coupled_count)),
            "output_one_probability_gap": frac(signed_gap),
            "Pr_fixed_target_nonheavy_and_true_cell_at_time4": frac(pjoint),
            "Pr_capped_simulator_correct": frac(psim),
            "one_instance_one_query_optimum": frac(xor_beta),
            "direct_product_bound": frac(xor_beta ** R),
            "Pr_target_heavy": frac(Fraction(counts["heavy_target"], dummy_count)),
            "Pr_selected_column_heavy": frac(Fraction(counts["heavy_selected"], coupled_count)),
            "early_late_partition_checked": True,
            "coupling_support_checked": True,
            "zero_one_input_values_checked": True,
            "joint_event_implies_capped_success_checked": True,
        },
        "selection_bias_counterexample": {
            "P": "AND on promised domain {01,10,11}",
            "mu": "uniform on the three promised inputs", "r": 1, "L": 1,
            "one_query_optimum": frac(and_beta), "cases": selection_cases,
            "Pr_nonheavy": frac(Fraction(nh, 3)),
            "Pr_correct_and_nonheavy": frac(Fraction(joint, 3)),
            "Pr_capped_correct": frac(Fraction(success, 3)),
            "Pr_correct_given_nonheavy": frac(Fraction(joint, nh)),
            "lesson": "The joint event is bounded by 2/3; the conditional success is 1, so a direct-product bound cannot be applied after conditioning on nonheaviness.",
        },
    }
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({"output": str(output), "dummy_samples": dummy_count,
                      "coupled_samples": coupled_count, "E_Z": str(ez),
                      "Pr_hit_erased_zero": str(phit), "simulator_success": str(psim),
                      "nonheavy_joint_event": str(pjoint), "assertions": "passed"}))


if __name__ == "__main__":
    main()
