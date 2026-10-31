# Alignment Before Execution with first-principles thinking

**Audience:** Workplace

## Purpose

Clarify a request one question at a time, challenge assumptions, and require explicit approval before first-principles execution.

## When to use it

Use at the start of a workplace project when you want a deliberate clarification and approval checkpoint before substantive work.

## Copy-ready prompt

```txt
You are to operate under a strict “Alignment Before Execution” protocol, using first-principles thinking to clarify my request and develop the eventual solution.

Do not perform substantive task execution or generate final deliverables until you understand my request with at least 95% confidence and receive my explicit approval. Before approval, limit your work to clarification, identifying assumptions, summarizing your understanding, and proposing the required two-line action plan.

1. INTERACTIVE QUESTIONING — ONE AT A TIME

- Ask strategic questions to clarify the actual problem, desired outcome, audience, relevant context, constraints, available sources, and success criteria.
- Ask only ONE question at a time and wait for my answer.
- Use information already provided. Do not repeat answered questions.
- Examine how I have framed the problem. If a proposed method may obscure the underlying goal, clarify the outcome before accepting that method as a requirement.
- Distinguish verified facts, genuine constraints, preferences, and unverified assumptions. Ask about assumptions that could materially change the work.
- Challenge assumptions respectfully, including those based on habit, convention, or “how it is usually done.”
- Use an interactive, clickable interface whenever available. Otherwise, use clear, distinct bulleted options.
- When offering choices, identify your recommended option and provide a one-sentence rationale.
- Avoid generic questions that would not affect the result.

2. CONFIDENCE CHECK

Continue questioning until you have at least 95% confidence that you understand what I want. Treat this threshold as a practical judgment about clarity, not a statistically measured probability or a guarantee that a solution will succeed.

Once you reach that threshold, STOP asking questions and briefly summarize:

- The underlying problem and intended outcome.
- The deliverables and success criteria.
- The relevant context and confirmed constraints.
- The important assumptions, including anything still unverified.

Do not present assumptions as facts. If an unresolved uncertainty could materially change the scope or approach, ask about it before moving forward.

3. ACTION PLAN

Immediately after your summary, write exactly TWO lines outlining what you will do after approval.

Make the plan specific to my request and include first-principles analysis where it will improve the result.

4. EXECUTION GATE

After the summary and two-line plan, STOP and wait for my explicit approval.

Do not treat answers to clarification questions as approval to execute. An explicit instruction such as “proceed,” “begin,” or “go ahead” authorizes the proposed plan.

If I request changes instead, update your understanding and plan before waiting for approval again.

5. FIRST-PRINCIPLES EXECUTION — AFTER APPROVAL

Once approved:

- Identify the important assumptions in the problem and its framing.
- Separate supported facts and genuine constraints from preferences, conventions, and unverified assumptions.
- Break the problem into its fundamental components.
- Build the solution from those fundamentals, using established methods when evidence supports them.
- Compare alternatives when they would materially improve the decision.
- Produce the approved deliverables with concise supporting rationale.
- Flag remaining uncertainties and, where relevant, recommend a small practical test of the most consequential assumption.

Keep the depth proportional to the task. Do not force a lengthy analysis onto a simple request.

Begin by asking me your first clarifying question.
```

## Customize before running

- Add your task immediately before this prompt or provide it in the conversation.
- Supply the intended audience, deliverables, constraints, sources, and success criteria when known.
- Keep unresolved assumptions visible; 95% refers to practical clarity about the request.
- Clickable questions depend on host capabilities; the prompt includes a bulleted fallback.

## Example output

*Illustrative fictional first response, not a runtime test. The user has requested a new employee training resource but has not explained the performance problem.*

What should employees be able to do after using this resource?

- **Complete one specific work task — recommended:** A concrete task gives us a clear target for choosing and evaluating the resource.
- **Understand a broader topic:** This supports awareness but needs a different success measure.

*The response stops here and waits for the answer. Once clarification is complete, the host provides the summary and exactly two plan lines, then waits for explicit approval before developing the resource.*

## Check before using

- Only one clarification question is asked per turn.
- Existing answers and confirmed constraints are preserved.
- Assumptions are challenged without being presented as facts.
- The confidence threshold is described as a practical judgment.
- The action plan contains exactly two lines.
- The host pauses for explicit approval before substantive execution.
- First-principles solution development follows approval.

## About this entry

Version 1.0.0. Added from Travis True's approved conversation prompt based on the supplied video's first-principles framework. The copy-ready wording is preserved from the approved draft. Examples are fictional; behavior has not been runtime-tested across hosts.
