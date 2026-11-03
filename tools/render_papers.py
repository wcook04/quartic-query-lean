#!/usr/bin/env python3
"""Render the two papers, docs/expert_companion.md and docs/exposition.md, to PDF.

Compiles each paper's TikZ figures with Tectonic (the PDF goes to the output
directory, an SVG copy next to the source so GitHub shows it), then renders the
Markdown with Pandoc and Tectonic in the shared paper style. Requires pandoc,
tectonic and pdftocairo (Poppler). The PDFs, LaTeX, figure PDFs and logs stay in
the output directory, outside the checkout.

    python3 tools/render_papers.py [--paper expert|exposition|all] [--output-dir DIR]

With --output-dir and --paper all, each paper gets a subfolder of DIR; with one
paper, DIR is that paper's folder.
"""

import argparse
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BUILDS = ROOT.parent / "_builds/quartic-r4/render"
PAPERS = ("expert", "exposition")

# (source folder, figure names) for each paper.
FIGURES = {
    "expert": (DOCS / "figures", ["expert_column", "expert_planted"]),
    "exposition": (DOCS / "figures/exposition",
                   ["fig1_column", "fig2_board", "fig3_tournament", "fig4_planted"]),
}

# Style shared by both papers, modelled on the SK companion papers.
HEADER = r"""
% Shared paper style for docs/expert_companion.md and docs/exposition.md, modelled
% on the SK companion papers: Latin Modern 11pt, left-aligned title block, bold
% serif run-in numbered headings, unindented paragraphs, booktabs tables with
% wide gutters, one muted link colour.
\usepackage{needspace}
\usepackage{etoolbox}
% Loaded here because the table settings below need it even in a paper with no table.
\usepackage{longtable}
\usepackage{caption}
\captionsetup{font=small,labelfont=bf,margin=4mm,skip=6pt}
\captionsetup[table]{position=top}
\usepackage{titlesec}
\titleformat{\section}{\normalfont\large\bfseries\raggedright}{\thesection}{0.6em}{}
\titleformat{\subsection}{\normalfont\normalsize\bfseries\raggedright}{\thesubsection}{0.6em}{}
\titlespacing*{\section}{0pt}{3.2ex plus .8ex minus .3ex}{1.1ex plus .2ex}
\titlespacing*{\subsection}{0pt}{2.4ex plus .6ex minus .2ex}{0.7ex plus .2ex}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt plus 1pt}
\emergencystretch=3em
\widowpenalty=10000
\clubpenalty=10000
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\small\thepage}
\renewcommand{\headrulewidth}{0pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\small\thepage}\renewcommand{\headrulewidth}{0pt}}
\definecolor{paperlink}{RGB}{28,64,128}
\setlength{\abovedisplayskip}{6pt plus 2pt}
\setlength{\belowdisplayskip}{6pt plus 2pt}
% Tables: small type, airy rows, a 16pt gutter between columns.
\AtBeginEnvironment{longtable}{\small\renewcommand{\arraystretch}{1.12}\setlength{\tabcolsep}{8pt}}
\setlength{\LTpre}{8pt}
\setlength{\LTpost}{6pt}
\makeatletter
\def\verbatim@font{\small\ttfamily}
% Title block: bold title flush left, italic subtitle, author and date on one line.
\newcommand{\subtitle}[1]{\gdef\@subtitle{#1}}
\gdef\@subtitle{}
\renewcommand{\maketitle}{\thispagestyle{plain}\begingroup\raggedright
  {\Large\bfseries\@title\par}\vspace{7pt}
  \ifx\@subtitle\empty\else{\large\itshape\@subtitle\par}\vspace{5pt}\fi
  {\normalsize\@author\ \ \textperiodcentered\ \ \@date\par}\vspace{16pt}\endgroup}
\renewenvironment{abstract}{\noindent\textbf{Abstract.}\ \ignorespaces}{\par\vspace{4pt}}
\makeatother
"""

