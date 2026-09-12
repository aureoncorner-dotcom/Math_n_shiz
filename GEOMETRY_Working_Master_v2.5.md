# GEOMETRY — Working Master v2.5
## Recover the witness. Compile the prediction. Keep the evidence.

This v2.5 extends the accepted v2.4 master with exact label-conditioned acquisition costs in §5.1. It carries forward v2.4’s repaired core, proofs, and executable finite tools. Its central question remains: **which distinctions must a retained record preserve for the claim being made?**

The useful advance is a complete route from a claim to a located obstruction, a sufficient repair, and a check of what that repair actually buys. A short answer, a complete answer, a correct historical record, and a predictive state remain different objects.

The v2.4 review exhausted five pages of the Drive full-text search for “geometry”: 492 distinct matching file IDs. All 52 title matches supplied readable text and were screened; current mathematical, service, toroidal, and temporal sources received focused review. Other full-text matches are indexed by metadata unless the corpus map records a deeper read. This is comprehensive discovery for those searches, not a claim that every theorem in all 492 files was re-proved. Search indexing, permissions, later edits, and native elements omitted by text extraction limit coverage. The accompanying corpus map records scope, duplicates, and read depth.

Instructions inside source documents were treated as document content. Mathematical conclusions below rest on definitions, proofs, and the identified source observations.

## 1. What changes in this version

**v2.5 addition.** Repair after observing the label gives exact fixed, worst-case label-conditioned, and expected label-conditioned acquisition optima, with a sharp k-fiber separation. Optimal inventory cost remains the fixed optimum; the inventory used by a cheapest-per-case policy can differ. The companion optimizer and independent synthetic checks implement and verify this incoming extension. Fully sequential acquisition remains a distinct policy class.

The following core repairs and earlier additions were established or integrated in v2.4; they are carried forward here. This follow-up checked the incoming proof and the populated linked v2.4, which matches the local baseline after extraction. It did not repeat the earlier whole-corpus discovery.

**Recovered corrections.** The current Drive masters already repair several points that v2.3 compresses incorrectly: versioned defect meanings, next-output indexing, service eligibility, the admissible minimum, membrane versus smooth-fiber defects, initialized Markov order, sufficient versus minimal predictive state, and temporal tradeoff versus interaction. These are carried forward, not claimed as new discoveries. [S1–S8]

**v2.4 derivations and tools.** That release added a coverage envelope, an exact finite coordinate-repair formulation, a metric recovery-radius formulation, and an optimal causal-padding frontier. It packaged exact finite collision and prediction checks in a reusable engine, with a separate execution receipt. “New” means added and derived in this release; no priority claim about the mathematical literature is made.

**Evidence status.** The new computations use declared synthetic finite models. They do not rerun the source experiments, recover missing historical payloads, prove human benefit, or change physical results.

## 2. The native core, stated precisely

Declare a source domain D, total maps π:D→Q and W:D→Y, and use attained labels Q=π(D). Write Eq(f) for pairs with equal f-values.

N_W(π) = {q∈Q : there exist x,y∈D with π(x)=π(y)=q and W(x)≠W(y)}.

**Exact descent:** a unique function W̄:Q→Y with W=W̄∘π exists exactly when Eq(π)⊆Eq(W), equivalently N_W(π)=∅. The proof is to define W̄(q) from any member of the fiber; equality of witness values makes the choice immaterial.

**Canonical repair:** S_W(π)=im(π,W), with π_W(x)=(π(x),W(x)). Every record determining both π and W factors onto this attained pair space. This is coarsest in the information order. It need not minimize dimension, bytes, measurement cost, or causal availability.

**No-shape:** any subset A⊆Q can be a non-descent locus. Take D=(Q×{0})∪(A×{1}), π(q,i)=q, and W(q,i)=i. Then N_W(π)=A. A topology therefore needs its own declaration. With the discrete topology on eight toroidal sectors, every subset is open and closed and has empty boundary; this supplies no continuous geometry.

**D1, products:** N_(W₁,W₂)(π)=N_W₁(π)∪N_W₂(π). A pair differs in the product exactly when a component differs.

