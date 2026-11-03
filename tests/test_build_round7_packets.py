import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("round7", ROOT / "tools/build_round7_packets.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RoundSevenTests(unittest.TestCase):
    def setUp(self):
        MODULE.configure()

    def test_every_panel_renders_a_feedback_request_naming_no_reader(self):
        for job in MODULE.JOBS:
            request = MODULE.base.render_request(job, MODULE.REQUESTS)
            self.assertIn("Emulate perspectives, never people", request)
            self.assertIn("search online", request)
            self.assertIn("reading_log.md", request)
            for pattern in MODULE.base.reader_leak_patterns():
                self.assertIsNone(pattern.search(request), (job, pattern.pattern))

    def test_previous_round_sources_exist(self):
        for source in MODULE.PREVIOUS.values():
            self.assertTrue((ROOT / source).is_file(), source)

    def test_panels_have_prefixes_and_a_literature_sample(self):
        self.assertEqual(set(MODULE.JOBS), set(MODULE.PREFIX))
        self.assertEqual(set(MODULE.JOBS), set(MODULE.LITERATURE))
        for job in MODULE.JOBS:
            self.assertTrue(5 <= len(MODULE.LITERATURE[job]) <= 10, job)
            self.assertTrue(set(MODULE.LITERATURE[job]) <= set(MODULE.base.CATALOG), job)


if __name__ == "__main__":
    unittest.main()
