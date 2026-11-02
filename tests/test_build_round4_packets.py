import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MODULE = load("round4", ROOT / "tools/build_round4_packets.py")
FIXTURE = load("round3_fixtures", ROOT / "tests/test_build_round3_packets.py")
JOBS = ["02_short_expert", "03_examples_first"]


class RoundFourTests(unittest.TestCase):
    # Reuse the small fake repository/exemplar/literature fixture, not live sources.
    write = FIXTURE.RoundThreeTests.write

    def setUp(self):
        FIXTURE.RoundThreeTests.setUp(self)
        self.write("lean/QuarticQuery.lean", "import QuarticQuery.A\n")
        for name in MODULE.RENDER_SOURCES:
            self.write("research/returns/" + name, "Exact reused renderer fixture source\n")
        self.write("docs/reasoning_record.md", "# Reviewed integrated reasoning\n")
        self.write("docs/reasoning_record.bib", "@article{fixture}\n")
        self.write("docs/reasoning_record_correspondence.json", "[]")
        # The fake receipt binds the final fake sources including the aggregate.
        hashes = MODULE.previous.corpus.source_hashes(self.root)
        self.write("corpus/lean_dependencies.json", json.dumps({"roots": ["a"], "reached": ["a"], "source_hashes": hashes}))
        self.write("corpus/receipts/current.json", json.dumps({"kind": "lean_build", "status": "passed",
            "source_hashes": hashes, "declarations": ["a"]}))
        requests = self.root / "research/requests/round4"
        self.write("research/requests/round4/common.md", "# {title}\n{job}\n{boundary}\n")
        self.write("research/requests/round4/boundaries.md", "Joint events are not conditional success.\n")
        self.write("research/requests/round4/SELECTION.md", "Two independent fixtures.\n")
        for job in JOBS:
            self.write(f"research/requests/round4/{job}.md", "Advance this endpoint now.\n")
        specimen = Path(self.temp.name) / "structural_exemplars.json"
        source_path = next(iter(MODULE.previous.funnel.EXEMPLARS.values()))
        source = (self.root, self.options["exemplar_ref"], source_path)
        specimen.write_text(json.dumps({"schema": "quartic-structural-exemplars-v1", "sources": [
            {"member": f"writing/structural/{family}/specimen.md", "family": family,
             "repository": str(self.root), "commit": self.options["exemplar_ref"], "path": source_path,
             "sha256": MODULE.digest(MODULE.previous.funnel.content(source)),
             "reading_route": "Complete fake structural specimen"} for family in ("257", "sk", "graph-to-long")]}))
        methods = Path(self.temp.name) / "methods.json"
        application = Path(self.temp.name) / "portable.md"
        application.write_text("Task-specific portable method; no private runtime prerequisite.\n")
        methods.write_text(json.dumps({"schema": "quartic-method-sources-v1", "sources": [
            {"member": "methods/PORTABLE_APPLICATION.md", "path": str(application),
             "sha256": MODULE.digest(application.read_bytes()), "version": "fixture-v1",
             "application": "Apply to this exact job", "jobs": list(MODULE.JOBS)}]}))
        self.options.update(requests_dir=requests, structural_exemplars=specimen, method_sources=methods)
        pdf_links = patch.object(MODULE, "pdf_reading_sources", return_value=({}, {"links": []}))
        pdf_links.start()
        self.addCleanup(pdf_links.stop)
        self.receipt = Path(self.temp.name) / "review.json"
        self.accept_review()
        for mapping, values in ((MODULE.FOCUS, {j: ["lean/QuarticQuery/A.lean"] for j in JOBS}),
                                (MODULE.LITERATURE, {j: ["models-paper"] for j in JOBS}),
                                (MODULE.RETURNS, {j: [] for j in JOBS})):
            mock = patch.dict(mapping, values)
            mock.start()
            self.addCleanup(mock.stop)

    def accept_review(self):
        self.receipt.write_text(json.dumps({"status": "accepted", "reviewer": "independent fixture",
            "review_scope": "full integrated record", "pdf_sha256": MODULE.digest(b"%PDF-fixture-reading-copy"), "record_sha256": MODULE.digest(
                (self.root / "docs/reasoning_record.md").read_bytes()),
            "reviewed_files": {name: MODULE.digest((self.root / name).read_bytes()) for name in MODULE.REVIEWED_FILES},
            "source_snapshot_sha256": MODULE.previous.corpus.canonical_sha256(MODULE.previous.corpus.source_hashes(self.root))}))
        self.options["review_receipt"] = self.receipt
        pdf = Path(self.temp.name) / "reasoning_record.pdf"
        pdf.write_bytes(b"%PDF-fixture-reading-copy")
        render = Path(self.temp.name) / "render.json"
        render.write_text(json.dumps({"schema": "quartic-reasoning-record-render-v1",
            "status": "rendered_requires_visual_review", "source_unchanged": True,
            "source_sha256": MODULE.digest((self.root / "docs/reasoning_record.md").read_bytes()),
            "pdf": str(pdf), "pdf_sha256": MODULE.digest(pdf.read_bytes()), "renderer_sha256": "a" * 64}))
        self.options["record_render"] = render

    def test_freeze_and_build_are_auditable_and_reuse_packet_checker(self):
        packets = MODULE.prepare_batch(JOBS, **self.options)
        paths = MODULE.build_batch(JOBS, self.dest, MODULE.batch_digest(packets), **self.options)
        self.assertEqual(len(paths), 2)
        for path in paths:
            MODULE.previous.check_packets.audit(path)
        with self.assertRaisesRegex(FileExistsError, "new output folder"):
            MODULE.build_batch(JOBS, self.dest, MODULE.batch_digest(packets), **self.options)

    def test_pending_or_stale_review_prevents_build_and_creates_no_output(self):
        options = dict(self.options, review_receipt=None)
        packets = MODULE.prepare_batch(JOBS, **options)
        self.assertTrue(all(p["manifest"]["review_gate"]["status"] == "pending" for p in packets.values()))
        with self.assertRaisesRegex(ValueError, "accepted current review"):
            MODULE.build_batch(JOBS, self.dest, MODULE.batch_digest(packets), **options)
        self.assertFalse(self.dest.exists())
        self.write("docs/reasoning_record.md", "changed after review")
        with self.assertRaisesRegex(ValueError, "exact current|render is stale"):
            MODULE.prepare_batch(JOBS, **self.options)

    def test_review_binds_bibliography_correspondence_corpus_and_lean(self):
        for name in [*MODULE.REVIEWED_FILES, "lean/QuarticQuery/A.lean"]:
            with self.subTest(name=name):
                original = (self.root / name).read_bytes()
                (self.root / name).write_bytes(original + b"\nchanged")
                with self.assertRaisesRegex(ValueError, "stale"):
                    MODULE.review_status(self.root, self.receipt)
                (self.root / name).write_bytes(original)
        row = json.loads(self.receipt.read_bytes())
        row.pop("reviewed_files")
        self.receipt.write_text(json.dumps(row))
        with self.assertRaisesRegex(ValueError, "reviewed_files"):
            MODULE.review_status(self.root, self.receipt)

    def test_any_changed_input_invalidates_freeze(self):
        frozen = MODULE.batch_digest(MODULE.prepare_batch(JOBS, **self.options))
        self.write("research/adjudication/new_decision.md", "Accepted correction.\n")
        with self.assertRaisesRegex(ValueError, "freeze digest"):
            MODULE.build_batch(JOBS, self.dest, frozen, **self.options)
        self.assertFalse(self.dest.exists())

    def test_private_attachments_and_unselected_returns_never_enter_packets(self):
        self.write("research/returns/round3/attachments/input_10.txt", "PRIVATE SESSION TEXT")
        self.write("research/returns/round3/members/unselected/section.md", "unselected advisory text")
        packet = MODULE.prepare_batch([JOBS[0]], **self.options)[JOBS[0]]
        self.assertFalse(any("PRIVATE SESSION TEXT" in blob.decode(errors="ignore") for blob in packet["data"].values()))
        self.assertFalse(any("unselected advisory text" in blob.decode(errors="ignore") for blob in packet["data"].values()))
        self.assertIn("repository/docs/reasoning_record.md", packet["data"])
        self.assertIn("writing/SKILL.md", packet["data"])

    def test_manuscript_links_include_exact_return_contract_and_recursive_doc(self):
        target = "research/returns/round3/members/01_models_evidence/model_contract.json"
        self.write(target, '{"exact":"model contract"}')
        self.write("docs/linked.md", "Read [contract](../" + target + ").\n")
        self.write("docs/reasoning_record.md", "Read [seam](linked.md).\n")
        self.accept_review()
        packet = MODULE.prepare_batch([JOBS[0]], **self.options)[JOBS[0]]
        self.assertEqual(packet["data"]["repository/" + target], b'{"exact":"model contract"}')
        report = json.loads(packet["data"]["READING_LINK_CLOSURE.json"])
        self.assertTrue(any(row["target"] == "repository/" + target for row in report["links"]))

    def test_missing_private_and_escaping_manuscript_links_fail_closed(self):
        for link, error in (("missing.json", "missing load-bearing"),
                            ("../research/returns/round3/attachments/input_10.txt", "private attachment"),
                            ("../../../outside.txt", "escapes repository")):
            with self.subTest(link=link):
                self.write("docs/reasoning_record.md", "[Required source](" + link + ")\n")
                self.accept_review()
                with self.assertRaisesRegex(ValueError, error):
                    MODULE.prepare_batch([JOBS[0]], **self.options)

    def test_repository_to_custody_guide_branch_stops_before_private_attachments(self):
        self.write("README.md", "[Research](research/README.md)\n")
        self.write("research/README.md", "[Custody](returns/README.md)\n")
        self.write("research/returns/README.md", "[Historical private](round3/attachments/input_01.txt)\n")
        packet = MODULE.prepare_batch([JOBS[0]], **self.options)[JOBS[0]]
        self.assertIn("repository/research/returns/README.md", packet["data"])
        report = json.loads(packet["data"]["READING_LINK_CLOSURE.json"])
        self.assertFalse(any("attachments/" in row["target"] for row in report["links"]))
        self.assertIn("historical internal links are not claimed", report["interpretation"])

    def test_immutable_sender_readme_is_leaf_evidence(self):
        target = "research/returns/round3/members/01_models_evidence/README.md"
        self.write(target, "[Sender-only missing attachment](../../attachments/private.txt)\n")
        self.write("docs/reasoning_record.md", "[Historical readme](../" + target + ")\n")
        self.accept_review()
        packet = MODULE.prepare_batch([JOBS[0]], **self.options)[JOBS[0]]
        self.assertIn("repository/" + target, packet["data"])
        self.assertFalse(any("private.txt" in name for name in packet["data"]))

    def test_structural_specimens_are_pinned_hashed_and_required(self):
        packet = MODULE.prepare_batch([JOBS[0]], **self.options)[JOBS[0]]
        self.assertIn("writing/STRUCTURAL_EXEMPLARS.json", packet["data"])
        self.assertIn("writing/structural/257/specimen.md", packet["data"])
        with self.assertRaisesRegex(ValueError, "structural-exemplars"):
            MODULE.prepare_batch([JOBS[0]], **dict(self.options, structural_exemplars=None))
        spec = json.loads(self.options["structural_exemplars"].read_bytes())
        spec["sources"][0]["sha256"] = "0" * 64
        self.options["structural_exemplars"].write_text(json.dumps(spec))
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            MODULE.prepare_batch([JOBS[0]], **self.options)

    def test_matched_pdf_is_beside_manuscript_and_stale_render_fails(self):
        packet = MODULE.prepare_batch([JOBS[0]], **self.options)[JOBS[0]]
        self.assertIn("repository/docs/reasoning_record.pdf", packet["data"])
        self.assertIn("record_render/render.json", packet["data"])
        for name in MODULE.RENDER_SOURCES:
            self.assertIn("repository/research/returns/" + name, packet["data"])
        self.assertNotIn("record_render/reasoning_record.pdf", packet["data"])
        render = json.loads(self.options["record_render"].read_bytes())
        Path(render["pdf"]).write_bytes(b"%PDF-tampered")
        with self.assertRaisesRegex(ValueError, "PDF hash mismatch"):
            MODULE.prepare_batch([JOBS[0]], **self.options)

    def test_changed_pdf_layout_invalidates_acceptance_even_with_valid_render_receipt(self):
        render = json.loads(self.options["record_render"].read_bytes())
        pdf = Path(render["pdf"])
        pdf.write_bytes(b"%PDF-same-markdown-different-layout")
        render["pdf_sha256"] = MODULE.digest(pdf.read_bytes())
        self.options["record_render"].write_text(json.dumps(render))
        self.assertEqual(MODULE.record_render_status(self.root, self.options["record_render"])["pdf_sha256"], render["pdf_sha256"])
        with self.assertRaisesRegex(ValueError, "review PDF hash is stale"):
            MODULE.prepare_batch([JOBS[0]], **self.options)

    def test_pdf_annotation_targets_use_manuscript_directory_and_reject_private_links(self):
        # Call the real resolver while the fake-PDF integration seam remains mocked.
        spec = importlib.util.spec_from_file_location("round4_pdf_resolver", ROOT / "tools/build_round4_packets.py")
        isolated = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(isolated)
        target = "research/returns/round3/members/01_models_evidence/model_contract.json"
        self.write(target, '{}')
        render = {"pdf": "fake.pdf", "pdf_sha256": "a" * 64}
        with patch.object(isolated, "pdf_urls", return_value=("../" + target, "https://example.org/paper")):
            files, report = isolated.pdf_reading_sources(self.root, render)
        self.assertIn("repository/" + target, files)
        self.assertEqual(len(report["links"]), 1)
        with patch.object(isolated, "pdf_urls", return_value=("../research/returns/round3/attachments/input_10.txt",)):
            with self.assertRaisesRegex(ValueError, "private/nonportable"):
                isolated.pdf_reading_sources(self.root, render)

    def test_backend_source_selection_and_methods_enter_actual_job_context(self):
        job = "07_publication_backend"
        self.write(f"research/requests/round4/{job}.md", "Implement the existing adapter end to end.\n")
        source = (self.root, self.options["exemplar_ref"], "README.md")
        member = "external_backend/lean-exposition/pyproject.toml"
        spec = Path(self.temp.name) / "backend.json"
        spec.write_text(json.dumps({"schema": "quartic-backend-sources-v1", "required_members": [member],
            "sources": [{"member": member, "repository": str(self.root), "commit": self.options["exemplar_ref"],
            "path": "README.md", "sha256": MODULE.digest(MODULE.content(source))}]}))
        with patch.dict(MODULE.FOCUS, {job: ["lean/QuarticQuery/A.lean"]}), \
                patch.dict(MODULE.LITERATURE, {job: []}), patch.dict(MODULE.RETURNS, {job: []}):
            packet = MODULE.prepare_batch([job], **dict(self.options, backend_sources=spec))[job]
        self.assertIn(member, packet["data"])
        self.assertIn("methods/PORTABLE_APPLICATION.md", packet["data"])
        context = json.loads(packet["data"]["CONTEXT_MANIFEST.json"])
        self.assertEqual(context["job"], job)
        self.assertIn("JOB_READ_MAP.md", packet["data"])

    def test_build_cannot_omit_matched_record_render(self):
        options = dict(self.options, record_render=None)
        frozen = MODULE.batch_digest(MODULE.prepare_batch(JOBS, **options))
        with self.assertRaisesRegex(ValueError, "matched --record-render"):
            MODULE.build_batch(JOBS, self.dest, frozen, **options)
        self.assertFalse(self.dest.exists())

    def test_method_reference_closure_and_backend_fixture_scope(self):
        data = {"methods/math/SKILL.md": b"[Required method](references/proof.md)"}
        with self.assertRaisesRegex(ValueError, "missing method/specimen reference"):
            MODULE.context_link_report(data)
        data["methods/math/references/proof.md"] = b"Exact proof method"
        data["external_backend/lean-exposition/site/tests/fixtures/captured.md"] = b"[Logical captured document](../long/record.md)"
        report = MODULE.context_link_report(data)
        self.assertEqual(len(report["links"]), 1)
        self.assertIn("external_backend/lean-exposition/site/tests/fixtures/captured.md", report["source_owner_provenance_leaves"])

    def test_source_bound_evidence_labels_are_preserved(self):
        packet = MODULE.prepare_batch([JOBS[0]], **self.options)[JOBS[0]]
        snapshot = json.loads(packet["data"]["EVIDENCE_SNAPSHOT.json"])
        states = {r["member"].split("/")[-1]: r["source_currentness"] for r in snapshot["receipts"]}
        self.assertEqual(states["current.json"], "current")
        self.assertNotEqual(states["stale.json"], "current")
        self.assertEqual(states["legacy.json"], "legacy_unbound")

    def test_cross_job_mutation_does_not_create_mixed_batch(self):
        original = MODULE.prepare
        calls = 0

        def mutate(job, **options):
            nonlocal calls
            packet = original(job, **options)
            calls += 1
            if calls == 1:
                self.write("research/requests/round4/common.md", "changed {title}\n{job}\n{boundary}\n")
            return packet

        with patch.object(MODULE, "prepare", side_effect=mutate), self.assertRaisesRegex(ValueError, "across batch"):
            MODULE.prepare_batch(JOBS, **self.options)

    def test_requests_render_and_catalog_has_no_review_quota_or_eq19_job(self):
        self.assertEqual(set(MODULE.JOBS), set(MODULE.FOCUS))
        self.assertEqual(set(MODULE.JOBS), set(MODULE.LITERATURE))
        self.assertEqual(set(MODULE.JOBS), set(MODULE.RETURNS))
        for job in MODULE.JOBS:
            text = MODULE.render_request(job, ROOT / "research/requests/round4")
            self.assertIn("docs/reasoning_record.md", text)
            self.assertIn("full substantive result inline", text)
            self.assertNotIn("01_integrated_review", job)


if __name__ == "__main__":
    unittest.main()
