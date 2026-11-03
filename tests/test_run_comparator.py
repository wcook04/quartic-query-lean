"""Receipt-subject regression tests; these do not execute Lean or Comparator."""

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
SPEC = importlib.util.spec_from_file_location("run_comparator", TOOLS / "run_comparator.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ComparisonSubjects(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.config = self.directory / "comparator.json"
        self.config.write_text(json.dumps({"theorem_names": ["Checked.truth"]}), encoding="utf-8")

    def solution(self, content):
        (self.directory / "Solution.lean").write_text(content, encoding="utf-8")

    def test_comment_does_not_create_compared_subject(self):
        self.solution("/-\n  exact QuarticQuery.notActuallyCompared\n-/\n"
                      "theorem Checked.truth : True := by trivial\n")
        self.assertEqual(MODULE.compared_declarations(self.config), ["Checked.truth"])

    def test_unrelated_helper_does_not_create_compared_subject(self):
        self.solution("theorem auxiliary : True := by\n  exact QuarticQuery.helper\n"
                      "theorem Checked.truth : True := by trivial\n")
        self.assertEqual(MODULE.compared_declarations(self.config), ["Checked.truth"])

    def test_specialization_is_not_source_theorem_comparison(self):
        self.solution("theorem Checked.truth : 0 = 0 := by\n"
                      "  exact QuarticQuery.general_equality 0\n")
        self.assertEqual(MODULE.compared_declarations(self.config), ["Checked.truth"])

    def test_direct_configured_target_needs_no_proof_text_scan(self):
        self.config.write_text(json.dumps({"theorem_names": ["QuarticQuery.target"]}), encoding="utf-8")
        self.assertEqual(MODULE.compared_declarations(self.config), ["QuarticQuery.target"])

    def test_definition_targets_are_not_theorem_comparison_subjects(self):
        self.config.write_text(json.dumps({"theorem_names": [], "definition_names": ["A.f"]}), encoding="utf-8")
        self.assertEqual(MODULE.compared_declarations(self.config), [])

    def test_invalid_or_duplicate_names_fail(self):
        for names in ["A.x", [None], [""], ["  "], ["A.x", "A.x"]]:
            with self.subTest(names=names):
                self.config.write_text(json.dumps({"theorem_names": names}), encoding="utf-8")
                with self.assertRaises(ValueError):
                    MODULE.compared_declarations(self.config)

    def test_passing_receipt_contains_only_configured_subjects(self):
        self.solution("/-\n exact QuarticQuery.unrelated\n-/\n")
        captured = []
        hashes = {"lean/A.lean": "0" * 64}
        with patch.object(MODULE, "source_hashes", return_value=hashes), \
                patch.object(MODULE, "comparator", return_value=(["lake", "comparator"], 0, "ok")), \
                patch.object(MODULE, "stamp", side_effect=lambda name, command, status, log, extra:
                             {"name": name, "status": status, **extra}), \
                patch.object(MODULE, "write", side_effect=captured.append):
            self.assertTrue(MODULE.run_bundle(self.config, False))
        self.assertEqual(captured[0]["declarations"], ["Checked.truth"])
        self.assertEqual(captured[0]["declaration_scope"], "configured_theorem_names_only")


if __name__ == "__main__":
    unittest.main()
