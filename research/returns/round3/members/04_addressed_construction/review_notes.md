# Review and authoring notes

## Result and scope

The assigned addressed construction is sound at the scope checked. This return supplies a complete replacement of baseline §4, retaining its mathematical content, expanding the proofs where the model interface matters, and adding a reproducible example that distinguishes promise verification from address decoding.

The central implication is pointwise: a genuine winner has no zero for an opponent to find, while its correctly addressed cell finds a zero in every other column. Only the winner's own decoding must be reliable. The rival's partial-function instances and decoded label may be arbitrary.

The task is editorial and mathematical reconstruction. The construction and separation are attributed to OpenAI. The finite example, domain-test counterexample and explicit clean-oracle corollary are additional explanations, each recorded at its actual evidence level. No historical novelty, human endorsement, full-paper review or accepted integration is claimed.

## Ranked, located changes

### 1. Make the domain-recognition obligation visible

Baseline CL-transcripts and CL-fidelity already contain the necessary hypothesis, but their force becomes clearer in AC-circuit, AC-transcripts and the worked example. A transcript does not merely certify an output bit. Gate consistency first forces the entire true evaluation, and the domain output then certifies that the partial value exists.

The explicit counterexample is discriminating: on the second board, an unpromised all-one column passes 370 of 371 tests. The sole failure is its domain output. Removing the two domain checks gives 369/369 passes although the total function is zero. This is a failure of that proposed simplification, not a flaw in the original definition.

### 2. Explain off-promise decoder behavior using the actual small promise

AC-example-promise uses actual P_{2,4}. The positive input 00000000 has Φ=1/2; the unpromised input 11110000 has Φ=-1/2. Their projection success probabilities are both 1/4. Independent repetitions and a decision based only on those outcomes have identical laws. A plausible decoded label therefore supplies no proof of promise membership.

The scope matters: this is about the specified projection decoder, not every quantum algorithm or all information in its workspace. The exact domain circuit distinguishes the two inputs. AC-comparison then proves why even a garbage opponent label is harmless against a genuine winner.

### 3. Separate semantic equality from the output-test bridge

AC-winner uses a semantic predicate requiring defined partial answers. Its agreement with the paper's winner wording needs no circuit-realization assumption. AC-local-equivalence replaces those answers by transcript output tests and explicitly uses CircuitRealises C P.

This preserves a genuine distinction between two Lean bridges. It also explains why winsAt_iff_paperWinsAt cannot certify that an arbitrary circuit realizes the intended partial function. The canonical ledger's local-output definition is left intact; correspondence.json records the equivalence under the realization premise.

### 4. Use the current arbitrary-index evidence at its exact scope

Baseline CL-coherent-tests pointed chiefly to the older uniform sampler. AC-coherent now states the arbitrary-test-index direct-sum action for fixed candidate (i,s), fixed initial work states and retained workspace.

The supplied current theorem construction_lemma_2_2_complete combines the same coherent witnesses with finite embedding and physical compilation, not merely matching output distributions of unrelated witnesses. It gives 2q* ordinary bit queries. AC-clean-oracle proves the distinct reset-workspace interface at 4q* by compute-copy-uncompute and leaves its Lean tie empty.

The old unelaborated comments are historical. They do not override the current root receipt once source hashes and exact declaration membership are checked. Conversely, a root build does not extend the Construction Comparator's limited member list.

### 5. Preserve the difference between adaptive depth and support

AC-pointer-support explains why the test has depth ℓ+1 and support ℓ+m. The pointer is read before the target location is chosen. Each target bit is essential by selecting its row; each pointer bit is essential by assigning different values at the two rows selected by words differing only there.

The current physical-coordinate theorem supports this on full BitLoc inputs. The paper already gives adaptive lookup. The earlier ledger owns the faulty fixed-support wording; the current canonical row is corrected.

### 6. Keep source versions and historical roles exact

