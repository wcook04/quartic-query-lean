import importlib.util
import json
from pathlib import Path
import re
import sys
import tempfile
from unittest import mock
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
SPEC = importlib.util.spec_from_file_location("build_lean_links", ROOT / "tools/build_lean_links.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

SOURCE = """namespace Top

/-- A definition. -/
def size : Nat :=
  3

theorem size_pos :
    0 < size := by
  decide

end Top
"""


class LeanLinksTests(unittest.TestCase):
    def test_theorem_link_stops_at_statement(self):
        self.assertEqual(MODULE.locate(SOURCE, ["Top.size_pos"], "x"), (7, 8))

    def test_statement_let_binding_does_not_end_the_statement(self):
        # The amplifier link once stopped at `let M := ...`, hiding every conclusion.
        source = ("theorem amp (g : Nat) :\n    let M := g + 1\n    (f : Nat → Nat) (x : Nat) →\n"
                  "    f (x + M) = f (M + x) := by\n  intro M f x\n  rw [Nat.add_comm]\n")
        self.assertEqual(MODULE.locate(source, ["amp"], "x"), (1, 4))

    def test_definition_link_covers_doc_and_body(self):
        self.assertEqual(MODULE.locate(SOURCE, ["Top.size"], "x"), (3, 5))

    def test_run_of_declarations_spans_first_to_last(self):
        self.assertEqual(MODULE.locate(SOURCE, ["Top.size_pos", "Top.size"], "x"), (3, 8))

    def test_missing_declaration_is_an_error(self):
        with self.assertRaises(SystemExit):
            MODULE.locate(SOURCE, ["Top.absent"], "x")

    def test_paper_block_lists_used_labels_only(self):
        links = {"a": {"url": "https://example/a"}, "b": {"url": "https://example/b"}}
        block = MODULE.paper_block("see [x][b] and [y][own]\n\n[own]: https://o\n", links, "p")
        self.assertEqual(block, "<!-- lean-links -->\n[b]: https://example/b\n<!-- /lean-links -->")

    def test_record_uses_registry_and_preserves_handwritten_links_and_provenance(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = root / MODULE.RECORD
            path.parent.mkdir()
            original = ("An [ordinary description][thm-headline], [literature][source], "
                        "and [old record](https://github.com/wcook04/quartic-query-lean/blob/"
                        "e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#old).\n\n"
                        "[source]: https://example.org/paper\n")
            path.write_text(original)
            links = {"thm-headline": {"url": "https://example.org/theorem#L1-L2"}}
            with mock.patch.object(MODULE, "ROOT", root):
                updated = MODULE.updated_paper(MODULE.RECORD, links)
            self.assertTrue(updated.startswith(original))
            self.assertIn("[thm-headline]: https://example.org/theorem#L1-L2", updated)
            self.assertEqual(updated.count("[source]: https://example.org/paper"), 1)
            self.assertIn("e9dfefbf11e6d1f380f122caa2349d4be78f2c1f", updated)
            path.write_text(updated)
            with mock.patch.object(MODULE, "ROOT", root):
                self.assertEqual(MODULE.updated_paper(MODULE.RECORD, links), updated)
                path.write_text(original + "\nUnknown [claim][not-registered].\n")
                with self.assertRaisesRegex(SystemExit, "unknown Lean link labels not-registered"):
                    MODULE.updated_paper(MODULE.RECORD, links)

    def test_record_links_pin_whole_document_and_check_optional_anchor(self):
        old = "a" * 40
        url = f"{MODULE.REPOSITORY}/blob/{old}/{MODULE.RECORD}"
        with mock.patch.object(MODULE, "at_commit", return_value=("blob", '<a id="known"></a>')):
            result = MODULE.pin_record_links(f"[record]({url}) [proof]({url}#known)", "paper")
            self.assertNotIn(old, result)
            self.assertIn(f"{MODULE.RECORD})", result)
            self.assertIn(f"{MODULE.RECORD}#known)", result)
            with self.assertRaisesRegex(SystemExit, "missing"):
                MODULE.pin_record_links(f"[proof]({url}#missing)", "paper")
            self.assertEqual(MODULE.pin_record_links(url + ".bak", "paper"), url + ".bak")

    def test_unknown_label_is_an_error(self):
        with self.assertRaises(SystemExit):
            MODULE.paper_block("see [x][nope]\n", {}, "p")

    def test_record_revision_is_independent_of_lean_revision(self):
        record_commit = "b" * 40
        url = f"{MODULE.REPOSITORY}/blob/{MODULE.COMMIT}/{MODULE.RECORD}#new-proof"
        with mock.patch.object(MODULE, "RECORD_COMMIT", record_commit), \
                mock.patch.object(MODULE, "at_commit", return_value=("blob", '<a id="new-proof"></a>')) as read:
            result = MODULE.pin_record_links(url, "paper")
            read.assert_called_once_with(MODULE.RECORD, record_commit)
            self.assertIn(f"/blob/{record_commit}/", result)
            self.assertNotIn(MODULE.COMMIT, result)
        with mock.patch.object(MODULE, "RECORD_COMMIT", record_commit), \
                mock.patch.object(MODULE, "at_commit", return_value=("blob", '<a id="other"></a>')):
            with self.assertRaisesRegex(SystemExit, "new-proof"):
                MODULE.pin_record_links(url, "paper")

    def test_registry_is_current_and_pinned_links_name_the_commit(self):
        registry, _ = MODULE.build()
        self.assertEqual(MODULE.render(registry), MODULE.OUTPUT.read_text(encoding="utf-8"))
        for label, entry in registry["links"].items():
            ref = MODULE.COMMIT if entry["pinned"] else "main"
            self.assertIn(f"/{ref}/{entry['path']}", entry["url"], label)
            if "lines" in entry:
                start, end = entry["lines"]
                self.assertTrue(re.search(rf"#L{start}(-L{end})?$", entry["url"]), label)

    def test_papers_carry_current_link_blocks(self):
        registry = json.loads(MODULE.OUTPUT.read_text(encoding="utf-8"))
        for paper in MODULE.PAPERS:
            text = (ROOT / paper).read_text(encoding="utf-8")
            self.assertEqual(MODULE.updated_paper(paper, registry["links"]), text, paper)
        for bibliography in MODULE.RECORD_BIBLIOGRAPHIES:
            text = (ROOT / bibliography).read_text(encoding="utf-8")
            self.assertEqual(MODULE.pin_record_links(text, bibliography), text, bibliography)


if __name__ == "__main__":
    unittest.main()
