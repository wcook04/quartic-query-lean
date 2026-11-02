"""Consistency checks for this research return. No Lean elaboration is attempted.

Run: python validate_package.py
The mathematical and formal-evidence limits are described in VALIDATION.md.
"""
import hashlib
import json
import re
from pathlib import Path

root=Path(__file__).resolve().parent
required=['note.md','references.bib','quantitative.md','prior_art.json',
          'correspondence.json','NEW_STATEMENTS.json','STATEMENT_CHANGES.json','LEAN_GAPS.md']
for name in required:
    assert (root/name).is_file(),name
data={p.name:json.loads(p.read_text()) for p in root.glob('*.json')}
rows=data['NEW_STATEMENTS.json']
ids=[r['id'] for r in rows]
assert len(ids)==len(set(ids))
original=data['original_statement_index.json']['statements']
known=set(ids)|{r['id'] for r in original}
sources={r['declaration'] for r in data['source_declarations.json']['declarations']}
for r in original:
    sources.update(x['declaration'] for x in r.get('lean',[]))
for r in rows:
    assert {'id','statement','why_needed','depends_on','proposed_lean','route_note'}<=r.keys(),r['id']
    assert r['proposed_lean'].strip().startswith(('theorem ','noncomputable def ')),r['id']
    assert 'not elaborated or compiled' in r['signature_status'],r['id']
    assert not re.search(r'\b(sorry|admit)\b',r['proposed_lean']),r['id']
    for dep in r['depends_on']:
        assert dep in known or dep in sources,(r['id'],dep)

bibkeys=set(re.findall(r'@\w+\{([^,]+),',(root/'references.bib').read_text()))
for r in data['prior_art.json']['items']:
    assert {'status','closest_work','locator','difference'}<=r.keys()
    assert r['status'] in {'known','partly_known','not_found'}
    for w in r['closest_work']:
        if 'citation_key' in w:assert w['citation_key'] in bibkeys,w['citation_key']

passages=data['correspondence.json']
assert len({r['passage'] for r in passages})==len(passages)
indexed=0
for r in passages:
    text=(root/r['file']).read_text()
    pat=r'<!-- passage:'+re.escape(r['passage'])+r' -->(.*?)<!-- /passage:'+re.escape(r['passage'])+r' -->'
    found=re.findall(pat,text,re.S)
    assert len(found)==1,r['passage']
    body=found[0].strip()
    assert body.startswith(r['from']) and body.endswith(r['to']),r['passage']
    assert r['role'] in {'states','defines','proves','explains','uses','mentions'}
    for s in r['statement_ids']:assert s in known,(r['passage'],s)
    for name in r['lean']:assert name in sources,(r['passage'],name)
    for key in r['bibliography_keys']:assert key in bibkeys,key
    displays=re.findall(r'\$\$(.*?)\$\$',body,re.S)
    assert len(displays)==len(r['displays']),r['passage']
    for formula,entry in zip(displays,r['displays']):
        assert hashlib.sha256(formula.encode()).hexdigest()==entry['sha256'],entry['locator']
        for s in entry['statement_ids']:assert s in known,(entry['locator'],s)
    indexed+=len(displays)

math_blocks=0
for name in ['note.md','quantitative.md']:
    text=(root/name).read_text()
    anchors=re.findall(r'<!-- passage:([\w-]+) -->',text)
    assert set(anchors)=={r['passage'] for r in passages if r['file']==name},name
    assert text.count('$$')%2==0,name
    blocks=re.findall(r'\$\$(.*?)\$\$',text,re.S)
    stripped=re.sub(r'\$\$.*?\$\$','',text,flags=re.S)
    assert len(re.findall(r'(?<!\\)\$',stripped))%2==0,name
    blocks+=re.findall(r'(?<!\\)\$(.*?)(?<!\\)\$',stripped,re.S)
    for formula in blocks:
        depth=0
        for token in re.findall(r'(?<!\\)[{}]',formula):
            depth+=1 if token=='{' else -1
            assert depth>=0,(name,formula)
        assert depth==0,(name,formula)
        assert not re.search(r'(?<!\\)mathbb\b',formula),(name,formula)
        assert len(re.findall(r'\\begin\{',formula))==len(re.findall(r'\\end\{',formula)),(name,formula)
    assert '—' not in text,name
    math_blocks+=len(blocks)

for r in data['STATEMENT_CHANGES.json']:
    assert {'id','old','new','relation','reason'}<=r.keys()
    assert r['relation'] in {'stronger','weaker','equivalent','corrected'}
    assert not r['affects_frozen_corpus']

check=data['checks_output.json']
assert all(check['exact_constants'].values())
assert check['restriction_identity']['max_error']=='0'
result={
    'status':'passed',
    'required_files_present':required,
    'new_statement_records':len(rows),
    'original_statement_records_preserved':len(original),
    'anchored_passages':len(passages),
    'displayed_formulas_indexed':indexed,
    'math_blocks_brace_checked_including_inline':math_blocks,
    'bibliography_entries':len(bibkeys),
    'prior_art_ingredients':len(data['prior_art.json']['items']),
    'declaration_locations_indexed':len(data['source_declarations.json']['declarations']),
    'checks':['JSON syntax and required schemas','unique IDs and dependency references',
      'exact passage boundaries','display hashes and coverage','referenced source declaration names',
      'bibliography keys','balanced math delimiters and braces','exact finite-check outcomes'],
    'not_performed':['Lean elaboration','Lean or Lake build','Comparator run',
      'external kernel replay','certified quadrature error estimation','human review']}
(root/'validation_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
