"""Review scope and freshness gates without private literature or TeX dependencies."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('round9', ROOT / 'tools/build_round9_packets.py')
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class RoundNineTests(unittest.TestCase):
    def tearDown(self):
        M.round8.configure()

    def test_three_distinct_leads_and_actionable_chronological_contract(self):
        M.configure()
        self.assertEqual({'expert_paper', 'exposition', 'reasoning_record'}, set(M.JOBS))
        for job, lead in M.LEADS.items():
            request = M.base.render_request(job, M.REQUESTS)
            self.assertIn(f'The lead paper is the **{lead.replace("_", " ") if lead != "expert_companion" else "expert companion"}**', request)
            for required in ('sentence_audit.jsonl', 'coverage.json', 'No `keep` kind',
                             'before', 'previous_round_audit.json', 'advice'):
                self.assertIn(required, request)
            self.assertNotIn('{job}', request)
            M.base.check_readme_links(request, {'chronological_reading.md': b'protocol'})
        protocol = (M.REQUESTS / 'chronological_reading.md').read_text()
        for required in ('available_before', 'unresolved_after', 'later_resolution',
                         'answer-exposed', 'unreviewed', 'not independent blind readers'):
            self.assertIn(required, protocol)

    def test_complete_round8_text_returns_and_all_revision_records_included(self):
        included = set(M.PREVIOUS.values())
        for path in (ROOT / 'research/returns/round8/members').rglob('*'):
            if path.suffix in {'.md', '.json'}:
                self.assertIn(str(path.relative_to(ROOT)), included)
        for name in ('round8_synthesis.json', 'round8_revision.md', 'round8_validation.json'):
            self.assertIn('research/adjudication/' + name, included)
        for path in included:
            self.assertTrue((ROOT / path).is_file(), path)
        M.configure()
        for job, slugs in M.LITERATURE.items():
            self.assertEqual(len(slugs), len(set(slugs)))
            self.assertFalse(set(slugs) - set(M.base.CATALOG), job)

    def fixture(self, folder):
        root = folder / 'repo'; (root / 'docs').mkdir(parents=True)
        pdf = folder / 'expert_companion.pdf'; pdf.write_bytes(b'pdf fixture')
        for ext in ('md', 'bib'):
            (root / f'docs/expert_companion.{ext}').write_text('source ' + ext)
        receipt = {'status': 'rendered_requires_visual_review', 'pdf_sha256': M.base.digest(pdf.read_bytes()),
                   'inputs': {str(p.relative_to(root)): M.base.digest(p.read_bytes())
                              for p in (root / 'docs').iterdir()}}
        pdf.with_name('render.json').write_text(json.dumps(receipt))
        return root, pdf, receipt

    def test_fresh_receipt_binds_source_and_pdf(self):
        with tempfile.TemporaryDirectory() as temp:
            root, pdf, _ = self.fixture(Path(temp))
            result = M.render_provenance(root, {'expert_companion': pdf})
            self.assertEqual(M.base.digest(pdf.read_bytes()), result['expert_companion']['pdf_sha256'])

    def test_stale_pdf_source_and_incomplete_render_are_rejected(self):
        for mutation in ('pdf', 'source', 'incomplete', 'missing_bib'):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temp:
                root, pdf, receipt = self.fixture(Path(temp))
                if mutation == 'pdf':
                    pdf.write_bytes(b'wrong edition')
                elif mutation == 'source':
                    (root / 'docs/expert_companion.md').write_text('changed')
                elif mutation == 'incomplete':
                    receipt['status'] = 'rendering'
                else:
                    del receipt['inputs']['docs/expert_companion.bib']
                pdf.with_name('render.json').write_text(json.dumps(receipt))
                with self.assertRaises(ValueError):
                    M.render_provenance(root, {'expert_companion': pdf})

    def test_record_checks_native_layout_and_inline_bibliography(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'repo'; (root / 'docs').mkdir(parents=True)
            (root / 'tools').mkdir()
            source = root / 'docs/reasoning_record.md'; source.write_text('inline references')
            renderer = root / 'tools/render_reasoning_record.py'; renderer.write_text('renderer')
            layout = root / 'docs/layout.tex'; layout.write_text('layout')
            pdf = Path(temp) / 'reasoning_record.pdf'; pdf.write_bytes(b'pdf')
            receipt = {'status': 'rendered_requires_visual_review', 'source_sha256': M.base.digest(source.read_bytes()),
                       'renderer_sha256': M.base.digest(renderer.read_bytes()), 'source_unchanged': True,
                       'explicit_bibliographies': {}, 'layout_sources': {str(layout): M.base.digest(layout.read_bytes())},
                       'pdf_sha256': M.base.digest(pdf.read_bytes())}
            pdf.with_name('render.json').write_text(json.dumps(receipt))
            M.render_provenance(root, {'reasoning_record': pdf})
            layout.write_text('changed')
            with self.assertRaises(ValueError):
                M.render_provenance(root, {'reasoning_record': pdf})


if __name__ == '__main__':
    unittest.main()
