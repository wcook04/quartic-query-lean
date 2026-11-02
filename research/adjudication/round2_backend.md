# Round-two evidence backend

This adjudication repairs evidence freshness and dependency extraction. It does
not adjudicate the mathematics or establish a new successful Lean build.

## Observed defects

1. `record_evidence.py` previously imported the existing compiled `QuarticQuery`
   environment and labelled that inspection `lean_build: passed`. It neither
   rebuilt current source nor recorded the source bytes. The retained
   `lean-build-root.json` therefore records a historical environment inspection,
   not evidence that the present working tree compiles.
2. `build_corpus.py` previously pooled declaration names from every historical
   passed receipt. A later source edit could inherit a current-looking build or
   comparison flag without a new check. The recorded dependency closure had the
   same freshness problem.
3. `Reach.lean` previously descended only through public `QuarticQuery`
   declarations and internal names with that prefix. Lean's private names begin
   with `_private`, so a public root could depend on a public leaf through a
   private wrapper while the leaf was absent from the public closure. The
   statement-fidelity return supplies a concrete fixture for this case.

## Implemented behavior

- The recorder first runs `lake build QuarticQuery`, then inspects that compiled
  environment. It records nothing if either operation fails, input hashes move
  during the operations, a requested root is absent, or extraction reports an
  unresolved constant. Its receipt records the build and inspection commands
  separately.
- New build and Comparator receipts bind the complete local Lean source and
  configuration snapshot through SHA-256 hashes. Source edits, additions,
  removals, comparator configuration changes, toolchain changes and dependency
  manifest changes invalidate that binding. Snapshot collection excludes Lake
  dependencies and build caches. The scope is conservative: an unrelated local
  Lean module change also requires fresh evidence.
- Receipts are appended under timestamped names. Existing historical receipt
  files remain untouched. Each graph receipt retains its historical status,
  commit and time inside `receipt.operation`, with separate
  `receipt.currentness`: `current`, `stale`, or
  `legacy_unbound`. A legacy receipt without source hashes remains readable but
  cannot supply a current build or comparison flag.
- Each statement tie now exposes `build_evidence` and `comparison_evidence` as
  well as the compatible boolean fields. A checked statement still requires a
  reviewed `exact` or `stronger` tie and current build and Comparator receipts
  naming that same declaration in the corpus. Evidence for separate
  declarations cannot be combined. A stale or unbound closure supplies no
  current reach membership.
- Dependency extraction first walks every reachable available constant's type
  and body, in every namespace, once. It then projects through hidden parents to
  public `QuarticQuery` edges. Reverse projection avoids repeatedly scanning the
  common Mathlib closure for each public declaration. Existing `roots`,
  `declared`, `reached`, and `edges` keys remain; `hidden_paths` preserves one
  actual hidden-name witness per projected edge, `unresolved_constants` reports
  missing constants, and `traversed_constants` records the full traversal size.
  Witnesses do not enumerate every path. Displayed edges are this public
  projection, rather than direct raw constant references.

## Validation and integration boundary

- Focused corpus suite: 15 tests passed, including changed-source rejection,
  legacy evidence visibility, exact declaration matching, separate ties, stale
  reach, source additions/removals, and cache/configuration scope.
- Producer suite: 7 Python tests passed; 1 optional Lean fixture skipped in
  ordinary discovery. It checks build-before-inspection, failed-build refusal,
  changed-input refusal, unresolved/missing roots, comparison invalidation, and
  preservation of historical receipt files. Host-guard exit 75 writes no
  Comparator receipt, for either positive or negative checks.
- `make check-tests`: 91 tests completed with the optional Lean fixture skipped.
  The final additional exit-75 Comparator regression also passed in the focused
  producer suite (8 tests completed, one optional Lean fixture skipped).
- `python3 tools/check_repository.py`: passed at this work boundary.
- The optional Lean-only fixture adapts the preserved round-two private-wrapper
  fixture and additionally tests an intermediary in another namespace. It
  elaborates the actual implementation without building/importing the proof
  library. Run it with
  `QUARTIC_TEST_LEAN=1 python3 -m unittest discover -s tests -p 'test_record_evidence.py'`.
  The attempted native compile was deferred by the shared host guard (exit 75);
  it was not a Lean elaboration failure. Its temporary input was removed by the
  initial test cleanup, so cancellation of that exact obsolete future
  `cf_38b84de5309442899fda` was requested through the owning API. The regression
  now retains its input on deferral and reports a skipped validation. The
  That initial attempt did not elaborate the revised traversal. The later
  successful native regression is recorded in the closeout below; the full
  environment export remains a separate gate.
  A durable copy of the complete script plus regression is prepared at
  `/tmp/quartic-query-reach-backend/ReachRegression.lean`; after the shared build
  releases, run from `lean/`:
  `~/.elan/bin/lean /tmp/quartic-query-reach-backend/ReachRegression.lean`.
  This command compiles the complete script and fixture without executing
  `main`, importing `QuarticQuery`, or building the proof library.

