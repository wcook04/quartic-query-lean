# Fourth reading — closer mathematical and editorial review

I've reread the same 27-page exposition, this time concentrating on the exact claims, the examples' ability to teach the proof, and the places where a reader could draw an incorrect conclusion even though the mathematical statement is technically correct.

My assessment is more pointed now:

The paper is substantially better at explaining how the proof works than at explaining why this particular construction is necessary.

That distinction matters. The manuscript has convincing demonstrations of individual mechanisms, but still doesn't sufficiently expose the design decisions that make those mechanisms fit together.

I would not recommend adding another long preliminary overview. There is a more targeted way to improve it: make the key trade-offs and distinctions explicit at the exact passages where the reader needs them.

## 1. The most important missing explanation is the asymmetry of the certificate array

Pages 5–8 introduce the general board, with \\(r=20\log_2m\\) address bits and \\(2^r=m^{20}\\) cells per column.

The paper correctly explains why so many addresses make classical guessing difficult and why the number of cells remains polynomial in \\(m\\).

But I think it misses the most important pedagogical consequence.

The quantum algorithm can reach the selected cell without examining the other \\(2^r-1\\) cells.

On a promised column, it computes the \\(r\\) hidden partial-function answers quantumly, giving the address. It then accesses only that cell and searches its local tests.

The number of local tests is

\\[ K=2m-1+r(S+2), \\]

which is independent of the number \\(2^r\\) of other cells.

That is a remarkably important feature. The array can be huge without imposing an equally huge verification cost.

Classically, however, reaching the correct cell without first learning its address is precisely the event the direct-product argument makes unlikely.

This should be a central explanatory sentence in Section 2, not merely something readers infer after studying both algorithms.

It explains why the construction can afford such a large certificate array in the first place.

## 2. The manuscript needs to distinguish four things that its diagrams make look similar

On pages 4–6, the visual language of cells, addresses, certificates and winners is intuitive. But those terms represent different mathematical conditions.

A column can have a defined, correct address and still not be a winner. It can have internally consistent transcripts whose output bits fail the promised address. It can possess a cell that appears convincing but fails one pointer test. It can even defeat every rival in comparisons and still fail to win.

These distinctions are all present, but a reader has to reconstruct them across different examples.

I would introduce the following conceptual hierarchy immediately after Figure 2:

| Property             | What it establishes                                                                                         |
| -------------------- | ----------------------------------------------------------------------------------------------------------- |
| Promised address     | All partial-function answers exist and determine one cell                                                   |
| Correct transcript   | Stored gate values accurately represent the exact circuit's computation                                     |
| Valid certificate    | The candidate satisfies the string, domain, value, gate and pointer tests                                   |
| Comparison dominance | The candidate defeats rivals in the cheaper comparison procedure; this alone proves no certificate validity |

The final row is what motivates the false-pointer board in Section 4.

The third is what local verification establishes in Section 2.

The first two are prerequisites for a valid certificate, but neither is sufficient by itself.

A diagram that shows the true cells of columns 3 and 4 without explaining this hierarchy can unintentionally make them look like valid winning certificates. They aren't.

This is not a mathematical error. It is an avoidable cognitive ambiguity at the foundation of the paper.

## 3. The classical address is not simply a uniformly hidden string

This is a more substantive explanatory issue.

The introduction says the address is hidden, and the construction has \\(2^r\\) possible cells. An intuitive reader might naturally conclude that the lower bound is based on guessing a uniformly random \\(r\\)-bit address, with probability \\(2^{-r}\\).

That is not what Section 5 proves.

The address is the vector of answers to \\(r\\) independent partial-function samples drawn from a hard distribution \\(\mu\\). The output bits need not be uniformly distributed, and an adaptive decision tree can acquire partial information about them.

The actual guarantee comes from the separately capped direct-product lemma:

\\[ \Pr(\text{predict all }r\text{ answers})\leq (2/3)^r. \\]

Crucially, this bound accommodates adaptive allocation of queries among the samples, provided each sample's cap is respected.

This is much more subtle and interesting than merely hiding a uniformly selected cell.

