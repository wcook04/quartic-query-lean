**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

# Source and evidence audit

## Conclusion

The complete Forrelation lower-bound source and its semantic bridges were read. No mathematical error, hidden hypothesis, vacuity, or incorrect promise bridge was identified in that route. The one-block Stein argument and the elementary bounded-bias growth proof are supported by complete source proofs. This conclusion is a mathematical source inspection, not a new kernel verification. The new quantitative endpoints in `note.md` were checked independently as paper arguments; their remaining formal work is listed in `LEAN_GAPS.md`.

The supplied manifest gives repository pin **`c7e0c9161f0ad898889bd9166e7b354acd42188d`**. All **123 manifest-listed files** were checked against their recorded byte sizes and hashes; every listed file matched and none was missing. The archive has two further members, `READ_ME_FIRST.md` and `manifest.json`. This verifies consistency with the supplied manifest. It does not independently authenticate a remote Git object. [Source: supplied `manifest.json`.]

Neither `lean` nor `lake` is installed in this environment. No new compilation, axiom check, Comparator run or external-kernel replay was performed. The supplied `lean-toolchain` specifies `leanprover/lean4:v4.36.0-rc2`; downloaded project dependencies, compiled `.olean` artifacts and the standalone `corpus/receipts/` directory are absent from the packet. Historical evidence remains distinguishable from a reproducible fresh run. [Sources: `repository/lean/lean-toolchain`, archive inventory, `repository/corpus/README.md`.]

## What the source theorem actually says

`QuarticQuery.ForrelationLower.bansalSinhaLower`, at `repository/lean/QuarticQuery/ForrelationLower/Main.lean`, line 506, proves `QuarticQuery.BansalSinhaLower` without a mathematical premise. The latter definition quantifies over each fixed natural `k >= 2`, then supplies an eventual threshold in `t`. Its dimension is `mValue t = 2^(2t) = 4^t`; its lower bound is the natural floor of `m^(1-1/k)/(log_2 m)^2`. The error convention in `RLe` and `R` is at most `1/3`. [Source: `repository/lean/QuarticQuery/Statement.lean`, declarations `mValue`, `RLe`, `R`, `Lvalue`, `BansalSinhaLower`.]

The promise is one-sided at the positive threshold: true when `Phi >= 2^(-5k)`, false when `abs Phi <= 2^(-5k-1)`, and undefined otherwise. Large negative values are unpromised. `Phi_eq_PhiF` and the lemmas `P_yes` and `P_no` connect these exact public definitions to the internal real polynomial used in the proof. [Sources: `Statement.lean`, definitions `Phi` and `P`; `ForrelationLower/Promise.lean`, line 482; `ForrelationLower/Main.lean`, initial promise lemmas.]

The complexity definition is nonvacuous. The classical model constructs a tree that reads all coordinates, proves `RLe_set_nonempty`, and obtains `RLe_R` and `lt_R_of_not_RLe`. Thus the proof cannot obtain its lower bound from an empty set of feasible algorithms. `RandomizedProgram.depth` bounds every tree in its finite positive-weight support, and repeated queries are charged. [Sources: `Model/Classical.lean`, lines 231–308; `Statement.lean`, definitions of `RandomizedProgram`, its `depth` and `success`.]

The `namespace QuarticQuery ... end QuarticQuery` public-vocabulary body in the unconditional Comparator challenge was compared byte for byte with the corresponding body of `Statement.lean`; they match. This inspection supports fidelity of that frozen body. It is not a substitute for rerunning Comparator. [Sources: `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`; `repository/lean/QuarticQuery/Statement.lean`.]

## Main declaration locations

Paths in this table are relative to `repository/lean/QuarticQuery/ForrelationLower/`. Names have prefix `QuarticQuery.ForrelationLower.` unless stated otherwise.

