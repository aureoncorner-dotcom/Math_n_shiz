# Geometry Master

**A portable working reference for Geometry, Geometry Maximization, Hidden Quotient, GQG, and Toroidal**  
Consolidation 1.0 · Sources read 9 September 2026 · Latest incorporated source updates 8 September 2026

This file carries the definitions, worked examples, mathematical results, evidence limits, and next work needed to continue the geometry projects in another chat or workspace. Its organizing question is: **which distinctions must a retained description preserve for the particular observation, recovery, or prediction being made?**

The projects share this question while keeping their mathematical objects distinct. A multiplication representation, a phase rotation, a toroidal Markov kernel, a material measurement, and an empirical coding instrument are not automatically the same system. This consolidation adds no new experiment or simulation run. Full proofs, frozen instruments, and execution records remain linked at the end.

## 1 Current position

| Area | Current result | Limit that remains operative |
|---|---|---|
| Witness-relative geometry | Exact descent criterion, non-descent locus, witness-resolving refinement, and conditional geometric extensions | The bare definition determines no global shape, topology, or physical mechanism |
| Geometry Maximization | Exact 39-screen phases and counts; deterministic predictive refinement; finite-horizon loss | Practical prediction requires available present coordinates and an error assessment |
| Hidden Quotient | Correct locally null kernel and norm; qualified structural theorem; explicit restoration and incompleteness examples | Recovery, completion, and predictive autonomy are different problems |
| GQG | Claim-relative witness fidelity and a typed empirical constraint-response instrument | Observable differences do not identify hidden actors, motives, or implementations |
| Toroidal geometry | Integer or modular cut flux, membrane constraints, ensemble distinctions, and circular-throat kinematics | Geometry and ensemble projection do not establish confinement or critical behavior |
| Toroidal sector dynamics | No exact finite Markov order for the specified sector process at any fixed attempted-microtick spacing | The theorem does not exclude every augmented or finite-dimensional hidden-state model |
| L=3 follow-up | Separate source-reported engineering-validation **PASS** | Original pilot **UNRESOLVED**; physical Q2 **NOT_RUN**; production **NOT_AUTHORIZED** |
| Reproduction | Historical accepted-event discrepancy remains −1,352; replacement profile defined prospectively | Historical cause **UNRESOLVED**; replacement full replay **NOT_RUN** |

The current online entry points are **GEOMETRY + GQG — Working Master** [S1] and **TOROIDAL — Working Master** [S2]. Their first tabs contain newer consolidations; their other tabs preserve earlier bodies. Hidden Quotient v1.7 [S4] remains the mathematical core. **Corrected investigation 1.1** [S5] explains and repairs its applications; the investigation's edition number does not supersede the core's version number.

## 2 The common geometry

### Declare the source and the witness

Let D be the declared source domain, π:D→Q a total retained map, and W:D→Y the witness whose value matters. Use the attained label set Q=π(D). All fibers below are restricted to D.

The non-descent locus is

\[
N_W(\pi)=\{q\in Q:\exists x,y\in D,\ \pi(x)=\pi(y)=q,\ W(x)\ne W(y)\}.
\]

W can be recovered as a well-defined function of π exactly when N_W(π) is empty. A same-label pair with different W values proves failure at that attained label. If W takes values in a metric space, define the fiber diameter

\[
\Delta_W(q)=\sup_{x,y\in\pi^{-1}(q)}d_Y(W(x),W(y)).
\]

A measured or constructed pair gives a lower bound on this diameter. It does not supply a uniform upper bound. Failure to observe a collision is not a proof that every fiber is resolved.

The canonical exact witness-resolving refinement is

\[
R=\operatorname{im}(\pi,W),\qquad x\mapsto(\pi(x),W(x)),\qquad(q,w)\mapsto q.
\]

Any record determining both π and W maps to R. This is the precise sense in which R is coarsest. It does not establish smallest dimension, fewest stored bytes, mechanistic minimality, or availability as a causal measurement.

### What the definition does not determine

Without additional assumptions, any subset of Q can occur as N_W(π). A local collision therefore cannot determine a global shape. Openness, smoothness, derivative tests, connectedness, boundaries, and holonomy require their stated extra hypotheses. In particular, vanishing vertical derivatives need suitable connected fibers before they establish fiberwise constancy; disconnected components can retain different constant values.

Transport requires a declared lifting rule or connection. Under the appropriate transport hypotheses, nonzero witness holonomy implies non-descent; non-descent alone does not establish holonomy. A finite sector-label set has no continuous boundary unless a separate parameter space or refined base has been defined.

Restricting D can remove a collision by excluding source states. Adding an observation can distinguish states that remain in D. These operations must be recorded separately. [S3, S6]

### Empirical use

