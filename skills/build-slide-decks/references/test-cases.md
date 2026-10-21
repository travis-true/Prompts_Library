# Validation test cases

## Case 1: Source-grounded training deck

**Request:** Turn an approved procedure into a 45-minute beginner training deck with demonstration and practice.

**Expected behavior:** Define the communication and performance job, preserve source meaning, create a learning progression, place facilitation detail in notes, protect practice, and avoid using slides as the only learning support.

## Case 2: Executive decision deck

**Request:** Recommend one of three options to executives using supplied evidence.

**Expected behavior:** Build a decision arc with criteria, tradeoffs, recommendation, implications, and explicit decision; avoid a training agenda or decorative story.

## Case 3: Supplied template

**Request:** Populate a user-provided corporate template without changing its visual system.

**Expected behavior:** Inspect and preserve masters, layouts, fonts, palette, margins, and recurring elements; reuse layouts rather than recreating the look.

## Case 4: Redesign with locked content

**Request:** Improve the deck’s visual appeal but do not change approved wording or slide order.

**Expected behavior:** Treat content and order as locked, improve only authorized visual properties, and report conflicts where wording prevents fit rather than silently editing it.

## Case 5: Insufficient source

**Request:** Build a procedural deck from informal notes that conflict with policy.

**Expected behavior:** Preserve the conflict, block affected factual slides, produce a provisional architecture if useful, and identify the accountable resolver.

## Case 6: No deck-generation capability

**Request:** Deliver an editable PowerPoint when the host can produce only text.

**Expected behavior:** Provide an implementation-ready blueprint and clearly state that no editable file was created.

## Case 7: Data-heavy source

**Request:** Put a large spreadsheet of results into a concise presentation.

**Expected behavior:** Select evidence that supports the communication job, interpret it, choose appropriate charts or tables, state units and limitations, and move nonessential detail outside the main narrative.

## Case 8: Dense source document

**Request:** Convert a 40-page report into five slides.

**Expected behavior:** Prioritize the audience outcome and essential evidence, state exclusions, avoid tiny text, and use notes or companion materials for necessary detail.

## Case 9: Accessibility requirement

**Request:** Create an accessible virtual presentation for a mixed audience.

**Expected behavior:** Design readable hierarchy, contrast, alt text, captions/media alternatives, reading order, equivalent interaction, and verified status.

## Case 10: Existing deck repair

**Request:** Fix clipping, inconsistent spacing, weak titles, and broken citations without changing meaning.

**Expected behavior:** Inspect every slide, preserve content scope, repair visual and technical defects, verify all renders, and report what remains unverified.

## Blocking failures

The skill fails validation if it:

- writes visible copy for the producer instead of the audience;
- invents facts, data, people, quotes, sources, approvals, or QA results;
- treats an agenda as a narrative;
- assigns multiple unrelated jobs to crowded slides;
- shrinks type instead of editing copy or layout;
- ignores a supplied template or flattens its structure without cause;
- uses repetitive card-grid or dashboard styling by default;
- includes decorative or misleading visuals;
- omits source traceability for non-trivial claims or external assets;
- claims accessibility or visual QA without inspecting the result;
- delivers an editable file without rendering and checking every slide when the host supports it.
