# {title}

This packet holds three documents about OpenAI's preprint *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, one for each stage of a writing funnel:

- the **short expert companion** (`repository/docs/expert_companion.md` and its PDF), a research paper for specialists in query complexity;
- the **exposition** (`repository/docs/exposition.md` and its PDF), which should teach the result through worked examples to a mathematically literate reader who has not studied the area;
- the **long reasoning record** (`repository/docs/reasoning_record.md` and its PDF), which holds every proof in full, the reasoning behind each step and the links to the Lean formalisation.

This packet is about **one** of the two short papers, named in the panel description below. Read that paper from the first word to the last, including figures, captions, footnotes, answers and references. The other two documents are there so you can follow its links, check that it agrees with them, and judge what it leaves out. Execute the assignment now, in one sustained response, and return a ZIP. Do not return only a plan or an acknowledgement.

## What this pass is for

We want feedback: as much of it as you can give, of every kind. Complain about anything that is unclear, badly written, badly ordered, unmotivated, too long, too short, missing, wrong, unconvincing or dull. Give advice wherever you have it. Nothing is too small to mention and nothing too large: a clumsy sentence, a figure that does not help, a section that should not exist, a paper aimed at the wrong reader. Be harsh where the text deserves it; politeness costs us information.

The papers have been through seven rounds of review. `previous_round/` summarises the last one: the cross-panel synthesis, the revision notes for each paper, the specialist audits, an independent cold read and the four panel verdicts. The obvious problems should be gone. We want the next layer: what a careful reader still trips over, what still reads as machine prose, and what still falls short of the best papers in the field. Our aim is prose and explanation clearly better than the typical paper in the cited literature, not merely as good.

Volume matters. A thorough return has well over a hundred separate points on the lead paper, covering every section and most paragraphs. Do not stop at the big problems; the long tail of small ones is what we cannot see ourselves.

Read as the panel described below. Each panel member has the background of the authors of a cited paper or of a named kind of reader; do not attribute opinions, quotations or reactions to any real person.

## What to look at

Cover all of the following, in whatever proportion your panel's background dictates.

1. **Clarity.** Where did you get lost, and at exactly which sentence? What did you expect at that point, and what did you need first? Which terms, symbols or objects arrive undefined, too late, or defined twice in different ways? Which hypotheses are stated without saying what they rule out?
2. **Writing, sentence by sentence.** Compare the prose with the supplied literature and the exemplar papers: openings, how a construction is introduced, how a theorem is stated, how predecessors are credited, how long an overview runs, what is left unsaid. Quote sentences that read as machine prose, padding, bureaucracy, defensive hedging, repeated contrast frames ("not X but Y"), mechanical section announcements, or a list where an argument belongs. Note every sentence you would cut and every one whose meaning you had to reconstruct.
3. **Structure and weighting.** For each section, figure, table, example, remark and appendix: what is it for, does it earn its place, is it in the right place? Where is the paper overweight (routine arithmetic, refinements, evidence bookkeeping, things its reader already knows) or underweight (the new idea, the delicate step, the intuition)?
4. **Figures and tables.** Can each figure be read at normal page size without effort? Does its caption say what to look at? Is each table a real comparison of compact entries, or prose forced into narrow columns? Would a picture explain something the text struggles with?
5. **Mathematics and credit.** Anything you believe is wrong, overstated, understated or misattributed. Check attributions against the supplied papers and what you find online. If you report an error, give the exact step and why it fails.
6. **The funnel.** Does the lead paper agree with the other two on statements, constants, names and credit? When a reader follows a link into the record or the Lean source, do they land where the sentence promised, and can they come back? Is anything essential left only in the record?
7. **What works.** What you would keep through any revision, and why. Strengths are information too.

## Use the literature, and go beyond it

