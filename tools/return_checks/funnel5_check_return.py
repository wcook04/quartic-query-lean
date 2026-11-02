#!/usr/bin/env python3
"""Validate this reader/film return against its supplied source packet. No Lean is run."""
from pathlib import Path
from fractions import Fraction
import argparse, datetime, hashlib, json, re, sys

def sha(b): return hashlib.sha256(b).hexdigest()
def read(p): return json.loads(p.read_text())

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--packet',type=Path,required=True)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    out=Path(__file__).resolve().parents[1]
    packet=args.packet.resolve()
    observations=[]
    def check(condition, name, details=None):
        if not condition: raise AssertionError(name+(': '+str(details) if details is not None else ''))
        observations.append({'check':name,'status':'pass',**({'details':details} if details is not None else {})})

    required=['levels.md','levels.json','argument_map.json','fidelity_view.md','film_12min.md','film_4min.md','data_contract.md','correspondence.json','NEW_STATEMENTS.json','LEAN_GAPS.md','STATEMENT_CHANGES.json']
    check(all((out/f).is_file() for f in required),'required_deliverables_present',required)
    for p in out.rglob('*.json'): read(p)
    manifest=read(packet/'manifest.json')
    for m in manifest['members']:
        b=(packet/m['member']).read_bytes()
        assert len(b)==m['bytes'] and sha(b)==m['sha256'],m['member']
    check(True,'input_manifest_integrity',{'hashed_members':len(manifest['members']),'scope':'Matches the supplied manifest; does not authenticate an external build.'})
    corpus={s['id']:s for s in read(packet/'repository/corpus/statements.json')}
    dep=read(packet/'repository/corpus/lean_dependencies.json')
    declared=set(dep['declared'])|{t['declaration'] for s in corpus.values() for t in s['lean']}
    amap=read(out/'argument_map.json')
    for n in amap['nodes']:
        orig=corpus[n['id']]
        assert n['evidence']==orig['evidence'],n['id']
        assert n['statement']==orig['statement'],n['id']
        assert n['lean']==orig['lean'],n['id']
    check(True,'map_source_fields_unchanged',{'nodes':len(amap['nodes'])})
    node_ids={n['id'] for n in amap['nodes']}
    for e in amap['edges']:
        assert e['from'] in node_ids and e['to'] in node_ids
        path=e['source_dependency_path']
        assert path[0]==e['from'] and path[-1]==e['to']
        assert e['via']==path[1:-1]
        for a,b in zip(path,path[1:]): assert a in corpus[b]['depends_on'],(a,b)
        assert e['kind']=='supports' and e['reason'].strip()
    check(True,'collapsed_support_paths_resolve',{'edges':len(amap['edges'])})
    check(set(amap['reading_order']+amap['optional_reading'])==node_ids,'map_reading_order_covers_nodes')

    new=read(out/'NEW_STATEMENTS.json');newids={n['id'] for n in new}
    check(len(newids)==len(new),'new_statement_ids_unique')
    for n in new:
        assert {'id','statement','why_needed','depends_on','proposed_lean','route_note'}<=n.keys()
        assert set(n['depends_on'])<=set(corpus)|newids,n['id']
        assert n['formal_status']=='proposed_uncompiled'
        assert n['proposed_lean_context']=='import QuarticQuery\nopen QuarticQuery\nopen scoped BigOperators'
        assert ':=' not in n['proposed_lean'].split('\n',1)[0]
    check(True,'new_signatures_have_context_and_uncompiled_status',{'count':len(new),'elaboration_performed':False})
    check(read(out/'STATEMENT_CHANGES.json')==[],'no_existing_mathematical_statement_changed')

    anchor_files=['levels.md','film_12min.md','film_4min.md','fidelity_view.md','LEAN_GAPS.md']
    anchors={}
    for filename in anchor_files:
        txt=(out/filename).read_text()
        opens=re.findall(r'<!-- passage:([^>]+) -->',txt)
        pairs=list(re.finditer(r'<!-- passage:([^>]+) -->\s*(.*?)\s*<!-- /passage:\1 -->',txt,re.S))
        assert len(opens)==len(pairs),filename
        for m in pairs:
            assert m[1] not in anchors,m[1]
            anchors[m[1]]=(filename,m[2].strip())
    corr=read(out/'correspondence.json')
    check(len({c['passage'] for c in corr})==len(corr),'correspondence_unique')
    check({c['passage'] for c in corr}==set(anchors),'all_declared_passage_anchors_bound')
    roles={'states','defines','proves','explains','uses','mentions'}
    for c in corr:
        filename,body=anchors[c['passage']]
        assert filename==c['file'] and c['role'] in roles
        assert body.startswith(c['from']) and body.endswith(c['to']),c['passage']
        assert sha(body.encode())==c['body_sha256'],c['passage']
        assert set(c['statement_ids'])<=set(corpus),c['passage']
        assert set(c.get('new_statement_ids',[]))<=newids,c['passage']
        assert set(c['lean'])<=declared,(c['passage'],set(c['lean'])-declared)
    check(True,'passage_boundaries_ids_and_declarations_resolve',{'passages':len(corr)})

    levels=read(out/'levels.json')
    check([l['id'] for l in levels['levels']]==['one_sentence','one_paragraph','one_page','argument_map','reading_route'],'five_explanation_levels')
    for l in levels['levels']:
        assert l['opening_example']=='four_column_winner'
        assert l['novelty'] and l['why_it_matters'] and l['scope']
        assert set(l['statement_ids'])<=set(corpus)
    check(True,'each_level_has_example_novelty_importance_and_scope')
    films=read(out/'film_shots.json')['films']
    timing={}
    for key,total in [('film12',720),('film4',240)]:
        prev=0
        for s in films[key]:
            assert s['start_seconds']==prev
            assert s['end_seconds']-s['start_seconds']==s['duration_seconds']>0
            assert len(s['spoken'].split())==s['spoken_words']
            assert set(s['statement_ids'])<=set(corpus)
            assert set(s['new_statement_ids'])<=newids
            assert anchors[s['id']][1]==s['spoken']
            assert anchors[s['picture_passage']][1]==s['picture']
            prev=s['end_seconds']
        assert prev==total
        timing[key]={'planned_seconds':total,'shots':len(films[key]),'spoken_words':sum(s['spoken_words'] for s in films[key]),'timing_status':'planned, not recorded'}
    check(True,'film_durations_and_script_data_agree',timing)

    visual=read(out/'visual_data.json')
    W=visual['W']
    exactW=[[(-1)**((i&j).bit_count()) for j in range(4)] for i in range(4)]
    check(W==exactW,'walsh_matrix_matches_public_bit_parity_definition')
    assert [[sum(W[i][j]*W[k][j] for j in range(4)) for k in range(4)] for i in range(4)]==[[4*int(i==k) for k in range(4)] for i in range(4)]
    sample_results={}
    for key,expected in [('yes',1),('zero',0)]:
        z=visual['forrelation'][key]
        signs=[[1 if b==0 else -1 for b in row] for row in z['bits']]
        assert signs==z['signs']
        product=[sum(W[i][j]*signs[1][j] for j in range(4)) for i in range(4)]
        N=sum(signs[0][i]*product[i] for i in range(4))
        M=4*2
        phi=Fraction(N,M)
        assert product==z['Wz2'] and N==z['numerator'] and M==z['denominator']
        assert phi==Fraction(z['Phi'])==expected
        delta=Fraction(1,2**10)
        P=1 if phi>=delta else 0 if abs(phi)<=delta/2 else None
        assert P==z['P']==expected
        # Compute u^T D_z1 (W/2) D_z2 u with exact rational amplitudes.
        u=[Fraction(1,2)]*4
        after_d2=[u[i]*signs[1][i] for i in range(4)]
        after_h=[sum(Fraction(W[i][j],2)*after_d2[j] for j in range(4)) for i in range(4)]
        after_d1=[after_h[i]*signs[0][i] for i in range(4)]
        amplitude=sum(u[i]*after_d1[i] for i in range(4))
        assert amplitude==phi and sum(a*a for a in after_d1)==1
        sample_results[key]={'numerator':N,'denominator':M,'Phi':str(phi),'P':P,'projection_probability':str(amplitude*amplitude)}
    check(True,'forrelation_and_projection_calculations_exact',sample_results)
    p=visual['parameters']
    check(p['m']==2**(2*p['t'])==4 and p['ell']==2*p['t']==2 and p['r']==40*p['t']==40 and int(p['cells_per_column'])==2**40,'finite_parameter_values')
    exactL=Fraction(2,4).__floor__()
    check(p['L']==exactL==0 and Fraction(p['delta'])==Fraction(1,1024) and Fraction(p['delta_half'])==Fraction(1,2048),'small_example_floor_and_thresholds')
    ex=visual['example'];J=ex['zero_rows']
    check(ex['dummy_X']==[[int(row!=J[col]) for row in range(4)] for col in range(4)],'dummy_board_values')
    check(ex['planted_X']==[[1]*4]+ex['dummy_X'][1:],'planted_board_values')
    check(ex['address']==[1]+[0]*39,'address_from_exact_blocks')
    for ptr in ex['planted_pointers']:
        assert ex['planted_X'][ptr['target_column']][ptr['target_row']]==0
        assert ptr['target_row']==J[ptr['target_column']]
    check(True,'outward_pointer_targets_are_actual_zeros')
    diffs=[(i,j) for i in range(4) for j in range(4) if ex['dummy_X'][i][j]!=ex['planted_X'][i][j]]
    check(diffs==[(0,0)],'displayed_X_change_is_only_erased_zero')
    check(visual['local_tests']=={'circuit_size':'S','all_one':4,'pointers':3,'gates':'40*S','outputs':80,'total':'4+3+40*(S+2)'},'local_test_categories_match_card_testIndex_specialization')
    check((out/'worked_example.png').stat().st_size>0 and (out/'worked_example.svg').stat().st_size>0,'diagram_assets_present')

    checking=read(out/'checking_visual_data.json')
    check(checking['comparator_config']==read(packet/checking['config_source']),'comparator_configuration_exact_copy')
    for snippet in checking['source_excerpts'].values():
        pth=packet/snippet['source_file'];b=pth.read_bytes()
        assert sha(b)==snippet['source_sha256']
        assert '\n'.join(b.decode().splitlines()[snippet['line_start']-1:snippet['line_end']])==snippet['source_text']
    for case in checking['negative_controls']:
        assert (packet/case['source_file']).read_text()==case['source_text']
    check(True,'checking_film_source_snippets_and_negative_modules_exact')

    gaps=read(out/'LEAN_GAPS.json')
    for g in gaps['reading_order']: assert g['evidence']==corpus[g['id']]['evidence']
    check(True,'gap_statuses_preserve_corpus_values')
    for pth in out.glob('*.md'):
        assert '\u2014' not in pth.read_text(),pth.name
        assert not re.search(r'\b(?:TODO|TBD|FIXME)\b',pth.read_text()),pth.name
    check(True,'authored_markdown_has_no_em_dash_or_unresolved_placeholder')

    result={
        'status':'passed',
        'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source_packet_commit':manifest['repository_commit'],
        'checks':observations,
        'limits':[
            'No Lean elaboration, compilation, axiom export, Comparator execution, external-kernel replay or human review.',
            'New Lean signatures remain proposed_uncompiled.',
            'Circuit transcript bits and numerical circuit size are specified by the supplied circuit, not materialized or executed here.',
            'Finite arithmetic and file-consistency checks do not establish the asymptotic theorem or authenticate historical execution receipts.',
            'Film durations are proposed edit windows, not a measured narration performance.'
        ]
    }
    target=args.output or out/'checks/validation_report.json'
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(observations),'passages':len(corr),'films':timing,'report':str(target)},indent=2))

if __name__=='__main__': main()
