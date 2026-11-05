import Lean

open Lean

/-- A named outer parameter with this type constructor must occur exactly once. -/
private def parameters (isValue : Bool) (expr : Expr) : List (Name × Option Name) :=
  match isValue, expr with
  | false, .forallE n d b _ | true, .lam n d b _ =>
    (n, d.getAppFn.constName?) :: parameters isValue b
  | _, .mdata _ b => parameters isValue b
  | _, _ => []

private def matchingParameter (params : List (Name × Option Name)) (name target : Name) : Bool :=
  (params.filter (·.1 == name)) == [(name, some target)]

private def capture (state : Elab.Frontend.State) (source : String) : IO (Array Json) := do
  let env := state.commandState.env.setExporting false
  -- A section variable is re-elaborated with fresh FVarIds in each command.
  -- Limit the origin to an actual, single-line, written binder of a variable command.
  let mut declarationIds : Std.HashSet (Nat × Nat) := {}
  let mut origins : Std.HashMap (Nat × Nat) (Nat × Nat) := {}
  for stx in state.commands do
    if stx.getKind == ``Parser.Command.declaration then
      if let some name := stx[1].getArgs.find? (·.getKind == ``Parser.Command.declId) then
        if let some r := name[0].getRange? (canonicalOnly := true) then
          declarationIds := declarationIds.insert (r.start.byteIdx, r.stop.byteIdx)
    unless stx.getKind == ``Parser.Command.«variable» do continue
    for binder in stx[2].getArgs do
      unless [``Parser.Term.explicitBinder, ``Parser.Term.implicitBinder,
              ``Parser.Term.strictImplicitBinder].contains binder.getKind do continue
      let some span := binder.getRange? (canonicalOnly := true) | continue
      if (String.Pos.Raw.extract source span.start span.stop).contains '\n' then continue
      for id in binder[1].getArgs do
        let some r := id.getRange? (canonicalOnly := true) | continue
        origins := origins.insert (r.start.byteIdx, r.stop.byteIdx) (span.start.byteIdx, span.stop.byteIdx)
  let mut output := #[]
  for tree in state.commandState.infoState.trees do
    -- IDs may be reused between command snapshots. Never join across trees.
    let binderInfos ← tree.collectTermInfoM fun _ ti => do
      unless ti.isBinder do return none
      let some id := ti.expr.fvarId? | return none
      let some r := ti.stx.getRange? (canonicalOnly := true) | return none
      let some span := origins[(r.start.byteIdx, r.stop.byteIdx)]? | return none
      let some decl := ti.lctx.find? id | return none
      let some target := decl.type.getAppFn.constName? | return none
      unless (`QuarticQuery).isPrefixOf target do return none
      return some (id, span, decl.userName, target)
    if binderInfos.isEmpty then continue
    -- The elaborator records the local self declaration at the declaration's
    -- name before wrapping its type in the retained section variables. Compare
    -- its telescope with the final constant to isolate exactly that prefix.
    let headers ← tree.collectTermInfoM fun ci ti => do
      unless ti.isBinder do return none
      let some r := ti.stx.getRange? (canonicalOnly := true) | return none
      let key := (r.start.byteIdx, r.stop.byteIdx)
      unless declarationIds.contains key do return none
      let arity? := do
        let f ← ti.expr.fvarId?
        let d ← ti.lctx.find? f
        let ty := (instantiateMVarsCore ci.mctx d.type).1
        return (parameters false ty).length
      return some (key, ti.expr.constName?, arity?)
    let mut prefixSize : NameMap Nat := {}
    for (key, caller?, _) in headers do
      let some caller := caller? | continue
      let some decl := env.find? caller | continue
      let [arity] := (headers.filterMap fun (key', _, n) => if key' == key then n else none).eraseDups | continue
      let finalArity := (parameters false decl.type).length
      if arity < finalArity then prefixSize := prefixSize.insert caller (finalArity - arity)
    let uses ← tree.collectTermInfoM fun ci ti => do
      let some caller := ci.parentDecl? | return none
      if ti.isBinder then return none
      let .original .. := ti.stx.getHeadInfo | return none
      let some exprRange := ti.stx.getRange? (canonicalOnly := true) | return none
      let some count := prefixSize.find? caller | return none
      let some decl := env.find? caller | return none
      let expr := (instantiateMVarsCore ci.mctx ti.expr).1
      let ids := (collectFVars {} expr).fvarSet
      let mut found := #[]
      for (id, (lo, hi), name, target) in binderInfos do
        unless ids.contains id && hi <= exprRange.start.byteIdx do continue
        unless (ti.lctx.findFromUserName? name).map (·.fvarId) == some id do continue
        unless matchingParameter ((parameters false decl.type).take count) name target do continue
        let inValue := (decl.value? (allowOpaque := true)).any fun e =>
          matchingParameter ((parameters true e).take count) name target
        found := found.push <| Json.mkObj [("caller", toJson caller.toString), ("parameter", toJson name.toString),
          ("target", toJson target.toString), ("lo", toJson lo), ("hi", toJson hi), ("value", toJson inValue)]
      return some found
    for group in uses do
      for row in group do
        unless output.contains row do output := output.push row
  return output

def main (args : List String) : IO Unit := do
  let [module, path] := args | throw (IO.userError "expected module and source file")
  initSearchPath (← findSysroot)
  unsafe enableInitializersExecution
  let source ← IO.FS.readFile path
  let ctx := Parser.mkInputContext source path
  let (header, parser, messages) ← Parser.parseHeader ctx
  let options := ({} : Options).setBool `Elab.async false
  let (env, messages) ← Elab.processHeader header options messages ctx (mainModule := module.toName)
  let cmd := Elab.Command.mkState env messages options
  let state ← Elab.IO.processCommands ctx parser {cmd with infoState.enabled := true}
  for msg in state.commandState.messages.toList do
    if msg.severity == .error then throw (IO.userError (← msg.toString))
  IO.println (toJson (← capture state source)).compress
