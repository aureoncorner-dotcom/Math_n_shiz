I. The field-theory mechanism

1. The discrete parent and the physical model are not the same object

The exact six-state Fibonacci recurrence and candidate geometry \(Q_4\times C_6\) remain real mathematics, but they do not uniquely determine a continuum gauge theory. The \(Z_2\)-gauged rotor is a deliberately chosen constructor, not something secretly read backward out of the recurrence. 

This was the first major firewall:

\[
\boxed{
\text{discrete source}
\neq
\text{continuum realization}
}
\]

unless an explicit constructor earns that identification.

2. The fine field carries a local \(Z_2\) redundancy

The fundamental field is

\[
z\sim -z,
\]

while the physical local order parameter is

\[
\boxed{\Phi=z^2.}
\]

That makes \(\Phi\) gauge invariant even though \(z\) itself is fractionalized. 

3. The operator audit forces the first phase anisotropy to degree six

For an onsite monomial

\[
z^p z^{*q},
\]

local \(Z_2\) gauge invariance requires

\[
p+q\equiv0\pmod2,
\]

while the physical global \(Z_3\) symmetry requires

\[
p-q\equiv0\pmod3.
\]

Together they imply

\[
\boxed{p-q\equiv0\pmod6.}
\]

Therefore no pure phase anisotropy of degree \(2,3,4,\) or \(5\) survives. The first permitted phase-selecting operator is

\[
\boxed{z^6+z^{*6}.}
\]



4. The physical cubic becomes sixth order upstairs

The ordinary physical \(Z_3\) invariant

\[
\Phi^3+\Phi^{*3}
\]

becomes

\[
\boxed{
\Phi^3+\Phi^{*3}
=
z^6+z^{*6}
}
\]

because \(\Phi=z^2\). 

So the physical field still sees threefold locking, while the critical fine field sees a sixth-order perturbation.

5. The number six is earned by symmetry, not numerology

The six is the least common compatible phase degree:

\[
\boxed{\operatorname{lcm}(2,3)=6.}
\]

It is not inserted merely because a six-cycle appeared upstream. 

6. The physical field has a sharply identifiable charge-two scaling target

For the candidate charge-two \(O(2)\) lane,

\[
\boxed{\Delta_2=1.23629(11)}.
\]

This gives

\[
G_2(r)\sim r^{-2.47258},
\]

\[
\eta_\Phi\simeq1.47258,
\]

\[
\beta_\Phi\simeq0.83048,
\]

and

\[
\boxed{\chi_2(L)\sim L^{0.52742}.}
\]



7. Ordinary-vector \(XY\) behavior is dramatically different

If the physical field behaves as the ordinary \(O(2)\) vector instead of the charge-two operator, its susceptibility grows approximately as

\[
\boxed{\chi_\Phi(L)\sim L^{1.9618}.}
\]

That is so far from \(L^{0.52742}\) that the protocol can explicitly discriminate the two hypotheses rather than merely ask whether an exponent looks “sort of XY.” 

8. The \(XY^*\) claim is explicitly conditional

The clean lane requires:

\[
\text{deconfined gauge sector}
+
\text{gapped visons}
+
\text{critical }z
+
\text{irrelevant }z^6
+
\Phi=z^2.
\]

Without those conditions, the charge-two exponent alone does not earn the asterisk. 

9. Simultaneous vison criticality creates a separate lane

If the matter and vison sectors become critical together, the naive decoupled candidate

\[
XY\times\mathrm{Ising}
\]

has a weakly relevant energy–energy coupling,

\[
\boxed{y_w\simeq0.076>0.}
\]

So the decoupled fixed point is weakly unstable. The surviving possibilities include:

\[
\text{new coupled fixed point},
\qquad
\text{split transitions},
\qquad
\text{first-order runaway}.
\]




---

II. The simulation architecture

10. One fused question became three independent questions

The protocol now asks:

\[
\boxed{Q1:\text{ What is the physical charge sector?}}
\]

\[
\boxed{Q2:\text{ Is charge one asymptotically deconfined?}}
\]

\[
\boxed{Q3:\text{ Is the physical }Z_3\text{ anisotropy irrelevant?}}
\]

