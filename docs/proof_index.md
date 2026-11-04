# Theorems and proofs of the nearly quartic query separation

The separation theorem and construction are due to OpenAI. The three accompanying papers explain the proof at different levels: the [specialist companion](expert_companion.md), the [examples-first exposition](exposition.md), and the [complete reconstruction](reasoning_record.md). This index connects their mathematical results to formal statements and the implementations that prove them.

A specification states the intended mathematical obligation. Its intentional proof placeholder is not the proof: the separately compiled solution is checked against that specification. The links below therefore include proof implementations, not only specifications. Formal proofs of the same conclusion may use different intermediate statements from the printed argument. Detailed source versions, checks and limitations are retained in the [verification supplement](verification_details.md) and the machine-readable correspondence records.

## Main results

- **Optimal exponent four.** Every total Boolean function satisfies a universal quartic upper bound, and no smaller exponent works uniformly over all total functions. See the [specification](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L326), the [proof of the equality](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Unconditional.lean#L17-L18) and the [exclusion of smaller exponents](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Exponent.lean#L230-L236).
- **One family, with one circuit for both bounds.** For every fixed integer $k\ge2$, the same realizing circuit defines a total function with quantum cost $O_k(\sqrt m\,\log^{b_k}m)$ and randomized cost greater than $\lfloor mL_{k,m}/100\rfloor$ for all sufficiently large powers of four. The [headline specification](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L328-L334) also includes the optimal exponent and universal quartic bound; its [implementation](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Unconditional.lean#L21-L29) combines the family and exponent results.
- **Explicit family bounds.** The [named-family proof](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionFamily.lean#L28-L40) fixes the actual Forrelation circuit and gives logarithmic exponent six and classical coefficient $1/400$. This is stronger in its constants than the existential family specification; its verification evidence is listed separately in the supplement.
- **Failure of a universal cubic bound.** There is no constant bounding $R(f)$ by $C Q(f)^3$ for every total Boolean function. See the [specification](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L336-L338) and [proof](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Unconditional.lean#L40-L44). The fixed-$k$ family with $k=3$ already suffices.

## The partial function and its certificates

- **Forrelation hardness.** The [fixed-parameter specification](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L340) and [hardness proof](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/ForrelationLower/Main.lean#L524-L525) establish the eventual allowance used by the construction. The stronger [uniform estimate](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/ForrelationLower/Uniform.lean#L525-L532) gives $R(P_{k,m})>2m^{1-1/k}/(18225k^2\ln(4km))$ for integers $k\ge2$, $t\ge0$, $m=4^t$ and $15k+2\le2t$. The explicit growing-parameter schedule is an ordinary deduction from uniform upper and lower bounds; it is not a clause of the headline family specification.
- **An exact promise-and-value circuit.** The [circuit construction](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Forrelation/Circuit.lean#L336-L339) and [size theorem](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Forrelation/Circuit.lean#L477-L482) provide one circuit whose domain bit recognizes the promise exactly and whose value bit is correct there. Quantum decoding alone does not recognize unpromised inputs.
- **Winning and local certification.** The [winning condition](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L262-L272) requires an all-one column, promised address inputs, true transcripts and outward pointers reaching zeros. The [local-test equivalence](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Construction/LocalTests.lean#L235-L238) proves that all tests pass exactly at a winning column's true address; [uniqueness](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Construction/Winner.lean#L54-L56) follows because two all-one columns cannot point to zeros in each other.

## The quantum argument

- **Exact successful-label sampling.** Fresh comparison registers give product weights. The [tensor preparation](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumTensor.lean#L322-L335) and [measured-label amplification theorem](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Amplify.lean#L345-L352) identify the exact conditional pivot law, not an approximation to it. The finite schedule has a cap on every input, including when its success probability is below the promised threshold.
- **A short candidate list.** The [bounded tournament theorem](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumTournamentFacts.lean#L283-L303) applies to complementary comparison probabilities with a dominant candidate; comparisons among other candidates may be arbitrary. This is a separate candidate-list theorem. The headline query bound uses a measured-label Boolean continuation instead.
- **Verification and the total quantum bound.** The [verifier](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumComparison.lean#L496-L507) checks a proposed cell by searching its local tests. The [combined upper bound](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Bound.lean#L270-L273) gives $O_k(\sqrt m\log^6m)$ queries with a worst-case cap and bounded error on every total input.
- **The retained-state distinction.** The [abstract retained-state theorem](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean#L17-L52) concerns a stronger output interface than a measured label. Its successful-factor identity does not yet establish correspondence with the designated original physical subsystem after compilation, routing and uncomputation. That additional correspondence is not needed by the headline Boolean proof.

## The classical argument and the universal upper bound

- **Independent inputs with separate caps.** The [direct-product proof](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/DirectProduct.lean#L302-L308) bounds simultaneous success by the product of the one-input optima. The [realized capped-tree theorem](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalDirectProduct.lean#L877-L884) and [cap-event statement](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean#L18-L25) distinguish an unconditional success bound for a capped algorithm from a joint success-and-compliance event. Conditioning on compliance is not justified.
- **From a cell visit to a prediction.** The [fixed-time event bound](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L340-L348) uses a predictor that stops before exceeding its target-query allowance and has a default output on every other exit. The [planted-input reduction](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/Section4.lean#L16-L32) combines that bound with the independently erased zero and heavy-column count. It applies to every realizing circuit, allowing the same circuit as in the quantum upper bound.
- **The universal quartic bound.** The headline proof uses the [complexity-library route](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Bridge/DecisionTree.lean#L65-L68). The reconstruction prints the star-adversary argument; the [separate quartic theorem](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixA.lean#L65-L70) gives that route's explicit constant. Agreement of the conclusions does not imply that the printed and formal dependency paths are identical.

## Source directory

The entries below retain exact declaration destinations. A declaration link identifies source; the linked verification supplement supplies the corresponding build, axiom and statement-comparison evidence.

The [machine-readable index](lean_links.json) and [statement correspondence](../corpus/comparator_map.json) retain exact identifiers and checks.

<a id="amplifier-config"></a>
### The Comparator configuration of the amplifier statement

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/UniformAmplifier/comparator.json)

<a id="amplifier-solution"></a>
### The proof checked against the amplifier statement

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/UniformAmplifier/Solution.lean)

<a id="cmp-amplifier"></a>
### Bounded amplification returning the good state

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean#L17-L52)

<a id="cmp-degree"></a>
### Degree conventions

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/Degree/Challenge.lean#L14-L20)

<a id="cmp-direct-product"></a>
### The direct product with independent randomness

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean#L18-L25)

<a id="cmp-eq11"></a>
### The erased-zero identity with the bound 4G/m^2

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/Eq19/Challenge.lean#L19-L24)

<a id="cmp-le-iff"></a>
### The compared equivalences between complexity bounds and budget tests

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Foundations/Challenge.lean#L326-L330)

<a id="cmp-lemma22"></a>
### Four facts about winners

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Construction/Challenge.lean)

<a id="cmp-lemma22-full"></a>
### Lemma 2.2 as one statement

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/ConstructionFull/Challenge.lean#L14-L60)

<a id="cmp-negative"></a>
### The five wrong solutions

[Read the source](https://github.com/wcook04/quartic-query-lean/tree/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Negative)

<a id="cmp-winners"></a>
### The four compared winner theorems

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Construction/Challenge.lean#L326-L341)

<a id="cmp-zero-cost"></a>
### Zero-cost characterisation of D, R and Q

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/ModelZero/Challenge.lean#L11-L14)

<a id="def-D"></a>
### The definition of D

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L76-L77)

<a id="def-DLe"></a>
### The deterministic budget test

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L67-L69)

<a id="def-F"></a>
### The definition of F

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L274-L285)

<a id="def-G"></a>
### The definition of G

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L302-L303)

<a id="def-L"></a>
### The definition of L

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L297-L300)

<a id="def-P"></a>
### The definition of P

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L175-L182)

<a id="def-Q"></a>
### The definition of Q

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L139-L140)

<a id="def-QLe"></a>
### The quantum budget test

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L133-L137)

<a id="def-R"></a>
### The definition of R

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L71-L74)

<a id="def-RLe"></a>
### The randomized budget test

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L62-L65)

<a id="def-adaptive"></a>
### Quantum query algorithms

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L101-L107)

<a id="def-alpha"></a>
### The definition of the optimal exponent

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L317-L318)

