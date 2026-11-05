---
title: "Why OpenAI’s query separation is nearly quartic"
subtitle: "An examples-first explanation of the optimal randomized–quantum exponent"
author: "Will Cook"
date: "November 2026"
bibliography: exposition.bib
link-citations: true
---

# 1. A matrix with a hidden zero in every column

Take an $m\times m$ matrix of bits. Does it have an all-one column? To see the difficulty for a classical algorithm, hide one zero at random in each column. Now erase one uniformly chosen column's zero. A *single bit* distinguishes the two answers. A classical algorithm that reads a small fraction of the $m^2$ bits is unlikely to find it. On the quantum side one can search for a zero in a proposed column in about $\sqrt m$ queries, and search among $m$ columns in about $\sqrt m$ such tests. The costs multiply. Up to logarithmic factors the quantum cost is $m$ [@ABK2016, §3.1].

What information could we add to this matrix to bring the quantum cost down to $\sqrt m$, yet keep the classical cost close to $m^2$? Give each column a certificate with a pointer to a zero in each of its rivals. A pair of columns can then meet in a contest: inspect just their claims against each other. An all-one column with honest pointers can answer any such challenge. A useful certificate left at a known location, however, would give the classical algorithm more information too. So put each certificate at an address that is cheap to compute quantumly and hard even to guess classically. This defines a *new* total function: it asks whether a column has an all-one string **and** a valid certificate at its true address.