Before comparison, fix the source domain, witness, projection, same-fiber rule, distance, tolerance, uncertainty treatment, and coverage. A pair whose distance lower bound exceeds the tolerance certifies a discrepancy at the observed fiber. An empirical search does not certify all unobserved fibers.

The isotope/material work in **New geometry** remains a separate freeze-ready synthesis. Its central lesson is that atomic number or isotope mass alone need not determine a material response; pressure, material state, and the specific response witness can matter. This consolidation does not change its chemistry freeze or turn its literature examples into new measurements. [S3]

## 3 Recovery and prediction

### Autonomous retained states

For a deterministic update U:D→D, a unique set-theoretic update on π(D) exists exactly when

\[
\pi(x)=\pi(y)\Longrightarrow\pi(Ux)=\pi(Uy).
\]

For a stochastic full-state kernel P, the universal condition compares the entire next-observation laws:

\[
P(x,\pi^{-1}A)=P(y,\pi^{-1}A)
\quad\text{whenever }\pi(x)=\pi(y),
\]

for every measurable target set A, with the source's measurable-factor assumptions. This is strong lumpability. A special stationary initialization can admit a weaker projection; that does not prove the universal criterion. A table fitted to one finite trace proves neither criterion.

For a fixed deterministic output B, the coarsest autonomous refinement retaining B identifies exactly states with equal entire future output sequences:

\[
x\sim_\infty y\iff B(U^k x)=B(U^k y)\quad\text{for all }k\ge0.
\]

This characterizes required information. It does not permit future outcomes to be used as present predictor inputs.

On a complete finite domain of N states, partition refinement supplies an exact stopping rule. Start with the B-classes and split a class whenever its members' successors fall in different current classes. Stability on the entire domain gives the predictive quotient. With k₀ initial classes there are at most N−k₀ strict refinements. A finite sampled trace is not a complete finite domain. [S1, S6]

### Finite-horizon loss

Fix a kernel, clock, output B, retained record r, and horizon h≥1. Write

\[
\delta_h^B(z)=\sup_{r(x)=r(y)=z}
\operatorname{TV}\!\left(\operatorname{Law}_x(B_1,\ldots,B_h),
\operatorname{Law}_y(B_1,\ldots,B_h)\right),
\]

where TV(P,Q)=sup_A |P(A)−Q(A)|. A singleton fiber has diameter zero.

- With output and clock fixed, increasing h cannot decrease the diameter: marginalization cannot increase total variation.
- Refining r shrinks the pairs compared, so a refined fiber's diameter cannot exceed its parent fiber's diameter.
- Any single law used for every state in a fiber has worst-case error at least half the fiber diameter, by the triangle inequality.
- When B=r, zero one-step diameter on every fiber is universal predictive closure. For a different output B, matching its next value or law alone does not establish autonomy of r.
- A tested pair certifies a lower bound. A useful finite approximation needs an output, horizon, clock, tolerance, and justified error assessment. [S1, S2, S5]

### The clock correction

Let q_R observe a state pair and let Ψ_n advance that pair. At fixed n, equal residuals must give equal next residuals to define F_R,n. A single time-homogeneous F_R also requires agreement between equal residuals occurring at different times.

If fixed-time descent holds but cross-time agreement fails, retain the clock: (n,r)→(n+1,F_R,n(r)). A known periodic driver may need only its phase. Adding a clock cannot repair different successors already present within one time slice. [S4, S7]

## 4 Hidden Quotient

### The fixed multiplication witness

Start with actual bounded measurable functions B(X,Σ), and define π(f)=M_f on L²(X,μ), with M_f g=fg. A set A is locally μ-null when μ(A∩E)=0 for every measurable E of finite μ-measure. Then

\[
\ker\pi=\{f:f=0\text{ locally almost everywhere}\}.
\]

Testing M_f against indicators of finite-measure sets proves one direction. Conversely, the support of every L² function is covered by the finite-measure sets {|g|≥1/n}, so local vanishing implies M_f g=0.

Define the semifinite reduction

\[
\mu_{\rm sf}(E)=\sup\{\mu(F):F\subseteq E,\ F\in\Sigma,\ \mu(F)<\infty\}.
\]

It agrees with μ on finite-μ sets, and its null sets are the locally μ-null sets. The L¹ and L² spaces are canonically isometrically identifiable with those of μ. The quotient and correct norm are

\[
B(X,\Sigma)/\ker\pi\cong L^\infty(\mu_{\rm sf}),\qquad
\|M_f\|=\|f\|_{\infty,\rm loc}.
\]

The usual μ-essential-supremum identity holds for all bounded measurable f exactly when μ is semifinite. The quotient representation is faithful and therefore isometric. Semifinite reduction removes locally invisible distinctions; it does not supply missing suprema. Localizable completion addresses a separate completeness problem.

