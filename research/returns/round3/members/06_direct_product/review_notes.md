# Review notes and authoring receipt

## Mathematical disposition

The assigned capped direct-product theorem and OpenAI's proof are sound.
The baseline §6.1 already explains the core product mechanism accurately.
This return develops its interface with the requested joint event and
updates the stale formal-evidence description. It does not assert that
OpenAI's theorem was repaired, refuted, or newly discovered.

The finished section gives an ordinary complete proof. An independent AI
mathematical reader checked every display and its supporting argument,
including the event extension, exact examples, and normalized/weighted
identity, and found no mathematical must-fix. Four clarity suggestions
were incorporated: naming the one-input continuation factors accurately,
introducing the input tuple before abbreviating it, restating nonnegativity
for the weighted product, and specifying the default output in the example's
truncation. This is an additional AI check, not human review.

## Ranked and located corrections

### 1. State the event extension without changing Lemma 4.1

**Location:** baseline `CL-direct-product-statement` and its use in §6.5;
replacement `CL-joint-cap`, equation (6.7).

The canonical theorem quantifies algorithms respecting the separate caps on
every run. The requested event statement quantifies a possibly-uncapped
algorithm and bounds correctness together with realized cap compliance.
Keep the canonical theorem unchanged and register the latter as
`NCL-joint-cap`. Stop before the first attempted excess query and preserve
the original outputs on all untruncated runs. Original success with all
caps respected is contained in truncated-algorithm success. This proves the
event statement under the original input law, without a conditioning premise.

**Formal evidence:** existing endpoints contain the binder `T.capped`.
No generic event-and-truncation theorem was supplied. The new corollary is
proved in ordinary mathematics here and is not labelled Lean-checked.

### 2. Replace historical “uncompiled” claims with exact current evidence

**Location:** baseline `CL-product-law`, `CL-conditional-values`, and
`CL-supermartingale` evidence remarks; original return-4 blueprint and gap
record; live `Paper/ClassicalDirectProduct.lean` header.

The current Paper source includes the transcript law, positive local masses,
attained maxima, actual conditional product expectation, finite iteration,
and actual-success bridge. Its later native target passed. We recomputed
all six recorded local target inputs and all 124 local inputs in each of
the root build, final audit, and dependency export; they match. The audit
log and generated audit-source hashes also match.

Use the source-bound receipt state, while preserving original returns as
historical records. Do not replace “uncompiled” with “independently rebuilt”:
this review ran no Lean compiler. The `.olean` root bytes are absent.
The differing packet and receipt commit labels are reported in
`LEAN_GAPS.md`; equality of their recorded local source bytes is the actual
currency check. None of these observations is an exact-helper Comparator
pass or human review.

### 3. Distinguish probability after a fixed history from probability after selection

**Location:** `CL-product-law`, `CL-joint-cap`, and `CL-adaptive-example`.

The input law factors after conditioning on one actual positive-mass
transcript, because that transcript is a rectangle. The event of satisfying
the caps, or being nonheavy, can select a union of rectangles and destroy
that factorization. The worked example has joint success $5/16$ but
conditional success $5/8$, larger than $(3/4)^2$.

The assignment's loose phrase about a conditional bound not bounding a joint
event needs a logical qualification. If the conditional estimate were
actually proved, multiplying by the conditioning probability would give the
joint estimate. What fails is an application of the original hardness and
independence assumptions to the selected conditional law. The replacement
says this explicitly and keeps the cap event inside the probability.

### 4. Match a compound statement with every required formal component

**Location:** equations (6.2)–(6.6) and `correspondence.json`.

The continuation-value definition requires attainment and an upper bound
for every permitted tree. Equation (16) also says that unqueried inputs do
not change. The product step requires the fact that only one factor changes;
a general product of supermartingales need not be a supermartingale. Finite
iteration needs a terminating horizon, and terminal success needs the
separate semantic bridge. The source has these components, but a convenient
primary theorem name does not by itself cover the entire compound row.

At termination the potential bounds conditional success probability. It
does not bound the success indicator pointwise. The exact example makes
that distinction visible on a successful input in a history whose potential
is $1/4$.

