# Training-outline advisory QA

Use this mode for an existing training outline, agenda, workshop plan or facilitator outline. Review only the artifact and scope supplied. For actual final files, continue using the parent skill's final-candidate, repair, regression and release workflows. The extension does not replace them.

## Read and select scope

Read [standards](outline-review/01-review-standards.md), [severity and closure](outline-review/02-severity-and-finding-rules.md), and [outline dispositions](outline-review/08-disposition-gate.md). Use [intake](outline-review/00-intake-checklist.md), [alignment/time](outline-review/03-objective-alignment-and-timing.md), [practice/assessment](outline-review/04-activity-assessment-and-facilitation.md), [accessibility](outline-review/05-accessibility-review.md), [sources](outline-review/06-research-source-and-evidence-rules.md), and [higher-risk/software checks](outline-review/07-higher-risk-and-software-controls.md) as applicable. Read [handoff and record contract](outline-review/09-handoff-and-validation.md) before exporting the record.

Choose quick triage, full review, or review plus proposed revision. A review-only request does not authorize rewriting. A full review need not create a proposed artifact to satisfy validation. Missing/unreadable input or a text-only request may return an explicitly limited narrative. Proportional questioning does not require repeating known inputs.

## Review sequence

1. Freeze original source identity/version/hash and stable finding/source/objective IDs. Record audience, performance scope, duration, environment and supplied requirements without inventing authority.
2. Review performance alignment, source authority, original time arithmetic, declared breaks/administration, practice/scoring, facilitator usability and access provisions. Unknown original allocations remain unknown. Keep design evidence separate from actual rendered/file/platform tests.
3. Classify findings by impact at the artifact's claimed maturity. Preserve strengths and record evidence gaps, confidence, owner roles and acceptance criteria. Never silently omit an original objective or turn a preference into a required defect.
4. If authorized, propose only outline-level corrections with original-to-revised objective treatments. Keep proposed fixes unverified and original/proposed judgments independent. All material removals/narrowing decisions stay open until accepted.
5. Prepare a [development handoff](../templates/outline-review/development-handoff.md) to Live Training Session Design for unfinished scenarios, keys, materials and delivery work. Retain finding/source/objective IDs, artifact hashes, constraints, decisions, dependencies and acceptance criteria. Do not imply accepted ownership, external dispatch or workflow execution.
6. Complete the twelve review-quality checks. Run the local validator only if available; report actual result and limits. Later implementation returns version-specific evidence to QA for re-check rather than automatic closure.

## Relationship to parent QA statuses

Keep the specialized outline judgment alongside the parent QA status. Never relabel it as release authority.

| Outline result or finding | Parent QA interpretation |
| --- | --- |
| Critical / Major / Minor | CRITICAL / MAJOR / MINOR, retaining original F IDs and a stable DEF alias if needed |
| Enhancement | NOTE, optional improvement |
| Major revision required with material defects | QA FAIL for the reviewed outline-design scope |
| Not reviewable | NOT VERIFIED for the unsupported scope; identify the missing input |
| Minor revisions required | QA PASS WITH CONDITIONS only if remaining conditions satisfy the parent acceptance/owner/date/authority rules; otherwise QA FAIL or NOT VERIFIED as supported |
| Meets outline-review criteria | QA PASS only for completed, evidenced outline-design checks; actual materials and delivery remain separate |
| Prepared handoff | Not sent, accepted, executed or approved |

Missing required qualified review or material source decisions block favorable results in their applicable scope. Do not convert a known material defect into NOT VERIFIED to avoid QA FAIL. Do not call actual inaccessible final output merely an outline-design question.

For advisory review records, record AUTHORIZATION NOT VERIFIED and release_executed false. Actual authorization or release, if separately performed and evidenced, belongs in the existing parent authorization/release records, not inferred inside this advisory contract.

## Validator and examples

From the skill folder:

```sh
python scripts/validate_outline_review.py --package . --review examples/outline-review/worked-review.json --root .
```

Use the [worked review](../examples/outline-review/02-complete-worked-review.md), [unchanged source](../examples/outline-review/01-flawed-outline.md), [proposed revision](../examples/outline-review/03-proposed-revision.md), [handoff](../examples/outline-review/04-development-handoff.md), and [JSON record](../examples/outline-review/worked-review.json). Both example versions retain material unresolved findings and scoped QA FAIL; authorization is unverified and release has not occurred.

The standard-library validator checks arithmetic, IDs, hashes, objective coverage, lifecycle evidence records, handoff dependencies, and the QA status/severity mapping. It does not judge source truth, authenticate reviewer actions, inspect rendered accessibility, test learning effectiveness or grant release. Its structural PASS is a result about record consistency only.
