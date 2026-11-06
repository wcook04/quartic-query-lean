import { useEffect, useState } from "react";

export type Async<T> = { state: "loading" } | { state: "ready"; value: T } | { state: "failed"; error: Error };

export function useAsync<T>(run: () => Promise<T>, deps: unknown[]): Async<T> {
  const [result, setResult] = useState<Async<T>>({ state: "loading" });
  useEffect(() => {
    let live = true;
    setResult({ state: "loading" });
    run().then(
      (value) => live && setResult({ state: "ready", value }),
      (error) => live && setResult({ state: "failed", error: error instanceof Error ? error : new Error(String(error)) }),
    );
    return () => { live = false; };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);
  return result;
}
