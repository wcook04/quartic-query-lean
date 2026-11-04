# Round-ten input integrity audit

The input archive passed CRC testing and contains 6,176 files (65,106,294 archive bytes; 194,443,958 uncompressed bytes). There are no duplicate or unsafe member names, encrypted members or symbolic links.

All 6,174 manifest entries match their SHA-256 and byte counts both in the ZIP and in the extracted copy. The archive members not listed by the manifest are: READ_ME_FIRST.md, manifest.json. READ_ME_FIRST.md separately matches manifest.request_sha256; the manifest does not list itself.

All 9 draft bindings agree across SOURCE_STATUS, manifest metadata and actual bytes. All three declared PDF hashes match. Seventeen of eighteen render inputs are supplied at the declared path and match. The exposition receipt also declares `docs/figures/exposition/style.tex` (SHA-256 `b63231827c3f07218f2004beba07a62deba4d7bef1ef1b12c7d8dbb425b34380`), but neither that path nor matching bytes occur in the packet. This limits reconstruction of that supporting PDF; it does not make the PDF corrupt. The expert-companion inputs all match.

The PDF objects parse, with page counts: expert_companion.pdf: 18, exposition.pdf: 24, reasoning_record.pdf: 139, source.pdf: 19.

The supplied transcript contains 977,681 bytes and 1,096 lines. Its five snapshot envelopes declare 954 items in total, matching the 954 parsed native items; they include 291 evidence-reference objects and 291 objects explicitly reporting omitted characters. Its substantive content was not read in this metadata stage.

## Evidence limits

No manuscript or review prose was inspected. No submitted scripts, renderer, Lean build or Comparator were executed. A matching render receipt is provenance evidence, not fresh proof of rendering, mathematical correctness or human review. The record is explicitly marked as different from the earlier accepted-review hash and as an unreviewed working draft. This is disclosed source status, not a detected corruption.

Input ZIP SHA-256: `60f48603e8aa79668fb0df84d9d2739f039446c177792d80f8404d3873b88e76`
