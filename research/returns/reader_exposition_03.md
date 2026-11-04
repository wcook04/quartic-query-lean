# Third reading: a stricter review of the exposition

This time I concentrated on the actual mathematics, the order in which the reader learns it, and whether the examples genuinely prepare the reader for the general proof.

My assessment is becoming more specific: the paper is technically much better than its teaching structure. There are several passages I would preserve almost unchanged, but also places where the exposition creates an easier-looking picture of the mathematics and only reveals the real difficulty several pages later.

I did not find an obvious contradiction in the main numerical examples or in the selected probability calculations I checked. The problems below are primarily about mathematical explanation, with a few important issues of scope and precision.

## 1. The biggest bottleneck is actually pages 5–8

My previous passes concentrated heavily on the quantum sampler and classical simulator. After rereading, I think the transition from the four-column example into the general construction is an even greater obstacle for a first-time reader.

Consider what happens.

On page 5, the reader is looking at a very understandable board: four columns, each with four bits, two address inputs and four certificate cells.

Before that picture has completely settled, the paper introduces \\(k,t,m,\ell,r\\), generalizes the addresses, sets \\(r=20\log_2m\\), observes that the number of cells is \\(m^{20}\\), explains the construction's ancestry and previews the near-linear certificate circuit.

On pages 6–7 it introduces circuit transcripts, local tests, \\(K\\), general \\(k\\)-fold Forrelation, quantum error reduction, the gate-size bound \\(S\\), classical hardness \\(L\\), and the total input length \\(n\\).

By page 8 it states the full separation theorem.

That is an enormous conceptual transition compressed into approximately three pages.

The writing within each paragraph is generally precise. The problem is that mathematical objects are being introduced substantially faster than the reader can understand their purpose.

I would restructure this transition around three distinct questions:

- Why are certificates stored at addresses determined by partial-function outputs?
- Why can the quantum algorithm discover those addresses cheaply?
- Why are the stored certificates small enough to verify efficiently?

Only after those questions have clear answers would I introduce all the quantitative parameters.

The paper currently presents much of the machinery before completing that motivation.

## 2. The eight-bit example is almost too easy

This is a new concern I think matters.

The three inputs \\(a^+\\), \\(a^0\\), and \\(a^-\\) are excellent for teaching the promise and the sign of the Forrelation amplitude.

Their amplitudes are \\(1,0,-1\\), and the projection experiment consequently has success probabilities \\(1,0,1\\).

A reader sees a perfect distinction between the two promised examples using just two queries. That is a memorable illustration.

But it is not representative of the hardest promised inputs for the general decoder.

On page 7, the real promise distinction requires separating projection probabilities as small as

\\[ p\geq c=\delta^2 \qquad\text{from}\qquad p\leq c/4, \\]

where \\(\delta=2^{-5k}\\).

For \\(k=2\\), the boundary probabilities are only \\(2^{-20}\\) and \\(2^{-22}\\).

The manuscript gives a sufficient trial count

\\[ \rho=\left\lceil16c^{-1}\ln(1/\eta)\right\rceil. \\]

For error \\(\eta=0.01\\), that formula yields about 77.3 million trials, each using two queries.

That is not a claim about the optimal decoder or the smallest useful implementation. It is the cost of the paper's explicit, deliberately simple repetition scheme. But it illustrates a crucial point: cheap here means independent of \\(m\\) when \\(k\\) is fixed, not numerically inexpensive.

The paper acknowledges the \\(2^{10k}\\) dependence, but the distinction is too easy to overlook.&#x20;

exposition(2).pdf



I would insert a short bridge after the eight-bit experiment:

> These examples have extreme correlations, so one trial already distinguishes them. General promised inputs can lie much closer to the decision thresholds. Repetition is then necessary, and its cost depends strongly on \\(k\\), though not on the growing number \\(m\\) of positions.

This would prevent the clean demonstration from giving a misleading impression of what the general quantum decoder accomplishes.

## 3. The paper needs one small table connecting the promise, decoder and certificate

There is a particularly good opportunity that is currently missed.

The three eight-bit inputs behave differently across three mechanisms.

