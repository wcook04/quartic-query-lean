import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from lean_comments import strip_comments  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]


class StripComments(unittest.TestCase):
    def test_removes_line_block_doc_and_nested_comments(self):
        src = "/-! mod -/\n/-- doc /- nested -/ still -/\ntheorem a : 1 = 1 := rfl -- tail\n"
        self.assertEqual(strip_comments(src), "\n\ntheorem a : 1 = 1 := rfl \n")

    def test_keeps_markers_inside_strings_and_chars(self):
        src = 'def s := "-- not /- a comment"\ndef c := \'-\'\n'
        self.assertEqual(strip_comments(src), src)

    def test_primes_in_identifiers_are_not_char_literals(self):
        src = "theorem h' (l' : Nat) : l' = l' := rfl -- c\n"
        self.assertEqual(strip_comments(src), "theorem h' (l' : Nat) : l' = l' := rfl \n")

    def test_code_changes_remain_visible(self):
        a = "/- note -/\ntheorem t : 1 + 1 = 2 := rfl\n"
        self.assertNotEqual(strip_comments(a), strip_comments(a.replace("1 + 1", "2 + 0")))
        self.assertEqual(strip_comments(a), strip_comments(a.replace("note", "other")))

    def test_unterminated_comment_is_an_error(self):
        with self.assertRaises(ValueError):
            strip_comments("/- open\ntheorem t := rfl\n")

    def test_every_project_source_parses_and_keeps_its_declarations(self):
        for path in sorted((ROOT / "lean").rglob("*.lean")):
            if ".lake" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            code = strip_comments(text)
            for word in ("theorem ", "lemma ", "def ", "structure "):
                in_code = code.count("\n" + word) + code.count("\nprivate " + word)
                self.assertLessEqual(in_code, text.count(word), path)


if __name__ == "__main__":
    unittest.main()
