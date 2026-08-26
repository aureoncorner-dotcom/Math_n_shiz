Simulation Protocol v0.3-RC1

Dual-First, Direct-Cross-Validated Study of Charge-Sector Criticality and Sixfold Anisotropy in the Three-Dimensional Z_2-Gauged XY Model

Supersedes: Simulation Protocols v0.1 and v0.2
Theory status: Theory v0.1 unchanged
Document status: Audited release candidate
Structural freeze: Conditional
Execution freeze: Not active until Appendices A and B are completed and hashed
Primary purpose: Test charge-two O(2) critical scaling and irrelevance of the physical Z_3 anisotropy in an explicit three-dimensional Z_2-gauged rotor, while measuring the disputed charge-one confinement/deconfinement sector without promoting finite-size quasi-deconfinement into an asymptotic claim.

---

0. Release Note and Hard Corrections

Protocol v0.3-RC1 incorporates the corrections discovered during the v0.1–v0.3 audit.

The following points are now canonical:

1. Ordinary fundamental Wilson loops are not primary confinement/deconfinement discriminators in the presence of dynamical charge-one matter.

2. Flipping a noncontractible plane of link signs can leave every plaquette flux unchanged. Such a move is a global holonomy-sector operation, not a vison insertion.

3. The correctly normalized integer-current winding is
   [
   W_\alpha=\frac1L\sum_{\ell\parallel\alpha}I_\ell.
   ]

4. The stiffness is
   [
   \rho_\alpha=\frac{\langle W_\alpha^2\rangle}{L},
   ]
   while the dimensionless critical observable is
   [
   R_W=L\rho_\alpha=\langle W_\alpha^2\rangle.
   ]
   This agrees with the convention used by Coleman, Kuklov, and Tsvelik.

5. The old expression G_1/\sqrt{G_2} is not frozen as a Fredenhagen–Marcu observable.

6. Local dual charge-six source density is not an RG-order-parameter amplitude and cannot by itself establish anisotropy relevance or irrelevance.

7. Villain and cosine realizations remain separate microscopic models. Published Villain critical couplings may never be numerically imported into the cosine branch.

8. The susceptibility exponent test is not implemented as a fixed \pm0.02 kill window.

9. No fixed relation of the form
   [
   N\tau_{\rm int}\Rightarrow\text{specified exponent uncertainty}
   ]
   is assumed.

10. Most importantly: the naive odd-winding statistic is not treated as an observable of the fully link-summed periodic dual ensemble without an explicit global-sector construction.

In the written fully summed dual representation, the mod-two current satisfies

[
\bar I_\ell=I_\ell\bmod2
]

and the link projector implies

[
\boxed{\bar I=\partial M}
]

as a Z_2 chain relation.

Therefore the fully projected current parity is homologically trivial on the periodic torus unless an appropriate background holonomy, seam, or gauge-fixed sector is retained.

CKT's published implementation permits odd-current updates along one direction only after imposing the axial condition u_{ij}=1 on links in that direction.

Accordingly:

[
\boxed{\text{Q2 SECTOR GATE CLOSED}}
]

until Appendix A derives and validates the exact finite-volume sector construction used for odd-winding statistics.

This gate does not block Q1 or Q3.

---

1. Claim Boundary

1.1 Upstream discrete mathematics

The upstream project supplies an exact discrete refinement and candidate finite geometry.

Those mathematical constructions do not themselves establish that a physical Z_2 gauge field is generated.

Source equality, witness-induced equivalence, quotient equality, and physical realization remain separate claims unless an explicit constructor or proof joins them.

This simulation protocol therefore tests a separately selected microscopic model motivated by the operator structure frozen in Theory v0.1.

The local gauge redundancy is

[
z\sim-z,
]

and the physical local field is

[
\boxed{\Phi=z^2}.
]

The physical Z_3 operator satisfies

[
\Phi^3=z^6.
]

Thus the leading fine-field phase anisotropy considered here is

[
z^6+z^{*6}.
]

1.2 Prior art

The general composite-order mechanism is prior art.

Xu and Balents studied a continuum theory containing a sixth-order anisotropy and a physical composite order parameter V\sim\psi^2. The present project therefore makes no first-discovery claim for

[
\Phi=z^2,
\qquad
\Phi^3=z^6,
]

or for generic charge-two XY^*-type critical scaling.

The potentially distinctive contribution is narrower:

- the independent discrete-refinement/operator-selection route;
- an explicit Z_2-gauged rotor realization;
- direct comparison of distinct charge sectors;
- explicit finite-h_6 anisotropy testing;
- and a protocol that prevents finite-size quasi-deconfinement from automatically becoming an asymptotic deconfinement claim.

1.3 Relevant numerical controversy

Bonati, Pelissetto, and Vicari find continuous XY-class ordering transitions on the large-gauge-coupling line of the N=2 model. The gauge-invariant bilinear behaves there as the XY spin-two operator with

[
Y_{T,XY}=1.23629(11),
]

so its susceptibility scales approximately as

[
\chi\sim L^{0.5274}.
]

They contrast this with the ordinary-vector scaling lane

[
\chi\sim L^{1.96182}.
]

Coleman, Kuklov, and Tsvelik instead report large-scale simulations and heuristic arguments consistent with asymptotic confinement throughout phase III for every finite gauge coupling, together with a confinement radius that grows rapidly enough to mimic deconfinement on finite lattices. Their work is published as Phys. Rev. Lett. 134, 236001 (2025).

Protocol v0.3-RC1 assumes neither side is correct in advance.

---

2. Three Questions, Three Independent Verdicts

Q1 — Charge-sector criticality

Does the physical gauge-invariant field

[
\Phi_i=e^{2i\theta_i}
]

show the spin-two scaling dimension of the three-dimensional O(2) fixed point?

Target:

[
\boxed{\Delta_2=1.23629(11)}.
]

Hence

[
G_2(r)\sim r^{-2\Delta_2}
]

and

[
\boxed{
\chi_2(L)\sim L^{3-2\Delta_2}
=L^{0.52742\ldots}.
}
]

Competing ordinary-vector scaling predicts approximately

[
\boxed{\chi_2(L)\sim L^{1.96182}}.
]

Possible Q1 verdicts:

[
\boxed{\text{SUPPORTED}}
]

[
\boxed{\text{REJECTED}}
]

[
\boxed{\text{UNRESOLVED}}.
]

---

Q2 — Asymptotic charge-one confinement/deconfinement

Does the fractional charge-one field remain deconfined at arbitrarily large scales, or does apparent deconfinement terminate at a finite but potentially enormous confinement radius?

Possible verdicts:

[
\boxed{\text{EVIDENCE FOR CONFINEMENT}}
]

[
\boxed{\text{EVIDENCE FOR DECONFINEMENT}}
]

[
\boxed{\text{QUASI-DECONFINED / ASYMPTOTICALLY UNRESOLVED}}.
]

No Q2 verdict is issued until the Appendix-A global-sector construction passes validation.

