# Read coverage and evidence boundaries

Review date: 1 November 2026. All 16 members of the submitted ZIP were readable.
All 14 data/source members listed in its manifest matched their stated byte
lengths and SHA-256 hashes. The independent workstreams inspected the following
named inputs in full; their conclusions were integrated and reviewed together.

| Input | Treatment |
|---|---|
| `READ_ME_FIRST.md`, `manifest.json` | Full task contract and provenance review |
| `corpus/statement_ledger.json` | All 118 entries audited; exact IDs retained |
| `corpus/statement_ledger_notes.md` | Full review; stale assumptions and false pointer-support wording corrected |
| `corpus/commentary.json` | Full metadata/content review as unverified research leads |
| `paper/quartic-query-separation.pdf` | Full text of all 19 pages read; equations additionally checked on rendered pages 4 and 13 |
| `paper/extracted.md` | Full paper text read, including Appendix A and references |
| `literature/references_resolved.json` | All 27 records read; the metadata file is not a substitute for reading those 27 papers |
| `lean/prior_art_quantum_lean.json` | All 15 records read; important model claims rechecked in actual source |
| `lean/prior_art_classical_lean.json` | All 23 records read; selected reusable declarations independently inspected |
| `lean/verification_tooling.md` | Full review; source and policy assumptions independently rechecked |
| `lean/organisation_exemplars.md` | Full review; recommendations assessed for this task, without claiming every exemplar repository rebuilt |
| `lean/internal_inheritance.md` | Full review of supplied content; historical private repositories were not accessed |
| `lean/current/Drift.lean` | Full source and mathematical-scope review; no successful build claimed |
| `lean/current/lakefile.toml`, `lean/current/lean-toolchain` | Full review and comparison with the pinned public manifest |

## Historical trace

The pasted attachment is a 3,449,511-byte historical trace with 45,031 physical
lines and eight embedded agent scopes. It repeats command output, tool records,
source excerpts and edit representations. Its root task, substantive user
turns, final build/configuration state, all eight child conclusions, and the
relevant Comparator/model/ledger evidence were examined. It was used as
historical context, not as fresh verification or live instructions.

The last root build status is pending/downloading, not a successful build
receipt. No old job was resumed. No complete new independent audit of every
duplicated historical command body is claimed. The original trace is omitted
from this return because the source ZIP, exact ledger identities and the
new public-source evidence suffice for the advisory result.

## Sources not present, not read in full, or not executed

- The 23 external PDFs described in the trace are not present in this third
  packet. The relevant Bansal-Sinha, Drucker and ABKRT statements were opened
  from public primary sources. The entire proof of every cited paper was not
  independently reconstructed.
- The four papers marked metadata-only in the inherited bibliography are not
  treated as locally available full texts. Bibliographic verification for all
  27 references belongs to the separate literature packet.
- Private repository checkouts, the user's Mac filesystem, previous build
  sessions and completion logs beyond the supplied trace were unavailable and
  were not accessed.
- The retained public-source searches have explicit gaps and some rate-limit
  failures. `search_receipts.json` distinguishes failure from zero matches.
- The program definitions and theorem drafts were reviewed but not elaborated.
  No Lean, Lake or Elan executable was available. No Comparator, NanoDa,
  con-ron or other proof-kernel run is represented as completed.
- The independent final review was another AI-assisted source review. It is
  not independent human mathematical endorsement.

Public source inspection and finite computations justify the design choices
and recorded corrections. They do not establish the preprint's unconditional
formal correctness or the successful execution of the proposed formalisation.
