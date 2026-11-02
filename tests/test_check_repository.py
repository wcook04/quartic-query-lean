"""Exercise working and staged layout checks in isolated Git repositories."""

import importlib.util
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from zipfile import ZipFile


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
        self.manifest = {"format": "return-snapshots-v1", "snapshots": {}}
        for name in sorted(CHECKER.SNAPSHOT_IDS):
            files = {"README.md": "[sender-only](missing.md)\n"}
            if name == "1_statement_fidelity":
                files.update({"checks/example.py": "raise RuntimeError('do not run')\n",
                              "lean/Example.lean": "-- submitted source\n",
                              "LICENSE": "submitted license\n", "MANIFEST.sha256": "sender hash\n"})
            members = {}
            for member, content in files.items():
                self.write(f"{CHECKER.SNAPSHOT_ROOT}/{name}/{member}", content)
                data = content.encode()
                members[member] = {"size": len(data), "sha256": hashlib.sha256(data).hexdigest()}
            self.manifest["snapshots"][name] = {
                "archive": {"name": f"quartic_r2_{name}_return.zip", "sha256": "a" * 64},
                "members": members,
            }
        self.save_manifest()
        self.git("add", ".")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True)

    def write(self, path, content="evidence\n"):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)

    def save_manifest(self):
        self.write(CHECKER.SNAPSHOT_MANIFEST, json.dumps(self.manifest) + "\n")

    def errors(self, index=False, archive_dir=None):
        return CHECKER.check(CHECKER.GitView(self.root, index), archive_dir)

    def make_archives(self, archive_dir):
        for name, snapshot in self.manifest["snapshots"].items():
            path = Path(archive_dir) / snapshot["archive"]["name"]
            with ZipFile(path, "w") as archive:
                for member in snapshot["members"]:
                    archive.writestr(member, (self.root / CHECKER.SNAPSHOT_ROOT / name / member).read_bytes())
            snapshot["archive"]["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        self.save_manifest()

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

    def test_submitted_code_and_readme_are_accepted_as_verified_bytes(self):
        self.assertEqual([], self.errors())
        self.assertEqual([], self.errors(index=True))

    def test_unmanifested_members_are_rejected_even_if_they_are_evidence(self):
        for member in ("extra.py", "extra.md"):
            with self.subTest(member=member):
                path = f"{CHECKER.SNAPSHOT_ROOT}/1_statement_fidelity/{member}"
                self.write(path)
                self.assertTrue(any(path in e and "unmanifested" in e for e in self.errors()))
                self.git("add", path)
                (self.root / path).unlink()
                self.assertTrue(any(path in e and "unmanifested" in e for e in self.errors(index=True)))
                self.git("rm", "--cached", path)

    def test_unknown_snapshot_directory_is_rejected(self):
        path = f"{CHECKER.SNAPSHOT_ROOT}/8_unlisted/notes.md"
        self.write(path)
        self.assertTrue(any(path in e and "unmanifested" in e for e in self.errors()))

    def test_snapshot_byte_tampering_uses_staged_contents(self):
        path = f"{CHECKER.SNAPSHOT_ROOT}/1_statement_fidelity/checks/example.py"
        original = (self.root / path).read_text()
        self.write(path, "altered\n")
        self.git("add", path)
        self.write(path, original)
        self.assertEqual([], self.errors())
        self.assertTrue(any(path in e and "bytes differ" in e for e in self.errors(index=True)))

    def test_staged_manifest_cannot_be_masked_by_working_repair(self):
        path = f"{CHECKER.SNAPSHOT_ROOT}/1_statement_fidelity/README.md"
        record = self.manifest["snapshots"]["1_statement_fidelity"]["members"]["README.md"]
        original = record["sha256"]
        record["sha256"] = "b" * 64
        self.save_manifest()
        self.git("add", CHECKER.SNAPSHOT_MANIFEST)
        record["sha256"] = original
        self.save_manifest()
        self.assertEqual([], self.errors())
        self.assertTrue(any(path in e and "bytes differ" in e for e in self.errors(index=True)))

    def test_staged_snapshot_deletion_cannot_be_masked_by_working_restore(self):
        path = f"{CHECKER.SNAPSHOT_ROOT}/1_statement_fidelity/README.md"
        self.git("rm", "--cached", path)
        self.assertEqual([], self.errors())
        self.assertTrue(any(path in e and "member is missing" in e for e in self.errors(index=True)))

    def test_manifest_rejects_duplicate_keys_and_unsafe_member_paths(self):
        self.write(CHECKER.SNAPSHOT_MANIFEST, '{"format":"return-snapshots-v1","format":"return-snapshots-v1","snapshots":{}}')
        self.assertTrue(any("duplicate JSON key" in e for e in self.errors()))
        members = self.manifest["snapshots"]["1_statement_fidelity"]["members"]
        for path in ("../escape.py", ".", "/absolute.py", "subdir/../file.py"):
            with self.subTest(path=path):
                members[path] = {"size": 0, "sha256": hashlib.sha256(b"").hexdigest()}
                self.save_manifest()
                self.assertTrue(any("invalid member path" in e for e in self.errors()))
                del members[path]

    def test_manifest_cannot_admit_a_new_snapshot_root(self):
        self.manifest["snapshots"]["8_unlisted"] = self.manifest["snapshots"]["1_statement_fidelity"]
        self.save_manifest()
        self.assertTrue(any("snapshot IDs" in e for e in self.errors()))

    def test_manifested_generated_outputs_remain_forbidden(self):
        path = f"{CHECKER.SNAPSHOT_ROOT}/1_statement_fidelity/cache.pyc"
        self.write(path, "cached\n")
        data = (self.root / path).read_bytes()
        self.manifest["snapshots"]["1_statement_fidelity"]["members"]["cache.pyc"] = {
            "size": len(data), "sha256": hashlib.sha256(data).hexdigest(),
        }
        self.save_manifest()
        self.git("add", "-f", path)
        self.assertTrue(any(path in e and "output/cache" in e for e in self.errors()))

    def test_original_archives_bind_the_manifest_to_submitted_bytes(self):
        with tempfile.TemporaryDirectory() as archive_dir:
            self.make_archives(archive_dir)
            self.assertEqual([], self.errors(archive_dir=archive_dir))
            path = f"{CHECKER.SNAPSHOT_ROOT}/1_statement_fidelity/README.md"
            self.write(path, "changed together with manifest\n")
            data = (self.root / path).read_bytes()
            self.manifest["snapshots"]["1_statement_fidelity"]["members"]["README.md"] = {
                "size": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            }
            self.save_manifest()
            self.assertEqual([], self.errors())
            self.assertTrue(any("archive member differs" in e for e in self.errors(archive_dir=archive_dir)))

    def test_original_archive_hash_and_member_set_are_checked(self):
        with tempfile.TemporaryDirectory() as archive_dir:
            self.make_archives(archive_dir)
            snapshot = self.manifest["snapshots"]["1_statement_fidelity"]
            path = Path(archive_dir) / snapshot["archive"]["name"]
            with ZipFile(path, "a") as archive:
                archive.writestr("extra.txt", "extra")
            errors = self.errors(archive_dir=archive_dir)
            self.assertTrue(any("archive SHA-256 differs" in e for e in errors))
            self.assertTrue(any("archive member set differs" in e for e in errors))

    def test_archive_check_uses_staged_manifest(self):
        with tempfile.TemporaryDirectory() as archive_dir:
            self.make_archives(archive_dir)
            record = self.manifest["snapshots"]["1_statement_fidelity"]["archive"]
            original = record["sha256"]
            record["sha256"] = "b" * 64
            self.save_manifest()
            self.git("add", CHECKER.SNAPSHOT_MANIFEST)
            record["sha256"] = original
            self.save_manifest()
            self.assertEqual([], self.errors(archive_dir=archive_dir))
            self.assertTrue(any("archive SHA-256 differs" in e
                                for e in self.errors(index=True, archive_dir=archive_dir)))

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

    def test_contributor_and_agent_links_use_staged_contents(self):
        for path in ("CONTRIBUTING.md", "AGENTS.md"):
            with self.subTest(path=path):
                self.write(path, "[old](missing.md)\n")
                self.git("add", path)
                self.write(path, "[current](README.md)\n")
                self.assertEqual([], self.errors())
                self.assertTrue(any(path in e and "stale local link" in e
                                    for e in self.errors(index=True)))
                self.git("add", path)

    def test_contributor_guide_is_required_in_index(self):
        self.git("rm", "--cached", "CONTRIBUTING.md")
        self.assertEqual([], self.errors())
        self.assertTrue(any("CONTRIBUTING.md: required" in e
                            for e in self.errors(index=True)))

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
