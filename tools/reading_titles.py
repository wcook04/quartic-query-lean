"""Edition-bound mathematical captions for declarations exposed by the reader."""
import json
import re

SOURCE = "docs/reading_declaration_titles.json"
RESOURCE = "selection/declaration-titles.json"


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate declaration title key: {key}")
        result[key] = value
    return result


def title_record(name, value):
    if isinstance(value, str):
        rich = plain = value
    elif isinstance(value, list) and len(value) == 2 and all(isinstance(v, str) for v in value):
        rich, plain = value
    else:
        raise ValueError(f"{name}: expected a title or a rich/plain pair")
    for title in (rich, plain):
        if (not title.strip() or title != title.strip() or not title.isprintable()
                or "`" in title or title == name or "QuarticQuery." in title):
            raise ValueError(f"{name}: expected a readable declaration title")
    parts = rich.split("$")
    if (isinstance(value, list) and len(parts) == 1
            or len(parts) % 2 != 1 or any(not m.strip() or m != m.strip() for m in parts[1::2])
            or re.search(r"[\\_{}^≤≥=<>∑∈√ℕ₀-₉Α-Ωα-ω]", "".join(parts[::2]))
            or re.search(r"[\\${}]", plain)):
        raise ValueError(f"{name}: delimit inline title mathematics and supply a plain rendering")
    if not re.fullmatch(".+?".join(map(re.escape, parts[::2])), plain):
        raise ValueError(f"{name}: preserve the title's prose in its plain rendering")
    return {"title": rich, "title_plain": plain}


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
