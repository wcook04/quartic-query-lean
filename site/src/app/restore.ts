// Adapted from Lean Exposition's app/restore.ts and app/trail.ts, Apache-2.0.
// Source: wcook04/lean-exposition, revision 0064f9b1a9534720721ed49b16c765b2e0eef134.
// Inner scrollers belong to history entries; the session mirror lets us save the
// entry being left even after popstate has changed history.state underneath it.
import { useLayoutEffect, useSyncExternalStore } from "react";

export interface KeptScroll {
  window: [number, number];
  inner: Record<string, [number, number]>;
  focus?: string;
  disclosures?: boolean[];
}
interface Place { hash: string; edition: string; paper: string; scroll: KeptScroll }
interface Origin { key: string; label: string; place: Place }
interface Entry { key: string; hash: string; place?: Place; origin?: Origin }
const STATE = "quarticReadingPlace";
const STORE = "quartic:reading-places:v1";
const SCROLLERS = [".paper", ".inspector", ".inspector__body", ".contents", "[data-keep]"];
const INPUT = ["wheel", "touchstart", "pointerdown", "keydown"] as const;
const entries = new Map<string, Entry>();
const papers = new Map<string, Place>();
const focused = new Map<string, string>();
const listeners = new Set<() => void>();
let live: Entry;
let edition = "";
let paper = "";
let restoring = false;
let stopRestore: (() => void) | undefined;

const key = () => crypto.randomUUID();
const state = () => history.state && typeof history.state === "object" ? history.state : {};
const paperKey = (ed: string, id: string) => `${ed}:${id}`;
const notify = () => listeners.forEach((fn) => fn());
function persist() {
  entries.set(live.key, live);
  while (entries.size > 100) entries.delete(entries.keys().next().value!);
  try { sessionStorage.setItem(STORE, JSON.stringify({ entries: [...entries], papers: [...papers] })); } catch { /* storage may be unavailable */ }
  if (state()[STATE]?.key === live.key) history.replaceState({ ...state(), [STATE]: live }, "");
}
function focusSelector(el: Element | null): string | undefined {
  if (!(el instanceof HTMLElement) || !el.closest(".paper,.inspector,.contents")) return;
  if (el.id) return `#${CSS.escape(el.id)}`;
  const block = el.closest<HTMLElement>("[data-l0]");
  if (block && el === block) return `.paper [data-l0="${CSS.escape(block.dataset.l0!)}"]`;
  // Preserve focus on a particular control, including repeated labelled links.
  const scope = el.closest(".inspector") ? ".inspector" : el.closest(".contents") ? ".contents" : ".paper";
  const attr = el.getAttribute("aria-label") != null ? "aria-label" : el.getAttribute("href") != null ? "href" : null;
  if (attr) {
    const selector = `${scope} ${el.tagName.toLowerCase()}[${attr}="${CSS.escape(el.getAttribute(attr)!)}"]`;
    if (document.querySelectorAll(selector).length === 1) return selector;
  }
  const parts: string[] = [];
  let node: HTMLElement | null = el;
  while (node && !node.matches(scope)) {
    const tag = node.tagName.toLowerCase();
    const siblings: Element[] = Array.from(node.parentElement?.children ?? []).filter((n) => n.tagName === node!.tagName);
    parts.unshift(`${tag}:nth-of-type(${siblings.indexOf(node) + 1})`);
    node = node.parentElement;
  }
  return node ? `${scope} > ${parts.join(" > ")}` : undefined;
}
export function snapshotScroll(): KeptScroll {
  const inner: KeptScroll["inner"] = {};
  for (const selector of SCROLLERS) document.querySelectorAll<HTMLElement>(selector).forEach((el, i) => {
    inner[`${selector}@${i}`] = [el.scrollTop, el.scrollLeft];
  });
  return {
    window: [window.scrollY, window.scrollX], inner,
    focus: focusSelector(document.activeElement) ?? focused.get(live.key),
    disclosures: Array.from(document.querySelectorAll<HTMLDetailsElement>(".inspector details")).map((el) => el.open),
  };
}
function find(id: string): HTMLElement | undefined {
  const at = id.lastIndexOf("@");
  return document.querySelectorAll<HTMLElement>(id.slice(0, at))[Number(id.slice(at + 1))];
}

/** Retry while lazy manuscripts, math, figures and fonts change the layout.
 * Any reader input cancels the entire operation, including later font refits. */
