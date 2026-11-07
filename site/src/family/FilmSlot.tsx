// A film's place on a page, in the family's markup (styles in family.css).
// Adapted from lean-exposition site/src/app/FilmSlot.tsx at ed08df8,
// Copyright 2026 lean-exposition contributors, Apache-2.0. A film without a
// YouTube address is held in preparation; it switches by itself once the
// edition's `video` names one. Chapters open the papers on the same question.
import { clockTime, FILM_SERIES, isReleased, spokenTime, type FamilyFilm } from "./family";

export interface Chapter { start_seconds: number; route?: string; page?: string; title?: string; href?: string }

export function FilmSlot({ film, chapters = [], size = "large" }: { film: FamilyFilm; chapters?: Chapter[]; size?: "small" | "large" }) {
  const classes = ["film-slot", `film-slot--${size}`, !isReleased(film) && "film-slot--pending"].filter(Boolean).join(" ");
  if (!isReleased(film)) {
    return (
      <figure className={classes}>
        <div className="film-slot__frame film-slot__frame--pending" aria-hidden="true">
          <span className="film-slot__series">{FILM_SERIES}</span>
          <span className="film-slot__name">{film.short}</span>
          <span className="film-slot__status">In preparation</span>
        </div>
        <figcaption className="film-slot__caption">
          <p className="film-slot__title">{film.title}</p>
          <p className="film-slot__meta">Video in preparation</p>
          <p className="film-slot__text">{film.description}</p>
        </figcaption>
      </figure>
    );
  }
  const seconds = film.duration_seconds;
  return (
    <figure className={classes}>
      <a className="film-slot__frame" href={film.youtube} target="_blank" rel="noopener noreferrer" aria-hidden="true" tabIndex={-1}>
        {film.still && <img src={film.still} alt="" width={1280} height={720} loading="lazy" decoding="async" />}
        <span className="film-slot__play" />
        {seconds ? <span className="film-slot__time">{clockTime(seconds)}</span> : null}
      </a>
      <figcaption className="film-slot__caption">
        <p className="film-slot__title">
          <a href={film.youtube} target="_blank" rel="noopener noreferrer">
            {film.title}
            <span className="sr-only">, video on YouTube{seconds ? `, ${spokenTime(seconds)}` : ""}</span>
          </a>
        </p>
        <p className="film-slot__text">{film.description}</p>
        {chapters.length > 0 && <FilmChapters film={film} chapters={chapters} />}
      </figcaption>
    </figure>
  );
}

/** Chapters as an index keyed by time: the time opens the video there, the title opens the papers. */
export function FilmChapters({ film, chapters }: { film: FamilyFilm; chapters: Chapter[] }) {
  return (
    <ol className="film-chapters">
      {chapters.map((c) => {
        const name = c.title ?? c.route?.replace(/-/g, " ") ?? "";
        return (
          <li key={c.start_seconds}>
            <a className="film-chapters__time" href={`${film.youtube}&t=${c.start_seconds}s`} target="_blank" rel="noopener noreferrer"
              aria-label={`Watch from ${clockTime(c.start_seconds)}: ${name}`}>{clockTime(c.start_seconds)}</a>
            {c.href ? <a className="film-chapters__name" href={c.href}>{name}</a> : <span className="film-chapters__name">{name}</span>}
          </li>
        );
      })}
    </ol>
  );
}
