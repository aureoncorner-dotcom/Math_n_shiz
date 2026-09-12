"""Focused boundary and exact-certificate tests for the adaptive companion."""
import hashlib
import itertools
from fractions import Fraction
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from geometry_adaptive import label_conditioned_repairs, synthetic_example
from geometry_engine import IncompleteDomain


class AdaptiveRepairTests(unittest.TestCase):
    def setUp(self):
        self.domain = ("A0", "A1", "B0", "B1")
        self.q = dict(zip(self.domain, ("A", "A", "B", "B")))
        self.w = dict(zip(self.domain, (0, 1, 0, 1)))
        self.c = {"c1": dict(zip(self.domain, (0, 1, 0, 0))),
                  "c2": dict(zip(self.domain, (0, 0, 0, 1)))}
        self.costs = {"c1": 1, "c2": 1}

    def solve(self, **overrides):
        arguments = dict(domain=self.domain, retained=self.q, witness=self.w,
                         coordinates=self.c, costs=self.costs)
        arguments.update(overrides)
        return label_conditioned_repairs(**arguments)

    def validate_all_labels(self, result, domain=None, q=None, w=None, c=None):
        domain, q, w, c = domain or self.domain, q or self.q, w or self.w, c or self.c
        self.assertEqual(result.labels, tuple(dict.fromkeys(q[x] for x in domain)))
        self.assertEqual(set(result.policy), set(result.labels))
        self.assertEqual(set(itertools.chain.from_iterable(item.states for item in result.per_label)), set(domain))
        for item in result.per_label:
            self.assertTrue(item.batch.feasible)
            for x, y in itertools.combinations(item.states, 2):
                self.assertEqual(q[x], item.label)
                self.assertEqual(q[y], item.label)
                if w[x] != w[y]:
                    self.assertTrue(any(c[j][x] != c[j][y] for j in item.batch.selected))
        for x, y in itertools.combinations(domain, 2):
            if q[x] == q[y] and w[x] != w[y]:
                self.assertTrue(any(c[j][x] != c[j][y] for j in result.fixed.selected))

    def test_four_state_strict_gain_and_every_label(self):
        result = self.solve(label_probabilities={"A": "1/4", "B": "3/4"})
        self.assertTrue(result.feasible)
        self.assertEqual(result.policy, {"A": ("c1",), "B": ("c2",)})
        self.assertEqual(result.fixed.selected, ("c1", "c2"))
        self.assertEqual((result.fixed.cost, result.worst_cost, result.expected_cost), (2, 1, 1))
        self.assertEqual(result.optimal_inventory_cost, result.fixed.cost)
        self.validate_all_labels(result)

    def test_probabilities_are_optional_not_assumed_uniform(self):
        result = self.solve()
        self.assertIsNone(result.expected_cost)
        self.assertIsNone(result.label_probabilities)
        self.assertEqual(result.worst_cost, 1)

    def test_exact_fraction_costs_and_probabilities(self):
        result = self.solve(costs={"c1": "1/3", "c2": Fraction(5, 7)},
                            label_probabilities={"A": Fraction(1, 4), "B": "3/4"})
        self.assertEqual(result.fixed.cost, Fraction(22, 21))
        self.assertEqual(result.worst_cost, Fraction(5, 7))
        self.assertEqual(result.expected_cost, Fraction(13, 21))
        self.assertIsInstance(result.expected_cost, Fraction)
        self.validate_all_labels(result)

    def test_zero_costs_do_not_require_redundant_coordinates(self):
        result = self.solve(costs={"c1": 0, "c2": 0})
        self.assertEqual(result.policy, {"A": ("c1",), "B": ("c2",)})
        self.assertEqual(result.fixed.cost, 0)
        self.validate_all_labels(result)

    def test_empty_menu_constant_witness(self):
        result = self.solve(witness={x: 9 for x in self.domain}, coordinates={}, costs={})
        self.assertTrue(result.feasible)
        self.assertEqual(result.policy, {"A": (), "B": ()})
        self.assertEqual(result.fixed.selected, ())
        self.assertEqual(result.fixed.cost, 0)

    def test_empty_menu_different_values_between_labels_already_descend(self):
        result = self.solve(witness=self.q, coordinates={}, costs={})
        self.assertTrue(result.feasible)
        self.assertEqual(result.worst_cost, 0)

    def test_empty_menu_impossible_returns_real_pair(self):
        result = self.solve(coordinates={}, costs={})
        self.assertFalse(result.feasible)
        self.assertEqual(len(result.infeasible_pairs), 2)
        for pair in result.infeasible_pairs:
            self.assertEqual(self.q[pair.left], self.q[pair.right])
            self.assertNotEqual(self.w[pair.left], self.w[pair.right])
        self.assertEqual(result.policy, {"A": None, "B": None})

    def test_one_label_fixed_and_label_costs_coincide(self):
        q = {x: "only" for x in self.domain}
        result = self.solve(retained=q, label_probabilities={"only": 1})
        self.assertEqual(result.fixed.cost, result.worst_cost)
        self.assertEqual(result.expected_cost, result.worst_cost)
        self.validate_all_labels(result, q=q)

    def test_zero_probability_labels_still_repaired(self):
        result = self.solve(costs={"c1": 1, "c2": 100}, label_probabilities={"A": 1, "B": 0})
        self.assertTrue(result.feasible)
        self.assertEqual(result.expected_cost, 1)
        self.assertEqual(result.worst_cost, 100)
        self.assertEqual(result.policy["B"], ("c2",))
        self.validate_all_labels(result)

    def test_impossible_zero_probability_fiber_invalidates_all_domain(self):
        c = {"c1": self.c["c1"]}
        result = self.solve(coordinates=c, costs={"c1": 1}, label_probabilities={"A": 1, "B": 0})
        self.assertFalse(result.feasible)
        self.assertEqual(result.policy, {"A": ("c1",), "B": None})
        self.assertEqual(len(result.infeasible_pairs), 1)
        pair = result.infeasible_pairs[0]
        self.assertEqual((pair.label, pair.left, pair.right), ("B", "B0", "B1"))
        self.assertNotEqual(pair.left_value, pair.right_value)
        self.assertEqual(c["c1"][pair.left], c["c1"][pair.right])
        self.assertFalse(result.fixed.feasible)
        for name in ("worst_cost", "expected_cost", "optimal_inventory_cost",
                     "selected_policy_inventory_cost", "selected_policy_inventory"):
            self.assertIsNone(getattr(result, name))

    def test_local_policy_inventory_can_exceed_optimal_inventory(self):
        c = dict(self.c)
        c["common"] = self.w.copy()
        result = self.solve(coordinates=c, costs={"c1": 1, "c2": 1, "common": 1})
        self.assertEqual(result.policy, {"A": ("c1",), "B": ("c2",)})
        self.assertEqual(result.selected_policy_inventory_cost, 2)
        self.assertEqual(result.fixed.selected, ("common",))
        self.assertEqual(result.optimal_inventory_cost, 1)
        self.validate_all_labels(result, c=c)

    def test_deterministic_tie_uses_menu_order_not_sortable_names(self):
        names = (7, "first", ("tuple",))
        c = {name: self.w for name in names}
        result = self.solve(coordinates=c, costs={name: 1 for name in names})
        self.assertEqual(result.coordinate_order, names)
        self.assertEqual(result.fixed.selected, (7,))
        self.assertEqual(result.policy, {"A": (7,), "B": (7,)})

    def test_equal_cost_tie_chooses_fewer_coordinates(self):
        c = dict(self.c)
        c["common"] = self.w.copy()
        result = self.solve(coordinates=c, costs={"c1": 1, "c2": 1, "common": 2})
        self.assertEqual(result.fixed.selected, ("common",))
        self.assertEqual(result.fixed.cost, 2)

    def test_labels_use_first_occurrence(self):
        result = self.solve(domain=tuple(reversed(self.domain)))
        self.assertEqual(result.labels, ("B", "A"))
        self.assertEqual(tuple(result.policy), ("B", "A"))

    def test_callables_evaluated_once(self):
        calls = {"q": 0, "w": 0, "c1": 0, "c2": 0}
        def wrapped(name, values):
            def read(x):
                calls[name] += 1
                return values[x]
            return read
        result = self.solve(retained=wrapped("q", self.q), witness=wrapped("w", self.w),
                            coordinates={j: wrapped(j, values) for j, values in self.c.items()})
        self.assertTrue(result.feasible)
        self.assertEqual(calls, {"q": 4, "w": 4, "c1": 4, "c2": 4})

    def test_unhashable_witness_and_coordinate_values_use_equality(self):
        w = {x: [self.w[x]] for x in self.domain}
        c = {j: {x: [values[x]] for x in self.domain} for j, values in self.c.items()}
        result = self.solve(witness=w, coordinates=c)
        self.assertEqual(result.fixed.cost, 2)
        self.validate_all_labels(result, w=w, c=c)

    def test_invalid_cost_values(self):
        for value in (True, False, .5, float("nan"), float("inf"), object(), -1, "-1/2", "NaN", "1/0"):
            with self.subTest(value=value), self.assertRaises((TypeError, ValueError)):
                self.solve(costs={"c1": value, "c2": 1})

    def test_missing_extra_and_nonmapping_costs(self):
        for costs in ({"c1": 1}, {"c1": 1, "c2": 1, "extra": 1}, [1, 1]):
            with self.subTest(costs=costs), self.assertRaises((TypeError, IncompleteDomain)):
                self.solve(costs=costs)

    def test_invalid_probabilities(self):
        for probabilities in ({"A": 1}, {"A": 1, "B": 0, "extra": 0}, {"A": .25, "B": .75},
                              {"A": True, "B": 0}, {"A": "-1/2", "B": "3/2"},
                              {"A": "1/3", "B": "1/3"}, {"A": 0, "B": 0}, [1, 0]):
            with self.subTest(probabilities=probabilities), self.assertRaises((TypeError, ValueError)):
                self.solve(label_probabilities=probabilities)

    def test_incomplete_table_is_rejected_even_on_zero_probability_label(self):
        c = {"c1": self.c["c1"], "c2": {x: 0 for x in self.domain if x != "B1"}}
        with self.assertRaises(IncompleteDomain):
            self.solve(coordinates=c, label_probabilities={"A": 1, "B": 0})

    def test_invalid_domain_and_labels(self):
        for domain in ((), ("A0", "A0"), ([0],), (float("nan"),)):
            with self.subTest(domain=domain), self.assertRaises((TypeError, ValueError)):
                self.solve(domain=domain)
        with self.assertRaises(TypeError):
            self.solve(retained={x: [] for x in self.domain})
        with self.assertRaises(ValueError):
            self.solve(witness={x: float("nan") for x in self.domain})
        with self.assertRaises(IncompleteDomain):
            self.solve(retained={"A0": "A"})

    def test_guards_bound_exhaustive_search_and_generator_consumption(self):
        with self.assertRaises(ValueError):
            self.solve(max_coordinates=1)
        with self.assertRaises(ValueError):
            self.solve(max_states=3)
        with self.assertRaises(ValueError):
            self.solve(domain=itertools.count(), max_states=4)
        for value in (-1, True, 1.5):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.solve(max_coordinates=value)

    def test_example_is_reusable_and_synthetic(self):
        example = synthetic_example()
        self.assertEqual(example["fixed_cost"], "2")
        self.assertEqual(example["expected_cost"], "1")
        self.assertIn("synthetic", example["data"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
