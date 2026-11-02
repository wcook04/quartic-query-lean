# Round-two research returns

These seven folders preserve the submitted archive members, including the
authors' Lean and Python files, without modification. They are advisory source
material, not the repository's executable proof or tool owners. Their presence
does not establish a successful build or the correctness of their conclusions.
Review decisions and corrections belong in [adjudication](../../adjudication/).

| Return | Submitted focus |
| --- | --- |
| [1_statement_fidelity/](1_statement_fidelity/) | Statement fidelity |
| [2_lean_construction/](2_lean_construction/) | Construction |
| [3_lean_quantum_upper/](3_lean_quantum_upper/) | Quantum upper bound |
| [4_lean_classical_lower/](4_lean_classical_lower/) | Classical lower bound |
| [5_lean_appendix_a/](5_lean_appendix_a/) | Appendix A |
| [6_sharp_uniform_forrelation/](6_sharp_uniform_forrelation/) | Sharp uniform Forrelation |
| [7_single_family_exponent/](7_single_family_exponent/) | Single-family exponent |

[intake.json](intake.json) records each original archive's filename and SHA-256,
and the path, byte length and SHA-256 of every submitted file. The repository
check compares all 178 members against that manifest and rejects unlisted files
and mismatching bytes under these snapshot folders. Submitted READMEs keep the
sender's original relative links; they are checked as bytes rather than treated
as maintained navigation.

Before replaying a submitted checker, inspect its output paths and other side
effects. Use a scratch copy or its explicit output option; several checkers
write beside their own source even when launched from another working
directory. Recheck the original snapshot hashes afterward. Repairs and fresh
results belong with the maintained tools or adjudication, not in these folders.

```sh
python3 tools/check_repository.py
python3 tools/check_repository.py --index
```

The original ZIPs are kept outside the checkout. To verify those archives as
well as the extracted files, give the directory containing all seven original
ZIPs; add `--index` to use the staged manifest and staged member contents.

```sh
python3 tools/check_repository.py --archive-dir /path/to/original-archives
```

If the manifest itself changes, use the original ZIPs to check its contents;
the ordinary check cannot detect coordinated edits to a member and its manifest
entry. The recorded member bytes do not reproduce the original ZIP metadata;
the archive hashes identify the original ZIP files separately. The checker reads
the archives and submitted files as data and does not run submitted programs.
