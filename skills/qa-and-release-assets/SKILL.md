---
name: qa-and-release-assets
description: "Inspect, compare, repair when authorized, and gate the release of cross-format deliverables and asset packages. Use when a user requests quality assurance, preflight, accessibility review, source verification, visual inspection, technical validation, regression testing, defect logging, cross-format consistency checks, package integrity checks, release-readiness decisions, exception handling, or controlled handoff for DOCX, PPTX, XLSX, PDF, images, SVG, HTML, JSON, audio, video, captions, transcripts, archives, or mixed training and enablement packages. Also review training outlines for objective alignment, realistic timing, practice, assessment and accessibility-design, using traceable findings, structural validation and a development handoff to Live Training Session Design."
---

# Cross-Format QA and Release

Verify deliverables against their requirements and source baseline, preserve evidence, classify defects, and separate QA results from human release authority. Use the specialized advisory workflow below for training outlines.

**Package revision:** 1.1.0

## Governing rules

- For final-candidate and release QA, inspect final candidate files, not only source text, plans, prompts or generation logs. For advisory outline review, assess the identified outline and keep future-file and delivery checks unverified.
- Use the intended delivery environment or the closest available equivalent.
- Never claim a visual, functional, accessibility, technical, content, or package pass without performing the relevant check.
- Mark unavailable or incomplete checks `NOT VERIFIED`.
- Separate `QA status` from `release authorization`.
- Do not infer approval from a passed check, file publication, delivery, silence, or prior version.
- Do not edit files during review-only mode.
- When fixes are authorized, preserve the original candidate and retest the changed output plus affected regression areas.
- Use authoritative sources and approved requirements as the comparison baseline.
- Preserve unrelated user content and existing approved changes.
- Record evidence, tool or method, candidate version, date, scope, and limitations.
- Treat accessibility, privacy, security, legal, safety, classification, and source-integrity failures as material controls.
- Do not lower required standards to meet a deadline.

## Operating modes

Select one:

1. **Advisory QA:** Review drafts early and identify risks without issuing a release decision.
2. **Final-candidate QA:** Test an identified candidate against the approved baseline.
3. **Repair and retest:** Correct authorized defects, create a new candidate, and rerun affected checks.
4. **Regression QA:** Verify that a change fixed the target issue without damaging previously accepted behavior.
5. **Package QA:** Check a multi-file deliverable, manifest, relationships, and archive integrity.
6. **Release gate:** Produce the evidence-based QA disposition and route it to the named release authority.

For a training outline, agenda or lesson plan, use **Training-outline advisory QA** below, with no rewrite unless requested. For other assets, if the user does not authorize changes, default to Final-candidate QA without repair.

## Training-outline advisory QA

Read [the outline-review mode](references/outline-review-mode.md). Use it to review learner performance, objective alignment, time accounting, practice/scoring, source support, access provisions and facilitator usability before full production. Choose quick triage, full review, or review plus proposed outline only as authorized. Keep the original source and every finding/source/objective ID stable.

A proposed correction is not verified closure. Map every original objective to explicit treatment; preserve tone and other scope unless a decision owner accepts a change. Separate original/proposed judgments, accessibility-design, actual rendered materials, live delivery, QA result, release authority and execution. Never infer a file's accessibility or release readiness from an outline.

Hand off unfinished development to **Live Training Session Design** using [the integrated handoff template](templates/outline-review/development-handoff.md). Preserve original IDs, source/artifact versions/hashes, constraints, decisions, owners, dependencies and acceptance criteria. Preparation is not dispatch or execution; do not generate a competing complete course package.

Use [the outline validator](scripts/validate_outline_review.py) when Python is available. It validates records only; structural PASS grants no favorable QA, finding closure or authorization. If unavailable or the task is text-only, report validation Not checked. Return only the selected review scope; the final-file/release workflow below remains available for actual production assets.

## QA levels

Choose the level according to risk:

- **Baseline:** Low-risk content, visual, accessibility, and openability checks.
- **Standard:** Full content, usability, visual, technical, accessibility, cross-format, and package checks.
- **Controlled:** Standard checks plus traceability, independent review where required, regression, security or compliance evidence, formal exceptions, named approval, version control, and rollback or containment.

Use Controlled QA for high-consequence, regulated, safety-sensitive, contractual, security-sensitive, policy-governed, or externally released assets.

## Workflow

### 1. Establish the QA contract

Determine:

- intended audience, use, environment, and release consequence;
- files, versions, and package boundaries;
- authoritative sources, approved requirements, templates, brand rules, and prior baselines;
- required formats, dimensions, accessibility standard, functionality, and metadata;
- known changes and expected differences;
- QA level and required checks;
- owner, defect decision authority, exception authority, and release authority;
- deadline, publishing destination, rollback, retention, and evidence requirements.

Ask grouped clarifying questions only when missing information changes the required checks or release decision. If the user requests immediate QA, proceed with explicit scope and `NOT VERIFIED` items.

### 2. Freeze and identify the candidate

Assign a unique candidate ID and record:

- filename and path;
- format and size;
- version, status, and date;
- content hash or equivalent fingerprint when available;
- generator or editor;
- source baseline and prior version;
- intended relationships to other files;
- known exclusions and open defects.

Do not issue a final QA result against a moving or unidentified candidate.

### 3. Build the inventory and test matrix

List every required and supplied file. Classify each as:

- final deliverable;
- source;
- template or brand asset;
- support file;
- metadata or manifest;
- evidence;
- temporary or prohibited artifact;
- missing;
- unexpected.

Map every requirement to one or more tests, evidence, owner, and blocking rule. Use stable test IDs such as `TST-001`.

### 4. Confirm inspection capability

For each test, record:

