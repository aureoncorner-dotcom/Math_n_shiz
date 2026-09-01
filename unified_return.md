Unified Return-Residual Companion
Typed state dynamics, residual descent, and empirical firewall
Status: Technical edition · URR-RC-001 executed · residual closure UNRESOLVED
Claim Boundary
This companion records a typed state product, channel-specific residuals, the descent condition required for autonomous residual dynamics, dyadic movement, directionality, and empirical provenance. It does not identify the theorem, dyadic, retained-context, and empirical namespaces as one geometry; convert UNKNOWN into a resolved state; infer normative polarity from topology; or treat residual closure as empirical confirmation.
1. Typed State Dynamics
Let the joint state at loop n be:
S_n = (x_n, d_n, k_n)
Chart state: x_n ∈ X_C.
Dyadic encounter state: d_n ∈ X_D.
Retained context or seam state: k_n ∈ K.
This is a record product, not an identification of the three state spaces.
The state update is:
S_{n+1} = Φ_n(S_n)
x_{n+1} = H_{γ_n}(x_n)
d_{n+1} = T_{D,n}(d_n)
k_{n+1} = G_n(k_n, x_n, d_n)
The subscript n is retained because the route, T-mode, or context rule need not be stationary.
2. Typed Residual Product
Each channel uses its own declared comparison map:
Cmp_C: X_C × X_C → R_C
Cmp_D: X_D × X_D → R_D
Cmp_K: K × K → R_K
The residual components are:
δ^C_{n+1} = Cmp_C(x_n, x_{n+1})
δ^D_{n+1} = Cmp_D(d_n, d_{n+1})
δ^K_{n+1} = Cmp_K(k_n, k_{n+1})
The unified residual record is:
R_{n+1} = (δ^C_{n+1}, δ^D_{n+1}, δ^K_{n+1})
R_{n+1} is a typed tuple, not a scalar and not a common metric. If a channel has declared vector structure, Cmp(a,b) = b − a may implement its comparator. Subtraction is otherwise unavailable.
3. Residual Closure Requires Descent
Residual R_n depends on the state pair:
Z_n = (S_{n−1}, S_n)
q_R(Z_n) = R_n
The state-pair evolution is:
Ψ(S_{n−1}, S_n) = (S_n, Φ_n(S_n))
The update descends through the residual observation only if:
q_R(z) = q_R(z′) ⇒ q_R(Ψ(z)) = q_R(Ψ(z′))
When this implication holds, a representative-independent residual map exists:
F_R: im(q_R) → im(q_R)
F_R ∘ q_R = q_R ∘ Ψ
Only then may autonomous residual dynamics be written:
R_{n+1} = F_R(R_n)
Autonomous residual dynamics is a descent claim.
A failure witness has the form:
R_n = R_m but R_{n+1} ≠ R_{m+1}
Failure means the residual representation erased a dynamically relevant distinction or the domain was underspecified. The repair is to retain more context, refine C, D, or K, or narrow the declared domain—never to force closure.
4. Chart Residual Channel
For a loop route γ_n:
x_{n+1} = H_{γ_n}(x_n)
δ^C_{n+1} = Cmp_C(x_n, H_{γ_n}(x_n))
Allowed return classes include:
EXACT_RETURN
TRANSFORMED_RETURN
DRIFT
UNRESOLVED
A magnitude ‖δ^C‖ may be added only when the chart backend supplies the required metric or vector structure. The route γ_n remains part of the record:
same endpoint ≠ same route
5. Dyadic Residual Channel
The OMNIBUS dyadic observation is:
F_D(d_n) = (R_contact, C_bind, U_exit, N_third)
R_contact: reciprocal contact is available.
C_bind: a correction changes the next eligible behavior.
U_exit: exit is practically usable.
N_third: no compulsory constitutional third seat is required.
Let v_n = F_D(d_n). The dyadic residual is the typed transition:
δ^D_{n+1} = v_n → v_{n+1}
For fully resolved binary vectors, use the componentwise order:
v ⪯ w ⇔ v_i ≤ w_i for every coordinate i
Coordinate Movement
UP: v_n ≺ v_{n+1}.
DOWN: v_{n+1} ≺ v_n.
FLAT: v_n = v_{n+1}.
MIXED: neither resolved vector dominates the other.
UNRESOLVED: a required coordinate is UNKNOWN or the comparison is ineligible.
One improving coordinate does not cancel a simultaneous degradation.
Admissibility Gate
Let A_n = Adm_D(d_n).
0 → 1: OPENING.
1 → 1: STABLE_OPEN.
1 → 0: GATE_CLOSURE.
0 → 0: STILL_INADMISSIBLE.
Any unresolved endpoint: UNRESOLVED.
GATE_CLOSURE is a local admissibility transition, not residual closure. UNKNOWN is neither failure nor admissibility and may not be coerced to 0 or 1.
6. Retained-Context Residual
The retained-context channel contains only application-declared coordinates, for example:
k_n = (ρ_n, T-mode_n, memory_n, fatigue_n, …)
Its residual is:
δ^K_{n+1} = Cmp_K(k_n, k_{n+1})
Possible typed outputs include:
INTEGRATED
PRESERVED
FATIGUED
DISTORTED
DECAYED
UNCHANGED
UNRESOLVED
Every label requires a declared comparison rule. Observing k_n ≠ k_{n+1} does not by itself distinguish integration from distortion.
7. Empirical Provenance and Directionality Firewall
Empirical Provenance
Residuals do not manufacture empirical demotion. Use an explicit provenance join:
J_n: R_n ↝ {I_c records associated with episode n}
The empirical event record remains separately typed:
X_c(t) = (Object, Standing, Response, Route)
Eligibility remains separate:
χ_c(t) ∈ {1, 0, UNKNOWN}
Only eligible responses enter a declared denominator, and demotion is derived over a declared window rather than assigned from one response.
R_n ≠ X_c(t)
Residual and empirical records may be joined, compared, or crosswalked by provenance. Neither substitutes for the other.
Directionality Sidecar
Before assigning polarity, preserve:
constraint_source
constraint_standing
change_standing
route_source
route_holder
route_beneficiary
eligible_window
retained_context
The sidecar may be represented as:
P_n = (constraint source, constraint standing, change standing, route source, route holder, route beneficiary, eligible window, retained context)
Interpretive classification requires:
residual structure + directionality + empirical provenance
The forbidden shortcut is:
residual topology → good or bad
Dyadic movement ≠ normative polarity ≠ empirical demotion. Application-specific readings such as bigger, smaller, skewed, unchanged, or unresolved require their own declared rule.
8. Derived Residual Classification
Define the interpreted record:
ℜ_n = (R_n, P_n, J_n)
PROGRESSIVE
All required fields are resolved.
The dyadic state is UP, OPENING, or STABLE_OPEN.
No required admissibility coordinate degrades.
Directionality records authorized opening or preservation rather than third-held containment.
Retained context is integrated, preserved, or nondegrading.
Any empirical claim is independently supported through J_n.
Typical local forms are 0 → 1 or 1 → 1 with useful chart or context integration.
REGRESSIVE
The dyadic state is DOWN or the gate moves 1 → 0.
Usable contact, correction, or exit is lost.
The route becomes compulsory or third-held.
Retained context satisfies a declared fatigue, decay, or containment rule.
This classification does not require empirical demotion.
DISTORTED
Dir_D = MIXED; or chart, dyadic, and context channels disagree under their declared comparators; or the residual oscillates without a stable direction.
DISTORTED means incomparable or conflicting movement, not “whatever does not fit.”
UNCHANGED
The chart reports EXACT_RETURN, the dyadic channel is FLAT, and retained context is UNCHANGED.
UNRESOLVED
A required coordinate is UNKNOWN, censored, untyped, ineligible, or missing a provenance edge.
9. Minimal Detector Schema
The schema remains a reusable blank template. Executed runs are recorded separately and do not overwrite its defaults.
unified_return_residual:
  version: 0.1
  loop_id: null
  state_before:
    chart_state: null
    dyadic_state: null
    retained_context: null
  state_after:
    chart_state: null
    dyadic_state: null
    retained_context: null
  chart_residual:
    compare_rule: null
    route_gamma: null
    residual: null
    return_class: unresolved
  dyadic_residual:
    observation_before: [unknown, unknown, unknown, unknown]
    observation_after: [unknown, unknown, unknown, unknown]
    coordinate_direction: unresolved
    admissibility_before: unknown
    admissibility_after: unknown
    gate_transition: unresolved
  context_residual:
    compare_rule: null
    residual: null
    context_class: unresolved
  directionality:
    constraint_source: null
    change_standing: unknown
    route_source: null
    route_holder: null
    route_beneficiary: null
    polarity: unresolved
  empirical_links:
    constraint_response_record_ids: []
    eligibility_records_attached: false
    historical_v0_8_projection: null
  residual_closure:
    autonomous_F_R_claimed: false
    descent_test_run: false
    descent_status: unknown
  classification:
    residual_type: unresolved
    basis: []
    unresolved_fields: []
