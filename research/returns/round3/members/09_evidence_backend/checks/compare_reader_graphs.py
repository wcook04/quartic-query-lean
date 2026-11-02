#!/usr/bin/env python3
"""Compare the supplied retained/current informal graphs modulo one recorded delta.
This is a JSON/source audit, not native extraction or native consumer execution.
"""
import argparse,copy,hashlib,json
from pathlib import Path

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('packet',type=Path);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
 rels=['native_results/reader-acceptance/evidence-graph.json','repository/corpus/evidence-graph.json']
 graphs=[json.loads((a.packet/r).read_text()) for r in rels]
 def key(e):return 'receipt:'+e['receipt_path'] if 'receipt_path' in e else e['id']
 oldkeys={key(e) for e in graphs[0]['evidence']};newkeys={key(e) for e in graphs[1]['evidence']}
 added=sorted(newkeys-oldkeys);removed=sorted(oldkeys-newkeys)
 expected='receipt:corpus/receipts/comparator-Unconditional-2026-11-02T184546477430+0000.json'
 def normal(g):
  x=copy.deepcopy(g);mapping={e['id']:key(e) for e in x['evidence']}
  x['evidence']=[e for e in x['evidence'] if key(e)!=expected]
  def walk(v):
   if isinstance(v,str):return mapping.get(v,v)
   if isinstance(v,list):return [walk(t) for t in v]
   if isinstance(v,dict):
    z={k:walk(t) for k,t in v.items()}
    if 'evidence_ids' in z:z['evidence_ids']=sorted(i for i in z['evidence_ids'] if i!=expected)
    return z
   return v
  x=walk(x);x['evidence'].sort(key=lambda e:e['id']);return x
 equal=normal(graphs[0])==normal(graphs[1])
 result={'kind':'actual_json_graph_delta_check','sources':[{'member':r,'sha256':digest(a.packet/r)} for r in rels],'evidence_counts':[len(g['evidence']) for g in graphs],'added_evidence_keys':added,'removed_evidence_keys':removed,'expected_only_added_receipt':added==[expected] and not removed,'normalization':'Rename run evidence IDs to receipt paths, remove the single specified added receipt and its references, sort evidence/reference lists. Do not ignore any other field.','otherwise_equal':equal,'passed':added==[expected] and not removed and equal,'native_execution':False,'boundary':'Describes exact supplied informal graph bytes; does not validate either graph using the consumer or establish native extraction.'}
 a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));return 0 if result['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
