"""Evidence producer contracts; optional tiny Lean traversal regression.

QUARTIC_TEST_LEAN=1 enables a Lean-only fixture with the pinned toolchain. It
elaborates the actual Reach implementation without importing/building the proof
library. Ordinary Python discovery mocks external build/comparison commands.
"""

import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, TOOLS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(TOOLS))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.pop(0)
    return module


RECORD = load_script("record_evidence")
COMPARATOR = load_script("run_comparator")


def result(output="", code=0):
    return SimpleNamespace(returncode=code, stdout=output, stderr="")


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        lean = self.root / "lean"
        lean.mkdir()
        (lean / "lean-toolchain").write_text("test-toolchain")
        corpus = self.root / "corpus"
        (corpus / "receipts").mkdir(parents=True)
        self.old = corpus / "receipts/lean-build-root.json"
        self.old.write_text('{"status":"passed","historical":true}\n')
        self.hashes = {"lean/A.lean": "source-hash"}
        for name, value in {"ROOT": self.root, "LEAN": lean, "CORPUS": corpus}.items():
            mock = patch.object(RECORD, name, value)
            mock.start()
            self.addCleanup(mock.stop)

    def closure(self, **extra):
        return json.dumps({"declared": RECORD.ROOTS, "reached": RECORD.ROOTS,
                           "edges": {}, "unresolved_constants": [], **extra})

    def test_success_builds_before_inspection_and_preserves_old_receipt(self):
        with patch.object(RECORD, "source_hashes", return_value=self.hashes), \
                patch.object(RECORD.subprocess, "run", side_effect=[
                    result("build passed"), result(self.closure()), result("commit-id\n")]) as run:
            self.assertEqual(RECORD.main(), 0)
        self.assertEqual(run.call_args_list[0].args[0][1:], ["build", "QuarticQuery"])
        self.assertIn("scripts/Reach.lean", run.call_args_list[1].args[0])
        paths = list(self.old.parent.glob("lean-build-root-*.json"))
        self.assertEqual(len(paths), 1)
        receipt = json.loads(paths[0].read_text())
        self.assertEqual(receipt["source_hashes"], self.hashes)
        self.assertEqual(receipt["command"], ["lake", "build", "QuarticQuery"])
        self.assertEqual(json.loads(self.old.read_text()), {"status": "passed", "historical": True})
        self.assertEqual(json.loads((self.root / "corpus/lean_dependencies.json").read_text())
                         ["source_hashes"], self.hashes)

    def test_failed_build_never_reads_stale_olean_or_writes_evidence(self):
        with patch.object(RECORD, "source_hashes", return_value=self.hashes), \
                patch.object(RECORD.subprocess, "run", return_value=result("build failed", 1)) as run:
            self.assertEqual(RECORD.main(), 1)
        self.assertEqual(run.call_count, 1)
        self.assertFalse((self.root / "corpus/lean_dependencies.json").exists())
        self.assertEqual(list(self.old.parent.glob("*.json")), [self.old])

    def test_source_change_during_build_cannot_record_pass(self):
        with patch.object(RECORD, "source_hashes", side_effect=[self.hashes, {"lean/A.lean": "new"}]), \
                patch.object(RECORD.subprocess, "run", side_effect=[result(), result(self.closure())]):
            self.assertEqual(RECORD.main(), 1)
        self.assertFalse((self.root / "corpus/lean_dependencies.json").exists())

    def test_missing_root_or_unresolved_constant_cannot_record_pass(self):
        for extra in ({"declared": []}, {"unresolved_constants": ["Missing.constant"]}):
            with self.subTest(extra=extra), \
                    patch.object(RECORD, "source_hashes", return_value=self.hashes), \
                    patch.object(RECORD.subprocess, "run", side_effect=[
                        result(), result(self.closure(**extra))]):
                self.assertEqual(RECORD.main(), 1)
        self.assertFalse((self.root / "corpus/lean_dependencies.json").exists())


