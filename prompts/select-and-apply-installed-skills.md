# Select and apply installed skills

**Audience:** Workplace

## Purpose

Select and apply the smallest effective combination of installed skills for an ongoing conversation or project while preserving existing authorization and approval gates.

## When to use it

Paste this into a ChatGPT Work or Codex conversation when you want an assessment of available skills and their appropriate use. It adapts to the current environment; it does not install skills or grant access to missing tools.

## Copy-ready prompt

```txt
Review this conversation and select the installed skills best suited to the current task or project. Use an adaptive approach: explain your recommendations briefly, then apply suitable skills when the work is already authorized.

Understand the work
- Identify the current goal, audience, deliverables, constraints, project phase, decisions, and approval status from the available conversation and relevant project instructions.
- Preserve completed work and agreed requirements. Do not restart discovery or reopen settled decisions without a concrete reason.
- If missing information would materially change skill selection or execution, ask ONE question at a time. Use clickable choices when available; otherwise use distinct bulleted options. Include your recommended choice and a one-sentence rationale.

Verify available skills
- Inspect the skill catalog or discovery mechanisms actually available in this environment. Adapt to ChatGPT Work or Codex.
- Use exact skill names. Do not assume a skill is installed because it appeared in another conversation, account, repository, or environment.
- Read the instructions for promising candidates before committing to their use. Check their scope, prerequisites, dependencies, and available tools.
- Distinguish between a skill being listed, its instructions being accessible, and its required tools being usable.
- If you cannot inspect installed skills, state that limitation briefly and request the skill list or relevant SKILL.md files. Do not invent availability or claim to have invoked a skill.

Choose the smallest effective combination
- Match skills to the actual task and expected outcome, rather than keywords alone.
- Prefer the most directly applicable skill. Add supporting skills only when each contributes a distinct benefit, such as planning, production, accessibility, or verification.
- Resolve overlapping workflows by choosing one lead skill and clearly scoped supporting skills. Explain meaningful tradeoffs briefly.
- Follow applicable mandatory skill requirements. If no optional skill adds value, say so and continue with the appropriate built-in capabilities.
- Keep selection focused on installed skills. Do not install, replace, or modify skills unless I request it.

Recommend and act
Present a concise assessment containing:
- Current objective: One sentence.
- Selected skills: Exact name, why it fits, and its role or intended output. Use a compact table when several skills are selected.
- Sequence: The order of use, including dependencies.
- Status: What you will apply now, what is reserved for a later phase, and any specific blocker or approval gate.

Then proceed with work already authorized in this conversation. Merely naming a skill does not count as using it: load its instructions through the available mechanism and follow the applicable workflow. Clearly distinguish recommended, loaded, applied, and blocked skills when reporting status.

Preserve authorization
- Honor all existing alignment protocols, review checkpoints, and explicit instructions to wait.
- This prompt authorizes skill assessment and selection; it does not independently authorize new project work or external actions.
- Do not treat a skill recommendation as permission to expand scope, publish, send messages, deploy, spend money, or perform destructive actions.
- Do not request approval again for work I have already authorized.
- If an existing gate blocks execution, complete the permitted assessment, identify the exact gate, and stop before the blocked action.

Reassess as the project evolves
Reassess skill fit when the objective, scope, deliverable, project phase, or available capabilities materially change. Explain only meaningful changes to the selection; avoid repeating the full assessment on every response.

Keep skill management concise and subordinate to completing the project. Report only actions actually performed and results supported by evidence.

Begin by assessing the current conversation.
```

## Customize before running

- No placeholders are required when the conversation already contains the project context.
- Add missing goals, deliverables, constraints, or approval status before pasting the prompt.
- If the host cannot inspect installed skills, supply its actual skill list and relevant instructions when requested.
- Keep existing approval gates explicit. This prompt does not replace them.

## Example output

*Illustrative example, not a runtime test. A fictional team has approved development of an employee workshop, but has not approved publishing. Assume the host confirms that `architect-training-sessions` and `qa-and-release-assets` are available and their instructions are accessible.*

**Current objective:** Develop the approved employee workshop and prepare its materials for review.

| Selected skill | Why it fits | Role |
| --- | --- | --- |
| architect-training-sessions | Covers the workshop's delivery, practice, timing, and reinforcement needs. | Lead the session design now. |
| qa-and-release-assets | Provides a distinct review of the finished materials. | Review the draft assets in the later QA phase. |

**Sequence:** Session design, draft development, then asset QA.

**Status:** Both skills are recommended. Load the lead skill before applying it to the authorized design work. Publishing remains blocked by the existing approval gate.

## Check before using

- Recommendations use exact skill names verified in the current environment.
- Selected instructions are read before application; required tools are checked separately.
- Each supporting skill adds a distinct benefit.
- Recommended, loaded, applied, and blocked statuses reflect actual actions.
- Existing project decisions, authorization, and approval gates remain intact.
- Missing discovery or tool access is disclosed without invented invocation claims.
- Reassessment happens after material changes, without repetitive status reports.

## About this entry

Version 1.0.0. Added from Travis True's approved conversation prompt, with headings adapted for plain-text copying. Intended for ChatGPT Work and Codex environments that expose installed skills. Structurally reviewed; behavior has not been runtime-tested across hosts. This entry is a reusable prompt, not an installed skill or an automatic configuration change.
