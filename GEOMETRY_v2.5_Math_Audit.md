# Independent review: label-conditioned batch acquisition

**Disposition: ACCEPT as a substantive extension of v2.4 §5, under the proposal's stated assumptions. No false theorem or proof gap found.** This is a new acquisition-policy optimization relative to the fixed-menu result already implemented. It is not an escape from non-descent, a new topology, or a proof of reduced physical latency or energy.

Reviewed the full mathematical argument in `C:/Users/drewd/Documents/Codex/2026-09-12/vh/outputs/Geometry_Adaptive_Repair_Review.md`, and v2.4 §§5 and 8. The incoming review's broad-corpus and execution claims are source-reported here; this mathematical review does not independently certify that search provenance. The separate finite checks below were actually executed in this task.

## Assumptions that must remain adjacent to the formulas

1. D is a nonempty declared complete finite domain, and Q=π(D) contains attained labels only.
2. π and W are fixed total maps. The finite primitive menu c_j is total and genuinely queryable on the same unchanged state.
3. Both competitors know q before any additional acquisitions. Its cost is sunk or charged identically.
4. Each coordinate has a fixed finite nonnegative cost a_j, charged once when acquired. No label- or value-dependent price, acquisition side effect, or coupled capacity/admissibility constraint is included.
5. The policy selects a batch J(q) from q alone. Subsequent measured values do not alter this batch.
6. Every attained fiber is repairable before optimizing worst-case or expected cost. The expected objective uses a declared probability distribution p on all attained labels, while exact correctness still covers all D.

These assumptions are already present in the incoming review. Preserve them when compressing it into §5.1.

## Proof scrutiny

For each label q, H_q consists of the coordinate-separation sets of all same-q/different-W pairs. The retained record includes q and the selected indexed values in fixed order.

**Local sufficiency equivalence: correct.** Equal records must share q, hence use the same batch. They fail to distinguish a bad pair exactly when the chosen set misses that pair's separating edge. No comparison across different q is required, because q itself remains retained.

**Fixed optimum: correct.** A single global batch must hit every edge in every H_q, so its optimal cost is τ_a(∪_q H_q). This competitor may observe q; “fixed” means its acquired set is constrained not to vary with q.

**Worst-case label-policy optimum: correct.** Every exact policy costs at least τ_a(H_q) on q. Independent local minimizing choices attain all these lower bounds simultaneously, proving max_q τ_a(H_q). Independence of the feasible choices is essential here.

**Expected optimum: correct.** The same pointwise construction gives Σ_q p(q)τ_a(H_q). Nonnegative weights yield expected≤worst≤fixed. Zero-probability fibers need not use their minimum-cost repair to achieve the expected optimum, but they must still use some exact repair.

**Inventory equality: correct, with a distinction worth making explicit.** The union of any exact policy's acquired sets is a globally sufficient fixed set. Conversely an optimal fixed set can be used on every q. Therefore the separately minimized inventory objective equals the fixed optimum. An arbitrary policy made from independently selected local optima need not minimize inventory. Example: both fibers can be repaired by either c₁ or c₂ at unit cost. Choosing c₁ on one and c₂ on the other is acquisition-optimal per case but uses inventory 2; the optimum inventory is 1. This does not contradict the proposal's equality, whose left side explicitly minimizes over policies.

**k-label bound: correct.** If J_q is a local cost minimizer, its union hits every required edge. Since costs are nonnegative, cost(∪_q J_q)≤Σ_q cost(J_q). Thus fixed≤Σ local≤k·worst. The construction with two states per label and one private required coordinate per label attains fixed=k and worst=1 at unit prices. The displayed inequalities remain valid when worst=0; a ratio statement requires a positive denominator. In particular, worst=0 forces fixed=0 here.

**No distribution-free k-bound against expected cost: correct.** Two labels suffice: let one be already clean and the other require a unit-cost coordinate with probability ε>0. Then fixed=worst=1 and expected=ε, giving ratio 1/ε. This is true even with positive probability for both labels.

**Sequential distinction: correct.** With constant q and all eight states (s,a,b), W=a for s=0 and W=b for s=1. Omitting a fails on the s=0 states; omitting b fails on the s=1 states; omitting s fails when a≠b. Every fixed batch therefore needs all three coordinates. Reading s and then the relevant payload bit gives sequential worst-case cost 2. A one-query worst-case policy would have a fixed first coordinate and require that coordinate alone to resolve W, which none does. Thus 2 is optimal, not merely an exhibited upper bound. The batch theorem does not claim to optimize this stronger policy class.

## Edge cases and wording to preserve

- An empty family H_q is a clean fiber and has optimum zero because costs are nonnegative.
- A family containing the empty edge is impossible through the menu. Check feasibility before calculating expected objectives. Do not substitute a zero contribution for a zero-probability impossible fiber by treating 0·∞ as 0. Under the whole-domain claim, there is no exact policy at all.
- Zero-cost coordinates are permitted and do not invalidate the proofs. They may create multiple optimal or redundant solutions. Minimum cost, minimum cardinality and inclusion-minimality are distinct.
- Negative prices are outside scope: they invalidate the zero optimum for an empty edge family and the union-cost bound used in the k-factor proof. Do not silently accept them in implementation.
- Fixed nonnegative prices are not all possible cost models. Installation, shared setup, budgets, interference, state-dependent acquisition, and composite measurements require a new declared optimization problem.
- A policy whose domain or witness is only empirically sampled supplies an exact finite-table statement, not certified coverage of unobserved states.

## Service integration

The incoming review correctly catches a circular application: π_DS(E)=(O,A) already contains A, so its repair cost for witness A is zero. Before answering, use a separately declared π_pre that contains only available request/context information and repair an independently validated target. After answering, π_DS may be retained while W is a distinct audit witness, provided the queried historical evidence exists.

This preserves v2.4 §8's A_sel versus A_task distinction. Acquisition optimization does not certify answer completeness, predict future responses, or authorize historical evidence reconstruction. It also does not replace the joint invariance check for adaptive deletion and reselection.

## Independent verification executed here

`work/adaptive_math_check.py` exhaustively enumerated all 256 pairs of separating-set families over two coordinates, including empty families and families containing an empty edge. It evaluated six nonnegative cost profiles, including zero prices, and three probability profiles including zero-probability labels.

Result: **PASS**. There were 64 globally feasible family pairs, 192 globally impossible pairs, and 1,152 direct objective comparisons. For each feasible case it enumerated every exact batch policy and checked fixed optimum, local worst optimum, expected optimum, inventory equality and the k=2 bound. It separately checked the zero-probability impossible-fiber rule and an acquisition-optimal policy that is not inventory-optimal.

These are independent synthetic hypergraph checks, additional to the incoming review's source-reported binary-table verification. They are not service experiments or evidence of real-world acquisition savings.

## Suggested integration scope

Accept one increment: §5.1 with the local theorem, exact worst/expected formulas, four-state separation and separately optimized inventory equality. Include the k-bound as a short consequence, and one sentence distinguishing sequential policies. Add the pre-answer/audit qualification to §8. No theorem correction is needed; the compact release must retain the assumptions and edge cases above.

No output files or external documents were edited by this review.
