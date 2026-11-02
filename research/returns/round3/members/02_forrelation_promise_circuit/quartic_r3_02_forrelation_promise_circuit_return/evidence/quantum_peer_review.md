# Cold mathematical reading of the replacement section

Reviewed the entire `return/quartic_r3_02_forrelation_promise_circuit_return/section.md` draft (393 lines, 3,519 whitespace-delimited words at time of reading), including every displayed formula, the two tables, quantum implementation/evidence language, and citation roles. Review is source-level; it did not run Lean, execute the final checker, or independently reproduce all circuit gate counts.

## Concrete corrections

### 1. Restore inline mathematical delimiters and missing commands throughout

**Must correct before delivery.** The draft currently has no `$` or `\(` inline mathematical delimiters at all. It uses ordinary parentheses, so inline expressions will render as literal source text. Several commands have also lost their leading backslashes. Examples include `(k\ge2)` in the opening paragraph, `(delta>0)` in `forr_definition`, `(psi_z)` and `(Pi=|u\rangle\langle u|)` in `forr_quantum`, `(langle u,\psi_z\rangle=\Phi(z))`, `(mathcal L_z)` in `forr_coherent`, and `(lceil k/2\rceil)` in the interference comparison. All table mathematics has the same issue.

Use proper inline math delimiters consistently and restore `\delta`, `\psi`, `\Pi`, `\langle`, `\Phi`, `\mathcal`, `\lceil` where intended. The display environments themselves survived intact. This is a rendering/source transcription issue; do not treat it as a mathematical error in the intended formulas.

### 2. Qualify the complete wrapper's explicit repetition count and probability law

**Located at `forr_coherent`, paragraph beginning “Formal implementation of the asymptotic conclusion.”** The literal theorem `construction_lemma_2_1_ii_complete` existentially quantifies `n` and `L`. It does not state `n=q` or identify `L` with the displayed binomial polynomial. Its proof chooses `n=repetitions k eta=q` and `L=Bern(decodeProb k t q)`; `decode_samples` plus `compile_circ` give the directly parameterized `qk`/`2qk` conclusion.

The current wording “More precisely, the complete ... wrapper ... adds at most `2qk` ... one law `L_z`” can be read as attributing those extra equations to the wrapper's formal type. A precise repair is:

> Instantiating `decode_samples` at the displayed repetition count `q` and applying `compile_circ` gives a physical implementation of the binomial output law with cap `2qk`. The complete Lemma 2.1(ii) wrapper packages the same construction with its repetition count and law existentially quantified: the same isometry, initial state, output labeling and law occur in both the correctness clauses and the physical continuation equation.

Alternatively state explicitly that the wrapper **proof** chooses `n=q` and the displayed law. The mathematical conclusion is valid; this correction preserves exact theorem/type fidelity.

### 3. Define `Q_eta` precisely at its first appearance

**Located at `NEW-FOR-28`.** The draft says `Q_eta` uses the bit-query convention “as in §2.2,” but §2.2 itself defines `Q` at error `1/3`. A short phrase makes the replacement independently readable:

> Here `Q_eta` is the minimum worst-case bit-query budget of a procedure having error at most `eta` on every promised input, with the budget applying on every input and every measurement branch.

This may duplicate the retained §3 introductory convention during integration, so remove that duplication only after confirming the surrounding text. It is a notation completion, not a missing proof.

## Mathematical conclusions checked

- Normalization has exactly `k+1` factors of `m^(-1/2)`, yielding `M=2^(t(k+1))` on the stated `k>=2` domain. Matrix order, Boolean-to-sign convention, promise asymmetry, and both threshold directions are correct.
- The elementary moment proof gives `exp(-qc/16)` on no-inputs and the stronger `exp(-qc/10)` on yes-inputs. The strict lower-tail event and the integer/real threshold convention are treated correctly.
- The flag-recording unitary `Pi tensor X+(I-Pi) tensor I` is input independent and unitary. The retained tensor expansion and its measured binomial law hold on every input, including `p=0,1` with the stated polynomial convention.
- The ordinary full `qk`-query construction is valid: each phase diagonal is one physical query, fixed block relabelings are query free, and repeated trials use fresh registers with query-free address swaps. No stopping rule or promise test controls the cap.
- The current source's generic `2qk` implementation is distinguished from the ordinary `qk` proof. The draft correctly declines to identify its explicit tensor display with the implementation's concrete register layout.
- The exact circuit's off-promise output rule `(d,b)=(0,0)` follows from the two comparisons; the quantum procedure is allowed to output one there.
- The three worked examples are correct, including the chosen zero first block `(1,-1,1,1)`: its dot product with `(2,-2,-2,-2)` is zero. The numerator histogram and promise census are correct by the parity argument.
- Ideal intermediate bounds, modular arithmetic invariants, and signed recovery of final comparison integers are properly separated. The three final magnitude bounds imply strict inclusion inside the signed interval. I checked the displayed scalar inequality chain for the size bound, but did not reconstruct each implementation cost independently in this pass.
- Citation roles are correctly separated: AA supplies the earlier quantity and quantum interpretation; BS v3 supplies the parameterized promise; AA Proposition 6 and BS Proposition 1.2 are explicitly described as the different linear-interference law. The reference note correctly distinguishes arXiv locators from journal pagination.

## Evidence limits

No new mathematical defect was found beyond the formal attribution/notation corrections above. The physical continuation statement really concerns the same `F,L,out,o` witness, and its `Inhabited` choice is constructed from `k>=1,m>0`; no extra open mathematical premise is concealed there.

The section's broad receipt summaries and finite-checker execution results were not independently re-audited in this pass. The earlier delegated quantum audit verified focused source-hash attachment and inspected the relevant supplied theorem-type/axiom output. The parent evidence and circuit audits remain the authorities for the complete receipt and checker assertions.
