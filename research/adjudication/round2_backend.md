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
  revised traversal has not yet been elaborated or run on the full environment.
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
