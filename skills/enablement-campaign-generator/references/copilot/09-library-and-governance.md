# Asset governance and release

## Asset identity
Record campaign/version, tip and channel-asset IDs, sources/claims/metrics, phase, difficulty rationale, exact content path, owner, review/approval/publication statuses, approval evidence/version, expiry, refresh dependency and reuse notes. Revisions invalidate affected approvals, schedules and evidence until rechecked. Preserve audit history rather than relabeling stale approvals.

## Distinct lifecycle states
Content: Draft / In review / Approved for this campaign / Expired / Retired.
Publication: Not scheduled / Prepared / Scheduled / Published / Withdrawn. Approval is not scheduling; scheduling is not publication. Record actual schedule/execution IDs, approved asset version, channel, timezone/date and verification evidence for actual operations. A prepared handoff has no execution status beyond Prepared; not executed. Never infer a future action from a generated calendar.

Campaign release: Planning framework only / Draft complete; review required / Needs revision / Ready for release. Ready requires every applicable required quality check, exact-version asset approval, supported/unexpired claims, policy/support/owner decisions, actual accessibility checks, permitted measurement design and explicit release authorization. Known defects require Needs revision. Missing actual review/testing means draft. No authorization may be invented from a fictional example.

## Required fifteen checks
Q-01 behavior alignment; Q-02 journey progression; Q-03 channel adaptation; Q-04 prompt usability; Q-05 product verification; Q-06 responsible use; Q-07 human review; Q-08 visual accessibility; Q-09 publishing ownership; Q-10 support path; Q-11 measurement validity; Q-12 privacy; Q-13 reusable metadata; Q-14 expiration; Q-15 higher-risk review. Record each individually with applicability/rationale, required flag, scope, actual method/evidence/reviewer/date/version and corrective action. Excluded checks are Not applicable, not Pass. Design checks can pass only for their actual written scope; actual rendered/tenant/approval checks remain separate.
