"""Finite witness geometry: exact checks on a caller-declared finite domain.

Python standard library only. Hashable states, labels and coordinate names are
required. Values may be mappings or callables; every value is evaluated once.
Completeness of the declared table is checked. Whether that domain exhausts a
physical or historical system is a separate evidential question.

No empirical, historical, toroidal or temporal experiment is performed here.
"""

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from collections.abc import Mapping


class IncompleteDomain(ValueError):
    """A required value, successor or probability row is missing or invalid."""


class DescentFailure(ValueError):
    def __init__(self, collisions):
        self.collisions = collisions
        super().__init__("Witness does not descend on the declared domain.")


@dataclass(frozen=True)
class Collision:
    label: object
    left: object
    right: object
    left_value: object
    right_value: object


@dataclass(frozen=True)
class PartitionResult:
    blocks: tuple
    strict_refinements: int
    class_counts: tuple


@dataclass(frozen=True)
class RepairEdge:
    collision: Collision
    separating_coordinates: frozenset


@dataclass(frozen=True)
class RepairResult:
    feasible: bool
    inclusion_minimal: tuple
    minimum_cardinality: tuple
    edges: tuple


def _domain(domain):
    states = tuple(domain)
    if len(set(states)) != len(states):
        raise ValueError("The declared domain contains duplicate states.")
    return states


def _values(states, values, name):
    if not isinstance(values, Mapping) and not callable(values):
        raise TypeError(f"{name} must be a mapping or callable.")
    answer = {}
    for x in states:
        try:
            answer[x] = values[x] if isinstance(values, Mapping) else values(x)
        except KeyError as exc:
            raise IncompleteDomain(f"Missing {name} at {x!r}.") from exc
    return answer


def _collisions(states, retained, witness):
    first, bad = {}, {}
    for x in states:
        q = retained[x]
        if q not in first:
            first[q] = x
        elif q not in bad and witness[first[q]] != witness[x]:
            y = first[q]
            bad[q] = Collision(q, y, x, witness[y], witness[x])
    return bad


def non_descent(domain, retained, witness):
    """Return one actual collision certificate per bad attained label."""
    states = _domain(domain)
    p = _values(states, retained, "retained label")
    w = _values(states, witness, "witness")
    return _collisions(states, p, w)


def factor_map(domain, retained, witness):
    """Return the unique attained-label factor, or raise DescentFailure."""
    states = _domain(domain)
    p = _values(states, retained, "retained label")
    w = _values(states, witness, "witness")
    bad = _collisions(states, p, w)
    if bad:
        raise DescentFailure(bad)
    return {p[x]: w[x] for x in states}


def canonical_refinement(domain, retained, witness):
    """Return x -> (retained(x), witness(x)); no mechanistic claim is implied."""
    states = _domain(domain)
    p = _values(states, retained, "retained label")
    w = _values(states, witness, "witness")
    return {x: (p[x], w[x]) for x in states}


def _partition(states, signature):
    groups = {}
    for x in states:
        groups.setdefault(signature[x], []).append(x)
    return tuple(frozenset(group) for group in groups.values())


def _block_ids(blocks):
    return {x: i for i, block in enumerate(blocks) for x in block}


def deterministic_predictive_partition(domain, output, update):
    """Coarsest autonomous partition retaining output, on the entire table.

    Stable partition equality concerns equivalence classes, not label spelling.
    Missing successors are rejected; no terminal self-loop is manufactured.
    """
    states = _domain(domain)
    b = _values(states, output, "output")
    u = _values(states, update, "successor")
    universe = set(states)
    if any(u[x] not in universe for x in states):
        raise IncompleteDomain("Update leaves the declared finite domain.")
    blocks = _partition(states, b)
    counts = [len(blocks)]
    while True:
        ids = _block_ids(blocks)
        refined = _partition(states, {x: (ids[x], ids[u[x]]) for x in states})
        if refined == blocks:
            return PartitionResult(blocks, len(counts) - 1, tuple(counts))
        blocks = refined
        counts.append(len(blocks))


def _probability(value):
    if isinstance(value, bool) or not isinstance(value, (int, str, Fraction)):
        raise TypeError("Use exact int, Fraction or rational-string probabilities; no floats.")
    probability = Fraction(value)
    if probability < 0:
        raise IncompleteDomain("A transition probability is negative.")
    return probability


