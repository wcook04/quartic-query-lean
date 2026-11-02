## Your job: the long reasoning record (exposition and proof reconstruction)

Write the complete reasoning record of the preprint's theorem: the document in which every statement and every step can be checked by a careful reader, at the length that takes. The earlier exemplar `exemplars/long-reasoning-record.md` is about 33,000 words; use the length the mathematics needs.

1. Follow the preprint's dependency order, statement by statement, for all records in `corpus/statements.json`, including the added rows. For each: the exact statement with all quantifiers; a complete proof in ordinary mathematics, with no step left as "standard"; the Lean declarations that check it, with relation and route; and anything the Lean proof does differently.
2. Include the Forrelation lower bound in full along the route in `docs/forrelation_lower_bound_blueprint.md`, checked against the Lean source in `lean/QuarticQuery/ForrelationLower/` and the independent reading in `docs/forrelation_lower_bound_review.md`. Where the Lean proof is cleaner than the preprint (Lemma 4.1, the erased-zero bound `2G/m²`), present the cleaner argument and say so.
3. Where you find a cleaner derivation than both, write it, and put every new intermediate claim in `NEW_STATEMENTS.json` so it can be checked.
4. Mark each step's evidence plainly: checked in Lean by the same route, checked by another route, or proved here in prose only.

## Return one ZIP containing

- `reasoning-record.md`: the record, with `<!-- passage:NAME -->` anchors.
- `correspondence.json`, `NEW_STATEMENTS.json`, `STATEMENT_CHANGES.json`, `LEAN_GAPS.md` as specified above.
- `references.bib`: every cited work with DOI or arXiv identifier.
- `review_notes.md`: anything you believe is wrong or unclear in the Lean, the corpus or the preprint, with locations.