10. Executable Residual-Closure Test
Core question: Do two eligible episodes with the same observed residual produce the same next residual?
Eligibility
A comparison enters the equality/successor scan only when:
I_elig = 1 under a declared closure-test window.
One update_rule_id and domain_id govern both observations.
A complete typed R_n = (ΔC_n, ΔD_n, ΔK_n) is present.
A linked, observed R_{n+1} is present.
No UNKNOWN appears in the equality key or successor key.
At least two distinct present observations share the same residual key.
Decision Rule
Group eligible pairs by (update_rule_id, domain_id, ΔC_n, ΔD_n, ΔK_n).
If one equality group has more than one distinct successor tuple, retain the pair IDs as a descent counterexample and leave residual closure UNRESOLVED.
If no equality group has at least two observed successors, return UNRESOLVED_INSUFFICIENT_COVERAGE.
If every covered equality group has one successor tuple, report SAMPLE_CONSISTENT only. Do not promote a sample result to theorem-level CLOSED unless the declared domain is exhausted or a separate proof supplies the universal implication.
Residual closure is CLOSED only when descent is demonstrated on the declared domain. It remains UNRESOLVED when descent fails, is untested, or lacks eligible coverage.
11. First Executed Check — URR-RC-001
Status: EXECUTED · coverage-first gate · residual closure UNRESOLVED
Source and Unit
Source specifications: GQG v0.12 and OMNIBUS v7.77.
Observed source record: POST-FREEZE MOVEMENT LEDGER — Wobble + Coup + Corridors — v0.1.
Observed source Drive file ID: 1NllZE54FSGiV1dKNukEd2dnJBfKWelL1OZbpbJ_UJrk.
Unit tested: a typed present-residual/next-residual pair inside one declared update domain. A descriptive event classification was not substituted for a residual tuple.
Observed Scan
Candidate observed movement rows scanned: 10.
Frozen prospective nodes inspected with successors reserved: PF-USPS-01 and PF-EMP-01.
Complete typed present-residual/next-residual pairs: 0.
Equality groups with at least two observed successors: 0.
Retained counterexample pairs: 0.
Zero counterexamples is not positive evidence because zero eligible equality groups were available. The movement ledger preserves event classifications, frozen objects, state effects, and limits, but does not supply complete ΔC/ΔD/ΔK tuples, a common frozen update_rule_id, or typed successor links.
Executed Record
residual_closure_run:
  run_id: URR-RC-001
  mode: coverage_first_gate
  source_record_ids:
    - 1NllZE54FSGiV1dKNukEd2dnJBfKWelL1OZbpbJ_UJrk
    - 13g-nyjUeMrtQRECXugx7DAdX5RrN0OzA
    - 1n2DqVJOMqZMMk-Tzp96yTExrKE-0Y-F4
  candidate_observed_rows: 10
  reserved_successor_record_ids: [PF-USPS-01, PF-EMP-01]
  closure_eligible_present_successor_pairs: 0
  equal_residual_groups_with_two_successors: 0
  counterexample_pair_ids: []
  autonomous_F_R_claimed: false
  descent_test_run: true
  descent_status: unresolved_insufficient_eligible_repeats
  closure_status: unresolved
  refinement_required: true
