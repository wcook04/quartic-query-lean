import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MODULE = load("round5", ROOT / "tools/build_round5_packets.py")
URL = "https://github.com/wcook04/quartic-query-lean/blob/main/"


class RoundFiveTests(unittest.TestCase):
    def write(self, name, text, base=None):
        path = (base or self.root) / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text if isinstance(text, bytes) else text.encode())
        return path

    def git(self, *args):
        subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        base = Path(self.temp.name)
        self.root, self.annexes, self.dest = base / "repo", base / "annexes", base / "out"
        for name in MODULE.REPOSITORY_FILES:
            self.write(name, f"fixture {name}\n")
        self.write("docs/reasoning_record.md", '# Record\n\n<a id="upper"></a>\nThe accepted text.\n')
        self.write("docs/expert_companion.md", "# Companion\n\n![Column](figures/column.svg)\n\n"
            f"See [the record]({URL}docs/reasoning_record.md#upper) and [statement]({URL}lean/QuarticCorpus/Unconditional/Challenge.lean#L1-L1).\n")
        self.write("docs/figures/column.svg", "<svg/>")
        self.write("docs/exposition.md", "# Exposition\n\nSee [overview](#exposition).\n")
        for name in MODULE.NAVIGATION_FILES:
            self.write(name, "{}" if name.endswith(".json") else "# Navigation\n")
        for path in MODULE.EXEMPLARS.values():
            self.write(f"{MODULE.EXEMPLAR_ROOT}/{path}", "Exemplar about another theorem.\n")
        self.write("research/returns/round3/attachments/input_10.txt", "PRIVATE SESSION TEXT")
        self.write("research/adjudication/round4_papers.md", "Editorial review naming a reader.")
        self.git("init", "-q")
        self.git("-c", "user.email=t@example.org", "-c", "user.name=t", "add", "-A")
        self.git("-c", "user.email=t@example.org", "-c", "user.name=t", "commit", "-q", "-m", "fixture")
        accepted = MODULE.digest((self.root / "docs/reasoning_record.md").read_bytes())
        self.write(MODULE.REVIEW_RECEIPT, json.dumps({"record_sha256": accepted}))
        self.write("docs/reasoning_record.md", '# Record\n\n<a id="upper"></a>\nThe edited text.\n')
        paper = base / "paper"
        self.write("source.pdf", b"%PDF-preprint", paper)
        self.write("extracted.md", "Preprint text.\n", paper)
        slugs = {slug for job in MODULE.JOBS for slug in MODULE.LITERATURE[job]}
        for slug in slugs:
            self.write(f"{slug}/extracted.md", "Literature text.\n", self.annexes)
            self.write(f"{slug}/source.pdf", b"%PDF-literature", self.annexes)
            self.write(f"{slug}/annex_notes.json", '{"url": "/Users/someone/private.pdf"}', self.annexes)
        pdfs = {name: self.write(f"{name}.pdf", b"%PDF-" + name.encode(), base) for name in ("expert", "exposition", "record")}
        self.options = dict(root=self.root, requests_dir=ROOT / "research/requests/round5", annexes=self.annexes,
            paper_annex=paper, expert_pdf=pdfs["expert"], exposition_pdf=pdfs["exposition"], record_pdf=pdfs["record"])
        mock = patch.object(MODULE.round4, "pdf_reading_sources", return_value=({}, {"links": []}))
        mock.start()
        self.addCleanup(mock.stop)

    def test_build_writes_five_audited_archives_index_and_never_overwrites(self):
        paths = MODULE.build_batch(list(MODULE.JOBS), self.dest, **self.options)
        self.assertEqual(len(paths), 5)
        for path in paths:
            MODULE.check_packets.audit(path)
            with zipfile.ZipFile(path) as archive:
                names = set(archive.namelist())
                readme = archive.read("READ_ME_FIRST.md").decode()
                self.assertIn("repository/docs/expert_companion.pdf", names)
                self.assertIn("repository/docs/figures/column.svg", names)
                self.assertIn("findings.json", readme)
                MODULE.check_readme_links(readme, {n: b"" for n in names})
        audit = json.loads((self.dest / "batch-audit.json").read_bytes())
        self.assertEqual([row["job"] for row in audit["archives"]], list(MODULE.JOBS))
        self.assertTrue((self.dest / "INDEX.md").is_file())
        with self.assertRaisesRegex(FileExistsError, "new output folder"):
            MODULE.build_batch(list(MODULE.JOBS), self.dest, **self.options)

    def test_figures_with_bracketed_captions_and_their_sources_enter_the_packet(self):
        # Three round-five figures were missing because their captions held `X[1]`.
        self.write("docs/exposition.md", "# Exposition\n\n![Board: $X_2[1]=0$.](figures/board.svg){width=100%}\n")
        self.write("docs/figures/board.svg", "<svg/>")
        self.write("docs/figures/board.tex", "% tikz")
        names = MODULE.figure_sources(self.root)
        self.assertEqual(names, ["docs/figures/board.svg", "docs/figures/board.tex", "docs/figures/column.svg"])
        files = MODULE.inputs("exposition_for_students", **self.options)
        self.assertIn("repository/docs/figures/board.svg", files)
        self.assertIn("repository/docs/figures/board.tex", files)

    def test_private_sources_reader_file_and_annex_metadata_are_excluded(self):
        packet = MODULE.prepare("long_record_navigation", **self.options)
        blobs = b"".join(packet["data"].values()) + packet["request"].encode()
        self.assertNotIn(b"PRIVATE SESSION TEXT", blobs)
        self.assertNotIn(b"naming a reader", blobs)
        self.assertNotIn(b"/Users/someone", blobs)
        self.assertFalse(any(name.endswith("annex_notes.json") for name in packet["data"]))

    def test_named_reader_in_a_draft_fails_closed(self):
        patterns = self.root / "private_reader_patterns.txt"
        patterns.write_text("# private\n(?<!Example, )\\bAda\\b(?! Example)\n", encoding="utf-8")
        original = MODULE.READER_LEAKS
        MODULE.READER_LEAKS = MODULE.reader_leak_patterns(patterns)
        try:
            self.write("docs/exposition.md", "# Exposition\n\nWritten for Ada, who asked for the path.\n")
            with self.assertRaisesRegex(ValueError, "names a private reader"):
                MODULE.prepare("expert_referee_short", **self.options)
            self.write("docs/exposition.md", "# Exposition\n\nCites Ada Example and a coauthor.\n")
            MODULE.prepare("expert_referee_short", **self.options)
        finally:
            MODULE.READER_LEAKS = original

    def test_link_map_resolves_targets_and_flags_reader_visible_defects(self):
        _, report = MODULE.resolve_draft_links(self.root)
        rows = {row["link"]: row for row in report["links"]}
        self.assertTrue(rows[URL + "docs/reasoning_record.md#upper"]["anchor_found"])
        self.assertTrue(rows[URL + "lean/QuarticCorpus/Unconditional/Challenge.lean#L1-L1"]["line_range_valid"])
        self.assertEqual(report["problem_count"], 0)
        self.write("docs/exposition.md", f"[gone]({URL}docs/reasoning_record.md#missing) [far]({URL}lean/Challenge.lean#L1-L900)\n")
        self.assertEqual(MODULE.resolve_draft_links(self.root)[1]["problem_count"], 2)
        self.write("docs/exposition.md", "![Missing](figures/none.svg)\n")
        with self.assertRaisesRegex(ValueError, "missing draft link target"):
            MODULE.resolve_draft_links(self.root)

    def test_record_since_pdf_diff_and_hash_binding(self):
        packet = MODULE.prepare("expert_referee_short", **self.options)
        status = json.loads(packet["data"]["SOURCE_STATUS.json"])
        self.assertFalse(status["record"]["markdown_matches_accepted_review"])
        self.assertEqual(status["record"]["changed_lines"], 2)
        self.assertIn(b"+The edited text.", packet["data"]["repository/docs/reasoning_record.since_pdf.diff"])
        self.assertIn("repository/docs/expert_companion.pdf", status["drafts"])
        self.assertEqual(packet["manifest"]["drafts"], status["drafts"])

    def test_freeze_digest_detects_changed_drafts(self):
        frozen = MODULE.batch_digest(MODULE.prepare_batch(["quantum_mechanism"], **self.options))
        self.write("docs/expert_companion.md", "# Companion revised\n")
        with self.assertRaisesRegex(ValueError, "freeze digest"):
            MODULE.build_batch(["quantum_mechanism"], self.dest, frozen, **self.options)
        self.assertFalse(self.dest.exists())

    def test_missing_literature_original_fails_instead_of_being_invented(self):
        slug = MODULE.LITERATURE["classical_mechanism"][0]
        (self.annexes / slug / "source.pdf").unlink()
        with self.assertRaisesRegex(ValueError, "cited-only"):
            MODULE.prepare("classical_mechanism", **self.options)

    def test_maintained_requests_name_no_reader_and_render_for_every_job(self):
        self.assertEqual(set(MODULE.JOBS), set(MODULE.LITERATURE))
        self.assertEqual(set(MODULE.JOBS), set(MODULE.CITED_ONLY_BY_JOB))
        for job in MODULE.JOBS:
            text = MODULE.render_request(job, ROOT / "research/requests/round5")
            self.assertIn("findings.json", text)
            self.assertIn("lean_link", text)
            for pattern in MODULE.READER_LEAKS:
                self.assertIsNone(pattern.search(text), (job, pattern.pattern))
            for slug in MODULE.LITERATURE[job]:
                self.assertIn(slug, MODULE.CATALOG)


if __name__ == "__main__":
    unittest.main()