<a id="def-bansal-sinha"></a>
### The Forrelation hardness statement

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L305-L309)

<a id="def-basis"></a>
### The basis states

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L84-L87)

<a id="def-bit-input"></a>
### Bit inputs

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L15)

<a id="def-bitloc"></a>
### The input bits of a column

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L232-L238)

<a id="def-circuit"></a>
### Fan-in-two circuits

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L190-L199)

<a id="def-comparison"></a>
### The unused comparison predicate

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L289-L293)

<a id="def-compliant"></a>
### Success together with respecting the caps

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/RealizedCaps.lean#L111-L120)

<a id="def-gate"></a>
### Gate consistency

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L208-L213)

<a id="def-hit"></a>
### The hitting probability and expected count

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/Eq19/Spec.lean#L65-L76)

<a id="def-numerator"></a>
### The Forrelation numerator

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L160-L166)

<a id="def-oracle"></a>
### The bit oracle

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L89-L94)

<a id="def-output-mass"></a>
### The output probability of a quantum algorithm

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L96-L126)

<a id="def-partial"></a>
### Partial Boolean functions

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L18-L19)

<a id="def-pointer"></a>
### Pointer decoding

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L249-L260)

<a id="def-querycap"></a>
### The query cap

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L109-L116)

<a id="def-randomized"></a>
### Randomized algorithms

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L46-L60)

