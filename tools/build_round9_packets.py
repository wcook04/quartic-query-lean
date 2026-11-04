#!/usr/bin/env python3
"""Build three round-nine chronological improvement-review packets, one per paper.

Reuse the existing frozen batch writer, link closure, private-name checker and
register stage. Require each supplied PDF's native render.json to bind its bytes
to the current manuscript. Outputs must be a new directory outside the checkout.
"""
import argparse
import json
from pathlib import Path
import posixpath
import re
import subprocess
import sys
import tempfile
import zipfile
from urllib.parse import quote, unquote, urlsplit, urlunsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_round8_packets as round8

round7, round6, base = round8.round7, round8.round6, round8.base
ROOT = base.ROOT
REQUESTS = ROOT / 'research/requests/round9'
JOBS = {
    'expert_paper': 'Chronological specialist review of the expert companion',
    'exposition': 'Chronological learning review of the exposition',
    'reasoning_record': 'Chronological proof and explanation review of the long record',
}
PREFIX = {'expert_paper': 'XP9', 'exposition': 'EX9', 'reasoning_record': 'RR9'}
LEADS = {'expert_paper': 'expert_companion', 'exposition': 'exposition', 'reasoning_record': 'reasoning_record'}
LITERATURE = {
    **round8.LITERATURE,
    'reasoning_record': list(dict.fromkeys(round8.LITERATURE['expert_paper'] + [
        'quartic-ref-01-forrelation-a-problem-that-optimally-separ',
        'quartic-ref-22-towards-proving-strong-direct-product-theo',
        'quartic-lit-girish-forrelation-is-extremally-hard',
        'quartic-lit-ambainis-iraids-kokainis-certificate-v3',
        'quartic-lit-buhrman-dewolf-decision-tree-survey',
        'arxiv-2103-11604',
        'quartic-ref-11-tight-bounds-on-quantum-searching',
        'quartic-ref-08-quantum-lower-bounds-by-polynomials'])),
}
CITED_ONLY = {job: ['yao1977', 'nisan1991', 'bss2003'] for job in JOBS}
PREVIOUS = {
    **{f'previous_round/{p.name}': str(p.relative_to(ROOT))
       for p in sorted((ROOT / 'research/adjudication').glob('round8_*')) if p.is_file()},
    **{f'previous_round/returns/{p.relative_to(ROOT / "research/returns/round8/members")}': str(p.relative_to(ROOT))
       for p in sorted((ROOT / 'research/returns/round8/members').rglob('*'))
       if p.is_file() and p.suffix in {'.md', '.json'}},
    'previous_round/intake.json': 'research/returns/round8/intake.json',
    **{name.replace('previous_round/', 'earlier_round7/', 1): path for name, path in round8.PREVIOUS.items()},
}
state = {'work': None}


def add_local_writing_method(files, root, generated):
    """Keep the original guide and rebase its compatibility copy's local links.

    Reuse the reading-source closure so linked guides stay at their repository
    paths. The manifest binds both the unchanged source and the relocated copy.
    Frozen packets are never modified by this builder.
    """
    source = root / 'docs/writing_method.md'
    member = 'repository/docs/writing_method.md'
    closure, _ = base.round4.linked_sources(root, {member: (source, 'writing_method')})
    for name, (path, role) in closure.items():
        files.setdefault(name, (base.safe_source(path), role, 'repository:' + name.split('/', 1)[1]))

    text = source.read_text(encoding='utf-8')
    references = re.compile(r'(?m)^ {0,3}\[(?!\^)[^\]\n]+\]:\s*(<[^>\n]+>|\S+)')
    replacements = []
    for pattern in (base.repository_checks.LINK, references):
        for match in pattern.finditer(text):
            raw = match.group(1)
            target = urlsplit(raw.strip('<>'))
            if target.scheme or target.netloc or not target.path:
                continue
            # linked_sources above has already rejected missing/escaping paths.
            path = (source.parent / unquote(target.path)).resolve()
            destination = 'repository/' + path.relative_to(root.resolve()).as_posix()
            if destination not in files and not any(n.startswith(destination.rstrip('/') + '/') for n in files):
                raise ValueError(f'writing-method link not packaged: {raw}')
            relative = quote(posixpath.relpath(destination, 'skills'), safe='/')
            value = urlunsplit(('', '', relative, target.query, target.fragment))
            if raw.startswith('<'):
                value = '<' + value + '>'
            replacements.append((match.start(1), match.end(1), value))
    for start, end, value in sorted(replacements, reverse=True):
        text = text[:start] + value + text[end:]
    relocated = generated / 'quartic-writing-method.md'
    relocated.write_text(text, encoding='utf-8')
    files['skills/quartic-writing-method.md'] = (
        relocated, 'relocated_writing_method', 'generated:repository:docs/writing_method.md')