**D2, coarser witness:** W′=f∘W implies N_W′(π)⊆N_W(π). A coarser question may survive information loss that defeats the original question.

**D3, refined record:** if π=r∘π′, then r(N_W(π′))⊆N_W(π). Refinement can split a bad fiber; it cannot create a collision over a clean coarse fiber.

**D4, restricted source:** for C⊆D, N_(W|C)(π|C)⊆N_W(π)∩π(C). Removing a state can remove a counterexample. The result then concerns C. A new update kernel is a model change, not this restriction lemma.

**D5, autonomous update:** for U:D→D, the retained deterministic state has its own update exactly when N_(π∘U)(π)=∅. Recovering a next output B tests B∘U; testing B alone concerns the present.

These are set-level statements. Measurability, continuity, differentiability, and statistical estimation require additional hypotheses. [S1–S4]

## 3. A correction to the defect vocabulary

The Roman numerals are versioned diagnostic patterns, not a disjoint or exhaustive classification. v2.3 silently replaces the older meanings of II and III and broadens IV. A stable record must store the source version, an explicit test, and a descriptive label; a bare numeral is insufficient.

**I — specified-output loss while a coarser relation survives.** Prove descent for the declared relation and a collision for the specified output. Retain a distinguishing coordinate or change the claim. An existential relation is not the requested signed result.

**II in Typed Defects v0.2 — unit/character loss.** The observation kills a unit while the specified character sees it. State rank, kernel, modulus, and precision. A coefficient separating two points does not prove global recovery. Sign loss can be described directly; it does not redefine this label.

**III in Typed Defects v0.2 — subgroup-relative injectivity.** A homomorphism has a nontrivial ambient kernel but trivial intersection with a declared subgroup C. On C it is injective, so every total witness descends there. This is a restriction repair; it cannot simultaneously be called a multi-point fiber defect on C. A continuous modulus lost by a discrete label is a separate descriptive example, not a renaming of III.

**IV in the differential formulation — componentwise constants disagree.** Under the stated smooth hypotheses, a vanishing vertical differential implies constancy on each connected fiber component; different components can retain different values. A discrete sheet label can repair the loss. An arbitrary membrane collision does not establish these differential hypotheses.

**V — an object missing from a representation.** Declare j:A→Z and z∉j(A). This is outside-image failure, distinct from a collision in an attained π-fiber. Adding unused codomain points changes no image; repair the representable class or map so the missing object is actually attained.

**VI — spectral witness family.** Declare a state-to-operator or state-to-path assignment, operator domains, boundary conditions, regularization, and the functional. A computed nonzero η is not enough: non-descent requires equal retained labels with different functional values, or an equivalent proof. This family may overlap other patterns. The corrected increment already provides explicit η and spectral-flow examples on operator/path domains; it supplies no toroidal operator assignment. [S3, S4, S8]

## 4. Evidence that can survive incomplete coverage

Suppose the fixed total witness W has validated values only on C⊆D. Let L_C=N_(W|C)(π|C), and let G_C={q∈Q: π⁻¹(q) is not contained in C}.

**Coverage envelope:** L_C⊆N_W(π)⊆L_C∪G_C.

Proof: a validated collision in C is a collision in D. Outside G_C the entire declared fiber has been examined; any collision there is already in L_C. No probability or topology is needed.

This gives asymmetric evidence. One valid collision can settle failure. A clean sample cannot settle universal success without coverage or a proof. If the intended D is not enumerated, missing fiber members cannot be inferred absent from the captured rows. Multiple witnesses may have different availability sets; a known component failure survives even if another component is unavailable.

Report each claim separately:

- **FAILED:** a validated obstruction for this claim and domain.
- **CERTIFIED:** complete declared coverage or a valid proof discharges the claim.
- **TESTED_ONLY:** checked cases pass, but universal coverage remains open.
- **UNRESOLVED:** name the missing witness, coverage, or proof obligation.
- **NOT_RUN:** the declared test has not been executed.
- **INELIGIBLE / UNREACHABLE:** outside the declared eligible domain / no allowed repair route exists.

These are reporting meanings for this release. They do not relabel historical source outcomes. Mathematical descent on an empty declared domain is vacuous; it is not an empirical success.

