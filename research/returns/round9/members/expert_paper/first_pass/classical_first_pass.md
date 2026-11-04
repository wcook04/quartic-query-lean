# Frozen first encounter: randomized lower-bound perspective

Status: frozen before opening the reasoning record, previous-round feedback,
writing-method material, or any supplied/online research paper. This is a
model's simulated chronological audit, not an observed human reading and not
an independent blind reader experiment. The shared task context disclosed the
paper's purpose, review protocol, and that previous revisions existed.

Source: `repository/docs/expert_companion.md`, SHA-256
`7fddfa0c37f7d038ba58adde4e7685263f3ba7733d0fd87a8a3eea4ce653f8ab`.
All source prose through line 399 and the link definitions through line 415
were read. The bibliography database was read after the appendix, because the
Markdown has an empty generated reference container at lines 345–348. This
does not count as an in-order inspection of the printed reference pages.

Retrieval limitation: an initial combined tool response containing instructions
and lines 1–145 was truncated and exposed later source lines before the opening
was re-requested. Lines 1–74 were then explicitly read, followed by 75–171,
172–291, and 292–415. Accordingly the early section read is a simulation with
partial prior exposure, not a pristine cold read. No other account or source
paper had been opened before this freeze. There were no off-document detours.

## Title, abstract, introduction (1–35)

- The title promises the optimal exponent, whereas the subtitle signals a
  companion. The abstract makes the original result's attribution available
  immediately. I still need the manuscript's own mathematical contribution
  distinguished from reconstruction: the sampler and predictor are described
  as reconstructed, but their relationship to the source's statements is not
  yet a precise two-item map.
- In the abstract, the hard-input distribution and “number of columns times
  the address-hardness scale” arrive before an address query has been
  distinguished from a certificate query. I predict an explicit accounting
  explanation rather than an assumption that address secrecy alone multiplies
  hardness by the number of columns.
- Line 14 calls a certificate the object that defeats rivals. I do not yet
  know whether the comparison checks certificate validity or merely follows a
  suggested pointer. This is an important possible confusion because direct
  certificate verification is typically the costly operation.
- Lines 16–22 explicitly place the result in a bit-query model, with free
  computation and a uniform exponent constant. The all-input cap for partial
  functions is a nonstandard-looking convention that deserves a short
  explanation of why it agrees with usual bounded-query hardness citations.
- The theorem provides separate inequalities in m. I can divide exponents,
  but the displayed bounds do not yet explicitly assert a uniform-in-k family.
  The abstract's single-family 4-o(1) wording therefore creates a pending
  quantifier question rather than an immediate contradiction.
- The exact coefficient 1/400 and logarithmic exponent six are visible; I now
  expect the proof to make their provenance recoverable without following
  numerous pinned external links.
- Line 34 announces that the unconditioned event is central. Its wording is
  technical before I have seen the light-column event; I predict that this
  warning will be explained at the simulator, not used as a substitute for it.

## Overview and literature (36–71)

- The selected cell is addressed by r independent partial-function values,
  but the overview has not yet said that r is an exact multiple of log m.
  This is acceptable staging; the precise multiplier is expected at the
  construction and union bound.
- The formal meaning of a gate-value transcript is deferred. I need both the
  domain output and value output to be checked: evaluating a partial function
  cheaply does not establish that an input is promised.
- The comparison overview distinguishes the expensive local-test search from
  following pointers. The reader must still infer that a losing column's
  decoded label can be arbitrary without creating a zero in an all-one winner.
- Line 44 introduces a dummy run before a tree has been named. Its selected-
  zero argument is convincing only if I is independent of the complete dummy
  transcript, not merely uniform. The sentence says independently, so I expect
  the later proof to preserve exactly that coupling.
- The address-budget L in line 46 could be read as a per-instance allowance or
  the sum over all r instances. I need the latter for the light-column count,
  followed by an explicit implication to the separate-cap direct product.
- “Thus” in the overview jumps over combining the two discovery events and
  turning distinguishability into query complexity. I predict a single
  discrepancy inequality later to close this chain.
- The historical cheat-sheet formula introduces a second dimension m'. The
  R(g)m'^2 composition assertion is mathematically substantive; its cited
  location should isolate the composition fact as well as the cheat-sheet
  transformation. I expect logs/parameter dependence to remain explicit.
- The pointer comparison is an alphabet/accounting issue, not just a different
  drawing: storing m pointers separately and charging log m for one lookup is
  the decisive step. This deserves a precise comparison with the predecessor's
  query model, particularly since its reason for rejecting direct pointers is
  quoted only by a section locator.
- The Forrelation/Rorrelation distinction is now explicit. The exact circuit
  requirement, not only partial-function hardness, determines which source can
  be transplanted. I predict an exact promise convention next.

## Function and local tests (73–116)

- The parameter order k,t,m,ell,r is clear, but k's integrality is implicit in
  this section; it was explicit in the theorem. The sign convention is fixed.
- The one-sided promise leaves large negative Phi unpromised. The sentence
  saying the exact circuit “certifies it even on unpromised inputs” could be
  misconstrued as certifying a P-value there; the circuit should instead certify
  domain failure and reject the purported address certificate.