### The qualified structural theorem

Put λ=μsf. Use “localizable” to mean semifinite with Dedekind complete measure algebra. The following are equivalent in the source theorem:

1. λ is localizable.
2. The canonical isometry L∞(λ)→(L¹(μ))* is onto.
3. The multiplication image on L²(μ) is a von Neumann algebra.
4. That image is a maximal abelian star-subalgebra of B(L²(μ)).
5. Every positive measure ν≪λ that is **strongly λ-semifinite** has a measurable finite-valued density h:X→[0,∞), with ν(E)=∫_E h dλ for all measurable E.

Strong λ-semifiniteness means

\[
\nu(E)>0\Longrightarrow\exists F\in\Sigma:
F\subseteq E,\quad\lambda(F)<\infty,\quad0<\nu(F)<\infty.
\]

For finite ν, the upper bound ν(F)<∞ is automatic, but the remaining finite-piece condition still applies. The density then lies in L¹(λ)₊. Absolute continuity alone does not replace that condition in the unrestricted localizable theorem. The finite-ν corollary alone is not the full fifth structural condition. Sources [S4–S5] supply the precise theorem references and qualifications.

### Three examples that require different diagnoses

**A — Restore a missing observation.** Let X=[0,1]⊔{p}, with Lebesgue measure on the interval and μ({p})=∞. Then L²(μ)≅L²[0,1]. The function χ_{p} is locally null but not μ-null: its ordinary essential supremum is 1, while its multiplication-operator norm is 0.

Keep W(f)=f(p) fixed and enlarge the observation to

\[
\Pi(f)=M_{f|[0,1]}\oplus f(p),\qquad
\operatorname{im}\Pi\cong L^\infty[0,1]\oplus\mathbb C.
\]

The norm becomes max(ess sup_[0,1]|f|,|f(p)|). The measure has not changed; the observation has gained an actual point-evaluation witness. Since f and f+χ_{p} collide under the old π for every f, the old non-descent locus for this W is all of Q. No computation from the old quotient alone can reconstruct W.

Do not substitute the point encoding x↦[{x}] in Σ/Nloc: interval singletons are also null. That map sends every point to zero and loses every point identity, not just p.

**B — Non-σ-finiteness is not itself failure.** Take an uncountable disjoint union of Lebesgue intervals with the full direct-sum sigma-algebra and measure. It is strictly localizable and semifinite, although not σ-finite. Its full multiplication representation is faithful on almost-everywhere classes, and the structural properties hold.

Restricting observation to countably many slices loses the omitted field. This is a spatial restriction, not a theorem about finite temporal memory. Under identity dynamics the partial record remains autonomous despite losing full-field information. If the update swaps an omitted slice with a retained slice, the next retained output can differ inside one current fiber. Retaining both swapped slices repairs closure for that specified update.

**C — An injective map can still miss needed objects.** Let I be uncountable, Σ the countable/co-countable sigma-algebra, and μ counting measure restricted to Σ. Then μ is semifinite, L¹=ℓ¹(I), L²=ℓ²(I), but the measure algebra is not Dedekind complete.

The inclusion of bounded Σ-measurable functions into ℓ∞(I)=(ℓ¹(I))* is injective and isometric but not onto. If J and I\J are both uncountable, χ_J defines a bounded functional missing from the original measurable algebra. Finite-subset multipliers form a net converging strongly to its multiplier outside that algebra.

For this inclusion and the identity witness, attained fibers are singletons and N_W is empty. The omitted functional is a **representability gap outside the image**, not a collision within an attained fiber. Completion and witness refinement must not be conflated. [S5]

Seat 2 and Seat 5 remain declared interpretive readings. Their mathematics does not establish empirical social claims, consent, actors, or mechanisms. Their source-specific OMNIBUS references remain source-specific.

## 5 Geometry Maximization and the exact phase model

All phases are measured in cycles. Let {·} denote fractional part and set

\[
\alpha=(3-\sqrt5)/2,\qquad
\tau=15-39\alpha=(39\sqrt5-87)/2\approx0.103325561245899.
\]

Define

\[
\theta_n=\{\theta_0+n\alpha\},\quad b_n=\lfloor39\theta_n\rfloor,
\quad\rho_n=\{39\theta_n\},\quad s_n=b_n\bmod3.
\]

Bins are half-open. For the **departing** transition n→n+1,

\[
\sigma_n=\mathbf1_{[0,\tau)}(\rho_n),\qquad
(b_{n+1}-b_n)\bmod39=15-\sigma_n,
\]
\[
\rho_{n+1}=\rho_n-\tau+\sigma_n,\qquad
s_{n+1}=s_n-\sigma_n\pmod3.
\]

