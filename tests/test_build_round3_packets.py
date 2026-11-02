import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("round3", ROOT / "tools/build_round3_packets.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
JOBS = ["01_models_evidence", "02_forrelation_promise_circuit"]


class RoundThreeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        base = Path(self.temp.name)
        self.root = base / "repository"
        self.root.mkdir()
        self.dest = base / "output"
        for name in ("README.md", "AGENTS.md", "CONTRIBUTING.md", "LICENSE", "Makefile",
                     "lean/README.md", "corpus/README.md", "research/returns/README.md",
                     "research/returns/round2/README.md", "research/returns/round2/intake.json",
                     "research/README.md", "research/intake/statement_ledger.json",
                     "research/adjudication/funnel_adjudication.json",
                     "research/adjudication/round2_integration.md",
                     "research/returns/funnel/1_long_reasoning_record/reasoning-record.md",
                     "tools/build_corpus.py"):
            self.write(name, "{}" if name.endswith(".json") else "source text\n")
        self.write("lean/QuarticQuery/Statement.lean", "def statement := True\n")
        self.write("lean/QuarticQuery/A.lean", "theorem a : True := trivial\n")
        self.write("lean/QuarticQuery/B.lean", "theorem b : True := trivial\n")
        self.write("lean/lakefile.toml", "name = 'fixture'\n")
        self.write("lean/lean-toolchain", "leanprover/lean4:v4.24.0\n")
        self.write("lean/lake-manifest.json", "{}")
        self.write("lean/QuarticCorpus/fixture.json", "{}")
        hashes = MODULE.corpus.source_hashes(self.root)
        self.write("corpus/lean_dependencies.json", json.dumps({"roots": ["a"], "reached": ["a"],
                                                             "source_hashes": hashes}))
        for name, status, binding in (("current", "passed", hashes), ("pending", "running", hashes),
                                      ("stale", "passed", {"old": "0" * 64}),
                                      ("legacy", "passed", None)):
            receipt = {"kind": "lean_build", "name": name, "status": status, "declarations": ["a"]}
            if binding:
                receipt["source_hashes"] = binding
            self.write(f"corpus/receipts/{name}.json", json.dumps(receipt))
        self.write("corpus/statements.json", '{"stale_generated_claim": {"built": true}}')
        requests = self.root / "research/requests/round3"
        self.write("research/requests/round3/common.md", "# {title}\n\n{job}\n\n{boundary}\n")
        self.write("research/requests/round3/boundaries.md", "Source presence is not a build.\n")
        self.write("research/requests/round3/SELECTION.md", "Two focused fixture jobs.\n")
        for job in JOBS:
            self.write(f"research/requests/round3/{job}.md", f"Read the primary sources for {job}.\n")
            for folder in MODULE.RETURNS[job]:
                self.write("research/returns/" + folder + "/blueprint.md", "Advisory return.\n")
        self.writing = base / "writing"
        self.writing.mkdir()
        for name in MODULE.GUIDES:
            (self.writing / name).write_text("Portable mathematical writing guidance: " + name)
        (self.writing / "SKILL.md").write_text("Use literal mathematical prose and exact hypotheses.\n")
        self.paper = base / "paper"
        self.paper.mkdir()
        (self.paper / "source.pdf").write_bytes(b"%PDF-fixture-original")
        (self.paper / "extracted.md").write_text("Full preprint conversion\n")
        self.annexes = base / "annexes"
        for slug in ("models-paper", "circuit-paper", "unrelated-paper"):
            folder = self.annexes / slug
            folder.mkdir(parents=True)
            (folder / "extracted.md").write_text("Full primary text for " + slug)
            (folder / "source.pdf").write_bytes(b"%PDF-" + slug.encode())
            (folder / "annex_notes.json").write_text("{}")
        for path in MODULE.funnel.EXEMPLARS.values():
            self.write(path, "Exemplar writing, not quartic evidence.\n")
        for command in (["init", "--quiet"], ["add", "."], ["-c", "user.name=Fixture",
                        "-c", "user.email=fixture@example.invalid", "commit", "--quiet", "-m", "fixture"]):
            subprocess.run(["git", "-C", str(self.root), *command], check=True, capture_output=True)
        commit = subprocess.run(["git", "-C", str(self.root), "rev-parse", "HEAD"],
                                check=True, capture_output=True, text=True).stdout.strip()
        self.options = dict(root=self.root, requests_dir=requests, paper_annex=self.paper,
            annexes=self.annexes, writing_skill=self.writing / "SKILL.md", writing_guides=self.writing,
            exemplar_repo=self.root, exemplar_ref=commit)
        focus = patch.dict(MODULE.FOCUS, {JOBS[0]: ["lean/QuarticQuery/A.lean"],
                                          JOBS[1]: ["lean/QuarticQuery/B.lean"]})
        literature = patch.dict(MODULE.LITERATURE, {JOBS[0]: ["models-paper"], JOBS[1]: ["circuit-paper"]})
        focus.start()
        literature.start()
        self.addCleanup(focus.stop)
        self.addCleanup(literature.stop)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def prepare(self, jobs=JOBS):
        return MODULE.prepare_batch(jobs, **self.options)

    def dependency_fixture(self):
        roots, packages = {}, []
        for name, source, contents in (("complexitylib", "Complexity/A.lean", "public import all Cslib.B\nimport Mathlib.NotBundled\n"),
                                        ("cslib", "Cslib/B.lean", "module\npublic import Init\n")):
            folder = Path(self.temp.name) / name
            folder.mkdir()
            for file, text in (("LICENSE", "Apache-2.0\n"), ("lean-toolchain", "fixture\n"),
                               ("lake-manifest.json", "{}"), ("lakefile.toml", "name='fixture'\n"),
                               (source, contents), (source.replace("/A.", "/Unused.").replace("/B.", "/Unused."),
                                                    "import Missing.Unrelated\n")):
                path = folder / file
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text)
            for command in (["init", "--quiet"], ["add", "."], ["-c", "user.name=Fixture", "-c",
                            "user.email=fixture@example.invalid", "commit", "--quiet", "-m", "dependency"]):
                subprocess.run(["git", "-C", str(folder), *command], check=True, capture_output=True)
            commit = subprocess.run(["git", "-C", str(folder), "rev-parse", "HEAD"],
                                    check=True, capture_output=True, text=True).stdout.strip()
            roots[name] = folder
            packages.append({"name": name, "rev": commit, "configFile": "lakefile.toml", "url": "fixture:" + name})
        packages.append({"name": "mathlib", "rev": "f" * 40, "url": "fixture:mathlib"})
        self.write("lean/lake-manifest.json", json.dumps({"packages": packages}))
        self.write("lean/QuarticQuery/A.lean", "import QuarticQuery.B\n")
        self.write("lean/QuarticQuery/B.lean", "import Complexity.A\n")
        return roots

    def test_dependency_closure_is_focused_recursive_and_pin_bound(self):
        roots = self.dependency_fixture()
        files, provenance = MODULE.dependency_sources(JOBS[0], self.root, roots)
        self.assertIn("dependencies/complexitylib/Complexity/A.lean", files)
        self.assertIn("dependencies/cslib/Cslib/B.lean", files)
        self.assertIn("dependencies/complexitylib/LICENSE", files)
        self.assertIn("dependencies/cslib/lakefile.toml", files)
        self.assertFalse(any("Unused" in name or "Mathlib/" in name or ".lake" in name for name in files))
        self.assertEqual({row["package"] for row in provenance["packages"]}, {"complexitylib", "cslib"})
        self.assertIn("Mathlib.NotBundled", provenance["foundation_modules_omitted"])
        packet = MODULE.prepare_batch([JOBS[0]], **dict(self.options, dependency_roots=roots))[JOBS[0]]
        recorded = json.loads(packet["data"]["DEPENDENCY_SOURCES.json"])
        for member, value in recorded["members"].items():
            self.assertEqual(value, MODULE.digest(packet["data"][member]))

    def test_selected_missing_dependency_import_fails(self):
        roots = self.dependency_fixture()
        (roots["cslib"] / "Cslib/B.lean").unlink()
        with self.assertRaisesRegex(ValueError, "missing selected Lean import source"):
            MODULE.dependency_sources(JOBS[0], self.root, roots)

    def test_dependency_checkout_revision_must_match_manifest(self):
        roots = self.dependency_fixture()
        manifest = json.loads((self.root / "lean/lake-manifest.json").read_bytes())
        manifest["packages"][0]["rev"] = "0" * 40
        self.write("lean/lake-manifest.json", json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "dependency pin mismatch"):
            MODULE.dependency_sources(JOBS[0], self.root, roots)

    def test_dirty_selected_dependency_cannot_claim_pinned_bytes(self):
        roots = self.dependency_fixture()
        (roots["complexitylib"] / "Complexity/A.lean").write_text("import Cslib.B\n-- changed source\n")
        with self.assertRaisesRegex(ValueError, "differ from the pinned commit"):
            MODULE.dependency_sources(JOBS[0], self.root, roots)

    def test_import_header_ignores_nested_comments_and_stops_at_body(self):
        imports = MODULE.lean_imports("module\n/- import Bad.A /- nested -/ -/\n"
            "public meta import all Complexity.A -- comment\nimport\n  Cslib.B\n"
            "namespace Example\nimport Bad.Body\n")
        self.assertEqual(imports, ["Complexity.A", "Cslib.B"])

    def test_per_job_focus_preserves_primary_originals_and_complete_bound_source(self):
        packets = self.prepare()
        for job, selected, unselected in ((JOBS[0], "models-paper", "circuit-paper"),
                                           (JOBS[1], "circuit-paper", "models-paper")):
            packet = packets[job]
            data = packet["data"]
            self.assertIn(f"literature/{selected}/source.pdf", data)
            self.assertIn(f"literature/{selected}/extracted.md", data)
            self.assertFalse(any(unselected in name or "unrelated-paper" in name for name in data))
            snapshot = json.loads(data["EVIDENCE_SNAPSHOT.json"])
            for path, digest in snapshot["source_hashes"].items():
                self.assertEqual(MODULE.digest(data["repository/" + path]), digest)
            for name in MODULE.GUIDES:
                self.assertIn("Portable mathematical writing", data["writing/" + name].decode())
            self.assertIn("repository/research/returns/funnel/1_long_reasoning_record/reasoning-record.md", data)
            self.assertIn("repository/research/adjudication/round2_integration.md", data)
            exemplar = next(row for row in packet["manifest"]["members"] if row["member"].startswith("exemplars/"))
            self.assertEqual(exemplar["role"], "style_exemplar_not_mathematical_evidence")
            self.assertIn(self.options["exemplar_ref"], exemplar["source"])
        self.assertIn("repository/lean/QuarticQuery/A.lean", packets[JOBS[0]]["manifest"]["primary_read"])
        self.assertNotIn("repository/lean/QuarticQuery/B.lean", packets[JOBS[0]]["manifest"]["primary_read"])

    def test_currentness_and_pending_are_independent_and_mtime_irrelevant(self):
        self.write("lean/.lake/build/lib/lean/QuarticQuery/A.olean", "forged newer artifact")
        packet = self.prepare([JOBS[0]])[JOBS[0]]
        snapshot = json.loads(packet["data"]["EVIDENCE_SNAPSHOT.json"])
        rows = {row["name"]: row for row in snapshot["receipts"]}
        self.assertEqual((rows["current"]["status"], rows["current"]["source_currentness"]), ("passed", "current"))
        self.assertEqual((rows["pending"]["status"], rows["pending"]["source_currentness"]), ("running", "current"))
        self.assertEqual(rows["stale"]["source_currentness"], "stale")
        self.assertEqual(rows["legacy"]["source_currentness"], "legacy_unbound")
        self.assertFalse(any(".olean" in name for name in packet["data"]))
        self.write("lean/QuarticQuery/A.lean", "theorem a : False := by sorry\n")
        changed = self.prepare([JOBS[0]])[JOBS[0]]
        snapshot = json.loads(changed["data"]["EVIDENCE_SNAPSHOT.json"])
        self.assertEqual(snapshot["dependency_export"]["source_currentness"], "stale")
        self.assertEqual(next(row for row in snapshot["receipts"] if row["name"] == "current")["source_currentness"], "stale")
        self.assertIn("No build was run", changed["data"]["BUILD_STATUS.md"].decode())

    def test_supplied_paper_identity_is_hash_bound_without_an_invented_git_pin(self):
        packet = self.prepare([JOBS[0]])[JOBS[0]]
        provenance = packet["manifest"]["paper_provenance"]
        self.assertEqual(provenance["sha256"], MODULE.digest((self.paper / "source.pdf").read_bytes()))
        self.assertNotIn("4eaee875", packet["manifest"]["source_paper"])
        self.assertIsNone(provenance["metadata_member"])

    def test_native_results_preserve_raw_status_and_scope_instead_of_upgrading_logs(self):
        record = Path(self.temp.name) / "native.json"
        hashes = MODULE.corpus.source_hashes(self.root)
        binding = {"lean/QuarticQuery/A.lean": hashes["lean/QuarticQuery/A.lean"]}
        raw = {"status": "running", "source_hashes": binding, "targets": [{"status": "passed", "name": "a"}]}
        record.write_text(json.dumps(raw))
        log = Path(self.temp.name) / "native.log"
        log.write_text("Native build is still running.\n")
        options = dict(self.options, native_results={"run.json": record}, native_logs={"run.log": log})
        packet = MODULE.prepare_batch([JOBS[0]], **options)[JOBS[0]]
        snapshot = json.loads(packet["data"]["EVIDENCE_SNAPSHOT.json"])
        native = snapshot["native_results"][0]
        self.assertEqual(native["status"], "running")
        self.assertEqual(native["source_currentness"], "current_for_recorded_inputs_only")
        self.assertEqual(json.loads(packet["data"]["native_results/run.json"]), raw)
        self.assertEqual(packet["data"]["native_logs/run.log"], log.read_bytes())
        record.write_text(json.dumps({"status": "passed", "source_hashes": {"/foreign/lean/A.lean": hashes["lean/QuarticQuery/A.lean"]}}))
        packet = MODULE.prepare_batch([JOBS[0]], **options)[JOBS[0]]
        native = json.loads(packet["data"]["EVIDENCE_SNAPSHOT.json"])["native_results"][0]
        self.assertEqual(native["source_currentness"], "unresolved_source_labels")

    def test_native_inventory_maps_canonical_paths_and_explicit_fixture_bytes(self):
        record = Path(self.temp.name) / "inventory.json"
        fixture = Path(self.temp.name) / "fixture.lean"
        fixture.write_text("def fixture := True\n")
        source = self.root / "lean/QuarticQuery/A.lean"
        raw = {"kind": "bounded native inventory", "results": [
            {"target": "A", "status": "passed", "inputs_before": {
                str(source): MODULE.digest(source.read_bytes()), str(fixture): MODULE.digest(fixture.read_bytes())},
                "inputs_unchanged": True}, {"target": "B", "status": "skipped"}]}
        record.write_text(json.dumps(raw))
        options = dict(self.options, native_results={"inventory.json": record}, native_sources={"fixture.lean": fixture})
        packet = MODULE.prepare_batch([JOBS[0]], **options)[JOBS[0]]
        rows = json.loads(packet["data"]["EVIDENCE_SNAPSHOT.json"])["native_results"]
        self.assertEqual(rows[0]["source_currentness"], "current_for_recorded_inputs_only")
        self.assertEqual(set(rows[0]["input_members"]), {"repository/lean/QuarticQuery/A.lean", "native_sources/fixture.lean"})
        self.assertEqual(rows[1]["source_currentness"], "legacy_unbound")
        source.write_text("changed after the native run\n")
        packet = MODULE.prepare_batch([JOBS[0]], **options)[JOBS[0]]
        rows = json.loads(packet["data"]["EVIDENCE_SNAPSHOT.json"])["native_results"]
        self.assertEqual(rows[0]["status"], "passed")
        self.assertEqual(rows[0]["source_currentness"], "stale")

    def test_batch_writes_are_independently_audited_and_request_hash_is_bound(self):
        digest = MODULE.batch_digest(self.prepare())
        with patch.object(MODULE.check_packets, "audit", wraps=MODULE.check_packets.audit) as audit:
            paths = MODULE.build_batch(JOBS, self.dest, digest, **self.options)
        self.assertEqual(audit.call_count, 2)
        for job, path in zip(JOBS, paths):
            self.assertEqual(MODULE.check_packets.audit(path)[0], job)
            with zipfile.ZipFile(path) as archive:
                manifest = json.loads(archive.read("manifest.json"))
                self.assertEqual(MODULE.digest(archive.read("READ_ME_FIRST.md")), manifest["request_sha256"])
        self.assertFalse(list(self.dest.glob(".quartic*")))

    def test_existing_second_destination_blocks_entire_batch_without_overwrite(self):
        self.dest.mkdir()
        sent = self.dest / f"quartic_r3_{JOBS[1]}.zip"
        sent.write_bytes(b"already sent archive")
        with self.assertRaises(FileExistsError):
            MODULE.build_batch(JOBS, self.dest, MODULE.batch_digest(self.prepare()), **self.options)
        self.assertEqual(sent.read_bytes(), b"already sent archive")
        self.assertEqual(list(self.dest.iterdir()), [sent])

    def test_changed_source_requires_new_freeze_and_creates_no_output(self):
        digest = MODULE.batch_digest(self.prepare())
        self.write("lean/QuarticQuery/B.lean", "source changed after approval\n")
        with self.assertRaisesRegex(ValueError, "approved freeze digest"):
            MODULE.build_batch(JOBS, self.dest, digest, **self.options)
        self.assertFalse(self.dest.exists())

    def test_input_change_while_reading_fails(self):
        content = MODULE.funnel.content
        changed = False

        def mutate(source):
            nonlocal changed
            blob = content(source)
            if source == self.root / "lean/QuarticQuery/A.lean" and not changed:
                changed = True
                source.write_text("changed while reading\n")
            return blob

        with patch.object(MODULE.funnel, "content", side_effect=mutate):
            with self.assertRaisesRegex(ValueError, "changed while being read"):
                self.prepare([JOBS[0]])

    def test_new_receipt_during_packaging_removes_all_new_archives(self):
        digest = MODULE.batch_digest(self.prepare())
        write = MODULE.write_archive

        def mutate(path, packet):
            write(path, packet)
            self.write("corpus/receipts/arrived.json", '{"kind":"lean_build","status":"running"}')

        with patch.object(MODULE, "write_archive", side_effect=mutate):
            with self.assertRaisesRegex(ValueError, "changed during packaging"):
                MODULE.build_batch(JOBS, self.dest, digest, **self.options)
        self.assertEqual(list(self.dest.iterdir()), [])

    def test_exclusive_publication_preserves_concurrent_sent_archive(self):
        digest = MODULE.batch_digest(self.prepare([JOBS[0]]))
        link = MODULE.os.link

        def race(source, destination):
            destination.write_bytes(b"concurrent sent archive")
            return link(source, destination)

        with patch.object(MODULE.os, "link", side_effect=race):
            with self.assertRaises(FileExistsError):
                MODULE.build_batch([JOBS[0]], self.dest, digest, **self.options)
        self.assertEqual((self.dest / f"quartic_r3_{JOBS[0]}.zip").read_bytes(), b"concurrent sent archive")
        self.assertFalse(list(self.dest.glob(".quartic*")))

    def test_missing_primary_literature_does_not_fall_back_to_notes(self):
        (self.annexes / "models-paper/source.pdf").unlink()
        with self.assertRaisesRegex(ValueError, "lacks original PDF or TeX"):
            self.prepare([JOBS[0]])

    def test_selected_supplement_is_required_and_preserved_at_its_exact_path(self):
        with patch.dict(MODULE.LITERATURE_SUPPLEMENTS, {"models-paper": ["supplements/publisher.pdf"]}):
            with self.assertRaisesRegex(ValueError, "missing selected literature edition"):
                self.prepare([JOBS[0]])
            path = self.annexes / "models-paper/supplements/publisher.pdf"
            path.parent.mkdir()
            path.write_bytes(b"%PDF-selected publisher edition")
            packet = self.prepare([JOBS[0]])[JOBS[0]]
        self.assertEqual(packet["data"]["literature/models-paper/supplements/publisher.pdf"], path.read_bytes())

    def test_external_backend_contract_is_supplied_only_to_backend_job(self):
        job = "09_evidence_backend"
        source = Path(self.temp.name) / "schema.json"
        source.write_text('{"type":"object"}')
        self.write(f"research/requests/round3/{job}.md", "Inspect the actual supplied schema.\n")
        with patch.dict(MODULE.FOCUS, {job: ["lean/QuarticQuery/A.lean"]}), \
                patch.dict(MODULE.RETURNS, {job: []}):
            options = dict(self.options, backend_sources={"schema.json": source}, backend_unavailable={
                "lean-exposition": "Not supplied in this focused fixture", "comparator": "No native source fixture"})
            packets = MODULE.prepare_batch([JOBS[0], job], **options)
        self.assertNotIn("external_backend/schema.json", packets[JOBS[0]]["data"])
        self.assertEqual(packets[job]["data"]["external_backend/schema.json"], source.read_bytes())
        status = json.loads(packets[job]["data"]["BACKEND_INPUT_STATUS.json"])
        self.assertTrue(all(row["status"] == "incomplete_or_unavailable" for row in status["groups"]))

    def test_backend_job_cannot_silently_omit_primary_contract_sources(self):
        with self.assertRaisesRegex(ValueError, "requires actual lean-exposition contracts"):
            MODULE.inputs("09_evidence_backend", **self.options)

    def test_cross_job_input_drift_does_not_create_a_mixed_batch(self):
        prepare = MODULE.prepare
        calls = 0

        def mutate(job, **options):
            nonlocal calls
            packet = prepare(job, **options)
            calls += 1
            if calls == 1:
                self.write("research/requests/round3/common.md", "# Changed {title}\n{job}\n{boundary}\n")
            return packet

        with patch.object(MODULE, "prepare", side_effect=mutate):
            with self.assertRaisesRegex(ValueError, "changed across the batch"):
                self.prepare()

    def test_working_directory_output_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "outside the repository"):
            MODULE.build_batch(JOBS, self.root / "packets", "unused", **self.options)

    def test_cli_validation_is_default_and_build_requires_freeze(self):
        args = ["--root", str(self.root), "--paper-annex", str(self.paper), "--annexes", str(self.annexes),
                "--writing-skill", str(self.writing / "SKILL.md"), "--writing-guides", str(self.writing),
                "--exemplar-repo", str(self.root), "--exemplar-ref", "HEAD", "--only", JOBS[0],
                "--dest", str(self.dest)]
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(MODULE.main(args), 0)
        self.assertIn("no ZIPs written", output.getvalue())
        self.assertFalse(self.dest.exists())
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
            MODULE.main([*args, "--build"])
        self.assertEqual(error.exception.code, 2)

    def test_catalog_is_bounded_and_every_job_has_source_roles(self):
        self.assertLessEqual(len(MODULE.JOBS), 10)
        self.assertEqual(set(MODULE.JOBS), set(MODULE.FOCUS))
        self.assertEqual(set(MODULE.JOBS), set(MODULE.LITERATURE))
        self.assertEqual(set(MODULE.JOBS), set(MODULE.RETURNS))

    def test_every_maintained_request_renders(self):
        requests = ROOT / "research/requests/round3"
        for job in MODULE.JOBS:
            with self.subTest(job=job):
                text = MODULE.render_request(job, requests)
                self.assertIn(MODULE.JOBS[job], text)
                self.assertIn("source_read_receipt.json", text)
                self.assertIn("writing/SKILL.md", text)


if __name__ == "__main__":
    unittest.main()
