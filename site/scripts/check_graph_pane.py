"""Drive the built reader in Chromium and check its Graph view against docs/graph-pane.md.

For each paper at 1440x900 and 2560x1440 the script follows the paper to a linked paragraph,
clicks a tied phrase, clicks a paragraph and clicks a card, and after each step runs the
shared checks in graph_pane_checks.py. It also opens the largest neighbourhoods of the proof
map. A click must never change the open view. The exit status is 1 when any check fails.

    cd site && VITE_BASE_PATH=/quartic-query-lean/ npm run build
    python3 scripts/check_graph_pane.py              # serves dist/ itself on a free port
    python3 scripts/check_graph_pane.py --shots /tmp/quartic-shots

It needs Python's Playwright package with Chromium installed (`pip install playwright`,
`playwright install chromium`).
"""
from __future__ import annotations

import argparse
import functools
import http.server
import socketserver
import sys
import threading
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from graph_pane_checks import check_graph_pane, check_scrolls  # noqa: E402

BASE = "/quartic-query-lean/"
PAPERS = ["expert", "exposition", "reconstruction", "original"]
SIZES = [(1440, 900), (2560, 1440)]
DOCK = ".graph-dock"
# The largest neighbourhoods: the two declarations with the most cards around them, and the
# paragraph of the reconstruction that defines Forrelation.
BIG = [
    ("reconstruction", "d=QuarticQuery.Upper.Fkm_QLe"),
    ("reconstruction", "d=QuarticQuery.Upper.tournament_runs"),
    ("reconstruction", "s=passage%2Fforr_definition"),
]


def serve(dist: Path) -> tuple[socketserver.TCPServer, str]:
    """Serve dist/ under BASE on a free local port."""

    class Handler(http.server.SimpleHTTPRequestHandler):
        def translate_path(self, path: str) -> str:
            path = path.split("?", 1)[0].split("#", 1)[0]
            if path.startswith(BASE):
                path = "/" + path[len(BASE):]
            return super().translate_path(path)

        def log_message(self, *args) -> None:
            pass

    server = socketserver.ThreadingTCPServer(("127.0.0.1", 0), functools.partial(Handler, directory=str(dist)))
    server.daemon_threads = True
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f"http://127.0.0.1:{server.server_address[1]}{BASE}"


def settle(page: Page, ms: int = 900) -> None:
    page.wait_for_selector(".fg__card.is-subject", timeout=20000)
    page.wait_for_timeout(ms)


def view(page: Page) -> str:
    return page.evaluate("() => document.querySelector('.inspector__modes button[aria-pressed=true]')?.textContent?.trim() ?? ''")


def subjects(page: Page) -> str:
    return page.evaluate("() => document.querySelector('.fg')?.dataset.subjects ?? ''")


def follow_to_linked(page: Page) -> bool:
    """Scroll the paper so that a linked paragraph a third of the way in sits on the reading line."""
    return page.evaluate(
        """() => { const paper = document.querySelector('.paper');
        const blocks = [...document.querySelectorAll('.manuscript .source-block.is-linked')];
        if (!paper || !blocks.length) return false;
        const block = blocks[Math.floor(blocks.length / 3)];
        paper.scrollTop += block.getBoundingClientRect().top - paper.getBoundingClientRect().top - paper.clientHeight * 0.3;
        return true; }"""
    )


