# Focused Lean and evidence audit: addressed construction

Reviewed 2 November 2026 against the extracted round-three job-04 packet. This is an independent source review and receipt/hash check. **No Lean, Lake, Comparator, or external kernel was executed in this review.** The companion `lean_audit.json` records 37 exact source signatures or full source-level type restatements, their context binders, file hashes, per-declaration evidence membership, and exact reading scopes.

## 1. Mathematical disposition

The inspected construction definitions and the local-test proof support the intended total-function construction. I did not identify a mathematical error in these clauses. The revision should retain the following dependency order:

1. Acyclic circuit syntax supplies one unique evaluation transcript on every input, including off-promise inputs.
2. The semantic winner predicate requires defined partial-function answers, a column of ones, the correct transcripts at those answers' address, and outward pointers to zeros in every other column.
3. Uniqueness and totality follow directly from that semantic predicate, without a circuit-realization premise.
4. The circuit-realization premise allows replacing semantic partial-function answers by local gate and output tests.
5. The common test family has shallow **adaptive decision trees**. Coherent evaluation uses retained query history and finite direct sums.
6. A genuine winner cannot be disqualified by any incoming pointer. At its true address it disqualifies each other column. Only its own decoder needs a correctness guarantee.

### Semantic wording versus the circuit bridge

`QuarticQuery.winsAt_iff_paperWinsAt` is unconditional in the circuit: both sides already state the values of the partial function. It does not certify that an arbitrary circuit computes that function.

`QuarticQuery.winsAt_iff_outputs`, `QuarticQuery.winsAt_iff_localTests`, and `QuarticQuery.Paper.construction_win_at_address_outputs` explicitly require `CircuitRealises C f`. This is an ordinary supplied premise, discharged in the intended family by the exact Forrelation circuit. It is not an extra hardness assumption. It must not disappear when mapping prose to the local-test theorem.

`CircuitRealises` contains (a) existence of a consistent transcript, and (b) the domain-output equivalence and value-output correctness for every consistent transcript on every raw input. Transcript existence is independently supplied for every acyclic circuit by the transcript module. Thus the domain test is exact even on an input for which the partial function has no value.

### Uniqueness, totality, and malformed data

`winsAt_unique` proves uniqueness of both column and address. Column uniqueness uses only the all-one condition and the outgoing zero witness into an alleged second winner. Address uniqueness uses only the single-valued partial function. No circuit realization, decoding guarantee, or promise on any opponent is needed.

`addressedF` has the total type `TotalBool (BitLoc ℓ r C.size κ)`. Its existential winner condition is a proposition with a Boolean decision under Lean's classical convention. The `noncomputable` keyword is not a partiality marker. In the finite instance it is a finite Boolean function on all assignments to the physical coordinates.

The pointer encoding is a bijection between all length-ℓ Boolean words and the `2^ℓ` target rows. No invalid pointer strings are excluded. An off-promise instance, incorrect transcript, or pointer that hits a one makes relevant candidate conditions false; it never leaves the function undefined.

## 2. Exact test count, support, and query costs

For fixed `(i,s)`, the common test index type is

```lean
Column ℓ ⊕ Fin (2 ^ ℓ - 1) ⊕ Fin r × (Fin S ⊕ Bool).
```

The cardinality is `2^ℓ+(2^ℓ−1)+r(S+2)`. The two Boolean output labels are separate tests, not an OR condition: false indexes the domain-output test and true indexes the value-output equality. The circuit's two designated output gates need not be assumed distinct in the generic circuit syntax.

The exact uniform adaptive depth bound is `max 3 (ℓ+1)`. At the paper's `m=4^t`, `t≥1`, one has `ℓ=2t≥2`, so it becomes `ℓ+1`. Each pointer test reads its ℓ physical pointer bits before reading the target they select. Its complete fixed support has `ℓ+m` distinct essential coordinates. `construction_pointer_every_physical_coordinate` transfers independent witnesses from a lookup schema to the real `BitLoc` coordinates; this is stronger than checking only an abstract lookup function.