def render_provenance(root, pdfs):
    """Fail closed on stale PDF bytes, source text, figures or renderer inputs."""
    result = {}
    for name, pdf in pdfs.items():
        receipt = json.loads(pdf.with_name('render.json').read_text())
        if receipt.get('status') != 'rendered_requires_visual_review':
            raise ValueError(f'{name}: no completed native render receipt')
        if receipt.get('pdf_sha256') != base.digest(pdf.read_bytes()):
            raise ValueError(f'{name}: PDF does not match render receipt')
        if name == 'reasoning_record':
            hashes = {f'docs/{name}.md': receipt['source_sha256'],
                      'tools/render_reasoning_record.py': receipt['renderer_sha256']}
            # Native record receipt also binds every explicit bibliography.
            for path, sha in {**receipt['explicit_bibliographies'], **receipt['layout_sources']}.items():
                hashes[str(Path(path).relative_to(root))] = sha
            if not receipt.get('source_unchanged'):
                raise ValueError('record source changed while rendering')
        else:
            hashes = receipt['inputs']
        required = {f'docs/{name}.md'}
        if name != 'reasoning_record':
            required.add(f'docs/{name}.bib')
        if not required <= set(hashes):
            raise ValueError(f'{name}: manuscript or bibliography absent from receipt')
        for path, sha in hashes.items():
            source = (root / path).resolve()
            if root.resolve() not in source.parents or base.digest(source.read_bytes()) != sha:
                raise ValueError(f'{name}: stale render input {path}')
        result[name] = {'pdf_sha256': receipt['pdf_sha256'], 'inputs': hashes,
                        'visual_acceptance': 'separate human/agent page inspection; not established by these hashes'}
    return result


def add_render_inputs(files, root, provenance):
    """Close the packet over every input claimed by its native render receipt."""
    for name, receipt in provenance.items():
        packaged = {}
        for relative, expected in receipt['inputs'].items():
            base.check_packets.check_name(relative)
            source = base.safe_source(root / relative)
            if base.digest(source.read_bytes()) != expected:
                raise ValueError(f'{name}: changed render input {relative}')
            member = 'repository/' + relative
            if member in files and files[member][0].read_bytes() != source.read_bytes():
                raise ValueError(f'{name}: render input collision {member}')
            files.setdefault(member, (source, 'native_render_input', 'repository:' + relative))
            packaged[relative] = member
        receipt['packaged_inputs'] = packaged


def inputs(job, **options):
    files = round7.inputs(job, **options)
    root = options['root']
    pdfs = dict(zip(('expert_companion', 'exposition', 'reasoning_record'),
                    (options['expert_pdf'], options['exposition_pdf'], options['record_pdf'])))
    provenance = render_provenance(root, pdfs)
    add_render_inputs(files, root, provenance)
    generated = Path(state['work']) / job
    generated.mkdir(parents=True, exist_ok=True)
    for name in LEADS.values():
        source = (root / f'docs/{name}.md').read_text()
        path = generated / f'{name}.lines.txt'
        path.write_text(''.join(f'{i:05d} | {line}\n' for i, line in enumerate(source.splitlines(), 1)))
        files[f'reading/{path.name}'] = (path, 'numbered_reading_copy', f'repository:docs/{name}.md')
    receipt = generated / 'RENDER_PROVENANCE.json'
    receipt.write_bytes(base.encoded(provenance))
    files[receipt.name] = (receipt, 'render_binding', 'generated:current-source-and-PDF-hashes')
    files['chronological_reading.md'] = (root / 'research/requests/round9/chronological_reading.md',
                                             'review_method', 'repository:research/requests/round9/chronological_reading.md')
    method = Path(round7.state['lean_exposition'])
    for name in ('docs/authoring.md', 'docs/erdos-method-transfer.md',
                 'src/lean_exposition/resources/templates/critique-request.md',
                 'papers/qaoa-sk/long/reasoning-record.md'):
        files[name] = (base.safe_source(method / name), 'writing_method_support', 'lean-exposition:' + name)
    files['src/lean_exposition/resources/register/rules.json'] = (
        Path(round7.state['register']) / 'register_rules.json', 'sanitized_register_rules',
        'generated:register/register_rules.json')
    add_local_writing_method(files, root, generated)
    return files


