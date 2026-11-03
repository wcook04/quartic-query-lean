# Twenty questions for the authors

Priority order for the modeled student/lecturer panel. These are questions about the current documents, not reported reactions of real people. Quotes are exact excerpts from the supplied current Markdown. Full consequences, sources and round-five dispositions are in `findings.json` and `findings.md`.

1. **What prevents a classical algorithm from distinguishing the inputs without first finding a certificate?** (SX-004)

   Locator: `repository/docs/exposition.md`, line 32; Overview: reason for four.

   > locating it inside one column means naming an address, which costs $L$ queries there

   Explain the two exposure channels and the aggregate guessing bound before using the mL heuristic.

2. **Can the reader carry one existing weight-table row all the way to an actual sampled quantum pivot?** (SX-019)

   Locator: `repository/docs/exposition.md`, line 177; §4: quantum pivot sampling.

   > Success has probability $|w|/m$

   Identify the success flag, success-and-label mass, total success probability, conditional label law and what amplification changes.

3. **How do the global, column-total and per-instance query budgets fit together?** (SX-030)

   Locator: `repository/docs/exposition.md`, line 232; §5: simulator query caps.

   > stops before the $(L+1)$-st of these

   The simulator stops after L target queries in total; the direct product permits L per instance. Show the implication and why it introduces no factor r.

4. **Which object in Section 1 is the raw projection experiment, and which is the bounded-error decoder?** (SX-009)

   Locator: `repository/docs/exposition.md`, line 74; §1: projection experiment.

   > The quantum algorithm for $P$ starts in $u$

   The showcased probabilities 1, 0, 1 conceal the need for Section 3 repetition on other promised inputs.

5. **What must the intended student already be able to do beyond recognize the query oracle?** (SX-001)

   Locator: `repository/docs/exposition.md`, line 26; Overview: audience.

   > a graduate student who knows the query models above

   Specify operational prerequisites for retained workspace, amplification and conditioning on an adaptive transcript.

6. **What changes when a student follows the simulator link into the record’s XOR example?** (SX-031)

   Locator: `repository/docs/exposition.md`, line 236; §5: simulator proof excursion.

   > traces the simulator on a small board, including a run where it stops

   Announce the function, input law, indexing and budget reset, and identify the generic simulation operation that survives.

7. **Must the independent Forrelation hardness proof be read before the construction?** (SX-042)

   Locator: `repository/docs/reasoning_record.md`, line 118; Reading guide versus §1.1 Dependencies and proof recovery.

   > The central construction can be read after §§3.1–3.5 and the precise ingredient statement in §3.17;

   Reconcile the opening “required” route with the later permission to accept the ingredient statement and continue.

8. **What existing task would demonstrate that a student can perform the advertised learning outcomes independently?** (SX-003)

   Locator: `repository/docs/exposition.md`, line 26; Overview and worked-example route.

   > By the end the reader should be able to build the function on a four-column board

   Use a changed case already present, with its answer separated, rather than add new mathematical material.

9. **Why is the address length logarithmic, and what is the coefficient 20 buying?** (SX-011)

   Locator: `repository/docs/exposition.md`, line 94; §2: attribution and address length.

   > they used about $10\log n$ copies, and here $r=20\log_2m$

   Connect it to the all-query guessing union bound and the affordable quantum decoder when it first appears.

10. **Precisely which parts of the Section 2 board are reused in the planted-pair illustration?** (SX-024)

   Locator: `repository/docs/exposition.md`, line 195; §5: planted-pair example reset.

   > the planted input is column $1$'s part of Figure 2

   Distinguish reused geometry from resampled promised inputs and newly blank certificate cells.

11. **Can one positive adaptive history demonstrate the product posterior before the counterexamples change the conditioning event?** (SX-028)

   Locator: `repository/docs/exposition.md`, line 221; §5: product posterior.

   > the tuples consistent with $\tau$ form a product

   Show coordinatewise restrictions and remaining budgets in an existing finite example.

12. **Which failure event and which histories does each error bound concern?** (SX-020)

   Locator: `repository/docs/exposition.md`, line 179; §4: success and failure events.

   > After the winner is listed nothing is claimed

   Separate decoder error, pivot-sampler failure, omission of the winner and final false acceptance, preserving the unconditional query cap.

13. **Which certificate-verification cost made the old cheat-sheet route stop at the cubic arithmetic used here?** (SX-005)

   Locator: `repository/docs/exposition.md`, line 38; Overview: Where this sits, final paragraph.

   > The same arithmetic shows why the earlier route stops at three.

   Map the old construction’s roles to cheap comparisons and delayed verification in the new one.

14. **Can the student identify the exact bits read by one local gate or pointer test?** (SX-014)

   Locator: `repository/docs/exposition.md`, line 114; §2: local tests.

   > On the board $K=4+3+2(180+2)=371$

   Relate the fixed public circuit to the untrusted transcript bits before emphasizing 180 gates or 371 tests.

15. **Why is an undiscovered zero still uniform after the full adaptive dummy transcript?** (SX-026)

   Locator: `repository/docs/exposition.md`, line 210; §5: The erased zero.

   > an undiscovered zero is uniform among its column's unread positions

   Use the independence and blank-cell assumptions at the point of the early-discovery bound.

16. **What can a lecturer assign as a quantum-focused route or a classical-focused route?** (SX-007)

   Locator: `repository/docs/exposition.md`, line 51; Overview, reading guidance.

   > The boxed proof in Section 5 can be skipped;

   Give retained statements, departure points, return points and endpoints using existing sections.

17. **Why does the first reading need the 9/40 amplifier constant at the moment it learns the tournament?** (SX-022)

   Locator: `repository/docs/exposition.md`, line 181; §4: fixed-cap amplification.

   > at least $9/40$ whenever $p\ge\gamma$

   Preserve the complete amplifier contract, but justify the priority of the numerical derivation or mark it optional.

18. **Which single statement-reading action should a student perform first in Section 7?** (SX-033)

   Locator: `repository/docs/exposition.md`, line 265; §7: first formal reading.

   > Five definitions carry the content.

   Distinguish a useful initial definition check from the deeper configuration and helper-theorem audit; clarify the referents of “neither” (SX-035).

19. **Relative to the current Lemma 2, what extra conclusion actually justifies the amplifier table’s “stronger” label?** (SX-040)

   Locator: `repository/docs/expert_companion.md`, line 338; Appendix A, Table 2, full amplifier row.

   > Stronger conclusion (the returned state)

   The printed lemma already includes a returned normalized good state; identify the actual additional claim without altering evidence status.

20. **Which exact checkout should the reproduction instructions use?** (SX-041)

   Locator: `repository/docs/expert_companion.md`, line 351; Appendix A, Reproducing the check.

   > the commit the links point to.

   The comment and generated links identify different commits. Distinguish historical execution provenance from the intended reading edition.