def run(page: Page, url: str, shots: Path | None, size: tuple[int, int]) -> list[str]:
    bad: list[str] = []
    w = size[0]

    def shot(name: str) -> None:
        if shots:
            page.screenshot(path=str(shots / f"quartic-{name}-{w}.png"))

    for paper in PAPERS:
        page.goto(f"{url}#/read/{paper}?v=graph")
        page.wait_for_selector(".manuscript:not([hidden])", timeout=30000)
        settle(page, 1500)
        if follow_to_linked(page):
            page.wait_for_timeout(1800)
            settle(page)
        label = f"{paper} {w} following"
        bad += check_graph_pane(page, label, dock=DOCK)
        bad += check_scrolls(page, label)
        if paper == "reconstruction":
            shot("following")

        # A tied phrase in view: it becomes the subject and the view stays Graph.
        phrase = page.locator(".manuscript .phrase[data-phrase]:not(.is-untied)").nth(3)
        if phrase.count():
            phrase.scroll_into_view_if_needed()
            page.wait_for_timeout(400)
            phrase.click()
            settle(page, 1500)
            label = f"{paper} {w} phrase"
            if view(page) != "Graph":
                bad.append(f"{label}: a phrase click changed the view to {view(page)}")
            bad += check_graph_pane(page, label, dock=DOCK)
            bad += check_scrolls(page, label)
            if paper == "reconstruction":
                shot("phrase")
            page.keyboard.press("Escape")
            page.wait_for_timeout(600)

        # A linked paragraph clicked away from its phrases: the view stays Graph.
        block = page.locator(".manuscript .source-block.is-linked").nth(2)
        block.scroll_into_view_if_needed()
        box = block.bounding_box()
        if box:
            page.mouse.click(box["x"] + 6, box["y"] + 4)
            page.wait_for_timeout(1200)
            if view(page) != "Graph":
                bad.append(f"{paper} {w} paragraph: a paragraph click changed the view to {view(page)}")
            bad += check_graph_pane(page, f"{paper} {w} paragraph", dock=DOCK)

        # A neighbour card: it becomes the subject, the view stays Graph, and its line is drawn.
        card = page.locator(".fg__card:not(.is-subject)").first
        if card.count():
            target = card.get_attribute("data-card")
            card.scroll_into_view_if_needed()
            card.click()
            settle(page, 1500)
            label = f"{paper} {w} card"
            if subjects(page) != target:
                bad.append(f"{label}: clicking {target} made {subjects(page)} the subject")
            if view(page) != "Graph":
                bad.append(f"{label}: a card click changed the view to {view(page)}")
            bad += check_graph_pane(page, label, dock=DOCK)
            bad += check_scrolls(page, label)
            if paper == "reconstruction":
                shot("card")
            page.keyboard.press("Escape")
            page.wait_for_timeout(800)
            if page.locator(".graph-acts__btn", has_text="Follow the paper").count():
                bad.append(f"{paper} {w}: Escape did not return the pane to following the paper")

    for i, (paper, query) in enumerate(BIG):
        page.goto(f"{url}#/read/{paper}?v=graph&{query}")
        page.wait_for_selector(".manuscript:not([hidden])", timeout=30000)
        settle(page, 2500)
        if query.startswith("s="):
            # A paragraph named in the address: click it so that its steps are the subject.
            block = page.locator(".manuscript .source-block.is-selected").first
            block.scroll_into_view_if_needed()
            box = block.bounding_box()
            page.mouse.click(box["x"] + 6, box["y"] + 4)
            settle(page, 2500)
        label = f"{paper} {w} big {query}"
        bad += check_graph_pane(page, label, dock=DOCK)
        bad += check_scrolls(page, label)
        if i == 0:
            shot("big")
    return bad


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--url", help="a running build, e.g. http://127.0.0.1:8641/quartic-query-lean/")
    ap.add_argument("--dist", type=Path, default=Path(__file__).resolve().parent.parent / "dist")
    ap.add_argument("--shots", type=Path, help="save screenshots of the reconstruction's states here")
    args = ap.parse_args()
    server = None
    url = args.url
    if not url:
        if not (args.dist / "index.html").exists():
            print(f"No build at {args.dist}; run `VITE_BASE_PATH={BASE} npm run build` first.", file=sys.stderr)
            return 2
        server, url = serve(args.dist)
    if args.shots:
        args.shots.mkdir(parents=True, exist_ok=True)
    bad: list[str] = []
    errors: list[str] = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for size in SIZES:
                page = browser.new_page(viewport={"width": size[0], "height": size[1]})
                page.on("pageerror", lambda e: errors.append(str(e)))
                page.on("console", lambda m: m.type == "error" and errors.append(m.text))
                bad += run(page, url, args.shots, size)
                page.close()
            browser.close()
    finally:
        if server:
            server.shutdown()
    bad += [f"console: {e}" for e in errors]
    for line in bad:
        print("FAIL", line)
    print("graph pane checks:", "passed" if not bad else f"{len(bad)} failures")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
