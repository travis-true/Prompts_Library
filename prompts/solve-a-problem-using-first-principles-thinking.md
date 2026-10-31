# Solve a problem using first-principles thinking

**Audience:** Workplace

## Purpose

Challenge assumptions, identify fundamental facts, and build a practical solution with a small validation test.

## When to use it

Use when a workplace problem feels stuck, a familiar solution is being assumed, or you want to distinguish real constraints from convention.

## Copy-ready prompt

```txt
Help me solve the following problem using first-principles thinking:

[Describe the problem, desired outcome, and relevant context.]

1. Identify the important assumptions embedded in the problem and how I have framed it. Distinguish verified facts, genuine constraints, preferences, and unverified assumptions.
2. Challenge assumptions based on habit, convention, or “how it is usually done.” Flag anything you cannot verify.
3. Break the problem into its fundamental components: what we know, what must be achieved, and what limits actually apply.
4. Build a practical solution from those fundamentals. Consider established approaches when supported by evidence, without treating convention as a requirement.
5. Recommend the strongest approach, explain the key tradeoffs, and identify the smallest useful test of its most important unverified assumption.

Ask clarifying questions when missing information would materially change your recommendation. Present concise conclusions and supporting rationale.

My problem: [Insert problem.]
```

## Customize before running

- Replace both bracketed placeholders with your problem, desired outcome, and context.
- Supply evidence, relevant requirements, and constraints you already know.
- Identify any existing approval gate; this standalone prompt does not create the integrated version's mandatory pause.

## Example output

*Illustrative fictional example, not a runtime test. A team believes a recurring support issue requires a longer training course.*

**Assumption:** More course time will reduce repeat support requests; this is unverified.

**Known facts supplied:** The same task generates repeat requests, and employees cannot find its instructions at the point of work.

**Candidate solution:** Test a short, searchable job aid before committing to a longer course.

**Small test:** Observe a few employees attempting the task with the draft job aid and record where they still need help. Set success criteria before the test.

## Check before using

- Facts, constraints, preferences, and assumptions are distinguished.
- Unverified claims remain labeled.
- Recommendations follow from supplied evidence.
- Useful established methods are considered rather than dismissed.
- A practical test targets a consequential uncertainty.
- No hypothetical test outcome is reported as an actual result.

## About this entry

Version 1.0.0. Added from Travis True's approved conversation prompt based on the supplied video's first-principles framework. The copy-ready wording is preserved from the approved draft. Examples are fictional; behavior has not been runtime-tested across hosts.