Q2 never determines Q1.

---

Q3 — Sixfold anisotropy

For small frozen h_6\neq0, does the perturbation

[
\cos6\theta
]

flow toward zero at critical scales?

Because

[
\Phi=e^{2i\theta},
]

the same operator is

[
\cos6\theta

\cos(3\arg\Phi).
]

The primary observable is therefore gauge invariant.

Possible Q3 verdicts:

[
\boxed{\text{IRRELEVANT}}
]

[
\boxed{\text{RELEVANT}}
]

[
\boxed{\text{UNRESOLVED}}.
]

---

3. Microscopic Models

3.1 Primary cosine production model

The canonical direct action is

[
\boxed{
H_{\cos}

-J\sum_{\langle ij\rangle}
\sigma_{ij}\cos(\theta_i-\theta_j)
-\kappa\sum_pB_p
-h_6\sum_i\cos6\theta_i
}
]

with

[
\theta_i\in[0,2\pi),
]

[
\sigma_{ij}=\pm1,
]

and

[
B_p=\prod_{\ell\in p}\sigma_\ell.
]

Define

[
z_i=e^{i\theta_i},
\qquad
\Phi_i=e^{2i\theta_i}.
]

The local gauge transformation is

[
z_i\rightarrow s_i z_i,
]

[
\sigma_{ij}\rightarrow s_i\sigma_{ij}s_j,
]

[
s_i=\pm1.
]

Equivalently,

[
s_i=-1
\quad\Longleftrightarrow\quad
\theta_i\rightarrow\theta_i+\pi.
]

Define

[
\boxed{t=\tanh\kappa}.
]

---

3.2 Villain validation model

The Villain branch replaces the direct cosine bond factor with the periodic Gaussian Villain weight.

After dualization, the matter-current weight is

[
\boxed{
w_J^{\rm V}(I)

\exp\left(-\frac{I^2}{2J}\right).
}
]

This branch exists principally to reproduce the published CKT current/membrane results.

Villain and cosine critical couplings are not interchangeable. CKT explicitly report substantial nonuniversal displacement between their Villain and cosine phase boundaries.

---

3.3 Convention map

For N=2, BPV use

[
H_s=-2J_{\rm BPV}
\sum_{\langle ij\rangle}
\sigma_{ij}\cos(\theta_i-\theta_j).
]

Therefore

[
\boxed{
J_{\rm protocol}

J_{\rm CKT}

2J_{\rm BPV}.
}
]

Gauge coupling maps as

[
\boxed{
\kappa_{\rm protocol}=K_{\rm BPV},
}
]

while CKT commonly use

[
\boxed{
t=K_{\rm CKT}=\tanh\kappa.
}
]

BPV's K=0.8 point with J_c\simeq0.229 therefore corresponds to protocol matter coupling

[
J_c\simeq0.458.
]

Their K=1 value

[
J_c=0.22729(3)
]

corresponds to

[
J_{\rm protocol}=0.45458(6).
]

BPV's normalization is explicit in their lattice Hamiltonian.

---

4. Dual Representation

4.1 Exact cosine-current representation

Use the Fourier expansion

[
e^{J\sigma_\ell\cos\Delta\theta_\ell}

\sum_{I_\ell\in\mathbb Z}
\mathcal I_{|I_\ell|}(J)
\sigma_\ell^{I_\ell}
e^{iI_\ell\Delta\theta_\ell},
]

and

[
e^{h_6\cos6\theta_i}

\sum_{n_i\in\mathbb Z}
\mathcal I_{|n_i|}(h_6)e^{i6n_i\theta_i}.
]

For the plaquette term,

[
e^{\kappa B_p}

\cosh\kappa
\sum_{M_p=0}^{1}
t^{M_p}B_p^{M_p}.
]

After integrating \theta and summing the Z_2 links,

[
\boxed{
Z_{\cos}

C_{\cos}
\sum_{{M,I,n}}
t^{\sum_pM_p}
\prod_\ell
\mathcal I_{|I_\ell|}(J)
\prod_i
\mathcal I_{|n_i|}(h_6)
\prod_i
\delta_{\mathbb Z}
!\left[(\nabla\cdot I)i+6n_i\right]
\prod\ell
\delta_{\mathbb Z_2}
!\left[I_\ell+M_\ell\right].
}
]

Here

[
M_p\in{0,1},
]

[
I_\ell\in\mathbb Z,
]

[
n_i\in\mathbb Z,
]

and

[
M_\ell

\sum_{p\supset\ell}M_p.
]

The parity projector is equivalently

[
\Delta_\ell

\frac{
1+(-1)^{I_\ell+M_\ell}
}{2}.
]

---

4.2 Villain form

Replace only the link weight:

[
\boxed{
\mathcal I_{|I_\ell|}(J)
\rightarrow
\exp\left(-\frac{I_\ell^2}{2J}\right).
}
]

Thus

[
\boxed{
Z_{\rm V}

C_{\rm V}
\sum_{{M,I,n}}
t^{\sum_pM_p}
\prod_\ell
e^{-I_\ell^2/(2J)}
\prod_i
\mathcal I_{|n_i|}(h_6)
\prod_i
\delta_{\mathbb Z}
[(\nabla\cdot I)i+6n_i]
\prod\ell
\delta_{\mathbb Z_2}
[I_\ell+M_\ell].
}
]

At

[
h_6=0,
]

only n_i=0 contributes, giving

[
\boxed{\nabla\cdot I=0}.
]

This is the conserved-current Villain branch used for the CKT calibration.

---

4.3 Charge-six leakage

For finite h_6,

[
\boxed{
(\nabla\cdot I)_i=-6n_i.
}
]

Thus integer current can terminate only in multiples of six.

On a periodic lattice,

[
\sum_i(\nabla\cdot I)_i=0,
]

so

[
\boxed{
\sum_i n_i=0.
}
]

This exact source-neutrality identity is a hard code test.

---

4.4 Parity conservation

Modulo two,

[
6n_i=0.
]

Therefore

[
\boxed{
\nabla\cdot I=0\pmod2.
}
]

Charge-six sources preserve current parity.

This is the exact dual manifestation of the operator-selection statement that a sixth-order anisotropy does not violate the Z_2 gauge parity structure.

---

5. Global-Sector Gate for Q2

This section is mandatory.

In the completely link-summed periodic dual,

[
I_\ell+M_\ell=0\pmod2.
]

Writing the plaquette variables as a Z_2 2-chain M,

[
M_\ell=(\partial M)_\ell.
]

Therefore

[
\boxed{
I\bmod2=\partial M.
}
]

A boundary represents the trivial element of the first homology group.

Thus the fully projected ensemble does not automatically contain an independently variable odd mod-two winding class.

This matters because CKT's published odd-current algorithm is not simply the unrestricted implementation of the fully summed periodic formula: their odd update is allowed along one direction after the gauge condition

[
u_{ij}=1
]

has been imposed on links parallel to that direction.

