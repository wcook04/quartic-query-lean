# {title}

This packet holds three documents about OpenAI's preprint *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*: a short expert companion (`repository/docs/expert_companion.md` and its PDF), an examples-first exposition (`repository/docs/exposition.md` and its PDF), and a long reasoning record (`repository/docs/reasoning_record.md` and its PDF) that holds the full proofs and the links to the Lean formalisation. Execute the assignment now, in one sustained response, and return a ZIP. Do not return only a plan or an acknowledgement.

## What this pass is for

The documents have already been through five rounds of review, most recently a round of located corrections (`previous_round/`). They are now mathematically careful. This pass asks a different question: **would the experts who wrote the cited papers find these documents worth their time, and what would they ask the authors?**

You are not a copy editor and you are not rewriting. Read as a panel of experts from the community named below. For each expert reader, adopt the background and priorities of the authors of a specific cited paper (for example, "a reader with the background of the authors of the cheat-sheet paper"). Do not attribute opinions, quotations or reactions to any real, named person; the panel is a set of informed perspectives, each anchored in what a cited paper shows its authors know and care about.

Then interrogate the documents the way such a reader would in a seminar or a referee report:

- **Why are you doing this?** For each section, figure, table, example, remark and appendix: what is it for, would this reader need it, and does it earn its place? Ask why a proof is done this way and not the obvious way, why a step is spelled out or skipped, why a constant or a refinement is shown.
- **Weighting.** Where do the documents overweight what these readers already know or do not care about, and underweight what is new, surprising or delicate to them? Estimate page share now versus page share deserved.
- **What they would want to see** that is absent: context, the comparison with their own method, the reason the previous approach stopped, the key idea stated in their language, a cleaner statement, a figure, a sanity check, a pointer to the formal statement.
- **What would make them stop reading**, and where.
- **What they would admire** and what must survive any revision.

Use the supplied literature to make each perspective concrete: read how each cited paper introduces its construction, what it assumes without comment, how long its overview is, how it states theorems and credits predecessors. Use it to check every attribution the documents make to that paper.

## Principles from readers of AI-produced mathematics

`reader_principles.md` lists principles distilled from feedback by researchers who have read AI-produced mathematics and interfaces over it. Judge the documents against them. They are criteria, not findings: say where each is met and where it fails, with locators.

## How the documents are produced

`skills/` holds the general writing method the documents follow (record to short paper, record to exposition, and their shared README). Where a weakness you find comes from the method rather than this instance, say so in `method_findings` so the method can be improved for every future paper.

## State of the evidence

All formal claims the documents make were checked against the actual receipts before this packet was built: the four headline theorems are accepted by Comparator (including a paranoid run); Lemma 2.2, its two parts and the erased-zero identity are directly compared; the round-four additions are built and their dedicated comparisons accepted. `previous_round/round5_statement_fidelity.md` records an independent check of every cited Lean statement against the claim it is cited for. Do not spend findings re-verifying receipts; do judge whether the documents present the evidence in a way these readers would trust and use. `SOURCE_STATUS.json` binds the packet to the exact bytes by SHA-256; `LINK_MAP.json` resolves every link in the two papers.

`previous_round/` also holds last round's verdicts and the per-finding dispositions. Do not repeat a finding that was fixed; do say if a fix landed badly or created a new problem.

{job}

## Return format

Return one ZIP containing:

1. `findings.json`: an object with `packet` (this packet's job name), `source_sha256` (copy the `drafts` object from `SOURCE_STATUS.json`), `panel` (a list of the expert perspectives you adopted, each with the cited paper it is anchored in and what that reader already knows), and `findings`, a list. Each finding has
   - `id`: the prefix given below and a number;
   - `paper`: `expert_companion`, `exposition`, `reasoning_record` or `all`;
   - `perspective`: which panel perspective raises it;
   - `locator`: `section` and `quote` (an exact phrase of at most 25 words from the current Markdown), optional `pdf_page`;
   - `kind`: `question` (what the reader would ask the authors), `overweighted`, `underweighted`, `missing`, `misplaced`, `unclear`, `credit`, `error`, `evidence_presentation`, or `keep`;
   - `severity`: `critical`, `high`, `medium`, `low` or `keep`;
   - `finding`: the question or the problem, in that reader's terms;
   - `why_it_matters`: what it costs that reader;
   - `suggested_direction`: what to change, without replacement prose;
   - `evidence`: optional exact locators in the literature, preprint, record or Lean source.
2. `weighting.md`: a table per document of sections with current page share, the share this panel thinks they deserve, and one line of reasoning each.
3. `questions.md`: the twenty most important questions this panel would ask the authors, in priority order, each with its locator.
4. `method_findings.json`: weaknesses that come from the writing method in `skills/`, each with the rule it would change.
5. `verdict.md`: at most one page: would this panel read to the end, the five changes that matter most, and what must be kept.

Aim for several dozen findings. Every finding must quote the current text. One precise question beats three vague complaints. If you believe you have found a mathematical error, mark it `error`, give the exact step and why it fails. State which sources you actually read and which you only sampled.

{boundary}
