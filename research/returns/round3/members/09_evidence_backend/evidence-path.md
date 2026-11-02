# Independent semantics and current evidence for the quartic-query development

**Focused round-three return, job 09 — 2 November 2026.** This is an advisory backend and statement-correspondence contribution. It is not an integrated paper or a new native verification of the quartic theorem. The original packet remains unchanged.

<!-- passage:EVID-RESULT -->
## 1. Result and remaining boundary

The existing evidence backend correctly preserves source-bound build, comparison and reach records. Its principal remaining defect is that a successful rebuild can revive an old mathematical correspondence judgment after the definitions have changed. This return supplies a tested patch that makes **review freshness a separate condition**. It also enforces the existing decision to withhold the separately derived `r2-live-*` helpers from the preprint-only graph.

The mathematical contribution is concrete: independently stated tests of the actual query models, a proposed theorem containing both clauses of equation (19), an independently authored finite-law specification and explicit bridges to the project definitions, and discriminating negative controls. The new Lean sources are **proposed and uncompiled**. A real `lean-exposition extract --build` launch was attempted on an accepted, source-current existing declaration; it exited 127 because the executable is absent. Native extraction, new Lean elaboration, and new Comparator judgments remain incomplete.

The source audit verified all 400 payload members against the packet manifest, all 124 local Lean/configuration inputs against the source snapshot, and the distinction between 12 current supplied receipts and 11 legacy-unbound receipts. These checks establish agreement of supplied bytes and recorded fields. They do not independently reproduce the recorded native executions. The attached text file `Pasted text(20261102-190840-1).txt` was unavailable and has not been used.
<!-- /passage:EVID-RESULT -->

## 2. The objects being checked

The preprint fixes worst-case **bit-query** complexity: an algorithm is chosen before its input, correctness is pointwise on the promise domain, and success is at least $2/3$. A randomized query cap bounds every positive-weight decision tree; a quantum query cap bounds every measurement branch. See OpenAI [OAI26], §1, p. 1, §2.1, pp. 3–4, and the supplied `Statement.lean`. The proposed tests exercise finite consequences of these definitions; they do not replace a review of the entire models.

Three questions have separate answers. Does the Lean kernel accept a proof of a particular proposition? Does that proposition agree with the challenge and its referenced definitions? Does the proposition express the mathematics intended by the preprint? The supplied Comparator recursively checks non-target constants as well as theorem types. Empty `definition_names` does **not** cause referenced definitions to be ignored: it leaves no definition holes. But matching a shared erroneous definition is still agreement with that erroneous definition. This distinction agrees with the official Lean validation documentation [LEAN-VALIDATION] and the actual supplied `Lake/Check/Compare.lean` implementation [LAKE436].

For this return, “independent” describes how the expected mathematical answer and experiment were specified. It does not mean a new foundational logic, an unseen human author, a complete independent formalization, or a completed native run.

<!-- passage:EVID-IDENTITY -->
## 3. Independent model expectations

### 3.1. A zero-query program cannot compute one-bit identity

Let $f(x)=x$ on the two one-bit inputs. A deterministic tree of depth zero is a constant leaf. A finite mixture of such trees therefore has a true-answer probability $p$ that is independent of the input. Correctness on the true input gives $p\ge 2/3$. Correctness on the false input gives $1-p\ge 2/3$. Adding them yields $1\ge4/3$, a contradiction. Thus

\[
\neg\operatorname{RLe}(f,0).
\]

The proposed `QuarticQuery.SemanticReview.identity_not_zero` proves this against the actual `QueryTree`, `RandomizedProgram`, and `RLe`. It first derives input-independence from the tree structure and then proves that the two output masses sum to one using the actual weight normalization. It does not assume these properties in a parallel model. Moving the algorithm existential inside the input quantifier changes the answer: on each input separately one can choose the correct constant leaf. `SemanticMutations.lean` states both sides of this distinction.
<!-- /passage:EVID-IDENTITY -->

<!-- passage:EVID-OR -->
### 3.2. Two-bit OR tests the inclusive threshold

Choose with probability $1/3$ each: output true, query the first bit and return it, or query the second bit and return it. All three trees have depth at most one. Their successes are:

