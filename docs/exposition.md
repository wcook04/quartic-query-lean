---
title: "How many bits must an algorithm read?"
subtitle: "OpenAI’s nearly quartic separation between randomized and quantum queries"
author: "Will Cook"
date: "November 2026"
bibliography: exposition.bib
link-citations: true
---

# 1. Finding a column of ones

Does any column in this table consist entirely of ones?

|       | Column 1 | Column 2 | Column 3 | Column 4 |
|:------|:--------:|:--------:|:--------:|:--------:|
| Row 1 | 1 | 0 | 1 | 1 |
| Row 2 | 1 | 1 | 0 | 1 |
| Row 3 | 1 | 1 | 1 | 0 |
| Row 4 | 0 | 1 | 1 | 1 |

The answer is no. Reading down the columns, we find zeros in rows $4,1,2,3$, respectively. Now change just the bottom left entry from zero to one. Column 1 now consists of four ones, so the answer changes to yes.

Imagine that the entries are covered. To read one you specify a row and a column. In either version, asking for row 2 of column 3 returns zero. That zero rules out column 3 as an all-one column. Asking for row 4 of column 1 returns zero on the first table and one on the second. Reading one specified entry is called a *query*. The cost is the number of queries. You can remember everything you have read and use it to choose where to look next.

If these were the only two possible tables, we could distinguish them just by reading the bottom left entry. What makes the problem hard is that the zero could have been anywhere. To see the difference, make a new four-by-four table. In each column choose the position of its single zero uniformly at random, independently of the other columns. Then choose one of the four columns at random and change its zero to one. Suppose you inspect the top row in both versions. You make four queries on each. You see different replies precisely when the changed zero was in the top row, which happens with probability $1/4$. Inspecting the top two rows costs eight queries per table and raises that probability to $1/2$.

The same experiment works with $m$ rows and $m$ columns. Inspecting the first $h$ rows costs $mh$ queries and detects the change with probability $h/m$. This calculation concerns a particular choice of queries. In Section 5 we will also allow the algorithm to choose its next query after seeing all the earlier answers.

**What counts as a quantum query?** A classical algorithm chooses a position and obtains the bit stored there. A randomized classical algorithm can use coin flips to choose its positions. To see what a quantum algorithm can do with one query, take two entries $x_1,x_2$ of the table. Prepare the unit vector $(1,1)/\sqrt2$, with one coordinate for each position. One quantum query in its *sign* form multiplies coordinate $j$ by $(-1)^{x_j}$: zero leaves the sign alone, and one reverses it. Thus the new vector is
$$
       \frac{1}{\sqrt2}\bigl((-1)^{x_1},(-1)^{x_2}\bigr).
$$
If the bits are equal, this vector lies on the line through $(1,1)$. If they differ, it lies on the line through $(1,-1)$. The lines are perpendicular. Measuring in these two directions determines with certainty whether the bits agree. After one classical read, the other bit could still take either value. For the query model see [@BuhrmanDeWolf2002, §3; @deWolf2026, chapters 1, 2 and 7].

**How far apart can the two costs be?** Let $f$ be a yes-or-no question about a string of bits. We call $f$ *total* if every string of its specified length has an answer. Write $R(f)$ for the least number of queries sufficient for a randomized classical algorithm to answer $f$ correctly with probability at least $2/3$ on each string. The number is a cap on every run, including runs on which the algorithm errs. Define $Q(f)$ using the same requirements for a quantum algorithm. In both models, calculations between queries are free.

A theorem of Aaronson, Ben-David, Kothari, Rao and Tal bounds $R(f)$ by a constant times $(1+Q(f))^4$ for every total $f$ [@ABKRT2020]. Could a smaller power work for all such questions? OpenAI proved it could not [@OpenAI2026, Theorem 1.1][^ai]. For every exponent below four, there are questions for which the ratio of the classical cost to that power of $1+Q(f)$ is arbitrarily large. This is the sense in which the separation is *nearly quartic*.

The plain table above is only the starting point for those questions. On the modified table, for instance, we can show someone three entries that rule out columns 2, 3 and 4. We need only tell them which row to read in each. OpenAI makes these row numbers part of the input. Whoever fills in the table may write down wrong row numbers. How can an algorithm use them before it knows which ones are correct?

# 2. Comparing two columns

