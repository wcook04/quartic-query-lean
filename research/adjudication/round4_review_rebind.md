# Round-four review rebind

Round four added Lean modules without changing any reviewed declaration. Review
bindings hash the complete local Lean snapshot, so the additions made all 162
bound ties in [`corpus/ties.json`](../../corpus/ties.json) `stale` and left every
statement `unassessed`. This record checks the one question a rebind may answer:
did round four change the meaning of a reviewed declaration? It did not. The
[machine-readable record](round4_review_rebind.json) holds the full path lists.

**Scope.** This rebind certifies that round-four additions did not alter
reviewed declarations, statement rows or tie judgments. It is not a new
semantic review of the statements. Each relation, route, premise
classification and note keeps the authority of its original review.

## Changed paths (working tree against `752826a`)

| Path | Class | Effect on review |
| --- | --- | --- |
| `lean/QuarticQuery.lean` | modified | 11 appended `public import` lines; the file holds only `module` and imports |
| `lean/README.md` | modified | prose section added; not a snapshot input |
| 62 `.lean` and 10 `.json` files under `lean/` | new | listed in the JSON record |
| `lean-toolchain`, `lakefile.toml`, `lake-manifest.json` | unchanged | none |

No file was removed. The other 151 snapshot entries present at HEAD are
byte-identical. The old snapshot was computed from `git archive HEAD lean`
outside the checkout and equals the value recorded in every binding, so each
binding was current at HEAD.

## Import closure

A Lean declaration elaborates only from its own module and that module's
transitive imports. All 133 pre-existing modules except the root are
byte-identical to HEAD, and their imports name only pre-existing modules or the
external packages `Mathlib`, `Complexity` and `Lean`. The root
`lean/QuarticQuery.lean` aggregates imports, declares nothing, and is imported by
no module. The 62 new modules therefore lie outside the import closure of every
pre-existing module: their declarations, instances, attributes, simp sets and
notation cannot reach a reviewed declaration. New module names come from new
paths, so none shadows an existing module. One new definition shares a short name
with a reviewed declaration: `QuarticQuery.ForrelationLower.RealQueryTree.weight`
against `QuarticQuery.Tournament.weight`. Their fully qualified names differ.

## Tie checks

For each of the 162 bound ties (121 statements):

1. the stored binding equals `expected_review_binding` over the HEAD snapshot;
2. `statement_sha256`, `row_sha256`, `declaration` and `judgment_sha256` equal
   `expected_review_binding` over the current snapshot;
3. the declaration's file exists at HEAD and is byte-identical now. 131 ties
   name their `file`; the other 31 were located by definition search in the HEAD
   tree.

All 162 passed and none stays stale. Only
`review_binding.source_snapshot_sha256` changed. The 327 ties without a binding
were not touched.

| Snapshot | SHA-256 | Entries |
| --- | --- | ---: |
| old (HEAD) | `43f007e0916f14d513d076e8036b9bb05aa29897b5b9eb7bc4a8d6551d63c2b3` | 152 |
| new | `0d109ea9e9b7f4a766640d406409e30589fb4c5a4e645b6d6888569fa2edf29f` | 224 |

The new value equals the frozen source inventory of the
[round-four formal integration](round4_formal.md).

## Command

Run from the repository root:

```sh
python3 - <<'PY'
import sys, json, re
sys.path.insert(0, "tools")
import build_corpus as bc
path = bc.CORPUS / "ties.json"
OLD = "43f007e0916f14d513d076e8036b9bb05aa29897b5b9eb7bc4a8d6551d63c2b3"
new = bc.canonical_sha256(bc.source_hashes())
text = path.read_text(encoding="utf-8")
key = '"source_snapshot_sha256": "'
assert text.count(key + OLD + '"') == text.count(OLD) == 162
path.write_text(text.replace(key + OLD + '"', key + new + '"'), encoding="utf-8")
before = json.loads(text); after = json.loads(path.read_text(encoding="utf-8"))
ledger, hashes = bc.rows(), bc.source_hashes()
for k in before:
    for b, a in zip(before[k], after[k], strict=True):
        if "review_binding" in b:
            b = {**b, "review_binding": {**b["review_binding"], "source_snapshot_sha256": new}}
            assert bc.review_currentness(k, ledger[k], a, hashes) == "current"
        assert a == b
PY
python3 tools/build_corpus.py
python3 tools/build_comparator_map.py
```

## Coverage

| Field | HEAD | Before rebind | After rebind |
| --- | --- | --- | --- |
| review | current 121 | stale 121 | current 121 |
| formal statement | exact 51, stronger 31, partial 39 | unassessed 121 | exact 51, stronger 31, partial 39 |
| route | same 54, alternative 9, none 58 | none 121 | same 54, alternative 9, none 58 |
| build | built 121 | built 121 | built 121 |
| comparator | compared 4, wrapper 8, not run 109 | not run 121 | not run 121 |
| reach | reached 65, outside 56 | reached 65, outside 56 | reached 65, outside 56 |

Comparator credit is a receipt fact, independent of review. The receipts that
named tie declarations are bound to the HEAD snapshot and are now stale; the
current 2026-11-03 corpus receipts configure no tie declaration directly.
Restoring that credit needs fresh Comparator runs, which a review rebind cannot
supply.
