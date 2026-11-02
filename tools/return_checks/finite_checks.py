"""Small exact/numerical checks for the advisory design; NOT Lean proofs.

Run with Python 3 and NumPy. Generates finite_checks.json next to this script.
No theorem about all parameters or all quantum algorithms is established here.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
import math

import numpy as np


def forrelation_checks():
    m, k = 4, 2
    W = np.array([[(-1) ** ((i & j).bit_count()) for j in range(m)]
                  for i in range(m)], dtype=np.int64)
    assert np.array_equal(W @ W, m * np.eye(m, dtype=np.int64))
    checked = 0
    for signs in product((-1, 1), repeat=k*m):
        z = np.array(signs, dtype=np.int64).reshape((k, m))
        N = int(z[0] @ W @ z[1])
        M = m * math.isqrt(m) ** (k - 1)
        phi = F(N, M)
        delta = F(1, 2 ** (5*k))
        positive = 2 ** (5*k) * N >= M
        small = 2 ** (5*k+1) * abs(N) <= M
        assert positive == (phi >= delta)
        assert small == (abs(phi) <= delta/2)
        assert not (positive and small)
        assert -1 <= phi <= 1
        checked += 1
    return {"m": m, "k": k, "inputs_checked": checked,
            "result": "exact integer thresholds and Walsh orthogonality agree"}


def tournament_checks():
    m, T, eps = 6, 4, F(1, 100)
    a = [[F(0) for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(i + 1, m):
            a[i][j] = 1 - eps if i == 0 else F(1 + ((3*i+j) % 7), 9)
            a[j][i] = 1 - a[i][j]
    states = [(F(1), (F(1),)*m, False)]
    checked = 0
    for _ in range(T):
        next_states = []
        for prob, w, seen in states:
            W = sum(w)
            if not W:
                next_states.append((prob, w, seen))
                continue
            expectation = sum(w[p]/W * sum(w[i]*a[i][p] for i in range(m))
                              for p in range(m))
            assert expectation == (W*W-sum(v*v for v in w))/(2*W)
            assert expectation <= W/2
            checked += 1
            for p in range(m):
                if w[p]:
                    next_states.append((prob*w[p]/W,
                                        tuple(w[i]*a[i][p] for i in range(m)),
                                        seen or p == 0))
        states = next_states
    assert sum(p for p, _, _ in states) == 1
    expected = sum(p*sum(w) for p, w, _ in states)
    miss = sum(p for p, _, seen in states if not seen)
    assert expected <= F(m, 2**T)
    assert miss <= F(2*m, 2**T)
    assert all(seen or w[0] >= (1-eps)**T for _, w, seen in states)
    return {"m": m, "T": T, "eps": str(eps), "histories": len(states),
            "drift_instances": checked, "expected_final_weight": str(expected),
            "winner_miss_probability": str(miss), "result": "passed exactly"}


def capped_product_checks():
    inputs = tuple(product((0, 1), repeat=2))
    rows = []
    for name, f in [("AND", lambda x: x[0] & x[1]),
                    ("XOR", lambda x: x[0] ^ x[1])]:
        def best(r):
            @lru_cache(None)
            def value(domains, remaining):
                terminal = F(1)
                for d in domains:
                    count = sum(f(inputs[u]) for u in d)
                    terminal *= max(F(count, len(d)), F(len(d)-count, len(d)))
                candidates = [terminal]
                for h in range(r):
                    if not remaining[h]:
                        continue
                    for bit in range(2):
                        next_budget = list(remaining)
                        next_budget[h] -= 1
                        total = F(0)
                        for answer in (0, 1):
                            d = tuple(u for u in domains[h] if inputs[u][bit] == answer)
                            if not d:
                                continue
                            next_domains = list(domains)
                            next_domains[h] = d
                            total += F(len(d), len(domains[h])) * value(
                                tuple(next_domains), tuple(next_budget))
                        candidates.append(total)
                return max(candidates)
            return value((tuple(range(4)),)*r, (1,)*r)
        beta = best(1)
        for r in range(1, 4):
            actual = best(r)
            assert actual == beta**r
            rows.append({"function": name, "copies": r, "per_copy_cap": 1,
                         "optimal_success": str(actual), "beta_power": str(beta**r)})
    # Query x0; if x0=0, stop and output AND=0; otherwise query x1.
    # The nonheavy event (at most L=1 queries) is exactly x0=0.
    rows.append({"conditioning_counterexample": "AND, uniform two-bit input",
                 "unconditional_optimal_one_query_success": "3/4",
                 "adaptive_algorithm_success_given_nonheavy": "1",
                 "joint_nonheavy_and_success_probability": "1/2",
                 "conclusion": "conditioning on nonheavy invalidates the beta bound"})
    return rows


if __name__ == "__main__":
    result = {"kind": "finite checks, not formal proofs",
              "forrelation": forrelation_checks(),
              "tournament": tournament_checks(),
              "capped_product": capped_product_checks()}
    path = Path(__file__).with_name("finite_checks.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "pass", "output": str(path),
                      "scope": result["kind"]}))
