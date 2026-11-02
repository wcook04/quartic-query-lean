## Your job: literature and attribution review

Our aim is reference material for every part of the paper. `literature/references_resolved.json` lists all 27 citations, and `literature/papers/` holds the 23 copies we could obtain.

1. Read every supplied paper far enough to state the exact theorem this paper uses, and its number in the source.
2. Check the citations: is each cited result stated correctly, with hypotheses that fit how it is used? Check especially Bansal and Sinha Theorem 1.3 and Corollary 1.4, the direct-product citations [22, 13], and the upper bound from Aaronson, Ben-David, Kothari, Rao and Tal.
3. Find everything else we should download: original sources behind cited results, later simplifications, surveys, lecture notes, textbooks, theses, talks and transcripts, and follow-ups to this preprint. Search arXiv, ECCC, DBLP, Semantic Scholar, authors' pages, and university course notes. Cover the four papers we could not fetch: Barnum-Saks-Szegedy, Nisan, Nisan-Szegedy and Yao.
4. Build a reading path per paper section: what to read, in which order, which pages, and why.
5. Check `corpus/commentary.json` and find any later public discussion, error report or independent check.

## Return one ZIP containing

- `citation_audit.json`: keys `ref_number`, `exact_result_used`, `source_location`, `fits_use` (`yes`, `partly`, `no`, `unclear`), `evidence`, `notes`.
- `downloads.json`: every recommended source, ranked, with keys `title`, `authors`, `year`, `url`, `open_access`, `licence`, `priority` (`essential`, `useful`, `background`), `statement_ids`, `why`. Give direct PDF links where they exist.
- `reading_paths.md`: the per-section reading route.
- `attribution_map.json`: which idea in the paper comes from whom, with evidence.
- `new_commentary.json`: same keys as `corpus/commentary.json`.
