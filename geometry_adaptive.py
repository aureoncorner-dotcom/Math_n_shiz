"""Exact label-conditioned coordinate acquisition on a complete finite table.

Companion to the adjacent geometry_engine.py; Python standard library only.
The label q must already be available to both competing methods. A fixed menu
contains total, available primitive measurements of the same unmodified state.
Each policy chooses one batch after q; it never chooses a later measurement
from an earlier measurement's value. This is not a sequential optimizer.

Costs are nonnegative exact rationals. Label probabilities are optional and
never waive correctness at zero-probability attained labels. Costs concern
acquisition, not latency, energy, bytes, service deletion, or physical evidence.
Exactness covers the full caller-declared table; completeness of a real system,
advance availability of q, and query nonmutation are caller-held obligations.

Search is exhaustive and exponential in the coordinate menu. Defaults bound
the menu at 20 coordinates and the table at 256 states; callers can explicitly
raise those guards. Values supplied as callables are evaluated once per state.
"""

from collections.abc import Mapping
from dataclasses import dataclass
from fractions import Fraction
from itertools import islice

from geometry_engine import Collision, IncompleteDomain, RepairEdge, coordinate_repairs


@dataclass(frozen=True)
class BatchOptimum:
    feasible: bool
    selected: tuple | None
    cost: Fraction | None
    edges: tuple[RepairEdge, ...]
    infeasible_pair: Collision | None


@dataclass(frozen=True)
class LabelOptimum:
    label: object
    states: tuple
    batch: BatchOptimum


@dataclass(frozen=True)
class AcquisitionResult:
    feasible: bool
    labels: tuple
    coordinate_order: tuple
    per_label: tuple[LabelOptimum, ...]
    fixed: BatchOptimum
    worst_cost: Fraction | None
    expected_cost: Fraction | None
    optimal_inventory_cost: Fraction | None
    selected_policy_inventory: tuple | None
    selected_policy_inventory_cost: Fraction | None
    label_probabilities: tuple | None
    infeasible_pairs: tuple[Collision, ...]
    scope: str = "exact on the full declared finite table; label-conditioned batches only"

    @property
    def policy(self):
        """Fresh label-to-batch mapping; None explicitly marks an impossible fiber."""
        return {item.label: item.batch.selected for item in self.per_label}


def _guard(value, name, minimum):
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{name} must be an integer at least {minimum}.")


def _states(domain, maximum):
    states = tuple(islice(iter(domain), maximum + 1))
    if len(states) > maximum:
        raise ValueError("Domain exceeds the explicit finite-table size limit.")
    if not states:
        raise ValueError("The declared finite domain must be nonempty.")
    if any(state != state for state in states):
        raise ValueError("Domain states must have reflexive equality; NaN is not a valid state.")
    try:
        unique = set(states)
    except TypeError as exc:
        raise TypeError("Domain states must be hashable.") from exc
    if len(unique) != len(states):
        raise ValueError("The declared domain contains duplicate states.")
    return states


def _values(states, values, name):
    if not isinstance(values, Mapping) and not callable(values):
        raise TypeError(f"{name} must be a mapping or callable.")
    answer = {}
    for state in states:
        try:
            answer[state] = values[state] if isinstance(values, Mapping) else values(state)
        except KeyError as exc:
            raise IncompleteDomain(f"Missing {name} at {state!r}.") from exc
        if answer[state] != answer[state]:
            raise ValueError(f"{name} at {state!r} must have reflexive equality; NaN is invalid.")
    return answer


def _rational(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, str, Fraction)):
        raise TypeError(f"{name} must be an exact int, Fraction, or rational string; no floats.")
    try:
        number = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"{name} must be a finite exact rational.") from exc
    if number < 0:
        raise ValueError(f"{name} must be nonnegative.")
    return number


def _exact_keys(mapping, keys, name):
    if not isinstance(mapping, Mapping):
        raise TypeError(f"{name} must be a mapping.")
    expected, supplied = set(keys), set(mapping)
    if supplied != expected:
        missing = tuple(key for key in keys if key not in supplied)
        extra = tuple(key for key in mapping if key not in expected)
        raise IncompleteDomain(f"{name} must cover exactly the declared keys; missing={missing!r}, extra={extra!r}.")


def _weighted_optimum(states, retained, witness, coordinates, costs, maximum):
    """Reuse the existing bad-pair hitting engine, then optimize exact weights."""
    repair = coordinate_repairs(states, retained, witness, coordinates, max_coordinates=maximum)
    if not repair.feasible:
        edge = next(edge for edge in repair.edges if not edge.separating_coordinates)
        return BatchOptimum(False, None, None, repair.edges, edge.collision)
    names = tuple(coordinates)
    positions = {name: i for i, name in enumerate(names)}

    def rank(chosen):
        ordered = tuple(name for name in names if name in chosen)
        return (sum((costs[name] for name in ordered), Fraction(0)),
                len(ordered), tuple(positions[name] for name in ordered))

    # Nonnegative costs plus cardinality tie-breaking guarantee an optimum
    # among inclusion-minimal hitting sets, even when some costs are zero.
    best = min(repair.inclusion_minimal, key=rank)
    selected = tuple(name for name in names if name in best)
    return BatchOptimum(True, selected, rank(best)[0], repair.edges, None)


