#!/usr/bin/env python3
"""Preserve the seven round-four submissions without executing their code.

Round-four returns carry their full packet context (record, Lean tree, PDFs,
wheels), so the extracted members stay local. Git keeps the manifest, which
binds every original archive and member by size and SHA-256.
"""

import argparse
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from intake_round3_returns import digest, unpack  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "research/returns/round4"
DOWNLOADS = Path.home() / "Downloads"
RETURNS = (
    ("02_short_expert", "quartic_r4_02_short_expert_return.zip"),
    ("03_examples_first", "quartic_r4_03_examples_first_return.zip"),
    ("04_quantum_completion", "quartic_r4_04_quantum_completion_return.zip"),
    ("05_classical_completion", "quartic_r4_05_classical_completion_return.zip"),
    ("06_corpus_fidelity", "quartic_r4_06_corpus_fidelity_return.zip"),
    ("07_publication_backend", "quartic_r4_07_publication_backend_return.zip"),
    ("08_adversarial_audit", "quartic_r4_08_return.zip"),
)


def main():
    if (DEST / "intake.json").exists():
        raise SystemExit(f"Refusing to overwrite {DEST / 'intake.json'}")
    DEST.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="round4-intake-", dir=DEST) as temporary:
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
    """Verify local originals and members against their recorded hashes."""
    manifest = json.loads((DEST / "intake.json").read_text())
    for record in manifest["returns"]:
        archive = record["archive"]
        archive_path = DEST / archive["preserved"]
        if digest(archive_path.read_bytes()) != {k: archive[k] for k in ("bytes", "sha256")}:
            raise ValueError(f"archive mismatch: {archive_path}")
        with tempfile.TemporaryDirectory(prefix="round4-verify-") as temporary:
            if unpack(archive_path, Path(temporary)) != record["members"]:
                raise ValueError(f"archive members mismatch: {archive_path}")
        member_root = DEST / record["members_root"]
        for entry in record["members"]:
            path = member_root / entry["path"]
            if path.is_symlink() or digest(path.read_bytes()) != {k: entry[k] for k in ("bytes", "sha256")}:
                raise ValueError(f"snapshot bytes mismatch: {path}")
    print(f"Verified {len(manifest['returns'])} archives")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="verify an existing intake")
    if parser.parse_args().verify:
        verify()
    else:
        main()
