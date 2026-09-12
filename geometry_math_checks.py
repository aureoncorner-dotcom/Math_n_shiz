"""Independent synthetic hypergraph checks for label-conditioned batch repair."""
from fractions import Fraction
from itertools import product

subsets = tuple(frozenset(j for j in range(2) if mask & (1 << j)) for mask in range(4))
families = tuple(tuple(subsets[i] for i in range(4) if mask & (1 << i)) for mask in range(16))
costs = ((0, 0), (0, 1), (1, 0), (1, 1), (1, 3), (2, 5))
probabilities = ((Fraction(0), Fraction(1)), (Fraction(1, 4), Fraction(3, 4)), (Fraction(1), Fraction(0)))

def hits(chosen, family):
    return all(chosen & edge for edge in family)

feasible_count = impossible_count = comparisons = 0
for pair in product(families, repeat=2):
    policies = [(a, b) for a, b in product(subsets, repeat=2)
                if hits(a, pair[0]) and hits(b, pair[1])]
    if not policies:
        impossible_count += 1
        assert any(frozenset() in family for family in pair)
        continue
    feasible_count += 1
    for prices in costs:
        cost = lambda chosen: sum(prices[j] for j in chosen)
        local = [min(cost(chosen) for chosen in subsets if hits(chosen, family)) for family in pair]
        fixed = min(cost(chosen) for chosen in subsets if all(hits(chosen, family) for family in pair))
        worst = min(max(cost(a), cost(b)) for a, b in policies)
        inventory = min(cost(a | b) for a, b in policies)
        assert worst == max(local)
        assert inventory == fixed
        assert worst <= fixed <= sum(local) <= 2 * worst
        for p in probabilities:
            expected = min(p[0] * cost(a) + p[1] * cost(b) for a, b in policies)
            assert expected == sum(weight * minimum for weight, minimum in zip(p, local))
            assert expected <= worst
            comparisons += 1

# Zero-probability bad fiber still invalidates an exact whole-domain claim.
pair = ((frozenset(),), ())
assert not [(a, b) for a, b in product(subsets, repeat=2) if hits(a, pair[0]) and hits(b, pair[1])]

# Independently chosen local optima need not optimize installed inventory.
pair = ((frozenset((0, 1)),), (frozenset((0, 1)),))
assert hits(frozenset((0,)), pair[0]) and hits(frozenset((1,)), pair[1])
assert len(frozenset((0,)) | frozenset((1,))) == 2
assert min(len(chosen) for chosen in subsets if all(hits(chosen, f) for f in pair)) == 1

print({'status': 'PASS', 'synthetic_family_pairs': len(families) ** 2,
       'globally_feasible_pairs': feasible_count, 'globally_impossible_pairs': impossible_count,
       'cost_profiles': len(costs), 'probability_profiles': len(probabilities),
       'objective_comparisons': comparisons,
       'scope': 'Independent finite hypergraph and edge-case checks; no source experiment rerun.'})
