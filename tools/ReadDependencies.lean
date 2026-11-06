import Lean

/- Dependency categories adapted from lean-exposition's Extract.lean (f5a1403),
Copyright 2026 lean-exposition contributors, Apache-2.0. Structural cases
adapted from Comparator/Util.lean (d03acab), Copyright 2025 Lean FRO, LLC,
author Henrik Böving, Apache-2.0. The module boundary includes private helpers. -/
open Lean

private def structural : ConstantInfo → Array Name
  | .inductInfo v => v.ctors.toArray ++ v.all.toArray
  | .ctorInfo v => #[v.induct]
  | .recInfo v => v.rules.foldl (init := #[]) fun acc r => acc.push r.ctor ++ r.rhs.getUsedConstants
  | _ => #[]

def main : IO Unit := do
  initSearchPath (← findSysroot)
  let env ← importModules #[{ module := `QuarticQuery, importAll := true }] {}
    (loadExts := false) (level := .private)
  let env := env.setExporting false
  let names (deps : Array Name) := toJson (deps.map toString |>.qsort (· < ·))
  let (rows, refs) := env.constants.fold (init := ([], ({} : NameSet))) fun acc n c => Id.run do
    let some idx := env.getModuleIdxFor? n | return acc
    let mod := env.header.moduleNames[idx.toNat]!
    unless (`QuarticQuery).isPrefixOf mod do return acc
    let value := c.value? (allowOpaque := true)
    let t := c.type.getUsedConstants
    let v := (value.map Expr.getUsedConstants).getD #[]
    let structureRefs := structural c
    let seen := (t ++ v ++ structureRefs).foldl (fun set dep => set.insert dep) acc.2
    return ((n.toString, Json.mkObj [("module", toJson mod.toString),
      ("type", names t),
      ("value", names v),
      ("has_body", toJson value.isSome), ("structural", names structureRefs)]) :: acc.1, seen)
  let externalModules := refs.toList.filterMap fun n => do
    let idx ← env.getModuleIdxFor? n
    let mod := env.header.moduleNames[idx.toNat]!
    guard (!( `QuarticQuery).isPrefixOf mod)
    return (n.toString, toJson mod.toString)
  IO.println (Json.mkObj [("nodes", Json.mkObj rows), ("external_modules", Json.mkObj externalModules)]).compress
