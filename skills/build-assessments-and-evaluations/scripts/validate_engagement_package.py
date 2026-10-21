#!/usr/bin/env python3
"""Validate local engagement-package structure; never infer proficiency or approve use."""
import argparse
from datetime import date
import json
from pathlib import Path
import re

STATES={'Draft complete; review required','Needs revision','Planning framework only','Ready for use'}
STAKES={'unresolved','low-stakes-practice','proficiency-check','high-stakes-qualification'}
SIGNALS=r'certific|authoriz|employment|eligib|job qualification|hiring|promotion|disciplin|continued employment'


def validate_record(d,root):
    errors=[]
    def need(ok,msg):
        if not ok:errors.append(msg)
    def text(x):return isinstance(x,str) and bool(x.strip())
    def integer(x):return type(x) is int and x>=0
    def load(path):
        if not text(path):errors.append('Missing local file path');return ''
        p=(root/path).resolve()
        if not p.is_relative_to(root.resolve()) or not p.is_file():errors.append('Missing or unsafe local path: '+path);return ''
        return p.read_text(encoding='utf-8')
    def index(values,label):
        need(isinstance(values,list),label+' must be a list');out={}
        for item in values if isinstance(values,list) else []:
            if not isinstance(item,dict):errors.append(label+' item must be object');continue
            id=item.get('id');need(text(id) and id not in out,label+' IDs must be unique/nonempty')
            if text(id):out[id]=item
        return out
    def refs(values,known,label):
        need(isinstance(values,list) and bool(values),label+' must be nonempty references')
        for id in values if isinstance(values,list) else []:need(id in known,label+': unknown reference '+str(id))
    if not isinstance(d,dict):return ['Record must be an object']
    need(d.get('schema_version')=='1.1','Unsupported schema version')
    version=d.get('artifact_version');need(text(version),'Missing artifact version')
    state=d.get('release_state');need(state in STATES,'Invalid release state')
    body=load(d.get('document'));need(f'**Version:** {version}' in body,'Document version differs');need(f'**Release state:** {state}' in body,'Document release state differs')
    stakes=d.get('stakes',{});classification=stakes.get('classification');need(classification in STAKES,'Invalid stakes classification')
    signals=stakes.get('consequence_signals',[])
    need(isinstance(signals,list),'Consequence signals must be a list')
    has_signal=bool(signals) or bool(re.search(SIGNALS,str(d.get('intended_use','')),re.I))
    answered=stakes.get('clarification_status')=='Answered' and text(stakes.get('clarification_answer')) and stakes.get('clarified_use') in ['practice-only-no-consequences','proficiency-decision','consequential-decision']
    if has_signal and not answered:
        need(stakes.get('clarification_required') is True,'Consequential signals require clarification')
        need(classification=='unresolved','Unknown consequential stakes cannot default to low stakes')
        need(stakes.get('consequential_decisions_enabled') is False,'Unresolved consequences must block decisions')
        need(state!='Ready for use','Unresolved consequential stakes block readiness')
    if has_signal and classification=='low-stakes-practice':need(answered and stakes.get('clarified_use')=='practice-only-no-consequences' and stakes.get('consequential_decisions_enabled') is False,'Practice classification requires explicit nonconsequential clarification')
    need(type(stakes.get('consequential_decisions_enabled')) is bool,'Decision enablement must be explicit')
    if classification=='unresolved':need(stakes.get('consequential_decisions_enabled') is False,'Unresolved stakes cannot enable decisions')
    objectives=index(d.get('objectives'),'Objective');sources=index(d.get('sources'),'Source');standards=index(d.get('standards'),'Standard')
    for id,s in sources.items():need(text(s.get('version')) and text(s.get('locator')),id+': missing source version/locator');load(s.get('path'))
    learner_text='\n'.join(load(path) for path in {a.get('learner_path') for a in d.get('assets',[]) if isinstance(a,dict) and text(a.get('learner_path'))})
    for id,o in objectives.items():need(text(o.get('text')) and o.get('text','') in learner_text,id+': missing objective text')
    modules=index(d.get('agenda'),'Agenda');elapsed=0;sums={'instruction':0,'break':0,'administration':0}
    for id,m in modules.items():
        mins=m.get('minutes');need(type(mins) is int and mins>0,id+': invalid minutes');need(m.get('kind') in sums,id+': invalid kind');need(m.get('start_minute')==elapsed,id+': start minute mismatch')
        if type(mins) is int and mins>0:
            elapsed+=mins
            if m.get('kind') in sums:sums[m['kind']]+=mins
    need(elapsed==d.get('total_minutes'),'Agenda total differs')
    for field,kind in [('break_minutes','break'),('administration_minutes','administration'),('instructional_minutes','instruction')]:need(d.get(field)==sums[kind],field+' differs')
    rows=re.findall(r'^\| (M-\d+|B-\d+) \| (\d+) \| (\d+) \| (instruction|break|administration) \|',body,re.M)
    need(len(rows)==len(modules),'Markdown agenda count differs')
    for (id,start,mins,kind),m in zip(rows,modules.values()):need(id==m['id'] and int(start)==m['start_minute'] and int(mins)==m['minutes'] and kind==m['kind'],'Markdown agenda differs')
    for field,label in [('total_minutes','Session total'),('break_minutes','Break minutes'),('administration_minutes','Fixed administration'),('instructional_minutes','Instructional minutes'),('embedded_minutes','Embedded asset time')]:need(f'**{label}:** {d.get(field)} minutes' in body,'Markdown accounting differs: '+label)
    fallbacks=index(d.get('fallbacks'),'Fallback');assets=index(d.get('assets'),'Asset');placed={id:[] for id in modules};embedded=0;covered=set()
    for id,a in assets.items():
        need(a.get('kind') in ['learning','support','evaluation'],id+': invalid asset kind')
        if a.get('kind')=='learning':refs(a.get('objective_ids'),objectives,id+' objectives');covered.update(a.get('objective_ids',[]))
        else:need(text(a.get('support_purpose')) or text(a.get('evaluation_question')),id+': support/evaluation purpose required')
        refs(a.get('source_ids'),sources,id+' sources')
        for field in ['version','title','difficulty','delivery_mode','evidence','review_status','owner','technology']:need(text(a.get(field)),id+': metadata missing '+field)
        need(a.get('stake') in STAKES,id+': invalid asset stake')
        need(type(a.get('minutes')) is int and a['minutes']>0,id+': invalid duration')
        learner=load(a.get('learner_path'));key=load(a.get('key_path'))
        need(f'**Version:** {version}' in learner and f'**Version:** {version}' in key,id+': learner/key version differs')
        need(text(a.get('learner_prompt_quote')) and a.get('learner_prompt_quote','') in learner,id+': missing learner prompt')
        for fact in a.get('required_fact_quotes',[]):need(text(fact) and fact in learner,id+': required fact missing')
        need(bool(a.get('required_fact_quotes')),id+': required facts must be declared')
        need(text(a.get('key_quote')) and a.get('key_quote','') in key,id+': answer key reference missing')
        need('Facilitator-only keys' not in learner and 'SCN-001 model' not in learner,id+': learner file contains key material')
        need(text(a.get('feedback_quote')) and a.get('feedback_quote','') in key,id+': feedback missing')
        if a.get('retry_asset_id'):need(a['retry_asset_id'] in assets,id+': unknown retry asset')
        criteria=index(a.get('criteria'),id+' criteria');need(bool(criteria),id+': criteria missing')
        for cid,c in criteria.items():need(text(c.get('description')) and type(c.get('critical')) is bool and type(c.get('max_points')) is int and c['max_points']>0,id+'/'+cid+': invalid criterion')
        rule=a.get('decision_rule')
        if rule is None:
            need(a.get('classification')=='No proficiency decision',id+': absent decision rule cannot classify proficiency')
        else:
            sid=rule.get('standard_id');std=standards.get(sid,{})
            need(bool(std) and std.get('authorized') is True and text(std.get('authority')) and text(std.get('source_id')),id+': decision rule needs authorized standard')
            need(std.get('source_id') in sources,id+': standard source unknown')
            need(std.get('artifact_version')==version,id+': standard version differs')
            need(rule.get('critical_rule')=='all',id+': critical criteria cannot be compensated')
            maximum=sum(c['max_points'] for c in criteria.values())
            need(type(rule.get('threshold')) is int and 0<rule['threshold']<=maximum,id+': threshold invalid')
            need(std.get('threshold')==rule.get('threshold') and std.get('critical_rule')=='all' and id in std.get('asset_ids',[]),id+': rule differs from authorized standard scope/threshold')
            ev=std.get('evidence') or {};standard_text=load(ev.get('path'))
            need(text(ev.get('quote')) and ev.get('quote','') in standard_text,id+': standard evidence missing')
            if stakes.get('consequential_decisions_enabled') is False:need(a.get('classification')=='No proficiency decision',id+': disabled decision cannot classify proficiency')
        placement=a.get('placement');need(placement in ['embedded','follow-up','additional'],id+': invalid placement')
        if placement=='embedded':
            mid=a.get('parent_module');module=modules.get(mid);offset=a.get('offset_minutes')
            need(bool(module) and module.get('kind')=='instruction',id+': activity parent must be instruction')
            need(integer(offset),id+': embedded offset invalid')
            if module and integer(offset) and type(a.get('minutes')) is int:
                need(offset+a['minutes']<=module['minutes'],id+': activity exceeds parent module')
                placed[mid].append((offset,offset+a['minutes'],id));embedded+=a['minutes']
        elif placement=='additional':errors.append(id+': additional activity requires parent agenda reallocation')
        need(a.get('fallback_id') in fallbacks,id+': fallback reference missing')
        fb=fallbacks.get(a.get('fallback_id'),{})
        if rule is not None and stakes.get('consequential_decisions_enabled') is True:need(fb.get('classification')=='Equivalent' and fb.get('verification_status')=='Verified' and fb.get('proficiency_use_allowed') is True,id+': unverified/non-equivalent fallback cannot support proficiency decision')
    need(covered==set(objectives),'Objective evidence coverage differs')
    need(embedded==d.get('embedded_minutes'),'Embedded total differs; do not double-count')
    for intervals in placed.values():
        ordered=sorted(intervals)
        for before,after in zip(ordered,ordered[1:]):need(before[1]<=after[0],'Embedded activities overlap: '+before[2]+'/'+after[2])
    for id,fb in fallbacks.items():
        refs(fb.get('objective_ids'),objectives,id+' objectives');need(fb.get('classification') in ['Equivalent','Partially equivalent','Not equivalent'],id+': invalid equivalence')
        need(fb.get('verification_status') in ['Verified','Not checked','Needs revision'],id+': invalid verification status')
        need(text(fb.get('rationale')),id+': equivalence rationale required')
        if fb.get('classification')=='Equivalent':need(fb.get('primary_construct')==fb.get('fallback_construct') and not fb.get('omitted_evidence'),id+': Equivalent claim loses construct/evidence')
        if fb.get('verification_status')=='Verified':
            verification=fb.get('verification') or {};ev=verification.get('evidence') or {};verified_text=load(ev.get('path'))
            need(verification.get('artifact_version')==version and text(verification.get('reviewer')) and text(verification.get('method')),id+': verified fallback needs version/reviewer/method')
            need(text(ev.get('quote')) and ev.get('quote','') in verified_text and text(ev.get('result')),id+': verified fallback evidence missing')
            try:date.fromisoformat(verification.get('date',''))
            except (ValueError,TypeError):errors.append(id+': verified fallback date invalid')
        if fb.get('classification')!='Equivalent' or fb.get('verification_status')!='Verified':need(fb.get('proficiency_use_allowed') is False,id+': limited fallback cannot claim proficiency use')
    if stakes.get('consequential_decisions_enabled') is True:
        need(classification in ['proficiency-check','high-stakes-qualification'] and state=='Ready for use','Actual decision use requires resolved stakes and verified readiness')
        need(any(a.get('decision_rule') is not None for a in assets.values()),'Actual decision use requires a supplied standard/rule')
    obs=d.get('observation',{})
    need(all(type(obs.get(k)) is int and obs[k]>0 for k in ['learners','scoring_minutes_per_response','total_scoring_minutes']),'Observation workload missing')
    if all(type(obs.get(k)) is int for k in ['learners','scoring_minutes_per_response','total_scoring_minutes']):need(obs['learners']*obs['scoring_minutes_per_response']==obs['total_scoring_minutes'],'Individual scoring workload differs')
    need(obs.get('individual_collection') is True and obs.get('unobserved_result')=='Not observed','Sampling cannot establish individual performance')
    need(obs.get('scoring_placement')=='Outside session' or obs.get('total_scoring_minutes',0)<=d.get('instructional_minutes',0),'Scoring workload exceeds session')
    evaluation=index(d.get('evaluation'),'Evaluation')
    for id,ev in evaluation.items():
        need(type(ev.get('selected')) is bool,id+': evaluation selection required')
        if ev.get('selected'):
            for field in ['question','indicator','owner','timing','analysis','action','limits']:need(text(ev.get(field)),id+': selected measure missing '+field)
            refs(ev.get('source_asset_ids'),assets,id+' evaluation assets')
        else:need(text(ev.get('rationale')),id+': unselected measure needs rationale')
    checks=index(d.get('quality_checks'),'Quality')
    need(set(checks)=={f'Q-{i:02}' for i in range(1,13)},'All twelve quality checks required')
    for id,q in checks.items():
        need(type(q.get('applicable')) is bool,id+': applicability missing')
        if not q.get('applicable'):need(q.get('status')=='Not applicable' and text(q.get('rationale')),id+': exclusion cannot be Pass');continue
        need(q.get('status') in ['Pass','Needs revision','Not checked'],id+': status invalid')
        if q.get('status')=='Pass':
            need(q.get('artifact_version')==version and text(q.get('method')) and text(q.get('reviewer')),id+': Pass metadata/version missing')
            try:date.fromisoformat(q.get('date',''))
            except (ValueError,TypeError):errors.append(id+': Pass date invalid')
            ev=q.get('evidence') or {};s=load(ev.get('path'));need(text(ev.get('quote')) and ev.get('quote','') in s and text(ev.get('result')),id+': actual evidence missing')
    if classification=='high-stakes-qualification' or has_signal and not answered:need(checks.get('Q-12',{}).get('applicable') is True,'Consequential governance check cannot be excluded')
    opens=index(d.get('open_items'),'Open item')
    for id,o in opens.items():need(text(o.get('owner')) and text(o.get('description')) and type(o.get('blocks_current_use')) is bool and o.get('status') in ['Open','Resolved'],id+': invalid open-item record')
    if state=='Ready for use':
        need(all(q.get('status')=='Pass' for q in checks.values() if q.get('applicable')),'Readiness has unperformed/failed checks')
        need(not any(o.get('blocks_current_use') and o.get('status')!='Resolved' for o in opens.values()),'Readiness has blocking open items')
    if any(q.get('status')=='Needs revision' for q in checks.values() if q.get('applicable')):need(state=='Needs revision','Known defect requires Needs revision state')
    handoffs=index(d.get('handoffs'),'Handoff');need({h.get('destination') for h in handoffs.values()}=={'live-training-session-design','qa-and-release-assets'},'Production and QA handoff destinations differ')
    handoff_body=load(d.get('handoff_document'))
    for id,h in handoffs.items():
        need(h.get('status')=='Prepared; not executed',id+': handoff cannot imply execution')
        refs(h.get('asset_ids'),assets,id+' assets');refs(h.get('source_ids'),sources,id+' sources');refs(h.get('objective_ids'),objectives,id+' objectives')
        need(bool(h.get('tasks')) and text(h.get('acceptance_criteria')),id+': handoff tasks/acceptance missing')
        if handoff_body:
            for ref in h.get('asset_ids',[])+h.get('source_ids',[])+h.get('objective_ids',[]):need(ref in handoff_body,id+': handoff lost reference')
    return errors


