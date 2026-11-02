"""Exact finite check of a four-candidate probabilistic tournament.

This is an independent arithmetic illustration, not a Lean or quantum-circuit
check. It uses Fraction throughout. The optional artificial stage-failure law
is admissible but is not asserted to equal the packet's physical amplifier.
"""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import json

NAMES = ("s", "a", "b", "c")
M = 4
T = 12  # least integer with 2**T >= 1000*M
EPS = F(1, 1000*T)
Q = 1-EPS
A = (
    (F(0), Q, Q, Q),
    (EPS, F(0), F(1), F(0)),
    (EPS, F(0), F(0), F(1)),
    (EPS, F(1), F(0), F(0)),
)


def weights(history):
    w = [F(1) for _ in range(M)]
    for p in history:
        w = [v*A[i][p] for i, v in enumerate(w)]
    return w


def advance(law, artificial_failure=False):
    out = defaultdict(F)
    for (history, stopped), mass in law.items():
        w = weights(history)
        total = sum(w, F(0))
        if stopped or total == 0:
            out[history, True] += mass
            continue
        fail = EPS if artificial_failure else F(0)
        out[history, True] += mass*fail
        for p, wp in enumerate(w):
            if wp:
                out[history+(p,), False] += mass*(1-fail)*wp/total
    return {h:p for h,p in out.items() if p}


def miss(law):
    return sum((p for (history,_),p in law.items() if 0 not in history), F(0))


def main():
    assert 2**(T-1) < 1000*M <= 2**T
    assert all(A[i][i] == 0 for i in range(M))
    assert all(0 <= v <= 1 for row in A for v in row)
    assert all(A[i][j]+A[j][i] == 1 for i in range(M) for j in range(M) if i != j)
    assert all(A[0][j] >= 1-EPS for j in range(1,M))
    assert A[1][2] == A[2][3] == A[3][1] == 1

    ideal = {((),False):F(1)}
    real = {((),False):F(1)}
    rows = []
    tested_histories = set()
    for step in range(T+1):
        assert sum(ideal.values(), F(0)) == sum(real.values(), F(0)) == 1
        assert all(p >= 0 for p in list(ideal.values())+list(real.values()))
        assert all(len(h) == len(set(h)) for h,_ in ideal)
        assert miss(real) <= miss(ideal)+step*EPS
        expected_weight = sum((mass*sum(weights(h),F(0)) for (h,_),mass in ideal.items()),F(0))
        assert expected_weight <= F(M,2**step)
        rows.append({"step":step,"ideal_miss":str(miss(ideal)),"artificial_failure_miss":str(miss(real)),"ideal_expected_total_weight":str(expected_weight)})
        for history,_ in ideal:
            tested_histories.add(history)
            w = weights(history)
            total = sum(w,F(0))
            if total:
                direct_drift = sum((w[p]/total*sum((w[i]*A[i][p] for i in range(M)),F(0)) for p in range(M)),F(0))
                paired_drift = (total**2-sum((v*v for v in w),F(0)))/(2*total)
                assert direct_drift == paired_drift <= total/2
            if 0 not in history:
                assert w[0] >= Q**len(history) >= 1-len(history)*EPS
        if step < T:
            ideal = advance(ideal)
            real = advance(real, artificial_failure=True)

    assert rows[1]["ideal_miss"] == "3/4"
    assert F(rows[2]["ideal_miss"]) == F(3,4)/(2-EPS)
    assert all(F(r["ideal_miss"]) == 0 for r in rows[3:])
    exact_artificial_miss = EPS + (1-EPS)*F(3,4)*EPS + (1-EPS)**2*F(3,4)/(2-EPS)*EPS
    assert miss(real) == exact_artificial_miss
    assert miss(real) <= 3*EPS <= T*EPS

    w_a = weights((1,))
    W_a = sum(w_a,F(0))
    conditional_a = [w/W_a for w in w_a]
    assert W_a == F(23999,12000)
    assert conditional_a == [F(11999,23999),F(0),F(0),F(12000,23999)]
    after_ac = weights((1,3))
    assert after_ac == [Q**2,F(0),F(0),F(0)]

    # Negative control: at zero weight, setting f=0 would leave total mass zero.
    zero_history = (1,3,0)
    assert sum(weights(zero_history),F(0)) == 0
    totalized_division_wrong_mass = F(0) + (1-F(0))*F(0)
    assert totalized_division_wrong_mass != 1

    result = {
      "status":"passed",
      "scope":"finite exact rational illustration only; no universal proof, Lean build, or physical-circuit execution",
      "candidate_order":NAMES,
      "m":M,"T":T,"epsilon":str(EPS),
      "comparison_table":[[str(v) for v in row] for row in A],
      "cycle":"a beats b; b beats c; c beats a, each with probability one",
      "after_pivot_a":{"weights":[str(v) for v in w_a],"total":str(W_a),"stage_success":str(W_a/M),"conditional_index_law":[str(v) for v in conditional_a]},
      "after_pivots_a_c":{"weights":[str(v) for v in after_ac],"conditional_next_pivot":"s with probability one"},
      "initial_expected_next_total_weight":"3/2",
      "ideal_s_selected_by_third_pivot":True,
      "histories_with_checked_drift":len(tested_histories),
      "artificial_failure_law":"f(L)=epsilon when W(L)>0; f(L)=1 when W(L)=0; demonstration only",
      "artificial_failure_miss_exact":str(exact_artificial_miss),
      "zero_weight_negative_control_detected":True,
      "steps":rows,
    }
    dest=Path(__file__).with_name("tournament_example.json")
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ["status","histories_with_checked_drift","artificial_failure_miss_exact","after_pivot_a"]},indent=2))


if __name__ == "__main__":
    main()
