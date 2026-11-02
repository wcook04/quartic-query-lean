#!/usr/bin/env python3
"""Exact finite illustration of the addressed construction (Python stdlib only).

Run: python3 check_example.py
Optional: python3 check_example.py --write-data DIR

This uses the actual promise P_{2,4}, but uses r=2 address instances instead
of the paper's r=40.  Its two-output circuit is synthesized from a truth table;
it is not the paper's asymptotically efficient Walsh arithmetic circuit.
Neither this example nor these finite checks establish a query separation.

Internal columns, rows, inputs and gates are zero based.  Displayed columns
and rows are one based.  Address and pointer bit strings are big endian.
One physical bit query means one call to Reader.read, including repeated reads.
"""

from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


M, ELL, R, INPUT_BITS = 4, 2, 2, 8
ADDRESSES = tuple(product((0, 1), repeat=R))
INPUTS = tuple(product((0, 1), repeat=INPUT_BITS))
W = tuple(tuple((-1) ** ((i & j).bit_count()) for j in range(M)) for i in range(M))
ZERO = ("constant", 0)
ONE = ("constant", 1)


def word(bits):
    return "".join(map(str, bits))


def unword(bits):
    return tuple(int(c) for c in bits)


def numerator(bits):
    """N=z_1^T W z_2, using signs (-1)^bit and unnormalized Walsh W."""
    return sum((-1) ** (bits[i] + bits[M + j]) * W[i][j]
               for i in range(M) for j in range(M))


def partial(bits):
    """Use the original integer promise comparisons, not rounded decimals."""
    n = numerator(bits)
    if (2 ** 10) * n >= 8:
        return 1
    if (2 ** 11) * abs(n) <= 8:
        return 0
    return None


def rational_reference(bits):
    """Independent normalized matrix-vector evaluation and rational thresholds."""
    z1 = [1 - 2 * a for a in bits[:M]]
    z2 = [1 - 2 * a for a in bits[M:]]
    hz2 = [sum(Fraction(W[i][j], 2) * z2[j] for j in range(M))
           for i in range(M)]
    phi = sum(z1[i] * hz2[i] for i in range(M)) / M
    delta = Fraction(1, 2 ** 10)
    answer = 1 if phi >= delta else 0 if abs(phi) <= delta / 2 else None
    return phi, answer


def apply_gate(op, left, right):
    if op == "and":
        return left & right
    if op == "or":
        return left | right
    if op == "not":
        return 1 - left
    if op == "copy":
        return left
    raise ValueError(op)


class Circuit:
    """Shared Shannon synthesis; every gate has at most two predecessors."""

    def __init__(self):
        self.gates = []
        self.gate_cache = {}
        self.table_cache = {}
        values = [partial(bits) for bits in INPUTS]
        domain = self.synthesize(tuple(int(v is not None) for v in values), 0)
        value = self.synthesize(tuple(int(v == 1) for v in values), 0)
        # Include two distinct non-input output gates in the transcript count.
        self.d = self.gate("copy", domain, ZERO, fresh=True)[1]
        self.b = self.gate("copy", value, ZERO, fresh=True)[1]

    def gate(self, op, left, right=ZERO, *, fresh=False):
        key = (op, left, right)
        if not fresh and key in self.gate_cache:
            return self.gate_cache[key]
        ref = ("gate", len(self.gates))
        self.gates.append(key)
        if not fresh:
            self.gate_cache[key] = ref
        return ref

    def synthesize(self, table, depth):
        key = (depth, table)
        if key in self.table_cache:
            return self.table_cache[key]
        if all(v == table[0] for v in table):
            out = ONE if table[0] else ZERO
        else:
            half = len(table) // 2
            low = self.synthesize(table[:half], depth + 1)
            high = self.synthesize(table[half:], depth + 1)
            variable = ("input", depth)
            if low == high:
                out = low
            elif low == ZERO and high == ONE:
                out = variable
            elif low == ONE and high == ZERO:
                out = self.gate("not", variable)
            elif low == ZERO:
                out = self.gate("and", variable, high)
            elif high == ZERO:
                out = self.gate("and", self.gate("not", variable), low)
            elif low == ONE:
                out = self.gate("or", self.gate("not", variable), high)
            elif high == ONE:
                out = self.gate("or", variable, low)
            else:
                left = self.gate("and", self.gate("not", variable), low)
                right = self.gate("and", variable, high)
                out = self.gate("or", left, right)
        self.table_cache[key] = out
        return out

    def evaluate(self, bits):
        transcript = []

        def get(ref):
            kind, index = ref
            if kind == "input":
                return bits[index]
            if kind == "gate":
                return transcript[index]
            return index

        for op, left, right in self.gates:
            transcript.append(apply_gate(op, get(left), get(right)))
        return tuple(transcript)

    def as_json(self):
        return {
            "input_bits": INPUT_BITS,
            "non_input_gates": len(self.gates),
            "domain_output_gate": self.d,
            "value_output_gate": self.b,
            "gates": [dict(index=g, op=op, left=left, right=right)
                      for g, (op, left, right) in enumerate(self.gates)],
        }


