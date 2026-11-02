# Data contract for the reader and films

## Identity and entry point

Start from the worked example's all-one column and outward pointers. Selecting either a sentence or a depicted object resolves to one or more existing statement IDs. The same ID survives movement between the one-sentence explanation, the paragraph, the page, the map, the paper route, the film and the evidence inspector. Example-specific calculations use a separate namespace until they are admitted as statements. They never inherit a checked status from a general theorem merely because that theorem motivated the example.

The source snapshot is `c7e0c9161f0ad898889bd9166e7b354acd42188d`, as recorded in the supplied `manifest.json`. Its source paper is recorded as `openai/math 4eaee875`. The SHA-256 values in that manifest match every listed file in this packet on inspection. This checks packet integrity against its own manifest; it does not authenticate an external build or prove the mathematics. [Packet: `manifest.json`; `AUDIT_FINDINGS.json`, `checks`.]

## Existing inputs

| File | Use | Boundary |
| --- | --- | --- |
| `corpus/statements.json` | Stable IDs, normalized statements, hashes, authored dependencies, declarations and separate evidence fields | No complete Lean type, exact paper quote, or run ID on each tie |
| `corpus/ties.json` | Reviewed declaration-to-statement relations, routes, hypotheses and notes | Some entries are stale or inconsistent; see audit findings |
| `corpus/lean_dependencies.json` | Recorded declaration edges and headline closure | This is not the paper dependency graph; it contains no source/export hash binding in its current top level |
| `corpus/evidence-graph.json` | Existing graph-schema projection and summarized run records | Several review strings are stale; negative-control verdicts are collapsed into harness success |
| `corpus/coverage.json` | Internal consistency checks and filtering by evidence field | Counts are not a measure of truth or reader understanding |
| `corpus/README.md` | The meaning of each evidence field | The consumer must honor those distinctions |
| `lean/QuarticQuery/Statement.lean` | Actual public vocabulary and definitions | Source inspection is not a build or semantic review |
| `lean/QuarticQuery/Results/Unconditional.lean` | Source headline type and proof references | Includes a floor-form lower bound; exact wording must stay visible |
| `lean/QuarticCorpus/*/{Challenge,Solution}.lean` and `comparator.json` | Compared names, Challenge statements, wrappers and allowed axioms | The files do not establish that a particular run took place |
| `docs/statement_fidelity_review.md` | Semantic review findings and known route differences | Earlier snapshot; no Lean was run by that reviewer |
| `docs/forrelation_lower_bound_review.md` | AI mathematical reading of the new route | Its extrapolated quantitative improvements are not Lean theorems |
| `docs/forrelation_route_prior_art.md` | Search boundaries and attribution for the route | Failure to find an antecedent is not evidence of priority |
| `paper/extracted.md` and the PDF | Paper wording, section route and visual formula verification | The extracted line number is a hint; the PDF is authoritative for damaged displays |

Paths in this table are relative to `repository/`, except the paper and packet-manifest paths. Existing field values are copied unchanged into the return. New display advisories live outside those records. `formal_origin: ours` identifies the local formalization; it is not a novelty or priority claim about the mathematics. Likewise, `external_inputs` records the preprint's cited sources and must not be converted automatically into an open hypothesis of the final Lean theorem. Read the theorem type and its discharge path.

## Five levels and their joins

| Level | Output | Main source join | Additional data required |
| --- | --- | --- | --- |
| One sentence | `levels.json` sentence object and corresponding passage in `levels.md` | `def-F`, `claim-winner-dominates`, `thm-1.1` | Exact sentence text, passage ID, worked-example reference, disclosure link |
| One paragraph | Paragraph object | Construction, the two query bounds, and `thm-1.1` | Role of each sentence; explicit total-function and asymptotic scope |
| One page | Page sections | The same endpoints plus the precise mechanism and hard steps | Ordered passage blocks, definitions-before-use, source links and new example IDs |
| Argument map | `argument_map.json` | `statements.json[id]`, its `depends_on`, and `ties.json[id]` | Plain labels, one-line edge reasons, collapsed-path IDs, hard-step explanations and route advisories |
| Paper route | Ordered route object | Each row's `section` and `source_line`, plus verified paper headings | Reading purpose, exact section/page anchors, optional prerequisites and return links |