The paper eventually explains the distinction rigorously. But I would explicitly warn against the uniform-address intuition at the first mention of the \\(2^r\\) cells.

That would make the classical lower bound feel like the solution to a genuine problem rather than an unusually elaborate justification for the obvious difficulty of guessing an address.

## 4. A concrete mathematical improvement to the eight-bit example

I independently enumerated all \\(2^8=256\\) possible inputs to the small Forrelation function in Section 1.

The paper says that \\(\Phi\\) is a multiple of \\(1/8\\), which is true, but surprisingly weak.

In fact, its only possible values are

\\[ \Phi\in\\{-1,-\tfrac12,0,\tfrac12,1\\}. \\]

The exact distribution is:

| \\(\Phi\\) | Number of inputs | Partial-function result |
| ---------- | ---------------- | ----------------------- |
| \\(-1\\)   | 8                | Undefined               |
| \\(-1/2\\) | 96               | Undefined               |
| \\(0\\)    | 48               | 0                       |
| \\(1/2\\)  | 96               | 1                       |
| \\(1\\)    | 8                | 1                       |

This gives a stronger and more complete teaching opportunity than the current three examples.

The small partial function has 152 promised inputs and 104 unpromised inputs. At this size, the exact certificate circuit can simply distinguish the sign of the integer numerator \\(N=z_1^TWz_2\\):

- \\(N>0\\): domain bit 1, value bit 1.
- \\(N=0\\): domain bit 1, value bit 0.
- \\(N<0\\): domain bit 0, value bit 0.

The paper could use this to connect three ideas: the mathematical promise, the quantum projection experiment and the exact classical circuit.

Currently, the exact circuit appears in Section 2 as a somewhat abstract object, while the actual Forrelation arithmetic was completed in Section 1.

A tiny worked example of the circuit's output on the five possible values of \\(\Phi\\) would close that gap.

This is a more valuable addition than another general explanation of what circuit transcripts are.

It would show the reader what is actually being certified.

## 5. The circuit explanation is rigorous in principle but incomplete as a worked example

Page 6 gives a NOT–OR gate example to show how local consistency tests work.

This is useful, and the explanation of why changing two stored gate values cannot hide a false computation is particularly good.

However, it teaches the generic idea of circuit transcripts, not the specific arithmetic of the circuit used in the separation.

The manuscript then claims a near-linear circuit bound on page 7, sketches a Walsh-transform implementation on page 8, and moves on.

The actual intellectual bridge is missing: how does a calculation of Forrelation become a collection of locally checkable Boolean gate equations?

The reader needs to see at least one step of that conversion.

I would show a four-coordinate Walsh transform performed with additions and subtractions, then explain how those integer arithmetic operations can be implemented by a fixed fan-in-two Boolean circuit whose intermediate gate values are stored in the transcript.

The reader does not need all 180 gates of the small example. They need enough to connect the matrix calculation they understand to the Boolean circuit the verifier checks.

That would substantiate the near-linear circuit-size claim pedagogically rather than merely citing its construction in the reasoning record.

The importance of the size estimate is explained, but its underlying mechanism could be more concrete.&#x20;

exposition(2).pdf



## 6. The most useful missing quantum example involves two genuinely fractional comparisons

Section 4.3 is careful about the fact that successful comparison probabilities multiply across independent fresh registers.

The key identity is

\\[ w_i=\prod\_{b=1}^j a\_{i,p_b}. \\]

But the main worked fractional example on page 13 has only one previously selected pivot.

It demonstrates normalization of fractional weights, not their multiplication across several comparisons.

The genuinely illuminating calculation is currently relegated to the answer to Question 2 on page 23.

Using the paper's fractional matrix, after pivot 2 the weights are

\\[ (1,0,2/3,1/4). \\]

After pivot 4 they become

\\[ (1,0,4/15,0), \\]

because, for instance, the third column survives the first pivot with probability \\(2/3\\) and the second with probability \\(2/5\\).

Thus its weight is \\(4/15\\). The preparation succeeds with probability \\(19/60\\), and the conditional law on successful sampling is

\\[ (15/19,0,4/19,0). \\]

