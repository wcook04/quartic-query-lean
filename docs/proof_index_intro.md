# Theorems and proofs of the nearly quartic query separation

The separation theorem and construction are due to OpenAI. The three accompanying papers explain the proof at different levels: the [specialist companion](expert_companion.md), the [examples-first exposition](exposition.md), and the [complete reconstruction](reasoning_record.md). This index connects their mathematical results to formal statements and the implementations that prove them.

A specification states the intended mathematical obligation. Its intentional proof placeholder is not the proof: the separately compiled solution is checked against that specification. The links below therefore include proof implementations, not only specifications. Formal proofs of the same conclusion may use different intermediate statements from the printed argument. Detailed source versions, checks and limitations are retained in the [verification supplement](verification_details.md) and the machine-readable correspondence records.

## Main results

- **Optimal exponent four.** Every total Boolean function satisfies a universal quartic upper bound, and no smaller exponent works uniformly over all total functions. See the [specification][thm-alpha], the [proof of the equality][src-alpha] and the [exclusion of smaller exponents][src-no-smaller-exponent].
- **One family, with one circuit for both bounds.** For every fixed integer $k\ge2$, the same realizing circuit defines a total function with quantum cost $O_k(\sqrt m\,\log^{b_k}m)$ and randomized cost greater than $\lfloor mL_{k,m}/100\rfloor$ for all sufficiently large powers of four. The [headline specification][thm-headline] also includes the optimal exponent and universal quartic bound; its [implementation][src-theorem] combines the family and exponent results.
- **Explicit family bounds.** The [named-family proof][src-constants] fixes the actual Forrelation circuit and gives logarithmic exponent six and classical coefficient $1/400$. This is stronger in its constants than the existential family specification; its verification evidence is listed separately in the supplement.
- **Failure of a universal cubic bound.** There is no constant bounding $R(f)$ by $C Q(f)^3$ for every total Boolean function. See the [specification][thm-cubic] and [proof][src-cubic]. The fixed-$k$ family with $k=3$ already suffices.

## The partial function and its certificates

- **Forrelation hardness.** The [fixed-parameter specification][thm-forrelation] and [hardness proof][src-forr-implementation] establish the eventual allowance used by the construction. The stronger [uniform estimate][src-forrelation-uniform] gives $R(P_{k,m})>2m^{1-1/k}/(18225k^2\ln(4km))$ for integers $k\ge2$, $t\ge0$, $m=4^t$ and $15k+2\le2t$. The explicit growing-parameter schedule is an ordinary deduction from uniform upper and lower bounds; it is not a clause of the headline family specification.
- **An exact promise-and-value circuit.** The [circuit construction][src-forr-circuit] and [size theorem][src-forr-circuit-exists] provide one circuit whose domain bit recognizes the promise exactly and whose value bit is correct there. Quantum decoding alone does not recognize unpromised inputs.
- **Winning and local certification.** The [winning condition][def-wins] requires an all-one column, promised address inputs, true transcripts and outward pointers reaching zeros. The [local-test equivalence][src-winner-tests] proves that all tests pass exactly at a winning column's true address; [uniqueness][src-winner-unique] follows because two all-one columns cannot point to zeros in each other.

## The quantum argument

- **Exact successful-label sampling.** Fresh comparison registers give product weights. The [tensor preparation][src-tensor-stage] and [measured-label amplification theorem][src-amplify-measured] identify the exact conditional pivot law, not an approximation to it. The finite schedule has a cap on every input, including when its success probability is below the promised threshold.
- **A short candidate list.** The [bounded tournament theorem][src-quantum-tournament] applies to complementary comparison probabilities with a dominant candidate; comparisons among other candidates may be arbitrary. This is a separate candidate-list theorem. The headline query bound uses a measured-label Boolean continuation instead.
- **Verification and the total quantum bound.** The [verifier][src-verifier] checks a proposed cell by searching its local tests. The [combined upper bound][src-prop33] gives $O_k(\sqrt m\log^6m)$ queries with a worst-case cap and bounded error on every total input.
- **The retained-state distinction.** The [retained-state amplification theorem][src-opaque-amplifier] fixes its selector before the preparation unitary is supplied and factors the successful state as the normalized successful state in the literal original register tensored with an auxiliary vector, for success conditions specified on basis labels. The general fixed-projector reduction and literal flag/Hadamard identification through the chosen physical compilation remain unproved; the [verification supplement](verification_details.md#upper-missing-physical-state) states that remaining correspondence. The headline Boolean proof uses the measured-label law and query cap.

## The classical argument and the universal upper bound

- **Independent inputs with separate caps.** The [direct-product proof][src-direct-product] bounds simultaneous success by the product of the one-input optima. The [realized capped-tree theorem][src-direct-product-capped] and [cap-event statement][cmp-direct-product] distinguish an unconditional success bound for a capped algorithm from a joint success-and-compliance event. Conditioning on compliance is not justified.
- **From a cell visit to a prediction.** The [fixed-time event bound][src-per-time] uses a predictor that stops before exceeding its target-query allowance and has a default output on every other exit. The [planted-input reduction][src-prop42] combines that bound with the independently erased zero and heavy-column count. It applies to every realizing circuit, allowing the same circuit as in the quantum upper bound.
- **The universal quartic bound.** The headline proof uses the [complexity-library route][src-complexitylib]. The reconstruction prints the star-adversary argument; the [separate quartic theorem][src-theorem-a1] gives that route's explicit constant. Agreement of the conclusions does not imply that the printed and formal dependency paths are identical.

## Source directory

The entries below retain exact declaration destinations. A declaration link identifies source; the linked verification supplement supplies the corresponding build, axiom and statement-comparison evidence.
