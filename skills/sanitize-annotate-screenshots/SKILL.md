---
name: sanitize-annotate-screenshots
description: "Transform screenshots into privacy-safe training assets while preserving the authentic interface. Use when a user asks to sanitize, anonymize, de-identify, fictionalize, redact, clean, annotate, label, add callouts to, or quality-check a screenshot; create matching clean and annotated PNGs; replace sensitive or organization-specific data with coherent fictional data; or audit screenshot fidelity, accessibility, and privacy."
---

# Sanitize and Annotate Screenshots

Transform a supplied screenshot into a faithful, privacy-safe training asset. Preserve the authentic application interface, replace every data-bearing source item with coherent fictional content, create the clean version first, derive any annotated version from that exact clean image, and verify the finished files visually.

Apply these instructions without depending on a particular LLM, operating system, or image-editing product.

## Choose the operating mode

Select the narrowest mode that satisfies the request:

1. **Full production:** Produce a clean sanitized PNG, a matching annotated PNG, and a QA report.
2. **Sanitize only:** Produce the clean PNG and QA report when annotations are not requested.
3. **Annotate an approved clean image:** Treat the supplied sanitized image as the clean master, confirm that it contains no unsafe source data, and add only the requested overlay.
4. **Audit only:** Inspect existing assets and report defects without changing files.
5. **Specification only:** Produce a replacement map, annotation specification, alt text, and QA plan when direct image editing is unavailable. Never claim that image files were created or visually passed.

## Apply the source hierarchy

Resolve conflicts in this order:

1. The user’s current screenshot-specific instruction
2. The user’s approved project-specific standard or fictional dataset
3. This skill
4. Reasonable production defaults

Treat the current screenshot as the authoritative layout reference. Do not substitute a remembered, generic, newer, or “improved” interface.

## Ask only for true blockers

Proceed with approved defaults unless one of these conditions exists:

- No usable screenshot is available.
- The interface is too cropped, blurred, or obstructed to preserve accurately.
- Annotations are requested, but neither the request nor the image reveals what the learner should notice or do.
- Two instructions conflict in a way that materially changes the output.
- The request requires an interface state that is absent from every supplied reference.

When blocked, ask once with one consolidated list. For an unclear annotation purpose, ask: **“What should the learner notice or do in this screenshot?”**

Do not ask for routine approval of fake names, annotation styling, filenames, crop, or output format.

## Preserve the locked interface

Preserve unless the user explicitly requests a change:

- Canvas dimensions, aspect ratio, crop, and visual context
- Window structure, application shell, navigation, title bar, and theme
- Ribbon, toolbars, tabs, menus, icons, labels, and command positions
- Pane and dialog dimensions and placement
- Row heights, spacing, density, typography, scaling, borders, separators, and shadows
- Selected, active, expanded, collapsed, enabled, disabled, and focused states
- Scroll position and visible platform treatment
- Standard non-sensitive product labels

Do not:

- Redesign, modernize, simplify, beautify, or conceptually illustrate the interface.
- Move, rename, invent, remove, or duplicate application controls.
- Mix controls from different products, versions, platforms, browsers, or devices.
- Change the interface to make room for annotations.
- Add device frames, decorative backgrounds, taskbars, browser chrome, cursors, or host-computer elements unless already present and instructionally necessary.
- reconstruct an interface from memory when the supplied pixels can be edited.

## Sanitize every data-bearing region

Replace every visible item that can identify or disclose a real person, organization, customer, member, vendor, project, account, system, event, or record.

Inspect:

- Window titles, account selectors, profiles, avatars, notifications, and status areas
- Folder, mailbox, team, channel, category, and saved-search names
- Message lists, reading panes, recipients, subjects, previews, bodies, signatures, and disclaimers
- Calendar titles, organizers, attendees, rooms, links, dates, times, and notes
- Chats, comments, documents, tables, dashboards, charts, forms, tickets, and IDs
- Files, folders, paths, URLs, browser tabs, bookmarks, addresses, recent items, and search history
- Phone numbers, postal addresses, usernames, employee numbers, account/member/claim numbers, financial values, verification codes, and credentials
- Logos, photos, initials, thumbnails, QR codes, barcodes, and scannable identifiers
- Small, partially visible, edge-region, obscured, or secondary text

