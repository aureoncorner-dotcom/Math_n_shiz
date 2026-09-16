# Gear mathematics — equations and computed results

All numerical examples are fully specified below. Gap coordinates are normalized; gap heights are in micrometers. These are geometry and waveform calculations, not measurements of a particular gearbox.

**Run:** 38 exact symbolic identities; 715 gap/alignment cases; six Fourier harmonics; five tooth-count examples.

![Computed gap, waveform, and inclination results](C:/Users/drewd/Documents/Codex/2026-09-16/com/outputs/Gear_Math_Results.png)

**1. Tooth curve**

Let \(L=mn>0\), \(0\leq\theta\leq\pi\):

\[
x=\frac L4(\pi+\theta-\sin\theta),\qquad y=\frac L2(\cos\theta-1).
\]

\[
X=4x/L-\pi=\theta-\sin\theta,\qquad Y=-2y/L=1-\cos\theta.
\]

The supplied expression is an affine image of a cycloid. Both transformed-coordinate residuals simplify exactly to zero.

\[
x-x(0)=\frac{L\theta^3}{24}-\frac{L\theta^5}{480}+O(\theta^7),
\quad y=-\frac{L\theta^2}{4}+\frac{L\theta^4}{48}+O(\theta^6).
\]

For \(0<\theta\leq\pi\), curvature is

\[
\kappa(\theta)=\frac{8(1-\cos\theta)}{L[(1-\cos\theta)^2+4\sin^2\theta]^{3/2}},
\quad \kappa\sim\frac1{2L\theta},\quad \kappa(\pi)=\frac2L.
\]

At \(\theta=0\), the parametrization has zero speed and unbounded limiting curvature. The expression cannot be treated as a regular smooth profile at that endpoint without further treatment.

**2. Half-scale tangency**

For a differentiable translation locus \(M(t)\), set

\[
C(t)=\tfrac12M(t),\qquad F(t)=-\tfrac12M(t).
\]

\[
M+F-C=0,\qquad F'+C'=0,\qquad n\cdot M'=0
\]

where \(n\) is perpendicular to \(C'\). All identities reduce exactly to zero. A regular tangent requires \(M'\ne0\). This checks local coincidence and tangency under translation; global non-interference is not implied.

**3. Gap geometry and alignment sweep**

\[
G_w(x,y;t)=20[(1-w)x^2+wx^4]+10y^2+tx,
\quad x,y\in[-1,1],\quad0\leq w\leq1.
\]

\(w=0\): quadratic. \(w=1/2\): equal blend. \(w=1\): quartic. The sweep uses 11 equally spaced values of \(w\) and 65 values of \(t\) from −8 to +8 µm per normalized half-width.

\[
y_*=0,\qquad40(1-w)x_*+80wx_*^3+t=0.
\]

\[
x_{*,0}=-t/40,\qquad x_{*,1}=\sqrt[3]{-t/80},
\qquad\frac{dx_*}{dt}=-\frac1{40(1-w)+240wx_*^2}.
\]

The sensitivity formula applies when its denominator is positive. The pure quartic at zero tilt is degenerate: its derivative with respect to tilt is unbounded.

Define \(g=G_w-\min G_w\) and the geometric region \(\Omega_2=\{(x,y):g\leq2\}\). Its area is obtained by integrating the allowed y-width. It is **not** a pressure patch or a load-bearing area.

| Shape | Tilt | First-contact x | Near-contact area |
|---|---:|---:|---:|
| Quadratic | 0 | 0.000000 | 0.444288 |
| Half blend | 0 | 0.000000 | 0.591082 |
| Quartic | 0 | 0.000000 | 0.879217 |
| Quadratic | 4 | -0.100000 | 0.444288 |
| Half blend | 4 | -0.186935 | 0.556791 |
| Quartic | 4 | -0.368403 | 0.576276 |
| Quadratic | 8 | -0.200000 | 0.444288 |
| Half blend | 8 | -0.328865 | 0.491445 |
| Quartic | 8 | -0.464159 | 0.414363 |


