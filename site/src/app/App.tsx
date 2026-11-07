import { useEffect, useState } from "react";
import { openEdition, type Edition } from "./edition";
import { go, href, useRoute } from "./router";
import { Home } from "../home/Home";
import { ReaderPage } from "./ReaderPage";
import { face, PAPERS, SUPPLEMENT } from "./papers";
import { About } from "./About";
import { FAMILY } from "../family/family";
import { useScheme } from "../family/theme";
import plectis from "../family/plectis.svg?url";

export function App() {
  const route = useRoute();
  const [edition, setEdition] = useState<Edition | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [requested] = useState(() => route.ed ?? null);
  const [scheme, setScheme] = useScheme();

  useEffect(() => {
    openEdition(requested).then(setEdition, (e) => setError(e instanceof Error ? e.message : String(e)));
  }, [requested]);

  useEffect(() => {
    const titles: Record<string, string> = { home: "Quartic reader", about: "How to read the evidence · Quartic reader" };
    const known = route.paper != null && (PAPERS.some((p) => p.id === route.paper) || route.paper === SUPPLEMENT.id);
    document.title = route.page === "read" ? `${known ? face(route.paper!).tab : "Paper unavailable"} · Quartic reader` : titles[route.page] ?? titles.home;
  }, [route.page, route.paper]);

  return (
    <>
      <a className="skip" href="#main" onClick={(e) => { e.preventDefault(); document.getElementById("main")?.focus(); }}>Skip to the reading</a>
      <header className="site">
        <span className="fam-lockup">
          <a className="fam-lockup__home" href={FAMILY.owner.home} rel="author" title="All of Will Cook’s websites and videos">
            <img src={plectis} alt="Will Cook: all websites and videos" width={26} height={26} />
          </a>
          <span className="fam-lockup__rule" aria-hidden="true" />
          <a className="fam-lockup__site" href={href({ page: "home" })} aria-current={route.page === "home" ? "page" : undefined}>
            <span className="fam-lockup__name">Quartic Reader</span>
          </a>
        </span>
        <span className="site__tools">
          <a className="site__about" href={href({ page: "about" })}>How to read the evidence</a>
          <button type="button" className="scheme" onClick={() => setScheme(scheme === "dark" ? "light" : "dark")} aria-label={scheme === "dark" ? "Switch to day colours" : "Switch to night colours"}>
            {scheme === "dark" ? "Day" : "Night"}
          </button>
        </span>
      </header>
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
        <main id="main" className="notice-page"><h1>The reading edition did not load.</h1><p>{error}</p><p>Reload the page to try again.</p></main>
      )}
      {!edition && !error && <p className="pending pending--page" role="status">Opening the reading edition…</p>}
      {edition && route.page === "home" && <Home edition={edition} />}
      {edition && route.page === "about" && <About />}
      {edition && route.page === "read" && <ReaderPage key={`${edition.permalink}:${route.paper}`} edition={edition} route={route} />}
    </>
  );
}
