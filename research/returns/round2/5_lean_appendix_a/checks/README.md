# Reproducing the supplemental checks

Run these commands from the extracted return directory with Python 3.10 or later. The adversary and Huang scripts also require NumPy. These are finite arithmetic and static source checks. They do not elaborate Lean, inspect a compiled environment, run Comparator, or prove the general statements.

```bash
python checks/adversary_checks.py > checks/adversary_checks.json
python checks/sensitivity_small_cubes.py > checks/sensitivity_small_cubes_output.json
python checks/huang_and_restriction_checks.py
python checks/source_coefficient_check.py > checks/source_coefficient_check.json
```

The Huang script writes its result beside the script. The other scripts write JSON to standard output. Their result files distinguish exact arithmetic from floating-point diagnostics. Assertions stop execution on a failed check.

## Static source and metadata check

The integrity checker needs the original packet and the dependency source trees at the revisions in `source_manifest.json`. Supply their absolute paths:

```bash
python checks/validate_return.py \
  --packet /absolute/path/to/quartic_r2_5_lean_appendix_a \
  --complexitylib /absolute/path/to/complexitylib_pinned \
  --cslib /absolute/path/to/cslib_pinned \
  --mathlib /absolute/path/to/mathlib_pinned
```

It checks required files, metadata consistency, passage anchors, source declaration inventory, direct import paths, forbidden proof placeholders, and the original packet's file hashes. It writes `validation.json`. A successful result establishes those checks only; it is not a substitute for elaboration or independent statement comparison.

## Lean integration

After copying the returned `lean/QuarticQuery/Paper/AppendixA*.lean` modules into the existing pinned project, the proposed build command from that project's Lean directory is:

```bash
lake build QuarticQuery.Paper.AppendixA
```

This command has not been run in this environment. All returned Lean modules retain their `unelaborated` status until a successful build is recorded. Any dependency, axiom, or Comparator evidence must then be generated from that compiled environment.

## Archive integrity

`return_manifest.json` records the size and SHA-256 digest of each other delivered file. The manifest excludes itself. Re-running a check can rewrite its JSON result, so compare the manifest before regenerating outputs if byte-for-byte integrity matters.