# Additions that differ between the papers.
HEADER_EXTRA = {
    "expert": r"""\usepackage{newunicodechar}
\newunicodechar{≥}{\ensuremath{\geq}}
% Break reference URLs only after a slash or hyphen (pandoc loads xurl,
% which otherwise breaks inside words).
\AtBeginDocument{\def\UrlBreaks{\do\/\do-}\def\UrlBigBreaks{\do\:}}
\AtBeginDocument{\graphicspath{{@OUT@/}}}
""",
    "exposition": r"""\usepackage[skins,breakable]{tcolorbox}
\definecolor{boxframe}{RGB}{150,160,175}
\definecolor{boxback}{RGB}{246,247,249}
\newtcolorbox{aside}[1]{breakable, enhanced, colback=boxback,
  colframe=boxframe, boxrule=0.5pt, arc=2pt, left=6pt, right=6pt,
  top=4pt, bottom=4pt, toptitle=2pt, bottomtitle=2pt,
  fonttitle=\small\bfseries, coltitle=black, colbacktitle=boxframe!22,
  title={#1}, fontupper=\small, before upper={\setlength{\parskip}{4pt}}}
\makeatletter\renewcommand{\fps@figure}{htbp}\makeatother
""",
}

# Keep short tables whole: ask for room before a table of at most twelve rows.
LUA_TABLE = r"""
function Table(el)
  local rows = 0
  for _, body in ipairs(el.bodies) do rows = rows + #body.body end
  if rows <= 12 then
    return {pandoc.RawBlock("latex", "\\needspace{" .. (2 * rows + 4) .. "\\baselineskip}"), el}
  end
end
"""

LUA = {
    "expert": r"""-- The Markdown shows SVG figures on GitHub; LaTeX uses the PDF beside them.
function Image(el)
  el.src = el.src:gsub("%.svg$", ".pdf")
  return el
end
""" + LUA_TABLE + r"""-- An HTML comment <!-- pdf-page-break --> starts a new page in the PDF only.
function RawBlock(el)
  if el.format == "html" and el.text:match("^%s*<!%-%- pdf%-page%-break %-%->%s*$") then
    return pandoc.RawBlock("latex", "\\newpage")
  end
end
""",
    "exposition": r"""local figdir = FIGDIR
""" + LUA_TABLE + r"""
function Image(el)
  local name = el.src:match("figures/exposition/([%w_]+)%.svg$")
  if name then el.src = figdir .. "/" .. name .. ".pdf" end
  return el
end
function Div(el)
  if el.classes:includes("aside") then
    local title = el.attributes["title"] or ""
    local blocks = pandoc.List()
    blocks:insert(pandoc.RawBlock("latex", "\\begin{aside}{" .. title .. "}"))
    blocks:extend(el.content)
    blocks:insert(pandoc.RawBlock("latex", "\\end{aside}"))
    return blocks
  end
end
""",
}

# Numeric citation style for the expert paper (the exposition uses Pandoc's default).
NUMERIC_CSL = r'''<?xml version="1.0" encoding="utf-8"?>
<style xmlns="http://purl.org/net/xbiblio/csl" class="in-text" version="1.0" demote-non-dropping-particle="sort-only">
  <info>
    <title>Numeric (companion)</title>
    <id>numeric-companion</id>
    <updated>2026-11-03T00:00:00+00:00</updated>
  </info>
  <macro name="author">
    <names variable="author">
      <name initialize-with=". " delimiter=", " and="text" delimiter-precedes-last="never"/>
      <substitute><text variable="title"/></substitute>
    </names>
  </macro>
  <citation collapse="citation-number">
    <sort><key variable="citation-number"/></sort>
    <layout prefix="[" suffix="]" delimiter="; ">
      <group delimiter=", ">
        <text variable="citation-number"/>
        <group delimiter=" ">
          <label variable="locator" form="symbol"/>
          <text variable="locator"/>
        </group>
      </group>
    </layout>
  </citation>
  <bibliography entry-spacing="0" second-field-align="flush">
    <layout suffix=".">
      <text variable="citation-number" prefix="[" suffix="]"/>
      <group delimiter=". ">
        <text macro="author"/>
        <text variable="title" font-style="italic"/>
        <group delimiter=", ">
          <text variable="container-title"/>
          <text variable="collection-title"/>
          <group delimiter=" ">
            <text variable="volume"/>
            <text variable="issue" prefix="(" suffix=")"/>
          </group>
          <text variable="page"/>
          <text variable="publisher"/>
          <date variable="issued"><date-part name="year"/></date>
          <text variable="note"/>
        </group>
        <text variable="URL"/>
      </group>
    </layout>
  </bibliography>
</style>
'''

COLOURS = ["-V", "colorlinks=true", "-V", "linkcolor=paperlink",
           "-V", "urlcolor=paperlink", "-V", "citecolor=paperlink"]
