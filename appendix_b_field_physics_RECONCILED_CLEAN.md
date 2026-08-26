Appendix B

Pre-Run Parameter, Statistical, Fit, Resource, and Immutable-Output Freeze Card

Protocol: Simulation Protocol v0.3-RC1
Companion: Appendix A — Three-Axis Fixed-Holonomy Sector Construction
Appendix status: Structural freeze candidate
Execution status: Not frozen until the generated point tables, production-length table, software fingerprint, and manifest root are completed and hashed
Purpose: Freeze every parameter set, lattice ladder, chain rule, random-number rule, thermalization criterion, stopping rule, fit family, calibration tolerance, verdict condition, resource ceiling, and raw-output convention before target production observables are opened.

All literature benchmark numbers in this appendix are inherited from the main protocol. They are calibration targets, not re-derived claims.

---

B.0. Freeze Boundary

Appendix B separates three classes of information.

B.0.1 Frozen scientific choices

The following are fixed by this appendix:

- microscopic model branches;
- boundary and holonomy conventions;
- gauge couplings;
- anisotropy couplings;
- lattice-size ladders;
- initial coupling brackets;
- deterministic refinement algorithms;
- chain counts;
- RNG algorithm;
- seed derivation;
- thermalization tests;
- autocorrelation estimator;
- blocking and resampling rules;
- reweighting admissibility;
- fit families;
- L_{\min} ladders;
- calibration tolerances;
- first-order diagnostics;
- Q1, Q2, and Q3 verdict rules;
- resource ceilings;
- raw-data schema;
- immutable-output procedure.

None of these may be altered after the execution root is created.

B.0.2 Pilot-filled machine quantities

The following may be measured during calibration-only blind pilots:

- wall time per sweep;
- memory consumption;
- acceptance rates;
- autocorrelation times;
- estimator variances;
- winding-sector transition rates;
- replica-exchange acceptance;
- resulting production lengths calculated by the frozen rule in §B.7.

The pilot system may calculate these quantities internally, but it must not display:

- Q1 fitted exponents;
- comparisons between the charge-two and ordinary-vector hypotheses;
- Q3 anisotropy trends across L;
- Q2 asymptotic direction;
- first-order verdicts at target production points.

B.0.3 Pre-execution failure rule

If blind timing pilots show that the frozen ladder cannot be completed under the resource ceiling, the project must stop before target production.

A reduced ladder requires a new protocol version and new hash.

After target production begins, resource exhaustion produces an unresolved result. It does not permit retrospective removal of expensive sizes or observables.

---

B.1. Canonical Branch Identifiers

Every run must carry exactly one branch identifier.

Identifier| Microscopic model| Representation| Boundary/sector| Primary role
"V-DUAL-FULL"| Villain| Dual| Fully link-summed PBC| CKT and pure-gauge calibration
"C-DUAL-FULL"| Cosine| Exact dual| Fully link-summed PBC| Stage-B Q1 production
"C-DIR-PBC"| Cosine| Direct| Full periodic gauge ensemble| Direct cross-validation
"C-DIR-XY0"| Cosine/XY| Direct| Trivial flat holonomy| Pure-XY calibration
"V-FH-000"| Villain| Dual fixed-holonomy| $Z_{000}$ with explicit $q\in\mathbb Z_2^3$| Canonical Q2/CKT fixed-holonomy calibration
"C-FH-000"| Cosine| Dual fixed-holonomy| $Z_{000}$ with explicit $q\in\mathbb Z_2^3$| Conditional Q2 production
"C-DIR-FH"| Cosine| Direct fixed-holonomy| $Z_h$, $h\in\mathbb Z_2^3$| Independent $Z_{e_\alpha}/Z_{000}$ ratio validation
"V-CKT-AX-Z"| Villain| Reconstructed axial comparator| One-axis $z$ comparator only| Literature-validation comparator; never canonical Q2
"C-DIR-H6"| Cosine| Direct| Full periodic gauge ensemble| Stage-C Q3 production
"POTTS-AF3"| AF three-state Potts| Direct spins| Fully periodic bulk| Global six-state control

The fully link-summed branches satisfy the mod-two homology projection established in Appendix A. Accordingly,

[
\boxed{
\texttt{V-DUAL-FULL}
\text{ and }
\texttt{C-DUAL-FULL}
\text{ do not report }f_{\rm odd}^{(\alpha)}.
}
]

Only the Appendix-A-validated three-axis fixed-holonomy ensemble

[
\boxed{Z_{\rm FH}=Z_{000}}
]

carries the canonical Q2 sector statistic. The reconstructed CKT axial branch is a comparator only and may not replace $Z_{000}$ in a Q2 verdict.

---

B.2. Coupling and Observable Conventions

The cosine production action is

[
H_{\cos}

-J\sum_{\langle ij\rangle}
\sigma_{ij}\cos(\theta_i-\theta_j)
-\kappa\sum_pB_p
-h_6\sum_i\cos6\theta_i.
]

Define

[
t=\tanh\kappa.
]

The physical field is

[
\Phi_i=e^{2i\theta_i}.
]

The physical susceptibility is normalized as

[
\boxed{
\chi_2

N\left\langle|m_\Phi|^2\right\rangle

\sum_rG_2(r),
}
]

where

[
m_\Phi=\frac1N\sum_i\Phi_i.
]

The integer winding convention at h_6=0 is

[
\boxed{
W_\alpha

\frac1L
\sum_{\ell\parallel\alpha}I_\ell.
}
]

The dimensionless winding quantity is

[
\boxed{
R_W

\frac13
\sum_{\alpha=x,y,z}
\langle W_\alpha^2\rangle
}
]

unless an explicitly ensemble-labeled directional fixed-holonomy or comparator observable is identified.

The Binder ratio is

[
\boxed{
U_4

1-
\frac{\langle|m_\Phi|^4\rangle}
{2\langle|m_\Phi|^2\rangle^2}.
}
]

A dual U_4 estimator is not assumed.

For dual Stage-B runs, the primary locator pair is

[
\boxed{
R_\xi,\ R_W.
}
]

For direct runs, the primary locator pair is

[
\boxed{
R_\xi,\ U_4.
}
]

A dual Binder ratio may enter only after a four-point estimator has been independently derived and validated.

---

B.3. Hard Resource Ceiling

The baseline resource ceiling is:

[
\boxed{
20{,}000\ \text{physical CPU core-hours}.
}
]

The corresponding baseline assumes up to 16 physical CPU cores.

The storage ceiling is

[
\boxed{
2.0\ {\rm TB}
}
]

for raw time series, checkpoints, histograms, correlators, manifests, and immutable derived outputs.

The maximum resident working-memory allowance is

[
\boxed{
112\ {\rm GiB}.
}
]

The remaining physical memory is reserved for the operating system, filesystem cache, and failure-safe checkpointing.

Maximum lattice sizes are:

[
\boxed{
L_{\max}^{\rm direct}=128,
}
]

[
\boxed{
L_{\max}^{\rm direct,Q2}=96,
}
]

[
\boxed{
L_{\max}^{\rm dual}=192.
}
]

The baseline budget does not assume GPU acceleration.

A GPU implementation may replace the CPU kernel only if, before execution freeze, it passes:

- bitwise or statistical reproducibility tests;
- direct comparison with the CPU implementation;
- detailed-balance tests;
- small-volume tests;
- and a new software/hardware hash.

Introducing a materially different GPU kernel after production begins creates a new execution branch and invalidates pooled timing assumptions.

---

B.4. Random-Number Architecture

B.4.1 Generator

Use

[
\boxed{
\texttt{Philox4x32-10}.
}
]

No implementation-defined default generator is permitted.

B.4.2 Master seed

For every chain, define the 128-bit master seed as the first 128 bits of

[
\boxed{
{\rm SHA256}
\left(
H_P
\Vert
H_A
\Vert
H_B
\Vert
H_C
\Vert
{\rm branch}
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
{\rm chain_id}
\right),
}
]

where:

- H_P is the main-protocol hash;
- H_A is the Appendix-A hash;
- H_B is the Appendix-B hash;
- H_C is the code-commit hash.

Numeric parameters are encoded using their exact stored decimal strings, not platform-dependent binary formatting.

B.4.3 Domain-separated streams

The following operations use domain-separated Philox streams:

- rotor proposals;
- link proposals;
- cube proposals;
- plaquette-current proposals;
- even worms;
- odd worms;
- global membrane moves;
- replica exchange;
- bootstrap resampling;
- synthetic GOF generation.

The stream key is

[
{\rm SHA256}({\rm master\ seed}\Vert{\rm stream\ label}).
]

No stream is reused between chains or algorithmic functions.

B.4.4 Checkpoint state

Every checkpoint stores:

- complete configuration;
- complete RNG counter and key;
- sweep number;
- measurement number;
- accumulated histogram state;
- worm state, if a checkpoint occurs between completed macro-sweeps;
- file checksum.

Production checkpoints occur only between completed compound or macro-sweeps.

A resumed run must reproduce an uninterrupted reference run bit for bit through the next 1,024 scalar measurements.

---

B.5. Chain Counts and Initial Conditions

Run class| Independent chains
Coarse locator scan| 4
Bisection/refinement scan| 4
Calibration confirmation| 8
Stage-B Q1 production| 8
Stage-C Q3 production| 8
Fixed-holonomy Q2 dual production| 8
Direct fixed-holonomy ratio validation| 8
Each thermodynamic-integration / free-energy-ratio ladder| 2 independent ladders
First-order equal-weight confirmation| 8

