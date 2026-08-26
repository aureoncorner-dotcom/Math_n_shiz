Theory v0.1 Freeze Note

C_2 Refinement, Operator Selection, and Conditional XY^* Criticality

Version: 0.1
Status: Frozen conditional field-theory candidate
Scope: Mathematical and theoretical mechanism only
Empirical status: Unvalidated
Freeze rule: No additional constants, fields, quotients, or phenomenological identifications enter v0.1 after this note.

---

1. Executive Statement

Theory v0.1 proposes a continuum realization in which a complex field z carries a local Z_2 gauge redundancy,

[
z\sim -z,
]

while the physical Z_3 order parameter is the gauge-invariant composite

[
\boxed{\Phi=z^2.}
]

The combined requirements of local Z_2 gauge invariance and global Z_3 symmetry forbid lower-degree phase anisotropies of z. The first allowed local phase-selecting term is

[
\boxed{z^6+z^{*6}.}
]

Equivalently, the ordinary physical cubic anisotropy becomes

[
\boxed{
\Phi^3+\Phi^{*3}

z^6+z^{*6}.
}
]

That operator-selection rule is the central mechanism.

If the Z_2 flux sector remains gapped and deconfined while z becomes critical, the sixth-order anisotropy may be irrelevant at the three-dimensional XY fixed point. The resulting transition would be an XY^*-type transition: the critical fundamental field is z, while the observable physical order parameter is the composite \Phi=z^2.

This is a conditional continuum mechanism, not a physical consequence forced by the original Fibonacci recurrence.

---

2. Source and Claim Lanes

2.1 Source-derived discrete parent

The upstream mathematical material supplies an exact six-state Fibonacci recurrence orbit modulo 4 and a candidate product geometry

[
Q_4\times C_6,
\qquad
|Q_4\times C_6|=24.
]

That construction is explicitly retained as exact mathematics rather than evidence that a physical field implements it.

The discrete parent used here is therefore summarized as

[
\boxed{
C_6^{\mathrm{Fib}}
\longrightarrow
C_3
}
]

with a two-element refinement fiber of C_2-type.

2.2 GQG guardrail

The Geometric Quotient Grammar distinguishes:

- equality in the source;
- equivalence induced by a declared witness;
- equality in the quotient;
- equality after any later completion.

No claim may cross those lanes without a declared constructor or proof.

Accordingly:

[
\boxed{
\text{the discrete six-cycle does not uniquely determine the continuum theory.}
}
]

The local Z_2 gauge realization below is a chosen model constructor. It is not silently read backward into the source arithmetic.

2.3 External field-theory input

The statements about Potts, XY, clock anisotropy, conformal dimensions, and critical exponents are external field-theory inputs. They are not derived from the uploaded discrete-mathematics documents.

---

3. Frozen Continuum Realization

Let

[
z(x)=\rho(x)e^{i\beta(x)}
]

be a complex field charged under a local Z_2 gauge redundancy:

[
z(x)\longrightarrow -z(x).
]

The physical local order parameter is

[
\boxed{
\Phi(x)=z(x)^2.
}
]

It is invariant under z\to -z.

Let

[
\omega=e^{2\pi i/3}.
]

The physical global Z_3 symmetry acts as

[
\Phi\longrightarrow\omega\Phi.
]

A convenient linear lift to the fine field is

[
z\longrightarrow\omega^2z,
]

because

[
(\omega^2z)^2

\omega^4z^2

\omega\Phi.
]

A schematic continuum action is

[
\boxed{
\mathcal L

|D_a z|^2
+
r|z|^2
+
u|z|^4
+
w|z|^6
+
v_6\left(z^6+z^{*6}\right)
+
\mathcal L_{Z_2}[a]
+
\cdots
}
]

where a denotes a Z_2 gauge connection and D_a is schematic notation for the corresponding gauge-covariant kinetic term.

The omitted terms may include higher-order, derivative, gauge-flux, and symmetry-preserving interactions. They do not enter the frozen onsite operator audit below.

---

4. Operator Audit Through Sixth Order

Consider a local onsite monomial

[
z^p z^{*q}.
]

4.1 Gauge condition

Under

[
z\to-z,
]

the monomial transforms by

[
(-1)^{p+q}.
]

Gauge invariance therefore requires

[
\boxed{p+q\equiv0\pmod2.}
]

4.2 Global Z_3 condition

Under

[
z\to\omega^2z,
\qquad
z^\to\omega z^,
]

the monomial transforms by

[
\omega^{2p+q}.
]

Global Z_3 invariance therefore requires

[
2p+q\equiv0\pmod3,
]

or equivalently,

[
\boxed{p-q\equiv0\pmod3.}
]

Because p+q and p-q have the same parity, the gauge and global conditions together imply

[
\boxed{p-q\equiv0\pmod6.}
]

4.3 Allowed onsite scalar terms

