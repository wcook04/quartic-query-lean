// Addresses are hashes, so a static host under any subpath serves every link.
//   #/                                   the front page
//   #/read/<paper>?s=<selection>&v=…     a paper, a selected passage and an open view
import { useEffect, useState } from "react";

export type View = "passage" | "statement" | "lean" | "journey" | "graph" | "closed";

export interface Route {
  page: "home" | "read" | "about";
  paper?: string;
  /** A selection ID from selection/<paper>.json, or l<start>-<end> for free lines. */
  s?: string;
  /** A PDF page with no indexed statement. */
  p?: number;
  v?: View;
  st?: string;
  d?: string;
  j?: string;
  /** An element ID inside the paper, from a cross-paper link. */
  a?: string;
  /** A step within a journey. */
  step?: string;
  /** The edition a shared link was made in. */
  ed?: string;
}

export function parse(hash: string): Route {
  const [path, query = ""] = hash.replace(/^#/, "").split("?");
  const parts = path.split("/").filter(Boolean);
  const q = new URLSearchParams(query);
  if (parts[0] === "about") return { page: "about" };
  if (parts[0] !== "read" || !parts[1]) return { page: "home" };
  const p = q.get("p");
  return {
    page: "read", paper: decodeURIComponent(parts[1]),
    s: q.get("s") ?? undefined, p: p ? Number(p) : undefined,
    v: (q.get("v") as View) ?? undefined, st: q.get("st") ?? undefined,
    d: q.get("d") ?? undefined, j: q.get("j") ?? undefined, step: q.get("step") ?? undefined, a: q.get("a") ?? undefined, ed: q.get("ed") ?? undefined,
  };
}

export function href(route: Route): string {
  if (route.page === "home") return "#/";
  if (route.page === "about") return "#/about";
  const q = new URLSearchParams();
  for (const key of ["s", "p", "a", "v", "st", "d", "j", "step", "ed"] as const) {
    const value = route[key];
    if (value != null && value !== "") q.set(key, String(value));
  }
  const query = q.toString();
  return `#/read/${encodeURIComponent(route.paper!)}${query ? "?" + query : ""}`;
}

export function go(route: Route, replace = false) {
  const next = href(route);
  if (next === location.hash) return;
  if (replace) history.replaceState(history.state, "", next);
  else history.pushState(history.state, "", next);
  window.dispatchEvent(new HashChangeEvent("hashchange"));
}

export function useRoute(): Route {
  const [route, setRoute] = useState(() => parse(location.hash));
  useEffect(() => {
    const on = () => setRoute(parse(location.hash));
    window.addEventListener("hashchange", on);
    window.addEventListener("popstate", on);
    return () => { window.removeEventListener("hashchange", on); window.removeEventListener("popstate", on); };
  }, []);
  return route;
}
