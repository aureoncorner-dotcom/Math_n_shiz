# Defect calculus applied to toroidal sectors
## Working increment v0.1 — 11 September 2026
CC0 • Anonymous

Status: formal application of Typed Defects v0.2 to objects already declared in TOROIDAL Working Master / Geometry Master §§7–9.
Does not alter: TD-COS-FH-001 all-orders theorem, L=3 PASS, original-pilot UNRESOLVED, physical Q2 NOT_RUN, chemistry freeze, Hidden Quotient v1.7, 39-screen algebra.


## 0 Declared objects (do not mix)

Fix cubic \(L\ge 2\), the ideal cosine kernel TD-COS-FH-001 at \(J=1\), \(t=1/2\), \(h_6=0\), fixed-reference \(Z_{000}\), unbounded integer currents.

| Name | Object |
|---|---|
| Source domain \(D\) | Constraint-satisfying states \(X=(I,M,q)\) on the \(L^3\) lattice: \(\operatorname{div}I=0\), membrane constraint |
| Kernel \(K\) | Attempted-microtick mixture of Geometry Master §8; identities and rejections both advance the clock |
| Spacing \(d\in\mathbb Z_{>0}\) | Attempted-microtick stride; \(R=K^d\) |
| Sector map \(\pi_q\) | \(\pi_q(X)=q\in(\mathbb Z/2)^3\) |
| Signed winding \(W\) | \(W_\alpha=F_\alpha(k)\), integer, cut-independent on this divergence-free domain |
| Membrane \(M\) | Mod-two 2-chain |
| Full state | \(X\) itself; \(K\) is Markov on \(D\) |
| Sector process | \(Y_n=\pi_q(X_{dn})\) |
| History-\(m\) record | \(r_m=(Y_0,\ldots,Y_{m-1})\) |
| Belief state | \(\nu_n(\,\cdot\mid Y_0,\ldots,Y_n)\), the causal posterior on \(D\) |

The L=3 rotor/gauge follow-up is a **different kernel** (angle proposals then link flips; accepted-sweep clock). Lemma D4 applies: a result on that domain is not a result on TD-COS-FH-001.


## 1 Static loci

### 1.1 Sector from winding (coarsening)

On this source-free divergence-free domain, \(q\) is the parity of the integer cut class. Write

\[
\pi_q \;=\; \operatorname{parity}\circ W.
\]

**Lemma T1 (D2).** \(N_{\pi_q}(\pi_W)=\varnothing\).

Parity is a function of signed winding. The coarser label always descends through the finer one.

**Lemma T2 (D2 converse fails).** \(N_W(\pi_q)=(\mathbb Z/2)^3\) on this domain, for the natural range of \(W\).

Each sector fiber contains currents of every compatible even (or odd) winding of arbitrarily large \(|W|\). Distinct signed windings share a sector. Recovering load-like \(W\) from sector \(q\) fails everywhere. This is Kind I: the relation (parity / sector) survives; the specified output (signed winding) does not.

Do not identify \(q\) with \(W\). Geometry Master already forbids replacing signed \(W\) by a volume average or by parity when sources are present. Here sources are zero and the identification still fails in the reverse direction.

### 1.2 Product of static witnesses (D1)

\[
N_{(q,W)}(\pi_q)=N_q(\pi_q)\cup N_W(\pi_q)=N_W(\pi_q),
\]

since \(N_q(\pi_q)=\varnothing\) tautologically. Retaining only \(q\) loses \(W\). Retaining \((q,W)\) kills the static Kind I defect for \(W\), and creates a different predictive question. The all-orders theorem is **not** a theorem about \((q,W)\). Geometry Master §8 states this limit explicitly. Defect calculus repeats it as D1: cleaning the sector witness does not clean the winding witness, and adding winding changes the predictive locus.

### 1.3 Membrane

\(M\) is independent discrete data subject to the constraint. \(N_M(\pi_q)\) is nonempty: many membranes sit over one sector. Kind IV (discrete extra sheet), not Kind I. Legal repair: retain \(M\), or retain a declared functional of \(M\). Illegal repair: treat sector frequencies as membrane frequencies. Dual-sector probabilities and direct holonomy counts are different observables (L=3 record already separates them).

### 1.4 Sourced restriction (D4)

With charge-six sources, integer winding is unavailable and cuts agree only modulo six. Restricting \(D\) to sourced states **removes** the integer-\(W\) witness rather than repairing it. That is domain change, not descent. The modular class is a different witness. Kind III only if a stated subgroup of states is shown to inject into a stated target; do not call modular reduction “GHS” or a speedup.


