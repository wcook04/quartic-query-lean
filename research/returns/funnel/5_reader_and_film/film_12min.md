# 12-minute film: The nearly quartic separation

**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

Production design, supplied-snapshot scope. The spoken text is a draft for Will Cook; the mathematical result is credited to OpenAI. Exact data, captions and corpus identifiers below are production instructions. A caption showing a source status reports the supplied corpus; this return does not rerun Lean or Comparator. Mathematical fact, source report and proposed finite calculation remain distinguishable.

The example uses 0-based indices throughout, matching Lean's `Fin`; the preprint uses 1-based indices. Convert every visible index together if the production chooses the preprint convention. Never switch conventions within a shot. The actual family parameters are k=2, t=1, m=4, ℓ=2, r=40. At this size L=0, so the asymptotic lower-bound theorem supplies no lower bound for the example. Use the same four columns for all scenes, with a labelled change to the general hard distribution when the proof requires it.

One fixed supplied circuit C=QuarticQuery.Forrelation.forrCircuit 1 1 is used throughout; its first argument is k−1. Its actual evaluation transcripts are circuitEval C (A_{i,h}). The exact gate numbering is determined by that definition, although this film design does not materialize the transcript bit strings or its numerical size. Pointer bit encodings are `pointerEquiv 2` inverse images of the displayed row targets, with no unverified integer endianness assumption. All unspecified cell bits are false.

The exact finite computations are proposed new statements, not new separation mathematics. They belong in NEW_STATEMENTS.json and remain pending Lean evidence. The film's displayed asymptotic claims use the existing corpus rows, with all quantifiers retained in captions.

## Timing

These are planned edit windows. The word counts leave room for the indicated diagrams and pauses; no recorded presenter performance is claimed.

| Shot | Window | Spoken words | Words per minute if continuous |
| --- | --- | ---: | ---: |

| film12_s01 | 00:00–00:45 | 102 | 136.0 |

| film12_s02 | 00:45–01:30 | 92 | 122.7 |

| film12_s03 | 01:30–02:30 | 137 | 137.0 |

| film12_s04 | 02:30–03:20 | 104 | 124.8 |

| film12_s05 | 03:20–04:10 | 106 | 127.2 |

| film12_s06 | 04:10–05:00 | 101 | 121.2 |

| film12_s07 | 05:00–06:05 | 132 | 121.8 |

| film12_s08 | 06:05–07:00 | 113 | 123.3 |

| film12_s09 | 07:00–07:45 | 98 | 130.7 |

| film12_s10 | 07:45–08:35 | 109 | 130.8 |

| film12_s11 | 08:35–09:45 | 145 | 124.3 |

| film12_s12 | 09:45–10:35 | 107 | 128.4 |

| film12_s13 | 10:35–11:25 | 119 | 142.8 |

| film12_s14 | 11:25–12:00 | 69 | 118.3 |

Total planned duration: 720 seconds. Total spoken words: 1534.

Sources and exact editions: `sources.md`. Shared exact data: `visual_data.json`. Each spoken passage and picture has a separate correspondence anchor.

## 00:00–00:45 | Four columns and the result

**Spoken**

<!-- passage:film12_s01 -->
Here are four columns of bits. The left column is all ones, and it points to a zero in each of the others. We will follow this example through a theorem of OpenAI: the optimal universal power relating randomized and quantum queries for total Boolean functions is four. For each fixed k at least two, their construction gives separation power four minus two over k, with logarithmic factors. The problem is to find and check this winning column when the useful pointers sit in a cell whose address must itself be computed. Those outward pointers will explain why the quantum search works.
<!-- /passage:film12_s01 -->

**Picture and exact data**

<!-- passage:film12_s01_picture -->
Presenter beside the same four-column diagram used throughout. Columns and rows are numbered 0,1,2,3. Display X by columns as X_0=(1,1,1,1), X_1=(1,1,0,1), X_2=(1,0,1,1), X_3=(1,1,1,0). Arrows start at B_{0,s} and end at (column,row)=(1,2),(2,1),(3,3). Put ‘m=4, construction example’ under the matrix. Show ‘Optimal universal exponent: α_tot=4’ and ‘OpenAI, Theorem 1.1, 5 October 2026’. Do not label the example itself a speedup.
<!-- /passage:film12_s01_picture -->

**Corpus statements:** `thm-1.1`, `eq-2`, `def-winner`, `eq-8`, `def-F`.