The correction belongs to the old ledger's fixed-support wording. The original preprint's Lemma 2.2 already uses the adaptive pointer read. `Paper/Section2.lean` still has an ambiguous “Correction” comment near its older `lemma_2_2`; cite the ledger as the error's owner.

For the family size bound, `construction_K_bound` has the actual hypothesis

```lean
t ≥ 1,
S ≤ A * mValue t * (2*t)^2
```

and concludes

```lean
card(TestIndex (2*t) (40*t) S) ≤ (42+20*A)*mValue t*(2*t)^3.
```

The constant A is fixed for the family and supplied by the circuit-size theorem. The exact count alone does not prove the asymptotic estimate. `construction_K_family` chooses B before t and supplies the concrete circuit, so the parameter order is visible.

## 3. Three coherent interfaces that must remain separate

| Interface | What the actual theorem supplies | Query units |
|---|---|---|
| `Upper.test_samples` / older `Paper.lemma_2_2` | A specified uniform distribution on test labels with the exact failing-test flag, with a coherent sampler witness | `max 3 (ℓ+1)` abstract reads before physical compilation |
| `Paper.construction_lemma_2_2_ii` | For each fixed `(i,s)`, arbitrary complex coefficients of the common test index; each index block applies its exact unitary and retains its work; all wrong-output amplitudes vanish | Same common abstract read count |
| `Paper.construction_lemma_2_2_complete` | The same arbitrary-index witnesses plus a finite physical embedding and a continuation transformer, correct on every embedded state and every continuation | At most `2(ℓ+1)` ordinary bit queries at `m≥4` |

The complete theorem has the quantifier order `∀ i s, ∃ Z … F … w emb P, …`: it selects one coherent family and then physically compiles those same witnesses. It does not obtain the abstract accuracy statement and physical cost from unrelated circuit witnesses.

The state-level output guarantee starts each index-specific work register at its selected ket `o e`. The coefficient vector is arbitrary; no normalization premise is needed for the linear identity. If the coefficient vector is normalized, the unitary image is normalized. The physical compiler's equality is stronger on its own interface: it preserves continuation probabilities for every embedded logical vector.

The theorem fixes candidate `(i,s)` and allows arbitrary **test-index** superpositions. Coherence over `(i,s,e)` can be obtained by another finite direct-sum instantiation of `construction_controlled_exact_samples`, but it is not literally the type of `_ii` or `_complete`. Avoid assigning that expanded claim directly to those names.

No inspected theorem packages a clean XOR oracle with all work reset. A standard compute-copy-uncompute argument gives that ordinary mathematical corollary with an extra factor two, hence at most `4(ℓ+1)` physical queries using the retained-work implementation. This should be stated and mapped separately. The return should not label the `2(ℓ+1)` retained-work bound as a clean-oracle bound.

The generic abstract theorem has no finite-coordinate-type assumption on κ because its circuit uses only finitely many reads. The physical compiler requires a finite inhabited coordinate type. The concrete `ForrelationCoord`/`Loc` specialization supplies these instances. No gate-complexity or workspace-size bound follows.

## 4. Winner domination on garbage addresses

The two deterministic statements are especially useful in the replacement proof:

* `winner_no_incoming_zero`: for any other column c and every address a, its pointer into the winning column reads true.
* `winner_finds_zero`: at the genuine winner's true address, its outgoing pointer reads false in every other column.

`Upper.cmpProb_winner` then gives

```lean
addrLaw n x i s ≤ cmpProb n x i j
```

under a genuine winning witness, `j≠i`, and positive k. The opponent's address law is nonnegative and has total mass one because it is the law of a unitary sampler on every input. No opponent promise appears.

`Paper.quantumWinner_dominates` combines this with `addrLaw_good`. Its full ordinary premises are `1≤k`, `1≤t`, `0<ε≤1`, enough repetitions for error `ε/(40*t)`, a genuine winning witness at s, and `j≠i`. It concludes `1−ε≤cmpProb n x i j`. The complete type is in the JSON and in the source-bound native type log. The new section can explain the deterministic event inclusion without reproducing all decoder parameters; its correspondence must retain them.

