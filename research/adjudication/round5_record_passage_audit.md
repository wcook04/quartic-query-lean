# Round-five record revision: passage meaning audit

Scope: the 36 `text_changed` and 6 `added` passages in
[round5_record_rebind.json](round5_record_rebind.json), compared with
`git show HEAD:docs/reasoning_record.md`, plus the new Reading guide and §2.9
tables. Each passage's verdict is in
[round5_record_passage_audit.json](round5_record_passage_audit.json). Results:
29 editorial, 9 correction, 4 regression.

Sources checked: the preprint text (`source_packet/paper/source.pdf`), the
Comparator configs at `659b571`, the receipts in `corpus/receipts/`,
[round4_formal.md](round4_formal.md), `corpus/ties.json`,
`corpus/lean_dependencies.json`, and the round-five referee files.

## Regressions

1. **R3-01-QUANTIFIERS (line 86): a hypothesis was dropped.** The old text
   began "For sufficiently large m" and raised a positive inequality to a
   nonnegative power. The new text states
   $1+Q\le(1+C_k)\sqrt m(\log_2m)^{b_k}$ with no condition on $m$. Fix: add
   "For sufficiently large $m$" and "the positive inequality … to the
   nonnegative power $\alpha$".
2. **upper-purpose (line 2125): the preprint is quoted too strongly.** The
   new text says the preprint "singles out these two … as the most relevant
   recent work". Preprint §1.1, p. 2, says only that "their comparison-based
   viewpoint is particularly relevant here". Fix: "identifies these two
   certificate-complexity separations as recent work whose comparison-based
   viewpoint is particularly relevant".
3. **history-construction-evidence (added, line 6117): an old claim of direct
   comparison now sits in an added passage.** The passage says the
   Construction receipt "compares the four source theorems … together with
   their checked wrappers". The config lists only the four `Checked.*`
   wrappers, and the 3 November receipt has `configured_theorem_names_only`.
   Under the record's own F.1 policy, the source theorems therefore have
   wrapper-mediated credit only. Fix: name the configured `Checked.*` wrappers
   and call the source theorems wrapper-mediated.
4. **forr_advantage: a claim marker moved and the bindings were not updated.**
   `NEW-FOR-19` moved, intact, into `forr_historical_threshold` (Appendix D).
   The (F33)⇒(F34) step checks. However, the rebind says "Claim lists are
   unchanged", and `reasoning_record_correspondence.json` `passages` still
   places NEW-FOR-19 under forr_advantage. Fix: record the move in the rebind
   and in the correspondence passage lists.

## Corrections verified

- CAT-def-Sf and CAT-thm-A.1: the link labels are fixed.
- CL-selection-independence-example: $(3/4)^4=81/256$ is correct.
- forr_bs_mismatch: $L\to\Lambda$ is applied consistently.
- ROOT-REFERENCES and upper-purpose: the AIK2026 entry matches preprint ref. [5].
- forr_credit: the BS/SSW rorrelation distinction is supported by referee
  LR-011 and SSW §1.8.
- forr_validation_scope: Comparator compares
  `Checked.forrelation_lower_bound`, and `bansalSinhaLower` gets no separate
  credit. The config and receipts confirm this.
- CL-literature-and-verification: `direct_product_external_finite_realized_caps`
  is limited to a finite seed space, with a joint-event bound $\beta^r$, as
  round4_formal states.
- upper-missing-physical-state: the scope of `uniformOpaqueAmplifier`, and the
  gaps still unproved, match round4_formal.

## Reading guide and §2.9

No status claim lacks support. The Unconditional config names exactly the four
configured targets, and receipt T033042 accepted exactly those four. The type
of `theorem_one_one` is as described, with the integer floor form, an
existential $b$ and quantifier order ∀k ∃S,A,b,t₀ ∀t ∃C. The rows for
uncompared statements are right. The "review not current" marks match the
missing `review_binding` fields in ties.json.

Two statuses are understated:

- Lemma 2.2 and `eq19_whole` were accepted again on 3 November at `9a0a5cd`
  (receipts `*-2026-11-03T120058951138`), and Unconditional passed a paranoid
  run then (T121735). Neither §2.9 nor Appendix F mentions these runs.
- The Theorem A.1 row should name its wrapper, `Checked.universal_quartic_bound`.

## Minor wording in moved history

Appendix F passages still say "the current integration" for the 2 November
runs. history-exponent-evidence has a dangling "all these names". The
AC-evidence pointer says §2.9 summarizes the construction statements, but §2.9
lists only Lemma 2.2. forr_repetition no longer derives $5/2<e<11/4$, which
loses completeness but changes no claim.
