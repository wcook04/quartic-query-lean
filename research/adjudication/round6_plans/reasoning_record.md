# Round six: revision plan for the reasoning record

Inputs: the four round-six panel returns (60 findings on the record), the
current `docs/reasoning_record.md` (sha256 `2c9971d1…`, HEAD `9bdd443`) and the
operator's direction of 3 November. Dispositions, one row per finding, are in
[`../round6_dispositions/reasoning_record.json`](../round6_dispositions/reasoning_record.json):
33 fix, 25 keep, 1 decline (CX027), 1 defer (FX032). All 60 quotes were found
in the current Markdown; the supplied PDF predates it.

## Operator direction and how it changes the weighting

Will wants the papers to read like ordinary mathematical literature, with the
bureaucracy outside the PDF, and every sentence improved. For the record this
means:

- The mathematical body (§§1–7, Appendix A) reads as a long paper. Lean names,
  receipts, review authorities and chronology leave the body and collect in one
  new **Appendix G, Formal statements and evidence**, plus repository sidecars.
  Claim markers stay (they are invisible HTML comments).
- Reading routes are fixed once, in the front matter, not with status labels in
  each section.
- Exposition findings (C1, C2, C4, C5) come first. Evidence findings (C3) are
  done by moving and separating material, never by adding labels in the body.
- A line-edit pass covers everything a reader is routed through first.

## Phase 1. The front-matter route guide (C1)

Replace "Who each part is for" and the three-column table (lines 14–23, outside
passages) with a short guide of four routes. Remove "required" everywhere.

| Route | Read | Accept as cited, and why that is safe | Second route, and its reason |
|---|---|---|---|
| The construction (first reading, either specialism) | §1; §2.1 and §§2.3–2.4 (one algorithm for all inputs, all-input worst-case cap, one-sided promise); §3 preview and §§3.1–3.4 (contracts; skip the gate arithmetic and the §3.5 census); §3.17; §4 (skip the §4.5 remark); §§5.1–5.4; §6 (Lemma 4.1 statement and the cap-event corollary, then §§6.2–6.6); §§7.1–7.2 | Forrelation hardness: Bansal–Sinha Thm 1.3 and Cor. 1.4 imply (F3) by (F4)–(F5) in §3.6. Universal bound: ABKRT Thm 2, through the four-link bridge at the head of Appendix A | — |
| The complete proof | the construction route plus §§3.6–3.15, the §6.1 conditional-value proof and §§A.1–A.5 | — | §§3.6–3.15 give the explicit threshold 13669k² and the uniform estimate (F43) that §7.4 uses; Appendix A fixes the constant 35⁴ |
| Model audit | §2.2 minima, §2.5 bridges, §2.6 examples (risk map), §§2.7–2.8, the §4.5 remark | — | — |
| One formal statement | Appendix G.1 (bounded check), then G.2–G.8 as needed; §5.6 and the formal parts of §6.1 that the headline roots reach | — | — |

Literature audits (Appendices D, E) and execution history (Appendix F) are
listed once below the table. §1.1 "Dependencies" and "Reading routes" then cite
these routes by name; delete "They remain in their original numbered location
so every returned proof locator stays usable" (internal reasoning).

Labels that change, all outside passages: §5.6 heading drops "Optional" and its
first sentence names both audiences (QX-037, FX031); §4.5 becomes a remark
(CX029); a purpose sentence precedes the §6.1 second proof (CX005); the §3
preview gains the forward pointer from S to K and verification (QX-030); an
example risk map opens §2.6 (FX034), every locator verified first. FX031: read
`corpus/lean_dependencies.json` before listing the §6.1 second proof or the §6.4
alternatives on the formal route.

## Phase 2. Mathematical exposition (C2, C4, C5)

- **§7.4, letting k grow (QX-003).** New unclaimed passage `ROOT-GROWING-K`
  after §7.3, holding the derivation that the companion remark summarizes. Derive
  every inequality by hand. A numerical scan for t in [80, 5000] and three
  larger t found no failure of R ≥ Q^{4−ε(ℓ)}, but that scan is not the proof.
  End with the fact that no R = Ω(Q⁴) follows. Point to it from the end of
  `ROOT-NO-SMALLER` and from line 88 of `R3-01-QUANTIFIERS`. Coordinate with the
  expert adjudicator, who decides what stays in the companion.
