#!/usr/bin/env python3
"""Check that the split's graph frames its subject: the card and all its drawn neighbours.

After a card is chosen on the Graph tab (every card of the Lean proof map), and after the
paper is followed to each linked paragraph of the three papers, the chosen or lit cards and
every drawn card directly joined to them by a map edge must lie wholly inside the visible
graph area. It needs Playwright for Python and a served production build (see
check_phrase_clicks.py).

    python3 tools/check_graph_focus.py http://127.0.0.1:8731/quartic-query-lean/ --width 1440 --height 900
"""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ("expert", "exposition", "reconstruction")
MEASURE = """(neighbours) => {
  const area = document.querySelector('.inspector__map');
  const canvas = area && area.querySelector('.graph__canvas:not([hidden])');
  if (!canvas || !canvas.offsetParent) return null;
  const a = area.getBoundingClientRect(), c = canvas.getBoundingClientRect();
  const box = { top: Math.max(a.top, c.top), bottom: Math.min(a.bottom, c.bottom), left: Math.max(a.left, c.left), right: Math.min(a.right, c.right) };
  const cards = new Map([...canvas.querySelectorAll('.card[data-record], .tier-card[data-record]')].filter(e => e.offsetParent).map(e => [e.dataset.record, e]));
  const selected = [...cards.values()].filter(e => e.matches('.is-selected,[data-selected=true]') || e.closest('[aria-selected=true]')).map(e => e.dataset.record);
  const lit = [...cards.values()].filter(e => e.dataset.trail === 'here' || e.classList.contains('is-here')).map(e => e.dataset.record);
  const subject = selected.length ? selected : lit;
  const want = new Set(subject);
  for (const id of subject) for (const n of neighbours[id] || []) if (cards.has(n)) want.add(n);
  const outside = [...want].filter(id => { const r = cards.get(id).getBoundingClientRect();
    return r.top < box.top - 1 || r.bottom > box.bottom + 1 || r.left < box.left - 1 || r.right > box.right + 1; });
  return { subject: subject.length, checked: want.size, outside };
}"""


def main(base, width, height, limit):
    from playwright.sync_api import sync_playwright
    manifest = ROOT / "build/reading-api/v1/index.json"
    resources = json.loads(manifest.read_text())["resources"]
    proof = json.loads((manifest.parent / resources["selection/proof-map.json"]["href"]).read_text())
    neighbours = {}
    for e in proof["edges"]:
        neighbours.setdefault(e["from"], []).append(e["to"])
        neighbours.setdefault(e["to"], []).append(e["from"])
    neighbours.setdefault(proof["root"], []).append("paper:thm-1.1")
    cards = sorted(n for n, c in proof["cards"].items() if c["kind"] not in ("inductive", "structure", "class"))
    failures, counts = [], {"cards": 0, "paragraphs": 0}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height})
        for name in cards[:limit]:
            page.goto(f"{base}#/read/reconstruction?v=graph&d={name}")
            page.wait_for_selector(".inspector__map .card[data-record], .inspector__map .tier-card", timeout=60000)
            page.wait_for_timeout(1100)
            got = page.evaluate(MEASURE, neighbours)
            counts["cards"] += 1
            if got and got["outside"]:
                failures.append({"card": name, **got})
        for paper in PAPERS:
            page.goto(f"{base}#/read/{paper}")
            page.wait_for_selector(".manuscript .phrase", timeout=60000)
            page.wait_for_timeout(1000)
            total = page.evaluate("document.querySelectorAll('.manuscript .source-block.is-linked').length")
            for i in range(min(total, limit)):
                page.evaluate("""(i) => { const b = document.querySelectorAll('.manuscript .source-block.is-linked')[i];
                  const pane = b.closest('.paper'); pane.scrollTop += b.getBoundingClientRect().top - pane.getBoundingClientRect().top - pane.clientHeight * 0.3; }""", i)
                page.mouse.move(300, 500)
                page.mouse.wheel(0, 1)
                page.wait_for_timeout(1300)
                got = page.evaluate(MEASURE, neighbours)
                counts["paragraphs"] += 1
                if got and got["subject"] and got["outside"]:
                    failures.append({"paragraph": f"{paper}#{i}", **got})
        browser.close()
    print(f"{width}x{height}: {counts['cards']} cards chosen, {counts['paragraphs']} linked paragraphs followed, {len(failures)} with a neighbour outside the graph area")
    for f in failures[:30]:
        print(" ", json.dumps(f, ensure_ascii=False)[:240])
    return 1 if failures else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("base")
    parser.add_argument("--width", type=int, default=1440)
    parser.add_argument("--height", type=int, default=900)
    parser.add_argument("--limit", type=int, default=10**6)
    args = parser.parse_args()
    sys.exit(main(args.base, args.width, args.height, args.limit))
