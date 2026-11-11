// This site's two videos. Titles, addresses and lengths come from the family
// registry (family.json); the stills are local copies of the published
// thumbnails from https://github.com/wcook04/wcook04.github.io
// (assets/films/next/short-quartic-*.webp and assets/films/quartic-query-*.webp).
import { FAMILY, type FamilyFilm } from "./family";
import short1280 from "./quartic-short-thumbnail.webp";
import short640 from "./quartic-short-thumbnail-640.webp";
import long1280 from "./quartic-video-thumbnail.webp";
import long640 from "./quartic-video-thumbnail-640.webp";

function registered(id: string, still: string, still_small: string): FamilyFilm {
  const film = FAMILY.films.find((f) => f.id === id);
  if (!film) throw new Error(`family.json has no film ${id}`);
  return { ...film, still, still_small };
}

/** The short video, 1:50. */
export const SHORT_FILM = registered("short-quartic", short1280, short640);
/** The full video, 34:02. The homepage takes its title and chapters from the edition. */
export const LONG_FILM = registered("quartic-query", long1280, long640);
export const LONG_STILLS = { still: long1280, still_small: long640 };