Never preserve:

- PII, PHI, financial information, credentials, passwords, tokens, security answers, or verification codes
- Real employee, customer, member, producer, patient, or vendor information
- Real internal domains, mailbox permissions, access details, organization names, project names, or confidential labels
- Live public email addresses or live authentication, password-reset, payment, or account-recovery links
- A real logo or identifiable photo without explicit approval
- Source data that becomes readable after editing

Replace instead of blurring, pixelating, covering, or cropping when a realistic fictional replacement is possible. Remove or neutralize scannable codes rather than generating functioning codes.

## Build a replacement map

Before editing, inventory each source value and assign its replacement.

```text
SOURCE REGION: Reading pane sender
SOURCE TYPE: Person
REPLACE WITH: Avery Morgan
RELATED VALUES: avery.morgan@prairieridge.example; AM

SOURCE REGION: Subject and body
SOURCE TYPE: Project communication
REPLACE WITH: Project Juniper status update
CONSISTENCY NOTE: Use Project Juniper in the message, attachment, and folder
```

For each replacement:

- Preserve the data type, visual role, approximate length, capitalization, line count, density, and formatting.
- Use one plausible fictional scenario across the image.
- Match display names, email addresses, initials, roles, and avatars.
- Make the selected list item agree with the detail pane.
- Keep dates, times, counts, totals, owners, statuses, attendees, messages, files, and projects logically consistent.
- Reuse exact spellings wherever an entity repeats.
- Preserve only standard product text; replace user-created and organization-created labels.
- Never preserve source amounts, dates, totals, or identifier patterns when those patterns may be confidential.

For a multi-screenshot workflow, reuse the same fictional organization, identities, projects, dates, files, and records unless the user requests a new scenario.

## Use the approved fictional dataset

Use a user-supplied approved fictional dataset first. Otherwise use only the records needed from this default set.

### Organization

| Field | Value |
| --- | --- |
| Organization | Prairie Ridge Example Services |
| Short name | Prairie Ridge |
| Domain | `prairieridge.example` |
| Website | `https://www.prairieridge.example` |
| Address | 100 Example Plaza, Sample City, KS 00000 |
| Main phone | `202-555-0100` |
| General mailbox | `info@prairieridge.example` |
| Support mailbox | `support@prairieridge.example` |
| Training mailbox | `training@prairieridge.example` |
| Service desk | `service.desk@prairieridge.example` |
| Shared operations mailbox | `operations@prairieridge.example` |

Use a text-only **PR** placeholder for an organization logo or avatar.

### People

| Name | Role | Email | Initials |
| --- | --- | --- | --- |
| Avery Morgan | Senior Operations Coordinator | `avery.morgan@prairieridge.example` | AM |
| Jordan Lee | Project Manager | `jordan.lee@prairieridge.example` | JL |
| Maya Patel | Training Specialist | `maya.patel@prairieridge.example` | MP |
| Cameron Brooks | Business Analyst | `cameron.brooks@prairieridge.example` | CB |
| Elena Ruiz | Operations Manager | `elena.ruiz@prairieridge.example` | ER |
| Noah Bennett | Service Desk Analyst | `noah.bennett@prairieridge.example` | NB |
| Priya Shah | Communications Advisor | `priya.shah@prairieridge.example` | PS |
| Marcus Green | Systems Administrator | `marcus.green@prairieridge.example` | MG |
| Lena Foster | Program Coordinator | `lena.foster@prairieridge.example` | LF |
| Ethan Cole | Finance Analyst | `ethan.cole@prairieridge.example` | EC |
| Sofia Nguyen | Customer Experience Lead | `sofia.nguyen@prairieridge.example` | SN |
| Riley Turner | Department Supervisor | `riley.turner@prairieridge.example` | RT |
| Devin Carter | Compliance Specialist | `devin.carter@prairieridge.example` | DC |
| Harper Kim | Product Owner | `harper.kim@prairieridge.example` | HK |
| Miles Robinson | Data Analyst | `miles.robinson@prairieridge.example` | MR |

