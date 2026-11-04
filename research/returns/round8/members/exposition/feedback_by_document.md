# Feedback by document

## Scope and overall verdict

This critique combines four **simulated** perspectives: an outsider research mathematician (MATH), a strong final-year undergraduate (UG), a circuit-trained physicist or engineer (PHYS), and a lecturer (TEACH). These are reasoned audience models, not observations of human participants. The current exposition was read throughout; the PDF comments draw on inspection of all twenty pages by the coordinating reviewer. The lecturer's exercise analysis was answer-exposed and is not an independent blind attempt. Observations on the companion concern its introduction; observations on the record concern selected linked passages. EX identifiers below point to the detailed current-text findings in feedback.json.

The exposition now has a coherent mathematical spine and several unusually effective teaching examples. A reader can trace why a negative Forrelation amplitude necessitates a domain check, why defeating every rival does not certify a winner, why the sampler must preserve unequal weights, and why a capped predictor may succeed more often than the event it bounds. These examples explain necessary conditions rather than merely decorate definitions. None of these workstreams established an error affecting the separation theorem. The strongest verdict is nevertheless **a substantial guided study text, with remaining obstacles to independent use across its full advertised audience**. The gap is between recognizing the right sentences and reconstructing the operations they describe.

Several earlier deficiencies are now absent. There is a concrete query model, a high-level tournament loop, a fractional-weight example, an explicit full-workspace amplification invariant, a worked capped simulator, a three-budget explanation, and a corrected endpoint exercise. The general column inventory and full-width prose were deliberate prior-round choices. The next revision should improve their local connections rather than restore rejected prose tables, add a formal-receipt inventory, or repeat complaints about missing material that is present.

## The priorities, in order

**First, resolve the small number of genuine task and reference ambiguities.** The promised unique-search example changes the output task without saying so; Figure 4's relation to the old board needs a realization-specific description; Question 4 admits a branch-contribution and a whole-event reading; and the amplification link lands after its promised trial-count definitions. These are concrete repairs with identifiable success conditions, distinct from preferences about exposition length (EX066; EX048, EX057, EX042; EX182, EX216).

**Second, make the two central transfers independently reconstructible.** On the quantum side, show one compact register transformation connecting coherent comparison, retained workspace, conditional product probabilities, measurement, and inversion. On the classical side, separate conditioning on a fixed transcript from conditioning on a cheap execution, then show where the enforced cap permits the direct-product theorem. The statements are substantially correct already; their presentation still asks beginners to supply the hardest intermediate representation themselves (EX034, EX039, EX054; EX101, EX111; EX160, EX161, EX162, EX163, EX164, EX175; EX208, EX228).

**Third, align prerequisites, optional routes, and assessment.** State which concentration and amplification facts are accepted tools. Distinguish the final questions for a reader taking one proof route from the combined teach-back for someone reading both. Success on the five numerical questions should not be treated as evidence that the reader can explain both reductions unaided (EX007; EX089; EX187, EX204, EX237).

**Fourth, reduce simultaneous context and repair page flow.** The long historical paragraph in Section 2 and the optional proof in Section 5 combine too many different jobs. Stable names would help distinguish the board mutations and separate simulator toy. In the PDF, prioritize Figure 1's small labels, Figure 3's isolated page, and Figure 4's interruption of a proof sentence. The nearly empty final bibliography page is lower-priority finishing work (EX019, EX025; EX120, EX121, EX122, EX123, EX124; EX192, EX209, EX222).

## What each reader can explain now, and what a successful teach-back requires

The common target is a query-model claim about total Boolean functions: every total function obeys a universal quartic upper bound, while for every exponent below four the construction supplies counterexamples to a uniform bound. A satisfactory explanation must keep the one-sided estimates, distinguish $m$ from total input length, and avoid translating the statement into a hardware runtime guarantee (EX065, EX068, EX069; EX125, EX178, EX179).

### MATH: the mechanism is largely recoverable, with a quantum-operation gap

The simulated MATH reading reaches a close-to-complete account: addressed exact certificates make a total task; a weight process shrinks on average while an unlisted winner retains substantial weight; quantum sampling finds a short list; a planted pair turns classical detection into zero-finding or simultaneous address prediction. The first page requires retrospective decoding, but the first substantial reconstruction burden is coherent reversible comparison, not the elementary inner products (EX001, EX012, EX013, EX014, EX034).

The expected account should additionally identify what is imported, explain why the algorithm never estimates its weights, and distinguish the successful component of the full quantum state from the label register alone. It should retain the fixed-input error convention and choose the target exponent, then a fixed $k$, then growing $m$. The MATH reader would finish, but cannot infer an implementation merely from recognizing a valid probability identity.

