import { useEffect, useState } from "react";
import type { Edition } from "../app/edition";
import { href } from "../app/router";
import { PAPERS, SUPPLEMENT } from "../app/papers";
import { Board } from "./Board";
import { inlineTex } from "../text/html";
import { Exponent } from "./Exponent";
import { Architecture } from "./Architecture";
import type { BoardData } from "./Board";
import { FilmSlot, type Chapter } from "../family/FilmSlot";
import { SisterSites } from "../family/SisterSites";
import type { FamilyFilm } from "../family/family";
import videoThumbnail from "../family/quartic-video-thumbnail.webp";

interface Entrance {
  audience: string;
  question: string;
  preview: string;
  stops: string[];
  first_selection?: string;
}

// Four independently readable accounts, with the concise companion first.
const ORDER = ["expert", "exposition", "reconstruction", "original"];

export function Home({ edition }: { edition: Edition }) {
  const [entrances, setEntrances] = useState<Record<string, Entrance> | null>(null);
  const [loadError, setLoadError] = useState(false);
  const [board, setBoard] = useState<BoardData | null>(null);
  const [family, setFamily] = useState<any>(null);
  const [video, setVideo] = useState<{ film: FamilyFilm; chapters: Chapter[] }>(() => ({ film: heldFilm(null), chapters: [] }));

  // The edition's `video` entry turns the held frame into the YouTube film.
  useEffect(() => {
    let live = true;
    edition.reader.resource("reading.json").then((reading: any) => {
      if (!live || !reading.video) return;
      const routes: any[] = reading.routes ?? [];
      setVideo({
        film: heldFilm(reading.video),
        chapters: (reading.video.chapters ?? []).map((c: any) => {
          const r = routes.find((x) => x.id === c.route);
          return { ...c, title: c.title ?? r?.title, href: r?.reconstruction ? href({ page: "read", paper: "reconstruction", s: `passage/${r.reconstruction}` }) : undefined };
        }),
      });
    }, () => {});
    return () => { live = false; };
  }, [edition]);

  useEffect(() => {
    let live = true;
    edition.reader.home().then(({ entrances, board, family }) => {
      if (live) {
        setEntrances(entrances);
        setBoard(board);
        setFamily(family);
      }
    }, () => { if (live) setLoadError(true); });
    return () => { live = false; };
  }, [edition]);

  return (
    <main id="main" className="home">
      <section className="hero">
        <div className="hero__text">
          <h1 className="hero__title">How many bits must an algorithm read?</h1>
          <p className="hero__lede">
            For every power below four, OpenAI built a total Boolean function whose randomized query cost exceeds that
            power of its quantum query cost. Four is the best possible exponent. Read their paper, three accounts of
            its proof, and a Lean proof you can open beside any of them.
          </p>
          <p className="hero__links">
            <a className="button" href={href({ page: "read", paper: "expert" })}>Read the expert companion</a>
            <a className="button button--quiet" href={href({ page: "read", paper: "exposition" })}>Start with a worked example</a>
          </p>
        </div>
        {board ? <Board data={board} /> : loadError ? <p role="alert">The reading guide could not be loaded.</p>
          : !entrances && <div className="board board--pending" role="status">Loading the table…</div>}
      </section>

      {family && (
        <section className="math-bands">
          {family.scaling && <Exponent examples={family.scaling.examples} parameters={family.scaling.parameters} />}
          {family.overview && <Architecture stages={family.overview} edition={edition} />}
        </section>
      )}

      <section className="film" aria-labelledby="film-h">
        <FilmSlot film={video.film} chapters={video.chapters} />
        <div>
          <h2 id="film-h">Watch it first</h2>
          <p>
            The video follows the general exposition: the table, comparing columns through pointers, the hidden
            address a classical algorithm must name, and the exponent. Each chapter opens the papers at the same
            question.
          </p>
        </div>
      </section>

      <section className="ways" aria-labelledby="ways-h">
        <h2 id="ways-h">Four ways into the same argument</h2>
        <p>The expert companion carries the main argument. Follow a passage into a worked example, a complete derivation or OpenAI’s source, then return to where you were reading.</p>
        <ol className="ways__list">
          {ORDER.filter((paper) => paper in edition.reader.documents).map((paper) => {
            const e = entrances?.[paper];
            const p = PAPERS.find((x) => x.id === paper)!;
            return (
              <li key={paper} className={`way way--${paper}`}>
                <p className="way__tab">{p.tab}</p>
                <h3 className="way__q">{e ? e.question : " "}</h3>
                <p className="way__who">{e?.audience}</p>
                {e && <p className="way__preview" dangerouslySetInnerHTML={{ __html: inlineTex(e.preview) }} />}
                <p className="way__go">
                  <a href={href({ page: "read", paper, s: e?.first_selection })} aria-label={`Start reading ${p.name}`}>{paper === "original" ? "Open the paper" : "Start reading"}</a>
                </p>
              </li>
            );
          })}
        </ol>
        <p className="ways__supplement">
          The <a href={href({ page: "read", paper: SUPPLEMENT.id })}>verification details</a> hold the full statement
          catalogue and checking history. They distinguish the scope of each formal statement from the written proof.
        </p>
      </section>

      <section className="credit" aria-labelledby="credit-h">
        <h2 id="credit-h">Whose work is this?</h2>
        <p>
          The theorem and construction are OpenAI’s, published with no Lean formalization. The three accounts and the
          Lean development are the Quartic project’s, prepared with AI systems under Will Cook’s direction.
        </p>
        <p>
          Lean reports each declaration’s statement, dependencies and axioms. The links between paper passages and
          Lean, and the judgments that a statement matches exactly, more strongly or only in part, were written and
          reviewed with AI. The site labels each of these where it appears. <a href={href({ page: "about" })}>How to read the evidence</a>
        </p>
      </section>
      <footer className="home-foot"><SisterSites /></footer>
    </main>
  );
}

function heldFilm(v: any): FamilyFilm {
  return {
    id: "quartic", short: "Quartic", still: v?.youtube_id ? videoThumbnail : null,
    title: v?.title ?? "A nearly quartic separation, explained",
    description: v?.description ?? "The board, the quantum comparisons and why the exponent approaches four.",
    youtube: v?.youtube_id ? `https://www.youtube.com/watch?v=${v.youtube_id}` : null,
    duration_seconds: v?.duration_seconds ?? null,
  };
}
