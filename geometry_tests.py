"""Exact tests. All data below are synthetic finite mathematical examples."""
import importlib.util
import itertools
import json
import sys
import time
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('geometry_engine', ROOT / 'geometry_engine.py')
G = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G
SPEC.loader.exec_module(G)


def all_maps(domain, values):
    for row in itertools.product(values, repeat=len(domain)):
        yield dict(zip(domain, row))


def equivalent_pairs(domain, blocks):
    ids = {x: i for i, block in enumerate(blocks) for x in block}
    return {(x, y) for x in domain for y in domain if ids[x] == ids[y]}


class GeometryTests(unittest.TestCase):
    cases = {}

    def test_D1_product_union_exhaustive(self):
        d = (0, 1, 2)
        maps = list(all_maps(d, (0, 1)))
        count = 0
        for p, a, b in itertools.product(maps, repeat=3):
            pair = {x: (a[x], b[x]) for x in d}
            self.assertEqual(set(G.non_descent(d, p, pair)),
                             set(G.non_descent(d, p, a)) | set(G.non_descent(d, p, b)))
            count += 1
        self.cases['D1'] = count

    def test_D2_witness_coarsening_exhaustive(self):
        d = (0, 1, 2)
        count = 0
        for p, w, f in itertools.product(all_maps(d, (0, 1)), all_maps(d, (0, 1)), all_maps((0, 1), (0, 1))):
            coarse = {x: f[w[x]] for x in d}
            self.assertLessEqual(set(G.non_descent(d, p, coarse)), set(G.non_descent(d, p, w)))
            count += 1
        self.cases['D2'] = count

    def test_D3_observation_refinement_exhaustive(self):
        d = (0, 1, 2)
        count = 0
        for refined, r, w in itertools.product(all_maps(d, d), all_maps(d, (0, 1)), all_maps(d, (0, 1))):
            p = {x: r[refined[x]] for x in d}
            projected_bad = {r[q] for q in G.non_descent(d, refined, w)}
            self.assertLessEqual(projected_bad, set(G.non_descent(d, p, w)))
            count += 1
        self.cases['D3'] = count

    def test_D4_domain_restriction_exhaustive(self):
        d = (0, 1, 2)
        count = 0
        for p, w, mask in itertools.product(all_maps(d, (0, 1)), all_maps(d, (0, 1)), range(8)):
            c = tuple(x for x in d if mask & (1 << x))
            self.assertLessEqual(set(G.non_descent(c, p, w)),
                                 set(G.non_descent(d, p, w)) & {p[x] for x in c})
            count += 1
        self.cases['D4'] = count

    def test_D5_autonomy_and_exact_factor(self):
        d = (0, 1, 2)
        count = 0
        for p, u in itertools.product(all_maps(d, (0, 1)), all_maps(d, d)):
            next_label = {x: p[u[x]] for x in d}
            autonomous = all(p[x] != p[y] or next_label[x] == next_label[y] for x in d for y in d)
            self.assertEqual(not G.non_descent(d, p, next_label), autonomous)
            if autonomous:
                factor = G.factor_map(d, p, next_label)
                self.assertTrue(all(factor[p[x]] == p[u[x]] for x in d))
            else:
                with self.assertRaises(G.DescentFailure):
                    G.factor_map(d, p, next_label)
            count += 1
        self.cases['D5'] = count

    def test_collision_certificate_and_canonical_repair(self):
        p = {0: 'q', 1: 'q', 2: 'r'}
        w = {0: 'left', 1: 'right', 2: 'other'}
        bad = G.non_descent((0, 1, 2), p, w)
        self.assertEqual(set(bad), {'q'})
        certificate = bad['q']
        self.assertEqual(p[certificate.left], p[certificate.right])
        self.assertNotEqual(w[certificate.left], w[certificate.right])
        refined = G.canonical_refinement((0, 1, 2), p, w)
        self.assertFalse(G.non_descent((0, 1, 2), refined, w))

    def test_predictive_compiler_against_finite_future_equivalence(self):
        d = (0, 1, 2)
        count = 0
        for b, u in itertools.product(all_maps(d, (0, 1)), all_maps(d, d)):
            result = G.deterministic_predictive_partition(d, b, u)
            words = {}
            for x in d:
                state, word = x, []
                for _ in range(len(d)):
                    word.append(b[state])
                    state = u[state]
                words[x] = tuple(word)
            expected = {(x, y) for x in d for y in d if words[x] == words[y]}
            self.assertEqual(equivalent_pairs(d, result.blocks), expected)
            self.assertLessEqual(result.strict_refinements, len(d) - len(set(b.values())))
            count += 1
        self.cases['deterministic_compiler'] = count

    def test_delayed_split_and_compressible_cycle(self):
        self.assertEqual(G.synthetic_demo()['delayed_split_class_counts'], (2, 3, 4))
        result = G.deterministic_predictive_partition(range(4), lambda x: x % 2, lambda x: (x + 1) % 4)
        self.assertEqual(result.class_counts, (2,))
        self.assertEqual(set(result.blocks), {frozenset((0, 2)), frozenset((1, 3))})

    def test_missing_data_rejected_not_patched(self):
        with self.assertRaises(G.IncompleteDomain):
            G.deterministic_predictive_partition((0, 1), {0: 0, 1: 1}, {0: 1})
        with self.assertRaises(G.IncompleteDomain):
            G.deterministic_predictive_partition((0, 1), {0: 0, 1: 1}, {0: 1, 1: 2})
        with self.assertRaises(G.IncompleteDomain):
            G.non_descent((0, 1), {0: 0}, {0: 0, 1: 1})
        with self.assertRaises(ValueError):
            G.non_descent((0, 0), {0: 0}, {0: 0})

    def test_stochastic_future_law_equivalence_need_not_be_lumpable(self):
        d = ('x', 'y', 'u', 'v', 'w', 'c', 'd')
        b = dict(zip(d, ('A', 'A', 'B', 'B', 'B', 'C', 'D')))
        half = Fraction(1, 2)
        p = {'x': {'u': half, 'v': half}, 'y': {'w': 1},
             'u': {'c': 1}, 'v': {'d': 1}, 'w': {'c': half, 'd': half},
             'c': {'c': 1}, 'd': {'d': 1}}
        result = G.strong_lumpable_partition(d, b, p)
        self.assertEqual(result.class_counts, (4, 6, 7))
        def words(start, horizon):
            running = {(start, (b[start],)): Fraction(1)}
            for _ in range(horizon):
                following = {}
                for (state, word), mass in running.items():
                    for nxt, probability in p[state].items():
                        key = (nxt, word + (b[nxt],))
                        following[key] = following.get(key, 0) + mass * probability
                running = following
            result = {}
            for (_, word), mass in running.items():
                result[word] = result.get(word, 0) + mass
            return result
        for horizon in range(9):
            self.assertEqual(words('x', horizon), words('y', horizon))
        # Infinite equality follows from the two absorbing endpoints, not this loop.
        self.assertEqual(p['x'].get('u', 0), half)
        self.assertEqual(p['y'].get('u', 0), 0)

    def test_strong_compiler_coarsest_by_partition_enumeration(self):
        d = (0, 1, 2)
        half = Fraction(1, 2)
        row_options = ({0: 1}, {1: 1}, {2: 1}, {0: half, 1: half})
        candidate_partitions = ((frozenset(d),),
            (frozenset((0,)), frozenset((1, 2))),
            (frozenset((1,)), frozenset((0, 2))),
            (frozenset((2,)), frozenset((0, 1))),
            (frozenset((0,)), frozenset((1,)), frozenset((2,))))
        count = 0
        for b, rows in itertools.product(all_maps(d, (0, 1)), itertools.product(row_options, repeat=3)):
            p = dict(zip(d, rows))
            result = G.strong_lumpable_partition(d, b, p)
            relation = equivalent_pairs(d, result.blocks)
            for candidate in candidate_partitions:
                pairs = equivalent_pairs(d, candidate)
                respects = all(b[x] == b[y] for x, y in pairs)
                stable = all(sum((p[x].get(z, 0) for z in block), Fraction(0)) ==
                             sum((p[y].get(z, 0) for z in block), Fraction(0))
                             for x, y in pairs for block in candidate)
                if respects and stable:
                    self.assertLessEqual(pairs, relation)
            self.assertTrue(all(b[x] == b[y] for x, y in relation))
            for x, y in relation:
                for block in result.blocks:
                    self.assertEqual(sum(p[x].get(z, 0) for z in block), sum(p[y].get(z, 0) for z in block))
            count += 1
        self.cases['strong_lumpability_compiler'] = count

    def test_kernel_invalid_and_inexact_rows_rejected(self):
        for kernel in ({0: {0: '1/2'}}, {0: {1: 1}}, {}):
            with self.assertRaises(G.IncompleteDomain):
                G.strong_lumpable_partition((0,), {0: 0}, kernel)
        with self.assertRaises(TypeError):
            G.strong_lumpable_partition((0,), {0: 0}, {0: {0: 1.0}})

    def test_coordinate_repairs_against_direct_descent(self):
        d = (0, 1, 2)
        p = {x: 0 for x in d}
        count = 0
        for w, a, b in itertools.product(all_maps(d, (0, 1)), repeat=3):
            coordinates = {'a': a, 'b': b}
            result = G.coordinate_repairs(d, p, w, coordinates)
            feasible = []
            for size in range(3):
                for subset in itertools.combinations(coordinates, size):
                    observation = {x: (p[x], tuple(coordinates[j][x] for j in subset)) for x in d}
                    if not G.non_descent(d, observation, w):
                        feasible.append(frozenset(subset))
            minimal = {s for s in feasible if not any(t < s for t in feasible)}
            self.assertEqual(set(result.inclusion_minimal), minimal)
            self.assertEqual(result.feasible, bool(feasible))
            if feasible:
                smallest = min(map(len, feasible))
                self.assertEqual(set(result.minimum_cardinality), {s for s in feasible if len(s) == smallest})
            count += 1
        self.cases['coordinate_repairs'] = count

    def test_inclusion_minimal_is_not_minimum_and_unavailable_repair(self):
        demo = G.synthetic_demo()
        self.assertEqual(demo['inclusion_minimal_repairs'], [['a'], ['b', 'c']])
        self.assertEqual(demo['minimum_cardinality_repairs'], [['a']])
        result = G.coordinate_repairs((0, 1), {0: 0, 1: 0}, {0: 0, 1: 1}, {'constant': {0: 0, 1: 0}})
        self.assertFalse(result.feasible)
        self.assertFalse(result.edges[0].separating_coordinates)

    def test_empty_domain_is_vacuous(self):
        self.assertEqual(G.factor_map((), {}, {}), {})
        self.assertEqual(G.deterministic_predictive_partition((), {}, {}).blocks, ())
        self.assertEqual(G.strong_lumpable_partition((), {}, {}).blocks, ())
        self.assertEqual(G.coordinate_repairs((), {}, {}, {}).inclusion_minimal, (frozenset(),))

    def test_minimax_simplex_and_finite_horizon_bound_exact_examples(self):
        for m in range(2, 9):
            radius = 1 - Fraction(1, m)
            uniform = [Fraction(1, m)] * m
            for i in range(m):
                delta = [Fraction(int(i == j)) for j in range(m)]
                distance = sum(abs(a-b) for a, b in zip(delta, uniform)) / 2
                self.assertEqual(distance, radius)
        for epsilon in (Fraction(0), Fraction(1, 10), Fraction(1, 2), Fraction(1)):
            for h in range(1, 9):
                error = 1 - (1 - epsilon) ** h
                self.assertLessEqual(error, min(1, h * epsilon))
                # In the absorbing two-label example, the wrong-model path stays
                # all-zero with probability (1-epsilon)^h: the bound is attained.
                self.assertEqual(error + (1-epsilon) ** h, 1)


if __name__ == '__main__':
    started = time.perf_counter()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(GeometryTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    receipt = {
        'status': 'PASS' if result.wasSuccessful() else 'FAIL',
        'scope': 'Exact synthetic finite examples and exhaustive small declared tables only.',
        'python_version': sys.version.split()[0],
        'test_methods': result.testsRun,
        'failures': len(result.failures),
        'errors': len(result.errors),
        'exhaustive_case_counts': GeometryTests.cases,
        'exhaustive_cases_total': sum(GeometryTests.cases.values()),
        'duration_seconds': round(time.perf_counter() - started, 4),
        'demonstration': G.synthetic_demo(),
        'historical_replay_performed': False,
        'physical_experiment_performed': False,
        'temporal_experiment_performed': False,
        'limitations': ['No finite test proves an unrestricted theorem.',
            'Declared table completeness does not establish empirical coverage.',
            'Coordinate repair search is exponential and menu-relative.',
            'Strong lumpability is different from history-level finite Markov order.']}
    (ROOT / 'geometry_verification.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
    sys.exit(0 if result.wasSuccessful() else 1)