PLUS = unword("00000000")
ZERO_CASE = unword("00010010")
MINUS = unword("11110000")


def make_board(circuit):
    xs = [(1, 1, 1, 1), (0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1)]
    instances = [(PLUS, ZERO_CASE), (MINUS, ZERO_CASE),
                 (PLUS, ZERO_CASE), (PLUS, ZERO_CASE)]
    columns = []
    for i in range(M):
        cells = {}
        for address in ADDRESSES:
            pointers = {}
            for j in range(M):
                if j == i:
                    continue
                # Rivals' pointers into the all-one column traverse all four
                # rows as the proposed address varies. Other pointers hit zeros.
                target = int(word(address), 2) if j == 0 else xs[j].index(0)
                pointers[j] = unword(f"{target:02b}")
            cells[address] = {
                "pointers": pointers,
                "transcripts": tuple(circuit.evaluate(a) for a in instances[i]),
            }
        columns.append({"X": xs[i], "A": instances[i], "cells": cells})
    return columns


class Reader:
    def __init__(self, board):
        self.board = board
        self.history = []

    def read(self, location):
        self.history.append(location)
        kind, i, *rest = location
        column = self.board[i]
        if kind == "X":
            return column["X"][rest[0]]
        if kind == "A":
            h, q = rest
            return column["A"][h][q]
        address, h_or_j, q = rest
        cell = column["cells"][address]
        if kind == "pointer":
            return cell["pointers"][h_or_j][q]
        if kind == "transcript":
            return cell["transcripts"][h_or_j][q]
        raise ValueError(location)


def indices(circuit):
    """The index list depends on sizes only, not on i, s or the input."""
    out = [("column", q) for q in range(M)]
    out += [("pointer", j) for j in range(M - 1)]
    out += [("gate", h, g) for h in range(R) for g in range(len(circuit.gates))]
    out += [("domain", h) for h in range(R)]
    out += [("value", h) for h in range(R)]
    return tuple(out)


def local_test(reader, circuit, i, address, index):
    kind, *arg = index
    if kind == "column":
        return reader.read(("X", i, arg[0]))
    if kind == "pointer":
        rank = arg[0]
        j = rank if rank < i else rank + 1
        pointer_bits = tuple(reader.read(("pointer", i, address, j, q))
                             for q in range(ELL))
        target = int(word(pointer_bits), 2)
        return 1 - reader.read(("X", j, target))
    h = arg[0]
    if kind == "domain":
        return reader.read(("transcript", i, address, h, circuit.d))
    if kind == "value":
        return int(reader.read(("transcript", i, address, h, circuit.b)) == address[h])
    g = arg[1]
    claimed = reader.read(("transcript", i, address, h, g))

    def get(ref):
        origin, q = ref
        if origin == "constant":
            return q
        if origin == "input":
            return reader.read(("A", i, h, q))
        return reader.read(("transcript", i, address, h, q))

    op, left, right = circuit.gates[g]
    return int(claimed == apply_gate(op, get(left), get(right)))


