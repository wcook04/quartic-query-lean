from pathlib import Path
import argparse,hashlib,json,re,shutil
parser=argparse.ArgumentParser(description='Recheck the supplied round-three job02 packet bytes and scoped evidence without running Lean or editing the packet.')
parser.add_argument('--packet',type=Path,required=True,help='Extracted round-three job02 packet root')
parser.add_argument('--output',type=Path,default=Path('evidence_audit_output'),help='Directory for newly computed JSON evidence')
parser.add_argument('--archive',type=Path,help='Optional original ZIP for its SHA-256')
args=parser.parse_args()
R=args.packet.resolve()
O=args.output.resolve()
if O==R or R in O.parents: raise ValueError('Output must be outside the preserved packet.')
O.mkdir(parents=True,exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(n,x): (O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def read(n):return json.loads((R/n).read_text())
def chk(mapping,prefix=''):
 results=[]
 for p,h in mapping.items():
  f=R/prefix/p
  results.append({'member':str(f.relative_to(R)), 'exists':f.is_file(), 'sha256_matches':f.is_file() and sha(f)==h})
 return results
m=read('manifest.json')
members=[]
for e in m['members']:
 p=R/e['member']
 members.append({'member':e['member'],'exists':p.is_file(),'bytes_match':p.is_file() and p.stat().st_size==e['bytes'],'sha256_match':p.is_file() and sha(p)==e['sha256']})
inputs=chk(m['input_sha256'])
root=read('repository/corpus/receipts/lean-build-root-2026-11-02T182539383153+0000.json')
full=chk(root['source_hashes'],'repository')
actual_local={str(p.relative_to(R/'repository')):sha(p) for p in (R/'repository/lean').rglob('*') if p.is_file() and (p.suffix=='.lean' or p.name in ['lean-toolchain','lakefile.toml','lake-manifest.json','comparator.json'] or (p.parent.name=='Negative' and p.suffix=='.json'))}
e=read('EVIDENCE_SNAPSHOT.json')
receipts=[]
for q in e['receipts']:
 d=read(q['member']); checks=chk(d.get('source_hashes',{}),'repository')
 receipts.append({'member':q['member'],'kind':q['kind'],'name':q['name'],'status':q['status'],'declared_source_currentness':q['source_currentness'],'sha256_matches_snapshot':sha(R/q['member'])==q['sha256'],'source_hash_count':len(checks),'source_matches':all(x['sha256_matches'] for x in checks) if checks else None,'source_hash_set_matches_full_snapshot':set(d.get('source_hashes',{}))==set(root['source_hashes']),'declarations':d['declarations'],'sandboxed':d.get('sandboxed'),'paranoid':d.get('paranoid'),'exit_code':d.get('exit_code')})
dep=read('repository/corpus/lean_dependencies.json')
ver=read('native_results/final-evidence/reviewed_axiom_audit_verdict.json')
audit=read('native_results/final-evidence/reviewed_axiom_audit.json')
auditlog=R/'native_logs/final-evidence/reviewed-type-axiom-audit.log'
audittext=auditlog.read_text()
recordtypes={}
pat=re.compile(r"^([A-Za-z][\w.]*)\s.*?^'\1' (?:depends on axioms: \[[^\n]*\]|does not depend on any axioms)\s*$",re.M|re.S)
# A safer splitter uses exact expected declaration names, so adjacent blocks never bleed.
for n in audit['declarations']:
 start=re.search(r'^'+re.escape(n)+r'(?=\.\{|\s|\s*:)',audittext,re.M)
 end=re.search(r"^'"+re.escape(n)+r"' (.+)$",audittext,re.M)
 if start and end and start.start()<end.start():
  recordtypes[n]={'type_printout':audittext[start.start():end.start()].strip(),'axioms_printout':end.group(1)}
unexpected_axioms=[]
for n,v in recordtypes.items():
 found=re.search(r'\[([^]]*)\]',v['axioms_printout'])
 declared=[] if found is None else [x.strip() for x in found.group(1).split(',') if x.strip()]
 unexpected=sorted(set(declared)-set(ver['allowed_axioms']))
 if unexpected: unexpected_axioms.append({'declaration':n,'unexpected_axioms':unexpected})
comparator={n:[q['member'] for q in receipts if q['kind']=='comparator' and q['status']=='passed' and q['declared_source_currentness']=='current' and n in q['declarations']] for n in root['declarations']}
ids=['def-walsh-sign','eq-3','eq-4','claim-proj-prob','lem-2.1.ii','claim-N-phi','claim-integer-tests','claim-circuit-size','lem-2.1.iii','lem-2.1']
statements=read('repository/corpus/statements.json'); ties=read('repository/corpus/ties.json')
selected=[]
for s in statements:
 if s['id'] not in ids: continue
 row={k:v for k,v in s.items() if k!='lean'}
 row['lean']=[]
 for t in s['lean']:
  n=t['declaration']; q=dict(t)
  q.update({'exact_name_in_current_root_build':n in root['declarations'],'exact_name_in_current_reach':n in dep['reached'],'current_comparator_membership':comparator.get(n,[]),'in_explicit_axiom_audit':n in audit['declarations']})
  if n in recordtypes:q.update(recordtypes[n])
  fp=R/'repository'/q['file'] if q.get('file') else None
  if fp is not None and fp.is_file():
   q['source_sha256']=sha(fp)
   source=fp.read_text()
   found=re.search(r'(?m)^(?:@\[[^\n]*\]\s*)?(?:(?:noncomputable|private|protected)\s+)*(?:theorem|lemma|def|abbrev)\s+'+r'(?:[A-Za-z_][\w]*\.)*'+re.escape(n.rsplit('.',1)[-1])+r'(?=\s|\{|:)',source)
   if found:
    rest=source[found.start():]
    if q.get('kind')=='theorem':
     # Local let-bindings can contain ':=' inside the theorem type.
     # The selected theorems use ':= by' or a final ':=' line for proof bodies.
     following=re.search(r'(?m)^(?:@\[[^\n]*\]\s*)?(?:(?:noncomputable|private|protected)\s+)*(?:theorem|lemma|def|abbrev|end)\b',rest[1:])
     bound=following.start()+1 if following else len(rest)
     region=rest[:bound]
     proof=re.search(r':= by\b',region)
     if proof is None:proof=re.search(r':=[ \t]*\n',region)
     end=found.start()+proof.start() if proof else source.find(':=',found.start())
    else:end=source.find(':=',found.start())
    if end!=-1:q['source_signature']=source[found.start():end].strip()
    q['source_signature_line']=source.count('\n',0,found.start())+1
  row['lean'].append(q)
 selected.append(row)
proposal=read('repository/research/adjudication/round2_construction_quantum_ties.json')
selected_proposal=[q for q in proposal['rows'] if q.get('id',q.get('statement_id')) in ids]
summary={'archive_sha256':sha(args.archive) if args.archive else None,'manifest_sha256':sha(R/'manifest.json'),'packet_repository_commit':m['repository_commit'],'root_receipt_commit':root['commit'],'manifest_members_checked':len(members),'manifest_member_failures':[x for x in members if not all(x.get(k,True) for k in ['exists','bytes_match','sha256_match'])],'input_sha256_entries_checked':len(inputs),'input_hash_failures':[x for x in inputs if not x['sha256_matches']],'local_lean_config_hashes_checked':len(full),'local_hash_failures':[x for x in full if not x['sha256_matches']],'local_snapshot_extra_files':sorted(set(actual_local)-set(root['source_hashes'])),'local_snapshot_missing_files':sorted(set(root['source_hashes'])-set(actual_local)),'root_declaration_count':len(root['declarations']),'dependency_export_hash_matches_snapshot':sha(R/'repository/corpus/lean_dependencies.json')==e['dependency_export']['sha256'],'dependency_export_source_checks':{'count':len(dep['source_hashes']),'all_match':all(x['sha256_matches'] for x in chk(dep['source_hashes'],'repository'))},'dependency_export_root_count':len(dep['roots']),'dependency_export_reached_count':len(dep['reached']),'dependency_export_unresolved':dep['unresolved_constants'],'axiom_verdict_passed':ver['passed'],'axiom_log_hash_matches_verdict':sha(auditlog)==ver['log_sha256'],'axiom_source_hash_matches_verdict':sha(R/'native_sources/final-evidence/reviewed_axiom_audit.lean')==ver['audit_source_sha256'],'axiom_audit_declarations':len(audit['declarations']),'axiom_audit_unique_names':len(set(audit['declarations'])),'axiom_audit_all_names_in_root':set(audit['declarations']).issubset(root['declarations']),'axiom_success_marker_present':'R2_AXIOM_AUDIT_OK declarations=258' in audittext,'axiom_printout_unexpected_axioms':unexpected_axioms,'axiom_type_blocks_found':len(recordtypes),'axiom_allowed':ver['allowed_axioms'],'local_lean_available':shutil.which('lean'),'local_lake_available':shutil.which('lake'),'new_build_executed':False,'limits':['Input bytes and included receipt/log hashes independently checked; recorded external native execution itself was not repeated.','Dependency manifest revisions are bound, but all dependency checkout bytes and tool executable bytes were not part of the 124-source root receipt.','No compiled .olean artifact was supplied here for independent hash check of recorded native artifact.','Before/after source hashes do not detect an intervening edit-and-revert.','No current Comparator receipt names Forrelation, Upper.decode or Paper.construction Forrelation declarations in this section; root theorem comparisons do not transfer to descendants or sibling helpers.']}
summary['receipt_hash_failures']=[q['member'] for q in receipts if not q['sha256_matches_snapshot']]
summary['current_receipt_binding_failures']=[q['member'] for q in receipts if q['declared_source_currentness']=='current' and not(q['source_matches'] and q['source_hash_set_matches_full_snapshot'])]
summary['integrity_checks_passed']=not any(summary[k] for k in ['manifest_member_failures','input_hash_failures','local_hash_failures','local_snapshot_extra_files','local_snapshot_missing_files','axiom_printout_unexpected_axioms','receipt_hash_failures','current_receipt_binding_failures']) and all(summary[k] for k in ['dependency_export_hash_matches_snapshot','axiom_verdict_passed','axiom_log_hash_matches_verdict','axiom_source_hash_matches_verdict','axiom_audit_all_names_in_root','axiom_success_marker_present']) and summary['axiom_audit_declarations']==summary['axiom_type_blocks_found']
dump('integrity_summary.json',summary)
dump('receipt_audit.json',receipts)
dump('section_statement_evidence.json',selected)
dump('section_round2_tie_proposals.json',selected_proposal)
selected_names={q['declaration'] for s in selected for q in s['lean']}
dump('recorded_lean_types.json',{k:v for k,v in recordtypes.items() if k in selected_names})
print(json.dumps(summary,ensure_ascii=False,indent=2))
print('\nSECTION SUMMARY')
for s in selected:
 print(s['id'],s.get('evidence'))
 for q in s['lean']:
  if q['relation'] in ['exact','stronger'] or q['declaration'].startswith('QuarticQuery.Paper'):
   print(' ',q['declaration'],'relation',q['relation'],'built',q['exact_name_in_current_root_build'],'reached',q['exact_name_in_current_reach'],'compared',bool(q['current_comparator_membership']),'axioms',q['in_explicit_axiom_audit'])

if not summary['integrity_checks_passed']:raise SystemExit(1)
