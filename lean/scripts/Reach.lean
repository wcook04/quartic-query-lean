import Lean

/-!
Print, as JSON, every `QuarticQuery` declaration reached from the named headline
theorems, and the `QuarticQuery` dependencies of each. Run from `lean/` with
`lake env lean --run scripts/Reach.lean <root theorem>...`. Proof bodies are read
from the compiled environment, so this reports what the kernel checked rather than
what a source file mentions.
-/

open Lean

def inProject (n : Name) : Bool :=
  (`QuarticQuery).isPrefixOf n && !n.isInternal

def bodyOf : ConstantInfo → Option Expr
  | .thmInfo v => some v.value
  | .defnInfo v => some v.value
  | .opaqueInfo v => some v.value
  | _ => none

def dependencies (env : Environment) (n : Name) : Array Name := Id.run do
  let some info := env.find? n | return #[]
  let mut seen : NameSet := {}
  let mut todo := info.type.getUsedConstants ++
    ((bodyOf info).map (·.getUsedConstants)).getD #[]
  let mut out : Array Name := #[]
  while !todo.isEmpty do
    let c := todo.back!
    todo := todo.pop
    if seen.contains c then continue
    seen := seen.insert c
    if inProject c then
      out := out.push c
    else if c.isInternal && (`QuarticQuery).isPrefixOf c then
      -- auxiliary lemmas belong to the declaration that generated them
      if let some aux := env.find? c then
        todo := todo ++ aux.type.getUsedConstants ++
          ((bodyOf aux).map (·.getUsedConstants)).getD #[]
  return out

def main (roots : List String) : IO Unit := do
  initSearchPath (← findSysroot)
  let env ← importModules #[{ module := `QuarticQuery, importAll := true }] {}
    (loadExts := false) (level := .private)
  let env := env.setExporting false
  let mut seen : NameSet := {}
  let mut todo : Array Name := roots.toArray.map String.toName
  let mut edges : Array (Name × Array Name) := #[]
  while !todo.isEmpty do
    let n := todo.back!
    todo := todo.pop
    if seen.contains n then continue
    seen := seen.insert n
    let deps := dependencies env n
    edges := edges.push (n, deps)
    todo := todo ++ deps
  let declared := env.constants.fold (init := (#[] : Array Name)) fun acc n _ =>
    if inProject n then acc.push n else acc
  let encode (names : Array Name) : Json := toJson (names.map toString |>.qsort (· < ·))
  let edgeJson := Json.mkObj (edges.toList.map fun (n, deps) => (toString n, encode deps))
  IO.println <| (Json.mkObj [("roots", toJson roots), ("reached", encode (edges.map (·.1))),
    ("declared", encode declared), ("edges", edgeJson)]).compress