- **§3.6 entry (QX-033, CX016, QX-032).** One paragraph in `forr_proof_spine`
  covering three things. What is cited: BS Theorem 1.3. What is reused: the BS
  Gaussian chain and rounding, BS Lemma 4.3, and GTW tree growth. What is
  reconstructed here: (F9), first-block interpolation (one raw derivative per
  block, against the level-k..k(k−1) weights in BS Theorem 3.2, with uniform
  levels kept by (F24)) and the stopped martingale. Reason for (F9): BS use Φ−½
  and Owen's T, while (F9) satisfies (Ψγ)′ = −φγ in algebraic functions, so the
  constants come out explicit and elementary. Make no novelty claim.
- **§6.6 (QX-034).** The BS v3 line forensics shrink to one pointer to Appendix E.
- **Appendix E (CX025).** Headings by purpose; one sentence on what (F60) yields.
- **§4.2 input length (QX-028).** Add a paragraph after `AC-layout`:
  m[m + rkm + 2^r((m−1)ℓ + rS)] = O_k(m²²ℓ³) bits. The record's n is km, so no
  new n.
- **CX026.** One sentence in `AC-attribution` on the inherited role of a unique
  accepting certificate.
- **CX008.** Correct the classical heuristic at lines 10 and 137: two routes,
  lucky guesses allowed, few heavy columns.
- **QX-036.** Delete the BHMT Theorem 12 sentence.

## Phase 3. Concentrate the evidence apparatus (C3)

Create **Appendix G, Formal statements and evidence**, after Appendix F.

- **G.1 Checking one statement** (FX028; anchor `#record-statement-check`). One
  configured target, R/Q definitions with read-all witnesses, the Solution
  forwarding, one revealing control, what the check concludes and what it
  does not.
- **G.2 Model map** (FX036, QX-029): definitions, proved translations and
  ordinary identifications. It includes the deferred-measurement contract and
  the warning that equal acceptance laws do not identify the output subsystem.
- **G.3 Statement table** (QX-008, FX027, FX030, FX029). This is the old second
  table of §2.9 with separate columns: execution status; corpus relation (bound
  to the 2 November sources); round-five textual review (3 November, automated,
  Lean not run); "stronger in / weaker in" for the exceptional rows; pinned type
  links. No status is raised by inference.
- **G.4–G.8.** The per-section formal passages move here intact (moved only, no
  body change): `forr_validation_scope` (trimmed, QX-035), `AC-evidence`,
  `upper-current-formal-scope` (its pointer "stated precisely below" retargeted),
  `upper-missing-physical-state` (claim `r3-q-physical-state-bridge` moves with
  it), the Lean half of `CL-literature-and-verification` as a new passage
  carrying FX026 (recursive `actualComplies` against `actualCount`, ordinary
  equivalence, finite seeds per FX043), `CL-formal-scope`,
  `ROOT-EXPONENT-CORRESPONDENCE`, `R3-A-ASSEMBLY` and `R3-A-FORMAL`.

The section numbers §§2.9, 3.16, 4.8, 5.5, 6.7, 7.3 and A.6 stay, so returned
locators keep working. Each keeps two to four reader-level sentences: what is
formalized, which route the headline uses, the one material qualification and
a link to G. Body §2.9 keeps the four headline statements in mathematical form.
FX033 makes Appendix F's tense explicit. FX032 is deferred to a sidecar view,
captured for the backend.

## Phase 4. Line-edit pass (first-routed text)

