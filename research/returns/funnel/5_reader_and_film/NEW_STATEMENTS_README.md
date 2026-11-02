# Proposed finite statements

Every entry in `NEW_STATEMENTS.json` is an uncompiled proposal for the worked example. The signatures use the supplied public vocabulary and existing declarations; they introduce no new separation theorem. Their shared context is:

```lean
import QuarticQuery
open QuarticQuery
open scoped BigOperators
```

The `proposed_lean` strings are signatures, without `:=` or proof bodies. They have been checked against the source vocabulary by inspection, but have not been elaborated. The exact integer and rational calculations reproduced by `checks/check_return.py` are independent finite consistency checks. They are not Lean evidence for these proposed declarations.

The example fixes `C = QuarticQuery.Forrelation.forrCircuit 1 1`; the first argument is one less than `k`. Its transcripts are exactly `circuitEval C (A i h)`. The numerical gate count and transcript bit strings are not materialized. The three visible pointer targets are decoded row labels; their stored bits are defined by `pointerEquiv 2` inverse images, so the design assumes no unchecked endianness.

The unchanged corpus remains the authority for earlier statements. `STATEMENT_CHANGES.json` is empty because this return proposes no change to a mathematical statement in that corpus. Disputed correspondence metadata is recorded separately in `AUDIT_FINDINGS.json`.