<a id="def-realises"></a>
### Exact circuits for P

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L215-L221)

<a id="def-reindex"></a>
### Renaming the coordinates of a partial function

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L27-L29)

<a id="def-totalise"></a>
### Totalisation

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L21-L22)

<a id="def-tree"></a>
### Decision trees and their depth

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L33-L44)

<a id="def-universal"></a>
### The universal power bound

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L311-L315)

<a id="def-wins"></a>
### The winning condition

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L262-L272)

<a id="direct-product-config"></a>
### The Comparator configuration of the direct-product statement

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/RealizedCaps/comparator.json)

<a id="src-alpha"></a>
### The unconditional exponent theorem

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Unconditional.lean#L17-L18)

<a id="src-alpha-infimum"></a>
### The infimum argument for the exponent

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Exponent.lean#L240-L248)

<a id="src-amplification"></a>
### The abstract bounded amplification statement

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Amplification/Bounded.lean#L238-L293)

<a id="src-amplify-measured"></a>
### Bounded amplification of the measured label

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Amplify.lean#L345-L352)

<a id="src-budget"></a>
### The explicit quantum budget

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Bound.lean#L86-L90)

<a id="src-budget-constant"></a>
### The constant of the explicit quantum budget

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Bound.lean#L52-L57)

<a id="src-budget-exponential"></a>
### The quantum bound with constant 2^53 k 2^(10k)

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Bound.lean#L286-L290)

<a id="src-coherent-amplify"></a>
### The coherent trial loop of Lemma 3.1

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumAmplification.lean#L352-L361)

<a id="src-common-workspace"></a>
### A common workspace for finitely many samplers

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumWorkspace.lean#L23-L34)

<a id="src-comparison-state"></a>
### The comparison state

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumComparison.lean#L216-L223)

