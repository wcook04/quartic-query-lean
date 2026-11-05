import { useEffect, useState } from "react";
import { openEdition, type Edition } from "./edition";
import { go, href, useRoute } from "./router";
import { Home } from "../home/Home";
import { ReaderPage } from "./ReaderPage";
import { About } from "./About";

export function App() {
  const route = useRoute();
  const [edition, setEdition] = useState<Edition | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [requested] = useState(() => route.ed ?? null);

  useEffect(() => {
    openEdition(requested).then(setEdition, (e) => setError(e instanceof Error ? e.message : String(e)));
  }, [requested]);

  useEffect(() => {
    const titles: Record<string, string> = { home: "Quartic reader", about: "How to read the evidence · Quartic reader" };
    document.title = route.page === "read" ? `${route.paper} · Quartic reader` : titles[route.page];
  }, [route.page, route.paper]);

  return (
    <>
      <a className="skip" href="#main" onClick={(e) => { e.preventDefault(); document.getElementById("main")?.focus(); }}>Skip to the reading</a>
      <header className="site">
        <a className="site__name" href={href({ page: "home" })}>Quartic reader</a>
        <a className="site__about" href={href({ page: "about" })}>How to read the evidence</a>
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
      {edition && route.page === "read" && <ReaderPage edition={edition} route={route} />}
    </>
  );
}
