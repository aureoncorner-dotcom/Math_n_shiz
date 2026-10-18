# Geometry Master

**A portable working reference for Geometry, Geometry Maximization, Hidden Quotient, GQG, and Toroidal**  
Consolidation 2.0 · Live source review: 18 October 2026 · Incorporates the later v2.6, September 28 integration, and current direct-service correction

This file carries the definitions, worked examples, mathematical results, evidence limits, and next work needed to continue the geometry projects in another chat or workspace. Its organizing question is: **which distinctions must a retained description preserve for the particular observation, recovery, or prediction being made?**

The projects share this question while keeping their mathematical objects distinct. A multiplication representation, a phase rotation, a toroidal Markov kernel, a material measurement, and an empirical coding instrument are not automatically the same system. This consolidation includes small independent mathematical checks, but no new empirical experiment, historical sampler replay, or physical validation. Full proofs, frozen instruments, and execution records remain linked at the end.

**What changed in 2.0.** Added exact finite measurement repair and acquisition costs, the unbounded batch/sequential query gap, coverage and approximation guarantees, geometric stability examples, and claim/delivery checks. Updated toroidal verifier recovery and preserved the unresolved sampler discrepancy. Corrected source precedence for Hidden Quotient and FAILED versus UNRESOLVED closure. The core hypotheses, source domains, and original phase formulas remain explicit.

**Read route.** §§2–4 give the core and Hidden Quotient; §5 gives the phase model; §§7–9 give Toroidal; §§11–13 give practical acquisition, timing, and quantitative examples; §14 resolves evidence and version issues. This is one self-contained drop-in reference; source links are in §16.

## 1 Current position

| Area | Current result | Limit that remains operative |
|---|---|---|
| Witness-relative geometry | Exact descent, typed calculus, coverage envelope, canonical refinement, and available-coordinate repair | Set-level recovery does not supply regularity, causal availability, or a mechanism |
| Acquisition and approximation | Exact finite hitting-set and sequential formulations; n−1 versus ceil(log₂ n) query gap; uniform path-error bound | Declared menus, costs, complete domains, and uniform premises are required |
| Geometric and timing bounds | Recovery/conditioning distinction, global sampling bounds, optimal causal padding | Mathematical examples do not establish manufacturing or human benefit |
| Geometry Maximization | Exact 39-screen phases and counts; deterministic predictive refinement; finite-horizon loss | Practical prediction requires available present coordinates and an error assessment |
| Hidden Quotient | Correct locally null kernel and norm; qualified structural theorem; explicit restoration and incompleteness examples | Recovery, completion, and predictive autonomy are different problems |
| GQG | Claim-relative witness fidelity and a typed empirical constraint-response instrument | Observable differences do not identify hidden actors, motives, or implementations |
| Toroidal geometry | Integer or modular cut flux, membrane constraints, ensemble distinctions, and circular-throat kinematics | Geometry and ensemble projection do not establish confinement or critical behavior |
| Toroidal sector dynamics | No exact finite Markov order for the specified sector process at any fixed attempted-microtick spacing | The theorem does not exclude every augmented or finite-dimensional hidden-state model |
| L=3 follow-up | Separate source-reported engineering-validation **PASS** | Original pilot **UNRESOLVED**; physical Q2 **NOT_RUN**; production **NOT_AUTHORIZED** |
| Proof verifier | Complete all-orders source and rational certificate package recovered | Current access verified; historical successful reruns remain source-reported |
| Reproduction | Historical accepted-event discrepancy remains −1,352; replacement inputs recovered | Historical cause **UNRESOLVED**; adapter/recorder/validation and full replacement replay remain outstanding |

The current online entry points are **GEOMETRY — Working Master v2.6** [S16], **Geometry — Curated Upgrades** [S17], **GEOMETRY + GQG — Working Master** [S1], and **TOROIDAL — Working Master** [S2]. S1 and S2 have current working tabs and preserved earlier source tabs. Hidden Quotient v1.7 [S4] remains the mathematical core. **Corrected investigation 1.1** [S5] explains and repairs its applications; the investigation's edition number does not supersede the core's version number.

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

Transport requires a declared lifting rule or connection. Under the appropriate transport hypotheses, nonzero witness holonomy implies non-descent; non-descent alone does not establish holonomy. In the discrete topology on Q=(ℤ/2)³, every subset is clopen and has empty topological boundary. Smooth transport requires a separate base or refinement; graph transport and gauge holonomy can still be defined with their own structure.

Restricting D can remove a collision by excluding source states. Adding an observation can distinguish states that remain in D. These operations must be recorded separately. [S3, S6]

### Rules for changing a claim

