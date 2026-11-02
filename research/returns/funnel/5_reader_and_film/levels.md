# Why the optimal query exponent is four

**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

These are proposed reader texts for the supplied snapshot. The presenter scripts use the same construction. Source abbreviations and primary references are in `sources.md`; exact passage bindings are in `correspondence.json`.

## One sentence

<!-- passage:L1-sentence -->
A four-column picture of one all-one column pointing to zeros in its rivals illustrates OpenAI’s new construction of total Boolean functions, which proves that the optimal universal exponent relating randomized and quantum bit queries, with worst-case error at most one third, is four and refutes the cubic conjecture.

Source: OpenAI, Theorem 1.1, §2.2 and §3.3; `thm-1.1`, `cor-cubic-refuted`, `def-F`, `claim-winner-dominates`.
<!-- /passage:L1-sentence -->

## One paragraph

<!-- passage:L2-paragraph -->
Consider four columns whose bit strings are \(1111,1101,1011,1110\), with positions read from top to bottom. The first column can win if its correctly addressed certificate points to the displayed zero in each rival and certifies every answer used in its address. This illustrates OpenAI’s construction proving that the optimal universal exponent relating bounded-error randomized and quantum queries is four. A quantum procedure cheaply compares two columns: the winner’s correct pointer disqualifies its opponent, and no pointer can find a zero in the winner’s all-one string. Comparisons between losing columns may behave arbitrarily. A probabilistic tournament finds a short candidate list, after which quantum search checks the certificates. The randomized lower bound uses separate certificate arrays and a hidden winning column; reaching the relevant cell requires learning or guessing a vector of hard partial-function answers. For each fixed integer \(k\ge2\), the family has quantum cost at most \(C_k\sqrt m(\log_2m)^{b_k}\) and randomized cost at least \(c_km^{2-1/k}/(\log_2m)^2\) for sufficiently large powers of four \(m\). Choosing \(k\) before letting \(m\) grow rules out every universal exponent below four. Together with the earlier quartic upper bound of Aaronson, Ben-David, Kothari, Rao and Tal, this settles the exponent. These are worst-case bit-query bounds; the four-column picture illustrates the definition, and the theorem makes no claim about its running time.

Source: OpenAI, §§2–5 and Theorem A.1; ABKRT, Theorem 2. The literal four-column instance is specified in `visual_data.json` and proposed as `reader-example-instance` in `NEW_STATEMENTS.json`.
<!-- /passage:L2-paragraph -->

## One page

<!-- passage:L3-example -->
Consider four strings \(1111,1101,1011,1110\). The first column’s certificate points to the displayed zero in each rival, while its own all-one string prevents any incoming pointer from finding a zero. This illustrates OpenAI’s construction proving that the optimal universal exponent relating randomized and quantum query complexity is four, refuting the conjectured cubic relation. [OpenAI, Theorem 1.1, §2.2; ABKRT, Conjecture 2.]
<!-- /passage:L3-example -->

<!-- passage:L3-address -->
Each column has a separate array of certificate cells. The correct address is a vector of Forrelation answers, each defined only on a specified promise. A column wins when its address answers are all defined, the cell at that address contains correct circuit transcripts and pointers to zeros in every rival, and its own string is all ones. The total function asks whether a winner exists, assigning an answer to every input bit string. [OpenAI, Lemma 2.1, §2.2.]
<!-- /passage:L3-address -->

<!-- passage:L3-quantum -->
A quantum comparison produces proposed addresses for two columns and reads the pointers between them. A winner defeats its opponent whenever its own address is decoded correctly, even when the opponent’s Forrelation inputs fall outside their promises. Finding a short candidate list is harder: losing columns need not have a consistent order. The tournament samples using products of actual comparison probabilities. Amplitude amplification preserves this sampling law; a shrinking total weight bounds the chance of missing the winner. Quantum search then checks the listed certificates. [OpenAI, Lemma 3.1, Proposition 3.2, §3.3.]
<!-- /passage:L3-quantum -->

