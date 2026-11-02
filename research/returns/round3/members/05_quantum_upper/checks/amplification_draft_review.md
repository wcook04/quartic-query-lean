# Independent review of draft §5.1, returned-state example, §5.5 and 138/6072 accounting

Reviewed draft: `quantum_upper_return/section.md`, read on 2 November 2026. This is a mathematical/editorial review, not Lean execution. The amplification proof and both numerical constants are correct. The scope distinction between `Proc`, `Runs`, `Samples`, and the missing physical returned-state correspondence is justified. Before delivery, repair the following points.

## Priority 1: actual inline-math syntax is broken in the inserted prose

This affects many newly inserted passages, not the inherited proof. The generator raw strings themselves use bare parentheses, so regenerating currently preserves the defect.

Examples:

- `upper-returned-register`: `state ( |g\rangle\langle g|$` has an unmatched math delimiter; `(g)`, `(g\otimes\xi)`, `(\|\xi\|^2)` are literal prose.
- The counterexample has `pure ( |+\rangle)` and unrendered `(\{|+\rangle,|-\rangle\})`.
- `upper-padded-tournament-budget` uses bare `(c_{\mathrm{rd}})`, `(M_0=...)`, `(T\geq2)`.
- `upper-missing-physical-state` uses literal `(Pi)` and `(Pi_{\rm out})`; these should be `$\Pi$` and `$\Pi_{\rm out}$`.
- The top section interface, positivity paragraph, HMW comparison, and some later new prose share this problem.

Fix the raw generator strings deliberately to `$...$` or actual `\(...\)`; avoid a blanket regex that changes ordinary prose parentheses. Check unmatched dollar counts only as a coarse diagnostic; the specific mixed `( ... $` defect needs inspection. No mathematical rendering was assessed by this subtask.

## Priority 2: make the physical-state specification a complete scoped statement

The existing display has `ξ_x` introduced only when `p_x>0`, then uses it on the second line without carrying that scope. It also calls `B_x` a physical adaptive procedure while writing it as a linear state transformation. The following replacement removes both ambiguities and makes the heralding projector independent of the original output register.

### Suggested replacement for `upper-missing-physical-state`

The remaining formal target for the complete physical reading of Lemma 3.1 can be stated precisely. Fix a finite-dimensional original register $H$, a fixed initial basis state $|h_0\rangle$, a fixed orthogonal success projector $\Pi$, and an oracle-dependent unitary family $A_x$ represented by one circuit with at most $q$ logical reads. Put

$$
p_x=\|\Pi A_x|h_0\rangle\|^2,
\qquad g_x=\Pi A_x|h_0\rangle/\sqrt{p_x}\quad(p_x>0).
$$

For fixed $0<\gamma\leq1/2$ and $0<\eta<1/2$, the desired theorem must choose, independently of $x$, a finite auxiliary register $J$, a fixed initial basis state $|j_0\rangle$, a fixed auxiliary success projector $\Pi_J$, and a coherent circuit family $V_x$ on $H\otimes J$. The circuit includes one fixed routing controlled by the retained first-success record, and has at most $qN(2M+1)$ logical reads. With

$$
v_x=V_x(|h_0\rangle\otimes|j_0\rangle),\qquad
\Pi_{\rm out}=I_H\otimes\Pi_J,\qquad
s_x=\|\Pi_{\rm out}v_x\|^2,
$$

it must prove, for every input $x$,

$$
0\leq s_x\leq1,\qquad
p_x\geq\gamma\Longrightarrow s_x\geq1-\eta,\qquad
p_x=0\Longrightarrow s_x=0.
$$

Whenever $p_x>0$, it must additionally exhibit $\xi_x\in J$ such that

$$
\Pi_J\xi_x=\xi_x,\qquad
\|\xi_x\|^2=s_x,\qquad
\Pi_{\rm out}v_x=g_x\otimes\xi_x.
$$

Finally, compiling this same circuit $V$ must supply an ordinary bit-oracle program with all-branch query cap $2qN(2M+1)$ and the physical continuation equation on every embedded input vector. The successful-state guarantee above is required for the stated initial state; the arbitrary-vector clause concerns the compiler's realization of the same circuit, not a claim that amplification returns $g_x$ from arbitrary starting vectors.