A “yes” to one cannot silently answer the others. 

11. No asterisk by exponent alone

Even perfect charge-two scaling does not prove deconfinement. The protocol can validly finish with:

\[
\boxed{
\text{charge-two }O(2)\text{ scaling}
+
\text{irrelevant anisotropy}
+
\text{Q2 unresolved}.
}
\]

That is still publishable and scientifically meaningful.

12. Cosine and Villain models are separate microscopic realizations

The cosine model is the intended production rotor. The Villain model is retained primarily for reproducing CKT benchmarks.

They may share universal behavior, but their nonuniversal critical couplings cannot be laundered from one into the other. 

13. The model has an exact current–membrane dual description

The dual variables are:

\[
M_p\in\{0,1\}
\]

for plaquette membranes,

\[
I_\ell\in\mathbb Z
\]

for oriented integer currents, and

\[
n_i\in\mathbb Z
\]

for charge-six source variables.

The dual weight combines current amplitudes, membrane fugacity, divergence constraints, and mod-two link parity. 

14. Finite \(h_6\) makes integer currents “leaky” only in units of six

At nonzero anisotropy,

\[
\boxed{
(\nabla\!\cdot I)_i=-6n_i.
}
\]

Currents may begin or terminate only in multiples of six. On a periodic lattice the total source remains neutral:

\[
\boxed{\sum_i n_i=0.}
\]



15. Charge-six leakage does not destroy mod-two current conservation

Because six is even,

\[
6n_i\equiv0\pmod2,
\]

so

\[
\boxed{\nabla\!\cdot I\equiv0\pmod2.}
\]

The integer-loop picture becomes leaky, but the parity-loop structure survives. 

16. Local source density is not an RG flow parameter

The dual source density

\[
n_6=\frac1N\left\langle\sum_i|n_i|\right\rangle
\]

is useful for checking the finite-\(h_6\) algorithm, but it can carry a regular microscopic background. Therefore

\[
n_6\not\to0
\]

does not prove that the anisotropy is relevant. 

17. The winding normalization was corrected

The correct integer winding is

\[
\boxed{
W_\alpha
=
\frac1L
\sum_{\ell\parallel\alpha}I_\ell.
}
\]

A loop winding once contains \(L\) directed links and contributes \(W_\alpha=\pm1\). 

18. The stiffness itself is not the dimensionless crossing variable

The stiffness is

\[
\rho_\alpha
=
\frac{\langle W_\alpha^2\rangle}{L},
\]

while the dimensionless quantity is

\[
\boxed{
R_W=L\rho_\alpha=\langle W_\alpha^2\rangle.
}
\]



19. The original Wilson/vison/FM lane was repaired

Ordinary fundamental Wilson loops are not primary discriminators when dynamical charge-one matter screens flux.

The old expression

\[
G_1/\sqrt{G_2}
\]

was rejected as a fake Fredenhagen–Marcu observable. A real FM observable needs an open gauge transporter with matter endpoints and a geometrically matched closed contour. 

The old “flip a plane of links to insert a vison” idea was also reclassified: a plane-link flip can change global holonomy while leaving every plaquette flux unchanged. It is not automatically a magnetic-flux insertion.


---

III. The three-torus and Q2

20. The fully summed periodic dual projects away odd mod-two homology

This was the hard blocker that forced Appendix A.

In the completely link-summed periodic ensemble,

\[
\boxed{
Z_{\rm full}=\mathcal Z_{000}.
}
\]

The full periodic dual therefore contains only trivial mod-two current homology and cannot supply an independently fluctuating odd-winding statistic. 

That zero is an ensemble projection—not, by itself, evidence of confinement.

21. Q2 required a different, explicitly defined finite-volume ensemble

The protocol now separates:

\[
\boxed{Z_{\rm full}}
\]

for Q1, bulk thermodynamics, and \(h_6=0\) Q3 calibration, from

\[
\boxed{Z_{\rm FH}=Z_{000}}
\]

for Q2. 

22. The finite-volume geometry is genuinely \(T^3\)

The lattice is

\[
\Lambda_L=(\mathbb Z/L\mathbb Z)^3,
\]

