import Lean
open Lean

def main (args : List String) : IO Unit := do
  let [module, path] := args | throw (IO.userError "expected module path")
  initSearchPath (← findSysroot)
  unsafe enableInitializersExecution
  let text ← IO.FS.readFile path
  let ctx := Parser.mkInputContext text path
  let (header, parser, messages) ← Parser.parseHeader ctx
  let options := ({} : Options).setBool `Elab.async false
  let (env, messages) ← Elab.processHeader header options messages ctx (mainModule := module.toName)
  let result ← Elab.IO.processCommands ctx parser (Elab.Command.mkState env messages options)
  for message in result.commandState.messages.toList do
    if message.severity == .error then throw (IO.userError (← message.toString))
  let mut cuts := #[]
  for stx in result.commands do
    unless stx.getKind == ``Parser.Command.declaration do continue
    let some id := stx[1].getArgs.find? (·.getKind == ``Parser.Command.declId) | continue
    let some head := id[0].getRange? (canonicalOnly := true) | continue
    let some body := stx[1].getArgs.find? (fun c =>
      [``Parser.Command.declValSimple, ``Parser.Command.declValEqns, ``Parser.Command.whereStructInst].contains c.getKind) | continue
    let some cut := body.getPos? | continue
    cuts := cuts.push <| Json.mkObj [("id", toJson [head.start.byteIdx, head.stop.byteIdx]), ("cut", toJson cut.byteIdx)]
  IO.println (toJson cuts).compress
