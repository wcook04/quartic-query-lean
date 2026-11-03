import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
SPEC = importlib.util.spec_from_file_location("build_comparator_map", ROOT / "tools/build_comparator_map.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

SOURCE = """module

namespace Top

/-- A tree. -/
inductive Tree where
  | leaf
  | node (l r : Tree)

def Tree.size : Tree → Nat
  | .leaf => 1
  | .node l r => l.size + r.size

open Classical in
/-- Uses `Tree`. -/
noncomputable def pick (t : Tree) : Nat :=
  t.size

end Top

namespace Top.Checked

theorem size_pos (t : Tree) : 0 < t.size := by
  sorry

end Top.Checked
"""


class BlockTests(unittest.TestCase):
    def test_blocks_carry_namespaces_prefixes_and_pattern_arms(self):
        blocks = {b["name"]: b for b in MODULE.lean_blocks(SOURCE)}
        self.assertEqual(sorted(blocks), ["Top.Checked.size_pos", "Top.Tree", "Top.Tree.size", "Top.pick"])
        self.assertEqual(blocks["Top.Tree"]["doc_comment"], "A tree.")
        self.assertIn("| .node l r => l.size + r.size", blocks["Top.Tree.size"]["text"])
        self.assertTrue(blocks["Top.pick"]["text"].startswith("open Classical in\n/-- Uses"))
        lines = SOURCE.split("\n")
        for block in blocks.values():
            text = "\n".join(lines[block["line_start"] - 1:block["line_end"]])
            self.assertEqual(text, block["text"])
            self.assertEqual(hashlib.sha256(text.encode()).hexdigest(), block["sha256"])

    def test_theorem_statement_identifiers_resolve_through_namespaces(self):
        blocks = {b["name"]: b for b in MODULE.lean_blocks(SOURCE)}
        known = set(blocks)
        resolve = MODULE.resolver(known, "Top.Checked", [])
        found = MODULE.identifiers(MODULE.statement_text(blocks["Top.Checked.size_pos"]), resolve)
        self.assertEqual(found - {"Top.Checked.size_pos"}, {"Top.Tree"})

    def test_comments_do_not_create_dependencies(self):
        resolve = MODULE.resolver({"Top.Tree"}, "Top", [])
        self.assertEqual(MODULE.identifiers("/-- mentions Tree -/ -- Tree\nNat", resolve), set())


class RecordTests(unittest.TestCase):
    RECORD = ("intro\n<!-- passage:A -->\nThe map `R` is defined.\n\n<!-- claim:def-R -->\n"
              "Claim text.\n<!-- /passage:A -->\n<!-- passage:B -->\nchanged\n<!-- /passage:B -->\n")

    def correspondence(self):
        body = self.RECORD.split("<!-- passage:A -->")[1].split("<!-- /passage:A -->")[0]
        return {"passages": [{"id": "A", "sha256": hashlib.sha256(body.encode()).hexdigest(), "claims": ["def-R"]},
                             {"id": "B", "sha256": "0" * 64, "claims": []}]}

    def test_passage_hashes_are_verified_and_mismatches_reported(self):
        passages, mismatched = MODULE.record_passages(self.RECORD, self.correspondence())
        self.assertEqual(sorted(passages), ["A"])
        self.assertEqual(mismatched, ["B"])
        start, stop = passages["A"]["claim_segments"]["def-R"]
        quoted = MODULE.excerpt(self.RECORD, passages["A"], start, stop)
        self.assertEqual(quoted["excerpt"], "Claim text.")
        self.assertEqual(self.RECORD.split("\n")[quoted["line_start"] - 1], "Claim text.")

    def test_checked_wrappers_are_not_matched_by_implementation_short_names(self):
        passages, _ = MODULE.record_passages(self.RECORD, self.correspondence())
        mentions = MODULE.backtick_mentions(passages, ["QuarticQuery.R", "QuarticQuery.Checked.R"])
        self.assertIn("QuarticQuery.R", mentions)
        self.assertNotIn("QuarticQuery.Checked.R", mentions)


class GeneratedMapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.map = json.loads((ROOT / "corpus/comparator_map.json").read_text(encoding="utf-8"))
        cls.record = (ROOT / "docs/reasoning_record.md").read_text(encoding="utf-8")

    def test_every_block_hash_matches_its_challenge_lines(self):
        for challenge in self.map["challenges"]:
            lines = (ROOT / challenge["path"]).read_text(encoding="utf-8").split("\n")
            for block in challenge["blocks"]:
                text = "\n".join(lines[block["line_start"] - 1:block["line_end"]])
                self.assertEqual(hashlib.sha256(text.encode()).hexdigest(), block["sha256"], block["name"])

    def test_configured_positive_targets_and_only_they_are_direct(self):
        for challenge in self.map["challenges"]:
            configured = {name for config in challenge["configurations"] if config["role"] == "positive"
                          for name in config["theorem_names"]}
            direct = {b["name"] for b in challenge["blocks"] if b["comparison"]["credit"] == "direct"}
            self.assertEqual(direct, configured, challenge["path"])

    def test_glosses_are_exact_record_excerpts(self):
        lines = self.record.split("\n")
        for name, declaration in self.map["declarations"].items():
            gloss = declaration["primary_gloss"]
            if gloss is None:
                continue
            self.assertIn(gloss["excerpt"], self.record, name)
            self.assertEqual(hashlib.sha256(gloss["excerpt"].encode()).hexdigest(), gloss["excerpt_sha256"])
            self.assertIn(gloss["excerpt"].split("\n")[0], lines[gloss["line_start"] - 1], name)

    def test_record_passages_all_verify_and_gaps_are_explicit(self):
        self.assertEqual(self.map["record"]["passage_hash_mismatches"], [])
        for name, declaration in self.map["declarations"].items():
            self.assertEqual(declaration["gap"] is None, bool(declaration["record_references"]), name)

    def test_unused_vocabulary_is_not_credited_as_compared(self):
        unconditional = next(c for c in self.map["challenges"]
                             if c["path"] == "lean/QuarticCorpus/Unconditional/Challenge.lean")
        credit = {b["name"]: b["comparison"]["credit"] for b in unconditional["blocks"]}
        self.assertEqual(credit["QuarticQuery.Tournament.IsComparison"], "not_in_any_configured_statement")
        for name in ("QuarticQuery.R", "QuarticQuery.Q", "QuarticQuery.totalise", "QuarticQuery.alphaTot",
                     "QuarticQuery.AdaptiveProgram", "QuarticQuery.QLe"):
            self.assertEqual(credit[name], "statement_dependency", name)

    def test_headline_statement_links_through_the_wrapper_are_labelled(self):
        # The refreshed Unconditional receipt names only its configured wrapper, so
        # the proof reference to the implementation theorem carries no credit.
        links = self.map["declarations"]["QuarticQuery.Checked.theorem_one_one"]["statement_ids"]
        self.assertEqual({(l["statement_id"], l["join"], l["comparison_credit"]) for l in links},
                         {("thm-1.1", "solution_proof_reference", "none")})


if __name__ == "__main__":
    unittest.main()