<!-- passage:L3-classical -->
For the classical bound, start with one hidden zero in every column and blank cells. Erase a uniformly chosen column’s zero and fill its correct cell. Until a query reaches either change, the two inputs give identical answers. Separate arrays make addressing many possible winners expensive. A capped direct-product argument bounds adaptive address guesses by stopping a simulator before its budget is exceeded. It bounds a joint event, avoiding conditioning that could alter the independent hard-input distribution. [OpenAI, Lemma 4.1, §4.2, (18), (21), (22).]
<!-- /passage:L3-classical -->

<!-- passage:L3-bounds -->
Write \(R(f)\) and \(Q(f)\) for minimum worst-case bit queries, allowing error at most \(1/3\) on every input; computation between queries is unrestricted. For every fixed integer \(k\ge2\), there are positive constants \(c_k,C_k,b_k\) and total functions \(F_{k,m}\), for all sufficiently large powers of four \(m\), satisfying

\[
Q(F_{k,m})\le C_k\sqrt m(\log_2m)^{b_k},\qquad
R(F_{k,m})\ge c_k\frac{m^{2-1/k}}{(\log_2m)^2}.
\]

Given a proposed exponent \(0\le\alpha<4\), choose \(k\) with \(2-1/k>\alpha/2\), then increase \(m\). The ratio \(R(F_{k,m})/(1+Q(F_{k,m}))^\alpha\) becomes arbitrarily large. Aaronson, Ben-David, Kothari, Rao and Tal proved the universal quartic upper bound, so the optimal exponent is exactly four. The construction supplies exponents approaching four as fixed \(k\) varies; it does not establish an exact fourth-power separation for one fixed member-family. [OpenAI, (1), (2), §5, Theorem A.1; ABKRT, Theorem 2.]
<!-- /passage:L3-bounds -->

<!-- passage:L3-evidence -->
The supplied development reports an unconditional Lean proof of Theorem 1.1, with several alternative proof routes. Its local Comparator rehearsals and AI fidelity reviews are recorded separately. Original run receipts are absent from the supplied archive; no builds were reproduced here and no human review is reported. [Repository README; Results/Unconditional.lean; current statements.json; fidelity review, findings 3–7.]
<!-- /passage:L3-evidence -->

## Argument map

<!-- passage:L4-map -->
Keep the same column 0 and its three outward pointers in view. Begin at the definition of a winner, then follow two branches: the quantum comparison and verification bound, and the randomized planted-input bound. They meet at the family bounds, which combine with the earlier universal quartic bound to give the optimal exponent. The new work is the total-function family and its analyses; the reusable comparison argument tolerates arbitrary probabilities between losing columns. [OpenAI, §§2–5.]

`argument_map.json` is the complete map data. Its node identifiers are existing corpus statement identifiers. It retains each source evidence object, marks the difficult steps, explains every support edge, and gives a reading order. Source definitions and hypotheses remain visible even when they have no reviewed tie. The displayed route must distinguish paper support from the compiled declaration dependencies.

The first useful branch is `def-F` → `claim-winner-dominates` → `prop-3.2` and certificate verification → `prop-3.3`. The second is the coupled inputs and capped direct product → `prop-4.2`. The two bounds meet at `eq-2`; `claim-exponent-ratio` and `thm-A.1` lead to `thm-1.1`. These are compressed reading directions with intermediate assumptions available on expansion, not claims of direct Lean dependency.
<!-- /passage:L4-map -->

## Reading route

<!-- passage:L5-route -->
Return to the four strings \(1111,1101,1011,1110\). Read §2.2 until you can state every condition under which column 0 wins. Use that object to follow the two analyses below, and return to Theorem 1.1 after their bounds are available. This order places the new construction before its quantum implementation and makes clear how it improves the randomized-versus-quantum separation. [OpenAI, §§1.2, 2.2, 3, 4, 5.]