[]{#base-board}Use the table after the change, so column 1 consists entirely of ones. Suppose the three row numbers stored with column 1 are $1,2,3$, in that order. The numbers give rows in columns 2, 3 and 4, respectively. To check the number for column 3, read its second row. The bit there is zero. The other two numbers direct us to row 1 of column 2 and row 3 of column 4, also zeros. A stored row number used this way is a *pointer*. Following one requires reading the row number and then reading the bit at that row.

In the actual problem a column has several records of pointers. Only one record can count toward a yes answer. Its label, called its *address*, is obtained by answering questions about additional bits stored in the same column. Figure 1 uses two questions, so the possible labels are $00,01,10,11$. The answers for column 1 are one and zero, in that order, so we use the record labelled $10$. The figure draws the entries of column $i$ as a *horizontal* string $X_i$, in row order. The box $B_{1,10}$ is the record labelled $10$ in column 1. Its three solid arrows give the three pointers we have just checked.

Each address question has a specified answer on some strings of bits and no prescribed answer on others. The set on which an answer is prescribed is called its *promise*. In Figure 1 the symbols $a^+,a^0,a^-$ stand for three particular strings. The first has answer one, the second has answer zero, and the third is outside the promise. Thus $(a^+,a^0)$ gives address $10$. In column 2 the pair $(a^-,a^0)$ gives no address at all. Section 4 supplies the bits of these strings and calculates all three cases.

![The four columns from Section 1 after the change, with their pointer records underneath. From record $10$ of column 1, follow the middle solid arrow to the second entry of column 3. Follow the dashed arrow back to the third entry of column 1. The two bits read are zero and one.](figures/exposition/fig2_board.svg){width=92%}

The answer on the enlarged board is yes precisely when there is a column whose entries are all ones, whose address questions all have answers, and whose record at that address contains correct calculations of those answers and pointers to zeros in every other column. Such a record supplies a *certificate*: its contents can be checked against the input, one calculation step or one pointer at a time. We call a column meeting all the conditions a *winning column*. There can be at most one. If there were two all-one columns, no row number from one could lead to a zero in the other. If every column fails at least one condition, the answer is no, even on boards with undefined address answers.

**What can we learn by reading just two pointers?** Take columns 1 and 3 of Figure 1. Use record $10$ in column 1, and try any record in column 3. Read the pointer into column 3 from the first record and the pointer back into column 1 from the second. The first read of a pointed-to bit gives zero, evidence against column 3. The return read must give one because *every* entry of column 1 is one. This comparison returns index 1. For any pair of columns use the same rule: if just one pointer leads to zero, return the index of the column where that pointer is stored. If both lead to zero or neither does, return the smaller index. With the correct record for a winning column, the comparison returns that column even when the other address is wrong.

Can we accept a column just because every comparison returns its index? Change the first pointer in record $10$ of column 1 from row 1 to row 2. Now it leads to a one in column 2. The return pointer still leads to a one in column 1, so the tie rule returns 1. The comparisons with 3 and 4 still return 1 as well. Yet the certificate contains a false pointer, and each other column contains a zero. The correct answer is no. We shall use comparisons to make a short list of indices, then check the certificate at each listed column.

**Which indices should go on the list?** Consider the pointer values in Figure 2. We draw an arrow from $i$ to $j$ when the comparison of those two columns returns $i$. For example, a pointer from column 2 leads to the zero in column 3, and the pointer back leads to a one. This gives the arrow from 2 to 3. Comparing 3 with 4 returns 3. Comparing 4 with 2 returns 4. These three results form a cycle. They cannot come from sorting the columns in a single order.

![For these pointer values, the comparison returns column 1 against each other column. Among the remaining three columns the results form the cycle $2\to3\to4\to2$.](figures/exposition/fig3_tournament.svg){width=53%}

Pick one index uniformly at random and put it on the list. Call it the *pivot*. Retain only indices whose comparison with this pivot would return their own index. Take 2 as the pivot. The arrows into 2 come from 1 and 4, so those are the two remaining indices. If we had picked 1, no index would remain, and we would already have put the winning column on the list. For pivots $1,2,3,4$ the numbers remaining are $0,2,2,2$. Since each choice has probability $1/4$, the mean is $(0+2+2+2)/4=3/2$.

The count works for any $m$ indices if each pair has a fixed comparison result. Take one pair $i,j$. If the comparison returns $i$, then $i$ is retained when $j$ is pivot. Conversely, $j$ is discarded when $i$ is pivot. Thus this pair contributes one to the sum of the counts over all pivots. There are $m(m-1)/2$ pairs and $m$ equally likely pivots, so the expected number retained is $(m-1)/2$. The quantum procedure for obtaining an address can give different labels on successive runs. To use this count with that procedure, we must work out what to retain when the comparison of a pair is itself random.

# 3. Finding a winner by comparisons

Compare columns $2$ and $3$ twice on the same board. The strings, pointers and cells do not change. But the algorithm estimates the two addresses, and a second estimate can select a different cell. The comparison might therefore return $2$ the first time and $3$ the second. Which indices should we keep after comparing with a pivot?

## 3.1 Counting the indices retained by random comparisons

Suppose the first pivot was $2$. Compare $3$ with $2$ ten times. If the two indices are equally likely, the average number of times we obtain $3$ over many such sets of ten comparisons approaches five. Give $3$ a *weight* of $1/2$: this is the probability that a fresh comparison with $2$ returns $3$. Now compare $3$ with $4$ as well. If this second comparison also returns $3$ half the time, the chance of getting $3$ both times is $1/4$, its new weight. The two chances multiply because the second comparison starts afresh, independently of the first. With fixed outcomes the weights are just $1$ for the survivors and $0$ for the rest.

For fixed outcomes we want a uniform choice among the remaining indices. How can we make that choice without first listing them? Draw an index uniformly from the board. Discard it if it is already on the list. Otherwise compare it with each previous pivot and keep it only if every comparison returns the drawn index. Consider the following possible chances against pivot $2$:

| Column drawn | $1$ | $2$ | $3$ | $4$ |
| :--- | ---: | ---: | ---: | ---: |
| Chance of keeping this index after comparison with $2$ | $1$ | $0$ | $1/2$ | $1/4$ |
| Chance of drawing it **and** keeping it | $1/4$ | $0$ | $1/8$ | $1/16$ |

The last row adds to $7/16$. Of the draws we keep, the share belonging to column $3$ is $(1/8)/(7/16)=2/7$. The shares for all four columns are $4/7,0,2/7,1/7$. Uniform proposals have given us a way to draw the next pivot even with uncertain matches. For instance, $3$ is twice as likely as $4$ among the accepted draws because its acceptance probability is twice as high.

Here is the same calculation for $m$ columns. Write $w_i$ for the chance of keeping $i$ when we compare it afresh with every pivot so far. Before the first match, all weights equal one. Write $W=w_1+\cdots+w_m$. Drawing $i$ and keeping it has probability $w_i/m$, so the chance of keeping *some* column is $W/m$. Among the draws we keep, the chance of $i$ is therefore $w_i/W$. Imagine we can draw from these shares whenever $W>0$. Append the resulting pivot $p$ to the list. Let $a_{ip}$ be the probability of keeping $i$ in a comparison with $p$. We now require one extra successful comparison, so the new weight of $i$ is $w_i a_{ip}$. We discard $p$ in a comparison with itself: $a_{pp}=0$. Stop if $W=0$.

Does each new pivot still cut the number of survivors in half on average? The quantity to count now is their total weight. Fix the list so far and consider, for instance, columns $2$ and $3$. There are two contributions to count. We might draw $2$, leaving weight from $3$; or we might draw $3$, leaving weight from $2$. Here the two contributions to the expected remaining weight add to
$$
\frac{w_2}{W}\,w_3 a_{32}+\frac{w_3}{W}\,w_2 a_{23}
=\frac{w_2w_3}{W}.
$$
The equality holds because the comparison always returns one of the two indices: $a_{32}+a_{23}=1$. The same argument works for every pair. Adding, with $i<p$ to count each pair just once, gives
$$
\text{expected weight after this pivot}
=\frac{\sum_{i<p}w_iw_p}{W}
=\frac{W^2-\sum_i w_i^2}{2W}\le\frac W2.
$$
Indeed, expanding the square of $w_1+\cdots+w_m$ counts each pair twice and each square once. With four weights all equal to one, this gives $(16-4)/8=3/2$, the average we found for the fixed arrows in Section 2 [@AIK2026v3, §§4 and 6.1].

Starting from $m$, the expected total is thus at most $m/2$ after one pivot, $m/4$ after two, and $m/2^T$ after $T$. This tells us something about a *particular* column. Section 4 will give us a comparison that returns the winning index with probability at least $1-\varepsilon$ whenever that index is compared with another. After $T$ other pivots, its weight is still at least $1-T\varepsilon$: the chance of at least one incorrect comparison is no more than the sum of the individual error probabilities. Take $T=\lceil\log_2(1000m)\rceil$ (round up so $2^T\ge1000m$), and $\varepsilon=1/(1000T)$. If the winner has *not* been listed, its weight alone exceeds $1/2$. If this happened with probability $d$, the expected remaining weight would be at least $d/2$. But that expectation is at most $1/1000$. Thus the chance the list misses a genuine winner is at most $1/500$. Nothing requires a listed column to be a winner. We will check the list afterwards.

## 3.2 Sampling the next pivot

Drawing a column and trying it against all the pivots gives the right shares, but a single draw succeeds with probability only $q=W/m$. With four columns and just one survivor, about one draw in four succeeds. With $m$ columns and one survivor, we would need $m$ attempts on average. A quantum search can find that survivor in about $\sqrt m$ attempts. We will see how it improves the chance of success *without changing which columns appear among the successes*.

As in the two-bit example of Section 1, we use one amplitude for each position. Here the four positions are column labels. For instance $(1/2,1/2,1/2,1/2)$ gives the same chance to each column. To read the label (to *measure* it), square each amplitude: in this example we obtain one label, with chance $1/4$ for each. The squared amplitudes always sum to one. Negative amplitudes are allowed. Although $-1/2$ gives the same reading probability as $1/2$, the two numbers can cancel in an addition before we measure. Our examples need only real amplitudes.

A *superposition* of labels is a linear combination of their basis vectors. The basis vector for column $i$ has a one in position $i$ and zeros elsewhere. To apply a reversible quantum operation to the combination, apply it to each basis vector and take the same linear combination of the outputs. Give the search a place to store a bit, its *flag*. Starting with equal amplitudes on all columns, carry out the matches for each label, keeping the answers. Set the flag to $1$ for a new index if every comparison returned it; set the flag to $0$ for all other outcomes, including indices already on the list. Call this whole preparation $A$. The labels now include both the column and this extra information. Reading column $i$ together with flag $1$ has probability $w_i/m$, just as in the ordinary trial. So far we have saved nothing. The saving comes from changing the amplitudes *before reading them*.

On our board with fixed arrows, suppose the list already contains $2$ and $4$. Only the index $1$ is kept after both comparisons. Keep track of four amplitudes in column order, with the match results attached to the columns. Start with $(1/2,1/2,1/2,1/2)$. Perform two operations:

1. Change the sign for entries with flag $1$. We now have $(-1/2,1/2,1/2,1/2)$. A measurement at this point would still pick column $1$ only a quarter of the time.
2. Reflect the amplitudes about their average: an entry $x$ becomes $2(\text{average})-x$. The average here is $1/4$. The first entry becomes $1/2-(-1/2)=1$; each other entry becomes $1/2-1/2=0$.

Now a measurement returns column $1$ with certainty. The second operation is reflection about the line through the prepared vector, which has four equal coordinates in this example. No table of comparison outcomes is needed to implement this reflection. Undo the whole preparation, reflect about its known starting state, then run the preparation again. This is why the search retains the match results while it runs: throwing them away would prevent it from undoing the preparation [@BHMT2002, Lemma 1; @deWolf2026, §§7.1–7.3].

With several possible successful results, the first operation changes all their signs together. The second reflection gives the geometric reason that their relative chances remain the same. Group the prepared vector into two parts: all entries with flag $1$, and all entries with flag $0$. Their squared lengths (sums of squares) are $q$ and $1-q$. They occupy separate coordinates, so they are at right angles. For $0<q<1$ both parts have nonzero length; divide each by its length to get unit directions $g$ and $b$, for good and bad. The prepared state has coordinates $(\sqrt q,\sqrt{1-q})$ along these two directions. The flag operation reverses the first coordinate, and the other operation reflects about the line through that prepared point and the origin. Both act in this plane. They change the amount in direction $g$, but leave the proportions of the entries *within* $g$ untouched. Thus whenever we read flag $1$, the label still has the required chances $w_i/W$.

[]{#pivot-schedule}To see how many reflections are needed, measure the angle $\theta$ of the prepared vector from the $b$ axis, so $\sin\theta=\sqrt q$. The flag operation sends angle $\theta$ to $-\theta$; reflecting that about the line at angle $\theta$ gives $3\theta$. Each further pair adds $2\theta$. After $u$ pairs the probability of success is $\sin^2((2u+1)\theta)$. For small $q$, $\theta$ is approximately $\sqrt q$ in radians, so about $1/\sqrt q$ pairs suffice to turn the state towards $g$. Going too far loses some of the gain: in the four-column calculation a second pair takes the chance from one back to $1/4$. At $q=0$ nothing can succeed, and at $q=1$ the preparation already succeeds.

We do not know $q$. The algorithm draws a random number of reflections for each trial, sometimes zero. Under the [schedule in Appendix A.3](#amplification-schedule), it uses $O(\sqrt m\log(1/\varepsilon))$ preparations and reversals on *every* board, and fails with probability at most $\varepsilon$ whenever $q\ge1/(2m)$ [@BBHT1998, Lemma 2]. Stopping at the first success gives the same column shares whichever trial succeeded.

Append each successful pivot; stop if the schedule fails or the list reaches $T$ entries. While a winner is still missing, its weight exceeds $1/2$, so $q=W/m>1/(2m)$. Until the first failure we can give this search and the ideal drawing rule of Section 3.1 exactly the same successful draws. There are at most $T$ opportunities for failure before the winning index is listed, adding at most $T\varepsilon$ to the ideal chance $1/500$ of missing it. A later failure leaves the existing list intact. With at most $T$ comparisons per preparation, we have used $O(T^2\sqrt m\log(1/\varepsilon))$ comparisons and their reversals. How many input bits must the algorithm query to compare two columns?

# 4. Computing an address and checking its certificate

For the comparison of columns $1$ and $3$ in Figure 1 we used cell $10$ of column $1$. But the algorithm is given two strings of eight bits, not the label $10$. How does it obtain the first digit $1$ from $0111\,1000$, and the second digit $0$ from $0100\,1000$?

Start with the second half, $1000$, common to both strings. Replace each $0$ by $+1$ and each $1$ by $-1$, obtaining $g=(-1,1,1,1)$. Compare $g$ with each of the four fixed patterns below. Score $+1$ at every position of agreement and $-1$ at every disagreement; in other words, multiply the corresponding entries and add.

| Pattern | Agreements | Disagreements | Score |
| :--- | ---: | ---: | ---: |
| $(1,1,1,1)$ | 3 | 1 | $2$ |
| $(1,-1,1,-1)$ | 1 | 3 | $-2$ |
| $(1,1,-1,-1)$ | 1 | 3 | $-2$ |
| $(1,-1,-1,1)$ | 1 | 3 | $-2$ |

The pattern in each row agrees with every other row in two positions and disagrees in two. Thus if $H$ is the matrix having these rows divided by two, its rows are mutually perpendicular unit vectors. Multiplication by $H$, the *normalized Walsh transform*, preserves length. On our input, $Hg=(1,-1,-1,-1)$.

Now use the first block. For $0111$ its signs are exactly $(1,-1,-1,-1)$. To measure agreement with the transformed second block, take the dot product after dividing each vector by two to give it length one. Call the result $\Phi$. Here $\Phi=(1+1+1+1)/4=1$. For $0100$, two entries agree and two disagree, so $\Phi=0$. For $1000$, all four are opposite and $\Phi=-1$. In general the entries of a Walsh transform need not be signs; the dot product still measures alignment of the two unit vectors [@AA2018, §§1.1.1 and 3.2].

| Eight input bits | $\Phi$ | Prescribed address bit |
| :--- | ---: | :--- |
| $a^+=0111\,1000$ | $1$ | $1$ |
| $a^0=0100\,1000$ | $0$ | $0$ |
| $a^-=1000\,1000$ | $-1$ | undefined |

The prescription here is $1$ for $\Phi\ge\delta$, $0$ for $|\Phi|\le\delta/2$, and no answer otherwise, with $\delta=2^{-10}$ for two blocks. These first two ranges constitute the *promise*. Thus $(a^+,a^0)$ determines address $10$. There is no true address for $(a^-,a^0)$, since the first digit is undefined. This distinction will matter when we verify the board.

**How a query supplies the signs.** A bit query uses a position $j$ and an answer bit $b$. It leaves $j$ alone. If the input bit $x_j$ is zero it leaves $b$ unchanged; if $x_j$ is one it interchanges answer labels $0$ and $1$. Starting from $b=0$ would read the bit in the ordinary way. Instead give the two answer labels amplitudes $(1,-1)/\sqrt2$. Interchanging them gives $(-1,1)/\sqrt2$, the negative of the starting vector. For each position $j$, then, the query leaves this same answer vector multiplied by $+1$ or $-1$ according to $x_j$. Applied to a superposition of positions, this single bit query multiplies the position amplitudes by their respective signs. Measuring still yields a single outcome; the query has not reported the individual bits [@deWolf2026, §2.4].

Try it on $a^+$. Give the four positions equal amplitudes $u=(1,1,1,1)/2$. Query the second block, multiply by the known matrix $H$, and query the first block. The position vectors are
$$
\tfrac12(1,1,1,1)
\ \longmapsto\ \tfrac12(-1,1,1,1)
\ \longmapsto\ \tfrac12(1,-1,-1,-1)
\ \longmapsto\ \tfrac12(1,1,1,1).
$$
Apply $H$ once more. Its first row is $u$, so the *first amplitude* is the dot product of $u$ with the last vector. This is precisely the number $\Phi$ computed above: the last query supplied the signs from the first block, and dotting with $u$ adds and divides by two. Reading the first position therefore has probability $\Phi^2$. The two multiplications by $H$ use no input bits. On $a^+$ this outcome is certain and on $a^0$ it never occurs. On $a^-$ the last vector is $-u$, so the outcome is again certain. The experiment can return the same proposed digit for $a^+$ and $a^-$; it need only return the prescribed digit on the promise.

**From two queries to a comparison.** At full size, one address digit uses $k$ blocks of $m=4^t$ bits, where $t\ge1$. Write $F_{k,m}$ for the yes-or-no function on the resulting boards. Use the same experiment, starting with $u=(1,\ldots,1)/\sqrt m$: query the last block, apply $H$, query the preceding block, and so on. For this size the rows and columns of $H$ have binary labels $a,b$ of length $2t$. Its entry is $(-1)^{a\cdot b}/\sqrt m$, with a minus sign when an odd number of positions have a one in *both* labels. For $m=4$ this gives exactly the four patterns above. Writing $D_j$ for multiplication of each entry by the corresponding sign from block $j$, the first amplitude after the final transform is
$$
\Phi=u^{\mathsf T}D_1 H D_2 H\cdots H D_k u .
$$
This $k$-block quantity is called *Forrelation* [@AA2018, §3.2, Figure 1]. Here $\delta=2^{-5k}$. One trial uses $k$ queries, and its probability of the first outcome is at least $\delta^2$ if the prescribed digit is $1$ and at most $\delta^2/4$ if it is $0$. Repeat on fresh states and count first outcomes. Comparing their observed fraction with $\delta^2/2$ distinguishes those two ranges. For fixed $k$, $O_k(\log(1/\eta))$ queries suffice for error at most $\eta$ on the promise; the query cap holds even outside it. [Appendix A.5](#decoder-repetitions) gives the repetition count.

For $\ell=\log_2 m$, the full board uses $r=20\ell$ address digits. There are $2^r=m^{20}$ possible cells in each column, but obtaining an address does not involve searching through these cells. Run the experiment on each of the $r$ inputs with error at most $\varepsilon/r$ on the promise. If all $r$ inputs satisfy the promise, the chance of even one wrong digit is at most $r(\varepsilon/r)=\varepsilon$. Look up the pointer in the proposed cell; its $\ell$ bits name a row in the other column. Do this in both directions and read the two indicated string bits. At a winning column, the correct address yields a pointer to a zero, whereas reading *any* row in that all-one string returns one. So however poor the other address estimate, the comparison returns the winning index with probability at least $1-\varepsilon$. For a pair of nonwinning columns either outcome is allowed. Use the same order of indices to run the experiment whichever way the pair was presented; its two possible outcomes then have probabilities $a_{ip}$ and $a_{pi}$ summing to one.

Instead of reading the intermediate outcomes during the quantum search, retain them in separate registers (groups of bits in the quantum state). Compute the addresses, pointers and comparison bit from those labels. Only the final measurement is needed to give the comparison probabilities just calculated. Retaining the intermediate labels also allows the algorithm to undo the computation in reverse order. Either direction costs $O_k(r\log(r/\varepsilon)+\ell)$ bit queries. Arrays indexed by several answers were used in the construction called *cheat sheets* [@ABK2016, §3.1]; pointers to zeros appeared in earlier pointer functions [@GPW2018; @ABBLSS2017]. OpenAI's board combines both in each column [@OpenAI2026, §2].

![Fields in a full column. The address digits select a cell. The cell contains row indices for the other columns and records of the computations on this column's address inputs.](figures/exposition/fig1_column.svg){width=90%}

**What is stored as evidence?** In the example, measuring the first position gives the same outcome for $\Phi=1$ and $\Phi=-1$. For verification we need the *signed* value. There is an exact calculation: multiply signs, perform the Walsh sums by integer additions and subtractions, and compare the result with the thresholds, accounting for the known denominators. Two output bits suffice. The first, the *domain bit*, is $1$ exactly when the input lies in the promise. The second gives the prescribed digit then, and by convention is $0$ outside the promise. For $a^0$ the two outputs are $(1,0)$; for $a^-$ they are $(0,0)$.

Write the exact calculation as a fixed sequence of operations on bits, a Boolean *circuit*. Each operation, or *gate*, takes at most two previous bits or input bits and produces one bit according to a known rule. A *transcript* is a proposed list of the gate outputs, in order. For example, one gate in the small circuit computes “$u$ OR $y$”: its output should be $1$ if at least one of $u,y$ is $1$. If we read $u=1$, $y=0$, output $0$, those three readings expose an error. In this example $y$ is an input bit and $u$ is a previous gate output. When a gate uses an input bit we read the actual board bit; when it uses another gate, we read that gate's listed value. Any incorrect transcript has a *first* wrong entry; all its predecessors are correct, so it must fail just such a test. Conversely, if every gate test passes, the two output bits are correct. There are $S=O_k(m\ell^2)$ gates for one address input ([Appendix A.6](#exact-certification)).

[]{#domain-bit-board}Consider the strings $0111,1111,1011,1101$. Only column $2$ is all ones. Suppose its two address inputs are $(a^-,a^0)$, and every cell in column $2$ contains their exact transcripts and pointers to zeros in columns $1,3,4$. At cell $00$ the listed value digits do spell $00$. But the first output (promise membership) for $a^-$ is zero. No choice of cell can give this column a true address. Thus the answer on the board is zero even though all the pointers in that cell and every entry in its transcripts are correct.

For a listed column, estimate its address again and test that *one* cell. Check all $m$ entries in the column string for ones; follow its $m-1$ pointers to check for zeros; and check all $r$ transcripts. Each transcript requires the $S$ gate tests and two output tests, one for promise membership and one for agreement with the corresponding digit of the cell label. These are exactly the conditions for a winning column. There are
$$
K=m+(m-1)+r(S+2)=O_k(m\ell^3)
$$
tests. Reading a pointer and the bit at its destination costs $\ell+1$ queries. Each other test costs at most three. It is enough to *find one failed test*. If there is one, selecting a test uniformly finds a failure with probability at least $1/K$. The same quantum search as in Section 3.2 can find a failed test with error at most $\varepsilon$ in $O(\sqrt K\log(1/\varepsilon))$ test evaluations. If no test fails there is no failure to report.

Return $1$ if the search reports no defect for at least one listed index, and $0$ otherwise. On a board with no winner, at least one test fails at every listed index, whichever address was estimated. The chance that at least one of the at most $T$ searches reports no defect is at most $T\varepsilon$. On a board with a winner, the list contains its index except with probability at most $1/500+T\varepsilon$. The fresh estimate of its address is wrong with probability at most $\varepsilon$; at its correct address every test passes.

The costs add. Finding the list takes about $\sqrt m$ comparisons, up to logarithmic factors, and each comparison requires only logarithmic factors in bit queries for fixed $k$. Searching for a defect costs about $\sqrt m$ bit queries up to such factors, but we do that for only $T$ listed indices. The [full count](#quantum-query-count) gives $Q(F_{k,m})\le C_k\sqrt m(\log_2 m)^6$.

![The comparison reads two pointers and the indicated string bits. The separate search for a failed test runs only for indices on the resulting list.](figures/exposition/fig5_costs.svg){width=92%}

# 5. A classical query to the hidden cell

In the upper board of Figure 5 the strings are $1110,0111,1011,1101$. Each has a zero, so the function value is $0$. Make a second board by changing the last bit of column $1$ to a one. Its address inputs already have answers $1,0$. In cell $10$ of column $1$, put the correct gate values for these two inputs and the row numbers $1,2,3$ of the zeros in columns $2,3,4$. Column $1$ now satisfies every test, so the new function value is $1$.

![The upper and lower boards differ only at the fourth string bit of column 1 and within its cell 10. The arrows indicate the row numbers stored in the filled cell.](figures/exposition/fig4_planted.svg){width=90%}

Consider reading the domain bit for the first address input from cell $10$ of column $1$. On the upper board the reply is $0$ because every cell bit is zero. On the lower board it is $1$ because the first address input belongs to the promise. If all columns have true addresses and those addresses are supplied, the distinction is easy. Reading the first domain bit at the indicated label in each column would return all zeros on the first board and a one somewhere on the second, in at most $m$ reads. Without the labels, there are two distinct acts here. First the algorithm specifies the column, the cell label and the position within that cell. Then it receives one bit. **Selecting the right cell already predicts the address.** At the instant of this selection the reply is still unknown. An algorithm may compute the label, deduce it from earlier replies, or simply guess it. We shall bound the probability of selecting it by any of these means.

## 5.1 Two runs of the same decision tree

To prove a lower bound we shall choose both the first board and the changed column at random. For each fixed $k\ge2$ and all sufficiently large powers of four $m$, set
$$
L=\left\lfloor\frac{m^{1-1/k}}{(\log_2 m)^2}\right\rfloor\ge1.
$$
Write $P$ for the partial function in Section 4 that gives one Forrelation address digit. For a partial function the query limit applies on every input, while the answer is required to be correct only on the promise. The theorem of Bansal and Sinha gives $R(P)>L$. Thus every randomized algorithm using at most $L$ bit queries has error greater than $1/3$ on some promised input. We need one input *distribution* that works against all deterministic algorithms with that cap. Such a distribution $\mu$ exists by finite minimax. Indeed, if for every distribution some tree did better than $2/3$, minimax would give a random choice of trees with success at least $2/3$ on every input, contrary to $R(P)>L$. [@BansalSinha2021, Theorem 1.3 and Corollary 1.4; @Yao1977]

Build the first board as follows. Choose the row of the zero uniformly and independently in each column. Independently of the zeros, draw each of the $r$ address inputs in each of the $m$ columns separately from $\mu$. Set every cell bit to zero. This board has value $0$. Now draw a column number $I$ uniformly, independently of everything on that board. As in the figure, erase its zero and fill its true cell with correct transcripts and pointers to the zeros in the other columns. This board has value $1$. The procedure for drawing a pair may use the entire input. The algorithm being tested receives either board only through bit queries.

Suppose the algorithm uses at most $G$ queries. Use the same random choices of the algorithm on both boards. After fixing these choices the algorithm is a *decision tree*. Each node specifies the next bit to read, its two edges correspond to replies $0$ and $1$, and a leaf specifies the output. Starting from the same node, identical replies therefore give the same next node, however strongly the next query depends on the past. For different outputs the two runs must first receive different replies at a common node. It suffices to count, **on the run on the first board**, queries to the erased zero and queries anywhere inside the selected cell. Counting the entire cell only enlarges the probability, since some filled bits may still be zero.

**Reading the erased zero.** Suppose this run discovers zeros in three of the $m$ columns. Then three of the $m$ possible choices of $I$ select a discovered zero. In general, if $Z$ counts the distinct zeros discovered, the probability of reading the erased zero is $\mathbb E[Z]/m$. The full run on the first board is independent of $I$.

Before a column's zero has been found, it is uniform over the unread rows. Moving it between those rows preserves all previous replies, including the replies from the blank cells. If fewer than $m/2$ different rows of the column have been read, the chance of discovering its zero at the next query is at most $2/m$. Summing over the $G$ opportunities bounds the expected number of these discoveries by $2G/m$. Every other discovery occurs in a column where at least $m/2$ rows have already been read. At most $G/(m/2)$ columns can have this many reads. Thus $\mathbb E[Z]\le4G/m$, and the probability of reading the erased zero is at most $4G/m^2$.

## 5.2 Predicting the label of a queried cell

For each column, count the reads of its $r$ address inputs on the *entire* first-board run. Call the column **heavy on this run** if the count exceeds $L$, and **light on this run** otherwise. Cell and string reads are included in the overall budget $G$, but only reads of the address inputs contribute to this particular count. At most $G/L$ columns can be heavy. Hence the independent random column $I$ is heavy with probability at most $G/(mL)$. For a light column we can reconstruct a proposed cell label using at most $L$ reads of its address inputs.

Here is that reconstruction for a four-query tree. To see both branches with just four input bits, replace Forrelation in this example by the parity $a\oplus b$, which equals one when the two bits differ. A specified column $i$ has two independent pairs $(a,b)$ and $(c,d)$ of fair bits. Its address is $(a\oplus b,c\oplus d)$. Allow the predictor one read in total from these four bits. It can generate the rest of the first board independently, including the blank cells of column $i$.

The first query specifies a string bit, which the predictor can supply from its generated board. The second query specifies $a$, which uses the one permitted target read. Now follow the two possible replies.

- If $a=1$, query three is another string bit. The predictor supplies it from its generated board. Query four specifies a bit of cell $10$ in column $i$. The predictor outputs $10$ immediately. For instance, if $(a,b)=(1,0)$ and $(c,d)=(1,1)$, both predicted digits are correct.
- If $a=0$, query three specifies $c$. That would be a second target read. The predictor stops *before* reading $c$ and outputs a fixed default, say $00$.

The example has two counts. Query four on the first branch was reached with just one target read. On the second branch, even query three would already require a second target read. [Appendix C](#predictor-trace) computes the probabilities on both branches.

Now fix *in advance* any column $i$ and query number $j\le G$. The target consists of the $r$ independent samples in column $i$, and the desired output is the $r$-bit word of their $P$-values. Generate the rest of the first board independently, as in the example. Simulate the queries strictly before $j$, obtaining a bit from the target only when requested. Stop with a fixed default before the first target read beyond $L$. At step $j$, if the tree proposes a bit in a cell of column $i$, output the label of that cell before taking the query. Use the same default for every other proposal or if the tree has already stopped.

On any run where $i$ is light and the $j$th query is in its true cell, the predictor reproduces the entire preceding history within its allowance and returns the true label. Thus the probability of these **two events together** is at most the predictor's probability of getting all $r$ answers right. Conditioning on lightness would change the target distribution. For example, a tree can stop early on the inputs where its first read determines the answer and take more reads on the others.

For one sample drawn from $\mu$, even the best $L$-query predictor has success at most $2/3$. For $r$ independent samples, the chance of predicting *all* the answers is at most $(2/3)^r$ if each sample may be read at most $L$ times. Our predictor uses at most $L$ reads across all the samples, so it meets each separate limit. This multiplication requires proof because the predictor can switch between samples in response to earlier bits. For any fixed sequence of queries and replies, each sample is restricted only by its own recorded bits. With the tree fixed, these restrictions suffice to reproduce that sequence, so the conditional distributions still factor. Reading a bit of one sample can improve the best attainable success on that sample for a particular reply, but cannot improve it *on average* over the two replies. Taking this very query was already one possible strategy. The other samples retain their distributions and their remaining allowances. The calculation for the product is in [Appendix B](#direct-product-proof). [@Shaltiel2003; @Drucker2012, §1.3 and Lemmas 3.1–3.2]

For a fixed $i$ there are at most $G$ times when such a visit could occur. Adding the bounds gives $G(2/3)^r$ for a true-cell visit while $i$ is light. Averaging these $m$ bounds over the uniform choice $I$ gives the same bound. Taking $r=20\log_2m$ makes $(2/3)^r\le m^{-10}$, since $(2/3)^2<1/2$. Thus even $G$ attempts to select a label have small total success probability at the budgets considered here.

[]{#classical-finish}We have covered every way for the two outputs to differ. The following bounds are probabilities over the random pair, for each fixed choice of the algorithm's coins.

| Event on the first board | Probability at most |
| --- | --- |
| A query reads the zero of column $I$. | $4G/m^2$ |
| More than $L$ queries read address inputs of column $I$. | $G/(mL)$ |
| At most $L$ such reads occur, and a query visits the true cell of $I$. | $G(2/3)^r$ |

Set $G=\lfloor mL/100\rfloor$. Since $L\le m$, the sum is at most $4/100+1/100+1/(100m^8)<1/3$. Averaging over the coins preserves this inequality. But an algorithm of error at most $1/3$ on every board must output $1$ on the second board with probability at least $2/3$ and on the first with probability at most $1/3$. The difference is at least $1/3$, and is at most the probability that the two outputs differ. This contradicts the bound. Consequently $R(F_{k,m})>\lfloor mL/100\rfloor$.

# 6. Why the exponent is four

Could there be a constant $C$ such that $R(f)\le C(1+Q(f))^3$ for every total Boolean function $f$, whatever its input length? Try the boards with $k=3$. Ignoring logarithmic factors for a moment, their quantum cost is at most $\sqrt m$ and their classical cost is at least $m^{5/3}$. Cubing $\sqrt m$ gives $m^{3/2}$. The ratio $m^{5/3}/m^{3/2}=m^{1/6}$ grows without bound. Restoring the logarithms divides this ratio by at most a fixed power of $\log m$ and still leaves a quantity tending to infinity. Thus every proposed cubic constant fails on sufficiently large boards.

More generally, OpenAI constructs, for every fixed integer $k\ge2$ and all sufficiently large powers of four $m=4^t$, a total Boolean function $F_{k,m}$ with $Q(F_{k,m})=\widetilde O_k(\sqrt m)$ and $R(F_{k,m})=\widetilde\Omega_k(m^{2-1/k})$ [@OpenAI2026, Theorem 1.1 and its proof]. The tildes suppress powers of $\log m$. In explicit form, [Appendix A.1](#quantum-query-count) and Section 5 give the following bounds on this same function, using the same circuit in both estimates.
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6,
\qquad
R(F_{k,m})\ge \frac{m^{2-1/k}}{400(\log_2m)^2}.
$$
The first comes from listing columns by quantum comparisons and checking the list. For the second, the bound $R>\lfloor mL/100\rfloor$ uses one factor $m$ for the choice of column and $L=\lfloor m^{1-1/k}/(\log_2m)^2\rfloor$ for classical prediction of one address bit. For large $m$, rounding down to $L$ retains at least half the unrounded value, so the displayed constant $1/400$ suffices. Both the quantum constant $C_k$ and the size threshold for $m$ may depend on $k$.

Measured in powers of $\sqrt m$, the classical exponent is $4-2/k$, since $(\sqrt m)^{4-2/k}=m^{2-1/k}$. Given any proposed $0\le\alpha<4$, first choose an integer $k\ge2$ with $4-2/k>\alpha$. Keep this $k$ fixed and increase $m$. In the ratio of the classical lower bound to the $\alpha$th power of the quantum upper bound the excess exponent of $m$ is now positive:
$$
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
\ \ge\ c_{k,\alpha}\,
\frac{m^{2-1/k-\alpha/2}}{(\log_2m)^{2+6\alpha}}
\ \longrightarrow\ \infty.
$$
Here $c_{k,\alpha}>0$ is independent of $m$. Hence for every constant $C$ some total function violates $R(f)\le C(1+Q(f))^\alpha$.

It remains to show that the power four suffices for *every* total Boolean function. Write $D(f)$ for the least worst-case number of queries in a deterministic algorithm that computes $f$ exactly. The theorem of Aaronson, Ben-David, Kothari, Rao and Tal, building on Huang's sensitivity theorem, gives $D(f)=O(Q(f)^4)$ for total functions. A randomized algorithm may use the deterministic one, so $R(f)\le D(f)$. If $\alpha_{\rm tot}$ denotes the infimum of the nonnegative exponents for which one constant works for all total functions, these two results give $\alpha_{\rm tot}=4$. [@ABKRT2020; @Huang2019]

[^ai]: The theorem and construction are OpenAI's. This exposition and its Lean development were prepared with AI systems under the author's direction.

\clearpage

# Appendix A. Supporting calculations {.unnumbered}

[]{#quantum-query-count}

## A.1 Counting the quantum queries

We count calls to the bit oracle on the longest possible run of the algorithm in Sections 3 and 4, including all choices of the number of amplification iterations.

To evaluate the local tests on a superposition of test labels, compute each next input position reversibly and retain the earlier replies. To implement a read that is active only on some branches, query $x_j$ into a temporary bit, conditionally copy it to the answer bit, then query $j$ again to clear the temporary bit. This uses two ordinary oracle calls. On an inactive branch the answer and temporary bits are both restored. Padding to a common number of these controlled reads therefore has a fixed cap even in superposition. Running the computation backwards then restores its workspace. This implements the same tests using $O(\ell+1)$ bit queries per evaluation. [The controlled-read construction](https://github.com/wcook04/quartic-query-lean/blob/ba49281af72b53d9cfbb43320d7efdeb29d7ceca/docs/reasoning_record.md#AC-coherent) gives the gate sequence.

**Comparisons and verification.** A comparison uses $O_k(r\log(r/\varepsilon))$ queries for its decoders and $O(\ell+1)$ for its pointers, including the constant overhead of a reversible implementation. We count the tournament first, then verification.

Each stage uses $O(\sqrt m\log(1/\varepsilon))$ preparations, and each preparation makes at most $T$ comparisons. There are at most $T$ stages. Multiplying these three factors bounds the entire tournament by $O(\sqrt m\,T^2\log(1/\varepsilon))$ comparisons.

Verification makes at most $T$ fresh address decodings. For each candidate it searches the $K$ local tests, using $O(\sqrt K\log(1/\varepsilon))$ test evaluations. Thus the list requires $O(T\sqrt K\log(1/\varepsilon))$ test evaluations in all.

Adding the numbers of bit queries gives
$$
O_k\!\left(\sqrt m\,T^2\log(1/\varepsilon)
 [r\log(r/\varepsilon)+\ell]
 +T[r\log(r/\varepsilon)+\sqrt K\log(1/\varepsilon)\ell]\right).
$$
The first term counts queries during comparisons. The second counts queries during verification, both fresh address decoding and the search for a failed local test. Here $r,T,1/\varepsilon=O(\ell)$ and $K=O_k(m\ell^3)$. Bounding $\log(1/\varepsilon)=O(\ell)$, $\log(r/\varepsilon)=O(\ell^2)$ and $\sqrt K=O_k(\sqrt m\,\ell^2)$ deliberately enlarges the logarithms and square root. These substitutions give $O_k(\sqrt m\,\ell^6)$ for the tournament and $O_k(\sqrt m\,\ell^5)$ for verification ([the explicit count](https://github.com/wcook04/quartic-query-lean/blob/ba49281af72b53d9cfbb43320d7efdeb29d7ceca/docs/reasoning_record.md#upper-explicit-log6)). Therefore
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6.
$$
Thus the sixth power of the logarithm is sufficient. The factor $\sqrt m$ in the tournament comes from sampling the next pivot. In verification the comparable factor comes from the square root of the number of local tests. Full verification occurs only after the list has been produced, at most once per listed column.

[]{#earlier-recipe}

## A.2 Why the balanced AND–OR recipe stops at a cube

In the cheat-sheet construction [@ABK2016, §3.1], each of the $n$ input bits of a partial function $g$ is replaced by the answer to its own AND–OR instance on $n^2$ bits, for $n^3$ bits overall before adding certificates. In one instance, arrange the bits in $n$ rows of $n$ bits. Its answer is $1$ exactly when every row contains a $1$. To certify a $1$, specify the position of one $1$ in every row. To certify a $0$, specify a row whose entries are all zero. In either case reading the $n$ designated entries verifies the answer. Doing this for all instances determines an $n$-bit input to $g$. Given those bits, a computation using no further queries can decide whether they satisfy the promise of $g$.

Up to logarithmic factors, the cited composition and cheat-sheet argument supplies randomized lower bound $R(g)n^2$ and quantum upper bound $n$ when $Q(g)$ is polylogarithmic in $n$. Reading all $n$ bits gives $R(g)\le n$, so this calculation reaches at most a cubic separation. Ben-David's earlier Forrelation construction [-@BenDavid2015] and cheat sheets first gave power $5/2$. Tal [-@Tal2020] reached $8/3-o(1)$, and the nearly linear partial-function bounds of Bansal and Sinha [-@BansalSinha2021] and Sherstov, Storozhenko and Wu [-@SSW2023] gave $3-o(1)$. In the present construction, an address instance has about $m$ bits while the quantum search costs about $\sqrt m$. The partial-function hardness can therefore contribute almost two powers of the quantum cost. Section 3 explains how comparisons make that square-root search possible.

The search problem in Section 3 also differs from quantum minimum-finding, which uses an order [@DH1996], and from search with bounded-error tests for fixed Boolean answers [@HMW2003]. Three pairwise comparisons can form a directed cycle. The comparison model also allows each of two indices to be returned with probability $1/2$, so assigning one outcome as the fixed correct answer need not give success greater than $1/2$.

For a fixed input, its certificate size is the smallest number of bits whose values force the same function output on every consistent input. The largest such size is the certificate complexity. Ben-David and Kothari construct total functions whose randomized query complexity is smaller than their certificate complexity [@BDK2026, §§2–3].

\Needspace{8\baselineskip}

[]{#amplification-schedule}

## A.3 The amplification rotation and a finite schedule

For $0<q<1$, write $A|0\rangle=\sin\theta\,g+\cos\theta\,b$ as in Section 3.2. Here $A$ includes the index, all comparison registers and the final success flag. To reflect about $A|0\rangle$, apply $A^{-1}$, reflect about $|0\rangle$, and apply $A$ again. Retaining the decoder and pointer-read registers makes this inverse possible and gives it the same query cost as $A$. The two reflections act on the plane spanned by these orthonormal success and failure vectors. In the ordered orthonormal basis $(g,b)$, the success phase flip and the reflection about $A|0\rangle$ have matrices
$$
S=\begin{pmatrix}-1&0\\0&1\end{pmatrix},\qquad
R_{A0}=\begin{pmatrix}-\cos2\theta&\sin2\theta\\\sin2\theta&\cos2\theta\end{pmatrix}.
$$
Their product $R_{A0}S=\left(\begin{smallmatrix}\cos2\theta&\sin2\theta\\-\sin2\theta&\cos2\theta\end{smallmatrix}\right)$ sends $(\sin\theta,\cos\theta)$ to $(\sin3\theta,\cos3\theta)$. This calculation gives the rotation formula used in Section 3.2. It changes the total successful amplitude, leaving the normalized successful state unchanged.

We require a bound on the number of queries even when the success probability $q$ is arbitrarily small, and a bound on failure when $q$ exceeds a known threshold $\gamma$. Set $M=\lceil10/\sqrt\gamma\rceil$ and $N=\lceil\ln(1/\eta)/\ln(40/31)\rceil$. In each fresh trial use zero iterations with probability $1/2$, and otherwise choose $u$ uniformly from $0,\ldots,M-1$. Stop at the first acceptance, or after $N$ failures. Each trial uses at most $2M+1$ calls to $A$ or $A^{-1}$, so $N(2M+1)$ is an all-input cap.

To bound the failure probability, first suppose $\gamma\le q\le1/2$. Averaging the rotation formula gives [@BBHT1998, Lemma 2]
$$
\frac1M\sum_{u=0}^{M-1}\sin^2((2u+1)\theta)
=\frac12-\frac{\sin(4M\theta)}{4M\sin(2\theta)}
\ge\frac12-\frac1{4M\sqrt{2\gamma}}\ge\frac9{20},
$$
since $\sin(2\theta)=2\sqrt{q(1-q)}\ge\sqrt{2\gamma}$. Thus the randomized-iteration branch alone contributes at least $9/40$ to the trial's acceptance probability. If $q\ge1/2$, the zero-iteration branch contributes at least $q/2\ge1/4$. In either case, $N$ fresh trials all fail with probability at most $(31/40)^N\le\eta$. Each successful trial has the label law derived in Section 3.2, so stopping at the first success preserves it. If $q<\gamma$, the cap still holds, although the acceptance guarantee need not.

\Needspace{8\baselineskip}

## A.4 The small circuit and its local tests

[]{#circuit-check}The [explicit circuit for the four-column board](https://github.com/wcook04/quartic-query-lean/blob/ba49281af72b53d9cfbb43320d7efdeb29d7ceca/docs/reasoning_record.md#AC-example-promise) has $S=180$ non-input gates, so each candidate has $K=4+3+2(180+2)=371$ tests. In its zero-based numbering, write $x,y$ for input bits $6$ and $7$. Gates $1$ and $2$ compute $u=\neg x$, then $v=u\lor y$. On $a^+$ these last two input bits are both zero. To test gate $2$, read the proposed $u$, the actual $y$ and the proposed $v$. Reading $(1,0,0)$ exposes a false gate value, since $1\lor0=1$. The domain and value outputs are gates $178$ and $179$. Every cell contains $6$ pointer bits and $360$ transcript bits. With four cells in each of four columns, the full board has $4[4+16+4(6+360)]=5936$ input bits. Only one cell enters the tests for a given candidate. This four-column example uses $r=2$. Substituting $m=4$ into the formula $r=20\log_2m$ would give $r=40$. The classical lower bound applies for sufficiently large $m$.

[]{#decoder-repetitions}

## A.5 Repeating the projection experiment

For any requested error $0<\eta<1/2$, the projection experiment of Section 4 extends to every $k$. Phase kickback uses one query per sign diagonal, so a trial uses $k$ queries and has projection probability $p=\Phi^2$. On the promise, either $p\ge c=\delta^2$ or $p\le c/4$. Start each trial in fresh registers and repeat independently
$$
\rho=\lceil16c^{-1}\ln(1/\eta)\rceil
$$
times. Return one if at least $\rho c/2$ projections succeed. We use the following standard Chernoff estimates for the number $Z$ of successes in these independent Bernoulli trials:

| Promised case | Wrong decision | Tail bound used |
| --- | --- | --- |
| $p\ge c$ | $Z<\rho c/2$ | At most $\exp(-\rho c/8)$, hence at most $\exp(-\rho c/16)$. |
| $p\le c/4$ | $Z\ge\rho c/2$ | At most $\exp(-\rho c/16)$, by the upper tail at $p=c/4$ and monotonicity. |

Thus each error is at most $\eta$. The cap is $k\rho=O_k(\log(1/\eta))$ on every input. Here the subscript allows dependence on $k$, including the factor $c^{-1}=2^{10k}$. For a coherent comparison apply the trials in separate registers to the same fixed input. The resulting product state has the same joint outcome probabilities as the independent measurements.

[]{#exact-certification}

## A.6 Exact certification and the input size

The circuit uses integer arithmetic. The two factors $1/\sqrt m$ in $u$ and the $k-1$ internal Walsh factors give $\Phi=N/2^{t(k+1)}$ for an integer $N$. A fast Walsh transform recursively transforms two half-size vectors, then adds and subtracts their corresponding entries. These steps compute the numerator using additions and subtractions, and integer comparisons decide the two thresholds exactly. Since $m=4^t$ and $\sqrt m=2^t$, $\Phi\ge2^{-5k}$ is equivalent to $2^{5k}N\ge2^{t(k+1)}$. The small-value test is $2^{5k+1}|N|\le2^{t(k+1)}$. Words of $O(k\log m)$ bits suffice, including the threshold shifts. The [record's circuit construction](https://github.com/wcook04/quartic-query-lean/blob/ba49281af72b53d9cfbb43320d7efdeb29d7ceca/docs/reasoning_record.md#forr_circuit) gives the arithmetic and gate count. Each local gate test reads the proposed output and its at most two sources, using the actual address-input bits where the gate has external inputs.

**Why the bound in Section 5.1 holds.** For fixed $k$, Bansal and Sinha's lower bound for this one-sided promise [-@BansalSinha2021, Theorem 1.3 and Corollary 1.4] is at least a positive constant depending on $k$ times $m^{1-1/k}/(\log_2(km))^{1-1/k}$. Dividing this by the quantity $m^{1-1/k}/(\log_2m)^2$ used to define $L$ gives a factor of order $(\log m)^{1+1/k}$, which tends to infinity and absorbs the constant.

**Input length.** A column contains $m$ string bits, $rkm$ address-input bits, and $2^r$ cells, each containing $(m-1)\ell$ pointer bits and $rS$ transcript bits. Thus the general function has $n=m\bigl[m+rkm+2^r((m-1)\ell+rS)\bigr]$ input bits, which is $O_k(m^{22}(\log m)^3)$ since $2^r=m^{20}$. The input length is therefore polynomial in $m$. Both query bounds concern this same $n$-bit function, with $m$ counting its columns.

\Needspace{8\baselineskip}

[]{#direct-product-proof}

# Appendix B. The separate-cap direct product {.unnumbered}

Suppose one input $U$ is drawn from a distribution $\mu$, and $\beta$ is an upper bound on the probability of computing $P(U)$ using at most $L$ bit queries. Draw $r$ independent inputs $U_1,\ldots,U_r$ from $\mu$. A single algorithm can interleave its reads in any order, but must apply the limit $L$ to each input on every run. We prove that its chance of producing the entire word $(P(U_1),\ldots,P(U_r))$ correctly is at most $\beta^r$. The algorithm may also have random coins and other data drawn jointly independently of the inputs. The separately capped model is due to Shaltiel. We use Drucker's conditional-probability argument. [@Shaltiel2003; @Drucker2012, §1.3 and Lemmas 3.1–3.2]

Start with $P(x,y)=x\mathbin{\rm AND}y$, which equals one only on $11$. Give each of the four bit pairs equal probability and allow one query. If the first bit is zero, the answer is certainly zero. If it is one, the unread second bit is fair, so either guess has success $1/2$. The optimal success probability is $(1+1/2)/2=3/4$ (either bit could be read first). With two independent pairs and one read allowed from each, consider the first query to the first pair. The optimal success still available for the second pair is $3/4$ in either case. After a zero reply the product of the two best probabilities is $1\cdot(3/4)$. After a one reply it is $(1/2)(3/4)$. Their average is $9/16$, precisely $(3/4)^2$.

For general $P$, fix all the coins and other independent data, leaving the tree deterministic. Fix a history $\tau$ of queries and replies having positive probability. For sample $U_h$ let $E_h(\tau)$ consist of the inputs consistent with its recorded bits. A tuple in $E_1(\tau)\times\cdots\times E_r(\tau)$ reproduces the first reply, therefore the same second query and reply, and so on to the end of $\tau$. Conversely, every tuple producing that history must belong to this product. Thus conditioning on the history leaves independent samples with respective laws $\mu(\cdot\mid E_h(\tau))$.

Write $V_h(\tau)$ for the best success on $U_h$ with this conditional distribution and with its remaining queries (the original $L$ less the number already used on $U_h$). Suppose the next query reads $U_h$. Reading that bit and continuing optimally for each possible reply $b$ is one permissible strategy before the query, so
$$
\sum_b\Pr(b\mid\tau) V_h(\tau b)\le V_h(\tau).
$$
For every other sample both its conditional distribution and its remaining allowance are the same before and after this query. Multiplying the inequality by the other $V$'s shows that the conditional expected product after one query is at most its current value. The initial product is at most $\beta^r$.

At a leaf the tree outputs some fixed word $s$. By the independence just proved, the conditional probability that $s$ is correct is $\prod_h\Pr(P(U_h)=s_h\mid\tau)$. Each factor is at most $V_h(\tau)$, since guessing $s_h$ is an available strategy. Averaging first over leaves (there are at most $rL$ reads per run) and then over the fixed coins and other data proves the bound.

Return to the [final gap bound in Section 5](#classical-finish).

# Appendix C. Testing the classical hypotheses {.unnumbered}

Each of the following small experiments changes one feature of the probability argument in Section 5. The AND and parity functions let us count the possible inputs directly.

\Needspace{13\baselineskip}

### Independent planting

Choose a row in advance in each of four columns and read its bit. Each read has probability $1/4$ of finding its column's zero, so the expected number $Z$ of discoveries is $1$. Choosing $I$ independently and uniformly selects a discovered zero with probability $\mathbb EZ/4=1/4$.

Now choose $I$ uniformly among columns where a zero was found, falling back to a uniform choice from all four if none was found. By symmetry each column still has probability $1/4$ of selection. But the selected zero was read whenever *any* zero was found, with probability $1-(3/4)^4=175/256$. Independence from the run is what permits the averaging step in Section 5.1.

### Lightness is a joint event

Take AND on the three equally likely promised inputs $01,10,11$. A single query to either bit settles the answer on one input (the reply is zero) and leaves an equal choice between the two answers on the other two inputs. Thus the best one-query success is $2/3$.

Now read the first bit, return $0$ if it is zero, and otherwise read the second bit and return it. This procedure is always correct. It stays within one read only on input $01$. Its success *given* that it stays within one read is therefore $1$. The probability of success *and* staying within one read is $1/3$, below the one-query bound $2/3$. This is the distinction used in Section 5.2. [Further details of the example](https://github.com/wcook04/quartic-query-lean/blob/ba49281af72b53d9cfbb43320d7efdeb29d7ceca/docs/reasoning_record.md#CL-conditioning-counterexample)

[]{#predictor-trace}

### Two clocks in a capped simulation

Return to the four-query parity tree in Section 5.2. In this example $B_{i,s}$ denotes the cell at label $s$ in column $i$. The tree's fourth query specifies a bit of $B_{i,(a,0)}$ and the tree stops after that query. The simulator has a separate count $q$ of actual reads from $(a,b),(c,d)$ and a limit $L=1$. [The four-query tree](https://github.com/wcook04/quartic-query-lean/blob/ba49281af72b53d9cfbb43320d7efdeb29d7ceca/docs/reasoning_record.md#CL-simulator-example)

| Query number | Tree specifies | Simulator action |
| --- | --- | --- |
| $1$ | A string bit | Supply the bit, $q=0$. |
| $2$ | $a$ | Read it, so $q=1$. |
| $3$, if $a=1$ | Another string bit | Supply the bit, $q=1$. |
| $3$, if $a=0$ | $c$ | Stop and return $00$ before reading $c$. |
| $4$, if $a=1$ | A bit in $B_{i,10}$ | Return the proposed label $10$. |

On the $a=1$ branch, $10$ is correct exactly when $b=0$ and $c=d$. The chance of this branch *and* a correct label is $(1/2)(1/2)(1/2)=1/8$. On the $a=0$ branch, the default $00$ is also correct when $b=0$ and $c=d$, contributing another $1/8$. The predictor succeeds with probability $1/4$, whereas the probability that the tree stays within one target read and queries the correct cell at time four is only $1/8$. The difference comes entirely from correct default guesses. For a single fair pair, reading either bit leaves its parity uniformly random, so the two-input bound of Appendix B is $(1/2)^2=1/4$.

### Separate caps and independent information

*Separate caps.* Take the two independent AND inputs of Appendix B. With one read allowed from each, the probability of getting both answers right is at most $9/16$. With two reads to spend anywhere, read both bits of the first pair and guess zero for the second. This strategy is right on both answers with probability $3/4$.

*Joint independence.* For independent fair bits $X,Y$, suppose the task is to return $(X,Y)$ without any queries. A guess succeeds with probability $1/4$. If $X\oplus Y$ is supplied, output $(0,X\oplus Y)$. This is right whenever $X=0$, with probability $1/2$. The supplied bit is independent of each individual bit, yet it gives information about the pair. In Section 5.2 the simulated data are independent of the entire tuple.


# Appendix D. Exercises and answers {.unnumbered}

**Projection check.** For the two sign blocks obtained from $1111\,1000$ by the convention of Section 4, calculate the signed amplitude $\Phi$ and then the probability of the first measurement outcome. ([Answer](#answer-projection).)

[]{#question-1}**Question 1 (promise certification).** For the all-one column $2$ in the [example with an unpromised address input](#domain-bit-board), consider each of the four possible cell labels. Which of its two membership tests and two value tests fail? ([Answer](#answer-1).)

[]{#question-2}**Question 2 (conditional sampling and overshoot).** On the board with fixed arrows in Section 3.2, suppose the first two pivots were $2,4$. Calculate the chance of sampling column $1$ after one amplification iteration, then after two. For the separate example in Section 3.1 the weights after pivot $2$ are $(1,0,1/2,1/4)$. Suppose the next pivot is $4$, and that the probabilities of keeping the four labels against it are $(1,3/4,1/2,0)$. Find the probability of drawing each label and obtaining acceptance, and its conditional probability given acceptance. ([Answer](#answer-2).)

[]{#question-3}**Question 3 (independent planting).** In the first experiment in Appendix C, now read two fixed distinct rows per column. What is the probability of reading the zero in column $I$ when $I$ is chosen independently? What is it under the second selection rule? If later queries may depend on earlier replies, which identity still holds for an independent $I$? ([Answer](#answer-3).)

[]{#question-4}**Question 4 (two query counts).** In the [four-query parity example](#predictor-trace), change the $a=0$ branch so that query three specifies a bit in $B_{i,00}$. Suppose the tree stops after that read. What is the probability that $a=0$ and this is the true cell? Including the $a=1$ branch, what is the probability that the tree queries the true cell at time three or four and uses at most one target read in the whole run? Repeat the latter calculation if the $a=0$ branch reads $c$ *after* the cell query. ([Answer](#answer-4).)

[]{#question-5}**Question 5 (the power $3.5$).** Fix $k=4$. Which powers below four does Section 6 exclude using this one family of boards? Give a value of $k$ for which the calculation excludes $R(f)\le C(1+Q(f))^{3.5}$ itself. ([Answer](#answer-5).)

**Combined explanation.** Why is an all-one column with a valid certificate likely to be on the quantum list even if some trials produce no new pivot? In particular, what happens in a comparison with that column if the other proposed address comes from unpromised inputs? On the classical side, explain how the proposed coordinate of a cell query gives a prediction on the first board. Use the three events of Section 5 to bound the probability of different outputs by $4c+c+c/m^8$ when the query budget is at most $c\,mL$. Which part of the proof that $\alpha_{\rm tot}=4$ still needs a theorem about *all* total functions? ([Answer](#answer-combined).)

## Answers

[]{#answer-projection}**Projection check.** The first sign block is $(-1,-1,-1,-1)$ and its dot product with $(2,-2,-2,-2)$ is $4$. Thus the signed amplitude is $\Phi=4/8=1/2$ and projection probability is $|\Phi|^2=1/4$.

[]{#answer-1}**[Question 1](#question-1).** Both pointer and string conditions hold, and every recorded gate value is correct. The membership bits are $(0,1)$, so the first membership test fails at all four labels. The recorded value bits are $00$, so each digit $1$ in the label gives one additional failure. The failure counts at $00,01,10,11$ are therefore $1,2,2,3$.

\Needspace{15\baselineskip}

[]{#answer-2}**[Question 2](#question-2).** On the fixed-arrow board the weights after pivot $2$ are $(1,0,0,1)$. Multiply these, entry by entry, by the probabilities against $4$, namely $(1,0,1,0)$. This leaves $(1,0,0,0)$. A single unamplified preparation has success probability $q=1/4$, and every success returns column $1$. Thus $\theta=\pi/6$. One iteration gives success probability $\sin^2(3\pi/6)=1$, and two iterations give $\sin^2(5\pi/6)=1/4$. For the unequal-weight example, the new weights are $(1,0,1/4,0)$. Dividing by four gives the probabilities of drawing each index and accepting it, $(1/4,0,1/16,0)$. They add to $5/16$. Dividing by this total gives the conditional probabilities $(4/5,0,1/5,0)$.

[]{#answer-3}**[Question 3](#question-3).** Each zero is in a read position with probability $2/4$. With independent selection, $\Pr(\text{selected zero read})=\mathbb EZ/4=1/2$. Under the second selection rule, reading at least one zero suffices, which has probability $1-(1/2)^4=15/16$ because the row choices are fixed and the zero locations independent. For adaptive queries the identity $\mathbb EZ/4$ still holds for independent $I$. Once the whole run on the first board is specified, exactly $Z$ of the four choices of $I$ select a discovered zero.

[]{#answer-4}**[Question 4](#question-4).** The changed query at time three specifies the true cell when $a=0,b=0,c=d$, with probability $(1/2)(1/2)(1/2)=1/8$. If the tree stops after it, the target read count is one. The other branch gives a true-cell query at time four within the same cap when $a=1,b=0,c=d$, also with probability $1/8$. The two events are disjoint, so their union has probability $1/4$. If $c$ is read afterwards, there are two target reads on the $a=0$ branch. The cell query still occurred, but the run now exceeds the limit. Only the $a=1$ event at time four counts, with probability $1/8$.

[]{#answer-5}**[Question 5](#question-5).** At $k=4$ the exponent $4-2/k$ is $3.5$, so the ratio in Section 6 diverges for every $\alpha<3.5$ and proves $\alpha_{\rm tot}\ge3.5$. At $\alpha=3.5$ the power $2-1/k-\alpha/2$ of $m$ in the lower bound on the ratio is zero, leaving a reciprocal power of $\log m$. To get a diverging lower bound at this particular $\alpha$, choose $k=5$, giving $2-1/5-3.5/2=1/20>0$.

[]{#answer-combined}**Combined explanation.** When the correct address is used for the winning column, its pointer identifies a zero in the other column. Every pointer in the reverse direction identifies a one, for every proposed address. The probability of the correct comparison result is therefore at least the probability of decoding the winner's own address correctly. After $T$ pivots other than the winning one, the winning index would still have weight at least $(1-\varepsilon)^T\ge1-T\varepsilon>1/2$, yet the expected remaining total weight in the ideal sampling calculation is at most $m/2^T$. This bounds the probability of missing that index. Before its inclusion the actual sampler has success probability before amplification at least $1/(2m)$ and its probability of exhausting its trials is at most $\varepsilon$ per stage. Once a column is listed, later sampling failures cannot remove it.

In the classical simulation, stop at the proposed cell query and output its label. Stop earlier with a default if another target read would exceed $L$. A query to the true cell of a light column is therefore a correct prediction at that query time. For $G\le c\,mL$, the probabilities of reading the erased zero, selecting a heavy column, and visiting the true cell of a light selected column are respectively at most $4cL/m$, $c$, and $c\,mL\,m^{-10}$. Here $r=20\log_2m$ gives the last factor $m^{-10}$. The estimates use independence of $I$ to average over discovered zeros and heavy columns. For light columns one sums over times and averages over $I$. Since $L\le m$, the three bounds sum to at most $4c+c+c/m^8$. The constructed functions exclude every exponent less than four. The universal deterministic query bound gives the inequality at exponent four.

# Appendix E. Following the formal proofs {.unnumbered}

The [theorem index](https://github.com/wcook04/quartic-query-lean/blob/main/docs/proof_index.md) connects the mathematical statements to their Lean definitions and proofs. For example, the [winning condition](https://github.com/wcook04/quartic-query-lean/blob/main/docs/proof_index.md#def-wins) requires every address input of a winning column to satisfy the promise. In the example of Section 4, this excludes column $2$, the only all-one column. The [family theorem](https://github.com/wcook04/quartic-query-lean/blob/main/docs/proof_index.md#thm-headline) uses one circuit for both query bounds. The [explicit bounds](https://github.com/wcook04/quartic-query-lean/blob/main/docs/proof_index.md#src-constants) give the logarithmic exponent six and the factor $1/400$ in Section 6.

The formal quantum proof uses the probability distribution of the measured column label and verifies the resulting candidates. The separate statement that preserves the entire normalized successful quantum state is still to be formalized. The [optimal-exponent theorem](https://github.com/wcook04/quartic-query-lean/blob/main/docs/proof_index.md#thm-alpha) combines the constructed family with a formal proof of the universal quartic bound.

# References {.unnumbered}

::: {#refs}
:::

<!-- lean-links -->
<!-- /lean-links -->