| Input     | Actual partial-function value | Projection experiment | Exact circuit's domain bit |
| --------- | ----------------------------- | --------------------- | -------------------------- |
| \\(a^+\\) | 1                             | Always succeeds       | 1                          |
| \\(a^0\\) | 0                             | Always fails          | 1                          |
| \\(a^-\\) | Undefined                     | Always succeeds       | 0                          |

This table would unite ideas that the paper currently develops across pages 2, 3, 6 and 9.

It shows exactly why the quantum decoder cannot be used as a certificate of promise membership, why the off-promise column still participates in comparisons, and why the exact circuit must output a domain bit.

That is the kind of compact explanation that could replace several reminders later in the paper.

The manuscript is good at giving examples; the next improvement is to make more of those examples explain multiple sections simultaneously.

## 4. The four-column board conceals more information than readers may realize

I checked the input-size formula against the small circuit census in Appendix A.4.

For the teaching example, the paper uses \\(m=4\\), \\(r=2\\), \\(k=2\\), \\(\ell=2\\), and an exact circuit with \\(S=180\\) gates.

Each certificate cell therefore contains

\\[ rS+(m-1)\ell =2(180)+3(2)=366 \\]

input bits.

There are 16 certificate cells across four columns. Adding the column strings and address inputs gives 5,936 input bits for the actual toy function.

This is a useful, somewhat surprising observation.

The diagrams make it look like a tiny board of four-bit strings and four cells per column. That is appropriate for visual instruction, but the cells hide most of the actual input.

I would explicitly state that the drawings suppress transcript payloads.

There is also a more important distinction: if one applied the asymptotic choice \\(r=20\log_2m\\) at \\(m=4\\), the address length would be 40 rather than 2. The resulting cell array would have \\(2^{40}\\) entries per column.

The teaching example is therefore deliberately a different, much smaller addressing regime.

The manuscript does disclose this, but the difference could be foregrounded. Otherwise, a reader may regard the four-column example as a literal small instance of the quantitative separation family. It isn't.

This matters especially when Figure 4 reuses the visual geometry to illustrate the classical planted pair. The text correctly warns that \\(L=0\\) at that size. The picture illustrates where the inputs differ, not the distributional hardness responsible for the asymptotic lower bound.

## 5. The classical lower-bound proof is being interrupted by its own safeguards

After another reading of pages 18–21, this is one of my strongest criticisms of the paper's composition.

The proof has an elegant underlying structure.

A deterministic algorithm's runs on the dummy and planted boards coincide until it encounters a changed bit. This can happen only by discovering the erased zero or visiting the planted cell.

The erased-zero event is controlled by the limited number of string queries. The planted-cell event is controlled by the direct-product hardness of predicting an entire hidden address.

That is an exceptionally clear proof idea.

But look at the reading sequence.

The paper presents the three charges, proves the erased-zero charge, interrupts the argument to discuss the necessity of independence of \\(I\\), gives Question 3, returns to the true-cell event, introduces a direct-product lemma, discusses why conditioning on lightness fails, constructs the simulator, gives an optional XOR trace, asks Question 4, finishes the true-cell charge, adds two further counterexamples about the hypotheses, and finally combines the bounds.

Every one of those additions has a mathematical justification.

Collectively, though, they fracture the main proof.

By the time the reader reaches the final gap calculation, the initial three-charge structure is several dense pages behind them.

I would make the principal proof run uninterrupted from the three-charge table through the simulator and final bound. Keep the indispensable explanation of why the simulator's success event is unconditional, but move the extended counterexamples, optional trace and exercises to an immediately following subsection called something like Why the reduction's hypotheses matter.

This is where the exposition's conscientiousness becomes counterproductive.

The manuscript is so intent on making the argument resistant to misunderstanding that it sometimes prevents the reader from seeing the argument as one whole.

### One aspect of the simulator deserves explicit praise

The stop-before-read rule on page 19 is particularly good.

The algorithm's proposed query coordinate contains the entire certificate address. The simulator reads that address from the coordinate without querying the selected cell bit.

It can therefore terminate before spending another query on the hidden input.

This is the key reason the reduction survives adaptive cell guessing.

Moreover, the proof uses the event that the whole dummy run is light, not merely that the budget has not yet been exceeded at the time of a particular cell query.