- Property (i) requires a large-m threshold and does not promise L>=1 for every
  m. The later reduction needs 1<=L<=m, so I expect that rounding/threshold check
  to be done at substitution rather than silently assumed here.
- Property (iii)'s precise constant 200 is not derived locally. The same
  construction is required in both bounds, so the external circuit proof is a
  mandatory source dependency despite the paper's “check locally” aspiration.
- At line 101, the distinction between input coordinates and certified values
  matters. The cell is a free input string; only a selected cell's consistency
  is a condition for winning. The long sentence carries layout, alphabet,
  transcript semantics and acceptance at once; it will be hard to reuse as a
  definition when reading the simulator.
- At line 108 I can calculate the input length, but S is only upper-bounded and
  the formula is an encoding length rather than a claim all bits influence F.
  The circuit's fixed choice is explicit, so there is no present two-function
  ambiguity. I expect a matching concrete circuit theorem in the formal part.
- At lines 110–114, s_i is defined only on promised address tuples. The first
  description of the conjunction should be interpreted with that guard; the
  subsequent gate induction makes the intended all-input semantics available.
- The exact K count includes gate consistency at output gates and two further
  requirements; that double appearance is explained. One remaining issue is
  whether query costs count repeated wire locations or distinct coordinates;
  upper bounds are safe either way, but the later classical counts explicitly
  count repetitions.

## Quantum argument (118–177)

- This perspective reads the quantum proof to check that it is for the same
  total function, not to claim an independent quantum implementation audit.
- The distinction between exact conditional law and high-probability success
  is necessary. Lemma 2's positive success threshold and all-branch cap prevent
  an expected-time query bound from entering the headline theorem.
- At line 132, the sorted pair and common circuit ensure complementary
  probabilities. At line 137, loser promises are irrelevant because the
  winner is all ones. The earlier “certificate defeats” wording resolves here:
  the comparator does not read transcripts at all.
- The weight product is conditional on fixed input and history, with fresh
  comparison workspaces. Its independence is algorithmic, unlike the hard
  distribution's independent input blocks; the two uses should not share an
  unexplained generic “independence” label.
- The half-drift equation is an exact identity with a subtracted diagonal term.
  Markov is applied to weight, not to a random number of surviving candidates.
  I can follow the abstract four-candidate example without needing it to be an
  instance of the Boolean construction.
- Candidate verification is unconditional on promise satisfaction. Any false
  candidate fails a local test at every proposed address. This resolves the
  totality issue raised earlier. The error accounting is one-sided in the
  defect search but not in the address decoder; that distinction could be
  made easier to scan.
- The loose ell^6 estimate is safe in form. The explicit exponential C_k is
  optional for fixed k but becomes essential if §6 lets k grow.

## Classical reduction (179–282)

- Proposition 4 detaches the lower bound from Forrelation. The exact circuit
  has arbitrary size for this result; only the upper bound needed small S.
  The proposition should identify L as an integer so “depth L” and the capped
  simulator have their literal meanings. The statement currently gives only
  inequalities for L.
- Minimax at line 188 uses attained optimal success below 2/3; the choice of a
  non-strict beta=2/3 is safe. The law need not balance answer bits. This is not
  an information-theoretic argument from uniform answers.
- Lemma 5 has separate caps L on each input; the later predictor has total cap
  L. The preview says this is a deliberately stronger hypothesis, but I still
  expect the implication to be written at application.
- The unnormalised Bellman recurrence controls all-correct success on product
  restrictions. The reader has to supply that a deterministic transcript
  retains product form under adaptively chosen coordinate queries; an explicit
  sentence would make the proof's main invariant much easier to check.
- The second direct-product route substitutes Drucker's parameters in one
  sentence. I cannot validate 2 beta^r without the exact theorem inequality.
  This is a verification detour to make after freezing.
- Dummy inputs contain no answer-dependent cell contents, so supplying their
  outside coordinates as free data cannot leak the target address. The planted
  cell has true transcripts and pointers to the J_j; its input coordinates
  need not all change from zero. Line 226 correctly counts the larger hit event.
- The deterministic tree is fixed before sampling. In Eq. (10), both right-
  hand events are on the dummy run. This matters: a planted run's later
  behaviour could depend on I after a hit.
- Erased-zero discovery: before a zero is found, the next unqueried row has
  conditional hazard at most 2/m until half the rows have been read. Late
  discoveries charge at least m/2 queries each. Address and cell queries spend
  G but do not give zero information because dummy cells are blank. The proof
  is sound in structure; the switch from distinct rows to all queries deserves
  one explicit inequality to forestall a repeated-query objection.
- Heavy means terminal target-address query count exceeds L, including repeats.
  Thus heaviness can depend on future replies. It cannot be conditioned on when
  invoking product hardness; the paper flags exactly this danger at Eq. (12).
- At line 245, “at most G/L” is loose but correct with strict >L. The natural
  sharper integer bound is unnecessary; do not turn this into a false error.
- The original clock tau counts every tree query, while the simulator's budget
  only counts target-address queries. This resolves a potential coupling
  ambiguity; outputting the proposed cell's address costs no target query.