def validate_skill(root):
    errors=[];p=root/'SKILL.md'
    if not p.is_file():return ['Missing SKILL.md']
    if not re.match(r'---\nname: build-assessments-and-evaluations\ndescription: .+\n---\n',p.read_text()):errors.append('Minimal frontmatter invalid')
    if not (root/'agents/openai.yaml').is_file():errors.append('Missing UI metadata')
    for p in root.rglob('*.md'):
        prose=re.sub(r'```[\s\S]*?```','',p.read_text())
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',prose):
            if re.match(r'(?:https?://|mailto:|#)',target):continue
            dest=(p.parent/target.split('#')[0]).resolve()
            if not dest.is_relative_to(root.resolve()) or not dest.exists():errors.append(str(p.relative_to(root))+': missing/unsafe link '+target)
    return errors


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--record',type=Path);p.add_argument('--root',type=Path);p.add_argument('--skill',type=Path);a=p.parse_args();errors=[]
    try:
        if a.record:errors+=validate_record(json.loads(a.record.read_text()),(a.root or a.record.parent).resolve())
        if a.skill:errors+=validate_skill(a.skill.resolve())
        if not a.record and not a.skill:p.error('Supply --record and/or --skill')
    except (ValueError,TypeError,KeyError,AttributeError,OSError) as exc:errors.append('Malformed record or unreadable file: '+str(exc))
    print(json.dumps(dict(structural_validation='FAIL' if errors else 'PASS',errors=errors,limits='Checks declared structure, timing, references, scoring authority and evidence consistency. Does not authenticate standards/reviews, judge semantic equivalence, observe learners, test accessibility or authorize use.'),indent=2))
    return 1 if errors else 0
if __name__=='__main__':raise SystemExit(main())
