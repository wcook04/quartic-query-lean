#!/usr/bin/env python3
"""Validate the review contract against an unpacked original packet.

This does not invoke Lean or certify mathematical proofs. Run:
  python3 checks/validate_return.py --packet /path/to/unpacked/input
"""
from pathlib import Path
import argparse, hashlib, json, re, subprocess, sys

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def no_duplicates(pairs):
    out={}
    for k,v in pairs:
        if k in out:raise ValueError('duplicate JSON key: '+k)
        out[k]=v
    return out

def readj(path):
    return json.loads(Path(path).read_text(),object_pairs_hook=no_duplicates)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--packet',type=Path,required=True)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    out=Path(__file__).resolve().parents[1];packet=args.packet.resolve()
    failures=[];checks={}
    def check(ok,label):
        if not ok:failures.append(label)
    required=['baseline-review.md','coverage-map.json','repairs.json','correspondence.json','NEW_STATEMENTS.json','STATEMENT_CHANGES.json','LEAN_GAPS.md','references.bib','source_read_receipt.json','review_notes.md','STYLE_RULES.json','principal-claim-matrix.json','source-version-manifest.json','replacements.md','stein-k3-replacement.md','source-audits/bs-source-audit.md','source-audits/bs-weak-log-corollary.md']
    for f in required:check((out/f).is_file(),'missing '+f)
    checks['required_files']=len(required)
    jsons=list(out.rglob('*.json'))
    for p in jsons:
        try:readj(p)
        except Exception as e:failures.append(str(p.relative_to(out))+': '+str(e))
    checks['json_files_parsed']=len(jsons)
    for p in out.rglob('*'):
        if p.is_file() and p.suffix in ['.md','.json','.bib','.py']:
            s=p.read_text()
            check(not any(ord(c)<32 and c not in '\n\t\r' for c in s),'control character '+str(p.relative_to(out)))

    source=readj(out/'source-version-manifest.json')
    for r in source['inputs']:
        p=packet/r['member']
        check(p.is_file(),'missing original '+r['member'])
        if p.is_file():check(p.stat().st_size==r['bytes'] and digest(p)==r['sha256'],'input hash '+r['member'])
    checks['original_input_members_checked']=len(source['inputs'])

    cov=readj(out/'coverage-map.json')
    check(len(cov['baseline_passages'])==229,'baseline passage count')
    check(all(x['literal_boundary_check'] for x in cov['baseline_passages']),'original correspondence boundaries')
    check(len({x['member'] for x in cov['files']})==len(cov['files']),'duplicate coverage member')
    check(set(x['status'] for x in cov['files']) <= {'assessed','sampled','unassessed','unavailable'},'coverage vocabulary')
    for x in cov['files']:
        p=packet/x['member'];check(p.is_file() and digest(p)==x['sha256'],'coverage binding '+x['member'])
    checks['baseline_passages']=len(cov['baseline_passages']);checks['coverage_members']=len(cov['files'])

    reps=readj(out/'repairs.json')['repairs']
    for r in reps:
        t=r['target'];s=(packet/t['member']).read_text()
        check(digest(packet/t['member'])==t['sha256'],'repair hash '+r['id'])
        check(s.count(t['old'])==1,'repair uniqueness '+r['id'])
        if t['old'] in s:
            i=s.index(t['old']);check(s[:i].count('\n')+1==t['line_start'],'repair start line '+r['id'])
            check(s[:i+len(t['old'])].count('\n')+1==t['line_end'],'repair end line '+r['id'])
        check(t['old'].startswith(t['from']) and t['old'].endswith(t['to']),'repair boundary '+r['id'])
        check(hashlib.sha256(t['old'].encode()).hexdigest()==t['old_sha256'],'repair span digest '+r['id'])
        check(bool(r['owner']),'repair owner '+r['id'])
    checks['unique_version_bound_repairs']=len(reps)

    cor=readj(out/'correspondence.json')
    for c in cor:
        text=(out/c['document']).read_text()
        matches=list(re.finditer(r'<!-- passage:'+re.escape(c['passage'])+r' -->\s*(.*?)\s*<!-- /passage:'+re.escape(c['passage'])+r' -->',text,re.S))
        check(len(matches)==1,'return anchor '+c['passage'])
        if matches:
            body=matches[0].group(1);check(body.startswith(c['from']) and body.endswith(c['to']),'return correspondence boundary '+c['passage'])
        check(c['role'] in ['states','defines','proves','explains','uses','mentions'],'correspondence role '+c['passage'])
        check(not c['names_mentioned_without_new_type_claim'],'unresolved named type '+c['passage'])
        for t in c['formal_correspondences']:
            check(bool(t.get('source',{}).get('complete_type_text')),'missing complete type '+c['passage'])
    checks['return_correspondence_passages']=len(cor)

    matrix=readj(out/'principal-claim-matrix.json')
    check(len(matrix['rows'])==121 and len({r['id'] for r in matrix['rows']})==121,'original claim row count')
    selected=[t for r in matrix['rows'] for t in r['selected_ties']]
    aux=readj(out/'evidence/auxiliary-types.json')['declarations']
    receipts=readj(out/'evidence/hash-membership-audit.json')
    root=next(r for r in receipts['receipts'] if r['kind']=='lean-build-root' and r['source_state']=='current') if any(r['kind']=='lean-build-root' for r in receipts['receipts']) else next(r for r in receipts['receipts'] if r['kind']!='comparator' and r['source_state']=='current')
    for t in selected+list(aux.values()):
        ss=t['source'];p=packet/ss['member']
        check(digest(p)==ss['sha256'],'type source hash '+ss['member'])
        lines=p.read_text().splitlines();span='\n'.join(lines[ss['line_start']-1:ss['line_end']])
        check(ss['source_header'].strip() in span,'type source span '+ss['member']+':'+str(ss['line_start']))
        check(bool(ss.get('complete_type_text')),'complete type '+ss['member'])
        check(bool(t.get('current_root_build_receipt')),'root receipt '+ss['member'])
    checks['principal_original_claim_rows']=len(matrix['rows']);checks['selected_type_ties']=len(selected);checks['auxiliary_type_records']=len(aux)
    for r in receipts['receipts']:
        if r['source_state']=='current':
            a=r['source_audit'];check(a['inputs']==a['matching'] and not a['missing'] and not a['mismatches'],'receipt binding '+r['member'])
    for r in receipts['per_module_acceptance']:
        a=r['source_audit'];check(a['inputs']==a['matching'] and not a['missing'] and not a['mismatches'],'module binding '+r['module'])
    checks['current_receipts']=sum(r['source_state']=='current' for r in receipts['receipts'])
    checks['per_module_input_closures']=len(receipts['per_module_acceptance'])

    keys=re.findall(r'@\w+\{([^,]+)',(out/'references.bib').read_text())
    check(len(keys)==len(set(keys)),'duplicate bibliography keys')
    for key in ['OpenAI2026','BS21','GTW21','BHMT2002','Drucker2012','ABKRT2021','AA18']:
        check(key in keys,'required primary citation '+key)
    checks['bibliography_keys']=len(keys)
    states=readj(out/'NEW_STATEMENTS.json')
    check(len({x['id'] for x in states})==len(states),'new statement unique IDs')
    checks['new_explanatory_statements']=len(states)

    proc=subprocess.run([sys.executable,str(out/'checks/finite_checks.py')],capture_output=True,text=True)
    check(proc.returncode==0,'finite arithmetic process')
    if proc.returncode==0:
        result=json.loads(proc.stdout);check(result['status']=='passed','finite arithmetic assertions')
        saved=out/'checks/finite-checks.json'
        if saved.exists():check(result==readj(saved),'finite output reproducibility')
        checks['finite_checks']=result['status']
    result={'status':'passed' if not failures else 'failed','scope':'Input hashes, exact locations, JSON/correspondence/type-source consistency and finite arithmetic only; no new Lean, Comparator or theorem certification.','checks':checks,'failures':failures,'not_performed':['Lean compilation','Comparator execution','Complete imported proof audit','Final integrated manuscript rendering']}
    if args.output:args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if not failures else 1

if __name__=='__main__':raise SystemExit(main())
