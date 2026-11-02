"""Exercise the archive safety boundary without running submitted programs."""

import importlib.util
from pathlib import Path
import stat
import tempfile
import unittest
from zipfile import ZipFile, ZipInfo


SPEC = importlib.util.spec_from_file_location(
    "intake_round3_returns", Path(__file__).resolve().parents[1] / "tools/intake_round3_returns.py"
)
intake = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(intake)


class ExtractionTests(unittest.TestCase):
    def check_rejected(self, entries):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archive = root / "return.zip"
            with ZipFile(archive, "w") as output:
                for name, content in entries:
                    output.writestr(name, content)
            with self.assertRaises(ValueError):
                intake.unpack(archive, root / "out")
            self.assertFalse((root / "out").exists())

    def test_extracts_regular_files_and_hashes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with ZipFile(root / "return.zip", "w") as output:
                output.writestr("nested/file.txt", b"evidence\n")
            manifest = intake.unpack(root / "return.zip", root / "out")
            self.assertEqual((root / "out/nested/file.txt").read_bytes(), b"evidence\n")
            self.assertEqual(manifest, [{"path": "nested/file.txt", **intake.digest(b"evidence\n")}])

    def test_rejects_traversal_and_collisions_before_writing(self):
        self.check_rejected([("good.txt", "data"), ("../outside", "bad")])
        self.check_rejected([("A.txt", "one"), ("a.txt", "two")])
        self.check_rejected([("folder\\file", "bad")])

    def test_rejects_symlinks(self):
        link = ZipInfo("link")
        link.create_system = 3
        link.external_attr = (stat.S_IFLNK | 0o777) << 16
        self.check_rejected([(link, "../outside")])


if __name__ == "__main__":
    unittest.main()
