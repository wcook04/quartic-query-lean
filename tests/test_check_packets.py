"""Audit archive contracts without private inputs or live packet outputs."""

from contextlib import redirect_stderr, redirect_stdout
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import warnings
import zipfile


TOOLS = Path(__file__).resolve().parents[1] / "tools"
SPEC = importlib.util.spec_from_file_location("check_packets", TOOLS / "check_packets.py")
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class PacketAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.payload = {"repository/research/adjudication/adjudication.json": b"{}\n",
                        "repository/research/returns/adjudication.json": b"{}\n"}
        self.manifest = {
            "packet": "a_job", "source_paper": "a source revision",
            "members": [dict(member=name, source="/unavailable/historical/source",
                             bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
                        for name, data in self.payload.items()],
        }

    def write_zip(self, name="packet.zip", request=b"Read this first.\n", manifest=None,
                  extras=(), omit=()):
        path = self.root / name
        entries = [("READ_ME_FIRST.md", request),
                   ("manifest.json", json.dumps(self.manifest).encode() if manifest is None else manifest),
                   *self.payload.items(), *extras]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            with zipfile.ZipFile(path, "w") as archive:
                for member, data in entries:
                    if member not in omit:
                        archive.writestr(member, data)
        return path

    def test_all_manifest_variants_aliases_and_renamed_zip(self):
        for additions in ({}, {"repository_commit": "abc"},
                          {"repository_commit": "abc", "campaign": "round2", "future": True}):
            with self.subTest(additions=additions):
                self.manifest.update(additions)
                path = self.write_zip(name="renamed.zip")
                before = path.read_bytes()
                self.assertEqual(("a_job", 2), CHECKER.audit(path))
                self.assertEqual(before, path.read_bytes())
                self.assertEqual([path], list(self.root.iterdir()))

    def test_opaque_generated_and_git_source_labels(self):
        for source in ("generated", "/absent/repo@origin/main:papers/main.md"):
            self.manifest["members"][0]["source"] = source
            self.assertEqual(("a_job", 2), CHECKER.audit(self.write_zip()))

    def test_payload_corruption_and_wrong_byte_count(self):
        name = next(iter(self.payload))
        self.payload[name] = b"[]\n"
        with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
            CHECKER.audit(self.write_zip())
        self.payload[name] = b"longer"
        with self.assertRaisesRegex(ValueError, "byte length mismatch"):
            CHECKER.audit(self.write_zip())

    def test_manifest_coverage_and_duplicates(self):
        path = self.write_zip(extras=[("unexpected.txt", b"extra")])
        with self.assertRaisesRegex(ValueError, "unlisted in manifest"):
            CHECKER.audit(path)
        path = self.write_zip(omit=[next(iter(self.payload))])
        with self.assertRaisesRegex(ValueError, "missing from ZIP"):
            CHECKER.audit(path)
        self.manifest["members"].append(self.manifest["members"][0])
        with self.assertRaisesRegex(ValueError, "duplicate or reserved"):
            CHECKER.audit(self.write_zip())

    def test_required_request_and_manifest(self):
        for name in CHECKER.RESERVED:
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, "missing required"):
                CHECKER.audit(self.write_zip(omit=[name]))
        with self.assertRaisesRegex(ValueError, "empty"):
            CHECKER.audit(self.write_zip(request=b" \n"))

    def test_bad_json_and_manifest_shapes(self):
        for raw in (b"{", b"[]", b"null", b"{}"):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                CHECKER.audit(self.write_zip(manifest=raw))
        for rows in ({}, [], ["bad"], [{"member": 4}]):
            self.manifest["members"] = rows
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                CHECKER.audit(self.write_zip())

    def test_bad_manifest_row_fields(self):
        row = self.manifest["members"][0]
        for field, values in {"bytes": [True, -1, "3"], "sha256": [None, "bad", "x" * 64],
                              "source": [None, ""]}.items():
            original = row[field]
            for value in values:
                row[field] = value
                with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                    CHECKER.audit(self.write_zip())
            row[field] = original

    def test_unsafe_and_duplicate_archive_names(self):
        for name in ("/absolute", "../outside", "a/../outside", "./relative", "a//b",
                     "C:/file", "a\\b", "directory/", "manifest.json", "MANIFEST.JSON"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                CHECKER.audit(self.write_zip(extras=[(name, b"bad")]))

    def test_batch_continues_after_failure_and_deduplicates_paths(self):
        good = self.write_zip("z-good.ZIP")
        self.write_zip("a-bad.zip", manifest=b"{")
        (self.root / "notes.md").write_text("not a ZIP")
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            result = CHECKER.main([str(self.root), str(good)])
        self.assertEqual(1, result)
        self.assertEqual(1, out.getvalue().count("PASS"))
        self.assertIn("a-bad.zip", err.getvalue())

    def test_empty_directory_missing_file_and_non_zip_fail(self):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            self.assertEqual(1, CHECKER.main([str(self.root)]))
            self.assertEqual(1, CHECKER.main([str(self.root / "missing.zip")]))
            bad = self.root / "bad.zip"
            bad.write_text("not a ZIP")
            self.assertEqual(1, CHECKER.main([str(bad)]))
        self.assertIn("no ZIPs found", err.getvalue())

    def test_directory_error_does_not_skip_explicit_zip(self):
        good = self.write_zip()
        out, err = io.StringIO(), io.StringIO()
        with patch.object(Path, "iterdir", side_effect=PermissionError("unreadable directory")):
            with redirect_stdout(out), redirect_stderr(err):
                self.assertEqual(1, CHECKER.main([str(self.root), str(good)]))
        self.assertIn("PASS", out.getvalue())
        self.assertIn("unreadable directory", err.getvalue())

    def test_broken_deflate_stream_does_not_abort_batch(self):
        good = self.write_zip("z-good.zip")
        bad = self.root / "a-broken.zip"
        with zipfile.ZipFile(good) as source, zipfile.ZipFile(bad, "w", zipfile.ZIP_DEFLATED) as dest:
            for name in source.namelist():
                dest.writestr(name, source.read(name))
        with zipfile.ZipFile(bad) as archive:
            info = archive.getinfo(next(iter(self.payload)))
        data = bytearray(bad.read_bytes())
        offset = info.header_offset
        # Local header: fixed 30 bytes, then filename and extra-field lengths.
        offset += 30 + int.from_bytes(data[offset + 26:offset + 28], "little") + int.from_bytes(data[offset + 28:offset + 30], "little")
        data[offset] = 7  # Reserved DEFLATE block type, guaranteed decoder error.
        bad.write_bytes(data)
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            self.assertEqual(1, CHECKER.main([str(self.root)]))
        self.assertIn("a-broken.zip", err.getvalue())
        self.assertIn("z-good.zip", out.getvalue())

    def test_real_review_builder_contract(self):
        spec = importlib.util.spec_from_file_location("review_builder", TOOLS / "build_research_packets.py")
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        # Exercise every real job with temporary source inputs and real templates.
        inputs = {"intake": self.root / "intake", "papers_dir": self.root / "papers",
                  "paper_annex": self.root / "annex", "lean_dir": self.root / "lean"}
        inputs["papers_dir"].mkdir()
        (inputs["papers_dir"] / "citation.pdf").write_bytes(b"fixture citation")
        for job in builder.JOBS:
            for path in builder.members(job, **inputs).values():
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"fixture source\n")
            with redirect_stdout(io.StringIO()):
                builder.build(job, self.root, **inputs)
            packet, count = CHECKER.audit(self.root / f"quartic_{job}.zip")
            self.assertEqual(job, packet)
            self.assertEqual(len(builder.members(job, **inputs)), count)


if __name__ == "__main__":
    unittest.main()
