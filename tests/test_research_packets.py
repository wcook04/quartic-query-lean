"""Exercise packet source routing without private papers or a Lean installation."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

SCRIPT = Path(__file__).resolve().parents[1] / 'tools/build_research_packets.py'
SPEC = importlib.util.spec_from_file_location('packets', SCRIPT)
packets = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(packets)


class PacketTests(unittest.TestCase):
    def test_configured_cli_preserves_archive_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sources = dict(intake=root / 'intake', papers_dir=root / 'papers',
                           paper_annex=root / 'annex', lean_dir=root / 'lean')
            sources['papers_dir'].mkdir()
            (sources['papers_dir'] / 'reference.pdf').write_bytes(b'fixture PDF')
            for job in packets.JOBS:
                for path in packets.members(job, **sources).values():
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(('fixture: ' + path.name).encode())
            dest = root / 'output'
            result = subprocess.run([
                sys.executable, str(SCRIPT), '--dest', str(dest),
                '--intake-dir', str(sources['intake']),
                '--papers-dir', str(sources['papers_dir']),
                '--paper-annex', str(sources['paper_annex']),
                '--lean-dir', str(sources['lean_dir']),
            ], cwd=root, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(list(dest.glob('*.zip'))), 3)
            for job in packets.JOBS:
                with zipfile.ZipFile(dest / f'quartic_{job}.zip') as archive:
                    expected = packets.members(job, **sources)
                    self.assertEqual(set(archive.namelist()),
                                     set(expected) | {'manifest.json', 'READ_ME_FIRST.md'})
                    self.assertEqual(archive.read('READ_ME_FIRST.md').decode('utf-8'),
                                     packets.render_request(job))
                    manifest = json.loads(archive.read('manifest.json'))
                    for row in manifest['members']:
                        data = archive.read(row['member'])
                        self.assertEqual(data, expected[row['member']].read_bytes())
                        self.assertEqual(row['sha256'], hashlib.sha256(data).hexdigest())
                    self.assertIn('paper/quartic-query-separation.pdf', archive.namelist())
                    self.assertEqual('literature/papers/reference.pdf' in archive.namelist(),
                                     not job.startswith('3_'))
                    self.assertEqual('lean/current/Drift.lean' in archive.namelist(),
                                     not job.startswith('2_'))

    def test_request_edit_is_read_without_reimporting_tool(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            job = next(iter(packets.JOBS))
            (root / 'common.md').write_text('# {title}\n{job}\n{boundary}\n')
            (root / 'boundaries.md').write_text('Shared boundaries.')
            request = root / f'{job}.md'
            request.write_text('Initial instructions.')
            self.assertIn('Initial instructions.', packets.render_request(job, root))
            request.write_text('Revised instructions with literal {braces}.')
            self.assertIn('Revised instructions with literal {braces}.',
                          packets.render_request(job, root))

    def test_missing_request_names_the_missing_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(SystemExit, 'cannot read research request.*common.md'):
                packets.render_request(next(iter(packets.JOBS)), Path(tmp))

    def test_template_cannot_silently_omit_job_or_boundaries(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            job = next(iter(packets.JOBS))
            (root / 'boundaries.md').write_text('Boundaries')
            (root / f'{job}.md').write_text('Job')
            for template in ('{title} {job}', '{title} {unknown} {boundary}',
                             '{title} {job} {boundary} {boundary}', '{title'):
                with self.subTest(template=template):
                    (root / 'common.md').write_text(template)
                    with self.assertRaisesRegex(SystemExit, 'invalid research request template'):
                        packets.render_request(job, root)

    def test_missing_sources_fail_before_writing_packet(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            job = next(iter(packets.JOBS))
            with self.assertRaisesRegex(SystemExit, 'missing sources'):
                packets.build(job, root, intake=root,
                              paper_annex=root, lean_dir=root, papers_dir=root)
            self.assertEqual(list(root.glob('*.zip')), [])


if __name__ == '__main__':
    unittest.main()