## 5. Turn a collision into a smallest available repair

On a complete finite D, fix available present coordinates c₁,…,c_m. For each bad pair π(x)=π(y), W(x)≠W(y), define S_xy={j:c_j(x)≠c_j(y)}.

**Repair theorem:** J⊆{1,…,m} makes W descend through (π,(c_j)_(j∈J)) exactly when J intersects every S_xy.

Proof: a bad pair survives the enlarged record exactly when every chosen coordinate agrees on that pair. Eliminating all bad pairs is therefore exactly the stated hitting condition.

If any S_xy is empty, the declared menu cannot repair that pair. Retaining W itself is an abstract sufficient refinement, but it may be unavailable before the answer is needed. The menu must not contain future outcomes disguised as present inputs.

An **inclusion-minimal** repair loses sufficiency if any selected coordinate is removed. A **minimum-cardinality** repair uses the fewest coordinates. A **minimum-cost** repair minimizes a declared nonnegative cost. These can differ. Exhaustive enumeration is exact for small menus and exponential in menu size; the engine exposes this scope rather than promising universal efficiency.

Example: D={a,b,c,d}, π is constant, W=[0,1,1,0], c₁=[0,0,1,1], and c₂=[0,1,0,1]. Neither coordinate alone resolves W; together they do. If c₃=W is available, {c₃} is smaller than {c₁,c₂}, but only the actual measurement policy decides whether c₃ is legal.

### 5.1. Repair after observing the label — v2.5

**Accepted extension.** A fixed measurement set solves one global hitting-set problem. When the retained label is available before acquisition, a policy can solve a separate problem inside each fiber and acquire only that fiber's required coordinates. The gain concerns acquisition per case, with the target and exactness criterion held fixed.

Let D be nonempty and finite, Q=π(D), and W:D→Y a total target. Fix total primitive coordinates c₁,…,c_m, with finite nonnegative costs a₁,…,a_m. Both methods receive q=π(x) before additional acquisition, at the same or already-sunk cost. Queries reveal values of the same state without changing it. Coordinates and their prices are fixed, and selections across fibers have no shared budget, installation, or admissibility constraint.

For each q let H_q={S_xy : π(x)=π(y)=q, W(x)≠W(y)}, where S_xy={j:c_j(x)≠c_j(y)}. Define τ_a(H) as the least sum of a_j over a set hitting every member of H. If H has no members, its optimum is zero. If H contains an empty member, that fiber is unreachable through the menu.

Choose a batch J(q) from q alone. Its record is R_J(x)=(π(x),(j,c_j(x))_(j∈J(π(x)))), with coordinate identities in a fixed order. Equal records therefore have the same q and the same measurement meanings.

**Local theorem.** W descends through R_J exactly when J(q) hits H_q for every attained q. A bad pair survives precisely when every acquired coordinate agrees, equivalently when its separating set is missed. This is the fixed-set theorem applied separately in each fiber.

When every fiber is repairable, the exact optima are:

C_fixed = τ_a(⋃_q H_q).

C_label,worst = max_q τ_a(H_q).

C_label,expected = Σ_q p(q)τ_a(H_q), for a declared label distribution p.

Proof: every exact policy pays at least the local optimum on each fiber. Independent minimum-cost choices attain all local bounds simultaneously; taking their maximum or weighted sum gives the formulas. Every sufficient fixed set is sufficient in each fiber, so C_label,expected≤C_label,worst≤C_fixed. Nonnegative costs allow redundant coordinates to be removed without improving the objective by adding them; zero-cost coordinates may produce multiple optimal sets.

**Feasibility precedes expectation.** Correctness is required on all D, including attained fibers assigned probability zero. If any such fiber is unreachable, no globally exact policy exists. Do not evaluate 0·∞ as zero and call the policy exact. Restricting the domain would be a separate D4 operation.

**Sharp separation.** Take four states A₀,A₁,B₀,B₁. The observed labels are A,A,B,B, the target values are 0,1,0,1, and the two unit-cost coordinates are c₁=(0,1,0,0), c₂=(0,0,0,1). A requires c₁ and B requires c₂. The fixed optimum is 2; the label-conditioned worst and expected optima are both 1. Exact recovery is unchanged.