## 2 Predictive loci (the actual theorem)

The kernel is stochastic. Use the Working Master form of D5: autonomous retained dynamics iff equal retained labels imply equal next-observation laws for every measurable target.

### 2.1 Full state

**Lemma T3.** \(N_{\mathrm{Law}(X_1\mid X_0)}(\mathrm{id}_D)=\varnothing\).

\(K\) is Markov on \(D\). The full state is a clean predictive record. This is not new; it is the standing fact that the all-orders result is about a **quotient**, not about \(X\).

### 2.2 One-step sector

Let \(W^\rightarrow_q(X)=\mathrm{Law}(\pi_q(X_1)\mid X_0=X)\), a probability on the eight sectors.

**Lemma T4.** \(N_{W^\rightarrow_q}(\pi_q)\ne\varnothing\).

Different currents in one sector produce different next-sector laws. The proof engine of TD-COS-FH-001 is a quantitative form of this: states with current \(2N\) on every positive edge change the return law through a Bessel-tail term as \(N\to\infty\), so one sector label does not determine the next-sector kernel. Kind I again, now with witness = next-sector law rather than signed winding.

### 2.3 Finite sector history

Let \(r_m\) be the length-\(m\) sector string, \(m<\infty\). Let \(W^\rightarrow_{q,m}\) be the law of the next sector given the last \(m\) sectors and the hidden current/membrane.

**Lemma T5.** For every fixed \(L\ge 2\) and every fixed attempted-microtick spacing \(d\ge 1\), and every finite \(m\),

\[
N_{W^\rightarrow_{q,m}}(r_m)\ne\varnothing.
\]

This is the all-orders theorem, restated as “the predictive non-descent locus of every finite sector history is nonempty.” Finite Markov order would be \(N_{W^\rightarrow_{q,m}}(r_m)=\varnothing\) for some \(m\). The theorem says that set is never empty.

Classification: **predictive Kind I**, with optional Kind IV on the discrete eight-point base. It is not Kind V. The missing information (current, membrane) lies **inside** the \(\pi_q\)-fibers as extra source coordinates, not outside \(\operatorname{im}\pi_q\). Sector labels are attained. The fiber is heterogeneous for the future-sector law.

### 2.4 Canonical predictive refinement

The causal posterior \(\nu_n\) is \(\pi_W\) for the predictive witness “future sector path.” By Theorem 14.3 / D5, \(N\) of that refinement is empty: \(\nu_n\) is a sufficient belief state. Geometry Master already says its representation may be unbounded. That is an approximation problem, not a descent problem.

Do not feed future sectors into \(\nu_n\). The filter is a function of the observed past and the kernel.

### 2.5 Horizon diameters

\(\delta_h^q(z)\) on a sector-history fiber is nondecreasing in \(h\). The all-orders argument is stronger than one-step: it produces a defect that survives every finite memory. A single tested pair of currents in one sector would only lower-bound \(\delta_1\). The Bessel-tail family is a sequence of pairs that keeps the defect alive as \(N\) grows, which is why the order cannot stabilize.

### 2.6 What the theorem does not say (D4 / D3)

| Change | Calculus | Status |
|---|---|---|
| Finite-current truncation | D4, smaller \(D\) | Not covered. Locus may shrink. UNRESOLVED for that \(D\) |
| Accepted-move clock | different \(\pi\) / different \(K\) | Not covered |
| Adaptive schedule | different \(K\) | Not covered |
| Record \((q,W)\) | D1, different witness | Not covered |
| L=3 rotor/gauge sweep | different \(K\), D4 | Separate PASS; not this locus |
| Belief-state finite compression | approximation of a clean record | Not \(N\); needs \(B,h,\varepsilon\) |
| Physical Q2 | different ensemble, estimator, claim | NOT_RUN |


## 3 Kind table for this kernel

