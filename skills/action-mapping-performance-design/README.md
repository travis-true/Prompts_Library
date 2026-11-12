# action-mapping-performance-design

**Version:** 1.0.0  
**Format:** portable [Agent Skills](https://agentskills.io/specification) folder with `SKILL.md`, references, templates, examples, and evaluation cases.

This is an original, non-official implementation aid inspired by performance consulting and Cathy Moore's public action-mapping framework. It does **not** reproduce *Map It!* and is not affiliated with its author.

## What it does

- **Discover:** Turn a training request into an evidence-based performance problem, observable actions, barrier assessment, and possible interventions.
- **Design:** Turn approved outcomes/actions into a traceable action map and high-level authentic practice proposals.
- **Review:** Audit approved or draft training assets for workplace performance alignment without silently changing their contents.

## Included files

- `SKILL.md` — full runtime instructions and mode routing
- `assets/` — six editable Markdown templates
- `references/` — methodology, scenario design, review rubric, specialist integration
- `examples/` — provisional, non-approved OneNote-style example
- `evals/` — manual trigger and behavioral test cases
- `scripts/validate_skill.py` — local structural/self-contained validation script

## Install or reuse

1. Extract the ZIP; retain the **`action-mapping-performance-design`** folder name and contents.
2. In a tool supporting the Agent Skills specification, add the folder in its skills directory or through its supported importer. Exact installation steps vary by host.
3. Restart/reload skill discovery if required by that tool.
4. Ask for Discover, Design, or Review and supply the current project evidence and constraints.

**Note:** Portability means standards-based files, not guaranteed direct import by every Microsoft 365 Copilot surface. A host may need a separate adapter, agent instruction, or plugin packaging.

## Sample invocations

- `Use action-mapping-performance-design in Discover mode. Analyze this proposed Copilot workshop request; distinguish access, process, and skill barriers. Do not approve production.`
- `Use action-mapping-performance-design in Design mode. Draft AM-001 v0.1 from the attached approved needs brief. Preserve all approvals and holds.`
- `Use action-mapping-performance-design in Review mode. Evaluate this participant workbook for realistic decisions, independent performance evidence, and job-aid support. Do not alter approved wording.`

## Validation

From a shell with Python 3.9 or later:

```sh
python action-mapping-performance-design/scripts/validate_skill.py action-mapping-performance-design
```

For stricter schema verification, the published Agent Skills specification recommends a compatible `skills-ref` validator, when available. The bundled script checks directory naming, required frontmatter, referenced local files, and expected templates, but does not prove behavior inside every host.

## Governance / permissions

No external tools, account actions, content changes, stakeholder contacts, approvals, or automated deployment are performed by these files. They guide a connected agent only within its own host permissions and user authorization. Existing approved designs and evidence limits are preserved.

## Attribution

- Cathy Moore, [action mapping overview](https://blog.cathy-moore.com/action-mapping/)
- Cathy Moore, [workflow at a glance](https://blog.cathy-moore.com/action-mapping-workflow-at-a-glance/)
- [Agent Skills specification](https://agentskills.io/specification)

**License:** Not assigned in this package. The owner can choose distribution terms before publication or sharing.
