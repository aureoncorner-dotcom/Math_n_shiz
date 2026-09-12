"""Independent finite verification of label-conditioned coordinate acquisition.

This script implements no source-package APIs and imports no existing geometry
engine. It compares explicit retained-record collisions with independently
constructed bad-pair hitting conditions and exhaustive batch policies.
"""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
SOURCE_REVIEW = ROOT / 'Geometry_Adaptive_Repair_Source.md'
SOURCE_RECEIPT = ROOT / 'geometry_adaptive_source_receipt.json'
DESTINATION = ROOT / 'GEOMETRY_v2.5_Verification.json'


def exact_from_records(labels, target, coordinates, masks):
    """Direct criterion: equal acquired records must have equal target values."""
    seen = {}
    for state, label in enumerate(labels):
        mask = masks[label]
        record = (label, tuple((j, column[state]) for j, column in enumerate(coordinates) if mask & (1 << j)))
        if record in seen and seen[record] != target[state]:
            return False
        seen[record] = target[state]
    return True


def bad_pair_families(labels, target, coordinates):
    """Construct the alternative combinatorial condition from explicit pairs."""
    families = {q: set() for q in set(labels)}
    for x, y in combinations(range(len(labels)), 2):
        if labels[x] == labels[y] and target[x] != target[y]:
            edge = frozenset(j for j, column in enumerate(coordinates) if column[x] != column[y])
            families[labels[x]].add(edge)
    return families


def hits(mask, family):
    selected = {j for j in range(mask.bit_length()) if mask & (1 << j)}
    return all(selected.intersection(edge) for edge in family)


def mask_cost(mask, costs):
    return sum(cost for j, cost in enumerate(costs) if mask & (1 << j))


def minimum_or_none(values):
    return min(values, default=None)


def fraction_text(value):
    if value is None:
        return None
    return str(value)


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def exhaustive_four_state():
    labels = ('A', 'A', 'B', 'B')
    costs_all = ((1, 1), (1, 3), (0, 2))
    probabilities = {'A': Fraction(1, 4), 'B': Fraction(3, 4)}
    all_columns = tuple(product((0, 1), repeat=4))
    candidate_masks = range(4)
    policies = tuple({'A': a, 'B': b} for a, b in product(candidate_masks, repeat=2))
    counts = Counter()
    objective_fields = ('fixed', 'label_worst', 'label_expected', 'inventory')
    totals_by_profile = {}
    digest = sha256()

    for target, c1, c2 in product(all_columns, repeat=3):
        counts['binary_tables'] += 1
        coords = (c1, c2)
        families = bad_pair_families(labels, target, coords)
        global_family = families['A'] | families['B']
        fixed_feasible = []
        for mask in candidate_masks:
            direct = exact_from_records(labels, target, coords, {'A': mask, 'B': mask})
            combinatorial = hits(mask, global_family)
            check(direct == combinatorial, ('fixed/hitting', target, coords, mask))
            counts['fixed_set_sufficiency_comparisons'] += 1
            if direct:
                fixed_feasible.append(mask)

        feasible_policies = []
        for policy in policies:
            direct = exact_from_records(labels, target, coords, policy)
            combinatorial = all(hits(policy[q], families[q]) for q in ('A', 'B'))
            check(direct == combinatorial, ('policy/hitting', target, coords, policy))
            counts['policy_sufficiency_comparisons'] += 1
            if direct:
                feasible_policies.append(policy)

        unreachable = any(frozenset() in family for family in families.values())
        check(unreachable == (not fixed_feasible), 'empty separating set/fixed infeasibility')
        check(unreachable == (not feasible_policies), 'empty separating set/policy infeasibility')
        counts['unrepairable_tables'] += unreachable
        counts['tables_with_an_already_clean_fiber'] += any(not family for family in families.values())
        counts['empty_bad_pair_families'] += sum(not family for family in families.values())

        for costs in costs_all:
            local_optima = {q: minimum_or_none(mask_cost(mask, costs) for mask in candidate_masks if hits(mask, families[q])) for q in ('A', 'B')}
            formula = {
                'fixed': minimum_or_none(mask_cost(mask, costs) for mask in candidate_masks if hits(mask, global_family)),
                'label_worst': None if unreachable else max(local_optima.values()),
                'label_expected': None if unreachable else sum(probabilities[q] * local_optima[q] for q in ('A', 'B')),
            }
            formula['inventory'] = formula['fixed']
            brute = {
                'fixed': minimum_or_none(mask_cost(mask, costs) for mask in fixed_feasible),
                'label_worst': minimum_or_none(max(mask_cost(policy[q], costs) for q in ('A', 'B')) for policy in feasible_policies),
                'label_expected': minimum_or_none(sum(probabilities[q] * mask_cost(policy[q], costs) for q in ('A', 'B')) for policy in feasible_policies),
                'inventory': minimum_or_none(mask_cost(policy['A'] | policy['B'], costs) for policy in feasible_policies),
            }
            check(formula == brute, ('weighted optimum', target, coords, costs, formula, brute))
            counts['weighted_objective_bundles'] += 1
            counts['individual_objective_equalities'] += len(objective_fields)
            profile = str(costs)
            stat = totals_by_profile.setdefault(profile, Counter())
            stat['tables'] += 1
            stat['unrepairable'] += unreachable
            if not unreachable:
                check(brute['label_expected'] <= brute['label_worst'] <= brute['fixed'], 'cost ordering')
                check(brute['fixed'] <= sum(local_optima.values()) <= 2 * brute['label_worst'], 'two-label sharp bound')
                counts['cost_ordering_checks'] += 1
                counts['label_factor_bound_checks'] += 1
                stat['strict_worst_cost_advantage'] += brute['label_worst'] < brute['fixed']
                stat['strict_expected_cost_advantage'] += brute['label_expected'] < brute['fixed']
                stat['zero_fixed_cost_repairable'] += brute['fixed'] == 0
                if costs == (1, 1):
                    counts['strict_unit_cost_worst_advantage_tables'] += brute['label_worst'] < brute['fixed']
            digest.update(json.dumps([target, coords, costs, {key: fraction_text(brute[key]) for key in objective_fields}], separators=(',', ':')).encode())

    return dict(counts=counts, profiles=totals_by_profile, ordered_result_sha256=digest.hexdigest(), label_probabilities={q: str(p) for q, p in probabilities.items()})


