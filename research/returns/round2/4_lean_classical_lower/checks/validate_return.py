#!/usr/bin/env python3
"""Lexical package-integrity check. This neither parses nor elaborates Lean."""
import argparse
import hashlib
import json
import re
from pathlib import Path

EXPECTED = [
    'claim-product-law', 'def-value-V', 'eq-16', 'claim-supermartingale',
    'claim-final-bound', 'eq-17', 'def-dummy', 'def-planted', 'claim-Y-values',
    'eq-18', 'def-Z', 'claim-uniform-zero', 'claim-EZ', 'def-heavy',
    'def-simulator', 'eq-21', 'eq-22', 'eq-23', 'claim-tail', 'claim-numeric',
    'cor-R-omega', 'claim-exponent-ratio',
]
CLASSES = {'already_stated_under_another_name', 'few_lines_from_existing_declarations',
           'genuine_new_proof', 'prose_not_a_theorem'}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strip_comments(text):
    """Remove nested Lean block comments, line comments, and string literals.

    This is a small lexical filter for forbidden proof placeholders only;
    it deliberately does not claim to parse the language.
    """
    out, i, depth, quoted = [], 0, 0, False
    while i < len(text):
        pair = text[i:i+2]
        if depth:
            if pair == '/-':
                depth += 1
                i += 2
            elif pair == '-/':
                depth -= 1
                i += 2
            else:
                out.append('\n' if text[i] == '\n' else ' ')
                i += 1
        elif quoted:
            if text[i] == '\\':
                i += 2
            elif text[i] == '"':
                quoted = False
                i += 1
            else:
                i += 1
        elif pair == '/-':
            depth = 1
            i += 2
        elif pair == '--':
            end = text.find('\n', i)
            i = len(text) if end < 0 else end
        elif text[i] == '"':
            quoted = True
            i += 1
        else:
            out.append(text[i])
            i += 1
    require(depth == 0 and not quoted, 'Unclosed comment/string in lexical scan')
    return ''.join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--packet', type=Path,
                        help='Root of the original extracted input, with manifest.json')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    data = {}
    for p in sorted(root.rglob('*.json')):
        data[str(p.relative_to(root))] = json.loads(p.read_text())

    coverage = data['coverage_plan.json']
    require([x['id'] for x in coverage] == EXPECTED, 'Coverage order or identifiers')
    require(len({x['id'] for x in coverage}) == len(EXPECTED), 'Duplicate coverage identifiers')
    for row in coverage:
        require({'id', 'class', 'declaration', 'uses', 'difficulty', 'compiled', 'notes'} <= row.keys(),
                f'Missing coverage keys: {row.get("id")}')
        require(row['class'] in CLASSES, f'Invalid classification: {row["id"]}')
        require(row['compiled'] is False, f'Unsupported build claim: {row["id"]}')
        require(row['elaboration_status'] == 'unelaborated', row['id'])
    require(next(x for x in coverage if x['id'] == 'claim-EZ')['formal_relation'] == 'partial',
            'Compound expected-zero row must stay partial')
    require(data['STATEMENT_CHANGES.json'] == [], 'Unexpected canonical statement changes')

    decls, imports = {}, []
    files = sorted((root / 'lean' / 'QuarticQuery' / 'Paper').glob('Classical*.lean'))
    require(len(files) == 4, 'Expected the four requested source modules')
    pattern = r'^(?:noncomputable\s+)?(?:def|theorem|lemma|abbrev)\s+(\w+)'
    for path in files:
        text = path.read_text()
        require('UNELABORATED' in text[:1500], f'Missing status: {path.name}')
        require('namespace QuarticQuery.Paper' in text, f'Missing namespace: {path.name}')
        code = strip_comments(text)
        forbidden = re.findall(r'\b(?:sorry|admit|axiom|native_decide|sorryAx)\b', code)
        require(not forbidden, f'Forbidden proof placeholder in {path.name}: {forbidden}')
        require(not re.search(r'^unsafe\b', code, re.M), f'Unsafe declaration: {path.name}')
        for match in re.finditer(pattern, text, re.M):
            name = 'QuarticQuery.Paper.' + match.group(1)
            require(name not in decls, f'Duplicate new declaration: {name}')
            prefix = text[:match.start()]
            doc = re.search(r'/--\s*Ledger:\s+([\w.-]+)\.[\s\S]*?-/(?:\s*)$',
                            prefix[prefix.rfind('/--'):])
            require(doc is not None, f'Missing immediately preceding Ledger doc: {name}')
            decls[name] = {'file': str(path.relative_to(root)),
                           'line': prefix.count('\n')+1, 'ledger': doc.group(1)}
        for module in re.findall(r'^(?:public\s+)?import\s+([\w.]+)', code, re.M):
            require(module not in ['QuarticQuery.Paper.Section4', 'QuarticQuery.ForrelationLower.Uniform'],
                    f'Import of uncompiled input candidate: {module}')
            imports.append(module)
            rel = Path(*module.split('.')).with_suffix('.lean')
            if not (root/'lean'/rel).exists() and args.packet:
                require((args.packet/'repository'/'lean'/rel).exists(), f'Unknown import: {module}')
    require(set(decls) == set(data['declarations.json']), 'Declaration index mismatch')
    for row in coverage:
        require(row['declaration'] in decls, f'Coverage declaration absent: {row["id"]}')
        for field in ['file', 'line']:
            require(row[field] == decls[row['declaration']][field], f'Stale location: {row["id"]}')

    new = data['NEW_STATEMENTS.json']
    require(len({x['id'] for x in new}) == len(new), 'Duplicate new statement identifiers')
    for row in new:
        require({'id', 'statement', 'why_needed', 'depends_on', 'proposed_lean', 'route_note'} <= row.keys(),
                f'Missing new-statement keys: {row.get("id")}')
        require('theorem ' in row['proposed_lean'], f'Missing proposed signature: {row["id"]}')
        require('sorry' not in row['proposed_lean'], row['id'])
    known = set(EXPECTED) | {x['id'] for x in new}
    if args.packet:
        old = json.loads((args.packet/'repository/corpus/statements.json').read_text())
        known |= {x['id'] for x in old}
        for row in new:
            require(set(row['depends_on']) <= known, f'Unknown dependency: {row["id"]}')

    text = (root/'blueprint.md').read_text()
    require(text.count('<!-- passage:') == len(EXPECTED), 'Unexpected passage count')
    correspondence = data['correspondence.json']
    require(len(correspondence) == len(EXPECTED), 'Unexpected correspondence count')
    linked = []
    for row in correspondence:
        require({'passage', 'from', 'to', 'role', 'statement_ids', 'lean'} <= row.keys(),
                f'Correspondence schema: {row.get("passage")}')
        anchor = re.escape(row['passage'])
        match = re.search(r'<!-- passage:'+anchor+r' -->([\s\S]*?)<!-- /passage:'+anchor+r' -->', text)
        require(match is not None, f'Absent passage: {row["passage"]}')
        body = ' '.join(match.group(1).split())
        require(body.startswith(row['from']), f'Wrong first words: {row["passage"]}')
        require(body.endswith(row['to']), f'Wrong last words: {row["passage"]}')
        require(row['role'] in ['states', 'defines', 'proves', 'explains', 'uses', 'mentions'], row['passage'])
        require(row['statement_ids'][0] in EXPECTED, row['passage'])
        linked.append(row['statement_ids'][0])
        if args.packet:
            require(set(row['statement_ids']) <= known, f'Unknown statement id: {row["passage"]}')
        for declaration in row['lean']:
            if declaration.startswith('QuarticQuery.Paper.'):
                require(declaration in decls, f'Absent new source declaration: {declaration}')
    require(linked == EXPECTED, 'Correspondence order/coverage mismatch')

    original = {'status': 'not_requested', 'members': 0}
    if args.packet:
        manifest = json.loads((args.packet/'manifest.json').read_text())
        for entry in manifest['members']:
            path = args.packet / entry['member']
            require(path.exists(), f'Missing original member: {entry["member"]}')
            require(path.stat().st_size == entry['bytes'], f'Input length changed: {entry["member"]}')
            require(sha(path) == entry['sha256'], f'Input hash changed: {entry["member"]}')
        original = {'status': 'all_matched', 'members': len(manifest['members']),
                    'repository_commit': manifest['repository_commit']}

    output_manifest = {'status': 'not_yet_created'}
    if (root/'return_manifest.json').exists():
        manifest = data['return_manifest.json']
        for entry in manifest['members']:
            path = root / entry['path']
            require(path.exists() and sha(path) == entry['sha256'], f'Return hash mismatch: {entry["path"]}')
        output_manifest = {'status': 'all_matched', 'members': len(manifest['members'])}
    print(json.dumps({
        'status': 'passed', 'scope': 'JSON, source lexemes, file hashes, and exact passage bindings only',
        'lean_elaboration': 'not_run', 'comparator': 'not_run', 'coverage_rows': len(coverage),
        'new_statements': len(new), 'new_lean_files': len(files), 'indexed_declarations': len(decls),
        'imports': sorted(set(imports)), 'forbidden_proof_lexemes': [],
        'all_declarations_have_ledger_docs': True, 'all_new_coverage_compiled_false': True,
        'correspondence_passages': len(correspondence), 'original_manifest': original,
        'return_manifest': output_manifest,
    }, indent=2))


if __name__ == '__main__':
    main()