| Kind | Toroidal instance | Legal repair | Illegal repair |
|---|---|---|---|
| I Operation / output loss | \(q=\mathrm{parity}(W)\) loses \(W\); \(q\)-history loses next-\(q\) law | Retain \(W\), or retain \(\nu_n\), or retain declared current functionals | Treat sector string as winding; treat finite Markov table as the kernel |
| II Unit / character | No native unit group here. Character transform \(\mathcal Z_q\leftrightarrow Z_h\) is an ensemble change, not a local log | Keep \(Z_h\) and \(\mathcal Z_q\) as separate witnesses | Call a dual coefficient a Schirokauer map |
| III Subgroup | Source-free \(D\) vs sourced \(D\); integer \(W\) only on \(\operatorname{div}I=0\) | Restrict and rename the witness (modular class) | Infer sourced winding from source-free formulas |
| IV Discrete sector | Eight-point base; membrane sheets over one \(q\); holonomy 8-bin counts | Retain sheet / membrane / holonomy label as its own witness | Treat \(H_h\) counts as \(\hat p(q)\) |
| V Representability | Finite-current or finite-history encodings that miss functionals of unbounded \(I\) | Name the omitted functional; enlarge observation | Call “no finite Markov order” a missing dual. It is a fiber collision |

Kind II is listed to forbid a false identification with the NFS packet, not because a unit character is required on this kernel.


## 4 Transport, holonomy, shape

\(Q=(\mathbb Z/2)^3\) is a discrete eight-point set. Under the standing topology of \(Q\), \(N_{W^\rightarrow_q}(\pi_q)\) is a subset of eight points. Openness, \(\partial N\), and continuous holonomy **do not apply** to this \(Q\) (no-shape + missing hypotheses of Thm 14.5).

Witness-holonomy in the sense of Prop. 14.8 would require a declared connection on the fibers \(F_q=\{X:\pi_q(X)=q\}\) and loops in a **continuous** base. The discrete sector walk is not that object. Direct holonomy \(h\in(\mathbb Z/2)^3\) in the L=3 record is a **different witness** on a different kernel. Nonzero \(\mathfrak h_W\) would imply non-descent if those hypotheses were met; the converse remains false.

To speak of \(\partial N_{W,\varepsilon}\) one must enlarge the base to a parameter space (e.g. \((J,t,L)\)) on which \(\delta\) is defined and continuous. That enlargement has not been declared. Do not draw a boundary on the eight-point cube and call it lithium.

Ensemble note, D1 again: \(Z_h\) and \(\mathcal Z_q\) are different witnesses related by a character transform. \(Z_{\mathrm{full}}=\mathcal Z_{000}\) while \(Z_{000}=\frac18\sum_q\mathcal Z_q\). Full periodic summation forcing even-parity projection is an algebraic projection, not observed confinement, and not \(N_{\pi_q}\).


## 5 Clock

Attempted-microtick time is part of \(K\). Switching to accepted-move time is a different record. If fixed-time sector laws agreed and cross-time laws did not, a clock coordinate would be the Working Master repair. The all-orders theorem already fails **inside** one clock (attempted microticks). Adding a clock cannot repair a same-time fiber collision (Working Master §3). The defect is not a missing clock.


## 6 Empirical gate for this application

Frozen tuple for any numerical sector run that wants a defect-calculus readout:

- \(D\): named kernel, \(L\), current bound or “unbounded,” source convention
- \(\pi\): \(q\), or \(r_m\), or \((q,W)\), named
- \(W\): next-sector law, or signed \(W\), or dual \(\hat p(q)\), named
- \(d_Y\): total variation on sector measures, or integer distance on \(W\)
- \(\varepsilon\), coverage, same-fiber rule
- Defect kind: I (predictive) for the all-orders claim; I (static) for winding-from-sector; IV for membrane/holonomy mixups

Certified predictive non-descent on a **truncated** current box is only a lower bound on that box (D4). It does not replay the Bessel-tail argument and does not inherit the all-orders label.

L=3 PASS remains a separate engineering screen on holonomy counts and dual-reference probabilities. It is not a measurement of \(N_{W^\rightarrow_q}(\pi_q)\) for TD-COS-FH-001.


## 7 Disposition

The sector theorem is the statement that every finite sector history has nonempty predictive non-descent locus for next-sector law, under the declared kernel and attempted-microtick clock.

\[
\boxed{\text{SECTOR THEOREM = PREDICTIVE }N\ne\varnothing\text{ FOR EVERY FINITE }r_m}
\]
\[
\boxed{\text{STATIC }N_W(\pi_q)\text{ NONEMPTY; }N_q(\pi_W)\text{ EMPTY}}
\]
\[
\boxed{\text{BELIEF STATE }=\text{ CANONICAL PREDICTIVE REFINEMENT; COMPRESSION SEPARATE}}
\]
\[
\boxed{\text{ALL SOURCE STATUSES UNCHANGED}}
\]

Point TOROIDAL Working Master at this increment for the typing. Do not paste the typing into the all-orders proof. The proof stays the proof.
