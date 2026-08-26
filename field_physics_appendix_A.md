Appendix A

Exact Q2 Sector Construction, Axial-Seam Completion, and Algorithm Validation

Protocol: Simulation Protocol v0.3-RC1
Appendix status: Structural freeze candidate
Applies to: Q2 at h_6=0
Execution status: Q2 remains sealed until every mandatory validation test in §A.13 passes
Purpose: Define a mathematically complete finite-volume ensemble in which charge-one odd winding can be sampled, normalize that sector exactly, prove detailed balance and state-space reachability, validate it against a direct representation, and specify its relation to the axial implementation described by Coleman, Kuklov, and Tsvelik.

---

A.0. Executive Boundary

There are three distinct finite-volume objects.

A.0.1 Full periodic ensemble

The original physical partition function is

[
Z_{\rm PBC}

\sum_{{\sigma_\ell=\pm1}}
\int
\prod_i\frac{d\theta_i}{2\pi},
e^{-H[\theta,\sigma]},
]

with periodic boundary conditions in all three directions.

After every gauge link is summed, its dual current parity satisfies

[
I\bmod2=\partial M.
]

Consequently, the mod-two current homology is trivial on the three-torus. Odd global current winding is therefore projected out of the fully link-summed periodic dual ensemble.

That algebraic projection is not itself evidence for physical confinement. It means only that the full finite-volume gauge sum does not retain an independently variable charge-one winding sector.

A.0.2 Exact retained-seam axial representation

A periodic axial gauge may set all but one z-directed link per vertical column to +1, but it must retain the remaining seam or Polyakov-loop variable in each column.

The resulting retained-seam representation is exactly equivalent to Z_{\rm PBC}, including its normalization.

A.0.3 Flat axial sectors

A further restriction may set every retained axial seam variable to the same value

[
\eta=+1
\quad\text{or}\quad
\eta=-1.
]

The \eta=+1 branch is the literal periodic completion of the condition

[
\sigma_{i,z}=1
]

on every z-directed link.

It is the branch in which a charge-one current worm can move along z without violating a link-parity projector.

The flat axial branches are mathematically valid positive-weight direct ensembles, but they are conditioned sectors, not the full periodic partition function.

Accordingly, the Q2 winding observable defined here is named

[
\boxed{
f_{\rm odd}^{\rm ax}(L)
}
]

and is reported as the:

«axial-conditioned odd-winding weight.»

It is not called a gauge-independent deconfinement probability.

No physical Q2 verdict may rest on it alone.

---

A.1. Lattice, Orientation, and Winding Conventions

Use a cubic lattice

[
\Lambda_L=(\mathbb Z/L\mathbb Z)^3
]

with sites

[
\mathbf x=(x,y,z),
\qquad
x,y,z\in{0,\ldots,L-1}.
]

Each positively oriented link is denoted

[
\ell=(\mathbf x,\mu),
\qquad
\mu\in{x,y,z}.
]

Integer currents satisfy

[
I_{\mathbf x,\mu}

-I_{\mathbf x+\hat\mu,-\mu}.
]

The lattice divergence is

[
(\nabla\cdot I)_{\mathbf x}

\sum_\mu
\left(
I_{\mathbf x,\mu}

I_{\mathbf x-\hat\mu,\mu}
\right).
]

At

[
h_6=0,
]

the current is exactly conserved:

[
\boxed{
\nabla\cdot I=0.
}
]

For a conserved current, define the flux through the z-cut at fixed z_0,

[
Q_z(z_0)

\sum_{x,y}
I_{(x,y,z_0),z}.
]

Current conservation implies that Q_z(z_0) is independent of z_0.

The integer winding is therefore

[
\boxed{
W_z

Q_z(z_0)

\frac1L
\sum_{\ell\parallel z}I_\ell.
}
]

A single current loop wrapping once around the periodic z direction contributes

[
W_z=\pm1.
]

The corresponding stiffness convention is

[
\rho_z

\frac{\langle W_z^2\rangle}{L},
]

and the dimensionless winding observable is

[
R_W

\langle W_z^2\rangle.
]

This is the winding normalization stated by CKT.

---

A.2. Why the Fully Summed Periodic Dual Has No Odd Mod-Two Winding

At h_6=0, the full dual partition function has the form

[
Z_{\rm full}^{\rm dual}

C
\sum_{{M,I}}
t^{\sum_pM_p}
\prod_\ell w_J(I_\ell)
\prod_i
\delta_{\mathbb Z}
!\left[
(\nabla\cdot I)i
\right]
\prod\ell
\delta_{\mathbb Z_2}
!\left[
I_\ell+M_\ell
\right],
]

where

[
M_\ell

\sum_{p\supset\ell}M_p
]

and

[
w_J(I)

\begin{cases}
\mathcal I_{|I|}(J), & \text{cosine model},\[4pt]
e^{-I^2/(2J)}, & \text{Villain model}.
\end{cases}
]

Let

[
j_\ell=I_\ell\bmod2.
]

Treat the occupied plaquettes M_p=1 as a two-chain

[
M\in C_2(\Lambda_L,\mathbb Z_2).
]

Its boundary is the link chain

[
(\partial M)\ell=M\ell\bmod2.
]

The link projector gives

[
\boxed{
j=\partial M.
}
]

Therefore

[
[j]=0
\quad\text{in}\quad
H_1(T^3,\mathbb Z_2).
]

For any noncontractible cut \Sigma_\alpha,

[
\sum_{\ell\perp\Sigma_\alpha}I_\ell

0
\pmod2.
]

Equivalently,

[
\boxed{
W_\alpha=0\pmod2
}
]

in the fully link-summed periodic dual.