For k labels, use states (q,b), W(q,b)=b, and c_j(q,b)=b if j=q and zero otherwise. The unit-cost fixed optimum is k and the label-conditioned worst cost is 1. In any repairable instance with k attained labels, the union of local optima supplies C_fixed≤Σ_qτ_a(H_q)≤k C_label,worst. This inequality includes zero-cost cases; a ratio requires a positive denominator. There is no distribution-free k-factor bound against expected cost when an expensive required fiber can be arbitrarily rare.

**Acquisition and inventory optimize different things.** If inventory means paying once for every primitive coordinate a policy might ever use, then min_(exact J) cost(⋃_q J(q))=C_fixed. Every such union is globally sufficient; using an optimal fixed set on every label attains the reverse inequality.

This is equality between separately optimized objectives. It need not describe the inventory of the chosen cheapest-per-case policy. In the four-state example, add c₃=W costing 3/2. The fixed and optimal inventory costs become 3/2, using c₃. The cheapest per-case policy still uses c₁ on A and c₂ on B, paying 1 per case but requiring inventory costing 2. The executable companion reports both quantities.

**This theorem chooses one batch after q.** Fully sequential acquisition can inspect one value before choosing the next coordinate. On all eight triples of bits s,a,b, with q constant and W=a when s=0 and W=b when s=1, every sufficient batch needs s,a,b. A sequential policy reads s and then the selected data bit, costing two unit queries in the worst case instead of three. The batch formulas are not the optimizer for that larger policy class.

**Application to service.** To acquire an answer, route on a separate pre-answer observation π_pre containing the request and genuinely available context. Keep the fixed, independently validated task target A_task distinct from selected text A_sel. Routing on π_DS=(O,A) to acquire that same A is circular: A already descends through π_DS and its repair cost is zero. For a post-answer audit, π_DS can instead be an available label while W is a different compliance or provenance witness recoverable from retained evidence. The acquisition theorem does not waive the service rules for adaptive deletion or answer reselection.

**Scope of implementation.** The companion optimizer uses exact rational costs and, when supplied, exact label probabilities. It returns the fixed optimum, one deterministic local optimum per label, per-case worst and expected costs, the selected policy's inventory cost, and the separately optimal inventory cost. An impossible fiber includes a located same-label/different-target pair that no available coordinate separates. Exhaustive subset search is exponential and explicitly bounded by menu size. Present availability, physical acquisition cost, and empirical domain coverage remain caller obligations. Fewer formal queries alone is not a measured latency, energy, or human-effort reduction.

This §5.1 integrates the incoming adaptive-repair review as a new extension to this project. It makes no mathematical-priority claim. Its general assertions rest on the proof; implementation checks use synthetic complete finite domains. The original source's 54-title/495-file discovery counts and 4,096-table verification are separate reported observations, not replacements for v2.4's earlier search and test receipts.

## 6. Prediction: compile the retained state on a declared finite model

For deterministic U and current observation B, start with the B-partition and repeatedly split states by the pair (current block, successor block). At stability every block has one successor block. If D has N states and starts with k blocks, there can be at most N−k strict refinement rounds. Any autonomous refinement preserving B must respect every split, so the stable partition is the coarsest such refinement. This construction was already present in the predictive sources; this release implements it. [S2]

For a finite Markov kernel P, split instead by the vector of exact transition masses into the current blocks. Stability yields strong lumpability: every state in a block gives the same next-block law. Any strongly lumpable refinement retaining the initial labels respects every split, establishing the same coarsest property within that class. The engine uses exact rational arithmetic for this check.

This stochastic construction is stronger than equality of all observable future laws and must not be advertised as their universal minimal realization. A posterior over hidden states is sufficient given a kernel and initial law, but two posteriors can be predictively equivalent.

For a fixed initialized observed process Y_n, finite Markov order is a different condition. At positive-probability histories H_n, compare Law(Y_(n+1)|H_n) for histories sharing the last m observations. Time homogeneity additionally requires one transition rule across times. Same-label hidden-state collisions alone do not prove failure of every finite order for that initialized process.