An equivalent adaptive specification states that the designated original register is $g_x$ up to phase on every positive-mass successful history, with the same uniform cap. The ordinary fresh-trial and controlled-routing argument in §5.1 constructs such an algorithm. The packet does not supply a source-bound Lean theorem of this complete physical type. `Samples.bind` can retain a copy of a successful output label, while `Samples.runs` measures a complete basis label. An explicit output-subsystem or uncomputation correspondence is therefore still needed to promote a physical wrapper to the full state claim. Proposition 3.3 only uses the already supplied measured-label law, so this is a remaining formal correspondence obligation and not an extra premise in its ordinary proof.

## Priority 3: disambiguate the reflection sentence

In `upper-grover-trial`, “The reflections use no such calls” can be read as referring to the reflection about the prepared state, which does use $A$ and $A^{-1}$. Replace with:

> The elementary reflections $S_0$ and $S_\chi$ are input independent and contribute no additional calls to $A$ or $A^{-1}$.

The preceding count $2\ell+1$ already correctly charges the conjugated reflection about $A|0\rangle$.

## Priority 4: define the counterexample's notation explicitly

The two displayed states, their first-register marginals, and the distinguishing measurement are correct. Add immediately before them:

> Write $|\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2$.

Then use $I_2/2$ or say explicitly that $I$ is the identity on the first qubit. The example is correctly presented as a counterexample to inference from label laws, not to Lemma 3.1.

## Priority 5: tighten the HMW locator/description

The fixed-bit error hypothesis is on PDF pp.1–2 and repeated in §3 on PDF p.4. Its full finite search algorithm occurs on PDF p.7, so the bibliography phrase “§§1 and 3, pp.1–4, give ... the search construction” is too narrow. Use “§1, PDF pp.1–2, and §3, PDF pp.4–7” if discussing the whole construction. The in-body hypothesis-only citation may retain pp.1–4.

Section 5, PDF pp.8–9, is titled **Amplitude Amplification with Imperfect Verifier**. Change “discusses applications” to “discusses the imperfect-verifier generalization.” The AND–OR tree application is §4, PDF pp.7–8. Confirmed directly against the arXiv v2 PDF (https://arxiv.org/pdf/quant-ph/0304052v2), with §3 algorithm at PDF page index6 and §5 at indices7–8. Other amplification/source locators in the draft agree with the versions inspected earlier.

## Checks that pass

### Bounded amplification

The rotation matrix and state decomposition have the correct signs. The endpoint cases $p=0,1$ are correct. The exact averaging identity has denominator $4M\sin2\theta$; the proof deliberately weakens it to the paper's denominator $2M|\sin2\theta|$. The split into $\gamma\leq p\leq1/2$ and $p\geq1/2$ correctly gives trial success at least $9/40$. Repeating at most $N$ fresh trials gives failure at most $\eta$, without using the promise to justify the cap. The added positivity observation is correct because the zero-iteration half of the first trial contributes $p/2$ and $N\geq1$.

### The constant 138

The derivative is exactly $(x-1)^2/[x(x+1)^2]$. Consequently $\ln(40/31)\geq18/71>1/4$. Since $\eta<1/2$, $L=\ln(1/\eta)\geq1/2$. Hence $N\leq4L+1\leq6L$ and $2M+1\leq20/\sqrt\gamma+3\leq23/\sqrt\gamma$, giving 138. Crucially this bounds the whole padded product, as required downstream.

### The constant 6072

The padded physical list cap is

$$
B_{\rm list}=2T^2c_{\rm rd}N(2M_0+1).
$$

Applying 138 at $\gamma=1/(2m)$ and $\eta=\varepsilon$ gives

$$
B_{\rm list}\leq276c_{\rm rd}\sqrt{2m}T^2\ln(1000T).
$$

For $m\geq2$, the defined $T$ is at least 11, so certainly $T\geq2$ and $\ln(1000T)\leq11\ln T$. Using $\sqrt{2m}\leq2\sqrt m$ gives $276\cdot2\cdot11=6072$. The factor of two for logical-read compilation is present once at the start. Using a physical comparison cap as a logical-read upper bound and then this generic compiler gives a valid (possibly loose) upper bound. The prose could avoid ambiguity by consistently keeping $c_{\rm rd}$ for this numerical statement, with its subsequent conversion explanation as currently written.

### Scope

The statement that the physical label-law route suffices for Proposition 3.3 is correct. The distinction between literal tensor preparation and short-circuit state is correct. The new state factorization should remain marked as a required formal bridge; no read or build evidence of the existing `Samples` type supplies its missing output-subsystem clause.