The pedagogical reading order begins with the four-column example and previews the theorem. It can differ from a topological order of mathematical dependencies. A consumer must never interpret the reading order as a proof-order claim.

## Two distinct graph relationships

`argument_map.json` contains only existing corpus IDs as node identities. Each node retains its exact supplied `evidence` object. Each `supports` edge runs from prerequisite to consequence. `source_dependency_path` records a path in the supplied authored dependencies, and `via` gives the hidden internal IDs when a path has been collapsed. Every adjacent pair in each path has been checked against the original `depends_on` arrays. These are explanation dependencies, not extracted Lean proof dependencies.

For the declaration view, load `lean_dependencies.json.edges` separately. Its roots are `QuarticQuery.theorem_1_1_unconditional` and `QuarticQuery.cubic_bound_fails_unconditional`. Display membership in their closure on a particular declaration. Do not set every statement tied to a reached declaration to “exact,” and do not assign a paper node the status of its strongest downstream theorem. [Packet: `repository/corpus/lean_dependencies.json`; `AUDIT_FINDINGS.json`, AUDIT-08.]

A candidate source correspondence may be useful even when no reviewed tie exists. It is rendered as a candidate with its source link. It changes no corpus evidence field. `AUDIT-10` lists examples that already have relevant Lean code.

## Passage and shot identities

Every passage has a stable anchor `<!-- passage:NAME -->`. `correspondence.json` identifies its exact first and last words, role, source statement IDs and declaration names. Add optional `new_statement_ids`, `source_refs` and `evidence_note` fields when a passage includes new explanatory calculations, factual provenance or a disputed tie. The required fields retain the requested schema.

Each film shot needs:

- a stable shot ID, exact start and end seconds, and spoken text;
- a concrete picture specification with exact values, ordering and labels;
- existing `statement_ids` and separate `new_statement_ids`;
- sources for historical or verification claims;
- the evidence wording to use if the picture displays a checked claim;
- a pause allowance and spoken-word count.

The shot specification describes a picture. It does not claim an animation, a simulation, or a theorem has been built. The four-column example uses exact data in a single shared source object, so the column order, pointer positions and address bits cannot drift between levels and films. The production team can substitute a new example only by changing that object and rerunning its calculations and correspondence checks.

## Missing producer fields

The requested interface needs the following additions. These are proposed schema changes, not fabricated records:

| Proposed field | Purpose |
| --- | --- |
| `source_snapshot` | Full repository commit, dependency revisions, toolchain, paper revision and hashes |
| `source_location` | An authorized immutable source URL or bundled source path; no public URL is assumed for the private repository |
| `paper_excerpt` | Exact quoted sentence/display, preceding hypotheses, PDF page and bounding box, extraction span and source hash |
| `ledger_statement` | Existing normalized statement and its version history, distinct from the paper excerpt |
| `lean_type` | Fully qualified declaration name, elaborated full type, universes/implicit binders, export tool/version, source hash and export hash |
| `lean_source_excerpt` | Exact unelaborated signature plus the namespace and relevant section variables; available as a clearly labeled fallback |
| `definition_closure` | All nonlogical definitions in the theorem type, their hashes, and a way to expand them in dependency order |
| `reviewed_tie_id` | Stable identity for one statement/declaration relation, with reviewer kind, reviewed pin and clause-level scope |
| `hypothesis_discharge` | The binder, whether it is an ordinary hypothesis or an open premise, and the declaration discharging it on the headline path |
| `run_ref` | Original receipt identity, environment, command, source/export hashes and raw log hash |
| `comparator_result` | Actual accept/reject verdict and exit code; separate from a test harness's success |
| `negative_control_result` | Mutated artifact, expected diagnostic, observed diagnostic and whether rejection occurred for the intended reason |
| `declaration_map` | Explicit mapping from `QuarticQuery.Checked.*` wrapper to implementation declaration and Challenge declaration |
| `reachability_run_ref` | Run identity and compiled-environment hash for the dependency extraction |
| `semantic_review` | Review scope, definition checks, reviewer relationship to proof author, date, reviewed pin, findings and resolutions |
| `human_review_status` | Explicit reported state; absence of a person is not encoded as absence of all reviews |
| `display_advisories` | Separate warnings or disputed mappings without mutating the supplied raw record |
| `presentation` | Plain labels, diagram placement, stable example identity, reading-order rationale, film timing and accessibility text |