| Input | Required output | Correct trees | Success |
|---|---|---|---|
| 00 | false | first-bit and second-bit trees | $2/3$ |
| 01 | true | constant-true and second-bit trees | $2/3$ |
| 10 | true | constant-true and first-bit trees | $2/3$ |
| 11 | true | all three | $1$ |

This proves the upper bound of one query at the inclusive threshold. Since OR has both output labels, the preceding zero-query argument also gives a lower bound of one. Hence $R(\mathrm{OR}_2)=1$. The proposed files state the success probabilities, the cap, and the exact complexity. A strict-$2/3$ mutation is detected by input 00, where the specified mixture attains equality. This shows that **this mixture** fails the strict threshold; it does not assert that every one-query algorithm fails every stricter threshold without a separate argument.
<!-- /passage:EVID-OR -->

<!-- passage:EVID-PROMISE -->
### 3.3. The true-only promise has zero-query complexity

Define $g(1)=1$, with $g(0)$ undefined. A constant-true leaf succeeds on every promised input and makes no queries. The same constant output is admitted by the actual `ConstantOnPromise` branch of `QLe`. Thus $R$g$=Q$g$=0$. The proofs provide witnesses; they do not obtain zero by exploiting the convention for an empty natural-number infimum.

Replacing the undefined value by false makes $g$ the total one-bit identity, for which the zero-query claim fails. This example tests the domain convention as well as zero-query behavior. It does not claim that arbitrary off-promise behavior is correct on an enlarged domain.
<!-- /passage:EVID-PROMISE -->

<!-- passage:EVID-FORRELATION -->
### 3.4. The negative Forrelation example tests the sign of the high branch

For $k=2,t=1,m=4$, take both sign vectors to be $z=(-1,1,1,1)^T$. With the unnormalized Walsh matrix in the supplied coordinate order,

\[
W=\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix},\qquad Wz=-2z.
\]

Consequently $z^TWz=-8$. The denominator $m(\sqrt m)^{k-1}$ is 8, so $\Phi=-1$. The preprint's high branch requires $\Phi\ge2^{-10}$, while its low branch requires $|\Phi|\le2^{-11}$. Neither holds, so this input is outside the promise. Replacing the high branch by $|\Phi|\ge2^{-10}$ would incorrectly admit it as a true input. These are the exact thresholds in [OAI26], §2.1, equations (3)–(4).

The proposed semantic test computes the actual integer numerator, denominator and promise definition, using kernel reduction rather than native evaluation. It does not import the existing `Forrelation.Sanity` witness theorem. That existing theorem is acknowledged; the finite example is not claimed as a new result. The proposed file still requires actual Lean elaboration before its behavior can be reported as checked.
<!-- /passage:EVID-FORRELATION -->

The complete source types and conventions are in `semantic/semantic-expectations.json`; the proofs are in `semantic/lean/QuarticCorpus/Independent/Semantics.lean`. All four cases currently have ordinary mathematical justifications and proposed actual-definition Lean tests, with native execution explicitly outstanding.

<!-- passage:EVID-CONTROLS -->
## 4. What the negative controls distinguish

The returned controls distinguish three different observations.

1. **A genuine comparison rejection.** In the threshold specimen only the solution changes a referenced predicate from $p\ge2/3$ to $p>2/3$; the displayed target theorem is unchanged. The predicted rejection is a mismatch in `Round3.ThresholdSpec.Eligible`. The case passes only when an actual Comparator run exits 1 with that diagnostic. An import failure or absent executable is not a successful rejection test.
2. **Agreement on an impossible shared premise.** Both sides of the other specimen use a comparison structure with an extra field `impossible : False`. Its conditional target is provable by false elimination. Matching this challenge is expected to succeed because the specification itself is vacuous. A separate proposed theorem exhibits the actual two-candidate comparison matrix: zero diagonal and off-diagonal entries $1/2$. It also proves that the shared bad structure has no inhabitant. Thus the semantic expectation exposes the defect that agreement alone cannot expose. This is a source-predicted blind-spot experiment, not an observed Comparator acceptance.
3. **Finite toy arithmetic.** The existing `semantic_controls.py` was executed successfully. All seven named mutations changed exactly their designated expected answer. This program explicitly neither reads nor executes Lean. Its truth tables are finite evidence for the examples only.

