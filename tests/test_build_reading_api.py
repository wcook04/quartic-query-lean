"""Reader-facing contracts that a successful paper render alone cannot verify."""
import hashlib
import json
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

    def test_feedback_is_qualified_and_attributed(self):
        self.assertEqual(set(self.reading["entrances"]), set(api.PAPERS))
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