Accordingly the protocol distinguishes:

[
\boxed{
Z_{\rm full}
}
]

for Q1 and ordinary thermodynamics from a possible

[
\boxed{
Z_{\rm sector}
}
]

or seam/fixed-holonomy ensemble used for Q2.

Appendix A must construct one of the following exactly:

- a fixed-holonomy ensemble;
- an axial/maximal-tree gauge with explicit residual global variables;
- a seam-modified current ensemble;
- or equivalent periodic/antiperiodic sector partition functions.

Before Q2 production it must demonstrate:

1. exact relation to the original direct partition function;
2. which link parity projectors remain after gauge fixing;
3. treatment of the three toroidal Z_2 holonomies;
4. normalization of sector probabilities;
5. relation to CKT's axial implementation;
6. detailed balance;
7. sector reachability;
8. small-volume direct/dual agreement.

Until then:

[
\boxed{
\text{Q2 diagnostics are calibration-only and cannot trigger a physical verdict.}
}
]

---

6. Monte Carlo Kernels

6.1 h_6=0 dual moves

Move D1 — Cube surface toggle

Toggle M_p on all six faces of an elementary cube.

Every cube edge is touched twice, so the link-parity constraint remains unchanged.

Move D2 — Coupled plaquette-current loop

Toggle one M_p and simultaneously add or subtract an oriented elementary current loop around its boundary.

This preserves both current conservation and link parity.

Move D3 — Even worm

Introduce a temporary charge-two endpoint pair and move an endpoint through updates

[
\Delta I_\ell=\pm2.
]

This samples the physical charge-two sector and measures G_2.

Move D4 — Global closed membrane-sheet move

Propose toggling M_p on a noncontractible closed plaquette sheet.

This move is required to sample distinct membrane homology sectors not connected by elementary cube updates.

Move D5 — Conditional Q2 sector kernel

The odd-sector kernel is defined only after Appendix A.

It must explicitly identify the retained holonomy/seam variable that makes the odd sector possible.

---

6.2 Finite-h_6 local source transfer

For oriented link i\rightarrow j, propose

[
n_i\rightarrow n_i+s,
]

[
n_j\rightarrow n_j-s,
]

[
I_{ij}\rightarrow I_{ij}-6s,
]

with

[
s=\pm1.
]

The Villain Metropolis ratio is

[
\boxed{
R_{\rm V}

\frac{\mathcal I_{|n_i+s|}(h_6)}
{\mathcal I_{|n_i|}(h_6)}
\frac{\mathcal I_{|n_j-s|}(h_6)}
{\mathcal I_{|n_j|}(h_6)}
\exp
\left[
-\frac{
(I_{ij}-6s)^2-I_{ij}^2
}{2J}
\right].
}
]

The cosine ratio is

[
\boxed{
R_{\cos}

\frac{\mathcal I_{|n_i+s|}(h_6)}
{\mathcal I_{|n_i|}(h_6)}
\frac{\mathcal I_{|n_j-s|}(h_6)}
{\mathcal I_{|n_j|}(h_6)}
\frac{
\mathcal I_{|I_{ij}-6s|}(J)
}{
\mathcal I_{|I_{ij}|}(J)
}.
}
]

These expressions assume symmetric proposals.

This local move is constraint preserving but is not assumed globally ergodic.

---

6.3 Charge-six worm

Finite-h_6 dual production requires a separately validated charge-six worm or equivalent global routing algorithm.

The worm must demonstrate the ability to:

- create a temporary \pm6 divergence defect pair;
- route the endpoints over arbitrary separation;
- wind through every periodic direction;
- annihilate after contractible and noncontractible paths;
- reproduce exact small-volume statistics;
- and decorrelate the n_i sector efficiently.

Until those tests pass, finite-h_6 dual data are secondary only.

---

6.4 Direct cosine kernel

One compound direct sweep contains:

1. one rotor Metropolis proposal per site;
2. one gauge-link flip proposal per link;
3. five microcanonical/over-relaxation rotor proposals per site;
4. optional global holonomy updates at frozen intervals.

Rotor proposal:

[
\theta_i'

\theta_i+\delta_\theta u,
\qquad
u\sim{\rm Uniform}[-1,1].
]

Acceptance:

[
P_{\rm acc}

\min(1,e^{-\Delta H}).
]

Gauge-link proposal:

[
\sigma_{ij}'=-\sigma_{ij}.
]

At h_6\neq0, an over-relaxation move receives a Metropolis correction for the change in the onsite anisotropy.

Proposal-width adaptation is allowed only during thermalization/calibration.

No production adaptation is permitted.

---

7. Observables

7.1 Physical magnetization

[
\boxed{
m_\Phi

\frac1N
\sum_i e^{2i\theta_i}.
}
]

Define

[
M_\Phi=\langle|m_\Phi|\rangle.
]

The symbol M_3 is retired for this quantity to prevent confusion with the physical threefold harmonic.

---

7.2 Charge-two correlation function

[
\boxed{
G_2(r)

\left\langle
e^{2i\theta(r)}
e^{-2i\theta(0)}
\right\rangle.
}
]

The corresponding susceptibility is

[
\boxed{
\chi_2

\sum_rG_2(r).
}
]

Candidate spin-two XY scaling:

[
G_2(r)\sim r^{-2(1.23629)},
]

[
\chi_2\sim L^{0.52742}.
]

Ordinary-vector alternative:

[
\chi_2\sim L^{1.96182}.
]

BPV explicitly identify these distinct scaling powers.

---

7.3 Physical correlation length

Define

[
S_\Phi(\mathbf k)

\frac1N
\left\langle
\left|
\sum_j
e^{2i\theta_j}
e^{i\mathbf k\cdot\mathbf r_j}
\right|^2
\right\rangle.
]

Then

[
\boxed{
\xi_\Phi

\frac1{2\sin(\pi/L)}
\sqrt{
\frac{
S_\Phi(\mathbf0)
}{
\overline{
S_\Phi(\mathbf k_{\min})
}
}
-1
}.
}
]

The bar averages the three minimal cubic momenta.

Set

[
\boxed{
R_\xi=\frac{\xi_\Phi}{L}.
}
]

---

7.4 Binder ratio

Use the complex two-component convention

[
\boxed{
U_4

1-
\frac{
\langle|m_\Phi|^4\rangle
}{
2\langle|m_\Phi|^2\rangle^2
}.
}
]

The precise convention is frozen and must not be changed mid-analysis.

---

7.5 Integer winding and stiffness

At h_6=0,

[
\boxed{
W_\alpha

\frac1L
\sum_{\ell\parallel\alpha}I_\ell.
}
]

Then

[
\boxed{
\rho_\alpha

\frac{\langle W_\alpha^2\rangle}{L}.
}
]

The scale-invariant observable is

[
\boxed{
R_W

L\rho_\alpha

\langle W_\alpha^2\rangle.
}
]

CKT use exactly this winding normalization.