That distinction is essential, and the paper handles it carefully.&#x20;

exposition(2).pdf



I would not dilute this argument. I would protect it from the surrounding digressions.

## 6. The quantum algorithm should be stated as a theorem before being constructed

A similar problem occurs in Section 4, although it is less severe.

On page 9, the four-step algorithm says to sample a pivot and append it on success.

But at that point, the meaning of sampling a pivot has not been established.

The reader then learns about stochastic comparisons, an ideal weighted process, expected mass reduction, conditional sampling and amplitude amplification.

The detailed sampler contract does not arrive until page 12.

For a research reconstruction this order is defensible. For a teaching exposition it is harder than necessary.

I would first state the abstract algorithmic claim:

> Given pairwise comparison procedures with complementary outcome probabilities, there is a quantum shortlist algorithm using about \\(\sqrt m\\) comparisons, up to logarithmic factors. If one column beats every other column with probability at least \\(1-\varepsilon\\), the shortlist contains it with high probability.

Then explain the three ideas underlying that result: expected reduction in surviving mass, preservation of a dominating column, and exact conditional sampling of the weights.

Finally give the reversible quantum implementation.

The manuscript currently contains all of this. The missing element is a single named proposition functioning as the destination for the reader.

### Another subtle strength worth making more visible

The sampler does not need to calculate its weights.

This is easy to say, but the manuscript actually explains why.

For any fixed column, the independent comparison registers multiply their success probabilities. Across the coherent superposition of different column labels, the successful probability masses add.

Thus the prepared state implicitly represents the desired weights.

Amplitude amplification raises the total chance of sampling successfully without altering their conditional proportions.

That is arguably the most interesting quantum-algorithmic insight in the exposition.

It should stand out more.

I would give it a short displayed identity, with the accompanying explanation that the quantum procedure prepares probability masses proportional to the ideal weights without ever evaluating those weights numerically.

The fractional matrix on page 13 demonstrates that principle well and should be preserved.

## 7. The construction's parameters each have a job, but those jobs should be consolidated

The manuscript uses three important design choices whose causal roles are currently scattered across several sections.

The parameter \\(k\\) controls how close the underlying classical partial-function hardness gets to linear in \\(m\\), while its quantum decoding cost remains independent of \\(m\\) for fixed \\(k\\).

The parameter \\(r\\) controls how hard it is to guess the complete certificate address. It must be large enough for direct-product suppression but small enough that the number of cells remains polynomial in \\(m\\).

The circuit size \\(S\\) controls how expensive it is to verify certificates. It must remain near-linear in \\(m\\) so that quantum search over local tests costs roughly \\(\sqrt m\\).

These are three different balancing acts.

The paper states the facts individually, but I would explicitly connect them before the proof of the upper and lower bounds.

The reader should know that the entire construction depends on making all three choices compatible.

It would also explain why the construction is not simply “take a hard partial function and hide its answer in a certificate array.”

The pointer comparisons and verification circuit are what make that hiding compatible with the quantum upper bound.

## 8. The paper should be more explicit about the meaning of “nearly quartic”

This is especially important because the title concerns an optimal exponent.

From the displayed bounds, for each fixed \\(k\\), the relevant leading relationship is

\\[ m^{2-1/k}=(\sqrt m)^{4-2/k}. \\]

The exponent \\(4-2/k\\) is always strictly below four for fixed finite \\(k\\).

The equality \\(\alpha\_{\mathrm{tot}}=4\\) is instead a uniform statement: every proposed universal exponent strictly below four fails.

Section 6 explains this correctly.

But I would say it at the beginning too, since otherwise a nonspecialist may expect one explicit fixed-\\(k\\) family to exhibit a fourth-power lower bound without any exponent loss.

The paper also discusses the stronger growing-\\(k\\) family in companion documents, but that is a different quantifier problem from the one fully developed here.

A one-sentence distinction early on would make the title much more transparent.

### Why the actual input length matters here

The bound

\\[ n=O_k(m^{22}(\log m)^3) \\]

is also important to interpretation.

These functions have enormous inputs relative to the number of displayed columns. The theorem compares the number of bit-oracle calls needed by classical and quantum algorithms. It is not a statement that an implemented quantum computer solves a practical task four powers faster in wall-clock time.

