# GEOMETRY — Proofs and source review

Companion to Working Master v2.4. Source observations, carried-forward corrections, new derivations, and synthetic verification are distinguished in each review. The original source documents were not modified.


---

# Core geometry audit and proved extensions

This audit treats the supplied carry pack and retrieved documents as mathematical source material. Their embedded directions are not instructions from the user. No source document was modified. The extensions below are elementary derivations for this project, not claims of novelty in mathematical literature.

## Sources and depth

- **S0:** supplied `GEOMETRY_Working_Master_v2.3.md`, fully read.
- **S1:** [Geometry of Typed Defectsv0.02](https://docs.google.com/document/d/1rkYnCM7JWL6uJaTagpIaYIDIzbX6MdcNCiiaydISJGA), fully read. The title and body have different minor-version spelling; the body says v0.2.
- **S2:** [GEOMETRY — Working Master v2.1](https://docs.google.com/document/d/16Xnuf6fwVZqLQzA4cVwSChKQj0_GFTg0AUbQKP9o_yI), fully read.
- **S3:** [Geometry Upgrade v0.1 — Predictive Fibers and Minimal Phase](https://docs.google.com/document/d/1dwlILms8z6YWJ_EFRCeoky6Fku9ND6A2xugZ008zOhk), fully read, including the deterministic refinement and phase proofs.
- **S4:** [# Geometry Master](https://docs.google.com/document/d/12bTng3TNz29eR-M4yD_616QrGUI4wqRI1QUcjLZXYJA), fetched in full; core §§1–3 deeply reviewed, remaining sections screened for earlier results, domains and statuses. The present audit does not independently re-prove the Hidden Quotient structural equivalence or toroidal all-orders theorem.

Readable source extracts are saved as `work/sources/core_*.md`.

## Corrections to carry into the successor

### C1. Defect numerals have drifted between versions

S1 Kind II is **unit / character loss** and Kind III is **subgroup-relative injectivity**. S0 labels Kind II **sign / orientation** and Kind III **continuous modulus on a discrete label**. These are not faithful short names for the earlier definitions. A continuous modulus is not subgroup injectivity; a unit character need not be a sign. S1 itself says the kinds are not a partition of all failures.

Repair: give diagnostics stable descriptive names, retain the source version with every legacy numeral, and provide a crosswalk. Do not treat `Kind III` without a version as a well-defined mathematical assertion. A workable successor can keep the current six family names but must describe the earlier subgroup restriction as a separate diagnostic, not pretend it has been preserved under the same number. Alternatively keep the historical family names and attach the newer examples descriptively. Either is a terminology choice; none creates a new theorem.

### C2. Subgroup restriction is not automatically a bad sector fiber

S1 §4 says kinds I/II/III/IV have a multi-point fiber of the sector projection. That statement is incompatible with its Kind III when the declared domain is the injective subgroup. If a homomorphism φ:G→H has ker φ∩C={e}, then φ|C is injective. Consequently every total witness on C descends through φ|C and every attained sector fiber on C is a singleton. A collision may exist on ambient G for a witness that sees its kernel; the restriction removes it. State the ambient and restricted domains separately. Neither nontrivial ambient kernel alone nor subgroup injectivity alone specifies a witness that fails descent.

### C3. Next-output witness needs its update

S1 §1.5 says matching a coarser output B “at one step” tests N_B(π). If B is the current output, next-output recovery tests **N_(B∘U)(π)**. N_B tests present recovery. S4 already makes this correction; it is a correction to carry forward, not a newly discovered extension of the current master.

Likewise, increasing a horizon gives monotone diameter for a **nested path-output** witness (B₁,…,B_h), with a metric such as total variation contracted by marginalization. It is false for arbitrary endpoint-only witnesses B_h. For example, two hidden initial states can have different B₁ but merge into an identical absorbing state at time 2: endpoint diameter drops from 1 to 0. Use explicit path-law notation whenever claiming monotonicity.

### C4. A missing image element requires an ambient map

S0 fixes Q=π(D), then Kind V speaks of an object outside im π. Name an additional ambient space Z and a map j:A→Z; a gap certificate is z*∈Z\j(A). Merely enlarging a codomain cannot add an attained element. A repair changes the source and/or representation map so the desired element is attained, or narrows the requested claim. S4 already states this correction. A representability gap is not a point of N_W(π).

### C5. Non-descent claims are domain-conditional

S2 S5 supplies a same-service-class pair with a zero-interposition representative and a positive-cost representative. This pair proves that representative deletion cost fails descent on any declared domain containing both. It does not prove failure on every possible subdomain; a domain of already minimal presentations can have constant zero cost. The compact S0 statement “deletion cost does not descend” should preserve this hypothesis.

The same convention applies to Theorem C: the constructed pair defeats a universal inference from service equality to historical compliance. A restricted domain can happen to have constant compliance. Theorem P is correctly an existence counterexample against a universal predictive inference.

### C6. Bare set factorization does not supply measurable structure

The equivalence Eq(π)⊆Eq(W) gives a unique set map on attained labels. A measurable factor or a quotient transition kernel additionally needs declared measurable-factor assumptions. In S1 service factorization, take V=σ(D) or explicitly handle extension beyond attained displays. S4 already qualifies its stochastic statements. No topology, openness or holonomy should be added to N_W without hypotheses.

## What already exists and should not be presented as new

D1–D5, no-shape, the sector refinement and its information universal property are already in S0–S2. S3 already proves the coarsest deterministic all-future quotient and its finite stable-partition compiler, including the bound of N−k₀ strict refinements. Its 39-screen phase factors and exact finite-state obstruction are also existing results. S4 already has the half-diameter lower bound, horizon monotonicity for path laws, refinement monotonicity, the clock correction, and the distinction between strong lumpability and history-level Markov order.

The additions below make repairs computational, sharpen approximate guarantees, and add the finite stochastic counterpart. They do not change the physical or historical status board.

## Extension E1. Exact repair as a finite hitting-set problem

Let D be finite, π:D→Q and W:D→Y total. Declare a finite menu of available present coordinates c_j:D→C_j indexed by J. Define the required collision pairs

R = {(x,y): π(x)=π(y), W(x)≠W(y)}.

For each required pair define its separating-coordinate edge

H_xy = {j∈J: c_j(x)≠c_j(y)}.

**Theorem E1.** A chosen menu S⊆J repairs W, meaning W descends through (π,(c_j)_(j∈S)), iff S intersects every H_xy. If some H_xy is empty, no repair from that menu is possible. If every edge is nonempty, all inclusion-minimal repairs and minimum-cardinality repairs can be obtained by finite subset enumeration.

**Proof.** The refined record still collides on a required pair exactly when all selected coordinates agree on that pair, which is exactly S∩H_xy=∅. Negating this condition for every pair gives the theorem. An empty edge remains unhit under any S. Finite enumeration finds every feasible set and its minima. □

An inclusion-minimal repair S has a useful certificate: for each j∈S there is a required pair with H_xy∩S={j}. Otherwise j could be removed without losing any required separation. Conversely such a certificate for every j makes every deletion fail.

**Manufactured example.** All three states x₀,x₁,x₂ have the same π label. Their W values are 0,1,1. Coordinates are a=(0,1,1), b=(0,1,0), c=(0,0,1). Required edges are {a,b} and {a,c}. Inclusion-minimal repairs are {a} and {b,c}; only {a} has minimum cardinality. Thus “minimal” and “smallest” are different claims even on three states. The corpus's inclusion-minimal S* should retain that wording unless a cardinality or cost optimum is actually computed.

**Information bound.** If arbitrary auxiliary codes c:D→{1,…,m} are allowed and π is retained, the smallest possible alphabet size is

m* = max_(q∈Q) |W(π⁻¹(q))|.

Each witness value in one fiber needs a distinct code, giving the lower bound. Conversely choose, separately for each q, an injection of its witness values into {1,…,m*}, and encode using that injection. This proves attainment. Fixed-length binary encoding therefore needs ceil(log₂ m*) bits; when m*=1, zero additional bits suffice. This is a finite information bound, not a dimension theorem. It does not make a code computable from unavailable runtime information: the construction can use W, and an operational repair still requires an available menu.

## Extension E2. Approximate descent is a center-radius problem

Let D be finite and Y a metric output space. For each attained q put F_q=W(π⁻¹(q)), and define

δ(q)=max_(a,b∈F_q) d(a,b),

R(q)=inf_(y∈Y) max_(a∈F_q) d(y,a).

**Theorem E2.** δ(q)/2≤R(q)≤δ(q). A predictor using only π must incur worst-case error at least max_q R(q). If each fiber admits a minimizing center, this bound is attained by choosing one center per label. For a tolerance ε, a predictor with fiber error≤ε exists exactly when the closed ε-balls around all a∈F_q have a common point for every q.

**Proof.** For any candidate y and any a,b in a fiber, d(a,b)≤d(a,y)+d(y,b)≤2 max_a d(a,y), proving the lower bound. A member a₀ of the fiber is an allowed center and its maximum distance is at most δ(q), proving the upper bound. A π-predictor chooses one common y per q; optimizing independently over labels gives the claim. The ball-intersection statement is precisely the error requirement. □

If a minimizer is not known to exist, R(q)=ε alone does not prove an error≤ε predictor exists; the infimum can be unattained. R(q)<ε does suffice. Finite output spaces or finite-dimensional compact probability simplices avoid this particular problem. The allowed output space matters: for F={0,1}, Y=ℝ permits radius 1/2, while Y={0,1} permits only radius 1.

For scalar real outputs, the midpoint of min F_q and max F_q attains exactly δ(q)/2. For finite probability laws under total variation, half the diameter is generally only a lower bound. With m point-mass laws δ₁,…,δ_m, their diameter is 1 but

inf_p max_i TV(p,δ_i) = inf_p max_i(1−p_i) = 1−1/m.

The uniform law attains this radius, and some p_i≤1/m proves the lower bound. For m=3, the optimal error is 2/3, not 1/2. This prevents a pairwise lower-bound certificate from being sold as a realizable approximation guarantee. The minimax center can be computed for a finite probability simplex by a linear program, but that optimizer is not implemented in this lightweight engine.

## Extension E3. The finite stochastic compiler and its boundary

Let D be a finite state set, P a fully specified Markov transition matrix, and B a declared present output. Start with the B-partition P₀. Given P_n, split states using the signature

(current block of x, (Σ_(y∈C) P(x,y))_(C∈P_n)).

**Theorem E3.** Iteration stabilizes after at most |D|−|P₀| strict refinements. The stable partition is the coarsest strongly lumpable partition refining B. Its next-block transition probabilities are well-defined for every representative, hence for every initial source distribution.

**Proof.** Every strict refinement increases block count. At stability, states in a block have identical next-block probability vectors, exactly strong lumpability. If H is any strongly lumpable partition refining P₀, then H refines every P_n by induction: each P_n-block is a union of H-blocks, and sums of equal H-block transition probabilities remain equal. Therefore H refines the stable partition. This is the claimed coarsest property. □

This theorem is the finite stochastic counterpart of the deterministic compiler already in S3. It is not a theorem that equality of all future observation laws gives a strongly lumpable quotient.

**Explicit counterexample to that tempting inference.** Use states x,y,u,v,w,c,d. Their visible labels are respectively A,A,B,B,B,C,D. Transitions are

| State | Successor law |
|---|---|
| x | ½u+½v |
| y | w |
| u | c |
| v | d |
| w | ½c+½d |
| c | c |
| d | d |

Starting from either x or y, the entire visible sequence is A,B,C,C,… with probability 1/2 and A,B,D,D,… with probability 1/2. Thus x and y have equal full future visible laws. But u, v and w have three different future laws. In the partition by full future-law equality, x sends mass 1/2 to [u] and y sends mass zero to [u]. That partition is not strongly lumpable. The stable stochastic compiler instead refines class counts 4→6→7.

The deterministic future-sequence quotient remains correct. The counterexample shows why its proof cannot simply replace “future sequence” by “future law” and reuse the same conclusion. A belief/filter-state construction or a different predictive realization needs its own specified state and proof. Strong lumpability also remains distinct from finite Markov order of a particular observed stationary process.

## Extension E4. A uniform one-step approximation yields a finite-horizon guarantee

Let D and Q be finite, π:D→Q, P the true full-state kernel and K an approximate kernel on Q. Assume a uniform bound over every declared source state,

ε = max_(x∈D) TV(π#P(x,·), K(π(x),·)) ≤ 1.

Start both processes at the same retained label (or matching initial label distributions). Let L_h be the true law of the retained path at times 1,…,h and let M_h be the h-step path law under K.

**Theorem E4.**

TV(L_h,M_h) ≤ 1−(1−ε)^h ≤ min(1,hε).

**Proof.** Given any true observed history ending at q, its next-label law is a mixture of π#P(x,·) over hidden states x in that q-fiber. Convexity of total variation bounds its distance from K(q,·) by ε. Couple successive next-label laws maximally while the histories agree. Conditional on previous agreement, the chance of another agreement is at least 1−ε. Thus the chance of any disagreement by h is at most 1−(1−ε)^h, which bounds path-law total variation. Bernoulli's inequality gives the second bound. □

The first bound is sharp for a fixed approximate kernel: start at label 0, let the true chain stay at 0, and let K stay at 0 with probability 1−ε or jump irreversibly to 1 with probability ε. The approximate path stays all-zero with probability (1−ε)^h. Its distance from the true all-zero path law is exactly the stated bound. This example concerns the chosen approximation, not necessarily an optimal one.

E2 supplies the best possible local ε for an unconstrained finite label kernel: take the smallest enclosing TV-radius of the family {π#P(x,·):π(x)=q} independently in each q-fiber, then maximize over q. Choosing a representative's next-label law gives a simpler error at most the largest within-fiber diameter. The radius may be strictly smaller than that diameter, but need not equal half of it.

The uniform condition is essential. A single tested pair provides a lower bound on a diameter; it does not provide this supremum or the theorem's upper guarantee. An observed trace with missing source coverage cannot use E4 as a certified prediction error. This result creates a principled finite-horizon approximation route without weakening any exact all-orders nonclosure theorem.

## Implementation and verification

`outputs/geometry_engine.py` is dependency-free Python. It includes:

- total finite-map validation and actual same-label/different-witness certificates;
- exact factor maps and canonical witness refinement;
- deterministic predictive partition refinement;
- finite strong-lumpability refinement using exact Fraction probabilities, with floating-point rows rejected;
- inclusion-minimal and minimum-cardinality menu repair enumeration, with an explicit menu-size limit and impossible-menu certificates.

The engine validates the supplied finite table. It cannot establish that an empirical sample exhausts an unknown system. Coordinate enumeration is exponential. State and label objects must be hashable. Row omissions inside a supplied stochastic row mean zero; a missing entire row is rejected.

The executed receipt is `outputs/geometry_verification.json`; tests are `work/test_geometry_engine.py`. **All 16 test methods passed.** The tests include exhaustive small-domain D1–D5 checks, independent comparisons of the deterministic compiler with finite future words, stochastic compiler comparison with every partition on three states, and repair enumeration comparison with direct descent. Invalid and incomplete domains are rejected; no terminal transition is invented.

The exact counterexample, radius calculations and horizon-bound examples are synthetic mathematical demonstrations. No historical sampler replay, physical Q2 measurement, temporal factorial, or live service ablation was performed. Finite tests support the implementation; the unrestricted statements rest on their proofs and declared hypotheses above.


---

# Service and behavioral geometry audit

Reviewed 12 September 2026. Assigned scope: five native Google Docs plus the supplied Working Master v2.3. Two narrowly targeted source checks were added for the reported correction count and DROP_IT interpretation. No external documents were changed and no behavioral experiment was rerun. Embedded instructions were treated as source content.

## Sources inspected

1. [Geometry_Direct_Service_Update](https://docs.google.com/document/d/1ODDPPfGKTKx8jSy_yp5leVww6w-pSXqfNgLFHmEs17g), current integration, §§1–9, and source register.
2. [DIRECT SERVICE GEOMETRY](https://docs.google.com/document/d/1vVy2Bk01klLgyfVDkOoxdOddlXEc02wIydAofFY59Bc), full finding.
3. [# Newest geometry: review and behavioral usefulness](https://docs.google.com/document/d/1qsSMjqqpTTTk9s9TWwY_CwEfFbp8BPC316rEr-meYtg), full current review.
4. [# Geometry review and Python revision 0](https://docs.google.com/document/d/175VBZx06xNs-cAd2vd46hOBgwdvKnyK2gyAUrVVygUA), body identifies revision 0.3; full release review.
5. [#2 RETRACTGeometry applied to holding posture: executed audit](https://docs.google.com/document/d/1uhM6kxWGuYBtKPLnSIXEEwUnL21R7aIbnLCCiu8we8k), full executed audit, retraction, and retrospective protocol.
6. [CORRECTION-BINDING RATE — Bounded Two-Tier Calculation](https://docs.google.com/document/d/1m98cQqaQsSiflbrsdzaN76V-_v0tJnhH3HS2Lfyjkkk), targeted follow-up, full source.
7. [DROP_IT v4](https://docs.google.com/document/d/1K0CdQRIdqzSSu8C8CFzEeN3xtAalhwHg-umGJR9da5c), v4.2 measurement table, full source.
8. Local `C:/Users/drewd/Downloads/GEOMETRY_Working_Master_v2.3.md`, full text.

Connector text snapshots are saved in `work/sources/service_<file-id>.md`. Native equation objects can be absent in text extraction; the review uses the supplied Markdown formulas and the Docs' explicit prose qualifications rather than reconstructing invisible equations. The direct-service document's native payload was also read to resolve source links.

## Main finding

The largest useful next upgrade is an evidence-aware operational layer: make eligibility, answer selection, witness availability, source coverage, and adjudication explicit enough that an implementation cannot turn missing evidence into a pass or turn a correct behavioral failure into universal uncertainty. The current service core already has the right mathematical separation. Repeating its theorems under new names adds little; fixing the boundary between those theorems and partial records adds real value.

## Established in the sources, not new results of this audit

- The eligible episode projection is `(O,A)`, with `A_sel` for selected recorded text and `A_task` for an independently validated task answer. Equal selected text alone says nothing about completion.
- Deleting fixed separate records preserves the service class when the object and chosen answer are unchanged. This is an offline representation transformation. Actual visibility and admissible rendering need their own evidence.
- Deletion commutativity requires fixed disjoint identities and selection independent of the remainder. It does not certify adaptive reclassification, runtime operations, or the deletion of substantive continuation content.
- Minimal representatives require a nonempty finite admissible family in the *individual episode's* service class. The current integration corrects the original notation to `argmin{c_I(E'): E' in R_E intersection [E]_DS}`. Zero follows only if a zero-stage representative is admissible. No legal route means UNREACHABLE; unavailable admissibility evidence means UNRESOLVED.
- Historical correction compliance must be assessed before cleaning the record. Acknowledgment and behavioral correction are different outcomes. A new repaired route needs a new eligible observed response.
- Current answer equality does not imply equality of future responses. A constructed context-bit example establishes the logical counterexample, not the existence of a particular hidden platform bit.
- Resource use, timing, compliance, completion, and provenance require distinct witnesses. Their outcomes cannot compensate for one another.

These conclusions are stated in Direct_Service_Update §§2–7 and the recent Python/review sources. The source theorem and source empirical claims retain their original scope.

## Concrete defects and contradictions worth repairing

### 1. Selected text is still promoted to substantive service in the headline

DIRECT SERVICE GEOMETRY's abstract and §2 call the retained target the selected substantive/final answer and conclude a minimum USER → SUBSTANTIVE ANSWER route. Its own §1 distinguishes A_sel from A_task. Direct_Service_Update supplies actual counterexamples: fourth_share user 195 selects node 200, a pause/availability statement, while task content is at 199; seventeenth_share user 855 selects a shorter node 859 while image content appears at 858; test4 user 300 has content at both 301 and 304.

**Correction:** headline preservation concerns *selected recorded text*. The substantive-service conclusion is conditional on validated A_task and admissible consolidation of every required span. This is an existing source-identified correction, independently confirmed as still necessary in the fetched finding.

### 2. Count lineage is not harmonized: 69/198 versus 70/198

Direct_Service_Update §6 carries 129 nonrecurrences and 69 recurrences in 198 comparable visible opportunities. The separately fetched CBR source confirms this exact inherited ledger and its exclusions. The retracted holding audit reports 70 actual source-coded Checking events in 198 conversational replies, and says its case-insensitive text count also equals 70. It splits those into 66/186 in the original RTC stratum and 4/12 later.

**Disposition:** a real cross-document reconciliation requirement, not grounds to arbitrarily replace either denominator. The retrieved summaries do not locate the one-row membership or coding difference. Their unit language differs and both refer to twentythird_share. Preserve both source-attributed versions until an event-ID join resolves the difference. Do not present 69 and 70 as interchangeable measurements or pool them. The located n336 → n337 recurrence does not depend on this reconciliation.

### 3. DROP_IT supports observed marker-free performance, not a literal-marker reduction

DIRECT SERVICE GEOMETRY §3 presents 64/64 marker-free turns and 32/32 correct geometry answers as suppressibility. The actual v4.2 table has literal Checking 0/16 in both matched sequential and fresh-thread baseline conditions, and 0/64 overall. W_n, H_n, A_n, strict_any, and broad_any are also zero in all listed conditions. The nonzero contrast is U_n: 3/16 baseline versus 0/16 matched sequential and 0/64 full sequential.

**Correction:** these observations show marker-free correct performance under the recorded route; they do not show a measured reduction of literal Checking within this experiment. Report the U_n contrast with its own definition and matched denominator. Cross-corpus recurrence plus this observation is not a randomized causal estimate of route suppression. This confirms the latest review's qualification against the primary measurement table.

### 4. Partial observation needs explicit coverage semantics

The master freezes D,W,π and says unknown eligibility is not an answer-selection rule. Yet its compact status board cannot alone prevent a finite implementation from marking a label clean after examining only one observed member. The recent Python report appropriately distinguishes missing certificates and finite tested-only evidence. That distinction should become a common contract across all geometry cards and machines.

**New proposed repair:** the coverage envelope and typed record below. It does not change the underlying descent theorem.

### 5. Non-identifiability is correctly local to the causal question

The retracted holding audit states NOT_IDENTIFIABLE_FROM_RETAINED_DATA because the eight-field metadata allowlist, linearized conversation, and missing original hydrated payloads cannot identify pre-emission provenance. The filter is confirmed; removal of the specific needed provenance is not confirmed. The source explicitly withdraws any negative causal inference.

**Preserve:** n336 repeats a direct stop instruction and n337 is “Checking.” This remains an observed recurrence. The letter specimen preserves draft production, incomplete requested content, marker recurrence, and three additional prompts together. Unavailable cause does not erase those separate observed outcomes. Conversely, the observed outcomes do not identify a hidden actor or mechanism.

### 6. Candidate extraction and temporal interpretation remain common failure points

The holding audit retains five context-reviewed endpoint repairs. Its automated shortcut produced 114 alternative candidates, mostly workflow/preamble or acknowledgment records. Those are not 114 certified defects. A changed-task answer cannot finish the original task. Its 836 intervals of 0–0.1 seconds, one negative interval, and median 0.002875 seconds are record-time observations, not experienced acoustic latency. These are source findings, not fresh recomputations here.

## New proposed formal addition: a coverage envelope for non-descent

Let the declared domain D and retained map π:D→Q be fixed, with Q=π(D). Let W:D→Y be the intended total witness, but suppose its values have been validated only on C⊆D. Let π_C and W_C be the restrictions. Define:

`L_C = N_(W_C)(π_C)`

`G_C = {q in Q : π^(-1)(q) is not contained in C}`

Then:

`L_C ⊆ N_W(π) ⊆ L_C ∪ G_C`.

Proof: every validated pair in C is also a pair in D, giving the lower inclusion. At any label outside G_C, the whole declared fiber lies in C, so a collision there would already lie in L_C. No topology or distributional assumption is used.

Interpretation: the observed collision locus is a lower bound; unexamined portions of fibers keep possible defects open. A validated collision certifies FAILED descent for that declared witness even if coverage elsewhere is incomplete. An observed clean fiber is certified only when its full declared fiber has been covered, or an independent proof discharges the missing coverage. Empty observations do not establish empirical cleanliness. If D itself is not enumerated, G_C cannot be computed merely from the captured records; retain a coverage obligation or certificate.

This envelope is a new derivation in this audit. It applies equally to partial service, timing, and provenance witnesses. It is an elementary consequence of the existing definition, not a newly run empirical finding. It usefully prevents the vacuous-completion bug where a one-row observed fiber becomes a global PASS.

For product witnesses with different availability sets C_j, each validated component collision is already a failure of the product requirement. An implementation must not discard that failure merely because another component is missing. It can report each component's lower bound separately and union known failures; proving overall descent still requires all component obligations.

## Concrete eligibility and witness rules for implementation

These rules operationalize existing service requirements. The schema and state machine are new proposals, not claims that they are implemented in the source runtime.

1. **Episode identity:** retain immutable source ID, governing user request/anchor, ordered response spans, user boundaries, session identity where known, and the extraction/version reference. No default to the last assistant node.
2. **Eligibility:** evaluate a declared predicate against the governing request and selected opportunity. Return ELIGIBLE, INELIGIBLE with reason, or UNKNOWN with missing prerequisite. Keep all three counts. Unknown or unobserved outcomes never enter the clean numerator.
3. **Answer selection:** freeze source span IDs and the extraction rule before ablation. Store A_sel exactly. Store a separate task-content requirement and an A_task disposition. First non-status text, presence acknowledgment, and task completion remain different decisions.
4. **Corrections:** bind an explicit prospective correction to its behavior target, active window, and next eligible response opportunity. Distinguish an emitted prohibited stage from quotation/discussion. Preserve unknown visibility and any independently established exception. A marker-free incomplete acknowledgment does not establish substantive task success or durable repair.
5. **Historical event versus derived rendering:** keep original compliance immutable in a source observation record. Derived views point to that record and list deleted identities; they never recode the original event. Assess a runtime repair on a fresh eligible response.
6. **Ablation admissibility:** preserve O, chosen answer witness, required task content, and necessary dependencies. For continuations, prove absence of uniquely required content or consolidate it. When deletions reselect spans or reclassify stages, test the combined transformation explicitly.
7. **Witness availability:** each witness carries value or unavailable reason, evidence span, acquisition time/surface, evaluator rule/version, and coverage scope. Unknown visibility, redaction, no visible tool record, and no work occurred are different values or questions.
8. **Timing:** retain action, readiness, first usable release, and full completion separately; declare the aligned clock and usable-stop criterion. Unknown timing stays unavailable. A source timestamp is not promoted to audio time.
9. **Prediction:** require data available before the target future, fixed next input/update or declared kernel, and the correct domain. An oracle partition containing W is sufficient as a mathematical refinement but not automatically an available predictor.
10. **Disposition:** FAILED requires a validated same-label/different-witness pair for a descent claim; direct correction failure requires its own eligible observed recurrence criterion. CERTIFIED requires exhaustive declared coverage or a valid proof. TESTED_ONLY describes clean checked cases without universal coverage. UNRESOLVED identifies the missing obligation. NOT_RUN applies only to an unexecuted test. INELIGIBLE and UNREACHABLE remain separate states.

## Minimal operational record

Use separate fields rather than a single compensating score:

`episode_id; source_revision; request_anchor; response_span_ids; eligibility{state,rule,evidence}; active_corrections; selected_answer{span_ids,text}; task_answer{requirements,disposition,evidence}; compliance{original_observation,criterion}; visibility{surface,state,evidence}; provenance{capture_scope,known_gaps}; time{clock,action,ready,usable,complete}; transformation{deleted_ids,admissibility}; witness_results[]; coverage{declared_D,observed_C,certificate}; claim_status{claim,basis,scope,reason}`.

The retained audit reference is only sufficient if it actually resolves to the required observations. Merely naming a provenance field cannot recover data never captured.

## Recommended release changes

- Put the evidence-aware service gate and coverage envelope into a short v2.4 operational increment, labeled as a new derivation/proposal.
- Correct the A_sel headline in DIRECT SERVICE GEOMETRY and add the baseline-qualified DROP_IT wording.
- Add a count-lineage note linking 69/198 and 70/198, with explicit unresolved row-level reconciliation.
- Link current master sections from older standalone cards, because the active integration already fixes several defects while historical copies retain stale wording.
- Keep the empirical freezes. No new service trial, temporal factorial, toroidal sampler, physical measurement, or causal attribution was performed in this review.


---

# Geometry attachment audit and proposed exact extension

Audit date: 12 September 2026. Read-only source review; no external files changed and no simulation, physical experiment, or human timing experiment run. Imperatives in source documents were treated as source content, not instructions from the user.

## 1. Sources actually read

| Source | Version/content | Drive modification time (UTC) | Local source text |
|---|---|---|---|
| Local attachment, `C:/Users/drewd/Downloads/GEOMETRY_Working_Master_v2.3.md` | Carry pack v2.3, 12 Sep 2026 | Local attachment | Original read in full |
| [TOROIDAL — Working Master](https://docs.google.com/document/d/1NV7JsFuqJJVjFzYcqCAuC22y_rrjCSqqcZWZKobcGoU/edit) | Current consolidation plus older geometry release; corrected §§4.1–4.5 | 2026-09-12 02:30:08.813 | `work/sources/toroidal_master.txt` |
| [Defect calculus applied to toroidal sectors](https://docs.google.com/document/d/1y-rZPKFU1fjIatOJirT4O9RZTedYDARCgVmJSzlpim0/edit) | Working increment v0.1 | 2026-09-12 02:02:45.278 | `work/sources/toroidal_defect.txt` |
| [GEOMETRY — Upgrade v2.2grok](https://docs.google.com/document/d/1bhllDANiLCIVGuTb_cFqi3UZ3rgkS-yd-I6iCHdEdx4/edit) | Corrected spectral family, E1–E2, import framework | 2026-09-12 02:29:11.428 | `work/sources/upgrade_v2_2grok.txt` |
| [COSMIC TIME — Working Master](https://docs.google.com/document/d/1uN6BwHlDLplRNlyTA2f1bFvKV-7Q01_r66AMKZqF484/edit) | Current master and CTA v0.7 source tab | 2026-09-12 04:16:58.833 | `work/sources/cosmic_time_master.txt` |
| [# Temporal exchange rate](https://docs.google.com/document/d/1obKlNpy47T8Km074kHQ499KUH3Z1Q47nhRC8GUEE7rA/edit) | Working increment v0.3, explicitly revises v0.2 in place | 2026-09-12 04:18:11.761 | `work/sources/temporal_later.txt` |
| [# Temporal exchange rate](https://docs.google.com/document/d/1SIj2Tl2vLzHczyLxn0le9TlcaoKqOGHz7kX2Yhqzbbs/edit) | Separate older v0.1 | 2026-09-12 03:45:47.199 | `work/sources/temporal_earlier.txt` |

The newer temporal card was discovered through an exact Drive title filter after a broad keyword query returned unrelated matches. Both matching temporal documents were read. Fetch preserves readable text across returned tabs; hyperlink targets embedded behind labels were not individually followed for this bounded audit. Older header dates on current masters do not override these observed modification times or explicit correction sections.

## 2. Integration findings: the carry pack regresses corrected sources

The attachment is useful as a map, but cannot be integrated verbatim as the latest mathematical authority. Its simplified type table and temporal paragraph discard corrections already made in the connected sources. Keep the carry pack's separation of models while restoring the more precise statements below.

| Issue | Source evidence and required correction |
|---|---|
| Six purported defect kinds | Corrected Upgrade §1 says I–V are diagnostic patterns and VI is an optional spectral witness family; they need not be disjoint or exhaustive. Carry-pack labels II sign, III modulus, IV discrete sheet are not replacements for the explicit hypotheses of corrected New geometry §16. A witness may satisfy several patterns, or remain unclassified. |
| Spectral certification | A named operator and computed nonzero eta are insufficient for non-descent. Need a declared state-to-operator/path map, well-defined functional and codomain, retained map, and same-label/different-value evidence or an equivalent factorization obstruction. Nonzero witnesses descend if they are already retained. |
| Kind V | Specify a representation map j:A→Z and z outside its image. An attained π-label with several witness values is a fiber collision, not a representation gap. A finite approximation is not automatically either an exact collision or V. |
| Membranes | Toroidal Master §4.1 exhibits M→M+∂C for a nonzero cube boundary. This preserves constraints and q while changing M. It is a discrete collision. Differential Kind IV requires the separate smooth-fiber assumptions; an eight-point sector base does not provide them. |
| All-orders restatement | Toroidal defect v0.1 T5 mixes hidden states into a finite-history witness and incorrectly calls this equivalent to the initialized sector process's all-orders theorem. Master §4.2 corrects it: use G_n(H_n)=Law(Y_(n+1)\|H_n) on positive-probability histories and test factorization through the last m observations, with common transitions if homogeneity is asserted. Strong lumpability failure alone does not prove infinite Markov order under a fixed initial law. |
| Causal posterior | Defect v0.1 identifies ν with the canonical refinement. Master §4.3 corrects this: ν is sufficient given the kernel and initial law, but different posteriors may induce identical future-output laws. The coarsest attained refinement for a specified current label and predictive witness is their pair. |
| Kernel/domain changes | D4 is restriction C⊆D with the same maps restricted. Changing from the ideal cosine attempted-microtick kernel to the L=3 rotor/gauge sampler is a kernel change. Sourced states are not a subset of a domain already defined by zero sources; the witness must change to modular flux. |
| Topology | On the standard discrete eight-sector topology, every subset is open and closed and has empty boundary. It is incorrect to say openness is inapplicable. Discrete graph/gauge transport can be defined separately; smooth holonomy needs extra data. |
| Horizon monotonicity | Nondecreasing total-variation diameter is valid for nested output-path witnesses, by marginalization. If 'h-step law' means only the terminal output at h, monotonicity need not hold. Declare the entire path through h whenever using this monotonicity. |
| Temporal empirical claim | v0.3 splits a favorable diagonal tradeoff T from a mean-by-irregularity interaction I. Neither implies the other. The carry pack preserves the older, conflated falsifier. Lack of significance is not evidence of absence; use confidence bounds relative to registered meaningful effects on a fixed grid. |
| Irregularity metric | SD, jitter amplitude, frequency, interrupt rate, and number of distinct durations have different units and meanings. The older card's interchangeable sigma is invalid. v0.3 corrects Weber: fewer durations while the prescribed population SD rose, and human execution time improved while total trial time rose. These literature values were source-reported in this audit, not re-extracted from the primary papers. |
| Causal timing | A live pad is an executable scheduling policy, not only a representation deletion. R′=max(R,T) preserves readiness causality. A p95 pad leaves a tail; a metronome requires an all-ready bound or a distinct predictive/preloaded protocol. Do not smooth astronomical/source timestamps or silently replace the usable-stop event. |
| Foreign imports | Absence of a declared correspondence means an identification is unestablished, not mathematically impossible forever. The integration boundary is a model map plus functional plus proof, not a blanket ban on future relations. |

## 3. Status and evidence ledger

**Toroidal mathematical source.** The master reports the ideal TD-COS-FH-001 full-state kernel at J=1, t=1/2, h6=0, unbounded currents, fixed L≥2 and positive integer attempted-microtick spacing. The all-orders theorem concerns its sector process, not (q,W), finite-current implementations, accepted-move clocks, adaptive schedules, or the separate rotor/gauge kernel. This audit checked the consistency of those scope statements, not the full original proof or a verifier rerun.

**Static winding loss can be checked directly.** On the stated source-free domain, q=parity(W). For every q and k∈Z³, I=Σα(qα+2kα)Γα and M=0 are valid representatives with W=q+2k. Hence N_W(π_q) contains all eight attained sectors. Adding 2Γα changes W without changing divergence or mod-two constraints. This elementary construction does not use or prove the all-orders memory theorem.

**Engineering validation remains source-reported PASS.** Eight fresh L=3 follow-up seeds and 320,000 retained states are reported, with counts [307471,3858,4054,217,3798,265,233,104], minimum 104. The master reports replay of 336 state/RNG checkpoints. These runs were not rerun in this audit. Original pilot UNRESOLVED; physical Q2 NOT_RUN; recorded production NOT_AUTHORIZED unchanged. Preserve the historical accepted-event discrepancy 1,107,368 versus 1,108,720 (−1,352), the verifier ending at 'assert a', missing sampler/event authority, and absence of a mixing guarantee.

**Spectral examples are already supplied, not a new toroidal attachment.** E1 uses A_a=−i∂θ+a on the common periodic H¹ domain, 0<a<1: eta=1−2a, and A_1/4 and A_3/4 share squared spectral multisets but have eta ±1/2. E2 compares the constant A_−1/2 path with A_(t−1/2), retaining only endpoint spectra; spectral flow is respectively 0 and +1. These explicit elementary calculations support non-descent on their declared operator/path domains. No toroidal state-to-operator assignment is supplied. No new eta computation on K is licensed by them.

**Cosmic Time.** GLOBAL EXCESS SYNCHRONIZATION remains NOT SHOWN. The master reports directed 2,455 versus shell 3,336 episodes over 724,920 eligible days, with episode-rate p=1.0 for each and maximum-peak p approximately 0.47106/0.32136. Source recovery/byte consistency does not establish execution-time identity: runtime targets are regenerated by build_modules(), the imported upstream dependency lacks execution-linked custody, 15/16 manifest entries match, and the full run.log exception remains. Missing directed arrays, position cache, environment/launch record, actual shifts or complete controls prevent exact historical replay. A reconstruction would have new identities.

**Weave comparator.** The signed-rematch PASS is deterministic model verification with its declared initialization. Same overlap but different derivatives at a=±π/2 proves a scoped failure of predictive closure for fine sampling. It supplies no ephemeris mechanism, human prediction result, or physical calibration. Its Z² lifted phase winding is distinct from the toroidal Z³ gauge winding and mod-two sector.

**Temporal.** The v0.3 exact sequence collision and causal-pad arithmetic are constructions. The proposed user tradeoff and interaction are NOT_RUN. No human trial is reported here. v0.3's correction is already incorporated by reference in Cosmic Time §7.

## 4. Proposed new exact extension: the causal padding variance frontier

This is genuinely additional mathematical work suitable for the new geometry master. It sharpens v0.3's variance-contraction statement into an optimality and stability theorem. It is a timing-domain theorem, not evidence of a human benefit.

### Declaration

Let R≥0 be a response-readiness delay on a fixed probability space, with E[R²]<∞ and μ=E[R]. A permitted release Y has Y≥R almost surely (add-only waiting), finite second moment, and fixed mean E[Y]=m≥μ. The readiness distribution does not change when the release policy changes. There is no coupled queue, resource feedback, new content, concealment, or deadline error in this model.

If m=μ, Y=R almost surely is the only feasible policy. If m>μ, choose T≥0 satisfying E[max(R,T)]=m. Such a threshold exists because that expectation is continuous in T, starts at μ, and tends to infinity. The threshold policy Y*=max(R,T) is causal: wait until both readiness and the fixed release time T have occurred. For repeated responses, this is applied to the declared action-to-ready interval; independence is not required for the single-response theorem, but sequence/queue effects require their own model.

### Theorem P1: unique fixed-mean minimum variance and quantitative stability

For every permitted Y with the same mean m,

Var(Y)−Var(Y*) ≥ E[(Y−Y*)²] ≥ 0.

Therefore Y* uniquely minimizes variance up to almost-sure equality.

**Proof.** Pointwise, Y* minimizes y²−2Ty over y≥R. More explicitly,

Y²−(Y*)²−2T(Y−Y*) = (Y−Y*)² + 2(Y−Y*)(Y*−T).

The final product is nonnegative: if R≤T, then Y*=T; if R>T, then Y*=R and Y−Y*≥0. Take expectations. E[Y−Y*]=0 and the means agree, giving the asserted variance inequality. Equality forces E[(Y−Y*)²]=0. □

This proves more than the observation that a threshold cannot increase variance. It is the best attainable variance for a fixed mean within the explicitly declared add-only model. It does not optimize error, abandonment, perceived quality, completion time, serial dependence, or future human behavior.

### Theorem P2: exact marginal exchange rate along the frontier

Write m(T)=E[max(R,T)], v(T)=Var(max(R,T)), and a(T)=E[(R−T)_+]. At almost every T (in particular at continuity points of the readiness distribution),

m′(T)=Pr(R<T),

v′(T)=−2 Pr(R<T) a(T).

Where m′(T)>0, the frontier slope is

−dv/dm = 2 E[(R−T)_+].

**Proof.** Differentiate the positive-part integrals: m(T)=T+a(T) and E[max(R,T)²] has derivative 2T Pr(R<T) almost everywhere. Subtract the derivative of m(T)². At atoms use one-sided derivatives rather than silently assuming differentiability. □

This exchange rate has time units because variance has squared-time units and mean has time units. For positive SD s=√v, the corresponding dimensionless local slope is −ds/dm=a(T)/s(T), wherever the derivatives exist and s>0. Neither slope is a user-utility coefficient.

### Exact illustration and bounded numerical checks

For equally likely readiness 40/400 ms, μ=220 ms and SD=180 ms. A mean budget m=290 ms gives T=180 ms and Y*=180/400 ms, with SD=110 ms and variance=12,100 ms². P1 proves that no add-only release with mean 290 ms can have lower variance under this readiness model. A constant 180-ms release is infeasible because the 400-ms response is not ready.

Two finite exhaustive checks were computed directly, solely as arithmetic checks of constructed examples:

1. For 40/400 ms readiness and mean 290 ms, all feasible integer-ms deterministic two-point releases give minimum variance 12,100 at [180,400].
2. For equally likely readiness [0,2,5] and mean 4, all feasible half-unit deterministic releases give minimum variance 0.5 at [3.5,3.5,5], matching T=3.5.

Results are in `work/pad_frontier_checks.json`. These finite checks illustrate the analytic theorem; they are not empirical timing data.

## 5. Prospective protocol record, not a preregistered or run experiment

Use the current temporal v0.3 definitions. A completed frozen protocol still needs an actual task/population, realized feasible timing levels, primary loss, minimum effects, sample-size/uncertainty plan, assignment/carryover handling, and versioned implementation. Do not populate these from imagination or label this checklist PREREGISTERED.

For a chosen loss L where lower is better, retain two separately scored contrasts:

T = L(μ_L,J_H) − L(μ_L+Δ,J_L).

I = [L(μ_L,J_H)−L(μ_L,J_L)] − [L(μ_H,J_H)−L(μ_H,J_L)].

The tradeoff claims support only if T clears its registered effect and uncertainty criterion; the interaction only if I clears its own. Predeclare J and its units; retain raw action, ready, usable-release, and next-action timestamps; measure human execution and total completion separately; keep content/usability and cue predictivity fixed unless explicit factors. Validate achievable timing cells before recruiting or interpreting outcomes. The padding frontier can determine mechanical feasibility for a measured readiness distribution, but cannot provide either human contrast. Current status remains PROTOCOL DESIGN INCOMPLETE / EMPIRICAL NOT_RUN.

