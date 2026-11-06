"""Edition-bound captions and typeset ledger statements for the Quartic reader."""
from hashlib import sha256
import json
import re

SOURCE = "docs/reading_declaration_titles.json"
RESOURCE = "selection/declaration-titles.json"
STATEMENT_SOURCE = "docs/reading_statement_presentations.json"
STATEMENT_RESOURCE = "selection/statement-titles.json"


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate reader presentation key: {key}")
        result[key] = value
    return result


def title_record(name, value, *, field="title"):
    if isinstance(value, str):
        rich = plain = value
    elif isinstance(value, list) and len(value) == 2 and all(isinstance(v, str) for v in value):
        rich, plain = value
    else:
        raise ValueError(f"{name}: expected a title or a rich/plain pair")
    for title in (rich, plain):
        if (not title.strip() or title != title.strip() or not title.isprintable()
                or "`" in title or title == name or "QuarticQuery." in title):
            raise ValueError(f"{name}: expected readable {field} text")
    parts = rich.split("$")
    if (isinstance(value, list) and len(parts) == 1
            or len(parts) % 2 != 1 or any(not m.strip() or m != m.strip() for m in parts[1::2])
            or re.search(r"[\\_{}^≤≥=<>∑∈√ℕ₀-₉Α-Ωα-ω]", "".join(parts[::2]))
            or re.search(r"[\\${}]", plain)):
        raise ValueError(f"{name}: delimit inline mathematics in the {field} and supply a plain rendering")
    if not same_prose(parts[::2], plain):
        raise ValueError(f"{name}: preserve the {field} prose in its plain rendering")
    return {field: rich, field + "_plain": plain}


def same_prose(literals, plain):
    """Keep the surrounding prose verbatim, with at least one character per formula."""
    if len(literals) == 1:
        return plain == literals[0]
    if not plain.startswith(literals[0]) or not plain.endswith(literals[-1]):
        return False
    pos = len(literals[0])
    for literal in literals[1:-1]:
        match = plain.find(literal, pos + 1)
        if match == -1:
            return False
        pos = match + len(literal)
    return pos < len(plain) - len(literals[-1])


def declaration_titles(edition, graph, required):
    snapshot = graph["source_snapshot_sha256"]
    titles = {}
    if graph["currentness"] == "current":
        authored = json.loads(edition.read(SOURCE), object_pairs_hook=unique_keys)
        if authored["source_snapshot_sha256"] != snapshot:
            raise ValueError(f"{SOURCE}: review declaration titles against the new Lean source snapshot")
        entries = authored["titles"]
        missing, extra = required - entries.keys(), entries.keys() - required
        if missing or extra:
            raise ValueError(f"{SOURCE}: missing titles {sorted(missing)}; obsolete titles {sorted(extra)}")
        titles = {name: title_record(name, value) for name, value in entries.items()}
    edition.add(RESOURCE, {"schema": "quartic-declaration-titles-v1", "revision": edition.commit,
                           "source_snapshot_sha256": snapshot, "status": graph["currentness"], "titles": titles})
    return titles


def statement_presentations(edition, statements):
    """Bind each editorial rendering to the maintained wording used by the review."""
    entries = json.loads(edition.read(STATEMENT_SOURCE), object_pairs_hook=unique_keys)
    if entries.keys() != statements.keys():
        missing = sorted(statements.keys() - entries.keys())
        extra = sorted(entries.keys() - statements.keys())
        raise ValueError(f"{STATEMENT_SOURCE}: missing statements {missing}; obsolete statements {extra}")
    presentations, titles = {}, {}
    for ident, statement in statements.items():
        entry = entries[ident]
        digest = sha256(statement["statement"].encode()).hexdigest()
        if digest != statement["statement_sha256"] or entry["statement_sha256"] != digest:
            raise ValueError(f"{ident}: review the title and typeset body against the changed ledger wording")
        title = title_record(ident, entry["title"])
        body = title_record(ident, entry["body"], field="body")
        titles[ident] = title
        presentations[ident] = {**title, **body, "statement_sha256": digest}
    edition.add(STATEMENT_RESOURCE, {"schema": "quartic-statement-titles-v1", "revision": edition.commit,
                                     "titles": titles})
    return presentations
