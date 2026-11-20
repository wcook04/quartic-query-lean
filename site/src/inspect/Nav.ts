import { createContext, useContext } from "react";

export interface Nav {
  paper: string;
  openSelection(paper: string, id: string): void;
  openPassage(paper: string, anchor?: string): void;
  openStatement(id: string): void;
  /** Open a declaration in the Lean tab; with a phrase, its tied lines are lit. */
  openLean(name: string, phrase?: string): void;
  /** Open the Lean tab; it follows the paper unless a declaration is chosen. */
  openLeanTab?(): void;
  openGraph(name?: string): void;
  openPath(edge: string): void;
  openJourney(id: string): void;
  backToPassage(): void;
  /** Scroll the paper to a passage in it, keeping the current view open. */
  showInPaper(id: string): void;
}

export const NavContext = createContext<Nav | null>(null);
export const useNav = () => useContext(NavContext)!;
