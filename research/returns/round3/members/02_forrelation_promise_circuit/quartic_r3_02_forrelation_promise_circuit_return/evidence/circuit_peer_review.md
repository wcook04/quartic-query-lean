# Cold-reader review of the replacement §§3.1–3.5

## Scope and verdict

The replacement section was read in full, followed by a second read of the revised inline mathematics, circuit-size proof, examples, transcript paragraph and evidence note. The revised snapshot inspected during the second pass had SHA-256 `3656d6f0d78c08a5dbf41c4e777e0539db08b1eef17bf6154f3db7b1cadabf59`. The author continued editing concurrently; this receipt describes the inspected prose and the specific follow-up points below, not an immutable final release.

**Mathematical verdict: pass for the assigned ordinary proofs, with no change to the promise or circuit theorem required.** The final-sign bounds, constructor count, complete small-instance count, three examples, query-cap distinction and modular-word qualification are all correct. The supplied current-versus-historical evidence wording is appropriately qualified; the receipt counts and axiom claims remain the separate evidence auditor's responsibility.

No section source was edited by this reviewer. No Lean build or Comparator replay was performed.

## 1. Integer normalization and threshold tests

- The denominator has exactly (k+1) square-root factors: two boundary vectors and (k-1) Walsh matrices. Thus (M=2^{t(k+1)}), as stated, on the fixed (k\ge2) domain.
- The comparisons preserve nonstrict equality at both promise thresholds. The denominator is positive and the asymmetric positive yes case is maintained.
- The conclusion (d=b=0) off the promise is correct for this actual output pair, although a generic `CircuitRealises` contract alone would not constrain the off-promise value bit. The section correctly ties the stronger behavior to the concrete output theorem.
- The normalization and threshold conventions are held fixed in the example and throughout the section.

## 2. Quantum preparation and measured law

The ordinary phase construction gives one physical bit query per diagonal and preserves the minus response state. The deferred flag measurement is the same trial preparation, and the pure tensor expansion correctly yields the binomial law. The proof treats the boundary cases (p=0,1) through polynomial factors and specifies (0^0=1).

The two elementary tail estimates are valid:

\[
-qc/2+qp(e-1)\le-qc/16\quad(p\le c/4),
\]

\[
qc/2-qp(1-e^{-1})\le-qc/10\le-qc/16\quad(p\ge c).
\]

The ceiling choice for (q) is the same as the source's natural-number ceiling when (0<\eta<1/2). The retained-state argument keeps every trial and count register; no false clean-ancilla assertion is made. The discussion distinguishes the ordinary (qk) construction from the source compiler's (2qk) formal witness, and does not identify the source isometry with the literal displayed tensor register representation.

Small clarity improvement: define (Q_\eta) explicitly as the minimum worst-case bit-query cap achieving error at most (\eta) on the promise. Section 2.2 explicitly defines only the fixed (1/3)-error (Q); saying that (Q_\eta) is measured in the same model leaves its minimization convention implicit.

## 3. Modular circuit and signed comparisons

The ordinary ideal recurrence has the stated coarse magnitude bounds. Its discussion is correctly kept separate from the actual `Enc` congruence invariant.

For (s=5k), (e=t(k+1)), (w=s+3+e), the three values (A,B,C) obey

\[
|A|,|B|,|C|\le(2^{s+1}+1)M<2^{s+2}M=2^{w-1}.
\]

The final high-bit sign rule therefore applies without overflow ambiguity. The Boolean combination of the signs is exactly the positive comparison and the pair of lower/upper inequalities equivalent to the absolute-value comparison. Equality is accepted correctly. The arithmetic proof does not require signed decoding of all intermediate words.

The full-adder identity, complemented second operand, carry-in, and gate counts (6w,6w+1,6w) match the source constructors. The Walsh cost recurrence accounts for all additions and subtractions in the specified gate basis.

Optional local notation clarification: immediately before the displayed final Boolean tests, explicitly say that `neg(T)` denotes the high bit of the encoded residue of (T), or use the already explained predicate ([T<0]). The mathematical meaning is clear in context but the function name currently first appears in the display.

