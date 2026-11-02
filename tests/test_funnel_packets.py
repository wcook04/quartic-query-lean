import importlib.util
from pathlib import Path
import tempfile
import unittest


PATH = Path(__file__).resolve().parents[1] / "tools/build_funnel_packets.py"
SPEC = importlib.util.spec_from_file_location("funnel", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FunnelTests(unittest.TestCase):
    def test_every_job_has_a_request_and_renders(self):
        for job in MODULE.JOBS:
            text = MODULE.render_request(job)
            self.assertIn("NEW_STATEMENTS.json", text)
            self.assertNotIn("Aaronson", text)

    def test_missing_literature_is_an_error(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(SystemExit):
                MODULE.literature("2_short_expert_paper", Path(folder))

    def test_named_literature_exists_locally_when_annexes_are_present(self):
        if not MODULE.ANNEXES.is_dir():
            self.skipTest("annexes are local")
        for job in MODULE.JOBS:
            MODULE.literature(job)


if __name__ == "__main__":
    unittest.main()
