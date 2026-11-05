"""Retained closing-tactic attribution, including an opt-in real Lean replay.

QUARTIC_NATIVE_REPLAY=1 runs the fixture with this repository's pinned Lean
compiler and its standard library. No Quartic/Mathlib checkout or cache is used.
Run this test alone when native jobs are serialized by the caller.
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import record_retained_lines as replay


class RetainedRowsTest(unittest.TestCase):
    def test_native_index_range_starts_after_primary_name_in_utf8_bytes(self):
        raw = "-- 🧪\ntheorem alpha : True := by exact True.intro\n".encode()
        index = {"decls": {"Example.alpha": [1, 0, 1, len(raw.decode().splitlines()[1]), 1, 8, 1, 13]}}
        self.assertEqual(replay.declaration_ranges(raw, index, ["Example.alpha"]),
                         {"Example.alpha": [len("-- 🧪\ntheorem alpha".encode()), len(raw) - 1]})
        index["decls"]["Other.beta"] = index["decls"]["Example.alpha"]
        self.assertEqual(replay.declaration_ranges(raw, index, ["Other.beta"]), {})

    def test_returned_spans_are_inside_the_requested_caller(self):
        raw = b"other\nexact target\nother"
        pairs = {"caller": ["target"]}
        ranges = {"caller": [6, 18]}
        good = ["caller", "target", 6, 18]
        self.assertEqual(replay.validated_rows(pairs, raw, ranges, [good, good]),
                         {"caller": {"target": [[6, 18]]}})
        for bad in (["foreign", "target", 6, 18], ["caller", "foreign", 6, 18],
                    ["caller", "target", 0, 5], ["caller", "target", 6, 19],
                    ["caller", "target", 18, 18]):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                replay.validated_rows(pairs, raw, ranges, [bad])

    def test_native_candidate_schedule_has_no_lexical_fallback(self):
        raw = b"rfl\nexact wanted\n"
        scoped = {"caller": {"range": [4, len(raw)]}}
        self.assertEqual(replay.scheduled_spans(raw, scoped), [])
        scoped["caller"]["tactic_spans"] = [[4, len(raw) - 1]]
        self.assertEqual(replay.scheduled_spans(raw, scoped), [(4, len(raw) - 1)])
        for span in ([0, 3], [4, len(raw)]):
            scoped["caller"]["tactic_spans"] = [span]
            with self.subTest(span=span), self.assertRaises(ValueError):
                replay.scheduled_spans(raw, scoped)

    def test_native_capture_lock_rejects_a_second_capture_and_releases(self):
        with tempfile.TemporaryDirectory() as temp:
            checkout = Path(temp)
            (checkout / "lean/.lake/build").mkdir(parents=True)
            with replay.exclusive_reader_capture(checkout):
                with self.assertRaisesRegex(RuntimeError, "another native"):
                    with replay.exclusive_reader_capture(checkout):
                        self.fail("concurrent capture admitted")
            with replay.exclusive_reader_capture(checkout):
                pass

    def test_process_tree_memory_guard_kills_its_owned_job(self):
        with self.assertRaisesRegex(RuntimeError, "RSS budget"):
            replay.native_output([sys.executable, "-c", "import time; time.sleep(10)"], replay.ROOT, 1)
        self.assertEqual(replay.native_output([sys.executable, "-c", "print('ok')"], replay.ROOT), b"ok\n")

    def test_completed_evidence_survives_one_rejected_module(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "corpus").mkdir()
            (root / "lean/.lake/build/lib/lean").mkdir(parents=True)
            (root / "lean/lean-toolchain").write_text("fixture-toolchain")
            hashes = {"fixture": "source"}
            snapshot = replay.canonical_sha256(hashes)
            graph = {"source_snapshot_sha256": snapshot, "toolchain": "fixture-toolchain", "nodes": {}}
            requests = {}
            for module in ("A", "B"):
                caller = module + ".caller"
                raw = b"theorem caller : True := by exact target"
                (root / f"lean/{module}.lean").write_bytes(raw)
                (root / f"lean/.lake/build/lib/lean/{module}.ilean").write_text(json.dumps({
                    "decls": {caller: [0, 0, 0, len(raw), 0, 8, 0, 14]}}))
                graph["nodes"][caller] = {"module": module, "value": ["target"]}
                requests[caller] = ["target"]
            (root / "corpus/reading_dependencies.json").write_text(json.dumps(graph))
            (root / "corpus/reading_kernel_paths.json").write_text(json.dumps(graph))
            output = root / "corpus/reading_retained_lines.json"
            output.write_text(json.dumps({"requests": requests}))
            lo = raw.index(b"exact")
            def native(command, cwd, budget, env=None):
                if "--no-build" in command:
                    return b""
                if "python3" in command:
                    return b"{}"
                self.fail("unexpected native command")
            def module(lean, mod, source, scoped, budget, env):
                if mod == "B":
                    raise RuntimeError("native replay exceeded 4096 MiB RSS budget")
                return [["A.caller", "target", lo, len(raw)]]
            with mock.patch.object(replay, "ROOT", root), mock.patch.object(replay, "OUTPUT", output), \
                    mock.patch.object(replay, "source_hashes", return_value=hashes), \
                    mock.patch.object(replay, "native_output", side_effect=native), \
                    mock.patch.object(replay, "replay_module", side_effect=module):
                replay.record(root, None, False)
                # A subset update preserves a current completed module.
                replay.record(root, None, False, selected_modules=["B"])
                result = json.loads(output.read_bytes())
                self.assertIn("A.caller", result["nodes"])
                # A failed rerun also preserves its own earlier verified rows.
                for cache in (root / "lean/.lake/build/quartic-retained-lines").glob("*.json"):
                    cache.unlink()
                with mock.patch.object(replay, "replay_module", side_effect=RuntimeError("RSS budget")):
                    replay.record(root, None, False, selected_modules=["A"])
                result = json.loads(output.read_bytes())
                self.assertEqual(result["failed_attempts"], {"A": "RSS budget"})
                self.assertEqual(result["completed_modules"], ["A"])
                preserved = output.read_bytes()
                with mock.patch.object(replay, "replay_module", side_effect=RuntimeError("RSS budget")):
                    with self.assertRaisesRegex(ValueError, "native retained replay failed"):
                        replay.record(root, None, True, selected_modules=["A"])
                self.assertEqual(output.read_bytes(), preserved)
                kernel_path = root / "corpus/reading_kernel_paths.json"
                kernel_bytes = kernel_path.read_bytes()
                kernel_path.write_bytes(kernel_bytes + b"\n")
                replay.record(root, None, False, selected_modules=["B"])
                self.assertEqual(json.loads(output.read_bytes())["nodes"], {})
                kernel_path.write_bytes(kernel_bytes)
                output.write_bytes(preserved)
                result["producers"] = {}
                output.write_text(json.dumps(result))
                replay.record(root, None, False, selected_modules=["B"])
                self.assertEqual(json.loads(output.read_bytes())["nodes"], {})
                output.write_bytes(preserved)
            result = json.loads(output.read_bytes())
            self.assertEqual(result["nodes"], {"A.caller": {"target": [[lo, len(raw)]]}})
            self.assertEqual(result["completed_modules"], ["A"])
            self.assertEqual(set(result["uninspected_modules"]), {"B"})
            self.assertEqual(result["requests"], requests)

    def test_multiple_native_jobs_are_rejected_before_inspection(self):
        with self.assertRaisesRegex(ValueError, "exactly one Lean job"):
            replay.record(None, None, False, jobs=2)


@unittest.skipUnless(os.environ.get("QUARTIC_NATIVE_REPLAY") == "1",
                     "set QUARTIC_NATIVE_REPLAY=1 for the pinned native Lean fixture")
class NativeRetainedReplayTest(unittest.TestCase):
    def test_only_retained_payloads_in_the_callers_source_range_testify(self):
        for module_system in (False, True):
            with self.subTest(module_system=module_system):
                self.replay_fixture(module_system)

    def replay_fixture(self, module_system):
        self.assertIsNotNone(shutil.which("lean"), "install the pinned Lean toolchain")
        source = '''import Lean
namespace RetainedFixture
public theorem wanted : True := True.intro
public theorem alternative : True := True.intro
@[expose] public def Hidden := Nat
public def expectedOnly (x : Hidden) : Hidden := by
  exact x
public theorem direct : True := by
  exact wanted
public theorem abandoned : True := by
  first
  | have unused : True := by
      exact wanted
    fail
  | exact wanted
public theorem bulleted : True ∧ True := by
  constructor
  · exact wanted
  · exact wanted
public theorem inlined : True := by exact wanted
public theorem progress (P : Prop) (h : P) : P ∧ True := by
  simp only [and_true]
  exact h
public theorem donor : True := by
  exact wanted
end RetainedFixture
'''
        if module_system:
            source = source.replace("import Lean", "module\n\npublic import Lean", 1)
        raw = source.encode()
        env = os.environ.copy()
        env["ELAN_TOOLCHAIN"] = (replay.ROOT / "lean/lean-toolchain").read_text().strip()
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            path = folder / "RetainedFixture.lean"
            path.write_text(source)
            env["LEAN_PATH"] = temp
            objects = folder / ".lake/build/lib/lean"
            objects.mkdir(parents=True)
            compiled = subprocess.run(["lean", "-j1", "-M4096", "-o", str(objects / "RetainedFixture.olean"), str(path)],
                                      cwd=folder, env=env, capture_output=True, text=True)
            self.assertEqual(compiled.returncode, 0, compiled.stdout + compiled.stderr)
            if module_system:
                self.assertTrue((objects / "RetainedFixture.olean.private").is_file())
            names = ["expectedOnly", "direct", "abandoned", "bulleted", "inlined", "progress", "donor"]
            offsets = {name: raw.index(("public def " if name == "expectedOnly" else "public theorem ").encode()
                                      + name.encode()) for name in names}
            ranges = {name: [offsets[name], offsets[names[i + 1]] if i + 1 < len(names) else len(raw)]
                      for i, name in enumerate(names)}
            # The donor deliberately receives another declaration's source range.
            ranges["donor"] = ranges["direct"]
            targets = ["RetainedFixture.wanted", "RetainedFixture.alternative", "RetainedFixture.Hidden"]
            known = []
            for token in (b"exact x", b"exact wanted", b"simp only [and_true]", b"exact h"):
                pos = 0
                while (pos := raw.find(token, pos)) >= 0:
                    known.append([pos, pos + len(token)])
                    pos += len(token)
            requests = {"RetainedFixture." + name: {"range": ranges[name], "targets": targets,
                        "tactic_spans": [span for span in known if ranges[name][0] <= span[0] < span[1] <= ranges[name][1]]}
                        for name in names}
            rows = replay.replay_module(folder, "RetainedFixture", raw, requests, 4096, env)
        observed = {(c, d, raw[lo:hi].decode()) for c, d, lo, hi in rows}
        self.assertEqual(observed, {
            ("RetainedFixture.direct", "RetainedFixture.wanted", "exact wanted"),
            ("RetainedFixture.abandoned", "RetainedFixture.wanted", "exact wanted"),
            ("RetainedFixture.bulleted", "RetainedFixture.wanted", "exact wanted"),
            ("RetainedFixture.inlined", "RetainedFixture.wanted", "exact wanted"),
        })
        self.assertEqual(len([row for row in rows if row[0] == "RetainedFixture.bulleted"]), 2)
        surviving = raw.index(b"exact wanted", raw.index(b"  | exact wanted"))
        abandoned = [row for row in rows if row[0] == "RetainedFixture.abandoned"]
        self.assertEqual(abandoned, [["RetainedFixture.abandoned", "RetainedFixture.wanted",
                                     surviving, surviving + len(b"exact wanted")]])


if __name__ == "__main__":
    unittest.main()
