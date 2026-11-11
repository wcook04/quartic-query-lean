// The header's Videos control: this site's short and full video, one click
// from any page, the reading desk included. A native popover, so Escape and a
// click outside close it and focus returns to the button.
import { useId, useRef } from "react";
import { clockTime, isReleased, spokenTime, type FamilyFilm } from "./family";
import { LONG_FILM, SHORT_FILM } from "./films";

const ROWS: { film: FamilyFilm; kind: string; lead: boolean }[] = [
  { film: SHORT_FILM, kind: "Short video", lead: true },
  { film: LONG_FILM, kind: "Full video", lead: false },
];

export function VideoMenu() {
  const id = useId();
  const menu = useRef<HTMLDivElement>(null);
  const rows = ROWS.filter((r) => isReleased(r.film));
  if (!rows.length) return null;
  return (
    <>
      <button type="button" className="site__videos" popoverTarget={id} aria-label="Videos" title="Videos">
        <svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true">
          <rect x="1.7" y="3.2" width="12.6" height="9.6" rx="2.2" fill="none" stroke="currentColor" strokeWidth="1.4" />
          <path d="M6.7 6v4l3.4-2z" fill="currentColor" />
        </svg>
        <span className="site__videos-word">Videos</span>
      </button>
      <div ref={menu} id={id} popover="auto" className="videomenu" aria-label="Videos">
        {rows.map(({ film, kind, lead }) => (
          <a key={film.id} className={`videomenu__row${lead ? " videomenu__row--lead" : ""}`} href={film.youtube!} target="_blank" rel="noopener noreferrer"
            onClick={() => menu.current?.hidePopover()}>
            <span className="videomenu__pic">
              {film.still && <img src={film.still_small ?? film.still} alt="" width={640} height={360} loading="lazy" decoding="async" />}
              <span className="videomenu__play" aria-hidden="true" />
            </span>
            <span className="videomenu__words">
              <span className="videomenu__kind">{kind}</span>
              {film.duration_seconds ? <span className="videomenu__len"><span aria-hidden="true">{clockTime(film.duration_seconds)}</span><span className="sr-only">{spokenTime(film.duration_seconds)}</span>, on YouTube</span> : null}
            </span>
          </a>
        ))}
      </div>
    </>
  );
}