Write Eq(f) for pairs with equal f-values. Exact descent is Eq(π)⊆Eq(W). The corrected set-level calculus is:

| Change | Exact rule |
|---|---|
| Joint witnesses | N_(W₁,W₂)(π)=N_W₁(π)∪N_W₂(π) |
| Coarsened witness | N_(f∘W)(π)⊆N_W(π), with an actual coarsening f |
| Refined observation π=r∘π′ | r(N_W(π′))⊆N_W(π) |
| Restricted source C⊆D | N_(W restricted to C)(π restricted to C)⊆N_W(π)∩π(C) |
| Next output B under U | Test N_(B∘U)(π); retained-state autonomy tests N_(π∘U)(π) |

The diagnostic type numbers are versioned examples, not an exhaustive partition. A discrete membrane collision does not establish a smooth disconnected-fiber or holonomy defect. Set factorization does not automatically give measurable or continuous factorization; the quotient structure must support that conclusion. [S3, S16, S18]

### Empirical use

Before comparison, fix the source domain, witness, projection, same-fiber rule, distance, tolerance, uncertainty treatment, and coverage. A pair whose distance lower bound exceeds the tolerance certifies a discrepancy at the observed fiber. An empirical search does not certify all unobserved fibers.

A useful exact coverage envelope is available. Suppose W is total on D but validated only on C⊆D. Put L_C=N_(W restricted to C)(π restricted to C) and G_C={q:π⁻¹(q) is not contained in C}. Then L_C⊆N_W(π)⊆L_C∪G_C. A validated collision remains a failure; a fully examined clean fiber is clear; incomplete fibers remain open absent another proof. This is a deterministic envelope, not a confidence interval or prevalence estimate. If W is genuinely partial, first define the intended target. Different witnesses may have different coverage. [S16]

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

For a finite stochastic chain, split blocks by each state's exact vector of transition masses into the current blocks. The stable partition is the coarsest strongly lumpable refinement preserving the initial labels. This is not universally the smallest realization of observable future laws. A causal posterior is sufficient, not automatically minimal: different hidden-state posteriors can induce the same law of every future output. Under a fixed initialization, finite Markov order concerns admissible observed histories and their final m symbols. A hidden-state collision refutes universal lumpability; alone it does not refute every initialized finite-order law. [S16, S17]

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

### Achievable error needs a center and a uniform premise

For metric witness values F_q=W(π⁻¹(q)), let δ=diam F_q and r(q)=inf_(a∈Y) sup_(w∈F_q)d(a,w), with allowed answer space Y declared. For finite diameter, δ/2≤r(q)≤δ. Half-diameter need not be attainable: in a three-point answer space with all distinct distances one, δ=r=1. For bounded real witnesses and unrestricted real answers, the midpoint of inf F_q and sup F_q attains δ/2. An infimum need not be achieved in a general answer space, so require an actual center or an attainment argument. [S16]

