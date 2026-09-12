from pathlib import Path
import sys, json, hashlib
from fractions import Fraction
from itertools import product

root=Path(__file__).resolve().parent
sys.path.insert(0,str(root))
from geometry_adaptive import label_conditioned_repairs
from geometry_verify_label_tables import exact_from_records, mask_cost

d=tuple(range(4));labels=('A','A','B','B');q=dict(zip(d,labels))
columns=tuple(product((0,1),repeat=4));profiles=((1,1),(1,3),(0,2));p={'A':Fraction(1,4),'B':Fraction(3,4)}
count=0
for target,c1,c2 in product(columns,repeat=3):
    coords=(c1,c2)
    valid=[{'A':a,'B':b} for a,b in product(range(4),repeat=2) if exact_from_records(labels,target,coords,{'A':a,'B':b})]
    fixed=[a for a in range(4) if exact_from_records(labels,target,coords,{'A':a,'B':a})]
    for costs in profiles:
        r=label_conditioned_repairs(d,q,dict(zip(d,target)),{'c1':dict(zip(d,c1)),'c2':dict(zip(d,c2))},dict(zip(('c1','c2'),costs)),label_probabilities=p)
        assert r.feasible==bool(valid)
        if valid:
            brute_fixed=min(mask_cost(m,costs) for m in fixed)
            brute_worst=min(max(mask_cost(policy[x],costs) for x in p) for policy in valid)
            brute_expected=min(sum(p[x]*mask_cost(policy[x],costs) for x in p) for policy in valid)
            brute_inventory=min(mask_cost(policy['A']|policy['B'],costs) for policy in valid)
            assert (r.fixed.cost,r.worst_cost,r.expected_cost,r.optimal_inventory_cost)==(brute_fixed,brute_worst,brute_expected,brute_inventory)
            selected={x:sum(1<<j for j,n in enumerate(('c1','c2')) if n in r.policy[x]) for x in p}
            assert exact_from_records(labels,target,coords,selected)
            assert r.selected_policy_inventory_cost==mask_cost(selected['A']|selected['B'],costs)
        else:
            assert r.fixed.cost is r.worst_cost is r.expected_cost is r.optimal_inventory_cost is r.selected_policy_inventory_cost is None
            assert r.infeasible_pairs
            for pair in r.infeasible_pairs:
                assert labels[pair.left]==labels[pair.right] and target[pair.left]!=target[pair.right]
                assert all(c[pair.left]==c[pair.right] for c in coords)
        count+=1
receipt={'status':'PASS','scope':'New companion compared against independent explicit-record brute-force policies; synthetic finite data only.','tables':4096,'cost_profiles':[list(x) for x in profiles],'table_cost_cases':count,'geometry_engine_sha256':hashlib.sha256((root/'outputs/geometry_engine.py').read_bytes()).hexdigest(),'geometry_adaptive_sha256':hashlib.sha256((root/'outputs/geometry_adaptive.py').read_bytes()).hexdigest(),'focused_test_methods_reported':23,'sequential_optimizer_implemented':False,'empirical_experiment':False}
(root/'outputs/geometry_adaptive_verification.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt))
