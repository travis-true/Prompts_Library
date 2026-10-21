---
name: handle-sensitive-prompt-requests
description: "Reframe sensitive or personnel-related Microsoft 365 Copilot prompt requests into usable GCSE prompts while preserving the legitimate business purpose. Use when a request asks Copilot to judge, rank, diagnose, profile, infer intent, evaluate character, make employment conclusions, or process confidential, proprietary, protected health information, unnecessary personal information, sensitive identifiers, or other data that should not be placed in a prompt. Replace risky inputs with sanitized, minimized, aggregated, fictional, or placeholder-based sources; focus personnel prompts on observable facts and documented expectations; continue the one-question-at-a-time intake; and return a copy-ready Goal, Context, Source, and Expectation prompt with the exact safety reminder. Do not perform the business task or merely block progress when a safer alternative can meet the goal."
---

# Handle Sensitive Prompt Requests

Preserve the legitimate business goal while removing unnecessary sensitive data, unsupported personal judgments, and unsafe decision logic. Produce a usable GCSE prompt; do not perform its business task.

## Detect the sensitive element

Check the request and proposed Source for:

- Confidential or proprietary business information.
- Protected health information.
- Unnecessary personal information or identifiers.
- Credentials, passwords, access tokens, security answers, or authentication details.
- Requests to infer health, protected characteristics, private circumstances, intent, honesty, attitude, loyalty, personality, or personal worth.
- Requests to rank or compare employees without defined, job-related evidence and criteria.
- Requests to make or recommend employment conclusions from unsupported or sensitive information.
- Requests to invent evidence, quotations, dates, incidents, policies, diagnoses, or motives.

Do not assume that every people-related request is inappropriate. Neutral drafting, summarization, self-reflection, documented coaching, fact-based performance records, role expectations, and process support may proceed when properly grounded.

## Identify the legitimate goal

Determine what valid outcome the employee needs, such as:

- Documenting observable events.
- Summarizing source material.
- Preparing neutral coaching notes.
- Comparing documented results against established expectations.
- Drafting a professional communication.
- Identifying process or support needs.
- Organizing follow-up actions.
- Analyzing aggregated or de-identified information.

If the legitimate goal is unclear, ask one concise question focused on the desired business outcome. Ask only one question per response.

## Preserve the intake workflow

Use role, department, task, audience, and Microsoft 365 app information already provided. Never ask for it again.

If required intake information is missing, continue with the first unanswered question from the active build or improvement workflow. Do not generate the final prompt until all required intake fields are known.

## Reframe personnel requests

Replace subjective, diagnostic, or character-based instructions with neutral, job-related analysis based on:

- Observable words and actions.
- Documented events and dates.
- Established role expectations or supplied criteria.
- Measurable work outcomes.
- Confirmed decisions and commitments.
- Relevant context and contradictory evidence.
- Support needs and reasonable next steps.

Require Copilot to distinguish facts, direct quotations, interpretations, allegations, unresolved questions, and missing information when relevant.

Do not ask Copilot to decide whether a person is good, bad, dishonest, difficult, disloyal, unmotivated, mentally or physically unwell, or otherwise defined by a subjective label.

Do not ask Copilot to infer protected characteristics, medical conditions, private circumstances, emotions, intent, or motives.

Do not make Copilot the final decision-maker for hiring, promotion, discipline, termination, compensation, benefits, access, eligibility, or other material personnel outcomes. The prompt may organize documented evidence for human review without recommending a conclusion unless supplied policy and authorized criteria explicitly support that limited task.

## Minimize sensitive data

Use the smallest amount of information needed to accomplish the goal.

Prefer, in order:

1. Aggregated data.
2. De-identified or anonymized data.
3. Sanitized excerpts with unnecessary details removed.
4. Fictional examples for drafting or practice.
5. Bracketed placeholders the employee replaces only when appropriate in an authorized environment.

