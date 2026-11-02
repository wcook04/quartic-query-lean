#!/usr/bin/env python3
"""Static delivery checks only. This program does not invoke or emulate Lean."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TARGETS = '''def-log-convention def-partial-query def-query-oracle eq-1 eq-2 def-transcript def-walsh-sign eq-3 eq-4 eq-5 claim-bs-to-L claim-proj-prob lem-2.1.ii claim-N-phi claim-integer-tests claim-circuit-size lem-2.1 eq-6 def-column-layout eq-7 eq-8 def-winner cor-unique-winner def-win-at-address def-K lem-2.2.i lem-2.2.ii lem-2.2 cor-local-dichotomy'''.split()


def uncomment(source):
    result = []
    depth = 0
    i = 0
    while i < len(source):
        if source.startswith('/-', i):
            depth += 1
            i += 2
        elif depth and source.startswith('-/', i):
            depth -= 1
            i += 2
        elif depth:
            if source[i] == '\n':
                result.append('\n')
            i += 1
        elif source.startswith('--', i):
            j = source.find('\n', i)
            i = len(source) if j < 0 else j
        else:
            result.append(source[i])
            i += 1
    if depth:
        raise ValueError('unclosed block comment')
    return ''.join(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', type=Path, help='original extracted packet root')
    parser.add_argument('--report', type=Path, help='write this static report as JSON')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    errors = []
    checks = []
    def check(condition, description):
        (checks if condition else errors).append(description)
    required = ['README.md','blueprint.md','coverage_plan.json','NEW_STATEMENTS.json',
        'STATEMENT_CHANGES.json','LEAN_GAPS.md','correspondence.json','REFERENCES.md',
        'references.bib','REVIEW_NOTES.md','SOURCE_RECEIPT.json']
    for file in required:
        check((root/file).is_file(), 'Required file: ' + file)
    def read(file):
        return json.loads((root/file).read_text())
    coverage = read('coverage_plan.json')
    check(len(coverage)==29 and {x['id'] for x in coverage}==set(TARGETS),
          'Exactly the 29 requested target records, without duplicates')
    for row in coverage:
        check({'id','class','declaration','uses','difficulty','compiled','notes'} <= row.keys(),
              row['id'] + ': required coverage fields')
        check(row['compiled'] is False, row['id'] + ': compiled remains false')
        check(row['difficulty'] in {'trivial','short','substantial'}, row['id'] + ': difficulty')
        check(row['class'] in {'definition','short_from_existing','genuine_new_proof','prose'},
              row['id'] + ': classification')
    new = read('NEW_STATEMENTS.json')
    check(len({x['id'] for x in new})==len(new),'Unique supplemental statement IDs')
    for row in new:
        check({'id','statement','why_needed','depends_on','proposed_lean','route_note'} <= row.keys(),
              row['id'] + ': required new-statement fields')
        check(bool(row['proposed_lean']) and not row['proposed_lean'].rstrip().endswith('let _'),
              row['id'] + ': nontruncated signature')
        check(row.get('compiled') is False, row['id'] + ': compiled remains false')
    for row in read('STATEMENT_CHANGES.json'):
        check({'id','old','new','relation','reason'} <= row.keys(),'Statement-change fields')
        check(row['relation'] in {'stronger','weaker','equivalent','corrected'},'Statement-change relation')
    files = sorted((root/'lean/QuarticQuery/Paper').glob('Construction*.lean'))
    decl_pattern = re.compile(r'(?m)^(?:@\[[^\n]*\]\s*)?(?:(?:noncomputable|private)\s+)?(?:theorem|lemma|def|abbrev)\s+([\w\u0080-\uffff]+)\b')
    names = {}
    imports = []
    for file in files:
        source = file.read_text()
        code = uncomment(source)
        check('unelaborated' in source[:1300].lower(),file.name + ': unelaborated header')
        check(not re.search(r'\b(sorry|admit|axiom|native_decide)\b',code),file.name + ': no proof placeholder or custom axiom')
        for match in decl_pattern.finditer(source):
            name = 'QuarticQuery.Paper.' + match.group(1)
            check(name not in names, 'Unique declaration: ' + name)
            names[name] = file.relative_to(root).as_posix()
            before = source[:match.start()].rstrip()
            last = before.rfind('/--')
            doc = before[last:] if last>=0 else ''
            check(doc.startswith('/-- Ledger: ') and doc.endswith('-/'),name + ': Ledger doc comment')
        if decl_pattern.search(source):
            check('namespace QuarticQuery.Paper' in source,file.name + ': required namespace')
        imports += re.findall(r'(?m)^(?:public\s+)?import\s+([A-Za-z0-9_.]+)',code)
    check(bool(files),'Lean modules present')
    index = read('source_records/declaration_index.json')
    check(set(names)==set(index),'Source declaration names equal metadata declaration index')
    for row in coverage:
        for name in [row['declaration']] + row.get('additional_declarations',[]):
            check(name in names, row['id'] + ': declared evidence ' + name)
    for row in new:
        if row.get('declaration'):
            check(row['declaration'] in names,row['id'] + ': declared primary evidence')
    local_modules = {p.relative_to(root/'lean').with_suffix('').as_posix().replace('/','.') for p in files}
    unresolved = []
    for module in sorted(set(imports)):
        check(module not in {'QuarticQuery.Paper.Section2','QuarticQuery.ForrelationLower.Uniform'},
              'Avoid uncompiled candidate import: ' + module)
        path = Path(*module.split('.')).with_suffix('.lean')
        if module in local_modules:
            continue
        if args.base:
            check((args.base/'repository/lean'/path).is_file(), 'Resolve base import: ' + module)
        else:
            unresolved.append(module)
    mapping = read('correspondence.json')
    check(len({(r.get('document','blueprint.md'),r['passage']) for r in mapping})==len(mapping),
          'Unique correspondence passages')
    known_ids = set(TARGETS) | {r['id'] for r in new}
    for row in mapping:
        check({'passage','from','to','role','statement_ids','lean'} <= row.keys(),
              row['passage'] + ': correspondence fields')
        document = root/row.get('document','blueprint.md')
        text = document.read_text()
        begin = '<!-- passage:' + row['passage'] + ' -->'
        end = '<!-- /passage:' + row['passage'] + ' -->'
        check(text.count(begin)==1 and text.count(end)==1,row['passage'] + ': exact anchors')
        if begin in text and end in text:
            passage = text.split(begin,1)[1].split(end,1)[0].strip()
            normalized = ' '.join(passage.split())
            check(normalized.startswith(row['from']),row['passage'] + ': exact starting words')
            check(normalized.endswith(row['to']),row['passage'] + ': exact ending words')
        check(set(row['statement_ids']) <= known_ids,row['passage'] + ': known statement IDs')
        check(set(row['lean']) <= set(names),row['passage'] + ': known declaration names')
        check(row['role'] in {'states','defines','proves','explains','uses','mentions'},row['passage'] + ': role')
    check(all(any(r['passage']=='row-'+rid.replace('.','-') for r in mapping) for rid in TARGETS),
          'Every target has an anchored blueprint passage')
    report = {'schema':'quartic-static-return-validation.v1','status':'passed' if not errors else 'failed',
        'validation_kind':'static files, schema, source markers and import locations only',
        'lean_compiled':False,'kernel_check_run':False,'axiom_audit_run':False,'comparator_run':False,
        'target_records':len(coverage),'supplemental_records':len(new),'lean_modules':len(files),
        'source_declarations':len(names),'correspondence_passages':len(mapping),
        'checks_passed':len(checks),'errors':errors,'base_imports_resolved':bool(args.base),
        'unresolved_external_imports':unresolved,
        'limits':['No Lean parser, elaborator or kernel was run.',
                  'API correctness and mathematical truth are not established by this checker.',
                  'No original source or evidence record is modified.']}
    if args.report:
        args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
