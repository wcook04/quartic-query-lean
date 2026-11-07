"""Original source custody, numbering and native-reader location contracts."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from build_reading_api import Edition, ROOT
from original_manuscript import MANIFEST, SOURCE, numbered_labels, original_resources, source_files
from original_preprint import original_paper


@unittest.skipUnless(shutil.which("pandoc"), "Pandoc is required for native manuscript conversion")
class OriginalManuscriptTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.edition = Edition(ROOT)
        cls.statements = {r["id"]: r for r in cls.edition.json("corpus/statements.json")}
        cls.paper, cls.rows = original_paper(cls.edition, cls.statements)
        cls.fragment = original_resources(cls.edition, cls.paper, cls.rows)
        cls.html = cls.edition.resources["manuscripts/original.html"].decode()

    def test_vendored_bytes_and_license_are_exported_without_private_checkout(self):
        manifest = self.edition.json(MANIFEST)
        self.assertIn("Apache License", self.edition.resources[SOURCE + "/LICENSE.txt"].decode())
        self.assertEqual(self.paper["author"], "OpenAI")
        self.assertEqual(self.paper["format"], "pdf")
        self.assertIn("raw.githubusercontent.com/openai/math/", self.paper["url"])
        self.assertNotIn("/Users/", json.dumps(manifest))
        edition = Edition(ROOT)
        edition.inputs[SOURCE + "/sections/01-introduction.tex"] = b"An unapproved rewrite."
        with self.assertRaisesRegex(ValueError, "pinned bytes"):
            source_files(edition)

    def test_numbers_refs_and_figure_caption_come_from_original(self):
        self.assertIn('<ol type="i">', self.html)
        self.assertIn("Theorem 1.1", self.html)
        self.assertIn("Lemma A.5", self.html)
        self.assertIn(r"\tag{23}", self.html)
        self.assertIn('href="#thm:main">1.1</a>', self.html)
        self.assertIn('href="#eq:main-family">(2)</a>', self.html)
        self.assertIn('href="#ref-ABKRT21">3</a>', self.html)
        self.assertIn("Figure 1: The relevant cell of a winning column points outward to a zero", self.html)
        self.assertIn('data-resource="docs/original_source/outward-pointers.png"', self.html)
        self.assertNotIn("[eq:", self.html)
        self.assertIn("sec:exponent", self.fragment.ids)
        self.assertEqual(self.paper["rendered"]["checks"]["formula_count"], 528)
        self.assertFalse(self.paper["rendered"]["checks"]["manual_pdf_review"])

    def test_every_original_id_keeps_pdf_page_and_opens_source_passage(self):
        original, baseline = original_paper(Edition(ROOT), self.statements)
        text = self.edition.resources["manuscripts/original.tex"].decode().splitlines()
        rows = {r["id"]: r for r in self.rows}
        for old in baseline:
            row = rows[old["id"]]
            self.assertEqual(row["location"]["page"], old["location"]["page"])
            self.assertEqual(row["location"]["url"], old["location"]["url"])
            self.assertEqual(row["lines"], row["location"]["lines"])
            self.assertIn(row["location"]["anchor"], self.fragment.ids)
        row = rows["original/def-log-convention"]
        a, b = row["lines"]
        self.assertIn("logarithms to base two", " ".join(text[a-1:b]))
        row = rows["original/eq-21"]
        a, b = row["lines"]
        self.assertIn(r"\label{eq:capped-address}", " ".join(text[a-1:b]))

    def test_all_pages_have_usable_destinations_including_reference_only_page(self):
        self.assertEqual([r["page"] for r in self.paper["page_locations"]], list(range(1, 20)))
        for row in self.paper["page_locations"]:
            self.assertIn(row["anchor"], self.fragment.ids)
        self.assertEqual(self.paper["page_locations"][-1]["anchor"], "ref-Yao77")

    def test_counter_or_source_binding_drift_fails_closed(self):
        manifest, text = source_files(Edition(ROOT))
        destinations = deepcopy(manifest["destinations"])
        del destinations["equation.23"]
        with self.assertRaisesRegex(ValueError, "no PDF destination"):
            numbered_labels(text, destinations)
        edition = Edition(ROOT)
        changed = deepcopy(manifest)
        changed["statement_locations"]["def-log-convention"]["lines"] = [1, 2]
        edition.inputs[MANIFEST] = json.dumps(changed).encode()
        paper, rows = original_paper(edition, self.statements)
        with self.assertRaisesRegex(ValueError, "changed original source passage"):
            original_resources(edition, paper, rows)

    @unittest.skipUnless((ROOT / "site/node_modules/katex").exists(), "install site dependencies for actual KaTeX validation")
    def test_every_formula_renders_with_the_sites_actual_katex(self):
        script = r'''
const fs = require('node:fs');
const katex = require(process.cwd() + '/site/node_modules/katex');
const html = fs.readFileSync(0, 'utf8');
let count = 0;
for (const match of html.matchAll(/<span class="math (inline|display)">([\s\S]*?)<\/span>/g)) {
  const tex = match[2].replaceAll('&amp;', '&').replaceAll('&lt;', '<').replaceAll('&gt;', '>')
    .replace(/^\\[([]/, '').replace(/\\[)\]]$/, '');
  katex.renderToString(tex, {displayMode: match[1] === 'display', throwOnError: true, strict: 'ignore', trust: false});
  count++;
}
process.stdout.write(String(count));
'''
        count = subprocess.check_output(["node", "-e", script], input=self.html.encode(), cwd=ROOT)
        self.assertEqual(int(count), self.paper["rendered"]["checks"]["formula_count"])


if __name__ == "__main__":
    unittest.main()
