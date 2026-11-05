import Lean

open Lean

/-- Removing all outer binders is conservative for a right hand side written as
    a lambda. A constant occurring only in a declaration parameter cannot count
    as a use in its proof. -/
private def bodyConstants : Expr → Array Name
  | .lam _ _ body _ | .mdata _ body => bodyConstants body
  | e => e.getUsedConstants.filter ((`QuarticQuery).isPrefixOf ·)

/-- Parse the outer declaration. Nested lets in the statement do not start the
    proof. Only simple right hand sides have a candidate expression highlight. -/
private def regions (env : Environment) (name : Name) (command : String) : Option Json := do
  let .ok stx := Parser.runParserCategory env `command command | return Json.str "needs_module_context"
  guard (stx.getKind == ``Parser.Command.declaration)
  let bodies := stx[1].getArgs.filter fun child =>
    [``Parser.Command.declValSimple, ``Parser.Command.declValEqns, ``Parser.Command.whereStructInst].contains child.getKind
  let #[body] := bodies | none
  let cut := (← body.getPos?).byteIdx
  let rhs? : Option Json := do
    guard (body.getKind == ``Parser.Command.declValSimple)
    -- A termination clause or local where-declaration introduces extra source.
    guard (body.getNumArgs == 4 && !body[2].getPos?.isSome && !body[3].getPos?.isSome)
    let expr := body[1]
    let fragment := if expr.getKind == ``Parser.Term.byTactic then expr[1] else expr
    let span ← fragment.getRange? (canonicalOnly := true)
    let text := String.Pos.Raw.extract command span.start span.stop
    guard (!text.contains '\n' && !text.isEmpty)
    let decl ← env.find? name
    let val ← decl.value? (allowOpaque := true)
    return Json.mkObj [("lo", toJson span.start.byteIdx), ("hi", toJson span.stop.byteIdx),
      ("constants", toJson ((bodyConstants val).map Name.toString))]
  return Json.mkObj [("cut", toJson cut), ("rhs", toJson rhs?)]

def main (args : List String) : IO Unit := do
  let [path] := args | throw (IO.userError "expected JSON file of (name, command) pairs")
  initSearchPath (← findSysroot)
  unsafe enableInitializersExecution
  let env ← importModules #[{module := `QuarticQuery, importAll := true}] {} (loadExts := true) (level := .private)
  let input ← IO.ofExcept <| Json.parse (← IO.FS.readFile path)
  let commands ← IO.ofExcept <| fromJson? (α := Array (String × String)) input
  IO.println (Json.mkObj <| commands.toList.map fun (name, command) =>
    (name, toJson (regions (env.setExporting false) name.toName command))).compress