At finite h_6, ordinary integer-current winding is no longer treated as an exactly conserved topological number because

[
\nabla\cdot I=-6n.
]

---

7.6 Physical anisotropy harmonic

Define

[
\boxed{
A_3^\Phi(L)

\left\langle
\cos
\left[
3\arg(m_\Phi)
\right]
\right\rangle.
}
]

Equivalently,

[
A_3^\Phi=A_6^\uparrow.
]

It is threefold in the physical field and sixfold in the fine field.

At the critical point, irrelevance predicts

[
A_3^\Phi\rightarrow0
]

asymptotically.

In the ordered anisotropic phase it should eventually lock to a nonzero value.

Retain the complete histogram

[
P(\arg m_\Phi).
]

---

7.7 Zero-field anisotropy response

Define

[
H_6=\sum_i\cos6\theta_i.
]

At h_6=0,

[
\langle A_3^\Phi\rangle=0
]

by global U(1) symmetry.

Its response is

[
\boxed{
D_6(L)

\left.
\frac{\partial A_3^\Phi}{\partial h_6}
\right|_{h_6=0}

\langle A_3^\Phi H_6\rangle.
}
]

This supplies a zero-field estimator for the sign of the sixfold RG eigenvalue.

---

7.8 Dual charge-six source density

[
\boxed{
n_6

\frac1N
\left\langle
\sum_i|n_i|
\right\rangle.
}
]

Its roles are:

- algorithm validation;
- source-sector thermodynamics;
- autocorrelation diagnosis;
- direct/dual consistency checks.

It is not a Q3 kill observable.

A nonzero local source density can contain a regular analytic contribution even when the anisotropy scaling field is irrelevant.

---

7.9 Dual plaquette occupation

Define

[
m_M

\frac1{N_p}
\left\langle
\sum_pM_p
\right\rangle.
]

It is not equal directly to the physical plaquette flux.

Since

[
Z

(\cosh\kappa)^{N_p}
Z_{\rm dual}(t),
]

one obtains

[
\boxed{
\langle B_p\rangle

t+
\frac{1-t^2}{t}m_M,
\qquad t>0.
}
]

This transformed quantity is used in direct/dual equivalence tests.

---

7.10 Conditional odd-sector statistic

After Appendix A passes, define the sector-specific winding statistic

[
\boxed{
f_{\rm odd}(L)

P(W_z\ {\rm odd})
}
]

within the precisely defined retained-holonomy/seam ensemble.

It may not be computed from an ensemble for which odd current homology is algebraically projected out.

---

7.11 Charge-one confinement radius

For CKT benchmark reproduction, retain their axial-gauge charge-one correlator and radius definitions.

Their simulations at

[
t=0.7,
\qquad
J=0.336
]

showed charge-one radius saturation only for systems several times larger than the inferred confinement radius.

Production \xi_{\rm conf} is defined by the frozen fit in Appendix B, not by the heuristic membrane formula.

---

7.12 Fredenhagen–Marcu diagnostic

For a frozen open path \gamma,

[
\boxed{
R_{\rm FM}

\frac{
\left\langle
z_i^\dagger
\left(
\prod_{\ell\in\gamma}\sigma_\ell
\right)
z_j
\right\rangle
}{
\sqrt{
\left\langle
\prod_{\ell\in C(\gamma)}
\sigma_\ell
\right\rangle
}
}.
}
]

The open path and closed contour must be geometrically matched.

The conventional asymptotic interpretation is

[
R_{\rm FM}\rightarrow0
]

for a deconfined charged sector and

[
R_{\rm FM}\rightarrow{\rm nonzero}
]

for confinement/Higgs behavior. Modern analyses likewise describe vanishing versus nonvanishing Marcu–Fredenhagen ratios in these terms.

FM is secondary and cannot independently trigger Q2.

---

7.13 Magnetic twist

A twist modifies the action/sector, rather than merely flipping a gauge-equivalent link plane.

For a z-directed twist choose a coclosed stack \mathcal S_z of xy plaquettes wrapping the torus.

Define

[
H_\lambda

H_{\rm matter}
-\kappa
\sum_{p\notin\mathcal S_z}B_p
-\kappa(1-2\lambda)
\sum_{p\in\mathcal S_z}B_p.
]

Then

[
\boxed{
\Delta F_{\rm tw}

2\kappa
\int_0^1d\lambda
\left\langle
\sum_{p\in\mathcal S_z}B_p
\right\rangle_\lambda.
}
]

No universal scaling law is assumed before calibration.

---

7.14 First-order diagnostics

Measure:

- energy histogram;
- |m_\Phi| histogram;
- Binder behavior;
- susceptibility volume scaling;
- peak separation;
- free-energy barrier.

A finite-size double peak alone is insufficient.

---

8. Calibration Ladder

No target production analysis begins until all applicable rungs pass.

Rung A0 — Exact constraint tests

Use L=2 and L=3 small systems where exact or high-precision enumeration is feasible.

Verify:

[
\sum_i n_i=0,
]

[
(\nabla\cdot I)_i+6n_i=0,
]

and every parity projector exactly.

---

Rung A1 — Periodic homology audit

For the completely link-summed dual implementation verify numerically that the mod-two current satisfies

[
I\bmod2=\partial M.
]

This rung validates the Q2 sector warning rather than suppressing it.

---

Rung A2 — Pure Z_2 gauge

Set

[
J=0.
]

The pure gauge critical coupling is

[
\boxed{
\kappa_c=0.761413292(11)
}
]

in the direct convention, corresponding to

[
\boxed{
t_c

\tanh\kappa_c

0.6419086649\ldots
}
]

numerically. BPV quote the direct critical value 0.761413292(11).

The mapping is exact; the decimal critical value is numerical.

---

Rung A3 — Pure cosine XY

Take

[
\kappa=\infty,
\qquad
h_6=0,
]

and explicitly fix the trivial flat holonomy sector.

In protocol normalization,

[
\boxed{
J_c^{XY}

2(0.22708234)

0.45416468.
}
]

The holonomy qualification matters: BPV note that the gauge model with periodic boundary conditions at K\rightarrow\infty corresponds to an XY model with fluctuating boundary conditions unless the sector is fixed.

---

Rung A4 — Villain CKT transition

At

[
t=0.7,
]

reproduce

[
\boxed{
J_c=0.3335(3)
}
]

for the Villain branch.

---

Rung A5 — Villain CKT radius benchmark

At

[
t=0.7,
\qquad
J=0.336,
]

reproduce:

[
\rho_s\approx0.038,
]

long-ranged charge-two behavior,

and delayed saturation of the charge-one radius.

CKT report that saturation became visible only for L roughly three to four times the inferred confinement radius.

---

Rung A6 — Cosine first-order control

Use the BPV K=0.7 point as a normalization-aware first-order control.

BPV find

[
J_{\rm BPV,c}=0.2520(3).
]

Therefore protocol normalization gives approximately

[
\boxed{
J_c=0.5040(6)
}
]

at

