import importlib.util
from pathlib import Path
import tempfile
import unittest


PATH = Path(__file__).resolve().parents[1] / "tools/build_corpus.py"
SPEC = importlib.util.spec_from_file_location("build_corpus", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

SOURCE = """namespace Top

section Inner
variable (n : Nat)
end Inner

/-- Ledger: thm-1.1. A sentence with a dot. -/
theorem first : True := trivial

namespace Deep

/-- Ledger: lem-2.2.i, claim-winner-fidelity. Two rows. -/
theorem second : True := trivial

end Deep

/-- Ledger: def-K -/
def third : Nat := 0

end Top
"""


def ties(text):
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        (root / "A.lean").write_text(text, encoding="utf-8")
        original, MODULE.ROOT = MODULE.ROOT, root
        try:
            return MODULE.declared_ties(root)
        finally:
            MODULE.ROOT = original


class TieTests(unittest.TestCase):
    def test_ids_keep_their_dots(self):
        self.assertEqual(MODULE.tie_ids("thm-1.1. The theorem", 0), ["thm-1.1"])
        self.assertEqual(MODULE.tie_ids("lem-2.2.i, eq-14 rest", 0), ["lem-2.2.i", "eq-14"])

    def test_declarations_get_their_namespace_after_a_section_ends(self):
        found = ties(SOURCE)
        self.assertEqual(found["thm-1.1"][0]["declaration"], "Top.first")
        self.assertEqual(found["lem-2.2.i"][0]["declaration"], "Top.Deep.second")
        self.assertEqual(found["claim-winner-fidelity"][0]["declaration"], "Top.Deep.second")
        self.assertEqual(found["def-K"][0]["declaration"], "Top.third")


class EvidenceTests(unittest.TestCase):
    ROW = {"s": {"kind": "lemma", "statement": "x", "original_statement_sha256": None,
                 "corrected": False}}
    TIE = {"s": [{"declaration": "A.b", "kind": "theorem", "file": "f", "line": 1}]}

    def record(self, reviewed, runs):
        return MODULE.statement_records(self.ROW, self.TIE, reviewed, runs)[0]["evidence"]

    def test_presence_alone_is_unassessed_and_unbuilt(self):
        evidence = self.record({}, [])
        self.assertEqual(evidence["formal_statement"], "unassessed")
        self.assertEqual(evidence["build"], "not_run")
        self.assertEqual(evidence["comparator"], "not_run")

    def test_review_without_a_receipt_is_not_compared(self):
        reviewed = {"s": [{"declaration": "A.b", "relation": "exact", "route": "same"}]}
        self.assertEqual(self.record(reviewed, [])["comparator"], "not_run")

    def test_review_and_receipts_give_a_checked_statement(self):
        reviewed = {"s": [{"declaration": "A.b", "relation": "exact", "route": "same"}]}
        runs = [{"kind": kind, "status": "passed", "declarations": ["A.b"]}
                for kind in ("lean_build", "comparator")]
        self.assertEqual(self.record(reviewed, runs)["comparator"], "compared")

    def test_failed_receipt_counts_for_nothing(self):
        reviewed = {"s": [{"declaration": "A.b", "relation": "exact", "route": "same"}]}
        runs = [{"kind": "comparator", "status": "failed", "declarations": ["A.b"]}]
        self.assertEqual(self.record(reviewed, runs)["comparator"], "not_run")

    def test_unconditional_compared_tie_is_preferred(self):
        ties = {"s": [{"declaration": d, "kind": "theorem", "file": "f", "line": 1}
                      for d in ("A.cond", "A.uncond")]}
        reviewed = {"s": [{"declaration": "A.cond", "relation": "exact", "route": "same",
                           "hypotheses": ["H"]},
                          {"declaration": "A.uncond", "relation": "exact", "route": "same"}]}
        runs = [{"kind": kind, "status": "passed", "declarations": ["A.cond", "A.uncond"]}
                for kind in ("lean_build", "comparator")]
        evidence = MODULE.statement_records(self.ROW, ties, reviewed, runs)[0]["evidence"]
        self.assertFalse(evidence["conditional"])


if __name__ == "__main__":
    unittest.main()