### 5. Be explicit about schedule legality, zero mass, and repeated calls

**Location:** `CL-product-law` and `CL-conditional-values`.

An arbitrary syntactic transcript can impose consistent bit constraints
while naming an impossible query schedule. Positive actual transcript mass
implies schedule legality; the source proves this rather than assuming it.
Contradictory repeats yield zero mass. We assign no conditional probability
law there. Repeated calls count against the remaining budget, even though
they add no information.

Drucker's partial-assignment notation counts revealed coordinates and can
leave its potential unchanged on a repeated query. Here the explicit call
counter decreases the remaining allowance and therefore cannot improve the
optimum. Both conventions support the argument; their definitions should
not be identified literally.

### 6. Keep all-paths fairness and total-budget statements separate

**Location:** `CL-adaptive-example` and `CL-literature-and-verification`.

A total budget $rL$ permits concentrating the budget on a few inputs; it
does not imply a separate cap $L$ for every input. The example computes one
AND exactly and guesses zero on the other, obtaining $3/4>9/16$ with total
budget two. A total budget $L$ does imply every separate cap. The planted
simulator has this stronger total target-query cap, so its use of Lemma 4.1
is valid.

### 7. Attribute the precise result and edition

**Location:** final sources paragraph and `references.bib`.

| Source | Exact assessed statement | Role here |
|---|---|---|
| OpenAI, 5 October 2026, §4.1 Lemma 4.1, pp. 11–12 | Arbitrary hard input law, separate caps, vector output, independent information | Target theorem and conditional-value proof |
| Drucker, arXiv:1005.0644v2, §1.3; Lemmas 3.1–3.2, pp. 11–12; last paragraph of §3, p. 13 | Conditional continuation values, adaptive-history product law, and fair specialization | Closest proof source |
| Drucker, Theorem 1.1 | Global budget $\alpha\varepsilon Tk$ and success bound $(2^{\alpha\varepsilon}(1-\varepsilon))^k$ | Comparison only |
| Shaltiel, ECCC TR01-009, §5 Definition 4, Theorem 5, Lemma 7, printed pp. 11–12 | All-paths separate caps and XOR advantage under the report's uniform input law | Earlier fairness/proof antecedent |

Shaltiel's definition uses **at most** each allowance on every root-to-leaf
path. Its advantage convention is twice success minus one. The report's
§1.1 footnote 1 specifies uniform inputs; footnote 2 discusses the
concatenation/vector variant. Drucker's introductory footnote records the
fair-XOR antecedent and its vector consequence. A vector consequence can
be obtained using parity estimates for all subsets of coordinates, but a
single full-parity estimate does not by itself give the required product
bound. The replacement uses the direct conditional-value proof, which
avoids adding that separate transfer argument.

The supplied Drucker TeX is pinned to arXiv v2. Its retained local PDF is an
earlier, byte-distinct acquisition; relevant passages agree with the pinned
TeX and public v2, but full edition/byte equality was not established.
Shaltiel's report has a cover counted as PDF page 1, so printed pp. 11–12
are PDF pages 12–13. The original displays were visually checked. The
public OpenAI landing page was available; the public raw-PDF route failed
with an unsupported-content-type error. OpenAI's mathematics was assessed
in the supplied PDF bytes, not in an invented fresh download.

## Concrete simplification and its outcome

The baseline presented two complete proofs consecutively. We retained the
ordinary conditional proof because the assignment asks where adaptive
independence and terminal success enter, and retained the weighted induction
because it is the current headline route. Equation (6.11) now connects them:
history mass times the normalized product equals the unnormalized product
of weighted values. This removes any suggestion that the two arguments
establish unrelated invariants. The additional generic joint-event theorem
uses a short truncation construction, rather than introducing a second
stopping-time formalism. Its exact default output is irrelevant to the
upper bound and is fixed only when computing the example's exact success.

The conditional proof's remaining technical work is necessary: deleting
the schedule condition, zero-mass case, remaining allowance, or terminal
conditional comparison makes the reasoning invalid or incomplete. No
unbounded optional-stopping machinery or full-support approximation is
needed for this finite promised-domain argument.