<a id="src-complexitylib"></a>
### The agreement of deterministic complexity with complexitylib

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Bridge/DecisionTree.lean#L65-L68)

<a id="src-complies"></a>
### Compliance with the caps

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/RealizedCaps.lean#L50-L61)

<a id="src-conditional-value-module"></a>
### The conditional-value development

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalDirectProduct.lean)

<a id="src-constants"></a>
### Theorem 1 with the constants 6 and 1/400

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionFamily.lean#L28-L40)

<a id="src-construction-complete"></a>
### The complete evaluator theorem for Lemma 2.2

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionComplete.lean#L23-L67)

<a id="src-construction-full"></a>
### The construction lemma with physical-coordinate support

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionFull.lean#L21-L69)

<a id="src-construction-models"></a>
### The domain wrappers of the construction

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionModels.lean)

<a id="src-count"></a>
### The number of queries to each instance

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/RealizedCaps.lean#L101-L107)

<a id="src-coupled-average"></a>
### The joint average over the addresses, zeros and planted column

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/Planted/Main.lean#L26-L29)

<a id="src-cubic"></a>
### The unconditional failure of the cubic bound

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Unconditional.lean#L40-L44)

<a id="src-decoder"></a>
### The correctness of the decoder

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumComparison.lean#L52-L59)

<a id="src-direct-product"></a>
### The weighted direct product

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/DirectProduct.lean#L302-L308)

<a id="src-direct-product-average"></a>
### The finite-seed averaged direct product

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalDirectProduct.lean#L900-L909)

<a id="src-direct-product-capped"></a>
### The capped direct product by conditional values

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalDirectProduct.lean#L877-L884)

<a id="src-direct-product-caps"></a>
### The direct product with realized caps

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/RealizedCapsExternal.lean#L24-L34)

<a id="src-direct-product-module"></a>
### The weighted direct-product development

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/DirectProduct.lean)

<a id="src-discovered-zeros"></a>
### The number of discovered zeros

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L180-L185)

<a id="src-dummy"></a>
### The dummy input

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/Planted/Inputs.lean#L48-L54)

<a id="src-equation-15"></a>
### The tensor preparation of equation (15)

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumTensor.lean#L114-L131)

<a id="src-equation-19"></a>
### The whole erased-zero identity and bound

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/Eq19Whole.lean#L26-L33)

<a id="src-equation-19-expectation"></a>
### The erased-zero identity with the bound on E Z/m

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/Eq19Complete.lean#L23-L31)

<a id="src-equation-two"></a>
### The construction-family equation

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionFamily.lean#L56-L67)

<a id="src-erased-zero-bound"></a>
### The erased-zero bound with coefficient four

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L249-L254)

<a id="src-erased-zero-identity"></a>
### The identity Pr[hit] = E Z/m

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L204-L209)

<a id="src-error-bound"></a>
### The error bound of the complete algorithm

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumComparison.lean#L536-L549)

<a id="src-eventual-comparison"></a>
### The eventual strict comparison of powers

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Exponent.lean#L115-L123)

<a id="src-expected-zeros"></a>
### The expected number of discovered zeros

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L197-L202)

<a id="src-expected-zeros-bound"></a>
### The bound E Z <= 4G/m

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L238-L243)

<a id="src-exponent-choice"></a>
### The choice of k beating a given exponent

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Exponent.lean#L159-L161)

<a id="src-family-conditional"></a>
### The family bounds under the lower-bound premise

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Conditional.lean#L22-L31)

<a id="src-fixed-sequence"></a>
### The fixed-sequence normal form

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Bridge/Deferred.lean#L282-L290)

<a id="src-forr-census"></a>
### The finite census of small Forrelation instances

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Forrelation/Sanity.lean)

<a id="src-forr-circuit"></a>
### The canonical Forrelation circuit

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Forrelation/Circuit.lean#L336-L339)

