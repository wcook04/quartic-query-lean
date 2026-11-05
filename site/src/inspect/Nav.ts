import { createContext, useContext } from "react";

export interface Nav {
  paper: string;
  openSelection(paper: string, id: string): void;
  openStatement(id: string): void;
  openLean(name: string): void;
  openGraph(name?: string): void;
  openPath(edge: string): void;
  openJourney(id: string): void;
  backToPassage(): void;
}

export const NavContext = createContext<Nav | null>(null);
export const useNav = () => useContext(NavContext)!;