## Paper-authoring receipt

- **Object and genre:** replacement §6.1 of the supplied long reasoning
  record; a focused expository proof contribution, not an integrated paper.
- **Target reader:** a mathematically mature researcher familiar with basic
  classical query complexity, but not the local Lean naming conventions.
- **Contribution:** complete event-level interface, an exact discriminating
  example, explanation of the relationship between proof routes, and updated
  evidence alignment. No novelty or new quartic-separation claim.
- **Proof spine:** independent prior; legal transcript rectangle; conditional
  product law; attained one-input continuation values; one-factor conditional
  inequality; product iteration; conditional terminal success; finite seed
  averaging; truncation for the joint event.
- **Hard step:** adaptive scheduling is reconciled with independence by
  proving the actual execution event is the rectangle, then proving that
  only the queried factor changes. The terminal comparison connects that
  potential to the algorithm's real objective.
- **Concrete example:** two independent two-bit AND inputs, cap one;
  the adaptive second query and deliberately repeated call separate fixed
  histories from postselection on the cap event. Its fractions are exact.
  It illustrates the general theorem, rather than proving it by enumeration.
- **Mathematical taste dispositions:** mechanism demonstrated by the full
  invariant proof; economy demonstrated by truncation and normalization;
  structural yield demonstrated by the explicit failure of postselection;
  transfer demonstrated by the fixed-time planted simulator; reusable
  explanation supplied by the code and self-contained example. No additional
  research programme is needed for this editorial assignment.
- **Claim/Lean alignment:** canonical theorem unchanged; new corollary and
  normalization/explanatory examples separately registered. Compound claims
  retain all component declarations. Finite seed theorems are not silently
  promoted to arbitrary-space formal statements.
- **Citation roles:** OpenAI target/application; Drucker proof antecedent and
  separate global-budget comparison; Shaltiel earlier fair-XOR antecedent.
  QAOA and writing guides provide structure only, never mathematical authority.
- **Notation and equations:** repeated queries use explicit counters;
  $V_h$ is normalized, $W_c$ is unnormalized; every conditional law has positive
  mass. Local equation tags and stable passage/claim markers are retained.
- **Cold-reader disposition:** the second reader found no mathematical
  must-fix and identified four wording ambiguities, all corrected. Scope of
  that pass is this replacement, not the entire long record.
- **Exact open boundary:** no unresolved mathematical implication in the
  assigned lemma; generic truncation and arbitrary-information pushforward
  remain outside the literal supplied Lean types. No new formal proof is
  proposed or labelled compiled. Broader quartic mechanisms are unassessed.
- **Rendering:** Markdown source and equations were checked; no integrated
  PDF or HTML edition was compiled or visually inspected. Original Shaltiel
  source pages were rendered and inspected for the citation audit. The return
  does not claim final pagination or bibliography-render validation for the
  eventual integrated paper.
- **Reproducibility:** the exact example and source-byte audit both ran
  successfully. JSON parsing, passage boundaries, claim coverage, copied
  type provenance, and final file manifest are checked separately.
- **Missing source:** `Pasted text(20261102-190836).txt` was unavailable and
  was not read. The supplied ZIP's assignment was used. No conclusion about
  that text's contents or additional instructions is made.
- **Deliberate boundaries:** original repository sources, returns,
  adjudications, canonical statements, and baseline were preserved; no
  publication, merge, private-source access, or external communication occurred.

## Integration decisions

Use the replacement after checking its ordinary mathematics and correspondence
against the live integration source. Keep the baseline `NCL-weighted-value`,
`NCL-weighted-product`, and `NCL-finite-capped` identities. Add the four IDs
in `NEW_STATEMENTS.json` as advisory entries, with their stated evidence
classes. `STATEMENT_CHANGES.json` is empty because no canonical theorem
has been altered. Update stale evidence descriptions through the owning
corpus/adjudication surfaces, rather than editing preserved historical
returns or inferring comparison passes from compilation.
