#!/usr/bin/env python3
"""Build three round-ten improvement reviews with complete round-nine custody.

Reuse the frozen batch writer, native render checks, literature and register
stage. Original returns remain byte-identical; relocated maintained guides have
rebased links. Require the merged writing-method edition explicitly.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import posixpath
import re
import subprocess
import sys
import tempfile
import tarfile
import zipfile
from urllib.parse import quote, unquote, urlsplit, urlunsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_round9_packets as round9

round8, round7, round6, base = round9.round8, round9.round7, round9.round6, round9.base
ROOT = base.ROOT
REQUESTS = ROOT / 'research/requests/round10'
JOBS = dict(round9.JOBS)
PREFIX = {'expert_paper': 'XP10', 'exposition': 'EX10', 'reasoning_record': 'RR10'}
LEADS, CITED_ONLY = round9.LEADS, round9.CITED_ONLY
LITERATURE = {job: list(dict.fromkeys(round6.QUARTIC_LITERATURE)) for job in JOBS}
METHOD_COMMIT = '7bc9ef5d253d23527c6ccbd759c2eb24c0243ac7'
# R8 evidence and older verdicts remain historical, never active instructions.
PREVIOUS = {name.replace('previous_round/', 'earlier_round8/', 1): path
            for name, path in round9.PREVIOUS.items()}
state = {'work': None, 'supplementary_literature': None, 'complexitylib': None}
render_provenance = round9.render_provenance
add_local_writing_method = round9.add_local_writing_method
original_reader_leak_check = base.check_reader_leaks


def mask_bibliography_authors(text):
    """Mask braced BibTeX author values only in a temporary privacy-scan copy."""
    spans = []
    for match in re.finditer(r'(?im)^\s*author\s*=\s*\{', text):
        start, depth, cursor = match.end(), 1, match.end()
        while cursor < len(text) and depth:
            if text[cursor] == '{' and (cursor == 0 or text[cursor - 1] != '\\'):
                depth += 1
            elif text[cursor] == '}' and (cursor == 0 or text[cursor - 1] != '\\'):
                depth -= 1
            cursor += 1
        if depth == 0:
            spans.append((start, cursor - 1))
    for start, end in reversed(spans):
        text = text[:start] + re.sub(r'[^\n]', ' ', text[start:end]) + text[end:]
    return text


def check_reader_leaks(data, request):
    """Distinguish public cited authors from private readers, within verified sources."""
    scan = dict(data)
    provenance = json.loads(data.get('METHOD_PROVENANCE.json', b'{}'))
    if provenance.get('commit') == METHOD_COMMIT:
        for row in provenance.get('sources', []):
            member = row['member']
            if not member.endswith('.bib') or row.get('role') != 'pinned_writing_method_source':
                continue
            blob = data.get(member)
            if blob is None or base.digest(blob) != row.get('source_sha256') or base.digest(blob) != row.get('packaged_sha256'):
                raise ValueError(f'public bibliography privacy-scan binding mismatch: {member}')
            text = blob.decode('utf-8')
            # Generic private-context markers remain forbidden even inside author fields.
            if '/.codex/' in text or any(re.search(pattern, text, re.I) for pattern in base.GENERIC_LEAKS):
                original_reader_leak_check({member: blob}, request)
            scan[member] = mask_bibliography_authors(text).encode('utf-8')
    original_reader_leak_check(scan, request)


def verified_round9(root):
    """Read the custody inventory, requiring every original ZIP and member."""
    custody = root / 'research/returns/round9'
    inventory = json.loads((custody / 'intake.json').read_bytes())
    files = {'previous_round/intake.json': (base.safe_source(custody / 'intake.json'),
             'original_return_inventory', 'repository:research/returns/round9/intake.json')}
    seen = set()
    for submission in inventory['returns']:
        for relative, row in [(submission['archive']['preserved'], submission['archive']),
                              *[(submission['members_root'] + '/' + member['path'], member)
                                for member in submission['members']]]:
            base.check_packets.check_name(relative)
            if relative in seen:
                raise ValueError(f'duplicate round-nine custody path: {relative}')
            seen.add(relative)
            source = base.safe_source(custody / relative)
            if not source.resolve().is_relative_to(custody.resolve()):
                raise ValueError(f'round-nine custody path escapes inventory: {relative}')
            blob = source.read_bytes()
            if len(blob) != row['bytes'] or base.digest(blob) != row['sha256']:
                raise ValueError(f'round-nine custody hash or length mismatch: {relative}')
            label = 'repository:research/returns/round9/' + relative
            files['previous_round/' + relative] = (source, 'original_round9_return', label)
            if relative.startswith('members/'):
                files['previous_round/returns/' + relative.removeprefix('members/')] = (
                    source, 'original_round9_return_compatibility_alias', label)
    if {row['id'] for row in inventory['returns']} != set(JOBS) or len(inventory['returns']) != len(JOBS):
        raise ValueError('round-nine custody requires exactly the three lead-paper returns')
    return files


def rebase_markdown(text, source, root, member, files, prefix='repository/'):
    """Rebase maintained aliases to original repository paths, keeping fragments."""
    replacements = []
    references = re.compile(r'(?m)^ {0,3}\[(?!\^)[^\]\n]+\]:\s*(<[^>\n]+>|\S+)')
    for pattern in (base.repository_checks.LINK, references):
        for match in pattern.finditer(text):
            raw = match.group(1)
            target = urlsplit(raw.strip('<>'))
            if target.scheme or target.netloc or not target.path:
                continue
            path = (source.parent / unquote(target.path)).resolve()
            destination = prefix + path.relative_to(root.resolve()).as_posix()
            if destination not in files and not any(n.startswith(destination.rstrip('/') + '/') for n in files):
                raise ValueError(f'relocated decision link not packaged: {source}: {raw}')
            relative = quote(posixpath.relpath(destination, posixpath.dirname(member)), safe='/')
            value = urlunsplit(('', '', relative, target.query, target.fragment))
            replacements.append((match.start(1), match.end(1), '<' + value + '>' if raw.startswith('<') else value))
    for start, end, value in sorted(replacements, reverse=True):
        text = text[:start] + value + text[end:]
    return text


def add_round9_decisions(files, root, generated):
    owner = root / 'research/adjudication'
    paths = sorted({path for entry in owner.glob('round9*')
                    for path in ([entry] if entry.is_file() else entry.rglob('*')) if path.is_file()})
    required = {'round9_synthesis.json', 'round9_revision.md', 'round9_validation.json'}
    if not required <= {p.name for p in paths}:
        raise ValueError('missing round-nine synthesis, revision or validation')
    selected = {'repository/' + p.relative_to(root).as_posix(): (p, 'round9_adjudication_original') for p in paths}
    closure, _ = base.round4.linked_sources(root, selected)
    for name, (path, role) in closure.items():
        files.setdefault(name, (base.safe_source(path), role, 'repository:' + name.removeprefix('repository/')))
    for path in paths:
        member = 'previous_round/adjudication/' + path.relative_to(owner).as_posix()
        label = 'repository:' + path.relative_to(root).as_posix()
        if path.suffix == '.md':
            relocated = generated / member
            relocated.parent.mkdir(parents=True, exist_ok=True)
            relocated.write_text(rebase_markdown(path.read_text(), path, root, member, files), encoding='utf-8')
            files[member] = (relocated, 'relocated_round9_adjudication', 'generated:' + label)
        else:
            files[member] = (base.safe_source(path), 'round9_adjudication', label)


def add_writing_method(files, method, generated):
    """Supply the selected merged method and its native relative-link closure."""
    revision = base.git(method, 'rev-parse', 'HEAD').stdout.decode().strip()
    if revision != METHOD_COMMIT:
        raise ValueError(f'writing method must be merged revision {METHOD_COMMIT}, got {revision}')
    seeds = {'repository/skills/README.md': (method / 'skills/README.md', 'writing_method'),
             'repository/docs/register-stage.md': (method / 'docs/register-stage.md', 'writing_method')}
    closure, report = base.round4.linked_sources(method, seeds)
    tree = base.git(method, 'ls-tree', '-rz', revision).stdout
    objects = {}
    for row in tree.split(b'\0'):
        if row:
            metadata, path = row.split(b'\t', 1)
            objects[path.decode()] = metadata.split()[2].decode()
    records = []
    for name, (path, _) in sorted(closure.items()):
        member = name.removeprefix('repository/')
        source = base.safe_source(path)
        blob = source.read_bytes()
        git_hash = hashlib.sha1(b'blob ' + str(len(blob)).encode() + b'\0' + blob).hexdigest()
        if objects.get(member) != git_hash:
            raise ValueError(f'writing-method source differs from merged revision: {member}')
        records.append({'member': member, 'source_sha256': base.digest(blob), 'git_blob': git_hash})
        # Keep the established privacy-preserving register export at its native path.
        if member == 'src/lean_exposition/resources/register/rules.json':
            source = Path(round7.state['register']) / 'register_rules.json'
            role, label = 'sanitized_register_rules', 'generated:register/register_rules.json'
        else:
            role, label = 'pinned_writing_method_source', 'lean-exposition:' + revision + ':' + member
        if member in files and not files[member][2].startswith(('lean-exposition:', 'generated:register/')):
            raise ValueError(f'writing-method member conflicts with another source: {member}')
        files[member] = (source, role, label)
        records[-1]['packaged_sha256'] = base.digest(source.read_bytes())
        records[-1]['role'] = role
        if member.endswith('.bib'):
            records[-1]['privacy_scan'] = ('Exact public method bibliography author fields are treated as '
                'citation attribution only in a scan copy; original bytes, other fields and generic private-context checks remain intact.')
    guide = method / 'docs/register-stage.md'
    alias = generated / 'register-stage.md'
    alias.write_text(rebase_markdown(guide.read_text(), guide, method,
                                    'skills/register-stage.md', files, prefix=''), encoding='utf-8')
    files['skills/register-stage.md'] = (alias, 'relocated_writing_method',
        'generated:lean-exposition:' + revision + ':docs/register-stage.md')
    receipt = generated / 'METHOD_PROVENANCE.json'
    receipt.write_bytes(base.encoded({'schema': 'quartic-round10-method-provenance-v1',
        'repository': 'https://github.com/wcook04/lean-exposition', 'commit': revision,
        'sources': records, 'relative_link_count': len(report['links']),
        'boundary': 'Selected bytes match this Git revision. Register private evidence is sanitized; '
                    'source and packaged hashes distinguish it. Method availability is not evidence of paper quality.'}))
    files[receipt.name] = (receipt, 'writing_method_provenance', 'generated:pinned-writing-method')


def add_supplementary_literature(files, manifest):
    """Import source-bound additions without mutating the existing annex owner."""
    if manifest is None:
        raise ValueError('round ten requires the supplementary literature manifest')
    manifest = base.safe_source(Path(manifest))
    spec = json.loads(manifest.read_bytes())
    if spec.get('schema') != 'quartic-round10-supplementary-literature-v1' or not spec.get('sources'):
        raise ValueError('invalid supplementary literature manifest')
    ids = set()
    for row in spec['sources']:
        if not row.get('id') or row['id'] in ids:
            raise ValueError('supplementary literature IDs must be distinct')
        ids.add(row['id'])
        if row.get('role') not in {'query-literature', 'writing-literature'}:
            raise ValueError('unknown supplementary literature role')
        for key in ('title', 'source_url', 'edition', 'edition_relation'):
            if not row.get(key):
                raise ValueError(f'supplementary literature needs {key}: {row["id"]}')
        prefix = 'literature/' if row['role'] == 'query-literature' else 'writing_literature/'
        supplied = []
        for item in row['files']:
            member, relative = item['member'], item['path']
            base.check_packets.check_name(member)
            base.check_packets.check_name(relative)
            if not member.startswith(prefix) or member.casefold() in {n.casefold() for n in files}:
                raise ValueError(f'supplementary literature member collides or has wrong role: {member}')
            source = base.safe_source(manifest.parent / relative)
            if not source.resolve().is_relative_to(manifest.parent.resolve()):
                raise ValueError(f'supplementary source escapes manifest directory: {relative}')
            blob = source.read_bytes()
            if len(blob) != item['bytes'] or base.digest(blob) != item['sha256']:
                raise ValueError(f'supplementary literature hash or length mismatch: {relative}')
            files[member] = (source, row['role'], 'supplementary:' + row['id'] + ':' + relative)
            supplied.append(member)
        if not any(Path(n).name.startswith('extracted') and n.endswith(('.md', '.txt')) for n in supplied) or not any(
                n.endswith(('.pdf', '.tex', '.tar.gz', '.tgz')) for n in supplied):
            raise ValueError(f'supplementary source needs original PDF/TeX and extracted.md: {row["id"]}')
    files['SUPPLEMENTARY_LITERATURE.json'] = (manifest, 'supplementary_literature_inventory',
                                            'external:supplementary-literature-manifest')


def add_complexitylib(files, root, generated, checkout=None):
    """Export the bibliography's exact Lake-pinned source, never working bytes."""
    manifest = json.loads((root / 'lean/lake-manifest.json').read_bytes())
    dependency = next(row for row in manifest['packages'] if row['name'] == 'complexitylib')
    commit = dependency['rev']
    checkout = Path(checkout or root / 'lean/.lake/packages/complexitylib')
    tree = base.git(checkout, 'rev-parse', commit + '^{tree}').stdout.decode().strip()
    archive = base.git(checkout, 'archive', '--format=tar', commit).stdout
    rows = []
    occupied = {name.casefold() for name in files}
    with tarfile.open(fileobj=io.BytesIO(archive)) as exported:
        entries = {item.name: item for item in exported}
        for item in entries.values():
            if item.isdir():
                continue
            base.check_packets.check_name(item.name)
            resolved, visited = item, set()
            while resolved.issym() or resolved.islnk():
                if resolved.name in visited:
                    raise ValueError(f'cyclic Complexitylib source link: {item.name}')
                visited.add(resolved.name)
                target = posixpath.normpath(posixpath.join(
                    posixpath.dirname(resolved.name) if resolved.issym() else '', resolved.linkname))
                base.check_packets.check_name(target)
                if target not in entries:
                    raise ValueError(f'missing Complexitylib source link target: {target}')
                resolved = entries[target]
            if not resolved.isfile():
                raise ValueError(f'nonregular Complexitylib source: {item.name}')
            member = 'repository/dependency_sources/complexitylib/' + item.name
            if member.casefold() in occupied:
                raise ValueError(f'Complexitylib source collision: {member}')
            occupied.add(member.casefold())
            blob = exported.extractfile(resolved).read()
            destination = generated / member
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(blob)
            files[member] = (destination, 'pinned_cited_dependency_source',
                             'complexitylib:' + commit + ':' + item.name)
            original = item.linkname.encode() if item.issym() or item.islnk() else blob
            git_blob = hashlib.sha1(b'blob ' + str(len(original)).encode() + b'\0' + original).hexdigest()
            rows.append({'member': member, 'bytes': len(blob), 'sha256': base.digest(blob),
                         'git_mode': '120000' if item.issym() else ('100755' if item.mode & 0o111 else '100644'),
                         'git_blob_sha1': git_blob})
            if item.issym() or item.islnk():
                rows[-1].update(git_link_target=item.linkname, materialized_from=resolved.name,
                                materialized_target_sha256=base.digest(blob),
                                interpretation='Safe in-tree Git link materialized as regular bytes in ZIP.')
    expected = set(base.git(checkout, 'ls-tree', '-rz', '--name-only', commit).stdout.decode().strip('\0').split('\0'))
    actual = {row['member'].removeprefix('repository/dependency_sources/complexitylib/') for row in rows}
    if actual != expected:
        raise ValueError('Complexitylib Git export omitted tracked sources')
    receipt = generated / 'CODE_SOURCE_PROVENANCE.json'
    receipt.write_bytes(base.encoded({'schema': 'quartic-round10-code-source-v1',
        'citation_key': 'ComplexitylibPinned', 'repository': dependency['url'], 'commit': commit,
        'git_tree': tree, 'export_sha256': base.digest(base.encoded(rows)), 'sources': rows,
        'boundary': 'Full tracked source at the cited Lake pin; safe in-tree links are explicitly materialized. No dependency checkout changes, '
                    'build products, script execution, Lean run or new mathematical evidence.'}))
    files[receipt.name] = (receipt, 'cited_code_source_provenance', 'generated:pinned-complexitylib-source')


