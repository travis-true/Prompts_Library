---
name: build-slide-decks
description: "Plan, write, build, revise, or quality-check professional presentations and slide decks for training, enablement, executive communication, recommendations, decisions, demonstrations, workshops, technical briefings, change communication, and reference use. Use when a user requests a PowerPoint, PPTX, Google Slides deck, presentation outline, slide-by-slide blueprint, speaker notes, visual redesign, template-based deck, accessible slide system, or deck review. Support source-grounded creation, existing-template preservation, audience-facing copy, narrative architecture, visual direction, editable-file production when tools permit, and rendered QA."
---

# Presentation and Slide Deck Builder

Turn approved content and presentation requirements into a coherent audience experience. Produce either an implementation-ready slide blueprint or an editable, verified deck according to the host tool’s capabilities.

## Governing rules

- Define the audience and communication job before selecting slides or layouts.
- Use only supplied or authoritative sources for factual, technical, procedural, policy, compliance, or data claims.
- Never invent people, quotes, metrics, outcomes, approvals, source evidence, or validation.
- Preserve user-provided templates, masters, layouts, branding, terminology, and approved content unless change is explicitly authorized.
- Write visible copy for the intended audience. Keep production notes, talk tracks, timing, citations, and implementation instructions in speaker notes or the build specification.
- Give every slide one primary narrative job and one main claim.
- Prefer lower-density slides with high-value content. Shorten copy or change the layout before shrinking type.
- Use visuals to clarify meaning, evidence, sequence, comparison, emotion, or context—not as decoration alone.
- Apply accessibility and source traceability throughout.
- Do not claim an editable file, visual inspection, accessibility pass, or source verification that was not completed.
- Preserve the source file when editing unless the user explicitly requests in-place replacement.

## Operating modes

Select one:

1. **Blueprint:** Create the narrative, slide sequence, visible copy, notes, visual direction, and source map without generating a deck file.
2. **Build:** Create an editable presentation in the requested supported format and verify it visually.
3. **Revise:** Improve an existing deck while preserving authorized content, structure, or template constraints.
4. **Template population:** Use a supplied presentation as the visual and structural source; duplicate and populate its layouts.
5. **Review and repair:** Inspect content, narrative, design, accessibility, fidelity, and technical defects; implement fixes only when authorized.

If the host cannot create or inspect the requested file type, use Blueprint mode and state the limitation plainly.

## Workflow

### 1. Establish the presentation contract

Determine:

- intended audience and their context, knowledge, concerns, and decision rights;
- presentation job: educate, persuade, recommend, enable, facilitate, demonstrate, report, or support a decision;
- desired audience outcome;
- central takeaway or controlling question;
- delivery setting, modality, duration, presenter, and expected interaction;
- required topics, content boundaries, sources, and claims;
- target format, dimensions, platform, editability, and publishing destination;
- supplied template, reference deck, brand kit, images, data, or existing content;
- accessibility, confidentiality, attribution, and approval requirements;
- deadline and expected QA level.

Ask grouped clarifying questions only when missing answers could materially change the deck. Target roughly 95% confidence when questions are permitted. If immediate work is requested, proceed with labeled assumptions and confidence limits.

Express the communication job:

> By the end, **[audience]** should **[understand, believe, choose, approve, discuss, or do]** because **[central takeaway or evidence]**.

### 2. Inspect and classify inputs

Classify every input as:

- governing source;
- approved supporting content;
- visual/template constraint;
- data or evidence;
- draft;
- example;
- historical;
- unverified;
- conflicting;
- out of scope.

For existing decks, inspect every slide, notes field, master, layout, theme, repeated element, image, chart, footer, and section pattern available to the host. Record what must be preserved, what may change, and what requires approval.

Stop affected factual production when sources conflict or lack sufficient authority.

### 3. Choose the visual route

Use the first applicable route:

1. **Existing deck, template, or reference presentation:** Treat it as the visual source. Preserve the master-layout-slide hierarchy, reuse its layouts, and edit inherited elements rather than flattening or recreating them.
2. **Explicit visual or brand direction:** Build a coherent custom system from the supplied direction.
3. **No visual direction:** Create a restrained professional system suited to the audience, content, and setting.

Do not mix unrelated template systems. Explicit user instructions override defaults.

### 4. Build the narrative architecture

Read [references/deck-types-and-arcs.md](references/deck-types-and-arcs.md). Select a cumulative arc that fits the communication job.

Create a slide sequence in which:

- the opening establishes purpose, relevance, stakes, question, or tension;
- each slide answers a question or creates the need for the next;
- evidence is interpreted, not merely listed;
- examples and visuals support the claim;
- transitions prevent logical jumps;
- the close resolves the opening with an action, decision, application, synthesis, or productive question.

An agenda is not a narrative. Do not end abruptly on a detail or generic thank-you slide.

### 5. Assign slide jobs

Read [references/slide-taxonomy.md](references/slide-taxonomy.md). For every slide define:

- slide number and stable ID;
- slide job;
- primary claim or takeaway;
- audience-facing title;
- essential visible content;
- evidence and source;
- visual concept and layout type;
- speaker notes;
- interaction, demonstration, or transition;
- accessibility requirements.

Remove slides that repeat a prior job or do not advance the audience outcome.

### 6. Write audience-facing copy

- Use direct, specific, natural language.
- Prefer takeaway titles that state the point over topic labels.
- Use active verbs and plain language.
- Keep one-line titles on one line.
- Replace paragraphs with concise explanation, progressive reveal, speaker notes, or additional slides only when each addition earns its place.
- Avoid jargon, abstract noun clusters, empty slogans, mechanical parallelism, and repeated title formulas.
- Keep facilitator instructions, production comments, timings, and source management off the visible canvas unless the audience needs them.

Do not strip necessary qualifiers, conditions, exceptions, or uncertainty to achieve brevity.

### 7. Design the slide system

Read [references/design-and-accessibility.md](references/design-and-accessibility.md).

Define:

- canvas and safe margins;
- typography and hierarchy;
- palette and contrast;
- grid, alignment, spacing, and visual rhythm;
- image, icon, illustration, chart, table, and diagram treatment;
- title, section, content, activity, demonstration, evidence, and closing patterns;
- footer, source, version, and page-number behavior;
- animation and transition rules when applicable.

Vary slide silhouettes to fit the content while preserving visual coherence. Avoid dense dashboard or UI-card styling unless the communication job explicitly requires it.

### 8. Plan evidence and visuals

For each non-trivial claim or external asset:

- retain the source and locator;
- determine whether the audience needs visible attribution;
- include a source block in speaker notes;
- verify data labels, units, periods, definitions, and calculations;
- state uncertainty and limitations;
- never use a visual that implies unsupported precision or causality.

Choose the simplest effective visual:

- image for context, people, environment, or emotional grounding;
- chart for numeric relationships;
- table for exact comparison;
- diagram only when structure, sequence, or relationships are materially clearer visually;
- annotated screenshot for interface guidance;
- text when a visual adds no decision value.

Do not reuse the same non-background image repeatedly by default.

### 9. Design speaker notes

Include only applicable elements:

- purpose and transition;
- concise talk track;
- definition or context omitted from the canvas;
- demonstration setup and fallback;
- activity instructions and debrief;
- timing cues when requested;
- accessibility or facilitation notes;
- source block for external claims and assets.

Speaker notes must support delivery without becoming a transcript by default.

### 10. Build according to host capability

#### When editable deck creation is available

- Use the requested platform and format.
- Preserve native elements, master/layout relationships, editability, charts, notes, reading order, and alt text where supported.
- Use source or template layouts rather than drawing a look-alike deck.
- Create original layouts only when permitted.
- Keep intermediate files separate from final deliverables.

#### When only text output is available

Use [references/output-templates.md](references/output-templates.md) to produce an implementation-ready blueprint. Do not imply that a file was created.

### 11. Render and inspect

When the host supports rendering:

1. render every final slide;
2. inspect each slide at full size;
3. inspect a contact sheet for narrative flow and consistency;
4. fix unintended overlap, clipping, wrapping, weak contrast, broken connectors, unresolved placeholders, blurry crops, inconsistent spacing, and footer defects;
5. verify charts, tables, screenshots, notes, and citations against sources;
6. repeat until the deck passes.

Never dismiss an overlap warning without visual inspection.

### 12. Validate and release

Read [references/qa-and-release.md](references/qa-and-release.md). Report:

- deliverables and format;
- preserved template or source constraints;
- sources used and unresolved limitations;
- QA performed and results;
- accessibility status;
- approval or release status;
- open conditions and recommended next action.

Use only:

- `READY`
- `READY WITH CONDITIONS`
- `NOT READY`
- `NOT VERIFIED`

Do not claim production readiness from content review alone.

## Presentation-specific controls for learning decks

When the deck supports training:

- align slides to observable outcomes and session architecture;
- use the deck to support explanation, demonstration, interaction, practice, and debrief;
- do not make slides the sole learning asset when performance requires practice;
- protect realistic practice time from content expansion;
- place facilitator instructions and answer keys in notes or controlled guides;
- provide durable point-of-need support separately when learners must perform detailed work later;
- avoid claiming mastery from attendance, engagement, or slide completion.

When available, preserve the governing decisions from the training-session architecture and asset-routing skills.

## Required handoff

For Blueprint mode, provide:

- presentation contract;
- narrative arc;
- slide-by-slide specification;
- design system;
- notes and source map;
- implementation and QA requirements;
- gaps, risks, assumptions, and approval gate.

For editable-deck modes, provide the final file plus a concise summary of the build, sources, QA, accessibility, and unresolved conditions.

Use [references/test-cases.md](references/test-cases.md) to validate revisions to this skill.
