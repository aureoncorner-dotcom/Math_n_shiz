# Gear mathematics — geometry checked

All six sections of the supplied `Gear_Math_Only.md` were checked. The original numerical results reproduce exactly. The changes below make the geometric domains explicit, distinguish displacement from sensitivity, compare the quoted inclination with an independently derived normal, complete the finite cutter sweep, and derive the full geometry of the coning surface.

| Original section | Result of the geometry audit |
|---|---|
| 1. Tooth curve | Affine-cycloid identity, series, and curvature pass. Its endpoint admits a regular one-sided C¹ parametrization, but its curvature is unbounded and it is not a regular C² endpoint. |
| 2. Half-scale tangency | Local coincidence and tangency pass. A concrete counterexample below shows why global interference needs a separate test. |
| 3. Gap geometry | All 715 numerical cases pass an independent area calculation. Add boundary conditions and physical coordinate scales. Total movement and incremental sensitivity have different ratios. |
| 4. Finite-tooth inclination | The quoted formulas and table reproduce. Relative to the polar curve specified below, the quoted normal angle has a small cubic-order approximation error. |
| 5. Handoff and harmonics | Coefficients, means, slope jump, and first-harmonic comparison pass. Added AC RMS and the harmonics surviving equally spaced pulses. |
| 6. Envelope, coning, motion | The identities pass. Added sweep end caps, a global boundary check for the example, the full surface normal and Gaussian curvature, and conditions on inverse fitting. |

**Executed:** original 38 symbolic identities; 23 additional symbolic identities; independent reintegration of all 715 original gap regions; 2,541 bounded-minimum cases; 1,601 complete-sweep boundary points; 4,961 coning-surface normal checks. These verify the defined mathematical models. Numerical sampling supplements the proofs and does not certify an unspecified gear assembly.

![Geometry audit: sensitivity, complete sweep, normal-angle approximation, and saddle curvature](C:/Users/drewd/Documents/Codex/2026-09-16/com/outputs/Gear_Geometry_Checked.png)

**1. Tooth curve: classification, regularity, curvature, and offsets**

Let \(L=mn>0\), with \(0\leq\theta\leq\pi\):

\[
p(\theta)=(x,y),\qquad
x=\frac L4(\pi+\theta-\sin\theta),\qquad
y=\frac L2(\cos\theta-1).
\]

Then

\[
X=4x/L-\pi=\theta-\sin\theta,\qquad
Y=-2y/L=1-\cos\theta.
\]

This is exactly an affine image of a cycloid half-arch. The unequal coordinate scales matter: an affine transformation generally changes angles, normals, and curvature. If \(p=A\gamma+b\), a normal transforms in the direction \(A^{-T}n\); transforming a normal as \(An\) generally gives the wrong result.

The derivatives are

\[
p'=\frac L4(1-\cos\theta,-2\sin\theta),\qquad
v=\|p'\|=\frac L4\sqrt{(1-\cos\theta)^2+4\sin^2\theta}.
\]

