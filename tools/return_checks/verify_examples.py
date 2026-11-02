#!/usr/bin/env python3
"""Exact finite checks for worked_examples.md; no external dependencies.

This checks toy arithmetic and finite processes, not the asymptotic separation,
Forrelation lower bound, quantum circuit implementation, or unspecified circuit C.
"""
from fractions import Fraction as F
from itertools import product
import argparse
import json
from pathlib import Path


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def matvec(a, x):
    return tuple(dot(row, x) for row in a)


def transpose(a):
    return tuple(zip(*a))


def mul(a, b):
    return tuple(tuple(dot(row, col) for col in transpose(b)) for row in a)


def forr(z1, z2, h):
    return dot(z1, matvec(h, z2))/4


def partial_value(phi):
    delta = F(1, 1024)
    if phi >= delta:
        return 1
    if abs(phi) <= delta/2:
        return 0
    return None


def circuit_outputs_from_integer(n):
    m_denominator = 8
    one = 2**10*n >= m_denominator
    zero = 2**11*abs(n) <= m_denominator
    return int(one or zero), int(one)


def tournament_stats(a, steps):
    """Enumerate all ideal histories with exact rational probabilities."""
    size = len(a)
    nodes = [(F(1), (), tuple(F(1) for _ in range(size)))]
    stats = []
    for t in range(steps+1):
        assert sum(p for p, _, _ in nodes) == 1
        stats.append({
            'steps': t,
            'miss_candidate_1': sum(p for p, hist, _ in nodes if 0 not in hist),
            'expected_total_weight': sum(p*sum(w) for p, _, w in nodes),
        })
        if t == steps:
            break
        children = []
        for probability, hist, w in nodes:
            total = sum(w)
            if not total:
                children.append((probability, hist, w))
                continue
            expected_next = F(0)
            for pivot in range(size):
                if not w[pivot]:
                    continue
                assert pivot not in hist
                next_w = tuple(w[i]*a[i][pivot] for i in range(size))
                transition_probability = w[pivot]/total
                expected_next += transition_probability*sum(next_w)
                children.append((probability*transition_probability, hist+(pivot,), next_w))
            identity = (total**2-sum(v*v for v in w))/(2*total)
            assert expected_next == identity
            assert expected_next <= total/2
        nodes = children
    return stats


