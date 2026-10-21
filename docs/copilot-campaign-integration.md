# Enablement Campaign Generator — Copilot extension 1.1.0

[Open skill](../skills/enablement-campaign-generator/SKILL.md) · [Copilot workflow](../skills/enablement-campaign-generator/references/copilot/workflow.md) · [Back to library](../README.md)

The existing Enablement Campaign Generator incorporates Copilot Tip Campaign Builder 1.1.0. It retains general tool/process/behavior adoption planning and proportional output. Microsoft-specific sources and the structured tip schema apply only to the Copilot mode. No duplicate skill is added; the library retains 108 active resources and 36 skills.

## Included
- Thirty differentiated fictional tip fixtures with complete GCSE prompts, task-specific models/human checks, retrieval/retry and new-joiner paths.
- Sixty Teams/SharePoint adaptations and selected email/card examples; visual briefs with provisional alt text.
- Claim/source scope, dependencies, documentation versus tenant verification and expiry controls.
- Defined attempt, self-reported repeat-use and reviewed-sample metrics with unknown values null and no actual collection.
- Fifteen individual quality records and separate exact-version content approval, release, scheduling and publication evidence.
- Namespaced references, templates and worked records; standard-library validator and regression suite.
- Prepared QA, assessment and authorized-channel-owner handoffs preserving supplied finding/source/claim/tip/asset/metric IDs and dependencies.

## Use
Ask “Use Enablement Campaign Generator to improve these Copilot tips. Preserve source and asset IDs, verify claim scope and keep metrics bounded.” Specify a single tip, batch, calendar/review or complete campaign. Do not expand a general three-post campaign into thirty Microsoft tips or invent employee data collection to satisfy the schema.

The example is sequence-only and remains Draft complete; review required. Models are author-created fixtures; visual briefs are not rendered images. No tenant testing, policy/support approval, employee results, accessibility, scheduling or publication is established. Package file links must be replaced by confirmed approved hosted routes before actual publication.

## Validate from repository root
```sh
python scripts/validate_library.py
python skills/enablement-campaign-generator/scripts/validate_copilot_campaign.py --skill skills/enablement-campaign-generator --record skills/enablement-campaign-generator/examples/copilot/campaign.json --root skills/enablement-campaign-generator
python tests/test_copilot_campaign.py
```

Validation checks declared structure, IDs, local paths, prompt/input/model consistency, duplication indicators, calendar/prerequisites, source/claim scope, channel coverage, approval hashes, visual identity/final alt text, bounded metrics, quality/lifecycle consistency, blockers and prepared handoff references. It cannot authenticate reviewers/sources, assess semantic quality, run Copilot or tenant tests, establish learning/adoption, grant data permission or authorize publication. A specialized structural PASS does not release the parent campaign.

## Provenance
Adapted from revised Copilot Tip Campaign Builder 1.1.0. Its MIT license is retained at `skills/enablement-campaign-generator/references/copilot/LICENSE`. Runtime resources are namespaced; the original general campaign workflow remains the parent entry point. UI metadata invokes the existing skill name.

## Verification — October 21, 2026
All 94 imported regression tests passed against the integrated namespaced resources. Repository validation, skill metadata validation and structured package/record checks passed. Two independent text-only samples confirmed that a general request-form campaign remains scoped without Copilot content and that views/reactions/reported attempts do not become learning/adoption claims or release/scheduling authorization. These checks do not establish universal correctness or actual campaign release.