def label_conditioned_repairs(domain, retained, witness, coordinates, costs, *,
                              label_probabilities=None, max_coordinates=20,
                              max_states=256):
    """Return exact local batches, global fixed optimum, and acquisition costs.

    ``coordinates`` is an ordered mapping name -> total map/callable. ``costs``
    must contain exactly those names. Optional ``label_probabilities`` must
    contain every attained label, no others, and sum exactly to one. Omitting
    probabilities leaves expected_cost=None; no distribution is inferred.

    Ties use (exact cost, number of coordinates, menu-index tuple). Labels use
    first-occurrence order in domain. State and label objects must be hashable;
    coordinate and witness values need only support ordinary exact equality.

    The returned fixed optimum also gives *optimal* inventory cost. The union
    of independently chosen local optima can cost more; its cost is returned
    separately as selected_policy_inventory_cost. No inventory equality is
    asserted for that particular local-choice policy.

    If even one attained fiber is impossible, feasible=False, an actual pair
    certificate is returned for each impossible fiber, and all whole-domain
    policy costs are None. A zero label probability never hides that failure.
    Other fibers still receive their own optimum or certificate.
    """
    _guard(max_coordinates, "max_coordinates", 0)
    _guard(max_states, "max_states", 1)
    states = _states(domain, max_states)
    if not isinstance(coordinates, Mapping):
        raise TypeError("coordinates must be an ordered mapping of names to values.")
    names = tuple(coordinates)
    if len(names) > max_coordinates:
        raise ValueError("Coordinate menu exceeds the explicit exhaustive-search limit.")
    _exact_keys(costs, names, "costs")
    exact_costs = {name: _rational(costs[name], f"cost for {name!r}") for name in names}
    p = _values(states, retained, "retained label")
    w = _values(states, witness, "witness")
    c = {name: _values(states, coordinates[name], f"coordinate {name!r}") for name in names}
    fibers = {}
    for state in states:
        try:
            fibers.setdefault(p[state], []).append(state)
        except TypeError as exc:
            raise TypeError("Retained labels must be hashable.") from exc
    labels = tuple(fibers)
    probabilities = None
    if label_probabilities is not None:
        _exact_keys(label_probabilities, labels, "label_probabilities")
        probabilities = {q: _rational(label_probabilities[q], f"probability for {q!r}") for q in labels}
        if sum(probabilities.values(), Fraction(0)) != 1:
            raise ValueError("Label probabilities must sum exactly to one.")

    local = tuple(LabelOptimum(q, tuple(fiber),
                  _weighted_optimum(tuple(fiber), p, w, c, exact_costs, max_coordinates))
                  for q, fiber in fibers.items())
    fixed = _weighted_optimum(states, p, w, c, exact_costs, max_coordinates)
    failures = tuple(item.batch.infeasible_pair for item in local if not item.batch.feasible)
    if failures:
        return AcquisitionResult(False, labels, names, local, fixed, None, None,
            None, None, None, None if probabilities is None else tuple(probabilities.items()), failures)

    worst = max(item.batch.cost for item in local)
    expected = None if probabilities is None else sum(
        (probabilities[item.label] * item.batch.cost for item in local), Fraction(0))
    used = set().union(*(set(item.batch.selected) for item in local))
    inventory = tuple(name for name in names if name in used)
    inventory_cost = sum((exact_costs[name] for name in inventory), Fraction(0))
    return AcquisitionResult(True, labels, names, local, fixed, worst, expected,
        fixed.cost, inventory, inventory_cost,
        None if probabilities is None else tuple(probabilities.items()), ())


def synthetic_example():
    """Four manufactured states: fixed cost 2; label-conditioned cost 1."""
    domain = ("A0", "A1", "B0", "B1")
    retained = dict(zip(domain, ("A", "A", "B", "B")))
    witness = dict(zip(domain, (0, 1, 0, 1)))
    coordinates = {"c1": dict(zip(domain, (0, 1, 0, 0))),
                   "c2": dict(zip(domain, (0, 0, 0, 1)))}
    result = label_conditioned_repairs(domain, retained, witness, coordinates,
        {"c1": 1, "c2": 1}, label_probabilities={"A": "1/4", "B": "3/4"})
    return {"scope": result.scope, "data": "synthetic, not measured",
            "policy": result.policy, "fixed_coordinates": result.fixed.selected,
            "fixed_cost": str(result.fixed.cost), "worst_cost": str(result.worst_cost),
            "expected_cost": str(result.expected_cost),
            "optimal_inventory_cost": str(result.optimal_inventory_cost),
            "selected_policy_inventory_cost": str(result.selected_policy_inventory_cost)}


if __name__ == "__main__":
    import json
    print(json.dumps(synthetic_example(), indent=2))
