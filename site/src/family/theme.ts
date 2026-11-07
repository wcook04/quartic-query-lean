// Night by default, as the family's sites read best; a stored choice of day is
// kept. Adapted from lean-exposition site/src/app/theme.ts at ed08df8,
// Copyright 2026 lean-exposition contributors, Apache-2.0.
import { useEffect, useState } from "react";

export type Scheme = "light" | "dark";
const KEY = "quartic-theme";

export function currentScheme(): Scheme {
  return document.documentElement.getAttribute("data-theme") === "light" ? "light" : "dark";
}

function syncBrowserColour() {
  const colour = getComputedStyle(document.documentElement).getPropertyValue("--paper").trim();
  const meta = document.querySelector<HTMLMetaElement>('meta[name="theme-color"]');
  if (meta && colour) meta.content = colour;
}

export function setScheme(next: Scheme) {
  const root = document.documentElement;
  root.setAttribute("data-theme", next);
  syncBrowserColour();
  try { if (next === "dark") localStorage.removeItem(KEY); else localStorage.setItem(KEY, next); } catch { /* storage unavailable */ }
  document.dispatchEvent(new CustomEvent("quartic:scheme"));
}

export function useScheme(): [Scheme, (s: Scheme) => void] {
  const [scheme, set] = useState<Scheme>(currentScheme);
  useEffect(() => {
    syncBrowserColour();
    const on = () => set(currentScheme());
    document.addEventListener("quartic:scheme", on);
    return () => document.removeEventListener("quartic:scheme", on);
  }, []);
  return [scheme, setScheme];
}
