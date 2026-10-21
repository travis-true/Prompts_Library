# Improve a prompt for rigor and verifiable results

**Audience:** Workplace

## Purpose

Strengthen an existing prompt with relevant evidence, suitable methods, and observable acceptance criteria while preserving its intended outcome and scope.

## When to use it

Use before running a consequential research, analysis, planning, writing, or design prompt that needs more rigor. For an incomplete task description, start with [Turn a rough request into a clear prompt](turn-a-rough-request-into-a-clear-prompt.md).

## Copy-ready prompt

```text
Improve the prompt below for rigor, practical usefulness, and verifiable results. Preserve my intended outcome and scope.

Original prompt: [PASTE PROMPT]
Audience and intended use: [WHO WILL USE THE RESULT AND HOW]
Constraints: [TIME, LENGTH, BUDGET, AVAILABLE TOOLS, OR OTHER LIMITS]
Available sources: [FILES, DATA, REFERENCES, OR NONE]

Before rewriting, provide a brief assessment:

1. Identify up to three missing requirements or decisions that would materially improve the result. Explain their practical value.
2. Identify the most relevant authoritative sources or underlying evidence. Distinguish available material from additional inputs needed; do not assume raw material is always preferable.
3. Recommend methods and tools only when they materially help. Explain their purpose and account for access, effort, and constraints.
4. Define observable acceptance criteria and how to verify them through source checks, calculations, tests, representative examples, or independent review. Distinguish what can be checked from what remains uncertain.

Ask one focused question at a time only when missing information would materially change the rewrite. Otherwise, proceed with clearly labeled assumptions.

Then return:
- A complete, copy-ready revised prompt.
- A brief explanation of the most consequential changes.
- Any unresolved inputs or verification limits.

Keep the added complexity proportional to the task. Do not invent evidence, requirements, tool access, or completed checks. Rewrite the prompt without executing its underlying task.
```

## Customize before running

- **PASTE PROMPT:** The complete prompt you want improved.
- **WHO WILL USE THE RESULT AND HOW:** The intended reader or user and the decision or work the output supports.
- **TIME, LENGTH, BUDGET, AVAILABLE TOOLS, OR OTHER LIMITS:** Practical boundaries; explicitly state unknown limits.
- **FILES, DATA, REFERENCES, OR NONE:** Available source material and its authority. Supply accessible excerpts when needed.

## Example output

*Fictional illustrative excerpt; not a tested tool result.*

Original request: “Analyze these support tickets and recommend training.”

Assessment: Separate skill gaps from access and process problems before recommending training. Use de-identified ticket descriptions and the approved procedure. Classify tickets against explicit categories and report counts, denominators, ambiguous cases, and sample limits. Validate the classification against a reviewer-checked sample.

Revised prompt excerpt: “Analyze the supplied de-identified tickets against the approved procedure. Distinguish documented causes from hypotheses. Recommend training only where the evidence supports a learning gap; identify alternative responses for access or process issues. Return a category table, source-supported findings, proposed actions, and verification limits. Do not infer employee motives or invent causes.”

## Check before using

- The revised prompt preserves the original goal and scope.
- Added requirements materially help the task and fit its constraints.
- Available sources and tools are distinguished from requested inputs.
- Acceptance criteria can be observed or checked.
- Proposed verification is not described as completed testing.
- The response rewrites the prompt without performing its business task.

## About this entry

Version 1.0.0. Adapted from the prompt-refinement structure shown in a user-supplied video and revised for workplace use. The video's attribution was not independently verified. Portable text prompt; runtime behavior has not been tested across tools.