CKT write the full link-parity projector in their Villain Eq. 12 and subsequently introduce odd-current updates along one axis only after imposing an axial condition on the corresponding gauge links. Those are not automatically the same finite-volume ensemble unless the axial boundary and seam variables are specified.

Accordingly:

[
\boxed{
f_{\rm odd}^{\rm full}=0
}
]

is an algebraic property of the fully projected dual representation.

It is not used as a Q2 confinement verdict.

---

A.3. Exact Periodic Axial Gauge with Retained Seams

Choose the z direction as the Q2 measurement direction.

For every vertical column (x,y), define its gauge-invariant Polyakov sign

[
\boxed{
\eta_{xy}

\prod_{z=0}^{L-1}
\sigma_{(x,y,z),z}.
}
]

Perform a gauge transformation that sets

[
\sigma_{(x,y,z),z}=+1,
\qquad
z=0,\ldots,L-2.
]

The remaining seam link is

[
\sigma_{(x,y,L-1),z}

\eta_{xy}.
]

Thus the periodic axial representation contains an L^2-component seam field

[
\boldsymbol\eta

{\eta_{xy}},
\qquad
\eta_{xy}=\pm1.
]

A.3.1 Explicit gauge transformation

For each column, set

[
s_{xy,0}=1
]

and recursively define

[
s_{xy,z+1}

s_{xy,z},
\sigma_{(x,y,z),z},
\qquad
z=0,\ldots,L-2.
]

Then

[
s_{xy,z}
\sigma_{(x,y,z),z}
s_{xy,z+1}

1
]

for every nonseam z-link.

The transformed seam link is

[
s_{xy,L-1}
\sigma_{(x,y,L-1),z}
s_{xy,0}

\eta_{xy}.
]

The procedure is deterministic after fixing s_{xy,0}=1 for every column.

A.3.2 Exact partition-function decomposition

Let

[
Z_{\rm ax}[\boldsymbol\eta]
]

be the direct partition function with

[
\sigma_z(x,y,z)=1,
\qquad
z=0,\ldots,L-2,
]

and

[
\sigma_z(x,y,L-1)=\eta_{xy},
]

while every transverse x- and y-directed gauge link remains dynamical.

There are

[
L^2(L-1)=L^3-L^2
]

gauge links fixed by the axial transformation.

Therefore

[
\boxed{
Z_{\rm PBC}

2^{L^3-L^2}
\sum_{\boldsymbol\eta\in{\pm1}^{L^2}}
Z_{\rm ax}[\boldsymbol\eta].
}
]

The overall factor is independent of J, \kappa, and all observables.

This equation is the exact finite-volume completion of the axial gauge.

The retained seam variables may not be silently deleted.

A standard maximal-tree gauge is a complete lattice gauge fixing, while an axial gauge on a periodic lattice requires explicit treatment of boundary constraints and residual links. BPV emphasize precisely this boundary qualification.

A.3.3 Residual column gauge symmetry

The retained-seam axial representation is preserved by transformations

[
s_{x,y,z}=g_{xy},
\qquad
g_{xy}=\pm1,
]

that are constant along each vertical column.

The residual transformation acts on all matter variables in the column as

[
z_{x,y,z}\rightarrow g_{xy}z_{x,y,z}.
]

It also transforms the transverse links connecting neighboring columns.

Consequently, an axial charge-one correlator can be nonzero without an explicit transporter only when both endpoints lie on the same vertical column.

This is the residual symmetry noted in the CKT axial implementation. Their C_1(z) is restricted to equal x,y, whereas C_2 is gauge invariant and is not subject to that restriction.

---

A.4. Flat Axial Holonomy Sectors

Define two uniform seam configurations:

[
\eta_{xy}=+1
\quad
\forall(x,y),
]

and

[
\eta_{xy}=-1
\quad
\forall(x,y).
]

Their partition functions are

[
\boxed{
Z_{\rm ax}^{+}

Z_{\rm ax}[\eta_{xy}\equiv+1],
}
]

[
\boxed{
Z_{\rm ax}^{-}

Z_{\rm ax}[\eta_{xy}\equiv-1].
}
]

A.4.1 Periodic flat sector

In Z_{\rm ax}^{+},

[
\sigma_{(x,y,z),z}=+1
]

on every z-directed link.

This is the literal periodic realization of the axial condition described by CKT.

A.4.2 Antiperiodic flat sector

In Z_{\rm ax}^{-},

[
\sigma_{(x,y,z),z}=+1
]

for

[
z=0,\ldots,L-2,
]

and

[
\sigma_{(x,y,L-1),z}=-1
]

for every (x,y).

Every plaquette contains either zero or two links belonging to this uniform negative seam. Therefore all plaquette fluxes are unchanged.

The minus branch is a flat global Z_2 twist of the matter boundary condition in the z direction.

Both Z_{\rm ax}^{+} and Z_{\rm ax}^{-} have positive direct Boltzmann weights.

A.4.3 Conditioning boundary

Neither flat branch equals Z_{\rm PBC}.

Instead,

[
Z_{\rm ax}^{+}
]

and

[
Z_{\rm ax}^{-}
]

are two terms among the

[
2^{L^2}
]

retained-seam sectors appearing in

[
Z_{\rm PBC}

2^{L^3-L^2}
\sum_{\boldsymbol\eta}
Z_{\rm ax}[\boldsymbol\eta].
]

No local or global observable measured in a flat branch is automatically identified with its full-PBC expectation.

Such equality may occur asymptotically for some local gauge-invariant observables, but it is not assumed.

---

A.5. Dual Form of the Retained-Seam Axial Ensemble

Expand the matter and plaquette weights exactly as in the main protocol.

Only the transverse x- and y-directed gauge links are summed.

Consequently, the link-parity projector is imposed only on those transverse links.

For a general retained seam \boldsymbol\eta,

