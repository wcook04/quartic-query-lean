# Round six record revision: passage meaning audit

**Scope.** This audit covers the 42 `text_changed` passages and the 3 `added` passages listed in [round6_record_rebind.json](round6_record_rebind.json). Each was compared with `git show HEAD:docs/reasoning_record.md`, at sha256 `2c9971d1…`. The rebind reports 253 passages as moved only and no claim moved between passages. All 261 claim markers are present, and every old anchor still resolves.

**Who audited.** The agent that made the revision also wrote this audit. To compensate, every substantive sentence was checked against its source: the Lean file, the literature extract or the record passage it summarizes. The checks are listed below. This is not an independent human review.

**Verdicts.** Of the 7 claim-bearing passages whose wording changed, 5 are editorial and 2 are corrections. Of the 3 added passages, 1 is new mathematics and 2 were split out of existing passages. Two regressions were found during the audit and fixed before the final rebind, so none remains.

## Claim-bearing passages whose wording changed

| Passage (claims) | Change | Verdict | Check |
|---|---|---|---|
| `ROOT-RESULT` (eq-1, thm-1.1, eq-2) | The first paragraph is reduced to the attribution, since the new opening already states the result. The model sentences are merged. The final paragraph now points to §5.4 for $b_k=6$ and to §6.6 for $c_k=1/400$. The pointer to formal evidence moves to Appendix G. | editorial | The statements of (1), Theorem 1.1 and (2) are unchanged. Attributions to OpenAI Theorem 1.1 and ABKRT Theorem 2 are kept. The bound $D=O(Q^4)$ with $R\le D$ is kept. "After increasing the threshold" is kept for $1/400$, matching `CL-floors` ($t\ge8$). |
| `R3-01-QUANTIFIERS` (claim-exponent-ratio, cor-cubic-refuted) | The fixed-$k$ paragraph is rewritten. It now points to the growing-$k$ schedule in §7.3 instead of implying that no uniform control exists. | correction (QX-003) | "Strictly below $4-2/k$", "no single $k$ reaches four" and "the infimum needs no uniform statement" all keep the old meaning. The pointer is accurate: §7.3 proves the schedule. |
| `CL-address-guess` (claim-address-guess) | "Drucker's headline theorem has a different global-budget statement" becomes "would also serve, as §6.1 explains". | correction (expert handoff, item 1) | Checked against Drucker arXiv:1005.0644v2, Theorem 1.1 restated (extract line 145): $0<\alpha\le1$, hypothesis $\mathrm{Suc}_{T,\mu}\le1-\varepsilon$, partial functions allowed by the remark at extract line 69. With $T=L$, $\varepsilon=1/3$, $k=r$ and $\alpha=3/r$, the budget is $L$ and the bound is $2(2/3)^r$. Claim `claim-minimax-mu` gives success at most $2/3$ for depth-$L$ trees, hence for mixtures. `CL-simulator` caps the total at $L$, with side information independent of the targets. |
| `forr_bundle` (lem-2.1) | The closing paragraph about Lean declarations moves to Appendix G.5, rewritten there inside `forr_validation_scope`. | editorial | The three properties and the paragraph carrying the claim are unchanged. The moved content is preserved: an eventual threshold, $2qk$ against $qk$, and neither the sharper cap nor the explicit threshold in the compiled type. |
| `forr_integer` (claim-N-phi, claim-integer-tests) | An em-dash aside becomes a parenthesis. | editorial | Punctuation only. |
| `upper-tournament-evidence` (r2-quantum-coherent-list-witness) | The sentence on the quantifier order of the Lean list theorem moves to the lead of Appendix G.7. The pointer to the sequential-verification variant is reworded and now points to §5.5. | editorial | The list-witness statement and its quantifier sentences are unchanged. |
| `CAT-thm-1.1` (thm-1.1) | The link label §2.7 becomes Appendix G.2, with the same anchor. | editorial | The anchor `ROOT-EVIDENCE-CONVENTION` now sits in Appendix G.2. |

## Added passages

