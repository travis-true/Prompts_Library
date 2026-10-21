#!/usr/bin/env python3
"""Validate declared campaign structure without running Copilot, collecting data or publishing."""
import argparse,json,re,hashlib
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo,ZoneInfoNotFoundError

def validate(d,root):
 root=Path(root).resolve();errors=[]
 def need(ok,msg):
  if not ok:errors.append(msg)
 def text(v):return isinstance(v,str) and bool(v.strip())
 def number(v):return type(v) in [int,float] and v>=0
 def day(value,label):
  try:return date.fromisoformat(value)
  except (ValueError,TypeError):errors.append(label+' invalid date');return None
 def load(path):
  if not text(path):errors.append('Missing file/evidence path');return ''
  p=root/path
  if p.is_symlink() or not p.resolve().is_relative_to(root) or not p.is_file():errors.append('Missing/unsafe file '+path);return ''
  return p.read_text(encoding='utf-8')
 def index(items,label):
  need(isinstance(items,list),label+' must be list');out={}
  for v in items if isinstance(items,list) else []:
   if not isinstance(v,dict):errors.append(label+' item must be object');continue
   id=v.get('id');need(text(id) and id not in out,label+' IDs must be unique')
   if text(id):out[id]=v
  return out
 def refs(items,known,label):
  need(isinstance(items,list) and bool(items),label+' missing references')
  for id in items if isinstance(items,list) else []:need(id in known,label+' unknown reference '+str(id))
 def evidence(v,label):
  need(isinstance(v,dict),label+' actual evidence missing')
  if not isinstance(v,dict):return
  for k in ['path','quote','method','reviewer','date','version']:need(text(v.get(k)),label+' missing evidence '+k)
  need(v.get('version')==d.get('version'),label+' stale evidence version')
  dt=day(v.get('date'),label)
  if dt:need(dt<=date.today(),label+' future evidence date')
  body=load(v.get('path'));need(text(v.get('quote')) and v['quote'] in body,label+' evidence quote unresolved')
 if not isinstance(d,dict):return ['Record must be object']
 need(d.get('schema_version')=='1.1','Unsupported schema');version=d.get('version');need(text(version),'Missing version')
 state=d.get('release_state');need(state in ['Draft complete; review required','Ready for release','Needs revision','Planning framework only'],'Invalid release state')
 body=load(d.get('overview'));need(f'**Version:** {version}' in body,'Overview version differs');need(f'**Release state:** {state}' in body,'Overview state differs')
 sources=index(d.get('sources'),'Source');claims=index(d.get('claims'),'Claim');tips=index(d.get('tips'),'Tip');assets=index(d.get('assets'),'Asset');metrics=index(d.get('metrics'),'Metric')
 for id,s in sources.items():
  for k in ['title','publisher','url','path','quote']:need(text(s.get(k)),id+' source metadata missing '+k)
  parsed=urlparse(s.get('url',''));need(parsed.scheme=='https' and parsed.hostname in ['support.microsoft.com','learn.microsoft.com','www.microsoft.com'],id+' official Microsoft source required')
  accessed=day(s.get('accessed'),id)
  if accessed:need(accessed<=date.today(),id+' source access date in future')
  content=load(s.get('path'));need(text(s.get('quote')) and s['quote'] in content,id+' source excerpt unresolved')
 for id,c in claims.items():
  refs(c.get('source_ids'),sources,id+' sources');need(text(c.get('statement')) and text(c.get('dependencies')),id+' claim statement/dependencies missing')
  need(c.get('scope') in ['general-guidance','feature','license','tenant-workflow'],id+' invalid claim scope');need(c.get('documentation_status') in ['Checked','Not verified'],id+' invalid documentation status')
  need(c.get('environment_status') in ['Not checked','Pass','Needs revision'],id+' invalid environment status')
  if c.get('environment_status')=='Pass':evidence(c.get('environment_evidence'),id)
  refresh=day(c.get('refresh_by'),id)
  if state=='Ready for release':
   need(c.get('documentation_status')=='Checked',id+' unverified claim blocks release')
   if refresh:need(refresh>=date.today(),id+' expired claim blocks release')
   if c.get('scope')!='general-guidance':need(c.get('environment_status')=='Pass',id+' feature claim requires actual environment evidence')
 calendar=d.get('calendar',{});need(calendar.get('mode') in ['sequence-only','dated'],'Calendar mode missing');need(text(calendar.get('cadence')),'Calendar cadence missing')
 need(type(calendar.get('count')) is int and calendar.get('count')==len(tips) and len(tips)>0,'Calendar count differs')
 need([t.get('sequence') for t in tips.values()]==list(range(1,len(tips)+1)),'Tip sequence/order differs')
 if calendar.get('mode')=='sequence-only':need(calendar.get('timezone') is None and calendar.get('start_date') is None,'Sequence-only calendar cannot imply dates')
 else:
  start=day(calendar.get('start_date'),'Calendar')
  try:ZoneInfo(calendar.get('timezone',''))
  except (ValueError,TypeError,ZoneInfoNotFoundError):errors.append('Dated calendar requires valid timezone')
  dates=[day(t.get('date'),t['id']) for t in tips.values()]
  need(all(dates) and dates==sorted(x for x in dates if x),'Dated calendar order invalid')
  if dates and start:need(dates[0]==start,'Calendar start differs')
 unique={k:[] for k in ['scenario','inputs','model','review','question']}
 for id,t in tips.items():
  need(t.get('version')==version,id+' stale tip version');content=load(t.get('path'));need(id in content,id+' tip ID missing in file')
  for k in ['title','phase','mode','difficulty_rationale','new_joiner_path','scenario','inputs','model','review','question','reinforcement']:
   need(text(t.get(k)),id+' missing tip '+k)
   if k in unique:unique[k].append(t.get(k))
  need(t.get('difficulty') in ['Foundational','Intermediate','Advanced'],id+' invalid difficulty')
  need(t.get('mode') in ['retrieval/retry','new-task','repeat-use','application'],id+' invalid tip mode')
  for k in ['inputs','model','review']:need(text(t.get(k)) and t[k] in content,id+' '+k+' differs from file')
  p=t.get('prompt',{});need(set(p)=={'goal','context','source','expectation'} and all(text(v) for v in p.values()),id+' incomplete GCSE prompt')
  for k,v in p.items():need(text(v) and v in content,id+' filled prompt differs')
  need(p.get('source')==t.get('inputs'),id+' prompt source differs from supplied inputs')
  prereq=t.get('prerequisite_ids',[]);need(isinstance(prereq,list),id+' prerequisite list missing')
  for pid in prereq:need(pid in tips and tips.get(pid,{}).get('sequence',999)<t.get('sequence',0),id+' unknown/future prerequisite')
  refs(t.get('claim_ids'),claims,id+' claim')
  if t.get('metric_ids'):refs(t['metric_ids'],metrics,id+' metric')
  else:need(t.get('metric_ids')==[] and text(t.get('measurement_exclusion')),id+' missing metric or exclusion rationale')
  visual=t.get('visual',{})
  for k in ['concept','purpose','channel','ratio','composition','style','text_treatment','image_prompt','alt_text']:need(text(visual.get(k)),id+' visual missing '+k)
  w,h=visual.get('width'),visual.get('height');need(type(w) is int and w>0 and type(h) is int and h>0,id+' invalid dimensions')
  try:
   a,b=map(int,visual.get('ratio','').split(':'));need(a>0 and b>0 and w*b==h*a,id+' aspect ratio differs')
  except (ValueError,TypeError):errors.append(id+' invalid ratio')
  need(visual.get('status') in ['Brief only; not rendered','Rendered'],id+' invalid visual status')
  need(visual.get('accessibility_status') in ['Not checked','Pass','Needs revision'],id+' invalid visual accessibility')
  if visual.get('accessibility_status')=='Pass':need(visual.get('status')=='Rendered',id+' brief cannot pass rendered access');evidence(visual.get('evidence'),id+' visual')
  if visual.get('status')=='Rendered':
   path=visual.get('rendered_path');need(text(path),id+' rendered visual path missing')
   if text(path):
    target=root/path
    if target.is_symlink() or not target.resolve().is_relative_to(root) or not target.is_file():errors.append(id+' missing/unsafe rendered visual')
    else:need(visual.get('rendered_sha256')==hashlib.sha256(target.read_bytes()).hexdigest(),id+' rendered visual hash differs')
   need(visual.get('alt_text_final') is True and not str(visual.get('alt_text','')).startswith('Provisional:'),id+' final alt text missing')
  if state=='Ready for release':need(visual.get('status')=='Rendered' and visual.get('accessibility_status')=='Pass',id+' required visual not rendered/access checked')
 for k,values in unique.items():need(len(values)==len(set(values)),'Duplicate task-specific '+k)
 if len(tips)>=10:need(any(t.get('mode')=='retrieval/retry' for t in tips.values()),'Long sequence needs retrieval/retry')
 required=d.get('required_channels');need(isinstance(required,list) and bool(required) and len(required)==len(set(required)),'Required channels missing/duplicate')
 for id,a in assets.items():
  need(a.get('tip_id') in tips,id+' unknown parent tip');need(a.get('version')==version,id+' stale asset version')
  need(a.get('channel') in ['Teams','SharePoint','Email','Prompt card'],id+' invalid channel')
  content=load(a.get('path'));need(text(a.get('quote')) and a['quote'] in content,id+' channel content unresolved')
  need(a.get('content_status') in ['Draft','In review','Approved for this campaign','Expired','Retired'],id+' invalid content status')
  need(a.get('publication_status') in ['Not scheduled','Prepared','Scheduled','Published','Withdrawn'],id+' invalid publication status')
  need(text(a.get('owner')),id+' missing publishing owner');refs(a.get('claim_ids'),claims,id+' claim');refs(a.get('metric_ids'),metrics,id+' metric')
  expiry=day(a.get('expires'),id)
  if a.get('content_status')=='Approved for this campaign':
   evidence(a.get('approval'),id+' approval')
   if isinstance(a.get('approval'),dict):need(a['approval'].get('content_sha256')==hashlib.sha256(content.encode()).hexdigest(),id+' approved content hash differs')
  if a.get('publication_status') in ['Scheduled','Published']:
   need(a.get('content_status')=='Approved for this campaign',id+' publication requires approved asset');evidence(a.get('publication_evidence'),id+' publication')
   need(text(a.get('execution_id')) and text(a.get('scheduled_at')) and text(a.get('timezone')),id+' actual schedule/execution identity missing')
  if state=='Ready for release':
   need(a.get('content_status')=='Approved for this campaign',id+' draft asset blocks release');need(a.get('render_status')=='Pass',id+' rendered channel not checked');need(not a.get('owner','').startswith('Unassigned'),id+' publishing owner unresolved')
   if expiry:need(expiry>=date.today(),id+' expired asset blocks release')
 for tid in tips:
  for chan in required if isinstance(required,list) else []:need(sum(a.get('tip_id')==tid and a.get('channel')==chan for a in assets.values())==1,tid+' channel coverage/duplicate '+str(chan))
 for id,m in metrics.items():
  for k in ['layer','decision','numerator','denominator','population','period','deduplication','missingness','source','access_status','collection_owner','analysis_owner','analysis','limit','privacy','retention']:need(text(m.get(k)),id+' metric missing '+k)
  for k in ['baseline','target','result']:need(k in m and (m[k] is None or number(m[k])),id+' numeric unknown must be null or nonnegative')
  if m.get('target') is not None:need(text(m.get('target_authority')),id+' target authority missing')
  if m.get('result') is not None:evidence(m.get('result_evidence'),id+' observed result')
  attempt=bool(re.search(r'attempt|tried|try a prompt|prompt submissions|prompt completion',str(m.get('numerator','')),re.I))
  if attempt:need(m.get('layer')=='Attempt',id+' attempt cannot establish learning')
  need(m.get('collection_status') in ['Not authorized; not collected','Authorized; not collected','Collected','Excluded; not collected'],id+' collection status missing')
  if m.get('collection_status') in ['Authorized; not collected','Collected']:evidence(m.get('authorization'),id+' data authorization')
  if m.get('collection_status')=='Excluded; not collected':need(text(m.get('exclusion_rationale')),id+' collection exclusion rationale missing')
 checks=index(d.get('quality_checks'),'Quality');need(set(checks)=={f'Q-{i:02}' for i in range(1,16)},'Fifteen individual quality checks required')
 for id,q in checks.items():
  need(type(q.get('applicable')) is bool and type(q.get('required')) is bool,id+' applicability missing');need(text(q.get('scope')) and text(q.get('rationale')) and text(q.get('corrective_action')),id+' scope/rationale/action missing');need(q.get('version')==version,id+' stale quality version')
  need(q.get('status') in ['Pass','Needs revision','Not checked','Not applicable'],id+' invalid quality status')
  if q.get('applicable'):need(q.get('status')!='Not applicable',id+' applicable check excluded')
  else:need(q.get('status')=='Not applicable' and q.get('required') is False,id+' exclusion cannot Pass')
  if q.get('status')=='Pass':evidence(q.get('evidence'),id)
 opens=index(d.get('open_items'),'Open item')
 for id,o in opens.items():need(text(o.get('owner')) and text(o.get('description')) and type(o.get('blocking')) is bool and o.get('status') in ['Open','Resolved'],id+' open item incomplete')
 auth=d.get('release_authorization',{});need(auth.get('status') in ['Not checked','Authorized'],'Invalid authorization')
 if auth.get('status')=='Authorized':evidence(auth.get('evidence'),'Release authorization')
 if any(q.get('status')=='Needs revision' for q in checks.values()):need(state=='Needs revision','Known defect requires Needs revision')
 if state=='Ready for release':
  need(all(q.get('status')=='Pass' for q in checks.values() if q.get('required') or q.get('applicable')),'Readiness has unperformed quality checks')
  need(not any(o.get('blocking') and o.get('status')!='Resolved' for o in opens.values()),'Readiness has blocking open items')
  need(auth.get('status')=='Authorized','Readiness requires actual authorization')
  for m in metrics.values():need(m.get('collection_status')!='Not authorized; not collected','Measurement plan needs authorization or explicit removal before release')
 handoffs=index(d.get('handoffs'),'Handoff');need({h.get('destination') for h in handoffs.values()}=={'qa-and-release-assets','build-assessments-and-evaluations','authorized-channel-publishing-owner'},'Handoff destinations differ')
 handoff=load(d.get('handoff_path'))
 for id,h in handoffs.items():
  need(h.get('status')=='Prepared; not executed',id+' handoff cannot imply execution');need(isinstance(h.get('finding_ids'),list),id+' finding IDs missing')
  for field,known in [('source_ids',sources),('claim_ids',claims),('tip_ids',tips),('asset_ids',assets),('metric_ids',metrics),('open_item_ids',opens)]:refs(h.get(field),known,id+' '+field)
  need(text(h.get('owner')) and bool(h.get('tasks')) and text(h.get('acceptance')),id+' handoff owner/tasks/acceptance missing')
  for field in ['source_ids','claim_ids','tip_ids','asset_ids','metric_ids','open_item_ids','finding_ids']:
   for ref in h.get(field,[]):need(ref in handoff,id+' handoff lost reference')
 return errors

def validate_skill(root):
 root=Path(root);errors=[];p=root/'SKILL.md'
 if not p.is_file():return ['Missing SKILL.md']
 if not re.match(r'---\nname: enablement-campaign-generator\ndescription: [^\n]+\n---\n',p.read_text()):errors.append('Minimal frontmatter invalid')
 ui=root/'agents/openai.yaml'
 if not ui.is_file() or '$enablement-campaign-generator' not in ui.read_text():errors.append('Missing/stale UI metadata')
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
 print(json.dumps(dict(structural_validation='FAIL' if errors else 'PASS',errors=errors,limits='Declared structure only; no source authentication, semantic quality, tenant test, rendered accessibility, learning/adoption evidence, collection permission or publication authorization.'),indent=2));return bool(errors)
if __name__=='__main__':raise SystemExit(main())
