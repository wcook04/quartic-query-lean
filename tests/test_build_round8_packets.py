import importlib.util
from pathlib import Path
import re
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("round8", ROOT / "tools/build_round8_packets.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RoundEightTests(unittest.TestCase):
    def setUp(self):
        MODULE.configure()

    def test_each_panel_request_renders_with_its_lead_paper(self):
        for job, lead in (("expert_paper", "expert companion"), ("exposition", "exposition")):
            text = MODULE.base.render_request(job, MODULE.REQUESTS)
            self.assertIn(MODULE.JOBS[job], text)
            self.assertIn(f"The lead paper is the **{lead}**", text)
            self.assertNotIn("{", text.split("## Return format")[0].split("# ", 1)[1].splitlines()[0])

    def test_previous_round_and_literature_sources_exist(self):
        for member, path in MODULE.PREVIOUS.items():
            self.assertTrue((ROOT / path).is_file(), member)
        for job, slugs in MODULE.LITERATURE.items():
            self.assertEqual(set(slugs) - set(MODULE.base.CATALOG), set(), job)
            self.assertEqual(len(slugs), len(set(slugs)), job)

    def test_record_pdf_is_described_as_current(self):
        status = {"record": {"pdf_rendered_from": "the accepted Markdown", "since_pdf_diff": "x",
                             "changed_lines": 3}, "repository_commit": "abc", "acceptance_gate": "old"}
        with mock.patch.object(MODULE, "original_source_status", return_value=(status, b"diff")):
            result, diff = MODULE.source_status(ROOT, {}, None)
        self.assertIsNone(diff)
        self.assertNotIn("since_pdf_diff", result["record"])
        self.assertIn("current Markdown at repository commit abc", result["record"]["pdf_rendered_from"])

    def test_packet_map_links_only_shipped_previous_round_files(self):
        source = (ROOT / "tools/build_round8_packets.py").read_text(encoding="utf-8")
        start = source.index("def packet_map")
        linked = set(re.findall(r"\((previous_round/[^)]+)\)", source[start:source.index("def configure")]))
        self.assertTrue(linked)
        self.assertLessEqual(linked, set(MODULE.PREVIOUS))


if __name__ == "__main__":
    unittest.main()
