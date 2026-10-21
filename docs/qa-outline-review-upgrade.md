# QA and Release Assets — outline-review extension 1.1.0

[Open the skill](../skills/qa-and-release-assets/SKILL.md) · [Back to library](../README.md)

The existing QA skill now includes the Training Outline Reviewer 1.1.0 workflow as a specialized advisory mode. Its current name, path, icons, final-file checks, repair/regression modes and release/authorization controls are retained. No separate reviewer catalog entry is added; the library still contains 36 skills.

## What is included

- Proportional outline triage, full review, and authorized proposed-outline modes.
- Source-grounded findings, calibrated severity, lifecycle/closure evidence, and original/proposed dispositions.
- Objective coverage and preserve-first traceability, including the original tone objective.
- Separate total, break, administration and instructional time; the example is 90 total / 85 instructional minutes.
- Separate outline-design, rendered materials, delivery and qualification evidence.
- Review, finding, gap, traceability, proposed-outline and handoff templates.
- Worked original/review/proposal/handoff/JSON examples under `examples/outline-review/`.
- A standard-library validator and regression tests, including the outline-to-parent QA status mapping.
- A traceable handoff to [Live Training Session Design](../skills/live-training-session-design/SKILL.md) for unfinished development. Preparing it does not execute or dispatch it.

## Use

Ask: “Use QA and Release Assets to review this training outline. Keep the review scope explicit and prepare a development handoff for unresolved work.” Request a proposed outline only when needed. Review-only does not authorize editing or a full competing course build.

The reviewer retains stable finding/source/objective IDs and artifact hashes. Critical/Major/Minor map to CRITICAL/MAJOR/MINOR, while Enhancement maps to NOTE. The specialized outline disposition is separate from the parent QA result, actual authorization and execution. The example keeps scoped QA FAIL and AUTHORIZATION NOT VERIFIED because material work remains.

## Validate from repository root

```sh
python scripts/validate_library.py
python skills/qa-and-release-assets/scripts/validate_outline_review.py --package skills/qa-and-release-assets --review skills/qa-and-release-assets/examples/outline-review/worked-review.json --root skills/qa-and-release-assets
python tests/test_qa_outline_review.py
```

The validator checks records, references, hashes, timing, objective treatment, closure requirements, handoff coverage/dependencies and status mapping. It cannot establish source truth, actual reviewer execution, undeclared missing facts, independent severity judgments, accessibility, teaching effectiveness or approval. Native final artifacts still require the existing QA workflow.

## Provenance

The outline extension imports the revised Training Outline Reviewer package. Its original MIT license is retained at `skills/qa-and-release-assets/references/outline-review/LICENSE`. Runtime references/templates/examples are namespaced so existing QA resources remain intact.

## Verification — October 21, 2026

Repository validation, skill metadata validation, namespaced package/record validation and all 46 regression tests passed. The added QA mapping tests reject implied approval/release, an unconditional pass with material defects, missing condition acceptance, changed severity, duplicate defect aliases and missing candidate coverage.

Independent text-only trials checked both routes: an overloaded outline produced a scope-limited QA FAIL and a prepared development handoff without rewriting; a final-PDF request with no supplied candidate/evidence remained NOT VERIFIED with AUTHORIZATION NOT VERIFIED and no release claim. These are behavioral samples. No real final PDF, live delivery, rendered accessibility or organizational approval was verified during this extension.