class ComparatorTests(unittest.TestCase):
    def test_guard_deferral_writes_no_receipt(self):
        with patch.object(COMPARATOR, "source_hashes", return_value={"a": "same"}), \
                patch.object(COMPARATOR, "comparator", return_value=(["lake", "comparator"], 75, "queued")), \
                patch.object(COMPARATOR, "write") as write:
            self.assertFalse(COMPARATOR.run_bundle(Path("Bundle/comparator.json"), False))
            self.assertFalse(COMPARATOR.run_negative(Path("WeakenedConclusion.json")))
        write.assert_not_called()

    def test_changed_sources_invalidate_successful_comparison(self):
        config = Path("Bundle/comparator.json")
        with patch.object(COMPARATOR, "source_hashes", side_effect=[{"a": "before"}, {"a": "after"}]), \
                patch.object(COMPARATOR, "comparator", return_value=(["lake", "comparator"], 0, "ok")), \
                patch.object(COMPARATOR, "wrapped", return_value=["A.checked"]), \
                patch.object(COMPARATOR, "git_head", return_value="commit-id"), \
                patch.object(COMPARATOR, "stamp", side_effect=lambda n, c, s, l, extra: {"status": s, **extra}), \
                patch.object(COMPARATOR, "write") as write:
            self.assertFalse(COMPARATOR.run_bundle(config, False))
        self.assertEqual(write.call_args.args[0]["status"], "failed")
        self.assertTrue(write.call_args.args[0]["source_changed_during_run"])

    def test_new_comparison_receipt_does_not_replace_historical_file(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(COMPARATOR, "RECEIPTS", Path(folder)):
            old = Path(folder) / "comparator-Bundle.json"
            old.write_text("historical bytes")
            COMPARATOR.write({"name": "Bundle", "ran_at": "2026-11-02T12:00:00.123456+00:00"})
            self.assertEqual(old.read_text(), "historical bytes")
            self.assertEqual(len(list(Path(folder).glob("*.json"))), 2)


@unittest.skipUnless(os.environ.get("QUARTIC_TEST_LEAN") == "1", "set QUARTIC_TEST_LEAN=1 for Lean-only fixture")
class ReachTests(unittest.TestCase):
    def test_public_leaf_is_reached_through_private_and_other_namespace_wrappers(self):
        implementation = (ROOT / "lean/scripts/Reach.lean").read_text()
        # Adapted from the preserved round-two statement-fidelity return's
        # ReachPrivateFixture.lean; also checks a non-QuarticQuery intermediary.
        fixture = """
namespace QuarticQuery.ReachRegression
theorem publicLeaf : (1 : Nat) = 1 := rfl
private theorem privateWrapper : (1 : Nat) = 1 := by exact publicLeaf
theorem publicRoot : (1 : Nat) = 1 := by exact privateWrapper
end QuarticQuery.ReachRegression
namespace OtherNamespace
theorem wrapper : (1 : Nat) = 1 := by exact QuarticQuery.ReachRegression.publicLeaf
end OtherNamespace
namespace QuarticQuery.ReachRegression
theorem viaOtherNamespace : (1 : Nat) = 1 := by exact OtherNamespace.wrapper
end QuarticQuery.ReachRegression
open Lean Elab Command in
run_elab do
  let env ← getEnv
  let leaf := ``QuarticQuery.ReachRegression.publicLeaf
  for root in [``QuarticQuery.ReachRegression.publicRoot,
               ``QuarticQuery.ReachRegression.viaOtherNamespace] do
    let found := inspectClosure env #[root]
    unless found.publicNames.contains leaf do
      throwError "public leaf lost through hidden wrapper"
    unless found.edges.any (fun (source, targets) => source == root && targets.contains leaf) do
      throwError "projected edge through hidden wrapper lost"
    unless found.hiddenPaths.any (fun (source, paths) => source == root &&
        paths.any (fun (target, via) => target == leaf && !via.isEmpty)) do
      throwError "hidden path provenance lost"
    unless found.unresolved.isEmpty do
      throwError "unexpected unresolved constant"
  let missing := inspectClosure env #[`DoesNotExist]
  unless missing.unresolved == #[`DoesNotExist] do
    throwError "missing root not reported"
"""
        folder = Path(tempfile.mkdtemp(prefix="quartic-reach-regression-"))
        keep = False
        try:
            path = folder / "ReachRegression.lean"
            path.write_text(implementation + fixture)
            lean = os.environ.get("LEAN", str(Path.home() / ".elan/bin/lean"))
            checked = subprocess.run([lean, str(path)], cwd=ROOT / "lean", capture_output=True,
                                     text=True, timeout=60)
            if checked.returncode == 75:
                keep = True
                self.skipTest(f"Lean guard deferred compilation; queued input retained at {path}")
            self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
        finally:
            if not keep:
                shutil.rmtree(folder)


if __name__ == "__main__":
    unittest.main()
