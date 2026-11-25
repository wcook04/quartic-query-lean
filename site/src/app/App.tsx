import { useEffect, useState } from "react";
import { openEdition, SOURCE_READER, type Edition } from "./edition";
import { followSharedPaper, go, href, useRoute } from "./router";
import { isInitialReaderEntry } from "./restore";
import { Home } from "../home/Home";
import { ReaderPage } from "./ReaderPage";
import { face, PAPERS, SUPPLEMENT } from "./papers";
import { About } from "./About";
import { ResultsPage } from "../results/Results";
import { FAMILY } from "../family/family";
import { useScheme } from "../family/theme";
import { VideoMenu } from "../family/VideoMenu";
import plectis from "../family/plectis.svg?url";
import quarticMark from "../family/quartic.svg?raw";
import { Chevron, MoonIcon, SunIcon } from "./icons";

/** The Reading library's index. The source reader's masthead wordmark opens it. */
const LIBRARY_HOME = "https://wcook04.github.io/library/";

export function App() {
  const route = useRoute();
  const [edition, setEdition] = useState<Edition | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [arrival] = useState(() => ({ route, hash: location.hash }));
  const [scheme, setScheme] = useScheme();

  useEffect(() => {
    let active = true;
    openEdition(arrival.route.ed ?? null).then(async (loaded) => {
      const shared = await followSharedPaper(arrival.route, loaded.reader).catch(() => arrival.route);
      if (!active) return;
      if (shared !== arrival.route && isInitialReaderEntry() && location.hash === arrival.hash) go(shared, true);
      setEdition(loaded);
    }, (e) => { if (active) setError(e instanceof Error ? e.message : String(e)); });
    return () => { active = false; };
  }, [arrival]);

  useEffect(() => {
    const titles: Record<string, string> = { home: "Quartic reader", about: "How to read the evidence · Quartic reader", results: "OpenAI’s results and their Lean statements · Quartic reader" };
    const known = route.paper != null && (PAPERS.some((p) => p.id === route.paper) || route.paper === SUPPLEMENT.id);
    document.title = route.page === "read" ? `${known ? face(route.paper!).tab : "Paper unavailable"} · Quartic reader` : titles[route.page] ?? titles.home;
  }, [route.page, route.paper]);

  return (
    <>
      <a className="skip" href="#main" onClick={(e) => { e.preventDefault(); document.getElementById("main")?.focus(); }}>Skip to the reading</a>
      {SOURCE_READER ? (
        <header className="site site--source">
          <span className="source-lockup">
            <a className="source-lockup__library" href={LIBRARY_HOME} translate="no">
              <span className="source-paper-mark" aria-hidden="true" dangerouslySetInnerHTML={{ __html: quarticMark }} />
              <span className="source-lockup__long">Reading library</span>
              <span className="source-lockup__short">Library</span>
            </a>
            <span className="source-lockup__rule" aria-hidden="true" />
            <a className="site__name" href="/library/quartic/">Quartic query separation</a>
          </span>
          <div className="source-reader-actions">
          <details className="jump source-reader-menu">
            <summary className="tool">Menu<Chevron /></summary>
            <ul aria-label="Quartic reader menu" onClick={(event) => {
              if ((event.target as HTMLElement).closest("a")) event.currentTarget.closest("details")!.open = false;
            }}>
              <li><a href="/library/">Reading Library</a></li>
              <li><a href={href({ page: "read", paper: "original" })} aria-current={route.paper === "original" || route.page === "home" ? "page" : undefined}>OpenAI’s original paper</a></li>
              <li><a href={href({ page: "read", paper: SUPPLEMENT.id })} aria-current={route.paper === SUPPLEMENT.id ? "page" : undefined}>{SUPPLEMENT.tab}</a></li>
              <li><a href="/library/quartic/">Expert companion</a></li>
              <li><a href="/library/quartic/exposition/">Worked exposition</a></li>
              <li><a href="/library/quartic/reconstruction/">Full proof reconstruction</a></li>
              <li><a href={href({ page: "results" })} aria-current={route.page === "results" ? "page" : undefined}>Results and Lean statements</a></li>
              <li><button type="button" className="source-reader-scheme" onClick={() => setScheme(scheme === "dark" ? "light" : "dark")}>{scheme === "dark" ? "Switch to day colours" : "Switch to night colours"}</button></li>
            </ul>
          </details>
          <a className="fam-lockup__home source-reader-owner" href={FAMILY.owner.home} rel="author">
            <img src={plectis} alt="" width={23} height={23} />
            <span className="fam-lockup__owner" translate="no">Will Cook</span>
          </a>
          </div>
        </header>
      ) : <header className="site">
        <span className="fam-lockup">
          <a className="fam-lockup__home" href={FAMILY.owner.home} rel="author" title="All of Will Cook’s projects and videos">
            <img src={plectis} alt="" width={26} height={26} />
            <span className="fam-lockup__owner" translate="no">Will Cook</span>
          </a>
          <span className="fam-lockup__rule" aria-hidden="true" />
          <a className="fam-lockup__site" href={href({ page: "home" })} aria-current={route.page === "home" ? "page" : undefined}>
            <span className="fam-lockup__name" translate="no">Quartic Reader</span>
          </a>
        </span>
        <span className="site__tools">
          <a className="site__about site__results" href={href({ page: "results" })} aria-current={route.page === "results" ? "page" : undefined}>Results and Lean statements</a>
          <a className="site__about" href={href({ page: "about" })} aria-current={route.page === "about" ? "page" : undefined}>How to read the evidence</a>
          <VideoMenu />
          <button type="button" className="scheme" onClick={() => setScheme(scheme === "dark" ? "light" : "dark")}
            aria-label={scheme === "dark" ? "Switch to day colours" : "Switch to night colours"} title={scheme === "dark" ? "Day colours" : "Night colours"}>
            {scheme === "dark" ? <SunIcon /> : <MoonIcon />}
          </button>
        </span>
      </header>}
      {edition?.pinnedOlder && (
        <p className="banner" role="status">
          This link was made in an earlier edition, and you are reading that edition.{" "}
          <button type="button" className="textbutton" onClick={() => { go({ ...route, ed: undefined }); location.reload(); }}>Open the current edition</button>
        </p>
      )}
      {edition?.missingRequested && (
        <p className="banner banner--gap" role="status">
          This link names an edition this site does not hold. You are reading the current edition, where the passage may have moved.
        </p>
      )}
      {error && (
        <main id="main" className="notice-page" tabIndex={-1}>
          <h1>The reading edition did not load</h1>
          <p>The site could not open its copy of the papers and Lean records, so nothing is shown rather than a partial page.</p>
          <p className="notice-page__detail">{error}</p>
          <p className="notice-page__actions"><button type="button" className="tool tool--primary" onClick={() => location.reload()}>Reload the page</button></p>
        </main>
      )}
      {!edition && !error && <p className="pending pending--page" role="status"><span className="pending__bar" aria-hidden="true" />Opening the reading edition…</p>}
      {edition && route.page === "home" && (SOURCE_READER ? <ReaderPage edition={edition} route={{ page: "read", paper: "original" }} /> : <Home edition={edition} />)}
      {edition && route.page === "about" && <About />}
      {edition && route.page === "results" && <ResultsPage edition={edition} />}
      {edition && route.page === "read" && <ReaderPage key={`${edition.permalink}:${route.paper}`} edition={edition} route={route} />}
    </>
  );
}