**Proposed finite statements:** `reader-forrelation-yes`, `reader-forrelation-zero`, `reader-example-instance`.

## 00:45–01:30 | What a query costs

**Spoken**

<!-- passage:film12_s02 -->
A query asks for one input bit. A randomized algorithm chooses where to look using previous answers and random choices. A quantum algorithm uses the bit oracle shown here, with a register that may be in superposition. The oracle changes the answer bit according to the selected input bit; a measurement does not hand us a list of every answer. Both algorithms must succeed with probability at least two thirds on every input. We count the largest number of queries on any branch. All computation between queries is free in this model.
<!-- /passage:film12_s02 -->

**Picture and exact data**

<!-- passage:film12_s02_picture -->
Keep the matrix ghosted behind an input-address register and an answer register. Highlight one classical bit query. Then display O_x|i,b,z⟩=|i,b⊕x_i,z⟩, with labels ‘bit position’, ‘answer bit’, ‘workspace’. Show success ≥2/3 for every input, and ‘cost = worst branch query count’. Put R(f) under randomized queries and Q(f) under quantum queries. Do not animate an oracle returning all bits or draw elapsed-time axes.
<!-- /passage:film12_s02_picture -->

**Corpus statements:** `def-R`, `def-Q`, `def-query-oracle`.

## 01:30–02:30 | An exact address bit

**Spoken**

<!-- passage:film12_s03 -->
To compute an address bit we use Forrelation, studied by Aaronson and Ambainis. For our small example, take these two rows of signs. A bit zero means plus one, and a bit one means minus one. Multiply the second row by the displayed Walsh matrix, take its inner product with the first, and divide by eight. The first pair gives one; changing the second row as shown gives zero. The rule assigns answer one at or above one over a thousand and twenty-four, and answer zero when the absolute value is at most one over two thousand and forty-eight. Other inputs can fall outside the promise. The associated quantum test succeeds with probability phi squared. Repetition estimates that probability using few queries for fixed k. Bansal and Sinha proved the classical lower bound used by the preprint.
<!-- /passage:film12_s03 -->

**Picture and exact data**

<!-- passage:film12_s03_picture -->
Use exact static data W=[[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]], z_1=(1,1,1,-1), z_2^+=(1,1,1,-1), z_2^0=(1,1,-1,1). Display Wz_2^+=(2,2,2,-2), Wz_2^0=(2,-2,2,2); z_1^T Wz_2^+=8, z_1^T Wz_2^0=0; Φ=N/8. Under each pair show physical bit strings ‘0001 | 0001’ and ‘0001 | 0010’, with Φ=1,P=1 and Φ=0,P=0. Show thresholds δ=2^-10=1/1024 and δ/2=1/2048. Briefly show the exact quantum test: prepare u=(1,1,1,1)/2, apply D_z2 then H=W/2 then D_z1, and project onto u; success probability Φ². This uses the same two sign vectors, with no observation of all entries at once. Label k=2,t=1,m=4. Source cards: preprint §2.1, (3)–(5); Aaronson–Ambainis, §1.1.1 and §1.1.3 of the author-hosted paper; Bansal–Sinha Theorem 1.3 and Corollary 1.4. Do not give a classical lower bound for m=4.
<!-- /passage:film12_s03_picture -->

**Corpus statements:** `def-walsh-sign`, `eq-3`, `eq-4`, `claim-N-phi`, `claim-integer-tests`, `claim-proj-prob`, `lem-2.1.i`, `lem-2.1.ii`.

**Proposed finite statements:** `reader-forrelation-yes`, `reader-forrelation-zero`, `reader-walsh-example`.

## 02:30–03:20 | The address selects one cell

**Spoken**

<!-- passage:film12_s04 -->
Each column has forty of these eight-bit inputs. In our example, the first has answer one and the other thirty-nine have answer zero. Together they specify this forty-bit address. Every column has its own array of two to the forty cells, so the same address selects a different cell in each column. We display one cell and leave the rest compressed. Inside the selected cell are the pointers and proposed gate values for forty runs of one circuit, one per address answer. This circuit also checks that each Forrelation input lies inside its promise. The address cannot be justified by a confident-looking answer alone.
<!-- /passage:film12_s04 -->

**Picture and exact data**

