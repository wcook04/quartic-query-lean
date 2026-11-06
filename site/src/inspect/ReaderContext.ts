import { createContext, useContext } from "react";
import type { Reader } from "../app/edition";

export const ReaderContext = createContext<Reader | null>(null);
export const useReader = () => useContext(ReaderContext)!;