The correct ABK v2 printed locators are Definitions 14–15, pp. 20–21, and Lemma 17, p. 22. The supplied extraction's environment-wise numbering gives 10–11 and 13, respectively. The bibliography uses the inspected 9 July 2019 preprint while retaining the original 2016 STOC publication information.

Ambainis et al. v3 §1.2, p. 6, explicitly discuss direct outward pointers, together with the exponential-alphabet qualification. This construction exposes all pointer bits and charges ℓ queries for a selected pointer. No symbol-query result is transferred.

OpenAI's Lemma 2.2 is printed as one lemma. The .i/.ii identifiers belong to the local ledger; the replacement uses “classical part” and “coherent part” when describing the printed result.

## A concrete simplification attempt

The successful simplification is to prove transcript uniqueness once, then make all local/semantic equivalences consequences of that fact and the two-output circuit interface. This removes repeated reconstructions of circuit evaluation from the reader's proof path.

The tested unsuccessful simplification is to drop the domain-output checks and retain only gate consistency and the address-value checks. The second board refutes it exactly. Its failure identifies the essential extra information carried by d.

A second tempting simplification, replacing adaptive depth by small fixed support, is false for every nontrivial lookup. The six-coordinate/depth-three example exhibits the mechanism without suggesting a new lower-bound theorem.

## Independent AI checks and dispositions

Three separate AI tasks assessed primary sources, Lean/types/native evidence and the exact example. Two then reviewed an initial section draft. Their initial reports are preserved in evidence/; the following issues were corrected before finalization.

| Initial finding | Disposition |
|---|---|
| Inline math delimiters lost in draft transport and missing backslash before quad | Restored delimiters and corrected equation (4.12); checked all passage/display boundaries. |
| Board description disagreed with the checker | Aligned with complete serialized board: every pointer into columns 2–4 hits its zero; pointers into column 1 vary with the cell label. |
| Wrong-address failure counts listed 3,4,3 | Corrected to 1,2,1 at labels 00,01,11; all pointer tests there pass. |
| Selected type/axiom-audit scope too broad | Narrowed to audited names; root-build membership remains separate for every declaration. |
| “Workspace may depend on input” ambiguous | Fixed dimensions and initial states are stated; only final states depend on input. |
| “Preserves relative phases” could suggest an unchanged reduced label state | Replaced by exact linear action and explicit possible label/work entanglement. |
| ε not introduced | Added 0<ε<1/2 before the decoder bound. |
| Printed Lemma 2.2 described with ledger part numbers | Changed to classical/coherent parts; retained exact .i/.ii only for corpus identifiers. |
| Two boards implied to be serialized in board.json | Stated that board.json is the complete base board and the second board is constructed by the checker and described in output. |

The equal-projection-law calculation was added after the initial peer reports and separately checked by the example author. Final source and Lean statement/evidence reviews found no remaining material issue within their scopes; their dispositions are in evidence/final_peer_reviews.md. The final delivered checker/output hashes are in manifest.json and examples/validation.json; the earlier peer replay's hash identifies its earlier output, not the later extended output.

## Evidence and computation actually checked

- All 400 members covered by the input manifest match their recorded lengths and SHA-256 hashes.
- All 124 recorded local Lean/config hashes match the root-build, Construction Comparator, dependency export and selected type/axiom-audit records.
- The native audit source and log hashes match; its terminal audit marker and selected declaration records were inspected.
- All 23 receipt-file hashes listed in the source snapshot match.
- The current Construction Comparator contains exactly the four named core source theorems and their checked wrappers; newer construction wrappers are not silently added to it.
- The Python checker validates all 256 exact circuit inputs, all 16 base-board candidate pairs, all 360 selected transcript single-bit mutations, six essential pointer coordinates, 48 comparison cases and the domain-omission counterexample.
- The extended checker also verifies the two exact Bernoulli laws and all eight three-trial outcome patterns. Its general fixed-n conclusion is proved by the displayed product law in examples/README.md.
- The portable package validator checks anchors, display coverage, stored outputs, identifiers, source bindings and manifest integrity. Its actual result is checks/validation.json.

