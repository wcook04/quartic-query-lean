"""Build reader-facing fidelity records from Quartic's reviewed ties and recorded checks."""
import hashlib
import re

from build_comparator_map import lean_blocks
from build_corpus import canonical_sha256, currentness, source_hashes
from reading_titles import statement_presentations
from record_reading_dependencies import statement_targets


def evidence_resources(edition, statements, passages_by_statement, comparison, probes, answers_snapshot):
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

    native_path = "corpus/reading_statement_evidence.json"
    inspector_path = "tools/ReadStatementEvidence.lean"
    native = edition.json(native_path)
    edition.resources[native_path] = edition.read(native_path)
    edition.resources[inspector_path] = edition.read(inspector_path)
    current = (native["source_snapshot_sha256"] == canonical_sha256(hashes)
               and native["inspector_sha256"] == hashlib.sha256(edition.read(inspector_path)).hexdigest())
    targets = statement_targets(statements.values(), probes)
    if current and set(native["declarations"]) != set(targets):
        raise ValueError("reviewed declarations or probes changed; refresh the native statement inspection")

    def observation(path, name):
        module = path.removeprefix("lean/").removesuffix(".lean").replace("/", ".")
        result = native["declarations"].get(module + "/" + name)
        if result is None:
            return None
        return {"status": "current" if current else "stale", "receipt": native_path,
                "module": module, **(result if current else {})}

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
    # The previous audit retains its own snapshot. Emit current observations only
    # for the exact module and name returned by the native inspection.
    for key, observed in native["declarations"].items():
        module, name = key.split("/")
        if current:
            axiom_audits[name] = {"axioms": observed["axioms"], "inspector": inspector_path,
                                  "source": "lean/" + module.replace(".", "/") + ".lean",
                                  "receipt": native_path, "snapshot_currentness": "current",
                                  "historical_observation": axiom_audits.get(name)}
    edition.add("axiom-audits.json", axiom_audits)
    by_statement = {}
    for probe in probes:
        ident = probe["statement"]
        path = f"lean/QuarticCorpus/Independent/{probe['file']}.lean"
        name = "QuarticQuery.SemanticReview." + probe["name"]
        observed = observation(path, name)
        historical = name in receipt["declarations"]
        if ident not in statements or (not historical and observed is None):
            raise ValueError(f"unbound semantic probe: {ident}, {name}")
        block = source(path)[name]
        answer_current = current and answers_snapshot == native["source_snapshot_sha256"] and observed is not None
        by_statement.setdefault(ident, []).append({
            "authored_answer": probe["answer"] if answer_current else None,
            "answer_review": "bound_to_snapshot" if answer_current else "needs_review",
            "question": probe["question"], "kind": probe["kind"], "declaration": name, "source": path,
            "inspection": observed,
            "lines": [block["line_start"], block["line_end"]], "receipt": receipt_path if historical else native_path,
            "recorded_status": receipt["status"] if historical else "compiled_and_inspected",
            "receipt_currentness": freshness if historical else observed["status"]})

    edition.add("checks.json", checks)
    intake = {r["id"]: r for r in edition.json("research/intake/statement_ledger.json")}
    findings = {}
    decisions = edition.json("research/adjudication/adjudication.json")
    for finding in decisions["findings"]:
        for sid in finding["ledger_rows_affected"]:
            findings.setdefault(sid, []).append({k: finding[k] for k in
                ("id", "claim", "verdict", "paper_locus", "reason")})
    presentations = statement_presentations(edition, statements)
    for ident, statement in statements.items():
        reviewers = {t["declaration"]: t.get("reviewed_by") for t in authored.get(ident, [])}
        ties = []
        for tie in statement["lean"]:
            name = tie["declaration"]
            block = source(tie["file"]).get(name)
            entry = {**tie, "reviewed_by": reviewers.get(name),
                     "configured_checks": configs_by_name.get(name, []),
                     "inspection": observation(tie["file"], name)}
            if block:
                entry["declaration_lines"] = [block["line_start"], block["line_end"]]
            ties.append(entry)
        earlier = intake.get(ident, {}).get("statement")
        earlier_hash = hashlib.sha256(earlier.encode()).hexdigest() if earlier is not None else None
        if earlier_hash != statement["original_statement_sha256"]:
            raise ValueError(f"{ident}: intake wording differs from its bound hash")
        ledger_history = {"added_in_review": earlier is None, "wording_changed": statement["corrected"],
                          "earlier_ledger_wording": earlier if statement["corrected"] else None,
                          "adjudication_findings": findings.get(ident, [])}
        best = statement["evidence"]["formal_statement"]
        best_matches = [{"declaration": t["declaration"], "file": t["file"]} for t in ties
                        if t["review_evidence"] == "current" and t["relation"] == best and t["built"]]
        edition.add(f"fidelity/{ident}.json", {**statement, "lean": ties, "presentation": presentations[ident],
                    "ledger_history": ledger_history,
                    "review_scope": {"compared_text": "maintained_ledger_statement",
                                     "relation_origin": "authored_review",
                                     "type_and_axioms_origin": "compiled_lean_environment",
                                     "leading_matches": best_matches,
                                     "semantic_examples": "indexed" if ident in by_statement else "none_indexed"},
                    "passages": passages_by_statement.get(ident, []),
                    "semantic_probes": by_statement.get(ident, [])})