## 5. Evidence after independent hash verification

The source packet commit is `1dd469dd0042b937b739da3bc211eeb60bdf7462`. The current root-build receipt records commit `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`, at 18:25:39 UTC on 2 November 2026. The differing labels do not by themselves show drift: I compared the **complete recorded set of 124 local Lean/config hashes**, and every one matches the supplied current bytes.

The same 124-input verification passes for the dependency export, current Construction Comparator receipt, and reviewed type/axiom audit verdict. The audit source hash matches its supplied source, the full audit log hash matches the verdict, and the log ends with `R2_AXIOM_AUDIT_OK declarations=258`. All 23 receipt-byte hashes listed in the snapshot also match. These 29 independent hash checks are reproduced by `build_lean_audit.py`; they are evidence-custody checks, not Lean execution.

| Declaration group | Current root-build membership | Selected type/axiom audit | Construction Comparator |
|---|---|---|---|
| `winsAt_unique`, `existsUnique_gateConsistent`, `winner_no_incoming_zero`, `winner_finds_zero` | Yes | Not in that selected 258-name list | Yes, plus their `Checked` wrappers |
| `construction_lemma_2_2_i`, `_ii`, `_complete` | Yes | Yes | No |
| `construction_pointer_every_physical_coordinate` | Yes | Yes | No |
| `construction_unique_winner` | Yes | Yes | No; the related core uniqueness theorem is compared |
| `quantumWinner_dominates` | Yes | Yes | No |

The selected audit permits only `propext`, `Quot.sound`, and `Classical.choice`. This audit's preparation file still labels itself “unexecuted”; the separate passed verdict and matching terminal log supply the later result. Similarly, the historical “unelaborated” headers in the new Paper modules and old return-2 `LEAN_GAPS.md` do not describe the final packet's compilation state.

The current root receipt lists 2,652 compiled declarations. Its dependency export reaches 1,354 declarations from the two selected headline roots `theorem_1_1_unconditional` and `cubic_bound_fails_unconditional`. Most new exposition wrappers, including the complete Lemma 2.2 and winner-domination wrapper, are not reached by those roots. They are nevertheless compiled and audited. “Not reached,” “not compiled,” and “not proved” are different statements.

The Construction Comparator only selects its exact eight names. It does not directly compare all of Lemma 2.2 or every Paper wrapper. Its challenge imports Mathlib independently but mechanically shares the maintained definition and theorem specifications. A separate finite example is useful intended-meaning evidence; it is not a new Comparator receipt or universal proof.

## 6. Remaining boundaries for this section

There is no unresolved hardness premise in the inspected construction lemmas. The input premise needed for the local equivalence is the realized circuit supplied from §3. The circuit endpoint and size guarantee are enough; a stronger signed-integer refinement for every internal arithmetic register is not a prerequisite to §4. Likewise, a tight k-physical-query Forrelation projection routine is separate from the logarithmic coherent local-test cost.

No tiny exact example is contained in these Lean declarations. The parent contribution's independent Python example can demonstrate the semantic construction and adversarial garbage-address case; it should say precisely which partial function, address length, and circuit are schematic, and that no asymptotic separation or Lean theorem is established by finite checking.

The evidence report should say “the supplied source-bound receipts record a pass, and their local input hashes match”; it must not say “we reran Lean.” No human review is claimed.

## Reading receipt

The companion JSON has an explicit per-file scope list. It distinguishes full reads (the main construction modules, Statement, Decode, historical gaps, and the two adjudications), selected sections of the long record, sampled compiler/model interfaces, source-hash and membership inspection of receipts, and unassessed writing/literature assigned to other reviewers. The return-2 blueprint was sampled at the construction rows; all current proof modules underlying those rows were read fully. No claim of full-baseline or entire-literature review is made by this audit.