`literature/` holds a *sample* of the cited and related papers chosen for your panel, with extracted text and originals; the full bibliographies are in the `.bib` files and the preprint. Read the sample closely for how the field writes. **Then search online**: arXiv, journal pages, authors' home pages, lecture notes, textbooks, surveys, talks and blog posts on query complexity, Forrelation and quantum–classical separations. Use what you find to judge how the field explains these ideas, to check credit, and to find explanations, examples or figures that do better than ours. Cite every outside source you use with a URL or identifier, and say which you read and which you only skimmed.

## How the papers are produced

We want to improve the general method as well as these papers, so that the next paper, in any field, starts better.

- `skills/` holds the writing method: how a long record is built, how the short paper and the exposition are derived from it, and the register stage that measures and line-edits every draft against its cited literature.
- `register/` holds the register stage's output for this round: the general writing rules (`REGISTER_RULES.md`, with specimens from published papers), a profile of the supplied literature, and a measurement of where each draft sits against it (`measurement.txt`). The measurement is a detector, never a verdict. Tell us where it is right, where it misses what a reader notices, and where it flags something harmless.
- `reader_principles.md` lists principles distilled from researchers who have read AI-produced mathematics.
- `exemplars/` holds papers produced by the same method for other theorems.

Wherever a problem comes from the method rather than this instance, say so, name the rule or skill that let it through or caused it, and say what the method should do instead, phrased generally enough to help a paper on a different theorem in a different field.

## State of the evidence

The formal claims were checked against their receipts before this packet was built. Do not spend effort re-verifying receipts. Do say whether the paper presents the formal evidence in a way its intended reader would understand and use. `SOURCE_STATUS.json` binds the packet to exact bytes; `LINK_MAP.json` resolves every link in the two short papers. Do not re-raise a point that `previous_round/` shows was fixed, but do say where a fix landed badly or made something worse.

{job}

## Return format

Return one ZIP containing:

1. `feedback.json`: an object with `packet` (this packet's job name), `source_sha256` (copy the `drafts` object from `SOURCE_STATUS.json`), `panel` (the perspectives you adopted, each with its anchoring paper or kind of reader and what that reader already knows), `sources_read` (literature and online sources, each marked `read` or `skimmed`, online ones with URL), and `feedback`, a list. Each item has
   - `id`: the prefix given below and a number;
   - `paper`: `exposition`, `expert_companion`, `reasoning_record` or `all`;
   - `perspective`: which panel member raises it;
   - `locator`: `section` and `quote` (an exact phrase of at most 25 words from the current Markdown), optional `pdf_page`;
   - `kind`: `unclear`, `lost_here`, `missing_example`, `missing`, `teaching`, `prose`, `structure`, `overweighted`, `underweighted`, `figure`, `funnel`, `consistency`, `credit`, `error`, `evidence_presentation`, `question` or `keep`;
   - `severity`: `critical`, `high`, `medium`, `low` or `keep`;
   - `feedback`: the complaint, question or observation, in full, in your reader's terms;
   - `why_it_matters`: what it costs that reader;
   - `advice`: what you would do about it, as specifically as you like (a direction, a structure, an example to use, a source that does it well, a short phrase); optional;
   - `outside_source`: optional URL or identifier of a source that bears on it.
2. `reading_log.md`: a running account, section by section, of reading the lead paper: what you understood, where you slowed down, where you got lost, what you expected next and what you would have needed. Write it as you read, at length.
3. `feedback_by_document.md`: a long prose critique of the lead paper (overall verdict, main problems in order of importance, what its reader takes away now versus what they should, what must be kept), followed by shorter notes on how the other two documents serve it.
4. `literature_comparison.md`: how the supplied and online literature handles the same ideas (openings, examples, figures, statements, credit), with quotations of at most 25 words and locators, and where ours falls short or does better.
5. `method_feedback.json`: problems that come from the writing method (`skills/`, `register/`, `reader_principles.md`), each with the rule or skill concerned, the instances in these documents, and what the method should do instead, stated generally.
6. `verdict.md`: at most two pages: would your panel read the lead paper to the end, the ten changes that matter most, and what must be kept.

Every item in `feedback.json` must quote the current text exactly. State which sources you actually read and which you only sampled.

{boundary}
