"""Validate the published workplace collection without external dependencies."""
import json
import pathlib
import re
import sys
from collections import Counter

root = pathlib.Path(__file__).resolve().parents[1]
errors = []
catalog = json.loads((root / 'catalog.json').read_text())
counts = dict(Counter(item['type'] for item in catalog))
expected = {'prompts': 57, 'skills': 34, 'workflows': 7, 'resources': 7}
if counts != expected:
    errors.append(f'Catalog counts: {counts}; expected {expected}')
paths = [item['path'] for item in catalog]
if len(paths) != len(set(paths)):
    errors.append('Duplicate catalog paths')
for item in catalog:
    path = root / item['path']
    if not path.is_file():
        errors.append(f'Missing catalog file: {path}')
        continue
    text = path.read_text()
    if item['type'] == 'prompts':
        for section in ['Purpose', 'When to use it', 'Copy-ready prompt', 'Customize before running', 'Example output', 'Check before using']:
            if f'## {section}' not in text:
                errors.append(f'{path}: missing section {section}')
        if not re.search(r'```(?:text|txt)\n[\s\S]+?```', text):
            errors.append(f'{path}: missing copy-ready code block')
    if item['type'] == 'skills':
        match = re.match(r'---\nname: ([a-z0-9-]{1,63})\ndescription: (.+)\n---\n', text)
        if not match or match.group(1) != path.parent.name:
            errors.append(f'{path}: invalid skill frontmatter')
        else:
            try:
                if not json.loads(match.group(2)).strip():
                    errors.append(f'{path}: empty skill description')
            except ValueError:
                errors.append(f'{path}: description must be a quoted string')
        if item.get('status') != 'Installed skill import' and '## Workflow guide' not in text:
            errors.append(f'{path}: missing workflow')

for path in root.rglob('*.md'):
    text = path.read_text()
    rel = path.relative_to(root)
    if re.search(r'notion-file-block://|https?://(?:app\.)?notion\.(?:com|so)|<(?:mention|callout|table|tr|td|database|file|page)\b', text):
        errors.append(f'{rel}: unresolved source markup or link')
    if rel.parts[0] in ['prompts', 'skills', 'workflows', 'resources', 'planned']:
        if re.search(r'\b(?:education|educator|educators|student|students|teacher|teachers|classroom|school|homework|families|fractions)\b', text, re.I):
            errors.append(f'{rel}: residual non-workplace context')
    # Check prose links only; examples may legitimately contain Markdown syntax.
    prose = re.sub(r'```[\s\S]*?```', '', text)
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', prose):
        if re.match(r'(?:https?://|mailto:|#)', target):
            continue
        dest = (path.parent / target.split('#')[0]).resolve()
        if not dest.is_relative_to(root) or not dest.exists():
            errors.append(f'{rel}: broken or unsafe local link {target}')

actual = {str(p.relative_to(root)) for d in expected for p in ((root/d).glob('*/SKILL.md') if d == 'skills' else (root/d).glob('*.md')) if p.name != 'README.md'}
if actual != set(paths):
    errors.append('Catalog and active resource files differ')
if len(list((root/'planned').glob('*.md'))) - 1 != 7:
    errors.append('Expected seven planned idea pages')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('PASS: 105 active resources, 34 skills, 25 workplace prompt adaptations, 7 planned ideas; sections, skill frontmatter, catalog, local links, source markup, and workplace vocabulary checks passed.')
