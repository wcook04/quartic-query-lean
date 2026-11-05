"""Prepare Pandoc reading fragments with source ranges checked against the complete parse."""
import hashlib
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import posixpath
import re
import subprocess
import tempfile
from urllib.parse import quote, unquote, urlsplit

from render_reasoning_record import READER

MARK = re.compile(r"<!-- quartic-reader-line-(\d+) -->")


def parse(text, fmt):
    return json.loads(subprocess.check_output(["pandoc", "--from", fmt, "--to", "json"], input=text.encode()))


def located_document(text, fmt):
    """Only accept block boundaries whose markers preserve the entire Pandoc tree."""
    original = parse(text, fmt)
    lines = text.splitlines(keepends=True)
    front = lines.index("---\n", 1) + 1 if lines and lines[0] == "---\n" else 0
    if "quartic-reader-line-" in text:
        raise ValueError("reserved reader marker in manuscript")
    marked = []
    for i, line in enumerate(lines):
        if (i >= front and (i == 0 or not lines[i-1].strip()) and
                re.match(r"[A-Za-z#|!*$(\\\[<]", line) and not line.startswith(("[^", "[!", "<!-- /", "$$\n"))):
            marked.append(f"<!-- quartic-reader-line-{i+1} -->\n\n")
        marked.append(line)
    observed = parse("".join(marked), fmt)
    groups = []
    blocks = []
    start = front + 1
    for block in observed["blocks"]:
        match = MARK.fullmatch(block["c"][1]) if block["t"] == "RawBlock" and block["c"][0] == "html" else None
        if match:
            end = int(match[1]) - 1
            if blocks:
                groups.append((start, end, blocks))
            blocks = []
            start = end + 1
        else:
            blocks.append(block)
    if blocks:
        groups.append((start, len(lines), blocks))
    if observed["meta"] != original["meta"] or [b for _, _, group in groups for b in group] != original["blocks"]:
        raise ValueError("source markers changed the Pandoc parse; review manuscript boundaries")
    original["blocks"] = [{"t": "Div", "c": [["", ["source-block"], [["data-l0", str(a)], ["data-l1", str(b)]]], group]}
                          for a, b, group in groups]
    # The fragment writer leaves title metadata to the reader shell.
    abstract = original["meta"].get("abstract")
    if abstract:
        if abstract["t"] != "MetaBlocks":
            raise ValueError("unexpected Pandoc abstract")
        original["blocks"].insert(0, {"t": "Div", "c": [["", ["abstract"], []], abstract["c"]]})
    return original


class Fragment(HTMLParser):
    """Keep semantic HTML. Resolve paper links and keep figures inert until verified."""
    tags = set("a article aside blockquote br caption cite code col colgroup dd del details div dl dt em figcaption figure h1 h2 h3 h4 h5 h6 hr i img li ol p pre section small span strong sub summary sup table tbody td th thead tr ul".split())
    attrs = set("alt aria-label class colspan data-cites data-l0 data-l1 id role rowspan scope start title".split())

    def __init__(self, paper, paths, assets, source_url):
        super().__init__()
        self.paper, self.paths, self.assets, self.source_url = paper, paths, assets, source_url
        self.output = []
        self.ids = set()
        self.destinations = set()

    def handle_starttag(self, tag, attrs):
        if tag not in self.tags:
            raise ValueError(f"unhandled manuscript element {tag}")
        props = {k: v for k, v in attrs if k in self.attrs and v is not None}
        attributes = dict(attrs)
        style = attributes.get("style", "")
        layout = [rule.strip() for rule in style.split(";") if re.fullmatch(
            r"(?:text-align:\s*(?:left|right|center)|width:\s*\d+(?:\.\d+)?%)", rule.strip())]
        if layout:
            props["style"] = "; ".join(layout)
        if tag == "img":
            src = posixpath.normpath(posixpath.join(posixpath.dirname(self.paper), attributes["src"]))
            if src not in self.assets:
                raise ValueError(f"unpackaged manuscript image {src}")
            props["data-resource"] = src
        if tag == "a" and (href := attributes.get("href")):
            dest = urlsplit(href)
            if dest.scheme in ("http", "https") and dest.netloc:
                props["href"] = href
            elif href.startswith("#"):
                props["href"] = href
            elif dest.scheme or dest.netloc or href.startswith("/"):
                raise ValueError(f"unexpected manuscript link {href}")
            else:
                path = posixpath.normpath(posixpath.join(posixpath.dirname(self.paper), unquote(dest.path)))
                if path.startswith("../"):
                    raise ValueError(f"manuscript link leaves repository: {href}")
                props["href"] = self.source_url + quote(path) + ("#" + dest.fragment if dest.fragment else "")
                if path in self.paths:
                    props["data-paper"] = self.paths[path]
                    if dest.fragment:
                        props["data-fragment"] = unquote(dest.fragment)
        if "id" in props:
            if props["id"] in self.ids:
                raise ValueError(f"{self.paper}: duplicate anchor {props['id']}")
            self.ids.add(props["id"])
        if props.get("href", "").startswith("#"):
            self.destinations.add((self.paths[self.paper], unquote(props["href"][1:])))
        if "data-fragment" in props:
            self.destinations.add((props["data-paper"], props["data-fragment"]))
        for key in props.get("data-cites", "").split():
            self.destinations.add((self.paths[self.paper], "ref-" + key))
        self.output.append("<" + tag + "".join(f' {k}="{escape(v, quote=True)}"' for k, v in props.items()) + ">")

    def handle_endtag(self, tag):
        if tag not in self.tags:
            raise ValueError(f"unhandled manuscript element {tag}")
        if tag not in ("br", "col", "hr", "img"):
            self.output.append(f"</{tag}>")

    def handle_data(self, data):
        self.output.append(escape(data, quote=False))


