#!/usr/bin/env python3
"""Check a readable-outline review record; structural success is not approval."""
import argparse
from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path
import re

SEVERITIES={'Critical','Major','Minor','Enhancement'}
STATES={'Open','Revision proposed','Implemented; verification pending','Verified resolved','Deferred','Reopened'}
DISPOSITIONS={'Meets outline-review criteria','Minor revisions required','Major revision required','Not reviewable'}
QUALITY={f'Q-{n:02}' for n in range(1,13)}


def validate_review(data,root):
    errors=[]
    def need(ok,message):
        if not ok:errors.append(message)
    def text(x):return isinstance(x,str) and bool(x.strip())
    def integer(x):return type(x) is int and x>=0
    def load(path):
        if not text(path):errors.append('Missing local path');return ''
        p=(root/path).resolve()
        if not p.is_relative_to(root.resolve()) or not p.is_file():errors.append('Missing or unsafe local path: '+path);return ''
        return p.read_text(encoding='utf-8')
    def index(values,label):
        need(isinstance(values,list),label+' must be a list')
        out={}
        for item in values if isinstance(values,list) else []:
            if not isinstance(item,dict):errors.append(label+' item must be an object');continue
            id=item.get('id');need(text(id) and id not in out,label+' IDs must be unique and nonempty')
            if text(id):out[id]=item
        return out
    def refs(values,known,label,nonempty=True):
        need(isinstance(values,list) and (bool(values) or not nonempty),label+' must be a reference list')
        if isinstance(values,list):
            need(len(values)==len(set(values)),label+' has duplicate references')
            for v in values:need(v in known,label+': unknown reference '+str(v))
    def evidence(ev,label):
        if not isinstance(ev,dict):errors.append(label+': missing evidence object');return
        body=load(ev.get('path'))
        need(text(ev.get('quote')) and ev.get('quote','') in body,label+': evidence quote not found')
        need(text(ev.get('result')),label+': missing observed result')
    def verification(v,target,label):
        if not isinstance(v,dict):errors.append(label+': closure verification required');return
        need(v.get('artifact_id')==target,label+': closure artifact differs')
        need(v.get('artifact_version')==artifacts.get(target,{}).get('version'),label+': closure version stale')
        need(text(v.get('method')) and text(v.get('reviewer')),label+': closure method/reviewer missing')
        try:date.fromisoformat(v.get('date',''))
        except (TypeError,ValueError):errors.append(label+': invalid verification date')
        evidence(v.get('evidence'),label)
    if not isinstance(data,dict):return ['Review record must be an object']
    need(data.get('schema_version')=='1.1','Unsupported schema version')
    need(text(data.get('review_id')) and text(data.get('review_version')),'Missing review identity/version')
    need(data.get('mode') in ['full-review','review-plus-revision'],'Record requires a full review mode')
    scopes=data.get('scope',[])
    need(isinstance(scopes,list) and 'outline-design' in scopes,'Missing outline-design review scope')
    report=load(data.get('report'))
    need('**Review version:** '+str(data.get('review_version')) in report,'Report version mismatch')
    artifacts=index(data.get('artifacts'),'Artifact')
    bodies={}
    for id,a in artifacts.items():
        need(text(a.get('version')),id+': missing artifact version')
        body=load(a.get('path'));bodies[id]=body
        p=(root/str(a.get('path',''))).resolve()
        if p.is_relative_to(root.resolve()) and p.is_file():
            need(a.get('sha256')==hashlib.sha256(p.read_bytes()).hexdigest(),id+': artifact hash mismatch')
    sources=index(data.get('sources'),'Source')
    for id,s in sources.items():
        need(text(s.get('locator')) and s.get('kind') in ['supplied-fictional','supplied','official','reviewer-recommendation'],id+': missing source kind/locator')
        if s.get('artifact_id'):need(s['artifact_id'] in artifacts,id+': unknown source artifact')
    original=index(data.get('original_objectives'),'Original objective')
    revised=data.get('revised_objective_ids',[])
    need(isinstance(revised,list) and len(revised)==len(set(revised)),'Revised objective IDs invalid')
    for id,o in original.items():
        sid=o.get('source_id');need(sid in sources,id+': objective source missing')
        body=bodies.get(sources.get(sid,{}).get('artifact_id'),'')
        need(text(o.get('quote')) and o.get('quote','') in body,id+': original objective quote missing')
    findings=index(data.get('findings'),'Finding')
    for id,f in findings.items():
        need(f.get('severity') in SEVERITIES,id+': invalid severity')
        need(f.get('status') in STATES,id+': invalid lifecycle status')
        need(f.get('criterion_layer') in ['built-in','supplied-requirement'],id+': invalid criterion layer')
        for field in ['severity_rationale','confidence','original_location','impact','recommendation','acceptance_criteria','owner']:
            need(text(f.get(field)),id+': missing '+field)
        original_id=f.get('original_artifact_id');target=f.get('target_artifact_id')
        need(original_id in artifacts and (target in artifacts or data.get('mode')=='full-review' and target is None),id+': unknown original/target artifact')
        ev=f.get('evidence',{});need(isinstance(ev,dict),id+': invalid finding evidence')
        if not isinstance(ev,dict):continue
        refs(ev.get('source_ids'),sources,id+' evidence sources')
        need(ev.get('type') in ['quote','gap','calculation','conflict'],id+': invalid evidence type')
        need(text(ev.get('text')),id+': missing evidence text')
        if ev.get('type')=='quote':need(ev.get('text','') in bodies.get(original_id,''),id+': original evidence quote missing')
        if f.get('status')=='Verified resolved':verification(f.get('verification'),target,id)
        elif f.get('verification'):
            need(isinstance(f['verification'],dict),id+': invalid verification record')
        if f.get('status')=='Deferred':
            d=f.get('deferral',{})
            need(all(text(d.get(x)) for x in ['decision_owner','date','rationale','residual_impact','trigger','next_owner']),id+': incomplete deferral decision')
    counts=dict(Counter(f.get('severity') for f in findings.values()))
    expected={s:counts.get(s,0) for s in SEVERITIES}
    need(data.get('severity_counts')==expected,'Severity counts differ from findings')
    for sev,n in expected.items():need(f'{sev}: {n}' in report,'Report severity count mismatch: '+sev)
    treatments=data.get('objective_treatments',[])
    treated=[]
    for t in treatments:
        oid=t.get('original_objective_id');treated.append(oid)
        need(oid in original,'Unknown original objective in treatment')
        need(t.get('treatment') in ['Preserved','Revised','Deferred','Removed'],'Invalid objective treatment')
        refs(t.get('finding_ids'),findings,'Objective treatment findings')
        refs(t.get('source_ids'),sources,'Objective treatment sources')
        need(text(t.get('rationale')) and text(t.get('decision_owner')),'Objective treatment rationale/owner missing')
        need(t.get('decision_status') in ['Pending','Confirmed'],'Invalid objective decision status')
        refs(t.get('revised_objective_ids',[]),revised,'Revised objective treatment',nonempty=t.get('treatment') in ['Preserved','Revised'])
    if data.get('mode')=='review-plus-revision':
        need(len(treated)==len(set(treated)) and set(treated)==set(original),'Every original objective must have exactly one treatment')
    else:
        need(not treatments and not revised,'Full review does not require or silently create objective revisions')
    if data.get('mode')=='review-plus-revision':
        mapped={id for t in treatments for id in t.get('revised_objective_ids',[])}
        need(mapped==set(revised),'Unmapped revised objective')
    gaps=index(data.get('evidence_gaps'),'Gap')
    for id,g in gaps.items():
        need(text(g.get('description')) and text(g.get('owner')) and type(g.get('material')) is bool,id+': invalid gap description/owner/materiality')
        need(g.get('status') in ['Open','Resolved'],id+': invalid gap status')
        if g.get('status')=='Resolved':
            need(isinstance(g.get('evidence'),dict),id+': resolved gap needs evidence')
            if isinstance(g.get('evidence'),dict):evidence(g['evidence'],id)
    for label in ['original_timing']+(['proposed_timing'] if data.get('mode')=='review-plus-revision' else []):
        t=data.get(label,{})
        need(t.get('artifact_id') in artifacts,label+': artifact missing')
        rows=t.get('agenda',[]);need(isinstance(rows,list) and bool(rows),label+': agenda missing')
        valid=isinstance(rows,list) and all(isinstance(row,dict) and type(row.get('minutes')) is int and row['minutes']>0 for row in rows)
        need(valid,label+': invalid agenda rows')
        if not valid:continue
        total=sum(row['minutes'] for row in rows)
        need(integer(t.get('session_minutes')) and t.get('session_minutes',0)>0,label+': invalid session duration')
        need(total==t.get('row_total'),label+': agenda arithmetic mismatch')
        if integer(t.get('session_minutes')):need(t.get('variance')==total-t['session_minutes'],label+': variance mismatch')
        for row in rows:need(row.get('kind') in ['instruction','break','administration','unknown'],label+': invalid row kind')
        if label=='proposed_timing':
            elapsed=0
            for row in rows:
                need(row.get('kind')!='unknown',label+': proposed allocation unknown')
                need(type(row.get('start_minute')) is int and row['start_minute']==elapsed,label+': start minute mismatch')
                refs(row.get('objective_ids',[]),revised,label+' row objectives',nonempty=False)
                elapsed+=row['minutes']
            for field,kind in [('break_minutes','break'),('administration_minutes','administration'),('instructional_minutes','instruction')]:
                need(t.get(field)==sum(row['minutes'] for row in rows if row['kind']==kind),label+': '+field+' mismatch')
            body=bodies.get(t.get('artifact_id'),'')
            markdown=re.findall(r'^\| (\d+) \| (\d+) \| (Instruction|Break|Administration) \|',body,re.M)
            need(len(markdown)==len(rows),label+': Markdown row count mismatch')
            for (start,mins,kind),row in zip(markdown,rows):need(int(start)==row['start_minute'] and int(mins)==row['minutes'] and kind.lower()==row['kind'],label+': Markdown row differs')
            for field,title in [('row_total','Session total'),('break_minutes','Break minutes'),('administration_minutes','Fixed administration'),('instructional_minutes','Instructional minutes'),('variance','Variance')]:
                need(f'**{title}:** {t.get(field)} minutes' in body,label+': Markdown totals differ: '+title)
        else:
            body=bodies.get(t.get('artifact_id'),'')
            minutes=[int(x) for x in re.findall(r'^\| (\d+) \|',body,re.M)]
            need(minutes==[row['minutes'] for row in rows],label+': source agenda differs')
            if any(row.get('kind')=='unknown' for row in rows):need(t.get('instructional_minutes') is None,label+': unknown allocation cannot claim instructional total')
    dispositions=data.get('dispositions',[])
    need(len(dispositions)==len(artifacts),'One disposition per artifact is required')
    need(len({d.get('artifact_id') for d in dispositions})==len(dispositions),'Duplicate disposition artifact')
    domains=index(data.get('domain_checks'),'Domain')
    need(set(domains)=={'accessibility-design','accessibility-rendered','delivery','qualified-review'},'Required domain checks differ')
    for id,d in domains.items():
        need(d.get('status') in ['Pass','Needs revision','Not checked','Not applicable'],id+': invalid domain status')
        if d.get('status')=='Needs revision':
            refs(d.get('finding_ids'),findings,id+' domain findings')
            need(d.get('artifact_id') in artifacts,id+': failing domain artifact missing')
        if d.get('status')=='Pass':evidence(d.get('evidence'),id)
        if d.get('status') in ['Not checked','Not applicable']:need(text(d.get('rationale')),id+': unchecked/exclusion rationale missing')
    for d in dispositions:
        aid=d.get('artifact_id');value=d.get('value');need(aid in artifacts and value in DISPOSITIONS,'Invalid disposition artifact/value')
        refs(d.get('blocking_finding_ids',[]),findings,'Disposition blockers',nonempty=False)
        relevant=[f for f in findings.values() if f.get('original_artifact_id')==aid or f.get('target_artifact_id')==aid and f.get('status')!='Verified resolved']
        major={f['id'] for f in relevant if f.get('severity') in ['Critical','Major']}
        minor={f['id'] for f in relevant if f.get('severity')=='Minor'}
        need(major.issubset(set(d.get('blocking_finding_ids',[]))),'Disposition omits material finding IDs')
        if major:need(value in ['Major revision required','Not reviewable'],'Favorable disposition with unresolved Major/Critical findings')
        if any(g.get('material') and g.get('status')!='Resolved' for g in gaps.values()) or any(t.get('decision_status')=='Pending' and t.get('treatment') in ['Deferred','Removed'] for t in treatments):
            need(value in ['Major revision required','Not reviewable'],'Favorable disposition with material decision gaps')
        if value=='Meets outline-review criteria':need(not minor,'Meets criteria has unresolved Minor findings')
        if value in ['Meets outline-review criteria','Minor revisions required']:
            need(all(q.get('status')=='Pass' for q in data.get('quality_checks',[]) if q.get('applicable')),'Favorable disposition with incomplete review checks')
            for key,scope in [('accessibility-rendered','rendered-materials'),('delivery','delivery'),('qualified-review','qualified-review')]:
                if scope in scopes:need(domains.get(key,{}).get('status')=='Pass','Favorable expanded scope with unverified '+key)
        label='Original' if aid==data.get('original_timing',{}).get('artifact_id') else 'Proposed'
        need(f'**{label} disposition:** {value}' in report,'Report disposition mismatch: '+label)
    handoff=data.get('handoff',{})
    need(handoff.get('destination')=='live-training-session-design','Wrong handoff destination')
    need(handoff.get('status')=='Prepared; not executed','Handoff must not claim execution without separate external evidence')
    refs(handoff.get('artifact_ids'),artifacts,'Handoff artifacts');refs(handoff.get('source_ids'),sources,'Handoff sources')
    body=load(handoff.get('path'));tasks=index(handoff.get('tasks'),'Handoff task');coverage=set()
    for id,task in tasks.items():
        refs(task.get('finding_ids'),findings,id+' findings');coverage.update(task.get('finding_ids',[]))
        refs(task.get('source_ids'),sources,id+' sources');refs(task.get('objective_ids'),original,id+' objectives')
        refs(task.get('dependencies',[]),set(tasks)|set(gaps),id+' dependencies',nonempty=False)
        for field in ['task','acceptance_criteria','owner']:need(text(task.get(field)),id+': missing '+field)
        need(task.get('status') in ['Open','In progress','Ready for verification'],id+': invalid task status')
        need(id in body and task.get('acceptance_criteria','') in body,id+': handoff Markdown differs')
        for ref in task.get('finding_ids',[])+task.get('source_ids',[])+task.get('objective_ids',[]):need(ref in body,id+': handoff lost reference '+ref)
    need({f['id'] for f in findings.values() if f.get('severity')!='Enhancement' and f.get('status')!='Verified resolved'}.issubset(coverage),'Handoff misses unresolved defect findings')
    refs(handoff.get('scope_decision_ids',[]),gaps,'Handoff decisions',nonempty=False)
    need({g['id'] for g in gaps.values() if g.get('material') and g.get('status')!='Resolved'}.issubset(set(handoff.get('scope_decision_ids',[]))),'Handoff misses material scope decisions')
    for a in artifacts.values():need(a.get('sha256','') in body,'Handoff artifact hash differs')
    # Detect dependency cycles among tasks; gap dependencies are external decisions.
    visiting=set();done=set()
    def visit(id):
        if id in visiting:errors.append('Cyclic handoff task dependencies');return
        if id in done:return
        visiting.add(id)
        for dep in tasks[id].get('dependencies',[]):
            if dep in tasks:visit(dep)
        visiting.remove(id);done.add(id)
    for id in tasks:visit(id)
    quality=index(data.get('quality_checks'),'Quality check');need(set(quality)==QUALITY,'All twelve review-quality checks required')
    for id,q in quality.items():
        need(type(q.get('applicable')) is bool,id+': missing applicability')
        if not q.get('applicable'):
            need(q.get('status')=='Not applicable' and text(q.get('rationale')),id+': excluded check needs rationale and no Pass');continue
        need(q.get('status') in ['Pass','Needs revision','Not checked'],id+': invalid check status')
        if q.get('status')=='Pass':
            need(q.get('review_version')==data.get('review_version'),id+': stale review evidence')
            need(text(q.get('method')) and text(q.get('reviewer')),id+': Pass requires method and reviewer')
            try:date.fromisoformat(q.get('date',''))
            except (ValueError,TypeError):errors.append(id+': Pass requires actual ISO date')
            evidence(q.get('evidence'),id)
    bridge=data.get('qa_bridge',{})
    need(bridge.get('scope')=='outline-design','QA bridge must state outline-design scope')
    candidates=bridge.get('candidate_results',[])
    need(len(candidates)==len(artifacts) and {x.get('artifact_id') for x in candidates}==set(artifacts),'QA bridge candidate coverage differs')
    for candidate in candidates:
        aid=candidate.get('artifact_id')
        disposition=next((x.get('value') for x in dispositions if x.get('artifact_id')==aid),None)
        if disposition=='Major revision required':need(candidate.get('qa_status')=='QA FAIL','QA bridge cannot pass unresolved material outline defects')
        elif disposition=='Not reviewable':need(candidate.get('qa_status')=='NOT VERIFIED','QA bridge unreviewable scope must be NOT VERIFIED')
        else:need(candidate.get('qa_status') in ['QA PASS','QA PASS WITH CONDITIONS','QA FAIL','NOT VERIFIED'],'QA bridge invalid QA status')
        if disposition=='Minor revisions required':
            need(candidate.get('qa_status')!='QA PASS','QA bridge cannot give unconditional PASS with required minor revisions')
            if candidate.get('qa_status')=='QA PASS WITH CONDITIONS':
                conditions=candidate.get('conditions',[])
                need(isinstance(conditions,list) and bool(conditions),'QA bridge conditions require explicit acceptance records')
                for condition in conditions:
                    need(all(text(condition.get(k)) for k in ['owner','accepting_authority','scope','nonblocking_rationale']),'QA bridge condition ownership/acceptance missing')
                    try:date.fromisoformat(condition.get('date',''))
                    except (ValueError,TypeError):errors.append('QA bridge condition acceptance date invalid')
                    evidence(condition.get('evidence'),'QA bridge condition')
        # This contract is advisory: external authorization and release execution are outside its evidence model.
        need(candidate.get('authorization')=='AUTHORIZATION NOT VERIFIED','QA bridge cannot infer release authorization')
        need(candidate.get('release_executed') is False,'QA bridge cannot infer release execution')
    mapping=bridge.get('defect_map',[])
    need(len(mapping)==len(findings) and {x.get('finding_id') for x in mapping}==set(findings),'QA bridge finding coverage differs')
    need(len({x.get('qa_defect_id') for x in mapping})==len(mapping),'QA bridge defect aliases must be unique')
    severity_map={'Critical':'CRITICAL','Major':'MAJOR','Minor':'MINOR','Enhancement':'NOTE'}
    for row in mapping:
        finding=findings.get(row.get('finding_id'),{})
        need(text(row.get('qa_defect_id')) and row.get('qa_severity')==severity_map.get(finding.get('severity')),'QA bridge severity mapping differs')
    return errors