- The simulator's fallback cases do not explicitly include a tree that halts
  before tau. A depth-at-most-G tree can do so. The fixed-vector fallback needs
  to cover this case for the predictor to be total on every input.
- The simulator aborts before query L+1 and gets all free data jointly
  independently. It therefore meets Lemma 5 on every branch; Eq. (12) is event
  inclusion under the original product law, not conditional success on light
  columns. The sentence at 251 supplies the total-to-separate-cap implication.
- The union over tau followed by averaging over I cancels m, as displayed.
  There is no missing m factor. The G beta^r bound can count many hits; a union
  bound is enough because only an upper bound is needed.
- Eq. (14)'s three costs have different denominators; the following sentence
  attributes them but the third <=1/100 step is not shown. I can derive it from
  G<=m^2/100 and beta^r<=m^-10. A short arithmetic annotation would make the
  conspicuous numerical constant easier to audit.
- The final contradiction uses output acceptance gap >=1/3 after averaging
  correctness over each support; it does not need a second minimax theorem.
- The floor conversion t>=8 is not checked locally. My next verification task
  is to test L>=1, L<=m, floor loss, and the coefficient 1/400. The optional
  tighter zero-search constant interrupts the end of the core lower-bound
  proof and may be better placed at the zero-search discussion or in a note.

## Exponent and uniform refinement (284–329)

- The fixed-k conclusion follows from a power beating a logarithm; the order
  alpha -> k -> constants/threshold -> m is spelled out. No uniform-in-k
  conclusion should be inferred from this argument alone.
- Eq. (16) introduces a nontrivial new-looking quantitative hardness estimate
  while declining a priority claim. A reader needs to know exactly which
  hypotheses and derivations are reconstructed, rather than being left to
  judge it by the difference k^-2 versus the cited k^-29 dependence.
- The interpolation sketch imports a law nu_1 with possible off-promise mass,
  distinct from minimax mu. The pointwise bridge at lines 312–320 is essential;
  it is not permissible simply to apply promise correctness under nu_1.
- The pointwise upper and lower inequalities are plausible: use 0<=A<=1,
  Phi<=1 and the promised thresholds. The explanation omits these elementary
  inequalities, making the line “follows from correctness” do more work than
  correctness alone.
- The “constant error would swamp” conclusion is signal-dependent, not a
  general obstruction to distinguishing. The quantitative O(k)-repetition
  calculation requires ln(1/a_k)=Theta(k), and a statement of which error and
  query conventions are preserved.
- Serious first-encounter gap: §6 first says t>=13669 k^2 suffices for the
  earlier L=m^(1-1/k)/ell^2, then chooses k=floor(sqrt(t/20)). The latter has
  t/k^2 near 20 and cannot use that sufficient threshold. Presumably the
  growing-family calculation chooses a different smaller L directly from
  Eq. (16), but that choice is not shown. This is a missing bridge to verify,
  not yet a demonstrated false result.
- The growing-family statement R>=Q^(4-o(1)) also needs Q to tend to infinity
  to communicate a meaningful asymptotic ratio; the universal bound plus
  diverging R can establish that without a new theorem.

## Formal section and appendix (331–415)

- Section 7 distinguishes the existential log exponent of the compared family
  from explicit circuit constants. The statement links are pinned to a
  different commit than this supplied edition; link/source alignment must be
  checked in a second pass rather than inferred from their existence.
- The formal cap result is a joint success-and-compliance assertion. The main
  text's stronger always-capped algorithm is a special case; its applicability
  depends on the independent-randomness and finite-seed bridge in the record.
  The statement file alone cannot certify that informal identification.
- References are generated in the Markdown; their actual printed order and
  page break were not inspected here. Bib metadata was read after Appendix A.
- A.1 has a concrete sign vector; its Walsh-order convention is needed to
  recompute the advertised value. A.2 is an abstract probability example,
  distinct from the Boolean construction. A.3's false pointer makes candidate
  1 dominate because every comparison into X_1 sees a one and index 1 wins
  ties, even if address decoding is inaccurate.
- A.4 needs the dummy experiment's independently uniform zero rows. Its
  marginal-uniform I claim follows by exchangeability, not by independence.
  The arithmetic 175/256 is checkable without a source detour.
- A.5 omits the uniform law on each two-bit parity input when asserting
  beta=1/2. “Independent instances” alone does not imply that value. Add the
  input law; this is a premise omission in a finite example, not a failure of
  the intended counterexample.
- A.6 uses joint versus coordinatewise independence correctly in form. A.7
  uses redundant queries to make cap compliance informative; the repeat query
  is therefore essential to the example, not wasted exposition. I will
  enumerate its sixteen inputs after the freeze to verify the two fractions.
- A.8's eventual fixed-k threshold example is elementary; it should point back
  to the actual threshold mismatch that makes the growing choice nontrivial.

## Freeze boundary

The preceding observations are preserved even if later sources settle them.
No mathematical error is declared solely from this pass. Later source checks,
calculation results, prior-finding dispositions and final severity judgments
belong in separate analysis/feedback files.
