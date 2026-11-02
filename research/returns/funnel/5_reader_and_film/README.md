# The reader’s map and the film

**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

This ZIP contains the requested explanation design for OpenAI’s nearly quartic separation. Start with `levels.md` for the five levels of exposition. The film scripts use one exact four-column instance, then make an explicit switch to the general hard distribution when explaining the lower bound. The source preprint and its full Lean snapshot remain in the original supplied packet.

## Deliverables

| File | Purpose |
| --- | --- |
| `levels.md`, `levels.json` | One sentence, one paragraph, one page, argument map entry, paper reading route, and reasons for the level of detail. |
| `argument_map.json` | Existing corpus nodes, unchanged evidence fields, support reasons, collapsed dependency paths, difficult steps and alternative routes. |
| `fidelity_view.md` | Sentence-to-source interaction with separate exact paper text, normalized corpus text and complete Lean source type. |
| `film_12min.md`, `film_4min.md` | Complete spoken scripts and exact shot pictures, with planned timings and source identifiers. |
| `film_shots.json`, `visual_data.json`, `checking_visual_data.json` | Structured shots, exact worked-example data, and actual source snippets for the checking film. |
| `worked_example.png`, `worked_example.svg` | A precise reusable diagram of the running example. |
| `data_contract.md` | Source joins, missing fields, disagreement handling and interpretation rules. |
| `correspondence.json` | Exact anchored passage boundaries, roles, corpus IDs, declaration names and proposed example IDs. |
| `NEW_STATEMENTS.json`, `NEW_STATEMENTS_README.md` | Proposed finite Lean signatures and their shared import context; all uncompiled. |
| `LEAN_GAPS.md`, `LEAN_GAPS.json` | Reading-order limits, partial suppliers, alternative proofs and new example obligations. |
| `STATEMENT_CHANGES.json` | Empty: no existing mathematical statement has been changed. |
| `AUDIT_FINDINGS.json` | Concrete correspondence, locator and run-provenance findings. |
| `sources.md`, `source_manifest.json`, `READ_SCOPE.md` | Primary citations, exact editions, source pins and honest reading/checking boundaries. |
| `checks/check_return.py`, `checks/validation_report.json` | Reproducible structural and finite arithmetic checks. These do not run Lean. |

## Decisions that govern the design

The opening example emphasizes why a winner survives arbitrary rival behavior: every incoming pointer lands on a one, while its own verified cell points to a zero in each rival. The tournament needs complementary comparison probabilities and a dominant candidate, with no ordering among losers. Its quantum implementation must preserve the successful label distribution. The classical proof is explained through the erased zero, the filled cell and the capped simulator's joint event. These are the steps where compression can remove an essential hypothesis. [OpenAI, §§2.2, 3.1–3.3, 4.1–4.2; corpus IDs in `correspondence.json`.]

For each fixed k, the separation power is 4−2/k up to logarithmic factors. To exclude a proposed exponent below four, choose k first and then grow m. The earlier universal quartic upper bound is credited to Aaronson, Ben-David, Kothari, Rao and Tal, Theorem 2. The four-column example is a construction witness, with L=0, and makes no finite speedup claim. [OpenAI, Theorem 1.1 and §5; `sources.md`; `NEW_STATEMENTS.json`.]

The supplied record reports an unconditional Lean theorem and successful local Comparator checks. This return inspects the source and recorded evidence without replaying Lean or Comparator. An exact tie for `claim-bs-to-L` points to a different endpoint theorem and should not produce a checked badge. The current headline is distinct from the older conditional declaration. Expected rejection of a wrong solution is distinct from acceptance of a proof. Original receipts are absent, and the receipt commit differs from the final packet commit. These findings concern the displayed evidence; this audit does not identify a defect in the headline theorem. [`AUDIT_FINDINGS.json`; `READ_SCOPE.md`.]

## Reproducing the local checks

Run from the extracted return directory:

```bash
python checks/check_return.py --packet /absolute/path/to/extracted/original/quartic_packet
```

The standard-library checker validates the links, copied evidence, source snippets, timings and finite example. It verifies the original packet against its supplied manifest and reports its own limits. It requires no Lean installation. The raw mathematical source and metadata are read, never modified.
