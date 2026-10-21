# Handoff and structural validation

## Production boundary

A review can propose an outline-level correction. Do not develop a separate full course package under the reviewer. Prepare a handoff to **live-training-session-design / Live Training Session Design**, preserving original artifact IDs/versions/hashes, source IDs/locators, finding IDs, objective treatments, exact constraints, unresolved decisions, owner roles, dependencies and acceptance criteria.

The destination's repository definition is [Live Training Session Design](https://github.com/travis-true/Prompts_Library/tree/main/skills/live-training-session-design). If it is not available as a callable skill, provide the self-contained handoff for its workflow; do not claim it is installed or has run. Preparation alone authorizes no communication or external dispatch. Receiving development should produce versioned artifacts and return actual acceptance evidence for reviewer re-check; findings remain open until verified.

## Record contract

Use [the complete JSON example](../../examples/outline-review/worked-review.json) as the readable-outline review record (schema_version `1.1`). A quick triage or unreadable/missing outline may return a scope-limited narrative instead; do not fabricate a readable artifact to satisfy the record. For full-review mode, record only actual input artifacts and their dispositions, leave revised_objective_ids and objective_treatments empty, omit proposed_timing, and use null target_artifact_id for unimplemented findings. Preserve original objective IDs and handoff tasks. For review-plus-revision, add the proposed artifact, timing, treatments and independent disposition. Do not generate an unauthorized revision to satisfy a tool.

Run from the skill folder:

```sh
python scripts/validate_outline_review.py --package . --review examples/outline-review/worked-review.json --root .
```

For external deliverables, supply the review JSON and `--root` containing its relative paths. All local evidence/artifact paths must remain inside that root. The script reads local UTF-8 text, checks SHA-256 for referenced artifact bytes and uses only Python's standard library. It does not browse, execute course content, contact services or approve anything.

| Field | Required content |
| --- | --- |
| schema_version, review_id, review_version | Contract `1.1`, stable review identity and version |
| mode, scope, report | full-review or review-plus-revision; explicit reviewed domains; local Markdown report |
| artifacts | Unique IDs, version, path, SHA-256 of actual bytes; preserve original bytes |
| sources | Stable ID, kind, locator; artifact_id when backed by a local supplied artifact |
| original_objectives | Stable ID, source_id and literal source quote |
| revised_objective_ids, objective_treatments | Exactly one treatment per original; mapped revised IDs, findings, sources, rationale, decision owner/status |
| findings | Stable IDs, criterion layer, severity/impact/confidence, original/target identity, evidence, action, owner, acceptance criteria, lifecycle and actual closure record when applicable |
| severity_counts | Counts for all four severity categories, including zero |
| evidence_gaps | Unique IDs, description, materiality, owner, status; actual evidence for resolution |
| original_timing, proposed_timing | Artifact ID, capacity, row minutes/kind, totals, variance, break/admin/instruction totals; null when genuinely unknown in original |
| dispositions | Independent per-artifact judgment and all material blocker IDs |
| domain_checks | Separate accessibility-design, accessibility-rendered, delivery and qualified-review records |
| handoff | Destination, prepared status, artifact/source IDs, local handoff path, production tasks, preserved references, material decisions and dependencies |
| quality_checks | Q-01–Q-12 individually, applicability, status and actual version-specific evidence |

Each task has original finding/source/objective IDs, action, acceptance criteria, owner, dependency IDs and status. References must resolve; task dependencies must not cycle. Each unresolved defect must have a task. Optional Enhancements need not be accepted. Deferred findings retain their impact and need a real decision record; deferral is not resolution.

Verified resolved requires method, actual reviewer/date, target artifact/version and local evidence path, literal quote and observed result. A later artifact change makes that version's closure evidence stale. Each Pass quality record similarly requires current review version, method, reviewer, ISO date and a local evidence excerpt/result. Do not invent values to pass the validator.

The worked Markdown uses `Review version`, `Original disposition`, `Proposed disposition`, explicit severity counts and agenda tables with `Start minute | Minutes | Kind`. Its paired artifacts/handoff must agree with the JSON. The constrained format supports deterministic comparison; other review formats require adaptation rather than claims that this parser covers them.

## Limits

Structural success checks hashes, arithmetic, references, coverage and recorded consistency. It cannot discover undeclared missing objectives/facts, confirm source authority/truth, determine severity independently, authenticate reviewer actions, evaluate learning effectiveness, inspect actual accessibility or grant approval. Keep those judgments explicit and evidence-based. Never convert the original or proposed disposition from a script's exit code.

## Parent QA mapping record

The integrated validator additionally requires `qa_bridge`: scope `outline-design`; one candidate_results entry per artifact (artifact_id, qa_status, authorization, release_executed); and one defect_map entry per finding (finding_id, unique qa_defect_id alias, qa_severity). Preserve the original finding IDs. Map Critical/Major/Minor/Enhancement to CRITICAL/MAJOR/MINOR/NOTE.

Material unresolved outline findings require scoped QA FAIL. Not reviewable maps to NOT VERIFIED. Required Minor revisions cannot receive unconditional QA PASS. QA PASS WITH CONDITIONS requires nonblocking rationale, owner, accepting authority, date and actual acceptance evidence for each condition. Authorization remains AUTHORIZATION NOT VERIFIED and release_executed remains false in this advisory record. Actual external authorization/release, if separately performed, belongs in the parent workflow's separately evidenced records.