def add_citation_coverage(files, root, requests, annexes, paper_annex, generated):
    """Bind the reviewed citation map to the exact full sources actually shipped."""
    source = requests / 'citation_coverage.json'
    coverage = json.loads(source.read_bytes())
    if coverage.get('schema') != 'quartic-round10-citation-coverage-v1':
        raise ValueError('invalid citation coverage map')
    for relative, row in coverage['bibliographies'].items():
        paper = Path(relative).stem
        text = (root / relative).read_text()
        actual_keys = re.findall(r'@\w+\s*\{\s*([^,\s]+)\s*,', text)
        mapped = [r['citation_key'] for r in coverage['citations'] if r['paper'] == paper]
        if len(mapped) != len(set(mapped)) or set(mapped) != set(actual_keys) or len(mapped) != row['entry_count']:
            raise ValueError(f'citation map keys disagree with bibliography: {relative}')
        base.check_packets.check_name(relative)
        if base.digest((root / relative).read_bytes()) != row['sha256']:
            raise ValueError(f'citation map is stale for bibliography: {relative}')
    if base.digest((root / 'docs/reasoning_record.md').read_bytes()) != coverage['record_sha256']:
        raise ValueError('citation map is stale for record Appendix C')
    expected_slugs = set(LITERATURE['expert_paper']) | {'openai-math-284-quartic-query-separation'}
    if {row['slug'] for row in coverage['annex_sources']} != expected_slugs:
        raise ValueError('citation map must cover the complete literature selection and preprint')
    for annex in coverage['annex_sources']:
        slug = annex['slug']
        preprint = slug == 'openai-math-284-quartic-query-separation'
        if not preprint and slug not in LITERATURE['expert_paper']:
            raise ValueError(f'citation map source is not selected: {slug}')
        folder = paper_annex if preprint else annexes / slug
        prefix = 'paper/' if preprint else 'literature/' + slug + '/'
        for row in annex['files']:
            relative = row['annex_relative_path']
            base.check_packets.check_name(relative)
            path = base.safe_source(folder / relative)
            blob = path.read_bytes()
            if len(blob) != row['bytes'] or base.digest(blob) != row['sha256']:
                raise ValueError(f'citation source changed: {slug}/{relative}')
            member = prefix + relative
            if member in files and files[member][0].read_bytes() != blob:
                raise ValueError(f'citation source collision: {member}')
            files[member] = (path, 'citation_mapped_primary_source', 'annex:' + slug + '/' + relative)
            row['member'] = member
    supplement = json.loads(files['SUPPLEMENTARY_LITERATURE.json'][0].read_bytes())
    required = {(r['id'], r['role']) for r in coverage['supplementary_requirements']}
    actual = {(r['id'], r['role']) for r in supplement['sources']}
    if not required <= actual:
        raise ValueError(f'missing required supplementary sources: {sorted(required - actual)}')
    coverage['supplementary_sources'] = supplement['sources']
    coverage['cited_only_sources'] = supplement.get('cited_only_sources', [])
    coverage['exact_edition_unavailable'] = supplement.get('exact_edition_unavailable', [])
    coverage['code_source'] = json.loads(files['CODE_SOURCE_PROVENANCE.json'][0].read_bytes())
    if coverage['code_source']['commit'] != coverage['code_citation']['commit']:
        raise ValueError('citation map and pinned Complexitylib edition disagree')
    coverage['code_source'].pop('sources')  # Full per-file hashes live in the separate provenance file.
    by_slug = {r['slug']: [f['member'] for f in r['files']] for r in coverage['annex_sources']}
    for row in coverage['citations']:
        row['packaged_members'] = [member for slug in row['annex_slugs'] for member in by_slug.get(slug, [])]
        row['supplementary_editions'] = [r['id'] for r in supplement['sources']
                                        if row['citation_key'] in r.get('citation_keys', [])]
        row['packaged_members'] += [f['member'] for r in supplement['sources']
                                    if r['id'] in row['supplementary_editions'] for f in r['files']]
        if row.get('repository_source'):
            member = row['repository_source']
            if member in files or member == 'SOURCE_STATUS.json':
                row['packaged_members'].append(member)
        if row['citation_key'] in {coverage['code_citation']['citation_key'], 'Complexitylib2026'}:
            row['packaged_members'].append('CODE_SOURCE_PROVENANCE.json')
        row['package_status'] = 'source_content_supplied_see_edition_boundary' if row['packaged_members'] else 'cited_only'
    coverage['interpretation'] = ('Every listed member is byte-bound by the packet manifest. Source availability '
        'and separate editions are explicit; neither this inventory nor register measurements certify '
        'source comprehension, theorems, writing quality or equivalence of editions.')
    path = generated / 'LITERATURE_COVERAGE.json'
    path.write_bytes(base.encoded(coverage))
    files[path.name] = (path, 'current_citation_coverage', 'generated:research/requests/round10/citation_coverage.json')
    files['repository/research/requests/round10/citation_coverage.json'] = (
        source, 'reviewed_citation_map', 'repository:research/requests/round10/citation_coverage.json')