No Lean, Lake, Comparator, external kernel, public post or repository integration was executed during this contribution.

## Authoring receipt

| Field | Record |
|---|---|
| Object and genre | Self-contained replacement section in a long mathematical reasoning record. |
| Target reader | Mathematically mature researcher familiar with basic query complexity, new to this exact construction. |
| Contribution | Proof-forward exposition of a known construction, exact statement/evidence audit and new finite diagnostic examples. |
| Principal claim | Semantic winner equals the conjunction of locally checkable tests under exact circuit realization; F is total and its winning pair unique; a genuine winner beats every opponent with the winner decoder's success probability. |
| External field map | OpenAI is authority for this construction; ABK supplies cheat-sheet ancestry; Ambainis et al. supplies pointer ancestry with its alphabet qualification. |
| Proof spine | Exact circuit → unique transcript → semantic addressed winner → uniqueness/totality → local tests → adaptive depth/coherent evaluation → off-promise comparison. |
| Hard step | Respecting the promise while the whole input is total; coherent evaluation must retain input-dependent query history and count physical queries. |
| Example and limit | Actual P_{2,4}; schematic r=2 and separate finite circuit. All bits specified. No asymptotic-separation claim. |
| Strongest useful counterexample | Removing domain tests falsely accepts the explicitly constructed off-promise all-one column. |
| Claim/Lean alignment | Full types, implicit context, ordinary premises, source hashes and per-layer evidence in correspondence.json and evidence/. Clean oracle and finite example explicitly prose/computation only. |
| Canonical changes | None. New explanatory claims are separate records, and replacement passage locations are mapped for integration. |
| Parameter order | Fixed k for the paper family; circuit constant A_k fixed before size. Example r=2 is declared separately. |
| Citation roles | Exact editions and printed page/theorem locators; no historical comparison imported as a theorem for this construction. |
| Cold-reader difficulty | “Garbage address” could sound like an invalid pointer. Clarified that every pointer word is valid and that undefinedness concerns the partial inputs, not the cell label. |
| Notation | Actual input versus stored transcript kept separate; pointer-word decoding declared before X[p]; test output 1 means pass; q* distinct from domain output d. |
| Dependency-based simplification | One topological induction supports all transcript/output bridges. |
| Mechanism and understanding | Demonstrated by the outward-zero proof and equal-decoder-law example. |
| Elegance and proof economy | Demonstrated by shared transcript lemma; unnecessary attempt to drop domain checks explicitly refuted. |
| Structural yield | The example exposes exactly which clause rules out unpromised data and why the decoder need not detect it. |
| Transfer and connections | General finite partial-function/circuit interface is reusable; historical theorems are not transferred. |
| Further questions | No new broad research programme proposed. The concrete remaining formal task is packaging the optional clean XOR corollary, if a later consumer needs it. |
| Scope omissions | Full Forrelation lower bound, tournament proof, planted lower bound, exponent passage and unrelated literature unassessed here. |
| Exact open boundary | No missing ordinary construction implication found. The clean XOR interface has an ordinary proof but no exact supplied Lean bridge; downstream results remain their own sections' responsibility. |
| Rendering | Markdown and machine-readable files checked; no PDF typesetting, bibliography rendering or webpage rendering claimed. |
| Writing measurement | Private paper_register tooling was not supplied or invoked; source-located qualitative moves are recorded without a fabricated numerical style score. |
| Human review | None claimed. |

## Integration instructions

Replace the baseline section between its §4 heading and the immediately following §5 heading. integration_map.json identifies the exact source hash and maps each old CL passage to its new home. Use the supplied §3.17 circuit/decoder interface and leave the subsequent tournament and verifier proofs with their owning sections. Final synthesis should consume this return's actual files and refreshed correspondence, rather than assuming that a future round-three return already exists.
