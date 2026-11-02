#!/usr/bin/env python3
"""Read-only structural and integrity validation of this section return.

This is not Lean, Comparator, or an independent proof of the mathematics.
The optional --report writes the JSON result to an explicitly chosen file.
"""
import argparse
import ast
import hashlib
import json
import re
import shutil
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--packet", type=Path, help="Optional original extracted input packet for source hashes and canonical IDs")
    ap.add_argument("--report", type=Path, help="Optional destination for this validation result; default only prints")
    args = ap.parse_args()
    errors = []
    checks = {}
    def require(condition, message):
        if not condition:
            errors.append(message)
    def read_json(name):
        return json.loads((ROOT/name).read_text())

    required = [
        "README.md", "section.md", "section.pdf", "correspondence.json",
        "NEW_STATEMENTS.json", "STATEMENT_CHANGES.json", "LEAN_GAPS.md",
        "references.bib", "source_read_receipt.json", "review_notes.md",
        "STYLE_RULES.json", "manifest.json", "checks/exact_example_checker.py",
        "checks/exact_example_results.json", "checks/audit_evidence.py",
        "checks/render_section.py", "checks/pdf_header.tex", "checks/pdf_layout.lua",
        "evidence/lean_declarations.json", "evidence/correspondence_coverage.json",
        "evidence/pdf_review.json", "evidence/integrity_summary.json"
    ]
    for p in required:
        require((ROOT/p).is_file(), "Missing required file: "+p)
    if errors:
        result={"passed":False,"errors":errors}
        print(json.dumps(result,indent=2))
        return 1
    json_files = sorted(ROOT.rglob("*.json"))
    for path in json_files:
        try:
            json.loads(path.read_text())
        except (ValueError,UnicodeError) as e:
            errors.append(f"Invalid JSON {path.relative_to(ROOT)}: {e}")
    for path in ROOT.rglob("*.py"):
        try:
            ast.parse(path.read_text(),filename=str(path))
        except (SyntaxError,UnicodeError) as e:
            errors.append(f"Invalid Python syntax {path.relative_to(ROOT)}: {e}")
    checks["required_files"] = len(required)
    checks["parsed_json_files"] = len(json_files)

    section = (ROOT/"section.md").read_text()
    section_sha = sha(section.encode())
    require(not any(ord(c)<32 and c not in "\n\r\t" for c in section), "Section contains unexpected control characters")
    anchors = {}
    for m in re.finditer(r"<!-- passage:([A-Za-z0-9_]+) -->",section):
        name=m.group(1)
        end=section.find(f"<!-- /passage:{name} -->",m.end())
        require(name not in anchors,"Duplicate passage: "+name)
        require(end>=m.end(),"Unclosed passage: "+name)
        anchors[name]=(m.end(),end)
    require(len(anchors)==13,"Unexpected passage anchor count")
    correspondence = read_json("correspondence.json")
    registry_doc = read_json("evidence/lean_declarations.json")
    registry = registry_doc["declarations"]
    require(registry_doc["section_sha256"]==section_sha,"Declaration registry section hash mismatch")
    row_ids=[r["id"] for r in correspondence]
    require(len(set(row_ids))==len(row_ids),"Repeated correspondence ID")
    used_names=set()
    intervals=[]
    valid_roles={"states","defines","proves","explains","uses","mentions"}
    required_fields={"passage","from","to","role","statement_ids","lean","complete_lean_types",
                     "ordinary_premises","open_assumptions","relation","route","citation_role","evidence","span"}
    bib=(ROOT/"references.bib").read_text()
    bibkeys=set(re.findall(r"@\w+\{([^,\s]+),",bib))
    require(bibkeys=={"OAI26","AA14/18","BS20v3"},"Unexpected bibliography keys")
    for row in correspondence:
        rid=row["id"]
        require(required_fields<=row.keys(),rid+": missing correspondence fields")
        require(row["role"] in valid_roles,rid+": invalid role")
        require(row["passage"] in anchors,rid+": missing passage")
        span=row["span"]
        start,end=span["start_character"],span["end_character_exclusive"]
        text=section[start:end]
        require(text==span["text"],rid+": span text mismatch")
        require(sha(text.encode())==span["sha256"],rid+": span hash mismatch")
        require(span["section_sha256"]==section_sha,rid+": source hash mismatch")
        require(text.startswith(row["from"]) and text.endswith(row["to"]),rid+": boundary excerpts do not match")
        lo,hi=anchors[row["passage"]]
        require(lo<=start<end<=hi,rid+": span is outside its passage")
        require(section.count("\n",0,start)+1==span["start_line"],rid+": start line mismatch")
        require(section.count("\n",0,end-1)+1==span["end_line"],rid+": end line mismatch")
        intervals.append((start,end,rid))
        named=[t["declaration"] for t in row["complete_lean_types"]]
        require(named==row["lean"],rid+": Lean names and type records differ")
        for typ in row["complete_lean_types"]:
            name=typ["declaration"]
            used_names.add(name)
            require(name in registry,rid+": absent registry declaration "+name)
            if name in registry:
                full=registry[name]
                for k in ["source_signature","complete_source_type","source_member","source_sha256"]:
                    require(typ[k]==full[k],rid+": type catalog mismatch "+name+" / "+k)
                require(bool(typ["source_signature"]) and bool(typ["complete_source_type"]),rid+": empty exact type")
        for cit in row["citation_role"]:
            if "key" in cit:
                require(cit["key"] in bibkeys,rid+": undefined bibliography key "+cit["key"])
        require(row["evidence"]["fresh_lean_run"] is False,rid+": unexpected fresh Lean claim")
        require(row["evidence"]["fresh_comparator_run"] is False,rid+": unexpected fresh Comparator claim")
    require(used_names==set(registry),"Catalog and mapped name sets differ")
    checks["correspondence_entries"]=len(correspondence)
    checks["passage_anchors"]=len(anchors)
    checks["mapped_declarations"]=len(registry)

    def coverage(start,end):
        return [rid for a,b,rid in intervals if a<=start and end<=b]
    displays=list(re.finditer(r"(?ms)^\$\$\n.*?^\$\$",section))
    require(len(displays)==32,"Unexpected display count")
    require(section.count("\n$$")==64,"Unbalanced display delimiters")
    for i,m in enumerate(displays,1):
        rid=coverage(m.start(),m.end())
        require(len(rid)==1,f"Display {i} has {len(rid)} mappings")
        if rid:
            row=correspondence[row_ids.index(rid[0])]
            require(f"display-{i:02}" in row["span"]["displays"],f"Display {i} identifier mismatch")
    tables=list(re.finditer(r"(?m)(?:^\|[^\n]+\|[ \t]*\n)+",section))
    require(len(tables)==2,"Unexpected Markdown table count")
    for i,m in enumerate(tables,1):
        require(len(coverage(m.start(),m.end()-1))==1,f"Table {i} not mapped once")
    # Independent line-level coverage: every substantive line must lie in one mapped span.
    substantive=0
    position=0
    for line in section.splitlines(keepends=True):
        clean=line.strip()
        if clean and not clean.startswith("#") and not clean.startswith("<!--"):
            start=position+len(line)-len(line.lstrip())
            end=position+len(line.rstrip())
            require(len(coverage(start,end))==1,f"Unmapped or multiply mapped content line at character {start}")
            substantive+=1
        position+=len(line)
    blocks=[b for r in correspondence for b in r["span"]["content_blocks"]]
    require(len(blocks)==103 and len(set(blocks))==103,"Content block identifiers missing or repeated")
    marked=set(re.findall(r"<!-- claim:([^ >]+) -->",section))
    mapped_ids={s for r in correspondence for s in r["statement_ids"]}
    require(marked<=mapped_ids,"Unmapped marked claims: "+str(sorted(marked-mapped_ids)))
    checks.update(display_blocks=len(displays),markdown_tables=len(tables),
                  substantive_lines_covered=substantive,unique_content_blocks=len(set(blocks)))

    new=read_json("NEW_STATEMENTS.json")
    expected={"R3-FOR-COHERENT-LAW","R3-FOR-THREE-EXAMPLES","R3-FOR-CIRCUIT-SIZE"}
    require({x["id"] for x in new}==expected and len(new)==3,"Unexpected new statements")
    require(read_json("STATEMENT_CHANGES.json")==[],"Canonical statements unexpectedly changed")
    for row in new:
        require({"id","statement","why_needed","depends_on","proposed_lean","route_note"}<=row.keys(),
                row["id"]+": missing new statement fields")
        require(row["proposed_lean"] is None and row["lean"]==[],row["id"]+": unexpected new formal claim")
        require(row["passage"] in anchors,row["id"]+": missing anchor")
    examples=read_json("checks/exact_example_results.json")
    require(examples["passed"] is True,"Finite check report failed")
    require([x["input_count"] for x in examples["families"]]==[256,4096],"Wrong finite input scope")
    require(examples["families"][0]["census"]=={"0":48,"1":104,"undefined":104},"Census mismatch")
    integrity=read_json("evidence/integrity_summary.json")
    require(integrity["integrity_checks_passed"] is True,"Supplied evidence audit failed")
    checks["finite_checks_recorded_passed"]=True
    checks["canonical_statements_changed"]=0

    source_hash_checks=0
    if args.packet:
        packet=args.packet.resolve()
        require((packet/"manifest.json").is_file(),"--packet is not the original extracted packet")
        if (packet/"manifest.json").is_file():
            receipt=read_json("source_read_receipt.json")
            for rec in receipt["sources"]:
                p=packet/rec["member"]
                require(p.is_file(),"Missing source: "+rec["member"])
                if p.is_file():
                    require(sha(p.read_bytes())==rec["sha256"],"Source changed: "+rec["member"])
                    require(p.stat().st_size==rec["bytes"],"Source size changed: "+rec["member"])
                    source_hash_checks+=1
            for name,rec in registry.items():
                p=packet/rec["source_member"]
                require(p.is_file(),"Missing mapped Lean source: "+rec["source_member"])
                if p.is_file():
                    require(sha(p.read_bytes())==rec["source_sha256"],"Mapped source changed: "+name)
                    require(rec["source_signature"] in p.read_text(),"Source signature not found: "+name)
                    source_hash_checks+=1
            baseline=packet/"repository/research/returns/funnel/1_long_reasoning_record"
            old=json.loads((baseline/"correspondence.json").read_text())
            known={s for row in old for s in row["statement_ids"]}
            known|={x["id"] for x in json.loads((baseline/"NEW_STATEMENTS.json").read_text())}
            used=mapped_ids|{s for x in new for s in x["depends_on"]}
            require(used<=known|expected,"Unknown statement IDs: "+str(sorted(used-known-expected)))
    checks["optional_packet_source_records_checked"]=source_hash_checks

    pdf=ROOT/"section.pdf"
    require(pdf.read_bytes().startswith(b"%PDF-"),"Invalid PDF header")
    qa=read_json("evidence/pdf_review.json")
    require(qa["source_sha256"]==section_sha,"PDF source QA hash mismatch")
    require(qa["rendered_sha256"]==sha(pdf.read_bytes()),"PDF QA artifact hash mismatch")
    require(qa["visual_review"]["pages_inspected"]==list(range(1,10)),"Incomplete recorded visual review")
    if shutil.which("pdfinfo"):
        info=subprocess.run(["pdfinfo",str(pdf)],capture_output=True,text=True,check=True).stdout
        require(re.search(r"Pages:\s+9\b",info) is not None,"Unexpected PDF page count")
    if shutil.which("pdftotext"):
        txt=subprocess.run(["pdftotext",str(pdf),"-"],capture_output=True,text=True,check=True).stdout
        for s in ["3.1.", "3.2.", "3.3.", "3.4.", "3.5.", "References used", "104", "Bansal"]:
            require(s in txt,"Missing rendered text: "+s)
        require("\ufffd" not in txt,"PDF text contains replacement characters")
    checks["pdf_pages_recorded_visually_reviewed"]=9

    manifest=read_json("manifest.json")
    actual={p.relative_to(ROOT).as_posix():p for p in ROOT.rglob("*") if p.is_file() and p.name!="manifest.json"}
    indexed={r["path"]:r for r in manifest["members"]}
    require(set(actual)==set(indexed),"Manifest member inventory mismatch")
    for name,p in actual.items():
        require(not p.is_symlink(),"Unexpected symbolic link: "+name)
        if name in indexed:
            r=indexed[name]
            require(p.stat().st_size==r["bytes"] and sha(p.read_bytes())==r["sha256"],"Output manifest mismatch: "+name)
    checks["manifest_members_verified"]=len(indexed)
    result={
        "schema":"quartic-r3-02-return-validation-v1",
        "passed":not errors,
        "section_sha256":section_sha,
        "checks":checks,
        "errors":errors,
        "scope":"Structural correspondence, source/hash integrity, recorded finite-check status and PDF metadata/text. Ordinary proofs were reviewed separately; this script is not Lean, Comparator or a kernel proof.",
        "fresh_lean_run":False,
        "fresh_comparator_run":False
    }
    if args.report:
        args.report.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result["passed"] else 1

if __name__=="__main__":
    raise SystemExit(main())
