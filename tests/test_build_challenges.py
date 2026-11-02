import importlib.util
from pathlib import Path
import unittest


PATH = Path(__file__).resolve().parents[1] / "tools/build_challenges.py"
SPEC = importlib.util.spec_from_file_location("build_challenges", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

SOLUTION = """module

public import QuarticQuery.Statement
import QuarticQuery.Tournament.Drift

namespace QuarticQuery.Checked

-- CHALLENGE-BEGIN
open Finset

/-- Doc. -/
theorem first (n : Nat) : n = n := by
  -- proof
  exact secret n
  rfl

theorem second : True := by
  -- proof
  trivial
-- CHALLENGE-END

end QuarticQuery.Checked
"""


class ChallengeTests(unittest.TestCase):
    def test_region_keeps_statements_and_drops_proofs(self):
        region = MODULE.challenge_region(SOLUTION)
        self.assertIn("theorem first (n : Nat) : n = n := by\n  sorry", region)
        self.assertIn("theorem second : True := by\n  sorry", region)
        self.assertIn("/-- Doc. -/", region)
        self.assertNotIn("secret", region)
        self.assertNotIn("trivial", region)

    def test_challenge_imports_mathlib_only(self):
        statement = "module\n\npublic import Mathlib\n\n@[expose] public section\n\nnamespace Q\nend Q\n"
        text = MODULE.challenge_text(statement, SOLUTION)
        self.assertIn("public import Mathlib", text)
        self.assertNotIn("QuarticQuery.Statement", text)
        self.assertNotIn("Drift", text)

    def test_theorem_names_are_qualified(self):
        self.assertEqual(MODULE.theorem_names(SOLUTION),
                         ["QuarticQuery.Checked.first", "QuarticQuery.Checked.second"])

    def test_missing_markers_are_rejected(self):
        with self.assertRaises(ValueError):
            MODULE.challenge_region("theorem x : True := trivial\n")

    def test_region_without_a_proof_marker_is_rejected(self):
        text = "-- CHALLENGE-BEGIN\ntheorem x : True := trivial\n-- CHALLENGE-END\n"
        with self.assertRaises(ValueError):
            MODULE.challenge_region(text)


if __name__ == "__main__":
    unittest.main()
