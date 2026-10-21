# Build Assessments and Evaluations — engagement extension 1.1.0

[Open the skill](../skills/build-assessments-and-evaluations/SKILL.md) · [Back to library](../README.md)

The existing skill incorporates Training Engagement and Assessment Designer 1.1.0 as a specialized live-training workflow. Its name, path, measurement methods, Design/Build/Revise/Review/Analyze modes and broader evaluation scope remain. No separate skill entry is added; the library retains 36 skills.

## Included resources

- Corrected fictional 90-minute example: 85 instructional minutes, embedded activities counted once, complete learner facts, separate facilitator keys, annotated models, feedback and new-fact retry.
- Unknown-stakes clarification when certification, authorization, qualification, eligibility or employment consequences may apply. No automatic low-stakes classification or invented passing rule.
- Source-grounded criterion descriptions, explicit No proficiency decision without an authorized standard, individual evidence and scoring-capacity requirements.
- Equivalent / Partially equivalent / Not equivalent fallbacks with actual verification separate from design. Recognition cannot substitute for operation evidence.
- Namespaced workflow, references, scoped templates, learner/key/JSON examples, structural validator and regression suite.
- Prepared handoffs to Live Training Session Design for unfinished parent-course integration and QA and Release Assets for actual artifact/evidence checks. Preserve supplied finding IDs and source/objective/asset IDs, versions, dependencies, owners and acceptance criteria.

## Use

Ask: “Use Build Assessments and Evaluations to improve these live-training activities and assessments. Preserve the parent objectives, sources and agenda; clarify decision stakes and prepare any required development and QA handoffs.” Request a complete package explicitly when needed.

Single assets can use scoped templates and manual checks. The specialized JSON schema is for live-training asset sets/complete packages; do not manufacture a course, agenda or evaluation levels for surveys, blueprints, analysis-only work or other unrelated measurement modes.

## Verify from repository root

```sh
python scripts/validate_library.py
python skills/build-assessments-and-evaluations/scripts/validate_engagement_package.py --skill skills/build-assessments-and-evaluations --record skills/build-assessments-and-evaluations/examples/engagement/package.json --root skills/build-assessments-and-evaluations
python tests/test_engagement_assessment.py
```

The standard-library validator checks declared fields, source/asset/objective references, agenda arithmetic and embedded intervals, complete fact/key references, scoring-standard records, fallback evidence limits, individual observation/workload, evaluation decisions, twelve quality records, readiness and prepared handoff references. It does not authenticate source truth or standards, decide semantic equivalence, observe learners, establish psychometric validity, test accessibility or grant approval. Consequence keywords are a backstop; semantic clarification remains required.

A structural PASS is not the parent QA result, instrument validation, release authorization or a learner result. The example remains **Draft complete; review required** with actual access/fallback and delivery checks unperformed. Apply the existing QA and Release Assets workflow to actual candidate files and approval evidence.

## Provenance

Resources are adapted from the revised Training Engagement and Assessment Designer 1.1.0 package. Preserve its MIT license in `skills/build-assessments-and-evaluations/references/engagement/LICENSE`. The runtime resources are integrated into the existing skill rather than installed as a second competing workflow.

## Verification — October 21, 2026

All 52 imported regression tests passed against the namespaced integrated resources. Repository validation, skill metadata validation and specialized package/record validation passed. Two independent text-only behavior samples confirmed that uncertain certificate-program use triggers clarification without a pass score, while a three-question pacing survey remains scoped to reaction and makes no learning claim. These checks do not establish real delivery, accessibility or organizational approval.
