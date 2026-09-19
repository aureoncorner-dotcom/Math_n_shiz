import json, csv, re, hashlib, sys, argparse
from pathlib import Path
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')
parser = argparse.ArgumentParser(description='Recompute the geometry review retained-artifact checks.')
parser.add_argument('--session-transitions', type=Path, required=True)
parser.add_argument('--returned-records', type=Path, required=True)
parser.add_argument('--name-register', type=Path, required=True)
parser.add_argument('--output', type=Path, default=Path('Evidence_checks.recomputed.json'))
args = parser.parse_args()
csv_path = args.session_transitions
rows=list(csv.DictReader(csv_path.open(encoding='utf-8-sig')))
current_path=args.returned_records
d=json.loads(current_path.read_text(encoding='utf-8-sig'))
turns=d['turns']; texts=[]; assistant=[]
for t in turns:
 for i in t.get('items',[]):
  if i.get('type')=='userMessage':
   texts.extend(c['text'] for c in i.get('content',[]) if c.get('type')=='text')
  elif i.get('type')=='agentMessage': assistant.append(i.get('text',''))
counts=Counter(texts)
phrase,count=counts.most_common(1)[0]
name_path=args.name_register
names=json.loads(name_path.read_text(encoding='utf-8-sig'))
name_metrics=[]
for name,rs in names['groups'].items():
 joined=[' '.join(v.get('text','') for v in r.get('replies',[])) for r in rs]
 replies=[x for x in joined if x.strip()]
 name_metrics.append({'group':name,'prompt_turns':len(rs),'turns_with_reply':len(replies),'reply_turns_at_most_10_words':sum(len(x.split())<=10 for x in replies),'presence_wording':sum(bool(re.search(r"i['’]m (?:still )?here",x,re.I)) for x in replies),'evidence_vocabulary':sum(bool(re.search(r'evidence|record|establish|verify|confirm|attribution|proof|source|observable',x,re.I)) for x in replies)})
expected={m['group']:m for m in names['metrics']}
checks={m['group']:all(expected[m['group']][k]==v for k,v in m.items()) for m in name_metrics}
report={
 'scope':'Fresh checks of retained CSV/JSON artifacts; not a new raw-platform export, network-capture replay, or controlled experiment.',
 'sessions':{'rows':len(rows),'conversations':len(set(r['case'] for r in rows)),'tc_changes':sum(r['before']!=r['after'] for r in rows),'voice_changes':sum(r['voice_before']!=r['voice_after'] for r in rows),'bidi_both':sum(r['model_before']==r['model_after']=='bidi' for r in rows)},
 'returned_records':{'turns':len(turns),'distinct_turn_ids':len(set(t['id'] for t in turns)),'assistant_messages':len(assistant),'user_text_items':len(texts),'most_repeated_text_length':len(phrase),'most_repeated_text_count':count,'exact_fourfold_records':sum(t==phrase*4 for t in texts)},
 'name_register':{'metrics_recomputed':name_metrics,'matches_retained_metrics':checks,'scope':names['scope']},
 'inputs':[{'path':'external-source:'+p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [csv_path,current_path,name_path]]
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
