"""Reader-facing contracts that a successful paper render alone cannot verify."""
import hashlib
import json
import shutil
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import build_reading_api as api


class ReadingEditionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.edition = api.Edition(api.ROOT)
        api.compile_edition(cls.edition)
        cls.reading = json.loads(cls.edition.resources["reading.json"])

    def resource(self, path):
        return json.loads(self.edition.resources[path])

    def test_follow_a_route_in_both_directions(self):
        routes = api.unique(self.reading["routes"], "id")
        route = routes["erased-zero"]
        reverse = self.resource("reverse.json")
        self.assertIn(route["id"], reverse["routes_by_passage"][route["reconstruction"]])
        for paper, loc in route["locations"].items():
            path = self.reading["papers"][paper]["path"]
            lines = self.edition.resources[path].decode().splitlines()
            start, end = loc["lines"]
            paragraph = "\n".join(lines[start - 1:end])
            self.assertIn(loc["quote"], paragraph)
            self.assertEqual(api.digest(paragraph.encode()), loc["sha256"])
        for label in route["lean"]:
            self.assertIn(route["id"], reverse["routes_by_target"][label])
            formal = self.resource("formal-sources.json")[label]
            lines = self.edition.resources[formal["source"]].decode().splitlines()
            for name, span in formal["ranges"].items():
                start, end = span["declaration"]
                self.assertIn(name.rsplit(".", 1)[-1], "\n".join(lines[start - 1:end]))
                self.assertIn(label, reverse["declarations"][name]["targets"])

    def test_board_tasks_and_their_bound_entrance(self):
        known, hidden, pointers = self.resource(self.reading["board_example"])["scenes"]
        self.assertEqual(known["selections"][0]["id"], self.reading["entrances"]["exposition"]["first_selection"])
        differences = [(r+1, c+1) for r, row in enumerate(known["original"]) for c, bit in enumerate(row)
                       if bit != known["alternative"][r][c]]
        self.assertEqual(differences, [(4, 1)])
        self.assertEqual(hidden["fixed_row_strategy"][2],
                         {"rows_read": 2, "queries_per_board": 8, "difference_seen": {"numerator": 2, "denominator": 4}})
        self.assertEqual(pointers["correct_target_bits"], [0, 0, 0])
        self.assertEqual(pointers["altered_target_bits"], [1, 0, 0])
        self.assertEqual(pointers["rival_target_bits"], [1, 1, 1])

    @unittest.skipUnless(shutil.which("pandoc"), "Pandoc needed for the web manuscript export")
    def test_whole_manuscripts_preserve_math_tables_destinations_and_sources(self):
        edition = api.Edition(api.ROOT)
        api.compile_edition(edition, web_manuscripts=True)
        papers = json.loads(edition.resources["reading.json"])["papers"]
        class Tags(HTMLParser):
            def handle_starttag(self, tag, attrs):
                tags.append((tag, dict(attrs)))
        for key in [*api.PAPERS, "verification"]:
            descriptor = papers[key]
            tags = []
            Tags().feed(edition.resources[descriptor["rendered"]["resource"]].decode())
            ids = [a["id"] for _, a in tags if "id" in a]
            self.assertEqual(len(ids), len(set(ids)))
            for _, a in tags:
                if a.get("href", "").startswith("#"):
                    self.assertIn(a["href"][1:], ids)
            figures = {a["data-resource"] for tag, a in tags if tag == "img"}
            self.assertEqual(figures, set(descriptor["assets"]))
            if key in ("exposition", "expert"):
                cited_keys = {k for _, a in tags for k in a.get("data-cites", "").split()}
                linked_refs = {a["href"] for _, a in tags if a.get("role") == "doc-biblioref"}
                self.assertTrue(cited_keys)
                self.assertTrue({"#ref-" + k for k in cited_keys} <= linked_refs)
                notes = {a["id"]: a["href"] for _, a in tags if a.get("role") == "doc-noteref"}
                backlinks = {a["href"] for _, a in tags if a.get("role") == "doc-backlink"}
                self.assertEqual(set(notes), {ref[1:] for ref in backlinks})
                self.assertTrue(notes)
                for ref, dest in notes.items():
                    self.assertRegex(dest, r"^#fn[0-9]+$")
                    self.assertEqual(ref, "fnref" + dest[3:])
            if key == "reconstruction":
                self.assertIn("ROOT-RESULT", ids)
                self.assertTrue(any(tag == "table" for tag, _ in tags))
                self.assertTrue(any(a.get("class") == "math display" for _, a in tags))
                self.assertTrue(any(a.get("data-paper") == "exposition" for _, a in tags))
            if key == "exposition":
                self.assertTrue(any(i.startswith("fnref") for i in ids))
                self.assertTrue(any(i.startswith("ref-") for i in ids))
                first = self.resource("selection/board.json")["scenes"][0]["selections"][0]
                start = first["lines"][0]
                self.assertTrue(any(int(a["data-l0"]) == start for _, a in tags if "data-l0" in a))

    def test_four_papers_and_distinct_coverage_units(self):
        self.assertEqual(set(self.reading["paper_ids"]), {*api.PAPERS, "original"})
        self.assertEqual(self.reading["supplement_ids"], ["verification"])
        original = self.reading["papers"]["original"]
        self.assertEqual(original["format"], "pdf")
        self.assertNotIn("resource", original)
        for paper, counts in self.reading["coverage"].items():
            rows = self.resource(f"selection/{paper}.json")
            self.assertEqual(len(rows), counts["selections"])
            self.assertEqual(counts["source_sha256"], self.resource("selection/index.json")["documents"][paper]["sha256"])
        statements = {r["id"]: r for r in self.edition.json("corpus/statements.json")}
        rows = self.resource("selection/original.json")
        self.assertEqual(sorted(r["statements"][0] for r in rows), sorted(statements))
        with tempfile.TemporaryDirectory() as directory:
            wrong = Path(directory) / "original.pdf"
            wrong.write_bytes(b"%PDF-other")
            with self.assertRaisesRegex(ValueError, "pinned release"):
                api.original_paper(self.edition, statements, wrong)
        statements["eq-21"] = {**statements["eq-21"], "source_line": 1}
        with self.assertRaisesRegex(ValueError, "coordinates changed"):
            api.original_paper(self.edition, statements)

    def test_every_reviewed_tie_has_its_own_native_type_and_axioms(self):
        for sid, path in self.reading["fidelity"].items():
            record = self.resource(path)
            for tie in record["lean"]:
                if tie["review_evidence"] != "current":
                    continue
                native = tie["inspection"]
                self.assertEqual(native["status"], "current", sid)
                self.assertEqual("lean/" + native["module"].replace(".", "/") + ".lean", tie["file"])
                self.assertTrue(native["type"].strip())
                self.assertIsInstance(native["axioms"], list)
            for probe in record["semantic_probes"]:
                self.assertEqual(probe["inspection"]["status"], "current")
                self.assertTrue(probe["authored_answer"])
        amended = self.resource("fidelity/lem-2.2.i.json")
        self.assertNotEqual(amended["ledger_history"]["earlier_ledger_wording"], amended["statement"])
        self.assertIn("R1-AF-00", [f["id"] for f in amended["ledger_history"]["adjudication_findings"]])

    def test_changed_inspector_withholds_current_types_and_axioms(self):
        edition = api.Edition(api.ROOT)
        inspector = "tools/ReadStatementEvidence.lean"
        edition.inputs[inspector] = edition.read(inspector) + b"\n"
        api.compile_edition(edition)
        headline = json.loads(edition.resources["fidelity/thm-1.1.json"])
        tie = next(t for t in headline["lean"] if t["declaration"].endswith(".theorem_1_1_unconditional"))
        self.assertEqual(tie["inspection"]["status"], "stale")
        self.assertNotIn("axioms", tie["inspection"])
        self.assertNotIn("type", tie["inspection"])
        self.assertNotIn(tie["declaration"], json.loads(edition.resources["axiom-audits.json"]))
        model = json.loads(edition.resources["fidelity/def-R.json"])
        self.assertTrue(all(p["authored_answer"] is None for p in model["semantic_probes"]))

    def test_feedback_is_qualified_and_attributed(self):
        self.assertEqual(set(self.reading["entrances"]), {*api.PAPERS, "original"})
        self.assertEqual(self.reading["video"], self.edition.json(api.ROUTES)["video"])
        statement = self.resource(self.reading["fidelity"]["def-R"])
        self.assertTrue(any(t["reviewed_by"] for t in statement["lean"]))
        probe = next(p for p in statement["semantic_probes"] if "quantifier" in p["declaration"])
        self.assertIn(probe["declaration"], self.resource(probe["receipt"])["declarations"])
        self.assertIn(probe["declaration"], self.resource("axiom-audits.json"))
        control = self.resource("checks.json")["lean/QuarticCorpus/Independent/Controls/shared_blind_spot.json"]
        self.assertEqual(control["role"], "negative_control")
        self.assertEqual(control["latest_receipt"]["negative_control"], "accepted_shared_bad_spec_blind_spot")
        self.assertEqual(self.resource("provenance.json")["routes"]["origin"], "ai_authored_navigation")

    def test_stale_or_ambiguous_selector_and_bad_video(self):
        for text in ("different", "quote and quote"):
            with self.assertRaisesRegex(ValueError, "expected one"):
                api.locate_quote(text, "quote", "expert")
        video = {"youtube_id": "abcdefghijk", "chapters": [{"start_seconds": 0, "route": "pivot"}]}
        self.assertEqual(api.video_entry(video, {"pivot"}), video)
        with self.assertRaisesRegex(ValueError, "chapter"):
            api.video_entry(video, {})
        video["chapters"] *= 2
        with self.assertRaisesRegex(ValueError, "chapter"):
            api.video_entry(video, {"pivot"})

    def test_wrong_pdf_cannot_enter_an_edition(self):
        accepted = self.edition.json(api.ROUTES)["print_edition"]
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            path = folder / accepted["files"]["expert"]["file"]
            path.parent.mkdir()
            path.write_bytes(b"%PDF-unrelated edition")
            with self.assertRaisesRegex(ValueError, "PDF differs|paper sources differ"):
                api.print_downloads(self.edition, folder, accepted)

    def test_export_retains_old_objects_and_refuses_mixed_editions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args):
                subprocess.run(["git", "-c", "user.email=test@example.com", "-c", "user.name=Test", *args],
                               cwd=root, check=True, capture_output=True)
            git("init")
            source = root / "paper.md"
            out = root / "output"
            def snapshot():
                edition = api.Edition(root)
                edition.resources["paper.md"] = edition.read("paper.md")
                api.export(edition, out)
                return json.loads((out / "index.json").read_bytes())
            source.write_bytes(b"first")
            git("add", "paper.md")
            git("commit", "-m", "first")
            first = snapshot()
            source.write_bytes(b"next")
            with self.assertRaisesRegex(ValueError, "differs"):
                snapshot()
            self.assertEqual(first, json.loads((out / "index.json").read_bytes()))
            git("commit", "-am", "next")
            second = snapshot()
            self.assertNotEqual(first["revision"], second["revision"])
            for manifest, expected in [(first, b"first"), (second, b"next")]:
                entry = manifest["resources"]["paper.md"]
                self.assertEqual((out / entry["href"]).read_bytes(), expected)
                self.assertEqual(entry["sha256"], hashlib.sha256(expected).hexdigest())
            self.assertEqual(snapshot(), second)
