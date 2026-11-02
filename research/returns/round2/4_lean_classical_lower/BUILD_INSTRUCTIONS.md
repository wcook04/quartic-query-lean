# Pinned compilation and statement review

## Current status

All four new Lean modules are **unelaborated**. This environment had no `lean`, `lake`, or `elan` executable on `PATH`. No build command below was run. The scripts in `checks/` are separate exact arithmetic and package-integrity checks; they are not Lean tests.

## Pins

Use the supplied project's existing dependency files without updating them.

| Component | Pin |
| --- | --- |
| Project snapshot in the supplied manifest | `4c7544f8dcdfc18d3ecf8476ebd8c1090cd46f15` |
| Lean toolchain | `leanprover/lean4:v4.36.0-rc2` |
| Mathlib | `69552756cd8a2d2d48763cf7279fd814d6a1224d` |
| complexitylib | `62ca5c21461b2482e8bd12b7cb9b4937d887a33a` |
| cslib | `254e30e6d4299c51323aaeaf5f51a4763b375d4a` |

Copy the four files under `lean/QuarticQuery/Paper/` into that module directory in a separate checkout or review branch. The archive does not replace `QuarticQuery.lean`, `lakefile.toml`, `lake-manifest.json`, the canonical statement ledger, or the adjudication files.

From the project's `lean/` directory, compile the modules explicitly:

```bash
lake build QuarticQuery.Paper.ClassicalDirectProduct \
  QuarticQuery.Paper.ClassicalPlanted \
  QuarticQuery.Paper.ClassicalUniformZero \
  QuarticQuery.Paper.ClassicalAsymptotics
```

The uniform-zero module imports the new planted module. The asymptotic module imports the existing `QuarticQuery.Results.Unconditional`. None of the additions imports the uncompiled `Paper.Section4` or `ForrelationLower.Uniform` candidates.

Use the project's established resource guard if its local build policy requires one. Record the actual command, toolchain, dependency manifest, source commit and clean-tree status, exit code, and complete diagnostic log. The command above names the intended Lake targets; it does not override that policy.

## Combined import and axiom inspection

After the build succeeds, compile a temporary file importing all four modules. The following Lean snippet is also **unelaborated** here. It is intended to verify combined import compatibility and show the actual dependencies of the principal declarations:

```lean
import QuarticQuery.Paper.ClassicalDirectProduct
import QuarticQuery.Paper.ClassicalPlanted
import QuarticQuery.Paper.ClassicalUniformZero
import QuarticQuery.Paper.ClassicalAsymptotics

#check QuarticQuery.Paper.classical_direct_product
#check QuarticQuery.Paper.eq_18
#check QuarticQuery.Paper.uniform_zero_given_transcript
#check QuarticQuery.Paper.eq_23_randomized
#check QuarticQuery.Paper.classical_tail_parameters
#check QuarticQuery.Paper.classical_Fkm_ratio

#print axioms QuarticQuery.Paper.classical_direct_product
#print axioms QuarticQuery.Paper.uniform_zero_given_transcript
#print axioms QuarticQuery.Paper.eq_23_randomized
#print axioms QuarticQuery.Paper.classical_tail_parameters
#print axioms QuarticQuery.Paper.classical_Fkm_ratio
```

An axiom listing must be interpreted under the project's established trust policy; ordinary Lean foundations and an unproved custom assumption are different categories. Textual absence of `sorry` cannot substitute for this check.

## Review before updating evidence

Inspect the elaborated propositions, especially the conditional-law normalization, the meaning of `capped`, the actual randomized-program success fields, the support premise for planted positive inputs, and the use of the same circuit in both complexities. Compile the displayed signatures and compare them to the canonical statements. `NEW_STATEMENTS.json` uses existing vocabulary to make these comparisons reviewable.

Keep `claim-EZ` partial until its early/late random variables and intermediate bounds have their own proof. Compiling its endpoint alone does not close that compound statement. Record the alternative route of the erased-zero bound. If statement comparison or reachability is later performed, record it separately from compilation; no such result is supplied here.

## Reproducing the completed non-Lean checks

From this archive's root:

```bash
python3 -I checks/check_mathematics.py
python3 -I checks/validate_return.py --packet /absolute/path/to/extracted/input
```

The first command uses only exact Python integers and `fractions.Fraction`. The second checks file/JSON/correspondence integrity and the unchanged input manifest. It is a lexical source check and cannot parse or elaborate Lean. With no `--packet` argument it performs only the self-contained archive checks and reports the omitted input checks.