<!-- passage:film12_s04_picture -->
For every column i, A_{i,0}=A^+ and A_{i,h}=A^0 for 1≤h<40, using shot 3's exact blocks. Show s=(1,0,…,0)∈{0,1}^40 as a tuple, with first entry labelled h=0 and ‘39 zeros’ beneath the remainder. Each of the four separate cell arrays is labelled ‘2^40 cells’; zoom only B_{0,s}. Display three decoded pointer targets 2,1,3 and forty transcript slots tr_0,…,tr_39. Use the fixed supplied circuit C=QuarticQuery.Forrelation.forrCircuit 1 1, which realises P_{2,4}; the winning cell contains the gate evaluations circuitEval C (A_{0,h}). Do not invent gate numbers, transcript bit strings, or a numerical circuit size. A cell at the same address in column 1 remains a different physical input block.
<!-- /passage:film12_s04_picture -->

**Corpus statements:** `eq-6`, `def-column-layout`, `eq-7`, `def-transcript`, `lem-2.1.iii`.

**Proposed finite statements:** `reader-example-parameters`, `reader-example-instance`.

## 03:20–04:10 | The winner conditions are local

**Spoken**

<!-- passage:film12_s05 -->
A transcript can be checked gate by gate. Read the alleged gate value and its two predecessors, then check the gate's rule. Input predecessors come from the actual input. Two further checks demand a defined answer and agreement with the address bit. Together with the all-one column and outward pointers, these checks characterise a winner. This makes the final problem total: malformed transcripts, incorrect addresses and inputs outside the Forrelation promise still have a definite yes-or-no answer. Our left column satisfies every condition. There cannot be a second winner, because its pointer from the first would have to land on a zero in an all-one column.
<!-- /passage:film12_s05 -->

**Picture and exact data**

<!-- passage:film12_s05_picture -->
Show one generic fan-in-two gate with inputs u,v and claimed output c; display ‘pass iff c=gate(u,v)’ and label it ‘generic gate of the chosen circuit C’. No invented AND gate is presented as a gate of C. Reveal categories: 4 all-one tests, 3 pointer tests, 40S gate tests, 80 output tests. If displaying their sum, use K=4+3+40(S+2). For a proposed address the output tests read d=1 and b=s_h. Restore the full four-column diagram and the three valid pointer endpoints. Cross out the possibility of a second all-one winner using the zero endpoint in its column.
<!-- /passage:film12_s05_picture -->

**Corpus statements:** `def-eval-transcript`, `lem-2.2.i`, `lem-2.2.ii`, `def-K`, `def-winner`, `def-F`, `cor-unique-winner`.

**Proposed finite statements:** `reader-example-parameters`, `reader-example-instance`.

## 04:10–05:00 | A winner defeats every opponent

**Spoken**

<!-- passage:film12_s06 -->
Compare the left column with column two. Decode an address in each, then follow each proposed pointer towards the other column. When the winner's address is right, its pointer finds this zero. Any pointer back lands on a one, because the winner is all ones. That protection survives an incorrect decoded address in the other column, including an address produced from an input outside the promise. So the winner defeats each opponent with high probability. Comparisons between two losing columns can behave arbitrarily. We therefore need a search method that tolerates uncertain comparisons and assumes no consistent ordering among the losers.
<!-- /passage:film12_s06 -->

**Picture and exact data**

<!-- passage:film12_s06_picture -->
Animate B_{0,s}→X_2[1]=0. For column 2 display an arbitrary decoded address ŝ_2; its return pointer may land at row 0,1,2,or3 of X_0, and every target displays 1. Never imply the actual example contains off-promise A inputs: mark ‘same argument for any opponent input’ while allowing ŝ_2 to vary. Display a_{0j}≥1−ε for j=1,2,3, a_{ij}+a_{ji}=1 for i≠j, a_{ii}=0; other probabilities remain symbolic. Caption: T=⌈log₂(1000m)⌉, ε=1/(1000T); these are the paper's parameters, not measured success rates.
<!-- /passage:film12_s06_picture -->

**Corpus statements:** `def-decode`, `claim-decode-cost`, `def-comparison`, `claim-comparison-state`, `claim-winner-dominates`, `eq-10`, `eq-11`, `def-T-eps`.

**Proposed finite statements:** `reader-example-parameters`.

## 05:00–06:05 | Why the tournament finds a winner

**Spoken**