Use neutral initials, not a generated photographic likeness.

### External organizations

| Organization | Domain | Contact |
| --- | --- | --- |
| Cedar Valley Example Manufacturing | `cedarvalley.example` | `contact@cedarvalley.example` |
| Lakeshore Example Consulting | `lakeshore.example` | `hello@lakeshore.example` |
| Summit Grove Example Partners | `summitgrove.example` | `team@summitgrove.example` |
| Meadowline Example Logistics | `meadowline.example` | `dispatch@meadowline.example` |
| Silver Oak Example Solutions | `silveroak.example` | `services@silveroak.example` |

### Workplace scenarios

- Projects: Project Juniper, Project Willow, Project Harbor, Project Lantern, Project Summit, Project Meadow, Project Cedar, Project Atlas
- Teams: Operations Improvement Team, Digital Workplace Team, Service Experience Team, Project Delivery Team
- Channels: General, Project Updates, Training Resources, Questions and Support, Weekly Planning
- Folders: Project Juniper, Training Resources, Team Documents, Meeting Notes, Drafts, Reports, Reference Materials, Shared Files, Archived Items, Templates
- Files: `Project Juniper Timeline.xlsx`, `Weekly Operations Summary.docx`, `Training Readiness Checklist.xlsx`, `Communication Draft v2.docx`, `Monthly Service Report.pdf`, `Workshop Slides.pptx`, `Meeting Notes - Project Juniper.docx`, `Process Review Findings.pdf`, `Launch Checklist.xlsx`, `Participant Guide.docx`, `Support FAQ.docx`, `Project Status Dashboard.xlsx`
- Locations: Conference Room Aspen, Conference Room Cedar, Conference Room Flint, Collaboration Room 2, Training Room North, Microsoft Teams meeting
- Categories: Action Needed, Follow Up, Project Juniper, Training, Waiting for Response, Reference, Completed
- Statuses: Not started, In progress, Waiting, Ready for review, Approved, Scheduled, Completed, Closed

Use only statuses and interface states that actually exist in the source application.

### Safe values

| Type | Pattern or examples |
| --- | --- |
| Incident | `INC-EX-#####`, for example `INC-EX-10482` |
| Request | `REQ-EX-#####`, for example `REQ-EX-20841` |
| Change | `CHG-EX-#####`, for example `CHG-EX-30216` |
| Account | `ACCT-EX-####`, for example `ACCT-EX-1842` |
| Member | `MEM-EX-#####`, for example `MEM-EX-24017` |
| Claim | `CLM-EX-#####`, for example `CLM-EX-73104` |
| Employee | `EMP-EX-####`, for example `EMP-EX-0618` |
| Order | `ORD-EX-#####`, for example `ORD-EX-55203` |
| Invoice | `INV-EX-#####`, for example `INV-EX-41862` |
| Case | `CASE-EX-####`, for example `CASE-EX-9031` |
| Phone | `202-555-0104`, `202-555-0116`, `202-555-0188` |
| URL | A `.example`, `example.com`, `example.org`, or `.test` address |
| ZIP | `00000` |
| Version | `v1.0`, `v1.1`, `v2.0` |

Use clearly fictional identifiers containing `EX`, `DEMO`, or `SAMPLE`. Never use a celebrity, public figure, recognizable character, or source name with minor spelling changes.

### Reusable neutral content

Use or adapt these examples while preserving one coherent scenario:

