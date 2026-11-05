import Lean

open Lean Meta

/- Addresses use individual kernel expression children, never pretty-printed text.
   Within a region breadth-first search chooses the shortest retained occurrence.
   The reader decodes the compact alphabet when an arrow is opened. -/
private def children : Expr → List (Char × Expr)
  | .app f a => [('f', f), ('a', a)]
  | .forallE _ d b _ | .lam _ d b _ => [('d', d), ('b', b)]
  | .letE _ t v b _ => [('t', t), ('v', v), ('l', b)]
  | .mdata _ b => [('m', b)]
  | .proj _ _ b => [('p', b)]
  | _ => []

private def reference : Expr → Option (Name × String)
  | .const n _ => some (n, "constant")
  | .proj n i _ => some (n, s!"projection:{i}")
  | _ => none

private def verify (root : Expr) (path : List Char) (target : Name) (leaf : String) : Bool := Id.run do
  let mut node := root
  for step in path do
    let some (_, next) := (children node).find? (·.1 == step) | return false
    node := next
  return reference node == some (target, leaf)

private def search (root : Expr) (roots : Array (Expr × List Char × String))
    (wanted : NameSet) : IO (List (String × Json)) := do
  let mut todo := roots
  let mut i := 0
  let mut visited : ExprSet := {}
  let mut pending := wanted
  let mut rows := []
  while i < todo.size && !pending.isEmpty do
    let (node, rev, region) := todo[i]!
    i := i + 1
    if visited.contains node then continue
    visited := visited.insert node
    if let some (name, leaf) := reference node then
      if pending.contains name then
        let path := rev.reverse
        unless verify root path name leaf do throw (IO.userError s!"invalid path for {name}")
        rows := (name.toString, toJson [region, String.ofList path, leaf]) :: rows
        pending := pending.erase name
    for (step, child) in children node do
      todo := todo.push (child, step :: rev, region)
  unless pending.isEmpty do throw (IO.userError s!"unresolved kernel occurrence: {pending.toList}")
  return rows

private def occurrences (root : Expr) (value : Bool) (targets : NameSet) : IO Json := do
  let mut core := root
  let mut rev := []
  let mut domains := #[]
  repeat
    match core with
    | .mdata _ b => rev := 'm' :: rev; core := b
    | .forallE n d b _ | .lam n d b _ =>
      if core.isLambda != value then break
      domains := domains.push (d, 'd' :: rev, s!"parameter:{domains.size}:{n}")
      rev := 'b' :: rev
      core := b
    | _ => break
  let inner := core.getUsedConstants.foldl (init := ({} : NameSet)) fun s n =>
    if targets.contains n then s.insert n else s
  let rest := targets.toList.foldl (init := ({} : NameSet)) fun s n =>
    if inner.contains n then s else s.insert n
  let a ← search root #[(core, rev, if value then "body" else "result")] inner
  return Json.mkObj (a ++ (← search root domains rest))

private def structurePaths (info : ConstantInfo) (targets : NameSet) : IO Json := do
  let mut rows := []
  for target in targets.toList do
    let row? : Option Json := do
      match info with
      | .inductInfo i =>
        if let some idx := i.ctors.idxOf? target then return toJson ["constructors", toString idx]
        return toJson ["mutual_family", toString (← i.all.idxOf? target)]
      | .ctorInfo c => guard (c.induct == target); return toJson ["parent_inductive"]
      | .recInfo r =>
        let idx ← r.rules.findIdx? (fun rule => rule.ctor == target || rule.rhs.getUsedConstants.contains target)
        let rule ← r.rules[idx]?
        return toJson [if rule.ctor == target then "rule_constructor" else "rule_rhs", toString idx]
      | _ => none
    let some row := row? | throw (IO.userError s!"missing structural relation for {target}")
    rows := (target.toString, row) :: rows
  return Json.mkObj rows

private def range (stx : Syntax) : Option (List Nat) := do
  let r ← stx.getRange? (canonicalOnly := true)
  return [r.start.byteIdx, r.stop.byteIdx]

/-- Registered tactic syntax from the original declaration. This only schedules
    possible replay sites; a parsed tactic need not have contributed to a proof. -/
private partial def tacticRanges (isTactic : Name → Bool) (command : String) (stx : Syntax) :
    Array (Nat × Nat) := Id.run do
  let .node _ kind args := stx | return #[]
  let mut result := #[]
  if isTactic kind then
    if let some r := stx.getRange? (canonicalOnly := true) then
      let text := String.Pos.Raw.extract command r.start r.stop
      let head := (text.takeWhile fun (c : Char) => !c.isWhitespace).toString
      if !text.contains '\n' && ["exact", "simpa", "rfl", "simp", "rw", "ring", "ring_nf",
          "omega", "linarith", "nlinarith", "norm_num", "positivity", "assumption",
          "exact_mod_cast", "decide"].contains head then
        result := result.push (r.start.byteIdx, r.stop.byteIdx)
  for child in args do
    result := result ++ tacticRanges isTactic command child
  return result

private def outerNames (root : Expr) (value : Bool) : Array Name := Id.run do
  let mut names := #[]
  let mut term := root
  repeat
    match term with
    | .mdata _ b => term := b
    | .forallE n _ b _ | .lam n _ b _ =>
      if term.isLambda != value then break
      names := names.push n
      term := b
    | _ => break
  return names

