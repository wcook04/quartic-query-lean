import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


PATH = Path(__file__).resolve().parents[1] / "tools/build_round2_packets.py"
SPEC = importlib.util.spec_from_file_location("round2", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RoundTwoTests(unittest.TestCase):
    def evidence_fixture(self, root, bound=False):
        source = root / "lean/QuarticQuery/A.lean"
        source.parent.mkdir(parents=True)
        source.write_text("theorem a : True := trivial\n")
        (root / "corpus/receipts").mkdir(parents=True)
        deps = {"roots": ["A.root"], "reached": ["A.reached"]}
        receipt = {"commit": "historical-commit", "status": "passed"}
        if bound:
            deps["source_hashes"] = MODULE.corpus_evidence.source_hashes(root)
            receipt["source_hashes"] = deps["source_hashes"]
        (root / "corpus/lean_dependencies.json").write_text(json.dumps(deps))
        (root / "corpus/receipts/lean-build-root.json").write_text(json.dumps(receipt))
        rows = [{"id": "s", "kind": "lemma", "section": 1,
                 "lean": [{"declaration": name, "file": "lean/QuarticQuery/A.lean"}
                          for name in ("A.reached", "A.other")], "evidence": {}}]
        (root / "corpus/statements.json").write_text(json.dumps(rows))
        return source

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

    def test_legacy_and_stale_skeleton_do_not_assert_current_reach(self):
        for bound, expected in ((False, "legacy_unbound"), (True, "stale")):
            with self.subTest(bound=bound), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                source = self.evidence_fixture(root, bound)
                if bound:
                    source.write_text("theorem a : False := by sorry\n")
                text = MODULE.record_skeleton(root).decode()
                self.assertIn(f"Dependency-export source currentness: `{expected}`", text)
                self.assertIn(f"recorded reached; current reach unknown ({expected})", text)
                self.assertIn(f"not recorded reached; current reach unknown ({expected})", text)
                self.assertNotIn("outside the current headline closure", text)

    def test_current_skeleton_labels_current_membership_only_when_bound(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.evidence_fixture(root, bound=True)
            text = MODULE.record_skeleton(root).decode()
            self.assertIn("Dependency-export source currentness: `current`", text)
            self.assertIn("`A.reached` (reached)", text)
            self.assertIn("`A.other` (outside the current headline closure)", text)

    def test_build_status_distinguishes_artifact_mtime_from_source_bound_evidence(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.evidence_fixture(root)
            artifact = root / "lean/.lake/build/lib/lean/QuarticQuery/A.olean"
            artifact.parent.mkdir(parents=True)
            artifact.write_bytes(b"old artifact with newer mtime")
            text = MODULE.build_status(root).decode()
            self.assertIn("source currentness `legacy_unbound`", text)
            self.assertIn("does not bind its contents to the current source bytes", text)
            self.assertIn(".olean artifact exists", text)
            self.assertIn("| `QuarticQuery/A.lean` | yes | yes |", text)

    @unittest.skipUnless(MODULE.ANNEXES.is_dir(), "annex checkout not present")
    def test_priority_literature_exists_when_annexes_are_present(self):
        for job in MODULE.JOBS:
            MODULE.literature(job)


if __name__ == "__main__":
    unittest.main()
