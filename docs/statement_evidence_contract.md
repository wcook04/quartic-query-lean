# How statements, proofs and Lean stay in step

Lean work and written mathematics drift apart in a familiar way. A proof is
checked, a cleaner derivation is found while writing, and the published argument
no longer matches what was checked, while the checked proof sits unused. This
contract keeps the two aligned without freezing the mathematics early.

## The unit of agreement is a statement

A corpus statement is a displayed mathematical claim with a stable identifier and
a hash of its exact text. Lean is bound to statements, not to proof prose.
Comparator already works at this level: it fixes a theorem's type and everything
that type depends on, and lets the proof change. So:

1. **A proof may be replaced freely.** A shorter derivation of the same statement
   changes the Solution side only. The statement, its Challenge and its identifier
   are unchanged.
2. **A new displayed step is a new statement.** If a cleaner derivation introduces
   an intermediate claim that a reader is asked to believe, that claim gets its own
   row and its own evidence. It starts as unchecked and is shown as unchecked.
3. **A changed statement is a new record.** Strengthening or weakening a theorem
   creates a new statement and a new comparison. The old row stays in the history.

## Three separate facts per statement

| Field | Question it answers |
| --- | --- |
| `statement` | Is this exact claim checked by the kernel at the recorded pin? |
| `route` | Does the Lean proof follow the written proof: `same`, `alternative` or `none`? |
| `reach` | Is the declaration in the dependency closure of a headline theorem? |

A statement can be checked by an alternative route. That is a true, useful status
and is displayed as such. It is never displayed as a check of the written argument.

## Collapsing onto the elegant path

Keep the checked theorems whose statements are worth reading, and treat the rest
as scaffolding. Before a paper is released:

1. Every displayed claim in the paper resolves to a statement row.
2. Every statement row has a declaration, or an explicit `none` with its reason.
3. The dependency closure of the headline declarations is computed from the
   compiled environment. A declaration outside that closure leaves the default
   build root. It stays in Git history and is never counted as coverage.
4. Where the final derivation differs from the Lean proof of a load-bearing step,
   the step is either re-proved along the final route or marked `alternative`.

Counts of declarations or lines are not progress. The measure is whether every
claim a reader is asked to believe has a stated evidence class.