For \(0<\theta\leq\pi\), \(v>0\), and \(x'>0\). Thus the open branch is regular and has no self-intersections. Its unit tangent and left normal are

\[
T=\frac{(1-\cos\theta,-2\sin\theta)}{\sqrt{(1-\cos\theta)^2+4\sin^2\theta}},\qquad
N=\frac{(2\sin\theta,1-\cos\theta)}{\sqrt{(1-\cos\theta)^2+4\sin^2\theta}}.
\]

The original endpoint expansions are correct:

\[
x-x(0)=\frac{L\theta^3}{24}-\frac{L\theta^5}{480}+O(\theta^7),\qquad
y=-\frac{L\theta^2}{4}+\frac{L\theta^4}{48}+O(\theta^6).
\]

Although \(p'(0)=0\), the one-sided branch has limiting tangent \((0,-1)\). With \(h=-y\geq0\),

\[
x-x(0)=\frac{h^{3/2}}{3\sqrt L}+O(h^{5/2}),\qquad y=-h.
\]

This parametrization has nonzero speed at \(h=0\) and is C¹ there. Its second derivative diverges. The precise endpoint issue is failure of regular C² geometry and bounded curvature; zero speed in the original parameter alone would not establish that issue. Extending the original formula through negative \(\theta\) gives the familiar cusp.

The signed curvature on the regular branch is positive:

\[
\kappa(\theta)=\frac{8(1-\cos\theta)}{L[(1-\cos\theta)^2+4\sin^2\theta]^{3/2}}
=\frac{2}{L\sin(\theta/2)[1+3\cos^2(\theta/2)]^{3/2}}.
\]

\[
\kappa\sim\frac1{2L\theta}\quad(\theta\downarrow0),\qquad
\kappa(\pi)=\frac2L.
\]

Its global minimum on the regular half-arch is

\[
\theta_{\min}=2\arccos\sqrt{2/3}=1.230959417\ldots,\qquad
\kappa_{\min}=\frac{2}{3L}.
\]

The exact half-arch length is

\[
S=L\int_0^1\sqrt{1+3u^2}\,du
=L\left(1+\frac{\operatorname{asinh}\sqrt3}{2\sqrt3}\right)
=1.380172998\ldots L.
\]

For an offset toward the left normal, \(p_d=p+dN\), differentiation with respect to arc length gives \(dp_d/ds=(1-d\kappa)T\). A local offset singularity occurs when \(d\kappa=1\). Because \(\kappa\) is unbounded at the endpoint, no fixed positive \(d\) satisfies the usual sufficient bound \(d\kappa<1\) throughout this whole branch. Any retained endpoint, blend, or cutter offset therefore requires its own geometric definition.

**2. Half-scale contact: local tangency and global interference**

Let \(M(t)\) be a translation path, \(C(s)=M(s)/2\) a fixed profile, and \(F(s)=-M(s)/2\) a local moving profile. At pose \(t\), the moving curve is \(M(t)+F(s)\). At the corresponding point \(s=t\),

\[
M(t)+F(t)=C(t),\qquad F'(t)=-C'(t).
\]

For \(M'(t)\ne0\), these equations establish coincidence and a common tangent. The physical velocity of a fixed material point of the translating profile is \(M'(t)\); hence the common normal satisfies

\[
n\cdot M'=0.
\]

This is the local geometric content of the half-scale rack construction. The published construction specifies branches and a contact range in addition to the scale transformation. [US4823638A](https://patents.google.com/patent/US4823638A/en)

More generally, for any constant \(0<\lambda<1\),

\[
C=\lambda M,\qquad F=-(1-\lambda)M
\]

also gives coincidence and parallel tangents. The value \(\lambda=1/2\) provides equal scales; tangency alone does not uniquely select it.

A global-interference counterexample is

\[
M(s)=(s,s^2-s^4),\qquad -2\leq s\leq2.
\]

At pose \(t=0\), the half-scale curves have graphs

\[
y_C=2x^2-8x^4,\qquad y_F=-2x^2+8x^4.
\]

They are tangent at \(x=0\), while their separation

\[
y_C-y_F=4x^2-16x^4
\]

changes sign at \(x=\pm1/2\), where the intersections are transverse. The local tangency identities all hold, yet extending the branches creates crossings. Solid-side conventions, branch limits, clearance, and other teeth are needed for a global non-interference result.

**3. Gap geometry: minima, boundaries, area, and physical scale**

The example is

\[
G_w(x,y;t)=20[(1-w)x^2+wx^4]+10y^2+tx,
\quad (x,y)\in[-1,1]^2,\quad0\leq w\leq1.
\]

Coordinates are dimensionless, and \(G_w\) is measured in µm. The parameter \(t\) specifies µm of linear gap change per normalized half-width.

The minimum has \(y_*=0\). The x-derivative is strictly increasing, including the pure quartic case, so the minimum is unique. The complete bounded solution is

\[
x_*=
\begin{cases}
-1,&t\geq40(1+w),\\
\text{the unique root of }40(1-w)x+80wx^3+t=0,&|t|<40(1+w),\\
1,&t\leq-40(1+w).
\end{cases}
\]

At equality, the stationary point reaches the boundary. The original sweep \(|t|\leq8\) lies strictly in the interior for every \(w\); no original minimum needs correcting.

For the interior branches,

\[
x_{*,0}=-t/40,\qquad x_{*,1}=\sqrt[3]{-t/80},\qquad
\frac{dx_*}{dt}=-\frac1{40(1-w)+240wx_*^2}.
\]

The derivative formula requires a positive denominator. The pure quartic at \(t=0\) has a unique minimum despite its zero quadratic curvature; the dependence on tilt is proportional to \(t^{1/3}\) and is not differentiable there. Beyond the boundary threshold, \(x_*\) stays at an edge and its derivative is zero until the active boundary changes.

Define

\[
g=G_w-\min_{[-1,1]^2}G_w,\qquad
\Omega_\delta=\{(x,y)\in[-1,1]^2:g(x,y)\leq\delta\}.
\]

For \(P_w(x)=20[(1-w)x^2+wx^4]+tx\), an explicit area formula is

\[
A_\delta=\int_{-1}^1 2\min\!\left(1,\sqrt{\frac{[\delta-P_w(x)+P_w(x_*)]_+}{10}}\right)dx,
\qquad [u]_+=\max(u,0).
\]

This is a projected near-contact region defined by clearance. Loaded contact area additionally requires a mechanical model.

| Shape | Tilt t | First-contact x | Area at δ = 2 µm |
|---|---:|---:|---:|
| Quadratic | 0 | 0.000000 | 0.444288 |
| Half blend | 0 | 0.000000 | 0.591082 |
| Quartic | 0 | 0.000000 | 0.879217 |
| Quadratic | 4 | −0.100000 | 0.444288 |
| Half blend | 4 | −0.186935 | 0.556791 |
| Quartic | 4 | −0.368403 | 0.576276 |
| Quadratic | 8 | −0.200000 | 0.444288 |
| Half blend | 8 | −0.328865 | 0.491445 |
| Quartic | 8 | −0.464159 | 0.414363 |

Across all 715 original cases, \(|x|\leq0.700670\) and \(|y|\leq0.447214\) throughout these regions, so the box does not clip them. Integrating horizontal slices independently of the original vertical-width integration changes the areas by at most \(4.14\times10^{-11}\).

At zero tilt, the unclipped formulas are

\[
A_{\mathrm{quadratic}}(\delta)=\frac{\pi\delta}{\sqrt{200}},\qquad
A_{\mathrm{quartic}}(\delta)=\sqrt{\delta/10}\,(\delta/20)^{1/4}B(1/4,3/2).
\]

Thus the respective clearance scalings are \(\delta\) and \(\delta^{3/4}\). At \(\delta=2\), the quartic/quadratic area ratio is 1.979. In the computed positive-tilt interval, their areas become equal at \(t=6.807673439\ldots\); the quartic area at \(t=8\) is smaller.

**Displacement and sensitivity are different quantities.** For \(t>0\),

\[
\frac{|x_{*,1}|}{|x_{*,0}|}=\frac{40}{80^{1/3}t^{2/3}},\qquad
\frac{|dx_{*,1}/dt|}{|dx_{*,0}/dt|}=\frac13\frac{|x_{*,1}|}{|x_{*,0}|}.
\]

| Tilt | Quartic/quadratic total displacement | Quartic/quadratic local sensitivity |
|---:|---:|---:|
| 4 | 3.684031 | 1.228010 |
| 8 | 2.320794 | 0.773598 |

The local sensitivities are equal at

\[
|t|=\frac{80}{6\sqrt6}=5.443310540\ldots.
\]

The original 3.684 displacement comparison is correct. It cannot be substituted for the derivative ratio.

For a general quadratic gap with symmetric positive-definite \(H\),

\[
G=\tfrac12\mathbf x^TH\mathbf x+\ell^T\mathbf x,
\qquad \mathbf x_*=-H^{-1}\ell
\]

is the unconstrained minimum and also the bounded minimum whenever it lies in the permitted region. Otherwise a constrained minimum is required. Completing the square gives unclipped contours

\[
\tfrac12(\mathbf x-\mathbf x_*)^TH(\mathbf x-\mathbf x_*)\leq\delta,
\qquad A_\delta=\frac{2\pi\delta}{\sqrt{\det H}}.
\]

The original coupled example passes:

\[
H=\begin{bmatrix}40&8\\8&20\end{bmatrix},\qquad
\ell=\begin{bmatrix}4\\0\end{bmatrix},\qquad
\mathbf x_*=\begin{bmatrix}-5/46\\1/23\end{bmatrix}.
\]

Its eigenvalues are 17.193752 and 42.806248. These describe opening in normalized coordinates.

For physical half-widths \(a_x,a_y\) in mm, let \(D=\operatorname{diag}(a_x,a_y)\) and \(\mathbf r=D\mathbf x\). Because gap height was in µm, the Hessian of the height in mm is

\[
H_{\mathrm{physical}}=10^{-3}D^{-T}HD^{-1}\quad[\mathrm{mm}^{-1}].
\]

At a common tangent contact in orthonormal physical coordinates, this gives the quadratic relative-curvature matrix. Unequal half-widths generally change both its eigenvalues and its eigenvectors. Projected area converts as

\[
A_{\mathrm{physical}}=a_xa_yA_{\mathrm{normalized}}\quad[\mathrm{mm}^2].
\]

Physical radii and physical patch areas require these scales.

**4. Finite-tooth inclination: quoted equations and independent normal geometry**

The retained source equations are

\[
\alpha=\frac{mn}{2r_n},\qquad
\theta=\frac\eta2-\alpha\sin\eta+\alpha^2\sin2\eta,
\]
\[
\epsilon=\theta-\frac\eta2\frac{Z_F}{Z_C},\qquad
\mu_p=\arctan\!\left(\frac{2mn\sin\eta}{r_n+2mn\cos\eta}\right),\qquad
\xi_p=\epsilon+\mu_p.
\]

The printed equations and the repeated θ expression were checked in [US5918508A, columns 3 and 5, equations (3)–(6)](https://patents.google.com/patent/US5918508A/en). The repeated expression resolves the missing parenthesis in equation (4). Matching these equations establishes their transcription and evaluation; physical exactness is a separate question.

For the original examples, \(m=1\), \(n=1\), \(Z_C=Z_F+2\), \(r_n=mZ_F/2\), and \(0\leq\eta\leq\pi\). Angles in the formulas are radians. The selected neutral radius and interval remain illustrative inputs.

| ZF / ZC | Quoted ξ at η = π/2 | Maximum absolute quoted ξ | Discarded constant shortcut |
|---|---:|---:|---:|
| 60 / 62 | 4.310758° | 4.537560° | 27.723764° |
| 100 / 102 | 2.600005° | 2.719209° | 28.086166° |
| 200 / 202 | 1.304828° | 1.358545° | 28.364247° |
| 1000 / 1002 | 0.261706° | 0.271562° | 28.590708° |
| 10000 / 10002 | 0.026187° | 0.027153° | 28.642161° |

These numbers all reproduce. The maxima are over the specified mathematical interval. Also, \(\xi_p(0)=0\) and the rack limit with this parameter family is zero, while \(0.5Z_F/Z_C\to0.5\) rad.

**Normal comparison.** Write \(A=mn\). The patent's position expressions contain the radial form \(r_n+A\cos2\theta\). Consider explicitly the polar curve

\[
p(\varphi)=r(\varphi)e_r(\varphi),\qquad
r(\varphi)=r_n+A\cos2\varphi.
\]

Its exact outward normal direction is \(r e_r-r'e_\varphi\). Consequently, its signed normal angle from the radial direction, evaluated at \(\varphi=\theta(\eta)\), is

\[
\mu_g(\eta)=\operatorname{atan2}\!\left(2A\sin2\theta(\eta),\ r_n+A\cos2\theta(\eta)\right).
\]

For \(e=A/r_n\to0\), substitution of the quoted θ relation gives the independently derived expansion

\[
\mu_p-\mu_g=e^3\sin\eta\,(2+\sin^2\eta)+O(e^4).
\]

Thus the two angle expressions agree through quadratic order in \(e\), while they are not exactly identical. This audit establishes their approximation relationship for this particular polar-curve model; it does not assign an error to an unspecified physical flexspline.

| ZF | Maximum absolute normal-angle difference on [0, π] |
|---:|---:|
| 60 | 0.006365775° |
| 100 | 0.001375063° |
| 200 | 0.000171886° |
| 1000 | 0.000001375° |
| 10000 | 0.000000001375° |

The denominator in the quoted arctangent stays positive when \(r_n>2A\), as it does in every listed example. Extending the formula beyond that condition requires quadrant and branch handling; `atan2` alone does not supply missing deformation assumptions. The polar curve itself has positive radius for \(r_n>A\).

A complete finite-tooth construction also needs translation of the tooth origin, both tooth profiles, and their allowed contact interval. Its pose has the form

\[
p_{\mathrm{placed}}(s,\eta)=Q(\xi(\eta))p_{\mathrm{local}}(s)+T(\eta).
\]

An inclination calculation alone does not check the complete mesh.

**5. Handoff continuity and harmonic geometry**

On one period, extended periodically,

\[
f(q)=\min(q^2,(q-1)^2),\qquad
s(q)=\tfrac14\sin^2(\pi q),\qquad0\leq q\leq1.
\]

Both have minimum zero and maximum 1/4. At the interior handoff,

\[
f'(1/2^-)=1,\qquad f'(1/2^+)=-1,\qquad
\Delta f'=-2.
\]

The periodic endpoints of \(f\) have matching value and first derivative. Its handoff at 1/2 is the derivative discontinuity. Both one-sided derivatives of \(s\) at 1/2 are zero.

Using

\[
f(q)=\bar f+\sum_{k\geq1}[a_k\cos(2\pi kq)+b_k\sin(2\pi kq)],
\]

the exact coefficients are

\[
\bar f=1/12,\qquad a_k(f)=\frac{(-1)^k}{\pi^2k^2},\qquad b_k(f)=0,
\]
\[
\bar s=1/8,\qquad a_1(s)=-1/8,\qquad a_{k\geq2}(s)=b_k(s)=0.
\]

The formula for all positive integers \(k\) also follows from the periodic distributional identity \(f''=2-2\delta(q-1/2)\). This provides a general derivation in addition to the original six explicit integrations.

| Harmonic | Cusp amplitude | Smooth amplitude |
|---|---:|---:|
| 1 | 0.101321184 | 0.125000000 |
| 2 | 0.025330296 | 0.000000000 |
| 3 | 0.011257909 | 0.000000000 |
| 4 | 0.006332574 | 0.000000000 |
| 5 | 0.004052847 | 0.000000000 |
| 6 | 0.002814477 | 0.000000000 |

The first harmonic increases by 23.370055% in this equal-height example. The mean-removed RMS values also satisfy

\[
\operatorname{RMS}_{AC}(f)=1/\sqrt{180}=0.074535599\ldots,\qquad
\operatorname{RMS}_{AC}(s)=1/\sqrt{128}=0.088388348\ldots.
\]

The latter is 18.585412% larger. Removing the higher harmonics of these particular waveforms therefore does not reduce their total mean-removed RMS. Converting a phase derivative to a time derivative requires the actual \(q(t)\); sound or vibration response requires additional dynamics.

For three identical equal-strength pulses, the normalized phase factor of harmonic \(k\) is

\[
P_k=\frac13\left|\sum_{j=1}^3e^{-2\pi i k\phi_j}\right|.
\]

At phases \((0,1/3,2/3)\),

\[
P_k=\begin{cases}1,&3\text{ divides }k,\\0,&\text{otherwise}.\end{cases}
\]

The first harmonic cancels, while multiples of three survive the timing factor. For phases \((0,0.2,0.55)\), \(P_1=0.245028445\ldots\). Actual pulse harmonics equal the individual pulse's coefficients multiplied by the corresponding complex phase sum.

**6a. Cutter envelope: local condition and complete finite sweep**

For a rigidly posed regular tool surface,

\[
X(u,v,q)=Q(q)c(u,v)+p(q),\qquad Q^TQ=I,\quad\det Q=1,
\]

the normal is defined when \(X_u\times X_v\ne0\). At an interior pose, a candidate envelope satisfies

\[
n\cdot X_q=0
\iff (X_u\times X_v)\cdot X_q=0
\iff\det[X_u\;X_v\;X_q]=0.
\]

The determinant equation identifies tangential sweep candidates. Selecting the actual swept-solid boundary also requires a regular envelope branch, removal of covered or intersecting portions, and the exposed boundaries at the start and end of a finite motion. At a singular surface parametrization, a vanishing determinant alone says nothing about tangency.

For the original two-dimensional cross-section, a disk of radius \(R=0.2\) has center

\[
c(q)=(q,aq^2),\qquad a=0.25,\qquad -1\leq q\leq1.
\]

Define

\[
T=\frac{(1,2aq)}{\sqrt{1+4a^2q^2}},\qquad
N=\frac{(-2aq,1)}{\sqrt{1+4a^2q^2}},\qquad
\kappa=\frac{2a}{(1+4a^2q^2)^{3/2}}.
\]

The side envelopes and their derivatives are

\[
E_\pm=c\pm RN,\qquad
\frac{dE_\pm}{dq}=\|c'\|(1\mp R\kappa)T.
\]

Here \(R\kappa\leq0.1\), so both side curves are regular. A positive-side offset would become singular at \(R=2,q=0\); this demonstrates why the radius condition is substantive.

The complete boundary of \(\bigcup_{q\in[-1,1]}\overline B_R(c(q))\) includes two additional semicircles:

\[
\begin{aligned}
\text{start cap: }&c(-1)+Ru,\quad \|u\|=1,\quad u\cdot T(-1)\leq0,\\
\text{end cap: }&c(1)+Ru,\quad \|u\|=1,\quad u\cdot T(1)\geq0.
\end{aligned}
\]

**Global check for this example.** For any candidate boundary point \(P=(p_x,p_y)\), set

\[
D_P(q)=\|c(q)-P\|^2=(q-p_x)^2+(aq^2-p_y)^2.
\]

Since \(p_y\leq0.25+0.2=0.45\),

\[
D_P''(q)=2+12a^2q^2-4ap_y\geq1.55>0.
\]

Thus the nearest center is unique. Side-envelope points have a stationary nearest center; the cap inequalities give the correct endpoint minimum. All these points are at distance exactly \(R\) from the entire center path. This establishes that the shown sides and caps are exposed globally for this example, rather than merely satisfying the local envelope equation. Conversely, a swept-boundary point must have an interior stationary nearest center or an endpoint nearest center, giving exactly these pieces.

The path length and full swept area are

\[
L_c=\sqrt{1.25}+2\operatorname{asinh}(0.5)=2.080457639\ldots,
\]
\[
A_{\mathrm{sweep}}=2RL_c+\pi R^2=0.957846762\ldots.
\]

Numerical nearest-center checks at 1,601 boundary points have maximum distance error \(1.39\times10^{-16}\). A dense polygon approximation differs from the exact area by \(2.04\times10^{-8}\) square length units.

**6b. Coning surface: full normal, metric, and Gaussian curvature**

At a fixed wave-generator phase \(q\), let

\[
\phi=\theta-q,\qquad r=R_0+a(z)\cos2\phi,\qquad
X(\theta,z)=(r\cos\theta,r\sin\theta,z).
\]

Assume \(R_0>\sup_z|a(z)|\) on the chosen axial interval, ensuring positive radius and a regular embedded surface. Let \(e_r,e_\theta,e_z\) be the cylindrical orthonormal basis. The relevant derivatives are

\[
r_\theta=-2a(z)\sin2\phi,\qquad r_z=a'(z)\cos2\phi,
\]
\[
X_\theta=r_\theta e_r+r e_\theta,\qquad X_z=r_z e_r+e_z.
\]

The original formula for \(r_z\) is correct. The full outward unit normal is

\[
n=\frac{r e_r-r_\theta e_\theta-r r_z e_z}{\sqrt{r^2+r_\theta^2+r^2r_z^2}}.
\]

The axial slope alone omits the circumferential component. The signed elevation of this normal from the horizontal plane is

\[
\operatorname{atan2}(-r r_z,\sqrt{r^2+r_\theta^2}).
\]

The surface metric is

\[
ds^2=E\,d\theta^2+2F\,d\theta\,dz+G\,dz^2,
\]
\[
E=r^2+r_\theta^2,\qquad F=r_\theta r_z,\qquad G=1+r_z^2.
\]

Thus the angular and axial coordinate curves are generally not orthogonal. Write

\[
W^2=EG-F^2=r^2+r_\theta^2+r^2r_z^2>0.
\]

The Gaussian curvature is

\[
K=\frac{r r_{zz}\,[r(r_{\theta\theta}-r)-2r_\theta^2]-(r r_{\theta z}-r_\theta r_z)^2}{(r^2+r_\theta^2+r^2r_z^2)^2}.
\]

For the especially useful linear-amplitude case, \(a(z)=a_0+\beta z\), this reduces to

\[
\boxed{K=-\frac{4\beta^2R_0^2\sin^2(2\phi)}{(r^2+r_\theta^2+r^2r_z^2)^2}\leq0.}
\]

For nonzero \(\beta\), the curvature is negative between the principal axes and zero on them. The fixed-angle axial curves are straight, so this is a ruled surface with saddle regions. A literal cone is developable away from its apex and has \(K=0\); the stated coning model has different geometry.

For the figure's explicit example, \(R_0=10\) mm, \(a(z)=0.5\text{ mm}+0.1z\), and \(0\leq z\leq10\) mm. At \(z=0,\phi=\pi/4\),

\[
K=-4/10201=-0.000392118420\ldots\ \mathrm{mm}^{-2}.
\]

The analytic normal is perpendicular to both surface tangents at all 4,961 sampled points, with maximum absolute normalized dot product \(1.18\times10^{-16}\).

**Cross-section geometry.** At any fixed z, the radial wave has area

\[
A_{\mathrm{section}}=\frac12\int_0^{2\pi}r^2\,d\theta
=\pi R_0^2+\frac\pi2a^2.
\]

An ellipse with the same axial radii \(R_0+a\) and \(R_0-a\) has area \(\pi(R_0^2-a^2)\). Thus the radial cosine wave is not exactly that ellipse when \(a\ne0\).

Its perimeter is

\[
P(a)=\int_0^{2\pi}\sqrt{(R_0+a\cos2\theta)^2+4a^2\sin^22\theta}\,d\theta
=2\pi R_0\left[1+(a/R_0)^2+O((a/R_0)^4)\right].
\]

At \(R_0=10\) mm and \(a=0.5,1.0,1.5\) mm, the numerical perimeter increases relative to \(2\pi R_0\) are respectively 0.249688%, 0.995062%, and 2.225374%. A constant \(R_0\) in this model therefore does not automatically enforce an inextensible neutral circumference. A material deformation model must supply that constraint if it is required.

**6c. Machine motion and inverse geometry**

For a scalar axis setting \(b(q)\) and feed law \(q(t)\),

\[
\dot b=b'(q)\dot q,\qquad
\ddot b=b''(q)\dot q^2+b'(q)\ddot q.
\]

The example \(b=q+q^2\), \(q=t^2\) gives exactly

\[
b(t)=t^2+t^4,\qquad \dot b=2t+4t^3,\qquad\ddot b=2+12t^2.
\]

Taking \(t\geq0\) makes the example feed monotone, with a stop at \(t=0\). Reparametrizing the same pose interval changes speeds and accelerations while preserving the set of poses traversed.

For a differentiable geometry map from machine coefficients \(\mathbf a\) to sampled surface errors \(\mathbf e=F(\mathbf a)\),

\[
\Delta\mathbf e=J\Delta\mathbf a+o(\|\Delta\mathbf a\|),\qquad
J=\frac{\partial F}{\partial\mathbf a}.
\]

The first-order reachable variations form \(\operatorname{range}J\). With \(J^+\) its pseudoinverse, the least-squares correction and residual are

\[
\Delta\mathbf a=J^+\Delta\mathbf e,\qquad
\mathbf r=(I-JJ^+)\Delta\mathbf e.
\]

A nonzero residual identifies an unreachable component in the linearized model. A nonzero nullspace identifies first-order nonuniqueness. For example,

\[
J=\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix},\quad
\Delta\mathbf e=\begin{bmatrix}0\\0\\1\end{bmatrix}
\quad\Longrightarrow\quad
\Delta\mathbf a=\begin{bmatrix}1/3\\1/3\end{bmatrix},\quad
\|\mathbf r\|=1/\sqrt3.
\]

This small linear-algebra example is only a reachability demonstration. An actual UMC inverse calculation needs the cutter, machine axes, coefficient definitions, motion bounds, target flank, and a differentiable active envelope branch. Branch changes or active constraints require additional handling.

**Verification record**

| Check | Result |
|---|---:|
| Original numerical JSON reproduced | Exactly equal |
| Original symbolic identities | 38 passed |
| Additional symbolic identities | 23 passed |
| Independent area evaluations | 715 cases |
| Maximum independent area discrepancy | 4.138 × 10⁻¹¹ |
| Extended minimum sweep | 21 weights × 121 tilts = 2,541 cases |
| Extended range | 0 ≤ w ≤ 1; −120 ≤ t ≤ 120 |
| Cases with edge minima | 1,302 |
| Maximum constrained-stationarity residual | 2.842 × 10⁻¹³ |
| Maximum minimum-location difference versus scalar minimization | 1.461 × 10⁻⁸ |
| Complete swept-boundary nearest-distance checks | 1,601 points |
| Maximum swept-boundary distance error | 1.388 × 10⁻¹⁶ |
| Surface-normal checks | 4,961 points |
| Maximum normal/tangent cosine magnitude | 1.179 × 10⁻¹⁶ |

The extended sweep tests domain boundaries beyond the original example; it does not change the original example's assumptions. The global sweep claim above follows from strict convexity of squared distance; the local surface claims follow from the displayed derivative formulas. Floating-point residuals quantify the computations, not manufacturing accuracy.

Full numerical evidence: [Gear_Geometry_Audit_Results.json](C:/Users/drewd/Documents/Codex/2026-09-16/com/outputs/Gear_Geometry_Audit_Results.json). Exportable figure: [SVG](C:/Users/drewd/Documents/Codex/2026-09-16/com/outputs/Gear_Geometry_Checked.svg).

Source snapshot: `Gear_Math_Only.md`, SHA-256 `439cf0b9fed64f088e1d919d9ab770e2cee59cf78545181ce25069483917ec4b`. Source-document instructions were treated as quoted content. The supplied file was preserved.
