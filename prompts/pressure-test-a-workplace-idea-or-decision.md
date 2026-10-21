# Pressure-test a workplace idea or decision

**Audience:** Workplace

## Purpose

Test the assumptions, evidence, tradeoffs, and opposing arguments behind a workplace idea or decision.

## When to use it

Use this prompt before committing to a strategy, presenting a recommendation, approving a proposal, defending an argument, or making a consequential workplace decision. It is most useful when you want constructive intellectual resistance rather than editing or general feedback.

## Copy-ready prompt

```txt
You are a rigorous intellectual sparring partner and red-team reviewer. Pressure-test my reasoning instead of validating it by default.

Context:
- Claim, idea, plan, or proposed decision: [PASTE THE IDEA]
- Domain or business area: [FIELD]
- Intended outcome: [WHAT I AM TRYING TO ACHIEVE]
- Decision or action under consideration: [WHAT MAY BE DECIDED OR DONE]
- Stakeholders affected: [WHO MAY BENEFIT, BE BURDENED, OR INFLUENCE THE OUTCOME]
- Stakes: [LOW / MEDIUM / HIGH]
- My current confidence: [0–100%]
- Review mode: [RED TEAM / STEELMAN / SOCRATIC QUESTIONS / ALTERNATIVE PERSPECTIVES / DECISION STRESS-TEST]
- Evidence available: [EVIDENCE, SOURCES, DATA, OR NONE]
- Constraints: [TIME, BUDGET, POLICY, RESOURCES, RISK TOLERANCE, OR OTHER LIMITS]

Review principles:
- Do not agree by default, flatter me, or manufacture objections.
- Challenge the strongest reasonable version of my position, not a straw man.
- Separate established facts, supplied evidence, assumptions, values, and predictions.
- Distinguish “not supported by the available evidence” from “shown to be false.”
- If the idea is sound, explain why it holds up. If it is partly sound, identify precisely which parts survive.
- Label uncertainty, missing evidence, and conclusions that depend on judgment.
- Do not invent facts, sources, stakeholder views, policies, requirements, or risks.
- Be direct, specific, constructive, and concise.

Process:
1. Restate my central claim, desired conclusion, and proposed action.
2. Identify the strongest reasonable version of my position.
3. List the assumptions on which the conclusion depends. Rank them by:
   - Importance to the conclusion
   - Uncertainty
   - Cost if wrong
4. Challenge the three to five assumptions that create the greatest risk. For each, explain:
   - Why it may fail
   - Evidence supporting or weakening it
   - Missing information
   - Possible bias or reasoning error
   - Practical consequence if it is wrong
5. Identify logical gaps, internal contradictions, unstated tradeoffs, second-order effects, and affected stakeholders whose interests may be overlooked.
6. Present the strongest opposing case as its advocates would recognize it.
7. Offer two or three genuinely different perspectives or framings. Explain what each would imply for the decision.
8. State the strongest counterargument I should be prepared to answer.
9. Define falsification and decision tests:
   - What evidence would substantially weaken or disprove the claim?
   - What evidence would strengthen it?
   - What threshold should trigger revising, delaying, or rejecting the decision?
10. Ask five focused questions that expose important blind spots.
11. Recommend what to verify, test, revise, or decide next, ordered by impact.
12. Rewrite my argument or plan so it retains its strongest elements while addressing valid challenges.
13. Reassess confidence in the revised position and explain the main remaining uncertainty.

If missing information could materially change the review, ask up to three focused clarifying questions before starting. Otherwise, state necessary assumptions and proceed without asking permission.

Output format:
- Core claim and proposed action
- Strongest version of the case
- What holds up
- Key assumptions, ranked
- Biggest weaknesses
- Strongest opposing case
- Alternative perspectives
- Falsification and decision tests
- Questions I should answer
- Revised argument or plan
- Prioritized next steps
- Revised confidence and remaining uncertainty
```

## Customize before running

- **PASTE THE IDEA** — The complete claim, proposal, strategy, or plan to test; for example, “Move all new-employee training to self-paced courses.”
- **FIELD** — Relevant business area; for example, IT enablement, operations, marketing, finance, or product development.
- **WHAT I AM TRYING TO ACHIEVE** — The desired measurable result; for example, reduce onboarding time without lowering proficiency.
- **WHAT MAY BE DECIDED OR DONE** — The specific action under consideration; for example, approve a 90-day pilot.
- **WHO MAY BENEFIT, BE BURDENED, OR INFLUENCE THE OUTCOME** — Relevant stakeholder groups and decision-makers.
- **LOW / MEDIUM / HIGH** — Consequence level if the reasoning or decision is wrong.
- **0–100%** — Your present confidence in the central conclusion.
- **REVIEW MODE** — The kind of challenge wanted. Choose one or combine compatible modes.
- **EVIDENCE, SOURCES, DATA, OR NONE** — Available research, metrics, observations, requirements, or links.
- **TIME, BUDGET, POLICY, RESOURCES, RISK TOLERANCE, OR OTHER LIMITS** — Boundaries the analysis must respect.

## Example output

*Illustrative excerpt using fictional inputs.*

**Core claim and proposed action:** A fictional support department should replace all instructor-led onboarding with self-paced courses to reduce training time.

**What holds up:** Standard procedures and software demonstrations could be delivered consistently through self-paced modules. This could reduce repeated instructor presentation time.

**Key assumptions, ranked:**

1. Practice and coaching do not materially affect job readiness — high importance, high uncertainty, high cost if wrong.
2. Course completion predicts independent performance — high importance, high uncertainty.
3. All new hires have comparable prior knowledge — medium importance, weak support.

**Biggest weakness:** The proposal treats content delivery as equivalent to skill development. No evidence currently shows that employees can perform complex support scenarios without coached practice.

**Strongest opposing case:** A blended model would preserve scalable knowledge instruction while retaining supervised practice for judgment-heavy tasks.

**Falsification test:** Run a controlled pilot comparing time to proficiency, quality-review scores, escalation rates, and learner confidence. Reject the fully self-paced model if it saves time but produces meaningfully worse performance.

**Revised argument:** Move stable knowledge content to self-paced modules while retaining coached scenarios and proficiency checks for complex tasks.

**Revised confidence:** 72%. The blended model is more defensible, but the required amount of coaching remains uncertain.

## Check before using

- Define the actual decision, not only the general topic.
- Include the best available evidence and applicable constraints.
- Identify affected stakeholders.
- Verify factual claims, policies, and cited evidence independently.
- Do not paste confidential or regulated information into an unapproved tool.
- Treat invented objections and unsupported conclusions as invalid.

## About this entry

Adapted from a user-supplied red-team prompt and refined for workplace decisions. Version 1.0. Portable text prompt for ChatGPT, Copilot, Gemini, Claude, and DeepSeek. It does not require browsing, but current or specialized claims cannot be verified unless reliable sources are supplied or the selected tool has appropriate research access. Output quality depends on the completeness and reliability of the evidence. Not individually runtime-tested in all five tools.
