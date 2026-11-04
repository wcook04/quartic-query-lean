# Scoped quantum verification

## Outcome and purpose

No mathematical error was substantiated in the inspected projection decoder, coherent tests, complementary comparator, product-weight sampler, capped amplification, early-stop coupling, total-input verification or logarithmic cost combination. This is scoped proof and source inspection, not a whole-corpus proof audit or code execution. The exact claims and checks are in [quantum_verification_checks.json](../evidence/quantum_verification_checks.json); the Q-S source records in [sources_read.json](../sources_read.json) define their reading limits.

The principal structural recommendation is XP10-008: make the identity `Pr[success and label i] = w_i/m` available before the detailed finite amplifier schedule. Retain the complete local exact-law and all-branch-cap contract. The final advice and optional related-work update are in [feedback.json](../feedback.json), not in a separate competing candidate list.

## Technical checks that constrain the edit

The BBHT averaging expression is `1/2 − sin(4Mθ)/(4M sin(2θ))`. At the chosen cutoff the inspected calculation gives at least `19/40`, supporting the paper's weaker `9/20`. BHMT Theorem 3/QSearch provides expected cost and can continue indefinitely at zero success. A generic citation to that routine alone does not establish the bounded interface needed here. [Q-S04–Q-S05; quantum check inventory.]

The retained conditional good-state law supports the measured-label distribution used by the tournament. The preparation probability `W/m`, the amplified routine's success probability, and its conditional label law are three distinct quantities. Fresh workspaces and inverse access remain material to the stated construction. The additional formal physical-state correspondence is not silently substituted for the measured-label law used in the Boolean continuation. [Q-S15–Q-S17.]

The projection experiment and the interference experiment in Aaronson–Ambainis were checked against their original pages. No erroneous reference to their different probabilities was established in the present decoder discussion. Final certificate verification remains necessary even after finding a dominant comparison candidate, because dominance alone does not certify a winning column. [Q-S06; lead §3.3 and A.1–A.3.]

## Edition and inspection boundaries

Reasoning-record support comes from the current packaged file. The packet reports different bytes at the lead's public pin `8357f268732746d1575e05e7de8c888e20ad3793`. The review did not independently obtain that exact pinned body or verify a live hyperlink round trip. The narrower reconstruction of a later pin-only rebind is documented in [attached_context_review.json](../evidence/attached_context_review.json).

Supplied Lean statements and selected local proof text were inspected statically. No build, Comparator execution, dependency rerun or whole-module semantic audit was performed. The quantum specialist visually inspected four original literature pages: Aaronson–Ambainis pp.13–14, BBHT p.3, and published MPS p.30:13. The separate lead-PDF review covered all 18 pages and is recorded in [pdf_inspection.json](../evidence/pdf_inspection.json).
