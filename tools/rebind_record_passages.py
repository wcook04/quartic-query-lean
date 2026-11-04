#!/usr/bin/env python3
"""Rebind docs/reasoning_record_correspondence.json to an edited record.

The correspondence binds every `<!-- passage:ID -->` body of the record by line
range and SHA-256, and binds the whole record and its bibliography by hash.
Passages relocated into the verification supplement retain their identities,
with the owning file and its local lines recorded explicitly. After
an editorial revision this recomputes those bindings. It never changes which
claims the record carries: an existing passage keeps its reviewed claim list,
except that a claim whose `<!-- claim:ID -->` marker the revision moved into
another passage moves with it, and a new passage enters with no other claims. A passage whose body text changed (rather
than merely moved) is listed in the report, because its earlier review covered
different words and needs reading before anyone relies on it.

    python3 tools/rebind_record_passages.py --report research/adjudication/round5_record_rebind.json
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_comparator_map import CLAIM, PASSAGE  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "docs/reasoning_record.md"
SUPPLEMENT = ROOT / "docs/verification_details.md"
BIB = ROOT / "docs/reasoning_record.bib"
CORRESPONDENCE = ROOT / "docs/reasoning_record_correspondence.json"


def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    text = RECORD.read_text(encoding="utf-8")
    data = json.loads(CORRESPONDENCE.read_text(encoding="utf-8"))
    old = {p["id"]: p for p in data["passages"]}
    found = {}
    sources = {RECORD: text}
    if SUPPLEMENT.exists():
        sources[SUPPLEMENT] = SUPPLEMENT.read_text(encoding="utf-8")
    markers = {}
    for source, source_text in sources.items():
        for match in PASSAGE.finditer(source_text):
            ident, body = match.group(1), match.group(2)
            if ident in found:
                raise SystemExit(f"duplicate passage {ident}")
            found[ident] = {"id": ident,
                            "path": source.relative_to(ROOT).as_posix(),
                            "line_start": source_text.count("\n", 0, match.start(2)) + 1,
                            "line_end": source_text.count("\n", 0, match.end(2)) + 1,
                            "claims": old[ident]["claims"] if ident in old else [],
                            "sha256": sha256(body)}
            markers[ident] = {m.group(1) for m in CLAIM.finditer(body)}
    moved = []
    for ident, passage in found.items():
        for claim in list(passage["claims"]):
            if claim in markers[ident]:
                continue
            homes = [other for other, held in markers.items() if claim in held]
            if len(homes) == 1:
                passage["claims"].remove(claim)
                if claim not in found[homes[0]]["claims"]:
                    found[homes[0]]["claims"].append(claim)
                moved.append({"claim": claim, "from": ident, "to": homes[0]})
    missing = sorted(set(old) - set(found))
    if missing:
        raise SystemExit("passages removed from the record: " + ", ".join(missing))
    order = [p["id"] for p in data["passages"]] + [i for i in found if i not in old]
    report = {
        "schema": "quartic-record-passage-rebind-v1",
        "rebound_utc": datetime.now(timezone.utc).isoformat(),
        "record_sha256": {"before": data["record_sha256"], "after": sha256(text)},
        "bibliography_sha256": {"before": data.get("bibliography_sha256"),
                                "after": hashlib.sha256(BIB.read_bytes()).hexdigest()},
        "moved_only": sorted(i for i in old if old[i]["sha256"] == found[i]["sha256"]),
        "text_changed": sorted(i for i in old if old[i]["sha256"] != found[i]["sha256"]),
        "added": sorted(i for i in found if i not in old),
        "claims_moved": moved,
        "scope": ("Structural rebind after an editorial revision. Claim lists change only by claims_moved; "
                  "text_changed passages were reworded and their earlier review covered other words."),
    }
    data["passages"] = [found[i] for i in order]
    data["sources"] = {p.relative_to(ROOT).as_posix(): sha256(s) for p, s in sources.items()}
    data["record_sha256"] = report["record_sha256"]["after"]
    data["bibliography_sha256"] = report["bibliography_sha256"]["after"]
    CORRESPONDENCE.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.report.write_text(json.dumps(report, indent=1) + "\n", encoding="utf-8")
    print(f"{len(report['moved_only'])} moved, {len(report['text_changed'])} reworded, "
          f"{len(report['added'])} added")


if __name__ == "__main__":
    main()