| Place | Weakness | Intended improvement |
|---|---|---|
| Title | "complete reasoning record" is a house name | "…: complete proofs" (coordinate citations in the two short papers before changing) |
| Guide, "What is new" | heading promises novelty, then says everything is OpenAI's; "direct proof"; "exact small examples that test each convention" is vague | "What this record adds"; "an independent proof of the Forrelation lower bound"; name the examples; point formal statements to Appendix G |
| Guide, mechanism | classical sentence overstates (CX008) | two-route probabilistic sentence |
| §1.1 ¶4 | "a lower budget of order mL" | "a classical algorithm needs order mL queries" |
| §1.1 dependencies | locator-preservation aside; table duplicates the guide | cut the aside; keep the table as the dependency map only |
| §1.1 reading routes | long meta paragraph about destinations | two sentences: where the short papers enter and where they return |
| Where the exponent stood | "cheat sheets combined with …" gives no citation at first use; L heuristic | cite ABK cheat sheets; heuristic as CX008 |
| §2 lead | "lists the formal statements that are checked against them" | describe the models; the formal list is in Appendix G |
| §3 preview | "A reader who accepts property 1 …" duplicates the guide | keep one sentence; add the S → K pointer |
| `AC-interface` | "All queries below reveal one physical input bit." | "Every query reads one input bit." |
| `upper-section-interface` | "a correction of its formal correspondence"; "We repeat the particular uses of these facts below."; last sentence about formal evidence | "This section reconstructs the proof in full and adds an exact cyclic example; it changes no claim of the preprint."; delete; replace with a pointer to Appendix G |
| `upper-purpose` | sound; the list of antecedents is long before the method | move the antecedent paragraph after the drift sentence's consequence, unchanged |
| §6 target | one paragraph holding target, a five-link plan and a return note | target; a four-step numbered plan (coupling, erased zero, planted cell, heavy columns); the return note moves to the reading routes |

The executor finishes this pass sentence by sentence over §§1, 3.6, 4, 5 and
6 opening, plus the §§5.2 and 6.1 statements. Where a sentence in a
claim-bearing passage is genuinely badly written, improve it and accept the
re-audit; skip cosmetic-only changes there.

## Passages touched, and re-audit

- **Claim-bearing, body changed (re-audit required):** `R3-01-QUANTIFIERS`
  (line 88), plus any the line-edit pass selects, each listed in the audit.
- **Claim-bearing, moved only:** `upper-missing-physical-state`.
- **Claim-bearing, deliberately untouched:** `forr_threshold`, `forr_stein`,
  `forr_small_instance`, `forr_circuit`, `forr_boolean_arithmetic`,
  `CL-weighted-values`, `ROOT-RESULT`, `forr_bundle`.
- **Unclaimed, body changed:** `ROOT-NO-SMALLER`, `forr_proof_spine`,
  `CL-forrelation-input`, `forr_ssw_comparison`, `AC-attribution`,
  `upper-amplification-statement`, `R3-01-BRIDGES`, `AC-interface`,
  `upper-section-interface`, `forr_validation_scope`,
  `upper-current-formal-scope`, `CL-literature-and-verification` (split),
  `history-evidence-convention`.
- **Added:** `ROOT-GROWING-K` and the Lean half of the §6.1 sources.

After editing, run `python3 tools/rebind_record_passages.py --report
research/adjudication/round6_record_rebind.json`. No passage may be removed: a
split keeps the original id. Then write a passage meaning audit in the form of
round five, comparing every `text_changed` and `added` passage with HEAD, and
render the PDF. Check the moved anchors and every incoming anchor from the two
short papers.

## Coordination

- **Expert adjudicator:** the growing-k remark (QX-003/QX-052). The record will
  host the derivation at `#ROOT-GROWING-K`.
- **Both short papers:** the new anchors `#record-statement-check` (FX003–FX006,
  FX010, FX017, SX-033) and Appendix G. After the record lands, their pins move
  from `e9dfefb`. The record's §2.9 links pin `659b571`; the Unconditional
  statement files are identical at `e9dfefb`, so one snapshot map can serve all
  three documents (FX002, QX-006, CX014).
- **Shared evidence wording:** the round-five textual-review label must read the
  same in all three documents (CX004, FX001).

## Execution notes (3 November 2026)

Executed. Departures from the plan above:

- **Growing-$k$ derivation.** It is §7.3, not §7.4. §7.3 "Formal correspondence" moved into Appendix G, so the new section takes its number. The proved constant is **514**, giving $\varepsilon(\ell)=8\sqrt{10/\ell}+(56\log_2\ell+514)/\ell$. The companion's 508 passes the same numerical scan, but the inequality chain written in the record yields 514. The expert companion should either cite 514 or derive 508.
- **Evidence apparatus.** It now sits in Appendix G, after F. The old §§2.7–2.9 are G.2–G.4. The old §5.5 formal routes and returned-state target are G.7, and the old §6.7 is G.8. The Lean half of the §6.1 sources and the former §7.3 are G.8–G.9.
- **Section numbers.** The Boolean-continuation subsection is now §5.5. No section numbers cited by the short papers changed: they cite §§3.3–3.6, 3.15–3.16, 4.4, 5.1–5.4, 6, 6.1–6.6, 2.2–2.5.
- **Expert handoff.** All three items are incorporated: the Drucker remark in §6.1 and §6.2, the growing-$k$ derivation in §7.3, and the corrected amplifier row in G.4. The full row list from the handoff is in G.4, together with the bundle-boundary sentence. Appendix F points to the README reproduction section.
- **Generated files and tests.** Two files outside my listed ownership changed. `corpus/comparator_map.json` was regenerated with `tools/build_comparator_map.py`, because it quotes record passages. `tests/test_render_reasoning_record.py` had its pinned anchor and link counts updated to (365, 281). `make check` passes.