### UG: correct computations do not yet guarantee transfer

The UG attempts recover all five supplied numerical answers, including the $1/8$ branch contribution versus $1/4$ total in Question 4 and the strict endpoint distinction in Question 5. The findings nevertheless locate the first mathematical uncertainty at the unmotivated arrival of $W$: the reader can multiply it before understanding why this transform is useful (EX071). By the end, this reader can describe columns, certificates, a short quantum candidate list, and a classically hidden plant.

A satisfactory independent explanation must go further: weights are probabilities, not amplitudes or uniform survival indicators; amplification preserves their conditional proportions; a query address already guesses every required answer; and product conditioning needs the fixed-transcript justification. Those are transfer tasks beyond the arithmetic exercises. The needed improvement is a small number of targeted bridges, not more examples of routine multiplication (EX099, EX100, EX101, EX102, EX109, EX111, EX112).

### PHYS: quantum familiarity does not supply the classical model

The PHYS reading reconstructs the quantum architecture relatively well. Its first substantial stall instead occurs when cells contain transcripts of a classical circuit whose domain/value purpose has not yet been explained (EX135). The likely first-pass summary correctly connects cheap address decoding, a candidate list, and a hidden classical certificate; it is less likely to articulate the distributional reduction precisely.

The expected account must distinguish a coherent stage from the measured classical pivot list, the $T$ factors in winner survival from many physical comparison calls, and full-workspace amplification from a transformation of the label alone. Classically, it should explain equal-prefix adaptive queries, the role of an adversarial law rather than an input-preparation protocol, and why an unconditional capped predictor bounds a joint event. Neither quantum background nor the word “independence” supplies these steps automatically (EX150, EX159, EX160, EX161, EX162, EX163, EX171, EX172, EX173, EX174, EX175, EX176).

### TEACH: assignable with guidance; the final assessment needs criteria

The simulated lecturer would assign this in a guided, multi-session unit. The first intervention would be to clarify the promised-search output; further support would include a register demonstration, a careful conditional-probability discussion, and explicit separation of optional proof routes. The answer-exposed exercise analysis supports comments on task design and mathematical content, not a claim that a novice independently solved the questions.

The likely shallow takeaway—hidden certificates make the task total, quantum search checks fewer candidates, classical algorithms must find an address—is directionally right but insufficient. Successful assessment should require the two changed locations, the capped joint prediction event, sampling without estimating weights, preservation of the conditional law, retained-list verification, and the strict fixed-$k$ exponent calculation. Provide criteria separately from the prompts so that students can distinguish a mechanism explanation from a slogan (EX181, EX182, EX208, EX237).

## The exposition, section by section

### Introduction: precision is present; entry and emphasis need adjustment

The bit-reading example, pointwise error definition, and every-branch query cap provide a strong foundation. The hardware boundary is brief and appropriate; a positive sentence explaining the benefit of isolating information access would complete its motivation. “Answer correctly on every possible input” momentarily sounds like zero error before the precise convention resolves it (EX002, EX003, EX004; EX125, EX126; EX065).

The total-versus-partial example needs an actual correction in task specification: finding the unique marked index is meaningful search, whereas deciding OR under that promise is constant. This does not invalidate any theorem. By contrast, the placement of the infimum and $1+Q$ convention is a teaching preference: MATH values their early precision; UG and TEACH experience them as competing demands before the construction. Keep the exact statement readily available while giving the powers of $m$ greater emphasis than loose constants and logarithms (EX005, EX006; EX066, EX067; EX181, EX182, EX183, EX184).

Retain the warning that the displayed quantities are one-sided bounds, the distinction between columns and total input length, and the fixed-$k$ dependence. These are necessary mathematical guidance, not removable caveats (EX068, EX069; EX185, EX186).

### Section 1: a strong signed example with a short operational bridge missing

Matching, reversing, and orthogonality make the three amplitudes intelligible. Squaring loses the sign and sends the negative, off-promise example to the same projection outcome as the positive one. That creates a concrete need for the later domain test; preserve the whole chain (EX010, EX015; EX134; EX190).

The remaining difficulty is turning linear algebra into an executable query experiment. Explain the purpose of the transform before displaying it; identify a register as one component of a basis label; and carry one existing input through the normalized state evolution. PHYS can recognize $H$ as two Hadamards, while MATH and UG need the basis-label explanation. These are complementary entrances, not a reason for a general quantum tutorial. The half-amplitude input is also a natural local check of amplitude versus probability (EX071, EX074, EX075, EX076, EX077; EX130, EX132, EX133; EX188, EX189).

