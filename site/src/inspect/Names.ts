import { createContext, useContext } from "react";

/** Plain titles for Lean declarations, from the edition's proof map. */
export const NamesContext = createContext<Record<string, string>>({});
export const useNames = () => useContext(NamesContext);