<a id="src-forr-circuit-exists"></a>
### The existence of the Forrelation circuit

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Forrelation/Circuit.lean#L477-L482)

<a id="src-forr-implementation"></a>
### The proof of the Forrelation lower bound

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/ForrelationLower/Main.lean#L524-L525)

<a id="src-forr-integer"></a>
### The integer form of the Forrelation numerator

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean#L139-L152)

<a id="src-forr-output-bits"></a>
### The output rules of the constructed circuit

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationCircuit.lean#L55-L69)

<a id="src-forr-product"></a>
### The alternating product and its threshold

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean#L48-L54)

<a id="src-forr-promise"></a>
### The complete Forrelation promise

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean#L57-L65)

<a id="src-forr-tests"></a>
### The integer comparisons and output rules

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean#L166-L178)

<a id="src-forrelation-uniform"></a>
### The uniform Forrelation estimate

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/ForrelationLower/Uniform.lean#L525-L532)

<a id="src-found-zero"></a>
### The event that the dummy run finds a zero

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/Planted/ZeroSearch.lean#L156-L159)

<a id="src-le-iff-classical"></a>
### The classical equivalences between complexity bounds and budget tests

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Model/Classical.lean#L277-L282)

<a id="src-le-iff-quantum"></a>
### The quantum equivalence between complexity bounds and budget tests

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Model/Quantum.lean#L413-L414)

<a id="src-lemma-a2"></a>
### The spectral-adversary lemma

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixASpectralAdversary.lean#L105-L113)

<a id="src-lemma-a3"></a>
### The star and sensitivity estimates

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixAStar.lean#L480-L484)

<a id="src-lemma-a4"></a>
### The degree bound through spectral sensitivity

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixAHuangRoute.lean#L112-L117)

<a id="src-lemma-a5"></a>
### The bridge to Midrijanis's bound

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixASensitivity.lean#L288-L291)

<a id="src-lemma21"></a>
### Lemma 2.1 as one statement

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationComplete.lean#L63-L90)

<a id="src-lemma21-ii"></a>
### The coherent physical implementation of Lemma 2.1(ii)

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationComplete.lean#L21-L44)

<a id="src-lemma21-iii"></a>
### The circuit bound of Lemma 2.1(iii)

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationCircuit.lean#L109-L115)

<a id="src-no-smaller-exponent"></a>
### The exclusion of exponents below four

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Exponent.lean#L230-L236)

<a id="src-opaque-amplifier"></a>
### The opaque-preparation amplifier

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/UniformEndpoint.lean#L15-L53)

<a id="src-per-time"></a>
### The per-time event

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L340-L348)

<a id="src-planted-core"></a>
### The conditional planted lower bound

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/Planted/Main.lean#L201-L206)

<a id="src-pointer-support"></a>
### The essential coordinates of the pointer tests

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionPointerSupport.lean#L77-L85)

<a id="src-proc"></a>
### Abstract amplification procedures

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Amplification/Procedure.lean#L31-L39)

<a id="src-prop33"></a>
### Proposition 3.3 as an algorithm for the canonical circuit

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Bound.lean#L270-L273)

<a id="src-prop42"></a>
### Proposition 4.2, for every realising circuit and for the canonical circuit

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/Section4.lean#L16-L32)

<a id="src-q-bound"></a>
### The quantum query bound with logarithmic exponent six

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Bound.lean#L277-L280)

<a id="src-quantum-tournament"></a>
### The quantum tournament bound

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumTournamentFacts.lean#L283-L303)

<a id="src-quartic-cap"></a>
### The quartic bound at a quantum query cap

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixA.lean#L46-L51)

<a id="src-quartic-hybrid"></a>
### The hybrid quartic bound with coefficient 19600

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixA.lean#L104-L106)

<a id="src-quartic-minimum"></a>
### The quartic bound at the attained quantum minimum

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixA.lean#L59-L62)

