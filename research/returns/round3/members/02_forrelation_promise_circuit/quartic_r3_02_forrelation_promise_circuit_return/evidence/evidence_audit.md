# Job 02 source and evidence audit

## Finding

The frozen packet supplies current, source-bound evidence that the integrated Forrelation sources and the relevant `Paper` wrappers compiled. No Lean or Lake executable is available in this review environment, so **no fresh Lean build or Comparator run was performed here**. The checks below independently recompute file and receipt hashes, exact declaration membership, recorded type blocks, and the stated axiom allowlist.

The new wrappers should not be described as uncompiled merely because their preserved header comments say `UNELABORATED`. Conversely, none of the declarations assigned to §§3.1–3.5 is named in a current Comparator receipt. Their successful compilation, reviewed statement relation, and presence or absence in the dependency closure are separate facts.

## Recomputed evidence

`audit_evidence.py` is a portable read-only verifier for this exact packet. Run it with `--packet PATH_TO_EXTRACTED_PACKET --output NEW_OUTPUT_DIRECTORY`; add `--archive PATH_TO_ORIGINAL_ZIP` to record the archive hash. It writes only to the separate output directory and requires Python's standard library. It does not run Lean.

- All **453** members listed in `manifest.json` match their byte counts and SHA-256 hashes.
- All **448** entries in `manifest.input_sha256` match.
- All **124** local Lean/configuration files bound by the timestamped root receipt match. The independently enumerated local snapshot has no missing or extra files relative to the bound set.
- The passed root receipt names **2,652** declarations. All **91** declaration records mapped to the ten selected statement rows are members of that current declaration set.
- The current dependency export hash and all its 124 source bindings match. It has two roots, 1,354 reached public declarations, and no unresolved constants.
- All receipt hashes listed in `EVIDENCE_SNAPSHOT.json` match. Every receipt classified there as current has the same complete 124-file binding and matching bytes.
- The final type/axiom audit's log and audit-source hashes match the supplied passed verdict. All **258** expected unique declaration printouts are present, every audited name is in the root-build declaration list, the exact success marker is present, and the recorded axiom lists contain only `propext`, `Quot.sound`, and `Classical.choice`.

The packet manifest records repository commit `1dd469dd0042b937b739da3bc211eeb60bdf7462`; the current root receipt records commit `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`. This difference does not make the receipt stale: the complete local source binding matches exactly. Currentness here is determined by those hashes, not by assuming equal commit labels.

The original attachment SHA-256 is `db412239bd75e1a7fc23d262903265ac5229d2d48c59c0f7ff743901d71cde24`. The packet manifest SHA-256 is `53528c475a467609c2f1d5640e7db843711ae80764d80ed87077f1b292d53b7a`.

## Current source locators

The decisive build evidence is `repository/corpus/receipts/lean-build-root-2026-11-02T182539383153+0000.json`. It records `lake build QuarticQuery`, followed separately by the compiled-environment declaration inspection. The older `lean-build-root.json` is retained historical evidence and has no source binding.

The source-current type/axiom result is the conjunction of:

1. `native_results/final-evidence/reviewed_axiom_audit.json`, which prepares the expected names and allowlist;
2. `native_sources/final-evidence/reviewed_axiom_audit.lean`, the actual assertions and print requests;
3. `native_logs/final-evidence/reviewed-type-axiom-audit.log`, ending with `R2_AXIOM_AUDIT_OK declarations=258`;
4. `native_results/final-evidence/reviewed_axiom_audit_verdict.json`, which records native exit zero, unchanged inputs and the matching log hash.

The preparation JSON retains the word `unexecuted` in its kind. That preparation label does not negate the later supplied execution log and passed verdict. Do not cite the preparation record alone as an executed check.

`repository/research/adjudication/round2_construction_quantum.md`, sections “Mathematical dispositions” and “Per-target crosswalk,” records the integrated construction/quantum review. The corresponding `round2_construction_quantum_ties.json` records the reviewed source hashes, ordinary premises, additional assumptions and remaining clauses. `repository/corpus/ties.json` and `repository/corpus/statements.json` contain the subsequently integrated ties and computed evidence states.

