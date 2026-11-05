// Copied from proof-reader web/src at e2df888, Copyright 2026 proof-reader
// contributors, Apache-2.0 (adapted from Lean Exposition's map).
// prefers-reduced-motion, read live: a change in the system setting applies at once.

import { useEffect, useState } from "react";

const QUERY = "(prefers-reduced-motion: reduce)";

export function useReducedMotion(): boolean {
  const [reduced, setReduced] = useState(() => typeof window !== "undefined" && !!window.matchMedia?.(QUERY).matches);
  useEffect(() => {
    const mq = window.matchMedia?.(QUERY);
    if (!mq) return;
    const on = () => setReduced(mq.matches);
    on();
    mq.addEventListener("change", on);
    return () => mq.removeEventListener("change", on);
  }, []);
  return reduced;
}
