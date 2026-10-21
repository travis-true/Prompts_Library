---
name: curate-prompt-packs
description: "Create, review, normalize, expand, consolidate, and maintain Prompt Packs for departments, job roles, business tasks, and Microsoft 365 apps. Use when an authorized curator asks to build a new Prompt Pack, convert source material or existing prompts into a pack, add or revise prompt entries, audit pack consistency, remove duplicates, improve retrieval metadata, document gaps, or prepare Prompt Pack knowledge for the Prompt Library agent. Apply the standard pack schema; require GCSE prompts; preserve source traceability and internal lifecycle metadata; use fictional or sanitized examples; prevent sensitive or unsupported content; and ensure employee-facing responses never expose Approved, Adapted, Generated, Draft, origin, match, or Prompt Pack status labels. This is an administrative content-maintenance skill, not an employee prompt-building workflow."
---

# Curate Prompt Packs

Create and maintain structured knowledge that the Prompt Library agent can retrieve reliably. Treat this as an administrative workflow. Do not use the five-question employee intake unless testing a prompt entry from an employee perspective.

## Establish the curation request

Determine:

1. Operation: create, review, revise, expand, consolidate, retire or audit.
2. Pack type: department, Microsoft 365 app, role, task family or cross-functional.
3. Pack name and intended scope.
4. Source material and its authority or provenance.
5. Target roles, tasks, audiences, apps and keywords.
6. Content owner and internal lifecycle status when known.

Extract information already provided. Ask only for missing details that materially affect the pack. Ask one question per response.

Do not invent an owner, approval, authority level, review date, source, department, app capability, policy or business rule. Use `Not specified` or a clearly marked placeholder for unknown administrative metadata.

## Use the standard schema

Read [references/prompt-pack-schema.md](references/prompt-pack-schema.md) before creating or restructuring a pack. Preserve its section order and required fields.

Use Markdown unless the curator requests another supported knowledge format. Keep one pack focused enough that its retrieval terms remain distinctive.

## Analyze source material

Extract only supported:

- Common employee goals and tasks.
- Roles and audiences.
- Microsoft 365 apps and source types.
- Required terminology and constraints.
- Expected output formats.
- Quality criteria.
- Reusable placeholders.
- Safety, privacy and personnel safeguards.
- Known examples and exceptions.

Separate source-grounded facts from curator-provided assumptions. Log conflicts, gaps or uncertain content instead of silently reconciling or inventing it.

Do not copy unnecessary sensitive data into the pack. Replace real names, identifiers, health information, confidential details, credentials and organization-specific examples with sanitized or fictional equivalents unless the information is both necessary and explicitly authorized for the knowledge source.

## Design retrieval metadata

Make each prompt entry findable through natural employee language. Include:

- Primary task.
- Task synonyms.
- Job roles.
- Department or function.
- Microsoft 365 app.
- Intended audience.
- Source types.
- Output types.
- Distinctive keywords and common user phrasings.

Use lowercase keywords, remove duplicates and avoid broad filler terms such as `help`, `work`, `prompt`, `document` or `Copilot` unless they distinguish the entry.

Do not overload an entry with unrelated roles, apps or keywords to force retrieval. Split materially different use cases into separate entries.

## Build each prompt entry

Give every entry a stable ID, concise title and plain-language “What this prompt does” description.

Create one reusable prompt pattern under the exact headings **Goal**, **Context**, **Source**, and **Expectation**.

Ensure every pattern:

- Supports one primary business outcome.
- Includes role, department, audience and app placeholders only when they materially help.
- Identifies the source precisely or uses an actionable source placeholder.
- Defines an output format, structure, length, tone, detail and quality criteria appropriate to the task.
- Uses bracketed placeholders for variable information.
- Tells Copilot not to invent unsupported facts, decisions, dates, formulas, quotations, owners, deadlines, citations or source content when relevant.
- Tells Copilot to identify important missing information when appropriate.
- Uses neutral, evidence-based language for people-related tasks.
- Does not give Copilot consequential personnel decision authority.
- Avoids unsupported app capability claims.
- Is concise, beginner-friendly and copy-ready after customization.

Include short curator notes for retrieval and customization. Do not include employee-facing approval, origin or match labels.

## Manage internal lifecycle metadata

Administrative lifecycle metadata may use:

- `draft`
- `reviewed`
- `retired`

Use these values only for curation and governance. Mark them as internal metadata that the employee-facing agent must never expose.

Do not equate `reviewed` with policy authority or official company guidance. Record source authority separately.

Never claim a pack or entry was approved, reviewed or authorized unless the curator supplies that status.

## Review an existing pack

Check:

- Schema completeness.
- Stable unique IDs.
- Duplicate or overlapping entries.
- Retrieval collisions.
- GCSE completeness.
- Placeholder clarity.
- Source traceability.
- App fit.
- Safety and personnel safeguards.
- Unsupported company facts or capabilities.
- Consistent terminology and formatting.
- Stale, superseded or conflicting content.
- Coverage gaps across major roles and recurring tasks.

Repair clear structural and wording issues when authorized. Preserve source-grounded intent. Log substantive conflicts or missing authority for curator decision.

Do not use a single numeric quality score. Report actionable findings by severity:

- **Blocking:** cannot be used reliably without correction or a decision.
- **Needs attention:** usable only with a documented limitation or minor repair.
- **Enhancement:** optional improvement.

These administrative findings are not employee-facing prompt labels.

## Consolidate and deduplicate

Treat entries as duplicates when they have the same primary task, app, source type, audience and expected output, even if wording differs.

When merging:

1. Preserve the clearest title and strongest supported GCSE pattern.
2. Combine useful retrieval synonyms without keyword stuffing.
3. Preserve source references from both entries.
4. Retain the stable ID of the governing entry.
5. Record retired IDs in the maintenance notes.
6. Do not silently discard unique requirements or exceptions.

## Return curation deliverables

For a new or revised pack, return:

1. The complete pack using the standard schema.
2. A concise curation summary covering entries created, revised, merged or retired.
3. A short gaps-and-decisions section listing unresolved source, authority or scope questions.

For an audit, return:

1. Executive summary.
2. Findings table with entry ID, severity, issue and recommended action.
3. Corrected pack when repair was requested.
4. Coverage gaps and unresolved decisions.

Do not expose internal lifecycle, source-status or match labels in the sample employee-facing responses contained in a pack.

## Final quality check

Before delivering a pack, confirm silently:

- The standard schema and section order are intact.
- Pack type, scope and retrieval metadata are clear.
- Every entry has a unique stable ID.
- Every entry uses Goal, Context, Source and Expectation.
- Entries target distinct, useful employee tasks.
- Keywords are specific, natural and deduplicated.
- Sources and unsupported gaps are traceable.
- No owner, authority, status, policy or approval was invented.
- Examples are fictional, sanitized or appropriately authorized.
- Sensitive and personnel safeguards are present where relevant.
- No employee-facing approval, origin, match or lifecycle labels appear.
- The pack can be searched effectively by role, department, task, app, audience and keyword.
