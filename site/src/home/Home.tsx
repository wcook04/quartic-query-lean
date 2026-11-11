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
import { ResultsBand } from "../results/Results";
import { LeanCode } from "../lean/LeanCode";
import { RelationMark } from "../inspect/evidence";
import { useAsync } from "../app/useAsync";
import { isReleased, type FamilyFilm } from "../family/family";
import { LONG_STILLS, SHORT_FILM } from "../family/films";
import { clockTime, spokenTime } from "../family/family";
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

const REPOSITORY = "https://github.com/wcook04/quartic-query-lean";

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
            power of its quantum query cost. Four is the best possible exponent. This site has their paper, three
            accounts of its proof, and a proof in Lean, a program that checks mathematical proofs. The Lean opens in
            a pane to the right of each paper.
          </p>
          <p className="hero__note">
            The theorem and its proof are OpenAI’s. The three accounts, the Lean and the links between them were
            prepared with AI. <a href={href({ page: "about" })}>How to read the evidence</a>
          </p>
          <p className="hero__links">
            <a className="button" href={href({ page: "read", paper: "expert" })}>Read the expert companion</a>
            <a className="button button--quiet" href={href({ page: "read", paper: "exposition" })}>Start with a worked example</a>
          </p>
          {isReleased(SHORT_FILM) && (
            <a className="hero__film" href={SHORT_FILM.youtube} target="_blank" rel="noopener noreferrer">
              <span className="hero__film-pic">
                <img src={SHORT_FILM.still_small ?? SHORT_FILM.still ?? undefined} alt="" width={640} height={360} decoding="async" />
                <span className="hero__film-play" aria-hidden="true" />
              </span>
              <span className="hero__film-words">
                <span className="hero__film-kind">Short video</span>
                <span className="hero__film-len"><span aria-hidden="true">{clockTime(SHORT_FILM.duration_seconds ?? 0)}</span><span className="sr-only">{spokenTime(SHORT_FILM.duration_seconds ?? 0)}</span>, on YouTube</span>
              </span>
            </a>
          )}
        </div>
        {board ? <Board data={board} /> : loadError ? <p role="alert">The reading guide could not be loaded.</p>
          : !entrances && <div className="board board--pending" role="status">Loading the table…</div>}
      </section>

      <HeadlinePair edition={edition} />

      <ResultsBand edition={edition} />

      <section className="films" aria-labelledby="films-h">
        <h2 id="films-h">Two videos</h2>
        <div className="films__grid">
          <FilmSlot film={SHORT_FILM} kind="Short video" />
          <div className="films__full">
            <FilmSlot film={video.film} size="inline" kind="Full video" />
            <p className="films__note">
              In the full video I go through the general exposition in order: the table, comparing columns through
              pointers, the hidden address a classical algorithm must name, and the exponent. I start the construction
              at 7:16, after introducing queries with a single photon. Each chapter title is a link to the same
              question in the papers.
            </p>
            {video.chapters.length > 0 && isReleased(video.film) && <FilmChapters film={video.film} chapters={video.chapters} />}
          </div>
        </div>
      </section>

      <ReaderStill />

      {family && (
        <section className="math-bands">
          {family.scaling && <Exponent examples={family.scaling.examples} parameters={family.scaling.parameters} />}
          {family.overview && <Architecture stages={family.overview} edition={edition} />}
        </section>
      )}

      <section className="ways" aria-labelledby="ways-h">
        <h2 id="ways-h">Four ways into the same argument</h2>
        <p>The expert companion contains the main argument. Each linked passage has links to a worked example, a complete derivation and OpenAI’s source, and a link back to the passage.</p>
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
          The <a href={href({ page: "read", paper: SUPPLEMENT.id })}>verification details</a> contain the full statement
          catalogue and the checking history. For each formal statement they give its scope separately from the written proof.
        </p>
      </section>

      <section className="credit" aria-labelledby="credit-h">
        <div className="credit__who">
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
        </div>
        <div className="credit__build" aria-labelledby="build-h">
          <h3 id="build-h">Build the Lean</h3>
          <pre className="credit__cmd"><code>{"git clone https://github.com/wcook04/quartic-query-lean\ncd quartic-query-lean/lean\nlake build QuarticQuery"}</code></pre>
          <p>
            The <code>QuarticQuery</code> target builds at the recorded commit with no <code>sorry</code>, no custom
            axioms and no <code>native_decide</code>. The toolchain is <code>leanprover/lean4:v4.36.0-rc2</code>, with
            Mathlib pinned in the repository.
          </p>
          <p className="credit__links">
            <a href={`${REPOSITORY}/blob/main/lean/QuarticQuery/Results/Unconditional.lean`} target="_blank" rel="noopener noreferrer">The main theorem on GitHub</a>
            <a href={`${REPOSITORY}#what-is-checked-and-what-that-means`} target="_blank" rel="noopener noreferrer">What is checked, and what that means</a>
          </p>
        </div>
      </section>
      <footer className="home-foot"><SisterSites /></footer>
    </main>
  );
}

