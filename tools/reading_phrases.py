"""Phrase ties: each Lean declaration tied to the exact words of a paper that state it.

The maintained sources are docs/reading_phrases/<paper>.json, one per Quartic paper.
Each binds its quotations to the manuscript bytes and its Lean rows to the Lean
source snapshot of the recorded graph. The export rejects a source whose manuscript
or Lean has changed, a phrase that is missing from its paragraph, occurs twice there,
starts or ends inside a formula, crosses a paragraph or overlaps another phrase, and
a declaration without a title, a reading note or a topic. The phrase resource gives
the site each phrase's source lines, topic colour and Lean rows; the manuscript
renderer marks the same character ranges in the HTML.
"""
from hashlib import sha256
import json
import re

from build_comparator_map import lean_blocks
from reading_titles import title_record, unique_keys

SOURCE = "docs/reading_phrases/{paper}.json"
RESOURCE = "selection/phrases/{paper}.json"
SCHEMA = "quartic-reading-phrases-v1"
PAPERS = ("expert", "exposition", "reconstruction")
ROLES = {"statement", "definition", "explanation", "derivation", "example", "mention"}
RELATIONS = {"states", "defines", "part", "proof", "contains"}
FIDELITY = {"same", "stronger", "weaker", "different"}
MAX_SLICE = 1800
MAX_TOPICS = 9
NOTE_WORDS = (40, 100)
TITLE_WORDS = (2, 12)
LINK_NOTE_WORDS = 25
# Words the reader's prose avoids; the site's own labels follow the same rule.
AVOIDED = re.compile(r"\b(?:silent(?:ly)?|seamless(?:ly)?|robust(?:ly|ness)?)\b", re.I)


def math_spans(text):
    """Character ranges of $...$ and $$...$$ formulas; a backslash escapes the next character."""
    spans, i, n = [], 0, len(text)
    while i < n:
        if text[i] == "\\":
            i += 2
            continue
        if text.startswith("$$", i):
            end = text.find("$$", i + 2)
            if end < 0:
                break
            spans.append((i, end + 2))
            i = end + 2
            continue
        if text[i] == "$":
            j = i + 1
            while j < n and not (text[j] == "$" and text[j - 1] != "\\"):
                j += 1
            if j >= n:
                break
            spans.append((i, j + 1))
            i = j + 1
            continue
        i += 1
    return spans


def paragraph(text, offset):
    before = text.rfind("\n\n", 0, offset)
    start = before + 2 if before >= 0 else 0
    after = text.find("\n\n", offset)
    return start, len(text) if after < 0 else after


def locate(text, tie, formulas):
    """The character range of one phrase, under the rules its return was checked by."""
    at = f"phrase {tie['id']}"
    start_from = 0
    if tie.get("after"):
        if text.count(tie["after"]) != 1:
            raise ValueError(f"{at}: its after-quote must occur exactly once in the paper")
        start_from = text.index(tie["after"]) + len(tie["after"])
    begin = text.find(tie["from"], start_from) if tie.get("from") else -1
    if begin < 0:
        raise ValueError(f"{at}: from-quote not found: {tie.get('from')!r}")
    block_start, block_end = paragraph(text, begin)
    if text.count(tie["from"], max(block_start, start_from), block_end) != 1:
        raise ValueError(f"{at}: from-quote occurs more than once in its paragraph")
    stop = text.find(tie["to"], begin) if tie.get("to") else -1
    if stop < 0:
        raise ValueError(f"{at}: to-quote not found after its from-quote: {tie.get('to')!r}")
    end = stop + len(tie["to"])
    if end - begin > MAX_SLICE:
        raise ValueError(f"{at}: {end - begin} characters, more than {MAX_SLICE}")
    if "\n\n" in text[begin:end] and not text[begin:end].lstrip().startswith("$$"):
        raise ValueError(f"{at}: crosses a paragraph break")
    for a, b in formulas:
        if a < begin < b or a < end < b:
            raise ValueError(f"{at}: cuts the formula {text[a:b][:60]!r}")
    return begin, end