def source_status(root, data, record_pdf):
    status, diff = round8.source_status(root, data, record_pdf)
    for name in ('reasoning_record.md', 'reasoning_record.bib', 'reasoning_record.pdf'):
        path = 'repository/docs/' + name
        status['drafts'][path] = base.digest(data[path])
    return status, diff


def packet_map(job, data):
    return (round6.base_packet_map(job, data) + '\n'
        '- Required first-read method: [chronological review](chronological_reading.md).\n'
        f'- Lead-paper line locators: [numbered Markdown](reading/{LEADS[job]}.lines.txt).\n'
        '- Fresh render bindings: [RENDER_PROVENANCE.json](RENDER_PROVENANCE.json).\n'
        '- All writing skills: [method index](skills/README.md), [register stage](skills/register-stage.md), '
        '[local refinements](skills/quartic-writing-method.md), [reader principles](reader_principles.md).\n'
        '- Register: [rules](register/REGISTER_RULES.md), [measurement](register/measurement.txt), '
        '[literature profile](register/profile.json).\n'
        '- Read after the first pass: [round-eight decisions](previous_round/round8_synthesis.json), '
        '[revision notes](previous_round/round8_revision.md), [validation](previous_round/round8_validation.json), '
        'and the complete text/JSON returns under `previous_round/returns/`.\n'
        '- Older audits and verdicts remain under `earlier_round7/`; they describe earlier editions.\n')


def configure(lean_exposition=None, work=None):
    round8.configure(lean_exposition)
    round6.PREVIOUS = PREVIOUS
    base.CAMPAIGN, base.JOBS, base.PREFIX = 'round9', JOBS, PREFIX
    base.LITERATURE, base.CITED_ONLY_BY_JOB = LITERATURE, CITED_ONLY
    base.inputs, base.packet_map, base.source_status = inputs, packet_map, source_status
    state['work'] = work


def index_text(audit, status, frozen):
    lines = ['# Round-nine review packets', '',
             'Three independent packets, one lead paper each. Read sequentially before consulting past feedback. '
             'Return located improvements and sentence-level coverage, not praise or rewrites.', '',
             f'Source commit `{status["repository_commit"]}`. Freeze digest `{frozen}`.', '']
    for row in audit:
        lines.append(f'- [{row["archive"]}]({row["archive"]}): {JOBS[row["job"]]}; '
                     f'{len(row["literature_present"])} literature sources; SHA-256 `{row["sha256"]}`.')
    return '\n'.join(lines) + '\n\n[Batch audit](batch-audit.json). Nothing is sent by this builder.\n'


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    for name in ('annexes', 'paper-annex', 'expert-pdf', 'exposition-pdf', 'record-pdf'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--lean-exposition', type=Path)
    parser.add_argument('--dest', type=Path)
    parser.add_argument('--only', nargs='+', choices=list(JOBS))
    args = parser.parse_args(argv)
    options = dict(root=ROOT, requests_dir=REQUESTS,
                   **{name: getattr(args, name).resolve() for name in
                      ('annexes', 'paper_annex', 'expert_pdf', 'exposition_pdf', 'record_pdf')})
    try:
        with tempfile.TemporaryDirectory(prefix='quartic-r9-') as temp:
            configure(args.lean_exposition, Path(temp))
            round7.state['register'] = round7.build_register(round7.state['lean_exposition'], options['annexes'],
                                                            Path(temp), title='Round nine: chronological review')
            jobs = args.only or list(JOBS)
            if args.dest:
                for path in round8.build_batch(jobs, args.dest, campaign='round9', literature=LITERATURE,
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
