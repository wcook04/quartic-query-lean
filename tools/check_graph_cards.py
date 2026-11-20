#!/usr/bin/env python3
"""Render every graph card in the built reader and check that each title is whole.

Every card of the Lean proof map is opened on the Graph tab, which draws it with its
neighbours; every phrase declaration that the map does not draw is opened through its phrase,
which draws its Lean neighbourhood. For each drawn card the check fails when its title is cut
to "…" or to one word and "…", clipped by its box, or running past the card's border. It needs
Playwright for Python and a served production build (see check_phrase_clicks.py).

    python3 tools/check_graph_cards.py http://127.0.0.1:8731/quartic-query-lean/
"""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECK = """() => {
  const out = [];
  for (const el of document.querySelectorAll('.inspector__graph .card[data-record], .inspector__graph .lg-card')) {
    if (!el.offsetParent) continue;
    const box = el.getBoundingClientRect();
    const canvas = el.closest('.graph__canvas, .local-graph__body')?.getBoundingClientRect();
    if (box.width < 2 || (canvas && (box.bottom < canvas.top || box.top > canvas.bottom || box.right < canvas.left || box.left > canvas.right))) continue;
    const title = el.querySelector('.card__ctitle, .lg-card__title');
    if (!title) continue;
    const shown = title.dataset.short ?? (title.querySelector('.katex') ? null : title.textContent.trim());
    const cs = getComputedStyle(title);
    const hides = cs.overflow !== 'visible' || cs.webkitLineClamp !== 'none';
    const t = title.getBoundingClientRect();
    const clipped = hides && (title.scrollHeight > title.clientHeight + 2 || title.scrollWidth > title.clientWidth + 2);
    const overflow = t.right > box.right + 1 || t.bottom > box.bottom + 1 || t.left < box.left - 1;
    const stub = !!shown && /^(?:\\S+)?…$/.test(shown);
    if (clipped || overflow || stub || title.dataset.short) out.push({record: el.dataset.record, clipped, overflow, stub, short: title.dataset.short || null});
  }
  return out;
}"""


def main(base, width, height, limit):
    from playwright.sync_api import sync_playwright
    manifest = ROOT / "build/reading-api/v1/index.json"
    resources = json.loads(manifest.read_text())["resources"]
    load = lambda p: json.loads((manifest.parent / resources[p]["href"]).read_text())
    cards = sorted(n for n, c in load("selection/proof-map.json")["cards"].items() if c["kind"] not in ("inductive", "structure", "class"))
    undrawn = {}
    for paper in ("expert", "exposition", "reconstruction"):
        for tie in json.loads((ROOT / f"docs/reading_phrases/{paper}.json").read_text())["ties"]:
            for row in tie["lean"][:1]:
                if row["name"] not in cards and row["name"] not in undrawn:
                    undrawn[row["name"]] = (paper, tie["id"])
    failures = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height})
        for name in cards[:limit]:
            page.goto(f"{base}#/read/reconstruction?v=graph&d={name}")
            page.wait_for_selector(".inspector__graph .card[data-record]", timeout=60000)
            page.wait_for_timeout(900)
            bad = page.evaluate(CHECK)
            if bad:
                failures.append({"view": f"map:{name}", "cards": bad})
        print(f"passage map: {min(len(cards), limit)} cards opened, {sum(1 for f in failures if f['view'].startswith('map:'))} views with a cut title")
        for name, (paper, tie) in list(undrawn.items())[:limit]:
            page.goto(f"{base}#/read/{paper}?v=graph&d={name}&ph={tie}")
            try:
                page.wait_for_selector(".inspector__graph .lg-card, .inspector__graph .card[data-record]", timeout=20000)
            except Exception:
                failures.append({"view": f"neighbourhood:{name}", "cards": "nothing drawn"})
                continue
            page.wait_for_timeout(700)
            bad = page.evaluate(CHECK)
            if bad:
                failures.append({"view": f"neighbourhood:{name}", "cards": bad})
        print(f"neighbourhoods: {min(len(undrawn), limit)} declarations opened, {sum(1 for f in failures if f['view'].startswith('neighbourhood:'))} views with a cut title")
        browser.close()
    for f in failures[:40]:
        print(json.dumps(f, ensure_ascii=False)[:300])
    return 1 if failures else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("base")
    parser.add_argument("--width", type=int, default=1440)
    parser.add_argument("--height", type=int, default=900)
    parser.add_argument("--limit", type=int, default=10**6)
    args = parser.parse_args()
    sys.exit(main(args.base, args.width, args.height, args.limit))
