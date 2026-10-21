---
name: layered-image-prompts
description: "Build or revise image-generation prompts with clear subject, composition, lighting, detail, style, and exclusions. Use when Build or revise image-generation prompts with clear subject, composition, lighting, detail, style, and exclusions."
---

# Layered Image Prompts

## Purpose

Build or revise image-generation prompts with clear subject, composition, lighting, detail, style, and exclusions.

Primary audience: Workplace.

## When to use it

Use when you need to build or revise image-generation prompts with clear subject, composition, lighting, detail, style, and exclusions.

This skill writes prompts; it does not include an image generator. Control syntax and rendered results depend on the selected tool.

## Inputs and requirements

Rough idea or existing prompt, intended use, audience, target generator if known, aspect ratio, required text, visual constraints, and optional reference images.

This skill writes prompts; it does not include an image generator. Control syntax and rendered results depend on the selected tool. These instruction-only packages supply no external tools or executable scripts.

## Workflow guide

1. Identify the subject, intended use, required text, aspect ratio, target generator, and protected visual details. Inspect supplied reference images only with available image tools; ask for a description if inaccessible. Preserve the user's main idea.
2. Write the Idea layer as a short concrete subject-and-action statement. Translate vague quality requests into observable composition choices without adding conflicting subjects.
3. Write Camera/composition using framing, perspective, depth, and focal priority. Use lens or aperture language only when it helps a photographic effect; use layout and viewpoint terms for illustrations or diagrams.
4. Write Colors/lighting with direction, contrast, palette, and intended mood. Treat blue/calm, orange/warmth, or purple/tension as creative choices whose interpretation depends on context, not universal psychological facts.
5. Choose only 2–3 texture or micro details that support the subject. Use one style anchor, at most two. Prefer clear visual attributes; when two styles conflict, ask which should lead or state a dominant and secondary influence.
6. For a requested blend, record proportions as qualitative intent, not an exact controllable result. Write exclusions clearly; adapt to supported negative-prompt syntax only when verified for the target tool. Otherwise use ordinary language and prioritize desired visible features.
7. Check all layers for contradictions, unnecessary detail, text accuracy requirements, and crop/readability needs. Return labeled Idea, Camera, Colors, Details, Style, optional Blend, Negative, and Summary check, plus a combined copy-ready prompt. Explain only material choices. Flag unsupported controls; actual image generation is a separate request requiring an image tool.

### Start a request

```txt
Use Layered Image Prompts for this task.
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

Fictional brief: a calm 16:9 workshop banner about focused work, no lettering. Illustrative layers: Idea—a tidy desk beside a window; Camera—wide, eye-level view with empty space at right; Colors—soft warm morning light; Details—paper texture and subtle wood grain; Style—editorial illustration; Negative—no lettering or logos. Summary check: one focal area and room for a later title. Combined prompt: “Create a 16:9 editorial illustration of a tidy desk beside a window, viewed at eye level, with soft warm morning light, paper texture and subtle wood grain. Leave the right side open. Include no lettering or logos.”

## Check before using

Subject matches the brief; composition fits the use; only 2–3 details and up to two style anchors; exclusions are clear; no exact blend or image-quality guarantee; prompt generation and image generation are distinguished.

## Package scope

Instruction-only workplace edition reconstructed from the source workflow guide. No original ZIP, script, or external service is bundled. Required tools must be available separately. Structure can be validated locally; installation and runtime behavior have not been tested. See [skill use guidance](../../docs/using-skills.md).