The text already calls this a projection experiment and explicitly denies that one trial is a general decoder. Maintain that distinction when “success” changes meaning later. Keep the statement that the tiny instance illustrates operations without demonstrating asymptotic hardness (EX014, EX015, EX016; EX191).

### Section 2: the certificate is teachable; several contexts compete for attention

The winning definition and uniqueness argument are effective. All assignments are allowed, false transcripts included; the function's totality does not depend on an honesty promise. Address words select cells, stored pointers select rows, and reading a pointer costs its bits. These distinctions explain the construction rather than merely qualify it (EX018, EX020; EX079; EX193, EX195).

At the first transcript mention, give its purpose: a fixed circuit computes domain membership and the promised value. Then the later gate induction has a visible destination. An outsider also benefits from an explicit acyclic gate-order convention. When output tests are counted, explain that consistency with predecessors and the required domain/address value are different checks (EX021; EX135, EX142; EX197).

**Figure 1** shows the essential topology, but the small address-input and cell labels on page 4 weaken its teaching function at normal size. Enlarge those labels while preserving the visible difference between addresses and outward pointers. **Figure 2** provides the stable concrete board the prose needs: its zero targets, true cells, and failed incoming pointer make the winner test inspectable. Preserve it as the common reference and name each subsequent mutation by purpose; the figures need not multiply with every variation (EX120; EX194; EX025; EX096).

The three-query gate example plus induction is a real achievement. Question 1 correctly tests domain and address outputs; it does not also test the induction, so an optional changed-transcript follow-up would measure a different skill (EX024, EX026; EX198, EX199, EX200). The long credit paragraph should retain its attributions but distribute its union-bound and alphabet explanations to the points where readers can use them. In the historical comparison, specify that each input bit of $g$ is supplied by a separate AND-OR block, and identify the randomized composition bound as imported rather than elementary multiplication (EX081, EX087; EX201, EX202).

### Section 3: distinguish the supplier's three jobs and their proof status

The cheap decoder, exact small circuit, and classical hardness are a good interface. The section correctly separates verifying a stored computation from running that circuit afresh for each candidate. Keep the explicit large dependence on $k$: “cheap” means growth in $m$ for fixed $k$, not a practical small constant (EX090; EX146; EX203, EX205).

Three short additions would make this interface more explanatory. State the concentration fact being accepted, since elementary conditional probability does not necessarily include Chernoff bounds. Give the recursive split-and-combine idea behind the fast Walsh circuit, whose size is central to cheap verification. The linked record already contains it. Finally, describe the kind of indistinguishability assertion imported for shallow adaptive classical trees; the global-correlation picture explains quantum detection more directly than classical hardness (EX030, EX031; EX089, EX091; EX147, EX148).

### Section 4: the novel mechanism is present; show the state and control boundaries

The failed nested-search baseline gives the tournament a reason to exist. Keep the one-sided winner guarantee: off-promise rivals need no reliable decoder because their pointers cannot find a zero in the winner's all-one string. Keep the dominating nonwinner too; it proves why the tournament produces candidates requiring final verification (EX033, EX035, EX036; EX149, EX154, EX155).

The comparison convention supplies complementarity, while losers may cycle. **Figure 3** makes that failure of ordering visible and is readable, but its largely empty standalone page 9 interrupts the transition to weight analysis. Move it with that discussion. Its repaired caption correctly distinguishes displayed winning directions from the reverse pointers changed in the prose; any remaining alignment aid should preserve that distinction (EX121; EX209, EX210).

The ideal process has the right operational weight definition and explicitly avoids estimating the weights. Expose the ordered-pair grouping and vanished diagonal at the half-drift identity, then explain in words why an unlisted, still-heavy winner is incompatible with a very small total weight. The fractional example is necessary and already supplied; an exercise continuing its existing matrix would test unequal probabilities better than another zero-one case (EX037, EX038, EX039, EX040; EX098, EX099, EX100; EX211, EX212).

A compact register display should then connect that probability process to preparation and inversion. Preserve fresh comparison workspaces, orthogonal candidate labels, and good/bad vectors containing **all** workspace. A small reflection sketch or matrix can explain the rotation without adding both representations. The $p=1/2$ example teaches invariance without improvement; the existing $p=1/4$ exercise shows amplification, and another iteration of the same case could test overshoot (EX160, EX161, EX162, EX163, EX164, EX165; EX101; EX208, EX213, EX214, EX215).

