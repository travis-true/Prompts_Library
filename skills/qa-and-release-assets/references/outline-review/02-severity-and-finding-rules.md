# Severity, evidence and closure

## Calibrate to impact and artifact scope
- **Critical:** credible risk of material harm, a dangerous/altered controlling requirement, or a fundamental delivery/performance barrier. Explain the specific consequence and evidence; do not assume harm merely because a section is missing.
- **Major:** materially weakens the stated learning outcome, source reliability, design access or deliverability; correction may require redesign. Missing required participation alternatives, practice for promised performance, unsupported material claims or substantial overload may qualify.
- **Minor:** local clarity or usability issue with a limited correction; no material barrier to the reviewed scope.
- **Enhancement:** optional improvement, no demonstrated defect or required correction.

Use the same threshold in references, examples and reports. Explain severity with context: affected objective/requirement, impact, evidence and confidence. Missing audience/context may be a gap rather than a defect if conclusions remain supportable. Label unknown external conditions Not checked; do not report a proven inaccessible file without inspecting it. A lower severity for absent access arrangements requires a specific justification, not optimistic assumptions.

Combine shared root causes without inflating counts. Report original finding counts separately from current unresolved counts. Preserve severity history and rationale for any reclassification.

## Finding record
Use stable finding IDs. Include criterion layer (built-in / supplied requirement), category, severity, rationale/confidence, original artifact/version/location, source evidence or gap IDs, impact, proposed action, owner role, target artifact/version/location, acceptance criteria, dependencies, status, and verification evidence. No actual owner is assigned unless supplied; use role Unassigned when needed.

## Lifecycle
- **Open:** defect/gap recorded; no accepted correction.
- **Revision proposed:** suggested text or development action exists; not implemented or verified.
- **Implemented; verification pending:** a specific new artifact exists but acceptance checks are incomplete.
- **Verified resolved:** acceptance criteria actually checked against the target artifact/version; record method, evidence location/quote, observed result, reviewer identity/role and date. A script or proposed wording alone cannot close a semantic/design issue.
- **Deferred:** explicit decision records who accepted what, rationale, residual impact, target date/trigger and next owner. Deferral does not erase a blocking finding or grant readiness.
- **Reopened:** later evidence/change invalidates previous closure; preserve history.

Changing an artifact invalidates affected closure evidence unless the reviewer records why it still applies. Do not overwrite source hashes or claim the reviewer approved their own proposed revision without a separate re-review record. Enhancements may remain optional; their acceptance is not required for a favorable scoped disposition.