def test_summary(board, circuit, i, address):
    by_family = {name: {"pass": 0, "total": 0, "max_queries": 0}
                 for name in ("column", "pointer", "gate", "output")}
    for index in indices(circuit):
        reader = Reader(board)
        result = local_test(reader, circuit, i, address, index)
        family = index[0] if index[0] in by_family else "output"
        counts = by_family[family]
        counts["pass"] += result
        counts["total"] += 1
        counts["max_queries"] = max(counts["max_queries"], len(reader.history))
        assert len(reader.history) <= max(3, ELL + 1)
    return by_family


def semantic_winner(board, circuit, i, address):
    """Direct paper condition, without calling the local-test evaluator."""
    column = board[i]
    values = tuple(rational_reference(bits)[1] for bits in column["A"])
    if None in values or address != values or column["X"] != (1,) * M:
        return False
    cell = column["cells"][address]
    if cell["transcripts"] != tuple(circuit.evaluate(a) for a in column["A"]):
        return False
    return all(board[j]["X"][int(word(pointer), 2)] == 0
               for j, pointer in cell["pointers"].items())


def total_value(board, circuit):
    return int(any(semantic_winner(board, circuit, i, address)
                   for i in range(M) for address in ADDRESSES))


def change_transcript_bit(board, i, address, h, g):
    changed = deepcopy(board)
    transcripts = [list(t) for t in changed[i]["cells"][address]["transcripts"]]
    transcripts[h][g] ^= 1
    changed[i]["cells"][address]["transcripts"] = tuple(tuple(t) for t in transcripts)
    return changed


def pointer_support():
    """Exhaustively witness essentiality of all 2+4 pointer-test coordinates."""
    configurations = tuple(product((0, 1), repeat=ELL + M))

    def test(bits):
        return 1 - bits[ELL + 2 * bits[0] + bits[1]]

    witnesses = []
    for q in range(ELL + M):
        found = None
        for before in configurations:
            after = list(before)
            after[q] ^= 1
            if test(before) != test(after):
                found = {
                    "coordinate": f"p{q}" if q < ELL else f"X[{q - ELL + 1}]",
                    "before": word(before), "after": word(after),
                    "before_test": test(before), "after_test": test(after),
                }
                break
        assert found is not None
        witnesses.append(found)
    return {"configurations": len(configurations), "essential_coordinates": len(witnesses),
            "adaptive_depth": ELL + 1, "witnesses": witnesses}


def comparison_checks(board):
    """Condition on the winner's correct label, vary every rival label/target."""
    cases = 0
    for j in range(1, M):
        for rival_address in ADDRESSES:
            for incoming_target in range(M):
                outgoing = board[0]["cells"][(1, 0)]["pointers"][j]
                rival_disqualified = board[j]["X"][int(word(outgoing), 2)] == 0
                winner_disqualified = board[0]["X"][incoming_target] == 0
                # All 4 rival labels and all 4 possible stored pointers covered.
                assert rival_address in board[j]["cells"]
                assert rival_disqualified and not winner_disqualified
                cases += 1
    return {"rivals": M - 1, "rival_labels": len(ADDRESSES),
            "incoming_pointer_targets": M, "cases": cases,
            "winner_selected_in_all_cases": True,
            "condition": "winner label is its true address 10"}


def projection_decoder_check():
    """Only the specified projection-outcome decoder; not all algorithms."""
    phi_positive, _ = rational_reference(PLUS)
    phi_negative, _ = rational_reference(MINUS)
    p_positive = phi_positive ** 2
    p_negative = phi_negative ** 2
    assert p_positive == p_negative == Fraction(1, 4)
    # An explicit finite illustration of the product law. The arbitrary fixed
    # repetition-count claim follows algebraically from equal Bernoulli laws.
    patterns = {}
    for outcomes in product((0, 1), repeat=3):
        successes = sum(outcomes)
        positive_mass = p_positive ** successes * (1 - p_positive) ** (3 - successes)
        negative_mass = p_negative ** successes * (1 - p_negative) ** (3 - successes)
        assert positive_mass == negative_mass
        patterns[word(outcomes)] = str(positive_mass)
    assert sum(Fraction(mass) for mass in patterns.values()) == 1
    return {
        "positive_input": word(PLUS),
        "off_promise_input": word(MINUS),
        "Phi_positive": str(phi_positive),
        "Phi_off_promise": str(phi_negative),
        "equal_projection_success_probability": str(p_positive),
        "single_trial_law_on_both_inputs": {"failure": "3/4", "success": "1/4"},
        "three_independent_trials_ordered_pattern_masses_on_both_inputs": patterns,
        "ordinary_deduction": "For any fixed n, each ordered outcome pattern with h successes has mass (1/4)^h (3/4)^(n-h) on both inputs. Any decision rule using only these outcomes has the same output law.",
        "scope": "The preprint's projection decoder and independent repetitions using only its projection outcomes; no claim about all quantum algorithms.",
    }