B.5.1 Direct starts

For every eight-chain direct production point:

- four chains use a hot start;
- four chains use a cold start.

Hot start:

- independent uniform $\theta_i\in[0,2\pi)$;
- independent allowed gauge links;
- any required fixed holonomy constraint imposed exactly as specified by Appendix A.

Cold start:

[
\theta_i=0,
\qquad
\sigma_\ell=+1
]

except where a nontrivial fixed-holonomy sector or magnetic twist is explicitly required.

B.5.2 Full-dual starts

For every full-dual point:

- four chains start from
  [
  I_\ell=0,\quad M_p=0;
  ]
- four chains start from a randomized valid configuration generated by $10^4$ unconstrained calibration macro-sweeps that are discarded.

The randomizer output must satisfy every exact divergence and parity test.

B.5.3 Fixed-holonomy Q2 starts

For canonical $Z_{000}$ Q2 production, every chain stores

[
q=(q_x,q_y,q_z)\in\mathbb Z_2^3.
]

The eight production chains begin one-per-sector in the deterministic order

[
000,001,010,011,100,101,110,111.
]

Each initial current configuration must satisfy

[
\nabla\!\cdot I=0,
\qquad
I+M+\Gamma q=0\pmod2.
]

The Appendix-A mixing validation separately requires an all-$q=000$ start ensemble and an evenly distributed eight-sector start ensemble to converge to compatible stationary estimates. That validation is not replaced by the production initialization rule.

Initial $q$ must not determine the final chain label used in pooled analysis.

---

B.6. Sweep Definitions and Measurement Cadence

B.6.1 Direct compound sweep

One direct compound sweep contains:

1. one rotor Metropolis proposal per site;
2. one gauge-link proposal per dynamical link;
3. five rotor over-relaxation proposals per site;
4. one global holonomy proposal per direction every ten compound sweeps when the ensemble permits it.

At h_6\neq0, every over-relaxation move receives the required Metropolis correction.

B.6.2 Full-dual macro-sweep

One full-dual macro-sweep contains:

1. L^3 cube attempts;
2. 3L^3 coupled plaquette-current attempts;
3. completed even worms until cumulative worm length is at least 3L^3;
4. one noncontractible membrane-sheet proposal in each orientation.

B.6.3 Fixed-holonomy Q2 macro-sweep

One canonical $Z_{000}$ Q2 macro-sweep is the Appendix-A definition:

1. $L^3$ cube attempts;
2. $3L^3$ coupled plaquette-current attempts;
3. completed even worms until cumulative accepted path length is at least $3L^3$;
4. one randomly selected noncontractible closed-sheet attempt;
5. one sector-move attempt in each axis, $x,y,z$, in a uniformly shuffled order.

Every accepted state must satisfy

[
\nabla\!\cdot I=0,
\qquad
I+M+\Gamma q=0\pmod2.
]

No odd axial worm or vertical-column loop belongs to the canonical production kernel. Those moves are confined to the explicitly labeled `V-CKT-AX-Z` comparator when reproducing the literature implementation.

B.6.4 Scalar cadence

Record scalar observables after every completed compound or macro-sweep:

- energy components;
- matter derivative;
- gauge derivative;
- anisotropy derivative;
- R_W;
- |m_\Phi|^2;
- |m_\Phi|^4;
- A_3^\Phi;
- H_6;
- A_3^\Phi H_6;
- n_6;
- plaquette occupation;
- acceptance rates;
- winding and sector labels.

B.6.5 Expensive-observable cadence

Record or accumulate the following every four completed sweeps:

- structure factors;
- R_\xi;
- direct spatial correlators;
- fixed-separation G_2;
- the canonical Q2 charge-one confinement estimator;
- CKT axial charge-one correlators only when the labeled comparator is scheduled;
- angular histograms;
- energy and order-parameter histograms.

Worm endpoint histograms are accumulated continuously over completed worms and written at every checkpoint.

B.6.6 Checkpoint cadence

Write an atomic checkpoint every

[
\boxed{
1{,}024
}
]

completed compound or macro-sweeps.

The old checkpoint is retained until the new checkpoint passes its checksum.

---

B.7. Blind-Pilot and Production-Length Rule

B.7.1 Pilot visibility

The pilot controller may access estimator means and variances internally.

The analyst-facing report displays only:

- timing;
- memory;
- acceptance;
- \widehat\tau_{\rm int};
- estimated required sweeps;
- convergence status;
- reweighting overlap;
- sector transition count.

Cross-size target trends remain masked.

B.7.2 Initial pilot length

For each intended branch and size, run two pilot chains with:

[
2^{12}
]

thermalization sweeps followed by

[
2^{14}
]

measurement sweeps.

If the autocorrelation criterion below is not satisfied, extend both pilot chains by successive factors of two.

The pilot stops at the first length satisfying

[
N_{\rm pilot,chain}
\ge
200\widehat\tau_{\max}
]

and at least 64 candidate analysis blocks.

The pilot ceiling is

[
\boxed{
2^{20}
}
]

measurement sweeps per chain.

Failure to estimate autocorrelation below this ceiling is an algorithmic or mixing failure.

B.7.3 Precision targets

Observable| Acquisition target
R_\xi| absolute SE \le0.002
U_4| absolute SE \le0.002
R_W| absolute SE \le0.005
\chi_2| relative SE \le0.005
G_2(L/4)| relative SE \le0.010
G_2(L/2)| relative SE \le0.015
A_3^\Phi| absolute SE \le0.003
D_6| absolute SE \le0.005
f_{\rm odd}^{(\alpha)} for each axis| absolute SE \le0.010, plus Appendix-A round-trip/ESS rule
Canonical $Z_{000}$ charge-one confinement estimator| relative SE \le0.02 where its signal exceeds 5\sigma; CKT $C_1^{\rm ax}$ is comparator-only
Fixed-holonomy ratio integrand, when a $\lambda$ path is used| absolute SE \le0.002 after the frozen normalization
Twist integrand divided by stack area| absolute SE \le0.002

A relative target is not applied when the pilot mean is statistically compatible with zero. The corresponding absolute target is used instead.

B.7.4 Production-length calculation

Let:

- S_{\rm pilot} be the total number of pooled pilot measurement sweeps;
- \widehat{\rm SE}_{O,\rm pilot} be the blocked pilot standard error;
- \epsilon_O be the acquisition target;
- C be the number of production chains.

For every required observable,

[
S_{O,\rm req}

S_{\rm pilot}
\left(
\frac{
\widehat{\rm SE}_{O,\rm pilot}
}{
\epsilon_O
}
\right)^2.
]

Define

[
S_{\rm req}

\max_O S_{O,\rm req}.
]

The frozen per-chain production length is

[
\boxed{
N_{\rm prod}

2^{
\left\lceil
\log_2
\left[
\max
\left(
2^{16},
\frac{2S_{\rm req}}{C},
400\widehat\tau_{\max}
\right)
\right]
\right\rceil
}.
}
]

The factor two is a fixed variance-safety factor.

For Q2, include the slowest-axis sector-round-trip estimate:

[
N_{\rm RT}

\frac{
200
}{
\widehat r_{\rm RT}
},
]

where $\widehat r_{\rm RT}$ is the minimum, over $x,y,z$, of the pilot effective round trips per sweep for $q_\alpha:0\to1\to0$.

Then replace the maximum above by

[
\max(\cdots,N_{\rm RT}).
]

The hard per-chain production ceiling is

[
\boxed{
N_{\rm prod}\le2^{25}.
}
]

If the calculated requirement exceeds that ceiling or the global resource cap, execution cannot be frozen under this parameter card.

B.7.5 Generated production table

The pilot controller writes:

production_lengths.csv

with one row for every branch, parameter point, lattice size, and chain class.

Required columns:

branch
stage
L
kappa
t
J
h6
sector
chains
thermalization_sweeps
production_sweeps
measurement_stride
tau_max_pilot
precision_limiter
estimated_core_hours
estimated_storage_bytes
pilot_hash

This file is hashed before target production begins.

B.7.6 One permitted blind extension

After the frozen production length is completed, the controller may apply exactly one extension of

[
\boxed{
2N_{\rm prod}
}
]

if, while target directions remain masked, any of the following occurs:

- split \widehat R>1.01;
- required ESS fails;
- achieved standard error exceeds 1.25\epsilon_O;
- any Q2 axis fails the Appendix-A frozen round-trip/ESS gate.

All chains at that point are extended equally.

No second extension is permitted.

Failure after the extension gives:

[
\boxed{
\text{INSUFFICIENT MIXING OR PRECISION}.
}
]

The relevant scientific verdict is then unresolved.

---

B.8. Thermalization and Convergence

B.8.1 Frozen thermalization length

Using the pilot autocorrelation estimate, define

[
\boxed{
N_{\rm therm}

2^{
\left\lceil
\log_2
\left[
\max
\left(
2^{14},
100\widehat\tau_{\max}
\right)
\right]
\right\rceil
}.
}
]

For fixed-holonomy Q2 chains, thermalization must additionally contain at least ten effective $0\to1\to0$ round trips in every q-axis indicator.

B.8.2 Convergence observables

Direct chains are checked using:

- matter energy;
- gauge energy;
- |m_\Phi|^2;
- R_\xi;
- U_4;
- H_6 when applicable.

Dual chains are checked using:

- current action;
- plaquette occupation;
- \chi_2;
- R_\xi;
- R_W;
- the three q-bit indicators for Q2.

B.8.3 Required convergence tests

Before production begins:

[
\boxed{
\widehat R_{\rm split}\le1.01
}
]