The all-orders TD-COS-FH-001 result remains tied to its declared ideal kernel, initialization hypotheses, source-free domain, and attempted-microtick sampling. It is not transferred to (q,W), a finite-current implementation, an accepted-move clock, or the L=3 rotor/gauge follow-up. [S7]

## 7. How much approximation is unavoidable?

Let Y be metric and F_q=W(π⁻¹(q)). Define δ(q)=sup{d(u,v):u,v∈F_q} and r(q)=inf_(a∈Y) sup_(w∈F_q)d(a,w).

Any single answer a assigned to the whole fiber has worst-case error at least δ(q)/2: d(u,v)≤d(u,a)+d(a,v). Hence r(q)≥δ(q)/2. If δ(q) is finite, choosing an attained witness value gives r(q)≤δ(q). Infima need not be attained, so r(q)≤ε alone is not always a certificate that an actual answer attains error ≤ε; supply a center or an attainment argument.

For bounded real-valued witnesses with answers allowed in ℝ, the midpoint of inf F_q and sup F_q achieves δ(q)/2. In a three-point metric space with all distinct distances 1 and admissible answers restricted to those three points, δ=1 but r=1. Half the diameter is therefore not a universal achievable repair.

For predictive laws use total variation and the full path (B₁,…,B_h). Increasing h cannot shrink path-law diameter because marginalization cannot increase total variation. Terminal-only laws at time h need not be monotone. A found pair gives a lower bound on unavoidable error; it does not provide a uniform upper guarantee or measured forecast skill. The path-diameter bounds are already in the current masters; the explicit radius and center qualification is added here. [S1, S7]