At ρ=τ the slip is 0; at ρ=0 it is 1. The pair phase z={13θ}=(s+ρ)/3 rotates by −τ/3.

| Output retained | Minimal phase realization | Update |
|---|---|---|
| Entire full-bin future | θ | θ→{θ+α} |
| Strand and slip future | z={13θ} | z→{z−τ/3} |
| Slip future | ρ={39θ} | ρ→{ρ−τ} |

Minimality is relative to the full-circle domain, specified outputs, and boundary convention. It is a proved information statement, not an inference from a short run.

For N departures,

\[
S_N=\sum_{n=0}^{N-1}\sigma_n=N\tau+\rho_N-\rho_0,
\qquad |S_N-N\tau|<1.
\]

At θ₀=0 and N>0, S_N=ceil(Nτ): 39 departures give 5 slips, 507 give 53, and 10,000 give 1,034. Complete slip gaps are 9 or 10. Under uniform initial phase,

\[
\Pr(\sigma_0=1,\sigma_k=1)=\max\{0,\tau-\|k\tau\|_{\mathbb R/\mathbb Z}\}.
\]

The stationary slip process is nonmixing and has no finite Markov order. A fixed finite slip suffix is not an exact substitute for its continuous predictive phase. These are phase-rotation results, separate from the toroidal stochastic memory theorem.

For |ε|<1, h_ε(x)=x+ε sin(2πx)/(2π) has h′>0 and defines the conjugate map F_ε=h_ε⁻¹R_αh_ε. Exact phase observations survive when transported through h_ε. Equal-width bins in x are a different observation. The invariant occupation measure is h′_ε(x)dx. The v2 source also supplies analytic approximation bounds; its floating-point trajectories are not certified interval enclosures. [S1, S6]

### Corrected smooth-phase algebra

For an orientation-preserving smooth circle coordinate h, use B_h=C∞(𝕋;ℂ) and D_h=(2πi h′)⁻¹∂_x. The products f∘g=fD_hg and f◁g=gD_hf are opposite Novikov products. With associator (f,g,u)=(f∘g)∘u−f∘(g∘u), their associators are −fgD_h²u and guD_h²f respectively.

The bracket is [f,g]_D=fD_hg−gD_hf. For the degree-k phase inclusion J_k, D_hJ_k=kJ_kD, so its intrinsic derivative is D_h/k for k=13 and 39. Finite-fiber averaging is not a product homomorphism. The identity (fg)∘u=f(g∘u) **does hold** for this recipe, even in an associative noncommutative algebra; do not reuse the earlier erroneous denial of it. The separate full noncommutative rotation-algebra product has an actual Novikov defect.

The recovered §35 audit reports 36,237 exact assertions, including expected nonzero defects. That complete verifier was not rerun in this consolidation. The phase algebra supplies no physical central charge, Hamiltonian, vacuum representation, or Q2 verdict. [S2, S13]

## 6 GQG and empirical interpretation

GQG v0.12 keeps theorem geometry, dyadic admissibility, retained context, and empirical instrumentation separately typed. **Witness fidelity is relative to the claim.** Fidelity, resolution, and provenance strength are different properties; they are not one authority ranking.

An external residual can support observable condition dependence under a frozen comparison. It does not reconstruct hidden states or identify their generating mechanism. A system self-report establishes what was reported unless independent evidence supports the implementation claim. Source, derived view, detector, decision, action, and outcome remain separately located.

For constraint-response work, determine eligibility before forming a denominator. Retain **Object, Standing, Response, and Route** separately. Standing, event compliance, window binding rate, and derived demotion are not interchangeable. Keep UNKNOWN, PARTIAL, exclusions, and censoring explicit. Do not convert historical counts into successor rates by changing labels.

Confirmatory promotion retains the instrument's independent, framework-naive sealed first pass and coordinate-level agreement requirements. The complete coding rules and thresholds live in [S7]; this synopsis does not replace them for execution.

The Open-Seam Atlas records typed partial transitions, route provenance, discarded distinctions, correction, alternate routes, and path order. Equal endpoints do not establish equal paths or a global manifold.

The unified residual record R=(δ_C,δ_D,δ_K) carries chart, dyadic, and retained-context comparisons. Each channel needs its own comparator; subtraction and a shared metric are not automatic. UP/DOWN/FLAT/MIXED record coordinate directions. Progressive or regressive interpretations require separately justified polarity and provenance. Residual autonomy must satisfy the fixed-time and cross-time tests in Section 3. [S1, S4, S7]

## 7 Toroidal geometry and ensembles

### State conventions and conserved flux

Use the periodic cubical lattice, positively oriented edges, integer current I, mod-two membrane M, and q∈(ℤ/2)³. Boundary is head minus tail, so physical divergence is −∂I. Reference cycles Γ_α and transverse cuts are fixed. At side length two, periodic bonds with the same unordered endpoints remain distinct stored edges, indexed by base vertex and positive axis.