def separation_family():
    cases = []
    counts = Counter()
    for k in range(1, 9):
        states = tuple(product(range(k), (0, 1)))
        labels = tuple(q for q, _ in states)
        target = tuple(b for _, b in states)
        coords = tuple(tuple(b if q == j else 0 for q, b in states) for j in range(k))
        candidate_masks = tuple(range(1 << k))
        fixed_valid = []
        for mask in candidate_masks:
            exact = exact_from_records(labels, target, coords, {q: mask for q in range(k)})
            counts['global_mask_checks'] += 1
            if exact:
                fixed_valid.append(mask)
        fixed_cost = min(mask.bit_count() for mask in fixed_valid)
        local_valid = {}
        for q in range(k):
            subset = [s for s, label in enumerate(labels) if label == q]
            local_labels = tuple(labels[s] for s in subset)
            local_target = tuple(target[s] for s in subset)
            local_coords = tuple(tuple(column[s] for s in subset) for column in coords)
            local_valid[q] = []
            for mask in candidate_masks:
                exact = exact_from_records(local_labels, local_target, local_coords, {q: mask})
                counts['local_mask_checks'] += 1
                if exact:
                    local_valid[q].append(mask)
        policy = {q: min(local_valid[q], key=lambda mask: (mask.bit_count(), mask)) for q in range(k)}
        check(exact_from_records(labels, target, coords, policy), 'k-label routed-record correctness')
        counts['composed_policy_record_checks'] += 1
        worst_cost = max(mask.bit_count() for mask in policy.values())
        expected_cost = sum(Fraction(mask.bit_count(), k) for mask in policy.values())
        # Exhaust every candidate installed menu. Exact policy existence under
        # that inventory factors into finite existential tests on every label.
        inventories = []
        for inventory in candidate_masks:
            counts['inventory_mask_checks'] += 1
            available_for_each_label = all(any(mask & ~inventory == 0 for mask in local_valid[q]) for q in range(k))
            if available_for_each_label:
                inventories.append(inventory)
        inventory_cost = min(mask.bit_count() for mask in inventories)
        check((fixed_cost, worst_cost, expected_cost, inventory_cost) == (k, 1, 1, k), ('k separation', k))
        check(all(policy[q] == (1 << q) for q in range(k)), 'selected local coordinate')
        cases.append(dict(labels=k, states=2*k, fixed_cost=fixed_cost, label_worst_cost=worst_cost, label_expected_uniform=str(expected_cost), inventory_cost=inventory_cost, local_policy={str(q): [q] for q in range(k)}))
    return dict(cases=cases, counts=counts, scope='All global and local batch masks plus every inventory mask enumerated for k=1..8; the exponentially larger Cartesian product of all k-label policies was not enumerated. Selected optimal policies were checked by direct full-record collisions.')