function heldFilm(v: any): FamilyFilm {
  return {
    id: "quartic", short: "Quartic", still: v?.youtube_id ? LONG_STILLS.still : null, still_small: LONG_STILLS.still_small,
    title: v?.title ?? "A nearly quartic separation, explained",
    description: v?.description ?? "The board, the quantum comparisons and why the exponent approaches four.",
    youtube: v?.youtube_id ? `https://www.youtube.com/watch?v=${v.youtube_id}` : null,
    duration_seconds: v?.duration_seconds ?? null,
  };
}

const STILL_PASSAGE = "expert/weight/0";
const STILL_ALT = "The expert companion open at the passage on tournament weight, which is highlighted. In the pane to its right, the two steps that passage relies on are highlighted in the graph of the Lean proof, under the main result.";

/** A real capture of the reader, in each scheme; the hidden scheme's image is never fetched (`loading="lazy"`). Adapted from lean-exposition's FrontPage ReaderStill. */
function ReaderStill() {
  const open = href({ page: "read", paper: "expert", s: STILL_PASSAGE, v: "graph" });
  return (
    <section className="readerstill" aria-labelledby="readerstill-h">
      <div className="readerstill__prose">
        <h2 id="readerstill-h">A paragraph and the Lean linked to it</h2>
        <p>
          In the picture, a reader has clicked a paragraph of the expert companion. In the pane on the right, the
          graph of the Lean proof has the steps that paragraph relies on highlighted, with their inputs and uses.
        </p>
        <p>
          A second click on the same paragraph opens those steps’ Lean, and a third opens the same argument in the
          other papers. With nothing clicked, the graph follows the paragraph being read. Each linked paragraph has a
          mark in the margin; some paragraphs are not linked yet.
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

const HEADLINE = "thm-1.1";

/** The paper's main theorem as the project records it, and the Lean theorem compared with it, from the
 *  edition's own statement review: the same record the reader's comparison panel shows. */
function HeadlinePair({ edition }: { edition: Edition }) {
  const review = useAsync(() => edition.reader.statementReview(HEADLINE), [edition]);
  if (review.state !== "ready") return review.state === "loading" ? <section className="pair pair--pending" aria-hidden="true" /> : null;
  const r: any = review.value;
  const lead = r.comparisons?.[0];
  if (!lead?.rawLean || !r.presentation?.body) return null;
  const page = r.paper?.selection?.location?.page;
  const file = String(lead.file ?? "").replace(/^lean\//, "");
  const open = href({ page: "read", paper: "expert", s: "expert/headline/0", v: "lean", d: lead.declaration });
  return (
    <section className="pair" aria-labelledby="pair-h">
      <h2 id="pair-h">Theorem 1.1 and the Lean theorem compared with it</h2>
      <div className="pair__grid">
        <article className="pair__side pair__side--paper">
          <p className="pair__who">OpenAI’s paper{page ? `, page ${page}` : ""}, as this project records the statement</p>
          <p className="pair__name" dangerouslySetInnerHTML={{ __html: inlineTex(`Theorem 1.1. ${r.presentation.title}`) }} />
          <p className="pair__body" dangerouslySetInnerHTML={{ __html: inlineTex(r.presentation.body) }} />
        </article>
        <p className="pair__label">
          <RelationMark relation={lead.relation} />
          <span className="pair__by">Label from an AI review. No expert has reviewed it yet.</span>
        </p>
        <article className="pair__side pair__side--lean">
          <p className="pair__who">The Quartic project’s Lean</p>
          <LeanCode text={lead.rawLean} from={lead.declaration_lines?.[0] ?? 1} self={lead.declaration} label={`Lean source of ${lead.declaration}`}
            url={lead.sourceURL} foldOver={0} caption={<><span className="leancode__file">{file}</span></>} />
        </article>
      </div>
      <p className="pair__go">
        <a className="button" href={open}>Open this theorem and its Lean</a>
        <a className="button button--quiet" href={href({ page: "read", paper: "original", s: `original/${HEADLINE}`, v: "statement", st: HEADLINE })}>Open the full comparison</a>
      </p>
    </section>
  );
}