## 4. Exact constructor count and the coefficient 337

The revised count is correct:

\[
S=6w((k+1)m+5k+t(k+1)+4)
 +(k-1)tm(12w+1)+7.
\]

Here is the independent reconciliation with the source:

1. The exact Walsh recurrence has (\operatorname{whtCost}(w,2t)=tm(12w+1)).
2. Numerator layers cost (1+6wkm+(k-1)tm(12w+1)).
3. The remaining arithmetic costs (6w(m+5k+t(k+1)+4)), plus three constant-true gates used outside the initial layers and three output gates. Those six gates plus the initial layer constant produce the final (+7).

Put (a=k+1). Since (t\ge1),

\[
w=5a-2+at\le6at.
\]

The bracket satisfies

\[
am+at+5k+4\le am+at+5a\le7amt
\]

because (m,t\ge1). Thus its contribution is at most (36at\cdot7amt=252a^2mt^2). Also (w\ge1), so

\[
(k-1)tm(12w+1)\le atm\cdot13w\le78a^2mt^2.
\]

Finally (7\le7a^2mt^2). Summing gives **252 + 78 + 7 = 337**, and (337\le800) gives precisely the existing (200(k+1)^2m(2t)^2) bound. There is no missing shift, comparison, or output-gate term. The explicit statement that this closed form is an ordinary derivation, not a newly compiled theorem, is correct and should remain.

## 5. Examples and census

The displayed (4\times4) Walsh matrix agrees with coordinate order (00,01,10,11), the source's natural integer indexing, and the bit-to-sign convention. For common second block ((-1,1,1,1)), the three first blocks give (N=8,0,-8) exactly. Every bit-block entry, promise value, projection probability, and exact output pair in the table is correct.

The parity proof accounts for all 256 inputs. The signed Walsh rows contribute 64 cases each at (N=4,-4); the other eight second blocks contribute eight times the binomial histogram (1,4,6,4,1). The final histogram (8,96,48,96,8) and census (104,48,104) follow. The explanation of the negative input's quantum answer is valid: with (p=1), all (q) trials succeed and the threshold output is one, while the circuit rejects promise membership.

Wording improvement: replace “the zero values satisfy the no promise” with “the zero values satisfy the zero case of the promise” or “the zero values are zero-inputs.” The present phrase can momentarily suggest absence of a promise.

## 6. Transcripts and evidence wording

The induction proving uniqueness of a consistent transcript is correct. Add constants to the sentence specifying predecessor wires: “Each new gate reads input wires, constants, or earlier gates.” The source includes constant-false predecessor wires and explicitly generated true gates.

The evidence note correctly distinguishes:

- current integrated source from historical returned candidate files;
- inspected prior native passes from execution performed in this review;
- ordinary mathematical arguments from exact Lean exported types;
- endpoint circuit correctness from the absent register-by-register signed correspondence;
- the compiled generic physical cap from the tighter unassembled formal cap;
- the full current Lemma 2.1 conjunction from the old baseline's claim that no conjunction existed.

The reviewer did not independently recompute the “124 files” root-receipt assertion or the principal-declaration axiom audit. Those specific facts need the parallel evidence audit and its source-bound references. They are phrased as supplied records rather than newly replayed validation, which is appropriate.

## 7. Rendering and citation cleanup

The initial draft had bare parentheses instead of inline math delimiters and several missing command backslashes. This was reported immediately. The second pass confirmed that the inline mathematical expressions, including (\Phi,\delta,\Pi,\psi,\mathcal L,\lceil k/2\rceil\), were restored and that the circuit-size revision was sound.

The broad delimiter conversion introduced one remaining bibliography formatting defect in the inspected revision: `**47**$3$` should be `**47**(3)` for the journal volume and issue. Restore ordinary equation labels `(3)–(5)` in the OpenAI reference if retaining the source's numbering style. These are formatting corrections, not mathematical or bibliographic-authority changes.

No new figure or rendered PDF was inspected in this cold-read pass; the deliverable reviewed is Markdown source.