def sequential_example():
    states = tuple(product((0, 1), repeat=3))
    target = tuple(a if s == 0 else b for s, a, b in states)
    coordinates = tuple(tuple(row[j] for row in states) for j in range(3))
    labels = ('Q',) * len(states)
    valid_fixed = [mask for mask in range(8) if exact_from_records(labels, target, coordinates, {'Q': mask})]
    fixed_cost = min(mask.bit_count() for mask in valid_fixed)
    counts = Counter()

    @lru_cache(None)
    def best(remaining, unused):
        counts['decision_subproblems'] += 1
        if len({target[i] for i in remaining}) <= 1:
            return 0
        possibilities = []
        for j in unused:
            branches = tuple(tuple(i for i in remaining if states[i][j] == value) for value in (0, 1))
            if any(not branch for branch in branches):
                continue
            counts['decision_query_options'] += 1
            costs = tuple(best(branch, tuple(other for other in unused if other != j)) for branch in branches)
            if all(cost is not None for cost in costs):
                possibilities.append(1 + max(costs))
        return min(possibilities, default=None)

    sequential_cost = best(tuple(range(8)), tuple(range(3)))
    check((fixed_cost, sequential_cost) == (3, 2), 'sequential selector separation')
    # Replay the proposed s-then-a/b policy against all states.
    records = {}
    for state, (s, a, b) in enumerate(states):
        j = 1 if s == 0 else 2
        record = ((0, s), (j, states[state][j]))
        check(record not in records or records[record] == target[state], 'sequential direct record')
        records[record] = target[state]
    return dict(fixed_batch_cost=fixed_cost, label_batch_cost=fixed_cost, sequential_worst_cost=sequential_cost, states_replayed=8, counts=counts, method='Exhaustive dynamic program over all state-consistent query choices; stop only on target-constant residual sets.')


def edge_and_service_cases():
    cases=[]
    # Empty bad-pair family; no query is needed even if a free query exists.
    labels=('A','A','B','B'); target=(1,1,0,0); coords=((0,1,0,1),(1,0,0,1))
    check(exact_from_records(labels,target,coords,{'A':0,'B':0}), 'clean fibers need no acquisition')
    cases.append(dict(name='empty_families',result='PASS',minimum_cost=0))
    # A zero-probability label still belongs to D and cannot be silently removed.
    target=(0,1,0,0); coords=((0,0,0,0),(1,1,0,0))
    valid=[policy for a,b in product(range(4),repeat=2) if exact_from_records(labels,target,coords,policy:={'A':a,'B':b})]
    check(not valid, 'unrepairable zero-probability label remains fatal')
    cases.append(dict(name='zero_probability_unrepairable_fiber',result='PASS',probabilities={'A':'0','B':'1'},globally_exact_policy_exists=False))
    # Free primitive measurements can repair a nonconstant target at zero cost.
    labels=('A','A'); target=(0,1); coords=((0,1),(0,0)); costs=(0,2)
    valid=[mask for mask in range(4) if exact_from_records(labels,target,coords,{'A':mask})]
    check(min(mask_cost(mask,costs) for mask in valid)==0 and 0 not in valid, 'zero cost is not zero information')
    cases.append(dict(name='free_coordinate_nontrivial_repair',result='PASS',minimum_cost=0,empty_selection_sufficient=False))
    # A service label containing the target answer has already solved recovery.
    labels=(('object',0),('object',1)); target=(0,1); coords=((0,1),)
    check(exact_from_records(labels,target,coords,{label:0 for label in labels}), 'pi_DS answer circularity')
    cases.append(dict(name='service_answer_already_in_label',result='PASS',minimum_cost=0,interpretation='A is already a coordinate of pi_DS=(O,A).'))
    # Before answering, the answer is not in the available pre-observation.
    labels=('request','request')
    check(not exact_from_records(labels,target,coords,{'request':0}), 'pi_pre must preserve uncertainty')
    check(exact_from_records(labels,target,coords,{'request':1}), 'available primitive resolves pre-answer target')
    cases.append(dict(name='service_pre_answer_observation',result='PASS',minimum_unit_cost=1,interpretation='pi_pre excludes the unknown answer; this is a synthetic fixed target, not task validation data.'))
    # Same service answer can hide different historical compliance values.
    labels=(('request','answer'),)*2; target=(0,1)
    check(not exact_from_records(labels,target,((0,1),),{labels[0]:0}), 'audit missing historical distinction')
    check(exact_from_records(labels,target,((0,1),),{labels[0]:1}), 'query existing historical evidence')
    cases.append(dict(name='post_answer_audit_acquires_existing_evidence',result='PASS',minimum_unit_cost=1))
    check(not any(exact_from_records(labels,target,((0,0),),{labels[0]:mask}) for mask in range(2)), 'uncaptured witness not reconstructible from constant evidence')
    cases.append(dict(name='post_answer_audit_uncaptured_evidence',result='PASS',globally_exact_policy_exists=False))
    return cases


