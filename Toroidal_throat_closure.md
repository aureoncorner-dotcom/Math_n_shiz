Toroidal Throat and Strain Closure Comparator — TTSC-1

Version: 0.1
Status: Structural draft; non-verdict-bearing Stage D comparator
Parent protocol: Simulation Protocol v0.3-RC1, three-axis fixed-holonomy Appendix A
Execution order: Runs only after the canonical Q2 validation gate passes
Theory boundary: Does not modify frozen Theory v0.1


---

1. Purpose

TTSC-1 tests whether a divergence-free current circuit winding around a periodic finite-volume lattice can display the local sequence

\[
\boxed{
\text{transverse convergence}
\longrightarrow
\text{maximum-throughflow throat}
\longrightarrow
\text{transverse divergence}
}
\]

without introducing a source, sink, mathematical singularity, or reversal of the intrinsic current orientation.

The hypothesis concerns local current geometry inside an already-established winding circuit. It does not replace the canonical Q2 observable.


---

2. Canonical topology remains unchanged

The canonical finite-volume geometry is

\[
\Lambda_L=(\mathbb Z/L\mathbb Z)^3,
\]

with global holonomy

\[
h=(h_x,h_y,h_z)\in\mathbb Z_2^3
\]

and current homology

\[
q=(q_x,q_y,q_z)\in\mathbb Z_2^3.
\]

The primary Q2 ensemble remains

\[
\boxed{Z_{\mathrm{FH}}=Z_{000}}.
\]

The exact character transform remains

\[
Z_h=\frac18
\sum_{q\in\mathbb Z_2^3}
(-1)^{h\cdot q}\mathcal Z_q,
\]

and the canonical odd-winding statistic remains

\[
\boxed{
f_{\mathrm{odd}}^{(\alpha)}
=
\frac12
\left(
1-\frac{Z_{e_\alpha}}{Z_{000}}
\right).
}
\]

TTSC-1 neither changes these definitions nor contributes directly to the Q2 verdict.


---

3. Continuum throat construction

Let \(s\) denote distance along a locally defined tube and \(r\) the transverse distance from its centerline.

For a locally straight, axisymmetric tube, define

\[
\boxed{
v_s=U(s),
\qquad
v_r=-\frac r2\frac{dU}{ds}.
}
\]

In cylindrical coordinates,

\[
\nabla\cdot\mathbf v
=
\frac{\partial v_s}{\partial s}
+
\frac1r\frac{\partial(rv_r)}{\partial r}
=
U'(s)-U'(s)=0.
\]

Therefore, the field is divergence-free.

For an embedded curved toroidal tube, this is the local leading-order form. The exact conservation equation is

\[
\boxed{
\nabla_i v^i
=
\frac1{\sqrt g}
\partial_i\!\left(\sqrt g\,v^i\right)=0,
}
\]

where \(g\) is the determinant of the local metric. Curvature corrections must be retained if the tube radius is not small relative to the toroidal curvature radius.


---

4. Frozen periodic throat profile

The comparator uses the preregistered positive periodic profile

\[
\boxed{
U_\epsilon(s)
=
U_0
\left[
1+\epsilon
\cos\left(\frac{2\pi(s-s_0)}L\right)
\right],
\qquad
0<\epsilon<1.
}
\]

Here:

\(s_0\) is the frozen throat location;

\(U_0>0\) is the mean longitudinal speed;

\(\epsilon\) is the frozen modulation strength;

\(U_\epsilon(s)>0\) everywhere.


At \(s=s_0\),

\[
U'(s_0)=0,
\qquad
U(s_0)=U_0(1+\epsilon),
\]

so the throat carries maximal longitudinal flow while transverse flow vanishes:

\[
\boxed{v_r(s_0)=0.}
\]

Immediately before the throat,

\[
U'(s)>0
\quad\Longrightarrow\quad
v_r<0,
\]

giving transverse convergence.

Immediately afterward,

\[
U'(s)<0
\quad\Longrightarrow\quad
v_r>0,
\]

giving transverse divergence.

Thus,

\[
\boxed{
v_r<0
\longrightarrow
v_r=0
\longrightarrow
v_r>0.
}
\]

