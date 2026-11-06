// A plain title as the edition writes it: `$…$` is TeX, typeset with KaTeX;
// backtick spans are formulas written in Unicode, set in the maths italic.
import { renderTex } from "./math";

export function titleHtml(text: string): string {
  const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  let out = "";
  let last = 0;
  const re = /\$([^$]+)\$|`([^`]+)`/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(text))) {
    out += esc(text.slice(last, m.index));
    out += m[1] != null ? renderTex(m[1], false).html : `<span class="umath">${esc(m[2])}</span>`;
    last = m.index + m[0].length;
  }
  return out + esc(text.slice(last));
}

export function Title({ text }: { text: string }) {
  return <span dangerouslySetInnerHTML={{ __html: titleHtml(text) }} />;
}

/** The words of a title without markup, for measuring and for screen readers. */
export const plainTitle = (text: string) => text.replace(/\$([^$]+)\$/g, "$1").replace(/`/g, "");
