// Will Cook's websites and films. family.json is an unchanged copy of sites.json
// from https://github.com/wcook04/wcook04.github.io (docs/family.md is the
// contract), as the SK Exposition site keeps it. Adapted from lean-exposition
// site/src/app/family.ts at ed08df8, Copyright 2026 lean-exposition contributors,
// Apache-2.0. This reader is not yet in the registry, so it names itself here.
import registry from "./family.json";

export interface FamilyLink { label: string; href: string }
export interface FamilySite { id: string; name: string; short: string; url: string }
export interface FamilyFilm {
  id: string;
  title: string;
  short: string;
  description: string;
  youtube: string | null;
  duration_seconds: number | null;
  still: string | null;
  /** A 640px copy of the still, for small frames. */
  still_small?: string | null;
}
export interface Family {
  owner: { name: string; home: string; lede: string; contact: FamilyLink[] };
  sites: FamilySite[];
  films: FamilyFilm[];
}

export const FAMILY = registry as unknown as Family;
export const SITE_NAME = "Quartic Reader";
/** The series name a held film frame carries. */
export const FILM_SERIES = SITE_NAME;

const YOUTUBE = /^https:\/\/(?:www\.youtube\.com\/watch\?v=|youtu\.be\/)[\w-]+/;
export function isReleased(film: FamilyFilm): film is FamilyFilm & { youtube: string } {
  return typeof film.youtube === "string" && YOUTUBE.test(film.youtube);
}
export function clockTime(seconds: number): string {
  const s = Math.max(0, Math.round(seconds));
  const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60);
  const pad = (n: number) => String(n).padStart(2, "0");
  return h ? `${h}:${pad(m)}:${pad(s % 60)}` : `${m}:${pad(s % 60)}`;
}
export function spokenTime(seconds: number): string {
  const s = Math.max(0, Math.round(seconds));
  const unit = (n: number, w: string) => `${n} ${w}${n === 1 ? "" : "s"}`;
  const parts = [Math.floor(s / 3600) && unit(Math.floor(s / 3600), "hour"), Math.floor((s % 3600) / 60) && unit(Math.floor((s % 3600) / 60), "minute"), s % 60 && unit(s % 60, "second")].filter(Boolean);
  return parts.length ? parts.join(" ") : unit(0, "second");
}
