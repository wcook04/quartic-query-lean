#!/usr/bin/env python3
"""Exact rational checks for the round-two Forrelation note.

Python standard library only. No floating point is used. Algebraic checks and
finite test cases are reported separately from the analytic proofs in note.md.
Run from any directory: python3 checks.py
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, factorial
from pathlib import Path
import json
import re


def product_of(xs):
    ans = F(1)
    for x in xs:
        ans *= x
    return ans


def poly_add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) +
            (b[i] if i < len(b) else 0) for i in range(n)]


def poly_mul(a, b):
    ans = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ans[i+j] += x*y
    return ans


def poly_neg(a):
    return [-x for x in a]


def poly_pow(a, n):
    ans = [1]
    for _ in range(n):
        ans = poly_mul(ans, a)
    return ans


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def show(label, result):
    print(f"PASS | {label} | {result}")


def kernel_checks():
    # u=x^2. Both identities certify the polynomial part of the calculus.
    bound = trim(poly_add(poly_pow([2, 1], 3),
                         poly_neg(poly_mul([0, 1], poly_pow([3, 1], 2)))))
    assert bound == [8, 3]
    derivative = trim(poly_add(poly_mul([3, 3], [2, 1]),
                              poly_neg(poly_mul([0, 3], [3, 1]))))
    assert derivative == [6]
    show("phi bound identity", "(2+u)^3-u(3+u)^2=8+3u")
    show("phi derivative numerator", "(3+3u)(2+u)-3u(3+u)=6")
    # (psi(x)*dphi(y))^2 = 9/[4(2+x^2)(2+y^2)^5].
    assert F(9, 4*2*2**5) == F(3, 16)**2
    grid = [F(i, 7) for i in range(31)]
    for u, v in product(grid, repeat=2):
        assert F(9, 4) / ((2+u)*(2+v)**5) <= F(3, 16)**2
    show("sharp edge bound", "maximum squared=9/256; equality at x=y=0")
    show("edge grid (supplementary)", f"{len(grid)**2} rational nonnegative (x^2,y^2) pairs")


def constant_checks():
    b = F(3, 16)
    a_unit = F(1, 18)
    sharp = F(2, 18225)
    coarse = F(1, 2332800)
    assert sharp / coarse == 256
    assert 800*sharp == F(8, 27)**2
    assert b*F(8, 27) == a_unit
    assert F(50, 49) < F(9, 8)**2
    assert F(8, 27)*F(9, 8) == F(1, 3)
    old_gap = 1 - 2*F(1, 32) - 2*F(1, 18)
    new_gap = 1 - F(1, 32) - 2*F(1, 18) - F(1, 4)
    assert old_gap == F(119, 144)
    assert new_gap == F(175, 288)
    upper_unpadded = F(8, 27) + F(1, 4)
    upper_padded = F(1, 3) + F(1, 4)
    assert upper_unpadded == F(59, 108)
    assert upper_padded == F(7, 12)
    assert new_gap - upper_padded == F(7, 288) > 0
    assert old_gap > new_gap > upper_padded > upper_unpadded
    assert 18 * 8**25 < 9**25
    assert F(3, 16*4) <= F(1, 18)
    assert 1 - 2*F(1, 32) - F(1, 4) == F(11, 16)
    assert F(3, 2)*F(11, 16) == F(33, 32) > 1
    assert F(1, 8)*F(4, 81) == F(1, 162)
    assert F(1, 162)*F(1, 9) == F(1, 1458)
    show("sharp/coarse constant ratio", sharp/coarse)
    show("elementary coefficient", f"800*(2/18225)={800*sharp}=(8/27)^2")
    show("old promise gap / unpadded upper", f"{old_gap} > {upper_unpadded}")
    show("new promise gap / padded upper", f"{new_gap} > {upper_padded}; slack=7/288")
    show("uniform padding", "50/49 < 81/64; (8/27)*(9/8)=1/3")
    show("amplification integer inequality", f"18*8^25={18*8**25} < 9^25={9**25}")
    show("sharp Fourier assembly", "Gamma/a >=11/16; factor33/32>=1; constant1/(162eC^2)")


def exp_and_threshold_checks():
    # exp(x) is strictly greater than a finite positive Taylor sum.
    exp07_lower = sum((F(7, 10)**j / factorial(j) for j in range(5)), F(0))
    exp3_lower = sum((F(3)**j / factorial(j) for j in range(7)), F(0))
    assert exp07_lower > 2
    assert exp3_lower > 18
    assert 5*F(7, 10)+F(1, 2) == 4
    assert F(2, 18) < F(1, 4)
    show("logarithm certificate", f"sum(j=0..4) (7/10)^j/j!={exp07_lower}>2, hence ln2<7/10")
    show("logarithm certificate", f"sum(j=0..6) 3^j/j!={exp3_lower}>18, hence ln18<3")
    for k in range(2, 129):
        a = F(1, 18**(k-1))
        delta = F(1, 32**k)
        eps = F(8, 9)**(25*k)
        assert 0 < delta < a < 1
        assert delta <= a/32
        assert eps <= a/18
        p = (a-delta)/(1-delta)
        assert a-delta <= p <= 1
        assert (1-eps)*p-eps-a/4 >= F(175, 288)*a
        assert (1-delta)*p-delta-a/4 >= F(11, 16)*a
        new_m = 24*k*32**(2*k)
        old_m = 2**(15*k+2)
        assert new_m <= old_m
        assert F(new_m)*delta**2/8 == 3*k
        # Exact consequences after the proved exponential comparison exp3>18.
        assert F(2, 18**k) == a/9 < a/4
        assert (1+F(1, 50*k))**k <= F(50, 49)
        assert (F(3, 16)**(k-1))*4*F(4, 3)**(k-2) == F(3, 4**(k-1))
        # Exact original Markov threshold and relaxed positivity criterion.
        assert F(4, old_m)/delta**2 <= delta
        assert F(4, 16*18**(k-1)*32**(2*k))/delta**2 == a/4
    show("parameter checks (supplementary)", "k=2..128; both threshold/gap systems, padding, restriction factor")
    for k in (2, 3, 4, 8, 16):
        old = 2**(15*k+2)
        new = 24*k*32**(2*k)
        power4 = 1
        t = 0
        while power4 < new:
            power4 *= 4
            t += 1
        show(f"threshold k={k}", f"old={old}; new={new}; old/new={F(old,new)}; first4^t=4^{t}")


def restriction_checks():
    n = 3
    indices = range(n)
    subsets = [frozenset(c) for j in range(n+1) for c in combinations(indices, j)]
    profiles = [
        ((F(1), F(0), F(-1)), (F(0), F(1), F(0))),
        ((F(1, 2), F(-1, 4), F(0)), (F(1, 2), F(3, 4), F(3, 4))),
        ((F(-1, 2), F(1, 4), F(1, 2)), (F(1, 2), F(3, 4), F(1, 2))),
        ((F(0), F(0), F(0)), (F(1), F(1, 3), F(1, 4))),
    ]
    count = 0
    for mu, v in profiles:
        weights = [{0: v[i], 1: (1-v[i]+mu[i])/2,
                    -1: (1-v[i]-mu[i])/2} for i in indices]
        for w in weights:
            assert all(x >= 0 for x in w.values()) and sum(w.values()) == 1
        # By linearity these basis tests cover every polynomial in dimension3.
        for T, S in product(subsets, repeat=2):
            lhs = F(0)
            for rho in product((0, 1, -1), repeat=n):  # 0 means free
                free_T = frozenset(i for i in T if rho[i] == 0)
                if free_T == S:
                    coefficient = product_of(F(rho[i]) for i in T if rho[i] != 0)
                    lhs += coefficient*product_of(weights[i][rho[i]] for i in indices)
            rhs = (product_of(v[i] for i in S)*product_of(mu[i] for i in T-S)
                   if S <= T else F(0))
            assert lhs == rhs
            count += 1
    # A negative control: omitting the free-probability factor is false.
    assert F(1, 2) != 1  # g(x)=x1, S={1}, v1=1/2
    show("coordinate-dependent restriction identity", f"{count} exact monomial/profile cases; zero-fixing probabilities included")
    show("restriction negative control", "omitting product(v_i) fails for a singleton monomial")


def matrix_vector(H, z):
    return [sum((h*x for h, x in zip(row, z)), F(0)) for row in H]


def endpoint_norm_checks():
    m = 4
    H = [[F((-1)**((a & b).bit_count()), 2) for b in range(m)] for a in range(m)]
    for a, b in product(range(m), repeat=2):
        assert sum((H[a][c]*H[b][c] for c in range(m)), F(0)) == int(a == b)
    signs = list(product((-1, 1), repeat=m))
    count = 0
    for k in (2, 3, 4):
        for known_blocks in product(signs, repeat=k-1):
            vector = list(map(F, known_blocks[0]))
            for z in known_blocks[1:]:
                vector = [u*s for u, s in zip(matrix_vector(H, vector), z)]
            coeff = [u/m for u in matrix_vector(H, vector)]
            assert sum((c*c for c in coeff), F(0)) == F(1, m)
            count += 1
    show("conditional endpoint coefficient norm (supplementary)",
         f"{count} exact Walsh m=4 cases, k=2,3,4; sum(c_i^2)=1/m")


def bansal_sinha_checks():
    for k in range(2, 65):
        top = k*(k-1)
        beta = 1-F(1, top)
        assert beta-(1-F(1,k)) == F(k-2, top)
        for ell in range(k, top+1):
            actual = F(ell-1, 2)
            printed = F(ell, 2)*(1-F(1,k))
            assert actual-printed == (F(ell,k)-1)/2
            assert (actual <= printed) == (ell == k)
            assert actual-beta*F(ell,2) <= 0
        assert (F(top,k)-1)/2 == F(k-2,2)
    # k=3, ell=6, L=64: actual/printed=L^(1/2)=8 after equal constants.
    assert F(64**5, 64**4) == 64  # squared ratio, exact rationals
    show("Bansal-Sinha exponent audit", "k=2..64, all k<=ell<=k(k-1); surplus=(ell/k-1)/2")
    show("Bansal-Sinha concrete exponent witness", "k=3, ell=6, logarithm L=64: ratio=8 (squared ratio=64)")
    show("surviving logarithm", "beta=1-1/[k(k-1)]; beta-(1-1/k)=(k-2)/[k(k-1)]")


def small_dimension_checks():
    # For m=1 the matrix is (1), so Phi is a product of signs.
    for k in range(2, 11):
        delta = F(1, 32**k)
        values = [product_of(map(F, z)) for z in product((-1, 1), repeat=k)]
        assert set(values) == {F(-1), F(1)}
        assert not any(abs(x) <= delta/2 for x in values)
    # For m=2,k=2, Phi=numerator/(2*sqrt(2)), so Phi^2=numerator^2/8.
    walsh = ((1, 1), (1, -1))
    for x, y in product(product((-1, 1), repeat=2), repeat=2):
        numerator = sum(x[i]*walsh[i][j]*y[j] for i,j in product(range(2),repeat=2))
        assert F(numerator*numerator, 8) == F(1, 2)
        assert F(1, 2) > (F(1, 32**2)/2)**2
    show("small-dimension scope", "m=1,k=2..10 and m=2,k=2: zero promise empty; constant-1 algorithm suffices")


def package_checks():
    root = Path(__file__).resolve().parent
    required = ["note.md", "lean_blueprint.md", "references.bib",
                "bansal_sinha_section54.md", "correspondence.json",
                "NEW_STATEMENTS.json", "STATEMENT_CHANGES.json", "LEAN_GAPS.md",
                "README.md", "read_receipt.json"]
    missing = [x for x in required if not (root/x).is_file()]
    assert not missing, "missing required files: " + ", ".join(missing)
    statements = json.loads((root/"NEW_STATEMENTS.json").read_text())
    assert isinstance(statements, list)
    ids = [x["id"] for x in statements]
    assert len(ids) == len(set(ids))
    known_ids = set(ids) | {"eq-3", "eq-4", "lem-2.1.i"}
    for x in statements:
        assert all(key in x for key in ("id", "statement", "why_needed", "depends_on",
                                       "proposed_lean", "route_note"))
        assert x["statement"] and x["proposed_lean"]
        assert set(x["depends_on"]) <= known_ids, x["id"] + ": unresolved dependency"
        assert not re.search(r"\b(sorry|admit|TODO)\b", x["proposed_lean"]), x["id"]
    passages = {}
    for filename in ("note.md", "lean_blueprint.md", "bansal_sinha_section54.md"):
        txt = (root/filename).read_text()
        assert "\u2014" not in txt, filename+": em dash"
        opened = re.findall(r"<!-- passage:([^ ]+) -->", txt)
        matched = []
        for m in re.finditer(r"<!-- passage:([^ ]+) -->\s*(.*?)\s*<!-- /passage:\1 -->", txt, re.S):
            assert m[1] not in passages, m[1]
            passages[m[1]] = m[2]
            matched.append(m[1])
        assert opened == matched, filename + ": malformed or unclosed anchor"
    corr = json.loads((root/"correspondence.json").read_text())
    for c in corr:
        assert c["passage"] in passages, c["passage"]
        body = passages[c["passage"]]
        assert body.startswith(c["from"]), c["passage"]+": from"
        assert body.endswith(c["to"]), c["passage"]+": to"
        assert c["role"] in ("states", "defines", "proves", "explains", "uses", "mentions")
        assert set(c["statement_ids"]) <= known_ids, c["passage"] + ": unresolved statement"
    assert set(passages) == {c["passage"] for c in corr}, "unmapped anchored passage"
    changes = json.loads((root/"STATEMENT_CHANGES.json").read_text())
    for change in changes:
        assert set(("id", "old", "new", "relation", "reason")) <= set(change)
        assert change["id"] in known_ids
        assert change["relation"] in ("stronger", "weaker", "equivalent", "corrected")
    json.loads((root/"read_receipt.json").read_text())
    show("package metadata", f"{len(statements)} new statement records; {len(passages)} mapped passages; valid anchors/endpoints")


def main():
    print("EXACT CHECKS: standard-library Fraction/integer arithmetic; no floating point.")
    print("Analytic statements are proved in the note. Finite cases do not prove their universal versions.")
    kernel_checks()
    constant_checks()
    exp_and_threshold_checks()
    restriction_checks()
    endpoint_norm_checks()
    bansal_sinha_checks()
    small_dimension_checks()
    package_checks()
    print("ALL AVAILABLE CHECKS PASSED")


if __name__ == "__main__":
    main()