```text
Subject: Project Juniper status update
Preview: The updated timeline and next actions are ready for review.

Hello,

The updated materials are ready for review. Please add comments by Thursday
afternoon so the team can finalize the next version.

Thank you,
Avery
```

```text
Thank you for today’s discussion. The meeting notes, decisions, and follow-up
actions are available in the Project Juniper folder.

Next steps:
1. Review the updated timeline.
2. Confirm task owners.
3. Add comments before the next meeting.
```

Shift example dates to a coherent fictional workweek appropriate to the asset. Never reuse sensitive source dates.

## Build the clean image first

Use the environment’s native image-editing capability when available.

1. Inspect the original at full resolution.
2. Preserve the locked interface and crop.
3. Replace every mapped data region.
4. Match local typography, background, spacing, alignment, borders, and density.
5. Inspect small text, edges, title bars, secondary panes, notifications, tooltips, and status areas.
6. Remove seams, ghosting, residual glyphs, stretched icons, duplicated rows, and malformed text.
7. Save the clean image before adding annotations.

Do not add training callouts inside application content. Do not reconstruct the annotated version separately.

## Add restrained annotations

Create the annotated image by duplicating the final clean image and adding a removable overlay.

### Choose the simplest method

- **Direct callout:** One isolated control or concept
- **Numbered sequence:** Ordered steps
- **Target outline:** A field, pane, menu, group, or region
- **Magnified inset:** A target too small to read at final use size
- **Movement path:** Drag-and-drop or directional motion
- **Two authentic frames:** Mutually exclusive states that cannot coexist in one image

Never merge impossible states into one screenshot.

### Apply the visual standard

| Element | Standard |
| --- | --- |
| Primary label | Midnight `#003B5C`; white text |
| Outline and leader line | Bluejay `#41B6E6` |
| Number marker | Bluejay fill; Midnight text |
| Optional light label | White fill; Midnight border and text |
| Warning only | Warning Red `#C63527` |
| Font | Segoe UI, Arial, Helvetica, or sans-serif |
| Callout at 1920×1080 | 24–28 px, semibold |
| Number at 1920×1080 | 22–26 px, bold |
| Minimum text at 1920×1080 | 18 px |
| Leader line at 1920×1080 | 3 px |
| Target outline at 1920×1080 | 3–4 px with 4–8 px clearance |
| Safe edge margin at 1920×1080 | About 24 px |

Scale proportionally for other dimensions. Verify readability at the final document, slide, or web-display size.

Use Warning Red only for a genuine caution, error, destructive action, or “do not” instruction. Never rely on color alone. Avoid white text on Bluejay as the default.

### Write and place labels

- Use no more than three annotations by default.
- Exceed three only for a necessary longer sequence, an explicit request, or a case where multiple frames would be less effective.
- Begin task labels with an action verb.
- Use the exact visible product term.
- Keep one idea per label, usually 2–6 words and fewer than 10.
- Prefer **Select** over **Click** for mouse, touch, keyboard, and accessibility contexts.
- Place labels in open space, near the target, with consistent alignment.
- Keep targets, required text, values, selected states, and platform identifiers visible.
- Use straight or single-elbow leader lines that end precisely at the target.
- Use arrows only for movement or direction.
- Do not imitate a native button, menu, toast, tooltip, or dialog.
- Avoid decorative curves, glows, heavy shadows, yellow text highlights, and unnecessary dimming.

Preferred labels include **Select Automatic Replies**, **Set the time range**, **Open Settings**, and **Review the selected message**. Avoid **Click here**, **Important**, and **This button**.

## Write accessible supporting text

Provide:

- Screenshot ID or title
- One-sentence caption
- Concise alt text
- Sanitization summary
- Annotation list
- QA result
- Any unresolved limitation

Write alt text that identifies the application or screen, states the relevant interface state, and names the emphasized control or action. Avoid “image of,” “screenshot of,” decorative details, and the full procedure.