def segments(text, begin, end, formulas):
    """A phrase in a pipe table is marked cell by cell; elsewhere it is one range."""
    if not text[paragraph(text, begin)[0]:].startswith("|"):
        return [(begin, end)]
    inside = [(a, b) for a, b in formulas if a < end and b > begin]
    cuts = [i for i in range(begin, end) if text[i] in "|\n" and text[i - 1] != "\\"
            and not any(a <= i < b for a, b in inside)]
    out = []
    for a, b in zip([begin] + [c + 1 for c in cuts], cuts + [end]):
        cell = text[a:b]
        if cell.strip() and not re.fullmatch(r"\s*:?-{3,}:?\s*", cell):
            lead = len(cell) - len(cell.lstrip())
            out.append((a + lead, a + len(cell.rstrip())))
    return out


def check_overlaps(path, located):
    """No two phrases share a character; `located` is sorted by start."""
    for (a0, a1, first), (b0, b1, second) in zip(located, located[1:]):
        if b0 < a1:
            raise ValueError(f"{path}: phrases {first['id']} and {second['id']} overlap")


def prose_check(where, value, words=None):
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ValueError(f"{where}: expected trimmed text")
    if AVOIDED.search(value):
        raise ValueError(f"{where}: avoid the word {AVOIDED.search(value)[0]!r}")
    if value.count("$") % 2:
        raise ValueError(f"{where}: unbalanced $")
    if re.search(r"[_^\\]", re.sub(r"\$[^$]+\$|`[^`]+`", "", value)):
        raise ValueError(f"{where}: set mathematics in $…$ and Lean names in backticks")
    if words:
        count = len(value.split())
        if not words[0] <= count <= words[1]:
            raise ValueError(f"{where}: {count} words, expected {words[0]} to {words[1]}")


class Declarations:
    """Declaration ranges from the recorded graph, or from the source of a file outside it."""
    def __init__(self, edition, modules):
        self.edition, self.modules, self.files = edition, modules, {}

    def lines(self, name, file):
        module = self.modules.get(name)
        if module is not None:
            shard = json.loads(self.edition.resources[f"proof/{module}.json"])
            if shard["source"] != file:
                raise ValueError(f"{name} is recorded in {shard['source']}, not {file}")
            node = shard["nodes"][name]
            return node["lines"], True
        if not re.fullmatch(r"lean/(?:QuarticQuery|QuarticCorpus)/[\w/]+\.lean", file):
            raise ValueError(f"{name}: unexpected Lean file {file}")
        if file not in self.files:
            raw = self.edition.read(file)
            self.edition.resources[file] = raw
            self.files[file] = {}
            for block in lean_blocks(raw.decode()):
                self.files[file].setdefault(block["name"], []).append([block["line_start"], block["line_end"]])
        found = self.files[file].get(name, [])
        if len(found) != 1:
            raise ValueError(f"{name} is not declared exactly once in {file}")
        return found[0], False


