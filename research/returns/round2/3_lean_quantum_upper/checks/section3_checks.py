#!/usr/bin/env python3
"""Finite, reproducible checks of Section 3 mathematics; not Lean verification.

Exact rational arithmetic checks drift and whole-list laws. Floating-point checks
exercise state formulas and parameter bounds. Negative controls deliberately
violate one condition and must be detected. No test establishes an infinite
quantifier or compilation of the proposed Lean source.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product, combinations
from collections import defaultdict
from pathlib import Path
import json, math, random, sys
import numpy as np

rng = random.Random(20261102)
report = {"kind": "finite_mathematical_checks", "lean_compiled": False,
          "seed": 20261102, "python": sys.version.split()[0],
          "numpy": np.__version__, "checks": {}, "negative_controls": {}}


def comparison(m, upper):
    a = [[F(0) for _ in range(m)] for _ in range(m)]
    for (i,j), p in zip(combinations(range(m), 2), upper):
        a[i][j], a[j][i] = p, 1-p
    return a


def drift(a, w):
    total = sum(w)
    return sum(w[p] / total * sum(w[i]*a[i][p] for i in range(len(w)))
               for p in range(len(w)))

vals = [F(0), F(1,3), F(1,2), F(2,3), F(1)]
weights = [F(0), F(1,2), F(1), F(3,2)]
drift_count = 0
for probs in product(vals, repeat=3):
    a = comparison(3, probs)
    for w in product(weights, repeat=3):
        total = sum(w)
        if not total:
            continue
        value = drift(a,w)
        assert value == (total*total-sum(q*q for q in w))/(2*total)
        assert value <= total/2
        drift_count += 1
report["checks"]["drift_exact"] = {"cases": drift_count, "passed": True}
a_bad = [[F(0) if i==j else F(9,10) for j in range(3)] for i in range(3)]
bad_drift = drift(a_bad, [F(1)]*3)
assert bad_drift > F(3,2)
report["negative_controls"]["noncomplementary_drift"] = {
    "detected": True, "expected_new_weight": str(bad_drift), "half_old_weight": "3/2"}


def enumerate_lists(a, cap, failure):
    """Forward enumeration of every stop/output branch; exact probabilities."""
    m = len(a)
    live = {(): F(1)}
    returned = defaultdict(F)
    for step in range(cap):
        nxt = defaultdict(F)
        for history, mass in live.items():
            w = [math.prod(a[i][p] for p in history) for i in range(m)]
            total = sum(w)
            if not total:
                returned[history] += mass
                continue
            f = failure(history)
            assert 0 <= f <= 1
            returned[history] += mass*f
            for pivot,wp in enumerate(w):
                if wp:
                    nxt[history+(pivot,)] += mass*(1-f)*wp/total
        live = nxt
    for history, mass in live.items():
        returned[history] += mass
    assert sum(returned.values()) == 1
    assert all(len(history)<=cap for history in returned)
    return dict(returned)

coupling_count = 0
for m in [2,3,4]:
    eps = F(1,50)
    for sample in range(40):
        a = comparison(m, [F(rng.randrange(21),20) for _ in combinations(range(m),2)])
        for j in range(1,m):
            a[0][j] = 1-F(rng.randrange(3),100)
            a[j][0] = 1-a[0][j]
        for cap in [0,1,2,3,4,6,12]:
            ideal = enumerate_lists(a,cap,lambda history:F(0))
            # Depends on the entire ordered history. After the winner is listed,
            # termination is allowed with probability one without losing it.
            def fail(history):
                if 0 in history:
                    return F(1)
                code = sum((j+1)*(v+1) for j,v in enumerate(history))
                return eps*F(code%3,2)
            real = enumerate_lists(a,cap,fail)
            miss0 = sum(q for h,q in ideal.items() if 0 not in h)
            miss1 = sum(q for h,q in real.items() if 0 not in h)
            assert miss1 <= miss0 + cap*eps
            assert miss0 <= F(2*m,2**cap)
            assert miss1 <= F(2*m,2**cap) + cap*eps
            assert all(len(set(h))==len(h) for h,q in real.items() if q)
            coupling_count += 1
report["checks"]["history_dependent_list_law_exact"] = {
    "cases": coupling_count, "max_stages": 12, "passed": True,
    "covers": ["normalization", "length", "zero total", "stop after winner",
               "history-dependent failure", "ideal miss", "actual miss"]}

# Explicit matrix rotation on complex states, independent of the scalar recurrence.
state_count = 0
max_state_error = 0.0
np_rng = np.random.default_rng(20261102)
for p in [0.0,1.0,0.25,0.5,0.01,0.9]+list(np_rng.random(60)):
    good = np_rng.normal(size=2)+1j*np_rng.normal(size=2)
    bad = np_rng.normal(size=2)+1j*np_rng.normal(size=2)
    good /= np.linalg.norm(good)
    bad /= np.linalg.norm(bad)
    g, b = np.r_[good,[0j,0j]], np.r_[[0j,0j],bad]
    psi = math.sqrt(p)*g + math.sqrt(1-p)*b
    flip = np.diag([-1,-1,1,1])
    grover = (2*np.outer(psi,psi.conj())-np.eye(4)) @ flip
    theta = math.asin(math.sqrt(p))
    actual = psi.copy()
    for ell in range(16):
        expected = math.sin((2*ell+1)*theta)*g + math.cos((2*ell+1)*theta)*b
        error = float(np.linalg.norm(actual-expected))
        assert error < 2e-12
        max_state_error = max(max_state_error,error)
        projected = actual.copy(); projected[2:] = 0
        mass = float(np.vdot(projected,projected).real)
        if p > 0 and mass > 1e-22:
            normalized = projected/math.sqrt(mass)
            assert np.linalg.norm(np.outer(normalized,normalized.conj())-np.outer(g,g.conj())) < 2e-12
        actual = grover @ actual
        state_count += 1
report["checks"]["grover_full_state_numeric"] = {
    "cases": state_count, "max_l2_error": max_state_error, "passed": True,
    "covers": ["p=0", "p=1", "global phase", "conditional pure state"]}

# Fresh comparisons and a short-circuit circuit have the same all-success
# amplitudes, yet generally different complete states.
def fresh_and_short(probs):
    t = len(probs)
    basis = list(product([0,1],repeat=t))
    fresh = np.array([math.prod(math.sqrt(p if bit else 1-p)
                              for p,bit in zip(probs,bits)) for bits in basis])
    short = np.zeros(2**t)
    for idx,bits in enumerate(basis):
        amp = 1.0; live = True
        for p,bit in zip(probs,bits):
            if live:
                amp *= math.sqrt(p if bit else 1-p)
                live = bool(bit)
            elif bit:
                amp = 0.0; break
        short[idx] = amp
    return fresh,short
f,s = fresh_and_short([0.5,0.5])
assert abs(np.linalg.norm(f)-1)<1e-14 and abs(np.linalg.norm(s)-1)<1e-14
assert abs(f[-1]**2-s[-1]**2)<1e-14
assert np.linalg.norm(f-s)>0.5
report["negative_controls"]["same_success_law_different_full_state"] = {
    "detected": True, "fresh_amplitudes": f.tolist(), "short_circuit_amplitudes": s.tolist(),
    "successful_probability_both": float(f[-1]**2), "full_state_l2_distance": float(np.linalg.norm(f-s))}

average_count = 0
for gamma in [0.5,0.25,0.05,0.001,0.00001]:
    M = math.ceil(10/math.sqrt(gamma))
    for p in np.linspace(gamma,0.5,101):
        theta = math.asin(math.sqrt(float(p)))
        avg = float(np.mean(np.sin((2*np.arange(M)+1)*theta)**2))
        middle = 0.5-1/(2*M*abs(math.sin(2*theta)))
        assert avg+1e-12 >= middle >= 0.45-1e-12
        assert 0.5*p+0.5*avg >= 9/40-1e-12
        average_count+=1
report["checks"]["equation_9_numeric"]={"cases":average_count,"passed":True}

budget_count=0
max_budget_ratio=0.0
for m in [2,3,4,7,10,16,31,100,1000,10**6,10**9]:
    T=(1000*m-1).bit_length()
    eps=1/(1000*T)
    M=math.ceil(10*math.sqrt(2*m))
    trials=math.ceil(math.log(1/eps)/math.log(40/31))
    for c in [1,2,7,100]:
        cap=2*c*T*T*trials*(2*M+1)
        bound=6072*c*math.sqrt(m)*T*T*math.log(T)
        assert cap <= bound
        max_budget_ratio=max(max_budget_ratio,cap/bound)
        budget_count+=1
    numeric_error=F(2*m,2**T)+F(1,1000)+F(1,1000*T)
    assert numeric_error < F(1,3)
report["checks"]["tournament_cap_numeric"]={"cases":budget_count,"max_ratio":max_budget_ratio,"passed":True}

report["all_passed"]=True
report["limitations"]=[
    "No Lean elaboration, kernel checking or Comparator run was performed.",
    "Finite cases and floating-point probes do not prove universal claims.",
    "The explicit noncomplementary matrix and unequal tensor states are negative controls, not failures of the source theorem."
]
out=Path(__file__).with_name('mathematical_checks.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