def section_contents(tree, outline, fragment, last_line):
    """Bind the printed headings to Pandoc's own destinations and source blocks."""
    headers = []
    for div in tree["blocks"]:
        attrs, children = div["c"]
        if "source-block" not in attrs[1]:
            continue
        bounds = dict(attrs[2])
        for child in children:
            if child["t"] == "Header":
                level, (anchor, classes, _), _ = child["c"]
                headers.append((level, anchor, classes, int(bounds["data-l0"]), int(bounds["data-l1"])))
    if len(headers) != len(outline):
        raise ValueError("rendered headings differ from the manuscript outline")
    contents = []
    active = []
    for row, (level, anchor, classes, first, last) in zip(outline, headers):
        if row["level"] != level or not first <= row["line"] <= last or anchor not in fragment.ids:
            raise ValueError(f"outline cannot locate heading {row['title']}")
        while active and active[-1]["level"] >= level:
            active.pop()["end_line"] = row["line"] - 1
        item = {**row, "title": re.sub(r"\s*\{[^}]+\}$", "", row["title"]), "anchor": anchor,
                "listed": "unlisted" not in classes, "end_line": last_line}
        active.append(item)
        contents.append(item)
    return contents


def manuscript_resources(edition, papers, texts, repository):
    paths = {p["path"]: key for key, p in papers.items()}
    version = subprocess.check_output(["pandoc", "--version"], text=True).splitlines()[0]
    fragments = {}
    for key, text in texts.items():
        paper = papers[key]
        tree = located_document(text, READER if key in ("reconstruction", "verification") else "markdown")
        bib = paper["bibliography"]
        with tempfile.TemporaryDirectory() as scratch:
            cmd = ["pandoc", "--sandbox", "--from=json", "--to=html5", "--mathjax", "--wrap=none"]
            if bib:
                basename = Path(bib).name
                Path(scratch, basename).write_bytes(edition.read(bib))
                tree["meta"]["bibliography"] = {"t": "MetaString", "c": basename}
                tree["meta"]["link-citations"] = {"t": "MetaBool", "c": True}
                cmd.extend(["--citeproc", "--fail-if-warnings"])
            result = subprocess.check_output(cmd, cwd=scratch, input=json.dumps(tree).encode())
        fragment = Fragment(paper["path"], paths, paper["assets"], f"{repository}/blob/{edition.commit}/")
        fragment.feed(result.decode())
        fragment.close()
        paper["contents"] = section_contents(tree, paper["outline"], fragment, len(text.splitlines()))
        fragments[key] = fragment
        resource = f"manuscripts/{key}.html"
        edition.resources[resource] = "".join(fragment.output).encode()
        paper["rendered"] = {"resource": resource, "source_sha256": hashlib.sha256(text.encode()).hexdigest(),
                             "renderer": version, "math": "tex", "range_unit": "source_block_lines_inclusive"}
    for key, fragment in fragments.items():
        for target, anchor in sorted(fragment.destinations):
            if anchor not in fragments[target].ids:
                raise ValueError(f"{key}: unresolved manuscript link to {target}#{anchor}")
