# Version-specific disposition gate

## Scope and language
Issue findings against an identified artifact/version. Use these instructional-design review terms:
- **Meets outline-review criteria:** reviewed scope is complete; applicable required checks have evidence; no unresolved Critical, Major or Minor defects, material decision gaps or missing required qualified review.
- **Minor revisions required:** no unresolved Critical/Major findings or material decision/qualified-review gaps; only localized Minor issues remain.
- **Major revision required:** unresolved Critical/Major findings, material source/scope decisions or missing mandatory qualified review block a favorable determination, but meaningful review/revision is possible.
- **Not reviewable:** no readable intended course or controlling evidence so absent/conflicting that a defensible scoped assessment cannot be made. Do not use this label to discard domains that can be assessed; report partial scope explicitly.

Legacy mapping: Approved as-is → Meets outline-review criteria; Approved with minor revisions → Minor revisions required; Needs major revision → Major revision required. Preserve legacy labels only when citing the original artifact/history, never as formal approval.

A proposed revision has its own artifact ID/version and separate disposition. Until its material proposed changes, missing activities/keys and decision gaps have been verified, preserve the appropriate unresolved state. Original findings remain against the original version; later verified closure affects only the re-reviewed target version.

## Decision rules
Use unresolved findings relevant to the current version, not the historical total. A proposed/implemented/deferred fix is not verified closure. Open Enhancements alone do not prevent a favorable determination. Unverified required criteria or material gaps cannot be converted into Minor just to enable a favorable label.

Keep these scopes separate: outline design, rendered artifacts, live delivery, subject-matter qualification and formal approval. A favorable outline-design disposition does not mean Ready for delivery. If delivery readiness is in scope, material untested delivery conditions block a favorable disposition for that expanded scope. If outside scope, mark them Not checked and include them in the handoff without presenting them as defects of the outline by default.

Record disposition, artifact/version, reviewed scope, basis, unresolved blockers, required revisions, evidence gaps, exclusions and required reviews. Do not imply organizational, legal, policy or compliance approval. Do not grant release from a validator result.