[
\boxed{
\begin{aligned}
Z_{\rm ax}[\boldsymbol\eta]

C_{\rm ax}
\sum_{{M,I}}
&;
t^{\sum_pM_p}
\prod_\ell w_J(I_\ell)
\prod_i
\delta_{\mathbb Z}
!\left[
(\nabla\cdot I)i
\right]
\
&\times
\prod{\ell\parallel x,y}
\delta_{\mathbb Z_2}
!\left[
I_\ell+M_\ell
\right]
\prod_{x,y}
\eta_{xy}^{
I_{(x,y,L-1),z}
+
M_{(x,y,L-1),z}
}.
\end{aligned}
}
]

There is no parity projector on z-directed links because those gauge links were not summed.

This is the exact mathematical reason that charge-one current updates are permitted along z in the axial branch.

---

A.6. Uniform Seam and the Odd-Winding Normalization

For a uniform seam

[
\eta_{xy}=\eta,
\qquad
\eta=\pm1,
]

the seam factor is

[
\eta^{
\sum_{x,y}
I_{(x,y,L-1),z}
+
\sum_{x,y}
M_{(x,y,L-1),z}
}.
]

Current conservation gives

[
\sum_{x,y}
I_{(x,y,L-1),z}

W_z.
]

The plaquette contribution is even:

[
\sum_{x,y}
M_{(x,y,L-1),z}

0
\pmod2.
]

One way to see this is to regard the uniform seam as a closed Z_2 one-cocycle a_z. Then

[
\langle a_z,\partial M\rangle

\langle da_z,M\rangle

0
\pmod2.
]

Therefore

[
\boxed{
Z_{\rm ax}^{\eta}

C_{\rm ax}
\sum_{{M,I}}
\pi_+(M,I),
\eta^{W_z},
}
]

where

[
\pi_+(M,I)

t^{\sum_pM_p}
\prod_\ell w_J(I_\ell)
\prod_i
\delta_{\mathbb Z}
[(\nabla\cdot I)i]
\prod{\ell\parallel x,y}
\delta_{\mathbb Z_2}
[I_\ell+M_\ell].
]

Define the positive sector sums

[
Z_{\rm even}

C_{\rm ax}
\sum_{\substack{{M,I}\W_z\ {\rm even}}}
\pi_+(M,I),
]

[
Z_{\rm odd}

C_{\rm ax}
\sum_{\substack{{M,I}\W_z\ {\rm odd}}}
\pi_+(M,I).
]

Then

[
\boxed{
Z_{\rm ax}^{+}

Z_{\rm even}+Z_{\rm odd},
}
]

and

[
\boxed{
Z_{\rm ax}^{-}

Z_{\rm even}-Z_{\rm odd}.
}
]

The normalized odd-winding weight in the positive axial branch is

[
\boxed{
f_{\rm odd}^{\rm ax}(L)

\frac{
Z_{\rm odd}
}{
Z_{\rm even}+Z_{\rm odd}
}.
}
]

It has the exact direct/dual identity

[
\boxed{
f_{\rm odd}^{\rm ax}(L)

\frac12
\left(
1-\frac{Z_{\rm ax}^{-}}{Z_{\rm ax}^{+}}
\right).
}
]

Equivalently, defining

[
r_{\rm odd}

\frac{Z_{\rm odd}}{Z_{\rm even}},
]

one has

[
f_{\rm odd}^{\rm ax}

\frac{r_{\rm odd}}{1+r_{\rm odd}},
]

and

[
\frac{Z_{\rm ax}^{-}}{Z_{\rm ax}^{+}}

\frac{1-r_{\rm odd}}{1+r_{\rm odd}}.
]

These identities supply:

- an exact normalization;
- a direct-representation estimator;
- a dual winding estimator;
- and a nontrivial direct/dual validation equation.

No asymptotic phase interpretation is built into them.

---

A.7. Interpretation Guard

The observable

[
f_{\rm odd}^{\rm ax}
]

answers the following finite-volume question:

«In the flat periodic axial sector Z_{\rm ax}^{+}, what fraction of the positive dual weight lies in configurations with odd integer winding W_z?»

It does not directly answer:

«What is the probability of odd winding in the fully gauge-summed periodic partition function?»

The latter is algebraically projected to zero.

It also does not by itself prove the existence or absence of an asymptotically free charge-one particle.

Accordingly:

[
\boxed{
f_{\rm odd}^{\rm ax}\neq
\text{standalone deconfinement order parameter}.
}
]

It is a Q2 witness that must be reported together with:

- the axial charge-one correlation radius;
- the properly defined Fredenhagen–Marcu ratio;
- the magnetic-twist free energy;
- and, where used, a separately defined stochastic-gauge charge-one correlator.

A Q2 physical verdict requires concordance.

---

A.8. Positive Dual Target Measure

Q2 production is performed at

[
h_6=0
]

in the positive flat axial sector

[
Z_{\rm ax}^{+}.
]

The normalized Monte Carlo target is

[
\boxed{
\Pi(M,I)

\frac1{Z_{\rm ax}^{+}}
t^{N_M}
\prod_\ell w_J(I_\ell)
\prod_i
\delta_{\mathbb Z}
[(\nabla\cdot I)i]
\prod{\ell\parallel x,y}
\Delta_\ell,
}
]

where

[
N_M=\sum_pM_p,
]

and

[
\Delta_\ell

\delta_{\mathbb Z_2}
[I_\ell+M_\ell].
]

All nonzero configurations have positive weight for

[
J>0,
\qquad
0<t\le1.
]

The Villain and cosine implementations differ only through w_J(I).

---

A.9. Detailed-Balance Kernels

Every production move must either use the explicit Metropolis ratios below or document an exactly equivalent heat-bath or rejection-free construction.

A.9.1 Move A1 — Cube surface toggle

