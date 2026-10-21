# Structured validation and handoffs

Use [campaign.json](../../examples/copilot/campaign.json) for schema 1.1. The example has 30 sequence-only tips, 60 draft Teams/SharePoint assets and selected email/card examples. Other batches can declare their own size/channels; do not invent channels or a full campaign for a single-tip request.

```sh
python scripts/validate_copilot_campaign.py --skill . --record examples/copilot/campaign.json --root .
```

The standard-library script checks IDs, local paths, tip and channel references, distinct scenario/output/check data, prompt components, calendar ordering, prerequisites, source/claim scope, dates, metric definitions, lifecycle/version consistency, fifteen quality records, unresolved blockers and prepared handoff references. It does not authenticate sources/reviewers, judge semantic uniqueness/learning, run Copilot, render channels, verify telemetry permission, schedule or publish anything. Text duplication checks are indicators, not semantic quality certification.

Fields: schema/artifact version, overview and release state; sequence-only calendar or dated calendar with timezone/cadence; source records and claim scopes/statuses; tips with complete input/goal/context/source/expectation/model/review/reinforcement and paths; channel assets; metrics; fifteen quality records; open items; release authorization; handoffs. Dates and quotations locate declared evidence, not independent authority. Preserve unknown numeric results as null.

Prepare QA and Release Assets, Build Assessments and Evaluations, and authorized-channel-publishing-owner handoffs with original finding/source/claim/tip/asset/metric IDs, versions, dependencies, owners and acceptance criteria. Publishing owner is a role until a real authorized recipient is confirmed. A prepared handoff is not sent, accepted, scheduled or executed. Keep release, scheduling and actual publication evidence separate.

Optional collection can be Excluded; not collected with a rationale. Tips without a selected metric need an explicit measurement_exclusion and empty metric_ids. Do not create data collection merely to complete the record.

Rendered visual records require an existing local rendered_path, matching rendered_sha256 and alt_text_final true with final rather than provisional alt text. These verify file identity and declared completion only; actual access testing still needs evidence. Approved channel content requires a matching content_sha256 in its approval record; edits invalidate that recorded approval.
