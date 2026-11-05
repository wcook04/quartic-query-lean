"""Reader-facing contracts that a successful paper render alone cannot verify."""
import hashlib
import json
import shutil
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import build_reading_api as api


class ReadingEditionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.edition = api.Edition(api.ROOT)
        api.compile_edition(cls.edition)
        cls.reading = json.loads(cls.edition.resources["reading.json"])

    def resource(self, path):
        return json.loads(self.edition.resources[path])

    def test_follow_a_route_in_both_directions(self):
        routes = api.unique(self.reading["routes"], "id")
        route = routes["erased-zero"]
        reverse = self.resource("reverse.json")
        self.assertIn(route["id"], reverse["routes_by_passage"][route["reconstruction"]])
        for paper, loc in route["locations"].items():
            path = self.reading["papers"][paper]["path"]
            lines = self.edition.resources[path].decode().splitlines()
            start, end = loc["lines"]
            paragraph = "\n".join(lines[start - 1:end])
            self.assertIn(loc["quote"], paragraph)
            self.assertEqual(api.digest(paragraph.encode()), loc["sha256"])
        for label in route["lean"]:
            self.assertIn(route["id"], reverse["routes_by_target"][label])
            formal = self.resource("formal-sources.json")[label]
            lines = self.edition.resources[formal["source"]].decode().splitlines()
            for name, span in formal["ranges"].items():
                start, end = span["declaration"]
                self.assertIn(name.rsplit(".", 1)[-1], "\n".join(lines[start - 1:end]))
                self.assertIn(label, reverse["declarations"][name]["targets"])

    def test_proof_map_witnesses_are_real_typed_hops_and_never_cross_a_card(self):
        graph = self.edition.json("corpus/reading_dependencies.json")["nodes"]
        view = self.resource(self.reading["proof_map"])
        cards = view["cards"]
        root = view["root"]
        self.assertEqual(cards[root]["statements"]["thm-1.1"]["relation"], "exact")
        self.assertEqual(cards["QuarticQuery.alphaTot_eq_four_unconditional"]["statements"]["thm-1.1"]["relation"], "partial")
        edges = {(e["from"], e["to"]) for e in view["edges"]}
        for name in cards:
            path = {name}
            while name != root:
                parent = cards[name]["parent"]
                self.assertIn((parent, name), edges)
                self.assertNotIn(parent, path)
                path.add(parent)
                name = parent
        skipped = False
        for e in view["edges"]:
            for first, w in e["witnesses"].items():
                hops = []
                while w is not None:
                    w, kind, target = view["paths"][w]
                    hops.append((kind, target))
                hops.reverse()
                self.assertEqual(hops[0][0], first)
                self.assertEqual(hops[-1][1], e["to"])
                self.assertFalse(any(target in cards for _, target in hops[:-1]))
                skipped |= len(hops) > 1
                name = e["from"]
                for kind, target in hops:
                    self.assertIn(target, graph[name][kind])
                    name = target
        self.assertTrue(skipped)
        sites = self.resource(view["use_site_resource"])
        self.assertEqual(sites["kernel_index"], "current")
        exported = {(caller, kind, dep) for caller, kinds in sites["compiled_witnesses"].items()
                    for kind, targets in kinds.items() for dep in targets}
        walked = set()
        for edge in view["edges"]:
            for cursor in edge["witnesses"].values():
                while cursor is not None:
                    parent, kind, target = view["paths"][cursor]
                    walked.add((edge["from"] if parent is None else view["paths"][parent][2], kind, target))
                    cursor = parent
        self.assertEqual(walked, exported)

    def test_reference_slices_and_paper_membership_on_the_exported_map(self):
        view = self.resource(self.reading["proof_map"])
        sites = self.resource(view["use_site_resource"])
        self.assertEqual(sites["reference_index"], "current")
        helpers = self.resource(view["helper_resource"])["helpers"]
        self.assertTrue(all(h["title"] and h["title"] != n for n, h in helpers.items()))
        nodes = {**helpers, **view["cards"]}
        repeated = False
        for caller, targets in sites["observations"].items():
            raw = self.edition.resources[nodes[caller]["source"]]
            for target, regions in targets.items():
                for group in regions.values():
                    named = [s for s in group if s["basis"] == "resolved_identifier"]
                    repeated |= len({s["lines"][0] for s in named}) > 1
                    for site in group:
                        start, stop = site["utf8_bytes"]
                        self.assertEqual(raw[start:stop].decode(), site["text"])
                        self.assertEqual(site["lines"][0], 1 + raw.count(b"\n", 0, start))
                        if site in named:
                            self.assertTrue(target == site["text"] or target.endswith("." + site["text"].removeprefix(".")))
        self.assertTrue(repeated)
        for paper, rows in view["papers"].items():
            linked = {n for row in rows for n in row["bindings"]}
            self.assertEqual(view["paper_cards"][paper]["cards"], sorted(linked))
            self.assertEqual(view["paper_cards"][paper]["count"], len(linked))

    def test_statement_identifier_one_line_proof_and_shared_binder(self):
        sites = self.resource("selection/proof-use-sites.json")
        refs = sites["observations"]
        walsh = refs["QuarticQuery.Forrelation.H_transpose"]["QuarticQuery.Forrelation.W_transpose"]
        self.assertTrue(any(s["text"] == "W_transpose" and s["lines"] == [194, 194] for s in walsh["value"]))
        proof = refs["QuarticQuery.Tournament.expected_final_weight"]["QuarticQuery.Tournament.expectFrom"]
        self.assertEqual([(s["basis"], s["lines"]) for s in proof["value"]], [("compiled_rhs", [215, 215])])
        preparation = "QuarticQuery.Amplification.Preparation"
        caller = preparation + ".angle"
        param, = sites["parameter_origins"][caller][preparation]
        self.assertEqual((param["parameter"], param["text"], param["lines"]), ("A", "Preparation", [188, 188]))
        self.assertTrue(param["in_value_parameter"])
        self.assertFalse(refs.get(caller, {}).get(preparation, {}).get("value"))

    def test_exact_source_for_constructor_result_and_written_parameter(self):
        sites = self.resource("selection/proof-use-sites.json")
        upper = "QuarticQuery.Upper."
        refs = sites["observations"]
        ctor, = refs[upper + "IsCirc"][upper + "IsCirc.step"]["structural"]
        self.assertEqual((ctor["basis"], ctor["text"]), ("constructor_declaration", "step"))
        name, = refs[upper + "IsCirc.step"][upper + "ReadSpec.op"]["type"]
        self.assertEqual((name["basis"], name["text"].removeprefix(".")), ("resolved_identifier", "op"))
        result, = refs[upper + "test_samples"][upper + "Tests"]["type"]
        self.assertEqual(result["basis"], "compiled_result")
        self.assertEqual(result["lines"][0], result["lines"][1])
        caller = "QuarticQuery.Amplification.Preparation.iterate_succ"
        dep = "QuarticQuery.Amplification.groverStep"
        retained, = refs[caller][dep]["value"]
        self.assertEqual((retained["basis"], retained["text"], retained["lines"]), ("retained_tactic", "rfl", [200, 200]))
        self.assertEqual(sites["replay_status"][caller][dep], "matched")
        written = [(caller, target, s) for caller, deps in sites["parameter_origins"].items()
                   for target, origins in deps.items() for s in origins if s["basis"] == "written_parameter"]
        self.assertTrue(written)
        for caller, target, origin in written:
            self.assertIn(origin["text"], origin["domain"])
            self.assertEqual(origin["source_region"], "declaration_parameter")
            self.assertTrue(sites["compiled_witnesses"][caller]["value"][target][0].endswith(":" + origin["parameter"]))
            self.assertNotIn(origin, refs.get(caller, {}).get(target, {}).get("value", []))

    def test_proof_sites_follow_utf16_locations_and_withhold_stale_capture(self):
        from record_proof_sites import Source
        raw = "🟦 theorem τ :=\n  λ".encode()
        source = Source(raw)
        self.assertEqual(raw[source.byte(0, 3):source.byte(0, 10)], b"theorem")
        self.assertEqual(raw[source.byte(1, 2):source.byte(1, 3)].decode(), "λ")
        with self.assertRaises(UnicodeDecodeError):
            source.byte(0, 1)
        edition = api.Edition(api.ROOT)
        for inspector in ("tools/ReadUseRegions.lean", "tools/ReadKernelPaths.lean", "tools/ReadRetainedLines.lean"):
            edition.inputs[inspector] = edition.read(inspector) + b"\n"
        api.compile_edition(edition)
        stale = json.loads(edition.resources["selection/proof-use-sites.json"])
        self.assertEqual(stale["reference_index"], "stale")
        self.assertEqual(stale["replay_index"], "stale")
        self.assertEqual(stale["kernel_index"], "stale")
        self.assertEqual(stale["compiled_witnesses"], {})
        self.assertTrue(all(site["basis"] == "elaborated_application"
                            for targets in stale["observations"].values() for regions in targets.values()
                            for sites in regions.values() for site in sites))

    def test_replayed_location_must_be_an_original_tactic_node(self):
        edition = api.Edition(api.ROOT)
        path = "corpus/reading_retained_lines.json"
        record = edition.json(path)
        caller = "QuarticQuery.Amplification.Preparation.sin_two_angle"
        graph = edition.json("corpus/reading_dependencies.json")["nodes"]
        target = next(iter(self.resource("selection/proof-use-sites.json")["compiled_witnesses"][caller]["value"]))
        # One byte inside the original tactic would pass a declaration-only bounds check.
        start, stop = edition.json("corpus/reading_kernel_paths.json")["nodes"][caller]["tactic_spans"][0]
        record["completed_modules"] = [graph[caller]["module"]]
        record["requests"] = {caller: [target]}
        record["declaration_ranges"] = {caller: [start, stop]}
        record["nodes"] = {caller: {target: [[start, start + 1]]}}
        edition.inputs[path] = json.dumps(record).encode()
        with self.assertRaisesRegex(ValueError, "outside verified tactic syntax"):
            api.compile_edition(edition)

    def test_kernel_capture_is_bound_to_its_dependency_record(self):
        edition = api.Edition(api.ROOT)
        path = "corpus/reading_kernel_paths.json"
        record = edition.json(path)
        record["dependency_sha256"] = "0" * 64
        edition.inputs[path] = json.dumps(record).encode()
        api.compile_edition(edition)
        sites = json.loads(edition.resources["selection/proof-use-sites.json"])
        self.assertEqual(sites["kernel_index"], "stale")
        self.assertEqual(sites["compiled_witnesses"], {})
        self.assertEqual(sites["reference_index"], "current")
        self.assertTrue(sites["observations"])

    def test_condensation_preserves_distinct_first_uses_and_stops_at_visible_cards(self):
        from reading_proof_map import map_edges, proof_map
        nodes = {n: {"value": [], "type": [], "structural": []} for n in "ABCDE"}
        nodes["A"].update(type=["B"], value=["C"])
        nodes["B"]["value"] = ["D"]
        nodes["C"]["structural"] = ["D", "external"]
        nodes["D"]["value"] = ["E", "A"]
        edges, paths = map_edges(nodes, {"A", "D", "E"})
        links = {(e["from"], e["to"]): e["witnesses"] for e in edges}
        self.assertEqual(set(links), {("A", "D"), ("D", "E"), ("D", "A")})
        self.assertEqual(set(links["A", "D"]), {"type", "value"})
        self.assertEqual(paths[links["A", "D"]["value"]][1:], ["structural", "D"])
        stale = proof_map(self.edition, {"currentness": "stale", "source_snapshot_sha256": "previous"}, {}, {}, {}, {})
        self.assertEqual(stale["currentness"], "stale")
        self.assertNotIn("edges", stale)

    def test_board_tasks_and_their_bound_entrance(self):
        known, hidden, pointers = self.resource(self.reading["board_example"])["scenes"]
        self.assertEqual(known["selections"][0]["id"], self.reading["entrances"]["exposition"]["first_selection"])
        differences = [(r+1, c+1) for r, row in enumerate(known["original"]) for c, bit in enumerate(row)
                       if bit != known["alternative"][r][c]]
        self.assertEqual(differences, [(4, 1)])
        self.assertEqual(hidden["fixed_row_strategy"][2],
                         {"rows_read": 2, "queries_per_board": 8, "difference_seen": {"numerator": 2, "denominator": 4}})
        self.assertEqual(pointers["correct_target_bits"], [0, 0, 0])
        self.assertEqual(pointers["altered_target_bits"], [1, 0, 0])
        self.assertEqual(pointers["rival_target_bits"], [1, 1, 1])

    @unittest.skipUnless(shutil.which("pandoc"), "Pandoc needed for the web manuscript export")
    def test_whole_manuscripts_preserve_math_tables_destinations_and_sources(self):
        edition = api.Edition(api.ROOT)
        api.compile_edition(edition, web_manuscripts=True)
        papers = json.loads(edition.resources["reading.json"])["papers"]
        class Tags(HTMLParser):
            def handle_starttag(self, tag, attrs):
                tags.append((tag, dict(attrs)))
        for key in [*api.PAPERS, "verification"]:
            descriptor = papers[key]
            tags = []
            Tags().feed(edition.resources[descriptor["rendered"]["resource"]].decode())
            ids = [a["id"] for _, a in tags if "id" in a]
            self.assertEqual(len(ids), len(set(ids)))
            for section in descriptor["contents"]:
                self.assertIn(section["anchor"], ids)
                self.assertGreaterEqual(section["end_line"], section["line"])
            if key == "reconstruction":
                self.assertFalse(descriptor["contents"][0]["listed"])
                self.assertTrue(any(h["anchor"] == "the-theorem-and-the-construction" for h in descriptor["contents"]))
            for _, a in tags:
                if a.get("href", "").startswith("#"):
                    self.assertIn(a["href"][1:], ids)
            figures = {a["data-resource"] for tag, a in tags if tag == "img"}
            self.assertEqual(figures, set(descriptor["assets"]))
            if key in ("exposition", "expert"):
                cited_keys = {k for _, a in tags for k in a.get("data-cites", "").split()}
                linked_refs = {a["href"] for _, a in tags if a.get("role") == "doc-biblioref"}
                self.assertTrue(cited_keys)
                self.assertTrue({"#ref-" + k for k in cited_keys} <= linked_refs)
                notes = {a["id"]: a["href"] for _, a in tags if a.get("role") == "doc-noteref"}
                backlinks = {a["href"] for _, a in tags if a.get("role") == "doc-backlink"}
                self.assertEqual(set(notes), {ref[1:] for ref in backlinks})
                self.assertTrue(notes)
                for ref, dest in notes.items():
                    self.assertRegex(dest, r"^#fn[0-9]+$")
                    self.assertEqual(ref, "fnref" + dest[3:])
            if key == "reconstruction":
                self.assertIn("ROOT-RESULT", ids)
                self.assertTrue(any(tag == "table" for tag, _ in tags))
                self.assertTrue(any(a.get("class") == "math display" for _, a in tags))
                self.assertTrue(any(a.get("data-paper") == "exposition" for _, a in tags))
            if key == "exposition":
                self.assertTrue(any(i.startswith("fnref") for i in ids))
                self.assertTrue(any(i.startswith("ref-") for i in ids))
                first = self.resource("selection/board.json")["scenes"][0]["selections"][0]
                start = first["lines"][0]
                self.assertTrue(any(int(a["data-l0"]) == start for _, a in tags if "data-l0" in a))

    def test_four_papers_and_distinct_coverage_units(self):
        self.assertEqual(set(self.reading["paper_ids"]), {*api.PAPERS, "original"})
        self.assertEqual(self.reading["supplement_ids"], ["verification"])
        original = self.reading["papers"]["original"]
        self.assertEqual(original["format"], "pdf")
        self.assertNotIn("resource", original)
        for paper, counts in self.reading["coverage"].items():
            rows = self.resource(f"selection/{paper}.json")
            self.assertEqual(len(rows), counts["selections"])
            self.assertEqual(counts["source_sha256"], self.resource("selection/index.json")["documents"][paper]["sha256"])
        statements = {r["id"]: r for r in self.edition.json("corpus/statements.json")}
        rows = self.resource("selection/original.json")
        self.assertEqual(sorted(r["statements"][0] for r in rows), sorted(statements))
        with tempfile.TemporaryDirectory() as directory:
            wrong = Path(directory) / "original.pdf"
            wrong.write_bytes(b"%PDF-other")
            with self.assertRaisesRegex(ValueError, "pinned release"):
                api.original_paper(self.edition, statements, wrong)
        statements["eq-21"] = {**statements["eq-21"], "source_line": 1}
        with self.assertRaisesRegex(ValueError, "coordinates changed"):
            api.original_paper(self.edition, statements)

    def test_every_reviewed_tie_has_its_own_native_type_and_axioms(self):
        for sid, path in self.reading["fidelity"].items():
            record = self.resource(path)
            for tie in record["lean"]:
                if tie["review_evidence"] != "current":
                    continue
                native = tie["inspection"]
                self.assertEqual(native["status"], "current", sid)
                self.assertEqual("lean/" + native["module"].replace(".", "/") + ".lean", tie["file"])
                self.assertTrue(native["type"].strip())
                self.assertIsInstance(native["axioms"], list)
            for probe in record["semantic_probes"]:
                self.assertEqual(probe["inspection"]["status"], "current")
                self.assertTrue(probe["authored_answer"])
        amended = self.resource("fidelity/lem-2.2.i.json")
        self.assertNotEqual(amended["ledger_history"]["earlier_ledger_wording"], amended["statement"])
        self.assertIn("R1-AF-00", [f["id"] for f in amended["ledger_history"]["adjudication_findings"]])

    def test_changed_inspector_withholds_current_types_and_axioms(self):
        edition = api.Edition(api.ROOT)
        inspector = "tools/ReadStatementEvidence.lean"
        edition.inputs[inspector] = edition.read(inspector) + b"\n"
        api.compile_edition(edition)
        headline = json.loads(edition.resources["fidelity/thm-1.1.json"])
        tie = next(t for t in headline["lean"] if t["declaration"].endswith(".theorem_1_1_unconditional"))
        self.assertEqual(tie["inspection"]["status"], "stale")
        self.assertNotIn("axioms", tie["inspection"])
        self.assertNotIn("type", tie["inspection"])
        self.assertNotIn(tie["declaration"], json.loads(edition.resources["axiom-audits.json"]))
        model = json.loads(edition.resources["fidelity/def-R.json"])
        self.assertTrue(all(p["authored_answer"] is None for p in model["semantic_probes"]))

    def test_feedback_is_qualified_and_attributed(self):
        self.assertEqual(set(self.reading["entrances"]), {*api.PAPERS, "original"})
        self.assertEqual(self.reading["video"], self.edition.json(api.ROUTES)["video"])
        statement = self.resource(self.reading["fidelity"]["def-R"])
        self.assertTrue(any(t["reviewed_by"] for t in statement["lean"]))
        probe = next(p for p in statement["semantic_probes"] if "quantifier" in p["declaration"])
        self.assertIn(probe["declaration"], self.resource(probe["receipt"])["declarations"])
        self.assertIn(probe["declaration"], self.resource("axiom-audits.json"))
        control = self.resource("checks.json")["lean/QuarticCorpus/Independent/Controls/shared_blind_spot.json"]
        self.assertEqual(control["role"], "negative_control")
        self.assertEqual(control["latest_receipt"]["negative_control"], "accepted_shared_bad_spec_blind_spot")
        self.assertEqual(self.resource("provenance.json")["routes"]["origin"], "ai_authored_navigation")

    def test_stale_or_ambiguous_selector_and_bad_video(self):
        for text in ("different", "quote and quote"):
            with self.assertRaisesRegex(ValueError, "expected one"):
                api.locate_quote(text, "quote", "expert")
        video = {"youtube_id": "abcdefghijk", "chapters": [{"start_seconds": 0, "route": "pivot"}]}
        self.assertEqual(api.video_entry(video, {"pivot"}), video)
        with self.assertRaisesRegex(ValueError, "chapter"):
            api.video_entry(video, {})
        video["chapters"] *= 2
        with self.assertRaisesRegex(ValueError, "chapter"):
            api.video_entry(video, {"pivot"})

    def test_wrong_pdf_cannot_enter_an_edition(self):
        accepted = self.edition.json(api.ROUTES)["print_edition"]
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            path = folder / accepted["files"]["expert"]["file"]
            path.parent.mkdir()
            path.write_bytes(b"%PDF-unrelated edition")
            with self.assertRaisesRegex(ValueError, "PDF differs|paper sources differ"):
                api.print_downloads(self.edition, folder, accepted)

    def test_export_retains_old_objects_and_refuses_mixed_editions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args):
                subprocess.run(["git", "-c", "user.email=test@example.com", "-c", "user.name=Test", *args],
                               cwd=root, check=True, capture_output=True)
            git("init")
            source = root / "paper.md"
            out = root / "output"
            def snapshot():
                edition = api.Edition(root)
                edition.resources["paper.md"] = edition.read("paper.md")
                api.export(edition, out)
                return json.loads((out / "index.json").read_bytes())
            source.write_bytes(b"first")
            git("add", "paper.md")
            git("commit", "-m", "first")
            first = snapshot()
            source.write_bytes(b"next")
            with self.assertRaisesRegex(ValueError, "differs"):
                snapshot()
            self.assertEqual(first, json.loads((out / "index.json").read_bytes()))
            git("commit", "-am", "next")
            second = snapshot()
            self.assertNotEqual(first["revision"], second["revision"])
            for manifest, expected in [(first, b"first"), (second, b"next")]:
                entry = manifest["resources"]["paper.md"]
                self.assertEqual((out / entry["href"]).read_bytes(), expected)
                self.assertEqual(entry["sha256"], hashlib.sha256(expected).hexdigest())
            self.assertEqual(snapshot(), second)