These controls require no custom axioms in proof-bearing candidates. Intentional `sorry` placeholders occur only in specification-only Challenge files; solutions must be checked with the standard permitted axioms. A source scan for holes is weaker evidence than a native transitive axiom audit, so the former is not reported as the latter.
<!-- /passage:EVID-CONTROLS -->

<!-- passage:EVID-EQ19 -->
## 5. Equation (19) requires both clauses

### 5.1. The complete statement and its premises

Fix \(\ell,r,S\in\mathbb N\), put $m=2^\ell$, and let \(\kappa\) be a finite set of address-string coordinates. There are \(r\) address strings per column, indexed by \(h\in[r]\); \(S\) is the number of transcript coordinates per address string in each cell. Let \(\mu:\{0,1\}^{\kappa}\to\mathbb R\) have nonnegative values summing to one. Independently sample every address string $A_{i,h}$ with law \(\mu\), every zero position $J_i$ uniformly in $[m]$, and a further uniform column $I$. The dummy input has a single zero at $X_i[J_i]$ in every column, the sampled address data, and fixed all-false cell bits. Let $T$ be a deterministic tree with depth at most $G$, counting every bit query, including repetitions. Let $Z$ count distinct columns whose designated zero is queried in the complete dummy run. Then

\[
\Pr\bigl[T(Y^{(0)})\text{ queries }X_I[J_I]\bigr]
=\frac{\mathbb E Z}{m},
\qquad
\Pr\bigl[T(Y^{(0)})\text{ queries }X_I[J_I]\bigr]
\le\frac{4G}{m^2}.
\]

The paper's powers of four are recovered by taking \(\ell=2t\); its address multiplicity is \(r=\lceil20\log_2 m\rceil=40t\), with the paper's cell-transcript size (see §2.2, equation (6)). The isolated bound holds for arbitrary \(r,S\). Normalization, nonnegativity and depth are ordinary premises of this statement. Hardness and support on the Forrelation promise are unnecessary for this isolated search statement; they enter later parts of the planted-input argument. This is the complete equation-(19) target in [OAI26], §4.2, pp. 12–13, rather than just its final inequality.

### 5.2. Proof of the equality

Fix the entire dummy run. It discovers exactly $Z$ designated zeros, one in each of $Z$ columns. The independently chosen $I$ hits one of those columns with probability $Z/m$. Averaging over the dummy experiment gives the equality. Equivalently, if $D_i(A,J)$ is the discovery indicator,

\[
\sum_{A,J}p_Ap_J\left(\frac1m\sum_iD_i(A,J)\right)
=\frac1m\sum_{A,J}p_Ap_JZ(A,J).
\]

This identity is algebraic in the address weights. Positivity and normalization justify reading the sums as probabilities and are used by the upper bound. Repeated queries do not increase $Z$, since each discovery is a membership event, not a query-occurrence count.

### 5.3. The preprint's bound and the supplied alternative route

Conditional on any positive-probability query-and-answer history up to the current time, provided the column's zero has not yet been discovered, its location is uniform among that column's unqueried positions. Fixing this history fixes the adaptive query schedule. By induction along the tree, the event of realizing it imposes exactly the recorded answer constraints and no additional constraint on an unqueried zero location. Data in other columns, independent address data and blank cells add no further information about that location. A repeated query to a known one cannot discover a new zero.

Call a discovery early when fewer than $m/2$ distinct positions in its column were queried before it. Its conditional probability at any query time is at most $2/m$. There are at most $G$ times, so early discoveries have expected count at most $2G/m$. Each remaining discovered column has received at least $m/2$ queries. On every run there are at most $2G/m$ such columns. Hence \(\mathbb E Z\le4G/m\), and the equality above gives the required probability bound.

The Lean development uses a different, stronger finite-tree induction. Fix one column, all outside data and a set $U$ of possible zero positions. Let $D_U$ be the number of worlds whose designated zero is found, and $Q_U$ the sum of queries to this column over those worlds. The invariant is \(|U|D_U\le2Q_U\). At a leaf both terms vanish. A query outside the column takes the same branch in every world. A column query at a position outside $U$ discovers nothing and adds \(|U|\) queries. For a position inside $U$, let $n=|U|-1$; write $d,q$ for the discovery count and query sum in the answer-one subtree on the remaining worlds. Induction gives $nd\le2q$, while $d\le n$. The queried-zero world contributes one discovery and at least one query, and every other world pays its root query. Thus

