// Where the four comes from. The edition supplies the exact leading powers
// for a few fixed k; logarithmic factors are always named beside them.
import { useState } from "react";

interface Example { k: number; quantum_power_in_m: string; classical_power_in_m: string; classical_power_in_sqrt_m: string }

const frac = (s: string) => { const [a, b = "1"] = s.split("/"); return Number(a) / Number(b); };

export function Exponent({ examples, parameters }: { examples: Example[]; parameters: string }) {
  const [i, setI] = useState(Math.min(2, examples.length - 1));
  const e = examples[i];
  const power = frac(e.classical_power_in_sqrt_m);
  return (
    <figure className="exponent" aria-labelledby="exp-h">
      <h2 id="exp-h">Why the exponent approaches four</h2>
      <p>
        Each board family has a fixed number <em>k</em> of blocks. Its quantum cost is about <em>m</em><sup>1/2</sup> and its
        randomized cost about <em>m</em><sup>2−1/<em>k</em></sup>, both up to powers of log <em>m</em>. Measured in powers of the
        quantum cost, the randomized cost is the (4 − 2/<em>k</em>)th power.
      </p>
      <div className="exponent__control">
        <label htmlFor="k-pick">Fix <em>k</em></label>
        <div className="exponent__ks" role="radiogroup" id="k-pick" aria-label="Number of blocks k">
          {examples.map((x, j) => (
            <button key={x.k} type="button" role="radio" aria-checked={i === j} className="kbtn" onClick={() => setI(j)}>{x.k}</button>
          ))}
        </div>
      </div>
      <p className="exponent__caption" id="exp-scale">Randomized cost, as a power of the quantum cost</p>
      <div className="exponent__scale" role="img" aria-labelledby="exp-scale" aria-describedby="exp-read">
        <div className="exponent__bar" style={{ width: `${(power / 4) * 100}%` }} />
        {[1, 2, 3].map((n) => <span key={n} className="exponent__tick" style={{ left: `${(n / 4) * 100}%` }}>{n}</span>)}
        <span className="exponent__tick exponent__tick--limit" style={{ left: "100%" }}>4, the limit</span>
      </div>
      <p className="exponent__read" id="exp-read" aria-live="polite">
        With <em>k</em> = {e.k}: quantum ≈ <em>m</em><sup>{e.quantum_power_in_m}</sup>, randomized ≈ <em>m</em><sup>{e.classical_power_in_m}</sup> = (<em>m</em><sup>1/2</sup>)<sup>{e.classical_power_in_sqrt_m}</sup>, ignoring logarithmic factors.
      </p>
      <p className="quiet">{parameters} No single family reaches four, but every exponent below four fails on the family for some fixed <em>k</em>.</p>
    </figure>
  );
}
