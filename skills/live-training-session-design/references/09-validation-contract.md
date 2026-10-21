# Validation record contract (schema_version 1.1)

Create a JSON sidecar for facilitator guides and complete packages. Copy the structure in [the example record](../examples/workplace-communication-workshop.course.json), replacing the fictional content and retaining stable IDs. Use Markdown headings and bold metadata labels as in [the example](../examples/workplace-communication-workshop.md); these are checked against the record. An outline may omit the sidecar if it clearly remains Planning framework only.

Run from the skill directory:

```sh
python scripts/validate_course.py --package .
python scripts/validate_course.py --course examples/workplace-communication-workshop.course.json
```

For an external deliverable, supply its JSON path and `--root` pointing to its deliverable folder. Relative paths resolve inside that folder; escaping it is rejected. The validator uses only Python's standard library and reads local files. It does not execute course content, browse, upload or approve anything.

## Required top-level fields

| Field | Meaning |
| --- | --- |
| schema_version | String `1.1` |
| artifact_version | Version of the actual course; must match Markdown |
| document | Relative UTF-8 Markdown path |
| release_state | One of the four release states |
| total_minutes, break_minutes, administration_minutes, instructional_minutes | Integer time accounting; breaks and administration may be zero |
| higher_risk, software_training | Explicit booleans controlling conditional checks |
| agenda | Ordered rows: id, start_minute, minutes, kind (instruction/break/administration), substeps (cue, minutes) |
| supporting_documents (optional) | Relative path, required_quotes and forbidden_quotes for checking learner-file consistency and answer-key separation |
| sources | id, kind (supplied/fictional/recommendation/official), locator; local_path and quote when local |
| objectives | id, text, instruction_modules, practice_ids, assessment_ids |
| practices | id, source_id, prompt_quote, required_facts list and facts object |
| assessments | id, practice_id, source_id, criteria, threshold, critical_rule `all`, invented_requirements_fail `true`, key_quote, feedback_quote, retry_quote; optional score_examples |
| traceability | element, source_ids, treatment (Preserved/Revised/Added/Removed) |
| open_items | id, owner, disposition, blocks_delivery, resolved; optional literal placeholder |
| quality_checks | All eleven IDs from the release rubric, each with applicability, status and evidence |

Each criterion has a unique id, positive integer points, a boolean critical flag and observable evidence. At least one criterion is critical. Threshold must be positive and no larger than possible points. Optional score_examples cover exactly the criterion IDs, map them to earned points, and declare expected_pass; an invented requirement always fails. These examples test scoring logic, not real learner performance.

Applicable Pass records require method, reviewer, ISO date, current artifact_version, and evidence entries containing a local path, literal quote and observed result. Non-applicable records require rationale, null status and empty evidence. Never fabricate these fields to make validation pass. Preserve Not checked and the draft state when work remains.

Markdown must include bold Version, Release state, Agenda total, Break minutes, Fixed administration minutes, Available instructional time and Allocated instructional time labels. Time values use `N minutes`. The agenda starts with an elapsed `H:MM` column followed by integer Minutes; its rows must match the record. Required fact strings, objective text and evidence excerpts must appear in the referenced Markdown. This intentionally constrained format makes drift detectable; adapting the validator is necessary for substantially different formats.

## Limits

A successful run checks structural consistency, totals, IDs, literal excerpts and recorded evidence requirements. It cannot detect all omissions, judge whether every necessary fact was declared, evaluate source authority or truth, inspect native-file accessibility, verify that a reviewer actually performed a test, or approve a course. Preserve separate content review, rendered-artifact checks and delivery verification. No static validator result grants Ready for delivery.
