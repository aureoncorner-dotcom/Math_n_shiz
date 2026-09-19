# **03 — Triadic Mediation Results — Source Edition**

This is a readable source edition. The source report's historical execution statements retain their original scope. Fresh verification and new integration decisions are recorded separately in the upgraded master. Formula and program notation are preserved as editable source text.

Original source: [Triadic\_Mediation\_Results\_v0\_1.md](https://drive.google.com/file/d/1R2JzBcvC18k1CGaS72A8mQGCVQpwXNhi/view?usp=drivesdk)

# **Triadic mediation · first executable result**

**The declared finite software comparison has now been run. Preserving the bias signal helped this controller; adding an identity mediator supplied no task-performance advantage over the equally informed direct controller.** The broader question of useful mediation in a real application remains open.

This companion is grounded in the current Drive Triadic Overlap Hypothesis · v2 [\# Triadic Overlap Hypothesis · v2](https://docs.google.com/document/d/116oVwVqZBV6eGKMCXvhjR606o8_h-t1CNOg9dSLbAQE/edit), modified Sep 6, 2026, especially §§4, 6, 8–9. Its experiment was explicitly unrun in that document. The Drive text was not changed. This package adds one specified toy implementation and its receipt, rather than retrospectively treating the framework as established.

## **What was executed**

TOH-MED-001-v0.1 compares direct, identity-preserving, bias-erasing, one-tick-delayed, and three-tick-delayed observations for the same scalar recovery controller. It uses exact rational updates, known true states, a declared finite grid, fixed disturbances, and separate raw and transformed records. The direct and preserving arms receive the same usable information and use the same policy.

Development: 40 arm-episodes / 3,840 ticks. Evaluation: **48 matched scenarios × 5 arms \= 240 arm-episodes / 23,040 ticks**, with 24 scenarios per workload. No training, random sampling, parameter search, exclusions, or repairs during evaluation. The protocol and scientific inputs were locally hash-sealed before evaluation. This is a local prospective commitment, not an externally registered or blinded study.

## **Evaluation outcomes**

Mean error is mean absolute post-action displacement from the target zero. J combines that error with explicitly modeled operations, scalar storage slots, and observation age under the declared weights. It is not measured CPU time or a deployment price.

| Context-dependent workload | Mean error | J | Unrecovered windows / total&nbsp;&nbsp; |
| :---- | ----: | ----: | ----- |
| Direct | 0.045058 | 0.104058 | 0 / 72 |
| Preserving mediation | 0.045058 | 0.138058 | 0 / 72 |
| Bias-erasing mediation | 1.722141 | 1.816141 | 48 / 72 |
| One-tick delay | 0.188493 | 0.323389 | 0 / 72 |
| Three-tick delay | 7.654476 | 7.868851 | 72 / 72 |

Recovery means entering |x|≤1/16 for three consecutive states before the next disturbance. Unrecovered windows are censored at their declared boundary; they are not proof of failure for all future time. Window-level first-entry and confirmation times are in episodes.jsonl.

| Overhead-control workload | Mean error | J | Unrecovered windows / total&nbsp;&nbsp; |
| :---- | ----: | ----: | ----- |
| Direct | 0.045058 | 0.104058 | 0 / 24 |
| Preserving mediation | 0.045058 | 0.138058 | 0 / 24 |
| Bias-erasing mediation | 0.045058 | 0.139058 | 0 / 24 |
| One-tick delay | 0.066985 | 0.201881 | 0 / 24 |
| Three-tick delay | 6.206535 | 6.420910 | 24 / 24 |

**Architecture:** Direct and preserving mediation have exactly equal states, received task state, actions, and forecasts at every paired tick across both workloads. Their mean error difference is exactly zero. Preserving mediation raises J by exactly 17/500 \= 0.034 under the base cost weights. Identity copying supplies no recovery or prediction improvement here, and fails the chosen value-added rule. This equality is expected from the model construction, so it is chiefly an implementation and fairness check.

**Information:** On the context-dependent workload, preserving versus erasing bias reduces mean error by 1.677083 and J by 1.678083; it meets the declared minimum-improvement and censoring criteria. On the control workload, where bias is always zero, erasure changes no trajectory or error. This supports the relevance of the chosen bias field to this stateless policy. The direct arm preserves that field too. The experiment does not establish that a separate mediator is necessary, or that an adaptive history-based estimator could not recover the missing bias.

**Timing:** Both delays increase finite-horizon error in this controller. One-tick delay still recovers within every window; three-tick delay does not meet the recovery criterion in any evaluation window. These results concern uncompensated delayed feedback at gain 1/2. They do not show that every delayed controller is unstable or that delay is irreversible information loss.

summary.json preserves exact fraction scores, all paired deltas, forecast error, constituent costs, and the declared cost-weight sensitivity grid {0,0.1,1,10}. Under zero cost weights, direct and identity mediation tie; positive weights charge the additional path. There are no inferential population p-values or confidence intervals for this finite deterministic grid.

## **Exact Twin Timelines benchmark**

The implementation reconstructs pairs from v2 §6 using exact rational coefficients in Q(√5), not floating phase comparisons. It checks the source's half-open observation boundary: zero slips, tau does not.

> * Six pairs at history lengths **1, 2, 39, 64, 127, and 1,024** have equal recorded histories and unequal next observations.  
> * At length 39, observations 1–39 match and observation 40 differs.  
> * Phase-aware direct and preserving predictors each get **12/12** next observations correct.  
> * The fixed history-only predictor gets **6/12** correct. Since each constructed pair has the same input and opposite next labels, any deterministic predictor limited to that identical history cannot get both members right. This is a fact about these balanced pairs, not a universal 50% accuracy ceiling.  
> * Twelve checks show that stale exact phase plus known age and rotation permits exact advancement. This benchmark repair differs from the deliberately uncompensated controller timing conditions.

The source's linked mathematical notes, source manifest, local evidence file, and original released executable were not recovered here. The benchmark therefore establishes the behavior of this **new reconstruction**, not byte-for-byte reproduction of the earlier release. Exact phase provision is an idealized input condition. No blind human trial was run, and no physical branching, agency, or chaos claim follows.

## **Evidence and review boundaries**

Seven mechanism tests passed before evaluation. After execution, all input/output hashes passed verification, and a separate read of the raw logs verified all 23,040 plant recurrences and recomputed all 240 episode mean errors exactly. JSON Schema engine validation was not run because that optional package was unavailable; the executable itself has no external dependencies. VALIDATION.json records this distinction.

Scientific inputs were not changed after evaluation. Full run receipts retain code, configuration, source, and protocol hashes; exact timestamps; environment; counts; and output hashes. No controller repairs were applied, and both repair logs are empty. In this artifact, preservation/erasure/delay are declared experimental conditions, not post-hoc repairs relabeled as original outcomes.

This closes one narrow software instantiation of §9. It leaves **application-level benefit and actual resource economics untested**. A next version should specify an additional useful mediator function and compare it against a direct design with the same information and computational opportunities. Candidate functions and new cost calibration belong in a new protocol version; this result remains available to challenge them.

The reusable package includes the CLI, protocol, configuration, source snapshot, raw records, tests, schemas, receipts, and this interpretation. Start with README.md to reproduce it.