| Step | Source declarations |
| --- | --- |
| Cube calculus | `Cube.lean`: `hasDerivAt_ext` (line 221), `D_D` (247). |
| Bounded Stein identity | `Stein.lean`: `hasDerivAt_phiS` (76), `stein_one` (137), `stein_pi` (268), `integral_reflect` (306). |
| Bias and one-direction walk | `Walk.lean`: `abs_wv_le_half` (152), `EarlyOnly` (317), `integral_walk` (364), `hasDerivAt_ext_s` (436). |
| Global identity and paths | `Walk.lean`: `exists_identity` (461), `Int_eq_paths` (541), `abs_cf_le` (556). |
| Uniform zero endpoint | `Cascade.lean`: `integral_ext_wv_zero` (256). |
| Distinct coordinate paths and advantage | `Cascade.lean`: `Lpath_nodup` (354), `Lpath_inj` (362), `advantage_le` (384). |
| Adaptive-tree growth | `TreeGrowth.lean`: `hit_azuma` (414), `hit_chaos_le` (514), `ext_Dl` (690), `sum_abs_ext_Dl_le` (738). |
| Positive hard mean | `Promise.lean`: `psi_dphi_ge` (271), `Phi_eq_PhiF` (482), `mass_ge` (499). |
| Uniform moments | `Promise.lean`: `ext_PhiF_zero` (559), `ext_PhiF_sq` (564). |
| Error reduction | `Amplify.lean`: `exists_amplified` (80). |
| Finite gap and eventual endpoint | `Main.lean`: `not_RLe_of_gap` (81), `exists_threshold` (347), `bansalSinhaLower` (506). |

The generated dependency record marks these key route declarations as declared and reached from the unconditional headline roots. This is recorded dependency evidence from a previous compiled environment; the closure was not recomputed here. [Source: `repository/corpus/lean_dependencies.json`.]

## What the proof inspection resolved

The Stein walk explicitly controls accumulated factors through `EarlyOnly`. On entering a Gaussian layer, differentiating the already differentiated cube coordinate gives zero by multiaffinity. The remaining terms move one derivative to the next input block. Earlier weights depend only on earlier Gaussian layers, so subsequent differentiations do not create omitted terms. Boundedness and differentiability hypotheses are supplied before each application of Stein. [Sources: `Walk.lean`, `integral_walk`, `hasDerivAt_ext_s`, `exists_identity`; `Cube.lean`, `D_D`.]

The generic matrix orientation in the source is `V(b) = sum_a H(b,a) U(a)`, producing `H(p_(r+1),p_r)` along a path. The blueprint's display reverses these two indices. Walsh symmetry makes the difference immaterial for the public target. `note.md` consistently uses the source orientation in its general orthogonal-matrix statement. [Sources: `Walk.lean`, `Vc` and `cf`; `repository/docs/forrelation_lower_bound_blueprint.md`, path identity.]

The tree-growth argument retains the queried-coordinate set and treats repeated queries through their already determined answers. Its maximal inequality stops before an increment loses its bound; it does not condition on a future event and then assume martingale behavior remains valid. The injectivity needed to sum derivatives over distinct sets is proved for the path family. [Sources: `TreeGrowth.lean`, `walk`, `hit`, `hit_azuma`, `hit_chaos_le`, `sum_abs_ext_Dl_le`; `Cascade.lean`, `Lpath_nodup`, `Lpath_inj`.]

The hard law is never assumed to be supported on the promise. The source derives pointwise comparisons between the acceptance probability, `Phi-delta`, and `Phi^2`, then averages them. Amplification uses `2 tau` independent runs with error at most `(8/9)^tau`. These facts explain both the promise exception term and the depth multiplier in the final inequality. [Sources: `Main.lean`, `not_RLe_of_gap`; `Amplify.lean`, `exists_amplified`.]

The paper strengthens several exact statements: its coefficient constant is `3/16` instead of the source's `3`; its identity is an integral form instead of the source's mean-value form; its general-matrix moments extend Walsh-specific declarations; and its new endpoints are uniform in `k`. The sharper endpoint additionally uses SSW Fourier growth, absent from these Lean modules. These are explicit formal gaps, not evidence of a defect in the old endpoint. [Sources: declarations above; `note.md`, equations (3), (4), (7), (12), (16)–(18); `LEAN_GAPS.md`.]

## Historical execution evidence

The separately attached raw trace, `Pasted text(20261102-112548).txt`, contains repeated nested command histories and intermediate failed states. Its final visible progress record `N069` reports the completed unconditional development and the final local checks. Earlier reports that the root build remained outstanding were superseded by later outputs. The following locators are physical lines in the supplied raw text; they identify historical tool output, not newly executed commands.

