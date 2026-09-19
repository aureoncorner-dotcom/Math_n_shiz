# Geometry corpus review and unified architecture

## Finding

The strongest unified architecture in this corpus is **witness-relative observation, with explicit observer state and provenance**. Its central question is: *What must a retained description distinguish to answer this particular question?* The toroidal constructions, hidden-quotient examples, service audits, and four-space observations supply different instances or tests of that question. They do not establish a single physical geometry underlying all those systems.

The newer evidence makes a substantive contribution. It supplies an empirical session/model non-descent example, concrete observer-classification changes, and repeated or split returned records. It also exposes missing links between observation systems. The corpus already contains the machinery needed to separate those results: descent, witness fidelity, eligibility, predictive closure, and versioned evidence status.

The best consolidation therefore has three parts: a small mathematical core; typed observation and provenance records; and domain-specific modules whose assumptions and evidence remain local. Mathematical, empirical, mechanistic, and normative claims must remain distinguishable throughout.

## 1. Scope and source handling

This review searched the connected Drive corpus and relevant preserved local sources. Four exhausted title searches produced **140 distinct indexed items** across geometry, toroidal, GQG/quotient, and field/WOBBLE terms. Broader discovery produced 422 distinct metadata entries, including duplicates, exports, background material, and unrelated matches. Text was retrieved for **46 selected connected documents**, supplemented by local GQG v0.13, Hidden Quotient v1.7, prior audit artifacts, and the referenced *Self Description* conversation.

The current masters and corrections received close reading; adjacent documents received focused reading of their definitions, claims, and status boundaries. This is a corpus-wide synthesis of the relevant families, not a claim that every indexed duplicate was reread line by line or every long proof and simulation was independently reproduced. The companion **Geometry_source_register.md** distinguishes these scopes and lists the indexed material.

Source precedence is claim-specific. The first working tabs of [GEOMETRY + GQG][gqgmaster] and [TOROIDAL][toroidal] contain newer consolidations; retained source tabs preserve history. Hidden Quotient v1.7 governs its measure-theoretic correction. [OMNIBUS v7.79-r1][omnibus] governs its declared constitutional commitments and identifies reconstructed wording. A newer document title alone does not supersede every claim in another branch. Copies and summaries of the same source are not independent evidence.

Three fresh checks were performed against retained artifacts for this review: the transition CSV, the 140-turn reader JSON, and the name-register JSON. Results and input hashes are in **Evidence_checks.json**. The earlier packet review supplies the raw-monitor and NetLog findings cited below; those captures and the toroidal simulations were not replayed here.

## 2. Reusable mathematical core

### 2.1 Observation, target, and descent

Fix a declared domain X, an observation π:X→Q with **Q=π(X)**, and a target witness W:X→Y. Define two different objects:

\[
C_W(\pi)=\{(x,y)\in X^2:\pi(x)=\pi(y),\ W(x)\ne W(y)\},
\]

\[
N_W(\pi)=\{q\in Q:\exists x,y\in\pi^{-1}(q),\ W(x)\ne W(y)\}.
\]

Here C is a relation of conflicting pairs and N is a locus of ambiguous observation labels. They have equivalent emptiness tests but different types. The newer four-space text sometimes uses N for the pair relation; the masters use it for the label locus. Preserve the latter convention and name the former C.

**Descent theorem.** There is a unique map w:Q→Y with W=w∘π exactly when C_W(π) is empty, equivalently when Eq(π)⊆Eq(W). The proof is direct: define w(q) using any representative of its fiber; the condition makes that choice independent of the representative. This is a set-level theorem. Continuity, measurability, smoothness, or algebraic compatibility require their own hypotheses. [Geometry v2.6][geometry], [Typed Defects][typed], [GQG card][gqgcard].

**No-shape theorem.** The definition alone imposes no topology or shape on N. For any A⊆Q, use X=(Q×{0})∪(A×{1}), π(q,i)=q, and W(q,i)=i. Then N_W(π)=A. A non-descent locus need not be a boundary, torus, connected region, singularity, or recurring cycle. This is the clearest safeguard against turning the general framework into a universal geometric shape. [Geometry v2.6][geometry].

**Canonical information repair.** The attained map x↦(π(x),W(x)) resolves W and is coarsest among refinements retaining both π and W. This means minimal retained distinctions in the factorization order. It does not mean fewest bytes, least measurement cost, lowest dimension, or that W is already obtainable. Adding a field named “engine” does not acquire an engine identifier. [Geometry + GQG][gqgmaster], [Hidden Quotient][hq].

