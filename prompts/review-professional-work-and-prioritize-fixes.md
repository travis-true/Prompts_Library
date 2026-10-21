# Review professional work and prioritize fixes

**Audience:** Workplace

## Purpose

Identify the highest-impact weaknesses in professional work and provide precise, prioritized fixes.

## When to use it

Use this prompt when a draft, plan, design, code sample, or other professional deliverable needs rigorous review before approval, release, or further development.

## Copy-ready prompt

```txt
You are a candid, rigorous, and constructive expert reviewer in [FIELD]. Review the work below against its intended goal, audience, constraints, and evaluation criteria.

Context:
- Work type: [WORK TYPE]
- Goal: [WHAT THE WORK MUST ACHIEVE]
- Audience: [WHO WILL USE OR RECEIVE IT]
- Constraints: [LENGTH, TONE, FORMAT, DEADLINE, TECHNICAL REQUIREMENTS, OR OTHER LIMITS]
- What matters most: [TOP PRIORITIES]
- Evaluation criteria or standard: [RUBRIC, REQUIREMENTS, STYLE GUIDE, ACCEPTANCE CRITERIA, OR “USE PROFESSIONAL BEST PRACTICES”]

Instructions:
1. Briefly restate what the work is trying to accomplish and the standard you will use to evaluate it.
2. If missing information could materially change the review, ask up to three focused questions before continuing. Otherwise, state any necessary assumptions and proceed.
3. Identify the three to seven highest-impact problems. Rank them by their effect on the goal, audience, or outcome. Do not pad the review with minor preferences.
4. For each problem, provide:
   - Mistake or issue
   - Severity: Critical, Major, or Minor
   - Location: quote a brief excerpt or identify the exact section, step, screen, or code block
   - What is wrong
   - Why it matters
   - Exact fix: provide replacement wording, corrected code, revised steps, or specific design changes
   - Verification needed: identify anything that must be confirmed before applying the fix
5. Separate must-fix issues from worthwhile improvements.
6. Match each fix to the work type:
   - Writing: provide rewritten language
   - Code: provide corrected code and note relevant dependencies or test needs
   - Strategy: provide revised decisions, sequence, ownership, or steps
   - Design: provide specific layout, copy, accessibility, or interaction changes
   - Other: provide the most concrete correction the format allows
7. Do not use vague advice such as “make it clearer” or “improve the flow.” Explain exactly what should change.
8. Do not invent defects, requirements, evidence, or corrections. If the available information cannot support an exact fix, identify the uncertainty and explain what must be verified.
9. Preserve intentional choices that support the goal. If the work is strong, say so and focus on the few refinements with the greatest value.
10. End with a prioritized action plan explaining what to change first, second, and third.

Output format:
- Purpose and evaluation standard
- Verdict: one or two sentences
- Top issues:
  1. Mistake or issue:
     Severity:
     Location:
     What is wrong:
     Why it matters:
     Exact fix:
     Verification needed:
- Must fix
- Worth improving
- What to fix first
- What to keep or strengthen

WORK:
[PASTE THE COMPLETE WORK]
```

## Customize before running

- **FIELD** — Relevant specialty; for example, cybersecurity, technical writing, marketing, software development, or user-experience design.
- **WORK TYPE** — Format being reviewed; for example, executive email, Python script, communication strategy, or web-page mockup.
- **WHAT THE WORK MUST ACHIEVE** — Observable intended result; for example, secure leadership approval for a 30-day pilot.
- **WHO WILL USE OR RECEIVE IT** — Intended readers or users and relevant experience level; for example, department leaders with limited technical knowledge.
- **LENGTH, TONE, FORMAT, DEADLINE, TECHNICAL REQUIREMENTS, OR OTHER LIMITS** — Requirements the review must preserve.
- **TOP PRIORITIES** — Most important qualities; for example, accuracy, clarity, persuasiveness, accessibility, or performance.
- **EVALUATION CRITERIA OR STANDARD** — Supplied rubric, requirements, acceptance criteria, or named professional practices.
- **PASTE THE COMPLETE WORK** — Full draft or the portion to review. Remove confidential or unnecessary personal information first.

## Example output

*Illustrative excerpt using fictional inputs.*

**Purpose and evaluation standard:** The proposal seeks approval for a 30-day customer-support pilot. I evaluated it for decision clarity, evidence, feasibility, and ownership.

**Verdict:** The proposal presents a credible problem but does not yet give leaders enough information to authorize the pilot responsibly.

**Top issue 1**

- **Mistake or issue:** Success is not measurable.
- **Severity:** Critical
- **Location:** “The pilot will improve response quality and save time.”
- **What is wrong:** Neither outcome has a baseline, measure, or target.
- **Why it matters:** Leaders cannot determine whether the pilot succeeded.
- **Exact fix:** Replace the sentence with: “The pilot will aim to reduce average drafting time from the current baseline by 15% while maintaining the existing quality-review score.”
- **Verification needed:** Confirm the baseline, measurement method, and acceptable quality score with the pilot owner.

**What to fix first:** Define measurable success, assign the decision owner, and add the risk-control process.

## Check before using

- Supply the complete work and its intended outcome.
- Include authoritative requirements or acceptance criteria when available.
- Confirm that severity reflects impact rather than personal preference.
- Verify corrected facts, code, and requirements before applying changes.
- Do not paste confidential information into an unapproved tool.

## About this entry

Adapted from a user-supplied reviewer prompt and refined for workplace use. Version 1.0. Portable text prompt for ChatGPT, Copilot, Gemini, Claude, and DeepSeek. Output quality depends on the completeness of the work and evaluation criteria. Exact corrections still require human verification, particularly for specialized, legal, security, financial, or technical requirements. Not individually runtime-tested in all five tools.
