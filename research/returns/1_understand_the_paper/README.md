# Nearly quartic query separation: explanation and audit

## Start here

Read **understanding.md** for the complete explanation, then **worked_examples.md** for the exact four-column example. Use **statement_review.json** to follow any of the original 118 ledger IDs. The more technical derivations are in **proof_audit.md**.

This is the requested advisory return for the supplied `quartic_1_understand_the_paper.zip`, together with a contextual review of `Pasted text(20261101-233050).txt`. It does not modify the source corpus or continue the historical trace's computer operations.

## Main assessment

The manual audit found **no fatal mathematical gap in the supplied manuscript**. In particular, the argument tolerates unpromised inputs in the quantum tournament, preserves the exact weighted sampling distribution, and handles adaptation in the planted-input lower bound without conditioning on an easy subset of the hard distribution.

The ledger review contains **116 correct entries and 2 corrected entries**, with every original ID present exactly once:

- **`lem-2.2.i`:** A pointer test is computable with `ell + 1` adaptive queries. It can nevertheless depend on all `m + ell` pointer and target coordinates. The ledger's fixed-small-support interpretation needs correction; the paper's query bound is correct.
- **`def-deg`:** Define Boolean degree to be zero for all constants, including the identically zero function, before asserting invariance under bit/sign encoding. This is a formal convention repair.

The **25 audit findings** include supported proof steps, formalisation obligations, corrections, and evidence limits. They are not 25 alleged mathematical errors. The high-severity finding concerns a possible overstatement of unconditional formal verification when an external theorem remains a hypothesis.

The theorem proves a separation exponent **4 - 2/k for each fixed k**, with logarithmic losses. Choosing a fixed k for each proposed smaller exponent makes the optimal universal exponent four. It does not exhibit an exact fourth-power family.

## Files

| File | Purpose |
|---|---|
| `understanding.md` | First-principles account of the construction, both bounds, Appendix A, novelty, and formalisation plan. |
| `statement_review.json` | All 118 original IDs, in original order, with the requested seven fields. |
| `audit_findings.json` | 25 observations, each with evidence, reasoning, and a concrete confirmation or falsification route. |
| `worked_examples.md` | Exact Forrelation inputs, outward pointers, cyclic and fractional tournaments, amplification, and adaptive conditioning. |
| `further_reading.json` | 19 primary reading recommendations with theorem/section guidance and relevant ledger IDs. |
| `proof_audit.md` | Full quantum, classical, appendix, and literature-comparison derivations. |
| `trace_context_review.md` | What the historical trace actually establishes, including the final failed setup/build attempt. |
| `read_coverage.json` | Exact reading scope for the manuscript, packet, trace, and all 23 supplied reference PDFs; four unavailable originals identified. |
| `verify_examples.py` | Standard-library-only exact arithmetic and finite enumeration checks. |
| `exact_example_results.json` | Reproducible output of those checks. |
| `source_manifest.json` | SHA-256 identities of the source attachments and the 30 verified manifest members. |

## Verification and limits

All 30 manifest members matched their declared byte sizes and SHA-256 hashes. The main manuscript was read in full. Dependency theorems were consulted in their original sources with the individual scopes recorded in `read_coverage.json`.

The exact checker enumerates all **256** order-two, dimension-four Forrelation inputs and all relevant finite tournament histories. It verifies the example where breaking a pointer destroys the true winner while leaving its comparison victories unchanged. It also checks the amplification ratios and the adaptive-conditioning counterexample.

From this directory, run:

```bash
python3 verify_examples.py --output exact_example_results.json
```

These finite checks do not prove the asymptotic theorem or instantiate the manuscript's circuit gate by gate. The Bansal–Sinha lower-bound interface was checked against its original statement; its complete Gaussian/Fourier proof was not independently reproved.

**No new Lean or Comparator run was performed.** The attached trace's last build notification reports failure during setup/cache work, with no successful theorem-compilation receipt. It does not establish a theorem-level Lean error. The supplied `Drift.lean` is an algebraic helper, not a model of the full tournament or separation. A later theorem with an explicit `BansalSinha` hypothesis remains conditional until that hypothesis is formally discharged.

## Citation and version conventions

All manuscript line references count **physical LF-delimited lines**, as the original ledger does. Use `text.split("\\n")`, not `text.splitlines()`: the extracted paper contains 19 form-feed page separators. The ledger's original line anchors are accurate under its convention.

References to `paper/...`, `corpus/...`, `literature/...`, or `lean/...` identify files in the **original input packet**. The source PDFs are not duplicated in this return. Their identities are preserved in `source_manifest.json`. Manuscript reference numbers are retained, while public primary-source links are collected in `further_reading.json`.

The trace review is a bounded structural and contextual reading, not a claim to have semantically reread every repeated tool transcript. Its line locators also count physical LF separators. Historical summaries, missing outputs, and proposed theorem signatures are not treated as successful verification receipts.

