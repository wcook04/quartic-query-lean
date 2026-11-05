import Lean

open Lean Meta

/-- Inspect maximal applications under their original local binders. Pretty-printed
    arguments are for display. The caller, callee and binder order come from Expr. -/
private def describe (e : Expr) : MetaM Json := do
  let mut ty ← inferType e.getAppFn
  let mut args := #[]
  for arg in e.getAppArgs do
    let .forallE name domain body info ← whnf ty | throwError "expected function at {e}"
    let proof ← isProp domain
    let term ← if proof && !arg.isFVar then pure Json.null else pure (toJson (toString (← ppExpr arg)))
    args := args.push (Json.mkObj [("binder", toJson name.toString),
      ("explicit", toJson info.isExplicit), ("proof", toJson proof),
      ("type", toJson (toString (← ppExpr domain))), ("argument", term),
      ("head_constant", toJson (arg.getAppFn.constName?.map Name.toString))])
    ty := body.instantiate1 arg
  return Json.mkObj [("callee", toJson e.getAppFn.constName!.toString), ("arguments", toJson args),
    ("result_type", toJson (toString (← ppExpr ty)))]

private partial def scan (targets : NameSet) (hits : IO.Ref (Array Json)) (e : Expr) :
    MonadCacheT Expr Unit MetaM Unit := checkCache e fun _ => do
  let visit := scan targets hits
  if let some n := e.getAppFn.constName? then
    if targets.contains n then
      let row ← describe e
      hits.modify (·.push row)
  match e with
  | .forallE .. => visitForall visit e
  | .lam .. => visitLambda visit e
  | .letE .. => visitLet visit e
  | .app .. =>
    unless e.getAppFn.isConst do visit e.getAppFn
    for arg in e.getAppArgs do visit arg
  | .mdata _ b | .proj _ _ b => visit b
  | _ => pure ()

def main (pairs : List String) : IO Unit := do
  initSearchPath (← findSysroot)
  let env ← importModules #[{module := `QuarticQuery, importAll := true}] {} (level := .private)
  let env := env.setExporting false
  let mut requests : NameMap NameSet := {}
  for pair in pairs do
    let [caller, callee] := pair.splitOn "=" | throw (IO.userError "expected caller=callee")
    requests := requests.insert caller.toName ((requests.find? caller.toName).getD {} |>.insert callee.toName)
  let mut rows := []
  for (caller, targets) in requests do
    let some value := (env.find? caller).bind (·.value? (allowOpaque := true))
      | throw (IO.userError s!"missing declaration body for {caller}")
    let hits ← IO.mkRef #[]
    let _ ← ((scan targets hits value).run).toIO
      {fileName := "<applications>", fileMap := default, maxHeartbeats := 0} {env}
    rows := (caller.toString, toJson (← hits.get)) :: rows
  IO.println (Json.mkObj rows).compress
