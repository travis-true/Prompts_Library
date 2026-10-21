#!/usr/bin/env python3
"""Check declared live-demo structure; never execute a demo or authorize delivery."""
import argparse,json,re
from pathlib import Path
from datetime import date

def validate(d,root):
 errors=[];root=Path(root).resolve()
 def need(ok,msg):
  if not ok:errors.append(msg)
 def text(v):return isinstance(v,str) and bool(v.strip())
 def number(v):return type(v) in [int,float] and v>=0
 def load(path):
  if not text(path):errors.append('Missing evidence/file path');return ''
  p=root/path
  if p.is_symlink() or not p.resolve().is_relative_to(root) or not p.is_file():errors.append('Missing/unsafe file: '+path);return ''
  return p.read_text(encoding='utf-8')
 def index(items,label):
  need(isinstance(items,list),label+' must be list');result={}
  for item in items if isinstance(items,list) else []:
   if not isinstance(item,dict):errors.append(label+' item must be object');continue
   id=item.get('id');need(text(id) and id not in result,label+' IDs must be unique')
   if text(id):result[id]=item
  return result
 def refs(items,known,label):
  need(isinstance(items,list) and bool(items),label+' references missing')
  for id in items if isinstance(items,list) else []:need(id in known,label+' unknown reference '+str(id))
 def evidence(v,label):
  need(isinstance(v,dict),label+' actual evidence missing')
  if not isinstance(v,dict):return
  for key in ['method','reviewer','date','artifact_version','path','quote']:need(text(v.get(key)),label+' missing evidence '+key)
  need(v.get('artifact_version')==d.get('artifact_version'),label+' stale evidence version')
  try:need(date.fromisoformat(v.get('date',''))<=date.today(),label+' future evidence date')
  except (ValueError,TypeError):errors.append(label+' invalid evidence date')
  content=load(v.get('path'));need(text(v.get('quote')) and v['quote'] in content,label+' evidence quote unresolved')
 if not isinstance(d,dict):return ['Record must be object']
 need(d.get('schema_version')=='1.1','Unsupported schema')
 version=d.get('artifact_version');need(text(version),'Missing artifact version')
 state=d.get('release_state');need(state in ['Ready for delivery','Draft complete; review required','Needs revision','Planning framework only'],'Invalid release state')
 body=load(d.get('document'));need(f'**Version:** {version}' in body,'Document version differs');need(f'**Release state:** {state}' in body,'Document state differs')
 need(text(d.get('intended_use')),'Missing intended use')
 objective=d.get('objective',{});need(text(objective.get('id')) and text(objective.get('text')),'Missing objective')
 sources=index(d.get('sources'),'Source')
 for id,s in sources.items():need(text(s.get('version')) and text(s.get('locator')) and text(s.get('kind')),id+' source metadata missing');load(s.get('path'))
 states=d.get('states');need(isinstance(states,list) and len(states)==len(set(states)) and all(text(x) for x in states),'Invalid states')
 states=states if isinstance(states,list) else []
 scenes=index(d.get('scenes'),'Scene');actions=index(d.get('actions'),'Action');assets=index(d.get('assets'),'Asset');recoveries=index(d.get('recoveries'),'Recovery')
 need(bool(scenes),'No scenes')
 for id,a in actions.items():
  need(a.get('source_id') in sources,id+' unknown action source');need(a.get('from_state') in states and a.get('to_state') in states,id+' unknown action state')
  need(a.get('effect') in ['read-only','mutation'],id+' invalid effect');need(type(a.get('non_idempotent')) is bool,id+' retry character missing')
  for key in ['success_signal','verification_route','on_unknown','retry_policy','authorization']:need(text(a.get(key)),id+' missing '+key)
  need(a.get('executed') is False,id+' record is design-only; actual execution requires separate evidence')
  if a.get('effect')=='read-only':need(a.get('from_state')==a.get('to_state'),id+' read-only cannot change state')
  if a.get('effect')=='mutation':
   need(a.get('verify_before_retry') is True,id+' mutation must verify before retry')
   need(bool(re.search(r'never repeat while outcome Unknown',str(a.get('retry_policy','')))),id+' unsafe unknown-outcome retry')
   need('switch' in str(a.get('on_unknown','')).lower() and 'inspect' in str(a.get('on_unknown','')).lower(),id+' unknown outcome needs state check and switch')
 for id,a in assets.items():
  need(a.get('status') in ['Planned','Created','Verified'],id+' invalid asset status');need(a.get('source_id') in sources,id+' unknown asset source');need(a.get('artifact_version')==version,id+' stale asset version');need(type(a.get('required')) is bool,id+' required flag missing')
  if a.get('status') in ['Created','Verified']:
   content=load(a.get('path'));need(text(a.get('quote')) and a['quote'] in content,id+' asset section unresolved')
  else:need(text(a.get('external_prerequisite')) or text(a.get('path')),id+' planned asset prerequisite missing')
  if a.get('status')=='Verified':evidence(a.get('verification'),id)
 for id,r in recoveries.items():
  need(r.get('scene_id') in scenes and r.get('asset_id') in assets,id+' unknown scene/backup reference')
  need(number(r.get('max_seconds')) and r.get('max_seconds',0)>0,id+' recovery budget missing')
  need(r.get('decision') in ['continue','switch','skip','stop'],id+' invalid recovery decision')
  for key in ['language','unknown_live_outcome','stop_rule']:need(text(r.get(key)),id+' missing '+key)
  if r.get('scene_id') in scenes and any(actions.get(a,{}).get('effect')=='mutation' for a in scenes[r['scene_id']].get('action_ids',[])):need(r.get('state_check_required') is True,id+' recovery must check state')
 for id,s in scenes.items():
  refs(s.get('objective_ids'),{objective.get('id'):objective},id+' objective');refs(s.get('action_ids'),actions,id+' action')
  for key in ['title','narration','optional_enrichment','expert_commentary','expected_result','failure_signal','observation','transition']:need(text(s.get(key)),id+' missing scene '+key)
  need(s.get('entry_state') in states and s.get('exit_state') in states,id+' invalid scene state')
  chain=s.get('entry_state')
  for aid in s.get('action_ids',[]):
   a=actions.get(aid,{})
   need(a.get('from_state')==chain,id+' broken action state chain');chain=a.get('to_state')
  need(chain==s.get('exit_state'),id+' scene exit differs')
  need(s.get('recovery_id') in recoveries and recoveries.get(s.get('recovery_id'),{}).get('scene_id')==id,id+' missing matching recovery')
  cp=s.get('checkpoint',{})
  for key in ['prompt','response_mode','expected_evidence','facilitator_response','fallback']:need(text(cp.get(key)),id+' incomplete checkpoint '+key)
  need(number(cp.get('max_seconds')) and cp.get('max_seconds',0)>0,id+' checkpoint time missing')
  times=s.get('durations',{});need(set(times)=={'standard','compressed','expanded'} and all(number(v) and v>0 for v in times.values()),id+' invalid duration variants')
  if all(number(times.get(x)) for x in ['compressed','standard','expanded']):need(times['compressed']<=times['standard']<=times['expanded'],id+' variants out of order')
 used=[a for s in scenes.values() for a in s.get('action_ids',[])];need(set(used)==set(actions),'Action coverage differs')
 paths=index(d.get('paths'),'Path');need(set(paths)=={'standard','compressed','expanded'},'Three timing paths required')
 for id,p in paths.items():
  steps=p.get('steps',[]);need(isinstance(steps,list) and [s.get('scene_id') for s in steps]==list(scenes),id+' path scene coverage/order differs')
  total=0;previous=None
  for step in steps:
   sid=step.get('scene_id');s=scenes.get(sid,{});minutes=step.get('minutes');need(number(minutes) and minutes>0,id+' invalid step duration')
   if number(minutes):total+=minutes
   need(minutes==s.get('durations',{}).get(id),id+' scene duration differs')
   parts=step.get('components_seconds',{});need(set(parts)=={'checkpoint','recovery_reserve','transition','narration_actions_loading'} and all(number(v) for v in parts.values()),id+' missing timing components')
   if number(minutes) and all(number(v) for v in parts.values()):need(sum(parts.values())==minutes*60,id+' component total differs')
   recovery=recoveries.get(s.get('recovery_id'),{});need(parts.get('recovery_reserve',-1)>=recovery.get('max_seconds',0),id+' recovery exceeds reserve')
   if id!='compressed':need(parts.get('checkpoint',-1)>=s.get('checkpoint',{}).get('max_seconds',0),id+' checkpoint exceeds allocation')
   need(step.get('mode') in ['prepared-text','planned-live-or-disclosed-storyboard'],id+' unknown path mode')
   need(text(step.get('action')) and text(step.get('result_preserved')) and isinstance(step.get('omissions'),list),id+' path description missing')
   if step.get('mode')=='prepared-text':need(step.get('entry_dependency') in assets,id+' missing prepared entry dependency');need(bool(step.get('omissions')),id+' prepared route must disclose omissions')
   else:
    need(step.get('entry_dependency')==s.get('entry_state'),id+' live entry dependency differs')
    if previous is not None:need(previous==s.get('entry_state'),id+' path state discontinuity')
   previous=s.get('exit_state')
  need(number(p.get('total_minutes')) and total==p.get('total_minutes'),id+' path total differs')
 fallbacks=index(d.get('fallbacks'),'Fallback');need(bool(fallbacks),'Fallback record missing')
 for id,f in fallbacks.items():
  refs(f.get('asset_ids'),assets,id+' assets');need(f.get('objective_id')==objective.get('id'),id+' unknown fallback objective')
  for key in ['construct','rationale','claim']:need(text(f.get(key)),id+' missing '+key)
  need(f.get('classification') in ['Equivalent','Partially equivalent','Not equivalent'],id+' invalid equivalence classification')
  need(isinstance(f.get('omissions'),list),id+' omissions missing')
  if f.get('classification')=='Equivalent':need(not f.get('omissions'),id+' Equivalent cannot omit target evidence')
  need(f.get('verification_status') in ['Not checked','Verified'],id+' invalid verification status')
  if f.get('verification_status')=='Verified':
   evidence(f.get('verification'),id)
   need(all(assets.get(a,{}).get('status')=='Verified' for a in f.get('asset_ids',[])),id+' verified fallback requires verified assets')
  need(f.get('proficiency_use_allowed') is False,id+' demonstration cannot imply proficiency')
 learner=load(d.get('learner_path'));key=load(d.get('key_path'));need(d.get('learner_path')!=d.get('key_path'),'Learner/key separation required');need('Facilitator-only' not in learner,'Learner file contains key material')
 practice=index(d.get('practice'),'Practice');need(bool(practice),'Practice missing')
 for id,p in practice.items():
  need(id in learner and id in key,id+' practice reference missing');quotes=p.get('fact_quotes',[]);need(isinstance(quotes,list) and len(quotes)>=4,id+' complete fact references required')
  for q in quotes:need(text(q) and q in learner,id+' supplied fact missing')
  need(text(p.get('key_quote')) and p['key_quote'] in key,id+' model key missing')
  if p.get('retry_id') is not None:need(p['retry_id'] in practice and p['retry_id']!=id,id+' unknown retry')
 need(number(d.get('practice_minutes_outside_demo')) and d.get('practice_minutes_outside_demo',0)>0,'Practice timing outside demo missing')
 checks=index(d.get('quality_checks'),'Quality');need(set(checks)=={f'Q-{i:02}' for i in range(1,14)},'Thirteen individual quality checks required')
 for id,q in checks.items():
  need(type(q.get('applicable')) is bool and type(q.get('required')) is bool,id+' applicability/required missing')
  need(text(q.get('rationale')) and text(q.get('scope')) and text(q.get('corrective_action')),id+' quality rationale/scope/action missing')
  need(q.get('artifact_version')==version,id+' stale quality version');need(q.get('status') in ['Pass','Needs revision','Not checked','Not applicable'],id+' invalid quality status')
  if q.get('applicable'):need(q.get('status')!='Not applicable',id+' applicable check excluded')
  else:need(q.get('status')=='Not applicable' and q.get('required') is False,id+' exclusion cannot count as pass')
  if q.get('status')=='Pass':evidence(dict(method=q.get('method'),reviewer=q.get('reviewer'),date=q.get('date'),artifact_version=q.get('artifact_version'),path=q.get('evidence_path'),quote=q.get('evidence_quote')),id)
 rehearsals=d.get('rehearsals',[]);need(isinstance(rehearsals,list) and {x.get('path_id') for x in rehearsals}=={'standard','compressed','expanded','offline','reset'} and len(rehearsals)==5,'Required rehearsal records missing/duplicate')
 for h in rehearsals:
  need(h.get('status') in ['Not checked','Pass','Needs revision'],'Invalid rehearsal status')
  if h.get('status')=='Pass':evidence(h.get('evidence'),'Rehearsal '+str(h.get('path_id')))
 opens=index(d.get('open_items'),'Open item')
 for id,o in opens.items():need(text(o.get('owner')) and text(o.get('description')) and type(o.get('blocking')) is bool and o.get('status') in ['Open','Resolved'],id+' invalid open item')
 authorization=d.get('release_authorization',{});need(authorization.get('status') in ['Not checked','Authorized'],'Invalid authorization')
 if authorization.get('status')=='Authorized':evidence(authorization.get('evidence'),'Release authorization')
 if any(q.get('status')=='Needs revision' for q in checks.values()) or any(h.get('status')=='Needs revision' for h in rehearsals):need(state=='Needs revision','Known defect requires Needs revision')
 if state=='Ready for delivery':
  need(all(q.get('status')=='Pass' for q in checks.values() if q.get('required') or q.get('applicable')),'Readiness has unperformed checks')
  need(all(a.get('status')=='Verified' for a in assets.values() if a.get('required')),'Readiness requires verified assets')
  need(all(h.get('status')=='Pass' for h in rehearsals),'Readiness requires actual rehearsals')
  need(not any(o.get('blocking') and o.get('status')!='Resolved' for o in opens.values()),'Readiness has blocking open items')
  need(authorization.get('status')=='Authorized','Readiness requires actual authorization')
  need(not any(s.get('kind')=='fictional-specification' for s in sources.values()),'Fictional-only environment cannot claim delivery readiness')
 handoffs=index(d.get('handoffs'),'Handoff');need({h.get('destination') for h in handoffs.values()}=={'live-training-session-design','build-assessments-and-evaluations','qa-and-release-assets'},'Handoff destinations differ')
 handoff=load(d.get('handoff_document'))
 for id,h in handoffs.items():
  need(h.get('status')=='Prepared; not executed',id+' cannot imply handoff execution')
  refs(h.get('source_ids'),sources,id+' source');refs(h.get('scene_ids'),scenes,id+' scene');refs(h.get('open_item_ids'),opens,id+' open item')
  need(isinstance(h.get('finding_ids'),list),id+' finding ID list missing')
  need(text(h.get('owner')) and bool(h.get('tasks')) and text(h.get('acceptance')),id+' handoff scope/acceptance missing')
  for ref in h.get('source_ids',[])+h.get('scene_ids',[])+h.get('finding_ids',[])+h.get('open_item_ids',[]):need(ref in handoff,id+' handoff lost reference')
  need(h.get('destination','') in handoff,id+' handoff destination missing in document')
 return errors