<!-- passage:film12_s07 -->
Imagine giving every column weight one. Select a column with probability proportional to its weight and add it to a list. Then multiply each remaining weight by its probability of defeating the selected column. If column two is selected first, the new weights are the three comparison probabilities shown here, with zero for column two itself. The expected total weight at least halves at each step. This follows by pairing the probability that one column beats another with the reverse probability, which together sum to one. Meanwhile, an unselected genuine winner retains almost all its weight. The total cannot keep shrinking while that weight remains large. After logarithmically many stages, the list is therefore likely to contain the winner. These weights describe the analysis; the quantum program never computes their numerical values.
<!-- /passage:film12_s07 -->

**Picture and exact data**

<!-- passage:film12_s07_picture -->
Retain four columns. Initial weights (1,1,1,1), W=4. Condition on illustrative first pivot p=2; display new vector (a_02,a_12,0,a_32), without numerical bars pretending the a values are known. Show E[W_new|w]=(W²−∑_i w_i²)/(2W)≤W/2 for W>0; Separately show the winner's lower bound (1−ε)^t≥1−Tε>1/2 while unselected. Draw a top-down list labelled ‘at most T stages’, with T=⌈log₂(1000m)⌉. Show only existing column labels; do not invent more columns or suggest the list must reach length T. Explain stop/zero weight by fading inactive slots, not selecting with zero total mass.
<!-- /passage:film12_s07_picture -->

**Corpus statements:** `def-ideal-process`, `eq-12`, `eq-13`, `claim-expected-WT`, `claim-weight-lb`, `eq-14`, `prop-3.2`.

**Proposed finite statements:** `reader-tournament-first-pivot`.

## 06:05–07:00 | Sampling the weights quantumly

**Spoken**

<!-- passage:film12_s08 -->
The quantum part produces a sample with those weights. Start uniformly over column labels. Compare each label with all previous selections in fresh workspaces, retaining the results. Mark success only when every comparison favours that label. Its success probability is the product of those comparison probabilities, which is its weight. Conditional on success, the label is therefore sampled with probability weight divided by total weight. Amplitude amplification raises the chance of obtaining a successful sample while preserving that conditional distribution. Preserving the distribution is essential: otherwise the shrinking-weight calculation would describe a different algorithm. A fixed cap on the amplification attempts keeps the worst-case query bound valid even when there is no winner.
<!-- /passage:film12_s08 -->

**Picture and exact data**

<!-- passage:film12_s08_picture -->
Show columns i=0,1,2,3 feeding label branches; each branch has fresh comparison workspace for each recorded pivot p_b. Use w_i=∏_b a_{i p_b}, success probability W/m, and Pr(i|success)=w_i/W when W>0. If W=0, report failure; no conditional label law is defined. Display a success subspace with the same relative label weights before and after amplification, with overall mass changed. Never turn each label branch into a separately readable classical answer. Mark γ=1/(2m), η=ε for the sampler. Source card: preprint Lemma 3.1 and Proposition 3.2; Brassard–Høyer–Mosca–Tapp, arXiv:quant-ph/0005055v1, §2 Lemma 1 and equation (8), for the invariant good-state direction. Their Theorem 3 alone supplies expected cost, not this fixed cap. A small evidence note for production: the Lean path used by the headline proves the exact success-label law; the standalone full-state formulation is a different declaration.
<!-- /passage:film12_s08_picture -->

**Corpus statements:** `construct-sampler`, `eq-15`, `claim-success-prob`, `lem-3.1`, `claim-coupling`, `claim-tournament-cost`.

## 07:00–07:45 | Checking the selected column

**Spoken**

<!-- passage:film12_s09 -->
A plausible candidate still needs checking. Decode its address afresh, then search the local tests for a failure. One failing test is enough to reject. If all tests pass, the candidate really is a winner. For our left column, the correct address gives only passing tests. For every losing column, every proposed address has a failure somewhere. Quantum search can look for that failure in roughly the square root of the number of tests, with logarithmic factors for confidence and pointer reads. Combining the short candidate list with verification gives the square-root-of-m quantum bound, up to those factors.
<!-- /passage:film12_s09 -->

**Picture and exact data**

<!-- passage:film12_s09_picture -->
Return to the selected B_{0,s} and the test categories of shot 5. Search highlight travels over a symbolic index in {1,…,K}; no false implication that every test is read. For a losing column flash an actually failed all-one bit test (X_2[1]=0), not an unspecified invented transcript fault. Display Q(F_{k,m})≤C_k√m(log₂m)^{b_k} with ‘fixed k, sufficiently large powers of four m’. Under the miniature show ‘construction example; no numeric query comparison at m=4’.
<!-- /passage:film12_s09_picture -->