def run():
    started=time.perf_counter()
    result={
        'status':'RUNNING',
        'verification_kind':'Independent synthetic finite reconstruction; no existing source verifier or geometry engine imported/executed.',
        'scope':'All binary target/c1/c2 columns on four states, labels A,A,B,B. Exact integer and rational arithmetic; queries read one fixed state without changing it.',
        'source_review':{'path':str(SOURCE_REVIEW),'sha256':sha256(SOURCE_REVIEW.read_bytes()).hexdigest()},
        'source_reported_receipt':{'path':str(SOURCE_RECEIPT),'sha256':sha256(SOURCE_RECEIPT.read_bytes()).hexdigest()},
        'checker':{'path':str(Path(__file__).resolve()),'sha256':sha256(Path(__file__).read_bytes()).hexdigest()},
        'cost_profiles':[[1,1],[1,3],[0,2]],
    }
    result['four_state']=exhaustive_four_state()
    result['k_label_separation']=separation_family()
    result['sequential_example']=sequential_example()
    result['edge_and_service_cases']=edge_and_service_cases()
    source=json.loads(SOURCE_RECEIPT.read_text(encoding='utf-8-sig'))
    mapping={
        'tables':'binary_tables',
        'fixed_mask_checks':'fixed_set_sufficiency_comparisons',
        'policy_checks':'policy_sufficiency_comparisons',
        'weighted_objective_checks':'weighted_objective_bundles',
        'unrepairable_tables':'unrepairable_tables',
        'strict_unit_cost_gap_tables':'strict_unit_cost_worst_advantage_tables',
    }
    result['comparison_with_source_reported_counts']={
        key:{'source_reported':source[key],'independently_reproduced':result['four_state']['counts'][mine],'matches':source[key]==result['four_state']['counts'][mine]} for key,mine in mapping.items()
    }
    check(all(x['matches'] for x in result['comparison_with_source_reported_counts'].values()),'source count reconciliation')
    result['status']='PASS'
    result['errors']=[]
    result['elapsed_seconds']=round(time.perf_counter()-started,6)
    result['completed_at_utc']=datetime.now(timezone.utc).isoformat()
    result['limitations']=[
        'Finite synthetic checks support the implemented identities; the general theorem still rests on its proof and hypotheses.',
        'No real service episode, historical conversation, sampler, timing intervention, energy use or human outcome was measured.',
        'The batch policy selects from q only; the separate sequential example permits branching on earlier acquired values.',
        'Probability zero does not remove a state from the declared exactness domain.',
        'Acquisition cost is not installation cost, visible deletion cost, latency or predictive autonomy.',
        'A_task must be a separately specified and validated target; the synthetic fixtures do not validate real task completion.',
    ]
    DESTINATION.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'counts':result['four_state']['counts'],'k_label_counts':result['k_label_separation']['counts'],'sequential':result['sequential_example'],'edge_and_service_cases':len(result['edge_and_service_cases']),'elapsed_seconds':result['elapsed_seconds'],'receipt':str(DESTINATION)},indent=2))


if __name__=='__main__':
    run()