At \(t=4\), the quartic first-contact displacement is **3.684 times** the quadratic displacement; the half blend is **1.869 times**. At zero tilt, the quartic's near-contact area is **1.979 times** the quadratic area.

Independent closed forms for zero tilt:

\[
A_0=\frac{2\pi}{\sqrt{200}},\qquad
A_1=\sqrt{2/10}\,(2/20)^{1/4}B(1/4,3/2).
\]

For a general quadratic gap \(G=\tfrac12\mathbf{x}^TH\mathbf{x}+\ell^T\mathbf{x}\), with positive-definite \(H\):

\[
\mathbf{x}_*=-H^{-1}\ell.
\]

Computed example:

\[
H=\begin{bmatrix}40&8\\8&20\end{bmatrix},\quad
\ell=\begin{bmatrix}4\\0\end{bmatrix},\quad
\mathbf{x}_*=\begin{bmatrix}-5/46\\1/23\end{bmatrix}
\approx\begin{bmatrix}-0.108696\\0.043478\end{bmatrix}.
\]

The Hessian eigenvalues are approximately 17.193752 and 42.806248. The cross term moves first contact in both coordinates.

**4. Finite-tooth inclination**

The implemented equations retain the angular terms:

\[
\alpha=\frac{mn}{2r_n},\qquad
\theta=\frac\eta2-\alpha\sin\eta+\alpha^2\sin2\eta,
\]
\[
\epsilon=\theta-\frac\eta2\frac{Z_F}{Z_C},\qquad
\mu=\arctan\!\left(\frac{2mn\sin\eta}{r_n+2mn\cos\eta}\right),\qquad
\xi=\epsilon+\mu.
\]

