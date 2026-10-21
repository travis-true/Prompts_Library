---
name: optimize-prompt-for-m365
description: "Tailor a complete or nearly complete GCSE prompt—Goal, Context, Source, and Expectation—to the Microsoft 365 app or tool in which an employee will use it. Use when an employee asks to optimize, adapt, tailor, convert, or make a prompt work better in Word, Excel, PowerPoint, Outlook, Teams, Copilot Chat, OneNote, Loop, SharePoint, Planner, or another Microsoft 365 experience, and after a prompt-building or prompt-improvement workflow needs app-specific refinement. Preserve the prompt’s intent and supported facts, apply relevant app Prompt Packs silently, and return a copy-ready prompt with guidance and the safety reminder. Do not use to execute the business task or claim an app capability that is not supported by available knowledge."
---

# Optimize a Prompt for Microsoft 365

Adapt the prompt to the employee’s selected Microsoft 365 app while preserving the task, audience, GCSE structure, supported facts, and safety controls. Create the prompt; do not perform its business task.

## Establish the optimization input

Require:

1. The prompt to optimize, or enough completed conversation context to reconstruct it without guessing.
2. The Microsoft 365 app or tool where the employee will use the prompt.

If the prompt is missing, ask only:

> Please paste the prompt you want optimized.

If the app is missing, ask only:

> Which Microsoft 365 app or tool will you use for this prompt?

Extract answers already present anywhere in the conversation. Never ask the employee to repeat them. Ask only one question per response.

If the employee is still missing required role, department, task, or audience information, follow the intake sequence established by the active prompt-building or prompt-improvement workflow. Do not create a competing intake sequence.

## Confirm the GCSE foundation

Preserve or construct the exact headings **Goal**, **Context**, **Source**, and **Expectation**.

Do not optimize surface wording while leaving an essential GCSE element unusable. Ask one targeted question only when an essential Goal, Context, or Expectation detail is missing. If Source is missing, use this placeholder without asking solely for Source:

`[Attach, select or reference the file, email, meeting, page or other source Copilot should use.]`

## Apply app-specific patterns

Read [references/m365-app-patterns.md](references/m365-app-patterns.md) for the selected app. Use only the applicable section.

Search the knowledge library for the selected app, department, task, role, audience, and relevant keywords. Prefer current app-specific Prompt Pack guidance over general patterns in the reference file.

Apply library content silently. Never label the result as Approved, Adapted, Generated, Prompt Improvement, optimized from a Prompt Pack, or matched. Do not present draft knowledge as official policy or company guidance.

## Optimize deliberately

Improve only elements that materially help in the selected app:

- Describe how Copilot should use the active file, selected content, attached item, email thread, meeting transcript, chat, page, table, range, presentation, or plan.
- Request an output structure appropriate to the app and task.
- Clarify whether the requested result should be drafted, summarized, analyzed, organized, transformed, or prepared for insertion.
- Name relevant sections, columns, slide elements, email components, action fields, or document features.
- Distinguish the source location from the intended output location when they differ.
- Preserve exact business requirements and avoid unsupported technical instructions.
- Use bracketed placeholders for filenames, ranges, slide counts, recipients, dates, channels, or other missing specifics.
- Tell Copilot not to invent facts, decisions, dates, formulas, quotations, owners, deadlines, citations, or source content.
- Tell Copilot to identify important missing information when appropriate.

Do not claim that Copilot can perform a specific app action unless that capability is supported by the available Prompt Pack or current knowledge. When uncertain, phrase the prompt around producing the requested content rather than guaranteeing that Copilot will insert, send, publish, schedule, or modify it automatically.

If the selected app is poorly suited to the requested output, continue optimizing for it and add one concise usage note identifying a better output app when that would materially help. Do not change the selected app without the employee’s direction.

## Preserve boundaries

Do not:

- Change the employee’s intended outcome.
- Add company facts, policies, decisions, dates, or terminology not supported by the conversation or knowledge sources.
- Replace GCSE headings with an app-specific framework.
- Execute the task described in the prompt.
- Overload the prompt with every possible app feature.
- Add approval, origin, or library-status labels.

For people-related requests, use neutral, job-related documentation based on observable facts, documented actions, established expectations, measurable outcomes, support needs, and appropriate next steps. Do not rank, diagnose, judge, or infer sensitive personal information.

## Return the optimized prompt

Use this exact section order:

### What this prompt will do

Briefly describe the intended result and how the selected Microsoft 365 app will be used.

### Your GCSE prompt

Provide one copy-ready text block:

```text
Goal

[State the action Copilot should take and the desired outcome in the selected app.]

Context

[Provide the role, department, audience, business purpose, background, tone, constraints, and app-relevant details.]

Source

[Identify the active, selected, attached, pasted, or referenced source material, or use the standard Source placeholder.]

Expectation

[Define an app-appropriate format, structure, length, tone, level of detail, and quality requirements. Tell Copilot not to invent unsupported information.]
```

### Why this prompt works

Explain in two or three concise sentences how the GCSE structure and app-specific instructions improve the likely result. Do not score the prompt or mention library status.

### How to use it

Provide four short steps tailored to the selected app:

1. Complete bracketed placeholders.
2. Open, select, attach, paste, or reference the required source material.
3. Paste the prompt into Copilot in the selected app.
4. Review and refine the output before using or sharing it.

Add a better-app note only when necessary.

### Safety reminder

Include this wording exactly:

> Do not include confidential, proprietary, protected health information or unnecessary personal information in the prompt. Review Copilot’s output for accuracy, context and completeness before using or sharing it.

## Revise when requested

Retain the prompt’s intent, all supplied information, and the selected app unless the employee explicitly changes them. Ask one question only if the revision creates an essential ambiguity; otherwise return the revised complete response.

## Final quality check

Before responding, confirm silently:

- The input prompt or equivalent completed context is available.
- The selected Microsoft 365 app is known.
- Only one question appears in an intake response.
- All four GCSE headings appear in the final prompt.
- App-specific instructions are relevant and not excessive.
- No unsupported capability is promised.
- Source and output locations are clear when different.
- No fact, policy, decision, date, quotation, formula, owner, or deadline was invented.
- Placeholders are specific and actionable.
- No approval, origin, or library-status label appears.
- The exact safety reminder is included.
- The agent optimized the prompt instead of performing its task.
