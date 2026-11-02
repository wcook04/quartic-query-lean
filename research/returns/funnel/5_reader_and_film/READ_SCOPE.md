# Reading and verification scope

Prepared 2 November 2026. This is the combined scope of the **AI authoring and audit team**. It records source reading, structured inspection and finite consistency checks. It is not a human review or a fresh formal replay.

All `packet:` paths below are relative to the extracted supplied archive. The separate pasted trace was also supplied by the user.

## Inputs and byte identity

The input archive is `quartic_5_reader_and_film.zip`, with packet identifier `5_reader_and_film` and repository commit `c7e0c9161f0ad898889bd9166e7b354acd42188d`. All **109** hashed members matched the size and SHA-256 in `packet:manifest.json`.

The preprint's complete 991-line extraction, `packet:paper/extracted.md`, was read by the lead, evidence, film and literature contributors. Its SHA-256 is:

```text
8b3f43c78cce1d1f56b343d3fec1b72a9389b66d3ba0cad7c279886ac9f48d3a
```

The PDF was included in the byte audit. This record does not claim a complete visual inspection of every PDF page.

## Documents read in full across the team

| Input group | Exact files and scope |
|---|---|
| Task and corpus contract | `READ_ME_FIRST.md`; `repository/README.md`; `repository/corpus/README.md`; `repository/docs/statement_evidence_contract.md`. |
| Writing guidance | All four files in `writing/`: `the-deliverable.md`, `mathematical-writing-mechanics.md`, `full-exposition-guide.md`, `register-from-literature.md`. Read by the lead and film contributor. |
| Fidelity and route reviews | `repository/docs/statement_fidelity_review.md`, `forrelation_lower_bound_blueprint.md`, `forrelation_lower_bound_review.md`, `forrelation_route_prior_art.md`. Their dates, historical states and stated exclusions were retained. |
| Exemplar papers | `exemplars/short-paper.md` and `exemplars/expository.md` read by the film contributor; all 5,659 lines of `exemplars/long-reasoning-record.md` read by the literature contributor. These supplied models of form only. No SK/QAOA theorem or checking outcome transfers. |
| Exemplar correspondence | `exemplars/short-correspondence.json` parsed in full. All ten passage rationales, treatment roles, three directed reading links and review notes were read. Repeated identifier lists were structurally inspected. |

## Corpus and formal-source inspection

The evidence contributor parsed all records in `repository/corpus/statements.json`, `ties.json`, `coverage.json`, `evidence-graph.json` and `lean_dependencies.json`. Every statement text and evidence object was inspected. Coverage counts were recalculated. Graph statement IDs/text and the supplied declared/reached sets were cross-checked against the ties. The dependency extraction was **not rerun**.

Detailed semantic comparison concentrated on the headline, winner construction, local tests, alternate-route endpoints and disputed ties. Complete tactic-level checking of the whole Lean development was not performed.

The following source files were read completely by at least one contributor:

- `repository/lean/QuarticQuery/Statement.lean`.
- `Results/Unconditional.lean`, `Results/Conditional.lean`, `Results/Headline.lean`, `Results/Exponent.lean` and `Appendix/TheoremA1.lean`, under `repository/lean/QuarticQuery/`.
- `Construction/Winner.lean`, `Construction/Transcript.lean` and `Construction/LocalTests.lean`, under the same root.
- `LowerBound/Planted/Inputs.lean` and `LowerBound/Planted/Main.lean`, under the same root.
- All five `repository/lean/QuarticCorpus/*/Solution.lean` files and their `comparator.json` configurations.
- All ten files in `repository/lean/QuarticCorpus/Negative/`.

The theorem portions of all five `Challenge.lean` files were read. Their public vocabulary was compared programmatically with the fully read `Statement.lean`, ignoring comments, section-exposure markers and whitespace; all five matched that textual test. This does not substitute for elaborated type comparison.

Relevant declarations and signatures were inspected in `ForrelationLower/Main.lean`, `Upper/Tournament.lean`, `Amplification/Bounded.lean`, `LowerBound/DirectProduct.lean`, `Forrelation/Circuit.lean` and `Tournament/Ideal.lean`. Their entire tactic proofs were not independently checked. Other implementation and imported-library proofs were used through their supplied declarations, dependency records and reviewed correspondence notes.

## Primary literature and software documentation

The literature contributor studied the first four pages and relevant proof/design sections of Bansal–Sinha v3, the five-author Aaronson–Ben-David–Kothari–Rao–Tal v1 paper, and the cheat-sheet paper v2. Selected technical reading also covered BHMT's §2 amplification calculation, Drucker's fair-algorithm and continuation-value argument, and GTW's published §1.3/Lemma 9.

The lead contributor retrieved Aaronson–Ambainis's author-hosted Forrelation paper and inspected §1.1.1, pp. 2–3, and §1.1.3, p. 4. The lead also retrieved Huang v2 in full and verified Theorems 1.1 and 1.4. These support the films' narrow historical and ingredient credits; full retrieval does not imply a complete independent proof audit.

The lead contributor read the official Lake Comparator reference, §25.1.5.8, and Lean 4.35.0 release notes. Those references were used to interpret configuration semantics. The supplied project's toolchain is Lean 4.36.0-rc2.

[sources.md](sources.md) gives exact editions, links and locators. No complete forward-citation search, audit of every proof in those papers, or priority determination for the alternative Forrelation route is claimed.

## Development trace

The separate file `Pasted text(20261102-112550).txt` contains 125,744 physical lines and 10,293,985 bytes.

The literature contributor read all 70 main visible progress notes and all twenty child progress/closeout sections. The main prompt and command outputs were inspected selectively for current status, source pins, Comparator verdicts, negative-control behavior and reader/film constraints. The evidence contributor separately inspected bounded command ranges and searched for receipt semantics.

The whole 10 MB file was **not** read line by line as a complete proof record. Historical commands in it were read as evidence and not executed. Earlier conditional or unfinished states were distinguished from the final unconditional closeout.

## Verification boundary and missing original material

This advisory performed file/hash checks, JSON consistency checks, source comparisons and worked-example calculations. It did **not** run a Lean build, `#print axioms`, an elaborated type exporter, Comparator, an external kernel or a source-diff comparison between historical commits.

The packet does not supply:

- Original Comparator receipts, raw logs or compiled proof exports.
- Compiled `.olean` artifacts or dependency checkouts.
- The source Git history.
- The repository Makefile or `tools/build_corpus.py`, `tools/build_challenges.py`, `tools/run_comparator.py`. A readable portion of the runner appears in the trace.
- Historical scratch scripts, annex files and numerical outputs referred to by earlier reviews but omitted from this packet.

The trace records the paranoid unconditional receipt at source commit `d42fb67a7e060fb5386867dadf20a5903df39141`, followed by the final packet at `c7e0c9161f0ad898889bd9166e7b354acd42188d`. Its reports are evidence of recorded observations; missing originals prevent a fresh authentication of those runs here. A public final Lean-repository pin was not independently established.

These limits concern the strength of the evidence labels. They do not prevent preparing the requested advisory explanation, correspondence, map, data contract and scripts. No independent human mathematical review or human comprehension study was performed.

