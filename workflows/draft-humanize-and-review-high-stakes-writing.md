# Draft, Humanize, and Review High-Stakes Writing

**Audience:** Workplace

## Purpose

Use a deliberate two-pass writing process for important content: first make the message accurate and well organized, then improve its clarity and voice, followed by a human read-aloud review.

## When to use it

Use for high-stakes or public-facing content such as proposals, landing pages, important announcements, articles, or pitches. For routine messages, use the Humanizer skill or a relevant quick prompt.

## Inputs and requirements

- **Required:** Desired outcome, intended audience, deliverable format, and any available source material.
- **Optional:** Draft text, voice preferences, claims requiring evidence, protected wording, length, and publishing constraints.
- **Review:** A human author or subject-matter reviewer should read high-impact content aloud and verify important claims before use.
- No particular writing app or text-expansion tool is required.

## Workflow guide

1. **Set the brief.** Define the purpose, audience, desired action or understanding, format, and constraints. Identify approved facts, claims, sources, and wording that must remain exact. Ask one focused question only when a missing detail materially affects the result.
2. **Draft for substance.** Create the structure and first draft from the brief and supplied sources. Prioritize logic, factual accuracy, and audience needs. Do not add unsupported claims, promises, examples, or evidence. Mark important gaps instead of filling them in.
3. **Humanize in a separate pass.** Apply the Humanizer skill or the appropriate workplace rewrite prompt. Prefer plain language, useful short sentences, and a voice suited to the reader. Use a plain-language target only when it fits the audience and preserves necessary detail. Treat “Would a person say this aloud?” as a diagnostic question, not a binary score.
4. **Run a human read-aloud review.** The author or reviewer reads the draft aloud and marks specific sentences that feel unclear, unnatural, or difficult to say. Revise only the marked parts while preserving meaning and voice. If the reviewer supplies no marked sentences, do not invent problems.
5. **Verify and finalize.** Compare the final text with the brief and sources. Check names, dates, numbers, claims, attribution, obligations, calls to action, and uncertainty. Separate open fact questions from style edits. Return the review-ready version and list unresolved claims or assumptions only when applicable.

### Optional read-aloud revision prompt

```txt
Revise only the sentences I marked below so they sound clear and natural for [AUDIENCE]. Keep the intended meaning, facts, tone, and required wording. Do not add details or rewrite unmarked sections.

Marked sentences and my notes:
[MARKED SENTENCES AND NOTES]

Full draft for context:
[CURRENT DRAFT]
```

### Optional text-expander shortcut

If you already use a text-expansion tool, save a short, reusable instruction and insert the text to edit. This is optional; tool setup is outside this workflow.

```txt
Make this clear and natural for [AUDIENCE]. Use short, readable sentences and remove unnecessary filler. Preserve the meaning, facts, attribution, and uncertainty. Keep the requested tone and format. Do not invent details.

Text:
[TEXT]
```

## Customize before running

- **Purpose:** What the content should accomplish. Example: “Help employees understand the portal launch and the action required.”
- **Audience:** The intended reader. Example: “Department managers.”
- **Format:** The deliverable. Example: “A 500-word blog post.”
- **Sources:** Approved facts, references, or source excerpts. Example: “The launch brief and the approved FAQ.”
- **Tone:** Desired voice. Example: “Direct, warm, and credible.”
- **Constraints:** Length, terminology, accessibility, approval requirements, and exclusions. Example: “Keep the product name and launch date exact.”
- **Draft:** Existing text to edit, if available. Enter “NONE” for a new draft.
- **Marked sentences and notes:** Human review feedback. If none, enter “NONE.”

## Example use and output

*Illustrative example using fictional information.*

**Brief:** Write an announcement for employees about a new request portal launching May 6. The approved FAQ says the old portal remains available until June 1. The tone should be direct and reassuring.

**Draft for substance:** “The new request portal launches May 6. The current portal remains available until June 1. Please use the new portal for new requests starting May 6.”

**Human review note:** “The last sentence sounds like a hard requirement, but the FAQ does not say what to do after May 6.”

**Targeted revision:** “The new request portal launches May 6. The current portal remains available until June 1. Check the FAQ for guidance on where to submit requests during the transition.”

**Open item:** Confirm whether the FAQ supports that final instruction before publishing.

## Check before using

- Is the brief clear enough to draft accurately?
- Are claims traceable to the supplied sources?
- Does the plain-language pass fit the actual reader?
- Did the human reviewer identify the lines revised in the read-aloud pass?
- Were unmarked sections and protected facts preserved?
- Are unresolved claims or assumptions visible before publication?

## Related resources

[Humanizer](../skills/humanizer/SKILL.md)

[Rewrite workplace text to sound clear and natural](../prompts/rewrite-workplace-text-to-sound-clear-and-natural.md)

[Rewrite employee learning communications](../prompts/rewrite-employee-learning-communications.md)

## About this entry

Version 1.0.0. Adapted from a submitted hybrid recommendation for baseline writing guidance, a separate high-stakes editing pass, and an author read-aloud check. The underlying image and original prompt referenced in the submission were not included. The claim that fixed language constraints are binary tests, that one reading target is universally appropriate, or that two passes guarantee better results was not independently verified; these are treated here as practical editing heuristics. The read-aloud review requires a human reviewer. No text-expander integration is included.

## Validation

This repository edition provides written instructions and related resource links. Original ZIP packages were not transferred or inspected. Installation, runtime behavior, and the effectiveness of the two-pass process have not been tested. Read-aloud review requires a human reviewer; editing heuristics do not guarantee quality.
