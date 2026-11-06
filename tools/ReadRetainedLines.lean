import Lean

open Lean

private def marker := `QuarticReaderRetainedProofLine

/-- Read only this module's persisted constants. Keep segmented regions together
    because later parts share earlier objects. No project imports are loaded. -/
private def persisted (path : System.FilePath) : IO (Array (ModuleData × CompactedRegion)) := do
  let first ← readModuleData path
  if !first.1.isModule then return #[first]
  readModuleDataParts #[path, OLeanLevel.server.adjustFileName path,
    OLeanLevel.private.adjustFileName path]

private def shadow (source : String) (headerEnd : Nat) (spans : Array (Nat × Nat)) : String := Id.run do
  let slice := fun (a b : Nat) => String.Pos.Raw.extract source ⟨a⟩ ⟨b⟩
  let mut out := slice 0 headerEnd ++ "\n\n@[expose] public def QuarticReaderRetainedProofLine.{u} {α : Sort u} (_i : Nat) (x : α) : α := x\n\n"
  let mut prev := headerEnd
  for (lo, hi) in spans do
    let tac := slice lo hi
    out := out ++ slice prev lo ++ "(first | (focus (refine (_root_.QuarticReaderRetainedProofLine " ++ toString lo ++
      " ?_); (" ++ tac ++ " <;> fail \"retained tactic left goals\"))) | " ++ tac ++ ")"
    prev := hi
  return out ++ slice prev source.utf8ByteSize

private def marked? (e : Expr) : Option (Nat × Expr) := do
  guard (e.getAppFn.constName? == some marker && e.getAppNumArgs == 3)
  let tag := e.getAppArgs[1]!
  let n ← tag.rawNatLit? <|> (do
    guard (tag.getAppFn.constName? == some `OfNat.ofNat)
    (← tag.getAppArgs[1]?).rawNatLit?)
  return (n, e.getAppArgs[2]!)

private partial def eraseMarkers (e : Expr) : Expr :=
  e.replace fun sub => (marked? sub).map fun (_, payload) => eraseMarkers payload

/-- The marker's expected type and tag cannot testify to a dependency. -/
private partial def collect (e : Expr) (save : Nat → Expr → IO Unit) : IO Unit := do
  e.forEach' fun node => do
    if let some (tag, payload) := marked? node then
      save tag (eraseMarkers payload)
      collect payload save
      return false
    return true

private def fullConstant? (parts : Array (ModuleData × CompactedRegion)) (name : Name) : Option ConstantInfo :=
  parts.reverse.findSome? fun part => part.1.constants.find? fun ci =>
    ci.name == name && (ci.value? (allowOpaque := true)).isSome

private def spans (request : Json) : IO (Array (Nat × Nat)) := do
  let rows ← IO.ofExcept (request.getObjValAs? (Array (Array Nat)) "spans")
  rows.mapM fun row => do
    unless row.size == 2 do throw (IO.userError "expected source span")
    return (row[0]!, row[1]!)

private def makeShadow (sourcePath destination requestPath : String) : IO Unit := do
  let source ← IO.FS.readFile sourcePath
  let request ← IO.ofExcept <| Json.parse (← IO.FS.readFile requestPath)
  let ranges ← spans request
  -- The native header parser determines the insertion boundary. Candidate text
  -- supplies no evidence; only the compiler and retained-payload check can do so.
  let (header, _, messages) ← Parser.parseHeader (Parser.mkInputContext source sourcePath)
  if messages.hasErrors then throw (IO.userError "invalid original import header")
  let some endPos := header.raw.getTailPos? | throw (IO.userError "missing import boundary")
  let mut prev := endPos.byteIdx
  for (lo, hi) in ranges do
    unless prev ≤ lo && lo < hi && hi ≤ source.utf8ByteSize do
      throw (IO.userError "invalid candidate source span")
    if (String.Pos.Raw.extract source ⟨lo⟩ ⟨hi⟩).contains '\n' then
      throw (IO.userError "expected single-line candidate")
    prev := hi
  IO.FS.writeFile destination (shadow source endPos.byteIdx ranges)

private def inspect (originalPath modifiedPath requestPath : String) : IO Unit := do
  let request ← IO.ofExcept <| Json.parse (← IO.FS.readFile requestPath)
  let endOf := Std.HashMap.ofList (← spans request).toList
  let compiled ← persisted originalPath
  let modified ← persisted modifiedPath
  if compiled.any (fun part => part.1.constNames.contains marker) then
    throw (IO.userError "marker name already in use")
  let rows ← IO.mkRef (#[] : Array Json)
  let callers ← IO.ofExcept (request.getObjVal? "callers")
  for (c, row) in (← IO.ofExcept callers.getObj?).toList do
    let targets ← IO.ofExcept (row.getObjValAs? (Array String) "targets")
    let bounds ← IO.ofExcept (row.getObjValAs? (Array Nat) "range")
    unless bounds.size == 2 do throw (IO.userError "expected caller source range")
    let some ci := fullConstant? compiled c.toName | continue
    let some mi := fullConstant? modified c.toName | continue
    let some original := ci.value? (allowOpaque := true) | continue
    let some observed := mi.value? (allowOpaque := true) | continue
    unless ci.type.equal mi.type && original.equal (eraseMarkers observed) do continue
    collect observed fun tag payload => do
      let some hi := endOf[tag]? | throw (IO.userError "unrecognised retained marker")
      -- An unfolded earlier declaration's marker belongs to its own source.
      unless bounds[0]! ≤ tag && hi ≤ bounds[1]! do return
      for d in payload.getUsedConstants do
        if targets.contains d.toString then
          rows.modify (·.push (toJson [toJson c, toJson d.toString, toJson tag, toJson hi]))
  IO.println (toJson (← rows.get)).compress

def main (args : List String) : IO Unit := do
  match args with
  | ["shadow", source, destination, requests] => makeShadow source destination requests
  | ["inspect", original, modified, requests] => inspect original modified requests
  | _ => throw (IO.userError "expected shadow SOURCE DESTINATION REQUESTS or inspect ORIGINAL MODIFIED REQUESTS")
