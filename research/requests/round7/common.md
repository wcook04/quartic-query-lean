# {title}

This packet holds the three documents about OpenAI's preprint *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, one for each stage of the writing funnel:

- the **long reasoning record** (`repository/docs/reasoning_record.md` and its PDF), which holds every proof in full, the reasoning behind each step and the links to the Lean formalisation;
- the **short expert companion** (`repository/docs/expert_companion.md` and its PDF), a research-paper account for specialists in query complexity;
- the **exposition** (`repository/docs/exposition.md` and its PDF), written for a reader who is *not* trained in this area. It should teach the result through worked examples, so that a mathematically literate newcomer can follow why the theorem is true and why it matters.

The short paper and the exposition are both derived from the long record. Execute the assignment now, in one sustained response, and return a ZIP. Do not return only a plan or an acknowledgement.

## What this pass is for

We want feedback: as much of it as you can give, of every kind. Complain about anything that is unclear, badly written, badly ordered, unmotivated, too long, too short, missing, wrong, unconvincing or dull. Give advice wherever you have it. Nothing is too small to mention and nothing is too large: a single clumsy sentence, a figure that does not help, a section that should not exist, a whole document that is aimed at the wrong reader. Be harsh where the text deserves it; politeness costs us information. The documents have been through six rounds of review (the last round is summarised in `previous_round/`), so the obvious problems are gone; we want the next layer, the things a careful reader still trips over.

Volume matters. A thorough return has well over a hundred separate points, covering every section of all three documents. Read every paragraph of the document your panel leads with, and read the others in full or in substantial part. Do not stop when you have found the big problems; the long tail of small ones is what we cannot see ourselves.

Read as the panel described below. Each panel member has the background of the authors of a cited paper or of a named kind of reader; do not attribute opinions, quotations or reactions to any real person.

## What to look at

Cover all of the following, in whatever proportion your panel's background dictates.

1. **Clarity.** Where did you get lost, and at exactly which sentence? What were you expecting at that point, and what did you need first? Which terms, symbols or objects arrive undefined, defined too late, or defined twice in different ways? Which hypotheses are stated without saying what they rule out?
2. **Teaching (above all in the exposition).** The exposition must be intelligible to someone who has not studied query complexity: say a mathematician from another field, a strong undergraduate in mathematics or computer science, or a physicist who knows a little quantum computing. Where does it assume knowledge such a reader lacks? Where is a worked example missing exactly where the reader needs one? Which examples are the wrong size, stop before they pay off, or illustrate something other than the hard step? Where does the reader lose the thread of why the exponent tends to four, why the obvious approaches fail and why each ingredient is needed?
3. **Writing, sentence by sentence.** Compare the prose with the supplied literature and with the exemplar papers: openings, how a construction is introduced, how a theorem is stated, how predecessors are credited, how long an overview runs, what is left unsaid. Quote sentences that read as machine prose, as padding, as bureaucracy, as defensive hedging or as a list where an argument belongs. Note every sentence you would cut and every one whose meaning you had to reconstruct.
4. **Structure and weighting.** For each section, figure, table, example, remark and appendix: what is it for, does it earn its place, is it in the right place? Where are the documents overweight (routine arithmetic, refinements, evidence bookkeeping, things the intended reader already knows) and underweight (the new idea, the delicate step, the intuition)?
5. **The funnel.** Does each derived document carry over what it should from the long record and leave behind what it should? Do the three agree on statements, constants, names and credit? Can a reader follow a claim from the exposition to the short paper to the full proof in the record and on to the Lean statement? Is the long record itself readable as the destination of those links: can a reader find what they came for, and is its reasoning recorded in a way a referee could audit?
6. **Mathematics and credit.** Anything you believe is wrong, overstated, understated or misattributed. Check attributions against the supplied papers and against what you find online.
7. **What works.** What you would keep through any revision, and why. Strengths are information too.

## Use the literature, and go beyond it

`literature/` holds a *sample* of the cited and related papers chosen for your panel, with extracted text and originals; the full bibliographies are in the `.bib` files and the preprint. Read the sample closely for how the field writes. **Then search online**: arXiv, journal pages, authors' home pages, lecture notes, textbooks, survey articles, talks and blog posts on query complexity, Forrelation and quantum–classical separations. Use what you find to judge how the field explains these ideas to newcomers and to experts, to check credit, and to find explanations, examples or figures that do better than ours. Cite every outside source you use with a URL or identifier, and say which you actually read and which you only skimmed.

