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

    @unittest.skipUnless(os.environ.get("QUARTIC_LAKE_CHECKOUT"), "opt-in native parameter inspection")
    def test_shadowed_and_unused_section_parameters(self):
        fixture = """import Init
namespace QuarticQuery.Fixture
structure Box where
  n : Nat
section
variable (x : Box)
def outer := x.n
section
variable (x : Box)
def inner := x.n
def unused := 2
def explicit (x : Box) := x.n
end
def resumed := x.n
def returned : (x : Box) → Nat := fun x => x.n
end
end QuarticQuery.Fixture
"""
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "ParameterFixture.lean"
            source.write_text(fixture)
            rows = json.loads(subprocess.check_output([
                "lake", "env", "lean", "--run", str(api.ROOT / "tools/ReadParameterOrigins.lean"),
                "ParameterFixture", str(source)
            ], cwd=Path(os.environ["QUARTIC_LAKE_CHECKOUT"]) / "lean"))
        first = fixture.index("(x : Box)")
        second = fixture.index("(x : Box)", first + 1)
        self.assertEqual({(r["caller"].split(".")[-1], r["lo"], r["value"]) for r in rows},
                         {("outer", first, True), ("inner", second, True), ("resumed", first, True)})

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
    def test_declaration_titles_are_lazy_and_bound_to_the_selected_edition(self):
        script = r"""
import assert from "node:assert/strict";
import {createHash} from "node:crypto";
import {openEdition} from "./tools/reader.mjs";
const revision = "a".repeat(40), otherRevision = "b".repeat(40);
const base = new URL("https://example.test/reading/v1/");
const hash = bytes => createHash("sha256").update(bytes).digest("hex");
const canonical = value => Array.isArray(value) ? "["+value.map(canonical).join(",")+"]"
  : value && typeof value === "object" ? "{"+Object.keys(value).sort().map(k => JSON.stringify(k)+":"+canonical(value[k])).join(",")+"}"
  : JSON.stringify(value);
const goal = "QuarticQuery.goal", helper = "QuarticQuery.helper";
const map = {revision,currentness:"current",root:goal,source_snapshot_sha256:"source",
  helper_resource:"selection/proof-helpers.json",cards:{[goal]:{title:"The `$x$` result",source:"Goal.lean",lines:[1,2],kind:"theorem"}},
  edges:[{from:goal,to:helper,witnesses:{value:0}}],paths:[[null,"value",helper]]};
const helpers = {revision,source_snapshot_sha256:"source",helpers:{[helper]:{title:"A $y$ helper",source:"Helper.lean",lines:[1,2],kind:"lemma"},
  "QuarticQuery.noTitle":{title:null}}};
function host(extra) {
  const objects = new Map(), resources = {};
  for (const [path, value] of Object.entries({"selection/start.json":{revision,documents:{},home:{}},...extra})) {
    const raw = new TextEncoder().encode(canonical(value)+"\n"), sha256 = hash(raw);
    const href = `objects/${sha256}.json`;
    resources[path] = {sha256,href,bytes:raw.length};
    objects.set(href,raw);
  }
  const payload = {schema:"quartic-reading-api-v1",revision,repository:"https://example.test/project",resources};
  const permalink = `edition-${hash(canonical(payload)+"\n")}.json`;
  const manifest = {...payload,permalink}, requests = [];
  return {requests,permalink,fetch:async (url, opts) => {
    assert.equal(opts.redirect,"error");
    const path = url.href.slice(base.href.length);
    requests.push(path);
    if (path === permalink) return Response.json(manifest);
    assert(objects.has(path),`Unexpected resource request: ${path}`);
    return new Response(objects.get(path));
  }};
}
async function open(extra) {
  const server = host(extra);
  return {server,reader:await openEdition(base,{edition:server.permalink,fetch:server.fetch})};
}
const canonicalTitle = {title:"A $\\sqrt{x}$ result",title_plain:"A square-root result"};
const current = await open({"selection/declaration-titles.json":{revision,status:"current",titles:{[goal]:canonicalTitle}},
  "selection/proof-map.json":{...map,cards:{[goal]:{...map.cards[goal],...canonicalTitle}}}});
assert.equal(current.server.requests.length,2,"Opening an edition never fetches declaration titles or the graph");
await current.reader.home();
assert.equal(current.server.requests.length,2);
const titles = await current.reader.declarationTitles();
assert.deepEqual(titles,{revision,status:"current",titles:{[goal]:canonicalTitle}});
assert.equal(current.server.requests.length,3,"Titles load one compact resource, without the graph or sources");
assert.deepEqual(await current.reader.declarationTitle(goal),{revision,name:goal,status:"current",...canonicalTitle});
assert.equal((await current.reader.declarationTitle("QuarticQuery.unknown")).status,"missing_title");
assert.equal((await current.reader.declarationTitle("And")).title,null);
await current.reader.declarationTitles();
assert.equal(current.server.requests.length,3,"Repeated and singular lookups share the verified resource");
assert.equal((await current.reader.proofMap()).cards[goal].title_plain,"A square-root result","Modern plain titles are never inferred from TeX");

const archived = await open({"selection/proof-map.json":map,"selection/proof-helpers.json":helpers});
assert.equal(archived.server.requests.length,2);
const oldMap = await archived.reader.proofMap();
assert.equal(archived.server.requests.length,3,"Opening a legacy graph does not fetch all helpers");
assert.equal(oldMap.cards[goal].title_plain,"The x result");
const captured = await archived.reader.declarationTitles();
assert.equal(captured.status,"archived_partial");
assert.deepEqual(captured.titles[goal],{title:"The `$x$` result",title_plain:"The x result"});
assert.deepEqual(captured.titles[helper],{title:"A $y$ helper",title_plain:"A y helper"});
assert(!Object.hasOwn(captured.titles,"QuarticQuery.noTitle"));
assert.equal(archived.server.requests.length,4,"Only this edition's captured card and helper titles are read");
assert.equal((await archived.reader.declarationTitle(goal)).status,"archived_partial");
const absent = await archived.reader.declarationTitle("QuarticQuery.unknown");
assert.equal(absent.status,"missing_title");
assert.equal(absent.titleIndexStatus,"archived_partial");
assert.equal(absent.title,null);
const path = await archived.reader.proofPath(goal,helper);
assert.equal(path.declarations[helper].title_plain,"A y helper");

const empty = await open({});
assert.deepEqual(await empty.reader.statementTitles(),{revision,status:"unavailable_in_edition",titles:{}});
const mixedStatements = await open({"selection/statement-titles.json":{revision:otherRevision,titles:{}}});
await assert.rejects(mixedStatements.reader.statementTitles(),/Mixed paper and graph editions/);
assert.deepEqual(await empty.reader.declarationTitles(),{revision,status:"unavailable_in_edition",titles:{}});
assert.equal(empty.server.requests.length,2,"Absent legacy title resources cause no speculative fetches");
const stale = await open({"selection/proof-map.json":{...map,currentness:"stale"},"selection/proof-helpers.json":helpers});
assert.deepEqual(await stale.reader.declarationTitles(),{revision,status:"stale",titles:{}});
assert.equal(stale.server.requests.length,3,"Stale graph titles are not recovered from helpers");
const staleIndex = await open({"selection/declaration-titles.json":{revision,status:"stale",titles:{[goal]:canonicalTitle}}});
assert.deepEqual(await staleIndex.reader.declarationTitles(),{revision,status:"stale",titles:{}});
const mixed = await open({"selection/declaration-titles.json":{revision:otherRevision,status:"current",titles:{[goal]:canonicalTitle}}});
await assert.rejects(mixed.reader.declarationTitles(),/Mixed paper and graph editions/);
const malformed = await open({"selection/declaration-titles.json":{revision,titles:{[goal]:canonicalTitle}}});
await assert.rejects(malformed.reader.declarationTitles(),/Invalid declaration title index/);
const mixedHelpers = await open({"selection/proof-map.json":map,
  "selection/proof-helpers.json":{...helpers,source_snapshot_sha256:"another source"}});
await assert.rejects(mixedHelpers.reader.declarationTitles(),/Mixed proof path sources/);
"""
        subprocess.run(["node", "--input-type=module", "-"], cwd=api.ROOT,
                       input=script, text=True, check=True)

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
// Shared links supply filenames only. Exercise the browser's trusted client
// under a deployment prefix with the real export as a mock static host.
const {openEdition, loadEditionResources} = await import("./tools/reader.mjs");
const {readFile} = await import("node:fs/promises");
const {dirname, join} = await import("node:path");
const {createHash} = await import("node:crypto");
const base = new URL("https://example.test/quartic/v1/");
const folder = dirname(process.argv[2]);
const info = JSON.parse(await readFile(process.argv[2]));
let count = 0, corrupt = false, corruptFigure;
async function request(url, opts) {
  count++;
  assert.equal(opts.redirect, "error");
  assert(url.href.startsWith(base.href));
  const path = url.href.slice(base.href.length);
  const bytes = await readFile(join(folder,path));
  if (corrupt && path === info.resources["docs/exposition.md"].href) bytes[0] ^= 1;
  if (path === corruptFigure) bytes[0] ^= 1;
  return new Response(bytes);
}
for (const bad of ["//outside.test/m.json","https://outside.test/index.json","../index.json","%2e%2e/foo","index.json"])
  await assert.rejects(openEdition(base,{edition:bad,fetch:request}),/Invalid edition permalink/);
