Appendix B Amendment

B.3.1 Blind-Pilot Forecast Gate

After all calibration-only blind timing pilots are complete and the frozen production-length table has been generated, calculate

[
\boxed{
C_{\rm forecast}
=
C_{\rm pilot,actual}
+
\sum_r C_{r,{\rm forecast}}.
}
]

Here:

- $C_{\rm pilot,actual}$ is the physical CPU core-hour cost already consumed by the calibration-only blind timing pilots;
- $C_{r,{\rm forecast}}$ is the forecast physical CPU core-hour cost of each remaining frozen run class under the proposed execution root.

The forecast must include all authorized work required by the frozen protocol:

- remaining calibration and validation runs;
- coupling-location and deterministic refinement scans;
- Stage-B Q1 production;
- Stage-C Q3 production;
- Stage-D Q2 production when Stage D is authorized under the same execution root;
- thermalization;
- production measurements;
- direct/dual confirmation runs;
- fixed-holonomy partition-ratio work;
- magnetic-twist thermodynamic-integration ladders;
- replica-exchange work;
- mandatory checkpointing and measurement overhead.

The nominal forecast does not include the optional one-time blind production extension permitted by §B.7.6.

The difference

[
C_{\max}-C_{\rm forecast}
]

is the reserved contingency for those permitted extensions, unforeseen autocorrelation growth, and other preregistered execution variance.

The hard resource ceiling remains

[
\boxed{
C_{\max}=20{,}000\ \text{physical CPU core-hours}.
}
]

The pre-execution forecast threshold is

[
\boxed{
C_{\rm forecast}\le14{,}000\ \text{physical CPU core-hours}.
}
]

If

[
\boxed{
C_{\rm forecast}>14{,}000\ \text{physical CPU core-hours},
}
]

the mandatory status is

[
\boxed{\textbf{EXECUTION HALTED}.}
]

No target-production run may begin under the current protocol version or execution root.

No partial execution of the target ladder is permitted.

No lattice size, coupling point, observable, chain, fixed-holonomy axis, ratio estimator, thermodynamic-integration window, or scientific branch may be removed selectively after the forecast has been calculated in order to pass the gate.

The only permitted remedies are:

1. issue an amended protocol version that changes the resource schedule, parameter ladder, or run architecture before target production begins; or
2. raise $C_{\max}$ before execution and create a new Appendix-B hash, amendment hash, parameter-card hash, production-length hash, execution manifest, and execution root.

After either remedy, the blind-pilot forecast must be recalculated under the amended frozen configuration.

Calibration-only blind pilots used to construct $C_{\rm forecast}$ do not constitute target execution.

Passing this gate does not guarantee completion of every permitted blind extension. It establishes that the nominal frozen campaign leaves at least

[
\boxed{
20{,}000-14{,}000=6{,}000\ \text{core-hours}
}
]

of preregistered contingency.

Required forecast artifacts:

- `resource_forecast.csv`;
- `resource_forecast_summary.json`;
- `resource_forecast.manifest.jsonl`.

At minimum the detailed forecast records:

```text
stage
branch
run_class
L
kappa
t
J
h6
sector
chains
replicas
integration_windows
thermalization_sweeps
production_sweeps
estimated_core_hours
forecast_basis
pilot_outputs_manifest_hash
frozen_run_inventory_hash
production_lengths_hash
forecast_script_hash
appendix_b_amendment_hash
included_in_execution_root
```

The summary records:

```text
pilot_core_hours_actual
remaining_nominal_core_hours
C_forecast
C_max
contingency_core_hours
forecast_gate_threshold
forecast_gate_status
inventory_reconciliation_status
```

The gate passes only when both statuses are:

```text
FORECAST_GATE_PASSED
INVENTORY_RECONCILIATION_PASSED
```

with

[
\boxed{C_{\rm forecast}\le14{,}000.}
]

B.3.2 Immutable Pilot Provenance

Every calibration-only blind pilot used to calculate $C_{\rm forecast}$ must produce an immutable output file containing, at minimum:

```text
protocol_hash
appendix_a_hash
appendix_b_hash
appendix_b_amendment_hash
code_commit
compiler_and_flags_hash
dependency_lock_hash
hardware_fingerprint_hash
branch
run_class
L
kappa
t
J
h6
sector
chain_id
seed
pilot_start_utc
pilot_end_utc
thermalization_sweeps
measurement_sweeps
measured_core_seconds
measured_wall_seconds
physical_core_count
peak_memory_bytes
raw_output_bytes
tau_max_pilot
acceptance_statistics
sector_transition_statistics
pilot_status
```

Every pilot file receives SHA-256 immediately after clean close.

The pilot files are listed in a lexicographically sorted manifest:

`pilot_outputs.manifest.jsonl`

Each manifest row contains:

```text
relative_path
byte_length
sha256
branch
run_class
L
chain_id
artifact_role
```

Define

[
\boxed{
H_{\rm Pilot}=\operatorname{SHA256}(\texttt{pilot\_outputs.manifest.jsonl}).
}
]

