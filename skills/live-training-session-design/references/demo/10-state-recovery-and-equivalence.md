# State, recovery and fallback equivalence

## State contract
Give every scene a known entry state and exit state. Record visible evidence separately from assumptions. Model each action as read-only, local draft edit, or mutation with precondition, affected record, expected transition, side effects, success signal and verification route. Assignment, sharing, sending, deletion and permission changes require explicit authority in the intended environment. A script specification is not permission to execute.

## Uncertain outcomes and retries
An error or missing confirmation does not prove an action failed. For a non-idempotent action, stop input and inspect the authoritative record/status or approved transaction history. Retry only after a verified not-applied result and an authorized safe-retry rule; otherwise never repeat. Name a finite recovery budget, including state-check time. If state cannot be determined within it, leave the outcome Unknown, stop the live mutation branch, and switch to a disclosed prepared asset. Do not create a duplicate, reassign, resend, or erase evidence to make the demonstration appear successful.

Choose continue/switch/skip/stop explicitly. Skip only optional content and preserve the required takeaway and safe state. Stop on unexpected real/private data, unauthorized changes, security/safety risk or integrity uncertainty. Describe containment and escalation; do not invent a successful cleanup. Reset must restore only authorized training objects and record actual before/after evidence; deletion is not automatically an acceptable reset.

## Equivalence
Record target objective, task/construct, primary evidence, fallback evidence, omissions, rationale and actual verification. Classify Equivalent, Partially equivalent, or Not equivalent. Distinguish equivalence of intended design from verification of an actual asset/path. Prepared screenshots may preserve observation of a finished result while omitting state transitions or independent operation. Narration/readback can preserve diagnosis without proving operation. Never infer individual proficiency from a presenter demonstration or audience recall.

Untested or changed-construct fallbacks cannot support claims about omitted evidence. Supply a narrower interpretation, accessible operation route or rescheduled practice. Match assets to source/environment versions and disclose when switching; do not imply a recorded/prepared state is a live result. No missing asset may be described as opened or available. Mark assets Planned / Created / Verified with local path or explicit external prerequisite and actual verification metadata when verified.

## Timing and scene variants
Count narration, actions/loading, checkpoint, transition and bounded recovery inside each scene budget. Sum scene budgets per path; do not add embedded interaction a second time. Identify omissions, entry-state dependencies and visible result in each compressed/standard/expanded path. A prepared entry state is a prerequisite, not an automatic result of skipped live actions. Do not switch a path mid-mutation. Expanded options are not rehearsed merely because listed.