This is a perfect example of the distinction between probabilities and amplitudes.

The product \\(4/15\\) is a probability of joint success, not an amplitude obtained by directly multiplying successful probabilities as coefficients in the quantum state.

Because the two comparison registers are independent and retained, the corresponding joint successful component has squared norm \\(4/15\\). The subsequent amplification preserves that component's relative contribution to the total successful state.

The exposition explains this correctly in general, but the main text would be stronger if it worked through the numerical example before giving the full tensor-product formula.

This is exactly where a reader new to quantum computation could confuse classical probability multiplication with quantum amplitude multiplication.

I would move part of Question 2's numerical solution into Section 4.3 and leave the overshoot calculation as the exercise.

## 7. The choice of logarithmic address length deserves a proper derivation

The paper explains that \\(r=20\log_2m\\) makes guessing the true address sufficiently unlikely while keeping the certificate array polynomial in size.

But why logarithmic, specifically?

This can be explained by putting together two constraints already proved in the manuscript.

The classical budget has order at most \\(m^2\\). The light true-cell contribution is bounded by

\\[ G(2/3)^r. \\]

To make this small, \\(r\\) must be at least a sufficiently large constant multiple of \\(\log m\\).

On the other hand, there are \\(2^r\\) cells per column. If \\(r\\) grew much faster than \\(\log m\\), the number of cells would cease to be polynomial in \\(m\\).

So the construction needs

\\[ r=\Theta(\log m) \\]

for two opposing reasons.

This is an elegant design constraint.

The exact choice \\(20\log_2m\\) then provides more than enough suppression for the union bound:

\\[ (2/3)^r\leq m^{-10}. \\]

That is a more satisfying explanation than simply stating that the value 20 is sufficient.

There is also a notation distinction worth emphasizing here: \\(r\\) indexes the certificate cell, while \\(\ell=\log_2m\\) indexes a row in another column. In the large construction \\(r=20\ell\\). Their equality in the toy board is incidental.

## 8. Section 5's strongest argument deserves a clearer hierarchy of claims

The classical proof is impressively careful about adaptive algorithms. I particularly like the distinction between a run being light at the instant of a cell visit and the whole run being light.

The paper correctly uses the latter.

But the three-charge proof contains two different kinds of reasoning.

The erased-zero charge is essentially a search problem. The zero in a column is uniformly distributed among positions not yet eliminated by queries.

The true-cell charge is a prediction problem. The cell selected by a query position reveals an attempted answer to a hard tuple of independent partial-function inputs.

Those mechanisms are fundamentally different.

I would make the section's first-difference argument look like a mathematical proposition with two subclaims:

Search obstruction: The algorithm is unlikely to read the erased zero in the independently selected planted column.

Prediction obstruction: Unless that column is heavy, the algorithm is unlikely to query a bit in its true certificate cell.

The heavy-column charge then appears as the cost of escaping the second obstruction.

This would give the reader a natural interpretation of the three charges rather than treating them as three unrelated probabilistic estimates.

The current three-charge table is good. The missing element is the conceptual relationship among the charges.

### The proof's error asymmetry is a real strength

Another detail I appreciated on rereading is the asymmetric correctness argument in Section 4.4.

When \\(F=1\\), the quantum algorithm does not need every shortlisted candidate to be classified correctly. It needs the real winner to enter the list, its address to be decoded correctly and its verification to pass.

When \\(F=0\\), every candidate has a failed local test at every proposed address, so the relevant risk is that the violation search misses a defect.

This is why the two rows of the error-budget table are different.&#x20;

exposition(2).pdf



That is good mathematical writing. I would preserve the asymmetry instead of replacing it with a looser all-purpose union bound.

It is also another case where the paper is stronger than a quick reading suggests.

## 9. I would distinguish the supporting theorems more sharply

There is one point where a specialist referee will be especially demanding: the exact promise used for the Forrelation lower bound.

The paper defines a one-sided promise, with \\(\Phi\geq\delta\\) giving output 1, sufficiently small absolute correlation giving output 0, and large negative correlation outside the promise.