with three frozen noncontractible cycles

\[
\Gamma_x,\Gamma_y,\Gamma_z
\]

and three dual cuts

\[
\Sigma_x,\Sigma_y,\Sigma_z.
\]

Their intersection pairing is

\[
\boxed{
\langle\Sigma_\alpha,\Gamma_\beta\rangle
=
\delta_{\alpha\beta}\pmod2.
}
\]



That is real toroidal topology, not merely donut imagery.

23. The direct model has eight global holonomy sectors

The three holonomy bits are

\[
h=(h_x,h_y,h_z)\in\mathbb Z_2^3.
\]

They define eight positive direct partition functions

\[
Z_h,
\]

with the primary Q2 ensemble

\[
\boxed{Z_{\rm FH}=Z_{000}.}
\]

The original periodic theory is recovered exactly by

\[
\boxed{
Z_{\rm full}
=
\sum_{h\in\mathbb Z_2^3}Z_h.
}
\]



24. The dual model has eight current-homology sectors

The matching dual label is

\[
q=(q_x,q_y,q_z)\in\mathbb Z_2^3.
\]

The parity constraint becomes

\[
\boxed{
\bar I+\partial M+\Gamma q=0.
}
\]



25. Holonomy and current homology are related by an exact character transform

The direct and dual sectors satisfy

\[
\boxed{
Z_h
=
\frac18
\sum_q(-1)^{h\cdot q}\mathcal Z_q,
}
\]

and

\[
\boxed{
\mathcal Z_q
=
\sum_h(-1)^{h\cdot q}Z_h.
}
\]

This is an eight-component Walsh–Hadamard transform. 

26. The Q2 bit really is winding parity

Pairing the parity constraint with a dual cut gives

\[
\boxed{
q_\alpha=W_\alpha\pmod2.
}
\]

Thus the canonical Q2 statistic is

\[
\boxed{
f_{\rm odd}^{(\alpha)}(L)
=
P_{Z_{000}}(q_\alpha=1)
=
P_{Z_{000}}(W_\alpha\text{ odd}).
}
\]



27. Odd winding has an independent partition-ratio check

For the single-axis holonomy bit \(e_\alpha\),

\[
\boxed{
f_{\rm odd}^{(\alpha)}
=
\frac12
\left(
1-\frac{Z_{e_\alpha}}{Z_{000}}
\right).
}
\]

So the same quantity is measured in two algebraically related but computationally distinct ways:

direct \(q\)-sector occupancy;

an independent free-energy ratio.




28. There is an exact global sector-changing move

The canonical Q2 update toggles

\[
q_\alpha\to q_\alpha\oplus1
\]

and simultaneously adds an oriented unit current around \(\Gamma_\alpha\).

This preserves both

\[
\nabla\!\cdot I=0
\]

and

\[
I+M+\Gamma q=0\pmod2.
\]

The cosine and Villain acceptance ratios are explicitly frozen. 

29. The CKT axial construction became a comparator, not the canonical ensemble

The one-axis \(z\)-axial implementation is retained only after reconstructing its periodic closure bit and mapping it to \(h_z\) and \(q_z\).

It may reproduce literature benchmarks, but it cannot replace the three-axis \(Z_{000}\) ensemble. 

30. Q2 now has severe validation gates

Before Q2 opens, the implementation must pass:

exact \(Z_2^3\) character algebra;

machine-exact chain identities;

\(L=2,3\) direct/dual enumeration;

detailed balance on the complete state graph;

reachability of all eight \(q\) sectors;

independent ratio agreement;

cubic-axis symmetry;

translated-cycle checks;

sector mixing, \(\widehat R\), ESS, and round trips;

the CKT comparator.




31. Rare sectors cannot masquerade as confinement

Every Q2 axis must produce at least 100 effective sector round trips in aggregate, with

\[
\widehat R<1.01
\]

and effective sample size at least \(1000\).

If mixing fails, the result is

\[
\boxed{
\text{Q2 UNRESOLVED — SECTOR MIXING NOT VALIDATED},
}
\]

not “evidence for confinement.” 

