import { createContext, useContext } from "react";

/** Authored titles captured by this reading edition, keyed by exact Lean name. */
export interface DeclarationTitle { title: string; title_plain: string }
export type DeclarationTitles = Record<string, DeclarationTitle>;
export const NamesContext = createContext<DeclarationTitles>({});
export const useNames = () => useContext(NamesContext);

export const isProjectDeclaration = (name: string) => /^Quartic(Query|Corpus)\./.test(name);

/** Missing editorial data never turns an identifier into a mathematical title. */
export function declarationTitle(titles: DeclarationTitles, name: string): DeclarationTitle {
  return titles[name] ?? {
    title: isProjectDeclaration(name) ? "Title unavailable" : "External package reference",
    title_plain: isProjectDeclaration(name) ? "Title unavailable" : "External package reference",
  };
}