def inputs(job, **options):
    root = options['root']
    files = round7.inputs(job, **options)
    generated = Path(state['work']) / job
    generated.mkdir(parents=True, exist_ok=True)
    pdfs = dict(zip(LEADS.values(), (options['expert_pdf'], options['exposition_pdf'], options['record_pdf'])))
    provenance = render_provenance(root, pdfs)
    for name in LEADS.values():
        source = (root / f'docs/{name}.md').read_text()
        path = generated / f'{name}.lines.txt'
        path.write_text(''.join(f'{i:05d} | {line}\n' for i, line in enumerate(source.splitlines(), 1)))
        files[f'reading/{path.name}'] = (path, 'numbered_reading_copy', f'repository:docs/{name}.md')
        files[f'render_receipts/{name}.json'] = (pdfs[name].with_name('render.json'),
                                              'native_render_receipt', 'external:native-render/' + name)
    receipt = generated / 'RENDER_PROVENANCE.json'
    receipt.write_bytes(base.encoded(provenance))
    files[receipt.name] = (receipt, 'render_binding', 'generated:current-source-and-PDF-hashes')
    for name in ('chronological_reading.md', 'literature_standard.md'):
        files[name] = (base.safe_source(options['requests_dir'] / name), 'review_method',
                       'repository:research/requests/round10/' + name)
    files.update(verified_round9(root))
    add_round9_decisions(files, root, generated)
    add_writing_method(files, Path(round7.state['lean_exposition']), generated)
    add_local_writing_method(files, root, generated)
    add_supplementary_literature(files, state['supplementary_literature'])
    add_complexitylib(files, root, generated, state['complexitylib'])
    add_citation_coverage(files, root, options['requests_dir'], options['annexes'], options['paper_annex'], generated)
    return files