[
\kappa=0.7.
]

Their K=0.7 transition is reported as first order.

---

Rung A7 — Cosine direct/dual equivalence

Compare direct and exact cosine-dual simulations for frozen small systems.

Required common observables include:

[
\langle B_p\rangle,
]

[
G_2(r),
]

[
\chi_2,
]

[
R_\xi,
]

and derivatives of \ln Z available in both representations.

Do not require M_\Phi=\langle|m_\Phi|\rangle unless an explicit dual estimator has been derived.

---

Rung A8 — AF three-state Potts external control

Use the simple-cubic antiferromagnetic three-state Potts model as an external global six-state control.

Its role is to calibrate:

- ordinary XY critical analysis;
- emergent bulk O(2);
- sixfold ordered-state locking.

It is not a gauge-theory constructor.

Modern work explicitly describes emergent bulk O(2) behavior and a Z_6-ordered structure in this system.

---

9. Staged Execution

Stage A — Validation

Run Rungs A0–A8 as applicable.

Required deliverables:

- convention map;
- exact-constraint unit tests;
- detailed-balance tests;
- small-volume enumeration;
- direct/dual equivalence tables;
- autocorrelation estimates;
- global-sector diagnostics;
- RNG reproducibility;
- hash reproducibility.

A hard calibration failure stops target production.

---

Stage B — h_6=0 charge-sector study

Use the cosine model at three frozen moderate gauge couplings.

For every point:

1. locate the matter transition;
2. measure R_\xi;
3. measure U_4;
4. measure G_2;
5. measure \chi_2;
6. measure R_W as an auxiliary quantity;
7. run first-order diagnostics;
8. perform Q1 fits.

Q2 data may be generated only if the sector gate has passed.

---

Stage C — Nonzero h_6

Only Stage-B points surviving the continuous critical lane enter Stage C.

Use the direct cosine model as the primary representation.

Measure:

[
A_3^\Phi,
]

[
D_6,
]

[
P(\arg m_\Phi),
]

[
R_\xi,
]

and first-order diagnostics.

Finite-h_6 dual data are secondary until the charge-six worm is validated.

---

Stage D — Conditional Q2 branch

This stage opens only after Appendix A.

Use:

- sector-conditioned odd winding;
- charge-one confinement-radius fits;
- FM ratio;
- magnetic twist free energy.

The Q2 verdict remains independent of Q1 and Q3.

---

10. Fit Package FP-0.3-RC1

10.1 Statistical architecture

Field| Frozen RC value
Independent chains| 8
RNG| Philox4x32-10
Production adaptation| Prohibited
Autocorrelation estimator| \Gamma-method with automatic self-consistent window
Thermalization minimum| \max(10^4,100\widehat\tau_{\max}) compound sweeps
Block length| \lceil20\max_O\widehat\tau_{\rm int,O}\rceil, minimum 32 measurement intervals
Resampling| 5,000 hierarchical chain/block bootstrap replicates
Fit covariance| Full correlated covariance when numerically stable
Covariance cutoff| eigenmodes with \lambda/\lambda_{\max}<10^{-10} removed
Minimum fit sizes| 4 lattice sizes
Minimum residual degrees of freedom| 4
Acceptable bootstrap GOF| p\ge0.05
Strong GOF rejection| p<0.01
Strong model preference| \Delta{\rm AICc}\ge10
Primary L_{\min} sequence| 12,16,24,32,48, where enough larger sizes remain
Optional stopping| Prohibited

Calibration-only blind pilots may determine fixed production lengths before target observables are unmasked.

No production run may be lengthened because the emerging result appears favorable or unfavorable.

---

10.2 Deterministic seed generation

For each chain construct

[
{\rm seed}

{\rm first128bits}
\left[
{\rm SHA256}
(
{\rm protocol\ hash}
\Vert
{\rm code\ commit}
\Vert
{\rm model}
\Vert
L
\Vert
\kappa
\Vert
J
\Vert
h_6
\Vert
{\rm sector}
\Vert
{\rm chain\ id}
)
\right].
]

No hand-selected seeds.

---

10.3 Critical-point locator

Use R_\xi and U_4 as primary critical-point observables.

Let

[
x=(J-J_c)L^{1/\nu}.
]

Fit

[
\boxed{
R_a(J,L)

R_a^\star
+a_{a1}x
+a_{a2}x^2
+
L^{-\omega}
(b_{a0}+b_{a1}x)
}
]

for

[
a\in{R_\xi,U_4}.
]

Frozen fit families:

Family| \nu| \omega
C-XY| 0.6717| 0.789
C-\nu| free on [0.60,0.80]| 0.789
C-full| free on [0.60,0.80]| free on [0.4,1.3]
C-FO| 1/3| not interpreted as XY

BPV use \nu_{XY}=0.6717 in their successful scaling collapses for the continuous transitions.

For every bootstrap replicate:

1. refit J_c;
2. refit R_\xi^\star;
3. solve
   [
   R_\xi(J_L,L)=R_\xi^\star;
   ]
4. interpolate all Q1/Q3 observables to J_L;
5. propagate the shared interpolation covariance.

---

10.4 Reweighting rule

Reweighting is allowed only when

[
N_{\rm eff}^{\rm rew}
\ge
0.30N_{\rm raw}
]

and neighboring energy/action histograms overlap adequately.

Otherwise the deterministic additional-point rule in the parameter card applies.

---

11. Q1 Fit Package

11.1 Susceptibility models

At fixed R_\xi,

[
\boxed{
\chi_2(L)

b_0+
aL^\kappa
\left(
1+cL^{-\omega}
\right).
}
]

The additive analytic background b_0 is mandatory.

This is especially important because BPV note that along the spin-two lane the analytic-background correction behaves approximately as L^{-0.5274}, which can dominate the usual XY irrelevant correction L^{-0.789}.

Frozen hypotheses:

H2 — Spin-two target

[
\boxed{
\kappa=0.52742.
}
]

H1 — Ordinary-vector alternative

[
\boxed{
\kappa=1.96182.
}
]

Hfree

[
0\le\kappa\le3.
]

HFO

[
\kappa=3,
]

admissible only in conjunction with independent coexistence evidence.

Each hypothesis is run with:

1. c=0;
2. c\neq0,\ \omega=0.789;
3. c\neq0,\ \omega\in[0.4,1.3].

---

11.2 Spatial-correlator co-primary fit

For

[
s\in
\left{
\frac14,\frac13,\frac12
\right},
]

fit

[
\boxed{
G_2(sL,L)

L^{-2\Delta}
\left(
a_s+c_sL^{-\omega}
\right).
}
]

A single common \Delta is shared across all fractional separations.

Frozen comparisons:

[
\Delta=1.23629
]

versus

[
\Delta=0.519088.
]

The first is the XY spin-two dimension; the latter is the vector dimension reported by BPV.

---

11.3 Q1 support rule

Q1 is SUPPORTED only if:

1. first-order criteria do not fire;
2. H2 has acceptable GOF for at least three consecutive frozen L_{\min} windows, including the largest admissible window;
3. the free-exponent 95% interval includes 0.52742;
4. that interval excludes 1.96182;
5. H2 beats H1 by
   [
   \Delta{\rm AICc}\ge10;
   ]
6. the spatial-correlator estimate includes
   [
   1.23629;
   ]
7. it excludes
   [
   0.519088;
   ]
8. successive asymptotic estimates move by less than one combined standard deviation.

Q1 is REJECTED only when the spin-two target is stably incompatible across the final three admissible L_{\min} windows and a frozen alternative fits acceptably.

Otherwise:

[
\boxed{\text{Q1 UNRESOLVED}}.
]

---

12. Q3 Fit Package

12.1 Zero-field response

At fixed R_\xi,

[
\boxed{
D_6(L)

aL^{y_6}
\left(
1+cL^{-\omega}
\right).
}
]

The target condition for irrelevance is

[
\boxed{y_6<0}.
]

---

12.2 Finite-field joint response

Fit

[
\boxed{
A_3^\Phi(L,h_6)

a_0h_6L^{y_6}
\left(
1+a_1L^{-\omega}
\right)
+
b_3h_6^3L^{3y_6}.
}
]

The cubic term tests deviation from linear response.

Negative-h_6 controls test

[
\boxed{
A_3^\Phi(-h_6)

-A_3^\Phi(h_6)
}
]

within statistical uncertainty.

---

12.3 Nonzero-asymptote alternative

At fixed h_6,

[
\boxed{
A_3^\Phi(L)

A_\infty+cL^{-p},
\qquad p>0.
}
]

---

12.4 Ordered-state locking test

At a frozen ordered-side coupling, verify eventual nonzero anisotropic locking.

The operational dangerous-irrelevance pattern is

[
\boxed{
A_3^\Phi(K_c,L)\rightarrow0
}
]

while

[
\boxed{
A_3^\Phi(K>K_c,L)\rightarrow{\rm nonzero}.
}
]

---

12.5 Q3 support rule

Q3 irrelevance is SUPPORTED only when:

1. the upper 95% confidence bound on y_6 lies below zero in the zero-field-response fit;
2. the finite-h_6 fit independently gives y_6<0;
3. both conclusions survive the final three L_{\min} windows;
4. a nonzero critical asymptote is disfavored by
   [
   \Delta{\rm AICc}\ge10;
   ]
5. sign-reversal controls pass;
6. ordered-state locking is observed.

Q3 is REJECTED when a nonnegative y_6 or stable nonzero critical asymptote is supported.

Otherwise:

[
\boxed{\text{Q3 UNRESOLVED}}.
]

---

13. Conditional Q2 Fit Package

This section is inactive until Appendix A passes.

13.1 Odd-sector models

Use the actual sector counts with a binomial/block-bootstrap likelihood.

Persistent model

[
\boxed{
{\rm logit},f_{\rm odd}(L)

b_0+b_1L^{-\omega_o}.
}
]

Suppressed model

[
\boxed{
{\rm logit},f_{\rm odd}(L)

b_0-
\left(
\frac{L}{\lambda_o}
\right)^p.
}
]

Primary:

[
p=1.
]

Secondary:

[
p\in[0.5,2].
]

---

13.2 Charge-one radius

For the CKT calibration retain

[
\boxed{
\widetilde R_1^2

\frac{
\sum_z d_L(z)^2C_1(z)
}{
\sum_zC_1(z)
},
}
]

with

[
d_L(z)=\min(z,L-z).
]

Production C_1 is fit to

[
\boxed{
C_1(z;L)

A
\frac{
\cosh[(L/2-z)/\xi_{\rm conf}]
}{
\sinh[L/(2\xi_{\rm conf})]
}.
}
]

Competing long-range model:

[
\boxed{
C_1(z;L)

C_\infty+
A
\frac{
\cosh[(L/2-z)/\xi]
}{
\sinh[L/(2\xi)]
}.
}
]

The CKT membrane formula is retained as qualitative theory motivation only and does not define the measured \xi_{\rm conf}.

---

13.3 Scale-admissibility rule

Use the upper 95% confidence bound on the fitted confinement radius.

A finite-size Q2 claim is admissible only if

[
\boxed{
L_{\max}
\ge
4\xi_{\rm conf}^{95%,{\rm upper}}.
}
]

If not,

[
\boxed{
\text{Q2 INCONCLUSIVE — QUASI-DECONFINED WINDOW NOT EXCLUDED}.
}
]

The factor four is a conservative protocol convention motivated by the published CKT observation that asymptotic charge-one saturation became visible only on lattices about 3!-!4 times the inferred radius. It is not asserted to be universal.

---

13.4 Frozen FM geometry

For sizes divisible by four choose

[
r=L/4.
]

Use a square closed contour of side r.

The open numerator is an L-shaped half-contour formed by two adjacent sides joining opposite square corners.

Average:

- both complementary L paths;
- all three plane orientations;
- all translations.

No alternative contour family is introduced after target data are opened.

---

13.5 Frozen magnetic twist

Use the coclosed-stack interpolation of §7.13.

Freeze

[
\lambda

0,\frac1{16},\frac2{16},\ldots,1.
]

Use all 17 windows.

Replica exchange or equivalent extended-ensemble sampling may be used only if fixed before production.

---

13.6 Q2 verdict rule

No physical Q2 verdict rests on one statistic.

Evidence must be concordant among:

- the validated sector statistic;
- charge-one radius;
- FM;
- twist free energy.

Sector ambiguity, scale failure, or diagnostic disagreement gives

[
\boxed{\text{Q2 UNRESOLVED}}.
]

---

14. First-Order Package

At the finite-size equal-weight point define the barrier

[
\boxed{
\Delta F_L

\ln
\frac{
\sqrt{
P_{\max,1}P_{\max,2}
}
}{
P_{\min}
}.
}
]

For a first-order transition in three dimensions,

[
\Delta F_L

cL^2+c_0+\cdots.
]

The first-order lane fires only if:

1. a two-component mixture is preferred over a one-component description by
   [
   \Delta{\rm BIC}\ge10
   ]
   for at least the three largest sizes;
2. the lower 95% confidence bound on the L^2 barrier coefficient is positive;
3. either the peak separation extrapolates to nonzero latent heat or the susceptibility scales consistently with L^3.

Finite-size bimodality without growing barrier does not suffice.

---

Appendix A — Algorithm and Q2 Sector Validation Card

Appendix A is complete only when all fields below are filled and passed.