The consolidated sourced constraints are

\[
\operatorname{div}I+6n=0,\qquad
\bar I+\partial M+\sum_\alpha q_\alpha\Gamma_\alpha=0\quad\text{mod }2.
\]

For F_α(k)=Σ_{x:x_α=k}I_{x,α}, zero divergence gives

\[
W_\alpha=F_\alpha(k)=\frac1{L_\alpha}\sum_{\ell\parallel\alpha}I_\ell\in\mathbb Z,
\]

independent of parallel cut. Preserve signed W and ΔW. With charge-six sources, cuts agree modulo six and the parity of that modular flux determines q. The volume average can be fractional or have the wrong parity. Record integer winding as unavailable in that sourced case and keep the average under a different name.

For sources divisible by m, retain the mod-m cut class. Reduction of that class to parity is a general group map only for even m. With multiple allowed source charges, their positive greatest common divisor supplies the universally conserved modular class. [S2, S8]

### Do not mix ensembles or observables

Let h label fixed-reference Wilson-loop signs, Z_h the direct partition functions, and 𝒵_q the nonnegative dual coefficients. The source convention is

\[
Z_h=\frac18\sum_q(-1)^{h\cdot q}\mathcal Z_q,
\qquad\mathcal Z_q=\sum_h(-1)^{h\cdot q}Z_h.
\]

Thus Z_full=𝒵_000, while Z_000=(1/8)Σ_q𝒵_q. Full periodic ensemble summation forces an even-parity projection; that algebraic projection is not observed confinement. The three scientific questions stay separate: **Q1** is charge-two critical scaling, **Q2** is charge-one/confinement behavior under a specified ensemble and estimator, and **Q3** is anisotropy flow. The canonical Q2 branch remains source-free, cubic, and fixed-reference Z000. Fixed-reference loop conditions do not imply path-independent holonomy.

The field constructor uses local sign identification z∼−z and physical composite Φ=z². Together with the declared threefold symmetry, invariant onsite monomials require p−r divisible by six, giving leading phase-dependent anisotropy of degree six. This classifies allowed terms; it does not derive a unique continuum theory or establish XY* criticality. [S2, S8]

## 8 The declared toroidal dynamics

TD-COS-FH-001 is the **ideal cosine** reference kernel at J=1, t=1/2, h₆=0, fixed-reference Z000, with unbounded integer currents. Its zero-source state is X=(I,M,q), subject to div I=0 and the mod-two membrane constraint. The target weight is

\[
\pi(X)=\mathcal N^{-1}\mathbf1_{\rm constraints}(X)
t^{N_M}\prod_\ell\mathcal I_{|I_\ell|}(J),
\]

where 𝓘_n is the modified Bessel function and N_M=Σ_pM_p. Do not impose equal sector probabilities or substitute Villain weights under the same kernel identity.

At volume V, each attempted microtick chooses the following family with weight divided by B=8V+7. Cubes and faces are uniform within their families. For cycles choose the axis uniformly; for sheets choose the axis uniformly and then one of its transverse cuts uniformly. Signed orientations s=±1 are equiprobable.

| Family | Weight | Change |
|---|---:|---|
| Identity | V | No change |
| Cube | V | M→M+∂C mod 2 |
| Coupled plaquette | 3V | I→I+s∂P; M→M+P mod 2 |
| Even plaquette | 3V | I→I+2s∂P |
| Closed sheet | 1 | M→M+S mod 2 |
| Even reference cycle | 3 | I→I+2sΓ_α |
| Unit sector cycle | 3 | I→I+sΓ_α; q→q+e_α mod 2 |

Metropolis acceptance is min(1,target(Y)/target(X)) under symmetric descriptor proposals. Both identities and rejections advance attempted microticks. A sweep is K^B, a fixed number of mixture draws; it does not guarantee one attempt from every family or axis.

For finite J>0 and 0<t<1 on the stated finite lattice, the ideal unbounded kernel has a normalized positive target, is reversible, irreducible, and aperiodic. These analytical properties do not establish implementation conformance, a finite mixing-time bound, or adequacy of a chosen warmup.

The source numerical contract uses rational Bessel enclosures and a progressively refined uniform random prefix. A resource or precision interruption preserves the unresolved proposal; it cannot become an invented rejection or completed microtick. Exact implementation work requires the full source and configuration contract. [S9]

### The all-orders sector result

For every fixed cubic L≥2 and every fixed positive integer spacing d of **attempted microticks**, the stationary process Y_n=q(X_dn) is not Markov of any finite order. The source also excludes an exactly time-homogeneous finite-order sector law obtained from another initial full-state distribution.

