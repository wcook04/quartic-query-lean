#!/usr/bin/env python3
"""Validate the return's JSON, anchors, display coverage and type consistency.

This checks the handoff structure, not mathematical truth or Lean proofs.
Run from any directory; an optional positional argument overrides the return
directory. The result is written to stdout.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory',type=Path,nargs='?',default=Path(__file__).resolve().parents[1])
    root=parser.parse_args().directory.resolve()
    required=['section.md','worked_example.md','correspondence.json','lean_types.json',
              'NEW_STATEMENTS.json','STATEMENT_CHANGES.json','LEAN_GAPS.md',
              'references.bib','source_read_receipt.json','review_notes.md',
              'STYLE_RULES.json','evidence_audit.json','README.md',
              'checks/check_adaptive_example.py','checks/check_result.json',
              'checks/audit_packet.py','checks/source_binding_result.json']
    assert all((root/p).is_file() for p in required)
    for p in root.rglob('*.json'):
        if p == root/'checks/validation.json':
            continue  # May be the stdout destination of this invocation.
        json.loads(p.read_text())
    section=(root/'section.md').read_text()
    starts=re.findall(r'<!-- passage:([^ ]+) -->',section)
    ends=re.findall(r'<!-- /passage:([^ ]+) -->',section)
    assert starts==ends and len(starts)==len(set(starts))
    passages={m.group(1):m.group(2).strip() for m in re.finditer(
        r'<!-- passage:([^ ]+) -->\n(.*?)\n<!-- /passage:\1 -->',section,re.S)}
    rows=json.loads((root/'correspondence.json').read_text())
    types=json.loads((root/'lean_types.json').read_text())['declarations']
    types={d['declaration']:d for d in types}
    assert set(passages)=={r['passage'] for r in rows}
    covered_claims=set()
    covered_displays=[]
    used_types=set()
    allowed_roles={'states','defines','proves','explains','uses','mentions'}
    for row in rows:
        body=passages[row['passage']]
        assert body.startswith(row['from']) and body.endswith(row['to'])
        assert row['role'] in allowed_roles
        covered_claims.update(row['statement_ids'])
        actual={d['declaration']:d for d in row['complete_lean_types']}
        names=set(row['lean']+row['supporting_lean'])
        assert names==set(actual)
        used_types.update(names)
        for name in names:
            assert actual[name]['source_signature']==types[name]['source']['signature']
            assert actual[name]['complete_lexical_context']==types[name]['source']['section_context']
            assert actual[name]['elaborated_type_observation']==types[name]['elaborated_type_observation']
            assert actual[name]['actual_evidence']==types[name]['evidence']
        for display in row['displays']:
            assert display['exact_display'] in body
            covered_displays.append(display['label'])
    claims=set(re.findall(r'<!-- claim:([^ ]+) -->',section))
    assert claims <= covered_claims
    labels=re.findall(r'\\tag\{([^}]+)\}',section)
    assert len(labels)==len(set(labels)) and sorted(labels)==sorted(covered_displays)
    assert section.count('\\[')==section.count('\\]')==len(labels)
    assert section.count('$') % 2 == 0
    added=json.loads((root/'NEW_STATEMENTS.json').read_text())
    assert len({x['id'] for x in added})==len(added)
    assert all(x['id'] in covered_claims and x['passage'] in passages for x in added)
    assert json.loads((root/'STATEMENT_CHANGES.json').read_text())==[]
    bibkeys=set(re.findall(r'@\w+\{([^,]+),',(root/'references.bib').read_text()))
    assert all(c['key'] in bibkeys for r in rows for c in r['citation_role'])
    example=json.loads((root/'checks/check_result.json').read_text())
    source=json.loads((root/'checks/source_binding_result.json').read_text())
    assert example['all_assertions_passed'] and source['all_byte_checks_passed']
    print(json.dumps({
        'kind':'return structure and consistency check','passed':True,
        'section_sha256':hashlib.sha256(section.encode()).hexdigest(),
        'passage_anchors':len(starts),'numbered_displays':len(labels),
        'new_statement_ids':[x['id'] for x in added],
        'canonical_statements_changed':0,'type_records':len(types),
        'types_used_in_correspondence':len(used_types),
        'supplied_elaborated_type_records':sum(x['elaborated_type_observation'] is not None for x in types.values()),
        'example_check_passed':example['all_assertions_passed'],
        'input_byte_check_passed':source['all_byte_checks_passed'],
        'equation_delimiters_and_labels_checked':True,
        'fresh_lean_execution':False,'fresh_comparator_execution':False,
        'integrated_paper_rendered':False,'human_mathematical_review':False,
        'scope':'JSON, anchors, displays, supplied-type consistency and prior exact-check outputs; not a mathematical proof checker.'
    },indent=2))


if __name__=='__main__':
    main()
