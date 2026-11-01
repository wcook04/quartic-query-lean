# Internal inheritance for this repo

Read 1 Nov 2026, from git refs and read-only. Lean Exposition is `origin/main` c2e7811 (LE). The local checkout sits 18 commits behind, without the alignment layer. `~/src/plectis-erdos` does not exist, so Erdős means `origin/main` ba0d1e8be from a worktree (PE). Counts below are recomputed.

## (a) Reuse

- **Printed-statement identity.** PE `docs/paper_lean_coverage.json`: one row per asserting environment, with `statement_sha256`. PE `evidence/paper_evidence.json` adds `statement_key`, page, number and statement text.
- **Line-level ties.** LE `src/lean_exposition/alignment.py`, `docs/record-alignment.md`: byte slices, exact Lean lines, `clause`, and `"lean": []` meaning "no Lean of its own". Its "what a reader may conclude" section is the wording to keep.
- **Failed checks stay.** LE `src/lean_exposition/contracts.py` and `schemas/graph.schema.json` (under `src/lean_exposition/resources/`): evidence statuses `passed/failed/unavailable/not_run`, and `kernel_checked` needs a bound build receipt.
- **Pinned reads.** LE `src/lean_exposition/web.py`, `bundle.py`: frozen edition, `manifest=` pin, 409 on mismatch.
- **Reader.** Proof Reader `tools/paper.py` (`resolve`), `tools/reading.py`: word-for-word PDF check, each quote found exactly once, lines inside their declaration, passage `role`. `web/src/map/` is the shared map.
- **Negative controls.** PE `verification/NegativeSolutions/`, `verification/comparator*-negative-mismatch.json`. `negative_is_semantic` in `scripts/write_erdos249_totient_kernel_comparator_receipt.py` requires exit 1 and the expected mismatch in the log. A crash does not pass.
- **Per-value provenance.** Atlas `curated/sources/*.json` (`atlas_source_v1`: credit, licence, `reuse`, snapshot commit), `curated/check_scope_coverage.py` (quotations checked), `ALIGNMENT.md` (`relation` kept apart from `status`), `data/works.json`.
- **Counts with denominators.** Atlas `backend/catalog.json`: value, unit, rule, universe, receipt.

## (b) Defects to avoid

| Defect | Evidence |
|---|---|
| Status masking | `claims.json` declarations still hold only `name/module/line`. My module-plus-name join: 57 of 123 joinable claims mix class or prior-art state under one `status`. |
| Unjoined registries | Coverage rows have no `claim_id`; 38 of 689 reach a claim by label. Claims use short names, so exact-name overlap with coverage (1,506 names) and `main_results` (49) is 0. Coverage pins 436f55eb, claims 2a8c1667. |
| Join script without output | `scripts/paper_claim_evidence.py` exists; `evidence/claim_evidence.json` is not committed. |
| Presence read as compilation | `build_declaration_atlas.py` is a regex scan. 133,115 of 164,639 listed declarations sit outside `compiled_modules()`. The 490 claim rows are all inside it, and one of 1,672 coverage references is not. Atlas `build_lean_claims.py` and LE `lean_index.py` are also text-only; LE at least stamps `dependency_source`. |
| Authored graph read as proof | SK graph: 131 nodes, all `unverified` or `open`; `extraction_status: not_run`; no Lean dependency edge; 252 of 266 edges are authored `supports`. |
| Our paper as the anchor | LE ties attach only to `STAGES` (long, short, expository). The manuscript is a `source` with a free-text `locator`. |
| Shared metadata as correspondence | Passage-level Compare was replaced by steps with exact slices (`site/src/compare/table.ts`). |
| Vocabulary drift | Three relation sets: `ALIGNMENT.md`, coverage `lean.status`, LE `RELATIONS`. |
| Pointer checks read as meaning | Audit sample: 135 right, 14 loose, 1 wrong of 150, all AI readers (`verification/tie-audit.json`). Bytes land either way. |
| Edition size | Static edition of 1,391 hashed files, 208 MB (local build, older branch). |

**Memory against code.** Chain of custody is stale on counts: 160 claims (103), 49 `main_results` (19), 20 with `claim_id` binding 19 claims (5/4), 126 of 126 labels resolve (87/103). Short-name joins now partly work (34 of 49), so its "don't try" is outdated, though they remain unsafe. There are more than three registries now. Masking: the finding holds; the file is `docs/semantic_corpus.json.gz` and the audit script lives in `ai_workflow` only. I did not recheck its 7/57 split. Atlas memory: 133,115 reproduces; 314 modules, against its 294. Compare memory: the path exists only at LE `origin/main`. Reader memory matches Proof Reader's `AGENTS.md`.

## (c) Canonical data model

| Entity | Stable id | Keys and fields |
|---|---|---|
| manuscript | `ms:<slug>@<version>` | source URL, licence, PDF and TeX hashes |
| statement | `st:<slug>:<tex-label>`, else `st:<slug>:p<page>-<kind><number>` | printed kind and number, byte range, `statement_sha256`, `statement_key` |
| reference | `ref:<slug>:<printed-number>` → `work:<doi or arXiv id>` | printed text; `cites` rows give statement, reference, locator, and whether the source was read |
| declaration | `lean:<fully.qualified.Name>@<commit>` | module, lines, type hash, axioms, `dependency_source`, `compiled` |
| prior-art project | `prior:<slug>` | `atlas_source_v1` fields, pinned commit |
| comparator challenge | `cmp:<entry>` | config hash, challenge and solution declarations, permitted axioms, `expect: accept|reject` |
| check run | `run:<kind>:<ci-id or receipt-hash>` | subjects, pins, tool digests, status, receipt hash |
| explanation span | `ex:<doc>:b<start>-<end>` | `text_sha256`, role, author, review state |
| tie (join row) | `tie:<statement>:<declaration>` | `relation`, `role`, lines, clause, note, author, reader, pin |