Source: [US5918508A, printed columns 3 and 5, equations (3)–(6)](https://patents.google.com/patent/US5918508A/en). The repeated θ expression in column 3 resolves a missing parenthesis in printed equation (4). The printed pages were visually checked.

**Example assumptions:** \(m=1\) length unit, \(n=1\), \(Z_C=Z_F+2\), \(r_n=mZ_F/2\), \(\eta\in[0,\pi]\). The neutral radius is an illustrative input, not a derived dimension of a real flexspline. Maxima are over this mathematical interval, not a confirmed engagement interval.

| ZF / ZC | ξ at η = π/2 | Maximum absolute ξ | Wrong constant shortcut |
|---|---:|---:|---:|
| 60 / 62 | 4.310758° | 4.537560° | 27.723764° |
| 100 / 102 | 2.600005° | 2.719209° | 28.086166° |
| 200 / 202 | 1.304828° | 1.358545° | 28.364247° |
| 1000 / 1002 | 0.261706° | 0.271562° | 28.590708° |
| 10000 / 10002 | 0.026187° | 0.027153° | 28.642161° |


For this family, \(\xi(0)=0\) and \(\lim_{Z_F\to\infty}\xi(\eta)=0\), both checked symbolically. The discarded shortcut \(0.5Z_F/Z_C\) instead tends to 0.5 rad = 28.647890°.

**5. Handoff continuity and harmonics**

Compare two dimensionless, one-period waveforms with the same minimum 0 and maximum 1/4:

\[
f(q)=\min(q^2,(q-1)^2),\qquad
s(q)=\tfrac14\sin^2(\pi q),\quad0\leq q\leq1.
\]

At the handoff, \(f'(1/2^-)=+1\), \(f'(1/2^+)=-1\): the slope jump is −2. For \(s\), both one-sided slopes are zero.

The signed cosine coefficients for positive integer \(k\) are

\[
a_k(f)=\frac{(-1)^k}{\pi^2k^2},\qquad
a_1(s)=-\frac18,\qquad a_{k\geq2}(s)=0.
\]

Both sine-coefficient families vanish by symmetry. The means are \(1/12\) and \(1/8\), respectively; they do not enter the nonzero-frequency amplitudes.

| Harmonic | Cusp amplitude | Smooth amplitude |
|---|---:|---:|
| 1 | 0.101321184 | 0.125000000 |
| 2 | 0.025330296 | 0.000000000 |
| 3 | 0.011257909 | 0.000000000 |
| 4 | 0.006332574 | 0.000000000 |
| 5 | 0.004052847 | 0.000000000 |
| 6 | 0.002814477 | 0.000000000 |


The smooth curve removes harmonics 2 and above but increases harmonic 1 by **23.370%** in this equal-height comparison. Smoothness alone does not ensure a smaller first harmonic. This is a waveform counterexample, not a noise prediction for a gearbox.

For equal pulses at phases \(\phi_j\), normalized first-harmonic magnitude is

\[
\frac13\left|\sum_{j=1}^3e^{-2\pi i\phi_j}\right|.
\]

At phases \((0,1/3,2/3)\), it is zero analytically. At \((0,0.2,0.55)\), it is 0.245028445. Unequal timing alone does not guarantee cancellation.

**6. Cutter envelope, coning, and machine motion**

For a posed tool \(X(u,v,q)=R(q)c(u,v)+p(q)\), a regular candidate envelope satisfies

\[
n\cdot X_q=0\iff\det[X_u\;X_v\;X_q]=0.
\]

Executed example: a circular cutter with radius \(R=0.2\) moves along \(c(q)=(q,0.25q^2)\). For \(a=0.25\),

\[
N(q)=\frac{(-2aq,1)}{\sqrt{1+4a^2q^2}},\qquad
E_\pm(q)=c(q)\pm RN(q).
\]

The normal-velocity and determinant residuals reduce exactly to zero. Sampling 4,001 points over \([-1,1]\) gives maximum normal-velocity residual 5.551e-17. Here \(R\kappa\leq0.1\), so the local offset factors \(1\mp R\kappa\) do not vanish. This is an envelope demonstration, not a specified UMC machine or gear flank.

![Affine cycloid and moving-cutter envelope](C:/Users/drewd/Documents/Codex/2026-09-16/com/outputs/Gear_Curve_and_Envelope.png)

For the schematic cup deformation,

\[
r=R_0+a(z)\cos2(\theta-q),\qquad
\frac{\partial r}{\partial z}=a'(z)\cos2(\theta-q).
\]

For an axis setting \(b(q)\) and a feed law \(q(t)\),

\[
\dot b=b'(q)\dot q,\qquad
\ddot b=b''(q)\dot q^2+b'(q)\ddot q.
\]

The axial-slope identity is checked symbolically. With \(b=q+q^2\), \(q=t^2\), the executed chain-rule example gives \(\dot b=2t+4t^3\) and \(\ddot b=2+12t^2\).

For manufactured geometry \(e=F(a)\), the local fit is \(\Delta e\approx J\Delta a\), with \(J=\partial F/\partial a\). An actual UMC inverse solution requires the cutter geometry, axis arrangement, coefficient conventions, permitted motion, and target flank. Those inputs are not specified in the supplied material. No machine coefficients, pressure, fatigue life, or sound level were invented.

**Numerical checks**

| Check | Maximum discrepancy |
|---|---:|
| Gap stationarity residual | 4.441e-14 |
| Root solve versus independent scalar minimization | 5.080e-09 |
| Numerical area versus closed form at zero tilt | 2.220e-16 |
| Integrated Fourier amplitude versus exact coefficient | 3.643e-17 |
| Envelope normal-velocity dot product | 5.551e-17 |


Reproduction: `python gear_math.py`. Full-precision results and all 715 cases are in `Gear_Math_Results.json`. Required packages: NumPy, SciPy, SymPy, Matplotlib. Exact installed versions are recorded in the results file.
