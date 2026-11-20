"""Topic colours: every two topics of a paper must be told apart on the page.

Each tone in site/src/paper/phrases.css is an OKLCH colour; the underline draws it at 78%
over the page. Every pair of first shades in a palette must differ by CIEDE2000 ΔE ≥ 15 in
the dark and light themes, and each must stay ΔE ≥ 15 from the colours that already mean
something: amber, red, the exact, stronger and partial match colours and mauve.
"""
import itertools
import json
import math
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CSS = ROOT / "site/src/paper/phrases.css"
BACKGROUND = {"dark": "#1c1526", "light": "#f8f0e2"}
MEANING = {"dark": ["#fab250", "#f3a43a", "#ea8470", "#55c7df", "#b49bff", "#a7b0ba", "#ca98c5"],
           "light": ["#a25200", "#c9761a", "#a04034", "#0b6f86", "#6d3fd4", "#47505b", "#8c4f86"]}
ALPHA = 0.78
MINIMUM = 15.0
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
def over(tone_lin,bg_lin,alpha):
    # color-mix with transparent: the tone at 78% opacity over the page, blended in sRGB.
    t=[lin_to_gamma(c) for c in tone_lin]; b=[lin_to_gamma(c) for c in bg_lin]
    return tuple(gamma_to_lin(alpha*x+(1-alpha)*y) for x,y in zip(t,b))


def palettes():
    """{(topic count, theme): {tone: (L, C, h)}} from the stylesheet."""
    found = {}
    rule = re.compile(r'(:root\[data-theme="light"\] )?\[data-topic-count="(\d+)"\] \[data-tone="(\d+)"\] '
                      r'\{ --tone: oklch\(([\d.]+) ([\d.]+) ([\d.]+)\); \}')
    for light, count, tone, L, C, h in rule.findall(CSS.read_text()):
        found.setdefault((int(count), "light" if light else "dark"), {})[int(tone)] = (float(L), float(C), float(h))
    return found


def drawn(colour, theme):
    return lab(over(oklch_to_srgb(*colour), hex_rgb(BACKGROUND[theme]), ALPHA))


def topic_counts():
    return {len(json.loads((ROOT / f"docs/reading_phrases/{p}.json").read_text())["topics"])
            for p in ("expert", "exposition", "reconstruction")}


class TopicColourTests(unittest.TestCase):
    def test_every_paper_has_a_palette_in_both_themes(self):
        found = palettes()
        for count in topic_counts():
            for theme in BACKGROUND:
                self.assertEqual(set(found[(count, theme)]), set(range(2 * count)), (count, theme))

    def test_topics_differ_by_at_least_fifteen(self):
        for (count, theme), tones in palettes().items():
            firsts = [drawn(tones[2 * t], theme) for t in range(count)]
            worst = min(de2000(a, b) for a, b in itertools.combinations(firsts, 2))
            self.assertGreaterEqual(worst, MINIMUM, f"{count} topics, {theme}: ΔE {worst:.1f}")

    def test_topics_keep_clear_of_meaning_colours_and_the_page(self):
        for (count, theme), tones in palettes().items():
            page = lab(hex_rgb(BACKGROUND[theme]))
            for tone, colour in tones.items():
                self.assertTrue(in_gamut(oklch_to_srgb(*colour)), (count, theme, tone))
                mark = drawn(colour, theme)
                self.assertGreaterEqual(de2000(mark, page), 30, (count, theme, tone))
                if tone % 2 == 0:
                    for meaning in MEANING[theme]:
                        self.assertGreaterEqual(de2000(mark, lab(hex_rgb(meaning))), MINIMUM, (count, theme, tone, meaning))


if __name__ == "__main__":
    unittest.main()
