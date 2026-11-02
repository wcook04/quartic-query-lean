#!/usr/bin/env python3
"""Validate this return's archive bytes and basic handoff structure.
This validates packaging, JSON, source syntax and correspondence references;
it does not elaborate Lean, run Comparator, or certify mathematical meaning.
"""
import argparse,ast,hashlib,json,re,zipfile
from pathlib import Path,PurePosixPath

def json_unique(data):
 def pairs(xs):
  out={}
  for k,v in xs:
   if k in out:raise ValueError('Duplicate JSON key: '+k)
   out[k]=v
  return out
 return json.loads(data,object_pairs_hook=pairs)

def check_content(files):
 required={'README.md','evidence-path.md','acceptance_cases.json','correspondence.json','NEW_STATEMENTS.json','STATEMENT_CHANGES.json','LEAN_GAPS.md','references.bib','source_read_receipt.json','review_notes.md','STYLE_RULES.json'}
 assert required<=set(files),'Required return file missing'
 parsed={n:json_unique(b) for n,b in files.items() if n.endswith('.json')}
 for n,b in files.items():
  if n.endswith('.py'):ast.parse(b.decode(),filename=n)
 report=files['evidence-path.md'].decode()
 anchors={m.group(1):m.group(2) for m in re.finditer(r'<!-- passage:([^ ]+) -->\n(.*?)\n<!-- /passage:\1 -->',report,re.S)}
 assert len(anchors)==12
 roles={'states','defines','proves','explains','uses','mentions'}
 for row in parsed['correspondence.json']:
  assert row['passage'] in anchors
  body=anchors[row['passage']]
  assert row['from'] in body and row['to'] in body
  assert body.index(row['from'])<=body.rindex(row['to'])
  assert row['role'] in roles
  assert set(row['lean'])=={x['declaration'] for x in row['complete_lean_types']}
  for key in ['ordinary_premises','open_assumptions','relation','route','citation_role','evidence_state']:assert key in row
  for t in row['complete_lean_types']:
   assert t['type'] and t['source'] and t['type_evidence']
   assert t['source'].startswith('repository/') or t['source'] in files
 for row in parsed['NEW_STATEMENTS.json']:
  assert {'id','statement','why_needed','depends_on','proposed_lean','route_note'}<=row.keys()
 assert parsed['STATEMENT_CHANGES.json']==[]
 cases=parsed['acceptance_cases.json']['cases'];assert len({x['id'] for x in cases})==len(cases)
 for case in cases:
  base=case.get('path_base','')
  for key in ['receipt','config','command_evidence','historical_receipt']:
   if key in case:assert base+case[key] in files,(case['id'],key,base+case[key])
  for key in ['evidence','files']:
   for ref in case.get(key,[]):assert base+ref in files,(case['id'],ref)
 for member in files:assert '/Round3/' not in member,'Obsolete staging files included'
 holes=[]
 for n,b in files.items():
  if n.endswith('.lean'):
   for lineno,line in enumerate(b.decode().splitlines(),1):
    if re.match(r'^\s*(sorry|admit)\b',line):holes.append({'file':n,'line':lineno,'text':line.strip()})
 assert len(holes)==4 and all('Challenge.lean' in x['file'] for x in holes),holes
 assert report.count(r'\[')==report.count(r'\]')
 assert report.count(r'\(')==report.count(r'\)')
 assert report.count('$')%2==0
 return {'json_files':len(parsed),'python_files':sum(n.endswith('.py') for n in files),'lean_files':sum(n.endswith('.lean') for n in files),'correspondence_entries':len(parsed['correspondence.json']),'passage_anchors':len(anchors),'acceptance_cases':len(cases),'derived_control_entries':len(parsed['NEW_STATEMENTS.json']),'intentional_challenge_holes':holes,'required_files_present':True,'correspondence_boundaries_match':True,'acceptance_paths_resolve':True,'json_parse_with_duplicate_key_check':'passed','python_ast_parse':'passed','markdown_math_delimiter_balance':'passed','scope':'Packaging/source checks only; no native Lean, Comparator, consumer or visual rendering.'}

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('target',type=Path);ap.add_argument('--out',type=Path);a=ap.parse_args()
 if a.target.is_dir():
  files={str(p.relative_to(a.target)):p.read_bytes() for p in a.target.rglob('*') if p.is_file() and p.name!='manifest.json'}
  result={'kind':'actual_prearchive_return_structure_check',**check_content(files),'checked_payload_files':len(files),'archive_integrity':'not_applicable_directory_check'}
 else:
  with zipfile.ZipFile(a.target) as z:
   names=z.namelist();assert len(names)==len(set(names))
   for n in names:
    q=PurePosixPath(n);assert not q.is_absolute() and '..' not in q.parts and '\\' not in n
   files={n:z.read(n) for n in names}
  m=json_unique(files['manifest.json']);members=m['members'];assert {x['member'] for x in members}==set(files)-{'manifest.json'}
  for x in members:
   b=files[x['member']];assert len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'],x['member']
  result={'kind':'actual_final_return_archive_validation',**check_content(files),'archive':a.target.name,'archive_sha256':hashlib.sha256(a.target.read_bytes()).hexdigest(),'archive_bytes':a.target.stat().st_size,'archive_members':len(files),'manifest_payload_members':len(members),'archive_integrity':'passed','duplicate_names':False,'unsafe_member_paths':False}
 result['passed']=True
 if a.out:a.out.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
 return 0
if __name__=='__main__':raise SystemExit(main())
