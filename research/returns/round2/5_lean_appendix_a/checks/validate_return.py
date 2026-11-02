#!/usr/bin/env python3
"""Static return integrity checks. This is not a Lean compiler or Comparator.

Optional source roots let this checker resolve direct imports and compare the
unchanged input archive's manifest. No network access is performed.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil


HERE = Path(__file__).resolve().parents[1]
EXPECTED = [
    'def-deg', 'def-bs', 'def-Gamma-i', 'claim-perron', 'def-adv-progress',
    'claim-per-query', 'claim-final-overlap', 'lem-A.2', 'def-Sf',
    'lem-A.3.bs', 'lem-A.3.lambda', 'lem-A.3', 'claim-restrict-parity',
    'def-huang', 'claim-huang-spectrum', 'claim-interlace', 'lem-A.4',
    'claim-round-block', 'lem-A.5',
]
REQUIRED = [
    'blueprint.md', 'coverage_plan.json', 'NEW_STATEMENTS.json',
    'STATEMENT_CHANGES.json', 'correspondence.json', 'LEAN_GAPS.md',
    'references.bib', 'README.md', 'READING_LOG.md', 'ATTRIBUTION.md',
    'LICENSE', 'source_manifest.json', 'declaration_index.json',
    'assembly_plan.json', 'SOURCE_CORRECTIONS.json', 'SOURCE_COEFFICIENT_CHECK.md',
]
DECL = re.compile(r'(?m)^(?:(?:noncomputable|private|protected|unsafe)\s+)*'
                  r'(theorem|lemma|def|abbrev|instance|structure)\s+([^\s(:]+)')


def without_comments(s):
    """Remove nested Lean comments and strings while preserving newlines."""
    out = []
    i = 0
    depth = 0
    line = False
    string = False
    while i < len(s):
        if line:
            if s[i] == '\n':
                line = False
                out.append('\n')
            else:
                out.append(' ')
            i += 1
        elif depth:
            if s[i:i+2] == '/-':
                depth += 1
                out.extend('  ')
                i += 2
            elif s[i:i+2] == '-/':
                depth -= 1
                out.extend('  ')
                i += 2
            else:
                out.append('\n' if s[i] == '\n' else ' ')
                i += 1
        elif string:
            if s[i] == '\\' and i + 1 < len(s):
                out.extend('  ')
                i += 2
            elif s[i] == '"':
                string = False
                out.append(' ')
                i += 1
            else:
                out.append('\n' if s[i] == '\n' else ' ')
                i += 1
        elif s[i:i+2] == '--':
            line = True
            out.extend('  ')
            i += 2
        elif s[i:i+2] == '/-':
            depth = 1
            out.extend('  ')
            i += 2
        elif s[i] == '"':
            string = True
            out.append(' ')
            i += 1
        else:
            out.append(s[i])
            i += 1
    assert depth == 0 and not string, 'Unclosed source comment or string'
    return ''.join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--packet', type=Path)
    parser.add_argument('--complexitylib', type=Path)
    parser.add_argument('--cslib', type=Path)
    parser.add_argument('--mathlib', type=Path)
    args = parser.parse_args()
    tests = []
    errors = []

    def check(name, cond, detail=None):
        tests.append({'check': name, 'passed': bool(cond), 'detail': detail})
        if not cond:
            errors.append(name)

    check('required_files', all((HERE / p).is_file() for p in REQUIRED))
    parsed = {}
    for p in HERE.rglob('*.json'):
        if p.name in ('validation.json', 'return_manifest.json'):
            continue
        try:
            parsed[str(p.relative_to(HERE))] = json.loads(p.read_text())
        except Exception as e:
            check('parse_' + str(p.relative_to(HERE)), False, str(e))
    check('all_json_parse', not errors, {'json_files': len(parsed)})
    cov = parsed['coverage_plan.json']
    check('exact_requested_row_order', [x['id'] for x in cov] == EXPECTED)
    fields = {'id','class','declaration','library_declaration','uses','difficulty','compiled','notes'}
    check('coverage_keys', all(fields <= x.keys() for x in cov))
    check('no_new_build_claims', all(x['compiled'] is False for x in cov))
    check('documented_classes', all(x['class'] in {'exact','stronger','partial','weaker','none'} for x in cov))
    new = parsed['NEW_STATEMENTS.json']
    check('new_statement_keys', all({'id','statement','why_needed','depends_on','proposed_lean','route_note'} <= x.keys() for x in new))
    changes = parsed['STATEMENT_CHANGES.json']
    check('statement_change_keys', all({'id','old','new','relation','reason'} <= x.keys() for x in changes))
    check('statement_change_relations', all(x['relation'] in {'stronger','weaker','equivalent','corrected'} for x in changes))
    ids = [x['id'] for x in new]
    check('new_statement_ids_unique', len(ids) == len(set(ids)))

    declarations = {}
    local_imports = {}
    missing_docs = []
    placeholders = []
    forbidden = []
    sources = {}
    for p in sorted((HERE / 'lean').rglob('*.lean')):
        s = p.read_text()
        code = without_comments(s)
        module = '.'.join(p.relative_to(HERE / 'lean').with_suffix('').parts)
        sources[module] = p
        check('status_' + p.name, bool(re.search(r'unelaborated', s, flags=re.I)))
        check('namespace_' + p.name, 'namespace QuarticQuery.Paper' in code)
        local_imports[module] = re.findall(r'(?m)^(?:public )?import\s+(\S+)', code)
        if '@@' in s:
            placeholders.append(str(p.relative_to(HERE)))
        forbidden.extend((p.name, m.group(0)) for m in re.finditer(r'\b(sorry|admit|axiom|native_decide)\b', code))
        for m in DECL.finditer(code):
            name = 'QuarticQuery.Paper.' + m.group(2)
            declarations[name] = str(p.relative_to(HERE))
            begin = s.rfind('/--', 0, m.start())
            end = s.find('-/', begin)
            doc = s[begin:end+2] if begin >= 0 and end < m.start() else ''
            lead = re.match(r'/--\s+Ledger:\s+(\S+)', doc)
            if not lead or lead.group(1).rstrip('.') not in set(EXPECTED + ['thm-A.1']):
                missing_docs.append(name)
    check('no_proof_placeholders_or_custom_axioms', not forbidden, forbidden)
    check('all_declarations_have_ledger_doc', not missing_docs, missing_docs)
    check('no_unfilled_templates', not placeholders and '@@' not in (HERE/'blueprint.md').read_text(), placeholders)
    check('coverage_declarations_exist', all(x['declaration'] in declarations for x in cov))
    index = parsed['declaration_index.json']
    check('source_index_names_match', set(x['name'] for x in index) == set(declarations), {'declarations': len(declarations)})

    # Detect a source import cycle among returned modules. External imports are not elaborated.
    state = {}
    cycles = []
    def visit(m, stack):
        if state.get(m) == 1:
            cycles.append(stack + [m])
            return
        if state.get(m) == 2:
            return
        state[m] = 1
        for imp in local_imports[m]:
            if imp in local_imports:
                visit(imp, stack + [m])
        state[m] = 2
    for m in local_imports:
        visit(m, [])
    check('returned_import_graph_acyclic', not cycles, cycles)
    roots = [HERE/'lean']
    if args.packet:
        roots.append(args.packet/'repository/lean')
    roots.extend(p for p in (args.complexitylib,args.cslib,args.mathlib) if p)
    if args.packet and args.complexitylib and args.cslib and args.mathlib:
        unresolved=[]
        for imports in local_imports.values():
            for imp in imports:
                rel=Path(*imp.split('.')).with_suffix('.lean')
                if not any((r/rel).is_file() for r in roots):
                    unresolved.append(imp)
        check('direct_import_paths_exist_at_supplied_roots', not unresolved, sorted(set(unresolved)))
    else:
        tests.append({'check':'direct_import_paths_exist_at_supplied_roots','passed':None,'detail':'Optional source roots not supplied; not checked.'})

    assembly = without_comments((HERE/'lean/QuarticQuery/Paper/AppendixA.lean').read_text())
    route = without_comments((HERE/'lean/QuarticQuery/Paper/AppendixAHuangRoute.lean').read_text())
    check('assembly_invokes_literal_A4', 'appendixA4_paper_route f' in assembly)
    check('no_direct_old_quartic_endpoint_call', not re.search(r'\b(complexity_le_mul_pow_four|D_le_Q_pow_four)\b', assembly))
    check('literal_A4_no_direct_old_spectral_endpoint_call', not re.search(r'\b(degree_le_spectralSensitivity_sq|appendixA4)\b', route))

    corr = parsed['correspondence.json']
    anchor_map = {}
    for document in sorted(set(x.get('document','blueprint.md') for x in corr)):
        text=(HERE/document).read_text()
        aa=list(re.finditer(r'<!-- passage:([^>]+) -->',text))
        for k,a in enumerate(aa):
            anchor_map[(document,a.group(1))]=text[a.end():aa[k+1].start() if k+1<len(aa) else len(text)].strip()
    bad_corr=[]
    for x in corr:
        key=(x.get('document','blueprint.md'),x['passage'])
        p=anchor_map.get(key)
        if p is None or not p.startswith(x['from']) or not p.endswith(x['to']):
            bad_corr.append(key)
        if x['role'] not in {'states','defines','proves','explains','uses','mentions'}:
            bad_corr.append(('bad_role',x['passage']))
        for name in x['lean']:
            if name.startswith('QuarticQuery.Paper.') and name not in declarations:
                bad_corr.append(('missing_declaration',name))
    check('exact_passage_correspondence', not bad_corr, bad_corr)
    known_ids=set(EXPECTED+['thm-A.1','def-Q','def-R','def-D','def-query-oracle'])|set(ids)
    if args.packet:
        known_ids|={x['id'] for x in json.loads((args.packet/'repository/corpus/statements.json').read_text())}
    missing_ids=sorted({z for x in corr for z in x['statement_ids'] if z not in known_ids})
    check('correspondence_statement_ids_resolve', not missing_ids, missing_ids)

    if args.packet:
        manifest=json.loads((args.packet/'manifest.json').read_text())
        bad=[]
        for item in manifest['members']:
            p=args.packet/item['member']
            if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:
                bad.append(item['member'])
        check('original_input_hashes_unchanged',not bad,{'members':len(manifest['members']),'mismatches':bad})

    result = {
        'kind':'static_integrity_check',
        'lean_compiled':False,
        'comparator_run':False,
        'external_kernel_run':False,
        'compiled_dependency_closure_extracted':False,
        'compiler_on_path':{x:shutil.which(x) for x in ['lean','lake','elan']},
        'source_modules':len(sources),
        'source_declarations':len(declarations),
        'tests':tests,
        'passed':not errors,
        'errors':errors,
        'scope':'Source and metadata integrity only. Passing does not typecheck or prove the Lean declarations.',
    }
    (HERE/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'passed':not errors,'checks':len(tests),'errors':errors,
                      'lean_compiled':False,'output':'validation.json'}))
    raise SystemExit(0 if not errors else 1)


if __name__ == '__main__':
    main()
