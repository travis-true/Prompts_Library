#!/usr/bin/env python3
"""Check local package/course structure. Never certify content or grant release approval."""
import argparse
import json
import re
from datetime import date
from pathlib import Path

CHECKS = {'alignment', 'timing', 'sources', 'assessment', 'accessibility-design',
          'accessibility-rendered', 'facilitator', 'open-items', 'delivery',
          'qualified-review', 'software'}
STATES = {'Ready for delivery', 'Draft complete; review required', 'Needs revision', 'Planning framework only'}


def validate_course(data, root):
    errors = []
    def require(ok, message):
        if not ok:
            errors.append(message)
    def text(value):
        return isinstance(value, str) and bool(value.strip())
    def number(value):
        return type(value) is int and value > 0
    def read_local(name):
        require(text(name), 'Missing evidence/document path')
        if not text(name):
            return ''
        path = (root / name).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            errors.append('Missing or unsafe local file: ' + name)
            return ''
        return path.read_text(encoding='utf-8')
    def index(items, label):
        require(isinstance(items, list), label + ' must be a list')
        out = {}
        for item in items if isinstance(items, list) else []:
            require(isinstance(item, dict), label + ' item must be an object')
            if not isinstance(item, dict):
                continue
            key = item.get('id')
            require(text(key) and key not in out, label + ' IDs must be nonempty and unique')
            if text(key):
                out[key] = item
        return out
    require(isinstance(data, dict), 'Course record must be an object')
    if not isinstance(data, dict):
        return errors
    require(data.get('schema_version') == '1.1', 'Unsupported schema_version')
    version = data.get('artifact_version')
    require(text(version), 'Missing artifact_version')
    doc = read_local(data.get('document'))
    require('**Version:** ' + str(version) in doc, 'Document and record versions differ')
    for supporting in data.get('supporting_documents', []):
        body = read_local(supporting.get('path'))
        for quote in supporting.get('required_quotes', []):
            require(text(quote) and quote in body, 'Supporting document is missing required text: ' + str(quote))
        for quote in supporting.get('forbidden_quotes', []):
            require(text(quote) and quote not in body, 'Supporting document contains forbidden text: ' + str(quote))
    state = data.get('release_state')
    require(state in STATES, 'Invalid release state')
    require('**Release state:** ' + str(state) in doc, 'Document and record release states differ')
    modules = index(data.get('agenda'), 'Agenda')
    total = data.get('total_minutes')
    breaks = data.get('break_minutes')
    admin = data.get('administration_minutes')
    require(number(total), 'Total minutes must be a positive integer')
    require(type(breaks) is int and breaks >= 0, 'Break minutes must be a nonnegative integer')
    require(type(admin) is int and admin >= 0, 'Administration minutes must be a nonnegative integer')
    elapsed = 0
    sums = {'instruction': 0, 'break': 0, 'administration': 0}
    for key, m in modules.items():
        minutes, kind = m.get('minutes'), m.get('kind')
        require(number(minutes), key + ': invalid minutes')
        require(kind in sums, key + ': invalid kind')
        require(type(m.get('start_minute')) is int and m.get('start_minute') == elapsed, key + ': start time mismatch')
        steps = m.get('substeps', [])
        require(isinstance(steps, list) and bool(steps), key + ': missing substeps')
        valid_steps = isinstance(steps, list) and all(isinstance(s, dict) and number(s.get('minutes')) and text(s.get('cue')) for s in steps)
        require(valid_steps, key + ': invalid substeps')
        if valid_steps:
            require(sum(s['minutes'] for s in steps) == minutes, key + ': substep minutes differ')
        if number(minutes):
            elapsed += minutes
            if kind in sums:
                sums[kind] += minutes
    require(bool(modules), 'Agenda is empty')
    require(elapsed == total, 'Agenda row total differs from session total')
    require(sums['break'] == breaks, 'Break sum differs from declared breaks')
    require(sums['administration'] == admin, 'Administration sum differs from declared administration')
    if all(type(v) is int for v in [total, breaks, admin]):
        usable = total - breaks - admin
        require(usable > 0 and usable == data.get('instructional_minutes') == sums['instruction'], 'Instructional minutes mismatch')
    labels = {'Agenda total': total, 'Break minutes': breaks, 'Fixed administration minutes': admin,
              'Available instructional time': data.get('instructional_minutes'), 'Allocated instructional time': sums['instruction']}
    for label, value in labels.items():
        require(f'**{label}:** {value} minutes' in doc, 'Markdown timing differs: ' + label)
    # Cross-check displayed agenda rows, not only the self-reported record.
    rows = re.findall(r'^\| (\d+):(\d\d) \| (\d+) \|', doc, re.M)
    require(len(rows) == len(modules), 'Markdown agenda row count differs')
    for row, m in zip(rows, modules.values()):
        require(int(row[0])*60 + int(row[1]) == m.get('start_minute') and int(row[2]) == m.get('minutes'), 'Markdown agenda timing mismatch')
    sources = index(data.get('sources'), 'Sources')
    for key, source in sources.items():
        require(source.get('kind') in ['supplied', 'fictional', 'recommendation', 'official'], key + ': invalid source kind')
        require(text(source.get('locator')), key + ': missing source locator')
        if source.get('local_path'):
            body = read_local(source['local_path'])
            require(text(source.get('quote')) and source.get('quote', '') in body, key + ': source quote not found')
    practices = index(data.get('practices'), 'Practices')
    assessments = index(data.get('assessments'), 'Assessments')
    objectives = index(data.get('objectives'), 'Objectives')
    require(bool(objectives) and bool(practices) and bool(assessments), 'Objectives, practice and assessment cannot be empty')
    for key, p in practices.items():
        require(p.get('source_id') in sources, key + ': unknown source ID')
        facts = p.get('facts', {})
        require(isinstance(facts, dict), key + ': facts must be an object')
        required = p.get('required_facts', [])
        require(isinstance(required, list) and bool(required), key + ': declare required facts')
        for fact in required if isinstance(required, list) else []:
            value = facts.get(fact) if isinstance(facts, dict) else None
            require(text(value), key + ': missing practice fact ' + str(fact))
            if text(value):
                require(value in doc, key + ': practice fact missing from Markdown: ' + str(fact))
        require(text(p.get('prompt_quote')) and p.get('prompt_quote', '') in doc, key + ': practice prompt not found')
    for key, a in assessments.items():
        require(a.get('practice_id') in practices, key + ': unknown practice')
        require(a.get('source_id') in sources, key + ': unknown source')
        criteria = index(a.get('criteria'), key + ' criteria')
        require(bool(criteria) and any(c.get('critical') is True for c in criteria.values()), key + ': at least one critical criterion required')
        maximum = 0
        for cid, criterion in criteria.items():
            require(type(criterion.get('critical')) is bool, key + '/' + cid + ': critical must be boolean')
            require(number(criterion.get('points')) and text(criterion.get('evidence')), key + '/' + cid + ': points/evidence missing')
            if number(criterion.get('points')):
                maximum += criterion['points']
        threshold = a.get('threshold')
        require(number(threshold) and threshold <= maximum, key + ': invalid threshold')
        require(a.get('critical_rule') == 'all' and a.get('invented_requirements_fail') is True, key + ': required critical/invention rules missing')
        for field in ['key_quote', 'feedback_quote', 'retry_quote']:
            require(text(a.get(field)) and a.get(field, '') in doc, key + ': missing grounded ' + field)
        for case in a.get('score_examples', []):
            scores = case.get('scores', {})
            require(set(scores) == set(criteria), key + ': scoring case must cover exactly the criterion IDs')
            valid = all(type(scores.get(cid)) is int and 0 <= scores[cid] <= c['points'] for cid, c in criteria.items())
            require(valid, key + ': invalid scoring values')
            if valid and number(threshold):
                passed = all(scores[cid] == c['points'] for cid, c in criteria.items() if c.get('critical')) and sum(scores.values()) >= threshold and not case.get('invented_requirements', False)
                require(type(case.get('expected_pass')) is bool and case['expected_pass'] == passed, key + ': scoring rule mismatch')
    for key, objective in objectives.items():
        require(text(objective.get('text')) and objective.get('text', '') in doc, key + ': objective missing from Markdown')
        for field, collection in [('instruction_modules', modules), ('practice_ids', practices), ('assessment_ids', assessments)]:
            ids = objective.get(field, [])
            require(isinstance(ids, list) and bool(ids), key + ': missing ' + field)
            for ref in ids if isinstance(ids, list) else []:
                require(ref in collection, key + ': unknown reference ' + str(ref))
                if field == 'instruction_modules' and ref in modules:
                    require(modules[ref].get('kind') == 'instruction', key + ': instruction cannot refer to a break')
    for key, item in {**practices, **assessments}.items():
        require(any(key in o.get('practice_ids', []) + o.get('assessment_ids', []) for o in objectives.values()), key + ': not mapped to an objective')
    for element in data.get('traceability', []):
        require(text(element.get('element')) and element.get('source_ids'), 'Traceability element/source IDs required')
        require(all(ref in sources for ref in element.get('source_ids', [])), 'Traceability contains unknown source ID')
        require(element.get('treatment') in ['Preserved', 'Revised', 'Added', 'Removed'], 'Invalid source treatment')
    require(bool(data.get('traceability')), 'Traceability record is empty')
    opens = index(data.get('open_items'), 'Open items')
    for key, item in opens.items():
        require(text(item.get('owner')) and text(item.get('disposition')) and type(item.get('blocks_delivery')) is bool and type(item.get('resolved')) is bool, key + ': incomplete open-item record')
    found_placeholders = set(re.findall(r'\[(?:TODO|TBD|Enter\b|Insert\b|Course title\b)[^\]\n]*\]', doc, re.I))
    tracked = {x.get('placeholder') for x in opens.values()}
    for token in found_placeholders:
        require(token in tracked, 'Untracked placeholder: ' + token)
    checks = index(data.get('quality_checks'), 'Quality checks')
    require(set(checks) == CHECKS, 'Required quality check IDs differ')
    require(type(data.get('higher_risk')) is bool and type(data.get('software_training')) is bool, 'Risk and software applicability must be explicit booleans')
    for key, check in checks.items():
        applies = check.get('applicable')
        require(type(applies) is bool, key + ': missing applicability')
        must_apply = key not in ['qualified-review', 'software'] or (key == 'qualified-review' and data.get('higher_risk')) or (key == 'software' and data.get('software_training'))
        require(not must_apply or applies is True, key + ': required check cannot be excluded')
        if applies is False:
            require(text(check.get('rationale')) and check.get('status') is None and not check.get('evidence'), key + ': exclusion needs rationale and no Pass/evidence')
            continue
        status = check.get('status')
        require(status in ['Pass', 'Needs revision', 'Not checked'], key + ': invalid status')
        if status == 'Pass':
            require(check.get('artifact_version') == version, key + ': stale review version')
            require(text(check.get('reviewer')) and text(check.get('method')) and bool(check.get('evidence')), key + ': Pass needs reviewer/method/evidence')
            try:
                date.fromisoformat(check.get('date', ''))
            except (ValueError, TypeError):
                errors.append(key + ': Pass needs an actual ISO review date')
            for ev in check.get('evidence', []):
                body = read_local(ev.get('path'))
                require(text(ev.get('quote')) and ev.get('quote', '') in body and text(ev.get('result')), key + ': evidence quote/result missing')
    if state == 'Ready for delivery':
        require(all(c.get('status') == 'Pass' for c in checks.values() if c.get('applicable')), 'Ready state has unperformed or failed checks')
        require(not any(i.get('blocks_delivery') and not i.get('resolved') for i in opens.values()), 'Ready state has unresolved delivery blockers')
    if any(c.get('applicable') and c.get('status') == 'Needs revision' for c in checks.values()):
        require(state == 'Needs revision', 'Material defect requires Needs revision release state')
    return errors