32. Accessible sizes must be genuinely large relative to the confinement radius

A Q2 interpretation is admissible only if

\[
\boxed{
L_{\max}
\ge
4\xi_{\rm conf}^{95\%,\mathrm{upper}}.
}
\]

Otherwise the mandatory result is

\[
\boxed{
\text{Q2 INCONCLUSIVE — QUASI-DECONFINED WINDOW NOT EXCLUDED}.
}
\]




---

IV. The fit package and resource freeze

33. The weak susceptibility divergence demands an additive background

Because the charge-two susceptibility grows only as

\[
L^{0.52742},
\]

a regular constant background can dominate moderate sizes.

Therefore the primary fit is

\[
\boxed{
\chi_2(L)
=
b_0+
aL^\kappa
\left(1+cL^{-\omega}\right),
}
\]

with \(b_0\) mandatory. 

34. The spatial correlator became co-primary

The protocol also fits

\[
\boxed{
G_2(sL,L)
=
L^{-2\Delta}
\left(a_s+c_sL^{-\omega}\right)
}
\]

at fractional separations such as

\[
s=\frac14,\frac12.
\]

This avoids the additive susceptibility background and independently tests \(\Delta_2\). 

35. Q3 is measured on a fixed-\(R_\xi\) trajectory

Instead of comparing anisotropy while thermally drifting with size, the protocol tunes each size to

\[
\boxed{
R_\xi(J_L,h_6,L)=R_\xi^\star.
}
\]

That approximates a phenomenological RG trajectory and isolates anisotropy flow more cleanly. 

36. A zero-field anisotropy response was discovered

At \(h_6=0\),

\[
\langle A_3^\Phi\rangle=0,
\]

but the derivative is measurable:

\[
\boxed{
D_6(L)
=
\operatorname{Cov}(a_3^\Phi,H_6).
}
\]

It is fitted as

\[
D_6(L)\sim L^{y_6},
\]

providing a direct sign test for

\[
\boxed{y_6<0.}
\]

Finite positive and negative \(h_6\) values supply linear-response and sign-reversal checks. 

37. The first-order lane became a real finite-size test

A double peak alone no longer kills the continuous lane.

The protocol requires:

a two-component model favored by \(\Delta\mathrm{BIC}\ge10\);

a free-energy barrier growing as \(L^2\);

and either nonzero latent heat or \(L^3\) susceptibility behavior.




38. The timing audit found that lattice reach mattered more than redundant coupling points

The original schedule was estimated at roughly

\[
19{,}100\text{ core-hours}
\]

before allowed extensions, leaving almost no margin.

The repair kept the scientifically valuable maximum sizes and slimmed the nearby \(J\) grids:

five \(J\) points for smaller Stage-B lattices, three for \(L\ge64\);

five Stage-C points for \(L\le32\), three for \(L\ge48\);

two rather than four independent free-energy ladders.


These rules are now frozen in Appendix B.   

The back-of-the-envelope revised nominal estimate was approximately \(13.8\)–\(14.0\) thousand core-hours. The blind pilot—not that estimate—controls execution.

39. The protocol now has a hard forecast gate

The total resource ceiling is

\[
\boxed{
C_{\max}=20{,}000\text{ physical CPU core-hours}.
}
\]

But execution may begin only if the blind-pilot forecast satisfies

\[
\boxed{
C_{\rm forecast}\le14{,}000.
}
\]

That reserves at least \(6000\) core-hours for permitted blind extensions and unexpected autocorrelation growth. 

40. Expensive points cannot be quietly deleted

The frozen inventory must reconcile exactly with the forecast.

In particular, the \(L=192\) Q2 point cannot be dropped, deferred, relabeled optional, or silently shortened merely to pass the resource gate.

The only legal repairs are:

1. a formal amended protocol and new hash; or


2. a raised ceiling and new hash.





41. The execution now has a real provenance chain

The frozen lineage is

\[
\boxed{
H_{\rm Theory}
\rightarrow
H_{\rm Protocol}
\rightarrow
H_{\rm AppA}
\rightarrow
H_{\rm AppB}
\rightarrow
H_{\rm AppBAmend}
\rightarrow
H_{\rm Inventory}
\rightarrow
H_{\rm Pilot}
\rightarrow
H_{\rm Forecast}
\rightarrow
H_{\rm Execution}.
}
\]



