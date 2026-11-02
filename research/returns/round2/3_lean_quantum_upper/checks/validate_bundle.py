#!/usr/bin/env python3
"""Static packaging checks only. This script never elaborates Lean."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'def-grover-trial','claim-grover-state','claim-sin2theta','eq-9','def-aij',
    'eq-10','def-T-eps','eq-11','eq-13','claim-weight-lb','construct-sampler',
    'eq-15','claim-success-prob','claim-coupling','claim-tournament-cost',
    'prop-3.2','def-decode','claim-decode-cost','def-comparison',
    'claim-comparison-state','claim-winner-dominates','def-verify','claim-verify',
    'claim-error','claim-coherent-access',
}

def load(name):
    return json.loads((ROOT / name).read_text())

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def uncomment(s):
    """Remove nested block and line comments, preserving line positions."""
    out, depth, i, quoted = [], 0, 0, False
    while i < len(s):
        if depth:
            if s[i:i+2] == '/-':
                depth += 1; out.extend('  '); i += 2
            elif s[i:i+2] == '-/':
                depth -= 1; out.extend('  '); i += 2
            else:
                out.append('\n' if s[i] == '\n' else ' '); i += 1
        elif s[i] == '"':
            quoted = not quoted; out.append(s[i]); i += 1
        elif quoted:
            if s[i] == '\\' and i + 1 < len(s):
                out.extend(s[i:i+2]); i += 2
            else:
                out.append(s[i]); i += 1
        elif s[i:i+2] == '/-':
            depth = 1; out.extend('  '); i += 2
        elif s[i:i+2] == '--':
            j = s.find('\n', i)
            j = len(s) if j < 0 else j
            out.extend(' ' * (j-i)); i = j
        else:
            out.append(s[i]); i += 1
    assert depth == 0, 'Unclosed block comment'
    return ''.join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--packet', type=Path, default=ROOT.parent/'quartic_packet')
    ap.add_argument('--input-zip', type=Path,
        default=ROOT.parent/'upload/quartic_r2_3_lean_quantum_upper.zip')
    args = ap.parse_args()
    failures, checks = [], []

    def check(name, condition, detail=None):
        checks.append({'check':name,'passed':bool(condition),'detail':detail})
        if not condition:
            failures.append(name)

    required = ['README.md','blueprint.md','coverage_plan.json','NEW_STATEMENTS.json',
        'STATEMENT_CHANGES.json','LEAN_GAPS.md','correspondence.json',
        'SOURCE_AUDIT.md','references.json','EVIDENCE_CORRECTIONS.json',
        'source_manifest.json','declaration_manifest.json','READ_SCOPE.json',
        'checks/section3_checks.py','checks/mathematical_checks.json','checks/lean_checks.lean']
    check('required_files', all((ROOT/p).is_file() for p in required), required)
    for p in ROOT.rglob('*.json'):
        json.loads(p.read_text())
    cov, new, corr = load('coverage_plan.json'), load('NEW_STATEMENTS.json'), load('correspondence.json')
    names = [r['id'] for r in cov]
    check('exact_assigned_rows', len(names)==25 and set(names)==EXPECTED)
    check('unique_auxiliary_ids', len({r['id'] for r in new})==len(new))
    fields = {'id','class','declaration','uses','difficulty','compiled','notes'}
    check('coverage_required_fields', all(fields <= r.keys() for r in cov))
    nfields = {'id','statement','why_needed','depends_on','proposed_lean','route_note'}
    check('auxiliary_required_fields', all(nfields <= r.keys() for r in new))
    check('all_new_compiled_false', all(r.get('compiled') is False for r in cov+new))
    check('no_original_statement_changes', load('STATEMENT_CHANGES.json') == [])

    manifest = load('declaration_manifest.json')
    declarations = {r['name']:r for r in manifest}
    check('unique_source_names', len(declarations)==len(manifest))
    check('all_primary_declarations_exist', all(r['declaration'] in declarations for r in cov))
    check('coverage_signatures_match_manifest', all(
        r['lean_statement']==declarations[r['declaration']]['signature'] for r in cov))
    errors = []
    for r in manifest:
        source = (ROOT/r['file']).read_text()
        start = sum(len(line) for line in source.splitlines(keepends=True)[:r['line']-1])
        if not source[start:].startswith(r['signature']):
            errors.append(r['name'])
        if r['signature'].count('(') != r['signature'].count(')'):
            errors.append(r['name']+' (unbalanced parentheses)')
    check('signatures_are_complete_source_prefixes', not errors, errors)

    code_files = sorted((ROOT/'lean').rglob('*.lean'))
    code = {p:uncomment(p.read_text()) for p in code_files}
    admissions = []
    docs_missing = []
    imports_missing = []
    for p,s in code.items():
        for m in re.finditer(r'\b(sorry|admit|axiom|native_decide|unsafe)\b', s):
            admissions.append(str(p.relative_to(ROOT))+':'+m.group())
        check('unelaborated_label:'+p.name, 'UNELABORATED' in p.read_text().upper())
        check('namespace:'+p.name, p.name=='QuantumUpper.lean' or
            'namespace QuarticQuery.Paper' in s)
        original_text = p.read_text()
        for m in re.finditer(r'(?m)^(?:noncomputable )?(theorem|def|abbrev|instance)\s+', s):
            prefix = original_text[:m.start()]
            end = prefix.rfind('-/')
            start = prefix.rfind('/--', 0, end)
            if start < 0 or not prefix[start+3:end].lstrip().startswith('Ledger:'):
                docs_missing.append(str(p.relative_to(ROOT))+':'+str(s[:m.start()].count('\n')+1))
        for mod in re.findall(r'(?m)^(?:public )?import\s+(\S+)', s):
            rel = Path(*mod.split('.')).with_suffix('.lean')
            if not (ROOT/'lean'/rel).is_file() and not (args.packet/'repository/lean'/rel).is_file():
                imports_missing.append(mod)
            check('no_old_section3_import:'+p.name+':'+mod, mod!='QuarticQuery.Paper.Section3')
    check('no_admissions_or_custom_axioms_in_source', not admissions, admissions)
    check('ledger_documentation', not docs_missing, docs_missing)
    if args.packet.exists():
        check('import_paths_present', not imports_missing, imports_missing)

    text = (ROOT/'blueprint.md').read_text()
    anchors = re.findall(r'<!-- passage:([^ ]+) -->', text)
    check('one_mapping_per_anchor', len(anchors)==len(set(anchors))==len(corr)
        and set(anchors)=={r['passage'] for r in corr})
    bad_ranges = []
    allids = EXPECTED | {r['id'] for r in new}
    if (args.packet/'repository/corpus/statements.json').is_file():
        allids |= {r['id'] for r in json.loads((args.packet/'repository/corpus/statements.json').read_text())}
    for r in corr:
        a = '<!-- passage:'+r['passage']+' -->'
        b = '<!-- endpassage:'+r['passage']+' -->'
        body = text.split(a,1)[1].split(b,1)[0].strip()
        if not body.startswith(r['from']) or not body.endswith(r['to']):
            bad_ranges.append(r['passage'])
    check('exact_passage_boundaries', not bad_ranges, bad_ranges)
    id_errors = [(r['passage'],i) for r in corr for i in r['statement_ids'] if i not in allids]
    id_errors += [(r['id'],i) for r in new for i in r['depends_on'] if i not in allids]
    check('statement_ids_resolve', not id_errors, id_errors)
    check('every_assigned_row_has_passage', EXPECTED <=
        {i for r in corr for i in r['statement_ids']})

    sm = load('source_manifest.json')
    bad_hashes = [r['file'] for r in sm['source_files'] if sha(ROOT/r['file'])!=r['sha256']]
    check('source_hashes_match', not bad_hashes, bad_hashes)
    check('mathematical_probe_receipt_passed', load('checks/mathematical_checks.json')['all_passed'])
    check('compiler_status_honest', not sm['new_source_compiled'] and
        not sm['comparator_run'] and not sm['kernel_check_run'])

    original_check = {'performed':False}
    if args.input_zip.is_file() and args.packet.is_dir():
        mismatches, compared = [], 0
        with zipfile.ZipFile(args.input_zip) as z:
            for zi in z.infolist():
                if zi.is_dir():
                    continue
                parts = Path(zi.filename).parts
                try:
                    ix = parts.index('repository')
                except ValueError:
                    continue
                rel = Path(*parts[ix:])
                if len(rel.parts)>1 and rel.parts[1]=='lean' and (args.packet/rel).is_file():
                    compared += 1
                    if hashlib.sha256(z.read(zi)).hexdigest()!=sha(args.packet/rel):
                        mismatches.append(str(rel))
        original_check = {'performed':True,'files_compared':compared,'mismatches':mismatches}
        check('original_lean_sources_unchanged', compared>0 and not mismatches, original_check)

    receipt = {
        'kind':'static_package_validation', 'all_passed':not failures,
        'python':sys.version.split()[0], 'lean_compilation_performed':False,
        'lean_executable':shutil.which('lean'), 'lake_executable':shutil.which('lake'),
        'limitations':'No elaboration, type checking, kernel verification, Comparator '
            'execution, universal proof, or independent review of intended meaning.',
        'coverage_rows':len(cov),'auxiliary_records':len(new),
        'source_declarations':len(manifest),'source_modules':len(code_files),
        'mapped_passages':len(corr), 'checks':checks,
    }
    (ROOT/'checks/static_validation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ['all_passed','coverage_rows','auxiliary_records',
        'source_declarations','source_modules','mapped_passages']},indent=2))
    if failures:
        print('FAILED:', ', '.join(failures), file=sys.stderr)
        raise SystemExit(1)

if __name__ == '__main__':
    main()