def domain_omission_check(board, circuit):
    """An off-promise all-one column passes every test except its domain bit."""
    changed = deepcopy(board)
    changed[0]["X"] = (1, 1, 1, 0)
    changed[1]["X"] = (1, 1, 1, 1)
    # The off-promise column is now the sole all-one column. Every pointer
    # directed into a different column is chosen to hit that column's zero.
    for i, column in enumerate(changed):
        for address, cell in column["cells"].items():
            for j in cell["pointers"]:
                target = int(word(address), 2) if j == 1 else changed[j]["X"].index(0)
                cell["pointers"][j] = unword(f"{target:02b}")
    full = test_summary(changed, circuit, 1, (0, 0))
    assert full["column"]["pass"] == M
    assert full["pointer"]["pass"] == M - 1
    assert full["gate"]["pass"] == R * len(circuit.gates)
    assert full["output"]["pass"] == 3
    without_domain = [index for index in indices(circuit) if index[0] != "domain"]
    assert all(local_test(Reader(changed), circuit, 1, (0, 0), index)
               for index in without_domain)
    assert total_value(changed, circuit) == 0
    return {"column_X_strings": [word(c["X"]) for c in changed],
            "candidate": {"column": 2, "proposed_address": "00"},
            "full_test_counts": full,
            "tests_without_domain_checks": len(without_domain),
            "all_tests_without_domain_checks_pass": True,
            "semantic_F": 0,
            "explanation": "Correct transcripts of an off-promise input have d=0. Its domain test is the sole failed test."}


def board_json(board):
    return [{"column": i + 1, "X": word(c["X"]),
             "A": [word(a) for a in c["A"]],
             "cells": {word(s): {
                 "pointer_words_to_columns": {str(j + 1): word(p)
                                               for j, p in cell["pointers"].items()},
                 "transcripts": [word(t) for t in cell["transcripts"]],
             } for s, cell in c["cells"].items()}}
            for i, c in enumerate(board)]


