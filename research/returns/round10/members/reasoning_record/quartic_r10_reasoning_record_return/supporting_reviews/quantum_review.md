# Quantum specialist reread

This was the **first informed specialist perspective**, performed after the primary chronological pass was frozen. Independent source research preceded the current reading. It is not a cold pass. The exact current reading and formal-source limits are recorded in `quantum_scopes_read.json`; external editions, passages, and web retrievals are in `quantum_sources.json`. No manuscript was edited and no Lean or Comparator build was run. The expert companion and exposition were not opened during this specialist pass.

## Result and mathematical boundary

The three candidates below are concrete organizational repairs. I found no defensible mathematical-error label in the inspected quantum chain. This is a scoped review conclusion, not a certification of the whole manuscript or formal development.

The substantive reconstruction checked the following links:

- **Oracle and decoder.** The controlled phase oracle in §2 retains the response-bit control, so its one-query equivalence to the bit oracle is valid. The direct Forrelation circuit uses one phase-kickback bit query per diagonal, yielding amplitude Φ and projection probability Φ². The repetitions in §3.3 use a multiplicative moment bound, so the stated δ⁻² dependence is derived rather than borrowed from the separate linear-in-Φ interference experiment. The output threshold includes equality, and the displayed moment bounds apply to both tails. Fresh trial registers and retained history give an invertible preparation with an all-input cap.
- **Exact verification.** Transcript consistency identifies the unique circuit evaluation by topological induction, including on unpromised inputs. The separate domain-output test is essential for soundness there. Pointer lookups charge their individual address bits and one selected target bit; adaptive depth and complete coordinate support are explicitly distinguished. The arbitrary-index evaluator retains its workspace, and the stronger clean evaluator is justified only because each local output is exact.
- **Comparison.** The sorted unordered-pair circuit is the source of complementarity; separate independently designed ordered calls would not suffice. The retained decoded labels make the pointer calculation block diagonal, justifying its mixture law. The true winner cannot be disqualified by any rival label, and at its correct own label disqualifies the rival. Only the winner's decoder correctness enters the numerical dominance bound.
- **Capped amplification.** The two-dimensional calculation preserves the full normalized good vector. The mixture of zero Grover iterations and a uniform bounded iteration count covers both high and low success probabilities. A fixed number of fresh trials provides a cap even at zero success probability. The coherent controlled-iterate identity uses unconditional preparation and inverse calls and controls fixed reflections; the designated returned register factors from successful history records.
- **Weighted sampling and coupling.** Conditional on the candidate index, fresh comparison registers yield the product weight. Orthogonal candidate labels give total success W/m and exact conditional law w_i/W. Complementarity gives the displayed drift identity. The lower bound on the dominant weight is used only before that vertex appears. The coupling is conditioned on the entire agreed history, permits history-dependent stop probabilities, and stops charging failures after selection.
- **Total decision and budget.** Verification samples and fixes a fresh address, so every candidate/address search has exact local predicates. A nonwinner fails a test at every address; a winner passes at its true address. Conditioning on the completed tournament transcript preserves the fresh-verifier guarantees. The physical finite budget includes comparison recomputation, the inverse calls, trial padding, address decoding, and local-test search. The deliberately enlarged logarithmic exponent six follows from that budget; no optimization claim is needed.

The relevant primary authorities were actually read at bounded passages: Aaronson–Ambainis arXiv v1 §3.2; Bansal–Sinha full-version propositions and threshold definitions; BHMT arXiv v1 §2; BBHT arXiv v1 §4; the full supplied Høyer–Mosca–de Wolf extraction; Dürr–Høyer arXiv v2; the relevant pointer-function arguments; and the supplied source preprint §§1–3. Source-side notes also examine two outside-annex primary works without using their stronger oracle promises as a proof of the fractional-weight theorem.

## Formal-source checks

