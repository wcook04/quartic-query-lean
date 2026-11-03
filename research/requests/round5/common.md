# {title}

You are an independent referee of two working drafts about OpenAI's preprint *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*: a short expert companion (`repository/docs/expert_companion.md` and its rendered PDF) and an examples-first exposition (`repository/docs/exposition.md` and its rendered PDF). Both depend on a long reasoning record (`repository/docs/reasoning_record.md` and its PDF), which holds the full proofs and the links to the Lean formalisation. Execute the assignment now, in one sustained response. Do not return only a plan or an acknowledgement.

Your job is to **critique, not to rewrite**. Return many concrete, located findings that will let the authors make the next revision far better than typical AI-written mathematics. Report mainly what is bad, missing, misplaced, wasted, unclear, wrongly credited, badly ordered or badly linked to the Lean development. Also report what is good and must survive revision. Do not return a rewritten manuscript, replacement sections or new proofs. A suggested direction may include a short phrase or a sketch of structure, never a replacement passage.

## Who reads these papers

Read as the researchers whose papers these drafts cite would read them: the authors of the work on Forrelation, cheat sheets, pointer functions, the sensitivity theorem and its quantum consequences, optimal k-fold Forrelation separations, direct product theorems, amplitude amplification, quantum search and minimum or king finding. Judge whether those experts would find each paper clear, correctly credited, accurately placed in the history of randomized-versus-quantum separations, and efficient with their attention.

Apply these general principles of a strong mathematical paper:

- It models what its readers already know and does not spend pages on it. This field knows the query model, Forrelation and its quantum algorithm, amplitude amplification, minimax and Yao's principle, Markov and union bounds, the bound D = O(Q^4) through the sensitivity theorem, and the cheat-sheet framework.
- It spells out what they do not know: the new construction, the new mechanism in each bound, and every delicate point. Delicate points should be proved carefully and in one place.
- It shows the path to the result, not only the result. A reader should see early, in one or two lines, why the exponent is four, what stopped earlier methods, and what the new idea changes.
- It credits prior work exactly: which idea comes from which paper, at which locator, and what is new here.
- It lets a reader check that the Lean statement encodes the intended theorem without reading the proof: which file to read, which definitions matter, which theorems are compared, and what the checker does and does not establish.
- Its links work and land somewhere useful. A reader who follows a link from the short paper into the long record or the Lean source should arrive at the exact supporting argument.

Use the supplied literature in two ways: to check credit and locators, and to learn how this field writes. Notice what the cited papers assume without comment, how they state theorems, how long their overviews are and how they introduce their constructions. Use what you learn to judge the drafts. Do not use it to propose new results.

## What is in the packet and what state it is in

The drafts are **unreviewed working drafts**. Their statements about the newest Lean additions (the full-state amplifier, the direct product for arbitrary independent randomness, the zero-cost and degree sanity theorems, the sharper zero-search count) describe a rebuild and comparison that is finishing in parallel; judge the writing as stated and do not spend findings on that status. Locate every finding by section and quoted phrase, not only by page or line number. `SOURCE_STATUS.json` binds this packet to the exact bytes of every draft, rendered PDF and record by SHA-256. The record's PDF was rendered from an earlier version of its Markdown; `SOURCE_STATUS.json` records both hashes, and when the earlier text is available `repository/docs/reasoning_record.since_pdf.diff` shows the difference. Treat the Markdown as current.

`LINK_MAP.json` lists every link in the two drafts with the packet member it resolves to, and records whether its anchor or line range exists. Use it when you judge the linking layer, and check a sample of links yourself.

The Lean statement a reader must audit is `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`; its solution and Comparator configuration sit beside it, and `repository/corpus/comparator_map.json` maps each compared block to its record passage. `repository/docs/lean_links.json` gives every Lean object the drafts cite a plain name, file, line range and pinned link.

The writing exemplars under `exemplars/` concern another theorem (the Sherrington–Kirkpatrick order parameter): a long reasoning record, a short paper and an expository paper. Use them as examples of structure and register only. They establish nothing about this result.

## Earlier editorial findings on the predecessor drafts

An editorial review of the previous drafts found no mathematical error but recorded these problems. For each, check whether the current drafts resolve it. Report a remaining instance only with a fresh locator in the current text, and say when a problem has been fixed well.

