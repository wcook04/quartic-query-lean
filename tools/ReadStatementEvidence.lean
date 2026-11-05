import Lean

/- Inspect the types and transitive axioms of the declarations identified by
   the reviewed links. Verify the defining module before attaching evidence. -/
open Lean Meta

def main (requests : List String) : IO Unit := do
  initSearchPath (← findSysroot)
  let mut selected := #[]
  let mut modules : NameSet := {}
  for request in requests do
    let [mod, decl] := request.splitOn "/" | throw (IO.userError "expected module/declaration")
    selected := selected.push (mod.toName, decl.toName)
    modules := modules.insert mod.toName
  let imports := modules.toList.toArray.map fun mod => { module := mod, importAll := true : Import }
  unsafe enableInitializersExecution
  let env ← importModules imports {} (loadExts := true) (level := .private)
  let env := env.setExporting false
  let inspect : MetaM Json := do
    let mut rows := []
    for (mod, decl) in selected do
      let some idx := env.getModuleIdxFor? decl | throwError "unknown declaration {decl}"
      unless env.header.moduleNames[idx.toNat]! == mod do
        throwError "wrong source module for {decl}, expected {mod}"
      let info ← getConstInfo decl
      let type ← ppExpr info.type
      let axioms ← collectAxioms decl
      rows := (mod.toString ++ "/" ++ decl.toString, Json.mkObj [
        ("type", toJson type.pretty), ("axioms", toJson (axioms.map toString |>.qsort (· < ·)))]) :: rows
    return Json.mkObj rows
  let options := ({} : Options).setBool `pp.fullNames true
  let (data, _, _) ← inspect.toIO {fileName := "<reader>", fileMap := default, options} {env}
  IO.println data.compress