PAGE = ["-V", "fontsize=11pt", "-V", "papersize=a4", "-V", "geometry:margin=25mm"]


def run(argv, cwd=None, log=None):
    result = subprocess.run(argv, cwd=cwd, capture_output=True, text=True)
    if log:
        log.write_text(result.stdout + result.stderr)
    if result.returncode:
        raise SystemExit(f"failed: {' '.join(map(str, argv))}\n{result.stderr[-3000:]}")
    return result


def build_figures(paper, out):
    """Compile the paper's figures into out/figures and write SVGs beside the sources."""
    source, names = FIGURES[paper]
    figdir = out / "figures"
    figdir.mkdir(parents=True, exist_ok=True)
    for name in names:
        shutil.copy(source / f"{name}.tex", figdir)
        if (source / "style.tex").exists():
            shutil.copy(source / "style.tex", figdir)
        run(["tectonic", "--outdir", str(figdir), str(figdir / f"{name}.tex")],
            cwd=figdir, log=figdir / f"{name}.log")
        run(["pdftocairo", "-svg", str(figdir / f"{name}.pdf"), str(source / f"{name}.svg")])
    return figdir


def pandoc_command(paper, out, figdir, tex):
    """Return the Pandoc argument list for one paper (no files are touched)."""
    header = out / "header.tex"
    lua = out / ("images.lua" if paper == "expert" else "layout.lua")
    if paper == "expert":
        return ["pandoc", str(DOCS / "expert_companion.md"),
                "--from=markdown+tex_math_dollars+tex_math_single_backslash+pipe_tables+raw_tex",
                "--standalone", "--to=latex", "--citeproc", f"--csl={out / 'numeric.csl'}",
                f"--lua-filter={lua}", f"--include-in-header={header}",
                *PAGE, *COLOURS, f"--resource-path={DOCS}", "-o", str(tex)]
    return ["pandoc", str(DOCS / "exposition.md"), "--standalone", "--to=latex",
            "--citeproc", "--bibliography", str(DOCS / "exposition.bib"),
            "--lua-filter", str(lua), "--include-in-header", str(header),
            "-V", "papersize=a4", "-V", "fontsize=11pt", "-V", "geometry:margin=25mm",
            *COLOURS, "-o", str(tex)]


def render(paper, out):
    out.mkdir(parents=True, exist_ok=True)
    figdir = build_figures(paper, out)
    (out / "header.tex").write_text(
        HEADER + HEADER_EXTRA[paper].replace("@OUT@", str(out)))
    lua = LUA[paper].replace("FIGDIR", repr(str(figdir)))
    if paper == "expert":
        (out / "numeric.csl").write_text(NUMERIC_CSL)
        (out / "images.lua").write_text(lua)
        stage = out / "stage"
        shutil.rmtree(stage, ignore_errors=True)
        stage.mkdir()
        tex, name = stage / "expert_companion.tex", "expert_companion"
        workdir, tectonic_out = DOCS, stage
    else:
        (out / "layout.lua").write_text(lua)
        tex, name = out / "exposition.tex", "exposition"
        workdir, tectonic_out = DOCS, out
    run(pandoc_command(paper, out, figdir, tex), cwd=workdir, log=out / "pandoc.log")
    run(["tectonic", "--keep-logs", "--outdir", str(tectonic_out), str(tex)],
        cwd=out if paper == "exposition" else None, log=out / "tectonic.log")
    if paper == "expert":
        shutil.copy(tectonic_out / f"{name}.pdf", out / f"{name}.pdf")
    print(out / f"{name}.pdf")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--paper", choices=[*PAPERS, "all"], default="all")
    parser.add_argument("--output-dir", type=Path, default=None,
                        help="parent of per-paper folders, or the folder itself for one paper "
                             "(default: ../_builds/quartic-r4/render/<paper>/ beside the checkout)")
    args = parser.parse_args(argv)
    papers = list(PAPERS) if args.paper == "all" else [args.paper]
    outputs = {}
    for paper in papers:
        if args.output_dir is None:
            out = BUILDS / paper
        elif args.paper == "all":
            out = args.output_dir.resolve() / paper
        else:
            out = args.output_dir.resolve()
        if out == ROOT or ROOT in out.parents:
            parser.error("--output-dir must be outside the checkout")
        outputs[paper] = out
    return outputs


def main(argv=None):
    for paper, out in parse_args(argv).items():
        render(paper, out)


if __name__ == "__main__":
    main()
