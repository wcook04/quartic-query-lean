## Your panel: formal-methods readers and sceptics of AI-produced mathematics

Read all three documents with the eyes of researchers who formalise mathematics in Lean, maintain or review mathematical libraries, build statement-checking tools, or study how AI-written formal proofs go wrong (for example by proving a nearby, easier statement). Include at least one sceptic of AI-produced mathematics and one researcher who wants such work to succeed. Ground the perspectives in the formal artefacts supplied (`repository/lean/`, `repository/corpus/comparator_map.json`, `repository/docs/lean_links.json`, `previous_round/round5_statement_fidelity.md`) and in the papers' own evidence sections: the expert companion's Appendix A, the exposition's final section and the record's §2.9.

Press especially on:

- Would these readers trust the evidence presentation? What would they check first, can they check it in fifteen minutes, and where does the presentation make them suspicious or bored?
- Is it clear which statement was checked, by which tool, against which definitions, and what that does and does not establish? Is the same/stronger/weaker table convincing, and are the definitions of R, Q and the quantum model presented so a reader can confirm they are the standard ones?
- Where do the documents overweight evidence accounting (receipts, run history, configuration detail) relative to what a formal reader needs, and where do they underweight it (a hidden premise, a finite-seed restriction, a wrapper)?
- Where is the boundary between OpenAI's result, the Lean formalisation and these explanatory documents drawn, and is it drawn clearly enough that nobody mistakes an explanation for new mathematics?
- What a reader interface over these documents should show, given the principles in `reader_principles.md` (provenance of each link and graph edge, statement fidelity at each level).
