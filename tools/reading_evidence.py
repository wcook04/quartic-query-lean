"""Build reader-facing fidelity records from Quartic's reviewed ties and recorded checks."""
import hashlib
import re

from build_comparator_map import lean_blocks
from build_corpus import currentness, source_hashes


def evidence_resources(edition, statements, passages_by_statement, comparison, probes):
    """Give each statement its own retrievable account of the evidence and its scope."""
    authored = edition.json("corpus/ties.json")
    blocks = {}

    def source(path):
        if path not in blocks:
            raw = edition.read(path)
            edition.resources[path] = raw
            blocks[path] = {b["name"]: b for b in lean_blocks(raw.decode())}
        return blocks[path]

    configs_by_name = {}
    checks = {}
    for challenge in comparison["challenges"]:
        for config in challenge["configurations"]:
            path = config["path"]
            original = edition.json(path)
            summary = config["latest_receipt"]
            if summary:
                receipt = summary["receipt"]
                raw = edition.read(receipt)
                if hashlib.sha256(raw).hexdigest() != summary["receipt_sha256"]:
                    raise ValueError(f"changed comparison receipt: {receipt}")
                edition.resources[receipt] = raw
            checks[path] = {**config, "challenge": challenge["path"],
                            "permitted_axioms": original["permitted_axioms"]}
            for item in (path, challenge["path"], config["solution"]):
                edition.resources[item] = edition.read(item)
            for name in config["theorem_names"]:
                configs_by_name.setdefault(name, []).append(path)

    # These are recorded tests of specific alternative definitions or assumptions.
    # A test of a deliberately altered definition cannot refute the published theorem.
    receipt_path = "corpus/receipts/lean-build-round3-targeted-2026-11-02T204814950389+0000.json"
    receipt = edition.json(receipt_path)
    edition.resources[receipt_path] = edition.read(receipt_path)
    hashes = source_hashes(edition.root)
    for path, expected in hashes.items():
        if hashlib.sha256(edition.read(path)).hexdigest() != expected:
            raise ValueError(f"source changed during capture: {path}")
    freshness = currentness(receipt, hashes)

    # Match each recorded output to a directive in the exact inspector that ran.
    audit_path = "research/adjudication/round3_formal.json"
    audit = edition.json(audit_path)
    axiom_audits = {}
    for run in audit["type_and_axiom_audits"]:
        inspector = "lean/" + run["command"][-1]
        raw = edition.read(inspector)
        if hashlib.sha256(raw).hexdigest() != audit["source_hashes"][inspector]:
            # The old output remains in the adjudication; never attach it to new directives.
            continue
        names = re.findall(r"^#print axioms ([\w.]+)$", raw.decode(), re.M)
        if len(names) != len(run["axiom_sets"]):
            raise ValueError(f"axiom audit output count differs from directives: {inspector}")
        edition.resources[inspector] = raw
        for name, axioms in zip(names, run["axiom_sets"]):
            axiom_audits[name] = {"axioms": axioms, "inspector": inspector,
                                  "adjudication": audit_path, "log_sha256": run["log_sha256"],
                                  "snapshot_currentness": currentness(audit, hashes)}
    edition.add("axiom-audits.json", axiom_audits)
    by_statement = {}
    for probe in probes:
        ident = probe["statement"]
        path = f"lean/QuarticCorpus/Independent/{probe['file']}.lean"
        name = "QuarticQuery.SemanticReview." + probe["name"]
        if ident not in statements or name not in receipt["declarations"]:
            raise ValueError(f"unbound semantic probe: {ident}, {name}")
        block = source(path)[name]
        by_statement.setdefault(ident, []).append({
            "question": probe["question"], "declaration": name, "source": path,
            "lines": [block["line_start"], block["line_end"]], "receipt": receipt_path,
            "recorded_status": receipt["status"], "receipt_currentness": freshness})

    edition.add("checks.json", checks)
    for ident, statement in statements.items():
        reviewers = {t["declaration"]: t.get("reviewed_by") for t in authored.get(ident, [])}
        ties = []
        for tie in statement["lean"]:
            name = tie["declaration"]
            block = source(tie["file"]).get(name)
            entry = {**tie, "reviewed_by": reviewers.get(name),
                     "configured_checks": configs_by_name.get(name, [])}
            if block:
                entry["declaration_lines"] = [block["line_start"], block["line_end"]]
            ties.append(entry)
        edition.add(f"fidelity/{ident}.json", {**statement, "lean": ties,
                    "passages": passages_by_statement.get(ident, []),
                    "semantic_probes": by_statement.get(ident, [])})
