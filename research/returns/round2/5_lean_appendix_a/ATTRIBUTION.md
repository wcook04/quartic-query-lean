# Attribution and licensing

The mathematical Appendix A under review belongs to the supplied OpenAI preprint, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, dated 5 October 2026. The prior mathematical results are attributed in `references.bib` and at their precise uses in `blueprint.md`.

The new Lean files were produced by AI agents under the task's stated direction. No human review or successful new elaboration is represented. The proof of the universal quartic bound is not claimed as a new mathematical result.

Portions of the wrappers, Fourier-fiber argument and maximal-support reasoning adapt proof text from complexitylib revision `62ca5c21461b2482e8bd12b7cb9b4937d887a33a`. Relevant upstream source headers identify:

> Copyright (c) 2026 Samuel Schlesinger.
> Released under Apache 2.0 license.

The included `LICENSE` is copied from that revision to retain the upstream terms. The returned source modifies namespaces and function vocabulary, splits intermediate statements, supplies explicit bridges, and adds independent proofs for the general adversary matrix, literal star construction, recursive signed cube and its transport. These modifications are identified here and in file comments. No upstream endorsement is implied.

Mathlib and cslib declarations are imported at the pinned revisions; their source is not bundled wholesale. The original paper PDFs, annex archives and source repositories are not redistributed in this ZIP. Their exact source URLs and the content hashes needed to identify reviewed material are recorded in the bibliography and source manifest.
