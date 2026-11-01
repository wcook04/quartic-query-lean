#!/usr/bin/env python3
"""Build the three independent Type B research ZIPs for the quartic separation."""
import argparse
import hashlib
import json
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
INTAKE = ROOT / "research" / "intake"
SOURCES = pathlib.Path.home() / "src" / "quartic-query-sources" / "papers"
ANNEX = pathlib.Path.home() / "src/ai_workflow/annexes/openai-math-284-quartic-query-separation"
SIBLINGS = pathlib.Path.home() / "src/ai_workflow/annexes"

BOUNDARY = """## Boundaries

- Do not access Gmail or any other mailbox, connect any account, or request credentials. Use public web research and this packet only.
- This work is advisory. Our team decides what enters the repository.
- Everything here is unreviewed. The paper is an OpenAI preprint, and the ledger and prior-art files were prepared by AI agents. Check them against the paper rather than trusting them.
- Separate what you verified from what you infer. Give a URL or file and location for every factual claim, and say what would overturn each important conclusion.
- "Nearly quartic" means exponent 4 - 2/k for each fixed k. Never shorten it to a fourth-power family.
- Read every readable file your job names. List anything you could not read.
"""

COMMON = """# {title}

## Context

Will Cook, an economics undergraduate, is preparing an explanation of "A Nearly Quartic Separation Between Randomized and Quantum Query Complexity" (OpenAI, 5 October 2026). The first intended reader is Scott Aaronson, who named this result among those he cares about. Alongside the explanation, we are building a private Lean corpus, `quartic-query-lean`, in which every statement of the paper has a row and every formal claim is checked by Lean and Comparator.

No paper is being written in this round. We want understanding, sources and a checkable plan.

Start with `READ_ME_FIRST.md`, then `manifest.json`. The paper is at `paper/quartic-query-separation.pdf`. `paper/extracted.md` is its line-numbered text source for citations.

{job}

{boundary}
"""

JOBS = {
    "1_understand_the_paper": ("Understand and audit the paper", """## Your job: mathematical understanding and proof audit (proof/claim audit; no new theorems required)

Read the whole paper, then read cited papers wherever the argument depends on them.

1. Explain the proof from first principles to a reader who knows linear algebra and basic probability but no query complexity. Define R, Q, partial and total functions, Forrelation, certificates and cheat sheets before using them.
2. For every row of `corpus/statement_ledger.json`, say what it means, why it is needed and which step is hardest. Correct any row that misstates the paper.
3. Check every proof step yourself. Report gaps, hidden assumptions, constants, and places where the construction could fail, especially: behaviour outside the promise in the tournament; the planted-input lower bound; the adaptive direct-product argument; parameter choices r, l, epsilon and T.
4. Say which ideas are new compared with Aaronson, Ben-David and Kothari's cheat sheets, Bansal and Sinha, and Sherstov, Storozhenko and Wu.
5. Give hand-sized worked examples: the smallest board where the winner rule, outward pointers and tournament can be computed by hand, with exact numbers.

## Return one ZIP containing

- `understanding.md`: the first-principles explanation.
- `statement_review.json`: one row per ledger id with keys `id`, `verdict` (`correct`, `corrected`, `doubtful`), `plain_meaning`, `why_needed`, `hard_step`, `correction`, `evidence`.
- `audit_findings.json`: keys `location`, `severity`, `claim`, `reasoning`, `how_to_confirm`.
- `worked_examples.md`: computed examples.
- `further_reading.json`: keys `title`, `url`, `why`, `statement_ids`.
"""),
    "2_ground_in_literature": ("Ground every step in the literature", """## Your job: literature and attribution review

Our aim is reference material for every part of the paper. `literature/references_resolved.json` lists all 27 citations, and `literature/papers/` holds the 23 copies we could obtain.

1. Read every supplied paper far enough to state the exact theorem this paper uses, and its number in the source.
2. Check the citations: is each cited result stated correctly, with hypotheses that fit how it is used? Check especially Bansal and Sinha Theorem 1.3 and Corollary 1.4, the direct-product citations [22, 13], and the upper bound from Aaronson, Ben-David, Kothari, Rao and Tal.
3. Find everything else we should download: original sources behind cited results, later simplifications, surveys, lecture notes, textbooks, theses, talks and transcripts, and follow-ups to this preprint. Search arXiv, ECCC, DBLP, Semantic Scholar, authors' pages, and university course notes. Cover the four papers we could not fetch: Barnum-Saks-Szegedy, Nisan, Nisan-Szegedy and Yao.
4. Build a reading path per paper section: what to read, in which order, which pages, and why.
5. Check `corpus/commentary.json` and find any later public discussion, error report or independent check.

## Return one ZIP containing

- `citation_audit.json`: keys `ref_number`, `exact_result_used`, `source_location`, `fits_use` (`yes`, `partly`, `no`, `unclear`), `evidence`, `notes`.
- `downloads.json`: every recommended source, ranked, with keys `title`, `authors`, `year`, `url`, `open_access`, `licence`, `priority` (`essential`, `useful`, `background`), `statement_ids`, `why`. Give direct PDF links where they exist.
- `reading_paths.md`: the per-section reading route.
- `attribution_map.json`: which idea in the paper comes from whom, with evidence.
- `new_commentary.json`: same keys as `corpus/commentary.json`.
"""),
    "3_lean_and_comparator": ("Plan full Lean and Comparator checking", """## Your job: formalisation design

We want to check the whole paper in Lean, with Comparator on each published statement, using as much existing work as possible. Read `lean/prior_art_*.json`, `lean/verification_tooling.md`, `lean/organisation_exemplars.md`, `lean/internal_inheritance.md` and the current Lean in `lean/current/`, which may not have compiled yet.

1. Find every further GitHub repository, Lean Zulip thread, Mathlib pull request or other formalisation we have missed, including work on Forrelation, Fourier growth, direct-product theorems, multiplicative weights, Dürr-Høyer, amplitude amplification, and Bansal-Sinha style lower bounds. Open the source before listing it, and pin a commit.
2. Compare the quantum models in `troyjlee/quantum-query-complexity`, `cslib-community/complexitylib`, `QudeLeap/Lean-QuantumAlg` and `openai/math` (`OAI.Computability.QuantumFactoring`). Recommend one model for this paper, or a bridge, and state the Lean signatures of the core definitions: total and partial Boolean functions, R, Q, the bit oracle, Forrelation P, and F_{k,m}.
3. For each row of `corpus/statement_ledger.json`, give a Lean statement draft, its dependencies, reusable declarations with exact names and commits, estimated size in lines, and difficulty.
4. Design the conditional route: which results enter first as named hypotheses, how to keep them out of Comparator's permitted axioms, and how to remove each one later. Forrelation's lower bound is the expected largest hypothesis.
5. Design the Comparator layout: Statement, Challenge and Solution modules, negative controls that must be rejected, and the exact Palomar preparation needs. We will prepare only; nothing is to be submitted.
6. Check the licences of everything recommended. Check Lean version compatibility; we are on `leanprover/lean4:v4.36.0-rc2` with complexitylib `62ca5c21`.

## Return one ZIP containing

- `new_prior_art.json`: same keys as `lean/prior_art_quantum_lean.json`.
- `model_decision.md`: the recommendation with its reasoning.
- `core_definitions.lean`: draft signatures. Mark it as unbuilt unless you built it.
- `formalisation_plan.json`: one row per ledger id with keys `id`, `lean_statement`, `depends_on`, `reuse`, `estimated_lines`, `difficulty`, `route` (`prove`, `import`, `hypothesis`).
- `comparator_design.md` and `milestones.md`: ordered milestones, each with a pass test.
"""),
}

