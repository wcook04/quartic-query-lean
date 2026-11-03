## Your job: the long record as the destination of the short paper's links

Read `repository/docs/reasoning_record.md` and its PDF as the place a reader arrives after following a link from the expert companion or the exposition. This packet also contains the files the record itself links to (receipts, Lean sources, native views, adjudications and earlier returns), listed in `READING_LINK_CLOSURE.json`, so you can follow its links as a reader would.

Judge in particular:

- **Arrival.** For each link in `LINK_MAP.json` from the two drafts into the record, what does the reader find? Is the anchor the start of the supporting argument, or a table, a status note or the middle of an unrelated passage? Does the passage stand on its own, and does it tell the reader how to return?
- **Structure.** Is the record navigable as a whole: a roadmap, stable section numbers, a predictable shape for each proof, named statements that the short paper can cite? Where is the order wrong, where are proofs duplicated, and where is internal history mixed with mathematics?
- **Claims to evidence.** Pick the central claims (Theorem 1.1, the construction, each quantum step, each classical step, the Forrelation bound, the exponent) and trace each from the record to the exact Lean declaration and Comparator evidence. Does each claim link cleanly? Can the reader tell compared theorems from built-only declarations and from ordinary proofs without formal evidence?
- **Register.** Where does internal vocabulary (receipts, packets, audits, rounds) obstruct a mathematical reader? What should move to an appendix or a separate evidence file?
- **Size.** Which parts of the record would a reader arriving from the short paper never need, and which parts the short paper should point to but does not?

Compare with the long reasoning-record exemplar (`exemplars/long-reasoning-record.md` and `exemplars/qaoa-sk/long/reasoning-record.pdf`) for structure, return routes from the short paper and the separation of proof from evidence.