Namespace Results
Theorem status: the residual-descent implication remains conditional. URR-RC-001 neither proves nor disproves universal descent.
Dyadic status: UNRESOLVED. The source ledger lacks the four resolved dyadic coordinates required for coordinate-movement or gate-transition coding.
Empirical status: unchanged. No event was reclassified, no prospective score was altered, no demotion rate was manufactured, and no descriptive class was treated as a residual tuple.
First-Run Conclusion
The gate is executable and has been run. Its result is not UNKNOWN in the sense of “never tested”; it is UNRESOLVED because the existing records contain insufficient eligible repeated residual-successor observations.
The next admissible lift is record completion, not forced closure. Future loops must retain update_rule_id, domain_id, state_pair_observation_id, the typed R_n tuple, its observed successor, I_elig, and the provenance join.
12. Compact Checksum
S_n ─Φ→ S_{n+1} ─Compare→ R_{n+1}
Does Φ descend through the residual observation q_R?
One record may carry multiple typed channels; one record does not make one geometry.
Residual means declared comparison, not automatic subtraction.
State dynamics first; residual dynamics only after descent.
Equal present residuals with unequal successors expose a missing retained distinction.
Same endpoint does not imply same route.
Dyadic coordinate movement does not imply scalar coherence or normative polarity.
Residual topology does not imply empirical demotion.
UNKNOWN remains unresolved.
URR-RC-001 executed the gate but lacked eligible repeated successors, so closure remains UNRESOLVED.
No forced closure.
13. Next Admissible Run
Purpose
The next run should resolve the coverage defect exposed by URR-RC-001. It must add eligible repeated residual-successor observations, not strengthen the claim attached to the existing sample.
Minimum Acquisition Contract
Freeze before scanning:
One update_rule_id and one domain_id.
A declared eligibility window and I_elig rule.
Complete typed R_n = (ΔC_n, ΔD_n, ΔK_n) records.
Linked, observed R_{n+1} successors.
Source IDs, observation IDs, timestamps, pair IDs, and provenance joins.
A policy that excludes UNKNOWN from equality and successor keys.
The first analyzable group requires at least two distinct eligible present observations with equal residual keys and observed successors.
Outcome Ledger
No eligible repeated key: descent_status: unresolved_insufficient_eligible_repeats; closure_status: unresolved.
Equal R_n, unequal R_{n+1}: descent_status: failed_counterexample; closure_status: unresolved; retain the witness pair.
Equal R_n, equal R_{n+1} across covered groups: sample_status: sample_consistent; theorem_status: conditional; do not report universal closure.
Domain-exhaustive proof or a separately supplied theorem: theorem_status: closed_on_declared_domain; record proof scope and assumptions.
Namespace Lock
Theorem status changes only through a descent proof or counterexample.
Dyadic status changes only from complete resolved dyadic coordinates under declared coding rules.
Empirical status changes only through separately eligible empirical records and denominators.
No result in one namespace silently upgrades another.
The next gain is eligible repetition, not stronger language.