def validate_package(root):
    errors = []
    names = [p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
    skill = root / 'SKILL.md'
    if not skill.is_file():
        return ['Missing SKILL.md']
    s = skill.read_text()
    front = re.match(r'---\nname: ([a-z0-9-]{1,63})\ndescription: (.+)\n---\n', s)
    if not front:
        errors.append('Frontmatter must contain only name and description')
    if not (root / 'agents/openai.yaml').is_file():
        errors.append('Missing agents/openai.yaml')
    for name in names:
        if not name.endswith('.md'):
            continue
        text = (root / name).read_text()
        prose = re.sub(r'```[\s\S]*?```', '', text)
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', prose):
            if re.match(r'(?:https?://|mailto:|#)', target):
                continue
            dest = (root / name).parent / target.split('#')[0]
            if not dest.resolve().is_relative_to(root.resolve()) or not dest.exists():
                errors.append(name + ': missing/unsafe link ' + target)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--course', type=Path)
    parser.add_argument('--root', type=Path, help='Deliverable folder for course-relative paths')
    parser.add_argument('--package', type=Path)
    args = parser.parse_args()
    errors = []
    try:
        if args.course:
            root = (args.root or args.course.parent).resolve()
            errors.extend(validate_course(json.loads(args.course.read_text()), root))
        if args.package:
            errors.extend(validate_package(args.package.resolve()))
        if not args.course and not args.package:
            parser.error('Supply --course and/or --package')
    except (ValueError, TypeError, KeyError, OSError, AttributeError) as exc:
        errors.append('Invalid record or unreadable file: ' + str(exc))
    result = {'structural_validation': 'FAIL' if errors else 'PASS', 'errors': errors,
              'limits': 'Checks structure, arithmetic, references and recorded evidence consistency. Does not verify truth, instructional quality, rendered accessibility, approvals or actual delivery readiness.'}
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