\[
(n+1)(1+d)=nd+n+d+1\le2q+2n+1\le2(q+n+1)\le2Q_U.
\]

Averaging over the uniform zero position gives at most $2/m$ times the expected queries to that column. Average the outside data and sum over columns; their query counts total at most $G$. This yields \(\mathbb E Z\le2G/m\), hence a probability bound $2G/m^2$, which implies the required coefficient-four bound. No step needs distinct queries or stopping at first discovery. This is an **alternative proof route**, not formal verification of the printed early/late intermediate estimates.

### 5.4. What the source currently proves

| Declaration | Conclusion | Supplied current build | Supplied direct comparison |
|---|---|---|---|
| `Paper.erasedZero_eq_expectedZeros_div` | Equality with $\mathbb E Z/m$ | Yes, exact declaration listed | None |
| `Paper.expectedZeros_le_four` | $\mathbb E Z\le4G/m$ | Yes | None |
| `Paper.eq_19` | Probability at most $4G/m^2$ | Yes | None |
| `avg_foundZero_I_le` | Coefficient-two bound with address data fixed | Yes | None |
| New `Paper.eq19_whole` | Equality **and** probability bound | Uncompiled proposal | Unrun proposal |

All names in the table have prefix `QuarticQuery.`. Source-current supplied build evidence means the recorded source hashes match this packet, not that the present session reran Lean. The exact existing types and proofs are in `Paper/ClassicalPlanted.lean`, lines 180–258, and `LowerBound/Planted/ZeroSearch.lean`, lines 226–245.

The new `QuarticQuery.Paper.eq19_whole` contains both conjuncts and joins the existing equality and inequality proofs. A second specification writes out the product law, dummy input, distinct-zero count and erased-zero event independently; bridge theorems identify those quantities with the implementation. A direct comparison targets `eq19_whole` itself, while another comparison targets the independently specified theorem. These are separate declarations and cannot inherit each other's comparison status.

An inequality-only negative candidate is supplied to test omission of the equality. A repetition witness also distinguishes a path `[q,q]` and depth two from a discovery count of one. An additional AI source review found no definite source-level defect in the new files, but they remain uncompiled. The specification shares `QueryTree`, `BitLoc`, `path` and `depth`; these shared interfaces remain a stated semantic boundary.

The maintained corpus already calls the original `eq-19` tie **partial**. The old baseline Appendix B calls its inequality-only declaration `stronger`; that evidence paragraph should be corrected. The wrapper does not upgrade the separate compound `claim-EZ` row, which includes the early/late explanation as well as an endpoint bound.
<!-- /passage:EVID-EQ19 -->

<!-- passage:EVID-INDEPENDENCE -->
### 5.5. A finite control for independence

Uniformity of $I$'s marginal distribution is insufficient for the equality. For a four-column dummy input, query the first row in every column (row zero in the implementation). Each independently uniform zero is found with probability $1/4$, so $\mathbb E Z=1$. An independent uniform $I$ gives hit probability $1/4$, as required.

Change the law: when any zero was discovered, choose $I$ uniformly from the discovered columns; if none was discovered, choose it uniformly from all columns. By symmetry each column still has marginal probability $1/4$, but

\[
\Pr(\text{hit the selected zero})=\Pr(Z>0)
=1-(3/4)^4=175/256\ne1/4.
\]

The returned exact-rational script enumerated all 256 zero-location vectors and verified these values and all four uniform marginals. This is a deliberately different sampling law, not a counterexample to the preprint. It explains why the independent product specification is a substantive test and why validating only the final inequality would miss a different clause.
<!-- /passage:EVID-INDEPENDENCE -->

<!-- passage:EVID-FRESHNESS -->
## 6. Enforcing review freshness

### 6.1. The reproduced failure