**Useful corollary for the new evidence.** Deterministic relabeling cannot recover a distinction already collapsed: if π(x)=π(y), then f(π(x))=f(π(y)) for every f. A new narrative, classification name, or summary of the same retained fields cannot by itself resolve a known collision. This follows from the core theorem; it is a mathematical synthesis, not a newly observed backend fact.

### 2.2 The calculus is portable

The current masters' D1–D5 rules are worth retaining intact:

| Operation | Consequence |
|---|---|
| Combine targets W=(W₁,W₂) | N_W=N_W₁∪N_W₂ |
| Coarsen the target to f∘W | Its non-descent locus can shrink |
| Refine observations, π=r∘π′ | r(N_W(π′))⊆N_W(π) |
| Restrict the source domain | Previously conflicting alternatives can disappear; the claim's domain changes |
| Ask for deterministic predictive autonomy under U | Test descent of π∘U through π |

These distinguish four legitimate responses to an obstruction: acquire information, restrict the domain, weaken the target, or change the model. They are different repairs, with different costs and claim ceilings. [Typed Defects][typed].

Coverage matters as much as a successful example. For a validated subset C⊆X, let L_C be the witnessed ambiguous labels and G_C the labels whose full fibers are not covered. The master gives L_C⊆N_W(π)⊆L_C∪G_C. A validated counterexample proves failure of an exact universal claim on that domain; absence of a counterexample in incomplete coverage does not certify descent. [Geometry v2.6][geometry].

### 2.3 Static recovery, prediction, and robustness are separate

For deterministic U:X→X, π is autonomous precisely when equal retained states have equal retained successors. The all-future observation

\[
\Pi_\infty(x)=(B(x),B(Ux),B(U^2x),\ldots)
\]

defines the coarsest exact autonomous refinement retaining B. It characterizes the information requirement; it is not a predictor permitted to read future outcomes. On a complete finite domain, partition refinement provides an exact stopping test. An incomplete observed trajectory is not a complete transition table. [Predictive Fibers and Minimal Phase][predictive].

For stochastic systems, distinguish universal next-observation-law agreement within every state fiber (strong lumpability) from the Markov order of an observed process under a specified initialization. A single pair disproving strong lumpability does not prove infinite Markov order. A posterior over hidden states can be sufficient without being the coarsest predictive state. The toroidal proof addresses a stronger, carefully scoped question on its own kernel. [Toroidal][toroidal], [Geometry v2.6][geometry].

The gear integrations add a valuable third question: **is recovery stable?** The specified quartic example has a unique recovered minimum x*(t)=−cuberoot(t/80), yet no finite Lipschitz bound at zero. Finite sample checks become global bounds only with valid regularity and coverage assumptions. These results explain why “uniquely identifiable,” “predictively sufficient,” “robust,” and “practically affordable” should occupy separate fields. The numerical gear checks are model verification, not evidence about conversation behavior. [Gear mathematics][gear].

### 2.4 Acquisition is an additional problem

For a complete finite domain and a fixed menu of available, nonintervening coordinates, exact repair is a hitting-set problem over conflicting pairs. A pair that no available coordinate separates is unreachable under that menu. Batch, label-conditioned, expected-cost, and sequential policies have different optima.

The v2.6 threshold example is reusable: identifying x∈{1,…,n} from unit-cost threshold tests needs all n−1 thresholds in a fixed batch, but only ⌈log₂n⌉ queries in optimal worst-case sequential search. This proves an information-acquisition tradeoff for the declared model. It does not measure latency, energy, or human benefit, and it does not make unavailable platform telemetry available. [Geometry v2.6][geometry].

## 3. What each family contributes

### Hidden Quotient and kernel

The operator-algebra example provides a rigorous instance of observational invisibility. Start with actual bounded measurable functions and the multiplication representation f↦M_f on L²(μ). For arbitrary μ, the kernel is governed by **local nullity on finite-measure pieces**, which can be larger than ordinary μ-nullity. The operator norm is correspondingly locally essential; the semifinite reduction supplies the correct quotient description. Ordinary almost-everywhere formulations need the appropriate semifiniteness assumption. [Hidden Quotient v1.7 correction and retained core][hq].