def source_status(root, data, record_pdf):
    status, diff = round9.source_status(root, data, record_pdf)
    status['schema'] = 'quartic-round10-source-status-v1'
    status['writing_method'] = json.loads(data['METHOD_PROVENANCE.json'])['commit']
    status['previous_round_intake_sha256'] = base.digest(data['previous_round/intake.json'])
    return status, diff


def supplementary_map(data):
    if 'SUPPLEMENTARY_LITERATURE.json' not in data:
        return ''
    spec = json.loads(data['SUPPLEMENTARY_LITERATURE.json'])
    lines = ['\n## Additional full texts — read after freezing the first pass', '']
    for row in spec['sources']:
        links = ', '.join(f'[{Path(f["member"]).name}]({f["member"]})' for f in row['files'])
        lines.append(f'- {row["title"]} ({row["edition"]}): {links}. {row["edition_relation"]}')
    lines += ['', 'The final cited-only list refers to exact original editions. The supplied Barnum–Saks–Szegedy '
              '2002 primary report is an earlier version of the unavailable 2003 conference edition.']
    return '\n'.join(lines) + '\n'


def packet_map(job, data):
    return (round6.base_packet_map(job, data) + '\n'
        '- First pass only: [chronological protocol](chronological_reading.md) and '
        f'[lead-paper line locators](reading/{LEADS[job]}.lines.txt).\n'
        '- After freezing the first pass: [literature excellence standard](literature_standard.md), '
        '[writing skills](skills/README.md), [authoring guide](docs/authoring.md), '
        '[local refinements](skills/quartic-writing-method.md), [reader principles](reader_principles.md).\n'
        '- Fresh PDF bindings: [RENDER_PROVENANCE.json](RENDER_PROVENANCE.json); '
        'unaltered native receipts under `render_receipts/`.\n'
        '- Merged writing-method pin and source hashes: [METHOD_PROVENANCE.json](METHOD_PROVENANCE.json).\n'
        '- After freezing: [citation and edition coverage](LITERATURE_COVERAGE.json), '
        '[supplementary full texts](SUPPLEMENTARY_LITERATURE.json), and '
        '[pinned cited code](CODE_SOURCE_PROVENANCE.json). Every packet carries all 42 retained query-literature '
        'sources, the preprint, required supplemental editions and six complete writing-method sources. '
        'Exact-edition exceptions remain explicit in the inventories.\n'
        '- Register: [rules](register/REGISTER_RULES.md), [measurement](register/measurement.txt), '
        '[literature profile](register/profile.json).\n'
        '- After freezing the first pass: [complete round-nine custody](previous_round/intake.json), '
        '[synthesis](previous_round/adjudication/round9_synthesis.json), '
        '[revision account](previous_round/adjudication/round9_revision.md), '
        '[validation](previous_round/adjudication/round9_validation.json). '
        'Original ZIPs are under `previous_round/archives/`; every submitted member, including JSONL and scripts, '
        'is under `previous_round/members/` with compatibility copies under `previous_round/returns/`. '
        'Submitted scripts are preserved as evidence, not executed.\n'
        '- Complete round-nine decisions and disposition directories are under `previous_round/adjudication/`. '
        'Markdown aliases rebase links; exact originals remain at `repository/research/adjudication/`.\n'
        '- Earlier round-eight feedback remains under `earlier_round8/`, and round-seven evidence under '
        '`earlier_round7/`. Historical submissions and instructions describe earlier editions; '
        'this round\'s READ_ME_FIRST and chronological protocol own the current assignment.\n' + supplementary_map(data))