The longitudinal current does not reverse.


---

5. Stream-tube closure

For constant-density incompressible through-flow, the tube cross-sectional area must satisfy

\[
A(s)U_\epsilon(s)=Q,
\]

where \(Q\) is the conserved volume flux.

For a circular cross-section,

\[
A(s)=\pi R(s)^2.
\]

A compatible frozen radius profile is therefore

\[
\boxed{
R(s)
=
R_0
\sqrt{\frac{U_0}{U_\epsilon(s)}}.
}
\]

Consequently,

\[
\boxed{
\pi R(s)^2U_\epsilon(s)
=
\pi R_0^2U_0.
}
\]

The throat is the minimum-area, maximum-throughflow surface. No field value diverges and no singular matching rule is needed.


---

6. Periodic compensation

Because

\[
U(s+L)=U(s),
\]

convergence and divergence must compensate over the complete circuit.

Near a maximum of \(U\),

\[
\text{convergence}
\rightarrow
\text{throat}
\rightarrow
\text{divergence}.
\]

Near a minimum,

\[
\text{divergence}
\rightarrow
\text{wide region}
\rightarrow
\text{convergence}.
\]

The complete toroidal circuit therefore has the periodic structure

\[
\boxed{
\text{compression}
\rightarrow
\text{expansion}
\rightarrow
\text{compression}
\rightarrow\cdots
}
\]

rather than a one-way funnel.


---

7. Diamond-grid interpretation

The diamond grid is treated as a visualization or local routing chart on the existing periodic lattice.

Define diagonal directions

\[
e_+=(1,1),
\qquad
e_-=(1,-1).
\]

After opposite boundaries are identified, diagonal paths can become closed or helical winding circuits.

At every routing vertex,

\[
\boxed{
\sum_{\ell\ni v}s_{v\ell}I_\ell=0.
}
\]

Current may approach along one set of links, turn through the vertex and depart along another set without violating conservation.

The intrinsic current need not reverse. Only its projected transverse component changes sign.

If “diamond lattice” instead means a physical diamond-crystal adjacency graph, that constitutes a new microscopic model and requires new kernels, dual cells, enumeration checks and validation. TTSC-1 does not make that architecture change.


---

8. Discrete tube observables

Let \(\Sigma_s\) be a frozen transverse cross-section of the comparator tube.

Define the oriented longitudinal current through the section:

\[
Q_\parallel(s)
=
\sum_{\ell\pitchfork\Sigma_s}
\sigma_\ell I_\ell.
\]

Let \(F_\perp(s)\) denote the outward-oriented current through the side boundary of the segment between \(\Sigma_s\) and \(\Sigma_{s+\Delta s}\).

Discrete conservation requires

\[
\boxed{
Q_\parallel(s+\Delta s)
-
Q_\parallel(s)
+
F_\perp(s)=0.
}
\]

This is the lattice counterpart of the continuum divergence equation.

Before the throat,

\[
Q_\parallel(s+\Delta s)>Q_\parallel(s)
\]

requires

\[
F_\perp(s)<0,
\]

representing transverse inflow.

After the throat,

\[
Q_\parallel(s+\Delta s)<Q_\parallel(s)
\]

requires

\[
F_\perp(s)>0,
\]

representing transverse outflow.

Periodic closure requires

\[
\boxed{
\sum_{s=0}^{L-1}F_\perp(s)=0.
}
\]


---

9. Orientation-safe current measurements

The current ensemble can be symmetric under

\[
I\rightarrow-I.
\]

A direct signed-current average may therefore vanish even when individual configurations contain coherent winding circuits.

Let \(W_\parallel\) be the signed integer winding along the comparator direction.

Define

\[
\boxed{
\mathcal Q(s)
=
\frac{
\left\langle
W_\parallel Q_\parallel(s)
\right\rangle
}{
\left\langle W_\parallel^2\right\rangle
},
}
\]

and

\[
\boxed{
\mathcal F(s)
=
\frac{
\left\langle
W_\parallel F_\perp(s)
\right\rangle
}{
\left\langle W_\parallel^2\right\rangle
}.
}
\]

Under \(I\rightarrow-I\),

