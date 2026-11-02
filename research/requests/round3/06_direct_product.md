## Your section: adaptive transcripts and the capped direct product

**Prioritized reading.** Read baseline §6.1 completely, with the promise model in §2.1 and the use of the lemma in §6.5. Then read OpenAI §4.1, the specific Drucker/Shaltiel passages, the named direct-product declarations and return-4 review. For style, sample the QAOA long overview and its transition into §1.

Revise long-record §6.1 as a complete, independently readable proof of the capped direct-product lemma used by the planted argument. Define the independent input law, adaptive transcript, per-instance query counts, conditional continuation values and terminal success. Explain where the product bound is obtained and how it reaches the joint event that every output is correct and every per-instance cap is respected.

Use OpenAI §4.1 and Lemma 4.1 as the target. Compare Drucker, arXiv:1005.0644v2, §1.3 and Lemmas 3.1–3.2 (printed pp. 11–12), and Shaltiel, ECCC TR01-009, §5 Definition 4, Theorem 5 and Lemma 7 (pp. 11–12). Their hypotheses and target events differ: Drucker's Theorem 1.1 is a global-budget theorem; Shaltiel's cited statement is an XOR-advantage theorem for fair trees. Neither can be silently relabelled as this exact vector-output/per-instance-cap statement. Use the QAOA long record for motivating a hard proof before displaying its local lemmas.

Read `LowerBound/DirectProduct.lean`, `LowerBound/Minimax.lean`, candidate `Paper/ClassicalDirectProduct.lean`, return 4's blueprint and checks, and the classical adjudication and candidate ties. Derive the Cartesian-product transcript event and the conditional law only for positive-mass histories; handle impossible branches explicitly. Explain repeated queries, the relation between the potential and actual terminal success, and why a bound after conditioning on non-heavy behavior alone does not bound the joint event.

Return `section.md`, a minimal worked adaptive-tree example and exact check, and the common correspondence files. Identify whether the source follows the paper's supermartingale or an alternative sub-distribution/potential proof. A returned candidate proof is uncompiled until the exact native receipt says otherwise.