def strong_lumpable_partition(domain, output, kernel):
    """Coarsest strongly lumpable refinement retaining output.

    Each state needs a row mapping target states to exact probabilities. Missing
    targets within a supplied row mean zero. Rows must sum to exactly one.
    This is universal strong lumpability, not a stationary-data Markov test.
    """
    states = _domain(domain)
    b = _values(states, output, "output")
    supplied = _values(states, kernel, "kernel row")
    universe = set(states)
    rows = {}
    for x in states:
        if not isinstance(supplied[x], Mapping):
            raise TypeError("Each kernel row must be a mapping.")
        if set(supplied[x]) - universe:
            raise IncompleteDomain("Kernel has a target outside the declared domain.")
        rows[x] = {y: _probability(p) for y, p in supplied[x].items()}
        if sum(rows[x].values(), Fraction(0)) != 1:
            raise IncompleteDomain(f"Kernel row for {x!r} does not sum to one.")
    blocks = _partition(states, b)
    counts = [len(blocks)]
    while True:
        ids = _block_ids(blocks)
        signatures = {}
        for x in states:
            totals = [Fraction(0)] * len(blocks)
            for y, probability in rows[x].items():
                totals[ids[y]] += probability
            signatures[x] = (ids[x], tuple(totals))
        refined = _partition(states, signatures)
        if refined == blocks:
            return PartitionResult(blocks, len(counts) - 1, tuple(counts))
        blocks = refined
        counts.append(len(blocks))


def coordinate_repairs(domain, retained, witness, coordinates, *, max_coordinates=20):
    """Enumerate inclusion-minimal and smallest repairs from a finite menu.

    A repair intersects every separating-coordinate edge for a same-label,
    different-witness pair. An empty edge certifies that the menu cannot repair
    the declared domain. Enumeration is exponential; the explicit size guard
    can be raised by the caller. A minimum is menu-relative and domain-relative.
    """
    states = _domain(domain)
    if not isinstance(coordinates, Mapping):
        raise TypeError("coordinates must map names to coordinate maps.")
    names = tuple(coordinates)
    if len(names) > max_coordinates:
        raise ValueError("Coordinate menu exceeds the explicit exhaustive-search limit.")
    p = _values(states, retained, "retained label")
    w = _values(states, witness, "witness")
    c = {name: _values(states, values, f"coordinate {name!r}")
         for name, values in coordinates.items()}
    edges = []
    for x, y in combinations(states, 2):
        if p[x] == p[y] and w[x] != w[y]:
            separates = frozenset(name for name in names if c[name][x] != c[name][y])
            edges.append(RepairEdge(Collision(p[x], x, y, w[x], w[y]), separates))
    if any(not edge.separating_coordinates for edge in edges):
        return RepairResult(False, (), (), tuple(edges))
    minimal = []
    for size in range(len(names) + 1):
        for chosen in combinations(names, size):
            subset = frozenset(chosen)
            if any(previous <= subset for previous in minimal):
                continue
            if all(subset & edge.separating_coordinates for edge in edges):
                minimal.append(subset)
    smallest = min(map(len, minimal))
    best = tuple(subset for subset in minimal if len(subset) == smallest)
    return RepairResult(True, tuple(minimal), best, tuple(edges))


def synthetic_demo():
    """Small manufactured examples; these are not observations of a live system."""
    domain = (0, 1, 2, 3)
    delayed = deterministic_predictive_partition(
        domain, {0: 0, 1: 0, 2: 0, 3: 1}, {0: 1, 1: 2, 2: 3, 3: 3})
    repair = coordinate_repairs((0, 1, 2), {0: 'q', 1: 'q', 2: 'q'},
        {0: 0, 1: 1, 2: 1},
        {'a': {0: 0, 1: 1, 2: 1}, 'b': {0: 0, 1: 1, 2: 0},
         'c': {0: 0, 1: 0, 2: 1}})
    return {'scope': 'synthetic finite examples only',
            'delayed_split_class_counts': delayed.class_counts,
            'inclusion_minimal_repairs': [sorted(s) for s in repair.inclusion_minimal],
            'minimum_cardinality_repairs': [sorted(s) for s in repair.minimum_cardinality]}


if __name__ == '__main__':
    import json
    print(json.dumps(synthetic_demo(), indent=2))