for every convergence observable.

Also require:

[
\boxed{
{\rm bulk\ ESS}\ge400
}
]

and

[
\boxed{
{\rm tail\ ESS}\ge200
}
]

for the pooled thermalization diagnostics.

For every observable, the hot-start and cold-start final-quarter means must differ by less than two combined standard errors.

The mean of the second half of thermalization must differ from the final quarter by less than two combined standard errors.

B.8.4 Thermalization failure

One automatic doubling of thermalization is allowed before production.

If convergence still fails, the point does not enter production.

No production measurements are reclassified later as additional thermalization.

---

B.9. Autocorrelation, Blocking, and Resampling

B.9.1 Autocorrelation estimator

Use the \Gamma-method.

For each scalar observable, choose the first self-consistent window W satisfying

[
\boxed{
W\ge6\widehat\tau_{\rm int}(W).
}
]

The maximum allowed window is

[
W_{\max}=N/10.
]

Failure to find a stable window is reported.

B.9.2 Master autocorrelation time

For each run point define

[
\boxed{
\tau_{\max}

\max_O\widehat\tau_{\rm int,O}
}
]

over every primary observable available in that branch.

For Q2, include all three indicators $1[q_\alpha=1]$ and the eight-state $q$ residence process in this maximum.

B.9.3 Block length

Set the analysis block length to

[
\boxed{
B

2^{
\left\lceil
\log_2
\left[
\max
\left(
32,
20\tau_{\max}
\right)
\right]
\right\rceil
}.
}
]

Incomplete final blocks are retained in raw data but excluded from block-bootstrap analysis.

B.9.4 Hierarchical bootstrap

Use

[
\boxed{
5{,}000
}
]

hierarchical bootstrap replicates.

For each replicate:

1. resample independent chains with replacement;
2. resample complete blocks within each selected chain;
3. reconstruct reweighted observables;
4. rerun critical-point interpolation;
5. rerun the complete frozen fit family;
6. store fitted parameters and verdict predicates.

Q2 winding counts are resampled as block-level counts, not as independent per-sweep Bernoulli trials.

B.9.5 Confidence intervals

Use the 2.5th and 97.5th percentiles of the hierarchical bootstrap distribution.

All stated intervals are therefore 95% bootstrap intervals unless explicitly labeled otherwise.

B.9.6 Fit covariance

Use the full bootstrap covariance across:

- observables;
- couplings;
- sizes;
- fixed-R_\xi interpolations.

When the covariance matrix is numerically singular, diagonalize it and remove modes satisfying

[
\boxed{
\lambda/\lambda_{\max}<10^{-10}.
}
]

The number of retained modes is reported with every fit.

An uncorrelated fit may be shown as a diagnostic but cannot carry the primary verdict.

---

B.10. Reweighting and Interpolation

B.10.1 Direct cosine model

Store

[
E_J

\sum_{\langle ij\rangle}
\sigma_{ij}\cos(\theta_i-\theta_j),
]

[
E_\kappa

\sum_pB_p,
]

and

[
H_6

\sum_i\cos6\theta_i.
]

The exact configuration reweighting factor is

