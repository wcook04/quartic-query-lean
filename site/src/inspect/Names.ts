import { createContext, useContext } from "react";
import { statementName } from "../app/papers";

/** Authored titles captured by this reading edition, keyed by exact Lean name. */
export interface DeclarationTitle { title: string; title_plain: string }
export type DeclarationTitles = Record<string, DeclarationTitle>;
export const NamesContext = createContext<DeclarationTitles>({});
export const useNames = () => useContext(NamesContext);

/** Missing editorial data never turns an identifier into a mathematical title. */
export function declarationTitle(titles: DeclarationTitles, name: string): DeclarationTitle {
  return Object.hasOwn(titles, name) ? titles[name] : { title: "Title unavailable", title_plain: "Title unavailable" };
}

/** Statement labels are loaded once for the selected edition, never per row. */
export interface StatementTitles { status: string; titles: Record<string, DeclarationTitle> }
export const StatementNamesContext = createContext<StatementTitles>({ status: "loading", titles: {} });
export const useStatementNames = () => useContext(StatementNamesContext);

export function statementTitle(index: StatementTitles, id: string): DeclarationTitle {
  const printed = statementName(id);
  const numbered = /^(thm|lem|prop|cor|def|eq|claim|rem|fact|ex)-(?:[A-Z]\.)?\d+(?:\.\d+)*(?:\.(?:i|ii|iii|iv|v|vi|vii|viii|ix|x))?$/.test(id);
  const title = Object.hasOwn(index.titles, id) ? index.titles[id] : null;
  if (title) {
    return numbered && !title.title_plain.startsWith(printed)
      ? { title: `${printed}: ${title.title}`, title_plain: `${printed}: ${title.title_plain}` }
      : title;
  }
  // Earlier editions retain their printed statement names and navigation.
  if (index.status === "unavailable_in_edition" || index.status === "archived_partial")
    return { title: printed, title_plain: printed };
  const missing = index.status === "loading" ? "Loading title…" : "Title unavailable";
  return { title: numbered ? `${printed}: ${missing}` : missing, title_plain: numbered ? `${printed}: ${missing}` : missing };
}