export function restoreScroll(kept: KeptScroll): () => void {
  let frame = 0, ended = false, still = performance.now(), height = -1;
  const start = performance.now();
  const end = () => {
    if (ended) return;
    ended = true;
    restoring = false;
    cancelAnimationFrame(frame);
    document.fonts?.removeEventListener("loadingdone", changed);
    for (const type of INPUT) window.removeEventListener(type, end, true);
  };
  const changed = () => { still = performance.now(); };
  const step = () => {
    if (ended) return;
    let waiting = false, moved = false;
    document.querySelectorAll<HTMLDetailsElement>(".inspector details").forEach((el, i) => {
      const open = kept.disclosures?.[i];
      if (open != null && el.open !== open) { el.open = open; moved = true; }
    });
    const [top, left] = kept.window;
    if (Math.abs(window.scrollY - top) > 1 || Math.abs(window.scrollX - left) > 1) {
      window.scrollTo({ top, left, behavior: "instant" }); moved = true;
    }
    for (const [id, [y, x]] of Object.entries(kept.inner)) {
      const el = find(id);
      if (!el) { waiting = true; continue; }
      if (y > el.scrollHeight - el.clientHeight + 1 || x > el.scrollWidth - el.clientWidth + 1) waiting = true;
      if (Math.abs(el.scrollTop - y) > 1 || Math.abs(el.scrollLeft - x) > 1) {
        el.scrollTo({ top: y, left: x, behavior: "instant" }); moved = true;
      }
    }
    // Wait for actual manuscript content even when the saved offset was zero.
    if (document.querySelector(".paper .pending, .paper .manuscript[hidden]")) waiting = true;
    if (kept.focus) {
      const target = document.querySelector<HTMLElement>(kept.focus);
      if (target && document.activeElement !== target) target.focus({ preventScroll: true });
    }
    const nextHeight = document.documentElement.scrollHeight + Object.keys(kept.inner).reduce((sum, id) => sum + (find(id)?.scrollHeight ?? 0), 0);
    if (height !== nextHeight) moved = true;
    height = nextHeight;
    const now = performance.now();
    if (waiting || moved || document.fonts?.status === "loading") still = now;
    if (now - start >= 15000 || now - still >= 3000) return end();
    frame = requestAnimationFrame(step);
  };
  restoring = true;
  for (const type of INPUT) window.addEventListener(type, end, { capture: true, passive: true });
  document.fonts?.addEventListener("loadingdone", changed);
  frame = requestAnimationFrame(step);
  return end;
}
export const isRestoringReadingPlace = () => restoring;

/** Called before history mutation, while the old DOM and identity still agree. */
export function saveReadingPlace() {
  if (!live) return;
  // Preserve the intended target if we leave before its lazy content arrives.
  if (edition && paper && !restoring && document.querySelector(".paper") && live.hash.startsWith(`#/read/${encodeURIComponent(paper)}`)) {
    live.place = { hash: live.hash, edition, paper, scroll: snapshotScroll() };
  }
  if (live.place) papers.set(paperKey(live.place.edition, live.place.paper), live.place);
  persist();
}
export function previousPaperPlace(target: string): Place | undefined {
  saveReadingPlace();
  return papers.get(paperKey(edition, target));
}
export function excursionOrigin(label: string): Origin | undefined {
  saveReadingPlace();
  return live.origin ?? (live.place ? { key: live.key, label, place: live.place } : undefined);
}

/** Router integration: a replace refines this entry; a push has a fresh identity. */
export function navigateEntry(hash: string, replace = false, place?: Place, origin?: Origin | null) {
  saveReadingPlace();
  stopRestore?.();
  if (replace) {
    live = { ...live, hash };
    if (live.place) live.place = { ...live.place, hash };
  } else live = { key: key(), hash, place, origin: origin === null ? undefined : origin ?? live.origin };
  history[replace ? "replaceState" : "pushState"]({ ...state(), [STATE]: live }, "", hash);
  persist();
  notify();
}
function arrive() {
  // popstate already points to the destination. Save old DOM through live key.
  if (state()[STATE]?.key === live.key && location.hash === live.hash) return;
  saveReadingPlace();
  stopRestore?.();
  const held = state()[STATE] as Entry | undefined;
  live = held?.key && held.hash === location.hash ? entries.get(held.key) ?? held : { key: key(), hash: location.hash };
  history.replaceState({ ...state(), [STATE]: live }, "");
  persist();
  notify();
}
const subscribe = (fn: () => void) => { listeners.add(fn); return () => { listeners.delete(fn); }; };

/** Mount in ReaderPage, including when it is keyed by edition and paper.
 * Module/history state survives remount; a route replacement keeps its entry. */
export function useReadingPlace(id: string, editionKey: string) {
  const entry = useSyncExternalStore(subscribe, () => live.key);
  useLayoutEffect(() => {
    edition = editionKey; paper = id;
    const kept = live.place;
    if (kept?.edition === editionKey && kept.paper === id) {
      stopRestore?.(); stopRestore = restoreScroll(kept.scroll);
      return () => { stopRestore?.(); stopRestore = undefined; };
    }
  }, [entry, id, editionKey]);
}
export function useReturnToPaper(): { label: string; returnToOrigin(): void } | null {
  const origin = useSyncExternalStore(subscribe, () => live.origin);
  const currentPaper = decodeURIComponent(location.hash.replace(/^#\/read\//, "").split(/[?\/]/)[0]);
  if (!origin || origin.place.edition !== edition || origin.place.paper === currentPaper) return null;
  return { label: origin.label, returnToOrigin() {
    saveReadingPlace();
    stopRestore?.();
    live = { key: key(), hash: origin.place.hash, place: entries.get(origin.key)?.place ?? origin.place };
    history.pushState({ ...state(), [STATE]: live }, "", live.hash);
    persist(); notify();
    window.dispatchEvent(new HashChangeEvent("hashchange"));
  } };
}

if (typeof window !== "undefined") {
  try {
    const stored = JSON.parse(sessionStorage.getItem(STORE) ?? "{}");
    for (const [k, value] of stored.entries ?? []) entries.set(k, value);
    for (const [k, value] of stored.papers ?? []) papers.set(k, value);
  } catch { /* memory/history remain usable */ }
  const held = state()[STATE] as Entry | undefined;
  live = held?.key ? entries.get(held.key) ?? held : { key: key(), hash: location.hash };
  history.replaceState({ ...state(), [STATE]: live }, "");
  history.scrollRestoration = "manual";
  window.addEventListener("popstate", arrive);
  window.addEventListener("hashchange", arrive);
  window.addEventListener("pagehide", saveReadingPlace);
  document.addEventListener("focusin", () => {
    const selector = focusSelector(document.activeElement);
    if (selector) focused.set(live.key, selector);
  });
  document.addEventListener("visibilitychange", () => { if (document.visibilityState === "hidden") saveReadingPlace(); });
}