<a id="src-quartic-older"></a>
### The quartic bound with coefficient 20736

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Appendix/TheoremA1.lean#L51-L53)

<a id="src-query-oracle"></a>
### The bit-oracle identities

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionModels.lean#L178-L185)

<a id="src-ratio-abstract"></a>
### The exponent ratio for abstract sequences

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalAsymptotics.lean#L332-L348)

<a id="src-ratio-arithmetic"></a>
### The finite quotient calculation

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalAsymptotics.lean#L232-L240)

<a id="src-ratio-family"></a>
### The exponent ratio for the named family

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalAsymptotics.lean#L369-L386)

<a id="src-reach"></a>
### The dependency printer

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/scripts/Reach.lean)

<a id="src-repetitions"></a>
### The repetition count of the Forrelation sampler

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Forrelation/Repetition.lean#L191-L193)

<a id="src-runs"></a>
### Bit-query programs with a given output law

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Compile.lean#L329-L332)

<a id="src-samples"></a>
### Coherent samplers

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Sampler.lean#L113-L117)

<a id="src-stage-sampler"></a>
### The stage sampler of the tournament

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Tournament.lean#L62-L65)

<a id="src-tensor-stage"></a>
### The tensor stage built from samplers

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumTensor.lean#L322-L335)

<a id="src-theorem"></a>
### The unconditional Theorem 1.1

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Unconditional.lean#L21-L29)

<a id="src-theorem-a1"></a>
### Theorem A.1 in its displayed form

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixA.lean#L65-L70)

<a id="src-theorem-conditional"></a>
### Theorem 1.1 under the Forrelation hardness hypothesis

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Conditional.lean#L50-L60)

<a id="src-tournament-runs"></a>
### The acceptance guarantee of the tournament

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Tournament.lean#L362-L378)

<a id="src-transcript"></a>
### Consistent transcripts are true evaluations

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Construction/Transcript.lean#L62-L65)

<a id="src-uniform-zero"></a>
### The uniform position of an unseen zero

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalUniformZero.lean#L248-L257)

<a id="src-universal-power"></a>
### The universal quartic power bound

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Appendix/TheoremA1.lean#L68-L70)

<a id="src-verifier"></a>
### The verifier

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumComparison.lean#L496-L507)

<a id="src-walsh"></a>
### The Walsh definitions

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean#L26-L37)

<a id="src-winner-dominates"></a>
### The dominance of the winner

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumComparison.lean#L294-L302)

<a id="src-winner-paper"></a>
### The formal winning condition is the paper's

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Construction/LocalTests.lean#L326-L330)

<a id="src-winner-tests"></a>
### Winning as the conjunction of the local tests

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Construction/LocalTests.lean#L235-L238)

<a id="src-winner-unique"></a>
### The uniqueness of the winning pair

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Construction/Winner.lean#L54-L56)

<a id="src-zero-successor"></a>
### The induction with |U|+1

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/Planted/ZeroSearchSuccessor.lean#L17-L22)

<a id="src-zero-two"></a>
### The bound 2G/m^2

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L213-L219)

<a id="statement-config"></a>
### The Comparator configuration of the four theorems

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/comparator.json)

<a id="statement-file"></a>
### The statement file

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean)

<a id="statement-receipt"></a>
### The recorded paranoid Comparator run of the four theorems

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/corpus/receipts/comparator-Unconditional-2026-11-03T121735042729+0000.json)

<a id="statement-solution"></a>
### The proofs Comparator checks against the statement file

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Solution.lean)

<a id="thm-all"></a>
### The four compared theorems

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L326-L340)

<a id="thm-alpha"></a>
### The exponent theorem

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L326)

<a id="thm-cubic"></a>
### The failure of the cubic bound

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L336-L338)

<a id="thm-forrelation"></a>
### The Forrelation lower bound

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L340)

<a id="thm-headline"></a>
### The headline theorem

[Read the source](https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L328-L334)
