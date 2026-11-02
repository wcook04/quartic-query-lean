## Your job: the sharp uniform Forrelation lower bound, ready to formalise

The first-round route note (`previous_round/4_forrelation_route_note/`) proved on paper that our single-block argument gives a randomized lower bound for k-Forrelation uniform in k: elementary constant 2/18225 with denominator k^2 ln(4km) for m >= 2^(15k+2), and, with the Sherstov-Storozhenko-Wu Fourier estimate, no explicit inverse polynomial in k. Our Lean development now contains `lean/QuarticQuery/ForrelationLower/Uniform.lean`, which targets the coarser constant 1/2332800 from the existing lemmas (see `BUILD_STATUS.md` for whether it is built). Your job is to make the sharp results checkable and to settle what they mean.

1. Reconstruct the elementary proof of the 2/18225 bound independently from the note and the Lean source, at the granularity of Lean lemmas: the sharp kernel product psi(x) dphi(y) <= 3/16, the intermediate-block bias 1/4, the logarithmic specialisation of the growth bound, variable-error amplification, the exact promise gap with p = (a - delta)/(1 - delta) and q = min(1, 4/(m delta^2)), the uniform padding estimate, and the final arithmetic. For each lemma give the exact statement, a complete proof, and a Lean signature over the existing declarations in `ForrelationLower/`. Check every constant numerically with exact rational arithmetic in a standard-library script.
2. Decide what the strongest clean statement is. Is the threshold m >= 2^(15k+2) necessary for the argument, or an artefact? What is the best exponent of the logarithm this route gives? Compare, with exact formulas, against Bansal and Sinha (Theorem 1.3 and the Section 5.4 finding in `repository/research/adjudication/`), Sherstov-Storozhenko-Wu, and Tal.
3. Bansal and Sinha Section 5.4: two readings found that the inequality at main.tex line 1181 fails for k >= 3. Verify or refute this from the TeX in `literature/`. Then determine whether their stated Theorem 1.3, with denominator log(kN)^(1-1/k), can be recovered by a different argument (for example a level-by-level treatment, a different growth bound, or our single-block identity, which uses only level k). Either prove it or state precisely what blocks it.
4. Restriction transfer: the note's sharp route needs a coordinate-dependent version of Wu's restriction identity (`literature/` holds Wu's paper). State and prove the exact version needed.

## Return one ZIP containing

- `note.md`: the mathematics, with `<!-- passage:NAME -->` anchors; `references.bib`.
- `lean_blueprint.md`: the lemma-by-lemma plan with signatures, in dependency order, naming the existing declarations each one uses.
- `checks.py` (standard library, exact arithmetic) and `checks_output.txt`.
- `bansal_sinha_section54.md`: the verification and the repair attempt.
- `correspondence.json`, `NEW_STATEMENTS.json`, `STATEMENT_CHANGES.json`, `LEAN_GAPS.md` as specified above.