Store exact schema values independently from friendly text. For example, `conditional: true` may reflect explicit assumptions in a helper theorem, while the final theorem discharges them. The presentation should show the actual relevant hypothesis. A blanket “conditional result” badge on the whole project would be false. Conversely, an empty array of recorded hypotheses must not erase a visible binder, as it currently would for the legacy `theorem_1_1`. [AUDIT-03.]

## Comparator records and the snapshot boundary

The packet contains source/configuration files and graph summaries of local runs. The raw `corpus/receipts/` files are absent. The attached trace reports the unconditional paranoid run with receipt commit `d42fb67a7e060fb5386867dadf20a5903df39141`; the packet was then built at `c7e0c9161f0ad898889bd9166e7b354acd42188d`. The trace records a subsequent README/corpus update, which suggests the proof source was unchanged, but this advisory has not verified a Git diff or a compiled export across those pins. Keep the two identifiers separate. [Attached trace, O191–O193, local lines 8131–8172; `AUDIT_FINDINGS.json`, AUDIT-07.]

The negative controls use an intentionally successful harness outcome for an expected rejection. The full result must say “rejected as expected,” with the diagnostic. `status: passed` alone is insufficient. Challenge files may contain `sorry` placeholders specifying goals; the production Solution proof must satisfy the configured axiom policy. A blanket source grep across Challenge fixtures would mix roles and give a false result. [Packet: `repository/lean/QuarticCorpus/Unconditional/{Challenge,Solution}.lean`; attached trace, runner logic at local lines 972–1035.]

## Consumer behavior on incomplete or conflicting data

Preserve raw evidence and display an advisory alongside it. An unresolvable declaration opens a source-search result labeled unresolved, not a different nearby theorem. An absent receipt says “reported result; receipt unavailable in this packet.” A stale review remains readable at its original pin. A statement with no reviewed tie says exactly that. A disputed exact tie is prevented from generating a checked badge until resolved.

For `claim-bs-to-L`, the displayed arithmetic comparison remains a paper-step node. Its existing tie points to a theorem of `L<R(P)`, which supplies the endpoint by another proof. The active Lean route bypasses that comparison. The advisory must not rewrite the intermediate statement into the endpoint merely to make the evidence appear exact. No mathematical statement is changed in this design. [AUDIT-01.]

## Release checks for the assembled reader

Check identity and navigation rather than writing tests that mirror styling. Confirm that every displayed mathematical passage resolves to an existing or proposed statement; each declaration link resolves to the intended name and source hash; every copied evidence object is unchanged; every collapsed edge has a valid dependency path; every film shot uses the same example data; and each reported test result is interpreted according to its actual role. Review the high-impact semantic questions beside the definitions and the disputed correspondence before publishing.

A complete product can be released with visible gaps if its wording is accurate. Missing metadata should not be hidden behind a project-wide score, and unrelated unresolved mappings should not obscure the strongest result the snapshot actually reports.


## Concrete assets supplied with this design

`film_shots.json` stores both films under `films.film12` and `films.film4`. Each shot has `start_seconds`, `end_seconds`, `duration_seconds`, `spoken`, `picture`, `statement_ids`, `new_statement_ids`, `spoken_words` and `continuous_wpm`. Its spoken anchor is the shot ID; the picture anchor appends `_picture`. Planned duration is not a measured narration rate.

`visual_data.json` is the single source for the finite example. The `worked_example.svg` and PNG depict those values and carry no simulated execution data. `checking_visual_data.json` stores exact supplied source snippets, their source hashes and line spans, the unconditional Comparator configuration and the actual negative modules. These fields supply source text, not an elaborated type export or a new checker result.

`LEAN_GAPS.json` gives the affected displayed rows in reading order. `NEW_STATEMENTS.json` includes a shared `proposed_lean_context` and an explicit `formal_status`. `correspondence.json` records exact text boundaries and a body hash for each mathematical prose or picture passage. The check script validates these joins against the original packet.