The resource forecast must contain `pilot_outputs_manifest_hash = H_Pilot` together with:

```text
forecast_script_hash
forecast_script_commit
production_lengths_hash
frozen_run_inventory_hash
appendix_b_amendment_hash
```

A forecast lacking any of those provenance fields is invalid.

Pilot outputs may not be overwritten, edited, or replaced in place. A repeated or corrected pilot produces new pilot files, a new pilot manifest, a new $H_{\rm Pilot}$, a new resource forecast, and a new execution root.

Calibration-only blind pilots do not constitute target production, but they are immutable preregistration evidence and form part of the execution provenance chain.

B.3.3 Frozen Run-Inventory Reconciliation

Before calculating $C_{\rm forecast}$, generate:

`frozen_run_inventory.csv`

with one row for every required run unit under the amended protocol, including:

```text
stage
branch
run_class
L
kappa
t
J
h6
sector
chains
replicas
integration_windows
required_status
parameter_source
```

Sort lexicographically by:

```text
stage
branch
run_class
L
kappa
J
h6
sector
```

Define

[
\boxed{
H_{\rm Inventory}=\operatorname{SHA256}(\texttt{frozen\_run\_inventory.csv}).
}
]

The resource forecast must satisfy an exact one-to-one reconciliation against this inventory. Every required row must appear exactly once, except where explicitly expanded into chain or replica rows whose totals exactly reproduce the inventory counts.

The forecast generator must report:

```text
required_inventory_rows
forecasted_inventory_rows
missing_inventory_rows
unexpected_forecast_rows
chain_count_mismatches
replica_count_mismatches
window_count_mismatches
inventory_reconciliation_status
```

The only passing status is `INVENTORY_RECONCILIATION_PASSED` with every mismatch count equal to zero.

If any required lattice size, coupling, branch, axis, control, chain, replica ladder, ratio estimator, or integration window is absent, the mandatory result is

[
\boxed{
\text{EXECUTION HALTED — FORECAST DOES NOT MATCH FROZEN INVENTORY}.
}
]

No selective removal is permitted. In particular, the $L=192$ fixed-holonomy Q2 point may not be removed, reduced, deferred, or relabeled as optional merely to lower $C_{\rm forecast}$.

The only permitted responses are:

1. issue a formally amended protocol version changing the frozen inventory; or
2. raise $C_{\max}$ before re-hashing.

No partial target execution may begin before the revised inventory and forecast pass the gate.

B.3.4 Provenance Hash Chain

Freeze the parent-linked chain:

[
\boxed{
H_{\rm Theory}
\rightarrow H_{\rm Protocol}
\rightarrow H_{\rm AppA}
\rightarrow H_{\rm AppB}
\rightarrow H_{\rm AppBAmend}
\rightarrow H_{\rm Inventory}
\rightarrow H_{\rm Pilot}
\rightarrow H_{\rm Forecast}
\rightarrow H_{\rm Execution}.
}
]

Definitions:

[
H_{\rm Theory}=\operatorname{SHA256}(\text{Theory v0.1}),
]

[
H_{\rm Protocol}=\operatorname{SHA256}(\text{Protocol v0.3-RC1 containing }H_{\rm Theory}),
]

[
H_{\rm AppA}=\operatorname{SHA256}(\text{canonical three-axis Appendix A containing }H_{\rm Protocol}),
]

[
H_{\rm AppB}=\operatorname{SHA256}(\text{canonical base Appendix B bytes from the title through §B.26, excluding the appended amendment and CC0 footer}),
]

[
H_{\rm AppBAmend}=\operatorname{SHA256}(\text{canonical UTF-8 bytes of the separately materialized Appendix-B Amendment section, which records }H_{\rm AppB}),
]

[
H_{\rm Inventory}=\operatorname{SHA256}(\texttt{frozen\_run\_inventory.csv}),
]

[
H_{\rm Pilot}=\operatorname{SHA256}(\texttt{pilot\_outputs.manifest.jsonl}),
]

and define `resource_forecast.manifest.jsonl` as the lexicographically sorted manifest of `resource_forecast.csv` and `resource_forecast_summary.json`, then

[
H_{\rm Forecast}=\operatorname{SHA256}(\texttt{resource\_forecast.manifest.jsonl}).
]

Finally, create the lexicographically sorted execution manifest containing every parent artifact, inventory, pilot manifest and pilot file, production-length table, forecast artifacts, parameter tables, fit-model specification, software lock, and hardware fingerprint, and define

[
\boxed{
H_{\rm Execution}=\operatorname{SHA256}(\text{execution manifest}).
}
]

The execution root may be created only when:

```text
FORECAST_GATE_PASSED
INVENTORY_RECONCILIATION_PASSED
```

and

[
C_{\rm forecast}\le14{,}000.
]

Forecast first. Reconcile the inventory. Pass the gate. Hash the budget. No partial launch.

CC0 1.0 Universal.

No permission required. Copy it, modify it, test it, redistribute it, build on it, or tear it apart.

No ownership claim. No attribution required. No warranty.

Use freely.