OpenAI proved that the new functions attain the optimal separation exponent [@OpenAI2026, Theorem 1.1].[^ai] Write $Q$ and $R$ for quantum and randomized query complexity. For each fixed integer $k\ge2$ and all sufficiently large powers of four $m$, the same function satisfies
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6,
\qquad
R(F_{k,m})\ge \frac{m^{2-1/k}}{400(\log_2m)^2}.
$$
Here $m$ counts columns and $k$ controls the difficulty of one address problem. Ignoring logarithms, $m^{2-1/k}$ is the $(4-2/k)$th power of $\sqrt m$. For $k=2,3,4$ these powers are $3,10/3,7/2$. Across the family they approach four, the exponent in the universal upper bound of Aaronson, Ben-David, Kothari, Rao and Tal [@ABKRT2020]. These authors conjectured that three might suffice; the older balanced AND–OR cheat-sheet analysis reached a cube even with nearly optimal address problems. [Appendix A.2](#earlier-recipe) explains that limitation. The numerical coefficient and logarithmic power above come from the reconstruction.

A query reads one input bit, with computation between queries free. A quantum algorithm may apply a bit query in superposition. Both complexities use the least worst-case query budget giving error at most $1/3$ on each input. For a partial function only certain inputs, its *promise*, have prescribed answers, but its query budget holds everywhere. We assume finite-dimensional linear algebra, conditional probability and asymptotic notation; no quantum algorithm is assumed. We will use the hard-address lower bound, finite minimax and the universal quartic upper bound as inputs. For background on the model see [@BuhrmanDeWolf2002, §3; @deWolf2026, chapters 1, 2 and 7].

\clearpage

# 2. What can one column say about another?

[]{#base-board}In Figure 1 the column strings are $1111$, $0111$, $1011$ and $1101$. Column $1$'s address is $10$. Start at its cell marked $10$ and follow the three solid pointers. They reach $X_2[1]=0$, $X_3[2]=0$ and $X_4[3]=0$. Now follow the dashed pointer back from column $3$. It could land *anywhere* in column $1$ and it would still find a one. Two columns with all-one strings could never both produce the required pointers against each other.

![The four-column example. A cell label selects a box in its own column; a pointer from that box selects a row in another column. Column 1 wins.](figures/exposition/fig2_board.svg){width=92%}

We have drawn four cells so that every possible address fits on the page. Each column supplies two inputs to a partial Boolean function $P$. Their answers select its cell. If either is unpromised, there is no true cell. The full family uses $20\log_2m$ address bits, already forty at $m=4$.

How can one cell certify that it is the right one? For each address input it supplies every gate value of a public circuit. The circuit reports a *domain bit* (one if promised) and a *value bit* (the answer, zero if unpromised). In a winning cell every gate value must be correct, every domain bit one, and the value bits must spell its address. The column itself must be all ones and its pointers must reach zeros in all rivals. Every board, including one with false certificates, now has a definite answer.

In Figure 1 the transcripts are accurate. Columns $1,3,4$ have address $10$; column $2$'s first address input is unpromised and its second has answer zero. In every cell, a pointer into column $2,3$ or $4$ names its zero. A pointer into column $1$ names the row encoded by its own cell's address ($00$ through $11$ stand for rows $1$ through $4$).

**A first tournament.** Return to Figure 1. Suppose for the moment that each column can propose an address, and that column $1$ supplies its true label $10$. Compare two of them by following their pointers into one another. A zero disqualifies the column where it lies; choose the smaller index if both or neither are disqualified. Change just the pointer from this cell into column $2$ to row $2$, a one. Neither side can now disqualify the other, so the index rule still chooses $1$. It beats the remaining rivals too. Could we accept it as the winner? That very pointer is false. We can use comparisons to choose *whom to check*, but must ultimately check the certificate.

Restore Figure 1. This time change three pointers *between losers*, in every cell of the relevant columns. Let $2$ point to row $1$ of $4$, let $3$ point to row $2$ of $2$, and let $4$ point to row $1$ of $3$. In the match between $2$ and $3$, the first points to $X_3[2]=0$ while the second points to $X_2[2]=1$. Column $2$ wins. The other two matches complete the directed cycle in Figure 2. The comparisons between losers give no order in which to search.

![An arrow goes from the victor to the loser. Column 1 beats all three rivals. Each rival beats one of the other two. The dot in a pointer subscript denotes every cell in that column.](figures/exposition/fig3_tournament.svg){width=53%}

Choose a column uniformly as a pivot, keep it, and consider next the columns that beat it. Before calculating, try pivot $2$ in the figure. Which columns are still eligible? They are $1$ and $4$. For pivots $1,2,3,4$ the four survivor counts are $0,2,2,2$, averaging $3/2$. When nobody survives, the winner is already on the list.

Would this mean change if we reversed an arrow between two losers? Across all choices of pivot, each unordered pair contributes *one* survivor: the better of the two survives when the other is pivot. Reversing their match transfers the contribution from one choice of pivot to the other. Thus any fixed tournament of $m$ columns leaves on average $\binom m2/m=(m-1)/2$ after the first pivot. This gives us a reason to try searching by comparisons before paying to check whole certificates. To use it on the real board we need to answer two questions. How cheaply can a column find its own pointers? And what becomes of the survivor count if a comparison is random?

# 3. Reading an address

To reach a pointer, column $1$ first needs to find cell $10$. What can a single query tell us about a whole block of address bits? Start with the three inputs whose answers, or lack of one, determined the addresses in Figure 1.

Forrelation measures agreement between one sign pattern and the Walsh transform of another [@AA2018]. In the four-row example, split eight bits into two blocks of four and turn each bit $x$ into the sign $(-1)^x$. With $z_1,z_2$ the resulting sign vectors, set
$$
W=\begin{pmatrix}1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1\end{pmatrix},
\qquad H=W/2,\qquad
\Phi=\left\langle z_1/2, H(z_2/2)\right\rangle .
$$
The rows of $W$ are orthogonal and have norm two, so $H$ preserves lengths. Fix the second block to be $1000$, that is, $g=(-1,1,1,1)$. Multiplying gives $Wg=(2,-2,-2,-2)$. We can now read the three inputs used in Figure 1.

| Address input | Relation of $z_1/2$ to $H(g/2)$ | $\Phi$ | $P$ |
| --- | --- | --- | --- |
| $a^+=0111\,1000$ | equal | $1$ | $1$ |
| $a^0=0100\,1000$ | orthogonal | $0$ | $0$ |
| $a^-=1000\,1000$ | opposite | $-1$ | undefined |

On the board in Figure 1, column $1$ uses $(a^+,a^0)$ and column $2$ uses $(a^-,a^0)$. The promised cases, at this size, are $\Phi\ge2^{-10}$ and $|\Phi|\le2^{-11}$. In particular a large negative correlation is outside the promise. Its sign matters to certification.

**A two-query experiment.** A quantum state is a unit vector, with a basis vector $|j\rangle$ for each possible index. A measurement in that basis returns $j$ with probability equal to the squared modulus of its coefficient. One bit query flips an answer bit $b$ at each position $j$ where $x_j=1$, extending the rule $|j,b\rangle\mapsto|j,b\oplus x_j\rangle$ linearly. Give it the answer state $(|0\rangle-|1\rangle)/\sqrt2$. A flip reverses the sign of this vector. Thus one query multiplies *each amplitude* at position $j$ by $(-1)^{x_j}$, leaving the answer state available for reuse. Write $D_z$ for this diagonal operation.

Start with $u=(1,1,1,1)/2$. Query the second block, apply $H$, then query the first block. On $a^+$ the successive position states are
$$
u\ \longmapsto\ \tfrac12(-1,1,1,1)
\ \longmapsto\ \tfrac12(1,-1,-1,-1)
\ \longmapsto\ u .
$$
Asking whether the final state lies along $u$ succeeds with probability $|u^{\mathsf T}D_{z_1}HD_{z_2}u|^2=\Phi^2$. Concretely, apply $H$ once more and measure the first basis outcome, since $Hu=(1,0,0,0)$. This last transform costs no queries. On $a^0$ the success probability is zero. On $a^-$ the final state is $-u$ and the success probability is one. The decoder can therefore suggest the *same* first bit for columns $1$ and $2$ with certainty on our example. Only column $1$ has a true address. The projection sees the square of the correlation; it works as a decoder on the promise, yet can suggest a confident answer outside it.

[]{#domain-bit-board}**When a zero is not an answer.** Return to Figure 1. Give column $1$ a zero in its first row, erase column $2$'s zero, and point every pointer into column $1$ at row $1$. Would column $2$ win at $00$? All its pointers now find zeros. Its transcripts are accurate and their value bits spell $00$. But its first value bit is zero because its input is *unpromised*. The first domain bit exposes the mistake. Nobody wins on this board.

**The three scales.** In the calculation above we queried a block, changed basis, then queried the next block. Repeating this alternation compares a chain of $k$ sign patterns. In the full construction $m=4^t$, $t\ge1$, and each address input has $k$ blocks of length $m$. The normalized Walsh matrix has entries $H_{ab}=(-1)^{a\cdot b}/\sqrt m$ for binary indices of length $2t$. With $u=(1,\ldots,1)/\sqrt m$, put
$$
\Phi=u^{\mathsf T}D_{z_1}HD_{z_2}H\cdots HD_{z_k}u,\qquad \delta=2^{-5k}.
$$
The answer is $1$ for $\Phi\ge\delta$ and $0$ for $|\Phi|\le\delta/2$, and is undefined elsewhere. We need three facts about this one partial function.

* To **propose an address bit**, the preceding experiment takes $k$ queries, one per block. On promised inputs its success probability is either at least $\delta^2$ or at most $\delta^2/4$. Independent trials distinguish these ranges with error $\eta$ in $O_k(\log(1/\eta))$ queries. The constant can grow quickly with $k$. [Appendix A.5](#decoder-repetitions) gives the count.
* To **certify an address bit**, a circuit can compute the signed numerator of $\Phi$ exactly by Walsh additions and subtractions and compare it with the two thresholds. Its size is $O_k(m(\log_2m)^2)$. A claimed transcript can therefore expose a false answer through a local gate or output check. We count these checks when we verify a candidate. [Appendix A.6](#exact-certification) gives the integer calculation.
* To **discover an address bit classically**, Bansal and Sinha's lower bound [@BansalSinha2021, Theorem 1.3 and Corollary 1.4] gives $R(P)>L$ for all sufficiently large $m$ at fixed $k$, where, writing $\ell=\log_2m$,
$$
L=\left\lfloor m^{1-1/k}/\ell^2\right\rfloor.
$$
The small board illustrates the operations only. The classical hardness is a theorem about arbitrarily large blocks.

Figure 3 shows how these inputs fit together at full size. Each of the $m$ columns has its own array of cells. The $r=20\ell$ answers select one of $2^r=m^{20}$ cells; a pointer in that cell uses only $\ell$ bits to select a row of a rival. Thus even this enormous array has polynomial size in $m$. The actual length of the input includes the cells of every column and is much greater than $m$; the query model charges for the coordinates used. Addressed certificates come from cheat sheets [@ABK2016, §3.1] and direct pointers to other columns' zeros from pointer functions [@GPW2018; @ABBLSS2017]. OpenAI puts its outward pointers inside each addressed cell [@OpenAI2026, §2].

![At full size each column has the same fields. On a winning column the true address answers select the cell shown. Its pointers reach into other columns' strings, while its circuit transcripts certify the address inputs in its own column.](figures/exposition/fig1_column.svg){width=90%}

# 4. The quantum algorithm: a tournament

## 4.1 What a comparison decides

Use the decoder of Section 3 to supply the proposed addresses for our two-pointer comparison. Even an unpromised input yields a label pointing to an actual cell. Fix one experiment for each unordered pair; exchanging the names of the rivals simply exchanges its two possible outcomes. Hence for $a_{ij}=\Pr(i\text{ beats }j)$,
$$
a_{ij}+a_{ji}=1\quad(i\ne j).
$$

By convention, a column loses to itself, so $a_{ii}=0$. If $i$ genuinely wins the board, no pointer can find a zero in $X_i$, whatever a rival's decoder produces. Once $i$ decodes its own address correctly its pointer finds a zero in every rival. Giving each of its $r$ decodings error at most $\varepsilon/r$ therefore gives $a_{ij}\ge1-\varepsilon$ against each rival.

Quantum minimum-finding requires an order [@DH1996]. Here even a repeated match between two losers may have no preferred outcome. Bounded-error tests for a fixed edge orientation [@HMW2003] cannot represent a fair coin flip.

## 4.2 How much survives a pivot?

In Figure 2 a survivor beat every earlier pivot. With random comparisons we can still ask how often column $i$ would do so. Its weight $w_i$ is the probability of beating all the pivots in fresh, independent comparisons. Even a nonwinner can have weight one, as the column with the false pointer showed. Initially every weight is one. The natural extension of uniform choice among survivors is to draw $p$ with probability $w_p/|w|$, where $|w|=\sum_iw_i$. Keep $p$ on the list. Beating it is one additional requirement, so $w_i'=w_i a_{ip}$; in particular the pivot's own weight vanishes. If every weight vanishes, keep the current list. This ideal experiment uses probabilities inaccessible to the algorithm.

Why should the ideal experiment make progress? For each unordered pair $i,p$ there are two contributions to the expected remaining weight. Drawing $p$ as pivot leaves $w_i a_{ip}$ from $i$; drawing $i$ leaves $w_p a_{pi}$ from $p$. After multiplying by their respective selection probabilities, their combined contribution is $w_iw_p/|w|$, whatever happens in the comparison. For $|w|>0$ this gives
$$
\mathbb E[|w'|\mid w]
=\frac{\sum_{i<p}w_iw_p}{|w|}
=\frac{|w|^2-\sum_iw_i^2}{2|w|}
\le\frac{|w|}{2}.
$$
The missing diagonal explains the $-1$ in $(m-1)/2$: a pivot cannot survive itself. For four equal initial weights the formula gives $(16-4)/8=3/2$, just as on our cycle. The same equality holds if all six comparisons between distinct pairs are fair coin flips. It is *total weight*, rather than the number of surviving columns, that the proof can halve.

After $T$ stages, $\mathbb E|w_T|\le m2^{-T}$. Against any list of $T$ or fewer other pivots the genuine winner still has weight at least $(1-\varepsilon)^T\ge1-T\varepsilon$. Take $T=\lceil\log_2(1000m)\rceil$ and $\varepsilon=1/(1000T)$. An unlisted winner would account, by itself, for more than $1/2$ of a unit of weight. Hence
$$
\Pr(\text{winner missing from the list})
\le\Pr(|w_T|>1/2)\le 2m2^{-T}\le1/500 .
$$
The same lower bound on the unlisted winner's weight will pay for sampling: while it is missing, at least half a unit of weight remains to be found. The pivot method for fixed orientations [@AIK2026v3, §§4 and 6.1] has thus given a target law even for random comparisons. How could we draw a label with those relative weights without estimating a single $a_{ij}$?

## 4.3 Drawing from weights we cannot compute

Choose $i$ uniformly, compare it afresh with every pivot on the list, and accept it if it wins every comparison. For pivots $p_1,\ldots,p_j$,
$$
\Pr(\text{accept and draw }i)
=\frac{1}{m}\prod_{b=1}^j a_{ip_b}
=\frac{w_i}{m}.
$$
Sum over $i$ to obtain the acceptance probability $q=|w|/m$. Divide by $q$ to obtain the ideal pivot law $w_i/|w|$. The comparisons have done the weighting for us.

Try this with four columns and pivot $2$, now letting the four win probabilities be $(1,0,1/2,1/4)$ instead of the fixed arrows in Figure 2. Among successful trials, how often should column $3$ appear? It is proposed a quarter of the time and accepted on half of those trials. The four masses of acceptance are $(1/4,0,1/8,1/16)$, summing to $7/16$. Thus column $3$ appears on $(1/8)/(7/16)=2/7$ of successes. The full conditional law is $(4/7,0,2/7,1/7)$. Uniform choice among the three positive labels would already differ on the second pivot.

Independent rejection trials would cost $1/q$ attempts on average. Near the end of the tournament only a single column may retain much weight, and $1/q$ can be as large as order $m$ even with the winner still to find. Quantum amplitude amplification reduces the number of attempts. There is a distribution to preserve as well as a probability to increase.

Prepare a uniform superposition of the column labels and, controlled by each label $i$, run its comparisons with the earlier pivots in fresh registers. Retain the answers and compute a final bit indicating whether all comparisons were won. Conditional on $i$, squared amplitudes in distinct comparison registers multiply, so the mass on label $i$ with final bit one is exactly $w_i/m$. All operations so far are reversible. Write the resulting unit vector as
$$
\sin\theta\,g+\cos\theta\,b,\qquad \sin^2\theta=q,
$$
where $g$ is the normalized projection onto final bit one and $b$ the projection onto final bit zero, normalized likewise ($0<q<1$). Think of $g$ as one vector carrying all the successful labels in their correct proportions. A reflection that negates the successful states followed by a reflection about the initially prepared vector rotates their plane. After $v$ pairs of reflections the state is
$$
\sin((2v+1)\theta)\,g+\cos((2v+1)\theta)\,b .
$$
Only the *coefficient* of $g$ has changed. Measuring the label conditional on success still gives the probabilities within $g$, including the unequal probabilities we just calculated. A random iteration count or stopping on the first success of several fresh trials mixes copies of that same law [@BHMT2002, Lemma 1; @deWolf2026, chapter 7].

\Needspace{6\baselineskip}

Back on the deterministic board of Figure 2, try choosing pivots $2$ and then $4$. Only column $1$ beats both. Here $q=1/4$ and $\theta=\pi/6$. One rotation gives success probability $\sin^2(3\pi/6)=1$; a second brings it back to $1/4$. Since $q$ is unknown, the algorithm uses a bounded schedule of random rotation counts. With $O(\sqrt m\log(1/\varepsilon))$ preparations and inverses it succeeds except with probability $\varepsilon$ whenever $q\ge1/(2m)$ [@BBHT1998, Lemma 2]. It always stops within that cap. [Appendix A.3](#amplification-schedule) derives the schedule, including the reflection that uses the inverse preparation.

Append each successful measured label, stopping on failure or after $T$ pivots. Until the winner is listed, its weight exceeds $1/2$, so $q\ge1/(2m)$ and the success guarantee applies. We can draw the same label in the ideal and actual processes whenever the actual sampler succeeds, because its conditional law is exactly right. Over at most $T$ stages the chance of a failure before listing the winner is at most $T\varepsilon$. A failure *after* listing it costs nothing. For instance, once the list on Figure 2 is $(2,4,1)$, nobody can beat all three and nothing more need be found.

## 4.4 Checking the list

A full check would have been costly inside every comparison. Now we need it only for a listed column. Decode its address afresh and inspect the cell at that label. If a transcript contains a false gate value, take the *first* false value in gate order. Its predecessors are correct, so this gate violates its equation. Conversely, passing every gate test forces the whole evaluation to be correct. The domain and value bits must then agree with the claim that these inputs are promised and select this cell.

With $S$ gates per circuit, $m$ string tests, $m-1$ pointer tests, $rS$ gate equations and $2r$ output tests suffice. Each gate test reads at most three bits. Following a pointer reads its $\ell$ bits and the named string bit. Thus there are $K=2m-1+r(S+2)=O_k(m\ell^3)$ local tests, each costing $O(\ell)$ queries, and every nonwinner fails some test at every address. The number $2^r$ of possible cells has dropped out: we search the tests for the one cell our candidate actually claims.

Search for a violation in that cell. A uniform test finds a violation with probability at least $1/K$ if any exists, so the same bounded amplification searches for one using $O(\sqrt K\log(1/\varepsilon))$ test evaluations. Accept the board if any listed column passes. On a $0$-board every candidate, at any decoded address, has a defect. Each search misses a defect with probability at most $\varepsilon$. With at most $T$ searches the total probability of a false acceptance is at most $T\varepsilon$. On a $1$-board the list misses its winner with probability at most $1/500+T\varepsilon$. Decoding the winner's address incorrectly adds at most $\varepsilon$ more. At its correct address all tests pass.

What costs a power of $m$ here? Sampling a pivot takes order $\sqrt m$ preparations up to logarithms. Each preparation uses at most $T$ comparisons, each comparison only a polylogarithmic number of queries. Checking one candidate costs order $\sqrt K$, again up to logarithms, and $K=O_k(m(\log m)^3)$. There are at most $T=O(\log m)$ candidates. Thus both stages fit within $\widetilde O_k(\sqrt m)$ queries, where the tilde suppresses powers of $\log m$. The [full count](#quantum-query-count) gives $C_k\sqrt m(\log_2m)^6$. The expensive certificate search has moved outside the search for candidates.

# 5. Where a classical algorithm would have to look


Return to the hidden-zero matrix. On the quantum side an all-one string protected its owner from every incoming pointer. Here it lets us create a winning string by erasing one zero. On the enlarged board we must also plant a certificate. Start with every cell blank and fill just the selected column's true cell.

Fix $k$ and take $m$ large enough that $1\le L<R(P)$, with $L$ as in Section 3. By finite minimax there is one distribution $\mu$ on promised inputs of $P$ under which *every* deterministic $L$-query algorithm has success at most $2/3$ [@Yao1977]. Draw all the address inputs independently from $\mu$. In each string put its zero at an independent uniform position $J_i$. This produces the losing board $Y^0$. Draw the planted column $I$ uniformly and independently of the entire board, and make the two changes just described to get $Y^1$.

If each column's true address were public, the first domain bit in each of $m$ cells would separate the two boards: blank cells give zero, the planted transcript gives one. Hiding the address blocks that shortcut.

Figure 4 shows the two changes. The planted cell also reveals other columns' zero locations. Count queries on the losing board, where no cell leaks this information. Fix the algorithm's coins. On the two boards it asks exactly the same queries until the first differing answer, so it suffices to count any visit to the erased zero or the filled cell on the losing run. This run is independent of $I$. Let $G$ be the budget. Call a column *heavy* if the whole run spends more than $L$ queries on its address inputs and *light* otherwise.

| A hit on the losing run | Upper bound |
| --- | --- |
| The run discovers the zero of the selected column. | $4G/m^2$ |
| The selected column is heavy. | $G/(mL)$ |
| The selected column is light and the run visits its true cell. | $G(2/3)^r$ |

**The hidden zero.** Suppose the run has yet to find the zero of column $i$. Given what it has seen, the zero is uniform among the unread rows of $X_i$: moving it from one unread position to another preserves every answer and hence every choice so far. While fewer than half of that column's rows have been read, the next query finds the zero with probability at most $2/m$. That gives at most $2G/m$ early discoveries in expectation over the whole board. A later discovery requires at least $m/2$ previous reads *in its own column*, and the budget allows at most $2G/m$ such columns. If the run finds $Z$ zeros, the independently planted column is among them with probability $Z/m$. Averaging gives the first row of the table. The second follows from the same counting principle: more than $L$ address queries per heavy column leave at most $G/L$ heavy columns.

![Planting column 1 in a four-column board. The address inputs stay the same. Erase the zero in row 4 of column 1 and fill cell 10 with the certificates and pointers it needs. The reader sees the locations of both changes.](figures/exposition/fig4_planted.svg){width=90%}

\Needspace{5\baselineskip}

**The hidden cell.** Stop a run just as it specifies the coordinate $(i,10,u)$: bit $u$ in cell $10$ of column $i$. What prediction has it already made? If this is the true cell, both address answers must be $(1,0)$. The cell has yet to supply a bit. A predictor can simply intercept the coordinate and return its label. The only difficulty is reproducing the query within the predictor's own budget.

Consider one proposed query time $j$ and one column $i$. Imagine being handed the $r$ hidden address inputs of that column, with the task of predicting their answers. You can sample the rest of the losing board yourself: all other address inputs and all zero locations are independent of these $r$ inputs, and all cells are blank. Start the algorithm on this board. Answer its queries from what you sampled, except that a query to one of the hidden inputs must be forwarded and paid for. Stop *before* forwarding an $(L+1)$st such query. If the algorithm proposes $(i,s,u)$ at time $j$, output $s$ immediately, without reading that bit. On any other ending output a fixed address.

Try a run with two address inputs, one allowed target read and $j=4$. At time $1$ answer a string query from your simulated board. At time $2$ forward a query to the first address input. You have spent your one read. At time $3$ a query to another column still costs you nothing: answer it. If the fourth query is $(i,10,u)$, return $10$. If the third query had asked for the second address input instead, you would have stopped *there*, before seeing the answer. The algorithm's clock counts every query; your cap counts only those to the hidden tuple.

On any run where $i$ is light, you can reproduce all choices up to time $j$. Thus
$$
\{i\text{ light and query }j\text{ in its true cell}\}
\ \subseteq\
\{\text{the capped procedure predicts all }r\text{ answers}\}.
$$
A prediction can succeed in other ways, including a lucky default on a stopped run. This direction of inclusion is precisely what we need. The probability on the right is taken over the original independent samples. Conditioning first on a run being light could bias those samples toward easy ones.

The separate-cap direct-product lemma bounds that prediction probability by $(2/3)^r$ [@Shaltiel2003; @Drucker2012]. In detail, when each sample separately admits at most $\beta$ success in $L$ queries, a procedure with *at most $L$ queries to each sample on every run* predicts all $r$ independent answers with probability at most $\beta^r$. It can interleave the queries and use jointly independent side information. Our procedure makes at most $L$ forwarded queries in total, so it meets every separate cap.

Why does interleaving the queries across samples preserve the product bound? Fix the side information, the coins and a possible query history. Agreement with that history restricts each input through its own revealed bits, so the remaining input laws factor. Give each input a value: its best chance of a correct prediction with its remaining allowance. A query to one input leaves the others' values unchanged. On average it cannot increase the queried input's value either, since “ask this query, then continue optimally” was already one available strategy. The *product* of the values therefore cannot increase in expectation. It starts at most $\beta^r$ and at a leaf bounds the probability that the entire guess is correct. [Appendix B](#direct-product-proof) gives the details.

For fixed $i$, summing over the $G$ opportunities for a correct visit costs a factor $G$. To ask whether the *selected* column was visited we average this bound over $I$, giving $G(2/3)^r$ again. The address length balances two constraints: polynomially many cells on the board and polynomially many chances to guess. The same choice $r=20\log_2m$ gives $2^r=m^{20}$ on the storage side and $(2/3)^r\le m^{-10}$ per guess on the prediction side.

[]{#classical-finish}Putting the three charges together, the probability of different outputs on the two boards is at most
$$
\frac{4G}{m^2}+\frac{G}{mL}+G(2/3)^r .
$$
Take $G=\lfloor mL/100\rfloor$. Since $L\le m$, the three terms sum to at most $4/100+1/100+1/(100m^8)<1/3$. The same bound holds after averaging over the algorithm's coins. Yet success $2/3$ on every input requires acceptance probability at least $2/3$ on the winning boards and at most $1/3$ on the losing boards. That gap requires different outputs with probability at least $1/3$ in our paired experiment. Hence $R(F_{k,m})>\lfloor mL/100\rfloor$.

\clearpage

# 6. Why the exponent is four

The universal exponent asks for a *single* power $\alpha$ and constant $C$ such that $R(f)\le C(1+Q(f))^\alpha$ for every total Boolean function $f$. Write $\alpha_{\rm tot}$ for the infimum of such nonnegative exponents. To see how the construction rules a power out, try $\alpha=3$. With $k=3$ the classical exponent in $m$ is $2-1/3=5/3$, whereas cubing the quantum bound gives only $3/2$. The surplus $1/6$ of a power of $m$ eventually outweighs any fixed power of its logarithm.

The same calculation works against any $0\le\alpha<4$. Choose an integer $k\ge2$ with $1/k<(4-\alpha)/2$. Now *hold $k$ fixed*. The constant in the quantum decoder and the size threshold in the classical hardness theorem can both depend on it. For large enough $m$, the floor in $L$ costs at most a factor two, giving the lower bound with coefficient $1/400$ stated in Section 1. The ratio of the two sides then satisfies
$$
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
\ \ge\ c_{k,\alpha}\,
\frac{m^{2-1/k-\alpha/2}}{(\log_2m)^{2+6\alpha}}
\ \longrightarrow\ \infty .
$$
The surplus power is positive by our choice of $k$. No uniform constant $C$ can work. In the other direction, the universal bound of Aaronson, Ben-David, Kothari, Rao and Tal, building on Huang's sensitivity theorem [@ABKRT2020; @Huang2019], gives deterministic query complexity $D(f)=O(Q(f)^4)$ for total functions. Since $R(f)\le D(f)$, four suffices. Thus $\alpha_{\rm tot}=4$.

Compare the final construction with the bare matrix. Erasing a zero still makes one string all ones, and a classical algorithm that misses the erased bit still has to find a change somewhere else. The outward pointers create exactly such a change, a certificate that can challenge every rival. Hiding that certificate behind independent address problems preserves a classical cost of order $mL$. Even a guess that reaches the right cell has specified all its address answers before the first bit comes back.

Those same pointers let the quantum algorithm replace its nested search. A cheap address proposal lets a column read just the pointer relevant to its current opponent. The winner's weight stays high enough both to put it on the short list and to make sampling the next pivot affordable. Only the columns on that list need a full certificate check. On one side nearly $m$ queries' worth of classical work can be hidden in each of $m$ possible columns; on the other, comparison and verification each cost about $\sqrt m$, and their costs add.

[^ai]: The theorem and construction are OpenAI's. This exposition and its Lean development were prepared with AI systems under the author's direction.

\clearpage

# Appendix A. Supporting calculations {.unnumbered}

[]{#quantum-query-count}

## A.1 Counting the quantum queries

The main quantum argument in Section 4 uses the following count. It charges the same comparisons and local tests on every branch; early stopping can only reduce the cost.

A coherent test evaluation works on a superposition of test labels. It computes the next input position reversibly and retains earlier answers. To implement a read that is active only on some branches, query $x_j$ into a temporary bit, conditionally copy it to the answer bit, then query $j$ again to clear the temporary bit. This uses two ordinary oracle calls; on an inactive branch the answer and temporary bits are both restored. Padding to a common number of these controlled reads therefore has a fixed cap even in superposition. Running the computation backwards then restores its workspace. This implements the same tests using $O(\ell+1)$ bit queries per evaluation; [the controlled-read construction](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md#AC-coherent) gives the controlled implementation. No full transcript is read during a single test.

**The count.** Early stopping and randomized iteration counts make the number of queries depend on the run. The caps are fixed in advance and hold on every input and branch. A comparison uses $O_k(r\log(r/\varepsilon))$ queries for its decoders and $O(\ell+1)$ for its pointers, including the constant overhead of a reversible implementation. We count the tournament first, then verification.

Each stage uses $O(\sqrt m\log(1/\varepsilon))$ preparations, and each preparation makes at most $T$ comparisons. There are at most $T$ stages. Multiplying these three factors bounds the entire tournament by $O(\sqrt m\,T^2\log(1/\varepsilon))$ comparisons.

Verification makes at most $T$ fresh address decodings. For each candidate it searches the $K$ local tests, using $O(\sqrt K\log(1/\varepsilon))$ test evaluations. Thus the list requires $O(T\sqrt K\log(1/\varepsilon))$ test evaluations in all.

In bit-query units the two costs add:
$$
O_k\!\left(\sqrt m\,T^2\log(1/\varepsilon)
 [r\log(r/\varepsilon)+\ell]
 +T[r\log(r/\varepsilon)+\sqrt K\log(1/\varepsilon)\ell]\right).
$$
The first bracket charges comparisons; the second charges fresh address decoding and local-test search. Here $r,T,1/\varepsilon=O(\ell)$ and $K=O_k(m\ell^3)$. Bounding $\log(1/\varepsilon)=O(\ell)$, $\log(r/\varepsilon)=O(\ell^2)$ and $\sqrt K=O_k(\sqrt m\,\ell^2)$ deliberately enlarges the logarithms and square root. These substitutions give $O_k(\sqrt m\,\ell^6)$ for the tournament and $O_k(\sqrt m\,\ell^5)$ for verification ([the explicit count](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md#upper-explicit-log6)). Therefore
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6.
$$
The tournament and short-list verification costs add, in place of the earlier nested search product $\sqrt m\sqrt K$. Here $m$ counts columns. The exponent six is an artefact of this loose count. Square-root dependence comes from amplifying pivot sampling and searching the local tests. The short list limits how many verifications are needed; it is the quantum half of the exponent calculation.

[]{#earlier-recipe}

## A.2 Why the balanced AND–OR recipe stops at a cube

In the cheat-sheet construction [@ABK2016, §3.1], each of the $n$ input bits of a partial function $g$ is replaced by the answer to its own AND–OR instance on $n^2$ bits, for $n^3$ bits overall before adding certificates. In one instance, write the bits as $n$ rows of $n$ bits; its answer is $1$ exactly when every row contains a $1$. A $1$-certificate selects one $1$ in every row; a $0$-certificate selects one entire zero row. Thus either answer has a certificate of $n$ bits. Reading those certificates determines the $n$-bit vector supplied to $g$; the fixed domain predicate of $g$ can then be checked by free computation. The certificate reads remain charged.

Up to logarithmic factors, the cited composition and cheat-sheet argument supplies randomized lower bound $R(g)n^2$ and quantum upper bound $n$ when $Q(g)$ is polylogarithmic in $n$. Reading all $n$ bits gives $R(g)\le n$, so this calculation reaches at most a cubic separation. Ben-David's earlier Forrelation construction [-@BenDavid2015] and cheat sheets first gave power $5/2$; Tal [-@Tal2020] reached $8/3-o(1)$, and the nearly linear partial-function bounds of Bansal and Sinha [-@BansalSinha2021] and Sherstov, Storozhenko and Wu [-@SSW2023] gave $3-o(1)$. In the present construction, an address instance has about $m$ bits while the quantum search costs about $\sqrt m$. The partial-function hardness can therefore contribute almost two powers of the quantum cost. Section 4 explains how comparisons make that square-root search possible.

Certificate complexity is a separate measure: it counts the bits needed to force a function value. Ben-David and Kothari construct total functions for which randomized evaluation beats this measure [@BDK2026, §§2–3]. Their card encoding and the fixed-graph search cited in Section 4 are related constructions, not inputs to the randomized–quantum bound proved here.

\Needspace{8\baselineskip}

[]{#amplification-schedule}

## A.3 The amplification rotation and a finite schedule

For $0<q<1$, write $A|0\rangle=\sin\theta\,g+\cos\theta\,b$ as in Section 4.3. Here $A$ includes the index, all comparison registers and the final success flag. To reflect about $A|0\rangle$, apply $A^{-1}$, reflect about $|0\rangle$, and apply $A$ again. Retaining the decoder and pointer-read registers makes this inverse possible and gives it the same query cost as $A$. The two reflections act on the plane spanned by these orthonormal success and failure vectors. In the ordered orthonormal basis $(g,b)$, the success phase flip and the reflection about $A|0\rangle$ have matrices
$$
S=\begin{pmatrix}-1&0\\0&1\end{pmatrix},\qquad
R_{A0}=\begin{pmatrix}-\cos2\theta&\sin2\theta\\\sin2\theta&\cos2\theta\end{pmatrix}.
$$
Their product $R_{A0}S=\left(\begin{smallmatrix}\cos2\theta&\sin2\theta\\-\sin2\theta&\cos2\theta\end{smallmatrix}\right)$ sends $(\sin\theta,\cos\theta)$ to $(\sin3\theta,\cos3\theta)$. This calculation gives the rotation formula used in Section 4.3. It changes the total successful amplitude, leaving the normalized successful state unchanged.

Section 4 needs both a cap on every input and the conditional label law of Section 4.3. Set $M=\lceil10/\sqrt\gamma\rceil$ and $N=\lceil\ln(1/\eta)/\ln(40/31)\rceil$. In each fresh trial use zero iterations with probability $1/2$, and otherwise choose $v$ uniformly from $0,\ldots,M-1$. Stop at the first acceptance, or after $N$ failures. Each trial uses at most $2M+1$ calls to $A$ or $A^{-1}$, so $N(2M+1)$ is an all-input cap.

To bound the failure probability, first suppose $\gamma\le q\le1/2$. Averaging the rotation formula gives [@BBHT1998, Lemma 2]
$$
\frac1M\sum_{v=0}^{M-1}\sin^2((2v+1)\theta)
=\frac12-\frac{\sin(4M\theta)}{4M\sin(2\theta)}
\ge\frac12-\frac1{4M\sqrt{2\gamma}}\ge\frac9{20},
$$
since $\sin(2\theta)=2\sqrt{q(1-q)}\ge\sqrt{2\gamma}$. Thus the randomized-iteration branch alone contributes at least $9/40$ to the trial's acceptance probability. If $q\ge1/2$, the zero-iteration branch contributes at least $q/2\ge1/4$. In either case, $N$ fresh trials all fail with probability at most $(31/40)^N\le\eta$. Each successful trial has the label law derived in Section 4.3, so stopping at the first success preserves it. If $q<\gamma$, the cap still holds, although the acceptance guarantee need not.

\Needspace{8\baselineskip}

## A.4 The small circuit and its local tests

[]{#circuit-check}*Optional circuit census.* The [explicit circuit for the four-column board](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md#AC-example-promise) has $S=180$ non-input gates, so each candidate has $K=4+3+2(180+2)=371$ tests. In its zero-based numbering, input bits $6$ and $7$ feed gates $1$ and $2$: they compute $u=\neg x$, then $v=u\lor y$. On $a^+$ these last two input bits are both zero. To test gate $2$, read the proposed $u$, the actual $y$ and the proposed $v$. Reading $(1,0,0)$ exposes a false gate value, since $1\lor0=1$. The domain and value outputs are gates $178$ and $179$. Every cell contains $6$ pointer bits and $360$ transcript bits. With four cells in each of four columns, the full board has $4[4+16+4(6+360)]=5936$ input bits. Only one cell enters the tests for a given candidate. This toy uses $r=2$; the separation family uses $r=40$ when $m=4$, and its classical lower bound requires much larger $m$.

[]{#decoder-repetitions}

## A.5 Repeating the projection experiment

For any requested error $0<\eta<1/2$, the projection experiment of Section 3 extends to every $k$. Phase kickback uses one query per sign diagonal, so a trial uses $k$ queries and has projection probability $p=\Phi^2$. On the promise, either $p\ge c=\delta^2$ or $p\le c/4$. Start each trial in fresh registers and repeat independently
$$
\rho=\lceil16c^{-1}\ln(1/\eta)\rceil
$$
times; accept if at least $\rho c/2$ projections succeed. We use the following standard Chernoff estimates for the number $Z$ of successes in these independent Bernoulli trials:

| Promised case | Wrong decision | Tail bound used |
| --- | --- | --- |
| $p\ge c$ | $Z<\rho c/2$ | At most $\exp(-\rho c/8)$, hence at most $\exp(-\rho c/16)$. |
| $p\le c/4$ | $Z\ge\rho c/2$ | At most $\exp(-\rho c/16)$, by the upper tail at $p=c/4$ and monotonicity. |

Thus each error is at most $\eta$. The cap is $k\rho=O_k(\log(1/\eta))$ on every input. The subscript permits constants depending on $k$, here including $c^{-1}=2^{10k}$: cheap means fixed $k$ and growing $m$. Section 4 will retain the trial outcomes coherently instead of measuring them; their measurement probabilities and independence remain the same.

[]{#exact-certification}

## A.6 Exact certification and the input size

The circuit uses integer arithmetic. The two factors $1/\sqrt m$ in $u$ and the $k-1$ internal Walsh factors give $\Phi=N/2^{t(k+1)}$ for an integer $N$. A fast Walsh transform recursively transforms two half-size vectors, then adds and subtracts their corresponding entries. These split-and-combine steps compute the numerator using additions and subtractions, and integer comparisons decide the two thresholds exactly. For example, $\Phi\ge2^{-5k}$ is equivalent to $2^{5k}N\ge2^{t(k+1)}$; the small-value test is $2^{5k+1}|N|\le2^{t(k+1)}$. Words of $O(k\log m)$ bits suffice, including the threshold shifts. The [record's circuit construction](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md#forr_circuit) gives the arithmetic and gate count. The quantum verifier checks a stored computation of this circuit; it does not run the entire circuit on each candidate.

**The hardness allowance.** This is the consequence of the randomized lower bound of Bansal and Sinha for this one-sided promise [-@BansalSinha2021, Theorem 1.3 and Corollary 1.4]. For fixed $k$, the source bound is at least a positive constant depending on $k$ times $m^{1-1/k}/(\log_2(km))^{1-1/k}$. Dividing this by the unfloored expression for $L_{k,m}$ gives a factor of order $(\log m)^{1+1/k}$, which tends to infinity and absorbs the constant.

**Input length.** A column contains $m$ string bits, $rkm$ address-input bits, and $2^r$ cells, each containing $(m-1)\ell$ pointer bits and $rS$ transcript bits. Thus the general function has $n=m\bigl[m+rkm+2^r((m-1)\ell+rS)\bigr]$ input bits, which is $O_k(m^{22}(\log m)^3)$ since $2^r=m^{20}$. Thus the total input length is polynomial in $m$, although much larger than $m$. The three bracketed contributions are the column string, its address inputs, and its cell array. Here $n$ is the actual input length; $m$ controls the displayed query bounds. The comparison is between $R$ and $Q$ for this one function, with the same circuit; neither bound counts the time to read or allocate the whole input.

\Needspace{8\baselineskip}

[]{#direct-product-proof}

# Appendix B. The separate-cap direct product {.unnumbered}

We prove the separate-cap direct-product lemma used in Section 5. The input samples are independent, each has the same hard law, each individual cap holds on every branch, and the coins and side information are jointly independent of the entire tuple.

*Source note.* The separately capped setting goes back to Shaltiel's fair decision trees [-@Shaltiel2003]. The proof below is the conditional-value argument of Drucker's Lemmas 3.1–3.2, whose headline theorem uses one global budget instead [-@Drucker2012, §1.3 and the end of §3].

Fix the coins and side information. By joint independence the samples are still independent with law $\mu$, and the algorithm is a deterministic tree. Take a history $\tau$ of queries and answers that occurs with positive probability. Each recorded answer constrains only its own sample, and because the tree is deterministic, every tuple that agrees with these answers asks exactly these queries. So the tuples consistent with $\tau$ form a product $E_1(\tau)\times\dots\times E_r(\tau)$, and given $\tau$ the samples are independent with laws $\mu(\cdot\mid E_h(\tau))$.

Now measure the best success still available with the budget left. For AND on two independent fair bits with one query allowed, before querying it is $3/4$; after seeing a zero it is $1$, and after seeing a one with no queries left it is $1/2$. Let $q_h(\tau)$ count the queries to $U_h$ in $\tau$, and let $V_h(\tau)$ be the best probability of computing $P(U_h)$ under $\mu(\cdot\mid E_h(\tau))$ with at most $L-q_h(\tau)$ further queries. If the next query reads a bit of $U_h$, then querying it and continuing optimally is one strategy with that allowance, so averaging over the answer $b$,
$$
\sum_b\Pr(b\mid\tau)\,V_h(\tau b)\le V_h(\tau).
$$

One answer may raise $V_h$; only the average cannot. For two independent uniform AND inputs with caps of one query, observing first bit $0$ in $U_1$ gives $E_1=\{00,01\}$ and $E_2=\{00,01,10,11\}$; the second sample is still unrestricted. We have $V_1=V_2=3/4$ at the start; reading the first bit of $U_1$ makes $V_1=1$ or $1/2$ as the bit is $0$ or $1$, and $V_2$ stays $3/4$, so the product averages to $\tfrac12\cdot\tfrac34+\tfrac12\cdot\tfrac38=\tfrac9{16}$, its starting value.

In general the other samples keep their laws and allowances, so their values do not change, and $\prod_hV_h$ has nonincreasing expectation from step to step. It starts at most $\beta^r$. At a leaf with output $s$, the probability of being right given $\tau$ is $\prod_h\Pr(P(U_h)=s_h\mid\tau)\le\prod_hV_h(\tau)$. Averaging over leaves and then over the coins and side information finishes the proof; the query cap and the finite sets of input positions, answers and outputs allow only finitely many deterministic trees. Arbitrary independent randomness therefore reduces to a finite mixture of these behaviours.

Return to the [final gap bound in Section 5](#classical-finish).

# Appendix C. Testing the classical hypotheses {.unnumbered}

The following examples isolate the roles of independent planting, terminal lightness and the query caps. They change the partial function where stated; they are not small hard instances of the asymptotic family.

\Needspace{13\baselineskip}

### Independent planting

The identity $\Pr(\text{erased zero hit})=\mathbb EZ/m$ needs $I$ to be independent of the run. Query one fixed position in each of the four columns, so that $\mathbb EZ=1$ and an independent $I$ is hit with probability $1/4$. Suppose instead that $I$ is chosen uniformly among the columns where a zero was found, and uniformly among all four when none was found, which happens with probability $(3/4)^4=81/256$. By symmetry $I$ is still uniform on its own, but now it is hit whenever some zero was found, with probability $1-(3/4)^4=175/256$. A uniform marginal is a weaker condition than independence from the run, and the proof needs independence.

### Lightness is a joint event

**Why the event must be joint.** A run that stays light behaves like a capped algorithm, but it need not succeed with probability at most $\beta^r$ given that it stays light. Take $P=\text{AND}$ on the three promised inputs $01,10,11$, uniformly; any one-query algorithm is right with probability at most $\beta=2/3$. Read the first bit, output $0$ if it is $0$, and otherwise read the second bit. This algorithm stays within one query exactly on input $01$, where it is right, so its success given that it stays light is $1$. The true statement concerns the joint event: being right **and** staying within the caps has probability $1/3\le\beta$. This toy illustrates conditioning: it meets the one-query hard-law premise but has $R(P)=L=1$, so it does not instantiate the strict $L<R(P)$ regime of our construction ([record Appendix B.3](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md#CL-conditioning-counterexample)).

### Two clocks in a capped simulation

A small trace makes the cap concrete. Use the [record's XOR example](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md#CL-simulator-example), which changes the partial function to $P(a,b)=a\oplus b$. Use column $i$ as the target. In this separate toy, let the two inputs $(a,b)$ and $(c,d)$ be independent fair bit pairs, and set $L=1$. The dummy algorithm first reads an outside string bit, then $a$. Its third query is outside the target if $a=1$, and reads $c$ if $a=0$. Its fourth query proposes a bit in $B_{i,(a,0)}$.

| Global time | Proposed query | Forwarded count and action |
| --- | --- | --- |
| $1$ | Outside string bit | $q=0$; answer locally. |
| $2$ | $a$ | $q:0\to1$; forward. |
| $3$, $a=1$ | Outside target | $q=1$; answer locally. |
| $3$, $a=0$ | $c$ | $q=1=L$; stop before reading. |
| $4$, $a=1$ | Cell $B_{i,10}$ | $q=1$; output label $10$ without reading. |

If $a=1$, the simulator has spent its one target query learning $a$. It answers the third query from its outside information, then reaches the fourth query and outputs $10$, read from the proposed cell position. It does not read the bit in that cell.

If $a=0$, the proposed third query would read $c$, using a second target query. The simulator stops before that query and outputs the default address $00$. Its cap is enforced on this branch as well.

The first branch gives the light true-cell event exactly when $a=1,b=0,c=d$, with probability $1/8$. The simulator is also correct on $a=0,b=0,c=d$, another event of probability $1/8$. Its total success probability is $1/4$, the separate-cap bound $(1/2)^2$ for two fair XOR inputs. Aborting is part of the algorithm; the probabilities are under the original input distribution, without conditioning on the query count.

### Separate caps and independent information

*Separate caps.* Take AND on two independent inputs, each uniform on all four two-bit strings; one query to an input gives $\beta=3/4$. A pooled budget of two queries computes the first answer exactly and guesses $0$ for the second, which is right with probability $3/4>9/16$.

*Joint independence.* For the identity on fair bits $X,Y$ with $L=0$, the side information $X\oplus Y$ is independent of each bit separately, yet the guess $(0,X\oplus Y)$ is right whenever $X=0$, with probability $1/2>1/4$.

# Appendix D. Exercises and answers {.unnumbered}

These questions revisit the board, the weighted sampler and the capped predictor. The examples in Appendix C supply the independent-planting and two-clock setups. The answers follow the questions.

**Projection check.** For $1111\,1000$, calculate the signed amplitude $\Phi$ and then the projection probability. These are different quantities. The [answer](#answer-projection) is separated from the attempt.

[]{#question-1}**Question 1 (promise certification).** On the domain-bit board of Section 3, make one row for each of column $2$'s four addresses. In each row name the domain and value outputs that fail and count them; no gate indices are required. ([Answer](#answer-1).)

[]{#question-2}**Question 2 (conditional sampling and overshoot).** Reconstruct the cycled-board calculation in Section 4.3: after pivots $(2,4)$, why does one amplification iteration help and a second undo the gain? An iteration uses the entire preparation and its inverse, not one bit query. Now continue the unequal-weight example with pivot $4$, taking the four win probabilities against it to be $(1,3/4,1/2,0)$. Find the joint success masses and conditional label law. Multiply the current weights by the comparison probabilities; do not restart from all ones. ([Answer](#answer-2).)

[]{#question-3}**Question 3 (independent planting).** In the independent-planting example of Appendix C, now query two fixed distinct positions per column. How often is an independent $I$ hit, and how often the dependent one? If later queries depend on earlier replies, which identity still holds for an independent $I$, and why? ([Answer](#answer-3).)

[]{#question-4}**Question 4 (two clocks and the capped event).** In the two-clock trace of Appendix C, change the $a=0$ branch so that it proposes a query in $B_{i,00}$ at time $3$, before trying to read $c$. If the run stops after this cell query, what probability does the changed branch contribute, and what is the total probability of a light true-cell visit at either indicated time, including the unchanged $a=1$ branch at time $4$? What changes if the $a=0$ branch reads $c$ afterwards? Which fixed-time events must be bounded separately by the simulator lemma? ([Answer](#answer-4).)

[]{#question-5}**Question 5 (uniform constants and endpoint powers).** What does $k=4$ prove about $\alpha_{\rm tot}$? Which $k$ makes the argument of Section 6 exclude the endpoint bound $R(f)\le C(1+Q(f))^{3.5}$ itself? ([Answer](#answer-5).)

**Combined explanation.** Using the cycled board and the planted-pair/XOR examples, explain why the quantum list can contain a winner even when a later stage fails, and why any classical light visit gives a capped address prediction. Why does an arbitrary rival's off-promise decoder law not spoil comparison with a genuine winner? For the classical route, take an integer budget $G\le c\,mL$: reconstruct the three charges, show that their sum is at most $4c+c+c/m^8$, and identify where $L\le m$, $r=20\log_2m$ and averaging over the independent $I$ enter. Explain which half of $\alpha_{\rm tot}=4$ these mechanisms establish and which half uses the imported universal theorem. Try this before reading the [rubric](#answer-combined). A one-route reader may quote the other route's bound.

## Answers

[]{#answer-projection}**Projection check.** The first sign block is $(-1,-1,-1,-1)$ and its dot product with $(2,-2,-2,-2)$ is $4$. Thus the signed amplitude is $\Phi=4/8=1/2$ and projection probability is $|\Phi|^2=1/4$.

[]{#answer-1}**[Question 1](#question-1).** String, pointer and gate tests pass. Domain bits $(0,1)$ and value bits $(0,0)$ make the first domain test fail always, and a value test fail wherever the address differs from $00$: one failure at $00$, two at $01$ and $10$, three at $11$.

\Needspace{15\baselineskip}

[]{#answer-2}**[Question 2](#question-2).** Multiplying $(1,0,0,1)$ by $(a_{14},a_{24},a_{34},a_{44})=(1,0,1,0)$ gives $(1,0,0,0)$. A preparation succeeds with probability $1/4\ge\gamma$ and then yields column $1$; with $\theta=\pi/6$, one Grover iteration makes success certain, as $\sin^2(3\pi/6)=1$. A second iteration overshoots: $\sin^2(5\pi/6)=1/4$. For the fractional example the new weights are $(1,0,1/4,0)$, joint masses $(1/4,0,1/16,0)$, total success $5/16$, and conditional law $(4/5,0,1/5,0)$. Returning now to the cycled physical board, column $1$ passes verification from the list $\{2,4,1\}$. The unequal-weight example specifies only sampler probabilities; certification uses the board's strings, pointers and transcripts. Columns $2$ and $4$ have failed string tests; the bounded-error verifier discovers those failures with its stated high probability, not with certainty.

[]{#answer-3}**[Question 3](#question-3).** Even for adaptive queries, independence gives $\Pr(\text{erased zero hit})=\mathbb EZ/4$ by conditioning on the complete dummy run. For the fixed two-position experiment, an independent $I$ is hit with probability $\mathbb EZ/4=1/2$; the dependent choice misses only when no zero is found, so it is hit with probability $1-(1/2)^4=15/16$. This product uses two distinct fixed positions in each column and independent zero locations. An adaptive policy preserves the complete-run identity but need not preserve that fixed-pattern product.

[]{#answer-4}**[Question 4](#question-4).** First assume that the changed branch stops after the cell query. The cell query now occurs after only one target query, so the simulator reaches it and outputs $00$. It is a true-cell query when $a=0,b=0,c=d$, with probability $(1/2)(1/2)(1/2)=1/8$. Including the unchanged $a=1$ branch gives total probability $1/4$. If the algorithm instead reads $c$ afterwards, the entire $a=0$ branch is heavy and contributes zero to the joint light-visit event. No query is deleted from the count. The remaining probability is $1/8$, from the unchanged $a=1$ branch. In the stopping version, the fixed-time probabilities are $1/8$ at time $3$ and $1/8$ at time $4$; their union is $1/4$.

[]{#answer-5}**[Question 5](#question-5).** $k=4$ excludes every power strictly below $3.5$, so it proves $\alpha_{\rm tot}\ge3.5$. To exclude the endpoint inequality itself by this argument, take $k>2/(4-3.5)=4$, for example $k=5$. At $k=4$ and $\alpha=3.5$, the ratio estimate has $d=0$ and only a reciprocal logarithmic factor; it does not diverge. At $k=5$, $d=2-1/5-3.5/2=1/20>0$, so it does diverge.

[]{#answer-combined}**Combined explanation.** Each unlisted winner has weight at least $(1-\varepsilon)^T$. Halving makes this much remaining weight unlikely, and a later failure preserves the list already drawn. On the losing board, predict the address from a proposed query coordinate, aborting before the first unaffordable target query. Every light true-cell visit supplies a correct prediction at its query time. For $G\le c\,mL$ the three charges are bounded by $4cL/m$, $c$ and $c\,mL\,m^{-10}$. Since $L\le m$ these sum to at most $4c+c+c/m^8$. The first two charges use the independence of the planted column. In the third, sum over times and average over columns. These arguments exclude every smaller universal exponent; the deterministic quartic bound establishes that four suffices.

# Appendix E. Following the formal proofs {.unnumbered}

The [theorem index](https://github.com/wcook04/quartic-query-lean/blob/main/docs/proof_index.md) connects the mathematical statements to their Lean definitions and proofs. Start with the [winning condition](https://github.com/wcook04/quartic-query-lean/blob/main/docs/proof_index.md#def-wins): the domain-bit board fails precisely because one of its address inputs is not promised. The [family theorem](https://github.com/wcook04/quartic-query-lean/blob/main/docs/proof_index.md#thm-headline) uses one circuit for both complexities, and the [explicit bounds](https://github.com/wcook04/quartic-query-lean/blob/main/docs/proof_index.md#src-constants) give the six and $1/400$ printed here.

The formal quantum argument uses the exact probability law of the measured candidate, followed by verification. That law is what the Boolean algorithm needs. The stronger assertion about retaining the whole successful physical state has a separate correspondence still to be formalized; the headline result does not assume it. The [optimal-exponent theorem](https://github.com/wcook04/quartic-query-lean/blob/main/docs/proof_index.md#thm-alpha) combines the separating family with a formal proof of the universal quartic bound. The index explains these proof routes and gives their precise scope.

\clearpage

# References {.unnumbered}

::: {#refs}
:::

<!-- lean-links -->
<!-- /lean-links -->