I read actual local signatures for `QLe`, `Samples.amplify`, `uniformOpaqueAmplifier`, `quantumTournament`, the full local-test/support wrapper, and the complete Lemma 2.1 wrapper. The checks support the manuscript's separation between a measured-label law, a retained abstract factor, a compiled continuation, and a complete finite list law. The `quantumTournament` type chooses its law before the input and dominant vertex and includes both the normalized law and the cap. The supplied local subset did not contain `Upper/Compile.lean`, `Upper/Tournament.lean`, `Upper/Bound.lean`, or `Paper/QuantumComparison.lean`; those bodies were not silently treated as read. Nor was the historical execution evidence in Appendix G replaced by a fresh execution claim.

## Candidates

### Q-01: organization / algorithm orientation

**Location:** §5 opening, before §5.1; source lines 2063–2069. **Priority:** medium. **Confidence:** high.

> The algorithm first produces a short list that is likely to contain the winning column and then checks each listed column.

**What the reader has just received.** The opening imports the circuit, decoder, local-test count, and all-input cap from §§3–4 and states the target upper bound. It then gives a conceptual two-stage summary and a link-based reading route. The executable stopping and acceptance rules arrive separately at lines 2443 and 2599–2616, after the detailed amplifier and ideal tournament.

**Reader consequence.** The conceptual overview does not yet give a reader one complete program whose correctness the subroutine proofs are serving. In particular, amplification failure has opposite meanings in list generation and certificate checking. A chronological reader carries this unresolved control flow through the long state and drift calculations. This is an orientation issue, not an absent mathematical proof: lines 2610–2616 eventually explain the two meanings explicitly.

**Concrete repair.** Insert one short whole-algorithm block at the end of the §5 opening, using named subroutines whose contracts are proved below. State the fixed T-stage horizon; keep only the classical pivot list between stages; on stage-sampler failure return the current list; decode each listed column afresh and fix that measured address; search for a failed exact local test; output one at the first candidate for which that search reports failure, otherwise zero. Identify both amplification calls by (gamma,eta), namely (1/(2m),epsilon) and (1/K,epsilon). Use the block to replace, rather than add to, the later duplicated control-flow summary.

**Why this repair helps.** This makes the acceptance event and the all-input stopping rule visible before their quantitative analysis. It also makes clear why neither the ideal weights nor an accurate address for every rival is an algorithmic input.

**Source comparison and limits.**

