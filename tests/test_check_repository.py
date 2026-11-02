"""Exercise working and staged layout checks in isolated Git repositories."""

import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location("check_repository", Path(__file__).resolve().parents[1] / "tools/check_repository.py")
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-q")
        for path in CHECKER.REQUIRED:
            self.write(path, "")
        self.write(".gitignore", ".lake/\n/build/\n__pycache__/\n*.zip\n")
        self.write("README.md", "[tool](tools/check_repository.py) [license](LICENSE)\n")
        self.git("add", ".")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True)

    def write(self, path, content="evidence\n"):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)

    def errors(self, index=False):
        return CHECKER.check(CHECKER.GitView(self.root, index))

    def test_current_roles_and_future_lean_topics(self):
        for path in ["research/intake/source.txt", "research/intake/search.json", "lean/QuarticQuery/New/Topic.lean", "tools/README.md", "tests/test_future.py", ".github/workflows/check.yml"]:
            self.write(path)
        self.assertEqual([], self.errors())

    def test_lean_package_is_optional_until_published(self):
        self.assertEqual([], self.errors())
        self.assertEqual([], self.errors(index=True))

    def test_git_paths_with_newlines_are_not_split(self):
        self.write("research/a\nb.txt")
        self.git("add", ".")
        self.assertEqual([], self.errors())
        self.assertEqual([], self.errors(index=True))

    def test_code_in_research_is_rejected(self):
        self.write("research/intake/extract.py")
        self.assertTrue(any("executable code" in e for e in self.errors()))

    def test_retired_source_locations_cannot_return(self):
        for path in sorted(CHECKER.RETIRED):
            with self.subTest(path=path):
                self.write(path)
                self.assertTrue(any("superseded source location" in e for e in self.errors()))
                (self.root / path).unlink()

    def test_funnel_request_is_required_in_index(self):
        path = "research/requests/funnel/5_reader_and_film.md"
        self.git("rm", "--cached", path)
        self.assertEqual([], self.errors())
        self.assertTrue(any(path + ": required" in e for e in self.errors(index=True)))

    def test_unowned_root_file_is_rejected(self):
        self.write("extract.py")
        self.assertTrue(any("root file" in e for e in self.errors()))

    def test_ignored_outputs_are_not_traversed(self):
        self.write("lean/.lake/packages/mathlib/Bad.py")
        self.write("build/snapshot.zip")
        self.write("tools/__pycache__/bad.pyc")
        self.assertEqual([], self.errors())

    def test_forced_tracked_outputs_are_rejected(self):
        for path in ["lean/.lake/output.olean", "build/result.json", "packet.zip"]:
            self.write(path)
            self.git("add", "-f", path)
        self.assertEqual(3, len(self.errors()))
        self.assertEqual(3, len(self.errors(index=True)))

    def test_stale_readme_link(self):
        self.write("README.md", "[old](research/missing.json)\n")
        self.assertTrue(any("stale local link" in e for e in self.errors()))

    def test_staged_readme_is_checked_despite_working_repair(self):
        self.write("README.md", "[old](missing.md)\n")
        self.git("add", "README.md")
        self.write("README.md", "[valid](LICENSE)\n")
        self.assertEqual([], self.errors())
        self.assertTrue(any("stale local link" in e for e in self.errors(index=True)))

    def test_staged_addition_is_used_despite_unstaged_removal(self):
        self.write("research/new.txt")
        self.write("README.md", "[new](research/new.txt)\n")
        self.git("add", ".")
        (self.root / "research/new.txt").unlink()
        self.assertEqual([], self.errors(index=True))
        self.assertTrue(any("stale local link" in e for e in self.errors()))

    def test_staged_deletion_cannot_be_masked_by_untracked_restore(self):
        self.git("rm", "--cached", "LICENSE")
        self.assertTrue(any("LICENSE: required" in e for e in self.errors(index=True)))
        self.assertEqual([], self.errors())

    def test_staged_request_deletion_cannot_be_masked_by_working_restore(self):
        for name in ("common", "boundaries", "1_understand_the_paper",
                     "2_ground_in_literature", "3_lean_and_comparator"):
            with self.subTest(request=name):
                path = f"research/requests/review/{name}.md"
                self.git("rm", "--cached", path)
                self.assertTrue(any(f"{path}: required" in e for e in self.errors(index=True)))
                self.assertEqual([], self.errors())
                self.git("add", path)

    def test_deleted_optional_file_is_not_a_candidate(self):
        self.write("research/old.txt")
        self.git("add", "research/old.txt")
        self.git("rm", "-f", "research/old.txt")
        self.assertEqual([], self.errors())
        self.assertEqual([], self.errors(index=True))

    def test_nested_readme_relative_links_and_external_urls(self):
        self.write("tools/README.md", "[root](../README.md) [external](https://example.com/no-file) [anchor](#usage)\n")
        self.assertEqual([], self.errors())

    def test_local_link_cannot_escape_repository(self):
        self.write("README.md", "[private](../private.md)\n")
        self.assertTrue(any("escapes repository" in e for e in self.errors()))

    def test_symlink_is_rejected_in_both_views(self):
        (self.root / "research").mkdir(exist_ok=True)
        (self.root / "research/link.txt").symlink_to("../LICENSE")
        self.git("add", "research/link.txt")
        self.assertTrue(any("regular files" in e for e in self.errors()))
        (self.root / "research/link.txt").unlink()
        self.write("research/link.txt")
        self.assertTrue(any("regular files" in e for e in self.errors(index=True)))
        self.assertEqual([], self.errors())

    def test_non_git_directory_fails(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaises(RuntimeError):
                CHECKER.GitView(root)


if __name__ == "__main__":
    unittest.main()