Item| Required
Direct action| Exact equation and normalization
Cosine dual derivation| Full derivation
Villain dual derivation| Full derivation
Current orientation convention| Explicit
Boundary convention| Explicit
Three global gauge holonomies| Explicit
Full-PBC parity/homology relation| Proven
Q2 retained-holonomy/seam ensemble| Proven
Relation to original Z| Proven
Relation to CKT axial gauge| Proven
Even-worm transition probabilities| Frozen
Odd-sector kernel| Frozen
Charge-six local move| Frozen
Charge-six worm| Frozen
Detailed balance| Demonstrated for every move
Sector reachability| Demonstrated
Ergodicity limitations| Declared
Small-volume enumeration| Passed
Direct/dual equality| Passed
Global membrane tunneling| Measured
Q2 sector round trips| Measured
Finite-h_6 source autocorrelation| Measured

Until every Q2-specific row passes,

[
\boxed{\text{Q2 remains sealed}.}
]

---

Appendix B — Parameter Card PC-0.3-RC1

B1. Calibration parameters

Rung| Model| Couplings| Sizes| Target
A0| Exact constraints| t=0,0.3,0.7; h_6=0,0.02| 2,3| Exact constraint agreement
A1| PBC homology| representative t| 2,3,4,6| Verify mod-two boundary relation
A2| Pure Z_2 gauge| J=0; t=0.638 to 0.646, step 0.001| 8,12,16,24,32,48,64| t_c=0.6419086649
A3| Pure cosine XY| trivial holonomy; J=0.450 to 0.458, step 0.001| 8,12,16,24,32,48,64,96,128| J_c=0.45416468
A4| CKT Villain| t=0.7; J=0.3305,0.3320,0.3330,0.3335,0.3340,0.3350,0.3360| 8,12,16,24,32,48,64| J_c=0.3335(3)
A5| CKT radius| t=0.7,J=0.336| 24,32,48,64,72,96,128,160,192| delayed C_1 saturation
A6| Cosine FO control| \kappa=0.7, J=0.496,0.500,0.504,0.508,0.512| 8,12,16,24,32,48,64| first-order package fires
A7| Cosine direct/dual| t=0.6640367703,0.7; h_6=0,0.02; J=0.45,0.46,0.47| 4,6,8,12,16| common observables agree
A8| AF Potts| around published T_c| 8,12,16,24,32,48,64,96,128| XY + emergent O(2) + Z_6 locking

---

B2. Stage-B production gauge points

P1

[
\boxed{
\kappa=0.8000000000
}
]

[
\boxed{
t=0.6640367703
}
]

Initial matter bracket:

[
J\in[0.440,0.490].
]

Expected neighborhood from the BPV normalization map:

[
J_c\sim0.458.
]

Sizes:

[
\boxed{
L=
8,12,16,24,32,48,64,96,128.
}
]

---

P2

[
\boxed{
\kappa=0.8673005277
}
]

so

[
\boxed{
t=0.7000000000.
}
]

Initial bracket:

[
J\in[0.440,0.490].
]

Sizes:

[
\boxed{
L=
8,12,16,24,32,48,64,96,128.
}
]

This point aligns the cosine study with the same gauge fugacity used in the CKT Villain controversy benchmark without laundering the Villain matter coupling into the cosine model.

---

P3

[
\boxed{
\kappa=1.0000000000
}
]

[
\boxed{
t=0.7615941560.
}
]

Initial bracket:

[
J\in[0.440,0.490].
]

Expected neighborhood:

[
J_c\sim0.45458.
]

Sizes:

[
\boxed{
L=
8,12,16,24,32,48,64,96,128.
}
]

BPV find continuous large-K transitions at K=0.8 and K=1, with the gauge-invariant bilinear showing spin-two scaling.

---

B3. Deterministic J-location algorithm

For every Stage-B gauge point:

Coarse scan

[
J

0.440,0.445,\ldots,0.490
]

on

[
L=12,16,24.
]

Bracket

Identify the first common R_\xi/U_4 transition bracket.

Bisection

Bisect mechanically until bracket width satisfies

[
\boxed{
\Delta J\le2\times10^{-4}.
}
]

Production center

Define the bracket midpoint as J_0.

Frozen production grid

[
\boxed{
J

J_0+0.0005m,
\qquad
m=-4,-3,\ldots,4.
}
]

No Q1 exponent, Q3 harmonic, or Q2 output is visible during this determination.

If reweighting fails its ESS/overlap criterion, add the nearest unused half-step required to bracket R_\xi^\star.

No discretionary placement is allowed.

---

B4. Stage-C anisotropy parameters

Primary Stage-C gauge points:

[
\boxed{P1,\ P2}.
]

P3 remains an h_6=0 Q1 replication point unless the resource card is expanded before execution freeze.

Primary fields

[
\boxed{
h_6=0,\ 0.01,\ 0.02.
}
]

Nonlinearity sentinel

[
\boxed{
h_6=0.04.
}
]

Sign controls

[
\boxed{
h_6=-0.01,-0.02
}
]

for

[
L\le48.
]

Positive-field sizes

[
\boxed{
L=
8,12,16,24,32,48,64,96.
}
]

Critical trajectory

For each L, tune to

[
\boxed{
R_\xi

R_\xi^\star(t,h_6=0).
}
]

If that trajectory cannot be followed smoothly at nonzero h_6, the failure is reported rather than repaired by redefining the target.

Ordered locking point

Use

[
\boxed{
J_{\rm lock}

1.02J_c(t,h_6).
}
]

Ordered sizes:

[
16,24,32,48,64,96.
]

---

B5. Conditional Q2 parameters

Inactive until Appendix A passes.

Primary gauge points:

[
P1,\ P2.
]

Ordered-side measurement point:

[
\boxed{
J_{\rm Q2}

1.01J_c(t,0).
}
]

Sizes:

[
\boxed{
L=
48,64,96,128,160,192.
}
]

Primary sector statistic:

[
f_{\rm odd}
]

in the validated sector ensemble.

Charge-one radius:

joint periodic-exponential C_1 fit.

FM geometry:

square side

[
L/4.
]

Twist:

17 interpolation windows.

Admissibility:

[
L_{\max}
\ge
4\xi_{\rm conf}^{95%,{\rm upper}}.
]

Failure to reach an admissible ratio is not a protocol failure.

It produces an unresolved Q2 result.

---

B6. Production precision targets

Blind calibration pilots are used to fix run lengths before production observables are opened.

Candidate acquisition targets:

[
\boxed{
{\rm SE}(R_\xi)\le0.002
}
]

[
\boxed{
{\rm SE}(U_4)\le0.002
}
]

[
\boxed{
\frac{{\rm SE}(\chi_2)}{\chi_2}
\le0.005
}
]

[
\boxed{
{\rm SE}(A_3^\Phi)
\le0.003.
}
]

For Q2, require a frozen minimum effective number of sector round trips in addition to nominal standard-error targets.

Failure to obtain adequate sector mixing forces

[
\boxed{\text{Q2 UNRESOLVED}}.
]

---

B7. Resource cap

The resource ceiling is not guessed from theory.

It is determined from calibration-only blind timing pilots.

Before execution hashing, freeze:

[
\boxed{
L_{\max}^{\rm direct}
}
]

[
\boxed{
L_{\max}^{\rm dual}
}
]

