#!/usr/bin/env python3
"""Preserve the round-five critique returns without executing their code.

Round-five returns are referee findings and small checking scripts, so their
extracted members are committed for readers; the original archives stay local.
The long-record lens came back twice from two independent runs, and both are
kept. The manifest binds every archive and member by size and SHA-256.
"""

import argparse
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from intake_round3_returns import digest, unpack  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "research/returns/round5"
DOWNLOADS = Path.home() / "Downloads"
RETURNS = (
    ("expert_referee_short", "quartic_r5_expert_referee_short_return.zip"),
    ("quantum_mechanism", "quartic_r5_quantum_mechanism_return.zip"),
    ("classical_mechanism", "quartic_r5_classical_mechanism_return.zip"),
    ("exposition_for_students", "quartic_r5_exposition_for_students_return.zip"),
    ("long_record_navigation_a", "quartic_r5_long_record_navigation_return.zip"),
    ("long_record_navigation_b", "quartic_r5_long_record_navigation_return (1).zip"),
)


def main():
    if (DEST / "intake.json").exists():
        raise SystemExit(f"Refusing to overwrite {DEST / 'intake.json'}")
    DEST.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="round5-intake-", dir=DEST) as temporary:
        stage = Path(temporary)
        records = []
        for ident, archive_name in RETURNS:
            archive_data = (DOWNLOADS / archive_name).read_bytes()
            archive_copy = stage / "archives" / archive_name
            archive_copy.parent.mkdir(exist_ok=True)
            archive_copy.write_bytes(archive_data)
            members = unpack(archive_copy, stage / "members" / ident)
            records.append({"id": ident, "archive": {"source": archive_name,
                "preserved": f"archives/{archive_name}", **digest(archive_data)},
                "members_root": f"members/{ident}", "members": members})
        for name in ("archives", "members"):
            (stage / name).rename(DEST / name)
        (DEST / "intake.json").write_text(json.dumps({"returns": records}, indent=2) + "\n")
    print(f"Preserved {len(records)} archives at {DEST}")


def verify():
    """Verify members, and local originals where present, against their hashes."""
    manifest = json.loads((DEST / "intake.json").read_text())
    for record in manifest["returns"]:
        archive = record["archive"]
        archive_path = DEST / archive["preserved"]
        if archive_path.exists():
            if digest(archive_path.read_bytes()) != {k: archive[k] for k in ("bytes", "sha256")}:
                raise ValueError(f"archive mismatch: {archive_path}")
            with tempfile.TemporaryDirectory(prefix="round5-verify-") as temporary:
                if unpack(archive_path, Path(temporary)) != record["members"]:
                    raise ValueError(f"archive members mismatch: {archive_path}")
        member_root = DEST / record["members_root"]
        for entry in record["members"]:
            path = member_root / entry["path"]
            if path.is_symlink() or digest(path.read_bytes()) != {k: entry[k] for k in ("bytes", "sha256")}:
                raise ValueError(f"snapshot bytes mismatch: {path}")
    print(f"Verified {len(manifest['returns'])} returns")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="verify an existing intake")
    if parser.parse_args().verify:
        verify()
    else:
        main()