For a finite model and approximate retained transition kernel K, suppose every full-state row satisfies TV(π_#P(x,·),K(π(x),·))≤ε, with 0≤ε≤1 and matching initial retained laws. Then

\[
\operatorname{TV}(\text{true joint retained path through }h,
\text{approximate joint retained path through }h)
\le1-(1-\varepsilon)^h\le\min(1,h\varepsilon).
\]

Conditional next-label laws are mixtures of certified rows. Couple each step while histories agree; the chance of any disagreement gives the bound. A fitted trace or sampled maximum does not establish the required uniform row premise. Joint-path distances have the horizon monotonicity above; terminal-only distances need not. Refinement comparisons keep the target B fixed: changing B along with the retained record is a different problem. This guarantee was already in v2.4 and is recovered here from the current v2.6 source. [S16, §7]

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

### Tensor densities and the limits of finite sampling

The v1.61 proof-clarity patch extends the smooth phase frame to density weight λ: ρ_λ(f)a=fD_h a+λ(D_h f)a. For the existing smooth conjugate rotation F and h′>0, time acts by T_λa=(F′)^λ(a∘F); multiplication by (h′)^λ intertwines this with Koopman action. Its natural squared Hilbert norm integrates |a|² against (h′)^(1−2Re λ)dx. Positivity supplies a definite logarithm for complex powers. These are specified representation maps, not a physical field identification. [S31]

Uniform q-point phase averaging exactly integrates the products needed for the stated cocycle identity when each input frequency has absolute value at most B and q>3B. Thus q=39 suffices for B=12. Outside that band, aliasing can destroy the sampled formula's antisymmetry; antisymmetrizing does not generally restore the cocycle identity. These uniform phase samples are different from bin indicators. Brackets add frequencies, so a finite band is a test domain rather than a closed finite-dimensional Lie algebra or a finite predictive state. The patch's analytical extension and the separate v1.6 executable receipt retain distinct provenance. [S31]

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

### Explicit topological witnesses

The periodic cell complex has H₁(T³;ℤ)≅ℤ³. Choose reference cycles Γα and dual cuts Σα with intersection δαβ; Wα=⟨Σα,I⟩. In every sector q, I=Σα(qα+2kα)Γα with M=0 gives W=q+2k for arbitrary k∈ℤ³. Thus q loses winding in every sector, while W determines q. This static observation loss is distinct from temporal memory.

With charge-six sources, a₆=[I mod 6]∈H₁(T³;ℤ₆)≅ℤ₆³ and q=a₆ mod 2. Forced q=0 permits components 0,2,4 of a₆, not only zero. For direct gauge loops bounding a plaquette strip A, H(Γ′)H(Γ)=∏_(p∈A)B_p. Reference-loop signs therefore need not be path-independent when plaquette flux is present. [S2]

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

**Complete proof verifier recovered.** The native listing ending at `assert a` remains a historical copy. The complete proof, original verifier, and separate rational certificate checker are available at immutable commit `e8623fa88a6e049e17e7564222356a6675d6b29d`. The recovery reports byte-for-byte output reproduction, six exact character/convolution comparisons and three 70-digit local calculations; the separate checker adds nine exact clock checks for L=2,3,4 at d=1,2,B and outward-rational local enclosures at N=10,100,1000 with disjoint ratio intervals. The October review confirmed accessible complete source and receipts; it did not rerun those programs. These support the analytical proof and do not replay the historical sampler. [S24]

The historical recovery preserves reproduction-side code, reconstructed non-authoritative configuration, 80,000 retained measurements, 4,096 detailed prefix events, and 32 full state/RNG snapshots. Those differ from 88 digest-only checkpoints and from the missing companion's 96 reported post-initial full checkpoints. The original companion executable, authoritative configuration and complete event streams remain missing. The later handoff recovers exact replacement inputs, but configuration enforcement, lossless recording, restart/conformance validation, and full replay remain outstanding. Recovering a proof verifier does not close that execution gap. [S2, S25]

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

## 11 Choosing measurements that actually repair the claim

The abstract pair (π,W) specifies information, but W may be precisely what is unavailable. The newer master supplies an exact finite acquisition problem. Fix a nonempty complete finite domain D, an attained initial observation π, a total target W, and available total coordinates c₁,…,c_m with fixed nonnegative costs a_j. The initial-label cost is common or already paid. Queries reveal the same unchanged state. Availability, cost, and the intended target must be declared before optimization. [S16]

For every pair with π(x)=π(y) and W(x)≠W(y), form S_xy={j:c_j(x)≠c_j(y)}. A chosen coordinate set J repairs W exactly if and only if J meets every S_xy. A bad pair survives precisely when all selected coordinates agree on it. An empty S_xy means the entire menu cannot repair that pair. This is a hitting-set problem; inclusion-minimal, minimum-cardinality, and minimum-cost repairs are different objectives. Exhaustive search is exact for small menus but generally exponential. Matching and assignment prototypes are not general hitting-set solvers.

For example, take constant π, W=(0,1,1,0), c₁=(0,0,1,1), and c₂=(0,1,0,1) over four states. Neither coordinate alone suffices; together they do. A coordinate c₃=W would suffice alone only if it is actually available.

### Fixed batches, label-dependent batches, and sequential queries

Let H_q contain the separating sets S_xy within initial label q, and let τ_a(H) be the minimum cost of a set meeting every member of H. Assuming every required pair is repairable, independent choices across labels, and no shared installation budget,

\[
C_{\mathrm{fixed}}=\tau_a\!\left(\bigcup_qH_q\right),\quad
C_{\mathrm{label,worst}}=\max_q\tau_a(H_q),\quad
C_{\mathrm{label,expected}}=\sum_qp(q)\tau_a(H_q).
\]

A label-dependent batch is selected after observing q but before seeing its extra measurements. Expected cost needs a declared distribution. Exactness still covers states and labels assigned probability zero. With k attained labels, C_fixed≤k C_label,worst, sharply; no distribution-free k-factor comparison with expected cost follows. The cheapest potential inventory costs C_fixed, although a policy minimizing per-case cost can use a more expensive inventory. [S16, §§5–5.1]

Sequential acquisition can do much better. On D={1,…,n}, with constant π, target W(x)=x, and unit-cost thresholds c_t(x)=1[x≥t], t=2,…,n,

\[
C_{\mathrm{batch}}=n-1,\qquad
C_{\mathrm{sequential,worst}}=\lceil\log_2n\rceil.
\]

Each adjacent pair needs its unique threshold, so a batch must acquire all cuts. Binary search achieves the sequential upper bound; a depth-d binary tree has at most 2ᵈ leaves, proving optimality. At n=1024 this is 1023 batch queries versus 10 sequential queries. All 1023 thresholds remain necessary in the possible inventory. These are formal query costs, not measured time, energy, or labor savings.

For sequential expected cost, supply a state prior p(x) on D and define P(S)=Σ_(x∈S)p(x); label probabilities alone are insufficient. For a candidate set S with constant W, put V(S)=F(S)=0. Otherwise consider informative queries, with nonempty answer blocks S_jv:

\[
V(S)=\min_j\{a_j+\max_v V(S_{jv})\},\qquad
F(S)=\min_j\{a_jP(S)+\sum_vF(S_{jv})\}.
\]

V is worst-case remaining cost; F uses unnormalized prior mass. Maximize V, or sum F, over initial-label fibers for the overall objective. Every informative branch strictly shrinks S; repeated and uninformative queries can be removed with nonnegative costs. Zero-prior states still require exact recovery. If no informative query can resolve a nonconstant target, the menu is infeasible.

The source reports an exact finite sequential solver checked against exhaustive tree enumeration on 2,348 small models. Its documented defaults are 64 states, 16 coordinates, and 100,000 evaluated subproblems; exceeding bounds returns LIMIT. That source suite was not rerun here. Fresh October checks independently reproduce threshold costs for n=1,…,32 and the four-state prior (0.7,0.1,0.1,0.1): fixed batch cost 3, optimal sequential worst cost 2, optimal expected cost 1.5. An expected-optimal tree can have worst cost 3. [S16, §5.2]

For pre-answer use, optimize from available π_pre toward an independently specified target A_task. A policy using the pair (request, answer) to acquire that same answer is circular. Post-answer audits may use that pair to recover a different compliance or provenance witness.

## 12 Timing: a solvable scheduling problem with explicit limits

Mean delay, spread, number of distinct durations, current delay, and next-delay law are different witnesses. Cyclic records (40,40,160,160) and (40,160,40,160) share mean 100, population SD 60, and current entry 40, but their next entries are 40 and 160. This finite collision refutes that particular retained-state closure; it is not an infinite-memory theorem. [S23]

In the add-only scheduling model, readiness R≥0 has finite second moment. A release Y must obey Y≥R almost surely and E[Y]=m≥E[R]. Readiness is fixed; changing content, feedback, or queue dynamics changes the model. If m=E[R], only Y=R is feasible. Otherwise choose T with E[max(R,T)]=m. Then Y*=max(R,T) uniquely minimizes variance up to almost-sure equality:

\[
\operatorname{Var}(Y)-\operatorname{Var}(Y^*)
\ge E[(Y-Y^*)^2]\ge0.
\]

Indeed, Y²−Y*²−2T(Y−Y*)=(Y−Y*)²+2(Y−Y*)(Y*−T). The last term is nonnegative: when R>T both differences are nonnegative; otherwise Y*−T=0. Equal means eliminate the linear term after expectation. [S16, §9]

With m(T)=E[max(R,T)], v(T)=Var(max(R,T)), and a(T)=E[(R−T)_+], the differentiable frontier has −dv/dm=2a(T) wherever m′>0. For positive SD s, −ds/dm=a(T)/s. The two slopes have different units and are not preference coefficients.

For equally likely readiness 40/400 ms, mean readiness is 220 ms and SD is 180 ms. A 290-ms mean budget permits T=180 ms, giving releases 180/400 ms and SD 110 ms. A constant 180-ms release is infeasible. These are model calculations, independently checked in October; they do not demonstrate that padding benefits people. A favorable regularity/delay tradeoff is also distinct from an experimentally established interaction. The source's human timing experiment remains NOT_RUN; a separately executed toy mediation comparison is a different experiment. [S16, S23]

## 13 Worked additions: arithmetic, spectra, and geometric stability

### Arithmetic witnesses and a failed predictive repair

On y²=x³+2x+2 over F₁₃, P=(2,1) and Q=(3,3) give the same retained x-coordinates for (P,Q) and (P,−Q), but x(P+Q)=12 and x(P−Q)=11. Keeping both y-coordinates restores the signed inputs on the declared affine domain; no minimality is claimed. An existential signed-sum relation is a different target and requires its own domain, candidate x₃, and retained record. It cannot be called a coarsening of a specified sum without an actual factor map. [S3, §15]

For D={n∈ℤ:n≥2}, U(n)=2n+1, and primality bit q, let r(n)=(q(n),q(n)∧q(U(n))). Then r(3)=r(5)=(true,true), whereas r(7)=(true,false) and r(11)=(true,true). Thus the proposed Sophie Germain label is not autonomous. Even the genuine one-step window (q(n),q(U(n))) has the same counterexample. One additional future label is not automatically exact predictive closure. [S1, S3]

### Spectral witnesses need a declared observation

The spectral increment supplies exact examples in which equal squared spectra lose an eta witness, and equal endpoint spectra lose spectral flow. To reuse either, declare the domain-to-operator or domain-to-path map, domain and boundary conventions, spectral assumptions, and which output is retained. A computed eta, heat density, or spectral-flow number alone is not a same-fiber collision. The source keeps KPZ, Connes–Kreimer, GHY, APS, and the native constructions distinct until a correspondence is proved. These examples do not supply a toroidal sampler theorem or a physical central charge. [S20]

### Exact geometric recovery does not guarantee stable recovery

On [−1,1]², use G_w(x,y;t)=20[(1−w)x²+wx⁴]+10y²+tx, with 0≤w≤1. At t=0 every w gives endpoint readings (20,20), yet its δ=2 near-gap area changes from approximately 0.4442882938 at w=0 to 0.8792167529 at w=1. Endpoint readings lose the area witness. Within this calibrated family, G_w(1/2,0;0)=5−15w/4 recovers w exactly. A measurement error bounded by ε gives parameter error at most 4ε/15 before any clipping to [0,1]. [S19]

At w=1, the constrained minimizer is x*(t)=clip(−cuberoot(t/80),−1,1), y*=0. It is interior only for |t|<80; near zero its derivative is unbounded. The shorter GQG summary omits that tilt condition, so this master retains the corrected full-domain formula. A unique answer need not be Lipschitz-stable.

For a μ-strongly convex objective on a fixed nonempty compact convex domain, changing a linear tilt by Δℓ moves the constrained minimizer by at most ||Δℓ||/μ. If continuous fields f,g on the same nonempty compact domain differ uniformly by at most ε, their minimum-subtracted fields differ by at most 2ε. Consequently their near-gap sets obey Ω_f(δ−2ε)⊆Ω_g(δ)⊆Ω_f(δ+2ε), with negative-threshold sets empty. These bounds need the stated uniform and convexity assumptions.

A sampled violation v has global upper bound max_i v_i+Lh only when L is a valid Lipschitz constant and the sample is an h-net in the declared metric. Local tangency needs end caps, trimming, and a global interference check. Units, coordinate metric, active branch, and physical clock must be retained when the witness depends on them. A compact-domain bound cannot be applied to unbounded toroidal current space without additional tail control. [S16, S19]

## 14 Evidence, service, and version precedence

### Preserve a finding while keeping its cause open

Claim closure records the proposition, domain, criterion version, relevant evidence r_i, finding, disposition D_i, and action. Require D_i=g_i(r_i), with g_i independently declared and calibrated. Equal relevant evidence must give compatible dispositions, but a constant wrong classification is still wrong. If the defect criterion is b, substituting b∧k for “defect b and known cause k” wrongly erases a known defect at b=1,k=0. Unknown cause and observed defect belong in separate fields. A successful repair likewise need not identify the original cause. [S17]

For deterministic residual closure, a valid same-retained-state/different-successor pair establishes FAILED on the declared domain. An untested, underspecified, or insufficiently covered claim is UNRESOLVED. CLOSED requires a proof or complete applicable check. TTSC §20 still groups a valid failure with an untested claim; this master corrects that rule without inventing an executed TTSC failure. Stochastic closure compares successor laws, not two individual random outcomes. Within-time closure and cross-time homogeneity remain separate; adding a clock cannot repair the former. [S22]

### Selected text, a valid answer, and delivered work

Direct Service Geometry's text-preserving ablations concern a declared selected-text witness. They do not establish equal correctness, completion, latency, implementation, or service history. The current AS-001 contract separately checks faithful source selection S, task completion C, applicable content constraints K, claim-disposition fidelity P, historical service compliance H, and exact bytes B for a specified payload pair. A validated candidate requires S,C,K,P; delivery needs its own comparison with what was actually delivered. Its integration suite remains source-reported as unexecuted. [S17, S21]

The current recurrence correction uses one window of 198 eligible assistant replies after n334: 69 case-sensitive whole-word Checking recurrences, versus 70 case-insensitive recurrences. The extra match is n739. The stricter CORRECTION-BINDING RATE remains 129/198≈65.2%. These are alternative codings of one window, not independent cohorts. The literal DROP_IT baseline was already 0/16, so a 0/64 marker-free follow-up is not a measured reduction. These reconciled source counts establish no actor, intent, or mechanism and were not recounted from the raw transcript in this pass. [S21]

Transport observations, request records, session metadata, and returned records remain distinct spaces. Link them only with compatible identifiers, times, scope, and evidence for the actual relation. A process ID, endpoint, repeated answer, or file hash alone is not that join. [S17]

### Which source controls

The governing Hidden Quotient statement is qualified v1.7. The standalone multiplication document, despite its later Drive modification date, still omits the relative-semifiniteness condition in its RN paragraph, omits normalization in its dual-norm test, and says the quotient “trivializes” at semifiniteness. Use §4 here: normalize the finite-set test by 1/μ(A), and say local-null equivalence becomes ordinary almost-everywhere equivalence. The quotient of actual functions remains. Enlarging a codomain alone does not make a missing object enter the representation's image. Keep algebraic kernel, kernel pair Eq(π), and stochastic transition kernel distinct. [S4, S26, S33]

The restored Full-Packet Audit v0.2 is dated September 3. Its q-only closure label is historical; the later TD-COS-FH-001 theorem governs that specifically declared kernel. Neither theorem nor audit silently activates another protocol. Likewise, the October-modified Cos-Tim architecture's cross-domain coherence and approximately 43-day-cycle proposals remain hypotheses; its modification date supplies no test result or map identifying consciousness, governance, and heliophysics. [S29, S32]

The v2.6 receiving note and September 28 collection review report different recovery scopes for earlier repair-engine files. The latter ran locally recovered files but explicitly did not establish identity with earlier originals. Preserve that distinction rather than treating matching filenames or accumulated pass counts as release identity. The repeat-call matching bug and original vine conditioning defect are distinct from separately corrected derivatives and the finite geometry engine. [S16, S27]


## 15 Continue from here

1. **Choose the claim.** State the domain, retained record, witness or output, dynamics, clock, and required comparison. Separate static recovery, representability, exact autonomy, and approximate prediction.
2. **For mathematics, locate the obstruction.** Use same-fiber witnesses for non-descent, missing objects or suprema for completeness, and successor laws for predictive closure. Preserve the corrected examples and theorem hypotheses above.
3. **For toroidal replay, close the execution gap.** The complete proof verifier is recovered. Seek the original companion authority and comparable event prefixes if available. Otherwise work under the already defined prospective replacement profile, implement configuration enforcement and lossless recording, and validate replay without claiming the historical mismatch is solved.
4. **For useful prediction, specify an approximation problem.** Choose B, r, horizon, clock, tolerance, and evaluation domain. Compare full-state or causal-filter behavior with candidate retained coordinates. Report pairwise lower bounds separately from uniform guarantees.
5. **For empirical work, use the complete frozen instrument.** Preserve eligibility, denominator, uncertainty, coverage, holdouts, and independent confirmation. Fit validity, scale admissibility, accessibility, stationarity, and mixing remain separate conditions.

No new physical Q1/Q2/Q3 result, global non-descent geometry, holonomy, or mechanism attribution follows from assembling this file. Add future changes with the source, affected claim, evidence scope, and date. Do not promote a historical unresolved result by editing a summary label.

## 16 Sources, review coverage, and verification

These are the sources behind this consolidation. The equations and distinctions above can be read without opening them; execution and proof-level continuation require the relevant complete source.

- **S1 — [GEOMETRY + GQG — Working Master](https://docs.google.com/document/d/1Cn00U9Cj37QRrK2Xg3bX1417xYKstkFzednitR9xjog/edit)**. Current first tab; earlier Geometry v2 body in its source tab.
- **S2 — [TOROIDAL — Working Master](https://docs.google.com/document/d/1NV7JsFuqJJVjFzYcqCAuC22y_rrjCSqqcZWZKobcGoU/edit)**. Current consolidation v0.4 first tab, with September 28 integration and recovered verifier; earlier release retained separately.
- **S3 — [New geometry](https://docs.google.com/document/d/1DVgC8ia4Z1suHmLbcrDbvw1ETuSjkTm25_5DH8OOQNI/edit)**. Isotope synthesis, witness-relative geometry, and the geometry integration note.
- **S4 — [Hidden Quotient v1.7 master](https://drive.google.com/file/d/1VF_UeW26X5LYpMYpfEtYvry8PjGX77Bj/view)**. Qualified theorem, witness restoration, seven companion bridges, and current geometry addition.
- **S5 — [Hidden Quotient Corrected Investigation 1.1](https://drive.google.com/file/d/1u3gyUGRK7Teqaa1lCZBd-WvhCuZDQM1k/view)**. Precise theorem qualifications, examples A–C, and identity/swap dynamics.
- **S6 — [Geometry Upgrade v0.1 — Predictive Fibers and Minimal Phase](https://docs.google.com/document/d/1dwlILms8z6YWJ_EFRCeoky6Fku9ND6A2xugZ008zOhk/edit)**. Deterministic predictive quotient, finite compiler, and minimal-phase companion.
- **S7 — [GQG v0.12 instrument](https://drive.google.com/file/d/13g-nyjUeMrtQRECXugx7DAdX5RrN0OzA/view)**. Complete empirical eligibility/response instrument and typed residual framework; apply the later clock correction when discussing autonomy.
- **S8 — [Toroidal Master v0.2 with dynamics integration](https://drive.google.com/file/d/1103tr4UUEIbyLYUxfE1zaCyn_E6MyAxW/view)**. Detailed field, topology, throat, protocol, and lineage reference.
- **S9 — [Toroidal Dynamics v0.1](https://docs.google.com/document/d/1jDBi4zR7W4fkJ_1F_gKU-RQPfkBgiBllXF5Pw1onP1Q/edit)**. Drive title v0; body v0.1. Full ideal kernel and numerical policy.
- **S10 — [TD-COS-FH-001 sector process has no finite Markov order](https://docs.google.com/document/d/1ON-nOrXUCCixHFm4WYIbihKtY47wQ2p0ylgR4r4opiY/edit)**. Historical native all-orders proof copy; its truncated embedded verifier is superseded for runnable access by S24.
- **S11 — [L=3 direct-reference follow-up](https://docs.google.com/document/d/1YNIuAhjiY9szcA9Q5uvMm0N-b88KEQ15jjzFRLvdanY/edit)**. Separate PASS record, counts, uncertainty screens, and reported replay.
- **S12 — [Deterministic mismatch investigation](https://docs.google.com/document/d/1G88zvSUXi78R6uCMJYBEZpOmFpIiyP8OAK8_gtd9Hxw/edit)**. Historical discrepancy and missing authority.
- **S13 — [Toroidal note versus recovered Section 35](https://docs.google.com/document/d/11nZWX9optKPLn9PX90cNktrj84iyafFNi3Pj1LDFZEk/edit)**. Corrected phase algebra and source-reported exact audit.
- **S14 — [Prospective replacement amendment](https://docs.google.com/document/d/1gXUSaFvix1R_7-sqtkO5m8VqZqxGnDbl2JiLXas8KF4/edit)**. Replacement profile, hashes, configuration issue, event/restart contract, and preserved statuses.
- **S15 — [Five String Acoustic Resonator Rev B](https://docs.google.com/document/d/1U05hPPHklm9yZBUcNHkLMYwDaUaaftbLBFkmeEbv_zQ/edit?tab=t.a4ezxd7jm5ha)**. Use the Geometry update G1 tab for the stated dimensions.
- **S16 — [GEOMETRY — Working Master v2.6](https://docs.google.com/document/d/1S-mqz0aK_vCnmZiRVDPAr7rzTBgfoVuDDEyXEgHmkAk/edit)**. Exact repair, acquisition, path bounds, conditioning and causal padding.
- **S17 — [Geometry — Curated Upgrades](https://docs.google.com/document/d/1YGYq8OqNGejONtHdEidubFazE7BIEgfcvN_fxQS48ds/edit)**. Claim closure, AS-001, four-space evidence and September 28 integration.
- **S18 — [Geometry of Typed Defects](https://docs.google.com/document/d/1rkYnCM7JWL6uJaTagpIaYIDIzbX6MdcNCiiaydISJGA/edit)**. Versioned diagnostics; corrected calculus is also in New geometry §16.
- **S19 — [Gear mathematics — geometry checked](https://docs.google.com/document/d/1A2dGTW1cYhKV3nOs6at9GhjNX4ZWAoNp74013Gq2a4U/edit)**. Recovery, conditioning, coverage and geometric examples.
- **S20 — [GEOMETRY — Upgrade v2.2grok](https://docs.google.com/document/d/1bhllDANiLCIVGuTb_cFqi3UZ3rgkS-yd-I6iCHdEdx4/edit)**. Spectral witnesses and limits on imported correspondences.
- **S21 — [DIRECT SERVICE GEOMETRYv2.6](https://docs.google.com/document/d/1vVy2Bk01klLgyfVDkOoxdOddlXEc02wIydAofFY59Bc/edit)**. Current recurrence correction and selected-text/service-history distinction.
- **S22 — [TTSC-1 v0.3](https://docs.google.com/document/d/1M4B5m4fPfS1W7JBffL7B02hlq-86oKTDwyJZPeaL33Y/edit)**. Spatial comparator; §20 status wording corrected in this portable reference.
- **S23 — [Temporal exchange rate](https://docs.google.com/document/d/1obKlNpy47T8Km074kHQ499KUH3Z1Q47nhRC8GUEE7rA/edit)**. Timing witnesses and empirical limits.
- **S24 — [Complete TD-COS-FH-001 proof and verifiers](https://github.com/MailanPatternMonkey-ai/Gettin-Started/tree/e8623fa88a6e049e17e7564222356a6675d6b29d/corpus/mathematics/TD-COS-FH-001)**. Immutable recovered package and independent rational certificates.
- **S25 — [Toroidal Replay Handoff — Source Edition](https://docs.google.com/document/d/1BaTdiLY1HkwOe0Ums1rnM3WjCpx-CpAof6bE9i3qix0/edit)**. Recovered inputs and outstanding replacement implementation.
- **S26 — [Hidden Quotient Behind the Multiplication Representation](https://docs.google.com/document/d/1fdVBmS2i3lz0a8o2EAV5NP5Z1S_6kM7Vvgg_z0h9XW8/edit)**. Recovered standalone text; older qualifications do not supersede v1.7.
- **S27 — [Geometry collection review — September 28](https://docs.google.com/document/d/1FN4txPFFJdZKMXg2xg2BpoYslPNXBGjJ8dvTInFlvZc/edit)**. Historical 62-text review and scoped software receipts; not fresh October executions.
- **S28 — [Geometry update — current document index](https://docs.google.com/document/d/1XK-iCWufDUcsrumwR_1OP3_25XKutio4KePOm1KXQ30/edit)**. Routes current geometric additions and versions.
- **S29 — [Cos-Tim Architecture](https://docs.google.com/document/d/1mb_4itn1aFOkYHZbbOt_ysbzNYz11NirtW3CfM2-c0k/edit)**. Screened proposed cross-domain architecture; no new mechanism adopted.
- **S30 — [GQG card](https://docs.google.com/document/d/1Mrm8KAaUsh5e2izR9K4VZqNKEn5enEFshnskHuBznGg/edit)**. Current condensed GQG reference.
- **S31 — [Geometry Maximization v1.61 — Proof-Clarity Patch](https://docs.google.com/document/d/1xMAm07ObGKUfK5uMz-fvjr7v_IaS6DOoiB68LrZN9k8/edit)**. Screened proof-clarity lineage; detailed claims retain their original scope.
- **S32 — [Toroidal Full-Packet Audit v0.2](https://drive.google.com/file/d/1dkJr1shU0Rzf0jn55Ud_QT6-qHzWL4Pz/view)**. September 3 audit; read as historical protocol assessment, with later kernel theorem kept separate.
- **S33 — [Hidden Quotient — Core, Witness, and Strike](https://docs.google.com/document/d/1WhRhyVqrz7lZXPawJfjs8GBnnCis3oMCFYk6fnvFH7k/edit)**. Current native precedence notice and later integrations.

**Review coverage, 18 October 2026.** The direct Drive connector was unavailable; authenticated browser access recovered the current Docs. This pass searched geometry, toroidal, hidden quotient, and the full-packet audit, screened current indexes and version relationships, and read the current mathematical, Hidden Quotient, Toroidal, predictive, typed-defect, gear, spectral, timing, service, and integration texts listed below. The restored September packet was read in Drive's preview. Exported text represents selected working tabs, not every historical tab, native element, comment, revision, or file in Drive. Historical source links S4–S5 and S7–S15 are carried from the earlier consolidation unless specifically refreshed through their current receiving masters. This is a broad current-source upgrade, not a claim that every Drive file or every theorem was exhaustively re-proved.

**Verification in this pass.** The definitions, finite acquisition arguments, uniform path bound, and causal-padding proof received mathematical review. Independent exact checks cover n=1,…,32 threshold models, the skew-prior expected optimum, timing and prime-label examples, and a sharp path-law fixture through horizon 12. Large source suites and historical sampler receipts remain source-reported. The experimental rectangular-torus extension explored locally was not adopted into the governing theorem. Source export hashes and review depth are recorded in the accompanying review receipt.

**Version note.** This updates the portable file; online source bodies were not edited in this pass. Section 14 identifies older source wording that still needs synchronization. A linked document changing later does not silently update this snapshot. The pre-upgrade file is preserved in the review workspace.
