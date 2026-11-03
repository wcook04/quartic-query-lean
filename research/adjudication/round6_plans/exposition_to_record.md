# What the long record should receive from the round-six exposition revision

The exposition now links into the record only at these existing anchors, all present at the pinned commit `e9dfefb`:

- `forr_small_instance`
- `AC-example-tests`
- `upper-amplification-proof`
- `upper-cyclic-example`
- `upper-explicit-log6`
- `CL-minimax`
- `CL-early-late`
- `CL-simulator`
- `R3-A-RESULT`
- `R3-01-CLASSICAL`

It no longer links to `forr_repetition`, `forr_circuit_size`, `forr_target`, `upper-comparison-law`, `upper-coupling`, `CL-selection-independence-example`, `CL-independent-information`, `CL-product-law` or `CL-adaptive-example`. Those passages stay as they are; only the exposition's pointers to them were removed. Please keep the ten anchors above stable, or list any renames at the end of `round6_plans/reasoning_record.md`.

Material that left the exposition, together with where the record already holds it:

1. **Fixed-cap amplification constants.** The record keeps the trial recipe: no iteration with probability 1/2, otherwise a uniform number of iterations below ⌈10/√γ⌉. It also keeps the 9/40 trial success and the ⌈ln(1/η)/ln(40/31)⌉ repetitions, at #upper-amplification-proof. The exposition now states only the contract and links there for "the constants". I checked 9/40 numerically: the worst trial success over p ≥ γ is about 0.246.
2. **The fractional cycled-board variant.** This is the stage with weights (1−ε,0,0,1), success 23999/48000 and conditional probabilities 11999/23999 and 12000/23999. It now lives only at #upper-cyclic-example. The exposition replaced it with an exact stage on the actual board. On the cycled board every projection succeeds with probability 0 or 1, so the decoders there are exact and the comparisons deterministic. After pivot 2 the success-and-column masses are (1/4,0,0,1/4), success has probability 1/2, and the conditional law is (1/2,0,0,1/2); Grover iterations leave a success probability of 1/2 unchanged. After pivots 2 and 4 the weights are (1,0,0,0), success has probability 1/4, and one iteration makes success certain. If the record wants it, a two-line note at #upper-cyclic-example could add that the concrete board (as opposed to the abstract comparison table) has exact decoders and this ε-free behaviour.
3. **The minimax separating-hyperplane sketch** now lives only at #CL-minimax.
4. **The ℓ-power bookkeeping** behind (log m)^6 is at #upper-explicit-log6. The exposition keeps the two totals and the result.
5. **The two-instance cap-event dependence remark** is at #CL-adaptive-example. The exposition no longer mentions it.
6. **The Lean audit detail** moved out of the paper. This covers the Comparator configuration and receipt, the "built but not compared" constants theorem, the auxiliary amplifier and finite direct-product comparisons, the constant-on-promise branch of `QLe`, link-relation provenance and execution isolation. It belongs in record §2.9 and the repository metadata.
   - The exposition no longer says anything about statement review.
   - Record §2.9 still describes the amplifier and direct-product rows as unreviewed or stale. Round-five `research/adjudication/round5_statement_fidelity.md` (an AI review dated 3 November with no Lean run) covers all four headline theorems, `uniformOpaqueAmplifier` and `direct_product_external_finite_realized_caps` (CX004, QX-008, FX027). Bringing that into line is for the record owner.
7. **The board's bit count.** 5936 = 4[4+16+4(6+360)] is now printed in exposition §3, as the board instance of the input-size formula n. The record's #AC-example-tests could print it beside K=371 for symmetry.

Two pedagogical additions in the exposition would be easier to follow up if the record carried matching notes:

- **Simulator crosswalk (SX-031).** The exposition announces that record §6.5 uses a four-column XOR toy with L=1 and positions numbered from 0. The record's #CL-simulator-example could add one sentence on how that toy relates to the exposition's one-based Forrelation board.
- **The three budgets (SX-030).** The exposition states the chain: G for the whole run; L as the column total, which is also the heaviness threshold and the simulator's abort point; and L per instance, which is what the direct product needs. #CL-heavy already says that a nonheavy run uses at most L queries on each string, so no change is needed.

Answers to the four reader questions were checked exactly by the adjudicator's own script, `scratchpad/expo/answers.py`, which ships with no repository file. Q1 is the changed-board test failures: 1, 2, 2 and 3 at addresses 00, 01, 10 and 11. It agrees with the record's §4.4 description of the second board, where the only failure at 00 is the domain test.