def validate_package(root):
    errors=[];skill=root/'SKILL.md'
    if not skill.is_file():return ['Missing SKILL.md']
    if not re.match(r'---\nname: qa-and-release-assets\ndescription: .+\n---\n',skill.read_text()):errors.append('Minimal skill frontmatter invalid')
    if not (root/'agents/openai.yaml').is_file():errors.append('Missing UI metadata')
    for p in root.rglob('*.md'):
        prose=re.sub(r'```[\s\S]*?```','',p.read_text())
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',prose):
            if re.match(r'(?:https?://|mailto:|#)',target):continue
            dest=(p.parent/target.split('#')[0]).resolve()
            if not dest.is_relative_to(root.resolve()) or not dest.exists():errors.append(str(p.relative_to(root))+': missing/unsafe link '+target)
    return errors


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--review',type=Path);p.add_argument('--root',type=Path);p.add_argument('--package',type=Path);args=p.parse_args();errors=[]
    try:
        if args.review:errors+=validate_review(json.loads(args.review.read_text()),(args.root or args.review.parent).resolve())
        if args.package:errors+=validate_package(args.package.resolve())
        if not args.review and not args.package:p.error('Supply --review and/or --package')
    except (ValueError,TypeError,KeyError,AttributeError,OSError) as exc:errors.append('Malformed record or unavailable file: '+str(exc))
    print(json.dumps(dict(structural_validation='FAIL' if errors else 'PASS',errors=errors,limits='Checks structure, arithmetic, hashes, ID coverage and recorded consistency. Does not establish factual truth, severity judgment, actual verification, accessibility, delivery or approval.'),indent=2))
    return 1 if errors else 0
if __name__=='__main__':raise SystemExit(main())