Pilot outputs are immutable evidence feeding the forecast. They are not informal timing notes.


---

V. Hidden Quotient and GQG

42. The multiplication representation hides a larger kernel than ordinary nullity

For arbitrary measures,

\[
\ker\pi
\]

is the set of bounded functions that vanish locally almost everywhere—on every finite-measure set—not necessarily functions that vanish globally almost everywhere.

The infinite-mass point example proves the distinction. 

43. The correct general norm is the locally essential supremum

After quotienting,

\[
\boxed{
\|M_f\|
=
\|[f]\|_{B/\ker\pi}
=
\|f\|_{\infty,\mathrm{loc}}.
}
\]

The familiar ordinary essential supremum identity is recovered under semifiniteness, but it is not valid for arbitrary measures. 

44. Every measure acts on \(L^2\) as though it had first been semifinitely reduced

The quotient is naturally

\[
\boxed{
B(X,\Sigma)/\ker\pi
\cong
L^\infty(\mu_{\rm sf}),
}
\]

and for \(1\le p<\infty\),

\[
\boxed{
L^p(\mu)=L^p(\mu_{\rm sf}).
}
\]

So finite-\(p\) witnesses cannot distinguish the original measure from its semifinite reduction. 

45. There are two different repair thresholds

Hidden Quotient exposed two distinct seams:

1. Visibility: invisible mass is removed by semifinite reduction.


2. Gluing/completeness: missing suprema require localizable completion.



The first repair does not automatically perform the second. 

46. GQG now gives retained context a typed home without redefining ordinary quotients

An ordinary quotient remains determined by its source and equivalence relation.

The larger observational record also carries:

the witness;

retained context;

conditioning;

the claim rule;

the computational realization.




47. Retention and conditioning are different operations

Retaining a context map \(r:P\to S\) refines the observation:

\[
\Omega_{W\oplus r}
=
\langle\Omega_W,r\rangle.
\]

Conditioning instead restricts the source to a fiber:

\[
P_s=r^{-1}(s).
\]

Conditioning after quotienting is defined only if \(r\) descends through the quotient. 

48. No silent witness change

If the source, sector, boundary conditions, gauge choice, normalization, observable, or realization changes, the architecture changed.

Transporting a quotient claim requires a commuting square and descent certificate:

