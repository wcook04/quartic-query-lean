-- Layout only. The mathematical content is read from section.md.
function Code(el)
  if #el.text >= 48 and el.text:match("^%x+$") then
    local pieces = {}
    for i = 1, #el.text, 8 do
      pieces[#pieces + 1] = el.text:sub(i, i + 7)
    end
    return pandoc.RawInline("latex", "\\texttt{" ..
      table.concat(pieces, "\\allowbreak{}") .. "}")
  end
end

function Para(el)
  if #el.content > 0 and el.content[1].t == "Strong" then
    return {pandoc.RawBlock("latex", "\\Needspace{8\\baselineskip}"), el}
  end
end

function Header(el)
  if el.level == 2 and pandoc.utils.stringify(el):match("^3%.5") then
    return {pandoc.RawBlock("latex", "\\Needspace{24\\baselineskip}"), el}
  end
end

function Table(el)
  if #el.colspecs == 7 then
    local widths = {0.22, 0.16, 0.06, 0.06, 0.14, 0.20, 0.16}
    for i, spec in ipairs(el.colspecs) do
      spec[2] = widths[i]
    end
    return el
  end
end