## New and renamed anchors for the short-paper revisers

All old anchors still resolve. Some now sit in a different place, as listed below.

| Anchor | Where it is now | Content |
|---|---|---|
| `#formal-appendix` (new) | Appendix G heading | Formal statements and evidence |
| `#record-statement-check` (new) | Appendix G.1 | Bounded check of one statement (`Checked.theorem_one_one`), with what it establishes |
| `#formal-models-map` (new) | Appendix G.2 | Definitions, proved translations and ordinary identifications |
| `#ROOT-EVIDENCE-CONVENTION` (moved) | Appendix G.2 | Formerly §2.7 |
| `#evidence-checks` (moved) | Appendix G.3 | Formerly §2.8; semantic controls and the shared-specification control |
| `#checked-statements` (moved) | Appendix G.4 | Formerly §2.9; statement table with corpus and textual-review columns |
| `#forr_validation_scope` (moved) | Appendix G.5 | Forrelation formal scope |
| `#AC-evidence` (moved) | Appendix G.6 | Construction declarations |
| `#upper-current-formal-scope` (moved) | Appendix G.7 | Measured-label and list routes |
| `#upper-missing-physical-state` (moved) | Appendix G.7 | Returned-state target |
| `#CL-direct-product-formal` (new) | Appendix G.8 | Realized-caps endpoint; recursive `actualComplies` against `actualCount`; finite seeds |
| `#CL-formal-scope` (moved) | Appendix G.8 | Formerly §6.7 |
| `#ROOT-EXPONENT-CORRESPONDENCE` (moved) | Appendix G.9 | Formerly §7.3 |
| `#R3-A-ROUTES` (new) | Appendix G.9 | Three quartic routes table, formerly in §A.6 |
| `#R3-A-FORMAL` (moved) | Appendix G.9 | Appendix A declarations |
| `#ROOT-GROWING-K` (new) | §7.3 "Letting $k$ grow with $t$" | Growing-$k$ derivation, (7.5)–(7.6) |
| `#upper-continuation-induction` (unchanged anchor) | now §5.5 | Sequential verification; formerly §5.6 |
| `#CL-literature-and-verification` (unchanged anchor) | §6.1 "Sources" | Now holds the Drucker remark and credit only |
| `#ai-disclosure` (new) | final section "Use of AI tools" | Attribution and the no-review statement |
| `#record-reading-guide` (unchanged) | front matter | Four-route reading guide |

## Second pass (3 November 2026)

- **Line edit.** §§3–7 were line-edited throughout. Of 501 edits, 44 were corrected after an independent audit. Details are in `round6_record_passage_audit.md` (second-pass section) and `round6_record_lineedit_audit.json`.
- **§7.3.** It now states $\varepsilon$ with **508**, via the exact identity $40k+\ell/k-80x=40(x-k)^2/k<20$. The chain gives 474. The record and the companion now agree.
- **Exposition handoff.** All ten anchors the exposition uses are unchanged. Appendix G.4 already carries the round-five amplifier and direct-product judgments. Two notes were added:
  - `AC-example-tests` prints the board's 5936 input bits.
  - `CL-simulator-example` has a crosswalk to the exposition's board, linking `#CL-tiny-planted-example`, an existing anchor.
- **Anchors.** No new anchors in this pass.
- **Remaining `make check` failure.** `tools/build_lean_links.py --check` and its unit test fail. The cause is that `docs/expert_companion.md` links to `#ROOT-GROWING-K` and `#CL-direct-product-formal`, which do not exist at the pinned commit `e9dfefb`. `COMMIT` in `tools/build_lean_links.py`, which the coordinator owns, has to move to a commit that contains this record. Every other check passes.
