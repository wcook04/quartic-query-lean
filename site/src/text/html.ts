// The edition ships each manuscript as Pandoc HTML with TeX math spans.
// Sanitise it again on arrival, then typeset math in place with KaTeX.
import createDOMPurify from "dompurify";
import { renderTex } from "./math";

let purify: ReturnType<typeof createDOMPurify> | null = null;

function purifier() {
  if (purify) return purify;
  const p = createDOMPurify(window);
  p.addHook("uponSanitizeAttribute", (node, data) => {
    const tag = node.nodeName.toLowerCase();
    if (data.attrName === "href") data.keepAttr = tag === "a" && /^(#|https?:\/\/|mailto:)/i.test(data.attrValue.trim());
    if (data.attrName === "src") data.keepAttr = false; // figures arrive as verified blobs
  });
  p.addHook("afterSanitizeAttributes", (node) => {
    if (node.nodeName === "A" && /^https?:/.test(node.getAttribute("href") ?? "") && !node.hasAttribute("data-paper")) {
      node.setAttribute("target", "_blank");
      node.setAttribute("rel", "noopener noreferrer");
    }
  });
  purify = p;
  return p;
}

export function sanitizeManuscript(html: string): string {
  return purifier().sanitize(html, {
    ADD_ATTR: ["role", "data-l0", "data-l1", "data-paper", "data-fragment", "data-resource", "data-cites"],
    FORBID_TAGS: ["style", "script", "iframe", "object", "form", "input"],
    ALLOW_DATA_ATTR: true, RETURN_TRUSTED_TYPE: false,
  }) as string;
}

/** Typeset every Pandoc math span under `root`. */
export function typeset(root: HTMLElement) {
  for (const el of root.querySelectorAll<HTMLElement>("span.math")) {
    if (el.dataset.typeset) continue;
    const display = el.classList.contains("display");
    const tex = (el.textContent ?? "").replace(/^\\[([]/, "").replace(/\\[)\]]$/, "");
    el.innerHTML = renderTex(tex, display).html;
    el.dataset.typeset = "1";
    if (!display && tex.length <= 40) gluePunctuation(el);
  }
}

/** Keep punctuation that follows inline math on the math's line, so no line starts with a lone comma. */
function gluePunctuation(el: HTMLElement) {
  const next = el.nextSibling;
  if (!next || next.nodeType !== Node.TEXT_NODE) return;
  const m = /^[,.;:!?)\]’”]+/.exec(next.textContent ?? "");
  if (!m) return;
  const glue = document.createElement("span");
  glue.className = "math-glue";
  el.replaceWith(glue);
  glue.append(el, document.createTextNode(m[0]));
  next.textContent = next.textContent!.slice(m[0].length);
}

/**
 * Display equations a little wider than the column (up to a fifth) are set slightly smaller
 * so their numbers stay in view; wider ones keep their size and scroll sideways.
 */
export function fitDisplayMath(root: HTMLElement) {
  const shown = [...root.querySelectorAll<HTMLElement>(".katex-display")].filter((d) => d.offsetParent);
  for (const d of shown) d.style.fontSize = "";
  const ratios = shown.map((d) => d.clientWidth / d.scrollWidth);
  shown.forEach((d, i) => {
    const r = ratios[i];
    if (r < 1 && r >= 0.8) d.style.fontSize = `${Math.floor(r * 1000) / 10}%`;
  });
}

/** Typeset a short TeX-bearing string such as an authored note. */
export function inlineTex(text: string): string {
  const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  let out = "";
  let last = 0;
  const re = /\$\$([^$]+)\$\$|\$([^$\n]+)\$/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(text))) {
    out += esc(text.slice(last, m.index)) + renderTex(m[1] ?? m[2], !!m[1]).html;
    last = m.index + m[0].length;
  }
  return out + esc(text.slice(last));
}