**Id rules.** Ids never change with display order. Declarations are always fully qualified. Every derived value names its pin. A changed `statement_sha256` invalidates its ties and readings, as `evidence/relations.json` does for notes.

**Join keys.** `statement_id` joins ties, cites, spans and runs. Declaration name plus commit joins ties, challenges and runs. Nothing joins on title, short name or shared metadata.

**Per-statement fields, never merged:**

- `producer_claim`: what the manuscript asserts, with its proof state
- `logical_class`: per statement, using the PE vocabulary
- `prior_art`: `not_assessed` by default, with source
- `formal_statement`: `none | unassessed | partial | exact | stronger`, from ties
- `formal_origin`: `release | ours | prior_art | none`
- `build`: `not_run | failed | built_at_pin`, from runs
- `axioms`: from extraction runs
- `comparator`: `not_applicable | pending | compared | failed`, from runs
- `negative_control`: `none | rejected_as_expected | wrong_failure`
- `fidelity_reading`: `none | ai | named_person`, with reader and pin
- `informal_proof_reading`: same scale, kept apart

`partial` never adds up to `exact`. No overall status exists, and any summary is a count over one field with its denominator.

**Authored:** `corpus/manuscripts/*/manuscript.toml`, `statements.json`, `ties.json`, `cites.json`, `prior_art/*.json`, `challenges/*.json`, `readings/*.json`, `explanations/*.md`, `plain_names.json`, `non_claims.md`.

**Generated, never hand-edited:** `generated/manuscript_index.json` (hashes, spans, rects), `generated/lean.json` (elaborated extraction), `generated/compiled.json` (Lake target closure, the only source of `compiled`), `runs/*.json` (receipts), `generated/statement_status.json`, `generated/graph.json`, `generated/coverage.json`, `generated/edition.json` (manifest).

**Gates.** Fail on a dangling id, an unresolved quote, a tie to an uncompiled declaration claiming `exact` or `stronger`, a `compared` value without a run, or a statement with no row. Ship every join's output, and test that each registry row reaches a statement.

## (d) Read API

All routes take `manifest=`, return `snapshot`, and 409 on a mismatch.

| Endpoint | Fed by |
|---|---|
| `GET /api/v1` | `generated/edition.json` |
| `GET /overview` | `generated/coverage.json`, `edition.json` |
| `GET /manuscripts`, `/manuscripts/{id}` | `manuscript.toml`, `manuscript_index.json` |
| `GET /manuscripts/{id}/reading` | `manuscript_index.json`, `ties.json` |
| `GET /statements?manuscript=&field=&value=` | `statements.json`, `statement_status.json` |
| `GET /statements/{id}` | those plus `ties.json`, `cites.json`, `readings/`, `runs/` |
| `GET /declarations/{name}` | `generated/lean.json`, `compiled.json`, `ties.json` |
| `GET /lean/modules/{name}` | `lean.json`, pinned source |
| `GET /graph?root=&family=` | `generated/graph.json`, each edge typed `extracted` or `authored` |
| `GET /references`, `/references/{id}` | `cites.json`, `manuscript_index.json` |
| `GET /prior-art`, `/prior-art/{id}` | `prior_art/*.json`, `ties.json` |
| `GET /challenges/{id}` | `challenges/*.json`, `runs/` |
| `GET /runs/{id}` | `runs/*.json`, including failed runs |
| `GET /explanations/{id}` | `explanations/*.md`, span index |
| `GET /coverage?field=` | `generated/coverage.json` |
| `GET /search?q=` | statement text and plain names first, Lean names last |

## (e) A result with no release Lean

- Every printed statement still gets a row, so the manuscript stays the reader's way in.
- `formal_statement: none`, `formal_origin: none`, `comparator: not_applicable`. `pending` is reserved for existing exact Lean awaiting replay. Absent evidence is never counted as zero failures.
- The graph comes from `\ref` extraction plus authored `supports` edges, all typed `authored`. The Lean pane gives way to the printed proof, and a statement-level note says why no Lean exists.
- Prior-art Lean enters as a tie with `formal_origin: prior_art`, pinned, reading `unassessed` until read. Comparator stays silent on statement meaning.
- Lean we write later is `formal_origin: ours`, never presented as the release's. The manuscript claim and our formal claim keep separate rows wherever scope differs.

**What breaks if inherited unchanged:**

- Proof Reader: `shards()` reads `generated/lean.json` and `config["lean"]` unconditionally, and `resolve` builds on that. Make Lean optional.
- LE: graph contracts already cope. `qaoa_thermodynamic_first` is a goal with no `formalizes` edge. `formal_result` passages become unavailable, so use `source_argument`. `STAGES` must become manifest-driven, and `full_support` hard-coded in `FrontPage.tsx` must go.
- Atlas: already models this. 130 of 372 families and 380 of 719 manuscripts have no Lean, with `lean: null` rows.
