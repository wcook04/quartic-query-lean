#!/usr/bin/env python3
"""Render the maintained reasoning record using the preserved round-three layout.

Requires Pandoc, Tectonic and Poppler. Render only a frozen manuscript; no source
edits or bibliography rewriting occur. Output and logs stay outside this checkout.
The PDF still requires page-image review; process success is not visual acceptance.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
LAYOUT = ROOT / ("research/returns/round3/members/02_forrelation_promise_circuit/"
                 "quartic_r3_02_forrelation_promise_circuit_return/checks")
READER = ("markdown+tex_math_dollars+tex_math_single_backslash+pipe_tables+raw_tex"
          "-blank_before_header-superscript-subscript")
DEFAULT_OUTPUT = ROOT.parent / "_builds/quartic-r3/render"

# Adapt the submitted Code handler: all Lean identifiers need break opportunities,
# not just hexadecimal hashes. Let Pandoc escape each shaped Unicode string.
CODE_LAYOUT = r'''
local submitted_para = Para
local submitted_table = Table
function Table(el)
  local table = submitted_table(el) or el
  local gutter = pandoc.utils.stringify(el):find("Quartic coefficient", 1, true) and 9 or 6
  -- Keep comparison rows distinct at the existing font size, including cells
  -- whose prose wraps. Scope this to tables rather than changing math arrays.
  return {pandoc.RawBlock("latex", "\\begingroup\n" ..
    "\\renewcommand{\\arraystretch}{1.18}\n" ..
    "\\setlength{\\tabcolsep}{" .. gutter .. "pt}\n" ..
    "\\setlength{\\extrarowheight}{4pt}"), table,
    pandoc.RawBlock("latex", "\\endgroup")}
end
local function argument_backlink(el)
  return el.t == "Para" and #el.content > 0 and
    el.content[1].t == "Strong" and
    pandoc.utils.stringify(el.content[1]) == "Argument:"
end
function Para(el)
  -- The submitted generic bold-paragraph Needspace would push a one-line
  -- backlink away from the quotation it documents.
  if argument_backlink(el) then return el end
  return submitted_para(el)
end
function Pandoc(doc)
  local blocks = pandoc.List()
  local i, grouped = 1, 0
  while i <= #doc.blocks do
    local block, following = doc.blocks[i], doc.blocks[i + 1]
    if block.t == "BlockQuote" and following and argument_backlink(following) then
      -- Retain Pandoc's actual Header node (and its link target), but give the
      -- whole catalogue entry one consistent external gap. A local displayed
      -- paragraph heading avoids the standard run-in heading's variable skips.
      local at = #blocks
      while at > 0 and blocks[at].t == "RawBlock" do at = at - 1 end
      local prefix = pandoc.List()
      if at > 0 and blocks[at].t == "Header" and blocks[at].level == 4 then
        for n = at, #blocks do prefix:insert(blocks[n]) end
        for n = #blocks, at, -1 do blocks:remove(n) end
      end
      blocks:insert(pandoc.RawBlock("latex", "\\par\\addvspace{0.75\\baselineskip}\n" ..
        "\\begin{samepage}\n\\makeatletter\n" ..
        "\\renewcommand{\\paragraph}{\\@startsection{paragraph}{4}{\\z@}" ..
        "{0pt}{0.4\\baselineskip}{\\normalfont\\normalsize\\bfseries}}\n" ..
        "\\makeatother"))
      for _, item in ipairs(prefix) do blocks:insert(item) end
      blocks:insert(block)
      blocks:insert(pandoc.RawBlock("latex", "\\nopagebreak[4]"))
      blocks:insert(following)
      blocks:insert(pandoc.RawBlock("latex", "\\end{samepage}"))
      grouped, i = grouped + 1, i + 2
    else
      blocks:insert(block)
      i = i + 1
    end
  end
  doc.blocks = blocks
  io.stderr:write("catalogue_backlink_groups=" .. grouped .. "\n")
  return doc
end
local function breakable(text, code)
  local pieces = {}
  local run = 0
  for _, point in utf8.codes(text) do
    local char = utf8.char(point)
    local tex = pandoc.write(pandoc.Pandoc({pandoc.Plain({pandoc.Code(char)})}), "latex")
    tex = tex:match("^\\texttt{(.*)}%s*$") or tex
    if char == " " then tex = " " end
    run = run + 1
    if char:match("[%s%._,/:;()]") or run >= 12 then
      tex = tex .. "\\allowbreak{}"
      run = 0
    end
    pieces[#pieces + 1] = tex
  end
  local content = table.concat(pieces)
  return pandoc.RawInline("latex", code and ("\\texttt{" .. content .. "}") or content)
end
function Code(el)
  return breakable(el.text, true)
end
function Str(el)
  if utf8.len(el.text) >= 12 and
     (el.text:match("[_./={}\\]") or el.text:match("^%x+$")) then
    return breakable(el.text, false)
  end
end
'''


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reserve(path, gib):
    if shutil.disk_usage(path).free < gib * 1024 ** 3:
        raise RuntimeError(f"Fewer than {gib:g} GiB free at {path}; rendering stopped")


def walk(value):
    if isinstance(value, dict):
        yield value
        for item in value.values():
            yield from walk(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk(item)


def command(argv, *, cwd, log=None, timeout=600):
    run = subprocess.run(list(map(str, argv)), cwd=cwd, capture_output=True,
                         text=True, timeout=timeout)
    if log:
        log.write_text(run.stdout + run.stderr, encoding="utf-8")
    if run.returncode:
        raise RuntimeError(f"Command exited {run.returncode}: {argv}\n{run.stdout}{run.stderr}")
    return run.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT / "docs/reasoning_record.md")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--bibliography", type=Path, action="append", default=[])
    parser.add_argument("--min-free-gib", type=float, default=8)
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args()
    source = args.source.resolve(strict=True)
    output = args.output_dir.resolve()
    if output == ROOT or ROOT in output.parents:
        parser.error("--output-dir must be outside the source checkout")
    if args.min_free_gib < 8:
        parser.error("--min-free-gib must preserve at least 8 GiB")
    binaries = {name: shutil.which(name)
                for name in ("pandoc", "tectonic", "pdfinfo", "pdftoppm", "pdftotext")}
    if not all(binaries.values()):
        parser.error(f"missing rendering programs: {[k for k, v in binaries.items() if not v]}")
    source_hash = digest(source)
    ast = json.loads(command([binaries["pandoc"], source, "--from=" + READER, "--to=json"],
                             cwd=source.parent))
    nodes = list(walk(ast))
    citations = sorted({citation["citationId"] for node in nodes if node.get("t") == "Cite"
                        for citation in node["c"][0]})
    bibliographies = [p.resolve(strict=True) for p in args.bibliography]
    if citations and not bibliographies and "bibliography" not in ast.get("meta", {}):
        parser.error("Pandoc citation nodes found: supply --bibliography or manuscript bibliography metadata")
    receipt = {
        "schema": "quartic-reasoning-record-render-v1", "source": str(source),
        "renderer_sha256": digest(Path(__file__)),
        "source_sha256": source_hash, "reader": READER,
        "ast_counts": dict(Counter(node["t"] for node in nodes if "t" in node)),
        "citation_ids": citations, "citeproc": bool(citations),
        "explicit_bibliographies": {str(p): digest(p) for p in bibliographies},
        "layout_sources": {str(LAYOUT / name): digest(LAYOUT / name)
                           for name in ("render_section.py", "pdf_header.tex", "pdf_layout.lua")},
        "adaptation": ["Tectonic replaces unavailable XeLaTeX; original Pandoc layout filter and header reused.",
                       "Both dollar and single-backslash TeX math are parsed as math.",
                       "Latin Modern default text and the original DejaVu Sans Mono font file are selected through TeX packages.",
                       "Submitted Code break treatment extends to all identifiers and source-type spans without changing text.",
                       "Catalogue quotations and their Argument backlinks are kept together; one-line backlinks do not inherit generic bold-paragraph Needspace.",
                       "Comparison tables retain their font size and gain scoped row spacing to separate multiline cells.",
                       "Catalogue entry headings receive a consistent external gap; the quartic-route comparison reserves a larger horizontal gutter.",
                       "Section-specific Needspace and seven-column widths remain the submitted layout.",
                       "Headings immediately after HTML anchors/comments are recognized without source rewriting."],
        "tools": {name: {"path": path, "version": command([path, "--version"], cwd=source.parent).strip()}
                  for name, path in binaries.items() if name in {"pandoc", "tectonic"}},
        "visual_acceptance": "pending_page_image_review",
    }
    if args.preflight_only:
        print(json.dumps(receipt, indent=2))
        return 0
    output.mkdir(parents=True, exist_ok=True)
    reserve(output, args.min_free_gib)
    receipt["status"] = "rendering"
    # An interrupted retry must not leave an earlier success receipt looking
    # like evidence for the latest invocation.
    (output / "render.json").write_text(json.dumps(receipt, indent=2) + "\n")
    # The operation marker is invoked once by the authoring caller immediately
    # before this command, as required by the host PDF skill.
    with tempfile.TemporaryDirectory(prefix="render-", dir=output) as temporary:
        stage = Path(temporary)
        for name in ("pdf_header.tex", "pdf_layout.lua"):
            shutil.copyfile(LAYOUT / name, stage / name)
        with (stage / "pdf_layout.lua").open("a") as handle:
            handle.write(CODE_LAYOUT)
        # A text subscript occurs outside math in a retained source title. Keep
        # its printed meaning using LaTeX's actual subscript command.
        with (stage / "pdf_header.tex").open("a") as handle:
            handle.write("\n\\usepackage{newunicodechar}\n"
                         "\\usepackage{etoolbox}\n"
                         "\\emergencystretch=6em\n"
                         "\\AtBeginEnvironment{quote}{\\sloppy}\n"
                         "\\AtBeginEnvironment{itemize}{\\sloppy}\n"
                         "\\newunicodechar{₂}{\\textsubscript{2}}\n"
                         "\\newunicodechar{≥}{\\ensuremath{\\geq}}\n"
                         "\\newunicodechar{∎}{\\ensuremath{\\blacksquare}}\n"
                         "\\AtBeginDocument{\\let\\setminus\\smallsetminus}\n")
        tex = stage / "reasoning_record.tex"
        argv = [binaries["pandoc"], source, "--from=" + READER, "--standalone", "--to=latex",
                "--lua-filter=" + str(stage / "pdf_layout.lua"),
                "--include-in-header=" + str(stage / "pdf_header.tex"),
                "-V", "monofont=DejaVuSansMono.ttf",
                "-V", "fontsize=11pt", "-V", "geometry:margin=24mm",
                "-V", "colorlinks=true", "-V", "urlcolor=blue", "-o", tex]
        if citations:
            argv.append("--citeproc")
        for bibliography in bibliographies:
            argv.extend(["--bibliography", bibliography])
        receipt["pandoc_command"] = list(map(str, argv))
        command(argv, cwd=source.parent, log=output / "pandoc.log")
        reserve(output, args.min_free_gib)
        receipt["tectonic_command"] = [binaries["tectonic"], "--keep-logs", "--keep-intermediates",
                                        "--outdir", str(stage), str(tex)]
        try:
            command(receipt["tectonic_command"], cwd=source.parent, log=output / "tectonic.log")
        finally:
            for name in ("reasoning_record.tex", "reasoning_record.log"):
                if (stage / name).exists():
                    shutil.copyfile(stage / name, output / name)
        if digest(source) != source_hash:
            raise RuntimeError("Manuscript changed during rendering; PDF not promoted")
        for path, expected in {**receipt["layout_sources"],
                               **receipt["explicit_bibliographies"]}.items():
            if digest(Path(path)) != expected:
                raise RuntimeError(f"Rendering input changed during execution: {path}")
        pdf = stage / "reasoning_record.pdf"
        receipt["pdfinfo"] = command([binaries["pdfinfo"], pdf], cwd=source.parent)
        boxes = ET.fromstring(command([binaries["pdftotext"], "-bbox", pdf, "-"], cwd=source.parent))
        outside = []
        count = 0
        pages = list(boxes.iter("{http://www.w3.org/1999/xhtml}page"))
        for number, page in enumerate(pages, 1):
            width, height = float(page.attrib["width"]), float(page.attrib["height"])
            for word in page.iter("{http://www.w3.org/1999/xhtml}word"):
                count += 1
                a = word.attrib
                if (float(a["xMin"]) < 0 or float(a["yMin"]) < 0
                        or float(a["xMax"]) > width or float(a["yMax"]) > height):
                    outside.append({"page": number, "word": word.text, "box": a})
        receipt["page_box_check"] = {"pages": len(pages), "words": count,
                                     "outside_page": outside}
        if outside:
            raise RuntimeError(f"{len(outside)} extracted word boxes extend outside page bounds")
        warnings = (output / "tectonic.log").read_text()
        texlog = output / "reasoning_record.log"
        if texlog.exists():
            warnings += texlog.read_text(errors="replace")
        receipt["layout_diagnostics"] = sorted(set(re.findall(
            r"[^\n]*(?:Overfull|Missing character|Undefined control|undefined citations)[^\n]*",
            warnings, flags=re.I)))
        destination = output / pdf.name
        shutil.copyfile(pdf, destination)
        receipt["pdf"] = str(destination)
        receipt["pdf_sha256"] = digest(destination)
        receipt["source_unchanged"] = True
        receipt["status"] = "rendered_requires_visual_review"
        (output / "render.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
