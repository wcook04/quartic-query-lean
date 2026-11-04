"""Complete custody and pinned methods, with synthetic portable input fixtures."""
import importlib.util
import json
from pathlib import Path
import posixpath
import subprocess
import tempfile
import unittest
from unittest import mock
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('round10', ROOT / 'tools/build_round10_packets.py')
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class RoundTenTests(unittest.TestCase):
    def test_live_catalog_matches_the_inspected_five_author_title_page(self):
        slug = 'quartic-lit-aaronson-ambainis-bogdanov-quantum-vs-classical'
        label, edition = M.round6.EXTRA_CATALOG[slug]
        self.assertIn('Aaronson–Ambainis–Bogdanov–Cheung–Dinesh', label)
        self.assertNotIn('Yeung', label)
        self.assertEqual(edition, 'ECCC TR21-115 rev. 2')

    def tearDown(self):
        M.round8.configure()
        M.base.check_reader_leaks = M.original_reader_leak_check

    def test_requests_cover_three_leads_without_inherited_finding_quotas(self):
        M.configure(Path('/unused-method'))
        self.assertEqual({'expert_paper', 'exposition', 'reasoning_record'}, set(M.JOBS))
        for job, lead in M.LEADS.items():
            request = M.base.render_request(job, M.REQUESTS)
            self.assertIn(lead.replace('_', ' '), request)
            for required in ('sentence_audit.jsonl', 'coverage.json', 'first_pass/',
                             'freeze.json', 'later_annotations.jsonl'):
                self.assertIn(required, request)
            self.assertNotIn('{job}', request)
            self.assertNotRegex(request, r'(?:at least|target of)\s+(?:200|250|400)\s+findings')
        for job, slugs in M.LITERATURE.items():
            self.assertEqual(len(slugs), len(set(slugs)))
            self.assertFalse(set(slugs) - set(M.base.CATALOG), job)

    def custody_fixture(self, root):
        custody = root / 'research/returns/round9'
        custody.mkdir(parents=True)
        inventory = {'returns': []}
        for job in M.JOBS:
            members = {'sentence_audit.jsonl': b'{"unit": 1}\n',
                       'checks/reproduce.py': b'raise RuntimeError("never execute submitted code")\n',
                       'SHA256SUMS.txt': b'original submitted checksum evidence\n'}
            rows = []
            for name, blob in members.items():
                path = custody / 'members' / job / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(blob)
                rows.append({'path': name, 'bytes': len(blob), 'sha256': M.base.digest(blob)})
            archive = custody / 'archives' / (job + '.zip')
            archive.parent.mkdir(exist_ok=True)
            with zipfile.ZipFile(archive, 'w') as z:
                for name, blob in members.items():
                    z.writestr(name, blob)
            blob = archive.read_bytes()
            inventory['returns'].append({'id': job, 'archive': {
                'preserved': 'archives/' + archive.name, 'bytes': len(blob), 'sha256': M.base.digest(blob)},
                'members_root': 'members/' + job, 'members': rows})
        (custody / 'intake.json').write_text(json.dumps(inventory))
        return custody, inventory

    def test_all_original_archives_and_nonprose_members_are_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            custody, inventory = self.custody_fixture(root)
            files = M.verified_round9(root)
            for submission in inventory['returns']:
                for relative in [submission['archive']['preserved'],
                                 *[submission['members_root'] + '/' + row['path'] for row in submission['members']]]:
                    self.assertEqual((custody / relative).read_bytes(), files['previous_round/' + relative][0].read_bytes())
            self.assertEqual(3, sum(name.startswith('previous_round/archives/') for name in files))
            self.assertIn('previous_round/returns/expert_paper/checks/reproduce.py', files)

    def test_custody_missing_changed_duplicate_and_escaping_members_fail(self):
        for mutation in ('missing', 'changed', 'archive', 'duplicate', 'escape', 'missing_panel'):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                custody, inventory = self.custody_fixture(root)
                row = inventory['returns'][0]
                path = custody / row['members_root'] / row['members'][0]['path']
                if mutation == 'missing':
                    path.unlink()
                elif mutation == 'changed':
                    path.write_text('changed')
                elif mutation == 'archive':
                    (custody / row['archive']['preserved']).write_bytes(b'other ZIP')
                elif mutation == 'duplicate':
                    row['members'].append(row['members'][0])
                elif mutation == 'escape':
                    row['members'][0]['path'] = '../../../outside.jsonl'
                else:
                    inventory['returns'].pop()
                (custody / 'intake.json').write_text(json.dumps(inventory))
                with self.assertRaises((OSError, ValueError)):
                    M.verified_round9(root)

    def test_decisions_include_nested_files_and_rebase_only_maintained_aliases(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'repo'
            owner = root / 'research/adjudication'
            (owner / 'round9_dispositions').mkdir(parents=True)
            (root / 'docs').mkdir()
            (root / 'docs/exposition.md').write_text('# Exposition\n')
            for name in ('round9_synthesis.json', 'round9_validation.json', 'round9_dispositions/exposition.json'):
                (owner / name).write_text('{}\n')
            original = '[draft](../../docs/exposition.md#intro)\n[decision](round9_dispositions/exposition.json)\n'
            (owner / 'round9_revision.md').write_text(original)
            generated = Path(temp) / 'generated'; generated.mkdir()
            files = {}
            M.add_round9_decisions(files, root, generated)
            self.assertIn('previous_round/adjudication/round9_dispositions/exposition.json', files)
            self.assertEqual(original, files['repository/research/adjudication/round9_revision.md'][0].read_text())
            alias = 'previous_round/adjudication/round9_revision.md'
            for target in M.base.link_targets(files[alias][0].read_text()):
                member = posixpath.normpath(posixpath.join(posixpath.dirname(alias), unquote(urlsplit(target).path)))
                self.assertIn(member, files)

    def method_fixture(self, root):
        sources = {
            'skills/README.md': '[authoring](../docs/authoring.md)\n',
            'docs/authoring.md': '[reader](reader-review.md)\n[references](references.json)\n'
                                 '[rules](../src/lean_exposition/resources/register/rules.json)\n',
            'docs/reader-review.md': '# Freeze before critique\n',
            'docs/references.json': '{"references": []}\n',
            'docs/register-stage.md': '[authoring](authoring.md)\n',
            'src/lean_exposition/resources/register/rules.json': '{"original": true}\n',
        }
        for name, text in sources.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
        for args in (('init', '-q'), ('add', '.'),
                     ('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.test', 'commit', '-qm', 'fixture')):
            subprocess.run(['git', '-C', str(root), *args], check=True, capture_output=True)
        return subprocess.check_output(['git', '-C', str(root), 'rev-parse', 'HEAD']).decode().strip()

    def test_method_closure_is_pinned_and_register_transformation_explicit(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'method'; root.mkdir()
            pin = self.method_fixture(root)
            generated = Path(temp) / 'generated'; generated.mkdir()
            register = Path(temp) / 'register'; register.mkdir()
            (register / 'register_rules.json').write_text('{"sanitized": true}\n')
            with mock.patch.object(M, 'METHOD_COMMIT', pin), mock.patch.dict(M.round7.state, register=register):
                files = {}
                M.add_writing_method(files, root, generated)
                self.assertIn('docs/reader-review.md', files)
                self.assertIn('docs/references.json', files)
                receipt = json.loads(files['METHOD_PROVENANCE.json'][0].read_bytes())
                self.assertEqual(pin, receipt['commit'])
                rule = next(row for row in receipt['sources'] if row['member'].endswith('/rules.json'))
                self.assertNotEqual(rule['source_sha256'], rule['packaged_sha256'])
                (root / 'docs/reader-review.md').write_text('uncommitted change')
                with self.assertRaisesRegex(ValueError, 'differs from merged revision'):
                    M.add_writing_method({}, root, generated)
            with self.assertRaisesRegex(ValueError, 'must be merged revision'):
                M.add_writing_method({}, root, generated)

    def test_existing_batch_and_checkout_destinations_are_refused_before_prepare(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'repo'; root.mkdir()
            existing = Path(temp) / 'sent'; existing.mkdir()
            (existing / 'original.zip').write_bytes(b'preserved')
            with mock.patch.object(M.base, 'prepare_batch') as prepare:
                for dest in (root / 'new-output', existing):
                    with self.assertRaises((ValueError, FileExistsError)):
                        M.round8.build_batch(list(M.JOBS), dest, campaign='round10', root=root)
                prepare.assert_not_called()
            self.assertEqual(b'preserved', (existing / 'original.zip').read_bytes())

    def test_supplementary_sources_require_original_text_and_matching_hashes(self):
        with self.assertRaisesRegex(ValueError, 'requires the supplementary'):
            M.add_supplementary_literature({}, None)
        for mutation in (None, 'hash', 'missing_text', 'escape', 'collision'):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                entries = []
                for name, blob in (('source.pdf', b'complete PDF fixture'), ('extracted-ocr.md', b'full OCR text')):
                    (root / name).write_bytes(blob)
                    entries.append({'path': name, 'member': 'literature/fixture/' + name,
                                    'sha256': M.base.digest(blob), 'bytes': len(blob)})
                row = {'id': 'fixture', 'role': 'query-literature', 'title': 'Fixture',
                       'source_url': 'https://example.test/source', 'edition': 'earlier primary edition',
                       'edition_relation': 'Not the conference edition', 'files': entries}
                if mutation == 'hash':
                    entries[0]['sha256'] = '0' * 64
                elif mutation == 'missing_text':
                    row['files'] = entries[:1]
                elif mutation == 'escape':
                    entries[0]['path'] = '../source.pdf'
                spec = root / 'manifest.json'
                spec.write_text(json.dumps({'schema': 'quartic-round10-supplementary-literature-v1', 'sources': [row]}))
                files = {} if mutation != 'collision' else {entries[0]['member']: (root / 'source.pdf', '', '')}
                if mutation:
                    with self.assertRaises((ValueError, OSError)):
                        M.add_supplementary_literature(files, spec)
                else:
                    M.add_supplementary_literature(files, spec)
                    self.assertIn('SUPPLEMENTARY_LITERATURE.json', files)
                    self.assertEqual(b'full OCR text', files['literature/fixture/extracted-ocr.md'][0].read_bytes())

    def test_code_export_uses_pinned_git_bytes_and_leaves_checkout_untouched(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'repo'; (root / 'lean').mkdir(parents=True)
            dependency = Path(temp) / 'dependency'; dependency.mkdir()
            (dependency / 'Proof.lean').write_text('-- pinned source\n')
            (dependency / 'docs').mkdir()
            (dependency / 'docs/proof.lean').symlink_to('../Proof.lean')
            for args in (('init', '-q'), ('add', '.'),
                         ('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.test', 'commit', '-qm', 'pin')):
                subprocess.run(['git', '-C', str(dependency), *args], check=True, capture_output=True)
            commit = subprocess.check_output(['git', '-C', str(dependency), 'rev-parse', 'HEAD']).decode().strip()
            (root / 'lean/lake-manifest.json').write_text(json.dumps({'packages': [
                {'name': 'complexitylib', 'rev': commit, 'url': 'https://example.test/complexitylib'}]}))
            (dependency / 'Proof.lean').write_text('-- unrelated dirty change\n')
            (dependency / 'build.olean').write_bytes(b'not a source')
            generated = Path(temp) / 'generated'; generated.mkdir()
            files = {}
            M.add_complexitylib(files, root, generated, dependency)
            member = 'repository/dependency_sources/complexitylib/Proof.lean'
            self.assertEqual('-- pinned source\n', files[member][0].read_text())
            self.assertEqual('-- unrelated dirty change\n', (dependency / 'Proof.lean').read_text())
            alias = 'repository/dependency_sources/complexitylib/docs/proof.lean'
            self.assertEqual({member, alias, 'CODE_SOURCE_PROVENANCE.json'}, set(files))
            self.assertEqual('-- pinned source\n', files[alias][0].read_text())
            self.assertFalse(files[alias][0].is_symlink())
            receipt = json.loads(files['CODE_SOURCE_PROVENANCE.json'][0].read_bytes())
            self.assertEqual(commit, receipt['commit'])
            self.assertEqual(2, len(receipt['sources']))
            link = next(row for row in receipt['sources'] if row['member'] == alias)
            self.assertEqual('../Proof.lean', link['git_link_target'])
            self.assertEqual('Proof.lean', link['materialized_from'])
            self.assertEqual('120000', link['git_mode'])
            self.assertEqual(M.base.digest(b'-- pinned source\n'), link['materialized_target_sha256'])

    def test_reviewed_citation_map_covers_every_current_bibliography_without_local_paths(self):
        source = M.REQUESTS / 'citation_coverage.json'
        coverage = json.loads(source.read_bytes())
        self.assertNotIn('/Users/', source.read_text())
        self.assertNotIn('/tmp/', source.read_text())
        self.assertEqual(78, len(coverage['citations']))
        self.assertEqual(29, len(coverage['appendix_c_entries']))
        for row in coverage['citations']:
            if row.get('supplementary_source_ids'):
                self.assertEqual('supplementary_edition_supplied_see_edition_note', row['coverage_status'])
                self.assertIn('primary_annex_status', row)
        self.assertEqual(43, len(coverage['annex_sources']))
        for relative, row in coverage['bibliographies'].items():
            self.assertEqual(row['sha256'], M.base.digest((ROOT / relative).read_bytes()))
        self.assertEqual(set(M.LITERATURE['expert_paper']), set(M.round6.QUARTIC_LITERATURE))
        self.assertEqual(M.LITERATURE['expert_paper'], M.LITERATURE['exposition'])
        self.assertEqual(M.LITERATURE['expert_paper'], M.LITERATURE['reasoning_record'])

    def test_public_bibliography_author_exception_is_hash_bound_and_narrow(self):
        member = 'examples/public/references.bib'
        for case in ('public_author', 'unbound', 'changed_hash', 'notes', 'generic_author'):
            with self.subTest(case=case):
                text = '@article{example,\n  author = {Example, Ada},\n  title = {A public result},\n}\n'
                if case == 'notes':
                    text = text.replace('title =', 'note = {Ada provided a private review},\n  title =')
                elif case == 'generic_author':
                    text = text.replace('Example, Ada', 'email exchange')
                blob = text.encode()
                row = {'member': member, 'role': 'pinned_writing_method_source',
                       'source_sha256': M.base.digest(blob), 'packaged_sha256': M.base.digest(blob)}
                receipt = {'commit': M.METHOD_COMMIT, 'sources': [row]}
                if case == 'unbound':
                    receipt['commit'] = 'not-the-verified-pin'
                elif case == 'changed_hash':
                    row['source_sha256'] = '0' * 64
                data = {member: blob, 'METHOD_PROVENANCE.json': json.dumps(receipt).encode()}
                with mock.patch.object(M.base, 'READER_LEAKS',
                                       [__import__('re').compile(r'\bAda\b'), __import__('re').compile('email exchange')]):
                    if case == 'public_author':
                        M.check_reader_leaks(data, 'Request')
                        self.assertEqual(blob, data[member])
                    else:
                        with self.assertRaises(ValueError):
                            M.check_reader_leaks(data, 'Request')

    def test_round10_reuses_fail_closed_render_and_local_method_rebase(self):
        self.assertIs(M.render_provenance, M.round9.render_provenance)
        self.assertIs(M.add_local_writing_method, M.round9.add_local_writing_method)


if __name__ == '__main__':
    unittest.main()