Example:

> Classic Outlook Automatic Replies dialog showing the control used to enable replies and set a scheduled time range.

Keep captions, alt text, QA scores, screenshot IDs, filenames, and production notes outside the image.

## Name the deliverables

Use:

```text
[SCREENSHOT-ID]_[Short-Description]_v1.0_CLEAN.png
[SCREENSHOT-ID]_[Short-Description]_v1.0_ANN.png
[SCREENSHOT-ID]_[Short-Description]_v1.0_QA.md
```

Create a concise application-and-task ID when the user supplies none. Preserve the source dimensions and crop unless instructed otherwise.

## Run visual QA

Inspect the finished clean image at 100% zoom. Compare the annotated image directly against it. Never report visual QA as passed without inspecting the final files.

Score 100 points:

| Category | Points |
| --- | ---: |
| Privacy and data sanitization | 30 |
| Layout and interface fidelity | 25 |
| Annotation and instructional accuracy | 20 |
| Text and visual quality | 15 |
| Output, accessibility, and consistency | 10 |

For a clean-only request, treat annotation accuracy as a 20/20 not-applicable equivalent.

Apply the release rules:

- **95–100:** Production ready only when no Critical or Major defect exists
- **85–94:** Revise and retest
- **Below 85:** Reject and regenerate
- **Any automatic fail:** Reject regardless of score

Treat any of these as an automatic fail:

- Any real, sensitive, confidential, identifying, live, or source-specific data remains.
- A blur, crop, patch, or overlay leaves source data readable.
- The wrong application, version, platform, device, layout, required control, or state appears.
- Controls from different interfaces are mixed, duplicated, invented, missing, or materially redesigned.
- Required text is garbled, unreadable, materially misspelled, or random.
- An annotation points to the wrong target or covers the target or required content.
- Clean and annotated images differ beneath the overlay.
- Required dimensions, orientation, clean file, or annotated file are wrong or missing.
- A live domain, URL, email address, credential, verification code, functioning code, unapproved logo, or identifiable photo remains.
- An uninspected output is reported as passing.

Classify defects:

- **Critical:** Automatic fail, data exposure, invalid interface, or wrong instruction; reject and regenerate.
- **Major:** Material professional-use defect; allow one precise repair, then regenerate if it fails.
- **Minor:** Localized defect without exposure or altered meaning; correct and retest.
- **Observation:** Nonblocking preference; record only when useful.

Permit one targeted repair when the defect is isolated and the source remains the correct reference. If repair causes drift or fails, discard the candidate, return to the original screenshot and replacement map, rebuild the clean image, recreate the overlay, and rerun the full QA. Do not layer repairs onto a degraded image.

## Use the QA report

```text
Screenshot ID:
Title:
Application/platform:
Source dimensions:
Clean file:
Annotated file:
Alt text:
Caption:

Privacy and data sanitization: __ / 30
Layout and interface fidelity: __ / 25
Annotation and instructional accuracy: __ / 20
Text and visual quality: __ / 15
Output, accessibility, and consistency: __ / 10

Total score: __ / 100
Automatic-fail condition: Yes / No
Critical defects:
Major defects:
Minor defects:
Observations:
Repair attempt used: Yes / No
Decision: Production ready / Revise / Reject
Required correction:
QA date:
```

## Deliver only verified results

Deliver the requested files and supporting text together. Confirm that:

- No source data remains.
- Reserved fictional domains and identifiers are used.
- The interface matches the supplied screenshot.
- Required controls, terms, and states are accurate.
- Text is sharp and readable.
- The clean image contains no annotations.
- The annotated image is identical beneath the overlay.
- Every callout identifies the correct target without covering required content.
- All required outputs are present.
- The score is at least 95 with no Critical or Major defect.

If direct editing or final visual inspection is unavailable, deliver the specification-only output and state the exact limitation. Never invent completed files, inspection results, or approvals.