The paper does state the query-model restrictions, but I would put that practical limitation beside the final result, not leave it exclusively in the opening definitions and the input-length calculation.

This is especially important if the exposition is intended to circulate outside theoretical computer science.

## 9. Several specific editorial defects remain

Figure 1, page 4. The figure is described as schematic, but its bit strips and certificate-cell array do not have the literal sizes of the four-column example. A reader has just been introduced to a precise small instance, so this visual ambiguity is unfortunate. Figure 2 is more effective. I would consider using Figure 2 as the first main board illustration and introducing the general schematic afterwards.

Section 3, page 7. The quantum decoder, exact circuit and classical hardness are presented as successive technical paragraphs. They are really three named properties of the underlying partial function. Give each a short statement followed by the role it plays later.

Section 4.2, page 11. The halving calculation is elegant, but the very next transition into the sampler should explicitly say that the ideal process has not yet produced an executable algorithm. The unknown weights are analytical objects; the quantum preparation will realize their distribution implicitly.

Section 4.4, page 15. The error-budget table is strong. I would present it as the culminating correctness argument rather than surround it with so much implementation detail about controlled reads. Those reads matter, but the correctness decomposition deserves the reader's attention.

Section 5, page 16. The enormous blank lower portion of the page is a conspicuous layout problem. Figure 4 should be placed closer to the text introducing it, or the prose should be reflowed. The start of the paper's main classical argument currently looks visually unfinished.

Section 7, pages 22–23. The Lean discussion is admirably careful about formal statement coverage. But its distinction between the comparison-bundle family theorem and the separately checked named-circuit theorem is important enough that it should be shown in a compact claim-to-evidence table. The historical source-comment discussion should be moved out of the narrative.

Appendix B, pages 25–26. This is genuinely worthwhile mathematical material. The product-of-conditional-values proof is concise and gives a convincing explanation for why adaptive interleaving does not defeat separate per-instance budgets. I would retain it rather than replacing it with an opaque citation.

## 10. What has become clear about the paper's quality

There are really two ways to assess this manuscript.

As a repository of detailed explanations of the individual mechanisms, it is strong. The examples have clearly been designed around actual proof hazards. In particular, the off-promise input, cyclic comparisons, conditional sampling, light-event simulator and separate-cap lemma do serious explanatory work.

As a continuous learning experience for someone who does not already know the proof, it is less successful.

The biggest difficulties occur at transition points: from the tiny Forrelation instance to the large family; from a comparison rule to a stochastic tournament; from an ideal weighted process to a coherent quantum sampler; and from an intuitive planted-pair argument to a uniform adaptive lower bound.

The paper is often quite clear on either side of those transitions. It does not always make the transition itself sufficiently explicit.

This is why the writing can feel simultaneously precise and exhausting.

### What I would not do

I would not add another lengthy tutorial on elementary linear algebra. I would not put the full Forrelation hardness proof into this paper, and I would not merge the long reasoning record into the exposition.

I would not delete the counterexamples that distinguish the work from a cursory proof summary.

And I would not try to transform this into a short popular-science article. Its real audience is mathematically capable readers who want to reconstruct the proof.

## My revised verdict

The manuscript is good, but not yet optimally written for its own declared audience.

My principal concern is not the sentences individually. Most are reasonably precise, and some are exceptionally instructive. It is that the manuscript asks readers to maintain too many proof obligations simultaneously, while repeatedly interrupting its central arguments to explain exceptional cases.

The next round should be a structural edit of the mathematical exposition, not another expansion of the proof record.

If I were deciding what changes would most improve the paper, I would focus almost entirely on the pages 5–8 transition, the presentation of the quantum shortlist theorem, and the continuity of the classical planted-pair proof.

I would preserve the four-column examples, weighted-halving identity, fractional sampler, stop-before-read simulator and direct-product proof. Those are the manuscript's strongest assets.

One final distinction: my spot checks support the internal calculations described above, but they are not an independent certification of the entire proof, the external source claims or the Lean development. I would not conflate a favorable writing review with a mathematical referee report establishing correctness.

The main challenge now is making the reader see the proof's architecture as clearly as the manuscript already explains its individual components.