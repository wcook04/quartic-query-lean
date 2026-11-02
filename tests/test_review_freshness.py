"""Acceptance regressions for the two remaining source-evidence boundaries.

All operation receipts in these tests are explicit Python mocks. A passing
test is not a Lean build, Comparator run, or native extraction.
"""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


PATH = Path(__file__).resolve().parents[1] / "tools/build_corpus.py"
SPEC = importlib.util.spec_from_file_location("review_build_corpus", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ReviewFreshnessTests(unittest.TestCase):
    def setUp(self):
        self.ledger = {"s": {"kind": "lemma", "statement": "Zero satisfies the equality-to-zero predicate.",
                             "original_statement_sha256": None, "corrected": False,
                             "depends_on": []}}
        self.hashes = {"lean/Definition.lean": "a" * 64, "lean/Theorem.lean": "b" * 64,
                       "lean/lean-toolchain": "c" * 64}
        self.review = {"declaration": "A.permits_zero", "relation": "exact", "route": "same",
                       "premises": ["n is natural"], "open_assumptions": [],
                       "reviewed_by": "synthetic regression fixture"}
        self.review["review_binding"] = MODULE.expected_review_binding(
            "s", self.ledger["s"], self.review, self.hashes)

    def record(self, review=None, hashes=None, ledger=None, declarations=None):
        hashes = self.hashes if hashes is None else hashes
        review = self.review if review is None else review
        ledger = self.ledger if ledger is None else ledger
        declarations = [review["declaration"]] if declarations is None else declarations
        runs = [{"kind": kind, "status": "passed", "declarations": declarations,
                 "source_hashes": deepcopy(hashes), "command": ["mock", kind]}
                for kind in ("lean_build", "comparator")]
        reviewed = {ident: [review] for ident in ledger}
        return MODULE.statement_records(ledger, {}, reviewed, runs, hashes=hashes)[0]

    def assert_review_withheld(self, record, state="stale"):
        self.assertEqual(record["lean"][0]["review_evidence"], state)
        self.assertEqual(record["lean"][0]["reviewed_relation"], "exact")
        self.assertEqual(record["lean"][0]["relation"], "unassessed")
        self.assertEqual(record["evidence"]["formal_statement"], "unassessed")
        self.assertEqual(record["evidence"]["comparator"], "not_run")
        self.assertNotIn("assumption_declaration", record["evidence"])
        # Actual operation facts and semantic-review freshness are independent.
        self.assertTrue(record["lean"][0]["built"])
        self.assertTrue(record["lean"][0]["compared"])

    def test_bound_review_and_matching_receipts_keep_current_statement_credit(self):
        record = self.record()
        self.assertEqual(record["lean"][0]["review_evidence"], "current")
        self.assertEqual(record["evidence"]["formal_statement"], "exact")
        self.assertEqual(record["evidence"]["comparator"], "compared")
        self.assertEqual(record["evidence"]["premises"], ["n is natural"])
        self.assertEqual(record["evidence"]["open_assumptions"], [])
        self.assertFalse(record["evidence"]["conditional"])

    def test_current_build_and_comparison_cannot_attest_a_legacy_review(self):
        review = deepcopy(self.review)
        del review["review_binding"]
        before = deepcopy(review)
        self.assert_review_withheld(self.record(review), "legacy_unbound")
        self.assertEqual(review, before)
        self.assertNotIn("review_binding", review)

    def test_graph_retains_historical_ties_without_selecting_a_stale_review(self):
        for state in ("stale", "legacy_unbound"):
            review = deepcopy(self.review)
            if state == "stale":
                review["note"] = "Changed classification context"
            else:
                del review["review_binding"]
            record = self.record(review)
            graph = MODULE.evidence_graph([record], [], self.hashes)
            node = graph["nodes"][0]
            self.assertNotIn("declaration", node)
            self.assertEqual(node["status"], "unverified")
            metadata = next(e for e in graph["evidence"] if e["id"] == "tie_review_s")
            self.assertIn(metadata["id"], node["evidence_ids"])
            self.assertEqual(metadata["status"], "not_run")
            self.assertEqual(metadata["receipt"]["ties"], record["lean"])
            self.assertEqual(metadata["receipt"]["ties"][0]["review_evidence"], state)
            self.assertNotIn("assumption_declaration", metadata["receipt"])

    def test_definition_edit_with_unchanged_theorem_source_and_fresh_runs_stays_stale(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            lean = root / "lean"
            lean.mkdir()
            definition = lean / "Definition.lean"
            theorem = lean / "Theorem.lean"
            definition.write_text("def Allowed (n : Nat) : Prop := n = 0\n")
            theorem.write_text("import Definition\n"
                               "theorem permits_zero : Allowed 0 := by simp [Allowed]\n")
            before = MODULE.source_hashes(root)
            review = deepcopy(self.review)
            review["review_binding"] = MODULE.expected_review_binding(
                "s", self.ledger["s"], review, before)
            theorem_bytes = theorem.read_bytes()
            definition.write_text("def Allowed (n : Nat) : Prop := n ≤ 1\n")
            after = MODULE.source_hashes(root)
            self.assertEqual(theorem.read_bytes(), theorem_bytes)
            self.assertNotEqual(before, after)
            record = self.record(review, after)  # fresh mock passes on changed bytes
            self.assert_review_withheld(record)
            self.assertEqual(record["lean"][0]["build_evidence"], "current")
            self.assertEqual(record["lean"][0]["comparison_evidence"], "current")
            # Only an explicit renewed review may restore alignment credit.
            review["review_binding"] = MODULE.expected_review_binding(
                "s", self.ledger["s"], review, after)
            self.assertEqual(self.record(review, after)["evidence"]["comparator"], "compared")

    def test_source_addition_removal_pin_change_and_proof_change_all_invalidate(self):
        variants = [
            {**self.hashes, "lean/New.lean": "d" * 64},
            {key: value for key, value in self.hashes.items() if key != "lean/Definition.lean"},
            {**self.hashes, "lean/lean-toolchain": "d" * 64},
            {**self.hashes, "lean/Theorem.lean": "e" * 64},
        ]
        for hashes in variants:
            with self.subTest(hashes=hashes):
                self.assert_review_withheld(self.record(hashes=hashes))

    def test_changed_statement_or_context_does_not_inherit_old_review(self):
        for field, value in (("statement", "Every value satisfies the predicate."),
                             ("depends_on", ["new-definition"]), ("section", "new source")):
            ledger = deepcopy(self.ledger)
            ledger["s"][field] = value
            with self.subTest(field=field):
                self.assert_review_withheld(self.record(ledger=ledger))

    def test_changed_declaration_row_identity_or_judgment_requires_new_review(self):
        for field, value in (("declaration", "A.other"), ("route", "alternative"),
                             ("premises", []), ("open_assumptions", ["new hardness"]),
                             ("reviewed_by", "different reviewer")):
            review = deepcopy(self.review)
            review[field] = value
            with self.subTest(field=field):
                self.assert_review_withheld(self.record(review))
        review = deepcopy(self.review)
        review["relation"] = "stronger"
        record = self.record(review)
        self.assertEqual(record["lean"][0]["review_evidence"], "stale")
        self.assertEqual(record["lean"][0]["reviewed_relation"], "stronger")
        self.assertEqual(record["evidence"]["formal_statement"], "unassessed")
        ledger = {"renamed": deepcopy(self.ledger["s"])}
        self.assert_review_withheld(self.record(ledger=ledger))

    def test_malformed_or_partial_binding_fails_closed(self):
        for binding in (None, {}, {"schema": MODULE.REVIEW_SCHEMA},
                        {**self.review["review_binding"], "schema": "unknown"},
                        {**self.review["review_binding"], "source_snapshot_sha256": "not-a-hash"}):
            review = {**self.review, "review_binding": binding}
            with self.subTest(binding=binding), self.assertRaisesRegex(ValueError, "malformed review_binding"):
                self.record(review)

    def test_fresh_review_alone_does_not_supply_build_or_comparison_evidence(self):
        records = MODULE.statement_records(self.ledger, {}, {"s": [self.review]}, [], hashes=self.hashes)
        self.assertEqual(records[0]["evidence"]["review"], "current")
        self.assertEqual(records[0]["evidence"]["formal_statement"], "exact")
        self.assertEqual(records[0]["evidence"]["build"], "not_run")
        self.assertEqual(records[0]["evidence"]["comparator"], "not_run")


class DerivedProvenanceTests(unittest.TestCase):
    def row(self, ident="s", **extra):
        return {"id": ident, "kind": "claim", "statement": "A separately derived helper.",
                "original_statement_sha256": None, "corrected": False, "depends_on": [], **extra}

    def test_r2_live_helper_is_withheld_even_if_assigned_a_preprint_source(self):
        for source in ({}, {"source_id": "openai_preprint"}, {"source_id": "derived_research"}):
            row = self.row("r2-live-helper", **source)
            with self.subTest(source=source), self.assertRaisesRegex(ValueError, "withheld"):
                MODULE.statement_records({row["id"]: row}, {}, {}, [], hashes={})
            with self.subTest(source=source), self.assertRaisesRegex(ValueError, "withheld"):
                MODULE.evidence_graph([row], [], hashes={})

    def test_nonpreprint_source_is_never_silently_overwritten(self):
        row = self.row("separately-derived", source_id="derived_research")
        with self.assertRaisesRegex(ValueError, "withheld"):
            MODULE.statement_records({row["id"]: row}, {}, {}, [], hashes={})
        with self.assertRaisesRegex(ValueError, "withheld"):
            MODULE.evidence_graph([row], [], hashes={})

    def test_missing_helper_dependency_is_not_silently_dropped(self):
        row = self.row(depends_on=["r2-live-helper"])
        records = MODULE.statement_records({row["id"]: row}, {}, {}, [], hashes={})
        self.assertEqual(records[0]["depends_on"], ["r2-live-helper"])
        with self.assertRaisesRegex(ValueError, "missing prerequisite rows: r2-live-helper"):
            MODULE.evidence_graph(records, [], hashes={})


if __name__ == "__main__":
    unittest.main()