\[
W_\parallel\rightarrow-W_\parallel,
\qquad
Q_\parallel\rightarrow-Q_\parallel,
\qquad
F_\perp\rightarrow-F_\perp.
\]

The products remain invariant. This aligns current orientation without choosing a favorable direction after observing the data.

If

\[
\left\langle W_\parallel^2\right\rangle
\]

is too small for reliable estimation, the comparator is reported as unresolved.


---

10. Primary TTSC prediction

At the frozen throat location \(s_0\), TTSC predicts

\[
\boxed{
\mathcal Q(s_0)
=
\max_s\mathcal Q(s).
}
\]

For every preregistered offset \(\Delta\) in the primary throat window,

\[
\boxed{
\mathcal F(s_0-\Delta)<0,
}
\]

\[
\boxed{
\mathcal F(s_0)=0,
}
\]

\[
\boxed{
\mathcal F(s_0+\Delta)>0.
}
\]

The complete profile must also satisfy

\[
\boxed{
\sum_s\mathcal F(s)=0
}
\]

within the frozen numerical tolerance.


---

11. Flat control

The mandatory null control is

\[
\epsilon=0.
\]

Then

\[
U(s)=U_0,
\qquad
U'(s)=0,
\qquad
v_r=0.
\]

The flat comparator predicts

\[
\boxed{
\mathcal Q(s)=\text{constant},
\qquad
\mathcal F(s)=0.
}
\]

Any phase-locked throat signature that persists unchanged in the flat control is evidence against the proposed throat response.


---

12. Translated-throat control

The throat location \(s_0\) must be frozen before thermalization.

Additional runs may translate \(s_0\) using a preregistered displacement. A valid imposed-throat response must translate with the imposed profile.

If the measured maximum remains attached to a privileged lattice coordinate rather than following \(s_0\), the throat interpretation is rejected or classified as a lattice artifact.

No throat position may be selected after inspecting the measured current profile.


---

13. Distinction from an X-point

TTSC-1 tests a regular converging–diverging throat. It does not test reconnection.

A local incompressible saddle field may instead be written

\[
\mathbf v=(ax,ay,-2az),
\]

with

\[
\nabla\cdot\mathbf v=0.
\]

That field approaches along a stable direction and departs along unstable directions. The outflow direction is generally rotated relative to the inflow direction.

A magnetic-reconnection claim would additionally require:

magnetic-field variables;

field-line connectivity;

a nonideal diffusion region;

an induction equation;

evidence that the frozen-in condition fails locally.


None of those follow from conserved current winding alone.

An X-point or reconnection comparator must therefore be separately defined and may not inherit support from TTSC-1.


---

14. Relation to centripetal and centrifugal language

TTSC directly measures radial convergence and divergence:

\[
v_r<0
\quad\text{and}\quad
v_r>0.
\]

It does not directly measure centripetal or centrifugal acceleration.

Acceleration requires

\[
\mathbf a
=
\frac{\partial\mathbf v}{\partial t}
+
(\mathbf v\cdot\nabla)\mathbf v.
\]

Accordingly:

Permitted physical language: transverse convergence, maximum-throughflow throat, transverse divergence.

Permitted symbolic language: centripetal-in and centrifugal-out.

Prohibited identification: the signs of \(v_r\) alone prove centripetal or centrifugal forces.



---

15. Decision criteria

Result	Verdict

Preregistered pre-throat \(\mathcal F<0\), throat \(\mathcal F=0\), post-throat \(\mathcal F>0\); \(\mathcal Q\) maximal at \(s_0\); conservation and translation controls pass	TTSC SUPPORTED
No preregistered radial sign reversal, while sampling and conservation tests pass	TTSC REJECTED
Signature also appears unchanged at \(\epsilon=0\)	TTSC REJECTED — NON-THROAT OR LATTICE EFFECT
Signature remains fixed when the imposed throat is translated	TTSC REJECTED — PRIVILEGED-LOCATION ARTIFACT
Discrete divergence residual exceeds tolerance	TTSC INVALID — CONSERVATION FAILURE
Insufficient signed winding or sector mixing	TTSC UNRESOLVED — ORIENTATION OR MIXING INADEQUATE
Current changes direction longitudinally rather than only transversely	TTSC ANOMALY — BACKFLOW/REFLECTION MODEL REQUIRED