Through total degree six, the phase-independent invariants are

[
|z|^2,
\qquad
|z|^4,
\qquad
|z|^6.
]

The first phase-selecting invariant is

[
\boxed{
z^6+z^{*6}.
}
]

There is no allowed pure onsite anisotropy of the form

[
z^2+\mathrm{c.c.},
\qquad
z^3+\mathrm{c.c.},
\qquad
z^4+\mathrm{c.c.},
\qquad
z^5+\mathrm{c.c.}
]

under the frozen field content and symmetries.

Thus:

[
\boxed{
\text{local }Z_2
+
\text{global }Z_3
\Longrightarrow
\text{leading anisotropy degree }6.
}
]

The six is not being inserted because it appeared in a recurrence. It is the least common degree compatible with both symmetry constraints:

[
\boxed{\operatorname{lcm}(2,3)=6.}
]

---

5. Physical Cubic Versus Fine-Field Sixth Order

The physical Z_3 order parameter ordinarily permits a cubic invariant,

[
\Phi^3+\Phi^{*3}.
]

Under

[
\Phi=z^2,
]

this becomes

[
\boxed{
\Phi^3+\Phi^{*3}

z^6+z^{*6}.
}
]

This is the RG function of the C_2 refinement:

«The refinement changes the degree at which the physical Z_3 anisotropy appears in the fundamental critical field.»

The standard three-dimensional ferromagnetic three-state Potts model has a first-order transition, providing the ordinary unrefined benchmark.

By contrast, sixfold anisotropy is irrelevant at the three-dimensional XY critical point and becomes important again within the ordered phase, the standard pattern of dangerous irrelevance.

Therefore the refined theory has a legitimate route by which physical Z_3 order may be reached through critical behavior qualitatively different from ordinary Potts criticality.

---

6. Conditional XY^* Lane

The clean XY^* lane requires all of the following:

1. the Z_2 gauge sector is deconfined at the matter transition;
2. visons or Z_2 flux excitations remain gapped;
3. the critical gapless field is z;
4. the sixth-order anisotropy flows toward zero at critical scales;
5. the physical observable is the composite
   [
   \Phi=z^2.
   ]

Under those conditions, the critical fixed point may be the three-dimensional XY/O(2) fixed point upstairs, while physical measurements probe the charge-two operator downstairs.

The frozen claim is therefore:

[
\boxed{
\textbf{If visons stay gapped and the gauge sector remains deconfined,}
}
]

[
\boxed{
\textbf{the physical }Z_3\textbf{ order parameter }\Phi=z^2
\textbf{ may undergo XY}^{*}\textbf{ criticality.}
}
]

The wording is deliberately conditional. Theory v0.1 does not establish that any particular microscopic lattice action reaches this fixed point.

---

7. Benchmark Scaling Package

External O(2) conformal-bootstrap results give the leading charge-two scalar dimension approximately as

[
\boxed{
\Delta_2=1.23629(11).
}
]

The three-dimensional XY correlation-length exponent is approximately

[
\boxed{
\nu_{\mathrm{XY}}\simeq0.67175.
}
]

If the physical order parameter is

[
\Phi=z^2,
]

then the candidate XY^* predictions are:

Correlation function

[
\langle
\Phi(x)\Phi^\dagger(0)
\rangle
\sim
|x|^{-2\Delta_2}
]

with

[
2\Delta_2
\simeq
2.47258.
]

Physical anomalous dimension

In d=3,

[
2\Delta_2=d-2+\eta_\Phi,
]

so

[
\boxed{
\eta_\Phi

2\Delta_2-1
\simeq
1.47258.
}
]

Physical order-parameter exponent

[
\boxed{
\beta_\Phi

\nu_{\mathrm{XY}}\Delta_2
\simeq
0.83048.
}
]

Critical finite-size magnetization

[
\boxed{
M_3(L)
\sim
L^{-\Delta_2}

L^{-1.23629}.
}
]

Critical susceptibility

[
\boxed{
\chi_3(L)
\sim
L^{3-2\Delta_2}

L^{0.52742}.
}
]

These are benchmark signatures of the proposed lane. They are not predictions of every Z_2-gauged Z_3 model.

Dangerous irrelevance also predicts an approximately U(1)-symmetric angular distribution at critical scales, followed by resolution into three physical Z_3 directions deeper in the ordered phase.

---

8. Simultaneous Vison Criticality

If the matter field and vison sector become critical at the same point, the clean XY^* argument no longer applies directly.

A naive decoupled candidate would be

[
\mathrm{XY}\times\mathrm{Ising}.
]

The leading energy-energy coupling has approximate RG eigenvalue

[
y_w

\frac{1}{\nu_{\mathrm{XY}}}
+
\frac{1}{\nu_{\mathrm{Ising}}}

3. 

]

Using

