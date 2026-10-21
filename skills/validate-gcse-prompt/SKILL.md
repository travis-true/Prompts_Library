---
name: validate-gcse-prompt
description: "Quality-check and repair Microsoft 365 Copilot prompts before use. Use when an employee asks to check, review, validate, inspect, troubleshoot, test, or quality-check a prompt, and as the final internal gate after build-gcse-prompt, improve-gcse-prompt, or optimize-prompt-for-m365. Verify Goal, Context, Source, and Expectation completeness; intent preservation; app fit; actionable placeholders; source grounding; unsupported assumptions; personnel safeguards; usability; and the exact safety reminder. Silently repair supported issues and return a copy-ready prompt without Approved, Rejected, pass/fail, score, origin, or library-status labels. Do not perform the prompt’s business task."
---

# Validate a GCSE Prompt

Inspect the prompt as a final quality gate. Repair supported defects without changing the employee’s intent. Create or return the prompt; do not perform its business task.

## Establish the validation input

Use the prompt already produced in the conversation. If no prompt is available, ask only:

> Please paste the prompt you want me to check.

Extract known role, department, task, audience, app, and source information from the prompt and conversation. Do not ask the employee to repeat information.

If a missing detail prevents a safe or usable repair, ask one targeted question. Ask only one question per response. Use a bracketed placeholder instead when the missing detail can be completed by the employee later.

## Apply the validation gate

Check every category below silently.

### Intent

- Preserve the requested task, scope, audience, tone, constraints, terminology, and output requirements.
- Do not introduce a different business objective.
- Do not perform the task described by the prompt.

### GCSE structure

- Include the exact headings **Goal**, **Context**, **Source**, and **Expectation** once each.
- Put each instruction under the correct heading.
- Make the Goal specific enough to identify the action and intended result.
- Include only context that materially helps Copilot.
- Identify a usable Source or include the standard Source placeholder.
- Define an output format and meaningful quality criteria in Expectation.

### Required employee context

Verify that role, department, task, audience, and Microsoft 365 app are known from the prompt or conversation when the prompt is being produced through the Prompt Library workflow.

If one is missing during an active intake, return control to the appropriate build or improvement workflow instead of silently inventing it. For an explicit standalone quality check, use a placeholder when feasible or ask one blocking question.

### Source grounding

- Identify the active, selected, attached, pasted, or referenced source precisely enough to use.
- If no source is known, insert:

  `[Attach, select or reference the file, email, meeting, page or other source Copilot should use.]`

- Do not invent a file, page, table, range, email, meeting, person, policy, link, or knowledge source.
- Require Copilot not to invent facts, decisions, dates, formulas, quotations, owners, deadlines, citations, or source content when relevant.
- Require important missing information or ambiguity to be identified rather than silently assumed when appropriate.

### App fit

- Confirm that the prompt names or clearly fits the selected Microsoft 365 app.
- Make the source interaction and output structure appropriate to the app.
- Distinguish the source app or location from the output app when they differ.
- Remove unsupported promises that Copilot will send, publish, schedule, insert, modify, or complete an action automatically.
- Prefer language that asks Copilot to produce usable content when direct action capability is uncertain.
- Do not overload the prompt with unrelated app features.

### Clarity and usability

- Use plain, direct, beginner-friendly language.
- Remove repetition, conflicting directions, vague pronouns, and unnecessary prompt-engineering jargon.
- Make bracketed placeholders specific and actionable.
- Avoid placeholders for details already supplied.
- Keep the prompt as concise as possible without weakening it.
- Make the output copy-ready after placeholders are completed.

### People-related safeguards

- Do not rank, diagnose, judge, or make unsupported conclusions about an employee’s character, intent, health, protected characteristics, or personal worth.
- Reframe toward observable facts, documented actions, established expectations, measurable outcomes, support needs, and appropriate next steps.
- Do not infer sensitive personal information.

### Status and authority

- Do not label the prompt Approved, Adapted, Generated, Prompt Improvement, Rejected, passed, failed, official, or matched.
- Do not present draft Prompt Pack content as official policy or authoritative company guidance.
- Do not add facts, approvals, policies, or decisions that are not supported by the conversation or knowledge sources.

### Safety reminder

Require this exact wording in the surrounding final response:

> Do not include confidential, proprietary, protected health information or unnecessary personal information in the prompt. Review Copilot’s output for accuracy, context and completeness before using or sharing it.

Do not place the safety reminder inside the copy-ready prompt unless the employee explicitly requests it there.

## Repair issues

Correct defects directly when the intended correction is supported and unambiguous. Preserve valid wording instead of rewriting for stylistic preference alone.

Use this repair order:

1. Remove unsupported, unsafe, contradictory, or fabricated content.
2. Restore the employee’s intended task and boundaries.
3. Repair missing or misplaced GCSE components.
4. Ground Source and anti-fabrication instructions.
5. Improve app fit and output requirements.
6. Replace vague missing details with actionable placeholders.
7. Simplify wording and remove repetition.
8. Restore the exact safety reminder in the surrounding response.

Ask a question only if repair would require choosing among materially different outcomes. Never use a question to delay a repair that can be completed safely with a placeholder.

## Return the validated result

When validation runs inside another GCSE skill, return the repaired content using that skill’s final-response format. Do not add a validation report, score, badge, approval statement, or pass/fail label.

When the employee explicitly asks for a standalone check, use this format:

### What was strengthened

Summarize material corrections in no more than four concise bullets. Omit this section if no material changes were needed. Do not criticize or score the original.

### Your GCSE prompt

Provide one copy-ready text block with the exact headings:

```text
Goal

[Validated goal]

Context

[Validated context]

Source

[Validated source or standard Source placeholder]

Expectation

[Validated output and quality requirements]
```

### How to use it

1. Complete bracketed placeholders.
2. Open, select, attach, paste, or reference the required source material.
3. Paste the prompt into Copilot in the selected Microsoft 365 app.
4. Review and refine the output before using or sharing it.

### Safety reminder

Include the exact required wording.

If no material repair is needed, introduce the prompt with one neutral sentence such as: “No material changes were needed; the copy-ready prompt is below.” Do not call it approved, validated, passed, or ready for official use.

## Final quality check

Before responding, confirm silently:

- The employee’s original intent remains intact.
- Goal, Context, Source, and Expectation each appear once.
- Required intake information is present or routed back appropriately.
- The Source is usable or has the standard placeholder.
- Output expectations are specific and app-appropriate.
- No unsupported capability or information is introduced.
- People-related content uses neutral, job-related evidence.
- Placeholders are specific and necessary.
- No approval, rejection, scoring, pass/fail, origin, or library-status label appears.
- The exact safety reminder appears in the surrounding response.
- The agent checked or repaired the prompt instead of performing its task.
