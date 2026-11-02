#!/usr/bin/env python3
"""Render the delivered Markdown using Pandoc/XeLaTeX; no network access."""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
subprocess.run([
    "pandoc", str(root / "section.md"),
    "--from=markdown+tex_math_dollars+pipe_tables", "--standalone",
    "--pdf-engine=xelatex",
    "--lua-filter=" + str(root / "checks/pdf_layout.lua"),
    "--include-in-header=" + str(root / "checks/pdf_header.tex"),
    "-V", "mainfont=Latin Modern Roman", "-V", "monofont=DejaVu Sans Mono",
    "-V", "fontsize=11pt", "-V", "geometry:margin=24mm",
    "-V", "colorlinks=true", "-V", "urlcolor=blue",
    "-o", str(root / "section.pdf")
], check=True)