## Statement-level disposition

Every row below has a current build binding. None has current declaration-level Comparator membership. Exact/stronger below is the maintained relation review, not a conclusion inferred from compilation.

| Statement ID | Principal current declaration | Maintained relation and boundary |
| --- | --- | --- |
| `def-walsh-sign` | `QuarticQuery.Paper.construction_walsh_definitions` | Exact bundle of bit signs, Walsh parity, normalized matrix, uniform vector and sign diagonals on `m=4^t`. |
| `eq-3` | `QuarticQuery.Paper.construction_equation_3` | Exact matrix word and `delta=2^(-5k)`, for `k≥1`. |
| `eq-4` | `QuarticQuery.Paper.construction_equation_4` | Exact two branches, undefined case, input size and disjointness. |
| `claim-proj-prob` | `QuarticQuery.Paper.construction_projection_test` | Partial: exact squared-projection law and gap, `Samples k`, and `Runs (2*k)`. No complete `Runs k` witness. |
| `lem-2.1.ii` | `QuarticQuery.Paper.construction_lemma_2_1_ii_complete` | Exact reviewed tie: one coherent isometry, its own all-input Boolean law and promised correctness, connected to a physical continuation acting on every embedded logical state. |
| `claim-N-phi` | `QuarticQuery.Paper.construction_N_phi` | Exact numerator, denominator, Walsh scaling and normalized quotient bundle. |
| `claim-integer-tests` | `QuarticQuery.Paper.construction_integer_tests` and `QuarticQuery.Paper.construction_forr_output_bits` | Each partial individually. Together they give both comparison equivalences and the actual circuit output rules. A single exported conjunction is not supplied. |
| `claim-circuit-size` | `QuarticQuery.Paper.construction_circuit_costs` plus three ideal-integer bound lemmas | Partial. The modular endpoint/size theorem and the ideal-integer walk/prefix/butterfly bounds do not identify every stored register with an unbounded signed intermediate. |
| `lem-2.1.iii` | `QuarticQuery.Forrelation.exists_circuit` | Stronger parameter range, `k≥1,t≥1`; both actual realization and the explicit size cap. |
| `lem-2.1` | `QuarticQuery.Paper.construction_lemma_2_1_complete` | Exact reviewed conjunction; alternative route only in the lower-bound component. It is present, built and explicitly axiom-audited. |

All reviewed `Paper` principals in this table carry ordinary premises and empty additional `open_assumptions`. In particular, `k≥1`, `m=4^t`, `0<eta<1/2`, or `t≥1` are domain conditions, not newly unproved external hypotheses. The missing tight `Runs k` implementation and the missing register invariant remain omitted clauses; they are not hypotheses silently accepted by these theorems.

`section_statement_evidence.json` preserves all 91 row/declaration records, exact source signatures and source hashes, current build/comparison/reach membership, and complete recorded type/axiom printouts where supplied. `recorded_lean_types.json` contains the 15 directly relevant audited type blocks without prose abbreviation. The native `#check` output uses Lean's own pretty-printing; the source signatures preserve explicit existential binder types that the display may infer.

## Dependency reach and Comparator scope

The `Paper` wrapper principals above are **not** in the dependency closure of the two exported headline roots. Many of their underlying implementations are reached. A row such as `eq-3` can therefore have aggregate `reach: reached` while its exact wrapper tie has `reached: false`. Do not combine the exact relation of one declaration with the reached status of a different partial declaration.

The current positive Comparator bundles cover their actual listed names: Construction covers uniqueness/transcripts/winner lemmas, Foundations covers complexity definitions and reindexing, Separation covers its displayed aggregate theorems, Tournament covers two `Checked` declarations, and Unconditional covers the headline roots and `ForrelationLower.bansalSinhaLower`. No Forrelation promise/circuit/projection wrapper or decoder theorem is named. Passing the Unconditional bundle, including its paranoid run, does not make all helper rows Comparator-checked.