| Passage | Verdict | Check |
|---|---|---|
| `ROOT-GROWING-K` (§7.3) | new mathematics (QX-003, expert handoff item 2) | See the step-by-step check below. |
| `CL-direct-product-formal` | split from `CL-literature-and-verification`, with the FX026 sentences added | Checked against `lean/QuarticQuery/LowerBound/RealizedCaps.lean`, lines 50–61 and 101–120. `actualComplies` recurses along the observed branch and decrements the cap of the queried instance. `actualCount` is defined separately, and its docstring defers the equivalence to the ordinary proof. The induction sentence supplies that proof. The duplicate "no human review" sentence was dropped, since the appendix introduction states it once. |
| `R3-A-ROUTES` | split from `R3-A-ASSEMBLY` | The text is unchanged. |

### Step-by-step check of §7.3

- **The constant $C_k$.** The expansion of $C_k$ equals `budgetConst_eq_expanded` in `Upper/Bound.lean`. Its coefficients were recomputed from the §5.4 definition: $6\cdot48002\cdot258\cdot40+240=2972284080$, $6\cdot48002\cdot258\cdot4+6\cdot48002\cdot69\cdot42=1131887160$ and $6\cdot48002\cdot69\cdot4000=79491312000$. The term-by-term bound gives $N=5707107503019240<2^{53}=9007199254740992$.
- **The classical bound.** $X<m$. $\ln(4k)\le(1-\ln2)2t$ for $k\le2t/15$ and $t\ge32$, and $18225\cdot(4t^2/225)\cdot2t=648t^3$. $2^{32}\ge648\cdot32^3$, and $2^t/t^3$ increases for $t\ge4$. The steps $L=\lfloor X\rfloor\ge X/2$, $R\ge\lfloor mL/100\rfloor+1>mL/100$ and $200\cdot18225/2=1822500$ follow. The generic bound of §6 holds for every realizing circuit, so both bounds concern one function.
- **The schedule.** With $k=\lfloor\sqrt{t/20}\rfloor$ and $t\ge80$ we get $k\ge2$ and $15k+2\le2t$. The expressions for $A$, $B$ and $4B-A$ were rederived. The map $y\mapsto40y+40x^2/y$ decreases on $(0,x]$, and $40(x-1)+40x^2/(x-1)=80x+40/(x-1)$. Then $80x=2\sqrt{40\ell}$, $3\log_240=15.966$, $\log_21822500=20.798$, $212+20.80-15.96+40=256.84\le257$, $2\cdot257=514$ and $2\cdot28=56$. The cases $4B\le A$ and $\varepsilon\ge4$ are handled. $Q(F_t)\ge1$ because $F_t$ is not constant.
- **Numerical scan.** For $t=80,\dots,19999$ and $t=10^5,10^6,10^8$, the scan finds $2(4B-A)/\ell\le\varepsilon(\ell)$ everywhere, with margin at least $4\cdot10^{-7}$. This is a sample check; the proof is the chain above.
- **Constant mismatch with the companion.** The companion's remark uses the constant 508. The scan confirms that $4-A/B\le\varepsilon_{508}(\ell)$ over the same range, but the chain written here proves 514. The record states the constant it proves. Coordination is noted in the plan.

## Unclaimed passages with mathematical content

