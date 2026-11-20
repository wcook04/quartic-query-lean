import json
import pathlib
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from lean_comments import strip_comments  # noqa: E402
import build_corpus  # noqa: E402
import record_comment_migration as migration  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
PREFIX = "def ab : Nat := 1\ndef a (b : Nat) := 0\ndef b : Nat := 0\n"


def hashes(data):
    return {"lean/Probe.lean": migration.sha(data)}


def accepts(before, after):
    old, new = before.encode(), after.encode()
    with mock.patch.object(migration, "blob", lambda _commit, _path: old):
        try:
            migration.compare("base", hashes(old), hashes(new), lambda _path: new)
        except ValueError:
            return False
    return True


class StripComments(unittest.TestCase):
    def test_comments_become_one_space_and_keep_line_breaks(self):
        src = "/-! mod -/\n/-- doc /- nested -/\nstill -/\ntheorem a : 1 = 1 := rfl -- tail\n"
        self.assertEqual(strip_comments(src), " \n \n\ntheorem a : 1 = 1 := rfl  \n")

    def test_keeps_markers_inside_strings_chars_raw_strings_and_guillemets(self):
        for src in ['def s := "-- not /- a comment"\n', "def c := '-'\n",
                    'def s := r#"a" -- x"#\n', 'def s := r"/- x -/"\n', "def «--x» : Nat := 0\n"]:
            self.assertEqual(strip_comments(src), src, src)

    def test_primes_in_identifiers_are_not_char_literals(self):
        src = "theorem h' (l' : Nat) : l' = l' := rfl -- c\n"
        self.assertEqual(strip_comments(src), "theorem h' (l' : Nat) : l' = l' := rfl  \n")

    def test_unterminated_forms_are_errors(self):
        for src in ["/- open\ntheorem t := rfl\n", 'def s := r#"open\n', "def «open : Nat := 0\n"]:
            with self.assertRaises(ValueError):
                strip_comments(src)


class CommentOnlyComparison(unittest.TestCase):
    def test_code_changes_hidden_from_the_first_lexer_are_rejected(self):
        cases = [('def s := r#"a" -- old"#\n', 'def s := r#"a" -- changed"#\n'),
                 ("def «--x» : Nat := 0\n", "def «--x» : Nat := 1\n"),
                 (PREFIX + "def t := a/- separator -/b\n", PREFIX + "def t := ab\n"),
                 ('def s := r#"a"/- old -/"b"#\n', 'def s := r#"a"/- changed -/"b"#\n'),
                 ('def s := "-- old /- text"\n', 'def s := "-- changed /- text"\n'),
                 ("def c := '-'\n", "def c := '/'\n"),
                 ("@[simp] theorem t : 0 = 0 := rfl\n", "@[refl] theorem t : 0 = 0 := rfl\n")]
        for before, after in cases:
            self.assertFalse(accepts(before, after), before)

    def test_moving_code_between_lines_is_rejected(self):
        before = "/- A\n -/\ndef x := 1\n/- B -/\ndef y := 2\n"
        after = "/- A -/\ndef x := 1\n/- B\n -/\ndef y := 2\n"
        self.assertFalse(accepts(before, after))

    def test_guard_msgs_files_are_rejected(self):
        self.assertFalse(accepts("/-- info: 1 -/\n#guard_msgs in #eval 1\n",
                                 "/-- info: 2 -/\n#guard_msgs in #eval 1\n"))

    def test_comment_edits_are_accepted(self):
        self.assertTrue(accepts("/- a /- old -/ b -/\ndef n := 1 -- x\n",
                                "/- a /- new text -/ b -/\ndef n := 1 -- y\n"))


class MigrationReceipts(unittest.TestCase):
    def receipt(self, commit, old, new):
        return {"kind": migration.KIND, "status": "passed", "from_commit": commit,
                "from_source_hashes": hashes(old), "to_source_hashes": hashes(new),
                "from_snapshot_sha256": build_corpus.canonical_sha256(hashes(old)),
                "to_snapshot_sha256": build_corpus.canonical_sha256(hashes(new)), "changed": {}}

    def trusted(self, records, current):
        with tempfile.TemporaryDirectory() as name:
            corpus = pathlib.Path(name) / "corpus"
            (corpus / "migrations").mkdir(parents=True)
            for index, record in enumerate(records):
                (corpus / "migrations" / f"comment-migration-{index}.json").write_text(json.dumps(record))
            with mock.patch.object(build_corpus, "CORPUS", corpus):
                return build_corpus.migrated_snapshots(hashes(current))

    def test_a_receipt_whose_map_disagrees_with_its_digest_is_ignored(self):
        old, middle, current = b"def n := 0\n", b"def n := 1 -- a\n", b"def n := 1 -- b\n"
        bad = self.receipt("x", old, middle)
        bad["to_snapshot_sha256"] = build_corpus.canonical_sha256(hashes(current))
        self.assertEqual(self.trusted([bad], current), set())

    def test_receipts_are_never_chained(self):
        old, middle, current = b"def n := 0\n", b"def n := 1 -- a\n", b"def n := 1 -- b\n"
        reached = self.trusted([self.receipt("x", old, middle), self.receipt("y", middle, current)], current)
        self.assertEqual(reached, {build_corpus.canonical_sha256(hashes(middle))})

    def test_every_project_source_scans(self):
        for path in sorted((ROOT / "lean").rglob("*.lean")):
            if ".lake" not in path.parts:
                text = path.read_text(encoding="utf-8")
                self.assertEqual(strip_comments(text).count("\n"), text.count("\n"), path)


if __name__ == "__main__":
    unittest.main()