Suppose a reviewer marks a theorem an exact representation of a paper statement. Later, a referenced predicate changes while the theorem's displayed type name stays the same. The revised theorem and a regenerated Challenge may both compile and agree. The original producer then accepts the old `exact` judgment with new build and comparison receipts. There is no enforced check that the old judgment concerned the new predicate.

The acceptance test reproduces this behavior with explicit mocked operation receipts. It changes a definition body while leaving the complete theorem source unchanged and supplies fresh matching build/comparison records. The original builder returns current statement-level comparison credit; the patched builder preserves the operation facts but withholds the obsolete review.

### 6.2. The minimal patch

The patch adds an optional `review_binding` to the existing `corpus/ties.json` owner. Its fingerprints bind the statement ID and exact text, the complete corrected row, the declaration identity, the entire authored tie excluding its binding, and the existing whole-local-Lean/configuration snapshot. The authored fields include relation, route, ordinary premises, additional assumptions, reviewer and notes. Changing an implicit local definition is covered even when the theorem header is unchanged.

The builder never writes or refreshes the binding. It reports `current`, `stale`, `legacy_unbound` or `not_reviewed`; malformed bindings fail closed. Historical judgments remain available as `reviewed_relation` and `reviewed_route`. Effective relation and selected statement-level comparison credit require current review. For the demonstrated semantic edit followed by fresh mock runs, the result is:

| Field | Result |
|---|---|
| Declaration build evidence | current |
| Declaration comparison evidence | current |
| Review evidence | stale |
| Effective relation to the paper | unassessed |
| Statement-level comparison credit | not_run |

This is deliberately conservative. Any local Lean or bound configuration change invalidates the binding, including an unrelated module or proof-only edit. It binds dependency revisions, not actual dependency checkout or tool-executable bytes. It does not authenticate the reviewer. A future finer-grained implementation would need trustworthy elaborated-type and semantic-definition closure evidence; source-text heuristics would weaken the guarantee.

### 6.3. Validation and migration

The original supplied Python suite discovered 35 tests: 33 passed and two external integrations skipped. With the patch, 46 tests were discovered: 44 passed and the same two skipped. The 11 added cases cover semantic edits with fresh runs, source additions/removals and pins, statement/context and judgment changes, malformed bindings, the separation of reviews from operations, and helper provenance. `git apply --check --whitespace=error` passed against the frozen packet. These are actual Python results; the mocked transition tests are not native builds or comparisons.

The real corpus dry run contains 121 statements and 840 ties: 477 authored judgments and 363 doc-comment proposals. All 477 old judgments lack the new binding. The patch leaves them historically visible as `legacy_unbound`; it does not mass-attest them. It preserves current build evidence on all 840 ties and current comparison evidence on 19 ties; the 840 built ties refer to 816 distinct declarations. Statement-level compared rows fall from seven to zero until corresponding judgments are explicitly bound after review. That is the intended migration behavior, not a proof invalidation. The patch does not alter ties, Lean sources, receipts or generated corpus files in the original packet.

The patch changes only the corpus producer, its existing tests, one added regression file, and the two existing evidence guides. The eleven acceptance cases and exact output are under `backend/`.
<!-- /passage:EVID-FRESHNESS -->

<!-- passage:EVID-PROVENANCE -->
## 7. Derived statements retain their own provenance

The current graph has one source, the OpenAI preprint. Its producer assigns every input statement to that source. A demonstrated ingestion of a derived helper therefore silently misattributes it; a missing prerequisite is also silently omitted from its support edges. These are concrete producer behaviors, reproduced by the acceptance script, even though no `r2-live-*` helper is currently ingested.

Seven `r2-live-*` candidates are preserved in the round-two source owner, which already explicitly withholds them from this graph. None of those seven proposal records has an authored `depends_on` field. Guessing their dependencies from informal notes would create additional unsupported judgments.

This return therefore chooses **explicit withholding**. With the returned patch, the producer refuses `r2-live-*` rows even if they are labelled as preprint material, refuses explicitly nonpreprint `source_id` values, and refuses missing prerequisites instead of dropping edges. It does not discard the proposals from their source owner. A later mixed-source extension must retain their derived-source identity and reviewed dependency lists. No second statement registry is introduced.