No live receipts, generated corpus files, or historical review returns were
rewritten in this backend work. No full Lean build, corpus regeneration, or
commit was made. The batch integrator owns those operations after source freeze.
Until fresh bound runs exist, historical successful receipts are deliberately
`legacy_unbound`, and current corpus checks will fall rather than inherit them.

This is source-bound evidence from a local run. It does not establish a clean
clone reproduction: dependency manifest revisions are bound, but dependency
checkout bytes and tool executable bytes are not hashed. The source snapshots
also assume inputs are held still between the two boundary observations; a
change-and-revert during execution is not detected by before/after hashing.

The reusable lesson belongs in the evidence producers and their regressions:
importing an artifact and checking current source are separate operations, and
historical success must have an explicit freshness boundary. No new subsystem or
parallel evidence registry was introduced.

## Reviewed premises and open assumptions

The follow-up backend change supports two optional lists of strings on reviewed
ties: `premises`, for ordinary hypotheses already belonging to the matched
statement, and `open_assumptions`, for additional assumptions the selected
theorem has not discharged. Both are reviewer classifications; the corpus tool
does not infer them from Lean syntax or the availability of a standalone proof.

The original authored `hypotheses` list is preserved on each corpus tie. When
`open_assumptions` is absent, that list remains the effective open-assumption
list, retaining previous behavior. Supplying `premises` alone does not erase
legacy assumptions: a reviewer must explicitly supply `open_assumptions: []`
when the theorem has no additional open assumptions. No input ties were edited
or globally relabelled by this backend change.

Best-tie preference and the existing `conditional` field now use effective
`open_assumptions`, rather than treating every ordinary premise as an unproved
assumption. Selected corpus evidence exposes the declaration through
`assumption_declaration`, together with its `premises` and `open_assumptions`.
The graph carries this machine-readable metadata in an attached semantic-review
`receipt`, with its ordinary `declaration` and `boundary` fields supplying the
human-readable pointer. Selected metadata is omitted when no current built tie
is selected. Absence means unknown selection; it does not assert an empty
assumption list. All reviewed details remain available on individual corpus
ties. No metadata is assembled across different declarations.

The focused corpus suite has 21 Python tests and an additional opt-in installed
consumer integration regression. Added regressions cover an exact
theorem with ordinary premises and an explicitly empty open-assumption list, an
exact theorem with open hardness, unchanged legacy fallback, explicit assumption
classification in tie preference, malformed-field rejection, and omission of
unknown selected metadata. These use bound mocked receipts to exercise the
corpus semantics; they do not check the mathematical classification of a tie.

Compatibility review found that the installed `lean-exposition` graph schema
forbids additional node/evidence keys. The builder uses its existing `receipt`
object and node `boundary`/`declaration` fields. Adding direct
`premises`/`open_assumptions` node keys or direct `currentness` evidence keys
would violate the declared schema and is not done.

The real external contract reserves `kernel_checked` for formal declaration
nodes with matching build/extraction receipts and identified source bytes.
This graph is an informal statement/goal projection, so its claim/goal nodes
remain `unverified`, and imported assumptions remain `external`. Local build and
Comparator successes remain true in corpus records and nested metadata; the
graph does not present them as native verification/extraction receipts or
independent semantic review. Every node has an explicit boundary. Metadata
receipts attach to matching statement nodes and survive selection.

The external source-to-graph skill and `docs/contracts.md` require authored
support edges to run from consumer to prerequisite. The builder previously
reversed them, preventing a goal closure from recovering its ingredients.
That direction is repaired. The installed-consumer regression validates a
synthetic graph with current positive local build/comparison evidence, selects
a goal with a two-level prerequisite chain, and inspects that chain through the
actual CLI. Selection preserves the full recorded corpus; the argument view
excludes unrelated nodes. Attached operation/assumption metadata remains
available. Enable this test with
`QUARTIC_LEAN_EXPOSITION=/path/to/lean-exposition`; ordinary discovery names
that external prerequisite explicitly and skips the integration test.