def run():
    circuit = Circuit()
    s = len(circuit.gates)
    assert circuit.d != circuit.b
    for g, (_, left, right) in enumerate(circuit.gates):
        for origin, q in (left, right):
            assert origin != "gate" or q < g
            assert origin != "input" or 0 <= q < INPUT_BITS
    distribution = Counter()
    for bits in INPUTS:
        phi, value = rational_reference(bits)
        assert phi == Fraction(numerator(bits), 8)
        assert value == partial(bits)
        transcript = circuit.evaluate(bits)
        assert transcript[circuit.d] == int(value is not None)
        assert transcript[circuit.b] == int(value == 1)
        distribution[str(phi)] += 1

    board = make_board(circuit)
    rows, winners = [], []
    ktests = M + (M - 1) + R * (s + 2)
    assert len(indices(circuit)) == ktests
    for i in range(M):
        for address in ADDRESSES:
            counts = test_summary(board, circuit, i, address)
            passing = sum(c["pass"] for c in counts.values())
            local_winner = passing == ktests
            assert semantic_winner(board, circuit, i, address) == local_winner
            if local_winner:
                winners.append({"column": i + 1, "address": word(address)})
            rows.append({"column": i + 1, "address": word(address),
                         "passing_tests": passing, "total_tests": ktests,
                         "by_family": counts})
    assert winners == [{"column": 1, "address": "10"}]
    assert total_value(board, circuit) == 1

    # Changing one selected transcript bit always breaks its own gate equation.
    # This is an exhaustive single-flip check, not all possible corruptions.
    for h in range(R):
        for g in range(s):
            damaged = change_transcript_bit(board, 0, (1, 0), h, g)
            reader = Reader(damaged)
            assert local_test(reader, circuit, 0, (1, 0), ("gate", h, g)) == 0
            assert total_value(damaged, circuit) == 0

    # The off-promise rival can forge d=1 in an alleged transcript, but then
    # the changed output gate fails its gate-consistency test.
    forged = change_transcript_bit(board, 1, (0, 0), 0, circuit.d)
    forged_counts = test_summary(forged, circuit, 1, (0, 0))
    assert forged_counts["output"]["pass"] == 4
    assert forged_counts["gate"]["pass"] == 2 * s - 1
    assert not semantic_winner(forged, circuit, 1, (0, 0))

    reader = Reader(board)
    assert local_test(reader, circuit, 0, (1, 0), ("pointer", 2)) == 1
    pointer_history = reader.history
    samples = []
    for name, bits in (("positive", PLUS), ("zero", ZERO_CASE), ("off_promise", MINUS)):
        transcript = circuit.evaluate(bits)
        phi, value = rational_reference(bits)
        samples.append({"name": name, "bits": word(bits), "N": numerator(bits),
                        "Phi": str(phi), "P": value,
                        "domain_output": transcript[circuit.d],
                        "value_output": transcript[circuit.b],
                        "transcript": word(transcript)})

    summary = {
        "status": "all checks passed",
        "scope": {
            "promise": "actual P_{2,4}, delta=1/1024, exact rational arithmetic",
            "schematic_choices": "r=2 instead of r=40; truth-table circuit instead of asymptotic arithmetic circuit",
            "does_not_establish": "an asymptotic query separation, a Lean theorem, or arbitrary-board exhaustive validity",
            "bit_order": "big endian; displayed columns/rows one based, circuit gates zero based",
        },
        "parameters": {"k": 2, "m": M, "ell": ELL, "r": R,
                       "r_in_paper_at_m4": 40, "S": s, "K": ktests,
                       "input_bits": M * (M + R * INPUT_BITS + 2 ** R * ((M - 1) * ELL + R * s))},
        "walsh_integer_matrix": W,
        "exact_circuit": {"gate_count": s, "domain_gate": circuit.d, "value_gate": circuit.b,
                          "verified_inputs": len(INPUTS),
                          "Phi_histogram": dict(sorted(distribution.items()))},
        "instances": samples,
        "board_columns": [{"column": i + 1, "X": word(c["X"]),
                           "instance_bits": [word(a) for a in c["A"]],
                           "partial_values": [partial(a) for a in c["A"]]}
                          for i, c in enumerate(board)],
        "winner": winners[0],
        "winner_outward_pointer_words": {
            str(j + 1): word(p) for j, p in board[0]["cells"][(1, 0)]["pointers"].items()},
        "candidate_checks": rows,
        "local_tests_evaluated_on_base_board": M * len(ADDRESSES) * ktests,
        "single_selected_transcript_bit_flips_checked": R * s,
        "single_flip_total_function_values": "all zero",
        "forged_rival_domain_output": {"column": 2, "proposed_address": "00",
                                       "by_family": forged_counts},
        "example_pointer_read_history": pointer_history,
        "pointer_support_check": pointer_support(),
        "comparison_check": comparison_checks(board),
        "projection_decoder_equal_law": projection_decoder_check(),
        "domain_omission_counterexample": domain_omission_check(board, circuit),
        "F_on_base_board": total_value(board, circuit),
    }
    return summary, circuit.as_json(), board_json(board)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-data", type=Path, help="also write circuit.json and board.json here")
    args = parser.parse_args()
    summary, circuit, board = run()
    if args.write_data:
        args.write_data.mkdir(parents=True, exist_ok=True)
        for filename, data in (("circuit.json", circuit), ("board.json", board)):
            (args.write_data / filename).write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
