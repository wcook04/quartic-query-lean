"""Topic colours: computed per family, stored, and checked as the page draws them.

site/scripts/topic-colours.ts gives each family of topics one hue and each topic one shade of it
(site/src/paper/palette.ts) and stores them in docs/reading_phrases/colours-<paper>.json. These
checks read the stored colours as the site publishes them, with the underline at 78% opacity over
the page composited in sRGB: any two colours of different families differ by CIEDE2000 ΔE ≥ 10
(≥ 2.5 under deuteranopia and protanopia simulation), any two shades of one family by ΔE ≥ 6 in
every vision, every colour keeps 3:1 contrast against its page and lies in sRGB, and the stored
files are what the script computes from the current phrases.
"""
import itertools
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
BACKGROUND = {"dark": "#1c1526", "light": "#f8f0e2"}
ALPHA = 0.78
FAMILY_FLOOR = {"normal": 10.0, "dichromat": 2.5}
SHADE_FLOOR = 6.0
MIN_CONTRAST = 3.0
# Machado, Oliveira and Fernandes (2009), severity 1, on linear sRGB.
VISIONS = {
    "normal": None,
    "deuteranopia": ((0.367322, 0.860646, -0.227968), (0.280085, 0.672501, 0.047413), (-0.01182, 0.04294, 0.968881)),
    "protanopia": ((0.152286, 1.052583, -0.204868), (0.114503, 0.786281, 0.099216), (-0.003882, -0.048116, 1.051998)),
}
PAPERS = ("expert", "exposition", "reconstruction")


def oklch_to_srgb(L,C,h):
    a=C*math.cos(math.radians(h)); b=C*math.sin(math.radians(h))
    l_=L+0.3963377774*a+0.2158037573*b; m_=L-0.1055613458*a-0.0638541728*b; s_=L-0.0894841775*a-1.2914855480*b
    l,m,s=l_**3,m_**3,s_**3
    r=4.0767416621*l-3.3077115913*m+0.2309699292*s
    g=-1.2684380046*l+2.6097574011*m-0.3413193965*s
    bb=-0.0041960863*l-0.7034186147*m+1.7076147010*s
    return (r,g,bb)
def in_gamut(rgb): return all(-1e-4<=c<=1+1e-4 for c in rgb)
def lin_to_gamma(c):
    c=min(1,max(0,c)); return 12.92*c if c<=0.0031308 else 1.055*c**(1/2.4)-0.055
def gamma_to_lin(c): return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def hex_rgb(h): h=h.lstrip('#'); return tuple(gamma_to_lin(int(h[i:i+2],16)/255) for i in (0,2,4))
def lab(rgb_lin):
    r,g,b=rgb_lin
    X=0.4124564*r+0.3575761*g+0.1804375*b; Y=0.2126729*r+0.7151522*g+0.0721750*b; Z=0.0193339*r+0.1191920*g+0.9503041*b
    Xn,Yn,Zn=0.95047,1.0,1.08883
    f=lambda t: t**(1/3) if t>0.008856 else 7.787*t+16/116
    fx,fy,fz=f(X/Xn),f(Y/Yn),f(Z/Zn)
    return (116*fy-16,500*(fx-fy),200*(fy-fz))
def de2000(l1,l2):
    L1,a1,b1=l1;L2,a2,b2=l2
    C1=math.hypot(a1,b1);C2=math.hypot(a2,b2);Cb=(C1+C2)/2
    G=0.5*(1-math.sqrt(Cb**7/(Cb**7+25**7)))
    a1p=(1+G)*a1;a2p=(1+G)*a2;C1p=math.hypot(a1p,b1);C2p=math.hypot(a2p,b2)
    h1p=math.degrees(math.atan2(b1,a1p))%360;h2p=math.degrees(math.atan2(b2,a2p))%360
    dLp=L2-L1;dCp=C2p-C1p
    if C1p*C2p==0: dhp=0
    else:
        dhp=h2p-h1p
        if dhp>180: dhp-=360
        elif dhp<-180: dhp+=360
    dHp=2*math.sqrt(C1p*C2p)*math.sin(math.radians(dhp/2))
    Lbp=(L1+L2)/2;Cbp=(C1p+C2p)/2
    if C1p*C2p==0: hbp=h1p+h2p
    elif abs(h1p-h2p)<=180: hbp=(h1p+h2p)/2
    elif h1p+h2p<360: hbp=(h1p+h2p+360)/2
    else: hbp=(h1p+h2p-360)/2
    T=1-0.17*math.cos(math.radians(hbp-30))+0.24*math.cos(math.radians(2*hbp))+0.32*math.cos(math.radians(3*hbp+6))-0.20*math.cos(math.radians(4*hbp-63))
    dth=30*math.exp(-((hbp-275)/25)**2);RC=2*math.sqrt(Cbp**7/(Cbp**7+25**7))
    SL=1+0.015*(Lbp-50)**2/math.sqrt(20+(Lbp-50)**2);SC=1+0.045*Cbp;SH=1+0.015*Cbp*T;RT=-math.sin(math.radians(2*dth))*RC
    return math.sqrt((dLp/SL)**2+(dCp/SC)**2+(dHp/SH)**2+RT*(dCp/SC)*(dHp/SH))