| Passage | Change | Verdict and check |
|---|---|---|
| `CL-literature-and-verification` | The Drucker remark is added, and the Lean paragraphs move out to `CL-direct-product-formal`. | Correction. Checked as for `CL-address-guess`. The guessing term becomes $2G(2/3)^r\le2/(100m^8)$ by `claim-numeric`, and the total stays at most $6/100$ since $m^8\ge2$. |
| `forr_proof_spine` | Adds a paragraph on what follows Bansal and Sinha and what departs from them. | Credit. The BS extract supports the cited points: it uses Owen's T for $\Phi-\tfrac12$ (lines 205–209 and 284–294) and bounds level weights from $k$ to $k(k-1)$ (line 427). The identity $\varphi=x\Psi-\Psi'$ is (F10). The GTW antecedent is as in `forr_credit`. No novelty claim is made. |
| `R3-01-ZERO` | Adds a table mapping each example to the convention it tests. | Checked against `R3-01-ZERO`, `-IDENTITY`, `-OR`, `-OFFPROMISE` and `-PARITY`. Every listed value matches. The later-example pointers resolve to the cyclic tournament in §5.2, `CL-adaptive-example` and `CL-conditioning-counterexample`. |
| `R3-01-BRIDGES` | Adds a lead sentence stating the bridge contract, and rewords the closing paragraph. | The contract matches the displayed mass identity: for every $x$ and $\psi$, $T$ controlled phase queries and input-independent gates, with final states not identified. |
| `AC-attribution` | Adds the role of the GPW certificate and the direction of the pointers. | Editorial and credit. The audit corrected the locator "(4.5)–(4.6)" to "the uniqueness argument of §4.2" (regression 1, fixed). The direct-pointer antecedent stays with ABBLSS2015 in the same passage. |
| `ROOT-ARCHITECTURE`, `AC-interface`, `AC-total-unique`, `AC-example-*`, `AC-clean-oracle`, `AC-comparison`, `AC-pointer-support`, `upper-section-interface`, `upper-purpose`, `upper-comparison-law`, `upper-amplification-statement`, `ROOT-PARTIAL`, `R3-01-OFFPROMISE`, `CL-selection-independence-example`, `CL-randomized-contradiction`, `CL-forrelation-input`, `forr_credit`, `forr_ssw_comparison` | Line edits: contrast frames, intensifiers, review-history asides and Lean sentences removed from the body. Removed: the BHMT Theorem 12 aside and the BS v3 line forensics at §6.6, which stay in Appendix E. | Editorial. Each edited sentence was read against the old one: no hypothesis, quantifier or value changed. In `forr_ssw_comparison`, the new lead sentence restates the closing remark of the same passage: the factor $k$ cancels the order-$k/\eta^2$ amplification cost, and $C$ stays unspecified. |
| `ROOT-EVIDENCE-CONVENTION`, `upper-current-formal-scope`, `forr_validation_scope`, `AC-evidence`, `ROOT-EXPONENT-CORRESPONDENCE`, `R3-A-ASSEMBLY`, `history-evidence-convention`, `ROOT-NO-SMALLER`, `forr_historical_closure`, `upper-read-compiler`, `ROOT-CATALOGUE-INTRO` | Moved to Appendix G, retitled, trimmed of chronology, with internal pointers retargeted. Appendix F changed "now" to dated tense. | Editorial. The QX-035 chronology was trimmed. The uniform estimate (F43) is still described as built, axiom-audited and not configured for comparison. |

## Regressions found and fixed

1. **`AC-attribution`.** The first draft cited "the uniqueness lemma (4.5)–(4.6)". (4.5) is the winning condition, so the citation now reads "the uniqueness argument of §4.2".
2. **`ROOT-GROWING-K`.** The first draft said that the lost factor $Q(F_t)^{\varepsilon(\ell)}$ is unbounded. That needs a lower bound on $Q(F_t)$, which the record does not prove. The sentence now says only that the argument gives no bound $R=\Omega(Q^4)$.

## Outside passages, not audited as claim text

The new opening, the route guide, the §4.2 input-length paragraph, the Appendix G introduction and G.1–G.2, the reworked G.4 tables and the "Use of AI tools" section are outside passages.

- **G.4.** The corpus relations in G.4 were read from `corpus/ties.json`. The textual-review entries were read from `round5_statement_fidelity.md`. No status was raised.
- **Input length.** The count $m[m+rkm+2^r((m-1)\ell+rS)]=O_k(m^{22}\ell^3)$ was rederived from the layout table, with $2^r=m^{20}$ and $S=O_k(m\ell^2)$.
- **Bundle imports.** The import sentences were checked against the `import` lines of each Challenge file.

## Second pass: line edit of §§3–7 (3 November 2026)