\[
q_{W'}\circ T
=
\bar T\circ q_W.
\]



49. Separate witnesses may be conjoined but not substituted

If \(W_1,W_2,W_3\) support claims \(C_1,C_2,C_3\), GQG permits

\[
C_1\land C_2\land C_3,
\]

but not

\[
C_1\Rightarrow C_2
\]

without a declared inference rule.

That is exactly the formal grammar behind the Q1/Q2/Q3 split. 

50. Hashes prove lineage, not truth

A digest can establish byte identity, ordering, and provenance.

It cannot establish:

semantic correctness;

witness equivalence;

evidentiary independence;

physical validity.


One frozen hash can faithfully preserve a frozen bug. 


---

VI. The diamond torus and conserved-current picture

51. The diamond grid is a valid rotated rendering of the existing toroidal lattice

The canonical microscopic lattice remains cubic. But a square toroidal face may be rotated \(45^\circ\), producing the diagonal families

\[
e_+=(1,1),
\qquad
e_-=(1,-1).
\]

After opposite-edge identification, those tracks become closed or helical paths around the torus.

This changes the visualization, not the microscopic model.

52. A current can converge, turn, and diverge without a source or sink

At every routing vertex,

\[
\boxed{
\sum_{\ell\ni v}s_{v\ell}J_\ell=0.
}
\]

So the clean local picture is

\[
\boxed{
\text{convergence}
\longrightarrow
\text{redirection}
\longrightarrow
\text{divergence}.
}
\]

Nothing is created or destroyed. The current is merely rerouted.

53. The radial projection can reverse while the current never reverses

For a continuously oriented circuit,

\[
J_\parallel>0
\]

can remain true everywhere, while an embedding-relative radial projection passes through

\[
\boxed{
J_{\rm radial}<0
\longrightarrow
J_{\rm radial}=0
\longrightarrow
J_{\rm radial}>0.
}
\]

The path moves inward on one part of the embedded circuit and outward on another, but its intrinsic orientation never flips.

54. No singularity is required

The “turning point” can simply be a conserved routing region where the radial projection vanishes.

The canonical \(T^3\) has no intrinsic center, donut hole, throat, or radial coordinate. Those appear only after choosing an embedding.

So the strongest earned statement is:

\[
\boxed{
\text{projected radial reversal}
\neq
\text{intrinsic current reversal}.
}
\]

55. Q2 detects global circuit topology, not local directional anatomy

Q2 keeps

\[
q_\alpha=W_\alpha\pmod2.
\]

It therefore remembers whether a noncontractible cut is crossed oddly or evenly.

It forgets:

winding sign;

winding magnitude beyond parity;

local turning;

chirality;

handedness;

inward versus outward projection.

56. The raw-data architecture preserves more than the verdict uses
Appendix B stores both
and
So the canonical Q2 verdict uses parity, but the signed winding data are not destroyed. �
appendix_b_field_physics_RECONCILED_CLEAN.md
A later preregistered comparator could examine signed winding, oriented current correlations, or lattice circulation without rerunning the entire experiment—provided the raw estimator support is adequate.
57. Global seam sign and seam texture are not the same kind of object
A uniform seam sign can represent a global holonomy bit.
A checkerboard or random seam is an �-component conditioned texture that introduces local frustration or quenched disorder. It is not simply another member of the eight � topological sectors.
The clean distinction is:
GQG gives that distinction the CTX / COND language. �
GQG_Core_Card_v0.3.md
58. Nonuniform seam responses are not automatically probabilities
For a nonuniform negative-sign texture, the dual character factor can be signed.
Therefore the resulting even/odd decomposition need not define nonnegative probabilities. A checkerboard or random seam should be studied through a free-energy or character response—not casually called another �.
This is a derived correction from our latest seam analysis, not yet part of the frozen canonical protocol.
59. Dual currents are statistical currents, not yet real-time fluid trajectories
The � variables are currents in an equilibrium partition-function representation.
A valid configuration can be drawn as a conserved circuit, but the protocol does not yet prove that a physical particle or fluid parcel moves through the circuit in real time.
A real-time convergence–turn–divergence mechanism would require a separate dynamical model.

60. Post-freeze comparator SW-1 — signed odd-winding balance

Status. SW-1 is a separately preregistered, post-freeze supplemental comparator. It does not amend Simulation Protocol v0.3, Appendices A or B, the execution inventory, or the canonical Q2 decision rule.

The comparator asks one question:

[
\boxed{\text{Is canonical odd winding balanced between its two global orientations?}}
]

Frozen canonical baseline

SW-1 uses only accepted Z_{000} Q2 chains and the already-defined signed integer winding

[
W_\alpha

\frac{1}{L}
\sum_{\ell\parallel\alpha} I_\ell,
\qquad
\alpha\in{x,y,z}.
]

The canonical topological bit remains

[
q_\alpha=W_\alpha\pmod 2,
]

and the canonical Q2 observable remains

[
f_{\rm odd}^{(\alpha)}(L)

P_{Z_{000}}(q_\alpha=1)

P_{Z_{000}}(W_\alpha\text{ odd}).
]

Its independent canonical check remains

[
f_{\rm odd}^{(\alpha)}

\frac12
\left(
1-\frac{Z_{e_\alpha}}{Z_{000}}
\right).
]

None of these definitions, estimators, gates, fits, or verdicts is changed by SW-1.

Comparator definition

For each stored measurement t, define

[
X_{\alpha,t}

q_{\alpha,t},
\operatorname{sgn}(W_{\alpha,t}),
\qquad
\operatorname{sgn}(0)=0.
]

The primary post-freeze comparator is

[
\boxed{
S_{\rm odd}^{(\alpha)}(L)

\left\langle X_\alpha\right\rangle_{Z_{000}}

P(W_\alpha>0,\ q_\alpha=1)

P(W_\alpha<0,\ q_\alpha=1).
}
]

This gives the exact sign-resolved decomposition

[
f_{{\rm odd},+}^{(\alpha)}

\frac12
\left(
f_{\rm odd}^{(\alpha)}
+
S_{\rm odd}^{(\alpha)}
\right),
]

[
f_{{\rm odd},-}^{(\alpha)}

\frac12
\left(
f_{\rm odd}^{(\alpha)}

S_{\rm odd}^{(\alpha)}
\right),
]

with

[
f_{\rm odd}^{(\alpha)}

f_{{\rm odd},+}^{(\alpha)}
+
f_{{\rm odd},-}^{(\alpha)}.
]

Thus SW-1 partitions the canonical odd-winding mass without redefining or replacing it.

Exact null and interpretation

At h_6=0, current reversal

[
I_\ell\longmapsto-I_\ell
]

preserves the Z_{000} weight and q_\alpha, while sending

[
W_\alpha\longmapsto-W_\alpha.
]

The preregistered null is therefore

[
\boxed{S_{\rm odd}^{(\alpha)}(L)=0.}
]

A resolved nonzero value identifies sign imbalance in the stored chains. It triggers checks for inadequate sign mixing, orientation conventions, update asymmetry, or an undeclared oriented condition. It does not by itself establish chirality, local circulation, real-time flow, projected radial reversal, or a new phase.

Likewise, S_{\rm odd}=0 does not show that local currents never turn. It says only that the two global winding orientations are balanced.

Analysis and validation

The comparator must be frozen and hashed before any sign-resolved result is displayed. It shall:

- use the complete frozen Q2 size-and-axis inventory, with no selective removal;
- use no new ensemble, seam, mask, kernel, parameter point, lattice size, or simulation run;
- inherit the canonical autocorrelation-aware blocking procedure;
- require \widehat R<1.01, effective sample size at least 1000 for X_\alpha, and at least 100 effective positive-to-negative-to-positive sign round trips per analyzed axis;
- report simultaneous 95% block-bootstrap intervals over the complete preregistered (L,\alpha) grid;
- record the execution root, input raw hashes, comparator-preregistration hash, analysis-code hash, bootstrap seed, and creation time.

The allowed result labels are:

[
\text{SW-1 SIGN IMBALANCE DETECTED},
]

[
\text{SW-1 NO SIGN IMBALANCE DETECTED},
]

or

[
\text{SW-1 UNRESOLVED — SIGNED RAW SUPPORT OR SIGN MIXING INADEQUATE}.
]

Failure of SW-1 cannot be reported as confinement, and success cannot establish deconfinement. The canonical Q2 verdict remains determined exclusively by the frozen parity observable, partition-ratio check, validation gates, mixing requirements, and size-admissibility rule.

Freeze boundary

The status of the relevant quantities is:

- W_\alpha: frozen source estimator retained in the raw chains;
- q_\alpha, f_{\rm odd}^{(\alpha)}, and Z_{e_\alpha}/Z_{000}: canonical quantities;
- X_\alpha, S_{\rm odd}^{(\alpha)}, and f_{{\rm odd},\pm}^{(\alpha)}: post-freeze comparator quantities;
- seam textures, phase-duration variables, pulse masks, local oriented-current correlations, circulation measures, chirality, and radial projections: outside SW-1.

If the immutable raw schema does not contain per-measurement signed W_\alpha, SW-1 is not estimable from that execution. Signed winding may not be reconstructed from parity alone, and no replacement run may be added under the original execution root.
The deepest common pattern
Across the whole stack, the same rule keeps reappearing:
That single discipline produced:
the operator-selection theorem;
the Q1/Q2/Q3 split;
the fixed-holonomy repair;
the eight-sector transform;
the no-selective-removal rule;
the GQG retained-context upgrade;
and the diamond-torus visualization without inventing a singularity.
The current one-line synthesis is:
And the whole current corpus is dedicated under CC0: copy it, modify it, test it, redistribute it, build on it, or tear it apart. No attribution required. �
field_physics_appendix_A_THREE_AXIS_FIXED.md