def over(tone_lin, bg_lin, alpha):
    """The tone at `alpha` opacity over the page, composited in gamma-encoded sRGB."""
    t = [lin_to_gamma(c) for c in tone_lin]
    b = [lin_to_gamma(c) for c in bg_lin]
    return tuple(gamma_to_lin(alpha * x + (1 - alpha) * y) for x, y in zip(t, b))


def simulate(rgb, vision):
    matrix = VISIONS[vision]
    if matrix is None:
        return rgb
    return tuple(min(1, max(0, sum(m * c for m, c in zip(row, rgb)))) for row in matrix)


def luminance(rgb):
    return 0.2126729 * rgb[0] + 0.7151522 * rgb[1] + 0.0721750 * rgb[2]


def parse(colour):
    m = re.fullmatch(r"oklch\(([\d.]+) ([\d.]+) ([\d.]+)\)", colour)
    return tuple(float(v) for v in m.groups())


def stored(paper):
    return json.loads((ROOT / f"docs/reading_phrases/colours-{paper}.json").read_text())


class TopicColourTests(unittest.TestCase):
    def test_every_paper_has_one_colour_per_topic(self):
        for paper in PAPERS:
            topics = {t["id"] for t in json.loads((ROOT / f"docs/reading_phrases/{paper}.json").read_text())["topics"]}
            data = stored(paper)
            self.assertEqual(set(data["topics"]), topics, paper)
            self.assertLessEqual(len(data["families"]), 8, paper)
            for family in data["families"]:
                self.assertLessEqual(len(family["topics"]), 3, (paper, family["id"]))

    def test_floors_contrast_and_gamut_in_both_themes_and_every_vision(self):
        report = []
        for paper in PAPERS:
            data = stored(paper)
            for theme, page in BACKGROUND.items():
                page_rgb = hex_rgb(page)
                drawn = {}
                for tid, row in data["topics"].items():
                    rgb = oklch_to_srgb(*parse(row[theme]))
                    self.assertTrue(all(-1e-3 <= c <= 1 + 1e-3 for c in rgb), (paper, theme, tid))
                    drawn[tid] = over(tuple(min(1, max(0, c)) for c in rgb), page_rgb, ALPHA)
                    ratio = (max(luminance(drawn[tid]), luminance(page_rgb)) + 0.05) / (min(luminance(drawn[tid]), luminance(page_rgb)) + 0.05)
                    self.assertGreaterEqual(ratio, MIN_CONTRAST, (paper, theme, tid))
                family_of = {tid: row["family"] for tid, row in data["topics"].items()}
                for vision in VISIONS:
                    seen = {tid: lab(simulate(rgb, vision)) for tid, rgb in drawn.items()}
                    across, within = math.inf, math.inf
                    for a, b in itertools.combinations(seen, 2):
                        d = de2000(seen[a], seen[b])
                        if family_of[a] == family_of[b]:
                            within = min(within, d)
                        else:
                            across = min(across, d)
                    floor = FAMILY_FLOOR["normal" if vision == "normal" else "dichromat"]
                    self.assertGreaterEqual(across, floor, (paper, theme, vision))
                    self.assertGreaterEqual(within, SHADE_FLOOR, (paper, theme, vision))
                    report.append(f"{paper:15} {theme:5} {vision:12} families ΔE ≥ {across:5.1f}  shades ΔE ≥ {within:5.1f}")
        print("\n" + "\n".join(report))

    @unittest.skipUnless(shutil.which("node"), "Node is not installed")
    def test_stored_colours_are_what_the_script_computes(self):
        run = subprocess.run(["node", "site/scripts/topic-colours.ts", "--check"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr + run.stdout)


if __name__ == "__main__":
    unittest.main()
