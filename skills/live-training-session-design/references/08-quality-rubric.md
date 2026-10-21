# Quality rubric and release gate

## Applicability and evidence
Record each check separately. Use `applicable: false` with a specific rationale when a check genuinely does not apply; leave its status and evidence empty. Never present exclusion as a tested Pass. For applicable checks use Pass, Needs revision, or Not checked.

Record: check ID, applicability/rationale, status, method, evidence location and observed result, reviewer identity/role, review date, artifact version, corrective action, owner, retest status. A Pass requires evidence for that exact artifact version. A designed feature, planned check, checklist tick or plausible statement is not proof of execution. Missing or stale evidence becomes Not checked. Do not invent reviewer names, approvals or completed tests.

## Required check IDs

| ID | Check | Required evidence |
| --- | --- | --- |
| alignment | Performance and objective alignment | Each objective linked to instruction, practice and assessment |
| timing | Timing accuracy | Total, breaks, administration, row sum, instruction sum, module substeps and overload review |
| sources | Source traceability | Source IDs, versions, sections, treatment, unresolved conflicts and recommendations |
| assessment | Activities and assessment | Complete scenario inputs, learner action, answer key, critical criteria, threshold, feedback and remediation |
| accessibility-design | Accessible content design | Headings, instructions, equivalent participation and assessment design reviewed |
| accessibility-rendered | Actual materials accessibility | Check actual files for contrast, text size, reading order, headers, alternatives and keyboard behavior as applicable |
| facilitator | Facilitator usability | Scannable cues, materials, timings, transitions, expected responses and fallbacks |
| open-items | Placeholders and unresolved items | Each open item has disposition, owner and whether it blocks delivery |
| delivery | Live delivery readiness | Chosen mode, enrollment capacity, materials and delivery-tool checks and a timed walkthrough; designed alternatives alone do not pass |
| qualified-review | Higher-risk content review | Current controlling sources and explicit qualified-review evidence, scope and version |
| software | Software readiness | Actual feature/access tests, environment record, practice assets and tested fallback |

For an outline, explicitly report which build/release checks are not yet applicable to the planning artifact. Do not turn unfinished required work into an exclusion to claim readiness. Assess accessibility-rendered and delivery separately even when the material is Markdown or the course uses paper.

## Release decision
- **Needs revision:** known material defect remains.
- **Planning framework only:** only an outline or unsupported structure exists; content cannot yet support a teachable course.
- **Draft complete; review required:** substantive package exists but applicable checks, external reviews, rendered artifacts or environment tests remain open.
- **Ready for delivery:** all applicable checks Pass with current evidence; no unresolved delivery-blocking item; actual delivery setup verified; required qualified review documented. Unperformed external checks prevent readiness. A validator exit code never grants this status.

Use a separate approval record when actual approval is required: approver identity and role, date, artifact version, decision, scope, evidence location. Never infer approval from review or user preference. Do not claim approved, compliant, certified or legally sufficient without the corresponding authorized evidence. After changes, invalidate affected review evidence and retest.


## Demo component boundary
A demo has [thirteen scoped checks](../templates/demo/quality-report.md), separate from parent course readiness. Keep demo record, course record, actual verification and release authorization distinct. A structural demo PASS or a verified component does not establish readiness for the complete course. Preserve unresolved demo findings as parent integration dependencies.
