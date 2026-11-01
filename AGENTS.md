# Working in quartic-query-lean

Read [README.md](README.md) and [research/README.md](research/README.md) first.
This repository owns research intake, review requests, Lean source and the tools
that package them. It does not inherit the private ai_workflow runtime or its
commands.

## Ownership

- `research/intake/` holds original advisory research records. Keep their source
  references and uncertainty intact. Design proposals there are not implemented
  interfaces or verified mathematical claims.
- `research/requests/` owns maintained review instructions. Edit these source
  files and rebuild packets; do not edit generated ZIP instructions. Requests
  describe planned checking and are not proof evidence.
- `lean/` is the Lean project. Its toolchain and dependency files own the build.
  Do not infer successful compilation from a file's presence.
- `tools/` holds maintenance programs; `tests/` holds their regression tests.
- `README.md` and the directory READMEs explain current use. Keep commands and
  links aligned with the files they describe.
- PDFs, ZIPs, Lake dependencies and build products are local inputs or outputs,
  not new source owners. The packet builder accepts explicit external paths.

Before moving a file, find its consumers, including the packet builder. Preserve
archive member names and original research evidence. Avoid adding empty future
architecture: add a directory when an implementation needs it.

## Validation and commits

Run `make check` for Python tooling, layout and local README links. Run
`python3 tools/check_repository.py --index` after staging exact owned paths.
These checks do not validate proofs. Lean changes need their own build evidence.

Preserve concurrent and untracked work; do not stage it as part of an unrelated
cleanup. Commit only the changes you own. When reporting results, distinguish
source present, build attempted, build passed and independent review.
