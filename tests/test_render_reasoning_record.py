import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("render_reasoning_record", ROOT / "tools/render_reasoning_record.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
PANDOC = shutil.which("pandoc")
RECORD = ROOT / "docs/reasoning_record.md"

FIXTURE = """# Title

<a id="BLOCK-ANCHOR"></a>
<!-- passage:BLOCK-ANCHOR -->
See [the inline target](#INLINE-ANCHOR) and [the block target](#BLOCK-ANCHOR).
The [short expert draft](../research/returns/funnel/2_short_expert_paper/) is linked.
<!-- /passage:BLOCK-ANCHOR -->

Text with <a id="INLINE-ANCHOR"></a>an inline anchor and [a site](https://example.org/dir/).
"""


def link(target):
    return {"t": "Link", "c": [["", [], []], [], [target, ""]]}


def latex(source, folder):
    filters = MODULE.write_filters(Path(folder))
    argv = [PANDOC, str(source), "--from=" + MODULE.READER, "--to=latex"]
    argv += ["--lua-filter=" + str(path) for path in filters]
    return subprocess.run(argv, cwd=source.parent, capture_output=True, text=True, check=True).stdout


class NavigationInputTests(unittest.TestCase):
    def source(self, folder, text):
        path = Path(folder) / "docs/record.md"
        path.parent.mkdir(parents=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_unreviewed_directory_link_is_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            source = self.source(folder, "")
            with self.assertRaisesRegex(ValueError, "reviewed file target"):
                MODULE.navigation_inputs({"blocks": [link("../elsewhere/")]}, source)

    def test_reviewed_directory_link_needs_its_file(self):
        with tempfile.TemporaryDirectory() as folder:
            source = self.source(folder, "")
            with self.assertRaisesRegex(ValueError, "targets are missing"):
                MODULE.navigation_inputs({"blocks": [link("../research/returns/funnel/2_short_expert_paper/")]},
                                         source)

    def test_internal_link_needs_an_authored_anchor(self):
        with tempfile.TemporaryDirectory() as folder:
            source = self.source(folder, '<a id="A"></a>\n')
            self.assertEqual(MODULE.navigation_inputs({"blocks": [link("#A")]}, source)["internal_links"], 1)
            with self.assertRaisesRegex(ValueError, "without an authored anchor"):
                MODULE.navigation_inputs({"blocks": [link("#B")]}, source)

    def test_latex_check_rejects_missing_targets_and_directory_hrefs_only(self):
        good = "\\hypertarget{A}{}\\phantomsection\\label{A} \\href{https://example.org/dir/}{x}"
        self.assertEqual(MODULE.check_latex_navigation(good, ["A"]), {"latex_hypertargets": 1})
        with self.assertRaises(RuntimeError):
            MODULE.check_latex_navigation(good, ["A", "B"])
        with self.assertRaises(RuntimeError):
            MODULE.check_latex_navigation(good + "\\href{../dir/}{y}", ["A"])


@unittest.skipUnless(PANDOC, "Pandoc is required to run the Lua filters")
class FilterTests(unittest.TestCase):
    def test_fixture_anchors_become_destinations_and_directory_link_names_a_file(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "docs/record.md"
            source.parent.mkdir()
            source.write_text(FIXTURE, encoding="utf-8")
            tex = latex(source, folder)
        for anchor in ("BLOCK-ANCHOR", "INLINE-ANCHOR"):
            self.assertIn(f"\\hypertarget{{{anchor}}}{{}}\\phantomsection\\label{{{anchor}}}", tex)
        self.assertIn("../research/returns/funnel/2_short_expert_paper/paper.md", tex)
        self.assertNotIn("2_short_expert_paper/}", tex)
        self.assertIn("https://example.org/dir/", tex)
        self.assertNotIn("<a id", tex)

    def test_actual_record_reaches_every_anchor_without_changing_its_bytes(self):
        before = hashlib.sha256(RECORD.read_bytes()).hexdigest()
        correspondence = json.loads((ROOT / "docs/reasoning_record_correspondence.json").read_text())
        self.assertEqual(before, correspondence["record_sha256"])
        ast = json.loads(subprocess.run([PANDOC, str(RECORD), "--from=" + MODULE.READER, "--to=json"],
                                        capture_output=True, text=True, check=True).stdout)
        navigation = MODULE.navigation_inputs(ast, RECORD)
        self.assertEqual((navigation["authored_anchors"], navigation["internal_links"]), (365, 282))
        self.assertEqual(len(navigation["directory_links_retargeted"]), 5)
        with tempfile.TemporaryDirectory() as folder:
            tex = latex(RECORD, folder)
        anchors = MODULE.ANCHOR.findall(RECORD.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.check_latex_navigation(tex, anchors), {"latex_hypertargets": 365})
        self.assertEqual(hashlib.sha256(RECORD.read_bytes()).hexdigest(), before)

    def test_every_recorded_passage_keeps_its_anchor(self):
        # Papers, the comparator map and the correspondence link to these ids;
        # moving a passage must keep its anchor.
        correspondence = json.loads((ROOT / "docs/reasoning_record_correspondence.json").read_text())
        anchors = set(MODULE.ANCHOR.findall(RECORD.read_text(encoding="utf-8")))
        missing = sorted(p["id"] for p in correspondence["passages"] if p["id"] not in anchors)
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