## How the documents are produced

We want to improve the general method as well as these three documents, so that the next paper, in any field, starts better.

- `skills/` holds the writing method: how a long record is built, how the short paper and the exposition are derived from it, and the register stage that measures and line-edits every draft against its cited literature.
- `register/` holds the register stage's output for this round: the general writing rules (`REGISTER_RULES.md`, with specimens from published papers), a profile of the supplied literature, and a measurement of where each draft sits against it (`measurement.txt`). The measurement is a detector, never a verdict; tell us where it is right, where it misses what a reader notices, and where it flags something harmless.
- `reader_principles.md` lists principles distilled from researchers who have read AI-produced mathematics.
- `exemplars/` holds papers produced by the same method for other theorems.

Wherever a problem you find comes from the method rather than from this instance, say so, name the rule or skill that let it through (or caused it), and say what the method should do instead, phrased generally enough to help a paper on a different theorem.

## State of the evidence

The formal claims were checked against the actual receipts before this packet was built, and `previous_round/round6_statement_fidelity.md` records an independent comparison of each cited Lean statement with the claim it supports. Do not spend effort re-verifying receipts; do say whether the documents present the formal evidence in a way their intended reader would understand and use. `SOURCE_STATUS.json` binds the packet to exact bytes; `LINK_MAP.json` resolves every link in the two shorter papers. `previous_round/` holds last round's per-finding dispositions and plans: do not re-raise a point that was fixed, but do say where a fix landed badly or made something worse.

{job}

## Return format

Return one ZIP containing:

1. `feedback.json`: an object with `packet` (this packet's job name), `source_sha256` (copy the `drafts` object from `SOURCE_STATUS.json`), `panel` (the perspectives you adopted, each with its anchoring paper or kind of reader and what that reader already knows), `sources_read` (literature and online sources, each marked `read` or `skimmed`, online ones with URL), and `feedback`, a list. Each item has
   - `id`: the prefix given below and a number;
   - `paper`: `exposition`, `expert_companion`, `reasoning_record` or `all`;
   - `perspective`: which panel member raises it;
   - `locator`: `section` and `quote` (an exact phrase of at most 25 words from the current Markdown), optional `pdf_page`;
   - `kind`: `unclear`, `lost_here`, `missing_example`, `missing`, `teaching`, `prose`, `structure`, `overweighted`, `underweighted`, `funnel`, `consistency`, `credit`, `error`, `figure`, `evidence_presentation`, `question` or `keep`;
   - `severity`: `critical`, `high`, `medium`, `low` or `keep`;
   - `feedback`: the complaint, question or observation, in full, in your reader's terms;
   - `why_it_matters`: what it costs that reader;
   - `advice`: what you would do about it, as specifically as you like (a direction, a structure, an example to use, a source that does it well, a short phrase); optional;
   - `outside_source`: optional URL or identifier of a source that bears on it.
2. `reading_log.md`: a running account, section by section, of reading the document your panel leads with: what you understood, where you slowed down, where you got lost, what you expected next, and what you would have needed. Write it as you read, at length.
3. `feedback_by_document.md`: for each of the three documents, a long prose critique: the overall verdict, the main problems in order of importance, what the intended reader would take away now versus what they should take away, and what must be kept.
4. `literature_comparison.md`: how the supplied and online literature handles the same ideas (openings, examples, figures, statements, credit), with quotations of at most 25 words and locators, and where ours falls short or does better.
5. `method_feedback.json`: problems that come from the writing method (`skills/`, `register/`, `reader_principles.md`), each with the rule or skill concerned, the instances in these documents, and what the method should do instead, stated generally.
6. `verdict.md`: at most two pages: would your panel read each document to the end, the ten changes that matter most, and what must be kept.

Every item in `feedback.json` must quote the current text exactly. If you believe you have found a mathematical error, mark it `error` and give the exact step and why it fails. State which sources you actually read and which you only sampled.

{boundary}
