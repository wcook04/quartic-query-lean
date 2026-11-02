import importlib.util
import json
import os
from pathlib import Path
import subprocess
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
    HASHES = {"lean/A.lean": "current-source-hash"}
    ROW = {"s": {"kind": "lemma", "statement": "x", "original_statement_sha256": None,
                 "corrected": False}}
    TIE = {"s": [{"declaration": "A.b", "kind": "theorem", "file": "f", "line": 1}]}

    def record(self, reviewed, runs):
        return MODULE.statement_records(self.ROW, self.TIE, reviewed, runs,
                                        hashes=self.HASHES)[0]["evidence"]

    def runs(self, declarations):
        return [{"kind": kind, "status": "passed", "declarations": declarations,
                 "source_hashes": self.HASHES}
                for kind in ("lean_build", "comparator")]

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
        runs = self.runs(["A.b"])
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
        runs = self.runs(["A.cond", "A.uncond"])
        evidence = MODULE.statement_records(self.ROW, ties, reviewed, runs,
                                            hashes=self.HASHES)[0]["evidence"]
        self.assertFalse(evidence["conditional"])

    def test_exact_theorem_with_ordinary_premises_is_not_conditional(self):
        reviewed = {"s": [{"declaration": "A.b", "relation": "exact", "route": "same",
                           "hypotheses": ["n > 0"], "premises": ["n > 0"],
                           "open_assumptions": []}]}
        records = MODULE.statement_records(self.ROW, self.TIE, reviewed, self.runs(["A.b"]),
                                           hashes=self.HASHES)
        record = records[0]
        self.assertEqual(record["lean"][0]["hypotheses"], ["n > 0"])
        self.assertEqual(record["lean"][0]["premises"], ["n > 0"])
        self.assertEqual(record["lean"][0]["open_assumptions"], [])
        self.assertFalse(record["evidence"]["conditional"])
        self.assertEqual(record["evidence"]["comparator"], "compared")
        self.assertEqual(MODULE.node_status(record), "unverified")
        graph = MODULE.evidence_graph(records, [], self.HASHES)
        node = graph["nodes"][0]
        metadata = next(e["receipt"] for e in graph["evidence"] if e["id"] == "tie_review_s")
        self.assertEqual(metadata["premises"], ["n > 0"])
        self.assertEqual(metadata["open_assumptions"], [])
        self.assertEqual(metadata["assumption_declaration"], "A.b")
        self.assertEqual(node["declaration"], "A.b")
        self.assertIn("Additional open assumptions: none", node["boundary"])
        self.assertIn("tie_review_s", node["evidence_ids"])
        self.assertNotIn("premises", node)
        self.assertEqual(node["status"], "unverified")
        self.assertIn("Informal statement projection", node["boundary"])

    def test_explicit_open_hardness_makes_exact_checked_theorem_conditional(self):
        reviewed = {"s": [{"declaration": "A.b", "relation": "exact", "route": "same",
                           "premises": ["k >= 2"], "open_assumptions": ["BansalSinhaLower"]}]}
        records = MODULE.statement_records(self.ROW, self.TIE, reviewed, self.runs(["A.b"]),
                                           hashes=self.HASHES)
        self.assertTrue(records[0]["evidence"]["conditional"])
        self.assertEqual(records[0]["evidence"]["premises"], ["k >= 2"])
        graph = MODULE.evidence_graph(records, [], self.HASHES)
        node = graph["nodes"][0]
        self.assertEqual(node["status"], "unverified")
        metadata = next(e["receipt"] for e in graph["evidence"] if e["id"] == "tie_review_s")
        self.assertEqual(metadata["open_assumptions"], ["BansalSinhaLower"])
        self.assertIn("Additional open assumptions: BansalSinhaLower", node["boundary"])

    def test_legacy_hypotheses_remain_open_without_explicit_classification(self):
        for fields in ({}, {"premises": ["n > 0"]}):
            with self.subTest(fields=fields):
                reviewed = {"s": [{"declaration": "A.b", "relation": "exact", "route": "same",
                                   "hypotheses": ["H"], **fields}]}
                record = MODULE.statement_records(self.ROW, self.TIE, reviewed, self.runs(["A.b"]),
                                                  hashes=self.HASHES)[0]
                self.assertTrue(record["evidence"]["conditional"])
                self.assertEqual(record["lean"][0]["open_assumptions"], ["H"])

    def test_tie_preference_uses_open_assumptions_rather_than_ordinary_premises(self):
        reviewed = {"s": [{"declaration": "A.open", "relation": "exact", "route": "same",
                           "open_assumptions": ["hardness"]},
                          {"declaration": "A.premise", "relation": "exact", "route": "alternative",
                           "hypotheses": ["n > 0"], "premises": ["n > 0"], "open_assumptions": []}]}
        record = MODULE.statement_records(self.ROW, {}, reviewed, self.runs(["A.open", "A.premise"]),
                                          hashes=self.HASHES)[0]
        self.assertFalse(record["evidence"]["conditional"])
        self.assertEqual(record["evidence"]["route"], "alternative")
        self.assertEqual(record["evidence"]["premises"], ["n > 0"])

    def test_assumption_fields_reject_null_or_nonlist_values(self):
        for field in ("hypotheses", "premises", "open_assumptions"):
            for value in (None, "H", [None]):
                with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                    MODULE.reviewed_assumptions({"declaration": "A.b", field: value})

    def test_unselected_assumption_metadata_is_unknown_not_an_empty_list(self):
        reviewed = {"s": [{"declaration": "A.b", "relation": "exact", "route": "same",
                           "premises": ["k >= 2"], "open_assumptions": ["hardness"]}]}
        records = MODULE.statement_records(self.ROW, self.TIE, reviewed, [], hashes=self.HASHES)
        self.assertEqual(records[0]["lean"][0]["open_assumptions"], ["hardness"])
        node = MODULE.evidence_graph(records, [], self.HASHES)["nodes"][0]
        for field in ("assumption_declaration", "premises", "open_assumptions"):
            self.assertNotIn(field, records[0]["evidence"])
            self.assertNotIn(field, node)
        self.assertNotIn("declaration", node)
        self.assertIn("Informal statement projection", node["boundary"])
        self.assertEqual(node["status"], "unverified")

    def test_changed_source_does_not_inherit_historical_pass(self):
        reviewed = {"s": [{"declaration": "A.b", "relation": "exact", "route": "same"}]}
        runs = self.runs(["A.b"])
        records = MODULE.statement_records(self.ROW, self.TIE, reviewed, runs,
                                           hashes={"lean/A.lean": "changed-source-hash"})
        self.assertFalse(records[0]["lean"][0]["built"])
        self.assertEqual(records[0]["lean"][0]["build_evidence"], "stale")
        self.assertEqual(records[0]["lean"][0]["comparison_evidence"], "stale")
        self.assertEqual(records[0]["evidence"]["comparator"], "not_run")
        self.assertEqual(runs[0]["status"], "passed")

    def test_legacy_receipt_is_explicitly_unbound(self):
        run = {"kind": "lean_build", "status": "passed", "declarations": ["A.b"]}
        record = MODULE.statement_records(self.ROW, self.TIE, {}, [run],
                                          hashes=self.HASHES)[0]
        self.assertEqual(record["lean"][0]["build_evidence"], "legacy_unbound")
        self.assertFalse(record["lean"][0]["built"])
        self.assertEqual(MODULE.currentness(run, self.HASHES), "legacy_unbound")

    def test_build_and_comparison_of_different_ties_do_not_combine(self):
        ties = {"s": [{"declaration": d, "kind": "theorem", "file": "f", "line": 1}
                      for d in ("A.built", "A.compared")]}
        reviewed = {"s": [{"declaration": d, "relation": "exact", "route": "same"}
                          for d in ("A.built", "A.compared")]}
        runs = self.runs([])
        runs[0]["declarations"] = ["A.built"]
        runs[1]["declarations"] = ["A.compared"]
        record = MODULE.statement_records(self.ROW, ties, reviewed, runs,
                                          hashes=self.HASHES)[0]
        self.assertEqual(record["evidence"]["build"], "built_at_pin")
        self.assertEqual(record["evidence"]["comparator"], "not_run")
        self.assertEqual(MODULE.node_status(record), "unverified")

    def test_comparison_of_partial_tie_does_not_check_exact_tie(self):
        reviewed = {"s": [{"declaration": "A.b", "relation": "exact", "route": "same"},
                          {"declaration": "A.partial", "relation": "partial", "route": "same"}]}
        runs = self.runs(["A.b", "A.partial"])
        runs[1]["declarations"] = ["A.partial"]
        self.assertEqual(self.record(reviewed, runs)["comparator"], "not_run")

    def test_stale_reach_is_not_reported_as_current_membership(self):
        record = MODULE.statement_records(self.ROW, self.TIE, {}, [], {"A.b"},
                                          self.HASHES, "stale")[0]
        self.assertIsNone(record["lean"][0]["reached"])
        self.assertEqual(record["evidence"]["reach"], "stale")

    def test_graph_keeps_historical_pass_separate_from_currentness(self):
        run = {"kind": "lean_build", "status": "passed", "declarations": ["A.b"],
               "command": ["lake", "build"], "tool": "historical local run"}
        records = MODULE.statement_records(self.ROW, self.TIE, {}, [run], hashes=self.HASHES)
        graph = MODULE.evidence_graph(records, [run], self.HASHES)
        historical = next(e for e in graph["evidence"] if e["id"] == "run_0")
        self.assertEqual(historical["status"], "not_run")
        self.assertEqual(historical["receipt"]["operation"]["status"], "passed")
        self.assertEqual(historical["receipt"]["currentness"], "legacy_unbound")
        self.assertNotIn("currentness", historical)
        self.assertEqual(graph["nodes"][0]["status"], "unverified")