The resulting informal graph still has 121 nodes and 225 support edges, with 120 unverified nodes and one external assumption. It has extraction status `not_run`. Build facts attached as metadata remain build facts; they are not converted into native formal-node verification.
<!-- /passage:EVID-PROVENANCE -->

<!-- passage:EVID-SNAPSHOT -->
## 8. What the supplied native records establish

The frozen packet identifies repository commit `1dd469dd0042b937b739da3bc211eeb60bdf7462`. Its current native build/comparison records identify `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`. The actual 124-file source inventories agree. A differing later repository commit therefore does not itself make these receipts stale; source bytes, rather than commit-name equality, decide currentness under the supplied contract.

The 12 current receipts consist of one root build, five positive bundle comparisons, an additional paranoid Unconditional comparison, and five expected negative comparisons. Eleven older successful records lack the source binding and remain `legacy_unbound`. The supplied comparisons explicitly describe unsandboxed local runs. They are retained at that trust level rather than promoted to an independent hostile-input validation.

The current dependency export declares 2,652 public project constants, reaches 1,354 from its two headline roots, and records traversal of 61,138 constants with no unresolved names. It has 7,655 projected public edges and 584 retained hidden-path witnesses across 145 parents. The local audit checks consistency of those reported structures and verifies that the supplied native regression has the actual exporter as its exact byte prefix. It does not rerun the traversal.

The existing equality and `Paper.eq_19` are declared by the root build but are outside the two headline roots' reached set. The coefficient-two `avg_foundZero_I_le` is reached. A statement row's aggregate reach field can arise from another partial tie; it does not imply that its selected exact declaration lies in the headline proof. In particular the root export does not provide a target-specific dependency graph for the equality.

The supplied type/axiom audit reports 258 declarations using only `propext`, `Quot.sound`, and `Classical.choice`. Its source snapshot, script hash and retained complete log hash match. This is a consistent supplied audit, not a fresh one. The original source header “UNELABORATED” in `ClassicalPlanted.lean` predates the later successful source-bound receipt and should be treated as historical commentary.

The supplied reader acceptance really records `validate`, `select` and `inspect` on its retained **informal** graph. That graph's hash matches its receipt. It differs from the final corpus graph by the subsequently added paranoid comparison record and the resulting evidence references. Both share the same Lean source inventory and ties. The old reader receipt covers its retained graph exactly; it does not become a native extraction receipt or an execution on the later graph.

The complete byte and receipt audit is `checks/snapshot_audit.json`. Complete original build/comparison output is not always supplied: several retained logs are only summaries. Hash consistency cannot recreate unavailable full logs, authenticate the original host, prove clean-clone reproducibility, or detect a transient change-and-revert between the original recorder's boundary observations.
<!-- /passage:EVID-SNAPSHOT -->

<!-- passage:EVID-EXTRACTION -->
## 9. Native extraction was attempted and remains incomplete

The selected existing target is module `QuarticQuery.Paper.ClassicalPlanted`, declaration `QuarticQuery.Paper.erasedZero_eq_expectedZeros_div`. Its module hash is `b86c310788efd04527ce9977e6f1cb660cd6b2b6825dcb151ab33f1b94497c2f`. The source-current root build names it explicitly; the module's separate acceptance record also matches all 16 recorded inputs. It is an accepted source-current target under the supplied receipt contract.

The actual command used the existing CLI's `extract` route, this module and goal, `--module-prefix QuarticQuery`, and `--build`. It exited 127 at process launch with `lean-exposition: not found`; no graph was produced. The exact command, working directory, stdout and stderr are preserved in `eq19/native-extraction-attempt.json`. This launch-attempt record is not the consumer's native extraction receipt.

This environment also lacks Lean, Lake and Elan. The packet omits pinned build/dependency artifacts. Its ten selected `lean-exposition` files provide readable contracts and implementation, but not an installable complete tool: the CLI imports missing `bundle.py`, `intake.py` and `prove2me.py`, and extraction needs the absent `resources/lean/Extract.lean`. Package metadata and an installed entry point are absent; the active Python environment lacks `jsonschema`. `BACKEND_INPUT_STATUS.json` reports selected source custody, not runtime availability. No exact `lean-exposition` Git revision is supplied; its source-file hashes identify the reviewed edition.