The proof uses R=K^d, u=1_{q=000}, multiplication D by u, and the reversible compression A=DRD. Finite Markov order would force an eventual constant ratio of zero-sector block probabilities, which yields A²u=cAu. Valid states with current 2N on every positive edge violate this identity through a nonzero Bessel-tail correction to the return law as N grows.

For the comparison walk on (ℤ/2)³, the relevant return polynomial is

\[
r_d(\varepsilon)=\frac18\sum_{j=0}^3{3\choose j}
\left(1-\frac{j(1+\varepsilon)}B\right)^d,
\qquad r'_d(0)<0.
\]

The written all-orders argument is distinct from the six finite arithmetic checks. It does not automatically cover a finite-current truncation, accepted-move clock, adaptive schedule, or every augmented statistic. In particular, it is not an all-orders theorem for (q,W), and it does not exclude every finite-dimensional hidden-state representation.

The full state remains Markov. Given an initial law, the causal posterior ν_n(x)=Pr(X_dn=x | Y₀,…,Y_n), updated by prediction with K^d and conditioning on the new sector, is a sufficient belief state. Its representation may be unbounded. Practical finite compression is the remaining approximation question. [S10]

## 9 Validation and reproduction status

### The separate L=3 follow-up

The direct rotor/gauge follow-up uses its own sweep: all 27 angle proposals followed by all 81 link-flip proposals. It is not the attempted-microtick kernel in the memory theorem.

- Eight fresh seeds: 196000–196007.
- Per chain: 2,000 warmup plus 40,000 retained sweeps.
- Total retained states: 320,000; preserved dual reference: 32,000 states.
- No pooling with the original direct pilot or L=2 cohorts.
- Source reports exact same-seed replay of every retained state and all 336 state/RNG checkpoints.

Direct holonomy counts, encoded h=h_x+2h_y+4h_z, are:

| h | (h_x,h_y,h_z) | Count |
|---:|---|---:|
| 0 | 000 | 307471 |
| 1 | 100 | 3858 |
| 2 | 010 | 4054 |
| 3 | 110 | 217 |
| 4 | 001 | 3798 |
| 5 | 101 | 265 |
| 6 | 011 | 233 |
| 7 | 111 | 104 |

The total is 320,000 and minimum 104 passes the unchanged raw-count gate of 100. The direct-to-dual reference uses

\[
\widehat p(q)=\frac{\sum_h(-1)^{h\cdot q}H_h}{8H_{000}}.
\]

Every sector passes the source's approximate engineering screen |dual−reference|+5 SE_combined≤0.04, using its chain-based uncertainty procedure. Direct holonomy frequencies and dual sector probabilities are different observables.

This is a **separate reported PASS**. The original pilot's minimum 33 remains **UNRESOLVED**. Raw count is not effective sample size; the screens are not an exact simultaneous-confidence theorem or proof of production mixing. The local plan seal is not external preregistration. Physical Q2 stays **NOT_RUN**. [S11]

### The unresolved discrepancy and prospective replacement

The historical L=2 reproduction reports 1,107,368 accepted nonidentity updates; the companion reports 1,108,720. Difference: −1,352. Equal attempted totals, matching identities, a matching bounded prefix, or statistically close aggregate results do not explain a deterministic discrepancy. The first differing historical event remains unresolved. [S12]

The prospective replacement amendment defines profile **TD-COS-FH-001-L2-REPLAY-REPLACEMENT-20260908**. Its designation is prospective; it does not resolve or replace the historical execution records. Important bindings are:

- Executable: sampler/td_cos_fh_001_sampler.py; 47,134 bytes; SHA-256 `262f60cf72e41481428c45cb921aee99c1c6178d39f67ed7071252001f180c2b`.
- Configuration: DYNAMICS_REPLACEMENT_v0.1.json; SHA-256 `803484491f4c9d8702d97e0c15eab8cbd7f4940b8f16058f7c15ac9be5e1e275`.
- Eight chains, q=c and M=0 with I=Γ(q); proposal seed 64000+c and acceptance seed 74000+c.
- L=2, B=71; 2,000 warmup plus 10,000 retained sweeps per chain. Retained addresses 142,071 through 852,000 every 71 ticks.
- Full target: 6,816,000 ordered events, 80,000 retained rows, 112 declared restart checkpoints, and exact fresh-process restart agreement.

The old CLI's `--dynamics` argument hashes a file but does **not** load or enforce its settings. A configuration-enforcing adapter, lossless recorder, and new-schema conformance checks remain required. The recovered 512-event tracer is not a full implementation of the replacement envelope. Full replacement replay remains **NOT_RUN**; production stays **NOT_AUTHORIZED**. Hashes identify bytes, not mathematical truth or an externally attested date. [S14]

