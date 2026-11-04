#!/usr/bin/env python3
"""Render the maintained reasoning record using the preserved round-three layout.

Requires Pandoc, Tectonic and Poppler. Render only a frozen manuscript; no source
edits or bibliography rewriting occur. Authored HTML anchors become PDF
destinations, and each directory link is retargeted to a reviewed file. Output and logs stay outside this checkout.
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
local submitted_header = Header
function Header(el)
  local heading = submitted_header and submitted_header(el) or el
  -- The following lemma's paragraph guard can otherwise strand this heading
  -- after the newly completed evaluator. Reserve room before both blocks.
  if pandoc.utils.stringify(el.content) == "5.1. Amplification with a predetermined query cap" then
    return {pandoc.RawBlock("latex", "\\Needspace{14\\baselineskip}"), heading}
  end
  return heading
end
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


# PDF navigation, merged from the two round-four repairs (07 and 08). Pandoc's
# LaTeX writer drops raw HTML anchors, so the 339 authored `<a id>` targets had
# no PDF destination and all 199 internal links were inert. Each anchor becomes
# an explicit hypertarget; anchor-only paragraphs collapse into one raw block so
# no empty paragraphs are added. hyperref turns a relative link ending in `/`
# into a remote-PDF action for `<dir>/.pdf`, which does not exist; each such
# directory link is retargeted to the file its label names. The manuscript bytes
# are unchanged.
DIRECTORY_TARGETS = {
    "../research/returns/funnel/2_short_expert_paper/": "paper.md",
    "../research/returns/funnel/3_examples_first_exposition/": "exposition.md",
    ("../research/returns/round3/members/02_forrelation_promise_circuit/"
     "quartic_r3_02_forrelation_promise_circuit_return/checks/"): "exact_example_checker.py",
    "../research/returns/round3/members/04_addressed_construction/": "README.md",
    "../research/returns/round3/members/08_reviewed/quartic_r3_08_return/checks/": "exact_checks.py",
}
ANCHOR = re.compile(r'<a\s+id="([\w.:-]+)"\s*>\s*</a>')
NAVIGATION_LAYOUT = r'''
local directory_targets = DIRECTORY_TARGETS_TABLE

-- Pandoc emits \\hyperref[id] (label) or \\hyperlink{id} (hypertarget) depending
-- on its version; provide both destinations at the authored position.
local function target(id)
  return "\\hypertarget{" .. id .. "}{}\\phantomsection\\label{" .. id .. "}"
end

function RawBlock(el)
  if not FORMAT:match("latex") or el.format ~= "html" then return nil end
  local id = el.text:match('^%s*<a%s+id="([%w_%.:%-]+)"%s*>%s*</a>%s*$')
  if id then return pandoc.RawBlock("latex", target(id)) end
end

function RawInline(el)
  if not FORMAT:match("latex") or el.format ~= "html" then return nil end
  local id = el.text:match('^%s*<a%s+id="([%w_%.:%-]+)"%s*>%s*</a>%s*$') or
             el.text:match('^%s*<a%s+id="([%w_%.:%-]+)"%s*>%s*$')
  if id then return pandoc.RawInline("latex", target(id)) end
end

function Para(el)
  if not FORMAT:match("latex") then return nil end
  local targets = {}
  for _, inline in ipairs(el.content) do
    if inline.t == "RawInline" and inline.format == "latex" and
       inline.text:match("^\\hypertarget{[%w_%.:%-]+}{}\\phantomsection\\label{[%w_%.:%-]+}$") then
      targets[#targets + 1] = inline.text
    elseif inline.t == "RawInline" and inline.format == "html" and
           inline.text:match("^%s*</a>%s*$") then
      -- The closing tag of an opening anchor converted above.
    elseif inline.t ~= "Space" and inline.t ~= "SoftBreak" then
      return nil
    end
  end
  if #targets > 0 then
    return pandoc.RawBlock("latex", table.concat(targets, "\n"))
  end
end

function Link(el)
  if not FORMAT:match("latex") then return nil end
  local replacement = directory_targets[el.target]
  if replacement then
    el.target = replacement
    return el
  end
end
'''


def navigation_filter():
    """The navigation Lua filter with the reviewed directory-link targets."""
    entries = ",\n".join(f"  [{json.dumps(link)}] = {json.dumps(link + name)}"
                         for link, name in sorted(DIRECTORY_TARGETS.items()))
    return NAVIGATION_LAYOUT.replace("DIRECTORY_TARGETS_TABLE", "{\n" + entries + "\n}")


def write_filters(stage):
    """Stage the submitted layout filter with its adaptations, then navigation."""
    layout = stage / "pdf_layout.lua"
    shutil.copyfile(LAYOUT / "pdf_layout.lua", layout)
    with layout.open("a") as handle:
        handle.write(CODE_LAYOUT)
    navigation = stage / "pdf_navigation.lua"
    navigation.write_text(navigation_filter(), encoding="utf-8")
    return [layout, navigation]


def navigation_inputs(ast, source):
    """Check anchors and links before rendering; refuse an unreviewed directory link."""
    nodes = list(walk(ast))
    links = [node["c"][2][0] for node in nodes if node.get("t") == "Link"]
    anchors = ANCHOR.findall(source.read_text(encoding="utf-8"))
    internal = [link[1:] for link in links if link.startswith("#")]
    directories = sorted({link for link in links if link.endswith("/") and "://" not in link})
    unreviewed = [link for link in directories if link not in DIRECTORY_TARGETS]
    if unreviewed:
        raise ValueError(f"directory links need a reviewed file target: {unreviewed}")
    missing = [link + DIRECTORY_TARGETS[link] for link in directories
               if not (source.parent / (link + DIRECTORY_TARGETS[link])).is_file()]
    if missing:
        raise ValueError(f"reviewed directory-link targets are missing: {missing}")
    dangling = sorted(set(internal) - set(anchors))
    if dangling:
        raise ValueError(f"internal links without an authored anchor: {dangling}")
    if len(anchors) != len(set(anchors)):
        raise ValueError("authored anchors are not unique")
    return {"authored_anchors": len(anchors), "internal_links": len(internal),
            "directory_links_retargeted": {link: link + DIRECTORY_TARGETS[link] for link in directories}}


def check_latex_navigation(tex_text, expected):
    """Every authored anchor is a LaTeX destination and no directory href remains."""
    targets = set(re.findall(r"\\hypertarget\{([^}]+)\}", tex_text))
    missing = sorted(set(expected) - targets)
    leftover = sorted(link for link in set(re.findall(r"\\href\{([^}]*/)\}", tex_text)) if "://" not in link)
    if missing or leftover:
        raise RuntimeError(f"PDF navigation incomplete: missing anchors {missing}, directory links {leftover}")
    return {"latex_hypertargets": len(targets & set(expected))}


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
    try:
        navigation = navigation_inputs(ast, source)
    except ValueError as error:
        parser.error(str(error))
    receipt = {
        "schema": "quartic-reasoning-record-render-v1", "source": str(source),
        "navigation": navigation,
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
                       "Headings immediately after HTML anchors/comments are recognized without source rewriting.",
                       "Authored HTML anchors become PDF destinations and reviewed directory links name files (round-four 07/08 merge)."],
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
        shutil.copyfile(LAYOUT / "pdf_header.tex", stage / "pdf_header.tex")
        write_filters(stage)
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
                "--lua-filter=" + str(stage / "pdf_navigation.lua"),
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
        receipt["navigation"].update(check_latex_navigation(
            tex.read_text(encoding="utf-8"), ANCHOR.findall(source.read_text(encoding="utf-8"))))
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
        destinations = set(re.findall(r'"([^"]+)"\s*$',
                                      command([binaries["pdfinfo"], "-dests", pdf], cwd=source.parent), re.M))
        absent = sorted(set(ANCHOR.findall(source.read_text(encoding="utf-8"))) - destinations)
        if absent:
            raise RuntimeError(f"{len(absent)} authored anchors are not PDF destinations: {absent[:10]}")
        receipt["navigation"]["pdf_named_destinations"] = len(destinations)
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
        broken = sorted(set(re.findall(
            r"[^\n]*(?:Hyper reference|Reference|Label)[^\n]*(?:undefined|multiply defined)[^\n]*", warnings)))
        if broken:
            raise RuntimeError(f"{len(broken)} unresolved or duplicate link targets: {broken[:5]}")
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
