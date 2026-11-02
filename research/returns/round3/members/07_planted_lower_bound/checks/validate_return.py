#!/usr/bin/env python3
"""Validate this return's structure and exact-file correspondence, not its theorems.

Run from any directory. Optional --source-packet PATH additionally checks the
source hashes and literal signatures against the extracted original packet.
The script writes nothing. The examples and floor checks are separate scripts.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-packet', type=Path)
    args = parser.parse_args()
    base = Path(__file__).resolve().parent.parent
    required = [
        'README.md', 'section.md', 'correspondence.json', 'NEW_STATEMENTS.json',
        'STATEMENT_CHANGES.json', 'EVIDENCE_CORRECTIONS.json', 'LEAN_GAPS.md',
        'references.bib', 'source_read_receipt.json', 'review_notes.md',
        'STYLE_RULES.json', 'evidence/lean_declarations.json',
        'evidence/lean_evidence.json', 'lean/Eq19Complete.lean',
        'checks/planted_example.py', 'checks/planted_example.json',
        'checks/check_floors.py', 'checks/check_floors.json',
        'checks/validate_return.py',
    ]
    for member in required:
        require((base / member).is_file(), f'Missing required file: {member}')
    all_files = sorted(p for p in base.rglob('*') if p.is_file())
    for path in all_files:
        require(not path.is_symlink(), f'Unexpected symlink: {path}')
        require('__pycache__' not in path.parts, f'Unexpected cache file: {path}')

    json_files = [p for p in all_files if p.suffix == '.json']
    parsed = {str(p.relative_to(base)): read_json(p) for p in json_files}
    for path in all_files:
        if path.suffix in {'.md', '.json', '.lean', '.bib', '.py'}:
            text = path.read_text()
            require(not any(ord(c) < 32 and c not in '\n\r\t' for c in text),
                    f'Unexpected control character: {path}')

    section = (base / 'section.md').read_text()
    chunks = re.findall(r'<!-- passage:([^ ]+) -->\n(.*?)\n<!-- /passage:\1 -->',
                        section, re.S)
    starts = re.findall(r'<!-- passage:([^ ]+) -->', section)
    ends = re.findall(r'<!-- /passage:([^ ]+) -->', section)
    require(len(chunks) == len(starts) == len(ends), 'Unbalanced passage comments')
    require(len(starts) == len(set(starts)), 'Duplicate passage anchor')
    passages = dict(chunks)
    correspondence = parsed['correspondence.json']
    require(len(correspondence) == len(passages), 'Correspondence count mismatch')
    require(set(passages) == {r['passage'] for r in correspondence},
            'Correspondence passage names mismatch')
    catalog = parsed['evidence/lean_declarations.json']
    records = {r['declaration']: r for r in catalog['records']}
    require(len(records) == catalog['record_count'], 'Declaration count mismatch')
    allowed_roles = {'states', 'defines', 'proves', 'explains', 'uses', 'mentions'}
    all_ids = set()
    display_count = 0
    selected = set()
    type_occurrences = 0

    def check_types(names, types):
        nonlocal type_occurrences
        require(names == [t['declaration'] for t in types], 'Type/name mismatch')
        for typ in types:
            name = typ['declaration']
            require(name.startswith('QuarticQuery.'), f'Unqualified name: {name}')
            require(name in records, f'Missing source declaration: {name}')
            record = records[name]
            expected = (record.get('recorded_elaborated_type')
                        or record.get('complete_source_type_fully_qualified_projects')
                        or record.get('complete_source_type'))
            require(bool(expected), f'Only an incomplete/raw signature remains: {name}')
            require(typ['complete_type'] == expected, f'Type mismatch: {name}')
            require(bool(typ['type_status']), f'Missing type evidence label: {name}')
            require(typ['fresh_execution'] is False, f'Unexpected fresh-execution claim: {name}')
            require(typ['source_sha256'] == record['source_sha256'],
                    f'Source hash differs between type and catalog: {name}')
            require(typ['root_build_membership'] == record.get('root_build_membership'),
                    f'Build evidence mismatch: {name}')
            require(typ['explicit_transitive_axiom_audit'] == record.get('explicitly_axiom_audited'),
                    f'Axiom audit evidence mismatch: {name}')
            selected.add(name)
            type_occurrences += 1

    for row in correspondence:
        name = row['passage']
        body = passages[name]
        require(body.startswith(row['from']), f'Wrong from excerpt: {name}')
        require(body.endswith(row['to']), f'Wrong to excerpt: {name}')
        require(section.count(row['from']) == 1, f'Non-unique from excerpt: {name}')
        require(section.count(row['to']) == 1, f'Non-unique to excerpt: {name}')
        require(row['role'] in allowed_roles, f'Invalid role: {name}')
        require(bool(row['statement_ids']), f'Missing statement IDs: {name}')
        for field in ['ordinary_premises', 'open_assumptions', 'relation', 'route',
                      'citation_role', 'actual_evidence_state']:
            require(field in row, f'Missing field {field}: {name}')
        claim_comments = set(re.findall(r'<!-- claim:([^ ]+) -->', body))
        require(claim_comments <= set(row['statement_ids']), f'Unmapped claim: {name}')
        all_ids.update(row['statement_ids'])
        check_types(row['lean'], row['complete_lean_types'])
        displays = [s.strip() for s in re.findall(r'\\\[(.*?)\\\]', body, re.S)]
        require(displays == [d['latex'] for d in row['display_inventory']],
                f'Display inventory differs from section: {name}')
        for index, display in enumerate(row['display_inventory'], 1):
            require(index == display['index_in_passage'], f'Display ordering: {name}')
            for field in ['relation', 'ordinary_premises', 'open_assumptions',
                          'route', 'citation_role']:
                require(field in display, f'Missing display field {field}: {name}')
            check_types(display['lean'], display['complete_lean_types'])
        display_count += len(displays)
    require(section.count(r'\[') == section.count(r'\]') == display_count,
            'Display delimiters outside inventory or unbalanced')
    require(section.count(r'\(') == section.count(r'\)'), 'Unbalanced inline mathematics')

    bibliography = (base / 'references.bib').read_text()
    bibkeys = set(re.findall(r'@\w+\s*\{\s*([^,\s]+)', bibliography))
    usedkeys = set(re.findall(r'\[(ABK\w+|BS\w+|Drucker\w+|OpenAI\w+)(?:,|\])',
                             section))
    usedkeys.update(re.findall(r'\b(?:OpenAI2026Planted|ABK2019v2|BS2020v3|Drucker2014v2)\b',
                              json.dumps(correspondence)))
    require(usedkeys <= bibkeys, f'Unknown bibliography keys: {usedkeys-bibkeys}')
    internal_links = 0
    for path in [base / 'section.md', base / 'README.md', base / 'review_notes.md',
                 base / 'LEAN_GAPS.md']:
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if re.match(r'[a-z]+:', link) or link.startswith('#'):
                continue
            target = (path.parent / link.split('#', 1)[0]).resolve()
            require(target.is_relative_to(base), f'Link escapes return: {link}')
            require(target.is_file(), f'Broken local file link: {link}')
            internal_links += 1

    new_statements = parsed['NEW_STATEMENTS.json']
    new_ids = [r['id'] for r in new_statements]
    require(len(new_ids) == len(set(new_ids)), 'Duplicate new statement ID')
    for statement in new_statements:
        for field in ['id', 'statement', 'why_needed', 'depends_on', 'proposed_lean', 'route_note']:
            require(field in statement, f'Missing new-statement field: {field}')
        proposed = statement['proposed_lean']
        if proposed:
            require(proposed['status'] == 'uncompiled_proposal', 'Wrong wrapper status')
            require(proposed['complete_source'] == (base / proposed['file']).read_text(),
                    'Embedded wrapper source differs from returned source')
    require(parsed['STATEMENT_CHANGES.json'] == [],
            'This return is expected to preserve canonical baseline statements')
    require(parsed['checks/check_floors.json']['passed'] is True, 'Floor result failed')
    toy = parsed['checks/planted_example.json']
    require(toy['exact_enumeration']['Pr_hit_erased_zero']
            == toy['exact_enumeration']['E_Z_over_m'], 'Toy equality result inconsistent')
    require(toy['exact_enumeration']['coupled_samples'] == 16384, 'Toy sample count')
    require(toy['exact_enumeration']['counts']['sum_late'] == 0, 'Toy scope changed')
    require(parsed['source_read_receipt.json']['input_integrity']['all_sha256_match'],
            'Source integrity record failed')

    checked_source_types = 0
    if args.source_packet:
        packet = args.source_packet.resolve()
        for name, record in records.items():
            path = packet / record['source_member']
            require(path.is_file(), f'Missing source file: {path}')
            require(sha256(path) == record['source_sha256'], f'Source hash mismatch: {name}')
            signature = record['source_signature']
            require(signature in path.read_text(), f'Signature not literal source: {name}')
            require(hashlib.sha256(signature.encode()).hexdigest()
                    == record['source_signature_sha256'], f'Signature hash mismatch: {name}')
            checked_source_types += 1

    manifest_status = 'not_present_pre_manifest_check'
    manifest_member_count = 0
    manifest_path = base / 'manifest.json'
    if manifest_path.exists():
        manifest = read_json(manifest_path)
        members = manifest['members']
        names = [m['member'] for m in members]
        require(len(names) == len(set(names)), 'Duplicate manifest member')
        actual = {str(p.relative_to(base)) for p in all_files if p != manifest_path}
        require(actual == set(names), 'Manifest membership mismatch')
        for row in members:
            rel = Path(row['member'])
            require(not rel.is_absolute() and '..' not in rel.parts, 'Unsafe manifest path')
            path = base / rel
            require(path.stat().st_size == row['bytes'], f'Byte count mismatch: {rel}')
            require(sha256(path) == row['sha256'], f'Return hash mismatch: {rel}')
        manifest_status = 'all_member_bytes_and_hashes_match'
        manifest_member_count = len(members)
    print(json.dumps({
        'valid': True,
        'required_files_checked': len(required),
        'json_files_parsed': len(json_files),
        'passages': len(passages),
        'displays': display_count,
        'statement_ids_referenced': len(all_ids),
        'catalog_declarations': len(records),
        'selected_declarations': len(selected),
        'complete_type_occurrences_checked': type_occurrences,
        'bibliography_keys': sorted(bibkeys),
        'internal_file_links_checked': internal_links,
        'new_statements': len(new_statements),
        'source_declarations_hash_and_signature_checked': checked_source_types,
        'manifest_status': manifest_status,
        'manifest_members_checked': manifest_member_count,
        'meaning': 'Structural/integrity verification only; no theorem proving, Lean run, Comparator pass, human review or acceptance.',
    }, indent=2))


if __name__ == '__main__':
    main()