def phrase_resources(edition, texts, documents):
    """Validate every phrase source and add one resource per paper; return the marked ranges."""
    index = json.loads(edition.resources["selection/index.json"])
    graph = index["graph"]
    if graph["currentness"] != "current":
        raise ValueError("phrase ties need the current Lean graph")
    declarations = Declarations(edition, index["modules"])
    ranges, listing = {}, {}
    for paper in PAPERS:
        path = SOURCE.format(paper=paper)
        data = json.loads(edition.read(path), object_pairs_hook=unique_keys)
        text = texts[paper]
        if data.get("schema") != SCHEMA or data.get("paper") != paper or data.get("manuscript") != documents[paper]:
            raise ValueError(f"{path}: unexpected schema, paper or manuscript")
        if data["manuscript_sha256"] != sha256(text.encode()).hexdigest():
            raise ValueError(f"{path}: the manuscript changed; re-read every phrase against it and rebind manuscript_sha256")
        if data["lean_source_snapshot_sha256"] != graph["source_snapshot_sha256"]:
            raise ValueError(f"{path}: the Lean source changed; re-check every Lean row and rebind lean_source_snapshot_sha256")
        topics = data["topics"]
        ids = [t["id"] for t in topics]
        if not 1 <= len(topics) <= MAX_TOPICS or len(set(ids)) != len(ids):
            raise ValueError(f"{path}: expected one to {MAX_TOPICS} distinct topics")
        for topic in topics:
            prose_check(f"{path}: topic {topic['id']} name", topic["name"])
            prose_check(f"{path}: topic {topic['id']} description", topic["description"])
        formulas = math_spans(text)
        located, named, phrases = [], {}, []
        seen = set()
        for tie in data["ties"]:
            at = f"{path}: phrase {tie['id']}"
            if tie["id"] in seen:
                raise ValueError(f"{at}: repeated id")
            seen.add(tie["id"])
            if tie["role"] not in ROLES or tie["topic"] not in ids:
                raise ValueError(f"{at}: unknown role or topic")
            if tie["role"] in {"statement", "definition"} and not tie["lean"]:
                raise ValueError(f"{at}: a {tie['role']} needs a Lean row")
            begin, end = locate(text, tie, formulas)
            located.append((begin, end, tie))
            for row in tie["lean"]:
                where = f"{at} -> {row['name']}"
                if row["relation"] not in RELATIONS or row["fidelity"] not in FIDELITY:
                    raise ValueError(f"{where}: unknown relation or fidelity")
                if row["fidelity"] != "same":
                    prose_check(f"{where}: fidelity_note", row.get("fidelity_note"))
                if "link_note" in row:
                    prose_check(f"{where}: link_note", row["link_note"], (1, LINK_NOTE_WORDS))
                span, recorded = declarations.lines(row["name"], row["file"])
                if "lines" in row and not span[0] <= row["lines"][0] <= row["lines"][1] <= span[1]:
                    raise ValueError(f"{where}: lines {row['lines']} lie outside the declaration {span}")
                named.setdefault(row["name"], set()).add(tie["topic"])
        located.sort(key=lambda r: r[0])
        check_overlaps(path, located)
        if data["titles"].keys() != named.keys() or data["notes"].keys() != named.keys():
            missing = sorted((named.keys() - data["titles"].keys()) | (named.keys() - data["notes"].keys()))
            extra = sorted((data["titles"].keys() | data["notes"].keys()) - named.keys())
            raise ValueError(f"{path}: titles and notes must cover the tied declarations; missing {missing}; extra {extra}")
        titles = {}
        for name, value in data["titles"].items():
            titles[name] = title_record(name, value)
            prose_check(f"{path}: title of {name}", titles[name]["title_plain"], TITLE_WORDS)
        for name, note in data["notes"].items():
            prose_check(f"{path}: note of {name}", note, NOTE_WORDS)
        # A topic's phrases alternate between its two shades in reading order.
        count = {topic: 0 for topic in ids}
        marks = []
        for order, (begin, end, tie) in enumerate(located):
            topic = ids.index(tie["topic"])
            tone = topic * 2 + count[tie["topic"]] % 2
            count[tie["topic"]] += 1
            marks.extend((a, b, order, tie["id"], tone) for a, b in segments(text, begin, end, formulas))
            lean = []
            for row in tie["lean"]:
                span, recorded = declarations.lines(row["name"], row["file"])
                lean.append({key: row[key] for key in ("name", "file", "lines", "relation", "fidelity",
                                                       "fidelity_note", "link_note") if key in row}
                            | {"declaration_lines": span, "in_graph": recorded})
            phrases.append({"id": tie["id"], "order": order, "lines": [text.count("\n", 0, begin) + 1,
                                                                       text.count("\n", 0, end) + 1],
                            "text": text[begin:end], "role": tie["role"], "topic": tie["topic"], "tone": tone,
                            "lean": lean})
        ranges[paper] = marks
        resource = RESOURCE.format(paper=paper)
        edition.add(resource, {"schema": SCHEMA, "revision": edition.commit, "paper": paper,
                               "manuscript_sha256": data["manuscript_sha256"],
                               "lean_source_snapshot_sha256": data["lean_source_snapshot_sha256"],
                               "source": path, "topics": topics, "phrases": phrases,
                               "titles": titles, "notes": data["notes"]})
        listing[paper] = resource
    return ranges, listing