- OpenAI, preprint dated 5 October 2026, §3.2 Proposition 3.2 and §3.3 Proposition 3.3, supplied PDF pp. 8–10. Mathematical authority for the actual list-generation and final-verification steps; not evidence that current prose is incorrect.
- [Mande–Paraashar–Saurabh, FSTTCS 2023 published edition, quantum proof overview pp. 30:3–30:4; §4 Algorithm 4 and Theorem 19, pp. 30:11–30:13](https://doi.org/10.4230/LIPIcs.FSTTCS.2023.30). Writing comparison: relate the stored history, sampler contract, main loop, and query accounting. Its exact-edge theorem is not being transferred.
- [Ambainis, Understanding Quantum Algorithms via Query Complexity, arXiv:1712.06349v1, §5.1, pp. 12–13](https://arxiv.org/abs/1712.06349v1). Writing comparison: the address-finding and certificate-verification stages are explained as separate computational tasks.

### Q-02: organization / notation at a proof bridge

**Location:** §5.2, amplified stage law before the coupling; source lines 2443–2467. **Priority:** medium. **Confidence:** high.

> The compiled version rests on a finite-label statement.

**What the reader has just received.** Lines 2355–2380 derive the full tensor preparation and the exact successful-index law. Lines 2443–2445 give the real stopping rule and explain why amplification preserves that law. The next mathematical task is the history-conditioned coupling at line 2465.

**Reader consequence.** At precisely this transition, the Correspondence note introduces another label b, an input-indexed mass q_x(b), its total q_x, and f_x, as well as the measured/reset formal implementation. The coupling immediately changes back to a list L, weights w_i, total W, and f(L). The mathematical transition is correct but the reader must translate away an intermediate notation and a formal-evidence detour before seeing the transition kernel used by the coupling.

**Concrete repair.** At this location display the real transition kernel directly in the current-history notation: Pr[stop | L]=f(L), and Pr[next pivot=i | L]=(1-f(L))w_i(L)/W(L) when W(L)>0; when W(L)=0, f(L)=1. State f(L)<=epsilon only at the histories for which W(L)/m>=1/(2m). Then proceed to the coupling. Move the generic q_x(b) measured/reset discussion and its declaration-link distinctions to Appendix G.7, leaving one precise link here. Preserve the separate full-successful-state proof in §5.1.

**Why this repair helps.** The proposed display is the exact quantity from which the coupling constructs its two marginals, so it reduces a genuine notation change while preserving the distinction between the ordinary retained-state proof and the compiled measured-label route. It neither strengthens the sampler guarantee to all histories nor assumes independent stage failures.

**Source comparison and limits.**

- OpenAI, preprint dated 5 October 2026, proof of Proposition 3.2, equation (15) and the following sampling/coupling argument, supplied PDF pp. 9–10. The exact successful conditional law is the mathematical fact being connected to the ideal process.
- [Brassard–Høyer–Mosca–Tapp, arXiv:quant-ph/0005055v1, §2 Lemma 1 and equation (8), printed pp. 5–7](https://arxiv.org/abs/quant-ph/0005055v1). Supports preserving the whole normalized good component, from which the measured kernel follows; not a source for the fixed cap.
- [Childs, Lecture Notes on Quantum Algorithms, supplied edition dated 17 April 2025, §§19.1–19.3, printed pp. 87–89 (PDF pp. 95–97)](https://www.cs.umd.edu/~amchilds/qa/qa.pdf). Writing comparison: keep the mathematical search statement and the implementation/accounting task identifiable. Edition fixed by supplied hash in quantum_sources.json.

### Q-03: organization / example identity

**Location:** §4.4, finite local-test example; source lines 1928–1945. **Priority:** low-to-medium. **Confidence:** high.

> Its board uses Forrelation values $\Phi=+1$ and $-1$

**What the reader has just received.** §4.3 has specified a complete four-column board using Phi=+1/2, 0, and -1/2, with an explicit fill rule. §4.4 has derived the test list and soundness. Before applying its 371-test count to that board, line 1928 introduces the examples-first exposition and a second pair of nonzero Forrelation values; line 1930 directs an incoming reader back to that other account.

**Reader consequence.** The second board is introduced in the middle of a single worked example in the lead account. The phrase four-column board at lines 1932–1939 then requires the reader to recover whether it denotes the board just defined in §4.3 or the companion board mentioned immediately before it. The text correctly warns that decoder laws differ, but that warning creates an avoidable board-identification task for someone reading only this document.

**Concrete repair.** Let the local-test calculation continue directly from the named board of §4.3, explicitly calling it the §4.3 board. Move the alternate-board and return-to-exposition notice after the completed example, label it as a companion cross-reference, and state there that only the finite circuit and gate numbering are shared. Keep the Phi-dependent decoder laws tied to each separately named board. No numerical change to the 371 tests, 5936 input bits, or failed-test counts is proposed.

**Why this repair helps.** A worked example is most useful when the same concrete input persists across representation, local tests, and search probabilities. Stable naming prevents a source-convention warning from interrupting that chain or making accurate counts appear to apply to an unspecified board.

**Source comparison and limits.**

- [Ambainis, Understanding Quantum Algorithms via Query Complexity, arXiv:1712.06349v1, §4, pp. 9–12](https://arxiv.org/abs/1712.06349v1). Writing comparison: a fixed pointer representation is introduced before its acceptance conditions, certificate, and search roles. This supports stable example identity, not a mathematical criticism of either board.

The expert companion and exposition were not opened. This finding concerns the extra cross-document board introduced inside the lead account, and makes no claim about the correctness or quality of either other manuscript.

## Handoff

The lead-specialist reread ended before the classical specialist began. The candidate file is intentionally separate from the frozen primary observations: root should match each candidate to those units and merge duplicates rather than relabel this informed reread as an independent cold response. A later historical cross-document audit, if assigned, is a separate activity and will have its own scope record.
