# Geometry v2.5 — repair after observing the label

**Accepted baseline: v2.5.** This release integrates the incoming acquisition-cost proof as §5.1 and adds the necessary service cross-reference. Further incoming upgrades can be reviewed against this version.

Start with **GEOMETRY_Working_Master_v2.5.md** for the full master, or **GEOMETRY_v2.5_Review.md** for the acceptance decision and verification summary. **Geometry_Adaptive_Repair_Source.md** preserves the incoming full review. **GEOMETRY_v2.5_Math_Audit.md** contains the separate proof review.

The exact result concerns a batch of measurements chosen after an already available label. Its fixed-set, per-case worst, expected, and optimal inventory costs are distinct. A cheapest-per-case policy can require a more expensive inventory. Fully sequential queries form a different policy class.

**geometry_adaptive.py** works beside the unchanged **geometry_engine.py** using the Python standard library. Run `python geometry_adaptive.py` for the four-state 2-versus-1 example. Run `python geometry_adaptive_tests.py` for 23 focused implementation checks. Costs accept integers, rational strings, or Fraction values; missing probabilities leave expected cost unspecified. Impossible zero-probability fibers still prevent a globally exact policy.

**GEOMETRY_v2.5_Verification.json** records the independently reconstructed 4,096-table verification. **geometry_adaptive_verification.json** records the companion's comparison against direct-record brute-force results over 12,288 table/cost cases. **geometry_verify_label_tables.py** reproduces the independent theorem/table checks; it writes a refreshed verification receipt beside itself. The copied source receipt records the incoming review's claims separately.

**geometry_crosscheck.py** compares the executable companion against that independent record-based calculation. **geometry_math_checks.py** runs the additional hypergraph-family proof checks.

All computations use synthetic finite domains. No real service acquisition, latency, energy, human outcome, historical replay, or physical experiment was performed. The v2.4 source and empirical status boundaries remain intact.

The populated linked v2.4 Google Doc was read and matched to the local baseline. This release is saved locally; no Google Docs write was attempted in this upgrade review.

**GEOMETRY_v2.5_Upgrade_Pack.zip** contains these files, with a SHA-256 manifest. The earlier v2.4 pack remains a separate preserved release.