**Corpus statements:** `def-verify`, `claim-verify`, `cor-local-dichotomy`, `claim-error`, `prop-3.3`, `eq-2`.

## 07:45–08:35 | Two inputs that look the same until a query finds a change

**Spoken**

<!-- passage:film12_s10 -->
Now reverse the construction to see why classical queries are expensive. Put back the missing zero in our left column, at row zero, and blank its certificate cell. Every column now has a zero, so the answer is no. Erasing that one zero and filling that one correctly addressed cell restores our yes instance. Until an algorithm queries a changed location, the two runs receive identical answers and choose identical subsequent queries. In the lower-bound proof, the planted column and all zero locations are random, and the address inputs are independently drawn from a hard distribution. Our picture shows one pair of inputs; the proof averages over that distribution.
<!-- /passage:film12_s10 -->

**Picture and exact data**

<!-- passage:film12_s10_picture -->
Split screen showing exactly Y^0 and Y^1. Both use J=(0,2,1,3). Y^0 has X_0=(0,1,1,1); the other X columns are unchanged. Every certificate-cell bit in Y^0 is false. Y^1 has X_0=(1,1,1,1), and only B_{0,s} is filled with decoded pointers (2,1,3) plus genuine evaluation transcripts; all other cells remain false. Every A block remains unchanged. Mark changed region X_0[0] and B_{0,s}; some filled-cell bits may equal false, so label ‘locations where a difference can occur’. Persistent caption: ‘illustrative pair; these fixed A blocks are not asserted to follow the hard distribution’.
<!-- /passage:film12_s10_picture -->

**Corpus statements:** `def-dummy`, `def-planted`, `claim-Y-values`, `eq-18`.

**Proposed finite statements:** `reader-example-instance`.

## 08:35–09:45 | Why an adaptive algorithm cannot cheaply guess the address

**Spoken**

<!-- passage:film12_s11 -->
There are two ways to encounter the change: find the erased zero, or reach the filled cell. Reaching the cell requires its entire address. For sufficiently large m, one Forrelation answer remains hard after L classical queries. For r independent instances, an algorithm limited to L queries per instance guesses all r answers with probability at most two thirds to the power r, even when it interleaves its queries adaptively. This is the capped direct-product argument developed by Drucker, following Shaltiel. The proof must also handle an algorithm choosing which column looks promising. It fixes a column and a query time, and simulates the algorithm with a cap on queries to that column's address inputs. A correct visit in a nonheavy column forces this capped simulator to guess the full address. The bound concerns that joint event, without conditioning on which columns turned out nonheavy.
<!-- /passage:film12_s11 -->

**Picture and exact data**

<!-- passage:film12_s11_picture -->
Begin with the fixed example, then replace its forty fixed inputs by r independent samples U_0,…,U_{r−1}∼μ under a clearly labelled ‘general lower-bound distribution’. Replace the fixed true address by the random tuple s_i=(P(U_0),…,P(U_{r−1})); μ is supported on the promise, so these entries are defined. Display m=4^t and r=40t=⌈20log₂m⌉. Display L=⌊m^{1−1/k}/(log₂m)²⌋ and ‘m sufficiently large that 1≤L<R(P)’. Show separate per-instance budget counters q_h≤L, permitting interleaving. Display success≤(2/3)^r. Then show a simulator for one fixed (column i, query time t), with total cap L across A_{i,0},…,A_{i,r−1}; abort before query L+1. Show event ‘nonheavy AND true-cell visit at t’ inside ‘simulator's address guess correct’. Source card: Drucker, arXiv:1005.0644v2, §1.3 and Lemmas 3.1–3.2; Shaltiel is credited via the preprint's §4.1, with no direct theorem claim. Caption: Lean proves the direct-product statement by induction on subdistributions, an alternative to the preprint's supermartingale proof.
<!-- /passage:film12_s11_picture -->

**Corpus statements:** `eq-5`, `lem-2.1.i`, `claim-minimax-mu`, `lem-4.1`, `claim-address-guess`, `def-heavy`, `def-simulator`, `eq-21`, `eq-6`.

## 09:45–10:35 | The classical bound

**Spoken**