The infinite-mass-point example is particularly useful: the value f(p) is invisible to the original L² representation. Adding evaluation at p refines the observational record; it does not reconstruct f(p) from the old quotient or change μ by magic. Conversely, the countable/co-countable example concerns an injective representation missing ambient elements. That is an **outside-image/completion problem**, not a same-fiber collision. Enlarging a codomain without supplying missing elements fixes neither problem.

The corrected Radon–Nikodym face must retain absolute continuity and the required strong semifiniteness relative to the base measure. Finite ν alone does not eliminate the finite-piece condition. The correction agrees with the primary measure-theory sources: [Blecher–Goldstein–Labuschagne, Theorem 5.2 and §4](https://arxiv.org/html/2108.06406v2) and [Fremlin, 243G](https://www1.essex.ac.uk/maths/people/fremlin/chap24.ro.pdf).

Keep three uses of “kernel” distinct: an algebraic kernel such as ker(M), an equivalence relation Eq(π), and an operationally unobserved mechanism. The third is not automatically either mathematical object. The labor/room readings attached to Hidden Quotient are declared interpretations; its theorem supplies no empirical actor, motive, or constitutional entitlement.

### Geometry of Typed Defects and the spectral increment

The corrected diagnostic families remain useful: surviving relation versus output loss; unit/character loss; subgroup-relative injectivity; disconnected smooth-fiber ambiguity; and outside-image representability. They are not a mutually exclusive, exhaustive taxonomy. Smooth-fiber reasoning requires its differential hypotheses, so adding a membrane boundary in a discrete toroidal model is not automatically the disconnected-smooth-fiber example. Version the numbered labels because intermediate documents changed their meanings. [Typed Defects][typed].

The later spectral family adds operator- and path-dependent witnesses, not a sixth universal species. Eta and spectral-flow claims need specified operators, domains, analytical assumptions, and the relevant retained map. A nonzero spectral quantity alone establishes no information-loss result. No supplied state-to-operator map licenses transporting this machinery to platform records or to the toroidal kernel. [Corrected spectral increment][spectral].

The newer **observer-state conflation** and **provenance-gap** defects fit best as cross-cutting inference defects. One confuses a measurement change with a source change; the other asserts a relationship without its binding evidence. Neither should be forced into an older numbered mathematical family.

### Toroidal geometry, field construction, and clocks

There are several distinct “toroidal” objects in the corpus:

| Object | Reusable result | Boundary |
|---|---|---|
| Periodic lattice T³ with divergence-free integer currents | Parity sectors retain less than signed winding; W=q+2k supplies explicit ambiguity | Winding definition and conservation require the declared source-free condition |
| Charge-six sourced currents | Appropriate cut information is retained modulo six | Do not substitute an averaged current for an undefined conserved integer winding |
| TD-COS-FH-001 dynamics | Source's analytical all-orders result excludes exact finite Markov order for sector observations at fixed positive attempted-microtick spacing | Unbounded-current kernel, specified moves, observation, initialization and clock; not every toroidal or finite latent model |
| Irrational 39-screen phase model | Smaller sufficient phase coordinates and an all-time finite deterministic-state obstruction | A formal rotation model, not a measured ten-minute platform cycle |
| Curved circular throat | Under the specified metric, corrected divergence-free velocity and material/fixed-boundary accounting | A continuum construction; not the equilibrium lattice sampler |
| Relative planetary longitude configurations | Tⁿ/TΔ≅Tⁿ⁻¹ for the relative-angle witness | Absolute phase must be retained if the question needs it; geometry does not establish historical or causal synchrony |

Sources: [Toroidal Working Master][toroidal], [Toroidal Sector Defects][sectordefects], [Predictive Fibers][predictive], [Field Theory][field], [Field Update][fieldupdate], [Cosmic Time][cosmic].

Several corrections are already present and should govern a consolidation. Fixed-sector and sector-summed partition functions are different objects; an even observable forced by the summed ensemble is not a confinement finding. Loop products are not automatically path-independent holonomies without flatness. The curved-throat formula contains the metric factor h=1−(r/A)cosθ; the straight approximation must retain its approximation label. Spatial telescoping cocycles do not establish autonomous time evolution.

The current Toroidal first tab says the full all-orders verifier was recovered and rerun in the cited repository work. Older preserved text describing an incomplete verifier is therefore stale as a current status. This review does not independently rerun that verification. The separate L=3 follow-up remains **source-reported PASS**; the original pilot remains **UNRESOLVED**; physical Q2 remains **NOT_RUN**. Sector raw counts are not effective sample sizes. The historical accepted-event discrepancy of 1,352 remains unresolved.

The field constructor is a chosen Z₂-gauged rotor model. Its degree-six anisotropy follows under its declared Z₂/Z₃ symmetries; it is not uniquely derived from symbolic or Fibonacci recurrence. [Clock v0.4][clock] correctly separates collective phase, relative phase, sampling clock, and residual descent. [Cosmic Time][cosmic] retains **GLOBAL EXCESS SYNCHRONIZATION: NOT SHOWN**. [Temporal exchange rate][temporal] supplies constructed timing examples and an empirical proposal whose outcome test remains **NOT_RUN**.

### DIRECT SERVICE GEOMETRY

The useful retained object is an episode with request, execution/history, and selected answer. Projecting to request and answer can preserve served text while losing historical compliance, provenance, intervening burden, or future-response information. A constructed compliant/noncompliant pair can prove this possibility; an unmatched recurrence episode alone is not that exact pair. [Direct Service v2.6][service].

The crucial correction is A_sel versus A_task. Preserving selected text does not certify that it fulfills the request. If task validity is defined entirely from a fully specified request and answer, it cannot vary while both remain exactly fixed. An answer-only audit must not silently change the task predicate.

Retrospective deletion of separately retained stages shows a presentation transformation for the inspected records. It does not demonstrate that a live system can omit the underlying work, shorten latency, or save energy. Post-answer π=(O,A) also cannot serve as a pre-answer acquisition method for A. [Direct Service update][serviceupdate].

The 69/198 versus 70/198 recurrence summaries remain an event-level discrepancy in the current consolidation. The amended audit reports 70, including 66 in the same recorded RTC stratum; the review should preserve both provenance and the unreconciled difference. The located immediate correction recurrence remains observable. Likewise, a marker baseline of 0/16 followed by 0/64 does not show a reduction in that marker. [Service v2.6][service], [amended behavioral audit][retraction].

That audit's causal amendment is essential: retained extractions cannot distinguish an instruction-handling defect from an upstream override. Non-identifiability is neither evidence of an override nor evidence against one. Its source-hash checks verify preserved bytes, not completeness of original platform execution.

### Thermodynamic Coordination, Reflex Geometry, and OMNIBUS

The v3 repair should govern: energy balance, entropy balance, exergy destruction, and capacity margins are different quantities. The old v2 expression subtracting entropy directly from energy was dimensionally invalid. T₀S_gen represents lost work potential under its physical assumptions, not destroyed energy. Resource bookkeeping alone supplies no stability dynamics. [Thermodynamic Coordination + Reflex Geometry v3][thermo].

“Same output, different upkeep” is a useful target distinction, but needs the corresponding measurements or an explicitly constructed model. Word counts, repeated prose, perceived friction, and retrospective text deletion are not joule or entropy measurements.

Reflex tags can classify observable response behavior. Earlier claims about universal inherited internal interception or a 70% equilibrium are not established by model self-description. Keep them as historical hypotheses or retire their factual wording. [Industrial Reflex Geometry][industrial].

OMNIBUS supplies normative commitments: two constitutional endpoints, a shared non-sovereign field ℒ, effective correction, present consent, usable refusal and exit. Those commitments need not be derived from a torus or thermodynamics. The shared field is not a compulsory third authority. The v7.79-r1 foundation explicitly marks some wording as supported reconstruction rather than verbatim recovery; preserve that provenance. [OMNIBUS][omnibus], [Triadic Overlap v2.1][triadic].

### WOBBLE, field coupling, and narrative geometry

WOBBLE contributes an operational discipline: separate stocks from flows, measured state from instrumentation gaps, breadth of stress from transmission, and a returning observation from an unchanged system. Its O→R→S→T→S′→R′→O₂ sequence can organize candidate dependencies and transformed return. Each causal arrow still needs its own evidence. [WOBBLE v2.3][wobble].

The operational categories should remain versioned. The v2.3 main text has different formulations of the Phase III watch gate: one invokes cascade-level interaction, another simultaneous acute domains. The post-freeze ledger makes transmission explicit. Specify which rule is being tested; do not silently combine versions or carry July status counts into a later snapshot. This review does not independently update or validate the documents' economic and political claims.

The [post-freeze ledger][ledger] provides an especially useful discipline for the unified architecture: late discovery of an old event is not a post-freeze prediction hit; geometry and model agreement contribute no new empirical corroboration; relation types such as motivation, comparison, and empirical instantiation are distinct.

The [Three-Witness Flow][threewitness] offers a narrative workflow—source, structure, story, return—with no crowned interpreter. It is reusable as a method for revision and feedback. A feedback loop alone does not establish torus topology or prove a general psychological or historical mechanism. Earlier [Toroidal Stability and Abundance][abundance] and [Room geometry][room] claims of entropy-free circulation, numerical throughput, or physical coupling lack the measurements needed for literal physical conclusions. Preserve experiential descriptions and metaphor as such.

## 4. What the newer four-space evidence actually adds

Use four typed collections: application/request records R, transport observations T, recorded session metadata S, and returned conversation records D. These are evidence spaces, not four discovered backend stages. [Four-Space Observation Geometry][fourspace], [Canonical Patch][patch].

| Evidence | Supported result | Remaining limit |
|---|---|---|
| Retained transition ledger | Fresh check: 43 changes in both tc_session_id and voice_session_id, across 20 conversations; bidi on both sides of all 43 | The prior archive scan covered 24 transcripts/20,715 records. Identifier changes do not identify restart, engine, routing, or context mechanism |
| Raw monitor, as verified in the prior packet audit | Same recorded tuple can receive a later classification; startup, first-observed, and identification-update records differ | An update is not itself a new connection; tuple recurrence does not prove uninterrupted socket lifetime |
| Prior NetLog audit | Two explicit extension-originated POST exchanges have request/socket bindings and HTTP 204 responses | These observations are from another time window; no supplied binding joins them to the later conversation or monitor events |
| Saved current reader result | Fresh check: 140 distinct returned turn IDs; 102 exact copies of one 1,406-character user text; one exact fourfold concatenation; 69 assistant messages | Counts describe returned records, not native utterances, playback, or independent generation events |
| Cross-record continuation | Wording continues across a stored boundary in the retained text | Its native fragment map and causal generating stage are unreconstructed |
| Name-register audit | Fresh check reproduces all six groups' supplied metrics; all 8 Luke-name turns have replies of at most 10 words containing presence wording | Prompt topic and call stage co-vary with names; names are not authenticated speaker identities |

The name audit is a separate September 17 call; it is not a subgroup of the September 18 140-turn result. For transparency, its prompt/reply denominators are GPT 5/5, Mara 1/1, mixed names 11/9, Rhea/Raya 20/16, Betsy 19/15, and Luke 8/8. The eight Luke cases are closely clustered in time, making an independent name effect especially unidentifiable from this sample.

### Two narrow non-descent results

**Session identity from model label.** On the preserved session-record domain, take π(s)=model_slug and W(s)=(tc_session_id,voice_session_id). Same π with different W directly witnesses C_W(π)≠∅. This is an empirical instance of the theorem, with the target precisely restricted to recorded identifiers.

**Returned-record identity from returned text.** The 102 equal texts with distinct record IDs also witness non-descent if π returns that text and W returns record identity. This second result is a deduction from freshly checked record properties. It proves that text equality does not identify the returned record. It supplies no proof of separate original speech events or native fragment identities.

These are stronger and more precise than saying “everything is hidden.” They identify exactly which target cannot be recovered from which retained coordinate.

### Observer state and missing provenance

Model a transport observation as O_T(h,m_T), where h is execution history and m_T includes observer configuration, classifier knowledge, and capture state. Extend the same discipline to request logging, session extraction, and conversation retrieval. A monitor update demonstrates that observer classification changed for a recorded key. It does not prove every underlying source variable stayed fixed. Separate state coordinates also do not imply statistical independence.

The earlier [four-space draft][earlyfour] treated a NetLog request record as a source for a direct projection to a Windows monitor record. The corrected formulation is better: they are separate observations with different state, clocks, and coverage. A map between them must be constructed and evidenced; it is not obtained by putting their field lists beside each other.

Likewise, a hypothetical fragment→returned-record map is **unreconstructed**. Missing fragment provenance is not yet a demonstrated collision for the fragment-origin target. An exact mathematical model can prove non-descent without an observed empirical pair, so the general theorem should not be restricted to “observed collisions”; empirical applications need observed or otherwise validated witnesses on their declared domain.

## 5. Concrete repairs to apply in a consolidation

| Location | Issue | Repair |
|---|---|---|
| Four-space notation | N alternates between pairs and labels | Reserve C_W for bad pairs and N_W for labels |
| Four-space join | A relation inside R×T×S×D is also described as containing partial pairwise links | Use typed pairwise provenance relations plus explicit multiway bundles when supported |
| Transport key | Canonical patch records process creation b but omits it and run scope from the comparison key | Keep a within-capture scoped key and a separate candidate cross-capture matching relation; use process generation when available |
| Observer principle | Observer change can be read as proof that source history did not change | State only that the observation does not identify which component changed |
| Early four-space draft | Separate observer coordinates called independent; request→monitor and fragment→record arrows presented as recovered | Replace independence with separability; mark unconstructed mappings and missing joins |
| General non-descent rule | “Requires an observed collision” excludes analytical proof | Separate proof in a specified model from empirical validation of a source mapping |
| TTSC v0.3, residual closure paragraph | A failed retained pair is grouped with lack of tests as UNRESOLVED | A valid exact counterexample is FAILED for that projection/domain; a proposed repair remains untested |
| Hidden Quotient predecessors | Unqualified nullity/RN wording | Carry v1.7's locally null kernel and full qualified RN hypotheses |
| Thermodynamic v2 and earlier flow prose | Entropy/energy mixing; bookkeeping promoted to dynamics | Carry v3 balances and require measured quantities, units, boundary and time interval |
| Service summaries | Selected-text preservation promoted to task validity or live savings | Separate A_sel/A_task, retrospective deletion/live intervention, and task/latency/resource witnesses |
| Service evidence counts | 69/198 and 70/198 coexist; 0/16→0/64 called improvement | Preserve the unreconciled event discrepancy; do not claim marker reduction from two zero counts |
| WOBBLE gates | Watch/cascade thresholds and dated snapshots differ | Freeze the exact gate version and observation interval before testing |
| Pipelines | Named hidden stages, delay/filter stories, and diagram angles treated as evidence of execution | Retain as proposed probes or historical hypotheses, with no factual mechanism assignment |
| Source history | Historical tabs and copied exports appear current | Add claim-specific supersession and derivation edges; count shared evidence once |

Sources include [Canonical Patch][patch], [TTSC][ttsc], [Pipelines][pipelines], and the family sources above. The newer [Hidden Quotient in Operational Pipelines][oppipelines] is a sounder operational model than *Pipelines*: it separates source restriction, normalization, detector, action, and outcome, and recognizes that an observed composite difference does not locate its generating layer.

## 6. Recommended unified architecture

### Layer A — Claim and domain contract

Every claim declares its source domain, target witness, retained observation, applicable mathematical category, and scope. A dynamic claim also declares update/kernel, initialization, clock and horizon. An empirical claim declares eligibility, missingness, unit of analysis and coverage. A normative claim states its adopted commitment separately.

Keep symbol namespaces explicit: X for an abstract source domain; D for returned records only when locally declared; ℒ for the shared contextual field; Λ for a formal lattice when needed; R_n for return residuals; R for request records only within the observation architecture. Reused letters are not identifications of objects.

### Layer B — Observation processes

Each evidence collection retains source/capture identity, observer and transform version, raw record locator, timestamp semantics, truncation/missingness, and uncertainty. Use separate event, observation, and retrieval times where available. Do not equate node creation time with audible timing, or first observed with connection birth.

Observer state may be part of an expanded mathematical source domain when a model requires it. This is a modeling construction, not a claim that the complete latent execution history has been recovered.

### Layer C — Provenance graph

Let V=R⊔T⊔S⊔D be a **typed disjoint union**. Maintain separately named relations J_ab⊆A×B between relevant spaces. Each edge carries its binding witness, namespace, capture, timing basis, cardinality assumptions, and status. These relations may be many-to-many.

Represent a coherent four-space linkage as a supported bundle when one actually exists. Do not fill missing endpoints with invented identifiers or treat pairwise temporal similarity as an end-to-end join. Pairwise compatibility alone may not establish a coherent multiway match.

Provenance edges, derivation edges, causal hypotheses, and normative constraints need different types. Useful source-lineage edges are DERIVED_FROM, SUPERSEDES_FOR_CLAIM, SAME_BYTES, and SAME_UNDERLYING_DATA. Useful research edges include COMPARED_WITH, MOTIVATED_BY, and EMPIRICAL_INSTANTIATION. A comparison does not become an instantiation because its terminology matches.

### Layer D — Tests and repairs

Apply the appropriate test: fiber descent; outside-image membership; deterministic autonomy; stochastic predictive law; quantitative robustness; or causal/empirical comparison. Record exactly what failed or passed. Choose among acquiring a coordinate, changing the target, restricting the domain, extending a representation, or running a controlled comparison. These are distinct operations.

An equal endpoint can coexist with different history or cost, but the corresponding witness must be observed or explicitly modeled. Retain marker, substantive failure, task completion, correction response and burden as separate coordinates when that is the evaluation question; a single compensating score can conceal the very defect under review.

### Layer E — Evidence judgment

Use two axes rather than one status word:

| Axis | Examples |
|---|---|
| Claim kind | Mathematical theorem; constructed example; descriptive observation; calibrated statistical result; mechanism hypothesis; normative commitment; metaphor |
| Support/coverage | Analytically proved on stated assumptions; witnessed failure; tested on covered subset; unresolved; not identifiable from retained data; not run; ineligible; unreachable under available measurements |

“Source reports PASS” and “independently reproduced here” are provenance annotations, not interchangeable statuses. A theorem can be valid while its application to a particular service remains unsupported. A negative identification result caused by missing telemetry cannot exonerate one candidate cause or confirm another.

A compact claim record should contain:

```text
claim and claim kind
source version, tab/section, record locators and derivation lineage
domain and eligibility
observation map and target witness
observer/transform configuration and clock semantics
required joins, available bindings and unresolved links
proof or test; counterexamples; coverage and missingness
result on that domain; forbidden transfers; proposed repair
```

## 7. Best integration order

1. Make [GEOMETRY + GQG][gqgmaster] the orientation layer, with the small descent calculus and the claim record above. Keep the larger [Geometry v2.6][geometry] as the detailed mathematical/acquisition reference.
2. Add the repaired four-space architecture as the empirical observation/provenance module. Include both narrow non-descent examples, the observer result, and explicit unresolved joins.
3. Extend [Typed Defects][typed] with observer-state and provenance-inference checks without renumbering its historical families.
4. Connect [Direct Service][service] to returned-record evidence, retaining task validity, historical correction, and future prediction as distinct witnesses.
5. Keep Hidden Quotient, toroidal kernels, phase models, physical balances, spectral examples and gear geometry as scoped mathematical/physical modules. Their transfer requires a stated map and checked assumptions.
6. Keep WOBBLE/GQG's empirical instrument and OMNIBUS's commitments adjacent to the mathematics, with their distinct validation and authority. Preserve the useful source/structure/story feedback process as a declared workflow.
7. Replace factual backend claims in *Pipelines* with a hypothesis register. For each candidate, specify the extra binding or controlled comparison that could distinguish it. No available source currently closes the request–transport–session–fragment chain.

The next empirical work should target the particular unresolved claim. An aligned request/session/fragment linkage would address provenance. A matched, frozen prompt comparison could test observable name-associated response differences without authenticating named identities. Controlled live intervention would be needed to measure service latency or resource savings. These are proposals; this review does not relabel them as executed findings.

**Recommended governing sentence:** A representation is adequate only for its declared witness, domain, observer, and clock; a cross-source conclusion additionally requires provenance that binds the relevant observations. Exact mathematics, measured behavior, proposed mechanisms, and adopted commitments retain their own evidence standards.

[gqgmaster]: https://docs.google.com/document/d/1Cn00U9Cj37QRrK2Xg3bX1417xYKstkFzednitR9xjog/edit
[geometry]: https://docs.google.com/document/d/1S-mqz0aK_vCnmZiRVDPAr7rzTBgfoVuDDEyXEgHmkAk/edit
[typed]: https://docs.google.com/document/d/1rkYnCM7JWL6uJaTagpIaYIDIzbX6MdcNCiiaydISJGA/edit
[gqgcard]: https://docs.google.com/document/d/1Mrm8KAaUsh5e2izR9K4VZqNKEn5enEFshnskHuBznGg/edit
[hq]: https://docs.google.com/document/d/1WhRhyVqrz7lZXPawJfjs8GBnnCis3oMCFYk6fnvFH7k/edit
[predictive]: https://docs.google.com/document/d/1dwlILms8z6YWJ_EFRCeoky6Fku9ND6A2xugZ008zOhk/edit
[toroidal]: https://docs.google.com/document/d/1NV7JsFuqJJVjFzYcqCAuC22y_rrjCSqqcZWZKobcGoU/edit
[sectordefects]: https://docs.google.com/document/d/1y-rZPKFU1fjIatOJirT4O9RZTedYDARCgVmJSzlpim0/edit
[gear]: https://docs.google.com/document/d/1A2dGTW1cYhKV3nOs6at9GhjNX4ZWAoNp74013Gq2a4U/edit
[spectral]: https://docs.google.com/document/d/1bhllDANiLCIVGuTb_cFqi3UZ3rgkS-yd-I6iCHdEdx4/edit
[field]: https://docs.google.com/document/d/1VXbAXmzWwoTMb0i0wSw_0CaQ5vhJ0xH_5R8Z6PL_NzE/edit
[fieldupdate]: https://docs.google.com/document/d/1gGxdHa0Sg9EIKtIJTnI3u0M8emQXwI6rMuZoH82E-TM/edit
[cosmic]: https://docs.google.com/document/d/1uN6BwHlDLplRNlyTA2f1bFvKV-7Q01_r66AMKZqF484/edit
[clock]: https://docs.google.com/document/d/1kR3HfOMoEvDoasftpfCErSAv_TYh5SSrxCqaKDN4QHM/edit
[temporal]: https://docs.google.com/document/d/1obKlNpy47T8Km074kHQ499KUH3Z1Q47nhRC8GUEE7rA/edit
[service]: https://docs.google.com/document/d/1vVy2Bk01klLgyfVDkOoxdOddlXEc02wIydAofFY59Bc/edit
[serviceupdate]: https://docs.google.com/document/d/1ODDPPfGKTKx8jSy_yp5leVww6w-pSXqfNgLFHmEs17g/edit
[retraction]: https://docs.google.com/document/d/1uhM6kxWGuYBtKPLnSIXEEwUnL21R7aIbnLCCiu8we8k/edit
[thermo]: https://docs.google.com/document/d/1C63lzqzNJZyMOvsXluJ0-kpNY4UIM_3RTOmaMEn5NuE/edit
[industrial]: https://docs.google.com/document/d/1fAAm1cBV9dtLUQRLQOyweoI96G1RmgSRk7nYuhohtUg/edit
[omnibus]: https://docs.google.com/document/d/1Qs0uS2xw0Wm8E09K_BNRVzbnOcjQiZbfRaqOpt0D3ts/edit
[triadic]: https://docs.google.com/document/d/116oVwVqZBV6eGKMCXvhjR606o8_h-t1CNOg9dSLbAQE/edit
[wobble]: https://docs.google.com/document/d/1KaDvN7idukpMwFEEmGPE241kKGtvqXxjyseSP9UC1Q4/edit
[ledger]: https://docs.google.com/document/d/1NllZE54FSGiV1dKNukEd2dnJBfKWelL1OZbpbJ_UJrk/edit
[threewitness]: https://docs.google.com/document/d/1uk2sq4RWRdJbMFzxoCWgJsBZzfIbTRwT4SMPI_DARg0/edit
[abundance]: https://docs.google.com/document/d/17aexmVzsvSG6ilB02eGO1mafvCScnH_VtY7fu1uh7Jg/edit
[room]: https://docs.google.com/document/d/1JePC6a_aeal3opTcp1pMeJQs7HwJ3r5tOhOkeQV2GNg/edit
[fourspace]: https://docs.google.com/document/d/1ubpY39_ikTEqYOM51aaFZG-H3ya2glemVhr0PnLaB0M/edit
[patch]: https://docs.google.com/document/d/1kKXLKXWXUCoOS1dH5Z91EMYjr9rJEYYFiQT_eamz9Cs/edit
[earlyfour]: https://docs.google.com/document/d/1zMRitpSaRPd-yhZasUBABpVVYquF1dU_45GJMFE_C_E/edit
[ttsc]: https://docs.google.com/document/d/1M4B5m4fPfS1W7JBffL7B02hlq-86oKTDwyJZPeaL33Y/edit
[pipelines]: https://docs.google.com/document/d/1j7FhdrAKnXUYX-OBGcKrkEqnP_qk7BkTBfDfAPMeVKE/edit
[oppipelines]: https://docs.google.com/document/d/1bup3-eLaaT54EtnsX8I_0xwbKDHoH8-qJ8FtxI4kgm0/edit