def comparison_matrix(x, pointers):
    size = len(x)
    a = [[F(0) for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(i+1, size):
            i_disqualifies = x[j][pointers[i][j]-1] == '0'
            j_disqualifies = x[i][pointers[j][i]-1] == '0'
            winner = i if i_disqualifies != j_disqualifies and i_disqualifies else j if i_disqualifies != j_disqualifies else i
            a[winner][j if winner == i else i] = F(1)
    return tuple(tuple(row) for row in a)


def winner_indices(x, pointers):
    # All address instances in this base example are P0; the candidate at index
    # 0 carries canonical correct transcripts. Others have a zero in X and
    # hence cannot win regardless of their transcripts. This does not simulate C.
    return [i+1 for i in range(len(x))
            if x[i] == '1111'
            and all(x[j][pointers[i][j]-1] == '0' for j in range(len(x)) if j != i)]


def exact_results():
    h = tuple(tuple(F(v, 2) for v in row) for row in
              ((1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1)))
    identity = tuple(tuple(F(i == j) for j in range(4)) for i in range(4))
    assert mul(h, h) == identity
    v = (1,1,1,-1)
    z0 = (1,1,-1,1)
    assert matvec(h, v) == v
    named = {}
    for name, z1 in [('P1', v), ('P0', z0), ('undefined_negative', tuple(-t for t in v))]:
        phi = forr(z1, v, h)
        n = dot(z1, matvec(tuple(tuple(2*x for x in row) for row in h), v))
        assert n == 8*phi and n.denominator == 1
        named[name] = {'z1':z1, 'z2':v, 'Phi':phi, 'N':n,
                       'P':partial_value(phi), 'projection_probability':phi**2,
                       'circuit_d_b':circuit_outputs_from_integer(n)}
    assert [named[name]['Phi'] for name in named] == [1,0,-1]
    counts = {'P1':0,'P0':0,'undefined':0}
    histogram = {}
    for z1, z2 in product(product((-1,1), repeat=4), repeat=2):
        phi = forr(z1, z2, h)
        n = 8*phi
        assert n.denominator == 1
        value = partial_value(phi)
        d,b = circuit_outputs_from_integer(n)
        assert d == int(value is not None)
        assert not d or b == value
        counts['undefined' if value is None else f'P{value}'] += 1
        histogram[str(phi)] = histogram.get(str(phi), 0)+1
    assert sum(counts.values()) == 256
    assert counts == {'P1':104,'P0':48,'undefined':104}

    x = ('1111','0111','1011','1101')
    pointers = ((None,1,2,3),(1,None,2,1),(1,2,None,3),(1,1,1,None))
    cycle = comparison_matrix(x, pointers)
    expected_cycle = ((0,1,1,1),(0,0,1,0),(0,0,0,1),(0,1,0,0))
    assert cycle == expected_cycle
    assert winner_indices(x,pointers) == [1]
    broken = tuple(tuple(2 if i == 0 and j == 1 else pointers[i][j] for j in range(4)) for i in range(4))
    assert winner_indices(x,broken) == []
    assert comparison_matrix(x,broken) == cycle
    # At every possible opponent pointer target, the winner's all-one string
    # prevents disqualification. Its own correctly decoded pointer still finds 0.
    off_promise_checks = []
    for opponent in range(1,4):
        for arbitrary_target in range(1,5):
            assert x[0][arbitrary_target-1] == '1'
            assert x[opponent][pointers[0][opponent]-1] == '0'
            off_promise_checks.append({'opponent':opponent+1,'opponent_target':arbitrary_target,'winner_1_wins':True})
    cycle_stats = tournament_stats(cycle, 3)
    assert [s['miss_candidate_1'] for s in cycle_stats] == [1,F(3,4),F(3,8),0]

    fractional = tuple(tuple(F(0) if i == j or j == 0 else F(1) if i == 0 else F(1,2)
                             for j in range(4)) for i in range(4))
    frac_stats = tournament_stats(fractional, 4)
    assert [s['miss_candidate_1'] for s in frac_stats] == [1,F(3,4),F(3,8),F(3,40),0]
    w_after_2 = tuple(fractional[i][1] for i in range(4))
    assert w_after_2 == (1,0,F(1,2),F(1,2))
    assert sum(w_after_2) == 2
    next_law = tuple(w/sum(w_after_2) for w in w_after_2)
    next_expected_weight = (sum(w_after_2)**2 - sum(w*w for w in w_after_2))/(2*sum(w_after_2))
    assert next_expected_weight == F(5,8)

    g_before = (F(3,10),F(4,10))
    p = sum(g*g for g in g_before)
    assert p == F(1,4)
    g_after = tuple((3-4*p)*g for g in g_before)
    bad_factor = 1-4*p
    assert g_after == (F(3,5),F(4,5)) and bad_factor == 0
    before_cond = tuple(g*g/p for g in g_before)
    after_cond = tuple(g*g for g in g_after)
    assert before_cond == after_cond == (F(9,25),F(16,25))

    and_inputs = list(product((0,1), repeat=2))
    and_truth = lambda u: u[0] & u[1]
    one_query_scores = [sum(F(and_truth(u)==answer,4) for u in and_inputs) for answer in (0,1)]
    for index in (0,1):
        for answers in product((0,1), repeat=2):
            one_query_scores.append(sum(F(answers[u[index]]==and_truth(u),4) for u in and_inputs))
    assert max(one_query_scores) == F(3,4)
    variable_runs = []
    for a,b in and_inputs:
        q = 1 if a == 0 else 2
        out = 0 if a == 0 else b
        variable_runs.append({'input':(a,b),'queries':q,'output':out,'correct':out==(a&b),'nonheavy':q<=1})
    prob_nonheavy = sum(F(run['nonheavy'],4) for run in variable_runs)
    prob_joint = sum(F(run['nonheavy'] and run['correct'],4) for run in variable_runs)
    assert prob_nonheavy == prob_joint == F(1,2)
    capped_score = sum(F((0 if a == 0 else 0)==(a&b),4) for a,b in and_inputs)
    assert capped_score == F(3,4)
    r40 = 40
    t12 = (4000-1).bit_length()
    assert t12 == 12
    return {
        'status':'all exact assertions passed',
        'scope':'Finite arithmetic and ideal stochastic processes only; not an asymptotic or formal proof, not a gate-level simulation of the unspecified circuit C.',
        'parameters':{'m':4,'k':2,'r':r40,'ell':2,'T':t12,'epsilon':F(1,12000),'L':0,
                      'cells_per_column':2**40,'total_cells':2**42,'K_symbolic':'87 + 40*S',
                      'input_bits_symbolic':'1296 + 2^42*(6 + 40*S)'},
        'forrelation':{'H_squared_identity':True,'H_v_equals_v':True,'named_instances':named,
                       'all_256_pair_counts':counts,'Phi_histogram':histogram},
        'board':{'X':x,'pointers_one_based':pointers,'comparison_matrix':cycle,'winner_indices':[1],
                 'broken_pointer':{'source':1,'destination':2,'old_row':1,'new_row':2,
                                   'winner_indices':[],'comparison_matrix_unchanged':True},
                 'off_promise_pointer_checks':off_promise_checks,
                 'ideal_statistics':cycle_stats,
                 'transcript_scope':'The exact outputs (d,b) are checked; the fixed circuit C and its canonical gate transcripts are specified symbolically, not enumerated.'},
        'fractional_tournament':{'matrix':fractional,'weights_after_pivot_2':w_after_2,
                                 'next_pivot_law':next_law,'conditional_next_expected_total':next_expected_weight,
                                 'ideal_statistics':frac_stats},
        'amplification':{'good_amplitudes_before':g_before,'initial_success':p,
                         'good_multiplier':3-4*p,'bad_multiplier':bad_factor,
                         'good_amplitudes_after_one_Grover':g_after,
                         'conditional_good_probabilities_before':before_cond,
                         'conditional_good_probabilities_after':after_cond},
        'adaptive_conditioning':{'one_query_optimum':max(one_query_scores),'variable_depth_runs':variable_runs,
                                 'probability_nonheavy':prob_nonheavy,'probability_nonheavy_and_correct':prob_joint,
                                 'conditional_success_given_nonheavy':prob_joint/prob_nonheavy,
                                 'capped_simulator_success':capped_score,
                                 'two_copy_all_nonheavy_probability':prob_nonheavy**2,
                                 'two_copy_capped_success':capped_score**2}
    }


def encode(obj):
    if isinstance(obj,F):
        return str(obj)
    if isinstance(obj,dict):
        return {str(k):encode(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)):
        return [encode(v) for v in obj]
    return obj


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args=parser.parse_args()
    output=json.dumps(encode(exact_results()),indent=2,ensure_ascii=False)+'\n'
    if args.output:
        args.output.write_text(output)
    print(output,end='')


if __name__ == '__main__':
    main()