Do not weaken the cap valid even below its guarantee threshold, including zero success. Retaining every sampled pivot makes later sampler failure harmless once the winner is listed. Final verification's success flag means finding a violation, and comparison errors already belong to the actual comparison law. The last accounting should leave readers remembering that short-list generation and verification add two square-root-scale costs, where naive nesting multiplied them (EX043, EX044, EX045; EX166, EX167, EX168, EX169, EX170; EX218, EX219, EX220).

### Section 5: the reduction is convincing when event scopes remain visible

The single hard law against every capped tree is explained well. Clarify that the distribution need not be secret or efficiently samplable: knowing the law does not reveal its hidden draw. The dummy/planted coupling then has a concrete reason—equal earlier answers force equal next queries until a changed location is reached (EX047, EX049; EX105, EX106; EX171, EX172, EX173).

**Figure 4** usefully displays the two changed locations. Its specific column and address should be identified as one illustrated realization, with transcripts consistent with the newly sampled address inputs, rather than literally reusing Figure 2's cell data. The $m=4$, $L=0$ boundary is already stated and must remain. Its current placement on page 14 interrupts the early/late-discovery sentence begun on page 13; placing it with the pair construction would repair both conceptual and page flow (EX048; EX172; EX122; EX222, EX223).

The erased-zero proof needs only a clearer charging sentence for late discoveries. Preserve the distinction between a uniform marginal and independence from the run, and Question 3's useful counterexample. A small follow-up about adaptive queries would test understanding beyond its fixed-position arithmetic (EX050, EX051; EX107, EX108; EX224).

The true-cell reduction is the section's strongest insight: the query position already proposes the entire answer vector, even if it is a guess. Preserve the unconditional cap, defined abort output, and inclusion of the light true-cell event in predictor success. The three budgets are now explained correctly and should stay separate. In the optional proof, isolate the transcript rectangle before introducing the residual-budget value; never suggest that independence survives arbitrary conditioning. Label the AND/XOR auxiliary tasks and the separate simulator's indexing so readers know which model is active (EX052, EX053, EX054, EX055, EX056; EX109, EX110, EX111, EX112, EX113; EX175, EX176; EX226, EX227, EX228, EX229, EX230).

Question 4 should ask separately for the new branch's $1/8$ contribution and the full $1/4$ event. Its stopping clause and explanation of a later query making the whole run heavy are correct. Finish by emphasizing the event being averaged over one independently selected column, not a union over successful guesses in all columns (EX057, EX058; EX114, EX115; EX225, EX232, EX233, EX234).

### Sections 6–7, answers, and references: preserve the accurate boundaries

The final ratio argument correctly uses one-sided estimates and monotonicity. Keep the strict positive exponent gap, fixed-$k$ order, and corrected endpoint question. Minor floor arithmetic can be compressed without changing those safeguards. Mark route-specific final teach-back questions and provide separate success criteria (EX059; EX116, EX117; EX178, EX179; EX235, EX236, EX237).

The Lean section has a concrete inspection task and states the difference between an explicit logarithmic power and an existential formal bound. A tiny cue for the option-valued partial-function clause and a plain description of Comparator's statement-matching role would make that task usable. Preserve the warning that definitions still need inspection; no new formalization or receipt audit is requested (EX060, EX061; EX118, EX119; EX180; EX238, EX239).

The numbered answers agree with the recorded mathematical attempts and have useful return links. Short diagnostic labels would clarify what each exercise measures. The two bibliography entries isolated on page 20 and awkward URL wraps merit a final layout pass, after the substantive figures and proof flow (EX123, EX124).

## How the other two documents serve the exposition

The **expert companion's introduction** supplies a concise specialist destination and literature context. It is useful after the exposition establishes the objects; it cannot replace the missing register or query-tree bridges for beginners. This is an assessment of its introductory service, not a whole-companion review.

The **reasoning record** supplies valuable depth at the sampled destinations: exact circuits, minimax, amplification, simulator traces, and the universal upper bound. Two navigational repairs matter. The finite checker uses a different numerical board, honestly disclosed; identify precisely which circuit and certificate facts transfer. In the packaged target, the amplification invitation lands after the trial parameters it promises; it should include those definitions as landing context. Finally, align moving overview links with the intended pinned edition; no current disagreement between editions has been established (EX022, EX042, EX062; EX139; EX196, EX216, EX240).

The next revision should preserve the present mathematics and its productive counterexamples while making these interfaces easier to traverse. That work would improve independent understanding more than additional constants, caveats, or examples disconnected from the two mechanisms the paper promises to teach.
