# Live Training Session Design — demo extension 1.2.0

[Open skill](../skills/live-training-session-design/SKILL.md) · [Demo workflow](../skills/live-training-session-design/references/demo/workflow.md) · [Back to library](../README.md)

Live Training Session Design already covers demonstrations, software environments, fallbacks and release checks. It now incorporates Live Demo Script Builder 1.1.0 as a specialized mode. The existing [demonstration-script prompt](../prompts/turn-expert-notes-into-a-demonstration-script.md) links to these resources. No duplicate skill is added; counts remain 108 resources and 36 skills.

## Included
- Single-scene, script-improvement and explicit complete-demo modes; broader course modes remain intact.
- State preconditions, action side effects, success signals and safe handling of unknown mutation outcomes.
- Bounded recovery, no blind retry, safe switching and Planned / Created / Verified backup status.
- Fallback equivalence, omissions and actual verification distinguished from proficiency evidence.
- Corrected fictional TaskFlow example, complete learner facts, separate facilitator guidance, new-fact retry and created text storyboard.
- Planned 5/12/18-minute paths, thirteen quality records and prepared production/assessment/QA handoffs.
- Standard-library demo validator and regression suite, alongside the existing course validator.

## Use
Ask “Use Live Training Session Design to improve this demo script. Preserve source labels and state transitions, define safe recovery and disclose fallback limits.” Choose a single scene or complete demo package explicitly. Do not build a competing full course merely to satisfy a validator.

The live-training-session-design handoff destination means internal parent-course integration, not recursively invoking the same skill. Preserve source/finding/objective/scene/action/asset IDs, versions, dependencies, owners and acceptance criteria. Assessment development goes to Build Assessments and Evaluations; actual artifact/rehearsal/release checks go to QA and Release Assets. Handoffs remain Prepared; not executed.

## Validate from repository root
```sh
python scripts/validate_library.py
python skills/live-training-session-design/scripts/validate_demo.py --skill skills/live-training-session-design --record skills/live-training-session-design/examples/demo/demo.json --root skills/live-training-session-design
python tests/test_live_demo.py
python skills/live-training-session-design/scripts/validate_course.py --package skills/live-training-session-design --course skills/live-training-session-design/examples/workplace-communication-workshop.course.json --root skills/live-training-session-design/examples
python tests/test_live_training_session_design.py
```

The demo validator checks declared IDs, local assets, state chains, retry protections, timing arithmetic, fallback limits, learner/key references, thirteen quality records, rehearsal/release consistency and prepared handoff references. It cannot authenticate sources/reviews, test a live application, judge semantic equivalence, establish learner proficiency or approve delivery. A demo structural PASS cannot make the parent course ready; its separate quality and release gate still applies.

The example remains Draft complete; review required. TaskFlow is fictional; no real environment, live assignment/notification, access test, reset, delivery or organizational approval is verified. Text storyboard assets are created, not verified screenshots.

## Provenance and versions
The extension adapts revised Live Demo Script Builder 1.1.0; its MIT license is retained in `skills/live-training-session-design/references/demo/LICENSE`. The parent package revision is 1.2.0; existing course and demo example/schema versions retain their own identities. Runtime references/templates/examples are namespaced so existing resources remain intact.

## Verification — October 21, 2026
All 73 imported demo regression tests and all 30 existing course regression tests passed. Repository, skill metadata, demo package/record and parent course package/record checks passed. Two independent text-only trials confirmed that an uncertain assignment is not blindly repeated and that demo structural success does not grant parent-course readiness. These checks do not establish universal performance or actual delivery readiness.
