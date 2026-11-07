# OpenAI preprint source for the reading copy

The TeX and BibTeX files in this directory are unmodified copies of OpenAI's
[public source at the pinned revision](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/build).
The author remains OpenAI. The upstream [Apache 2.0 license](LICENSE.txt) permits
redistribution and adaptation. This directory adds the conversion manifest,
this notice and an illustration cropped from the published PDF. The HTML
conversion changes typesetting; it does not revise the authors' wording.

[manifest.json](manifest.json) pins every source and illustration by SHA-256,
the expanded TeX, the original PDF and its extracted layout. It records the
PDF's named destinations, citation numbering and reference text. The
illustration is a crop of page 6 at the recorded rectangle in PDF points;
the caption comes from the original TeX. Bibliography paragraphs come from
`pdftotext -layout`, joining wrapped lines and discretionary line-break
hyphens. The PDF remains the print authority and is available beside the HTML.

[The converter](../../tools/original_manuscript.py) uses the existing Pandoc
reader pipeline. It checks that adding source markers leaves the complete
Pandoc parse unchanged, preserves every formula node, applies the source's
section/theorem/equation counters, checks those numbers against the PDF's
named destinations and rejects unresolved references or remaining raw LaTeX.
The existing TeX math renderer then renders those formulas in the website.
The source's `mathtools` paired delimiters are expanded and display wrappers
are adapted for the website renderer; display content and numbers are retained.

The statement locations bind PDF layout coordinates to exact TeX source
paragraphs by their digest. They locate the published text associated with a
ledger entry; they do not turn the ledger's corrected or generalized wording
into the original author's wording. Page locations open the source paragraph
containing the start of each print page, or the figure/reference at that page;
native HTML reflows and has no physical page breaks.

A plain clone contains the complete input. Building requires Pandoc, with no
private source checkout or network download. Run `make reading-web` from the
repository root. To independently reproduce the PDF-derived reference text,
citation numbering, named destinations and figure pixels:

```sh
python3 tools/original_preprint.py /path/to/pinned-original.pdf --reading-source
python3 -m unittest discover -s tests -p 'test_original_manuscript.py'
```

These are mechanical source-preservation checks. They do not establish a full
manual PDF comparison or independent mathematical review. The separate
statement fidelity records retain their existing review scope.