Choose an elementary cube c uniformly.

Toggle the six plaquettes on its boundary:

[
M_p'

1-M_p,
\qquad
p\in\partial c.
]

No current changes.

Every cube edge belongs to two toggled plaquettes, so

[
M_\ell'=M_\ell
\pmod2.
]

All parity projectors remain satisfied.

Define

[
\Delta N_M

\sum_{p\in\partial c}
(1-2M_p).
]

The acceptance probability is

[
\boxed{
A_{\rm cube}

\min
\left(
1,
t^{\Delta N_M}
\right).
}
]

The proposal is its own inverse, so detailed balance follows immediately.

---

A.9.2 Move A2 — Coupled plaquette-current loop

Choose an oriented plaquette p uniformly and choose

[
s=\pm1
]

with equal probability.

Toggle

[
M_p'=1-M_p.
]

For each oriented boundary link \ell\in\partial p, define

[
\epsilon_{p\ell}

\begin{cases}
+1, & \ell\text{ agrees with the plaquette orientation},\
-1, & \ell\text{ opposes it}.
\end{cases}
]

Update

[
I_\ell'

I_\ell+s\epsilon_{p\ell}.
]

The added current is a closed elementary loop, so current conservation is preserved.

On every boundary link, both I_\ell\bmod2 and M_\ell\bmod2 flip. Thus every transverse parity projector remains satisfied.

The generic acceptance ratio is

[
\boxed{
R_{\rm plaq}

t^{1-2M_p}
\prod_{\ell\in\partial p}
\frac{
w_J(I_\ell+s\epsilon_{p\ell})
}{
w_J(I_\ell)
}.
}
]

Accept with

[
A_{\rm plaq}

\min(1,R_{\rm plaq}).
]

For the Villain branch,

[
\boxed{
R_{\rm plaq}^{\rm V}

t^{1-2M_p}
\exp
\left[
-\frac1{2J}
\sum_{\ell\in\partial p}
\left(
(I_\ell+s\epsilon_{p\ell})^2-I_\ell^2
\right)
\right].
}
]

For the cosine branch,

[
\boxed{
R_{\rm plaq}^{\cos}

t^{1-2M_p}
\prod_{\ell\in\partial p}
\frac{
\mathcal I_{|I_\ell+s\epsilon_{p\ell}|}(J)
}{
\mathcal I_{|I_\ell|}(J)
}.
}
]

The reverse proposal uses the same plaquette and -s, which has the same proposal probability.

---

A.9.3 Move A3 — Even closed-loop update

Choose a closed oriented path \gamma from a frozen path distribution satisfying

[
Q(\gamma)=Q(\gamma^{-1}).
]

Choose

[
s=\pm1
]

uniformly.

Propose

[
I_\ell'

I_\ell+2s\epsilon_{\gamma\ell}.
]

Because two is even, every parity projector is unchanged.

The generic ratio is

[
\boxed{
R_{2,\gamma}

\prod_{\ell\in\gamma}
\frac{
w_J(I_\ell+2s\epsilon_{\gamma\ell})
}{
w_J(I_\ell)
}.
}
]

Accept with

[
A_{2,\gamma}

\min(1,R_{2,\gamma}).
]

The path distribution must include:

- elementary contractible loops;
- deformable extended loops;
- and noncontractible loops in all three directions.

This move supplies a transparent correctness kernel against which the production even-worm implementation is tested.

---

A.9.4 Move A4 — Odd axial column loop

Choose a vertical column

[
(x_0,y_0)
]

uniformly and choose

[
s=\pm1
]

with equal probability.

Update every z-link on that column:

[
I_{(x_0,y_0,z),z}'

I_{(x_0,y_0,z),z}+s,
\qquad
z=0,\ldots,L-1.
]

This is a closed noncontractible loop.

It preserves current conservation.

No z-link parity projector exists in Z_{\rm ax}^{+}.

It changes

[
W_z\rightarrow W_z+s.
]

Therefore it connects even and odd winding sectors.

The acceptance ratio is

[
\boxed{
R_{\rm col}

\prod_{z=0}^{L-1}
\frac{
w_J(I_{(x_0,y_0,z),z}+s)
}{
w_J(I_{(x_0,y_0,z),z})
}.
}
]

For the Villain model,

[
\boxed{
R_{\rm col}^{\rm V}

\exp
\left[
-\frac1{2J}
\sum_{z=0}^{L-1}
\left(
(I_z+s)^2-I_z^2
\right)
\right].
}
]

For the cosine model,

[
\boxed{
R_{\rm col}^{\cos}

\prod_{z=0}^{L-1}
\frac{
\mathcal I_{|I_z+s|}(J)
}{
\mathcal I_{|I_z|}(J)
}.
}
]

Accept with

[
A_{\rm col}

\min(1,R_{\rm col}).
]

This move is mandatory even if a more efficient odd worm is also used. It is the reference sector-bridge move with manifest detailed balance.

---

A.9.5 Move A5 — Noncontractible membrane sheet

Choose a noncontractible plaquette sheet S_{\mu\nu} uniformly from the three orientations and all translations.

Toggle

[
M_p'=1-M_p,
\qquad
p\in S_{\mu\nu}.
]

Because the sheet is closed,

[
\partial S_{\mu\nu}=0.
]

Thus M_\ell\bmod2 is unchanged and no current update is required.

The ratio is

[
\boxed{
R_{\rm sheet}

t^{
\sum_{p\in S_{\mu\nu}}
(1-2M_p)
}.
}
]

Accept with

[
A_{\rm sheet}

\min(1,R_{\rm sheet}).
]

This move connects the distinct H_2(T^3,\mathbb Z_2) membrane sectors that cannot be connected by cube moves alone.

---

A.10. Extended Worm Detailed Balance

