import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("round6", ROOT / "tools/build_round6_packets.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RoundSixTests(unittest.TestCase):
    def setUp(self):
        MODULE.configure()

    def test_every_panel_renders_a_request_naming_no_reader(self):
        for job in MODULE.JOBS:
            request = MODULE.base.render_request(job, MODULE.REQUESTS)
            self.assertIn("Emulate perspectives, never people", request)
            self.assertIn("weighting.md", request)
            for pattern in MODULE.base.reader_leak_patterns():
                self.assertIsNone(pattern.search(request), (job, pattern.pattern))

    def test_principles_are_anonymous_and_previous_round_sources_exist(self):
        text = (MODULE.REQUESTS / "reader_principles.md").read_text(encoding="utf-8")
        for pattern in MODULE.base.reader_leak_patterns():
            self.assertIsNone(pattern.search(text), pattern.pattern)
        for source in MODULE.PREVIOUS.values():
            self.assertTrue((ROOT / source).is_file(), source)

    def test_panels_have_prefixes_and_literature(self):
        self.assertEqual(set(MODULE.JOBS), set(MODULE.PREFIX))
        self.assertEqual(set(MODULE.JOBS), set(MODULE.LITERATURE))
        self.assertTrue(all(MODULE.LITERATURE[job] for job in MODULE.JOBS))


if __name__ == "__main__":
    unittest.main()