It attributes the lower bound to Bansal and Sinha, Theorem 1.3 and Corollary 1.4.&#x20;

exposition(2).pdf



The published Bansal–Sinha work does establish the near-linear randomized hardness of \\(k\\)-Forrelation, at the relevant broad asymptotic scale.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



However, the exposition should make the exact transfer to its chosen promise particularly easy to audit.

The reader ought not to have to inspect the original source independently to determine whether the threshold convention, the large-negative inputs, and the chosen version of the randomized lower bound match.

A two- or three-sentence explanation of that correspondence would be worth more than another general literature comparison.

The same principle applies to the quantitative family theorem. The original OpenAI preprint states the nearly quartic separation and optimality of the exponent.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub

&#x20;Your specific constants and logarithmic exponents are presented as reconstructed, deliberately loose choices.



Those should have their own clearly attributed theorem statement rather than appear indistinguishably under the original Theorem 1.1 label.

I see this as a claim-auditability problem, not evidence that the claims are false.

## 10. The exercise design is more advanced than it first appears

The five questions are intelligently chosen, but they are demanding.

Question 1 tests promise certification. Question 2 requires understanding weighted conditional sampling and amplitude-amplification overshoot. Question 3 tests independence in the planted distribution. Question 4 tests the difference between whole-run budget conditions and local query-time conditions. Question 5 tests the quantifier order in exponent optimality.

That is a coherent learning progression.

But the paper's opening claim about prerequisites understates how difficult Questions 2 and 4 are.

A mathematically able reader might correctly understand the general result but struggle considerably with those exercises.

I would classify them by purpose: basic comprehension, proof reconstruction and technical extension. That would help readers understand whether failure to solve a particular problem means they have missed the main idea or merely have not mastered a delicate technical argument.

The separated answer section is valuable, and its internal links improve the PDF's usability. I would keep that structure.

The final combined-explanation exercise is particularly strong because it asks the reader to connect both sides of the proof, not merely reproduce isolated calculations.

## 11. What I would recommend for the next actual edit

I would make the changes in this order.

01

Improve the exact small circuit example, pages 2–7.

Exploit the five possible \\(\Phi\\) values and connect the integer numerator to the domain/value outputs. This makes the certification mechanism much more concrete.

02

Explain the certificate-array asymmetry at its introduction, page 5.

Say explicitly why quantum verification depends on the tests in one decoded cell rather than the total number of cells, while the classical difficulty is finding that cell.

03

Bring the two-pivot fractional calculation into Section 4.3.

Demonstrate the product of comparison probabilities before the general coherent-preparation argument.

04

Derive the two constraints on \\(r\\), pages 5 and 18–21.

Show why the hidden address must be long enough to defeat adaptive guessing but short enough to keep the input polynomial.

05

Make the one-sided Forrelation hardness transfer explicit, page 8.

This is the most important citation-level clarification because the precise promise matters to the rest of the construction.

## Final judgment after four readings

I would now separate the manuscript's quality into three dimensions.

Quality of worked mathematical explanations

8.5/10

Quality of the continuous teaching experience

7/10

Scholarly presentation and auditability

7.5/10

Editorial assessments, not independent correctness certification.

I am increasingly convinced that the manuscript's real strength is its careful construction of examples around specific failure modes.

That is not trivial. The examples reveal genuine technical subtleties in the proof.

But the next step is to explain more precisely why the construction has the shape it does, instead of continuing to give the reader more details about how each piece operates.

The most valuable revisions now are surprisingly small: one exact five-value Forrelation example, one explicit explanation of why only the selected cell is verified, one two-pivot fractional sampling calculation and one derivation of why the certificate address length must be logarithmic.

Together, those changes would improve the paper's explanatory depth without making it significantly longer.

I have checked the numerical claims discussed here against the definitions in the attached manuscript, but I have not independently verified every external theorem, the full Lean development or all arguments deferred to the reasoning record. The absence of a detected error in these checks should not be mistaken for a complete mathematical correctness review.

My conclusion is that the exposition is now strong enough that the largest remaining gains come from the precision of its teaching choices, rather than the addition of further technical content.