def configure(lean_exposition, work=None, supplementary_literature=None, complexitylib=None):
    round8.configure(lean_exposition)
    round6.PREVIOUS = PREVIOUS
    base.CAMPAIGN, base.JOBS, base.PREFIX = 'round10', JOBS, PREFIX
    base.LITERATURE, base.CITED_ONLY_BY_JOB = LITERATURE, CITED_ONLY
    base.inputs, base.packet_map, base.source_status = inputs, packet_map, source_status
    base.check_reader_leaks = check_reader_leaks
    state['work'] = work
    state['supplementary_literature'] = supplementary_literature
    state['complexitylib'] = complexitylib


def index_text(audit, status, frozen):
    lines = ['# Round-ten review packets', '',
             'Three independent packets, one lead paper each. Freeze the chronological first encounter before '
             'reading guidance or past feedback. Return concrete improvements and honest coverage, '
             'judged against excellent mathematical literature.', '',
             f'Source commit `{status["repository_commit"]}`. Writing method `{status["writing_method"]}`. '
             f'Freeze digest `{frozen}`.', '']
    for row in audit:
        lines.append(f'- [{row["archive"]}]({row["archive"]}): {JOBS[row["job"]]}; '
                     f'{len(row["literature_present"])} literature sources; SHA-256 `{row["sha256"]}`.')
    return '\n'.join(lines) + '\n\n[Batch audit](batch-audit.json). Nothing is sent by this builder.\n'


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    for name in ('annexes', 'paper-annex', 'expert-pdf', 'exposition-pdf', 'record-pdf', 'lean-exposition'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--dest', type=Path)
    parser.add_argument('--complexitylib', type=Path, help='Git checkout containing the Lake-pinned cited source')
    parser.add_argument('--supplementary-literature', type=Path, required=True,
                        help='source-bound supplemental query and writing literature manifest')
    parser.add_argument('--only', nargs='+', choices=list(JOBS))
    args = parser.parse_args(argv)
    options = dict(root=ROOT, requests_dir=REQUESTS,
                   **{name: getattr(args, name).resolve() for name in
                      ('annexes', 'paper_annex', 'expert_pdf', 'exposition_pdf', 'record_pdf')})
    try:
        with tempfile.TemporaryDirectory(prefix='quartic-r10-') as temp:
            configure(args.lean_exposition.resolve(), Path(temp), args.supplementary_literature, args.complexitylib)
            round7.state['register'] = round7.build_register(round7.state['lean_exposition'], options['annexes'],
                                                            Path(temp), title='Round ten: chronological review')
            jobs = args.only or list(JOBS)
            if args.dest:
                for path in round8.build_batch(jobs, args.dest, campaign='round10', literature=LITERATURE,
                                              cited_only=CITED_ONLY, index_renderer=index_text, **options):
                    print(f'PASS {path}')
            else:
                packets = base.prepare_batch(jobs, **options)
                print(f'Validated {len(packets)} packets; freeze digest {base.batch_digest(packets)}')
    except (OSError, ValueError, KeyError, ImportError, subprocess.CalledProcessError, zipfile.BadZipFile) as error:
        parser.exit(1, f'FAIL: {error}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