[
\boxed{
\log w'

\log w

(J'-J)E_J
+
(\kappa'-\kappa)E_\kappa
+
(h_6'-h_6)H_6.
}
]

B.10.2 Villain dual

Store

[
S_I=\sum_\ell I_\ell^2
]

and

[
N_M=\sum_pM_p.
]

For normalized expectation values, the configuration-dependent reweighting factor is

[
\boxed{
\log w'

\log w

-\left(
\frac1{2J'}-\frac1{2J}
\right)S_I
+
N_M\log\frac{t'}{t}.
}
]

Any J-dependent overall Villain normalization must be restored for free-energy derivatives.

B.10.3 Exact cosine dual

For every measurement block store the sparse count map

[
N_q

#{\ell:|I_\ell|=q}.
]

Then

[
\boxed{
\log w'

\log w

\sum_{q\ge0}
N_q
\log
\frac{
\mathcal I_q(J')
}{
\mathcal I_q(J)
}
+
N_M\log\frac{t'}{t}.
}
]

No current magnitude may be silently clipped.

The sparse histogram contains every observed q and an explicit maximum-current field.

B.10.4 Reweighting admissibility

For normalized weights \widetilde w_a, define

[
N_{\rm eff}^{\rm rew}

\frac1{
\sum_a\widetilde w_a^2
}.
]

Reweighting is admissible only when

[
\boxed{
N_{\rm eff}^{\rm rew}
\ge0.30N_{\rm raw}
}
]

and

[
\boxed{
\max_a\widetilde w_a\le0.02.
}
]

Adjacent simulated points must produce overlapping action distributions.

A reweighted estimate failing either condition is discarded.

---

B.11. Calibration Parameter Table

B.11.1 Mandatory calibration ladder

ID| Branch| Couplings| Sizes| Frozen requirement
"CAL-A0"| Direct/dual exact tests| $t=0,0.3,0.7$; $J=0.20,0.46$; $h_6=0,0.02$| $L=2,3$| Exact constraints and enumeration
"CAL-A1"| Full-dual homology| $t=0,0.3,0.7$; $J=0.20,0.46$| $L=2,3,4,6$| Full ensemble equals $\mathcal Z_{000}$ and supplies no independent odd-homology observable
"CAL-A2"| Pure $Z_2$ gauge| $J=0$; $t=0.638$ through $0.646$ in steps of $0.001$| $8,12,16,24,32,48,64$| Reproduce $t_c=0.6419086649$
"CAL-A3"| Standalone cosine XY| $J=0.450$ through $0.458$ in steps of $0.001$; trivial holonomy| $8,12,16,24,32,48,64,96,128$| Reproduce $J_c=0.45416468$
"CAL-A4"| Villain CKT transition| $t=0.7$; $J=0.3305,0.3320,0.3330,0.3335,0.3340,0.3350,0.3360$| $8,12,16,24,32,48,64$| Reproduce $J_c=0.3335(3)$
"CAL-A5"| Villain CKT radius| $t=0.7,\ J=0.336$| $24,32,48,64,72,96,128,160,192$| Reproduce published charge-one/charge-two scale separation in the labeled comparator and compare with canonical $Z_{000}$ sector statistics
"CAL-A6"| Cosine first-order control| $\kappa=0.7$, $t=0.6043677771$; $J=0.496,0.500,0.504,0.508,0.512$| $8,12,16,24,32,48,64$| First-order package fires
"CAL-A7a"| Cosine direct/dual equality| $t=0.6640367703,0.7$; $J=0.45,0.46,0.47$; $h_6=0$| $4,6,8,12,16$| Common observables agree
"CAL-A7b"| Finite-$h_6$ equality| Same $t,J$; $h_6=0.02$| $4,6,8,12$| Conditional on charge-six algorithm
"CAL-A8"| AF Potts| $T=1.220$ through $1.232$ in steps of $0.001$, then $0.00025$ refinement| $8,12,16,24,32,48,64,96,128$| XY criticality and $Z_6$ locking
"CAL-Q2"| Three-axis fixed-holonomy transform and ratio tests| $t=0,0.3,0.7$; $J=0.20,0.336,0.46$| $2,3,4,6,8$| Appendix-A $Z_h\leftrightarrow\mathcal Z_q$ transform, ratio, translated-cycle, symmetry, and mixing gates pass

B.11.2 Calibration tolerances

Calibration| Pass condition
Exact divergence/parity/source neutrality| Zero violations
Walsh-Hadamard projector identities| Machine-exact on the $\mathbb Z_2^3$ character table
Full-dual projection| $Z_{\rm full}=\mathcal Z_{000}$ to the frozen exact/numerical tolerance
Pure-gauge $t_c$| Combined $3\sigma$ agreement and absolute error $\le0.0015$
Pure-XY $J_c$| Combined $3\sigma$ agreement and absolute error $\le0.0010$
CKT Villain $J_c$| Combined $3\sigma$ agreement and absolute error $\le0.0015$
CKT stiffness at $J=0.336$| Within $0.038\pm0.006$
CKT $R_2$ growth| Largest three sizes compatible with linear growth
CKT $R_1$ saturation| Plateau model beats linear-growth model by $\Delta{\rm AICc}\ge10$ on the final admissible sizes
First-order control| All §B.19 first-order predicates fire
Direct/dual common observables| Each within combined $3\sigma$; none beyond $4\sigma$
Joint direct/dual consistency| Bootstrap joint $p\ge0.01$
Fixed-holonomy ratio identity| For every axis, $1-2f_{\rm odd}^{(\alpha)}=Z_{e_\alpha}/Z_{000}$ within combined $3\sigma$
Fixed-holonomy ratio numerical precision| Relative error $\le0.005$, or absolute error $\le0.005$ near zero
Axis symmetry| Correlated three-axis consistency-test $p\ge0.05$ at isotropic couplings
Translated-cycle check| Correlated four-placement consistency-test $p\ge0.05$ at every blind validation point
AF-Potts critical point| Absolute error $\le0.001$ in the frozen convention
AF-Potts angular control| Critical harmonic decreases; ordered harmonic locks

Failure of a calibration branch blocks only the scientific stages depending on that branch.

For example, failure of finite-$h_6$ dual calibration does not block direct Q3.

---

B.12. Stage-B Q1 Production Table

All Stage-B points use

[
h_6=0.
]

B.12.1 Gauge points

Point| \kappa| t=\tanh\kappa| Initial J bracket
"P1"| 0.8000000000| 0.6640367703| [0.440,0.490]
"P2"| 0.8673005277| 0.7000000000| [0.440,0.490]
"P3"| 1.0000000000| 0.7615941560| [0.440,0.490]

The production size ladder is

[
\boxed{
L=
8,12,16,24,32,48,64,96,128.
}
]

The primary Stage-B representation is "C-DUAL-FULL".

Matched "C-DIR-PBC" confirmation runs are performed at:

[
\boxed{
L=12,24,48,96
}
]

for each gauge point at the final critical neighborhood.

B.12.2 Coarse locator grid

For each gauge point, run:

[
\boxed{
J=0.440,0.445,\ldots,0.490
}
]

on

[
L=12,16,24.
]

Only the dimensionless locator observables and histogram-quality diagnostics are opened.

Q1 exponent outputs remain masked.

B.12.3 Transition-bracket rule

A matter-transition bracket must satisfy:

1. a sign change in the difference of R_\xi between at least one adjacent size pair;
2. supporting crossing or convergence behavior in R_W;
3. no unresolved reweighting-overlap failure.

If the R_\xi and R_W brackets are disjoint, both brackets are retained and refined.

They may indicate:

- split transitions;
- strong crossover;
- or locator failure.

No single bracket is chosen by discretion.

B.12.4 Bisection rule

Refine every retained bracket on

[
L=16,24,32
]

using deterministic midpoint bisection until

[
\boxed{
\Delta J\le2\times10^{-4}.
}
]

Define the midpoint of the matter-ordering bracket as J_0.

B.12.5 Initial confirmation grid

For

[
L\le48,
]

begin with the five-point grid

[
\boxed{
J=J_0+m(0.00075),
\qquad
m=-2,-1,0,1,2.
}
]

For

[
L\ge64,
]

begin with the three-point grid

[
\boxed{
J=J_0+m(0.00075),
\qquad
m=-1,0,1.
}
]

The reduction at large $L$ is a preregistered resource amendment. It does not alter the mechanical extension rule below.

B.12.6 Mechanical grid extension

If the frozen target R_\xi^\star is not bracketed at a size, add one point at a time in the required direction using increments of

[
0.00075.
]

The maximum allowed extension is

[
\boxed{
|J-J_0|\le0.006.
}
]

The procedure is automatic and uses only R_\xi.

If the target remains unbracketed at the limit, that size is marked:

[
\boxed{
\text{FIXED-}R_\xi\text{ TRAJECTORY NOT REACHED}.
}
]

It cannot be replaced by an analyst-selected coupling.

B.12.7 Frozen point file

The finalized Stage-B grid is written to:

stageB_points.csv

and hashed before Q1 observables are unmasked.

---

B.13. Stage-C Q3 Production Table

Only "P1" and "P2" enter primary Stage C.

B.13.1 Field values

Primary critical fields:

[
\boxed{
h_6=0,\ 0.01,\ 0.02.
}
]

Negative-field controls:

[
\boxed{
h_6=-0.01,\ -0.02.
}
]

Nonlinearity sentinel:

[
\boxed{
h_6=0.04.
}
]

B.13.2 Size ladders

For h_6=0,0.01,0.02:

[
\boxed{
L=
8,12,16,24,32,48,64,96.
}
]

For h_6=-0.01,-0.02:

[
\boxed{
L=
8,12,16,24,32,48.
}
]

For h_6=0.04:

[
\boxed{
L=
8,12,16,24,32,48,64.
}
]

B.13.3 Fixed-R_\xi trajectory

For each gauge point, define

[
R_\xi^\star(t)
]

from the corresponding Stage-B h_6=0 branch.

For every nonzero h_6 and every size, determine J_L(h_6) from

[
\boxed{
R_\xi(J_L,h_6,L)

R_\xi^\star(t).
}
]

Initial search bracket:

[
\boxed{
J\in[J_c(t,0)-0.010,\ J_c(t,0)+0.010].
}
]

Coarse step:

[
0.0025.
]

After bracketing, bisect to width

[
2\times10^{-4}.
]

The initial confirmation grid is size dependent.

For

[
L\le32,
]

use

[
\boxed{
J=J_{L,0}+m(0.0005),
\qquad
m=-2,-1,0,1,2.
}
]

For

[
L\ge48,
]

use

[
\boxed{
J=J_{L,0}+m(0.0005),
\qquad
m=-1,0,1.
}
]

The same mechanical extension and reweighting rules as Stage B apply.

B.13.4 Zero-field response

At h_6=0, measure

[
\boxed{
D_6(L)

{\rm Cov}
\left(
a_3^\Phi,
H_6
\right),
}
]

where the configuration-level harmonic is

[
a_3^\Phi

\begin{cases}
\Re\left[(m_\Phi/|m_\Phi|)^3\right],
& |m_\Phi|>10^{-14},\[4pt]
0,
& |m_\Phi|\le10^{-14}.
\end{cases}
]

The numerical-zero convention must be identical in every implementation.

B.13.5 Ordered-locking runs

For every positive primary h_6, define

[
\boxed{
J_{\rm lock}(t,h_6)

1.02J_c(t,h_6).
}
]

Run

[
L=16,24,32,48,64,96.
]

The ordered-side coupling is not retuned after angular histograms are opened.

---

B.14. Conditional Stage-D Q2 Table

This stage is sealed until every Appendix-A fixed-holonomy validation gate passes.

All Q2 production uses

[
h_6=0.
]

Only "P1" and "P2" enter primary Q2.

B.14.1 Ordered-side coupling

For each gauge point,

[
\boxed{
J_{\rm Q2}=1.01J_c(t,0).
}
]

The multiplication uses the unrounded fitted $J_c$.

B.14.2 Canonical fixed-holonomy dual ladder

For the complete $q\in\mathbb Z_2^3$ distribution, the three axis-resolved

[
f_{\rm odd}^{(\alpha)}(L)=P_{Z_{000}}(q_\alpha=1),
]

winding statistics, and the Appendix-A-validated charge-one confinement estimator, use

[
\boxed{
L=24,32,48,64,96,128,160,192.
}
]

Branch:

`C-FH-000`

Every run stores $q_x,q_y,q_z$ explicitly. No one-axis axial statistic may substitute for these data.

B.14.3 Independent fixed-holonomy ratio validation

For each axis $\alpha$, determine

[
\boxed{
\frac{Z_{e_\alpha}}{Z_{000}}
}
]

independently of direct $q$-occupancy counting on

[
\boxed{
L=8,12,16,24,32,48,64,96.
}
]

using the preregistered positive-weight direct free-energy-ratio estimator frozen in the Appendix-A validation artifact and `parameter_card.yaml`.

If that estimator uses a $\lambda$ interpolation, retain all 17 windows

[
\lambda=0,\frac1{16},\ldots,1
]

but use

[
\boxed{2\text{ independent ladders per axis}}
]

rather than four. This is part of the pre-execution resource amendment.

The exact identity

[
\boxed{
f_{\rm odd}^{(\alpha)}=\frac12\left(1-\frac{Z_{e_\alpha}}{Z_{000}}\right)
}
]

must pass before Q2 can open.

B.14.4 CKT one-axis comparator

At the published Villain validation points, run the reconstructed `V-CKT-AX-Z` comparator required by Appendix A. It is a literature-validation branch only. Its $C_1^{\rm ax}$, odd-$z$ statistics, or seam conventions cannot replace the canonical three-axis $Z_{000}$ data.

B.14.5 Fredenhagen–Marcu ladder

Use

[
\boxed{
L=16,24,32,48,64,96.
}
]

The square contour has side

[
r=L/4.
]

All listed sizes are divisible by four.

B.14.6 Magnetic-twist ladder

Use

[
\boxed{
L=16,24,32,48,64,96.
}
]

Use two independent 17-replica ladders:

[
\lambda=0,\frac1{16},\ldots,1.
]

B.14.7 Q2 scale admissibility

A physical Q2 interpretation is admissible only when

[
\boxed{
L_{\max}\ge4\xi_{\rm conf}^{95\%,{\rm upper}}.
}
]

Failure produces:

[
\boxed{
\text{Q2 INCONCLUSIVE — QUASI-DECONFINED WINDOW NOT EXCLUDED}.
}
]

No Q2 production is required at "P3".

---

B.15. Critical-Point Fit Package

B.15.1 Scaling variable

Define

[
x=(J-J_c)L^{1/\nu}.
]

For every dimensionless locator R_a, fit

[
\boxed{
R_a(J,L)

R_a^\star
+a_{a1}x
+a_{a2}x^2
+
L^{-\omega}
\left(
b_{a0}+b_{a1}x
\right).
}
]

B.15.2 Branch-specific locator sets

For "C-DUAL-FULL":

[
a\in{R_\xi,R_W}.
]

For "C-DIR-PBC" and "C-DIR-H6":

[
a\in{R_\xi,U_4}.
]

A direct helicity observable may be added as a cross-check.

A dual U_4 may be included only after estimator validation.

B.15.3 Frozen fit families

Family| \nu| \omega| Correction
"C0-XY"| 0.6717| —| none
"C1-XY"| 0.6717| 0.789| included
"C2-NU"| free on [0.60,0.80]| 0.789| included
"C3-FULL"| free on [0.60,0.80]| free on [0.4,1.3]| included
"C4-FO"| 1/3| —| first-order alternative

No fixed-point amplitude is shared between differing boundary or holonomy ensembles.

B.15.4 L_{\min} ladder

Run every admissible fit using

[
\boxed{
L_{\min}

12,16,24,32,48.
}
]

A fit requires:

- at least four lattice sizes;
- at least four residual degrees of freedom.

A fit window not meeting both requirements is not reported as admissible.

B.15.5 Goodness of fit

Use correlated nonlinear least squares.

Compute a parametric-bootstrap goodness-of-fit p-value using

[
\boxed{
2{,}000
}
]

synthetic datasets generated from the fitted covariance model.

Interpretation:

[
p_{\rm GOF}\ge0.05
]

is acceptable,

[
p_{\rm GOF}<0.01
]

is strong rejection.

---

B.16. Fixed-R_\xi Interpolation

For every hierarchical bootstrap replicate:

1. fit the critical-point locator;
2. extract J_c and R_\xi^\star;
3. solve
   [
   R_\xi(J_L,L)=R_\xi^\star;
   ]
4. interpolate all Q1 or Q3 observables to J_L;
5. retain the covariance arising from the common solution.

A central fit and its bootstrap replicates must use the same reweighting-admissibility mask.

No failed bootstrap replicate is silently replaced.

If more than 10% of bootstrap replicates fail to bracket R_\xi^\star, that size is removed from the corresponding fixed-R_\xi fit and the removal is reported.

The L_{\min} family is not otherwise modified.

---

B.17. Q1 Charge-Sector Fit Package

The target charge-two dimension is

[
\boxed{
\Delta_2=1.23629,
}
]

giving

[
\boxed{
\kappa_2=3-2\Delta_2=0.52742.
}
]

The ordinary-vector alternative is

[
\boxed{
\Delta_1=0.519088,
}
]

giving

[
\boxed{
\kappa_1=3-2\Delta_1=1.961824.
}
]

B.17.1 Susceptibility family

At fixed R_\xi, fit

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

The additive background b_0 is mandatory.

Frozen exponent hypotheses:

"Q1-H2"

[
\kappa=0.52742.
]

"Q1-H1"

[
\kappa=1.961824.
]

"Q1-HFREE"

[
0\le\kappa\le3.
]

"Q1-HFO"

[
\kappa=3.
]

Each hypothesis is run with:

1. c=0;
2. c\neq0,\ \omega=0.789;
3. c\neq0,\ \omega\in[0.4,1.3].

"Q1-HFO" cannot carry a first-order verdict without the independent histogram package in §B.19.

B.17.2 Spatial-correlator family

Primary fractional separations are

[
\boxed{
s=\frac14,\frac12.
}
]

For sizes divisible by three, retain

[
s=\frac13
]

as a secondary point.

Average over all three lattice axes and both displacement signs.

Fit

[
\boxed{
G_2(sL,L)

L^{-2\Delta}
\left(
a_s+c_sL^{-\omega}
\right),
}
]

with:

- one common \Delta;
- separate amplitudes a_s,c_s;
- the same L_{\min} ladder.

Frozen hypotheses:

[
\Delta=1.23629,
]

[
\Delta=0.519088,
]

and

[
\Delta\text{ free on }[0.4,1.5].
]

B.17.3 Q1 support rule

Q1 is SUPPORTED only if all conditions hold:

1. the first-order package does not fire;
2. "Q1-H2" has
   [
   p_{\rm GOF}\ge0.05
   ]
   for at least three consecutive admissible L_{\min} windows, including the largest;
3. the free-\kappa 95% interval contains 0.52742;
4. that interval excludes 1.961824;
5. the best admissible charge-two fit beats the best ordinary-vector fit by
   [
   \Delta{\rm AICc}\ge10;
   ]
6. the free spatial-correlator interval contains 1.23629;
7. that interval excludes 0.519088;
8. the fitted exponent changes by less than one combined standard deviation across the final three admissible L_{\min} windows.

B.17.4 Q1 rejection rule

Q1 is REJECTED only if:

1. the charge-two target is outside the 95% interval in the final three admissible L_{\min} windows;
2. the target fit has p_{\rm GOF}<0.01 in those windows or loses by
   [
   \Delta{\rm AICc}\ge10;
   ]
3. at least one preregistered alternative fits acceptably;
4. susceptibility and spatial-correlator analyses agree on the rejection.

If ordinary-vector scaling passes these conditions, report:

[
\boxed{
\text{Q1 REJECTED — ORDINARY-VECTOR LANE SUPPORTED}.
}
]

B.17.5 Q1 unresolved rule

Every other outcome is

[
\boxed{
\text{Q1 UNRESOLVED}.
}
]

A visually appealing effective slope is not a verdict.

---

B.18. Q3 Anisotropy Fit Package

B.18.1 Primary critical harmonic

[
\boxed{
A_3^\Phi(L,h_6)

\left\langle
\cos[3\arg(m_\Phi)]
\right\rangle.
}
]

B.18.2 Zero-field response

At h_6=0,

[
\boxed{
D_6(L)

{\rm Cov}(a_3^\Phi,H_6).
}
]

Fit

[
\boxed{
D_6(L)

aL^{y_6}
\left(
1+cL^{-\omega}
\right).
}
]

Frozen families:

1. c=0;
2. \omega=0.789;
3. \omega\in[0.4,1.3].

B.18.3 Finite-field joint fit

Fit the positive and negative small fields jointly:

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

The sign of h_6 is retained.

The h_6=0.04 data are excluded from the primary fit unless the fitted cubic contribution is below 20% of the linear contribution over every included size.

They remain a mandatory nonlinearity diagnostic.

B.18.4 Sign-reversal test

At matched L and |h_6|, test

[
\boxed{
A_3^\Phi(L,-h_6)

-A_3^\Phi(L,+h_6).
}
]

Define the normalized discrepancy

[
Z_{\rm sign}

\frac{
A_3^\Phi(+h_6)+A_3^\Phi(-h_6)
}{
\sqrt{
{\rm Var}[A_3^\Phi(+h_6)]
+
{\rm Var}[A_3^\Phi(-h_6)]
}
}.
]

Require

[
|Z_{\rm sign}|\le2
]

for the pooled matched-field test.

B.18.5 Nonzero-asymptote alternative

At fixed positive h_6, fit

[
\boxed{
A_3^\Phi(L,h_6)

A_\infty(h_6)
+
cL^{-p},
\qquad
p>0.
}
]

B.18.6 Ordered locking

At J_{\rm lock}, fit

[
\boxed{
A_{3,\rm lock}^\Phi(L)

A_{\rm lock,\infty}
+
cL^{-p}.
}
]

Ordered locking is supported only when

[
\boxed{
A_{\rm lock,\infty}^{95%,{\rm lower}}>0.
}
]

B.18.7 Q3 support rule

Q3 irrelevance is SUPPORTED only when:

1. the upper 95% bound on y_6 from D_6 is below zero;
2. the upper 95% bound from the finite-field joint fit is below zero;
3. both conditions survive the final three admissible L_{\min} windows;
4. the nonzero critical asymptote model loses by
   [
   \Delta{\rm AICc}\ge10;
   ]
5. the sign-reversal test passes;
6. the ordered-locking lower bound is positive;
7. no first-order criterion fires.

B.18.8 Q3 rejection rule

Q3 is REJECTED when either:

- the lower 95% bound on y_6 is nonnegative in both primary fit lanes; or
- a stable nonzero critical asymptote is preferred by
  [
  \Delta{\rm AICc}\ge10
  ]
  across the final three L_{\min} windows.

B.18.9 Q3 unresolved rule

Every other outcome is

[
\boxed{
\text{Q3 UNRESOLVED}.
}
]

A nonzero local dual source density cannot change that verdict.

---

B.19. First-Order Fit Package

B.19.1 Equal-weight point

For each L, determine the coupling at which the two candidate energy peaks have equal integrated weight using admissible reweighting.

If no stable two-peak description exists, no equal-weight point is declared.

B.19.2 Histogram storage

During pilots, determine a fixed energy range covering all observed values plus 10% margin.

Before production, freeze:

- 512 equally spaced energy-density bins;
- 512 equally spaced |m_\Phi| bins.

Production bin edges are stored in the point table and cannot change afterward.

Raw scalar time series are retained, so histogram analyses can be independently reconstructed.

B.19.3 One- versus two-component model

Fit:

- a single Gaussian component;
- a two-Gaussian mixture with ordered means.

The two-component description is strongly preferred when

[
\boxed{
\Delta{\rm BIC}\ge10.
}
]

B.19.4 Free-energy barrier

At the equal-weight point, define

[
\boxed{
\Delta F_L

\ln
\frac{
\sqrt{P_{\max,1}P_{\max,2}}
}{
P_{\min}
}.
}
]

Fit

[
\boxed{
\Delta F_L

c_2L^2+c_0+c_{-1}L^{-1}.
}
]

B.19.5 Latent-heat estimator

Let the fitted energy-density peak locations be

[
e_1(L),\ e_2(L).
]

Fit

[
\boxed{
\Delta e(L)

|e_2(L)-e_1(L)|

\Delta e_\infty+cL^{-1}.
}
]

B.19.6 First-order verdict

The continuous lane fails only if all conditions hold:

1. the two-component model wins by
   [
   \Delta{\rm BIC}\ge10
   ]
   for at least the three largest sizes;
2. the lower 95% bound on c_2 is positive;
3. either
   [
   \Delta e_\infty^{95%,{\rm lower}}>0
   ]
   or a susceptibility fit supports L^3 growth;
4. hot- and cold-start chains tunnel between both peaks or a validated extended-ensemble method establishes their relative weights.

Finite-size bimodality alone does not fire the verdict.

---

B.20. Conditional Q2 Fit Package

This section becomes active only after Appendix A changes status to:

[
\boxed{
\text{Q2 SECTOR VALIDATED — PHYSICAL VERDICT STILL CONDITIONAL}.
}
]

All primary Q2 results in this section carry the ensemble label

[
\boxed{Z_{000}}.
]

B.20.1 Three-axis fixed-holonomy odd-winding likelihood

For each axis $\alpha\in\{x,y,z\}$, let each analysis block contain:

- $n_{b,\alpha}$ observations of $q_\alpha$;
- $k_{b,\alpha}$ observations with $q_\alpha=1$.

Use the block-bootstrap count likelihood separately for each axis, and retain the full cross-axis covariance from the eight-state $q$ process.

Persistent model:

[
\boxed{
{\rm logit}\,f_{\rm odd}^{(\alpha)}(L)
=b_{0,\alpha}+b_{1,\alpha}L^{-\omega_o},
\qquad
\omega_o>0.
}
]

Suppressed model:

[
\boxed{
{\rm logit}\,f_{\rm odd}^{(\alpha)}(L)
=b_{0,\alpha}-\left(\frac{L}{\lambda_{o,\alpha}}\right)^p.
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

The cubic summary

[
\boxed{
f_{\rm odd}(L)=\frac13\sum_\alpha f_{\rm odd}^{(\alpha)}(L)
}
]

is reported only after all three axis-resolved fits. No Gaussian approximation is used for rare sector counts, and no axis may be dropped after inspection.

B.20.2 Charge-one confinement radius

The production confinement estimate

[
\xi_{\rm conf}
]

must come from the charge-one loop-size or correlation estimator that has passed the Appendix-A validation gate in the same $Z_{000}$ construction. The estimator identifier, geometry, normalization, and fit range are frozen in `parameter_card.yaml` before target production.

If the validated estimator supplies a periodic charge-one correlator $C_1^{\rm FH}(z;L)$, fit

[
\boxed{
C_1^{\rm FH}(z;L)
=
A\frac{\cosh[(L/2-z)/\xi_{\rm conf}]}
{\sinh[L/(2\xi_{\rm conf})]}.
}
]

with the competing long-range model

[
\boxed{
C_1^{\rm FH}(z;L)
=
C_\infty+
A\frac{\cosh[(L/2-z)/\xi]}
{\sinh[L/(2\xi)]}.
}
]

If the validated estimator is instead a loop-size statistic, use only the preregistered saturation model associated with that statistic. No post-hoc replacement is permitted.

The reconstructed CKT axial correlator $C_1^{\rm ax}$ is comparator-only and cannot by itself define the canonical $Z_{000}$ production $\xi_{\rm conf}$.

B.20.3 Fixed-holonomy partition-ratio identity

For every matched size and every axis, require

[
\boxed{
1-2f_{\rm odd}^{(\alpha)}
=
\frac{Z_{e_\alpha}}{Z_{000}}.
}
]

The direct ratio estimator is independent of $q$-occupancy counting. A reproducible failure on any axis closes Q2 and invalidates the corresponding odd-winding interpretation.

B.20.4 Symmetry and translated-cycle checks

At isotropic couplings, require the correlated three-axis symmetry test specified in Appendix A. Also require the frozen translated-cycle tuple checks. A failed axis or translated placement cannot be removed or averaged away.

B.20.5 FM models

Fit the Fredenhagen–Marcu ratio to:

Vanishing model

[
\boxed{
R_{\rm FM}(L)
=aL^{-p}(1+cL^{-\omega}),
\qquad p>0.
}
]

Nonzero-asymptote model

[
\boxed{
R_{\rm FM}(L)=R_\infty+cL^{-p}.
}
]

The FM result remains secondary.

B.20.6 Twist result

The magnetic-twist free energy is reported as

[
\Delta F_{\rm tw}(L)
]

with its full size dependence. No universal power is imposed.

It is compared against:

- the canonical $Z_{000}$ sector distribution;
- the validated $\xi_{\rm conf}$ estimator;
- FM;
- and pure-gauge calibration behavior.

The CKT axial comparator is reported separately and is never substituted for the canonical Q2 branch.

B.20.7 Evidence for confinement

Report EVIDENCE FOR CONFINEMENT only when:

1. every Appendix-A sector, ratio, symmetry, translated-cycle, and mixing gate passes;
2. the size-admissibility condition passes;
3. the suppressed model beats the persistent model by $\Delta{\rm AICc}\ge10$ for all three axes;
4. for every axis,
   [
   f_{\rm odd}^{(\alpha),95\%,{\rm upper}}(L_{\max})<0.05;
   ]
5. the finite-$\xi_{\rm conf}$ model beats its preregistered long-range alternative by $\Delta{\rm AICc}\ge10$;
6. FM favors a nonzero asymptote;
7. the twist result does not contradict the confinement interpretation.

B.20.8 Evidence for deconfinement

Report EVIDENCE FOR DECONFINEMENT only when:

1. every Appendix-A sector, ratio, symmetry, translated-cycle, and mixing gate passes;
2. the size-admissibility condition passes;
3. the persistent model beats the suppressed model by $\Delta{\rm AICc}\ge10$ for all three axes;
4. for every axis the asymptotic lower 95% bound satisfies
   [
   f_{\rm odd,\infty}^{(\alpha),95\%,{\rm lower}}>0;
   ]
5. the preregistered long-range charge-one model is preferred;
6. FM favors a vanishing limit;
7. the twist result does not contradict the deconfinement interpretation.

B.20.9 Q2 unresolved outcomes

Q2 is unresolved if:

- $L_{\max}<4\xi_{\rm conf}^{95\%,{\rm upper}}$;
- any partition-ratio identity fails;
- any axis or translated-cycle check fails;
- sector round trips, $\widehat R$, or ESS fail;
- the three axis-resolved asymptotics disagree;
- models are not strongly distinguishable;
- FM disagrees with the canonical winding/radius behavior;
- the twist result is contradictory;
- the canonical $Z_{000}$ charge-one confinement estimator is not validated;
- or the resource ceiling is reached.

The mandatory label for scale failure is

[
\boxed{
\text{Q2 INCONCLUSIVE — QUASI-DECONFINED WINDOW NOT EXCLUDED}.
}
]

---

B.21. Model Comparison and Stability Rules

B.21.1 AICc

For a model with k fitted parameters, n retained correlated data points, and maximized Gaussian log likelihood \ell,

[
\boxed{
{\rm AICc}

2k-2\ell
+
\frac{
2k(k+1)
}{
n-k-1
}.
}
]

AICc is not reported when

[
n\le k+1.
]

B.21.2 Strong preference

A difference

[
\boxed{
\Delta{\rm AICc}\ge10
}
]

is the frozen strong-preference threshold.

B.21.3 Stability across L_{\min}

For fitted parameter \vartheta, define consecutive-window displacement

[
D_i

\frac{
|\widehat\vartheta_i-\widehat\vartheta_{i+1}|
}{
\sqrt{
{\rm SE}i^2+{\rm SE}{i+1}^2
}
}.
]

A result is stable when

[
\boxed{
D_i<1
}
]

for both transitions among the final three admissible L_{\min} windows.

B.21.4 Reporting requirement

Every frozen model and every admissible L_{\min} result is retained in the final fit ledger.

The preferred model may be highlighted, but failed or competing fits are not deleted.

---

B.22. Raw-Data Schema

Each independent chain writes one HDF5 file.

Filename pattern:

`<stage>__<branch>__L<L>__k<kappa>__J<J>__h<h6>__<sector>__c<chain>.h5`

Exact decimal parameter strings are used.

B.22.1 Root metadata

Required root attributes:

```text
protocol_version
protocol_hash
appendix_a_hash
appendix_b_hash
appendix_b_amendment_hash
fit_package_hash
parameter_table_hash
production_lengths_hash
frozen_run_inventory_hash
pilot_outputs_manifest_hash
resource_forecast_hash
code_commit
compiler
compiler_flags
dependency_lock_hash
machine_fingerprint
rng_name
rng_master_seed
branch
stage
boundary_condition
holonomy_sector
reference_cycle_geometry_hash
twist_sector
L
kappa
t
J
h6
chain_id
thermalization_sweeps
production_sweeps
measurement_stride
start_type
creation_utc
```

B.22.2 Scalar series

Dataset:

`/series/scalars`

Required columns:

```text
sweep
matter_action
gauge_action
anisotropy_action
total_action
matter_derivative
plaquette_flux
M_occupation
chi2_estimator
Rxi
U4
Wx
Wy
Wz
RW
Mphi_abs
Mphi2
Mphi4
A3Phi
H6
A3Phi_H6
n6
qx
qy
qz
sector_round_trip_x
sector_round_trip_y
sector_round_trip_z
accept_rotor
accept_link
accept_cube
accept_plaquette_loop
accept_even_worm
accept_sector_x
accept_sector_y
accept_sector_z
accept_sheet
```

Unavailable observables are stored as explicit missing values with an availability mask.

For `C-DUAL-FULL` and `V-DUAL-FULL`, `qx=qy=qz=0` is stored as the projected label and is never interpreted as a sampled Q2 distribution.

B.22.3 Correlators and charge-one diagnostics

Datasets:

```text
/correlators/G2_axis
/correlators/G2_fractional
/q2/charge1_estimator
/comparator/CKT_C1_axial
/comparator/CKT_C2_axial
/structure_factor/Phi
```

Each contains the estimator-specific geometry, orientation, measurement count, and block identifier required by its frozen analysis definition.

B.22.4 Current-weight histograms

Exact cosine-dual runs store:

`/current/N_absI`

as a sparse table with columns:

```text
block_id
abs_current
link_count
```

Also store:

```text
max_abs_current
overflow_count
```

The overflow count must be zero.

Finite-$h_6$ dual runs similarly store the sparse $|n_i|$ histogram.

B.22.5 Worm and sector diagnostics

Datasets:

```text
/worm/even
/sector/transitions
/sector/q_residence
```

Required fields include:

```text
worm_id
start_sweep
charge
path_length
net_winding_x
net_winding_y
net_winding_z
closed
accepted_steps
rejected_steps
initial_qx
initial_qy
initial_qz
final_qx
final_qy
final_qz
sector_axis
sector_move_sign
sector_move_accepted
```

The reconstructed CKT comparator, when run, stores its one-axis odd-worm information under:

`/comparator/CKT_odd_worm`

and is never merged with the canonical sector-transition dataset.

B.22.6 Histograms

Datasets:

```text
/histograms/energy
/histograms/Mphi
/histograms/anglePhi
```

Store bin edges once and block-level counts separately.

B.22.7 Free-energy-ratio and twist integration

Datasets:

```text
/integration/holonomy_ratio
/integration/twist
```

Required fields:

```text
axis
lambda
replica_id
sweep
integrand
exchange_partner
exchange_accepted
holonomy_from
holonomy_to
```

---

B.23. Immutable Output and Hash Procedure

B.23.1 Preregistration bundle

Before target production, create:

protocol_v0.3-RC1.md
appendix_A.md
appendix_B.md
appendix_B_amendment.md
parameter_card.yaml
calibration_points.csv
stageB_points.csv
stageC_points.csv
stageD_points.csv
production_lengths.csv
fit_models.yaml
raw_schema.json
software_lock.txt
hardware_fingerprint.json
frozen_run_inventory.csv
pilot_outputs.manifest.jsonl
resource_forecast.csv
resource_forecast_summary.json
resource_forecast.manifest.jsonl

Each file receives SHA-256.

B.23.2 Execution manifest

Create a lexicographically sorted JSON-lines manifest containing:

relative_path
byte_length
sha256
artifact_role

The execution root is

[
\boxed{
H_{\rm execution}

{\rm SHA256}({\rm manifest}).
}
]

No target production begins until H_{\rm execution} is written to a read-only record.

B.23.3 Raw-file hashing

Every completed raw chain file receives SHA-256 immediately after clean close.

Checkpoint files are separately hashed but are not substituted for completed raw files.

B.23.4 Derived-output rule

Derived tables and plots are written to a separate directory.

Raw files are never overwritten.

Every derived artifact records:

- input raw hashes;
- analysis code commit;
- fit-model hash;
- bootstrap seed;
- creation time.

B.23.5 Bug-fix rule

A post-freeze bug requires:

1. a new code commit;
2. a written bug classification;
3. a list of affected branches and points;
4. invalidation of every affected output;
5. a new execution root;
6. complete rerun of affected points.

No corrected output may retain the old execution root.

---

B.24. Decision Ledger

Trigger| Frozen result
Calibration hard constraint fails| Dependent production branch closed
Direct/dual agreement fails| Affected representation closed
First-order package fires| CONTINUOUS LANE FAILED — FIRST ORDER
Charge-two target passes all Q1 predicates| Q1 SUPPORTED
Ordinary-vector alternative passes and charge-two target fails| Q1 REJECTED — ORDINARY-VECTOR LANE SUPPORTED
Stable non-target continuous exponent| Q1 REJECTED
Q1 drift or insufficient precision| Q1 UNRESOLVED
$y_6<0$ in both Q3 lanes and ordered locking passes| Q3 IRRELEVANCE SUPPORTED
Nonnegative $y_6$ or nonzero critical asymptote passes| Q3 REJECTED
Q3 crossover too slow| Q3 UNRESOLVED
Appendix-A fixed-holonomy gate incomplete| Q2 GATE CLOSED
Any $Z_{e_\alpha}/Z_{000}$ ratio identity fails| Q2 INVALID — SECTOR IMPLEMENTATION FAILURE
Axis, translated-cycle, or mixing gate fails| Q2 UNRESOLVED
Q2 scale criterion fails| Q2 INCONCLUSIVE — QUASI-DECONFINED WINDOW NOT EXCLUDED
Confinement predicates concordantly pass| EVIDENCE FOR CONFINEMENT
Deconfinement predicates concordantly pass| EVIDENCE FOR DECONFINEMENT
Q2 witnesses disagree| Q2 UNRESOLVED
$C_{\rm forecast}>14{,}000$ core-hours| EXECUTION HALTED — amend protocol or raise $C_{\max}$, then re-hash
Frozen inventory and forecast do not reconcile exactly| EXECUTION HALTED — FORECAST DOES NOT MATCH FROZEN INVENTORY
Blind resource cap exhausted after execution begins| Corresponding question UNRESOLVED
Finite-$h_6$ dual fails| DUAL $h_6$ BRANCH FAILED — NOT A THEORY FAILURE

---

B.25. Execution-Freeze Checklist

The execution root may be created only after every applicable item is complete.

- [ ] Main protocol text frozen and hashed.
- [ ] Appendix A three-axis fixed-holonomy text frozen and hashed.
- [ ] Appendix B frozen and hashed.
- [ ] Appendix-B resource amendment separately hashed and included in the provenance chain.
- [ ] Canonical direct action verified against Theory v0.1.
- [ ] Villain/cosine convention map verified.
- [ ] Every calibration point listed.
- [ ] Every Stage-B point listed, including the slim-grid large-$L$ rule.
- [ ] Every Stage-C point listed, including the slim-grid large-$L$ rule.
- [ ] Conditional Stage-D fixed-holonomy points listed.
- [ ] All lattice ladders fixed.
- [ ] All $h_6$ values fixed.
- [ ] All $J$-bracketing rules implemented.
- [ ] All reweighting sufficient statistics stored.
- [ ] RNG implementation unit tested.
- [ ] Seed generation unit tested.
- [ ] Checkpoint/restart reproducibility passed.
- [ ] Blind pilot controller masks target trends.
- [ ] Production lengths generated.
- [ ] Production-length table hashed.
- [ ] Frozen run inventory generated and hashed.
- [ ] Inventory reconciliation status is `INVENTORY_RECONCILIATION_PASSED` with zero mismatches.
- [ ] Immutable pilot outputs and `pilot_outputs.manifest.jsonl` generated and hashed.
- [ ] `resource_forecast.csv` and summary generated and hashed.
- [ ] Blind-pilot forecast gate passes with $C_{\rm forecast}\le14{,}000$ physical CPU core-hours.
- [ ] Hard resource ceiling remains $C_{\max}=20{,}000$ physical CPU core-hours.
- [ ] Forecast storage is within 2.0 TB.
- [ ] Maximum resident memory is within 112 GiB.
- [ ] Thermalization tests implemented.
- [ ] Autocorrelation estimator implemented.
- [ ] Blocking rule implemented.
- [ ] Hierarchical bootstrap implemented.
- [ ] Correlated fitting implemented.
- [ ] Parametric-bootstrap GOF implemented.
- [ ] AICc ledger implemented.
- [ ] Every $L_{\min}$ fit retained.
- [ ] First-order package implemented.
- [ ] Raw HDF5 schema validated with explicit $q_x,q_y,q_z$ state.
- [ ] Raw-file hashing validated.
- [ ] Derived-output provenance validated.
- [ ] Calibration ladder passed.
- [ ] Q2 Appendix-A gate passed or Stage D remains sealed.
- [ ] Software lock recorded.
- [ ] Hardware fingerprint recorded.
- [ ] Execution manifest created with every parent artifact in the frozen hash chain.
- [ ] Execution root written to read-only storage.

---

B.26. Frozen Result

Appendix B freezes the complete pre-run witness architecture:

[
\boxed{
\text{parameter points}
}
]

[
\boxed{
\text{size ladders}
}
]

[
\boxed{
\text{blind production lengths}
}
]

[
\boxed{
\text{fit families}
}
]

[
\boxed{
\text{verdict predicates}
}
]

[
\boxed{
\text{resource ceiling}
}
]

and

[
\boxed{
\text{immutable raw-output root}.
}
]

The only values generated after structural freeze and before execution freeze are machine-performance quantities calculated through the blind-pilot rule.

Those generated values are themselves frozen and hashed before target production begins.

No parameter is moved because an exponent looks promising.

No size is removed because a crossover is inconvenient.

No run is extended because a preferred verdict is nearly significant.

No fit family is invented after seeing residuals.

No Q2 result escapes the fixed-holonomy sector, ratio, symmetry, mixing, and scale gates.

No resource failure is converted into a theory failure.

[
\boxed{
\textbf{Appendix A makes the sector real.}
}
]

[
\boxed{
\textbf{Appendix B makes the test immutable.}
}
]

Freeze the parameters. Reconcile the inventory. Blind the targets. Hash the machine. Then let the lattice answer.

CC0 1.0 Universal

To the extent permitted by law, this work is dedicated to the public domain under

---

Appendix B Amendment

B.3.1 Blind-Pilot Forecast Gate

After all calibration-only blind timing pilots are complete and the frozen production-length table has been generated, calculate

[
\boxed{
C_{\rm forecast}
=
C_{\rm pilot,actual}
+
\sum_r C_{r,{\rm forecast}}.
}
]

Here:

- $C_{\rm pilot,actual}$ is the physical CPU core-hour cost already consumed by the calibration-only blind timing pilots;
- $C_{r,{\rm forecast}}$ is the forecast physical CPU core-hour cost of each remaining frozen run class under the proposed execution root.

The forecast must include all authorized work required by the frozen protocol:

- remaining calibration and validation runs;
- coupling-location and deterministic refinement scans;
- Stage-B Q1 production;
- Stage-C Q3 production;
- Stage-D Q2 production when Stage D is authorized under the same execution root;
- thermalization;
- production measurements;
- direct/dual confirmation runs;
- fixed-holonomy partition-ratio work;
- magnetic-twist thermodynamic-integration ladders;
- replica-exchange work;
- mandatory checkpointing and measurement overhead.

The nominal forecast does not include the optional one-time blind production extension permitted by §B.7.6.

The difference

[
C_{\max}-C_{\rm forecast}
]

is the reserved contingency for those permitted extensions, unforeseen autocorrelation growth, and other preregistered execution variance.

The hard resource ceiling remains

[
\boxed{
C_{\max}=20{,}000\ \text{physical CPU core-hours}.
}
]

The pre-execution forecast threshold is

[
\boxed{
C_{\rm forecast}\le14{,}000\ \text{physical CPU core-hours}.
}
]

If

[
\boxed{
C_{\rm forecast}>14{,}000\ \text{physical CPU core-hours},
}
]

the mandatory status is

[
\boxed{\textbf{EXECUTION HALTED}.}
]

No target-production run may begin under the current protocol version or execution root.

No partial execution of the target ladder is permitted.

No lattice size, coupling point, observable, chain, fixed-holonomy axis, ratio estimator, thermodynamic-integration window, or scientific branch may be removed selectively after the forecast has been calculated in order to pass the gate.

The only permitted remedies are:

1. issue an amended protocol version that changes the resource schedule, parameter ladder, or run architecture before target production begins; or
2. raise $C_{\max}$ before execution and create a new Appendix-B hash, amendment hash, parameter-card hash, production-length hash, execution manifest, and execution root.

After either remedy, the blind-pilot forecast must be recalculated under the amended frozen configuration.

Calibration-only blind pilots used to construct $C_{\rm forecast}$ do not constitute target execution.

Passing this gate does not guarantee completion of every permitted blind extension. It establishes that the nominal frozen campaign leaves at least

[
\boxed{
20{,}000-14{,}000=6{,}000\ \text{core-hours}
}
]

of preregistered contingency.

Required forecast artifacts:

- `resource_forecast.csv`;
- `resource_forecast_summary.json`;
- `resource_forecast.manifest.jsonl`.

At minimum the detailed forecast records:

```text
stage
branch
run_class
L
kappa
t
J
h6
sector
chains
replicas
integration_windows
thermalization_sweeps
production_sweeps
estimated_core_hours
forecast_basis
pilot_outputs_manifest_hash
frozen_run_inventory_hash
production_lengths_hash
forecast_script_hash
appendix_b_amendment_hash
included_in_execution_root
```

The summary records:

```text
pilot_core_hours_actual
remaining_nominal_core_hours
C_forecast
C_max
contingency_core_hours
forecast_gate_threshold
forecast_gate_status
inventory_reconciliation_status
```

The gate passes only when both statuses are:

```text
FORECAST_GATE_PASSED
INVENTORY_RECONCILIATION_PASSED
```

with

[
\boxed{C_{\rm forecast}\le14{,}000.}
]

B.3.2 Immutable Pilot Provenance

Every calibration-only blind pilot used to calculate $C_{\rm forecast}$ must produce an immutable output file containing, at minimum:

```text
protocol_hash
appendix_a_hash
appendix_b_hash
appendix_b_amendment_hash
code_commit
compiler_and_flags_hash
dependency_lock_hash
hardware_fingerprint_hash
branch
run_class
L
kappa
t
J
h6
sector
chain_id
seed
pilot_start_utc
pilot_end_utc
thermalization_sweeps
measurement_sweeps
measured_core_seconds
measured_wall_seconds
physical_core_count
peak_memory_bytes
raw_output_bytes
tau_max_pilot
acceptance_statistics
sector_transition_statistics
pilot_status
```

Every pilot file receives SHA-256 immediately after clean close.

The pilot files are listed in a lexicographically sorted manifest:

`pilot_outputs.manifest.jsonl`

Each manifest row contains:

```text
relative_path
byte_length
sha256
branch
run_class
L
chain_id
artifact_role
```

Define

[
\boxed{
H_{\rm Pilot}=\operatorname{SHA256}(\texttt{pilot\_outputs.manifest.jsonl}).
}
]

The resource forecast must contain `pilot_outputs_manifest_hash = H_Pilot` together with:

```text
forecast_script_hash
forecast_script_commit
production_lengths_hash
frozen_run_inventory_hash
appendix_b_amendment_hash
```

A forecast lacking any of those provenance fields is invalid.

Pilot outputs may not be overwritten, edited, or replaced in place. A repeated or corrected pilot produces new pilot files, a new pilot manifest, a new $H_{\rm Pilot}$, a new resource forecast, and a new execution root.

Calibration-only blind pilots do not constitute target production, but they are immutable preregistration evidence and form part of the execution provenance chain.

B.3.3 Frozen Run-Inventory Reconciliation

Before calculating $C_{\rm forecast}$, generate:

`frozen_run_inventory.csv`

with one row for every required run unit under the amended protocol, including:

```text
stage
branch
run_class
L
kappa
t
J
h6
sector
chains
replicas
integration_windows
required_status
parameter_source
```

Sort lexicographically by:

```text
stage
branch
run_class
L
kappa
J
h6
sector
```

Define

[
\boxed{
H_{\rm Inventory}=\operatorname{SHA256}(\texttt{frozen\_run\_inventory.csv}).
}
]

The resource forecast must satisfy an exact one-to-one reconciliation against this inventory. Every required row must appear exactly once, except where explicitly expanded into chain or replica rows whose totals exactly reproduce the inventory counts.

The forecast generator must report:

```text
required_inventory_rows
forecasted_inventory_rows
missing_inventory_rows
unexpected_forecast_rows
chain_count_mismatches
replica_count_mismatches
window_count_mismatches
inventory_reconciliation_status
```

The only passing status is `INVENTORY_RECONCILIATION_PASSED` with every mismatch count equal to zero.

If any required lattice size, coupling, branch, axis, control, chain, replica ladder, ratio estimator, or integration window is absent, the mandatory result is

[
\boxed{
\text{EXECUTION HALTED — FORECAST DOES NOT MATCH FROZEN INVENTORY}.
}
]

No selective removal is permitted. In particular, the $L=192$ fixed-holonomy Q2 point may not be removed, reduced, deferred, or relabeled as optional merely to lower $C_{\rm forecast}$.

The only permitted responses are:

1. issue a formally amended protocol version changing the frozen inventory; or
2. raise $C_{\max}$ before re-hashing.

No partial target execution may begin before the revised inventory and forecast pass the gate.

B.3.4 Provenance Hash Chain

Freeze the parent-linked chain:

[
\boxed{
H_{\rm Theory}
\rightarrow H_{\rm Protocol}
\rightarrow H_{\rm AppA}
\rightarrow H_{\rm AppB}
\rightarrow H_{\rm AppBAmend}
\rightarrow H_{\rm Inventory}
\rightarrow H_{\rm Pilot}
\rightarrow H_{\rm Forecast}
\rightarrow H_{\rm Execution}.
}
]

Definitions:

[
H_{\rm Theory}=\operatorname{SHA256}(\text{Theory v0.1}),
]

[
H_{\rm Protocol}=\operatorname{SHA256}(\text{Protocol v0.3-RC1 containing }H_{\rm Theory}),
]

[
H_{\rm AppA}=\operatorname{SHA256}(\text{canonical three-axis Appendix A containing }H_{\rm Protocol}),
]

[
H_{\rm AppB}=\operatorname{SHA256}(\text{canonical base Appendix B bytes from the title through §B.26, excluding the appended amendment and CC0 footer}),
]

[
H_{\rm AppBAmend}=\operatorname{SHA256}(\text{canonical UTF-8 bytes of the separately materialized Appendix-B Amendment section, which records }H_{\rm AppB}),
]

[
H_{\rm Inventory}=\operatorname{SHA256}(\texttt{frozen\_run\_inventory.csv}),
]

[
H_{\rm Pilot}=\operatorname{SHA256}(\texttt{pilot\_outputs.manifest.jsonl}),
]

and define `resource_forecast.manifest.jsonl` as the lexicographically sorted manifest of `resource_forecast.csv` and `resource_forecast_summary.json`, then

[
H_{\rm Forecast}=\operatorname{SHA256}(\texttt{resource\_forecast.manifest.jsonl}).
]

Finally, create the lexicographically sorted execution manifest containing every parent artifact, inventory, pilot manifest and pilot file, production-length table, forecast artifacts, parameter tables, fit-model specification, software lock, and hardware fingerprint, and define

[
\boxed{
H_{\rm Execution}=\operatorname{SHA256}(\text{execution manifest}).
}
]

The execution root may be created only when:

```text
FORECAST_GATE_PASSED
INVENTORY_RECONCILIATION_PASSED
```

and

[
C_{\rm forecast}\le14{,}000.
]

Forecast first. Reconcile the inventory. Pass the gate. Hash the budget. No partial launch.

CC0 1.0 Universal.

No permission required. Copy it, modify it, test it, redistribute it, build on it, or tear it apart.

No ownership claim. No attribution required. No warranty.

Use freely.