assert.equal(count,0);
const trusted = await openEdition(base,{edition:info.permalink,fetch:request});
const front = await trusted.home();
assert.equal(count,2,"Opening the guide needs just its manifest and the compact start resource");
assert.equal(front.entrances.exposition.first_selection, front.board.scenes[0].selections[0].id);
for (const [paper, entry] of Object.entries(front.entrances)) {
  assert((await trusted.resource(`selection/${paper}.json`)).some(r => r.id === entry.first_selection));
}
const requestsBeforeMap = count;
const map = await trusted.proofMap();
assert.equal(count, requestsBeforeMap + 1);
const focus = await trusted.proofFocus({paper:"original",id:"original/thm-1.1"});
assert(focus.cards.includes(map.root));
// The complete theorem leads; conditional helpers with the same conclusion follow it.
assert.equal(focus.cards[0], map.root);
assert.equal((await trusted.proofFocus({paper:"expert",id:"expert/headline/0"})).cards[0], map.root);
assert.deepEqual((await trusted.proofFocus({paper:"original",page:19})).cards, []);
const boardFocus = await trusted.proofFocus({paper:"exposition",id:front.entrances.exposition.first_selection});
assert.deepEqual(boardFocus.cards, []);
const edge = map.edges.find(e => Object.hasOwn(e.witnesses,"value") && map.paths[e.witnesses.value][0] !== null);
const hops = await trusted.proofWitness(edge.from,edge.to,"value");
assert.equal(hops[0].from,edge.from);
assert.equal(hops.at(-1).to,edge.to);
assert.equal(count, requestsBeforeMap + 1);
assert((await trusted.proofCardSource(map.root)).text.includes("theorem theorem_1_1_unconditional"));
assert.equal(count, requestsBeforeMap + 2);
const direct = map.edges.find(e => Object.values(e.witnesses).every(w => map.paths[w][0] === null));
const beforeDetails = count;
assert((await trusted.proofPath(direct.from,direct.to)).variants.every(v => v.helperCount === 0));
assert.equal(count,beforeDetails+1); // Verified source-use index is loaded on arrow click.
const from = "QuarticQuery.Upper.familyBoundsAt_of_lower", to = "QuarticQuery.Forrelation.forrConstant";
const detail = await trusted.proofPath(from,to,"value");
assert.equal(count,beforeDetails+2); // One verified helper catalog. Source stays on demand.
const helper = "QuarticQuery.Upper.budgetConst_pos";
assert.deepEqual(detail.variants[0].hops.map(h => [h.from,h.to,h.usage]), [[from,helper,"proof"],[helper,to,"proof"]]);
assert.equal(detail.variants[0].helperCount,1);
assert.deepEqual(detail.variants[0].compiledCoverage, {located:2,total:2,complete:true});
const compiled = detail.variants[0].hops[0].evidence.compiledWitness;
assert.equal(compiled.region,"body");
assert.deepEqual(compiled.leaf,{kind:"constant"});
assert(compiled.address.length > 0 && compiled.address.every(s => typeof s === "string"));
assert.equal(detail.variants[0].hops[0].evidence.status,"resolved_identifier");
const use = detail.variants[0].hops[0].evidence.sites.find(s=>s.text==="budgetConst_pos");
assert.match(use.url,/#L309-L309$/);
assert.deepEqual(use.lines,[309,309]);
const sourceLine=(await trusted.readText(detail.declarations[from].source)).split("\n")[308];
assert.equal(sourceLine.slice(...use.utf16_columns),use.text);
assert.equal(use.region,"value");
assert(detail.declarations[helper].title.includes("positive"));
const progress = await trusted.paperCardProgress({paper:"original",edition:trusted.permalink,
  visited:["original/thm-1.1","original/thm-1.1"],through:1});
assert.equal(progress.total,new Set(progress.cards).size);
assert(progress.visited.cards.includes(map.root));
assert.equal(progress.visited.count,new Set(progress.visited.cards).size);
assert(progress.through.count>=progress.visited.count);
const empty = await trusted.paperCardProgress({paper:"exposition",edition:trusted.permalink,visited:[front.entrances.exposition.first_selection]});
assert.equal(empty.visited.count,0);
await assert.rejects(trusted.paperCardProgress({paper:"original",edition:"foreign",visited:["original/thm-1.1"]}),/different edition/);
assert.equal(detail.declarations[helper].role,"helper");
assert((await trusted.proofPathSource(helper)).text.includes("budgetConst_pos"));
const missingSpan = await trusted.proofPathSource("QuarticQuery.Amplification.Preparation.mk");
assert.equal(missingSpan.lines,null);
assert.equal(missingSpan.text,null);
assert.equal(typeof missingSpan.compiledSignature,"string");
assert(missingSpan.url.endsWith(missingSpan.source));
const fieldSource = await trusted.proofPathSource("QuarticQuery.Amplification.Preparation.good");
assert.equal(fieldSource.lines,null);
assert.equal(fieldSource.definitionSite.text, "good");
assert.match(fieldSource.definitionSite.url, /#L37-L37$/);
const prep = "QuarticQuery.Amplification.Preparation";
const anglePaths = await trusted.proofPath(prep + ".angle", prep);
const angleHop = k => anglePaths.variants.find(v => v.firstKind === k).hops[0].evidence;
assert.equal(angleHop("type").status, "inherited_parameter");
assert.match(angleHop("type").sites[0].url, /#L188-L188$/);
assert.equal(angleHop("value").status, "declaration_only");
assert.deepEqual(angleHop("value").sites, []);
assert.equal(angleHop("value").sourceLimitation, "compiled_parameter_domain");
assert.deepEqual(angleHop("value").compiledWitness.parameter.name, "A");
assert.equal(angleHop("value").parameterOrigins[0].binder, "(A : Preparation H)");
const circuit = "QuarticQuery.Amplification.Circuit";
const callPath = await trusted.proofPath(circuit + ".calls", circuit, "value");
const origin = callPath.variants[0].hops[0].evidence;
assert.deepEqual(origin.sites, []);
assert.equal(origin.compiledWitness.region, "parameter");
assert.equal(origin.parameterOrigins[0].region, "declaration_parameter");
assert.equal(origin.parameterOrigins[0].parameter, "c");
assert.match(origin.parameterOrigins[0].url, /#L60-L60$/);
const tournamentNamespace = "QuarticQuery.Tournament.";
const expectation = await trusted.proofPath(tournamentNamespace+"expected_final_weight",tournamentNamespace+"expectFrom","value");
assert.equal(expectation.variants[0].hops[0].evidence.status,"compiled_rhs");
const multiple = map.edges.find(e => Object.keys(e.witnesses).length > 1);
const choices = await trusted.proofPath(multiple.from,multiple.to);
assert.deepEqual(choices.variants.map(v => v.firstKind),Object.keys(multiple.witnesses));
for (const v of choices.variants) {
  const witness = await trusted.proofWitness(multiple.from,multiple.to,v.firstKind);
  assert.deepEqual(v.hops.map(({usage,evidence,...hop}) => hop),witness);
}
assert.equal((await trusted.proofPath("paper:thm-1.1",map.root)).status,"not_a_dependency_edge");
await assert.rejects(trusted.proofPath(from,to,"type"),/witness kind/);
await assert.rejects(trusted.proofPathSource("toString"),/Unknown proof path/);
const familyDetails = await trusted.journey("forrelation-family");
assert.deepEqual(front.family, {overview:familyDetails.overview, scaling:familyDetails.scaling});
// Simulate the earlier manifest shape while serving the actual source-only package.
const legacy = JSON.parse(JSON.stringify(info));
delete legacy.permalink;
delete legacy.resources["selection/start.json"];
delete legacy.resources["selection/proof-map.json"];
delete legacy.resources["selection/declaration-titles.json"];
delete legacy.resources["selection/by-statement.json"];
delete legacy.resources["selection/applications.json"];
legacy.permalink = "edition-"+createHash("sha256").update(JSON.stringify(legacy)+"\n").digest("hex")+".json";
const archive = await openEdition(base,{edition:legacy.permalink,fetch:(url,opts) =>
  url.pathname.endsWith(legacy.permalink) ? Response.json(legacy) : request(url,opts)});
assert.equal((await archive.proofMap()).currentness,"unavailable_in_edition");
assert.deepEqual(await archive.declarationTitles(),{revision:archive.revision,status:"unavailable_in_edition",titles:{}});
assert.equal((await archive.proofPath(from,to)).status,"unavailable_in_edition");
const archived = await archive.manuscript("exposition");
assert.equal(archived.html,null);
assert.equal(createHash("sha256").update(archived.source).digest("hex"), archive.documents.exposition.sha256);
assert.equal((await archive.home()).family,null);
const oldSelection = await archive.resolve({paper:"exposition",id:front.entrances.exposition.first_selection});
assert.equal(oldSelection.position.edition,legacy.permalink);
assert.equal(oldSelection.text,archived.source.split("\n").slice(oldSelection.lines[0]-1,oldSelection.lines[1]).join("\n"));
const first = await trusted.resolve({paper:"original",id:"original/thm-1.1"});
assert.equal((await trusted.restore(first.position)).location.page,1);
await assert.rejects(trusted.restore({...first.position,edition:"other"}),/different edition/);
await assert.rejects(trusted.restore({...first.position,documentSha256:"other"}),/different manuscript/);
corrupt = true;
await assert.rejects(trusted.readText("docs/exposition.md"), /differs/);
corrupt = false;
assert((await trusted.readText("docs/exposition.md")).includes("Finding a column"));
const img = (await trusted.resource("reading.json")).papers.exposition.assets[0];
await assert.rejects(trusted.figure("original",img),/does not belong/);
corruptFigure = info.resources[img].href;
await assert.rejects(trusted.figure("exposition",img), /differs/);
corruptFigure = undefined;
const svg = await trusted.figure("exposition",img);
assert.equal(svg.type,"image/svg+xml");
assert((await svg.text()).includes("<svg"));
const badManifest = {...info, repository:"changed"};
await assert.rejects(loadEditionResources(new URL(info.permalink,base),{fetch:async()=>Response.json(badManifest)}),/permalink/);
const dangerous = JSON.parse(JSON.stringify(info));
dangerous.resources["reader.mjs"].href = "https://outside.test/reader.mjs";
delete dangerous.permalink;
dangerous.permalink = "edition-"+createHash("sha256").update(JSON.stringify(dangerous)+"\n").digest("hex")+".json";
await assert.rejects(loadEditionResources(new URL(dangerous.permalink,base),{fetch:async()=>Response.json(dangerous)}),/Invalid edition resource/);
const resolve = (paper, id) => reader.resolve({paper, id});
const find = (r, name) => r.proof.find(n => n.name.endsWith(name));
const review = await reader.statementReview("thm-1.1");
const statementIndex = await reader.statementTitles();
assert.equal(statementIndex.status, "current");
assert.deepEqual(statementIndex.titles[review.id], {title: review.presentation.title, title_plain: review.presentation.title_plain});
assert((await reader.statementReview("eq-13")).presentation.body.includes("$"));
assert.equal(review.paper.selection.location.destination, "theorem.1.1");
assert.equal(review.comparisons[0].declaration, "QuarticQuery.theorem_1_1_unconditional");
assert.equal(review.comparisons[0].relation, "exact");
assert(review.comparisons[0].rawLean.includes("theorem theorem_1_1_unconditional"));
assert(review.comparisons[0].inspection.type.includes("UniversalPower"));
assert(review.comparisons.some(c => c.declaration.endsWith(".alphaTot_eq_four_unconditional") && c.relation === "partial"));
assert.equal(review.scope.semantic_examples, "none_indexed");
const audit = (await reader.fromDeclaration(review.comparisons[0].declaration)).axiomAudit;
assert.equal(audit.snapshot_currentness, "current");
assert.deepEqual(audit.axioms, review.comparisons[0].inspection.axioms);
const cap = await reader.statementReview("eq-21");
assert(cap.comparisons[0].declaration.endsWith(".eq_21"));
assert(cap.comparisons[0].inspection.type.includes("Paper.reachedCellAt"));
assert(cap.comparisons[0].inspection.type.includes("prodW (QuarticQuery.prodW μ)"));
const model = await reader.statementReview("def-R");
assert(model.semanticExamples.some(p => p.kind === "alternative_definition" &&
  p.inspection.type.includes("oneBitIdentity") && p.inspection.status === "current"));
await assert.rejects(reader.statementReview("nonexistent"));
const original = await resolve("original", "original/thm-1.1");
assert.deepEqual(original.statements.find(s => s.id === review.id).presentation, review.presentation);
assert.equal(original.location.destination, "theorem.1.1");
assert.equal(original.text, null);
assert.equal(original.location.page, 1);
assert(original.proof.some(p => p.source.text && p.source.value.length));
const linked = original.relatedSelections[0].selections.map(s => s.paper);
for (const paper of ["exposition", "expert", "reconstruction"]) assert(linked.includes(paper));
const backlink = await reader.fromDeclaration(original.proof[0].name);
assert(backlink.treatments.some(t => t.selection === "original/thm-1.1" && t.statement === "thm-1.1" && t.review === "current"));
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
assert.deepEqual(family.overview.find(g => g.id === "assembly").after, ["quantum","classical"]);
assert.equal(family.scaling.examples.find(e => e.k === 4).classical_power_in_sqrt_m,"7/2");
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
