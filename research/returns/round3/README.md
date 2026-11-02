# Round-three research returns

These ten submissions are preserved as advisory evidence. Their mathematical
claims, proposed changes and reported checks require independent adjudication;
neither preservation nor a submitted result establishes correctness or a build.
The files under `members/` are unmodified archive members, including submitted
programs. Do not run those programs as part of intake.

| Archive | Submitted focus | Pasted input |
| --- | --- | --- |
| [01](members/01_models_evidence/) | Models and evidence | [01](attachments/input_01.txt) |
| [02](members/02_forrelation_promise_circuit/) | Forrelation promise and circuit | [02](attachments/input_02.txt) |
| [03](members/03_forrelation_lower_bound/) | Forrelation lower bound | [03](attachments/input_03.txt) |
| [04](members/04_addressed_construction/) | Addressed construction | Not present among these inputs |
| [05](members/05_quantum_upper/) | Quantum upper bound | [04](attachments/input_04.txt) |
| [06](members/06_direct_product/) | Direct product | [05](attachments/input_05.txt) |
| [07](members/07_planted_lower_bound/) | Planted lower bound | [06](attachments/input_06.txt) |
| [08](members/08_reviewed/) | Exponent and universal quartic upper bound | [07](attachments/input_07.txt) |
| [09](members/09_evidence_backend/) | Evidence backend and semantic controls | [08](attachments/input_08.txt) |
| [10](members/10_baseline_review/) | Baseline review | [09](attachments/input_09.txt) |

Input 10 is a local-only session packet, not an accompanying return. Its bytes
remain locally in `attachments/input_10.txt` and its hash is recorded in the
manifest; the file is excluded from public Git history. The matching above follows the archive names stated in each pasted text;
the return 04 README also reports that its own source attachment was unavailable.

[intake.json](intake.json) records the original archive filenames and hashes,
every member's path, size and SHA-256, and each pasted input's size and SHA-256.
The nine return texts also have their source attachment IDs. The locally preserved originals are under `archives/`; ZIPs and
the submitted PDF are ignored by Git under this repository's existing policy.
Consequently a normal clone will not itself contain those ignored bytes. Retain
the original archives as independent provenance, and compare their hashes when
reviewing changes to the manifest.

On a checkout containing the local archive copies and all extracted files:

```sh
python3 tools/intake_round3_returns.py --verify
```

This reads the ZIPs as data, validates member paths and checks archive, snapshot
and attachment hashes. It does not execute the returned files. Intake copies the
original files directly; it refuses to replace an existing snapshot.
