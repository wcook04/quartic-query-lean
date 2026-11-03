import importlib.util
import json
from pathlib import Path
import re
import sys
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

    def test_unknown_label_is_an_error(self):
        with self.assertRaises(SystemExit):
            MODULE.paper_block("see [x][nope]\n", {}, "p")

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


if __name__ == "__main__":
    unittest.main()