The existing consumer requires an actual native report with source identity and typed dependencies, a matching build record, and current source binding. It retains unavailable bodies and external expansion boundaries. A selected goal's prerequisites must come from that graph. Successful schema validation alone establishes neither statement fidelity nor a completed proof extraction. The returned commands use the actual `validate`, `select`, and `inspect` interface read from the supplied CLI; none was run on a nonexistent native graph.

To close this endpoint, obtain the complete matching tool distribution and pinned project environment, run extraction on the unmodified accepted target, retain the real native report and build/extraction receipts, validate the graph, select the equality, and inspect its prerequisites and provenance. `eq19/reentry-plan.json` supplies exact argument arrays. For new candidates, use a disposable copy with both returned Lean overlays and obtain fresh receipts for their enlarged source snapshot. The old receipts cannot certify newly added source files.
<!-- /passage:EVID-EXTRACTION -->

## 10. Integration order

1. Review and apply `backend/backend.patch` through the existing owner. Regenerate the corpus deliberately; expect unbound legacy semantic judgments to lose current alignment credit while operation facts remain.
2. Restore the precise native prerequisites and finish extraction of the accepted unchanged target. Retain actual outputs and the consumer's own checks.
3. Copy `semantic/lean/` and `eq19/overlay/lean/` into a disposable pinned project. They extend the existing `QuarticCorpus` and `QuarticQuery` libraries; no new library or registry is needed.
4. Build the semantic examples, mutations, full equation-(19) theorem, bridges and repetition controls. Inspect complete types and transitive axioms. Run the explicit comparison configurations; the existing one-level generated-bundle runner does not discover the nested independent configurations.
5. Record each successful operation against its exact declaration and frozen source. Review the complete statement and semantic dependencies, then record its review binding. Retain the independent-specification comparison and the direct whole-theorem comparison as separate facts.
6. Correct the baseline's historical evidence passages through its owner: §2.3 must identify its original evidence edition; Appendix B `eq-19` must not present the old stronger classification as current. Keep the ordinary mathematical proof and the alternative-route label intact.

The remaining native failures are missing-prerequisite boundaries. They are not mathematical counterexamples, and they are not expected negative-control successes. The return supplies the concrete files, tested backend repair, source correspondences and re-entry instructions needed for the next native pass.

## References and exact source locations

- **[OAI26]** OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, 5 October 2026. Supplied PDF SHA-256 `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`, public revision `4eaee875`. Mathematical authority for query conventions, signed promise, comparison predicate and equation (19). See `references.bib` for the pinned URL.
- **[QUARTIC]** Supplied quartic-query repository snapshot, commit `1dd469dd0042b937b739da3bc211eeb60bdf7462`; exact local-source hashes and receipt locators are in `checks/snapshot_audit.json` and `source_read_receipt.json`. Source implementation and recorded evidence, not independent scholarly authority.
- **[LAKE436]** Lean/Lake `v4.36.0-rc2`, supplied `Lake/Check/Compare.lean`, `Axioms.lean`, and `CLI/Check.lean`/`Help.lean`. The manifest's source paths identify this toolchain edition; individual content hashes are retained. Implementation authority for the proposed Comparator controls.
- **[LEX]** Supplied `lean-exposition` contracts, verification implementation, extraction implementation, CLI and schemas. File hashes identify the edition; no repository revision was supplied. Integration authority, not proof of a native extraction.
- **[LEAN-VALIDATION]** Lean Language Reference, [“Validating a Lean Proof”](https://lean-lang.org/doc/reference/latest/ValidatingProofs/), especially “Remaining Issues”; and [Lake, “Challenges and External Checkers”](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/). Accessed 2 November 2026. Background corroboration of the difference between a checked formal proposition and intended meaning; the packet's pinned implementation governs exact commands.

Reading coverage is focused rather than whole-manuscript: baseline §1.1, §2.3, §6.4 and the named Appendix B entries were assessed; §§2.1–2.2 were sampled, with targeted adjoining definitions and source owners read as needed. The QAOA examples and writing guides were used only as structural exemplars. They are not mathematical authority for the quartic result. The complete assessed/sampled/unavailable/unassessed scope is recorded separately.
