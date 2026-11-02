import importlib.util
from pathlib import Path
import unittest


PATH = Path(__file__).resolve().parents[1] / "tools/build_round2_packets.py"
SPEC = importlib.util.spec_from_file_location("round2", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RoundTwoTests(unittest.TestCase):
    def test_every_job_has_a_request_and_renders(self):
        for job in MODULE.JOBS:
            text = MODULE.render_request(job)
            self.assertIn("NEW_STATEMENTS.json", text)
            self.assertIn("BUILD_STATUS.md", text)
            self.assertNotIn("Aaronson", text)
            self.assertIn(job, MODULE.PRIORITY)

    def test_skeleton_places_every_statement(self):
        text = MODULE.record_skeleton().decode()
        import json
        rows = json.loads((MODULE.ROOT / "corpus/statements.json").read_text(encoding="utf-8"))
        rows = rows["statements"] if isinstance(rows, dict) else rows
        for row in rows:
            self.assertIn(f"`{row['id']}`", text)

    @unittest.skipUnless(MODULE.ANNEXES.is_dir(), "annex checkout not present")
    def test_priority_literature_exists_when_annexes_are_present(self):
        for job in MODULE.JOBS:
            MODULE.literature(job)


if __name__ == "__main__":
    unittest.main()
