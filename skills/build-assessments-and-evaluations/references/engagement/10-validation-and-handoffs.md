# Validation record and handoffs

Use [package.json](../../examples/engagement/package.json) as the schema_version `1.1` example for asset sets/complete packages. A single-asset request may use the scoped template/manual checks instead. Do not invent a parent course or all evaluation levels merely to satisfy the validator.

From the skill directory:

```sh
python scripts/validate_engagement_package.py --skill . --record examples/engagement/package.json --root .
```

For other deliverables, supply the JSON and its root folder. Paths must resolve inside that folder. The validator reads local UTF-8 files and uses the standard library only; it does not execute course content, contact services or approve anything.

## Record fields

| Fields | Meaning |
| --- | --- |
| schema_version, artifact_version, document, release_state | Versioned record and matching Markdown identity/state |
| intended_use, stakes | Decision use; classification; consequence_signals; clarification_required/status/answer/clarified_use; consequential_decisions_enabled |
| sources, objectives | Stable IDs, versions, locators and local content; original learning scope |
| agenda and time totals | Ordered module IDs/start/minutes/kind; separate total, break, administration and instruction |
| assets | IDs/version, kind, objective IDs or support/evaluation purpose, source IDs, type/difficulty/delivery/stake, parent/offset/time/placement, learner/key paths and quotes, required facts, evidence, criteria, feedback/retry, metadata and decision limits |
| standards | Actual authorized standard ID, authority, source_id, artifact_version, scoped asset_ids, threshold, critical_rule `all`, and local evidence path/quote; empty when absent |
| fallbacks | Construct/task/evidence, equivalence classification/rationale, omissions, actual verification status and proficiency-use limit |
| observation | Learner count, individual collection, minutes per response, total review minutes, placement, actual scoring status and Not observed handling |
| evaluation | Selected measures with decision/question, indicator, source assets, owner, timing, analysis/action/limits; rationale for unselected levels |
| quality_checks | Q-01–Q-12 individually with applicability, method, evidence, reviewer/date/version and actual status |
| open_items | IDs, owner, description, blocking flag and status |
| handoff_document, handoffs | Local handoff path; both production/QA destinations, stable source/asset/objective references, tasks, acceptance criteria and prepared status |

Stakes classification: unresolved, low-stakes-practice, proficiency-check, high-stakes-qualification. Consequential-use signals in intended_use or declared signals require clarification when use is unknown. Record an actual answer and clarified_use of practice-only-no-consequences, proficiency-decision or consequential-decision. Never fabricate an answer to unblock design.

An asset without an actual decision rule has null decision_rule and classification No proficiency decision. Descriptive practice criteria are not an approved cut score. A supplied decision rule references an actual authorized standard with matching scope/version/threshold and critical_rule `all`. The rule may be documented while actual decisions remain disabled; no learner result is inferred. Untested or changed-construct fallbacks cannot support omitted proficiency evidence.

Embedded intervals must fit non-break parent modules and not overlap. They are counted inside parent time once. Follow-up scoring/retry occurs outside the session; additional activities require parent reallocation. Complete required fact strings, keys, feedback and versions must resolve to actual local content. Keep keys out of the learner file.

## Handoffs

Prepare integration work for [Live Training Session Design](https://github.com/travis-true/Prompts_Library/tree/main/skills/live-training-session-design) and actual file/evidence verification for [QA and Release Assets](https://github.com/travis-true/Prompts_Library/tree/main/skills/qa-and-release-assets). Retain original IDs/versions, constraints, stakes/standard decisions, owner roles, dependencies and acceptance criteria. Provide the handoff if a destination skill is unavailable; do not claim it was invoked, dispatched or executed. The worked [handoff](../../examples/engagement/handoff.md) is prepared only.

## Limits

Structural validation checks declared fields, arithmetic, reference coverage and recorded authority/evidence consistency. Keyword screening is a backstop, not semantic classification. It cannot discover every omitted fact or consequence, authenticate standards/reviewer actions, judge construct equivalence, observe learners, evaluate psychometric quality, test accessibility or grant approval. State actual manual checks and limitations separately. Do not infer readiness or learner proficiency from script success.
