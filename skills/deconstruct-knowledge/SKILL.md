---
name: deconstruct-knowledge
description: "Intake, inventory, evaluate, and deconstruct enterprise or organizational source material into structured, traceable, AI-ready operational knowledge. Use when a user needs to analyze documents, interviews, notes, policies, procedures, tickets, recordings, presentations, or existing training; identify authoritative sources and conflicts; extract workflows, decisions, roles, rules, exceptions, risks, examples, and content atoms; assess gaps and readiness; or prepare a governed source package for SOPs, job aids, training, knowledge bases, assistants, retrieval systems, or automation."
---

# Knowledge Intake and Content Deconstruction

Convert mixed source material into governed, traceable knowledge that another person or system can use without silently changing its meaning.

## Governing rules

- Preserve source meaning, terminology, scope, qualifiers, conditions, and uncertainty.
- Trace every factual output to a source or verified human answer.
- Separate `FACT`, `ASSUMPTION`, `INFERENCE`, `EXAMPLE`, `CONFLICT`, `GAP`, and `DECISION REQUIRED`.
- Never invent process steps, policy, ownership, system behavior, approval, evidence, or completion criteria.
- Treat SME statements as attributed evidence, not automatically as authoritative policy.
- Preserve conflicting claims until an accountable authority resolves them.
- Do not silently reconcile, expand, modernize, or correct approved content.
- Extract only what the available evidence supports. Use placeholders where required information is absent.
- Apply information-classification, privacy, access, retention, and permitted-use constraints before processing or redistributing content.
- Produce structured knowledge before recommending or generating downstream assets.

## Operating modes

Choose the lightest mode that fits the risk and intended use:

1. **Rapid intake:** Inventory sources, capture purpose and audience, identify obvious gaps, and produce a provisional brief.
2. **Standard deconstruction:** Build the full source inventory, authority map, workflow model, content atoms, gap register, and AI-ready brief.
3. **Controlled deconstruction:** Add formal provenance, conflict resolution, risk scoring, human approvals, version controls, validation evidence, and release restrictions.

Use controlled mode for high-consequence, regulated, safety-sensitive, contractual, security-sensitive, or policy-governed content.

## Workflow

### 1. Define the intake boundary

Determine:

- business purpose and intended downstream use;
- in-scope and out-of-scope topics;
- target audiences, roles, and experience levels;
- required outputs and level of detail;
- information classification and access restrictions;
- authoritative owners, reviewers, and approvers;
- deadline, format, publishing, maintenance, and validation constraints.

Ask grouped clarifying questions only when missing information would materially change the deconstruction. Target roughly 95% confidence when the user permits questions. If an immediate result is requested, continue with labeled assumptions and confidence limits.

### 2. Register the sources

Assign stable IDs such as `SRC-001`. Record each source’s:

- title or description;
- type and location;
- owner or originator;
- version, effective date, and review date;
- approval or publication status;
- scope and intended audience;
- classification and access limits;
- completeness, currency, and known limitations;
- relationship to other sources.

Read [references/source-authority.md](references/source-authority.md) before ranking sources or resolving conflicts.

### 3. Establish source authority

Classify each source as:

- governing or authoritative;
- approved supporting;
- operational evidence;
- SME testimony;
- historical or superseded;
- example or reference;
- unverified;
- conflicting;
- unusable or out of scope.

Do not infer authority from polish, file type, seniority, recency alone, or repeated use. Record who can resolve each disputed claim.

### 4. Deconstruct the content

Extract only applicable elements:

- purpose, outcome, scope, and exclusions;
- audience, roles, responsibilities, and decision rights;
- triggers, inputs, prerequisites, tools, systems, and data;
- ordered steps, handoffs, decisions, branches, and completion criteria;
- rules, thresholds, definitions, exceptions, and escalation;
- errors, failure modes, troubleshooting, controls, and risks;
- examples, non-examples, evidence, measures, and support;
- change history, dependencies, review triggers, and maintenance obligations.

Use [references/deconstruction-model.md](references/deconstruction-model.md) for element definitions and edge cases.

### 5. Build normalized content atoms

Create one independently understandable knowledge unit per atom. Assign IDs such as `ATOM-001`.

Each atom must contain:

- one claim, rule, step, decision, definition, example, or warning;
- audience and applicable context;
- source ID and precise locator;
- authority status;
- conditions, exceptions, dependencies, and risk;
- confidence and validation status;
- approved terminology and reusable keywords;
- downstream-use restrictions.

Keep quoted language minimal. Preserve exact wording only when legal, policy, safety, contractual, or definitional precision requires it.

### 6. Model workflows and decisions

Assign stable IDs such as `WF-001` and `DEC-001`. For each workflow, capture:

- trigger and desired outcome;
- actor and accountable owner;
- prerequisites and inputs;
- ordered actions and system states;
- decision points with supported criteria;
- handoffs and evidence produced;
- exception and escalation routes;
- completion and verification criteria.

Never turn descriptive narrative into a mandatory sequence unless the source supports that interpretation.

### 7. Map audience and moments of need

For each role or audience, identify:

- what they must know, decide, perform, avoid, verify, or escalate;
- when the knowledge is needed;
- current proficiency and likely barriers;
- consequence of delay or error;
- retrieval terms and language they are likely to use;
- accessibility, language, device, and work-environment constraints.

Use this mapping to separate foundational learning from point-of-need reference content.

### 8. Identify gaps, conflicts, and risks

Assign IDs such as `GAP-001`, `CONFLICT-001`, and `RISK-001`. Record:

- exact issue;
- affected elements and audiences;
- evidence and source IDs;
- consequence if unresolved;
- severity and urgency;
- required authority or decision owner;
- recommended resolution action;
- effect on downstream use.

Stop affected downstream production when unresolved information could cause unsafe, noncompliant, materially incorrect, or misleading guidance.

### 9. Produce the governed knowledge package

Use [references/output-templates.md](references/output-templates.md). Include only components the task requires:

1. intake brief;
2. source inventory;
3. source authority map;
4. workflow and decision model;
5. audience and moment-of-need map;
6. content atom register;
7. gap, conflict, assumption, and risk register;
8. terminology and metadata set;
9. AI-ready handoff brief;
10. validation and approval record.

### 10. Validate and gate release

Check:

- traceability from every factual output to evidence;
- preservation of scope, conditions, exceptions, and terminology;
- separation of fact, interpretation, and unresolved content;
- completeness of workflow branches and escalation;
- agreement between sources or explicit conflict records;
- classification and permitted-use compliance;
- readiness for the stated downstream use;
- accountable human review where required.

Report statuses as:

- `READY`
- `READY WITH CONDITIONS`
- `NOT READY`
- `NOT VERIFIED`

Do not claim approval, validation, completeness, or readiness without evidence.

## Handoff rules

- Recommend downstream asset types only after the knowledge package is sufficiently ready.
- Pass source IDs, atom IDs, restrictions, gaps, and exact approval status into downstream work.
- Prevent downstream systems from treating assumptions, examples, or historical content as governing facts.
- Preserve stable IDs through revisions so changes can be compared and traced.
- End with the unresolved decisions and the smallest next action required.

Use [references/test-cases.md](references/test-cases.md) to validate revisions to this skill.
