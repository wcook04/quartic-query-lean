#!/usr/bin/env python3
"""Click every phrase tied to Lean in the built reader and check that its card opens.

For each of the three papers this opens the reader on the Graph tab, clicks every phrase
span that names a Lean declaration (in paragraphs, the abstract, captions, tables, lists,
asides and appendices alike) and checks that the split below the graph shows that
phrase's card for the phrase's first declaration. It needs Playwright for Python and a
served production build, for example:

    cd site && VITE_BASE_PATH=/quartic-query-lean/ npm run build
    python3 -m http.server 8731 --directory <folder holding quartic-query-lean -> site/dist>
    python3 tools/check_phrase_clicks.py http://127.0.0.1:8731/quartic-query-lean/

It prints the phrases whose click opened nothing (or the wrong card) and exits 1 if any.
"""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ("expert", "exposition", "reconstruction")


def expected(paper):
    data = json.loads((ROOT / f"docs/reading_phrases/{paper}.json").read_text())
    return {t["id"]: t["lean"][0]["name"] for t in data["ties"] if t["lean"]}


def main(base, papers, width, height, timeout):
    from playwright.sync_api import sync_playwright
    failures = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for paper in papers:
            want = expected(paper)
            page = browser.new_page(viewport={"width": width, "height": height})
            page.goto(f"{base}#/read/{paper}")
            page.wait_for_selector(".manuscript .phrase", timeout=60000)
            page.wait_for_timeout(800)
            dead = []
            for ident, name in want.items():
                span = page.locator(f'.manuscript .phrase[data-phrase="{ident}"]').first
                if not span.count():
                    dead.append((ident, "not rendered"))
                    continue
                span.evaluate("e => e.scrollIntoView({block: 'center'})")
                span.click()
                card = page.locator(f'.phrase-split [data-phrase-card="{ident}"][data-lean-name="{name}"]')
                try:
                    card.first.wait_for(timeout=timeout)
                except Exception:
                    dead.append((ident, "no card"))
            failures[paper] = dead
            print(f"{paper}: {len(want)} phrases with Lean, {len(dead)} dead")
            for ident, why in dead:
                print(f"  {ident}: {why}")
            page.close()
        browser.close()
    return 1 if any(failures.values()) else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("base", help="the served reader, ending in a slash")
    parser.add_argument("--paper", choices=PAPERS, action="append")
    parser.add_argument("--width", type=int, default=1440)
    parser.add_argument("--height", type=int, default=900)
    parser.add_argument("--timeout", type=int, default=4000, help="milliseconds to wait for each card")
    args = parser.parse_args()
    sys.exit(main(args.base, args.paper or PAPERS, args.width, args.height, args.timeout))
