# Live Training Session Design — revision 1.1.0

[Open the skill](../skills/live-training-session-design/SKILL.md) · [Back to library](../README.md)

The existing skill now includes the Live Training Course Builder 1.1.0 templates, validator, corrected examples and evidence-based release controls. The existing name and path are preserved; no duplicate catalog entry was added. Use [Architect Training Sessions](../skills/architect-training-sessions/SKILL.md) for broader lifecycle governance and this skill for session/course production.

## Included improvements

- Proportional intake and outline, facilitator-guide and complete-package modes.
- Objective-to-instruction/practice/assessment alignment and explicit source authority.
- Separate total, break, administration and instructional time, with timed facilitator substeps.
- Complete fictional scenario facts, facilitator-only model answers, critical scoring criteria and equivalent retries.
- Separate learner practice and a recommended transfer/follow-up plan.
- Eleven quality checks distinguishing applicability, written-design review, rendered accessibility, delivery testing and qualified review.
- Evidence tied to artifact version, review method/date/role and open delivery requirements.
- A standard-library Python validator, JSON validation contract and 30 regression tests.
- Minimal skill frontmatter, generated discovery metadata and retained MIT attribution for the imported package.

## Use and validation

The skill can be read as instructions or imported as its individual folder using a supported host. It supplies no external service or unavailable authoring/research tool. Python is needed only to run the bundled validator. Native Office/PDF files must be created and checked using tools available in the chosen environment.

From the repository root:

```sh
python scripts/validate_library.py
python skills/live-training-session-design/scripts/validate_course.py --package skills/live-training-session-design --course skills/live-training-session-design/examples/workplace-communication-workshop.course.json
python tests/test_live_training_session_design.py
```

For a new facilitator guide or complete course package, create a course JSON sidecar following the [validation contract](../skills/live-training-session-design/references/09-validation-contract.md). Keep it synchronized with the actual Markdown and run the validator with `--course` and, when needed, `--root` pointing to the deliverable folder.

## Examples

- [90-minute facilitator guide and scoring key](../skills/live-training-session-design/examples/workplace-communication-workshop.md).
- [Separate learner practice](../skills/live-training-session-design/examples/workplace-communication-learner-practice.md).
- [Matching validation record](../skills/live-training-session-design/examples/workplace-communication-workshop.course.json).
- [Original short support-session outline](../skills/live-training-session-design/examples/60-minute-support-session-outline.md).

The 90-minute example contains 85 instructional minutes and a five-minute pause. Its state is Draft complete; review required. Actual rendered materials, delivery-tool accessibility, timed rehearsal, support ownership and sponsor arrangements remain open. An outline is explicitly a planning artifact.

## Verification limits

The validator checks structure, time arithmetic, substeps, declared practice facts, objective mappings, source IDs, scoring examples, record consistency and evidence excerpts. It does not verify source truth, undeclared missing facts, actual reviewer execution, teaching effectiveness, rendered-file accessibility or approval. Structural success never grants Ready for delivery.

The regression suite includes positive and negative cases for timing, critical omissions, invented requirements, scenario drift, missing/stale evidence, applicability, placeholders, unsafe file paths and learner-answer separation. Independent skill trials are behavioral samples, not a guarantee across every host or request. See the dated verification record below.

## Verification record — October 21, 2026

Repository validation, skill metadata validation, package/course structural validation and 30 regression tests passed. A text-only independent trial confirmed that the integrated skill exposes a schedule conflict and withholds unsupported delivery/accessibility claims. No live course, rendered native-file accessibility or actual learner results were verified.


## Revision 1.2.0 — live demo specialization

Adds the revised Live Demo Script Builder 1.1.0 as a namespaced mode while retaining the original course workflow, validator and examples. See [demo usage, provenance and verification](live-demo-integration.md). Component and course evidence/release decisions remain separate.