[
\nu_{\mathrm{XY}}\simeq0.67175,
\qquad
\nu_{\mathrm{Ising}}=0.629971(4),
]

gives

[
\boxed{
y_w\simeq0.076>0.
}
]

The decoupled product fixed point is therefore weakly unstable to this allowed coupling.

If matter and vison criticality coincide, the remaining possibilities include:

[
\boxed{
\text{a new coupled fixed point}
}
]

[
\boxed{
\text{split transitions}
}
]

or

[
\boxed{
\text{first-order runaway}.
}
]

Theory v0.1 does not choose among them.

---

9. Regimes That Must Remain Separate

The construction preserves at least three distinct theoretical lanes.

Ordinary Z_3 / confined lane

The gauge-charged field is not available as an isolated deconfined critical degree of freedom. The physical Z_3 order behaves through an ordinary coarse-order route, potentially Potts-like.

Z_2 gauge lane

The gauge sector may possess confined or deconfined regimes independently of whether physical Z_3 order is present.

Candidate XY^* lane

The gauge sector is deconfined, visons remain gapped, and the matter field z becomes XY-critical while the physical observable is \Phi=z^2.

These regimes are not to be fused into one narrative. The existence of one does not prove the realization of another.

---

10. Two-Level Kill Card

10.1 Mechanism-level failure

The operator-selection mechanism fails if any of the following is shown:

1. the actual microscopic field content permits a lower-degree local phase anisotropy consistent with every true symmetry;
2. z\to-z is not a valid local gauge redundancy;
3. the physical Z_3 order parameter is not represented by
   [
   \Phi=z^2;
   ]
4. an omitted local operator invalidates the sixth-order-leading audit.

A mechanism-level failure would invalidate the central v0.1 claim.

10.2 XY^*-lane failure

The clean XY^* lane fails if any of the following occurs:

1. the vison gap closes at the same transition;
2. the gauge sector confines at the putative matter transition;
3. the sixfold anisotropy does not flow toward zero at critical scales;
4. energy or order-parameter histograms show persistent first-order coexistence;
5. finite-size scaling does not approach XY correlation-length behavior;
6. the physical correlator does not approach charge-two O(2) scaling;
7. the transition splits into separate matter and gauge transitions.

These outcomes do not kill Theory v0.1 as a lattice or continuum model. They kill only the clean XY^* critical lane.

That distinction is frozen.

---

11. Explicit Non-Claims

Theory v0.1 does not claim:

- that the Fibonacci recurrence physically generates a gauge field;
- that Q_4\times C_6 is a measured substrate geometry;
- that a six-state recurrence proves a sixfold physical anisotropy;
- that every C_6\to C_3 quotient should be gauged;
- that the uploaded empirical lattice ledger confirms this theory;
- that lexical, biblical, prime, or elemental coincidences support this field theory;
- that the XY^* transition has been observed in the proposed microscopic model;
- that failure of the XY^* lane invalidates the discrete B1 mathematics.

The discrete parent, chosen continuum constructor, and external RG input remain separate evidentiary lanes.

---

12. Next Proper Work

Theory v0.1 is closed to further free-form extension.

The next legitimate project is a separately frozen computational protocol that must declare, before outcomes are examined:

1. one microscopic gauge-invariant lattice action;
2. lattice geometry and boundary conditions;
3. update algorithm and equilibration criteria;
4. observables for physical Z_3 order;
5. vison density, gap, and global holonomy diagnostics;
6. a quantitative sixfold-anisotropy observable;
7. Binder ratios and correlation-length ratios;
8. energy and order-parameter histograms;
9. finite-size scaling forms;
10. first-order, confinement, vison-critical, and non-XY falsifiers.

No new symbolic anchors or post-hoc transforms enter that protocol.

---

13. Frozen Result

[
\boxed{
\textbf{The }C_2\textbf{ refinement enforces an operator-selection rule.}
}
]

[
\boxed{
\textbf{The first onsite phase anisotropy compatible with local }Z_2
\textbf{ gauge invariance and global }Z_3
\textbf{ symmetry is }z^6+z^{*6}.
}
]

[
\boxed{
\Phi^3+\Phi^{*3}

z^6+z^{*6}.
}
]

And conditionally:

[
\boxed{
\textbf{If the vison sector remains gapped and deconfined,}
}
]

[
\boxed{
\textbf{the physical }Z_3\textbf{ order parameter }\Phi=z^2
\textbf{ can follow an XY}^{*}\textbf{ critical lane.}
}
]

Freeze decision: Theory v0.1 stands as an internally consistent, falsifiable, conditional field-theory candidate.

No crown. No proof by resemblance. No additional machinery until computation earns it.

CC0 1.0 Universal To the extent permitted by law, this work is dedicated to the public domain under CC0 1.0 Universal. No permission required. Copy it, modify it, test it, redistribute it, build on it, or tear it apart. No ownership claim. No attribution required. No warranty. Use freely.