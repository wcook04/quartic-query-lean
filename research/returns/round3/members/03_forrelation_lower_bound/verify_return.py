#!/usr/bin/env python3
"""Structural/integrity checks and exact arithmetic; not a Lean or theorem prover."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from fractions import Fraction as F
from pathlib import Path

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def readj(p: Path):
    return json.loads(p.read_text())

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--packet',type=Path,help='Original extracted input packet; optional.')
    ap.add_argument('--return-dir',type=Path,default=Path(__file__).resolve().parent)
    args=ap.parse_args()
    out=args.return_dir.resolve()
    required=['section.md','correspondence.json','NEW_STATEMENTS.json','STATEMENT_CHANGES.json',
      'LEAN_GAPS.md','references.bib','source_read_receipt.json','review_notes.md','STYLE_RULES.json',
      'SOURCE_USAGE.md','historical_threshold.md','evidence/declaration_interfaces.json',
      'evidence/evidence_verification.json','evidence/route_boundaries.json']
    for name in required: assert (out/name).is_file(),('missing',name)
    for p in out.rglob('*.json'): readj(p)
    interface_list=readj(out/'evidence/declaration_interfaces.json')['declarations']
    interfaces={q['name']:q for q in interface_list}
    assert len(interfaces)==len(interface_list)==143
    anchors={}
    numbered={}
    total_displays=0
    for fn in ['section.md','historical_threshold.md']:
        text=(out/fn).read_text()
        assert not any(ord(c)<32 and c not in '\n\r\t' for c in text),('control_character',fn)
        assert text.count(r'\[')==text.count(r'\]'),('display_delimiters',fn)
        assert text.count('$')%2==0,('inline_delimiters',fn)
        starts=re.findall(r'<!-- passage:([^ ]+) -->',text)
        ends=re.findall(r'<!-- /passage:([^ ]+) -->',text)
        assert starts==ends and len(starts)==len(set(starts)),('anchors',fn)
        for a in starts:
            assert a not in anchors
            m=re.search(r'<!-- passage:'+re.escape(a)+r' -->(.*?)<!-- /passage:'+re.escape(a)+r' -->',text,re.S)
            assert m
            anchors[a]=(fn,m.group(1).strip())
        tags=re.findall(r'\\tag\{([FH]\d+)\}',text)
        assert len(tags)==len(set(tags)),('duplicate_tags',fn)
        for t in tags:
            assert t not in numbered
            numbered[t]=fn
        total_displays+=text.count(r'\[')
    assert {f'F{i}' for i in range(1,61)}<=numbered.keys()
    assert {f'H{i}' for i in range(1,4)}<=numbered.keys()
    for fn in ['section.md','historical_threshold.md']:
        text=(out/fn).read_text()
        for ref in re.findall(r'\(([FH]\d+)\)',text):
            assert ref in numbered,('unresolved_equation',fn,ref)
    corr=readj(out/'correspondence.json')
    assert {q['passage'] for q in corr}==set(anchors)
    mapped_tags=set()
    mapped_display_count=0
    all_ids=set()
    for q in corr:
        fn,body=anchors[q['passage']]
        assert q['file']==fn
        assert q['from'] in body and q['to'] in body
        assert body.find(q['from'])<=body.rfind(q['to'])
        if 'passage_sha256' in q:
            assert hashlib.sha256(body.encode()).hexdigest()==q['passage_sha256']
        assert q['role'] in ['states','defines','proves','explains','uses','mentions']
        all_ids.update(q['statement_ids'])
        assert set(q['lean'])==set(q['complete_lean_interfaces'])
        for name,actual in q['complete_lean_interfaces'].items():
            source=interfaces[name]
            for key in ['source_signature','source_definition','namespace','ambient_variables',
                        'local_notation','include_or_omit_before','source_sha256',
                        'elaborated_type_from_supplied_audit','evidence']:
                assert actual[key]==source[key],('interface_mismatch',name,key)
        displays=re.findall(r'\\\[(.*?)\\\]',body,re.S)
        assert len(displays)==len(q['display_correspondence'])
        for d in q['display_correspondence']:
            assert d['exact_display'] in body
            for n in d['lean']: assert n in q['complete_lean_interfaces']
            if re.fullmatch('[FH][0-9]+',d['display']):mapped_tags.add(d['display'])
            mapped_display_count+=1
    assert mapped_tags==set(numbered)
    assert mapped_display_count==total_displays
    new=readj(out/'NEW_STATEMENTS.json')
    assert len({q['id'] for q in new})==len(new)
    for q in new:
        for k in ['id','statement','why_needed','depends_on','proposed_lean','route_note']:assert k in q
    for q in readj(out/'STATEMENT_CHANGES.json'):
        for k in ['id','old','new','relation','reason']:assert k in q
    for q in readj(out/'STYLE_RULES.json'):
        assert q['source']['sha256'] and q['source']['locator']
    for fn in ['section.md','LEAN_GAPS.md','SOURCE_USAGE.md']:
        for link in re.findall(r'\]\(([^)]+)\)',(out/fn).read_text()):
            if '://' not in link and not link.startswith('#'):
                assert (out/link.split('#')[0]).exists(),('local_link',fn,link)
    scalar_checks={
      'amplification_25':18*8**25<9**25,
      'historical_amplification_30':32*8**30<9**30,
      'sharp_ratio_256':F(2,18225)/F(1,2332800)==256,
      'budget_identity':800*F(2,18225)==F(8,27)**2,
      'padding_bound':F(50,49)<F(9,8)**2,
      'edge_mean_identity':F(3,16)*F(8,27)==F(1,18),
      'gap':1-F(1,16)-F(1,9)==F(119,144),
      'strict_gap_margin':F(119,144)-F(7,12)==F(35,144)>0,
      'threshold_constant':F(2,18225)/6==F(1,54675),
      'threshold_strictness':4*13669-54675==1,
      'restriction_base_k2':F(3,16)*4==F(3,4),
      'restriction_inductive_ratio':F(3,16)*F(4,3)==F(1,4),
      'ssw_gap_factor':F(7,24)*F(9,2)==F(21,16),
      'ssw_constant':F(4,81)/8==F(1,162),
      'bs_geometric_base':(F(128)**(-1)/127)/(F(32)**(-2)/4)==F(32,127)<1,
      'bs_geometric_ratio':F(32,128)==F(1,4)<1}
    assert all(scalar_checks.values()),scalar_checks
    report={
      'status':'passed','mode':'structural checks, exact scalar arithmetic and optional byte checks',
      'passages':len(anchors),'numbered_displays':len(numbered),'all_displays_mapped':mapped_display_count,
      'declaration_interfaces':len(interfaces),
      'elaborated_types_supplied':sum(bool(q['elaborated_type_from_supplied_audit']) for q in interfaces.values()),
      'new_ordinary_statements':len(new),'exact_scalar_checks':scalar_checks,
      'fresh_lean_run':False,'finite_checks_are_not_proof_evidence':True}
    if args.packet:
        packet=args.packet.resolve()
        manifest=readj(packet/'manifest.json')
        for q in manifest['members']:
            p=packet/q['member']
            assert p.is_file(),('input_member_missing',q['member'])
            assert p.stat().st_size==q['bytes'],('input_size',q['member'])
            assert sha(p)==q['sha256'],('input_hash',q['member'])
        for q in interfaces.values():
            p=packet/q['file']
            assert sha(p)==q['source_sha256'],('interface_file_hash',q['name'])
            lines=p.read_text().splitlines()
            header='\n'.join(lines[q['line_start']-1:q['signature_end_line']])
            assert q['source_signature'] in header,('verbatim_header',q['name'])
        known_ids=set()
        for p in [
          packet/'repository/research/returns/funnel/1_long_reasoning_record/NEW_STATEMENTS.json',
          packet/'repository/research/returns/funnel/4_forrelation_route_note/NEW_STATEMENTS.json',
          packet/'repository/research/returns/round2/6_sharp_uniform_forrelation/NEW_STATEMENTS.json']:
            known_ids.update(q['id'] for q in readj(p))
        for q in readj(packet/'repository/research/returns/funnel/1_long_reasoning_record/correspondence.json'):
            known_ids.update(q['statement_ids'])
        known_ids.update(q['id'] for q in new)
        assert all_ids<=known_ids,('unknown_statement_ids',sorted(all_ids-known_ids))
        for q in new:assert set(q['depends_on'])<=known_ids,('unknown_new_dependency',q['id'])
        report['input_packet']={'manifest_members_verified':len(manifest['members']),'repository_commit_label':manifest['repository_commit'],'all_match':True}
    if (out/'MANIFEST.json').exists():
        m=readj(out/'MANIFEST.json')
        covered=set()
        for q in m['members']:
            p=out/q['member'];covered.add(q['member'])
            assert p.is_file() and p.stat().st_size==q['bytes']
            assert sha(p)==q['sha256'],('return_hash',q['member'])
        expected={str(p.relative_to(out)) for p in out.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
        assert covered==expected,('manifest_inventory',covered^expected)
        report['return_manifest']={'members_verified':len(covered),'all_match':True,'self_hash_excluded':True}
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