[
\boxed{
{\rm maximum\ wall/core\ budget}
}
]

and

[
\boxed{
{\rm maximum\ raw\ storage}.
}
]

After hashing, the ceiling cannot be raised because an asymptotic trend remains inconveniently unresolved.

Exhaustion of the budget is a valid reason for an unresolved result.

---

Appendix C — Immutable Output and Hash Procedure

Every stored block contains at least:

protocol_version
protocol_hash
fit_package_hash
parameter_card_hash
code_commit
compiler_hash
dependency_lock_hash
model_branch
boundary_condition
holonomy_sector
twist_sector
L
kappa
t
J
h6
chain_id
seed
macro_sweep
block_id
matter_energy
gauge_energy
anisotropy_energy
M_occupation
physical_plaquette_flux
chi2
G2_fractional_separations
Rxi
U4
RW
Mphi
A3Phi
H6
A3Phi_times_H6
n6
sector_counts
FM_numerator
FM_denominator
twist_lambda
acceptance_rates
worm_length_statistics
sector_round_trips
autocorrelation_diagnostics

Each data file receives SHA-256.

Create a lexicographically sorted manifest containing:

- filename;
- byte count;
- SHA-256;
- protocol hash;
- fit-package hash;
- parameter-card hash;
- code commit;
- compiler/dependency metadata.

The SHA-256 of the manifest is the immutable production root.

A post-freeze implementation bug requires:

1. new code commit;
2. new manifest root;
3. invalidation of affected production points;
4. complete rerun of affected points;
5. written erratum identifying whether the correction changed only implementation or also changed the frozen statistical ensemble.

No partial silent repair is permitted.

---

15. Decision Table

Observation| Required interpretation
Persistent coexistence with growing L^2 barrier| CONTINUOUS LANE FAILED — FIRST ORDER
Stable \chi_2\sim L^{0.52742} plus compatible G_2 dimension| Q1 SUPPORTED
Stable ordinary-vector \chi_2\sim L^{1.96182}| Q1 REJECTED — ORDINARY-VECTOR LANE SUPPORTED
Stable incompatible free exponent| Q1 REJECTED
Large drift / insufficient discrimination| Q1 UNRESOLVED
y_6<0, critical harmonic vanishes, ordered phase locks| Q3 IRRELEVANCE SUPPORTED
y_6\ge0 or stable nonzero critical asymptote| Q3 REJECTED
Anisotropy flow too slow to discriminate| Q3 UNRESOLVED
Q2 sector Appendix incomplete| Q2 GATE CLOSED
L_{\max}<4\xi_{\rm conf}^{95%,upper}| Q2 QUASI-DECONFINED / ASYMPTOTICALLY UNRESOLVED
Validated Q2 diagnostics concordantly support suppression| EVIDENCE FOR CONFINEMENT
Validated Q2 diagnostics concordantly support persistent charged sector| EVIDENCE FOR DECONFINEMENT
Q2 diagnostics disagree| Q2 UNRESOLVED
Finite-h_6 dual algorithm fails| DUAL h_6 BRANCH FAILED — NOT A THEORY FAILURE
Resource ceiling reached before discrimination| UNRESOLVED, NOT FAILED

---

16. Naming Rule

The phrase

[
\boxed{XY^*}
]

is not issued from the charge-two exponent alone.

If Q1 and Q3 succeed but Q2 remains unresolved, the allowed headline is:

«Charge-two O(2) critical scaling with irrelevant physical Z_3 anisotropy in a Z_2-gauged rotor, with asymptotic charge-one deconfinement unresolved.»

If Q1, Q3, and independently validated Q2 evidence all support fractional deconfinement, the allowed stronger language is:

«*Candidate XY^ criticality with charge-two physical order and irrelevant sixfold fine-field anisotropy.»

No asterisk by exponent alone.

---

17. Literature Roles

Xu & Balents, Phys. Rev. B 84, 014402 (2011).
Prior art for a composite physical order parameter V\sim\psi^2, sixth-order anisotropy, and an XY-critical mechanism.

Bonati, Pelissetto & Vicari, Phys. Rev. B 109, 235121 (2024).
Primary reference for the three-dimensional Z_2-gauge N-vector phase diagram, the N=2 large-gauge-coupling continuous transition, and distinct vector versus spin-two finite-size scaling.

Bonati, Pelissetto & Vicari, Phys. Rev. B 110, 125109 (2024).
Stochastic gauge-fixing analysis of gauge-dependent critical vector correlations.

Coleman, Kuklov & Tsvelik, Phys. Rev. Lett. 134, 236001 (2025).
Dual current/membrane formulation, Villain benchmark J_c=0.3335(3), large confinement-radius argument, and finite-size confinement interpretation.

Zhang, Ding, Deng & Zhang (2022).
Simple-cubic antiferromagnetic three-state Potts control, emergent bulk O(2), and Z_6 ordered structure.

Fradkin & Shenker (1979).
Gauge-Higgs continuity and the warning against naive Wilson-loop discrimination with fundamental matter.

Fredenhagen–Marcu / subsequent open-Wilson-line literature.
Secondary diagnostic for distinguishing deconfined charged sectors from confinement/Higgs behavior when ordinary Wilson loops are screened.

---

18. Frozen Strategic Result

Protocol v0.3-RC1 is designed to answer three separable questions:

[
\boxed{
Q1:
\text{Does }\Phi=z^2
\text{ show spin-two }O(2)\text{ critical scaling?}
}
]

[
\boxed{
Q2:
\text{Does the charge-one sector remain asymptotically deconfined?}
}
]

[
\boxed{
Q3:
\text{Does the physical }Z_3
\text{ anisotropy flow to zero at critical scales?}
}
]

The primary publishable target is

[
\boxed{
\text{charge-two }O(2)\text{ scaling}
+
\text{irrelevant physical }Z_3\text{ anisotropy}.
}
]

Q2 remains independently witnessed.

The protocol is explicitly permitted to terminate with

[
\boxed{\text{Q2 UNRESOLVED}.}
]

That outcome is scientifically valid.

The remaining work before execution freeze is finite and explicit:

[
\boxed{
\text{Appendix A: construct and validate the Q2 global sector}
}
]

plus

[
\boxed{
\text{Appendix B: fill blind-pilot production lengths and resource ceiling}
}
]

followed by

[
\boxed{
\text{hash everything before target production.}
}
]

No asterisk by exponent alone.
No Wilson-loop shortcut.
No local source density masquerading as RG flow.
No Villain/cosine coefficient laundering.
No finite-size deconfinement claim without a defined global sector and admissible scale separation.
No moving the witnesses after the lattice speaks.

[
\boxed{\textbf{Freeze the witnesses first. Then let the lattice answer.}}
]



CC0 1.0 Universal

To the extent permitted by law, this work is dedicated to the public domain under CC0 1.0 Universal.

No permission required. Copy it, modify it, test it, redistribute it, build on it, or tear it apart.

No ownership claim. No attribution required. No warranty.

Use freely.