SHARED = {
    "corpus/statement_ledger.json": INTAKE / "statement_ledger.json",
    "corpus/statement_ledger_notes.md": INTAKE / "statement_ledger_notes.md",
    "corpus/commentary.json": INTAKE / "commentary.json",
    "paper/quartic-query-separation.pdf": ANNEX / "source.pdf",
    "paper/extracted.md": ANNEX / "extracted.md",
}
LITERATURE = {"literature/references_resolved.json": INTAKE / "references_resolved.json"}
LEAN = {
    "lean/prior_art_quantum_lean.json": INTAKE / "prior_art_quantum_lean.json",
    "lean/prior_art_classical_lean.json": INTAKE / "prior_art_classical_lean.json",
    "lean/verification_tooling.md": INTAKE / "verification_tooling.md",
    "lean/organisation_exemplars.md": INTAKE / "organisation_exemplars.md",
    "lean/internal_inheritance.md": INTAKE / "internal_inheritance.md",
    "lean/current/Drift.lean": ROOT / "lean/QuarticQuery/Tournament/Drift.lean",
    "lean/current/lakefile.toml": ROOT / "lean/lakefile.toml",
    "lean/current/lean-toolchain": ROOT / "lean/lean-toolchain",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def papers():
    return {f"literature/papers/{p.name}": p for p in sorted(SOURCES.glob("*.pdf"))}


def members(job):
    out = dict(SHARED)
    if job.startswith("1_"):
        out |= LITERATURE | papers() | {"lean/current/Drift.lean": LEAN["lean/current/Drift.lean"]}
    elif job.startswith("2_"):
        out |= LITERATURE | papers()
    else:
        out |= LITERATURE | LEAN
    return out


def build(job, spec, dest):
    title, text = spec
    files = members(job)
    missing = [str(v) for v in files.values() if not v.is_file()]
    if missing:
        raise SystemExit("missing sources: " + ", ".join(missing))
    keys = [k.casefold() for k in files]
    if len(keys) != len(set(keys)):
        raise SystemExit("case-colliding members")
    request = COMMON.format(title=title, job=text, boundary=BOUNDARY)
    rows = [dict(member=k, source=str(v), bytes=v.stat().st_size, sha256=sha(v)) for k, v in files.items()]
    manifest = json.dumps(dict(packet=job, source_paper="openai/math 4eaee875", members=rows), indent=1)
    path = dest / f"quartic_{job}.zip"
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("READ_ME_FIRST.md", request)
        z.writestr("manifest.json", manifest)
        for k, v in files.items():
            z.write(v, k)
    with zipfile.ZipFile(path) as z:
        if z.testzip() is not None:
            raise SystemExit(f"bad zip {path}")
        for row in rows:
            if hashlib.sha256(z.read(row["member"])).hexdigest() != row["sha256"]:
                raise SystemExit(f"hash mismatch {row['member']}")
    mb = path.stat().st_size / 1e6
    if mb > 500:
        raise SystemExit(f"{path} over 500 MB")
    print(f"{path}  {mb:.1f} MB  {len(rows) + 2} members")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dest", type=pathlib.Path, default=pathlib.Path.home() / "Downloads" / "quartic_type_b_20261101")
    args = ap.parse_args()
    args.dest.mkdir(parents=True, exist_ok=True)
    for job, spec in JOBS.items():
        build(job, spec, args.dest)
