# Round-nine manuscript revision

This revision starts from `7772e4f2b98149a38ed69b88397982620f94bdac` and
assimilates all three [preserved returns](../returns/round9/README.md). Original
findings remain unchanged. Manuscript decisions belong to the three per-document
disposition files; method decisions have their own record. One repaired passage
may resolve several findings, but each finding receives its own decision.

The work is editorial: clarify the scope, prove the displayed intermediate
inferences, make algorithms executable from the description, and repair source
and reading links. It changes no Lean theorem or definition. A fresh PDF is not
a fresh proof check, and neither the returned simulated reviews nor our revised
reading pass is evidence of human comprehension.

## Evidence retained

The [intake validation](round9_intake_validation.json) records three original
archive CRC/hash checks and reruns of the supplied artifact and finite-example
checks against the original round-nine packets. All submitted members have
custody hashes. The complete Markdown coverage claims coexist with the stated
chronology and visual-coverage limitations; see the returns guide.

The previous round's `xor_exhaustive_16_inputs.new_total = 1/4` is a historical
record, not the current answer to the whole-run-lightness variant. When the
extra query makes a branch heavy, that branch is removed in its entirety from
the joint event. The round-nine exposition correction and its exact check
supersede that reading of the earlier receipt; the earlier file is preserved.

## Source and method

The three revisions apply the maintained `lean-exposition` stage methods to
their different readers. Writing literature guides what to explain and where;
it supplies no mathematical proof or empirical reader result. The per-document
revision notes identify inspected source passages and the resulting edits.

The [method dispositions](round9_method_revision.json) preserve all 48 method
findings, their individual decisions, transfer cases and limits. The existing
writing-method owners were refined upstream. The local
[writing guide](../../docs/writing_method.md) applies those refinements to the
quartic manuscripts. A packet-specific relocation defect was repaired in
`tools/build_round9_packets.py`: the source guide remains unchanged at its
repository path, while the compatibility copy receives valid rebased links and
the existing source-closure procedure includes their targets. Seven focused
builder tests, including the missing/escaping-target cases, passed. The sent
round-nine packets were not rebuilt or altered.

The source-link rebind also covers whole-document record links, which the
previous anchored-link pattern missed. A focused regression checks both forms
and still rejects absent anchors. During authoring, the full link test detected
stale generated label blocks after cited labels changed; regeneration is part
of final integration, rather than a claim that intermediate prose is current.

Final source validation found a version-bound renderer test still expecting the
previous record's 365 authored anchors and 327 internal links. The revised
record has 366 anchors and 359 links; the renderer resolves them and preserves
the source bytes. The fixture is refreshed for this reviewed edition, retaining
its actual LaTeX-destination and source-immutability assertions.

## Implemented revisions

The [synthesis index](round9_synthesis.json) accounts for all 538 current
manuscript findings without duplicating their individual reasoning. Read the
[expert decisions](round9_dispositions/expert_companion.json),
[exposition decisions](round9_dispositions/exposition.json) and
[record decisions](round9_dispositions/reasoning_record.json) for the returned
baseline quotation, verdict, explanation and exact current quotation/line span.
The same owners separately retain 287 prior-audit and supporting observations;
these are not 287 newly discovered defects or independent reviews. Three record
cross-document summaries and the exposition's four packaging/source observations
retain their narrower roles.

The [expert revision note](round9_expert_revision.md) explains the locally
complete tournament statement, explicit growing-parameter allowance and tighter
source attribution. The [exposition note](round9_exposition_revision.md) records
operational quantum states, the bounded sampler, simulator clocks and revised
exercises. The [record note](round9_record_revision.md) explains the full
probability-law and model transitions and the current formal-status account.
Each note identifies actual literary or mathematical exemplar passages and the
specific editorial decisions they informed.

The final reading links use source edition
`8357f268732746d1575e05e7de8c888e20ad3793`. A receiving source review caught an
overstatement in the expert trace description: the cited record trace shows
stopping before the second target query, while the later-heavy variant belongs
to the exposition exercise. The link label now promises exactly the operation
its destination supplies. This narrowed sentence was committed before choosing
the final link edition. Generated correspondence retains the older review's
edition boundary and does not silently extend that review to revised prose.

The [validation receipt](round9_validation.json) binds final source hashes,
repository checks, PDF hashes and inspection coverage. All 225 tracked Lean
files remain byte-identical to the recorded paranoid Comparator revision
`9a0a5cdace28594058f6df59b9b2e45a9e7c1a4f`. No new Lean or Comparator run was
needed or claimed for these editorial changes. No next-round review packets
were built.
