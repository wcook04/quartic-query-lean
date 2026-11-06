// Read-only client for the static Quartic selection API. All mathematical joins
// and graph edges come from the captured edition. No text similarity search.
export async function openReader(indexURL, {fetch: request = globalThis.fetch, expectedRevision} = {}) {
  const index = new URL(indexURL);
  async function bytes(url) {
    const response = await request(url);
    if (!response.ok) throw new Error(`HTTP ${response.status} for ${url}`);
    return response.arrayBuffer();
  }
  const decode = raw => new TextDecoder().decode(raw);
  const manifest = JSON.parse(decode(await bytes(index)));
  const revision = manifest.revision;
  if (manifest.schema !== "quartic-reading-api-v1" || (expectedRevision && expectedRevision !== revision))
    throw new Error("Reading edition mismatch");

  const cache = new Map();
  function resource(path) {
    if (!cache.has(path)) {
      const entry = manifest.resources[path];
      if (!entry) throw new Error(`Missing edition resource: ${path}`);
      cache.set(path, bytes(new URL(entry.href, index)).then(raw => {
        if (raw.byteLength !== entry.bytes) throw new Error(`Incomplete resource: ${path}`);
        return path.endsWith(".json") ? JSON.parse(decode(raw)) : decode(raw);
      }).catch(error => { cache.delete(path); throw error; }));
    }
    return cache.get(path);
  }
  const selection = await resource("selection/index.json");
  if (selection.revision !== revision) throw new Error("Mixed paper and graph editions");
  const {modules, documents} = selection;
  async function expand(name) {
    if (!Object.hasOwn(modules, name)) {
      const external = await resource("selection/external.json");
      const module = external.modules[name];
      if (typeof module !== "string") return {name, status: "outside_recorded_graph"};
      const owner = {Mathlib: "mathlib", Complexity: "complexitylib", Cslib: "cslib"}[module.split(".")[0]];
      const pkg = external.packages[owner];
      const url = pkg && `${pkg.url.replace(/\.git$/, "")}/blob/${pkg.revision}/${module.replaceAll(".", "/")}.lean`;
      return {name, module, status: "external_module_boundary", url: url ?? null};
    }
    const shard = await resource(`proof/${modules[name]}.json`);
    const node = shard.nodes[name];
    return {name, status: "recorded", module: modules[name], source: shard.source, ...node};
  }

  // Search only inside the recorded project. Stop at the first associated
  // declaration on each path; retain one shortest, typed witness per endpoint.
  async function neighbourhood(root, direction, associated, {depth = 4, limit = 8, budget = 120} = {}) {
    for (const n of [depth, limit, budget])
      if (!Number.isSafeInteger(n) || n < 1) throw new Error("Invalid graph budget");
    if (direction !== "uses" && direction !== "used_by") throw new Error("Unknown graph direction");
    const queue = [{name: root, path: []}], seen = new Set([root]), witnesses = [];
    let visited = 0, externalEdges = 0, depthLimited = false, limitReached = false;
    while (visited < queue.length && visited < budget && !limitReached) {
      const {name, path} = queue[visited++];
      const node = await expand(name);
      if (node.status !== "recorded") continue;
      const adjacent = direction === "uses" ? node : node.incoming;
      for (const kind of ["value", "type", "structural"]) {
        for (const next of adjacent[kind] || []) {
          if (!Object.hasOwn(modules, next)) { externalEdges++; continue; }
          if (seen.has(next)) continue;
          seen.add(next);
          const edge = direction === "uses" ? {from: name, to: next, kind} : {from: next, to: name, kind};
          const trace = [...path, edge];
          if (Object.hasOwn(associated, next)) {
            witnesses.push({name: next, path: trace});
            if (witnesses.length >= limit) { limitReached = true; break; }
          } else if (trace.length < depth) {
            queue.push({name: next, path: trace});
          } else depthLimited = true;
        }
        if (limitReached) break;
      }
    }
    return {root, direction, witnesses, externalEdges, visited, limitReached, depthLimited,
            budgetLimited: visited < queue.length && visited >= budget, bounds: {depth, limit, budget}};
  }

  async function declaration(name) {
    const node = await expand(name);
    if (!node.source || !node.lines) return node;
    const [start, end] = node.lines;
    const text = (await resource(node.source)).split("\n").slice(start-1, end).join("\n");
    return {...node, text, url: `${manifest.repository}/blob/${revision}/${node.source}#L${start}-L${end}`};
  }

  async function fromDeclaration(name) {
    const [reverse, source] = await Promise.all([resource("selection/reverse.json"), declaration(name)]);
    return {revision, name, source, treatments: Object.hasOwn(reverse, name) ? reverse[name] : []};
  }

  async function resolve({paper, line, endLine = line, id, documentSha256}, bounds) {
    if (!Object.hasOwn(documents, paper)) throw new Error("Unknown paper");
    const doc = documents[paper];
    if ((id == null || documentSha256 != null) && documentSha256 !== doc.sha256)
      throw new Error("Selection belongs to a different manuscript edition");
    if (id == null && (!Number.isSafeInteger(line) || !Number.isSafeInteger(endLine) ||
        line < 1 || line > endLine || endLine > doc.lines)) throw new Error("Invalid paper range");
    const [rows, argumentsData, labels, associated] = await Promise.all([
      resource(`selection/${paper}.json`), resource("selection/arguments.json"),
      resource("selection/targets.json"), resource("selection/reverse.json")]);
    if (id != null) {
      const owner = rows.find(r => r.id === id);
      if (!owner) throw new Error(`Unknown selection: ${id}`);
      [line, endLine] = owner.lines;
    }
    const matches = rows.filter(r => (r.lines[0] <= line && endLine <= r.lines[1]) ||
        ((r.label || r.referenced_passage) && line <= r.lines[0] && r.lines[1] <= endLine));
    const markedClaim = matches.some(r => r.claim);
    const topics = [...new Set(matches.map(r => r.topic).filter(Boolean))];
    const statements = new Set(), targets = new Set(), roots = new Map();
    function root(name, basis) {
      if (!roots.has(name)) roots.set(name, []);
      roots.get(name).push(basis);
    }
    for (const row of matches) {
      if (!markedClaim || !row.id.startsWith("passage/"))
        for (const sid of row.statements || []) statements.add(sid);
      if (row.label) targets.add(row.label);
    }
    for (const id of topics) {
      const topic = argumentsData.topics[id];
      for (const sid of topic.statements) statements.add(sid);
      for (const label of topic.labels) targets.add(label);
      for (const name of topic.constituents) root(name, {basis: "editorial_constituent", topic: id});
    }
    const records = await Promise.all([...statements].map(s => resource(`fidelity/${s}.json`)));
    for (const row of records) {
      for (const tie of row.lean) {
        const module = modules[tie.declaration];
        if (module && tie.file === `lean/${module.replaceAll(".", "/")}.lean`)
          root(tie.declaration, {basis: "statement_tie", statement: row.id, relation: tie.relation,
              route: tie.route, review: tie.review_evidence});
      }
    }
    const cited = [...targets].flatMap(label => labels[label]);
    for (const target of cited) for (const join of target.graph_joins)
      root(join.name, {basis: join.basis, label: target.label, source: join.source});
    const proof = await Promise.all([...roots].map(async ([name, basis]) => ({
      name, basis, source: await declaration(name), uses: await neighbourhood(name, "uses", associated, bounds),
      used_by: await neighbourhood(name, "used_by", associated, bounds)
    })));
    const lines = [line, endLine];
    const text = (await resource(doc.path)).split("\n").slice(lines[0]-1, lines[1]).join("\n");
    const [users, checks] = await Promise.all([resource("selection/statement-users.json"), resource("checks.json")]);
    const checkIDs = new Set(records.flatMap(s => s.lean.flatMap(t => t.configured_checks)));
    for (const target of cited) {
      for (const [path, config] of Object.entries(checks)) {
        if (target.url.includes("/" + config.challenge + "#") && config.theorem_names.includes(target.name))
          checkIDs.add(path);
      }
    }
    const comparisons = [...checkIDs].map(path => {
      const c = checks[path], r = c.latest_receipt;
      return {path, role: c.role, configuredNames: c.theorem_names, permittedAxioms: c.permitted_axioms,
              outcome: r?.negative_control ?? r?.status ?? "not_recorded",
              currentness: r?.currentness ?? "not_recorded", receipt: r?.receipt ?? null};
    });
    const paperData = (await resource("reading.json")).papers[paper];
    const headings = [];
    for (const h of paperData.outline) {
      if (h.line > line) break;
      while (headings.length && headings.at(-1).level >= h.level) headings.pop();
      headings.push(h);
    }
    const figures = topics.map(id => argumentsData.topics[id].figure).filter(Boolean);
    const citations = [...text.matchAll(/@([A-Za-z][\w:-]*)/g)].map(m => m[1]);
    return {revision, document: doc, paper, lines, text, matches, comparisons,
      context: {headings, figures, bibliography: paperData.bibliography, citationKeys: [...new Set(citations)]},
      scope: "Review judgments apply to their named statement and declaration. Editorial examples and constituents retain their indicated roles.",
      statementDependencies: records.map(s => ({id: s.id, requires: s.depends_on,
          usedBy: users[s.id] || [], externalInputs: s.external_inputs})),
      coverage: matches.length ? (proof.length || cited.length ? "associated_targets" : "passage_only") : "unmapped",
      topics: topics.map(id => ({...argumentsData.topics[id], treatments: argumentsData.treatments[id]})),
      editorialLinks: argumentsData.links.filter(e => topics.includes(e.source) || topics.includes(e.target)),
      statements: records, cited, proof, graph: selection.graph, citedLeanRevision: selection.registry_revision};
  }
  return {revision, documents, resolve, expand, fromDeclaration};
}
