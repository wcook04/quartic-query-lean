"""Exercise the edition consumer at real mathematical selections and across edits."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import build_reading_api as api
from reading_selection import BoundLocations
from reading_applications import application_resources


class BindingTests(unittest.TestCase):
    def test_move_preserves_binding_but_changed_mathematics_does_not(self):
        edition = api.Edition(api.ROOT)
        config = edition.json(api.ROUTES)
        row = next(r for r in config["routes"] if r["id"] == "weight")
        text = edition.read(api.PAPERS["exposition"]).decode()
        texts = {"exposition": "\n\n" + text}
        locations = BoundLocations(edition, config, api.PAPERS, texts, {}, api.locate_quote)
        loc = locations.check(row, "exposition", quote=row["exposition"])
        self.assertEqual(loc["lines"][0], api.locate_quote(text, row["exposition"], "old")["lines"][0] + 2)
        # Keep the exact selector but change the conclusion inside its paragraph.
        texts["exposition"] = text.replace(row["exposition"], row["exposition"] + " Changed assertion.")
        with self.assertRaisesRegex(ValueError, "selected text changed"):
            locations.check(row, "exposition", quote=row["exposition"])

    def test_unchanged_selection_with_changed_prerequisite(self):
        edition = api.Edition(api.ROOT)
        config = edition.json(api.ROUTES)
        documents = {**api.PAPERS, "verification": api.SUPPLEMENT}
        with tempfile.TemporaryDirectory() as temp:
            draft = Path(temp)
            for path in documents.values():
                (draft / path).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(edition.root / path, draft / path)
            record = draft / documents["reconstruction"]
            marker = "<!-- passage:CL-heavy -->"
            text = record.read_text()
            self.assertIn(marker, text)
            record.write_text(text.replace(marker, marker + "\nA changed threshold for a heavy column."))
            def report():
                return api.audit_bindings(edition, draft, documents, config, api.locate_quote)
            audit = report()
            self.assertEqual(audit["affected_topics"]["joint-event"], {
                "selections_locatable": True, "selection_text_as_bound": True, "prerequisites_as_bound": False})
            issues = audit["needs_review"]
            self.assertEqual([(r["id"], r["kind"], r["passage"]) for r in issues],
                             [("joint-event", "prerequisite_changed", "CL-heavy")])
            record.write_text(text + "\nA note outside the associated passages.\n")
            self.assertEqual(report()["needs_review"], [])

    def test_application_export_requires_both_a_source_site_and_compiled_use(self):
        edition = api.Edition(api.ROOT)
        graph = edition.json("corpus/reading_dependencies.json")
        plan = edition.json("docs/reading_applications.json")
        inspection = edition.json("corpus/reading_applications.json")
        step = plan["journeys"][0]["steps"][0]
        original = step["site"]
        topics = {topic: {} for j in plan["journeys"] for topic in j["topics"]}
        inputs = {"docs/reading_applications.json": plan, "corpus/reading_applications.json": inspection}
        with patch.object(edition, "json", side_effect=inputs.__getitem__):
            graph["currentness"] = "stale"
            application_resources(edition, graph, {}, topics)
            self.assertEqual(json.loads(edition.resources["selection/applications.json"])["journeys"], {})
            graph["currentness"] = "current"
            step["site"] = "unwritten Lean application"
            with self.assertRaisesRegex(ValueError, "application site"):
                application_resources(edition, graph, graph["nodes"], topics)
            step["site"] = original
            inspection["callers"][step["caller"]] = []
            with self.assertRaisesRegex(ValueError, "unwitnessed use"):
                application_resources(edition, graph, graph["nodes"], topics)


@unittest.skipUnless(shutil.which("node"), "Node required to exercise the ES module")
class ReaderConsumerTests(unittest.TestCase):
    def test_consume_six_selections_and_scope_from_the_static_edition(self):
        edition = api.Edition(api.ROOT)
        api.compile_edition(edition)
        with tempfile.TemporaryDirectory() as name:
            out = Path(name)
            # Working-tree tests may precede a commit. Use the actual packaging
            # path with the already captured resources and a fixture commit binding.
            fixture = api.Edition(api.ROOT)
            fixture.resources = edition.resources
            api.export(fixture, out)
            script = r"""