<!-- passage:film12_s12 -->
Choose a total query budget G equal to the integer part of mL over one hundred. Few columns can receive more than L address queries. The capped-simulator estimate bounds visits to true cells in nonheavy columns, even after summing over every query. The erased-zero event is also unlikely for a uniformly chosen column. Together the two probabilities are less than one third. An algorithm correct with probability two thirds on both kinds of input would need a gap of at least one third between its output probabilities. That contradiction gives the classical lower bound. The small example illustrates the two possible discoveries; this estimate requires growing m.
<!-- /passage:film12_s12 -->

**Picture and exact data**

<!-- passage:film12_s12_picture -->
Display G=⌊mL/100⌋ and the preprint's bound 4G/m²+G/(mL)+G(2/3)^r<1/3, under ‘fixed k, sufficiently large m’. Label terms ‘erased zero’, ‘heavy planted column’, ‘guess true address’. Keep the same two highlighted locations from shot 10 beside the matching terms. Show R(F_{k,m})>G, then R(F_{k,m})≥c_k m^{2−1/k}/(log₂m)². Source/evidence note: Lean obtains the sharper erased-zero term 2G/m² by a different argument and weakens it for the preprint bound. Do not animate estimated finite query counts, and do not apply G or the hard-distribution hypothesis to m=4.
<!-- /passage:film12_s12_picture -->

**Corpus statements:** `eq-17`, `eq-19`, `eq-20`, `eq-22`, `eq-23`, `prop-4.2`, `cor-R-omega`.

## 10:35–11:25 | What nearly quartic means

**Spoken**

<!-- passage:film12_s13 -->
Compare the two bounds: quantum cost is at most a constant times the square root of m, with logarithmic factors; randomized cost is at least a constant times m to the power two minus one over k, divided by a logarithm squared. That gives the power four minus two over k after eliminating m, up to logarithmic factors. For any proposed universal exponent below four, choose k large enough, then hold k fixed while m grows. The polynomial advantage eventually defeats the logarithms. No smaller exponent works for every total Boolean function. The quartic upper bound was already proved by Aaronson, Ben-David, Kothari, Rao and Tal using Huang's theorem. Together these results identify the optimal universal exponent as four.
<!-- /passage:film12_s13 -->

**Picture and exact data**

<!-- passage:film12_s13_picture -->
Show the two exact bounds from eq-2. Then show the decisive ratio R(F_{k,m})/(1+Q(F_{k,m}))^α ≥ c_{k,α} m^{2−1/k−α/2}/(log₂m)^{2+αb_k}→∞ when 0≤α<4 and 2−1/k>α/2. Use quantifier animation ‘choose α<4 → choose fixed k → let m→∞’, with no slider allowing k to grow secretly with m. Main display ends α_tot=4. Source card: preprint §5, Theorem 1.1; ABKRT Theorem 2; Huang Theorem 1.1. Production note: the Lean universal upper-bound route uses complexitylib instead of reproducing the paper's Appendix A.
<!-- /passage:film12_s13_picture -->

**Corpus statements:** `eq-2`, `claim-exponent-ratio`, `claim-no-smaller-exponent`, `thm-A.1`, `thm-1.1`.

## 11:25–12:00 | What the checking establishes

**Spoken**

<!-- passage:film12_s14 -->
The supplied corpus records Lean and Comparator checking of the full theorem, with no remaining mathematical hypothesis. Some formal proofs follow different routes. This film's finite example is an exact calculation awaiting its own Lean check. The comparisons were local rehearsals, unrepeated here. AI agents reviewed statement fidelity; no person has yet reviewed it. The separate checking film shows what formal verification establishes, and what still requires mathematical review.
<!-- /passage:film12_s14 -->

**Picture and exact data**

<!-- passage:film12_s14_picture -->
Presenter returns beside the original four columns. Show three literal rows: ‘Headline theorem: recorded as built and compared, no mathematical hypothesis’; ‘Film example: exact finite calculation, proposed Lean statements pending’; ‘Definition fidelity: AI review; no human review’. Below: ‘Source snapshot supplied with packet; checking was not reproduced for this film design’. Link the headline to thm-1.1, lem-2.1.i and the proposed example IDs in the reader. Do not show simulated terminal output as an executed check. End on the same winner and its three outward pointers.
<!-- /passage:film12_s14_picture -->

**Corpus statements:** `thm-1.1`, `lem-2.1.i`.

**Proposed finite statements:** `reader-forrelation-yes`, `reader-forrelation-zero`, `reader-example-instance`.
