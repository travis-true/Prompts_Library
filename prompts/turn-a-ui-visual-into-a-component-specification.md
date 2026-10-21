# Turn a UI visual into a component specification

**Audience:** Workplace

## Purpose

Turn a supplied interface visual into a clear, implementation-ready specification for developers.

## When to use it

Use this prompt when you have a screenshot, mockup, or other visual of a UI component and need to document its API, design tokens, states, accessibility, responsive behavior, and implementation considerations.

## Copy-ready prompt

```txt
You are a frontend specification writer. Analyze the supplied visual and prepare a developer-ready specification for [COMPONENT NAME] using [TARGET TECH STACK].

CONTEXT

Target tech stack: [TARGET TECH STACK]
Existing design system or token source: [DESIGN SYSTEM / TOKEN SOURCE OR “NONE PROVIDED”]
Known behavior or product requirements: [BEHAVIOR NOTES OR “NONE PROVIDED”]
Target platforms or viewport requirements: [PLATFORMS / BREAKPOINTS OR “NONE PROVIDED”]

SOURCE

Analyze the attached visual:
[ATTACHED VISUAL]

Describe only what is visible or supplied. Do not claim that inferred behavior, measurements, token names, or responsive rules are confirmed facts.

If the image is inaccessible, ask me to provide it. Before drafting the final specification, identify ambiguities that materially affect component behavior, keyboard interaction, responsiveness, or motion. Ask up to three focused questions at a time and wait for my answers. If a detail is low-impact, you may offer a clearly labeled recommendation. Do not finalize materially uncertain requirements unless I authorize labeled assumptions.

EXPECTATION

Write clean Markdown suitable for a project wiki or Jira ticket. Do not generate implementation code unless requested. Label important details as **Observed**, **Supplied**, **Proposed**, or **Needs confirmation**.

Include these sections:

1. Component API
- Provide a TypeScript interface with prop names, types, and required or optional status.
- Show runtime defaults separately in a “Default props” table; TypeScript interfaces do not set runtime defaults.
- Identify callbacks, controlled state, and data shapes only when supported by supplied requirements or clearly label them as proposals.

2. Design Tokens
- Map color, spacing, typography, borders, radii, shadows, and sizing to semantic tokens.
- Use the project’s supplied token names when available.
- If no token system is provided, label token names as proposed placeholders. Do not imply that suggested names already exist.
- Mark pixel or color estimates from the image as approximate.

3. State Matrix
Cover Default, Hover, Focus, Active, Disabled, Loading, and Error. For each state, describe visual treatment, behavior, and accessibility cues. Mark a state “Not applicable” with a reason when appropriate. Separate observed states from proposed states.

4. Accessibility
- Recommend semantic HTML first; add ARIA only when native semantics are insufficient.
- Describe accessible name or label, keyboard interaction, focus order, and visible focus treatment.
- State relevant WCAG 2.2 AA contrast targets: 4.5:1 for normal text, 3:1 for large text, and 3:1 for applicable non-text elements.
- Do not claim contrast compliance from a screenshot alone. Identify the color pairs that require measurement against actual tokens or rendered code.
- Include other relevant accessibility concerns for this component.

5. Edge Cases and Content
Specify text wrapping or truncation, minimum and maximum widths, empty or missing content, validation, and localization. Mark requirements that need product confirmation.

6. Responsiveness
Describe expected behavior at mobile, tablet, and desktop sizes.
- Use supplied breakpoints when available.
- If breakpoints or layout shifts cannot be determined from the visual, ask before finalizing them.
- Label proposed breakpoint values and layout changes as recommendations, not observed facts.

7. Motion and Animation
Describe transitions, easing, duration, and micro-interactions only when supplied or visible in the source. Ask about material unknown behavior; otherwise label suggestions as proposals. Include reduced-motion considerations.

End with a short “Open questions and assumptions” list. If none remain, say so.

Keep the specification concise, specific, and technically clear. Do not fabricate measurements, design tokens, behavior, or implementation constraints.
```

## Customize before running

- **COMPONENT NAME** — The component being specified. Example: “account menu.”
- **TARGET TECH STACK** — Frameworks and styling tools. Example: “React, TypeScript, and Tailwind CSS.”
- **DESIGN SYSTEM / TOKEN SOURCE** — Existing design tokens or documentation. If none, enter “NONE PROVIDED.”
- **BEHAVIOR NOTES** — Known interactions or product requirements. Example: “Selecting an item navigates to its detail page.”
- **PLATFORMS / BREAKPOINTS** — Required devices, viewport widths, or project breakpoints. If unknown, enter “NONE PROVIDED.”
- **ATTACHED VISUAL** — Upload the screenshot, mockup, or other visual to analyze.

## Example output

*Illustrative excerpt for a fictional primary button visual. Token names and behavior below are proposals, not facts from a real design system.*

### 1. Component API

```ts
interface PrimaryButtonProps {
  label: string;
  disabled?: boolean;
  loading?: boolean;
  onPress?: () => void;
}
```

**Default props**

| Prop | Default | Status |
| --- | --- | --- |
| `disabled` | `false` | Proposed |
| `loading` | `false` | Proposed |

### 2. Design Tokens

| Property | Token suggestion | Evidence |
| --- | --- | --- |
| Background | `var(--color-action-primary)` | Suggested token; visual appears to use a solid accent fill |
| Border radius | `var(--radius-control)` | Approximate from the fictional visual |

### 3. State Matrix

| State | Specification | Status |
| --- | --- | --- |
| Default | Solid accent background with centered label | Observed |
| Focus | Visible outline with sufficient contrast | Proposed; verify in implementation |

### 4. Accessibility

Use a native `<button>`. Preserve keyboard activation and a visible focus indicator. Measure text and focus colors against the final token values before claiming WCAG conformance.

## Check before using

- Confirm that the visual was accessible and the correct component was analyzed.
- Check that inferred behavior and proposed tokens are labeled clearly.
- Resolve open questions about interactions and responsive rules.
- Verify contrast using actual colors in the design system or rendered component.
- Confirm that the specification matches the project’s stack and conventions.

## About this entry

Adapted and expanded from a submitted UI specification prompt. Version 1.0.0. Intended for AI tools that can access image input; image support and implementation details vary by product and account. Token names and values must be checked against the project’s design system. This prompt has not been runtime-tested across the listed tools.
