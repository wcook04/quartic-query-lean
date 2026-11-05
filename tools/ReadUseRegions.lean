import Lean

open Lean

/-- Find only the immediate body of the outer declaration. Nested lets and
    occurrences of := in the statement must not start a proof region. -/
private def bodyStart (env : Environment) (command : String) : Option Nat := do
  let stx ← (Parser.runParserCategory env `command command).toOption
  guard (stx.getKind == ``Parser.Command.declaration)
  let bodies := stx[1].getArgs.filter fun child =>
    [``Parser.Command.declValSimple, ``Parser.Command.declValEqns, ``Parser.Command.whereStructInst].contains child.getKind
  let #[body] := bodies | none
  return (← body.getPos?).byteIdx

def main (args : List String) : IO Unit := do
  let [path] := args | throw (IO.userError "expected JSON file of (name, command) pairs")
  initSearchPath (← findSysroot)
  unsafe enableInitializersExecution
  let env ← importModules #[{module := `QuarticQuery}] {} (loadExts := true)
  let input ← IO.ofExcept <| Json.parse (← IO.FS.readFile path)
  let commands ← IO.ofExcept <| fromJson? (α := Array (String × String)) input
  IO.println (Json.mkObj <| commands.toList.map fun (name, command) =>
    (name, toJson (bodyStart env command))).compress