1. Placement and credit: the line of total-function separations (5/2 from cheat sheets, 8/3 − o(1) from Tal, 3 − o(1) from Bansal–Sinha and independently Sherstov–Storozhenko–Wu) was missing; pointer functions were not credited; k-fold Forrelation was not introduced as Aaronson–Ambainis's problem; the inheritance from cheat sheets (addressing by answers to independent partial-function instances, certificate at the address) was under-stated; comparison-based search work (Ben-David–Kothari 2026, Ambainis–Iraids–Kokainis 2026, Dürr–Høyer, Mande–Paraashar–Saurabh) and Høyer–Mosca–de Wolf were not discussed; the exposition misattributed the addressing idea.
2. The central idea was never put in one line: quantum about √m polylog, classical about m·L with L ≈ m^(1−1/k), hence R ≈ Q^(4−2/k); and what stopped the cheat-sheet route at three.
3. A reader could not quickly check the formal statement: no pointer to the statement file, implementation names cited instead of the compared names, and evidence accounting in internal vocabulary.
4. Formal-status sentences overreached or were stale: comparison credit for names that were not configured targets, a displayed theorem with constants stronger than what was compared, and stale statements about retained-state amplification, external randomness and the list-output tournament.
5. Pages were spent on known material (amplification proved in full, a long Forrelation lower-bound section) and too few on the delicate points; there were no figures.
6. Provenance debris, dead relative links and margin overruns appeared in the rendered PDFs.
7. Delicate points were present but not signposted: the erased-zero identity Pr[hit] = E[Z]/m and why the planted index must be independent of the whole run; joint (not pairwise) independence of coins and side information; a table of natural shortcuts that fail, each with its counterexample.
8. The exposition had good examples but no frame: the theorem appeared late, no road map, no history, no figures; some sections were overlong for strong students.
9. The logarithmic exponent in the displayed theorem was not derived.
10. Notation collided (M, T, t, G, N, s, q and γ each had two meanings), and equation numbers did not cross-reference the preprint's.
11. The growing-k section rested on a constant lemma with build evidence only and should become a short, explicit remark.
12. The abstract used undefined terms and led with minor formal refinements.
13. A version-specific remark about one displayed step of a cited paper needed either omission or a neutral footnote with its exact locator.
14. Internal project vocabulary appeared in reader-facing text.

{job}

## Comment on the Lean-linking layer

Every job also reviews the links between prose and formal evidence: whether central claims point to the exact compared theorem or to a built-only declaration, whether the reader can tell which, whether link targets exist and land on the supporting passage or declaration, whether names and line ranges match `Challenge.lean`, `Solution.lean` and `comparator_map.json`, and whether the formal-status sentences say exactly what the evidence supports. Use category `lean_link` for these findings.

## Return format

Return two things inline, and also as files if you can create files:

1. `findings.json`, an object with these fields:
   - `packet`: this packet's job name;
   - `source_sha256`: copy the `drafts` object from `SOURCE_STATUS.json`;
   - `findings`: a list. Each finding has
     - `id`: a short prefix for the job and a number, for example `ER-001`;
     - `paper`: `expert_companion`, `exposition`, `reasoning_record`, `lean_layer` or `both`;
     - `locator`: an object with `section` (the section number and heading) and `quote` (an exact phrase of at most 25 words from the current Markdown), plus optional `pdf_page`;
     - `severity`: `critical`, `high`, `medium`, `low` or `keep`;
     - `category`: one of `error`, `missing`, `misplaced`, `wasted`, `unclear`, `credit`, `history`, `notation`, `figure`, `structure`, `register`, `lean_link`, `keep`;
     - `finding`: what is wrong, or what is good;
     - `reader_impact`: which cited-literature readers would notice and why it costs them;
     - `suggested_direction`: what the revision should do, without replacement prose;
     - `evidence`: optional exact locators in the supplied literature, preprint, record or Lean source that support the finding.
2. `verdict.md`: at most one page. Give your overall judgement, the five changes that matter most, and what must be kept.

Aim for several dozen findings, ordered by severity, with the critical ones first. Every finding must quote the current text. Do not pad: one precise finding beats three vague ones. If you believe you have found a mathematical error, mark it `error`, give the exact step and why it fails, and keep it separate from writing criticism. State which sources you actually read and which you only sampled.

{boundary}
