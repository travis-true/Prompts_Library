# Accessibility and compliance QA

## Accessibility evidence

Combine applicable:

- automated checks;
- semantic or structural inspection;
- visual inspection;
- keyboard testing;
- screen-reader or assistive-technology testing;
- zoom, reflow, and alternate-format testing;
- representative user testing.

Record what was actually performed. Automated tools cannot determine whether alt text is meaningful, reading order is logical, instructions are clear, or an equivalent experience exists.

## Common accessibility controls

- descriptive title and language metadata;
- logical headings, landmarks, lists, and reading order;
- meaningful link and control names;
- sufficient contrast and readable typography;
- no color-only, audio-only, motion-only, or position-only meaning;
- meaningful alt text and decorative marking;
- simple tables with headers and relationships;
- captions, transcript, and audio description or equivalent;
- keyboard operation, visible focus, and logical focus order;
- clear instructions, labels, errors, and recovery;
- zoom, reflow, resizing, and responsive behavior;
- accessible alternatives for timed, drag-and-drop, hover-only, or pointer-dependent interactions.

## Privacy and classification

Verify:

- permitted source data and intended audience;
- correct classification label and access control;
- fictionalization, masking, redaction, or removal;
- no unnecessary identifiers, secrets, tokens, credentials, hidden data, comments, or metadata;
- retention, deletion, sharing, and publishing controls;
- screenshots, recordings, examples, logs, and test data follow the same rules as final content.

## Source, licensing, and attribution

- Trace non-trivial claims, data, images, media, fonts, icons, and excerpts.
- Verify license, permission, or organizational approval where required.
- Keep citations accurate and usable.
- Do not expose restricted internal source locations to unauthorized audiences.
- Respect attribution, modification, distribution, and expiration conditions.

## High-risk release controls

Require applicable evidence for:

- legal, policy, safety, security, privacy, financial, contractual, or regulatory review;
- content owner validation;
- version and effective date;
- known exceptions and escalation;
- authorized environment and audience;
- regression and rollback;
- named release authority.

Do not treat a general QA pass as specialist approval.