The production implementation may replace repeated closed-loop proposals with an extended-ensemble worm, provided it samples the same target measure.

A.10.1 Even worm

Introduce endpoint sites a,b with temporary divergence

[
(\nabla\cdot I)_i

2
\left(
\delta_{i,a}-\delta_{i,b}
\right).
]

The extended weight is

[
\Pi_2(M,I;a,b)
\propto
t^{N_M}
\prod_\ell w_J(I_\ell)
\prod_{\ell\parallel x,y}\Delta_\ell
\prod_i
\delta_{\mathbb Z}
\left[
(\nabla\cdot I)_i

2(\delta_{i,a}-\delta_{i,b})
\right].
]

A head step along an oriented link \ell changes

[
I_\ell\rightarrow I_\ell\pm2.
]

With symmetric nearest-neighbor proposals, the local acceptance is

[
\boxed{
A_{2,\ell}

\min
\left[
1,
\frac{
w_J(I_\ell')
}{
w_J(I_\ell)
}
\right].
}
]

If the forward and reverse neighbor probabilities differ, multiply the ratio by

[
\frac{q_{\rm reverse}}{q_{\rm forward}}.
]

The worm closes when a=b, returning to the physical ensemble.

A.10.2 Odd axial worm

Introduce charge-one endpoints on a common vertical column:

[
(\nabla\cdot I)_i

\delta_{i,a}-\delta_{i,b}.
]

The worm head is permitted to move only on z-directed links.

The local update is

[
I_\ell\rightarrow I_\ell\pm1.
]

Because no parity projector is imposed on z-links, the move remains valid.

With symmetric +\hat z/-\hat z proposals,

[
\boxed{
A_{1,\ell}

\min
\left[
1,
\frac{
w_J(I_\ell')
}{
w_J(I_\ell)
}
\right].
}
]

A worm that closes after wrapping the periodic direction changes W_z by an odd integer.

A worm that closes without wrapping changes only local current structure.

A.10.3 Worm insertion and removal

The endpoint-pair insertion probability, closure probability, and endpoint fugacity must be frozen before production.

If the extended ensemble assigns relative endpoint fugacity \lambda_q, every insertion, motion, and closure ratio must include the appropriate factor of \lambda_q.

The reference implementation uses symmetric insertion and closure probabilities and

[
\lambda_q=1.
]

Any alternative must provide its complete forward/reverse proposal ratio.

A.10.4 Correctness requirement

For every frozen L,J,t validation point, the production worm and the closed-loop reference kernels must agree for:

- P(W_z);
- f_{\rm odd}^{\rm ax};
- \langle W_z^2\rangle;
- current-density moments;
- plaquette occupation;
- and all common thermodynamic derivatives.

Failure is an algorithm failure.

---

A.11. Reachability and Ergodicity

The following reachability claim applies at

[
J>0,
\qquad
0<t<1,
\qquad
h_6=0.
]

It applies to configurations with nonzero target weight.

A.11.1 Local parity transformations

A coupled plaquette-current move adds the pair

[
(M,I)
\rightarrow
(M+p,\ I+\partial p)
]

modulo two.

Therefore arbitrary local changes in the plaquette field and their required current-parity boundaries can be assembled from elementary plaquette moves.

A.11.2 Closed membrane sectors

If two plaquette configurations differ by a closed two-cycle, cube moves generate the contractible part and noncontractible sheet moves generate the three toroidal homology components.

Thus every Z_2 plaquette-homology class is reachable.

A.11.3 Integer-current amplitudes

After two configurations have the same plaquette field and the same current parity, their current difference is even:

[
I'-I=2K.
]

It is also divergence free:

[
\nabla\cdot K=0.
]

Any divergence-free integer current on the periodic cubic lattice decomposes into:

- contractible plaquette curls;
- and three harmonic winding currents.

Even closed-loop moves or an even worm capable of periodic winding generate both parts.

A.11.4 Odd z-winding parity

The remaining distinction is the parity of W_z.

The odd axial column-loop move changes

[
W_z\rightarrow W_z\pm1.
]

Therefore it connects the even and odd winding classes.

A.11.5 Combined result

The move set

[
\boxed{
{
\text{cube},
\text{coupled plaquette-current},
\text{even worm},
\text{odd axial loop/worm},
\text{noncontractible sheet}
}
}
]

is state-space connecting on the positive support of Z_{\rm ax}^{+}.

This is a reachability statement, not an efficiency claim.

Production admissibility additionally requires observed tunneling.

A.11.6 Endpoint cases

At

[
J=0,
]

only

[
I_\ell=0
]

has nonzero matter-current weight, so

[
f_{\rm odd}^{\rm ax}=0.
]

At

[
t=0,
]

only

[
M_p=0
]

contributes.

Unlike the fully projected periodic dual, the axial-conditioned branch may still contain a noncontractible odd z-current loop when J>0, because no z-link parity projector is present.

Therefore the old rule

[
t=0\Rightarrow f_{\rm odd}=0
]

remains a hard test of the full link-summed dual, but it is not a valid hard test of Z_{\rm ax}^{+}.

This distinction must appear in the calibration report.

A.11.7 Empirical tunneling requirement

For every Q2 production point, each independent chain must show at least

[
100
]

effective round trips

[
W_z\ {\rm even}
\rightarrow
W_z\ {\rm odd}
\rightarrow
W_z\ {\rm even}
]

after thermalization.

A round trip is counted only after separation by at least one frozen sector autocorrelation time.

If this criterion fails:

[
\boxed{
\text{Q2 UNRESOLVED — SECTOR MIXING INADEQUATE}.
}
]

Increasing the production length after examining the direction of the Q2 result is prohibited.

---

A.12. Direct Representation of the Flat Axial Sectors

A.12.1 Direct positive-sector action

For \eta=\pm1, define fixed axial links

[
\sigma_{(x,y,z),z}^{(\eta)}

\begin{cases}
+1, & z=0,\ldots,L-2,\
\eta, & z=L-1.
\end{cases}
]

The transverse links remain dynamical.

The direct action is

[
\boxed{
\begin{aligned}
H_{\rm ax}^{(\eta)}
=&
-J
\sum_{\ell\parallel x,y}
\sigma_\ell
\cos(\Delta_\ell\theta)
\
&-
J
\sum_{\substack{\ell\parallel z\z<L-1}}
\cos(\Delta_\ell\theta)

J\eta
\sum_{x,y}
\cos
\left[
\theta_{x,y,0}

\theta_{x,y,L-1}
\right]
\
&-
\kappa
\sum_pB_p.
\end{aligned}
}
]

The uniform negative seam leaves every plaquette flux term unchanged.

A.12.2 Direct Monte Carlo kernel

One direct compound sweep contains:

1. one rotor Metropolis proposal per site;
2. five rotor over-relaxation proposals per site;
3. one link-flip proposal per transverse x- or y-directed link;
4. no proposal on fixed axial links.

Every proposal is accepted with

[
A=\min(1,e^{-\Delta H}).
]

This satisfies detailed balance with respect to

[
Z_{\rm ax}^{\eta}.
]

The transverse link variables are independently flippable, so their finite state space is connected.

Continuous rotor proposals with nonzero proposal density on an interval connect the rotor configuration space.

A.12.3 Direct seam-ratio estimator

Introduce an interpolation

[
H_\lambda

H_{\rm bulk}

J(1-2\lambda)
\sum_{x,y}
\cos
\left[
\theta_{x,y,0}

\theta_{x,y,L-1}
\right],
]

with

[
0\le\lambda\le1.
]

Then

[
H_{\lambda=0}=H_{\rm ax}^{(+)},
]

and

[
H_{\lambda=1}=H_{\rm ax}^{(-)}.
]

Since

[
\frac{\partial H_\lambda}{\partial\lambda}

2J
\sum_{x,y}
\cos
\left[
\theta_{x,y,0}

\theta_{x,y,L-1}
\right],
]

thermodynamic integration gives

[
\boxed{
\ln
\frac{
Z_{\rm ax}^{-}
}{
Z_{\rm ax}^{+}
}

-2J
\int_0^1d\lambda,
\left\langle
\sum_{x,y}
\cos
\left[
\theta_{x,y,0}

\theta_{x,y,L-1}
\right]
\right\rangle_\lambda.
}
]

Use the 17 frozen windows

[
\lambda

0,\frac1{16},\ldots,1.
]

Replica exchange between neighboring windows is permitted if frozen before production.

The resulting ratio supplies the independent direct estimator

[
\boxed{
f_{\rm odd,direct}^{\rm ax}

\frac12
\left(
1-
e^{
\ln Z_{\rm ax}^{-}

\ln Z_{\rm ax}^{+}
}
\right).
}
]

The direct and dual estimators must agree before Q2 opens.

---

A.13. Direct/Dual Small-Volume Agreement

Validation is performed in layers.

A.13.1 Gauge-fixing identity test

For

[
L=2,3,
]

enumerate gauge transformations or exhaustively test randomly selected gauge configurations.

For every configuration:

1. perform the deterministic axial transformation of §A.3;
2. verify that every nonseam z-link becomes +1;
3. verify that each seam variable equals the original column Polyakov product;
4. verify that every plaquette flux is unchanged;
5. verify that every gauge-invariant matter bond is unchanged;
6. verify that the reconstruction returns the original configuration up to a gauge transformation.

The number of preimages of every retained-seam configuration must equal

[
\boxed{
2^{L^3-L^2}.
}
]

This is an exact integer test.

A.13.2 Full retained-seam equivalence

Run:

- the ordinary ungauge-fixed direct PBC model;
- and the retained-seam axial direct model in which all \eta_{xy} remain dynamical.

Compare gauge-invariant observables:

- matter energy;
- plaquette flux;
- \chi_2;
- G_2(r);
- R_\xi;
- Binder ratio;
- and energy histograms.

The two implementations must agree because

[
Z_{\rm PBC}

2^{L^3-L^2}
\sum_{\boldsymbol\eta}
Z_{\rm ax}[\boldsymbol\eta].
]

A.13.3 Flat-positive direct/dual agreement

Run both:

- direct Z_{\rm ax}^{+};
- dual Z_{\rm ax}^{+}.

Required common observables are:

Matter derivative

For the exact cosine dual,

[
\frac{\partial\ln Z}{\partial J}

\sum_\ell
\left\langle
\frac{
\mathcal I_{|I_\ell|}'(J)
}{
\mathcal I_{|I_\ell|}(J)
}
\right\rangle_{\rm dual}.
]

Compare with the direct matter-bond expectation.

For the Villain model, include the complete Villain normalization before comparing J-derivatives.

Plaquette derivative

Compare the direct plaquette flux with

[
\boxed{
\langle B_p\rangle

t+
\frac{1-t^2}{t}
m_M,
}
]

where

[
m_M

\frac1{N_p}
\left\langle
\sum_pM_p
\right\rangle.
]

Physical correlators

Compare:

[
G_2(r),
\qquad
\chi_2,
\qquad
R_\xi.
]

Winding response

Compare dual

[
\langle W_z^2\rangle
]

with the correctly normalized direct helicity response to a continuous z-direction matter twist within the same axial sector.

A.13.4 Odd-sector normalization identity

Measure directly:

[
\frac{Z_{\rm ax}^{-}}{Z_{\rm ax}^{+}}
]

using the interpolation in §A.12.

Measure dually:

[
f_{\rm odd}^{\rm ax}

P(W_z\ {\rm odd}).
]

Require

[
\boxed{
1-2f_{\rm odd}^{\rm ax}

\frac{Z_{\rm ax}^{-}}{Z_{\rm ax}^{+}}
}
]

within the frozen uncertainty tolerance.

This is the decisive sector-normalization test.

A.13.5 Reference parameter set

The mandatory small-volume grid is

[
L\in{2,3,4,6,8},
]

[
t\in{0,0.3,0.7},
]

and representative matter couplings spanning weak, critical-neighborhood, and ordered behavior.

At minimum use

[
J\in{0.20,0.336,0.46},
]

with the understanding that the Villain value 0.336 is a calibration point only for the Villain branch.

A.13.6 Frozen numerical tolerance

For stochastic comparisons:

- every common observable must agree within combined 3\sigma;
- no observable may disagree by more than combined 4\sigma;
- the normalized sector identity must agree to relative precision
  [
  5\times10^{-3}
  ]
  or better when the ratio is not exponentially small;
- exact integer, parity, divergence, and gauge-fixing tests must pass with zero violations.

One isolated 3\sigma fluctuation may be rerun under a frozen replication rule.

A reproducible disagreement is a hard failure.

---

A.14. Relation to the CKT Axial Implementation

CKT first write a fully gauge-link-summed Villain dual partition function with a parity projector on every link. They then describe two current-update classes:

1. even-current updates;
2. odd-current updates along the z direction only,

stating that the latter are allowed under the gauge condition

[
u_{ij}=1
]

on z-directed links.

The finite-volume distinction is now explicit.

A.14.1 CKT Eq. 12 lane

The fully summed expression corresponds to

[
Z_{\rm full}^{\rm dual}
]

and enforces a parity projector on every link.

In that ensemble,

[
W_z=0\pmod2.
]

A.14.2 CKT odd-update lane

The odd z-current update corresponds instead to an axial representation in which z-directed gauge links have not been summed.

The literal periodic completion of

[
u_z=1
]

on every axial link is

[
\boxed{
Z_{\rm ax}^{+}.
}
]

In this branch:

- no z-link parity projector appears;
- charge-one axial worms are allowed;
- C_1(z) is defined only within one column;
- and W_z may be odd.

A.14.3 Seam ambiguity

The published description does not specify whether a periodic axial seam was:

- retained and sampled;
- retained but fixed;
- or removed by imposing a flat boundary sector.

Therefore the protocol does not declare an exact equivalence between the published code and Z_{\rm ax}^{+} merely from prose.

Instead:

[
\boxed{
\text{CKT ensemble identity is a calibration target, not an assumption.}
}
]

The implementation must attempt to reproduce their Villain benchmark using the literal Z_{\rm ax}^{+} completion.

If it succeeds, the result is reported as agreement with the CKT axial branch.

If it fails while the full-dual calibration succeeds, the discrepancy is investigated as a boundary-sector or seam-convention difference.

A.14.4 Gauge dependence

CKT explicitly state that their charge-one correlator is evaluated in the axial gauge, whereas the charge-two correlator is gauge invariant.

BPV separately emphasize that:

- complete gauge fixing must preserve gauge-invariant expectations;
- axial gauge on a periodic lattice requires boundary constraints;
- and a hard axial gauge need not expose the same critical vector correlations as their stochastic gauge-fixing construction.

Accordingly, the following names are mandatory:

[
\boxed{
C_1^{\rm ax}(z)
}
]

for the axial charge-one correlator, and

[
\boxed{
f_{\rm odd}^{\rm ax}(L)
}
]

for the axial-conditioned odd-winding weight.

They may not be renamed as gauge-independent observables.

---

A.15. CKT Replication Requirements

At

[
t=0.7,
\qquad
J=0.336
]

in the Villain branch, run the literal flat-positive axial ensemble

[
Z_{\rm ax}^{+}.
]

Required outputs:

1. stiffness near the published scale;
2. C_2 long-range behavior;
3. C_1^{\rm ax}(z);
4. \widetilde R_1 and \widetilde R_2;
5. P(W_z);
6. f_{\rm odd}^{\rm ax}(L);
7. odd-sector round trips;
8. sector-normalization comparison with Z_{\rm ax}^{-}/Z_{\rm ax}^{+}.

CKT report simulations in an axial gauge, a critical point

[
J_c=0.3335(3)
]

at t=0.7, stiffness near 0.038 at J=0.336, and delayed saturation of the charge-one radius on lattices above approximately L=90.

The replication report must distinguish:

- reproduced published numerical behavior;
- reproduced ensemble definition;
- and inferred ensemble equivalence.

These are separate claims.

---

A.16. Directional and Cubic-Symmetry Cross-Checks

The complete construction is repeated with measurement axes

[
\alpha=x,y,z.
]

For each direction, define:

[
Z_{{\rm ax},\alpha}^{+},
\qquad
Z_{{\rm ax},\alpha}^{-},
\qquad
W_\alpha,
\qquad
f_{{\rm odd},\alpha}^{\rm ax}.
]

Before averaging directions, verify that

[
f_{{\rm odd},x}^{\rm ax},
\quad
f_{{\rm odd},y}^{\rm ax},
\quad
f_{{\rm odd},z}^{\rm ax}
]

agree within frozen uncertainties.

A reproducible directional discrepancy is treated as:

- a code error;
- an anisotropic boundary implementation;
- or a failure of equilibration.

It may not be averaged away.

After validation, use

[
\boxed{
f_{\rm odd}^{\rm ax}

\frac13
\sum_{\alpha=x,y,z}
f_{{\rm odd},\alpha}^{\rm ax}.
}
]

The CKT literature-comparison branch remains z-directed to match their convention.

---

A.17. Production Macro-Sweep

One dual axial macro-sweep contains:

1. L^3 cube attempts;
2. 3L^3 coupled plaquette-current attempts;
3. completed even worms until their cumulative path length is at least
   [
   3L^3;
   ]
4. one odd axial worm;
5. one explicit odd column-loop proposal;
6. one noncontractible membrane-sheet proposal in each orientation.

Measurements occur only after complete macro-sweeps.

Record:

- W_x,W_y,W_z;
- winding parity;
- sector transition count;
- even and odd worm lengths;
- worm closure rate;
- column-loop acceptance;
- sheet acceptance;
- current density;
- plaquette occupation;
- and every observable listed in the immutable output card.

Proposal frequencies may be tuned during blind calibration only.

They are frozen before Q2 production.

---

A.18. Q2 Admissibility and Verdict Boundary

The axial sector passes its algorithmic gate only if:

1. all exact constraint tests pass;
2. the retained-seam decomposition is verified;
3. full direct PBC agrees with retained-seam direct PBC;
4. direct and dual Z_{\rm ax}^{+} agree;
5. the seam-ratio identity
   [
   1-2f_{\rm odd}^{\rm ax}
   Z_{\rm ax}^{-}/Z_{\rm ax}^{+}
   ]
   passes;
6. sector reachability is demonstrated;
7. sector round-trip requirements pass;
8. the three lattice directions agree;
9. the CKT Villain calibration is reproduced or its discrepancy is explained.

Passing these tests permits the protocol to report

[
f_{\rm odd}^{\rm ax}(L)
]

as a valid finite-volume sector statistic.

It does not, by itself, permit an asymptotic Q2 verdict.

A physical Q2 statement additionally requires:

- the frozen confinement-radius estimator;
- the scale condition
  [
  L_{\max}
  \ge
  4\xi_{\rm conf}^{95%,{\rm upper}};
  ]
- a correctly normalized FM measurement;
- a calibrated magnetic twist;
- and concordance among the witnesses.

If those requirements fail:

[
\boxed{
\text{Q2 UNRESOLVED}.
}
]

---

A.19. Mandatory Reporting Language

The following language is permitted:

«The axial-conditioned current ensemble exhibits a decreasing, persistent, or unresolved odd-winding weight over the simulated size range.»

«The direct flat-seam ratio and the dual winding histogram agree within uncertainty.»

«The CKT axial-gauge charge-one radius saturates or does not saturate over the admissible size range.»

The following language is prohibited from this appendix alone:

«Odd winding proves asymptotic deconfinement.»

«Absence of odd winding proves confinement.»

«The axial-conditioned partition function is the full periodic gauge theory.»

«Gauge fixing removes the need to retain periodic seams.»

«The CKT axial implementation is exactly Eq. 12 without further boundary information.»

---

A.20. Appendix-A Freeze Card

Requirement| Freeze condition
Full-PBC parity proof| Included and unit tested
Retained seam \eta_{xy}| Explicit in code and data
Full partition decomposition| Verified
Flat + axial sector| Implemented
Flat - axial sector| Implemented
Odd-sector normalization| Verified through 1-2f=Z_-/Z_+
Cube detailed balance| Passed
Plaquette-current detailed balance| Passed
Even-worm detailed balance| Passed
Odd-worm detailed balance| Passed
Odd column-loop detailed balance| Passed
Membrane-sheet detailed balance| Passed
Current conservation| Zero violations
Transverse parity| Zero violations
Winding normalization| Unit tested
Sector reachability| Demonstrated
Sector round trips| Meets frozen minimum
Full direct / retained-seam direct| Agreement passed
Flat-positive direct / dual| Agreement passed
Three-direction check| Agreement passed
CKT relation| Explicitly labeled
CKT Villain benchmark| Reproduced or discrepancy resolved
Gauge-conditioned naming| Enforced in outputs
Q2 physical verdict guard| Enforced

Only after every row passes may the protocol status change from

[
\boxed{
\text{Q2 SECTOR GATE CLOSED}
}
]

to

[
\boxed{
\text{Q2 SECTOR VALIDATED — PHYSICAL VERDICT STILL CONDITIONAL}.
}
]

---

A.21. Frozen Result

The mathematically defined Q2 winding object is

[
\boxed{
\left(
Z_{\rm ax}^{+},
Z_{\rm ax}^{-},
Z_{\rm even},
Z_{\rm odd},
f_{\rm odd}^{\rm ax}
\right).
}
]

Its exact normalization is

[
\boxed{
f_{\rm odd}^{\rm ax}

\frac{Z_{\rm odd}}{Z_{\rm even}+Z_{\rm odd}}

\frac12
\left(
1-\frac{Z_{\rm ax}^{-}}{Z_{\rm ax}^{+}}
\right).
}
]

Its positive dual ensemble is obtained by:

- fixing the flat + axial seam;
- imposing current parity only on transverse links;
- conserving integer current;
- and explicitly sampling even and odd z-winding sectors.

Its relation to the full periodic model is

[
\boxed{
Z_{\rm PBC}

2^{L^3-L^2}
\sum_{\boldsymbol\eta}
Z_{\rm ax}[\boldsymbol\eta].
}
]

Its relation to the CKT implementation is:

[
\boxed{
Z_{\rm ax}^{+}

\text{the literal periodic flat-seam completion of }u_z=1,
}
]

subject to direct numerical confirmation of the unpublished seam convention.

The central boundary is therefore frozen:

[
\boxed{
\text{The axial sector is real, normalized, reachable, and testable.}
}
]

[
\boxed{
\text{It is not silently promoted into the full periodic ensemble.}
}
]

[
\boxed{
\text{Its odd winding is a Q2 witness, not a verdict by itself.}
}
]

Retain the seam. Normalize the sectors. Prove the moves. Cross the representations. Then—and only then—open Q2.