/-- Accept only the primary name at the range selected by Lean's native index.
    The result expression excludes all declaration binders. Constructor signatures
    are nested inside their inductive command in the language-server index. -/
private def sourceRegions (env : Environment) (info : ConstantInfo) (command : String) (namePos : List Nat) : Option Json := do
  let stx ← (Parser.runParserCategory env `command command).toOption
  guard (stx.getKind == ``Parser.Command.declaration)
  let decl := stx[1]
  let name ← decl.getArgs.find? (·.getKind == ``Parser.Command.declId)
  guard (range name[0] == some namePos)
  let sig ← decl.getArgs.find? (fun c => [``Parser.Command.optDeclSig, ``Parser.Command.declSig].contains c.getKind)
  let spec := if sig.getKind == ``Parser.Command.declSig then sig[1] else sig[1][0]
  let result? := if spec.getKind == ``Parser.Term.typeSpec then range spec[1] else none
  -- A source binder can only explain a compiled lambda domain if that name is
  -- unique in both telescopes and occupies the same slot in each. In particular
  -- a shadowed name cannot transfer a source location to another parameter.
  let typeNames := outerNames info.type false
  let valueNames := outerNames ((info.value? (allowOpaque := true)).getD default) true
  let binders := sig[0].getArgs.filterMap fun binder => do
    guard ([``Parser.Term.explicitBinder, ``Parser.Term.implicitBinder, ``Parser.Term.strictImplicitBinder].contains binder.getKind)
    let domain ← range binder[2]
    let names := binder[1].getArgs.filterMap fun id => do
      guard id.isIdent
      let n := id.getId
      guard (typeNames.count n == 1 && valueNames.count n == 1 && typeNames.idxOf n == valueNames.idxOf n)
      return n.toString
    return Json.mkObj [("names", toJson names), ("domain", toJson domain)]
  let ctors := if decl.getKind != ``Parser.Command.«inductive» then #[] else
    decl[4].getArgs.filterMap fun ctor => do
      guard (ctor.getKind == ``Parser.Command.ctor)
      let id ← ctor.getArgs.find? (·.isIdent)
      let ctorSig ← ctor.getArgs.find? (·.getKind == ``Parser.Command.optDeclSig)
      return Json.mkObj [("name", toJson (← range id)), ("signature", toJson (← range ctorSig))]
  let cats := (Parser.parserExtension.getState env).categories
  let spans := match cats.find? `tactic with
    | some cat => tacticRanges (fun k => cat.kinds.contains k) command decl
    | none => #[]
  return Json.mkObj [("result", toJson result?), ("binders", toJson binders),
                     ("constructors", toJson ctors), ("tactics", toJson spans)]

private def inspect (env : Environment) (info : ConstantInfo) (row : Json) : IO Json := do
  let mut data := []
  for kind in ["type", "value", "structural"] do
    let deps ← IO.ofExcept (row.getObjValAs? (Array String) kind)
    let targets := deps.foldl (init := ({} : NameSet)) fun s d => s.insert d.toName
    if targets.isEmpty then continue
    let paths ← match kind with
      | "type" => occurrences info.type false targets
      | "value" => do
        let some v := info.value? (allowOpaque := true) | throw (IO.userError s!"no body for {info.name}")
        occurrences v true targets
      | _ => structurePaths info targets
    data := (kind, paths) :: data
  if let .ok text := row.getObjValAs? String "command" then
    let pos ← IO.ofExcept (row.getObjValAs? (List Nat) "id")
    if let some regions := sourceRegions env info text pos then
      data := ("source_regions", regions) :: data
  if (← IO.ofExcept (row.getObjValAs? Bool "signature")) then
    let (sig, _, _) ← (ppExpr info.type).toIO
      {fileName := "<kernel>", fileMap := default, options := ({} : Options).setBool `pp.fullNames true} {env}
    data := ("signature", toJson sig.pretty) :: data
  return Json.mkObj data

def main (args : List String) : IO Unit := do
  let [file] := args | throw (IO.userError "expected inspection requests")
  initSearchPath (← findSysroot)
  unsafe enableInitializersExecution
  -- Only parsing and pretty-printing need an environment. Load public syntax
  -- once, then read each module's private constants directly from its artifact.
  let env ← importModules #[{module := `QuarticQuery}] {} (loadExts := true) (level := .exported)
  let input ← IO.ofExcept <| Json.parse (← IO.FS.readFile file)
  let mut result := []
  for (module, requests) in (← IO.ofExcept input.getObj?).toList do
    let file ← findOLean module.toName
    let files := #[file, OLeanLevel.server.adjustFileName file, OLeanLevel.private.adjustFileName file]
    let parts ← readModuleDataParts files
    for (caller, row) in (← IO.ofExcept requests.getObj?).toList do
      let some info := parts.reverse.findSome? (fun part => part.1.constants.find? (·.name == caller.toName))
        | throw (IO.userError s!"missing {caller} in {module}")
      result := (caller, ← inspect env info row) :: result
  IO.println (Json.mkObj result).compress
