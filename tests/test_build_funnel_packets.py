import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


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

    def test_moved_adjudication_keeps_archive_names_and_includes_lean_guide(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            with patch.object(MODULE, "literature", return_value={}):
                files = MODULE.members("3_examples_first_exposition", root=root)
            for name in ("adjudication.json", "adjudication_notes.md"):
                self.assertEqual(files[f"repository/research/adjudication/{name}"],
                                 root / "research/adjudication" / name)
                self.assertEqual(files[f"repository/research/returns/{name}"],
                                 root / "research/adjudication" / name)
            self.assertEqual(files["repository/lean/README.md"], root / "lean/README.md")
            self.assertEqual(files["repository/tools/verify_examples.py"],
                             root / "tools/return_checks/verify_examples.py")

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
