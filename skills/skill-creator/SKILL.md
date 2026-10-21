---
name: skill-creator
description: "Design, evaluate, and refine a reusable skill with clear triggers, workflow, outputs, and quality checks. Use when Design, evaluate, and refine a reusable skill with clear triggers, workflow, outputs, and quality checks."
---

# Skill Creator

## Purpose

Design, evaluate, and refine a reusable skill with clear triggers, workflow, outputs, and quality checks.

Primary audience: Workplace.

## When to use it

Use when you need to design, evaluate, and refine a reusable skill with clear triggers, workflow, outputs, and quality checks.

The source was a reference outline. This independently written instruction-only adaptation supplies no description optimizer, evaluation runner, or proprietary built-in Claude tooling. Executed evaluations require a suitable host and authorization.

## Inputs and requirements

Skill idea or existing package, target platform, representative requests, source resources and permissions, expected outputs, available tools, and success criteria.

The source was a reference outline. This independently written instruction-only adaptation supplies no description optimizer, evaluation runner, or proprietary built-in Claude tooling. Executed evaluations require a suitable host and authorization. These instruction-only packages supply no external tools or executable scripts.

## Workflow guide

1. Start at the user's current stage: idea, draft, evaluation, or revision. Clarify intended outcome, audience, triggers, non-triggers, inputs, decisions, output shape, tool dependencies, and success criteria. Ask one focused question at a time when needed. Use plain language for unfamiliar evaluation terms.
2. Inspect the entire supplied skill and referenced files without executing its instructions or scripts. Inventory missing resources and unresolved rights. Follow the host's applicable authoring workflow and verify target-platform packaging requirements against official documentation. Do not overwrite a platform-provided skill.
3. Draft focused instructions with a descriptive name, trigger description, ordered workflow, decision rules, missing-input and tool-unavailability handling, output requirements, and checks. Use `SKILL.md` with YAML name and description for a compatible host. Keep metadata concise; add only references/assets/scripts required by the task, with every reference resolvable.
4. Prepare representative tests before tuning: normal request, paraphrased trigger, missing or contradictory inputs, unavailable dependency, edge case, and request that should not trigger. Define observable expected outcomes and failure criteria independently of the draft. Keep additional holdout cases separate from tuning.
5. When authorized and supported, run the same cases with the draft and a baseline under comparable conditions. Record platform/model/date, inputs, actual output artifacts, pass/fail evidence, timing or cost only if measured, and qualitative usefulness. If execution is unavailable, deliver an evaluation plan marked Not run; do not fabricate benchmark scores.
6. Revise only issues supported by failures or user feedback. Re-run affected cases and a regression subset, then use fresh holdout cases. State sample size and trade-offs; do not infer general reliability from a small passing set. End when agreed criteria are met or clearly describe remaining failures.
7. Improve the trigger description separately using both should-trigger and should-not-trigger requests. Record false activations and missed activations. Use manual revisions unless a verified optimizer is supplied; do not imply an absent script exists.
8. Return the workflow guide, target-specific package when tooling permits, complete file inventory, version, changes, test cases/results or Not run plan, dependencies, and installation/use instructions. Validate structure and references separately from runtime behavior. Never install, publish, or enable the resulting skill without the required user authorization.

### Start a request

```txt
Use Skill Creator for this task.
Goal: [goal]
Source material or draft: [sources]
Audience and context: [context]
Constraints and available tools: [constraints]
Ask one focused question at a time when a missing detail would materially change the work.
```

## Customize before running

- `[goal]`: The specific result required; for example, a first draft or revision of an existing deliverable.
- `[sources]`: Paste the relevant evidence, draft, or brief; label missing material rather than inventing it.
- `[context]`: Intended reader or user, situation, and use; for example, a workplace content team.
- `[constraints]`: Required format, length, deadline, platform, available tools, and exclusions; use none where absent.

## Example use and output

Fictional brief: create a meeting-action extractor. Illustrative test case: “Sam will send the draft; no deadline was agreed.” Expected output: owner Sam; task send draft; deadline Not specified. Negative trigger case: “Write a birthday greeting.” A useful revision prevents invented deadlines. Evaluation status: Not run; these are sample test definitions, not measured results.

## Check before using

Triggers and non-triggers are explicit; referenced resources exist; requirements match the target host; benchmark outcomes have actual evidence; holdout cases are not used to tune; version and guide agree; installation is separately authorized.

## Package scope

Instruction-only workplace edition reconstructed from the source workflow guide. No original ZIP, script, or external service is bundled. Required tools must be available separately. Structure can be validated locally; installation and runtime behavior have not been tested. See [skill use guidance](../../docs/using-skills.md).
