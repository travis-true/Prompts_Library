#!/usr/bin/env python3
"""Dependency-free structural checks for the bundled Agent Skill.

Usage: python scripts/validate_skill.py /path/to/action-mapping-performance-design
Does not substitute for a host-specific runtime check.
"""
from pathlib import Path
import re
import sys

NAME = 'action-mapping-performance-design'
EXPECTED = [
    'SKILL.md', 'README.md',
    'assets/performance-discovery-gate.md',
    'assets/barrier-diagnostic.md',
    'assets/action-map-template.md',
    'assets/practice-activity-brief.md',
    'assets/review-checklist.md',
    'assets/handoff-packet.md',
    'references/methodology-notes.md',
    'references/scenario-guidance.md',
    'references/quality-rubric.md',
    'references/agent-integration.md',
    'examples/onenote-illustrative.md',
    'evals/test-cases.md',
]


def validate(root: Path) -> list[str]:
    errors = []
    if root.name != NAME:
        errors.append(f'Folder must be named {NAME}, got {root.name!r}')
    skill = root / 'SKILL.md'
    if not skill.is_file():
        return errors + ['Missing SKILL.md']
    content = skill.read_text(encoding='utf-8-sig')
    front = re.match(r'\A---\n(.*?)\n---\n', content, re.S)
    if not front:
        return errors + ['SKILL.md must begin with YAML frontmatter']
    header = front.group(1)
    m_name = re.search(r'^name:\s*(.+?)\s*$', header, re.M)
    m_desc = re.search(r'^description:\s*(.+?)\s*$', header, re.M)
    if not m_name or m_name.group(1).strip('"\'') != NAME:
        errors.append('Missing or incorrect name frontmatter')
    if not m_desc:
        errors.append('Missing description frontmatter')
    else:
        desc = m_desc.group(1).strip('"\'')
        if not 1 <= len(desc) <= 1024:
            errors.append('description must be between 1 and 1024 characters')
    if len(content.splitlines()) >= 500:
        errors.append('SKILL.md exceeds recommended 500 lines')
    for req in EXPECTED:
        if not (root / req).is_file():
            errors.append(f'Missing expected file: {req}')
    for md in root.rglob('*.md'):
        txt = md.read_text(encoding='utf-8')
        # Only ordinary Markdown links, not code references.
        for target in re.findall(r'\]\(([^)]+)\)', txt):
            target = target.split('#')[0]
            if target.startswith(('http://', 'https://', 'mailto:', '#')) or not target:
                continue
            if not (md.parent / target).exists():
                errors.append(f'Broken local link in {md.relative_to(root)}: {target}')
    for marker in ('DISCOVER', 'DESIGN', 'REVIEW', 'Never invent', 'approval'):
        if marker not in content:
            errors.append(f'Missing key instruction marker: {marker}')
    return errors


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent)
    problems = validate(root)
    if problems:
        print('FAIL:')
        for issue in problems:
            print(' -', issue)
        raise SystemExit(1)
    print(f'PASS: {root.name} structure, metadata, files, links, and core controls')
    print(f'{len(list(root.rglob("*")))} total entries')


if __name__ == '__main__':
    main()
