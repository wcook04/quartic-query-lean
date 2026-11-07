"""Set OpenAI's unmodified TeX as HTML; reject lost nodes and unresolved references.

This adapts reading_manuscripts' complete-Pandoc-tree marker check. Source custody,
PDF-derived figure and references are hash bound; these are mechanical checks,
not a claim of independent mathematical or manual PDF review.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import PurePosixPath
import re
import subprocess

from reading_manuscripts import Fragment, parse

SOURCE = "docs/original_source"
MANIFEST = SOURCE + "/manifest.json"
MARKER = "quartic-reader-line-"
THEOREMS = {"theorem", "lemma", "proposition", "corollary", "definition", "remark"}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def nodes(tree, kind=None):
    if isinstance(tree, dict):
        if "t" in tree and (kind is None or tree["t"] == kind):
            yield tree
        for value in tree.values():
            yield from nodes(value, kind)
    elif isinstance(tree, list):
        for value in tree:
            yield from nodes(value, kind)


def source_files(edition):
    manifest = edition.json(MANIFEST)
    for path, expected in manifest["files"].items():
        if PurePosixPath(path).is_absolute() or ".." in PurePosixPath(path).parts:
            raise ValueError("original source path leaves its pinned directory")
        raw = edition.read(f"{SOURCE}/{path}")
        if digest(raw) != expected:
            raise ValueError(f"OpenAI source differs from pinned bytes: {path}")
        edition.resources[f"{SOURCE}/{path}"] = raw
    edition.resources[MANIFEST] = edition.read(MANIFEST)

    def expand(path, active=()):
        if path in active or path not in manifest["files"]:
            raise ValueError(f"unavailable or recursive original TeX input: {path}")
        text = edition.read(f"{SOURCE}/{path}").decode()
        return re.sub(r"\\input\{([^}]+)\}",
                      lambda m: expand(m[1] + ".tex", (*active, path)), text)

    return manifest, expand("main.tex")


def numbered_labels(text, destinations):
    """Interpret only the counters declared by this pinned preamble, then check PDF names."""
    section, sub, theorem, equation = 0, 0, 0, 0
    appendix = False
    labels, headings = {}, []
    token = re.compile(r"\\appendix|\\(section|subsection|paragraph)\{([^}\n]+)\}|"
                       r"\\begin\{(" + "|".join(sorted(THEOREMS)) + r"|equation|align)\}")
    for match in token.finditer(text):
        end = text.find("\n\n", match.end())
        near = text[match.end():end if end >= 0 else len(text)]
        label = re.search(r"\\label\{([^}]+)\}", near)
        line = text.count("\n", 0, match.start()) + 1
        if match[0] == r"\appendix":
            appendix, section, sub, theorem = True, 0, 0, 0
            continue
        if match[1] == "section":
            section += 1
            sub, theorem = 0, 0
            number = chr(64 + section) if appendix else str(section)
            dest = f"appendix.{number}" if appendix else f"section.{number}"
        elif match[1] == "subsection":
            sub += 1
            number = f"{section}.{sub}"
            dest = f"subsection.{number}"
        elif match[1] == "paragraph":
            headings.append({"level": 4, "number": None, "title": match[2], "line": line})
            continue
        elif match[3] in THEOREMS:
            theorem += 1
            number = f"{chr(64 + section) if appendix else section}.{theorem}"
            dest = f"theorem.{number}"
        else:
            equation += 1
            number, dest = str(equation), f"equation.{equation}"
            # A label in align can follow an unnumbered first line.
            stop = text.index(r"\end{" + match[3] + "}", match.end())
            found = re.findall(r"\\label\{([^}]+)\}", text[match.end():stop])
            if len(found) != 1:
                raise ValueError("original numbered display needs one source label")
            label = re.match(r"(.+)", found[0])
        if dest not in destinations:
            raise ValueError(f"original source numbering has no PDF destination: {dest}")
        if match[1]:
            headings.append({"level": 1 if match[1] == "section" else 2,
                             "number": number, "title": match[2], "line": line,
                             "page": destinations[dest]})
        if label:
            key = label[1] if match[3] not in ("equation", "align") else label[0]
            # Locate the whole environment, not a paragraph inferred from ledger wording.
            stop = text.index(r"\end{" + match[3] + "}", match.end()) + len(r"\end{" + match[3] + "}") if match[3] else match.end()
            labels[key] = {"number": number, "destination": dest, "page": destinations[dest],
                           "lines": [line, text.count("\n", 0, stop) + 1]}
    expected = {k for k in destinations if k.startswith(("equation.", "theorem."))}
    if expected != {v["destination"] for v in labels.values() if v["destination"].startswith(("equation.", "theorem."))}:
        raise ValueError("original source and PDF numbered statements differ")
    return labels, headings


def located_tree(text):
    original = parse(text, "latex")
    lines, marked, math = text.splitlines(keepends=True), [], False
    if MARKER in text:
        raise ValueError("reserved original source marker")
    for i, line in enumerate(lines):
        if i and not lines[i-1].strip() and not math and line.strip():
            marked.append(f"\\hypertarget{{{MARKER}{i+1}}}{{}}\n\n")
        marked.append(line)
        if r"\[" in line or re.search(r"\\begin\{(equation|align\*?|aligned|tikzpicture|array|cases)\}", line):
            math = True
        if r"\]" in line or re.search(r"\\end\{(equation|align\*?|tikzpicture)\}", line):
            math = False
    observed = parse("".join(marked), "latex")

    def marker(block):
        return block.get("t") == "Div" and block["c"][0][0].startswith(MARKER)

    def strip(value):
        if isinstance(value, dict):
            return {k: strip(v) for k, v in value.items()}
        if isinstance(value, list):
            return [strip(v) for v in value if not (isinstance(v, dict) and marker(v))]
        return value

    if strip(observed) != original:
        raise ValueError("original source markers changed the complete Pandoc parse")

    def groups(blocks, start, finish):
        output, pending = [], []
        for block in blocks:
            if marker(block):
                end = int(block["c"][0][0][len(MARKER):]) - 1
                if pending:
                    output.append(wrap(pending, start, end))
                start, pending = end + 1, []
            else:
                pending.append(block)
        if pending:
            output.append(wrap(pending, start, finish))
        return output

    def wrap(children, start, end):
        for child in children:
            if child["t"] == "Div":
                child["c"][1] = groups(child["c"][1], start, end)
        return {"t": "Div", "c": [["", ["source-block"], [["data-l0", str(start)], ["data-l1", str(end)]]], children]}

    observed["blocks"] = groups(observed["blocks"], 1, len(lines))
    return observed, original


def inline(text):
    return {"t": "Str", "c": text}


def original_resources(edition, paper, rows):
    manifest, text = source_files(edition)
    if manifest["pdf_sha256"] != paper["sha256"]:
        raise ValueError("original source adaptation belongs to a different PDF")
    labels, headings = numbered_labels(text, manifest["destinations"])
    if digest(text.encode()) != manifest["expanded_tex_sha256"]:
        raise ValueError("expanded original TeX differs from the position bindings")
    tree, _ = located_tree(text)
    references = {r["key"]: r for r in manifest["references"]}
    numbers = {v["destination"]: (key, v) for key, v in labels.items()}
    # The one source figure is reproduced from the PDF; no reconstructed drawing.
    labels["fig:outward"] = {"number": "1", "destination": "figure.1", "page": 6}
    maths_before = [n["c"] for n in nodes(tree, "Math")]
    heading_iter = iter(headings)
    contents = []
    transformed_math = []
    for node in list(nodes(tree)):
        kind = node["t"]
        if kind == "Header":
            spec = next(heading_iter)
            if node["c"][0] != spec["level"]:
                raise ValueError("original heading order changed")
            if spec["number"]:
                node["c"][2].insert(0, inline(spec["number"] + " "))
            contents.append({**spec, "anchor": node["c"][1][0], "listed": spec["level"] < 4,
                             "end_line": len(text.splitlines())})
        elif kind == "Div" and set(node["c"][0][1]) & THEOREMS:
            key = node["c"][0][0]
            if key not in labels:
                raise ValueError(f"unlabelled original theorem {key}")
            strong = next(nodes(node, "Strong"))
            if len(strong["c"]) != 3 or strong["c"][2]["t"] != "Str":
                raise ValueError("original theorem label structure changed")
            strong["c"][2]["c"] = labels[key]["number"]
        elif kind == "OrderedList":
            node["c"][0][1:] = [{"t": "LowerRoman"}, {"t": "TwoParens"}]
        elif kind == "Link":
            attrs, _, target = node["c"]
            props = dict(attrs[2])
            if key := props.get("reference"):
                if key not in labels:
                    raise ValueError(f"unresolved original reference {key}")
                value = labels[key]["number"]
                node["c"][1] = [inline(f"({value})" if props["reference-type"] == "eqref" else value)]
        elif kind == "Cite":
            citations = node["c"][0]
            parts = [inline("[")]
            for i, cite in enumerate(sorted(citations, key=lambda c: references[c["citationId"]]["number"])):
                ref = references[cite["citationId"]]
                if i:
                    parts.append(inline(", "))
                parts.append({"t": "Link", "c": [["", [], []], [inline(str(ref["number"]))], ["#ref-" + ref["key"], ""]]})
                if cite["citationSuffix"]:
                    parts.extend([inline(", "), *cite["citationSuffix"]])
            parts.append(inline("]"))
            node.clear(); node.update({"t": "Span", "c": [["", ["citation"], []], parts]})
        elif kind == "Figure":
            if node["c"][0][0] != "fig:outward":
                raise ValueError("unregistered original illustration")
            caption = node["c"][1][1]
            caption[0]["c"].insert(0, inline("Figure 1: "))
            node["c"][2] = [{"t": "Plain", "c": [{"t": "Image", "c": [["", [], []], [inline("Figure 1")], ["outward-pointers.png", ""]]}]}]
        elif kind == "Math":
            mode, tex = node["c"]
            found = re.findall(r"\\label\{([^}]+)\}", tex)
            tex = re.sub(r"\\label\{[^}]+\}", "", tex)
            tex = re.sub(r"\\begin\{equation\}|\\end\{equation\}", "", tex)
            tex = re.sub(r"\\(begin|end)\{align\*?\}", r"\\\1{aligned}", tex)
            tex = tex.replace(r"\notag", "").replace(r"\nobreak", "").replace(r"\smallskip", "")
            # mathtools' three paired delimiters; these definitions are exact
            # expansions of this source's declarations, including unbraced arguments.
            tex = r"\def\norm#1{\lVert#1\rVert}\def\abs#1{\lvert#1\rvert}\def\ip#1{\langle#1\rangle}" + tex
            if found:
                if len(found) != 1 or found[0] not in labels:
                    raise ValueError("unknown original display label")
                tex += r"\tag{" + labels[found[0]]["number"] + "}"
            node["c"] = [mode, tex.strip()]
            transformed_math.append(deepcopy(node["c"]))
            if found:
                body = deepcopy(node)
                node.clear(); node.update({"t": "Span", "c": [[found[0], ["equation"], []], [body]]})
    if len(transformed_math) != len(maths_before):
        raise ValueError("original formula count changed")
    # The abstract lives in Pandoc metadata, which a fragment does not print.
    abstract = tree["meta"].get("abstract")
    if abstract:
        tree["blocks"].insert(0, {"t": "Div", "c": [["abstract", ["abstract"], []], [{"t": "Header", "c": [2, ["abstract-heading", [], []], [inline("Abstract")]]}, *abstract["c"]]]})
    tree["blocks"].append({"t": "Header", "c": [1, ["references", [], []], [inline("References")]]})
    contents.append({"level": 1, "title": "References", "number": None, "anchor": "references", "line": len(text.splitlines()), "end_line": len(text.splitlines()), "listed": True, "page": 17})
    for ref in manifest["references"]:
        tree["blocks"].append({"t": "Div", "c": [["ref-" + ref["key"], ["csl-entry"], []], [{"t": "Para", "c": [inline(f"[{ref['number']}] {ref['text']}")]}]]})
    aliases = [("original-" + sid, loc["lines"][0]) for sid, loc in manifest["statement_locations"].items()]
    aliases.extend((loc["anchor"], loc["lines"][0]) for loc in manifest["page_locations"] if loc["anchor"].startswith("original-page-"))
    source_groups = [n for n in nodes(tree, "Div") if "source-block" in n["c"][0][1]]
    for anchor, line in aliases:
        candidates = [n for n in source_groups if int(dict(n["c"][0][2])["data-l0"]) <= line <= int(dict(n["c"][0][2])["data-l1"])]
        if not candidates:
            raise ValueError(f"original source alias has no paragraph: {anchor}")
        group = min(candidates, key=lambda n: int(dict(n["c"][0][2])["data-l1"]) - int(dict(n["c"][0][2])["data-l0"]))
        group["c"][1].insert(0, {"t": "Div", "c": [[anchor, [], []], []]})
    raw = [n for n in nodes(tree) if n["t"] in ("RawInline", "RawBlock")]
    if raw:
        raise ValueError(f"unhandled original LaTeX: {raw[0]}")
    # Reject missing/duplicated formulas during the HTML-writing round trip too.
    html = subprocess.check_output(["pandoc", "--from=json", "--to=html5", "--mathjax", "--wrap=none"], input=json.dumps(tree).encode()).decode()
    figure = SOURCE + "/outward-pointers.png"
    fragment = Fragment(SOURCE + "/main.tex", {SOURCE + "/main.tex": "original"}, [figure], manifest["repository"] + "/blob/" + manifest["revision"] + "/")
    fragment.feed(html); fragment.close()
    for target, anchor in fragment.destinations:
        if target != "original" or anchor not in fragment.ids:
            raise ValueError(f"unresolved original HTML destination {anchor}")
    for i, item in enumerate(contents[:-1]):
        item["end_line"] = next((later["line"] - 1 for later in contents[i+1:] if later["level"] <= item["level"]), len(text.splitlines()))
    for row in rows:
        dest = row["location"].get("destination")
        if dest in numbers:
            key, loc = numbers[dest]
            row["lines"] = loc["lines"]
            row["location"].update({"lines": loc["lines"], "anchor": key})
        else:
            sid = row["id"].removeprefix("original/")
            loc = manifest["statement_locations"].get(sid)
            if not loc:
                raise ValueError(f"missing original source location: {sid}")
            a, b = loc["lines"]
            body = "".join(text.splitlines(keepends=True)[a-1:b]).encode()
            if digest(body) != loc["tex_sha256"]:
                raise ValueError(f"changed original source passage: {sid}")
            row["lines"] = loc["lines"]
            row["location"].update({"lines": loc["lines"], "anchor": "original-" + sid,
                                    "source_scope": "source_paragraph", "tex_sha256": loc["tex_sha256"]})
    path = "manuscripts/original.tex"
    edition.resources[path] = text.encode()
    edition.resources["manuscripts/original.html"] = "".join(fragment.output).encode()
    paper.update({"path": path, "source_lines": len(text.splitlines()), "contents": contents, "page_locations": manifest["page_locations"], "assets": [figure],
                  "anchors": sorted(fragment.ids), "tex_source_revision": manifest["revision"],
                  "tex_sha256": digest(text.encode()), "source_manifest": MANIFEST,
                  "rendered": {"resource": "manuscripts/original.html", "source_sha256": paper["sha256"],
                               "tex_sha256": digest(text.encode()), "renderer": subprocess.check_output(["pandoc", "--version"], text=True).splitlines()[0],
                               "math": "tex", "range_unit": "expanded_original_tex_lines_inclusive",
                               "checks": {"source_files_sha256": True, "marker_parse_unchanged": True, "formula_count": len(transformed_math),
                                          "numbered_pdf_destinations": len(numbers), "internal_destinations_resolved": True,
                                          "manual_pdf_review": False}}})
    return fragment
