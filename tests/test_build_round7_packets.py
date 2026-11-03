import importlib.util
import json
import re
import sys
import tempfile
import types
from unittest import mock
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("round7", ROOT / "tools/build_round7_packets.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RoundSevenTests(unittest.TestCase):
    def setUp(self):
        MODULE.configure()

    def test_sanitization_preserves_rule_and_removes_private_records(self):
        rules = [{"id": f"RG-{i:02}", "title": f"Rule {i}", "status": "candidate",
                  "scopes": ["short"], "rule": "Public rule", "failure": "Public failure",
                  "limit": "Public limit", "probe": {"kind": "process"},
                  "specimens": [{"quote": "a public example", "source": "public"},
                                {"quote": "Private Person example", "source": "private"}],
                  "instances": [{"lesson": "public instance"}, {"lesson": "Private Person instance"}],
                  "example": {"before": "Private Person", "after": "private"}}
                 for i in range(1, 27)]
        data = {"rules": rules, "history": [{"id": "RG-01", "note": "Private Person"},
                                             {"id": "RG-02", "note": "public"}],
                "other": [{"nested": {"value": "Private Person"}}, {"value": "public"}]}
        measurements = [{"features": {"f": {"rules": ["RG-01", "RG-26"]}}}]
        result = MODULE.sanitize_register(data, measurements, [re.compile("Private Person")], ["RG-26"])
        self.assertEqual([r["id"] for r in result["rules"]], [r["id"] for r in rules])
        for rule in result["rules"]:
            self.assertEqual(rule["rule"], "Public rule")
            self.assertEqual(len(rule["specimens"]), 1)
            self.assertEqual(len(rule["instances"]), 1)
            self.assertNotIn("example", rule)
        self.assertEqual(result["history"], [{"id": "RG-02", "note": "public"}])
        self.assertEqual(result["other"], [{"nested": {"value": "a cited author"}}, {"value": "public"}])
        self.assertNotIn("Private Person", json.dumps(result))
        self.assertIn("omitted", result["export_note"])

    def test_build_register_preserves_rules_through_validation_and_render(self):
        rules = [{"id": f"RG-{i:02}", "title": f"Rule {i}", "status": "candidate",
                  "scopes": ["short"], "rule": "Public rule", "limit": "Public limit",
                  "specimens": [{"quote": "Private Person", "source": "private"},
                                {"quote": "Public example", "source": "public"}]}
                 for i in range(1, 27)]
        checked = []

        def produce(drafts, literature, out, title, job):
            target = Path(out) / "register"
            target.mkdir(parents=True)
            (target / "register_rules.json").write_text(json.dumps({"rules": rules}))
            (target / "measurement.json").write_text(json.dumps([
                {"features": {"f": {"rules": ["RG-01", "RG-26"]}}}]))
            (target / "measurement.txt").write_text("RG-01 RG-26")

        def validate(data):
            checked.append([row["id"] for row in data["rules"]])
            self.assertNotIn("Private Person", json.dumps(data))

        def render(selected, title):
            checked.append([row["id"] for row in selected])
            return "\n".join(row["id"] + " " + row["specimens"][0]["quote"] for row in selected)

        register = types.SimpleNamespace(build_packet_inputs=produce, validate_rules=validate,
                                         render_rules=render)
        package = types.ModuleType("lean_exposition")
        package.register = register
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in MODULE.SKILL_FILES:
                path = root / "skills" / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("See RG-26.")
            for name in MODULE.METHOD_DOCS:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("See RG-01.")
            with mock.patch.dict(sys.modules, {"lean_exposition": package}), \
                    mock.patch.object(MODULE.base, "reader_leak_patterns", return_value=[re.compile("Private Person")]):
                output = MODULE.build_register(root, root / "annexes", root / "out")
            data = json.loads((output / "register_rules.json").read_text())
            rendered = (output / "REGISTER_RULES.md").read_text()
            expected = [r["id"] for r in rules]
            self.assertEqual(checked, [expected, expected])
            self.assertEqual([r["id"] for r in data["rules"]], expected)
            self.assertNotIn("Private Person", rendered)
            self.assertIn("Public example", rendered)
            self.assertIn("omitted", rendered)

    def test_sanitization_fails_on_private_core_and_unresolved_references(self):
        rules = {"rules": [{"id": "RG-01", "rule": "Private Person"}]}
        with self.assertRaisesRegex(ValueError, "private marker in core"):
            MODULE.sanitize_register(rules, [], [re.compile("Private Person")])
        rules["rules"][0]["rule"] = "public"
        with self.assertRaisesRegex(ValueError, "unresolved register rule references"):
            MODULE.sanitize_register(rules, [{"features": {"f": {"rules": ["RG-99"]}}}], [])
        with self.assertRaisesRegex(ValueError, "unresolved writing-method"):
            MODULE.sanitize_register(rules, [], [], ["RG-99"])
        with self.assertRaisesRegex(ValueError, "unique"):
            MODULE.sanitize_register({"rules": rules["rules"] * 2}, [], [])

    def test_every_panel_renders_a_feedback_request_naming_no_reader(self):
        for job in MODULE.JOBS:
            request = MODULE.base.render_request(job, MODULE.REQUESTS)
            self.assertIn("Emulate perspectives, never people", request)
            self.assertIn("search online", request)
            self.assertIn("reading_log.md", request)
            for pattern in MODULE.base.reader_leak_patterns():
                self.assertIsNone(pattern.search(request), (job, pattern.pattern))

    def test_previous_round_sources_exist(self):
        for source in MODULE.PREVIOUS.values():
            self.assertTrue((ROOT / source).is_file(), source)

    def test_panels_have_prefixes_and_a_literature_sample(self):
        self.assertEqual(set(MODULE.JOBS), set(MODULE.PREFIX))
        self.assertEqual(set(MODULE.JOBS), set(MODULE.LITERATURE))
        for job in MODULE.JOBS:
            self.assertTrue(5 <= len(MODULE.LITERATURE[job]) <= 10, job)
            self.assertTrue(set(MODULE.LITERATURE[job]) <= set(MODULE.base.CATALOG), job)


if __name__ == "__main__":
    unittest.main()
