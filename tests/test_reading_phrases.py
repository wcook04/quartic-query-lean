"""Regression tests for phrase ties: location, overlap, binding and HTML marking."""
import copy
import json
from pathlib import Path
import shutil
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import reading_manuscripts as manuscripts  # noqa: E402
import reading_phrases as phrases  # noqa: E402

TEXT = ("Intro paragraph with $x$ and a phrase here.\n\n"
        "The bound $Q(f)\\le m$ holds for every input. The bound repeats later.\n\n"
        "| $a$ | $rqk$ | Reads for one address |\n| --- | --- | --- |\n| $b$ | $2$ | Reads twice |\n")


def tie(ident, start, end, **extra):
    return {"id": ident, "from": start, "to": end, **extra}


class LocateTests(unittest.TestCase):
    def setUp(self):
        self.formulas = phrases.math_spans(TEXT)

    def test_phrase_inside_one_paragraph(self):
        begin, end = phrases.locate(TEXT, tie("a", "The bound $Q(f)", "every input"), self.formulas)
        self.assertEqual(TEXT[begin:end], "The bound $Q(f)\\le m$ holds for every input")

    def test_repeated_from_quote_needs_after(self):
        with self.assertRaisesRegex(ValueError, "more than once in its paragraph"):
            phrases.locate(TEXT, tie("a", "The bound", "input"), self.formulas)
        begin, end = phrases.locate(TEXT, tie("a", "The bound", "later", after="every input. "), self.formulas)
        self.assertEqual(TEXT[begin:end], "The bound repeats later")

    def test_formula_cut_and_paragraph_break_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "cuts the formula"):
            phrases.locate(TEXT, tie("a", "Q(f)", "holds"), self.formulas)
        with self.assertRaisesRegex(ValueError, "paragraph break"):
            phrases.locate(TEXT, tie("a", "a phrase here.", "The bound $Q(f)"), self.formulas)
        with self.assertRaisesRegex(ValueError, "not found"):
            phrases.locate(TEXT, tie("a", "absent words", "here"), self.formulas)

    def test_table_phrase_is_marked_cell_by_cell(self):
        begin, end = phrases.locate(TEXT, tie("t", "| $a$ |", "Reads twice |"), self.formulas)
        cells = [TEXT[a:b] for a, b in phrases.segments(TEXT, begin, end, self.formulas)]
        self.assertEqual(cells, ["$a$", "$rqk$", "Reads for one address", "$b$", "$2$", "Reads twice"])

    def test_avoided_words_and_note_length(self):
        with self.assertRaisesRegex(ValueError, "avoid the word"):
            phrases.prose_check("note", "It changes the convention silently.")
        with self.assertRaisesRegex(ValueError, "words"):
            phrases.prose_check("note", "Too short.", phrases.NOTE_WORDS)


class FragmentTests(unittest.TestCase):
    def fragment(self, html, marks):
        fragment = manuscripts.Fragment("docs/p.md", {"docs/p.md": "p"}, [], "https://example.org/")
        fragment.feed(html)
        fragment.close()
        fragment.place_phrases(marks)
        return "".join(fragment.output)

    def test_markers_become_one_span_holding_whole_elements(self):
        html = "<p>A 0bound <em>here</em> <span class=\"math inline\">\\(x\\)</span> ends.</p>"
        out = self.fragment(html, {0: ("p-1", 3)})
        self.assertIn('<span class="phrase" data-phrase="p-1" data-tone="3">bound <em>here</em>', out)
        self.assertTrue(out.endswith("</span></span> ends.</p>"))

    def test_phrase_crossing_an_element_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "crosses an element boundary"):
            self.fragment("<p>A <em>0bound</em> here.</p>", {0: ("p-1", 0)})
        with self.assertRaisesRegex(ValueError, "not rendered"):
            self.fragment("<p>Plain.</p>", {0: ("p-1", 0)})

    def test_caption_alt_text_is_cleared_of_markers(self):
        out = self.fragment('<figure><figcaption>0Cap</figcaption></figure>', {0: ("c", 0)})
        self.assertIn('<span class="phrase" data-phrase="c" data-tone="0">Cap</span>', out)


@unittest.skipUnless(shutil.which("pandoc"), "Pandoc is not installed")
class PandocTests(unittest.TestCase):
    def test_markers_keep_the_parse(self):
        text = "Some *emphasis* and a phrase with $x^2$ here.\n"
        start = text.index("a phrase")
        end = text.index(" here")
        tree = manuscripts.located_document(text, "markdown", [(start, end, 0)])
        self.assertIn("0a", json.dumps(tree, ensure_ascii=False))

    def test_marker_inside_markup_is_rejected(self):
        text = "Intro.\n\n- first item\n- second item\n"
        start = text.index("- first")
        end = text.index(" item")
        with self.assertRaisesRegex(ValueError, "changed the Pandoc parse"):
            manuscripts.located_document(text, "markdown", [(start, end, 0)])


class SourceTests(unittest.TestCase):
    """The maintained sources are bound to the manuscript bytes and complete."""
    def test_sources_bind_their_manuscripts(self):
        import hashlib
        for paper in phrases.PAPERS:
            data = json.loads((ROOT / phrases.SOURCE.format(paper=paper)).read_text())
            manuscript = (ROOT / data["manuscript"]).read_bytes()
            self.assertEqual(data["manuscript_sha256"], hashlib.sha256(manuscript).hexdigest(), paper)
            named = {row["name"] for t in data["ties"] for row in t["lean"]}
            self.assertEqual(set(data["titles"]), named, paper)
            self.assertEqual(set(data["notes"]), named, paper)
            self.assertLessEqual(len(data["topics"]), phrases.MAX_TOPICS)

    def test_overlap_is_rejected(self):
        data = json.loads((ROOT / phrases.SOURCE.format(paper="expert")).read_text())
        text = (ROOT / data["manuscript"]).read_text()
        formulas = phrases.math_spans(text)
        first = data["ties"][0]
        begin, end = phrases.locate(text, first, formulas)
        clash = copy.deepcopy(first)
        clash["id"] = "clash"
        with self.assertRaisesRegex(ValueError, "overlap"):
            phrases.check_overlaps("expert", [(begin, end, first), (*phrases.locate(text, clash, formulas), clash)])
        with self.assertRaisesRegex(ValueError, "overlapping"):
            manuscripts.phrase_marked(text, [(begin, end, 0), (begin + 1, end, 1)])


if __name__ == "__main__":
    unittest.main()