**Method.** Seven writers, each covering one slice of §§3–7, proposed 501 prose replacements against the pass-one record. A mechanical checker accepted only replacements that keep every math segment, HTML comment, anchor, link target and backtick span byte-identical and in the same order, and that add no em dash.

Five auditors then read every replacement against the old text. None of them wrote any edits. They flagged 40 regressions and 4 style issues. All 44 were replaced by corrected text that restores the meaning, and none was reverted outright. The per-edit record is in [round6_record_lineedit_audit.json](round6_record_lineedit_audit.json): old text, draft, final text, verdict and problem.

The regressions fell into four groups:
- dropped qualifiers ("exact", "directly", "further", "correctly", "independently");
- loss of the word "source", which denotes the Lean source and so carries evidence attribution;
- negations restated as claims that are not equivalent;
- one false sentence: "the simulator sees no target string" (§6.5, `CL-simulator`). The simulator queries those strings; it receives none as side information. Fixed.

The rebind for this pass is [round6_record_rebind_pass2.json](round6_record_rebind_pass2.json): 168 passages moved only, 130 reworded, none added, no claim moved. Of the 130 reworded passages, 86 bear claims. After the corrections, the line edit is editorial in all 86. The audit recorded no regression to any statement, hypothesis, quantifier, constant or attribution in these passages, and no surviving change of evidence status.

| Claim-bearing passages with a corrected edit | Problem the correction removed |
|---|---|
| `forr_coherent`, `forr_small_instance`, `forr_uniform_assembly`, `upper-quantum-tournament`, `upper-padded-tournament-budget`, `upper-decode-cost`, `upper-explicit-log6`, `CL-early-late`, `CL-zero-optional`, `CL-discrepancy` | Evidence or attribution wording: "source", "compiled", "supplied" or "does not yet supply" had been dropped or strengthened. |
| `forr_definition`, `forr_integer`, `forr_circuit`, `forr_final_signs`, `upper-tournament-cost`, `CL-tail-numeric`, `CL-adaptive-example` | A negation or limit had been restated as a claim that is not equivalent, or a scope qualifier had been dropped. |
| `forr_boolean_arithmetic`, `CL-zero-optional` (edit 433) | A cost had been attached to the wrong case ("after" where the text should read "incurs"). |
| `CL-simulator` | The false sentence about side information, described above. |
| `forr_distribution`, `CL-product-law` | Style: a redundant connective, and a duplicated phrase at a line boundary. |

**`ROOT-GROWING-K` (§7.3), constant 508.** This adopts the expert companion's derivation (`round6_plans/expert_to_record_2.md`), checked step by step:
- Since $\ell=40x^2$, we have $40k+\ell/k-80x=(40/k)(k^2-2kx+x^2)=40(x-k)^2/k$.
- Since $k=\lfloor x\rfloor$, we have $0\le x-k<1$, and $k\ge2$, so this is $<20$.
- Since $80x=2\sqrt{40\ell}$, we get $40k+\ell/k\le2\sqrt{40\ell}+20$.
- With the unchanged bounds $3\log_2 40>15.96$ and $\log_2 1822500<20.80$, the sum is $20+212-15.96+20.80=236.84\le237$.
- Then $2\cdot237=474\le508$, so $\varepsilon_{508}(\ell)\ge2(4B-A)/\ell$, and the rest of the argument is unchanged.

The text states 508, to match the companion, and notes that the chain gives 474. The pass-one inequality with 40 is gone.

**Other additions in this pass.** Both were checked arithmetically.
- **`AC-example-tests`:** the board has $4[4+16+4(6+360)]=5936$ input bits. This uses $m=4$, $r=2$, $k=2$, $\ell=2$ and $S=180$, and is consistent with $K=7+2(180+2)=371$.
- **`CL-simulator-example`:** a crosswalk to the exposition. Here $P=a\oplus b$ is total, and rows and columns are labelled from zero; the toy is defined in §6.3 (`CL-tiny-planted-example`).

The concrete-board note proposed for `upper-cyclic-example` was not added. It concerns the exposition's board, and I did not verify its claim that every projection succeeds with probability 0 or 1.