import assert from "node:assert/strict";
import {openLocalOrHTTP} from "./tools/query_reading_api.mjs";
const reader = await openLocalOrHTTP(process.argv[2]);
const resolve = (paper, id) => reader.resolve({paper, id});
const find = (r, name) => r.proof.find(n => n.name.endsWith(name));
const cycle = await resolve("exposition", "exposition/cycle/1");
assert(cycle.text.includes("fig3_tournament.svg"));
assert(cycle.topics.some(t => t.kind === "illustrates" && t.id === "cycle"));
assert(cycle.topics.find(t => t.id === "cycle").treatments.every(t => t.paper !== "expert"));

const weight = await resolve("reconstruction", "passage/upper-weight-drift");
const drift = find(weight, ".quantumDrift");
assert(drift.source.value.includes("QuarticQuery.Tournament.expected_weight_eq"));
assert(drift.source.type.includes("QuarticQuery.Tournament.IsComparison"));
assert(drift.source.text.includes("quantumDrift"));
assert(drift.basis.some(b => b.statement === "eq-13" && b.relation === "stronger"));
assert(weight.topics.find(t => t.id === "weight").treatments.length === 3);
const limited = await reader.resolve({paper:"expert",id:"expert/weight/0"}, {depth:1,limit:1,budget:1});
assert(limited.proof.some(n => n.uses.limitReached || n.uses.depthLimited || n.uses.budgetLimited));
const incoming = await reader.expand("QuarticQuery.Tournament.expected_weight_eq");
assert(incoming.incoming.value.includes(drift.name));
for (const direction of ["uses","used_by"]) for (const hit of drift[direction].witnesses)
  for (const edge of hit.path) assert((await reader.expand(edge.from))[edge.kind].includes(edge.to));

const projection = await resolve("exposition", "exposition/projection/0");
assert(projection.statements.some(s => s.id === "eq-4" && s.semantic_probes.length));
assert(projection.statements.some(s => s.id === "claim-proj-prob" &&
       s.lean.some(t => t.relation === "partial")));
assert(projection.topics.some(t => t.note.includes("negative example")));
assert(projection.statements.some(s => s.lean.some(t => t.review_evidence === "legacy_unbound")));
assert(!projection.proof.some(n => n.basis.some(b => b.review === "legacy_unbound")));

const capped = await resolve("exposition", "exposition/joint-event/0");
assert(find(capped, ".Paper.eq_21").basis.some(b => b.review === "current" && b.relation === "exact"));
assert(capped.editorialLinks.some(e => e.relation === "analogous_to"));
assert(capped.statementDependencies.find(s => s.id === "eq-21").requires.includes("def-simulator"));

assert(capped.journeys.includes("capped-predictor"));
const simulator = await reader.journey("capped-predictor");
assert(simulator.steps.some(step => step.text.includes("avg_resample") && step.text.includes("T J A i t")));
const family = await reader.journey("forrelation-family");
const lower = family.steps.flatMap(s => s.uses).find(u => u.declaration.endsWith(".Gvalue_lt_R_addressedF"));
const inst = lower.compiled_uses_in_caller.find(t => t.arguments.some(a => a.binder === "hC"));
assert(inst.arguments.some(a => a.binder === "f" && a.argument.includes("P k t")));
assert(inst.arguments.some(a => a.binder === "L" && a.argument.includes("Lvalue k t")));
assert(inst.arguments.some(a => a.binder === "hC" && a.proof && a.type.includes("CircuitRealises")));
assert(family.interfaces.find(d => d.name.endsWith(".CircuitRealises")).text.includes("tr C.domainOut = true ↔ promised f x"));
assert(family.interfaces.find(d => d.name.endsWith(".FamilyBoundsAt")).text.match(/Fkm k t Cir/g).length === 2);
assert(family.steps.some(s => s.text.includes("Q_Fkm_le l t ht") && s.text.includes("Gvalue_lt_R_Fkm")));
for (const step of family.steps) {
  const caller = await reader.expand(step.caller);
  assert(step.uses.every(use => caller.value.includes(use.declaration)));
  assert(family.treatments.some(topic => topic.id === step.topic && topic.selections.length));
}
assert(simulator.steps.find(s => s.title.includes("Resample")).uses.some(u =>
  u.compiled_uses_in_caller.some(t => t.arguments.some(a => a.binder === "hguess" && a.type.includes("guessSuccess")))));

