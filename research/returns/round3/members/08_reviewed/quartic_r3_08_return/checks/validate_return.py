#!/usr/bin/env python3
"""Validate this editorial return's bytes, references, and correspondence.

This is a structural and exact-finite-check runner, not a Lean parser, new Lean
execution, or mathematical acceptance test. No third-party packages are needed.
Run from any directory. Optionally pass --input /path/to/the/extracted/input.
The script reads files and prints JSON; it does not modify them.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    required = {
        'README.md', 'section.md', 'correspondence.json', 'NEW_STATEMENTS.json',
        'STATEMENT_CHANGES.json', 'LEAN_GAPS.md', 'references.bib',
        'source_read_receipt.json', 'review_notes.md', 'STYLE_RULES.json',
        'evidence_validation.json', 'checks/exact_checks.py',
        'checks/exact_checks.json', 'checks/validate_return.py',
        'checks/validation_result.json', 'manifest.json',
    }
    actual_files = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
    assert required == actual_files, {'missing':sorted(required-actual_files), 'extra':sorted(actual_files-required)}
    documents = {name:json.loads((root/name).read_text()) for name in actual_files if name.endswith('.json')}
    manifest = documents['manifest.json']
    assert set(manifest['files']) == actual_files - {'manifest.json'}
    for name, item in manifest['files'].items():
        data = (root/name).read_bytes()
        assert item['size_bytes'] == len(data), name
        assert item['sha256'] == sha(data), name

    section = (root/'section.md').read_text()
    section_hash = sha((root/'section.md').read_bytes())
    starts = re.findall(r'<!-- passage:([^\s]+) -->', section)
    ends = re.findall(r'<!-- /passage:([^\s]+) -->', section)
    assert starts == ends and len(starts) == len(set(starts))
    rows = documents['correspondence.json']
    assert [r['passage'] for r in rows] == starts
    known_ids = set(manifest['known_statement_ids'])
    display_count = 0
    claim_count = 0
    support_count = 0
    names = set()
    for row in rows:
        anchor = row['passage']
        body = re.search(r'<!-- passage:'+re.escape(anchor)+r' -->(.*?)<!-- /passage:'+re.escape(anchor)+r' -->', section, re.S).group(1).strip()
        assert row['from'] and body.startswith(row['from']), anchor
        assert row['to'] and body.endswith(row['to']), anchor
        assert row['passage_sha256'] == sha(body.encode()), anchor
        assert row['section_sha256'] == section_hash, anchor
        assert row['role'] in {'states','defines','proves','explains','uses','mentions'}
        assert set(row['statement_ids']) <= known_ids, anchor
        support = {x['declaration']:x for x in row['formal_support']}
        assert set(row['lean']) == set(support), anchor
        names.update(row['lean'])
        support_count += len(row['formal_support'])
        for name, formal in support.items():
            assert '.' in name
            assert isinstance(formal['complete_type'],str) and formal['complete_type'].strip(), name
            assert '...' not in formal['complete_type'] and '…' not in formal['complete_type'], name
        claims = row['mathematical_claims']
        claim_count += len(claims)
        for claim in claims:
            assert all(k in claim for k in ['premises','open_assumptions','relation','route','citation_role','evidence_state','lean']), (anchor,claim)
            assert set(claim['lean']) <= set(support), (anchor,claim)
            assert set(claim.get('statement_ids',[])) <= known_ids, (anchor,claim)
            if claim.get('exact_excerpt'):
                assert claim['exact_excerpt'] in body, (anchor,claim)
        displays = re.findall(r'\\\[(.*?)\\\]',body,re.S)
        display_count += len(displays)
        if 'display_inventory' in row:
            assert [x['exact_tex'] for x in row['display_inventory']] == displays, anchor
            claim_ids = {x.get('claim_id',x.get('claim_label')) for x in claims}
            for display in row['display_inventory']:
                assert display['covered_by_claims'] and set(display['covered_by_claims']) <= claim_ids, anchor
        else:
            excerpts = [x.get('exact_excerpt') or '' for x in claims]
            for display in displays:
                assert any('\\['+display+'\\]' in excerpt for excerpt in excerpts), (anchor,display)
    assert section.count('\\[') == section.count('\\]') == display_count
    assert section.count('\\(') == section.count('\\)')
    assert not re.search(r'\b(?:TODO|FIXME|TBD)\b',section)

    bib = (root/'references.bib').read_text()
    bibkeys = set(re.findall(r'@\w+\s*\{\s*([^,]+)',bib))
    assert {'OpenAI2026','ABKRT2020','Huang2019','Midrijanis2004','SS2006','HLS2007','BSS2003'} <= bibkeys
    linkrefs = set(re.findall(r'\]\[([^\]]+)\]',section))
    definitions = set(re.findall(r'^\[([^\]]+)\]:\s+https?://',section,re.M))
    assert linkrefs <= definitions <= bibkeys
    assert documents['NEW_STATEMENTS.json'] == []
    change = documents['STATEMENT_CHANGES.json']
    assert len(change) == 1 and change[0]['id'] == 'claim-huang-spectrum'
    assert 'd >= 1' in change[0]['new']
    assert documents['source_read_receipt.json']['section_sha256'] == section_hash

    finite = subprocess.run([sys.executable,str(root/'checks/exact_checks.py')],capture_output=True,text=True,check=True)
    assert json.loads(finite.stdout) == documents['checks/exact_checks.json']
    assert documents['checks/exact_checks.json']['status'] == 'passed'
    evidence = documents['evidence_validation.json']
    assert evidence['all_input_hashes_match'] and evidence['input_hash_count'] == 472
    assert all(x['matches'] for x in evidence['input_hash_checks'])
    assert all(x['all_source_hashes_match'] for x in evidence['supplied_receipts'])
    assert all(x['matches'] for x in evidence['formal_support_source_checks'])
    source_checks = None
    if args.input:
        source_checks = 0
        for item in evidence['input_hash_checks']:
            path = args.input/item['path']
            assert path.is_file() and sha(path.read_bytes()) == item['expected_sha256'], item['path']
            source_checks += 1
        for item in evidence['formal_support_source_checks']:
            path = args.input/item['source_path']
            if not path.is_file():
                path = args.input/'repository'/item['source_path']
            assert path.is_file() and sha(path.read_bytes()) == item['source_sha256'], item['declaration']

    result = {
        'status':'passed',
        'scope':'Return bytes, exact references, correspondence structure, and independently executed finite checker; no new Lean or Comparator execution.',
        'files_including_manifest':len(actual_files),
        'payload_hashes_verified':len(manifest['files']),
        'passages':len(rows),
        'claim_records':claim_count,
        'displayed_equations':display_count,
        'formal_support_entries':support_count,
        'distinct_named_declarations':len(names),
        'complete_types_nonempty_without_ellipsis':True,
        'exact_passage_boundaries_and_display_inventory':True,
        'bibliography_keys_and_reference_links':True,
        'finite_check_output_reproduced':True,
        'original_input_hashes_rechecked_in_this_run':source_checks,
        'new_lean_execution':False,
        'new_comparator_execution':False,
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
