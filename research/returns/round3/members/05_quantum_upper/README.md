# Quantum upper bound: proposed replacement for §5

This return reconstructs the complete ordinary proof of OpenAI’s quantum upper bound and corrects its description of the supplied formal evidence. For every fixed integer $k\geq2$, the construction gives

$$
Q(F_{k,4^t})\leq C_k\,2^t(2t)^6\qquad(t\geq1),
$$

with one fixed query cap on every input and every execution branch. The proof covers bounded amplification, a probabilistic tournament with no ordering assumption on the losing candidates, noisy address decoding, complementary comparisons, and exact local verification. An exact four-candidate example makes the cyclic comparisons and conditional sampling probabilities explicit.

The current packet supplies a genuine bounded-list tournament theorem. The remaining formal gap is more specific: its successful-label amplification interfaces do not yet identify a designated physical output register with the original normalized successful quantum state. The ordinary state-preserving construction is explained, and the exact missing formal specification is isolated. The measured-label route already suffices for the stated query upper bound.

This is an **advisory section return**, prepared for integration and further checking. It preserves the preprint’s mathematical attribution and does not claim a new separation theorem, acceptance by the integrating team, or a final integrated paper. The fixed-$k$ statement above is the scope of this section.

## Reading order

1. **`section.md`** — the self-contained replacement for long-record §5. Its opening identifies the neighboring definitions and results it expects. Stable passage anchors locate the proof and correspondence records. Sections 5.1–5.4 carry the mathematics; §5.5 separates formal interfaces and evidence.
2. **`LEAN_GAPS.md`** — exact remaining clauses, differences between proof routes, and the limits of build and Comparator evidence. Read this alongside §5.5 before interpreting the formal claims.
3. **`correspondence.json`** and **`declaration_types.json`** — passage boundaries, roles, statement identifiers, exact declaration names and available types, premises, routes, and evidence dimensions. A source declaration, a successful build, a statement comparison, and intended mathematical meaning are recorded separately.
4. **`NEW_STATEMENTS.json`**, **`STATEMENT_CHANGES.json`**, **`statement_catalogue.json`**, and **`EVIDENCE_CORRECTIONS.json`** — the proposed statements, canonical-statement change record, referenced statement records, and corrections to earlier evidence descriptions. Proposed interfaces are not presented as checked Lean declarations.
5. **`references.bib`** and **`source_read_receipt.json`** — mathematical sources with the inspected editions and locators, source versions, and honest assessed, sampled, unavailable, or unassessed coverage. Historical sources have explicit roles; the source preprint remains the target and attribution source.
6. **`review_notes.md`** and **`STYLE_RULES.json`** — located findings, the authoring receipt, scope of the final review, and the specific writing moves taken from the supplied exemplars. The exemplars supply style guidance, not mathematical evidence.
7. **`checks/`** and the return’s byte manifest — reproducible finite calculations, the input-integrity and supplied-evidence audit records, and structural/hash validation. Their limited claims are described below.

## Reproduce the included checks

Run the following commands **from the root of the unpacked return** with Python 3. The scripts use the Python standard library and require no Lean installation.

```bash
python3 checks/tournament_example.py
python3 checks/state_example.py
python3 checks/validate_return.py
```

The first two scripts regenerate their sibling JSON reports, `checks/tournament_example.json` and `checks/state_example.json`. They use exact arithmetic. The tournament script checks the displayed cyclic example, its weights and conditional probabilities, normalization and drift along its finite histories, and an explicitly artificial admissible failure law. That artificial law is an illustration; it is not asserted to be the actual physical amplifier’s law. The state script checks the small example showing that a computational-basis label distribution does not determine a retained quantum state.

`checks/validate_return.py` performs read-only structural and hash validation and prints its JSON result. It checks the assembled return’s recorded consistency; it does not prove the mathematics or execute Lean. If a file is intentionally edited, its recorded hash should no longer be expected to match the original manifest. The arithmetic scripts are deterministic, so regeneration without source changes should preserve their recorded output bytes.

The JSON files under `checks/` record the runs and source comparisons performed while preparing this return. Input-integrity checks establish correspondence with the supplied bytes. The Lean-evidence audit examines the supplied source-bound receipts and their exact scope. Neither is a fresh proof execution.

## Evidence and review limits

**No fresh Lean build, declaration elaboration, or Comparator run was performed for this return.** Its formal-evidence conclusions concern the supplied receipts and the exact source bytes compared with them. No proposed physical retained-state bridge has been compiled or promoted to a checked result. Detailed source versions, hash relations, declaration coverage, and any rendering limits are recorded in the companion files.

The finite checks support their displayed examples and arithmetic only. They do not replace the symbolic tournament proof, establish the full addressed-certificate construction by enumeration, simulate the complete quantum algorithm, or certify a universal theorem. The complete ordinary argument is in `section.md`; the correspondence and gap records state how far the supplied formal results implement it.
