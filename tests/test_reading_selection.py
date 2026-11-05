"""Exercise the edition consumer at real mathematical selections and across edits."""
import json
import os
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
from reading_applications import application_resources, obligation_notes, witnessed_occurrences
from record_reading_dependencies import source_records


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
            mutations = [
                ("forr_definition", r"1,&\Phi(z)\ge\delta", r"1,&|\Phi(z)|\ge\delta", "projection"),
                ("forr_bundle", r"Fix $k\ge2$", r"Fix $k\ge3$", "same-family"),
            ]
            for anchor, old, new, topic in mutations:
                with self.subTest(anchor=anchor):
                    body = next(m for m in api.PASSAGE.finditer(text) if m[1] == anchor)
                    self.assertEqual(body[2].count(old), 1)
                    record.write_text(text[:body.start(2)] + body[2].replace(old, new) + text[body.end(2):])
                    changed = report()["affected_topics"]
                    self.assertTrue(changed[topic]["selection_text_as_bound"])
                    self.assertFalse(changed[topic]["prerequisites_as_bound"])
                    self.assertNotIn("joint-event", changed)
            record.write_text(text + "\nA note outside the associated passages.\n")
            self.assertEqual(report()["needs_review"], [])


    def test_discharge_requires_the_local_argument_and_a_witnessed_later_provider(self):
        edition = api.Edition(api.ROOT)
        route = edition.json("docs/reading_applications.json")["journeys"][0]
        steps = {s["id"]: s for s in route["steps"]}
        local = steps["classical-instance"]
        rule = next(r for r in local["obligations"] if r["binder"] == "hLR")
        inspection = edition.json("corpus/reading_applications.json")
        terms = [t for t in inspection["callers"][local["caller"]] if t["callee"] == rule["callee"]]
        uses = [{"declaration": rule["callee"], "compiled_uses_in_caller": terms}]
        local["obligations"] = [rule]
        rule["assembly"]["provider"] = "QuarticQuery.universalPower_four"
        with self.assertRaisesRegex(ValueError, "unsupported assembly link"):
            obligation_notes(local, steps, uses)
        rule["match"] = {"argument": "unrelated"}
        with self.assertRaisesRegex(ValueError, "no compiled proof"):
            obligation_notes(local, steps, uses)

    @unittest.skipUnless(os.environ.get("QUARTIC_LAKE_CHECKOUT"), "opt-in native Lean source inspection")
    def test_two_source_occurrences_of_one_lemma(self):
        fixture = """import Init
namespace Fixture
theorem keep (n : Nat) : n = n := rfl
theorem twice : (2 = 2) ∧ (5 = 5) :=
  ⟨keep 2,
   keep 5⟩
end Fixture
"""
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "OccurrenceFixture.lean"
            source.write_text(fixture)
            rows = json.loads(subprocess.check_output([
                "lake", "env", "lean", "--run", str(api.ROOT / "tools/ReadApplications.lean"),
                "--source", "OccurrenceFixture", str(source), "Fixture.twice=Fixture.keep"
            ], cwd=Path(os.environ["QUARTIC_LAKE_CHECKOUT"]) / "lean"))
        raw = fixture.encode()
        rows = source_records(rows, raw)
        for value in ("2", "5"):
            fragment = ("keep " + value).encode()
            start = raw.index(fragment)
            result = witnessed_occurrences(rows, "Fixture.twice", "Fixture.keep", raw, start, start + len(fragment))
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["text"], fragment.decode())
            self.assertEqual(result[0]["term"]["arguments"][0]["argument"], value)
        self.assertEqual(len(rows), 2)
        rows[0]["start"], rows[0]["end"] = rows[1]["start"], rows[1]["end"]
        with self.assertRaisesRegex(ValueError, "source bytes"):
            witnessed_occurrences(rows, "Fixture.twice", "Fixture.keep", raw, 0, len(raw))

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
            anchor = next(r for r in inspection["source_occurrences"]["QuarticQuery.LowerBound.Planted.Main"]
                          if r["term"]["callee"].endswith("Gvalue_lt_R_addressedF"))
            raw = edition.read("lean/QuarticQuery/LowerBound/Planted/Main.lean")
            # If two elaboration observations disagree on the very same source span,
            # the complete declaration evidence remains available, but no term wins the site.
            conflict = {**anchor, "term": {**anchor["term"], "arguments": []}}
            for other in (conflict, dict(anchor)):
                self.assertEqual(witnessed_occurrences([anchor, other], anchor["caller"],
                                 anchor["term"]["callee"], raw, 0, len(raw)), [])
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
const original = await resolve("original", "original/thm-1.1");
assert.equal(original.location.destination, "theorem.1.1");
assert.equal(original.text, null);
assert.equal(original.location.page, 1);
assert(original.proof.some(p => p.source.text && p.source.value.length));
const linked = original.relatedSelections[0].selections.map(s => s.paper);
for (const paper of ["exposition", "expert", "reconstruction"]) assert(linked.includes(paper));
const backlink = await reader.fromDeclaration(original.proof[0].name);
assert(backlink.treatments.some(t => t.selection === "original/thm-1.1"));
const eq21 = await resolve("original", "original/eq-21");
assert.equal(eq21.location.page, 13);
assert.equal(eq21.location.destination, "equation.21");
const generalized = await resolve("original", "original/prop-4.2-generic");
assert(generalized.matches[0].added_in_review && !generalized.location.destination);
const pdfHash = reader.documents.original.sha256;
const refs = await reader.resolve({paper:"original", page:19, documentSha256:pdfHash});
assert.equal(refs.coverage, "unmapped");
await assert.rejects(reader.resolve({paper:"original", page:1, documentSha256:"stale"}));
await assert.rejects(reader.resolve({paper:"original", page:20, documentSha256:pdfHash}));
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
const classical = family.steps.find(s => s.id === "classical-instance");
const inherited = classical.obligations.find(o => o.binder === "hLR");
assert.equal(inherited.evidence[0].basis, "caller_parameter");
assert.equal(inherited.assembly.step, "eventual-hardness");
const eventual = family.steps.find(s => s.id === inherited.assembly.step);
assert(eventual.uses.some(u => u.declaration === inherited.assembly.provider));
assert(eventual.text.includes(inherited.assembly.applied));
assert.equal(eventual.shared_board.basis, "identical_expr_under_one_existential");
assert(eventual.shared_board.function.includes("Fkm") && eventual.shared_board.circuit);
assert(classical.obligations.find(o => o.binder === "hL1").evidence.some(e => e.basis === "named_proof_term"));
const witnessed = classical.uses.find(u => u.declaration.endsWith("Gvalue_lt_R_addressedF"));
assert.equal(witnessed.attribution, "exact_source_occurrence");
assert(witnessed.occurrences.some(o => o.term.arguments.some(a => a.binder === "L" && a.argument.includes("Lvalue"))));
assert.equal(witnessed.compiled_term_scope, "declaration");
const fallback = family.steps.find(s => s.id === "upper-cost").uses[0];
assert.equal(fallback.attribution, "source_associated");
assert.deepEqual(fallback.occurrences, []);
assert(simulator.steps.every(s => s.mechanism && s.uses.length));
const fixedTime = simulator.steps.find(s => s.id === "average");
assert(fixedTime.mechanism.includes("original independent product law"));
assert(fixedTime.obligations.some(o => o.binder === "hguess"));
for (const s of simulator.steps) for (const use of s.uses)
  assert((await reader.expand(s.caller)).value.includes(use.declaration));
const tournament = await reader.journey(cycle.journeys.find(id => id === "weighted-tournament"));
assert(tournament.steps.some(s => s.caller.endsWith(".quantumDrift") && s.mechanism.includes("W/2")));
assert.equal(tournament.treatments.find(t => t.id === "cycle").correspondence_scope, "illustration");
const decoder = await reader.journey(projection.journeys.find(id => id === "sign-blind-decoder"));
assert(decoder.steps.some(s => s.id === "outputs" && s.text.includes("domainOut")));
assert(decoder.steps.some(s => s.id === "promise" && s.text.includes("decodeProb_correct")));
assert(decoder.correspondence.some(s => s.semantic_probes.some(p => p.declaration.endsWith(".absolute_high_changes_answer") && p.receipt_currentness)));
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