---

16. Mandatory reporting language

Permitted:

> “At fixed imposed throat geometry, winding-aligned current correlations converge transversely before the maximum-throughflow surface and diverge afterward.”



> “The measured profile is consistent with divergence-free throat kinematics.”



> “The transverse current projection changes sign while the longitudinal winding orientation is retained.”



Prohibited:

> “A singularity flips the current.”



> “The Q2 winding measurement proves a toroidal throat.”



> “The simulation demonstrates magnetic reconnection.”



> “The universe is physically a torus.”



> “Centripetal force becomes centrifugal force at the core.”




---

17. Relation to Theory v0.1 and Q2

Theory v0.1 remains the frozen local operator proposal

\[
z\sim-z,
\qquad
\Phi=z^2,
\qquad
z^6+z^{*6}.
\]

TTSC-1 introduces no new term, field or phenomenological identification into Theory v0.1.

Canonical Q2 continues to measure whether charge-one integer currents occupy the noncontractible winding sectors of \(T^3\).

TTSC-1 asks a different question:

> Given an oriented winding circuit and a separately imposed regular throat profile, does the local conserved-current geometry exhibit the preregistered convergence–maximum–divergence sequence?



A positive TTSC result does not alter Q1, Q2 or Q3.


---

18. Freeze card

Requirement	Freeze condition

Comparator status	Stage D; non-verdict-bearing
Throat profile	\(U_\epsilon(s)=U_0[1+\epsilon\cos(2\pi(s-s_0)/L)]\)
Regularity	\(0<\epsilon<1\)
Flat control	\(\epsilon=0\)
Throat location	\(s_0\) frozen before thermalization
Orientation	Signed \(W_\parallel\); no post-hoc direction choice
Conservation	Discrete residual identically zero or within frozen tolerance
Primary prediction	\(\mathcal F_-<0,\ \mathcal F_0=0,\ \mathcal F_+>0\)
Through-flow prediction	\(\mathcal Q(s_0)=\max_s\mathcal Q(s)\)
Periodic closure	\(\sum_s\mathcal F(s)=0\)
Translation control	Measured profile follows translated \(s_0\)
Execution order	Only after canonical Q2 gate passes
Theory boundary	No modification of Theory v0.1



---

19. Frozen comparator object

The TTSC-1 result object is

\[
\boxed{
\left(
U_\epsilon(s),
R(s),
Q_\parallel(s),
F_\perp(s),
\mathcal Q(s),
\mathcal F(s),
\mathcal R_{\mathrm{div}},
\mathcal R_{\mathrm{closure}}
\right).
}
\]

Here:

\(\mathcal R_{\mathrm{div}}\) is the frozen discrete-divergence residual;

\(\mathcal R_{\mathrm{closure}}\) is the periodic closure residual.


The central hypothesis is

\[
\boxed{
\mathcal F(s_0-\Delta)<0
\;\longrightarrow\;
\mathcal F(s_0)=0
\;\longrightarrow\;
\mathcal F(s_0+\Delta)>0,
}
\]

with

\[
\boxed{
\mathcal Q(s_0)=\max_s\mathcal Q(s)
}
\]

and no reversal of the longitudinal winding orientation.


---

20. Frozen conclusion

TTSC-1 formalizes the hypothesis that a divergence-free toroidal through-flow can converge toward a regular throat, attain maximal longitudinal transport and diverge afterward while preserving current conservation and global circuit closure.

It does not require a singularity.

It does not infer reconnection.

It does not modify canonical Q2.

It converts the intuition

\[
\text{centripetal in}
\rightarrow
\text{core}
\rightarrow
\text{centrifugal out}
\]

into the testable statement

\[
\boxed{
\textbf{A winding-aligned conserved current exhibits a preregistered transverse sign reversal across a regular maximum-throughflow throat.}
}
\]


CC0 1.0 Universal
To the extent permitted by law, this work is dedicated to the public domain under CC0 1.0 Universal.
No permission required. Copy it, modify it, test it, redistribute it, build on it, or tear it apart.
No ownership claim. No attribution required. No warranty.
Use freely.