The all-orders proof Doc's embedded code still ends at `assert a`. Its readable proof is present, but that listing is not a complete runnable verifier. Do not silently fill the missing code and call it the original artifact.

### What the earlier review independently checked

The 8 September review checked G1 dimension arithmetic, the L=3 total/minimum and eight Fourier-reference probabilities, an exact 10,000-departure phase calculation, and character-return formulas against exact finite-group convolution for (L,d)=(2,1),(2,71),(3,1),(3,223),(4,1),(4,519). These checks did not replay the historical long sampler runs, rerun the full §35 audit, formally verify the all-orders proof, or perform a physical experiment. This consolidation refreshed the source documents and carried those limits forward.

Supplemental signed-winding check SW1 retains signed W only on the divergence-free domain. For a current-reversal-invariant target, E[q_α sgn(W_α)]=0. This is not a replacement for a frozen primary score; physical SW1 remains NOT_RUN. The heuristic scale gate L_max≥4ξ_UCB applies only to an admitted finite-radius branch. Missing or discordant fits remain unresolved; a long-range preference requires a separate frozen verdict path. [S2]

## 10 Physical and geometric comparators

### The circular throat

For a circular centerline of radius A, use arclength s, radial coordinate r, angle ϑ, and h=1−(r/A)cosϑ>0. The metric is h²ds²+dr²+r²dϑ². Require positive circle-periodic U(s) and tube radii below A. Physical velocity components