def validate_skill(root):
 root=Path(root);errors=[];p=root/'SKILL.md'
 if not p.is_file():return ['Missing SKILL.md']
 if not re.match(r'---\nname: live-training-session-design\ndescription: [^\n]+\n---\n',p.read_text()):errors.append('Minimal frontmatter invalid')
 ui=root/'agents/openai.yaml'
 if not ui.is_file() or '$live-training-session-design' not in ui.read_text():errors.append('UI metadata missing or stale')
 for p in root.rglob('*.md'):
  prose=re.sub(r'```[\s\S]*?```','',p.read_text())
  for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',prose):
   if re.match(r'(https?://|mailto:|#)',target):continue
   dest=(p.parent/target.split('#')[0]).resolve()
   if not dest.is_relative_to(root.resolve()) or not dest.is_file():errors.append(str(p.relative_to(root))+': missing/unsafe link '+target)
 return errors

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--record',type=Path);p.add_argument('--root',type=Path);p.add_argument('--skill',type=Path);a=p.parse_args();errors=[]
 try:
  if a.record:errors+=validate(json.loads(a.record.read_text()),a.root or a.record.parent)
  if a.skill:errors+=validate_skill(a.skill)
  if not a.record and not a.skill:p.error('Supply --record and/or --skill')
 except (ValueError,TypeError,KeyError,AttributeError,OSError) as exc:errors.append('Malformed record or unreadable file: '+str(exc))
 print(json.dumps(dict(structural_validation='FAIL' if errors else 'PASS',errors=errors,limits='Declared structure only; no source authentication, actual execution, accessibility, semantic equivalence, learner proficiency or release authorization.'),indent=2));return bool(errors)
if __name__=='__main__':raise SystemExit(main())