| Trace locator | What the record supports |
| --- | --- |
| Lines 43691 and 43740 | Axiom output for `QuarticQuery.ForrelationLower.bansalSinhaLower` lists only `propext`, `Classical.choice`, and `Quot.sound`. |
| Line 43741 | An applied headline theorem is reported with the same standard axiom list. |
| Lines 7437–7441 | All five positive Comparator bundles report exit 0. |
| Lines 7446, 7461, 7475 | One negative-control runner initially reports `WRONG FAILURE`: its matcher expects `does not match`, while the actual diagnostic says `statement do not match`. The actual theorem mismatch is present, and the corrected runner reports `rejected as expected`. This is a diagnostic-matching defect, not evidence that the wrong solution was accepted. |
| Lines 8145–8146 | The unconditional comparison reports exit 0 and `paranoid_rc=0`. |
| Lines 8159 and 8171 | The final replay record is committed as `c7e0c91`, and the final packet pin is recorded. |

The README describes the Comparator runs as **unsandboxed local rehearsals**. The packet references a receipt directory but does not include it. It also does not include the compiled artifacts needed to replay those checks here. The proper conclusion is that source and recorded outputs support the stated historical checks, with replay still outstanding in this environment. No public release or human review is established by this audit. [Sources: `repository/README.md`, evidence table; `repository/corpus/README.md`; raw trace final progress record `N069`.]

## Corpus metadata repair

In `corpus/statements.json`, the `lem-2.1.i` record locates `QuarticQuery.ForrelationLower.bansalSinhaLower` as `kind: definition`, `file: lean/QuarticQuery/Statement.lean`, `line: null`. The actual declaration is a **theorem** in `lean/QuarticQuery/ForrelationLower/Main.lean`, line **506**. `Statement.lean` contains the proposition `BansalSinhaLower`, not the theorem proving it.

Repair the declaration locator and kind while preserving the statement identifier and its mathematical text. The relation of the theorem to the fixed-`k` claim is exact. This is a metadata correction, not a strengthening or weakening of `lem-2.1.i`. [Sources: the cited corpus record; `Main.lean`, line 506; `Statement.lean`, line 319.]

## Reading coverage and limits

**Complete source reading for this audit:** all eight `ForrelationLower` modules (`Cube`, `Stein`, `TreeGrowth`, `Walk`, `Cascade`, `Promise`, `Amplify`, `Main`); `Statement.lean`; `Model/Classical.lean`; and `Forrelation/Walsh.lean`, `Forrelation/Product.lean`, `Forrelation/Promise.lean`. These are thirteen Lean source files.

**Complete supporting-document reading:** `READ_ME_FIRST.md`; repository README; statement evidence contract; corpus README and coverage record; the lower-bound blueprint and review; the unconditional Solution, Comparator configuration and Results file; Lake configuration, manifest and toolchain. The unconditional Challenge's public-vocabulary body and its endpoint statements were read, and its public body was compared as described above. The full draft of `note.md` was read and its displayed mathematical calculations were independently checked.

**Structured and targeted inspection:** all manifest entries were verified; corpus statements, ties and dependency data were parsed, and relevant Forrelation records were read in full. The entire raw trace was indexed for section boundaries, route-related declarations, build outputs and final status. Its main visible-progress section was read in full, together with the relevant lower-bound and Comparator outputs. Repeated unrelated nested proof histories were not read as if they were distinct final source files.

**Separate coverage by the coordinating review:** the supplied preprint's `paper/extracted.md` and all four writing guides were read in full. The exemplar papers concern a different theorem and were sampled for presentation; they did not receive a full proof review. This broader reading is separate from the thirteen-file module audit above.

**Outside this source audit:** complete proof review of the other branches of the nearly quartic separation, exhaustive rereading of unrelated nested traces, and the literature/exemplar review assigned to the research work. The prior-art record provides the separate literature search coverage. No source named in the first coverage paragraph was inaccessible. Missing executable dependencies, compiled artifacts and standalone receipts are evidence limitations, not unread supplied sources.