assert(family.treatments.flatMap(t => t.selections).some(s => s.paper === "expert"));
assert(family.correspondence.some(s => s.lean.some(t => t.route === "alternative")));
const back = await reader.fromDeclaration(lower.declaration);
assert(back.journeys.includes(family.id));
const gaussianTrip = await reader.journey("gaussian-transport");
assert.equal(gaussianTrip.treatments.find(t => t.id === "gaussian-path").correspondence_scope, "constituents_only");
assert(gaussianTrip.steps.some(s => s.caller.endsWith(".mass_ge") && s.text.includes("PhiF t")));
assert(gaussianTrip.steps.some(s => s.caller.endsWith(".advantage_le_sharp")));
await assert.rejects(reader.journey("absent"), /Unknown reading journey/);

const gaussian = await resolve("reconstruction", "passage/forr_three_blocks");
assert(find(gaussian, ".Int_eq_paths").basis.every(b => b.basis === "editorial_constituent"));
assert(gaussian.topics.find(t => t.id === "gaussian-path").treatments.length === 1);

const head = await resolve("expert", "expert/headline/0");
assert(find(head, ".theorem_1_1_unconditional").basis.some(b => b.relation === "exact" && b.route === "alternative"));
assert(find(head, ".alphaTot_eq_four_unconditional").basis.some(b => b.relation === "partial"));
assert(head.comparisons.some(c => c.role === "positive" && c.receipt));
const reverse = await reader.fromDeclaration("QuarticQuery.theorem_1_1_unconditional");
assert(reverse.treatments.some(t => t.selection === "expert/headline/0"));
const blind = await reader.fromDeclaration("Round3.SharedBadSpec.vacuous_claim");
assert(blind.comparisons.some(c => c.role === "negative_control" && c.outcome === "accepted_shared_bad_spec_blind_spot"));
const eq = await resolve("expert", "expert/erased-zero/0");
assert(eq.statements.find(s => s.id === "eq-19").lean.some(t => t.relation === "stronger"));
const exact = await resolve("exposition", "exposition/weight/0");
const loc = {paper: "exposition", line: exact.lines[0], documentSha256: exact.document.sha256};
assert((await reader.resolve(loc)).topics.some(t => t.id === "weight"));
await assert.rejects(reader.resolve({...loc, documentSha256:"old"}), /edition/);
assert.equal((await reader.resolve({...loc, line:1})).coverage,"unmapped");
assert.equal((await reader.expand("NoSuchDeclaration")).status,"outside_recorded_graph");
const external = await reader.expand("And");
assert.equal(external.status,"external_module_boundary");
assert(external.module);
const upper = await resolve("reconstruction", "passage/R3-A-RESULT");
assert(upper.statements.some(s => s.id === "thm-A.1"));
const hard = await resolve("reconstruction", "passage/forr_uniform_assembly");
assert(find(hard,".forrelation_lower_uniform_sharp"));
assert(hard.editorialLinks.some(e => e.target === "same-family"));
assert(hard.topics.find(t => t.id === "uniform-hardness").treatments.every(t => t.paper === "reconstruction"));
"""
            subprocess.run(["node", "--input-type=module", "-", str(out / "index.json")],
                           cwd=api.ROOT, input=script, text=True, check=True)
