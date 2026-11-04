"""Check the paper renderer's argument handling without running Pandoc or Tectonic."""

import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest import mock
import json

MODULE = Path(__file__).resolve().parents[1] / "tools/render_papers.py"
SPEC = importlib.util.spec_from_file_location("render_papers", MODULE)
RENDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RENDER)


class ParseArgsTest(unittest.TestCase):
    def test_default_renders_both_papers_beside_the_checkout(self):
        outputs = RENDER.parse_args([])
        self.assertEqual(["expert", "exposition"], list(outputs))
        for paper, out in outputs.items():
            self.assertEqual(RENDER.ROOT.parent / "_builds/quartic-r4/render" / paper, out)

    def test_single_paper_uses_the_output_dir_itself(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = RENDER.parse_args(["--paper", "expert", "--output-dir", tmp])
            self.assertEqual({"expert": Path(tmp).resolve()}, out)

    def test_all_papers_get_subfolders(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = RENDER.parse_args(["--output-dir", tmp])
            self.assertEqual(Path(tmp).resolve() / "exposition", out["exposition"])

    def test_output_inside_the_checkout_is_refused(self):
        for target in (RENDER.ROOT, RENDER.ROOT / "build"):
            with self.assertRaises(SystemExit):
                RENDER.parse_args(["--paper", "exposition", "--output-dir", str(target)])

    def test_unknown_paper_is_refused(self):
        with self.assertRaises(SystemExit):
            RENDER.parse_args(["--paper", "record"])


class ReceiptTest(unittest.TestCase):
    def test_failed_retry_invalidates_old_success_receipt(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            (out / "render.json").write_text('{"status": "rendered_requires_visual_review"}')
            with mock.patch.object(RENDER, "input_hashes", return_value={"source": "hash"}), \
                 mock.patch.object(RENDER, "build_figures", side_effect=RuntimeError("failed render")):
                with self.assertRaises(RuntimeError):
                    RENDER.render("expert", out)
            self.assertEqual("rendering", json.loads((out / "render.json").read_text())["status"])


class ConfigurationTest(unittest.TestCase):
    def test_no_absolute_user_paths(self):
        self.assertNotIn("/Users/", MODULE.read_text())

    def test_pandoc_commands_name_the_papers(self):
        out = Path("/tmp/out")
        expert = RENDER.pandoc_command("expert", out, out / "figures", out / "e.tex")
        exposition = RENDER.pandoc_command("exposition", out, out / "figures", out / "x.tex")
        self.assertIn(str(RENDER.DOCS / "expert_companion.md"), expert)
        self.assertIn(f"--csl={out / 'numeric.csl'}", expert)
        self.assertIn(str(RENDER.DOCS / "exposition.md"), exposition)
        self.assertTrue(RENDER.NUMERIC_CSL.lstrip().startswith("<?xml"))


if __name__ == "__main__":
    unittest.main()