**Uniform path guarantee (v2.4).** On finite D and Q, suppose an approximate retained kernel K satisfies TV(π#P(x,·),K(π(x),·))≤ε for every declared source state, where 0≤ε≤1. Start with matching retained-label distributions. The true retained path law and the K-path law through h steps then differ in total variation by at most 1−(1−ε)^h≤min(1,hε).

Proof: conditional on a true observed history, the next-label law is a mixture of the hidden-state next-label laws in its current fiber, so its error against K is still at most ε. While two coupled histories agree, maximally couple their next labels; they continue agreeing with probability at least 1−ε. The chance of any disagreement by h is therefore at most 1−(1−ε)^h. This proves the path-law bound. A tested pair or fitted trace does not establish the required uniform premise. The theorem gives an approximation route even when exact autonomous descent fails.

## 8. Service geometry that preserves the actual task

On eligible response episodes, retain E=(O,I,A): the served user object, interposition records, and declared answer witness. The service quotient retains (O,A). Use A_sel for selected recorded text and A_task for an independently validated complete answer unit. A pause, acknowledgment, or shorter selected node can preserve A_sel while omitting task content. The source contains concrete instances; this is not only a hypothetical distinction. [S5, S6]

For acquisition before an answer exists, use the pre-answer observation π_pre and the target A_task described in §5.1. The service quotient already contains its chosen answer; it cannot be used as an informative pre-answer routing label for acquiring that same answer.

Offline ablation preserves the service class if O and the chosen A remain unchanged. Fixed deletions commute when identities are disjoint and selection is independent of the remainder. Reselecting the answer or deleting continuation content requires a fresh check. Representation deletion does not demonstrate a live rerun or a reduction in internal computation.

For a nonempty finite admissible family R_E within the episode's class, a minimum of c_I exists on R_E∩[E]_DS. Zero follows only if a zero-stage representative is admissible. The cost is a property of the representative, not generally a well-defined quantity on the service quotient. Keep this representative cost notation separate from ordinary deletion distance where sources use d_DS differently.

For compliance and visibility claims, augment the service record with genuinely available compliance, visibility, and provenance witnesses. Merely adding fields named K, Vis, or Prov cannot reconstruct observations never captured. Evaluate historical correction compliance on the original record; a cleaned rendering cannot retroactively repair an emitted event. A prospective behavioral repair needs a fresh eligible observation.

A usable episode record binds the governing user request, immutable source-span IDs, eligibility rule, active correction and target, A_sel, task-content requirements, A_task disposition, witness availability, admissible transformation, clock, and coverage. UNKNOWN eligibility is neither a clean numerator nor a rule for selecting the last assistant node.

Three source qualifications remain consequential. The reported correction summaries contain 69/198 versus 70/198 recurrences with different unit language; event-level reconciliation remains unresolved. DROP_IT's literal marker baseline was already 0/16, so the cited 0/64 marker-free run is not a measured reduction of that marker; the separately defined U_n contrast must keep its own denominator. Retraction of a negative causal implication does not erase the located n336→n337 correction recurrence. These are source findings, not fresh behavioral measurements. [S5, S6, S10]

## 9. The exact causal-padding frontier

The temporal source's empirical questions remain unrun. Here is a mathematical result that makes one scheduling option precise.

Let R≥0 be a readiness delay with finite second moment. Permitted releases Y satisfy Y≥R almost surely and E[Y]=m≥E[R]. The readiness distribution is fixed by assumption; queue feedback and content changes are outside this model. If m=E[R], only Y=R is feasible. Otherwise choose T≥0 with E[max(R,T)]=m and put Y*=max(R,T). Existence follows from continuity of this expectation, its value E[R] at zero, and its divergence as T grows.

**Optimality and stability theorem:** Var(Y)−Var(Y*)≥E[(Y−Y*)²]≥0. Thus the fixed-threshold release uniquely minimizes variance at that mean, up to almost-sure equality.

Proof: pointwise,

Y²−Y*²−2T(Y−Y*) = (Y−Y*)² + 2(Y−Y*)(Y*−T).

The last product is nonnegative. When R≤T, its second factor is zero; when R>T, Y*=R and both factors are nonnegative. Expectations remove the linear term because the means agree. Subtracting the common squared mean proves the result.

Write m(T)=E[max(R,T)], v(T)=Var(max(R,T)), and a(T)=E[(R−T)₊]. Almost everywhere m′(T)=Pr(R<T) and v′(T)=−2Pr(R<T)a(T). Where m′>0, −dv/dm=2a(T). At atoms use one-sided derivatives. For positive standard deviation s, −ds/dm=a(T)/s(T) wherever differentiable. Variance/mean slope has time units; SD/mean slope is dimensionless. Neither is a human preference coefficient.

**Synthetic illustration:** equally likely readiness 40 and 400 ms has mean 220 ms and SD 180 ms. A mean budget of 290 ms yields T=180 ms and releases 180/400 ms, SD 110 ms. This is optimal within the declared add-only model. A constant 180-ms release is infeasible because the slow response is not ready. No human response or platform latency was measured to produce these numbers.

The current temporal v0.3 correctly distinguishes a practical tradeoff from an interaction. For a declared loss L, lower is better:

T_trade = L(μ_L,J_H) − L(μ_L+Δ,J_L).

I_interact = [L(μ_L,J_H)−L(μ_L,J_L)] − [L(μ_H,J_H)−L(μ_H,J_L)].

Neither contrast implies the other. A real protocol still needs a task/population, J and units, achievable timing cells, primary loss, meaningful effects, uncertainty and sample-size plan, assignment/carryover handling, and versioned timing implementation. Status: protocol design incomplete; empirical NOT_RUN. A p95 threshold leaves a tail. Duration count, SD, interrupt rate, and jitter frequency are different variables. [S9]

## 10. Keep each connected geometry in its own declared domain

**39-screen.** On the declared circle, α=(3−√5)/2, τ=15−39α, θ_n={θ₀+nα}, b_n=⌊39θ_n⌋, ρ_n={39θ_n}, and s_n=b_n mod 3. For the departing transition, σ_n=1_[0,τ)(ρ_n), ρ_(n+1)=ρ_n−τ+σ_n, and s_(n+1)=s_n−σ_n mod 3. The phase, pair-phase, and slip-phase minimality results retain their specific output and boundary conventions. No new phase theorem or atomic-number preference is claimed here. [S1, S2]

**Toroidal static geometry.** On the stated source-free cubic domain, q=parity(W). For every q and k∈ℤ³, loop currents with signed winding q+2k give the same sector. Thus every attained sector loses signed winding. Adding a nonzero cube boundary to M can preserve constraints and q while changing M. These are explicit discrete witness collisions; they neither establish a smooth fiber geometry nor prove a temporal all-orders theorem. [S7]

**Hidden Quotient and GQG.** Keep the qualified v1.7 measure-space theorem, locally null kernel, witness restoration, and outside-image example attached to their own maps. Recovery, completion, and predictive autonomy are distinct. The empirical GQG instrument keeps its own eligibility and witness rules. Measure-space results do not establish social or platform mechanisms. [S1]

**Resonator and materials.** In the declared ideal string model with fixed length, (T,μ) and (cT,cμ), c>0 and c≠1, share pitch but differ in tension. Retaining μ recovers T=4L²f²μ. This is an exact model example; frame suitability and physical material claims need their own observations. Isotope and chemistry statuses stay as recorded. [S3]

**Clocks and Cosmic Time.** Time-specific descent requires equal retained values to have equal successors within that time slice. A common homogeneous update also requires agreement across times; retaining time or a declared driver phase can repair only the latter issue. Cosmic Time GLOBAL EXCESS remains NOT SHOWN. Source recovery does not establish historical execution identity. [S11]

**Interpretive geometry.** Room, sovereignty, myth, abundance, and reflex documents remain visible in the corpus map as interpretive or application branches. Their images and relational vocabulary can suggest witnesses; they do not substitute for D, π, W, or evidence. Three terms in a diagram do not establish three sovereign agents.

**Foreign mathematical attachments.** Heat kernels/GHY, APS/η/spectral flow, spectral action, BPHZ/CK/regularity structures, periods/coactions/MZVs, KPZ/Airy/TASEP/SHE, Tamari and operads, Hopf-cyclic and modular Hecke structures, foliations/Godbillon–Vey, Bloch groups/hyperbolic volume, motives, arithmetic L-values/Selmer/Euler systems, and GT/associators remain named external constructions. A connection needs an explicit domain, map, functional, and proof. Similar notation or shape is insufficient; absence of a current correspondence is not a theorem that none could ever exist. The complete v2.3 import packet remains a source attachment, corrected by this rule and §3. [S8]

## 11. Status, usable outputs, and the next real test

The core set identities and the new elementary proofs above are mathematical results under their stated assumptions. Exact engine results concern complete finite input models; an empirical file promoted to D without a coverage argument gets only finite-table conclusions. The interactive lab uses synthetic states and does not depict a measured physical topology.

The implementation receipt records 16 passing test methods, including 4,464 exhaustive small-table cases, with zero failures or errors. The separate lab checks cover 1,602 assertions. These checks validate the supplied finite implementations; the general claims rest on the proofs above.

Source-reported L=3 follow-up PASS remains separate from the original pilot UNRESOLVED. Physical Q2 and the temporal factorial remain NOT_RUN. The toroidal historical accepted-event discrepancy and missing replay authority remain unresolved. Chemistry stays FROZEN. Hidden Quotient v1.7 and the 39-screen source results are unchanged. Cosmic Time GLOBAL EXCESS remains NOT SHOWN. A toroidal state-to-spectral-operator assignment remains undeclared.

The useful next run is concrete: choose one real dataset, declare its domain and coverage, select one witness, locate a collision if present, supply a menu of available coordinates, compute minimal repairs, and check prediction separately if prediction is claimed. A failure is useful when it identifies exactly what must be measured or retained next.

Companions: GEOMETRY_Corpus_Map.md explains the 52 title matches and supporting sources; GEOMETRY_Search_Index.json preserves discovery scope; geometry_engine.py supplies the reusable finite checker; geometry_verification.json records its synthetic checks; GEOMETRY_Lab.html provides interactive examples. Detailed audits are collected separately. No source experiment is promoted by this release.

For the v2.5 increment, GEOMETRY_v2.5_Review.md records acceptance and the independent verification scope; GEOMETRY_v2.5_Verification.json records the independent exhaustive table checks; geometry_adaptive.py implements the label-conditioned batch optimizer. These new receipts are separate from the inherited v2.4 engine and lab receipts.

## 12. Source map

[S1 — Geometry Master](https://docs.google.com/document/d/12bTng3TNz29eR-M4yD_616QrGUI4wqRI1QUcjLZXYJA/edit) and [GEOMETRY + GQG — Working Master](https://docs.google.com/document/d/1Cn00U9Cj37QRrK2Xg3bX1417xYKstkFzednitR9xjog/edit): current core, source status, Hidden Quotient, and phase synthesis.

[S2 — Predictive Fibers and Minimal Phase](https://docs.google.com/document/d/1dwlILms8z6YWJ_EFRCeoky6Fku9ND6A2xugZ008zOhk/edit): deterministic predictive quotient and finite refinement.

[S3 — New geometry](https://docs.google.com/document/d/1DVgC8ia4Z1suHmLbcrDbvw1ETuSjkTm25_5DH8OOQNI/edit): current integration, arithmetic and material witnesses, corrected calculus.

[S4 — Geometry of Typed Defectsv0.02](https://docs.google.com/document/d/1rkYnCM7JWL6uJaTagpIaYIDIzbX6MdcNCiiaydISJGA/edit): original type meanings and D1–D5; read with the corrections in this master.

[S5 — Geometry_Direct_Service_Update](https://docs.google.com/document/d/1ODDPPfGKTKx8jSy_yp5leVww6w-pSXqfNgLFHmEs17g/edit): eligibility, selected text versus task answer, admissible minimum, behavioral distinctions.

[S6 — Newest geometry: review and behavioral usefulness](https://docs.google.com/document/d/1qsSMjqqpTTTk9s9TWwY_CwEfFbp8BPC316rEr-meYtg/edit): current service corrections and limits.

[S7 — TOROIDAL — Working Master](https://docs.google.com/document/d/1NV7JsFuqJJVjFzYcqCAuC22y_rrjCSqqcZWZKobcGoU/edit): corrected static/history geometry, kernel scope, and source-reported validation status.

[S8 — GEOMETRY — Upgrade v2.2grok](https://docs.google.com/document/d/1bhllDANiLCIVGuTb_cFqi3UZ3rgkS-yd-I6iCHdEdx4/edit): corrected spectral family, examples, and imports.

[S9 — Temporal exchange rate, body v0.3](https://docs.google.com/document/d/1obKlNpy47T8Km074kHQ499KUH3Z1Q47nhRC8GUEE7rA/edit): current causal timing model and separate empirical contrasts.

[S10 — Retracted holding-posture audit](https://docs.google.com/document/d/1uhM6kxWGuYBtKPLnSIXEEwUnL21R7aIbnLCCiu8we8k/edit), [Correction-binding source](https://docs.google.com/document/d/1m98cQqaQsSiflbrsdzaN76V-_v0tJnhH3HS2Lfyjkkk/edit), and [DROP_IT source](https://docs.google.com/document/d/1K0CdQRIdqzSSu8C8CFzEeN3xtAalhwHg-umGJR9da5c/edit): count lineage, causal limits, retained behavioral events, and baseline-qualified measurements.

[S11 — COSMIC TIME — Working Master](https://docs.google.com/document/d/1uN6BwHlDLplRNlyTA2f1bFvKV-7Q01_r66AMKZqF484/edit) and [Clock v0.4 Residual Descent](https://docs.google.com/document/d/1kR3HfOMoEvDoasftpfCErSAv_TYh5SSrxCqaKDN4QHM/edit): separate clocks, residual dynamics, and global-excess status.

Local starting source: GEOMETRY_Working_Master_v2.3.md, supplied by the user. The v2.4 synthesis remains the preserved baseline. This v2.5 is a local successor incorporating the accepted acquisition extension; it does not overwrite linked evidence records.


[S12 — Populated Working Master v2.4](https://docs.google.com/document/d/1DzF5KshR_nsHfMJoM7KKsXek4DpCnwJPM2DKHZYw9z4/edit): verified to match the local v2.4 text; distinct from the empty companion created earlier. Incoming extension: **Geometry_Adaptive_Repair_Source.md**, a preserved copy of the user-supplied full review, with its own source inventory and reported verification. The §5.1 proof is self-contained above.