class SourceSnapshotTests(unittest.TestCase):
    def test_source_edits_additions_and_removals_invalidate_receipt(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            lean = root / "lean"
            lean.mkdir()
            source = lean / "A.lean"
            source.write_text("theorem a : True := trivial\n")
            (lean / "lean-toolchain").write_text("pinned-version")
            snapshot = MODULE.source_hashes(root)
            run = {"source_hashes": snapshot}
            self.assertEqual(MODULE.currentness(run, MODULE.source_hashes(root)), "current")
            source.write_text("theorem a : False := by sorry\n")
            self.assertEqual(MODULE.currentness(run, MODULE.source_hashes(root)), "stale")
            source.write_text("theorem a : True := trivial\n")
            extra = lean / "B.lean"
            extra.write_text("def b := 1\n")
            self.assertEqual(MODULE.currentness(run, MODULE.source_hashes(root)), "stale")
            extra.unlink()
            self.assertEqual(MODULE.currentness(run, MODULE.source_hashes(root)), "current")
            source.unlink()
            self.assertEqual(MODULE.currentness(run, MODULE.source_hashes(root)), "stale")

    def test_build_cache_is_excluded_but_comparator_config_is_bound(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            cache = root / "lean/.lake/packages/dependency"
            cache.mkdir(parents=True)
            (cache / "Ignored.lean").write_text("ignored dependency bytes")
            config = root / "lean/QuarticCorpus/Bundle/comparator.json"
            config.parent.mkdir(parents=True)
            config.write_text("{}")
            self.assertEqual(set(MODULE.source_hashes(root)),
                             {"lean/QuarticCorpus/Bundle/comparator.json"})


@unittest.skipUnless(os.environ.get("QUARTIC_LEAN_EXPOSITION"),
                     "set QUARTIC_LEAN_EXPOSITION to an installed lean-exposition CLI")
class ConsumerContractTests(unittest.TestCase):
    def test_current_positive_statement_graph_validates_and_selects_its_prerequisites(self):
        hashes = {"lean/A.lean": "a" * 64}
        ledger = {ident: {"kind": "theorem", "statement": statement,
                          "original_statement_sha256": None, "corrected": False,
                          "depends_on": depends}
                  for ident, statement, depends in (
                      ("thm-1.1", "For every n > 0, n = n", ["middle"]),
                      ("middle", "The intermediate prerequisite", ["leaf"]),
                      ("leaf", "The terminal prerequisite", []),
                      ("unrelated", "An unrelated statement", []))}
        reviewed = {"thm-1.1": [{"declaration": "A.b", "relation": "exact", "route": "same",
                                 "premises": ["n > 0"], "open_assumptions": []}]}
        runs = [{"kind": kind, "status": "passed", "declarations": ["A.b"],
                 "source_hashes": hashes, "command": ["lake", "fixture"], "tool": "mock local operation"}
                for kind in ("lean_build", "comparator")]
        records = MODULE.statement_records(ledger, {}, reviewed, runs, hashes=hashes)
        self.assertEqual(records[0]["evidence"]["comparator"], "compared")
        graph = MODULE.evidence_graph(records, runs, hashes)
        self.assertTrue(all(node["status"] == "unverified" for node in graph["nodes"]))
        cli = os.environ["QUARTIC_LEAN_EXPOSITION"]

        def invoke(*args):
            checked = subprocess.run([cli, *map(str, args)], capture_output=True, text=True, timeout=30)
            self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
            return checked.stdout

        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "graph.json"
            selected = Path(folder) / "selected.json"
            path.write_text(json.dumps(graph))
            invoke("validate", path)  # schema and contracts.validate_graph
            invoke("select", path, "--goal", "thm-1.1", "--out", selected)
            result = json.loads(selected.read_text())
            # select preserves the recorded corpus and changes active goals;
            # inspect computes the selected prerequisite closure.
            self.assertEqual(result["selected_goals"], ["thm-1.1"])
            self.assertEqual({node["id"] for node in result["nodes"]}, set(ledger))
            self.assertEqual({(edge["from"], edge["to"]) for edge in result["edges"]},
                             {("thm-1.1", "middle"), ("middle", "leaf")})
            self.assertTrue({"run_0", "run_1", "tie_review_thm-1.1"}
                            <= {item["id"] for item in result["evidence"]})
            self.assertTrue(all(item["kind"] == "semantic_review" and item["status"] == "not_run"
                                for item in result["evidence"] if item["id"].startswith("run_")))
            summary = json.loads(invoke("inspect", selected))
            self.assertEqual(set(summary["argument_closure"]), {"thm-1.1", "middle", "leaf"})
            inspected = invoke("inspect", selected, "--goal", "thm-1.1", "--view", "arguments")
            self.assertIn("middle", inspected)
            self.assertIn("leaf", inspected)
            self.assertNotIn("unrelated", inspected)


if __name__ == "__main__":
    unittest.main()
