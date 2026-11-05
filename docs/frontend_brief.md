# Designing the Quartic reader

Build the first usable interaction around a mathematician opening Theorem 1.1 in OpenAI’s paper and asking “Does Lean prove this whole statement?” Keep the theorem in view while they inspect the answer. Someone arriving fresh should also have a natural starting point: the four-by-four board in our general exposition, where they can see what a query reveals before meeting the formal definition.

## Start with the two working readers

| Open this | Try this interaction | Adapt this implementation |
| --- | --- | --- |
| [Proof Reader, already open at a linked passage](https://wcook04.github.io/proof-reader/#/contextual-embeddings/@isoR-clam) | Switch between Graph and Lean while keeping the selected sentence in place. Follow a declaration and return to the passage. Give each such selection a shareable address. | [Paper and selection panes](https://github.com/wcook04/proof-reader/tree/e2df8880a892cc13ece046709f649c1860487b00/web/src/paper), [proof modes, source and fidelity components](https://github.com/wcook04/proof-reader/tree/e2df8880a892cc13ece046709f649c1860487b00/web/src/proof) |
| [SK Exposition](https://wcook04.github.io/lean-exposition-site/) | Start at the mathematical question, choose an account for your background, then compare what the printed theorem and the formal result each say. | [Audience entrances](https://github.com/wcook04/lean-exposition/blob/ed08df83416d8bfb23d02038b43dd3a5bd457795/site/src/home/LevelsBand.tsx), [statement comparison](https://github.com/wcook04/lean-exposition/blob/ed08df83416d8bfb23d02038b43dd3a5bd457795/site/src/compare/StatementSlice.tsx), [reading-position restoration](https://github.com/wcook04/lean-exposition/blob/ed08df83416d8bfb23d02038b43dd3a5bd457795/site/src/app/restore.ts) |

Use Claude’s installed `~/.claude/skills/frontend-design/SKILL.md` for typography, spacing and hierarchy. Give the paper comfortable line lengths and equations enough room. Use `visual-explanation-authoring` when adapting the upstream panes and the figures already cited by the Quartic manuscripts. Preserve upstream license notices when reusing code. Use `webapp-testing` for the browser walkthrough below. The public design and testing skills are available from [Anthropic’s frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) and [webapp-testing](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md).

## Give readers a way in

In the first 20–30 seconds, help a visitor understand what the separation measures, what quantum queries can buy, and where to start. Use the edition’s authored `entrances` for the question, preview and first stops. Offer the general exposition for learning the construction, the expert paper for its decisive steps, the reconstruction for following the full argument, and the original PDF for checking OpenAI’s wording. Credit the Quartic project for the Lean. List the verification supplement with the reconstruction. Show a video or chapter link only when the edition supplies one.

## Wire the paper before styling the graph

Use the [reading API](reading_api.md#resolve-a-paper-selection) to open one immutable edition through the client bundled with the frontend. Start from the existing export if available, or run `make reading-web` in a full checkout with Pandoc. Serve `build/reading-api` as static files. Resolve assets through the manifest relative to its URL, including when hosted under a subdirectory. Fetch `reading.json` for the paper list, entrances and downloads. Keep the edition permalink, paper ID and selection ID in shared links. On an edition mismatch, let the reader reopen the cited edition. Populate the switcher from the edition’s paper IDs and use its supplement IDs separately. On manuscript revisions, run the [binding audit](reading_api.md#revise-the-papers-and-retain-earlier-readings) before promoting the new edition.

| When the reader… | Use the backend this way |
| --- | --- |
| Opens a paragraph | Call `reader.resolve({paper, id})`. Render the source passage, its real figures and links. A free text range requires the document hash and source lines. For the original PDF, use its named destination or physical page. A page-only location supports a page jump. |
| Asks what Lean proves | Call `reader.statementReview(statementID)`. Place the published location, reviewed ledger wording and leading comparison together. Use the returned reviewer note, relation, proof route and raw Lean. Keep the full type, hypotheses, transitive axioms and any concrete checked example within reach. Distinguish an older ledger description from a quotation of the paper. |
| Follows the proof | Start from the selected declaration and expand nearby `uses` or `used_by` edges on demand. Use `reader.fromDeclaration(name).then(r => r.treatments)` for links back into the papers. Label formal dependencies as reported by Lean and passage associations as editorial. Render authored application explanations from `reader.journey(id)`. Highlight an exact source occurrence only when that use carries `exact_source_occurrence`. |
| Switches accounts or goes Back | Offer the returned related selections or topic treatments, with the passage’s role. Retain the reader’s selected passage, open mode, scroll and keyboard focus. On a phone, let them open the proof as a separate view with a visible return to the same sentence. |

Keep uncertainty local to the control it affects. For unmapped prose, keep the paper readable. For a partial match, show what the declaration covers. For missing axiom evidence, say “No axiom report for this declaration.” Reserve an empty axiom list for a current inspection that actually returned one. When an inspection is stale, keep its historical status visible and use the source for the chosen edition. Treat semantic examples as checks of their stated cases. A paper-wide verification percentage cannot be derived from the number of links.

Use the [browser edition](reading_api.md#browser-edition) for the actual UI. Bundle `openEdition` with the app, load the prepared HTML with `manuscript()`, load its figure resources with `figure(paper, path)`, and persist the `position` that `resolve()` returns. The edition supplies the board scenarios, predictions and opening passage. Keep the known one-query decision, unknown-board certificates and enlarged-board pointer check distinct.

## Walk through these before calling the frontend ready

Run these against the real edition to see the expected responses. Then perform the same actions through the UI at desktop and phone widths, using both pointer and keyboard.

```sh
manifest=build/reading-api/v1/index.json
node tools/query_reading_api.mjs "$manifest" --statement thm-1.1
node tools/query_reading_api.mjs "$manifest" exposition exposition/joint-event/0
node tools/query_reading_api.mjs "$manifest" --journey capped-predictor
node tools/query_reading_api.mjs "$manifest" --statement def-R
```

1. **Check the headline.** Open the original on page 1. The full family theorem is the exact match. The shorter theorem proving only the exponent is partial. Open raw Lean, follow one dependency, return, and reload the shared link. The same theorem and paper location should be selected.
2. **Understand a proof step.** From the exposition’s capped-prediction paragraph, show why visiting the true cell while the column is light implies a correct address prediction. Open equation (21) on page 13 of the original. The reader should see that the proof averages over the original independent inputs while lightness stays inside the event.
3. **Try to break a definition.** From the randomized-query definition, open the one-bit identity example. The reader should be able to explain why choosing an algorithm after seeing the input changes the answer, and inspect the Lean that checks the example.
4. **Try a gap.** Open page 19 of the original. The PDF should still open when the page has no indexed claim. Test a missing optional download, a stale selection and an unavailable proof resource. Preserve the paper and give a usable return path.

Check focus after closing the proof, readable math at narrow widths, a keyboard-accessible list of graph neighbours, and whether a direct link works in a fresh tab. In the general exposition, follow a citation into the bibliography, then follow a numbered footnote and its backlink. Open a real manuscript figure from a nested deployment URL. Keep the reader’s paper selection throughout. Capture the actual headline comparison on desktop and the passage-to-proof round trip on mobile for review.