The existing checks are unsandboxed local runs. The retained challenges share the maintained vocabulary and theorem specifications. They provide statement comparison against those challenges; they do not establish independent semantic authorship or a human mathematical review.

## Required baseline evidence corrections

These are evidence refreshes, not changes to the mathematical claims.

1. **§3.1, final source/evidence paragraph.** The sentence saying the `L` row has no formal tie is obsolete. `QuarticQuery.Paper.construction_equation_5` now has an exact reviewed tie to `eq-5`; it is built and in the explicit axiom audit. The definitions/word/promise also now have the exact wrapper ties listed above. The older component ties remain partial and should not be erased.
2. **§3.2, final source/evidence paragraph.** “No single cited declaration contains every sentence of either row” is now false for `claim-N-phi`, because `construction_N_phi` supplies the full bundle. It remains true that `claim-integer-tests` has separate comparison and actual-output theorems rather than a single exact conjunction tie.
3. **§3.3, evidence and `LEAN_GAPS` discussion.** The missing same-witness retained-state combination has been supplied by `construction_lemma_2_1_ii_complete`, at `Paper/ConstructionForrelationComplete.lean:25`. Keep the generic factor two and the missing tight physical `Runs k` implementation. The shorter `construction_lemma_2_1_ii` is explicitly documented as a partial helper; use `_complete` for the complete witness claim.
4. **§3.4, final source/evidence paragraph.** `abs_numerator_le` is no longer the sole declaration tied to `claim-circuit-size`. Current additional ties prove explicit ideal-integer walk, prefix and butterfly bounds and the actual modular circuit endpoint/size. Keep the distinction between ideal arithmetic and all stored circuit registers. The missing invariant must not be declared proved by assembling unrelated endpoint and growth facts.
5. **§3.17, final paragraph, and baseline `LEAN_GAPS` item 31.** The assertion that no single conjunction declaration exists is obsolete. `QuarticQuery.Paper.construction_lemma_2_1_complete`, at `Paper/ConstructionForrelationComplete.lean:66`, supplies the complete conjunction with current root-build membership and an explicit axiom-audit printout. No current Comparator receipt names it, and this session has not replayed it.
6. **Source headers.** All six integrated `ConstructionArithmetic`/`ConstructionForrelation*` modules still have historical `UNELABORATED` header text. The supplied receipt supersedes that historical status. No input source is edited in this review. `module_source_versions.json` identifies those modules and compares them with the preserved return-2 versions.

Suggested evidence replacement for the obsolete §3.17 paragraph:

> The current snapshot contains the complete conjunction as `QuarticQuery.Paper.construction_lemma_2_1_complete`. Its quantum clause uses the same coherent preparation and output law together with a physical continuation of the retained state; its classical clause uses the project's alternative fixed-parameter proof. The supplied source-bound root-build receipt includes this declaration, and the supplied type/axiom audit records only the stated standard axioms. No current Comparator receipt names the conjunction, and no new Lean run was performed for this revision.

This is a located recommendation for the consumer section, not an edit to the frozen baseline or an assertion that any future section return has been integrated.

## Scope and limits

Assessed in this subtask: packet/request roles; all manifest and input hash records; all current/legacy corpus receipt metadata; current dependency-export names and hashes; selected corpus rows and ties; the construction/quantum adjudication and relevant tie entries; native final audit source, verdict and all printed declaration/axiom blocks; current complete Forrelation witness signatures and their proofs; baseline §§3.1–3.5 and §3.17 for stale evidence statements; current integrated versus preserved return module bytes. Source proof details for arithmetic and quantum semantics are handled by the parallel mathematical auditors, not independently recertified by this metadata audit.

No external literature was searched in this subtask. No source input, corpus tie, Lean file or baseline text was changed. No human review, clean-clone reproduction or independent kernel execution is claimed.

The 124-file root binding includes dependency manifests but does not hash the full dependency checkout or executable binaries. The native `.olean` file is not supplied here; its recorded hash cannot be recomputed. Before/after hashes cannot detect a change-and-revert during the original run. These are the precise limits of the evidence supplied, not a reason to discard its successfully matched local-source scope.
