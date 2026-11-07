import { useEffect, useState } from "react";
import type { Edition } from "../app/edition";
import { href } from "../app/router";
import { PAPERS, SUPPLEMENT } from "../app/papers";
import { Board } from "./Board";
import { inlineTex } from "../text/html";
import { Exponent } from "./Exponent";
import { Architecture } from "./Architecture";
import type { BoardData } from "./Board";
import { FilmChapters, FilmSlot, type Chapter } from "../family/FilmSlot";
import { SisterSites } from "../family/SisterSites";
import { isReleased, type FamilyFilm } from "../family/family";
import videoThumbnail from "../family/quartic-video-thumbnail.webp";
import stillDark1440 from "./reader-passage-dark-1440.webp";
import stillDark2880 from "./reader-passage-dark-2880.webp";
import stillLight1440 from "./reader-passage-light-1440.webp";
import stillLight2880 from "./reader-passage-light-2880.webp";

const STILLS = { dark: { 1440: stillDark1440, 2880: stillDark2880 }, light: { 1440: stillLight1440, 2880: stillLight2880 } } as const;

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
          const to = c.page ? href({ page: "read", paper: c.page })
            : r?.reconstruction ? href({ page: "read", paper: "reconstruction", s: `passage/${r.reconstruction}` }) : undefined;
          return { ...c, title: c.title ?? r?.title, href: to };
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
    <main id="main" className="home" tabIndex={-1}>
      <section className="hero">
        <div className="hero__text">
          <h1 className="hero__title">How many bits must an algorithm read?</h1>
          <p className="hero__lede">
            For every power below four, OpenAI built a total Boolean function whose randomized query cost exceeds that
            power of its quantum query cost. Four is the best possible exponent. Read their paper, three accounts of
            its proof, and a Lean proof you can open beside any of them.
          </p>
          <p className="hero__note">
            The theorem and its proof are OpenAI’s. The three accounts, the Lean and the links between them were
            prepared with AI. <a href={href({ page: "about" })}>How to read the evidence</a>
          </p>
          <p className="hero__links">
            <a className="button" href={href({ page: "read", paper: "expert" })}>Read the expert companion</a>
            <a className="button button--quiet" href={href({ page: "read", paper: "exposition" })}>Start with a worked example</a>
          </p>
        </div>
        {board ? <Board data={board} /> : loadError ? <p role="alert">The reading guide could not be loaded.</p>
          : !entrances && <div className="board board--pending" role="status">Loading the table…</div>}
      </section>

      <ReaderStill />

      {family && (
        <section className="math-bands">
          {family.scaling && <Exponent examples={family.scaling.examples} parameters={family.scaling.parameters} />}
          {family.overview && <Architecture stages={family.overview} edition={edition} />}
        </section>
      )}

      <section className="film" aria-labelledby="film-h">
        <FilmSlot film={video.film} />
        <div>
          <h2 id="film-h">Watch it first</h2>
          <p>
            The video follows the general exposition: the table, comparing columns through pointers, the hidden
            address a classical algorithm must name, and the exponent. The construction begins at 7:16; the opening
            chapters introduce queries with a single photon. Each chapter title opens the papers at the same question.
          </p>
          {video.chapters.length > 0 && isReleased(video.film) && <FilmChapters film={video.film} chapters={video.chapters} />}
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
                <p className="way__tab">{p.tab}{paper === "expert" && <span className="way__badge">Start here</span>}</p>
                <h3 className="way__q">{e ? e.question : " "}</h3>
                <p className="way__who">{e?.audience}</p>
                {e && <p className="way__preview" dangerouslySetInnerHTML={{ __html: inlineTex(e.preview) }} />}
                <p className="way__go">
                  <a href={href({ page: "read", paper, s: e?.first_selection })} >{paper === "original" ? "Read OpenAI’s paper" : `Read the ${p.tab.charAt(0).toLowerCase()}${p.tab.slice(1)}`}</a>
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

const STILL_PASSAGE = "expert/weight/0";
const STILL_ALT = "The expert companion open at the passage on tournament weight, which is highlighted. Beside it, the graph of the Lean proof highlights the two steps that passage relies on, under the main result.";

/** A real capture of the reader, in each scheme; the hidden scheme's image is never fetched (`loading="lazy"`). Adapted from lean-exposition's FrontPage ReaderStill. */
function ReaderStill() {
  const open = href({ page: "read", paper: "expert", s: STILL_PASSAGE, v: "graph" });
  return (
    <section className="readerstill" aria-labelledby="readerstill-h">
      <div className="readerstill__prose">
        <h2 id="readerstill-h">A passage beside its Lean</h2>
        <p>
          In the picture, a reader has clicked a paragraph of the expert companion. The graph of the Lean proof
          beside it now highlights the steps that paragraph relies on, with their inputs and uses.
        </p>
        <p>
          Click the same paragraph again for those steps’ Lean, and once more for the same argument in the other
          papers. With nothing clicked, the graph follows the paragraph you are reading. A margin mark shows which
          paragraphs are linked; not all of them are yet.
        </p>
        <p><a href={open}>Open this paragraph</a></p>
      </div>
      <figure className="readerstill__fig">
        <a href={open} className="readerstill__link" aria-label="Open this paragraph of the expert companion with its Lean graph">
          {(["light", "dark"] as const).map((scheme) => (
            <img key={scheme} className={`readerstill__img readerstill__img--${scheme}`}
              src={STILLS[scheme][1440]} srcSet={`${STILLS[scheme][1440]} 1440w, ${STILLS[scheme][2880]} 2880w`}
              sizes="(min-width: 1000px) 62vw, 100vw" alt={STILL_ALT} width={1440} height={790} loading="lazy" decoding="async" />
          ))}
        </a>
      </figure>
    </section>
  );
}
