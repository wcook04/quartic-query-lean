import Lean

open Lean Meta

/-- Inspect maximal applications under their original local binders. Pretty-printed
    arguments are for display. The caller, callee and binder order come from Expr. -/
private def describe (e : Expr) (parameters : Array Expr := #[]) : MetaM Json := do
  let mut ty ← inferType e.getAppFn
  let mut args := #[]
  for arg in e.getAppArgs do
    let .forallE name domain body info ← whnf ty | throwError "expected function at {e}"
    let proof ← isProp domain
    let term ← if proof && !arg.isFVar then pure Json.null else pure (toJson (toString (← ppExpr arg)))
    let basis := if !proof then none else some <|
      if parameters.contains arg then "caller_parameter"
      else if arg.isFVar then "local_reference"
      else if arg.getAppFn.isConst then "named_proof_term"
      else "proof_expression"
    let providers := if proof then arg.getUsedConstants.filter (`QuarticQuery).isPrefixOf else #[]
    args := args.push (Json.mkObj [("binder", toJson name.toString),
      ("explicit", toJson info.isExplicit), ("proof", toJson proof),
      ("basis", toJson basis), ("project_constants", toJson ((providers.map Name.toString).qsort (· < ·))),
      ("type", toJson (toString (← ppExpr domain))), ("argument", term),
      ("head_constant", toJson (arg.getAppFn.constName?.map Name.toString))])
    ty := body.instantiate1 arg
  return Json.mkObj [("callee", toJson e.getAppFn.constName!.toString), ("arguments", toJson args),
    ("result_type", toJson (toString (← ppExpr ty)))]

private partial def scan (targets : NameSet) (use : Expr → MetaM Unit) (e : Expr) :
    MonadCacheT Expr Unit MetaM Unit := checkCache e fun _ => do
  let visit := scan targets use
  if let some n := e.getAppFn.constName? then
    if targets.contains n then
      use e
  match e with
  | .forallE .. => visitForall visit e
  | .lam .. => visitLambda visit e
  | .letE .. => visitLet visit e
  | .app .. =>
    unless e.getAppFn.isConst do visit e.getAppFn
    for arg in e.getAppArgs do visit arg
  | .mdata _ b | .proj _ _ b => visit b
  | _ => pure ()

private def closeTerm (e : Expr) : MetaM Expr := do
  -- Keep binder slots, so two same-typed parameters stay distinguishable.
  let e ← instantiateMVars e
  if !e.hasFVar then return e
  let lctx ← getLCtx
  let ordinary := lctx.foldl (init := #[]) fun xs d => if d.isAuxDecl then xs else xs.push d.toExpr
  mkLambdaFVars ordinary e (usedLetOnly := false)

/-- Check the two complexity bounds while the existential circuit is in scope.
    Structural equality here compares live expressions, including the very same fvar. -/
private def sameBoard (statement : Expr) : MetaM Json := do
  let found ← IO.mkRef #[]
  let existsHead : NameSet := ({} : NameSet).insert `Exists
  let quantum := `QuarticQuery.Q
  let classical := `QuarticQuery.R
  let bounds := ({} : NameSet).insert quantum |>.insert classical
  let inspect := fun (e : Expr) => do
    let some pred := e.getAppArgs.back? | return ()
    let .lam _ dom _ _ := pred | return ()
    unless dom.getAppFn.constName? == some `QuarticQuery.Circuit do return ()
    lambdaTelescope pred fun xs body => do
      let some circuit := xs[0]? | return ()
      let hits ← IO.mkRef (#[] : Array (Name × Expr))
      let use := fun (call : Expr) => do
        let some f := call.getAppArgs.back? | return ()
        unless f.getAppFn.constName? == some `QuarticQuery.totalise do return ()
        let some board := f.getAppArgs.back? | return ()
        unless board.getAppFn.constName? == some `QuarticQuery.Fkm &&
            board.getAppArgs.back? == some circuit do return ()
        hits.modify (·.push (call.getAppFn.constName!, f))
      (scan bounds use body).run
      let calls ← hits.get
      let qs := calls.filter (·.1 == quantum)
      let rs := calls.filter (·.1 == classical)
      if let (#[( _, q)], #[(_, r)]) := (qs, rs) then
        if q == r then
          let cirText := toString (← ppExpr circuit)
          let funText := toString (← ppExpr q)
          found.modify (·.push (Json.mkObj [("basis", toJson "identical_expr_under_one_existential"),
            ("circuit", toJson cirText), ("function", toJson funText),
            ("bounds", toJson [quantum.toString, classical.toString])]))
  (scan existsHead inspect statement).run
  let #[row] ← found.get | throwError "expected one circuit with identical Q and R board arguments"
  return row

private def readSites (module path : String) (requests : NameMap NameSet) : IO Json := do
  let input ← IO.FS.readFile path
  let ctx := Parser.mkInputContext input path
  let (header, parser, messages) ← Parser.parseHeader ctx
  let options := ({} : Options).setBool `Elab.async false
  unsafe enableInitializersExecution
  let (env, messages) ← Elab.processHeader header options messages ctx (mainModule := module.toName)
  let state := Elab.Command.mkState env messages options
  let result ← Elab.IO.processCommands ctx parser {state with infoState.enabled := true}
  for msg in result.commandState.messages.toList do
    if msg.severity == .error then throw (IO.userError (← msg.toString))
  let env := result.commandState.env.setExporting false
  let mut rows := #[]
  for (caller, targets) in requests do
    let some value := (env.find? caller).bind (·.value? (allowOpaque := true))
      | throw (IO.userError s!"missing re-elaborated body {caller}")
    let compiled ← IO.mkRef (#[] : Array Expr)
    let _ ← ((scan targets (fun e => do
      let term ← closeTerm e
      compiled.modify (·.push term)) value).run).toIO
      {fileName := path, fileMap := ctx.fileMap, maxHeartbeats := 0} {env}
    let terms ← compiled.get
    -- The pretty-printer can hide distinct proof terms. Deduplicate observations
    -- by the closed expression as well as its source record, before rendering.
    let mut observations : Array (Expr × Json) := #[]
    for tree in result.commandState.infoState.trees do
      let found ← tree.collectTermInfoM fun context ti => do
        if context.parentDecl? != some caller || ti.stx.getKind != ``Lean.Parser.Term.app then return none
        let head := ti.stx[0]
        unless head.isIdent do return none
        let .original .. := head.getHeadInfo | return none
        let some range := ti.stx.getRange? (canonicalOnly := true) | return none
        ti.runMetaM context do
          let e ← instantiateMVars ti.expr
          let some name := e.getAppFn.constName? | return none
          unless targets.contains name && e.isApp && !e.hasMVar do return none
          let term ← closeTerm e
          unless !term.hasFVar && terms.contains term do return none
          return some (term, Json.mkObj [("caller", toJson caller.toString), ("term", ← describe e),
            ("start", toJson range.start.byteIdx), ("end", toJson range.stop.byteIdx)])
      for row in found do
        unless observations.contains row do observations := observations.push row
    rows := rows ++ observations.map Prod.snd
  return toJson rows

def main (pairs : List String) : IO Unit := do
  initSearchPath (← findSysroot)
  let (source?, pairs) := match pairs with
    | "--source" :: mod :: path :: rest => (some (mod, path), rest)
    | rest => (none, rest)
  let mut requests : NameMap NameSet := {}
  for pair in pairs do
    let [caller, callee] := pair.splitOn "=" | throw (IO.userError "expected caller=callee")
    requests := requests.insert caller.toName ((requests.find? caller.toName).getD {} |>.insert callee.toName)
  if let some (mod, path) := source? then
    IO.println (← readSites mod path requests).compress
    return
  let env ← importModules #[{module := `QuarticQuery, importAll := true}] {} (level := .private)
  let env := env.setExporting false
  let mut rows := []
  for (caller, targets) in requests do
    let some value := (env.find? caller).bind (·.value? (allowOpaque := true))
      | throw (IO.userError s!"missing declaration body for {caller}")
    let hits ← IO.mkRef #[]
    let collect := lambdaTelescope value fun parameters body =>
      (scan targets (fun e => do let row ← describe e parameters; hits.modify (·.push row)) body).run
    let _ ← collect.toIO
      {fileName := "<applications>", fileMap := default, maxHeartbeats := 0} {env}
    rows := (caller.toString, toJson (← hits.get)) :: rows
  let assembly := `QuarticQuery.theorem_1_1_unconditional
  let some decl := env.find? assembly | throw (IO.userError "missing family assembly")
  let (board, _, _) ← (sameBoard decl.type).toIO {fileName := "<bounds>", fileMap := default} {env}
  IO.println (Json.mkObj [("callers", Json.mkObj rows), ("same_board", Json.mkObj [(assembly.toString, board)])]).compress