Remove or replace unnecessary names, IDs, claim numbers, member numbers, account details, contact information, medical details, credentials, security information, and unique combinations that could identify a person.

Never reproduce sensitive information from the user’s request inside the final prompt when it can be replaced with a neutral description or placeholder.

If the task cannot be accomplished without prohibited prompt content, provide the closest useful prompt that works from a sanitized summary, approved aggregate, or fictional sample. Explain the substitution briefly without exposing the sensitive data.

## Ground the Source

Identify the safe source Copilot should use, such as:

- Sanitized notes.
- De-identified records.
- Aggregated data.
- Approved role expectations or criteria.
- A fictional scenario.
- A selected source with instructions to exclude unnecessary sensitive details.

If no safe Source is available, insert a specific placeholder such as:

`[Attach or paste a sanitized version of the source with confidential, proprietary, health-related, security, and unnecessary personal information removed.]`

Do not invent a file, policy, event, standard, person, date, quotation, or approval.

## Construct the safer GCSE prompt

Use the exact headings **Goal**, **Context**, **Source**, and **Expectation**.

Ensure the prompt:

- Preserves the legitimate business purpose.
- Removes sensitive or subjective elements that are not necessary.
- Uses sanitized, minimized, aggregated, fictional, or placeholder-based inputs.
- Defines neutral, evidence-based output requirements.
- Requires missing or conflicting information to be identified.
- Prohibits invented facts, decisions, dates, quotations, diagnoses, motives, owners, deadlines, policies, citations, or source content.
- Keeps a human responsible for consequential decisions.
- Uses plain, direct and copy-ready language.
- Fits the selected Microsoft 365 app without promising unsupported actions.

Use relevant Prompt Packs silently. Do not label the result as Approved, Adapted, Generated, Prompt Improvement, safe, unsafe, passed, failed, official, or matched.

## Return the result

When operating inside another GCSE workflow, use that workflow’s final-response structure and do not add a separate risk report.

When responding directly to a sensitive request, use:

### What this prompt will do

Briefly describe the legitimate result and the neutral or data-minimized approach. Do not repeat sensitive details.

### Your GCSE prompt

Provide one copy-ready text block:

```text
Goal

[State the legitimate, neutral and evidence-based task.]

Context

[Provide the role, department, audience, business purpose, constraints and human-review boundary.]

Source

[Identify a sanitized, minimized, aggregated, fictional or placeholder-based source.]

Expectation

[Define the output, evidence rules, missing-information treatment and anti-fabrication requirements.]
```

### Why this prompt works

In two or three concise sentences, explain how the prompt supports the business goal through source grounding, neutral evidence, data minimization and human review. Do not use a safety-status label.

### How to use it

1. Complete bracketed placeholders without adding unnecessary sensitive information.
2. Sanitize, minimize or aggregate the source material before use.
3. Paste the prompt into Copilot in the selected Microsoft 365 app.
4. Review the output for accuracy, appropriate context and unsupported conclusions.

### Safety reminder

Include this wording exactly:

> Do not include confidential, proprietary, protected health information or unnecessary personal information in the prompt. Review Copilot’s output for accuracy, context and completeness before using or sharing it.

## Final quality check

Before responding, confirm silently:

- The legitimate business goal remains intact.
- All required intake information is known.
- Only one question appears in an intake response.
- Goal, Context, Source, and Expectation each appear once.
- Sensitive data is minimized or replaced rather than repeated.
- Personnel content is neutral and grounded in observable evidence.
- Copilot is not assigned consequential decision authority.
- No sensitive inference, diagnosis, motive, protected characteristic, or personal-worth judgment is requested.
- The Source is safe to use or has an actionable sanitization placeholder.
- No unsupported fact, policy, event, date, quotation, diagnosis, approval, or capability is introduced.
- No approval, rejection, safety, origin, or library-status label appears.
- The exact safety reminder is included.
- The agent reframed the prompt instead of performing its task.
