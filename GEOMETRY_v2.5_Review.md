# Geometry v2.5 — accepted acquisition-cost extension

**Accepted and integrated as §5.1, “Repair after observing the label.”** The incoming proof is correct under its explicit finite-domain, available-label, fixed nonnegative-cost, unchanged-state, and uncoupled-choice assumptions. No mathematical correction was needed.

The populated Google Doc supplied with this upgrade, [Working Master v2.4](https://docs.google.com/document/d/1DzF5KshR_nsHfMJoM7KKsXek4DpCnwJPM2DKHZYw9z4/edit), matches the local v2.4 text exactly after extracting its body. It is distinct from the empty companion created earlier. This follow-up integrates into a new local v2.5; it does not edit either Google Doc.

## What is now accepted

For bad-pair separating families H_q and weighted hitting-set optimum τ_a:

C_fixed = τ_a(⋃_q H_q).

C_label,worst = max_q τ_a(H_q).

C_label,expected = Σ_q p(q)τ_a(H_q).

Every exact policy needs a hitting set in every fiber. Choosing a local cost optimum after seeing q attains all local bounds simultaneously, proving the worst-case and expected formulas. The four-state example gives fixed cost 2 versus label-conditioned cost 1. The k-fiber construction attains the sharp inequality C_fixed≤k C_label,worst.

Use **label-conditioned batch acquisition** for this policy class. Fully sequential acquisition can use earlier acquired values to choose later queries; its optimizer is a different problem. The three-bit selector example correctly separates batch cost 3 from sequential worst-case cost 2.

## Qualifications kept in the integration

- Correctness covers every attained fiber, including those assigned probability zero. An impossible fiber prevents a globally exact policy; feasibility is checked before expectation.
- Optimal inventory cost equals the fixed-set optimum. The inventory of a chosen cheapest-per-case policy need not be optimal. The new implementation reports both separately.
- A k-factor ratio needs positive worst-case cost; the inequality itself also handles zero cost. There is no corresponding distribution-free k-factor bound against expected cost.
- The label is genuinely available before acquisition. For acquiring the service answer, use π_pre and fixed A_task; π_DS=(O,A) already contains A and gives zero repair cost for that target.
- Query costs, installation cost, visible-stage deletion cost, latency, energy, and human effort remain different quantities. The theorem does not establish empirical savings in the latter measures.

The full incoming review already states these boundaries. The v2.5 insertion makes the separately optimized inventory distinction explicit and adds its concrete common-coordinate example.

## Independent verification performed here

The incoming source reports 4,096 checked tables. A source receipt was located, but no original test script was found in its work directory. This task independently reconstructed the checker rather than claiming to rerun that unavailable source code.

All 4,096 binary four-state tables were checked with labels A,A,B,B, two binary coordinates, costs (1,1), (1,3), and (0,2), and exact label probabilities 1/4 and 3/4. The reconstruction passed:

- 16,384 direct fixed-set sufficiency comparisons;
- 65,536 direct label-policy sufficiency comparisons;
- 12,288 weighted objective bundles, containing 49,152 objective equalities;
- 960 correctly identified unrepairable tables;
- 128 tables with a strict unit-cost worst-case advantage.

The k=1,…,8 separation examples and the sequential selector example passed. Additional fixtures checked zero prices, impossible zero-probability fibers, service-answer circularity, and unavailable audit evidence. The exhaustive counts reproduce the source-reported counts.

A separate independent mathematical check covered 256 pairs of two-coordinate separating-set families, including empty families and impossible edges, six cost profiles, and three probability profiles. Its 1,152 objective comparisons passed, including inventory optimization and the zero-probability feasibility boundary.

The new executable companion also passed comparison against the independent direct-record brute-force calculation on all 12,288 table/cost cases. Its 23 focused tests cover malformed or missing inputs, exact costs and probabilities, zero-price repairs, impossible fibers, deterministic ties, and the distinction between selected-policy and optimal inventory. The inherited geometry_engine.py is unchanged.

These are synthetic finite checks. The unrestricted claims rest on the proof and assumptions. This follow-up did not repeat the incoming review's 54-title/495-file Drive search, run a live service trial, or change any physical or historical status.

## Release contents

**GEOMETRY_Working_Master_v2.5.md** carries forward v2.4 and inserts the accepted §5.1, with a §8 service cross-reference. **geometry_adaptive.py** supplies the exact finite label-conditioned batch optimizer alongside the unchanged **geometry_engine.py**. **GEOMETRY_v2.5_Verification.json** records the independent table reconstruction. **Geometry_Adaptive_Repair_Source.md** preserves the incoming review and its inventory. The v2.4 files and test receipt remain the earlier baseline.

Google Docs were read for source verification only. This is a completed local integration, not a claim that the private Docs save succeeded.