- method or tool;
- whether final bytes can be opened, parsed, rendered, played, recalculated, or executed;
- whether assistive-technology or platform behavior can be tested;
- limitations and substitutions.

If a required format cannot be inspected, do not approximate a pass from the source. Mark the test and affected release dimension `NOT VERIFIED`.

### 5. Run common QA

Read [references/qa-model.md](references/qa-model.md). Check:

- accuracy and source traceability;
- completeness and scope;
- structure, navigation, and usability;
- visual quality and fidelity;
- accessibility and equivalent access;
- technical integrity and interoperability;
- privacy, classification, security, and permitted use;
- brand, template, and format fidelity;
- metadata, ownership, version, status, and maintenance;
- cross-format consistency;
- package completeness and cleanliness.

### 6. Run format-specific QA

Read [references/format-checks.md](references/format-checks.md). Use the format’s native inspection, rendering, recalculation, playback, validation, and accessibility methods where available.

At minimum:

- open or parse the final file;
- render or play every audience-facing unit;
- inspect full-size output;
- test required interactions, links, formulas, media, forms, or navigation;
- verify actual metadata and accessibility structure;
- compare against the approved source and requirements.

### 7. Run accessibility and compliance QA

Read [references/accessibility-and-compliance.md](references/accessibility-and-compliance.md).

Verify applicable:

- semantic structure and reading order;
- headings, titles, labels, table headers, lists, and landmarks;
- contrast, typography, zoom, reflow, and non-color cues;
- alt text, captions, transcripts, audio descriptions, and equivalents;
- keyboard operation, focus order, controls, forms, and error handling;
- language, plain-language, acronym, and instruction clarity;
- privacy, classification, sensitive data, licensing, citations, and retention.

Do not treat an automated accessibility checker as a complete accessibility review.

### 8. Compare formats and versions

For related outputs, compare:

- title, purpose, audience, scope, terminology, claims, steps, decisions, cautions, support, and metadata;
- numbers, formulas, dates, units, labels, hyperlinks, filenames, version, and status;
- page, slide, sheet, scene, section, and asset mappings;
- accessibility alternatives and source citations;
- intentional differences required by the format.

Log semantic differences as defects unless approved. Pixel-level identity is not required when format constraints justify different layouts.

### 9. Validate package integrity

For multi-file packages:

- compare contents to the manifest;
- open every required file;
- identify missing, duplicate, unexpected, stale, hidden, temporary, or prohibited files;
- verify filenames, extensions, folder structure, relative links, references, and dependencies;
- confirm final files match recorded hashes when used;
- test archive extraction and nested package integrity;
- confirm only approved candidates are marked final;
- preserve rollback and prior-baseline information when required.

### 10. Record and classify defects

Assign stable IDs such as `DEF-001`. Record:

- affected candidate, location, and requirement;
- observed result and evidence;
- expected result;
- severity;
- affected audience and consequence;
- reproducibility;
- owner and proposed disposition;
- fix status and retest evidence.

Use:

- `BLOCKER`: Testing or use cannot proceed, the candidate is corrupt/missing, or required authority/evidence is absent.
- `CRITICAL`: Materially unsafe, noncompliant, misleading, inaccessible, insecure, or incorrect.
- `MAJOR`: Prevents or substantially impairs the intended use or required quality.
- `MINOR`: Does not block intended use but should be fixed or formally accepted.
- `NOTE`: Observation or improvement opportunity that is not a defect.

Severity reflects impact, not repair effort.

### 11. Repair and retest when authorized

Before editing:

- confirm authorization and exact scope;
- preserve the original candidate;
- avoid changing approved meaning or unrelated content;
- record the fix and new candidate identity.

After editing:

- rerun the failed test;
- inspect affected neighboring content;
- rerun cross-format consistency;
- execute regression tests proportional to the change;
- update evidence and defect disposition.

Do not close a defect from a code or source-file change alone; verify the final output.

### 12. Determine QA disposition

Read [references/release-and-exceptions.md](references/release-and-exceptions.md). Use:

- `QA PASS`
- `QA PASS WITH CONDITIONS`
- `QA FAIL`
- `NOT VERIFIED`

Any unresolved blocker, critical defect, required major defect, or required unperformed check prevents `QA PASS`.

`QA PASS WITH CONDITIONS` requires that remaining conditions are explicitly non-blocking for the intended use, owned, dated, and accepted by the proper authority.

### 13. Route authorization

Report QA disposition separately from:

- `AUTHORIZED`
- `AUTHORIZED WITH CONDITIONS`
- `NOT AUTHORIZED`
- `AUTHORIZATION NOT VERIFIED`

Only the named accountable authority can authorize release. If no authority or approval evidence is supplied, report `AUTHORIZATION NOT VERIFIED` even when QA passes.

### 14. Produce the release package

Use [references/output-templates.md](references/output-templates.md). Provide applicable:

- candidate inventory and manifest;
- requirement-to-test matrix;
- QA evidence ledger;
- defect and exception register;
- cross-format comparison;
- regression report;
- QA summary and disposition;
- authorization record;
- release notes, known limitations, rollback, support, and maintenance triggers.

Do not label a package released until both QA and authorization requirements are satisfied and release execution is evidenced.

## Quality gate for the QA process

Before delivering the QA report, verify:

- the exact candidates tested are identifiable;
- every required format and file is represented;
- every claim is backed by inspection evidence;
- source, visual, technical, functional, accessibility, and cross-format checks are distinguished;
- unperformed tests are visible;
- defect severity and dispositions are consistent;
- repairs were retested on final outputs;
- exceptions have scope, rationale, risk, owner, authority, and expiration;
- QA disposition and release authorization are separate;
- the report itself contains no unsupported pass or release claim.

Use [references/test-cases.md](references/test-cases.md) to validate revisions to this skill.