| Step | Location | Question to answer | Retain |
| --- | --- | --- | --- |
| 1 | §2.2; Figure 1; Lemma 2.2 | Which input bits make column 0 a winner? | A true-address cell certifies its address and points to a zero in every rival. |
| 2 | §1; Theorem 1.1; equation (2) | What must the two analyses prove? | The quantum upper bound grows as sqrt(m) times logarithms; the classical lower bound grows as m^(2-1/k) divided by logarithms. |
| 3 | §2.1; Lemma 2.1 statement | What properties are needed from Forrelation? | Classical hardness, quantum decoding and a small exact circuit have distinct jobs. |
| 4 | §3.3, through the winner comparison | Why do incorrect addresses in rivals cause no difficulty for a genuine winner? | No incoming pointer can find a zero in an all-one column. |
| 5 | §3.2; equations (10)–(15); §3.1 | How is a useful list sampled when losing comparisons are arbitrary? | Weights multiply by actual comparison probabilities; complementarity reduces expected total weight to at most half. |
| 6 | §3.3; verification; Proposition 3.3 | How does the list become a correct total-function algorithm? | Search for a failing test at the decoded address; every false candidate has a failed test. |
| 7 | §4.2 through equation (18) | Where can a query distinguish a planted winner from the blank input? | Only the erased zero and the planted cell differ. |
| 8 | §4.1; Lemma 4.1; §4.2 equations (19)–(23) | Why does adaptivity not make an unlearned address easy to guess? | The capped simulator bounds the joint event without conditioning on being nonheavy. |
| 9 | §5; Theorem 1.1 | How do these bounds rule out every exponent below four? | Choose k from alpha first; then let m tend to infinity. |
| 10 | Appendix A; Theorem A.1 | What is the independently known universal upper bound? | R <= D = O((1+Q)^4) for total Boolean functions. |
| 11 | Optional formal supplement: lower-bound blueprint and review | How was the paper’s external Forrelation hypothesis discharged? | A separate fixed-k proof establishes the precise weaker lower bound this construction uses. |
<!-- /passage:L5-route -->

## What to explain and what to recall

<!-- passage:L6-detail-choices -->
These are editorial choices for the stated audience, with the reason for each. The film spends more time on the concrete input than the expert synopsis does.

| Topic | Choice | Reason |
| --- | --- | --- |
| Decision trees and standard error reduction | Recall the query model once; link the routine details. | The stated audience has graduate-level query-complexity background. Re-teaching these tools would obscure the construction. |
| The certificate cell and its address | Work through the same cell, its Forrelation answers, pointers and gate checks. | Confusing the proposed address with a verified certificate erases the totality argument. |
| The comparison with an off-promise rival | Show both pointer directions explicitly. | This invariant is the reason the probabilistic tournament applies to every input. |
| Fractional tournament weights | Show one exact symbolic pivot update, then the drift identity. | Sorting and fixed-tournament intuitions are misleading; complementarity is the condition actually used. |
| Amplitude amplification | Assume its square-root scaling; explain preservation of the conditional law and branch cap. | Those two properties carry this argument; a full trigonometric derivation belongs in the linked Lemma 3.1. |
| Adaptive address guessing | Explain the capped simulator and the joint event. | Conditioning directly on being nonheavy could change the distribution; fluent independence language would hide the hard step. |
| Finite witness versus asymptotics | Mark m=4 as a construction example; retain k and logarithms in the general bound. | For the example L=0. It supplies no measured speedup or classical lower bound. |
| Earlier upper bound and the new lower construction | Attribute the upper bound at its use and place prior constructions in a short source note. | Formalization and exposition do not transfer mathematical priority. |
<!-- /passage:L6-detail-choices -->

## One example at every depth

<!-- passage:L7-worked-example -->
The example uses the actual parameters k=2, t=1, m=4, r=40 and two-bit pointers. Each column has 2^40 cells, represented by a labelled ellipsis and one selected cell. The forty address answers are (1,0,…,0). The full matrices and exact signed inputs are in `visual_data.json`; the transcript is the evaluation of the supplied circuit, not invented gate values. The example exercises the definition only. Its L is zero. The quantum-versus-classical theorem applies as m grows with k fixed.

The mathematical claim about the illustrative instance is separately proposed for Lean. Existing endpoint theorems do not give this newly authored example a new checked status automatically. The film keeps actual comparison probabilities symbolic.
<!-- /passage:L7-worked-example -->