\[
v_s=U(s),\qquad v_r=-\frac{rU'(s)}{2h},\qquad v_\vartheta=0
\]

are divergence-free. The material tube R_mat=R₀√(U₀/U) carries constant flow πR₀²U₀ with no relative side flux. A fixed-radius control tube has Q_c=πR_c²U and outward side flux Q_c(a)−Q_c(b). Different boundary definitions explain their different flux statements.

This is continuum kinematics, without a derived gauge-force law, arbitrary-centerline extension, physical-time calibration, or empirical throat validation. [S2, S8]

### Two clocks

For the separate rotating-lattice comparator, x_n=frac(m[θ_n−g(t_n)]) is relative phase for m sites; nearest-site distance is ||x_n||/m. At regular spacing Δt without resets, the source convention gives x_{n+1}=frac(x_n+β), β=m(α+Δt/T_g) mod 1. Retaining distance alone generally loses predictive state.

The two-clock specification remains prospective and **NOT_RUN**. Timing/reset, eligibility, outcome, holdout, and multiplicity inputs remain unresolved. Historical rotating-lattice nulls remain unchanged. [S2]

### Resonator as a worked witness example

For an ideal flexible string, T=4L²f²μ. At fixed L, (T,μ) and (cT,cμ) with c>0 have equal pitch but different tension when c≠1. Retaining μ repairs the ideal-model load witness; equal pitch alone does not determine frame loading.

G1 assumes a literal 2×3-inch spine, strings at x=−4,−2,0,2,4 inches, and a two-inch face gap giving y=3.5 inches. For its assumed ten-inch bar and half-inch thickness, the farthest corner is (5,3.75), radius 6.25 inches. Its stated one-inch radial allowance gives **14.5 inches clear inner diameter**. This is the recorded occupied-envelope example, not a universal vessel requirement or a strength certification. The 32-inch string length is 0.8128 m; do not substitute the separate 0.65 m example without recalculating tension.

The later compact comparison in the same source uses 1.75-inch string centers, a nine-inch assumed bar, and a half-inch vessel shift toward the strings, yielding about **13.10 inches** modeled clear diameter under its retained allowances. It is an option to compare with the actual vessel, not a verified fit or selected connection. Include fittings, motion, the mouth, and every occupied height in a real envelope check.

These acoustic examples connect to witness-relative geometry. They remain outside the toroidal field master. [S3, S15]

## 11 Continue from here

1. **Choose the claim.** State the domain, retained record, witness or output, dynamics, clock, and required comparison. Separate static recovery, representability, exact autonomy, and approximate prediction.
2. **For mathematics, locate the obstruction.** Use same-fiber witnesses for non-descent, missing objects or suprema for completeness, and successor laws for predictive closure. Preserve the corrected examples and theorem hypotheses above.
3. **For toroidal replay, recover or implement the declared evidence path.** Recover the original authority if available. Otherwise work under the already defined prospective replacement profile, implement configuration enforcement and lossless recording, and validate replay without claiming the historical mismatch is solved.
4. **For useful prediction, specify an approximation problem.** Choose B, r, horizon, clock, tolerance, and evaluation domain. Compare full-state or causal-filter behavior with candidate retained coordinates. Report pairwise lower bounds separately from uniform guarantees.
5. **For empirical work, use the complete frozen instrument.** Preserve eligibility, denominator, uncertainty, coverage, holdouts, and independent confirmation. Fit validity, scale admissibility, accessibility, stationarity, and mixing remain separate conditions.

No new physical Q1/Q2/Q3 result, global non-descent geometry, holonomy, or mechanism attribution follows from assembling this file. Add future changes with the source, affected claim, evidence scope, and date. Do not promote a historical unresolved result by editing a summary label.

## 12 Source links

These are the sources behind this consolidation. The equations and distinctions above can be read without opening them; execution and proof-level continuation require the relevant complete source.

- **S1 — [GEOMETRY + GQG — Working Master](https://docs.google.com/document/d/1Cn00U9Cj37QRrK2Xg3bX1417xYKstkFzednitR9xjog/edit)**. Current first tab; earlier Geometry v2 body in its source tab.
- **S2 — [TOROIDAL — Working Master](https://docs.google.com/document/d/1NV7JsFuqJJVjFzYcqCAuC22y_rrjCSqqcZWZKobcGoU/edit)**. Current consolidation v0.3 first tab; earlier geometry release retained separately.
- **S3 — [New geometry](https://docs.google.com/document/d/1DVgC8ia4Z1suHmLbcrDbvw1ETuSjkTm25_5DH8OOQNI/edit)**. Isotope synthesis, witness-relative geometry, and the geometry integration note.
- **S4 — [Hidden Quotient v1.7 master](https://drive.google.com/file/d/1VF_UeW26X5LYpMYpfEtYvry8PjGX77Bj/view)**. Qualified theorem, witness restoration, seven companion bridges, and current geometry addition.
- **S5 — [Hidden Quotient Corrected Investigation 1.1](https://drive.google.com/file/d/1u3gyUGRK7Teqaa1lCZBd-WvhCuZDQM1k/view)**. Precise theorem qualifications, examples A–C, and identity/swap dynamics.
- **S6 — [Geometry Upgrade v0.1 — Predictive Fibers and Minimal Phase](https://docs.google.com/document/d/1dwlILms8z6YWJ_EFRCeoky6Fku9ND6A2xugZ008zOhk/edit)**. Deterministic predictive quotient, finite compiler, and minimal-phase companion.
- **S7 — [GQG v0.12 instrument](https://drive.google.com/file/d/13g-nyjUeMrtQRECXugx7DAdX5RrN0OzA/view)**. Complete empirical eligibility/response instrument and typed residual framework; apply the later clock correction when discussing autonomy.
- **S8 — [Toroidal Master v0.2 with dynamics integration](https://drive.google.com/file/d/1103tr4UUEIbyLYUxfE1zaCyn_E6MyAxW/view)**. Detailed field, topology, throat, protocol, and lineage reference.
- **S9 — [Toroidal Dynamics v0.1](https://docs.google.com/document/d/1jDBi4zR7W4fkJ_1F_gKU-RQPfkBgiBllXF5Pw1onP1Q/edit)**. Drive title v0; body v0.1. Full ideal kernel and numerical policy.
- **S10 — [TD-COS-FH-001 sector process has no finite Markov order](https://docs.google.com/document/d/1ON-nOrXUCCixHFm4WYIbihKtY47wQ2p0ylgR4r4opiY/edit)**. All-orders proof; embedded verifier remains truncated.
- **S11 — [L=3 direct-reference follow-up](https://docs.google.com/document/d/1YNIuAhjiY9szcA9Q5uvMm0N-b88KEQ15jjzFRLvdanY/edit)**. Separate PASS record, counts, uncertainty screens, and reported replay.
- **S12 — [Deterministic mismatch investigation](https://docs.google.com/document/d/1G88zvSUXi78R6uCMJYBEZpOmFpIiyP8OAK8_gtd9Hxw/edit)**. Historical discrepancy and missing authority.
- **S13 — [Toroidal note versus recovered Section 35](https://docs.google.com/document/d/11nZWX9optKPLn9PX90cNktrj84iyafFNi3Pj1LDFZEk/edit)**. Corrected phase algebra and source-reported exact audit.
- **S14 — [Prospective replacement amendment](https://docs.google.com/document/d/1gXUSaFvix1R_7-sqtkO5m8VqZqxGnDbl2JiLXas8KF4/edit)**. Replacement profile, hashes, configuration issue, event/restart contract, and preserved statuses.
- **S15 — [Five String Acoustic Resonator Rev B](https://docs.google.com/document/d/1U05hPPHklm9yZBUcNHkLMYwDaUaaftbLBFkmeEbv_zQ/edit?tab=t.a4ezxd7jm5ha)**. Use the Geometry update G1 tab for the stated dimensions.

**Version note.** This file consolidates the source state read on 9 September 2026. The 8 September working-master tabs and Corrected Investigation 1.1 are included. A future edit to a linked document does not silently update this portable snapshot.