Both a synthetic current-positive graph and the current source-generated graph
passed the installed `validate_schema` and full `contracts.validate_graph`
without writing generated output. No formal declaration nodes, extraction
results, source identities, or proof receipts were invented.

With the installed CLI enabled, all 22 focused corpus tests passed, including
the real selection/inspection journey. The read-only source-generated graph had
121 nodes at this check. `python3 tools/check_repository.py`, Python compilation,
and the scoped whitespace check also passed after these changes.
The full Python suite with that integration enabled completed 99 tests with
only the optional native Lean fixture skipped.

The consumer-boundary defect was captured in the ai_workflow Task Ledger as
`cap_quick_quartic_corpus_informal_graph_must_prese_cd2ad6d663ab`, event
`wie_20261102T162211Z_3dc9dfe1`; its visibility receipt reports
`authority_event_visible=true` and `capture_claimable=true`.

## Backend closeout and packet reuse

The sole native build coordinator subsequently ran the complete current exporter
plus regression under the governed SSD inventory. Its recorded result is
`ReachRegression`, `status: passed`, `exit_code: 0`, `seconds: 15.07`, command
`lake env lean /tmp/quartic-query-reach-backend/ReachRegression.lean`.
The result was read directly from
`/Users/willcook/src/_builds/quartic-r2-ssd/native-inventory/results.json`;
`ReachRegression.log` is empty. The runner verified the complete exporter is
the fixture's exact byte prefix and recorded `inputs_unchanged: true`:

- Exporter SHA-256:
  `44ce6c1ace1e3914109b959c5d3466f00eba4090621d73d3b3ee2626be1f796b`.
- Fixture SHA-256:
  `3be41c8f056cb06feba16325ca6204d04d3935a8f41105815105a040c2b4a002`.

This compiles the whole script without executing `main`. Both a private wrapper
and a wrapper in another namespace preserve the public leaf, the projected
root-to-leaf edge, and a nonempty hidden-path witness; both traversals have no
unresolved names. A deliberately missing root appears in `unresolved`. All
assertions passed. This completes the native exporter-regression gate, not a
fresh full-library build or a full compiled-environment dependency export.
The backend agent issued no competing Lean call and left Lean sources frozen
during the coordinator's inventory.

The existing round-two builder also needed a bounded provenance correction for
reuse. Its record skeleton now calls the input a recorded dependency export,
computes `currentness` through the shared backend helper, and treats stale or
legacy membership as historical. A name absent from such an export no longer
gets described as outside the current headline closure. Its adjacent build
status page explicitly identifies the fixed named historical receipt and
describes `.olean` existence/mtime as artifact observations, not evidence that
present bytes compiled. It does not select or relabel newer receipts. Three
new temporary-fixture tests cover legacy/stale/current export wording and a
newer artifact whose timestamp cannot bind it to the source. All six focused
round-two tests passed. No new packet builder or sent archive was created or
rewritten by this correction.
The full Python suite with the installed-consumer integration enabled then
completed 102 tests with the optional native fixture skipped in ordinary
discovery; that fixture has the separate successful governed result above.
Layout, scoped whitespace and Python compilation checks passed.

Remaining native integration gates belong to the coordinator after source
freeze: finish the affected-module/full-root build; run the real recorder to
obtain a source-bound complete environment export; run the intended Comparator
bundles against the same source snapshot; regenerate the corpus and run the
normal repository/consumer checks. The passing tiny fixture supplies no credit
for those operations, and the backend changes do not upgrade historical
receipts.

The environment scope is explicit: `Reach.lean` imports `QuarticQuery`, whose
current root import file does not import the new `Paper` wrappers. A successful
standalone module inventory therefore cannot make those wrapper declarations
appear in this root environment export. Their integration needs intentional
root imports after native validation, or separately scoped genuine module
receipts; this closeout makes neither change during the frozen build. An absent
declaration correctly receives no root-environment build credit meanwhile.

The exact backend-owned pathset for the coordinator's scoped commit is:

- `tools/build_corpus.py`
- `tools/record_evidence.py`
- `tools/run_comparator.py`
- `tools/build_round2_packets.py`
- `lean/scripts/Reach.lean`
- `tests/test_build_corpus.py`
- `tests/test_record_evidence.py` (new, explicitly add it)
- `tests/test_build_round2_packets.py`
- `research/adjudication/round2_backend.md`

Root-owned guide, reviewed tie, generated corpus, proof-module and packet-builder
changes are outside this backend attribution list. No shared-tree commit was
made by the backend agent.
