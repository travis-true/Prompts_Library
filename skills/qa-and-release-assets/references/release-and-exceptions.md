# Release and exception rules

## QA disposition

| Status | Meaning |
| --- | --- |
| `QA PASS` | All required checks passed for the stated candidate and intended use |
| `QA PASS WITH CONDITIONS` | Only explicitly accepted, non-blocking conditions remain |
| `QA FAIL` | A blocker, critical defect, required major defect, or failed required check remains |
| `NOT VERIFIED` | Evidence is insufficient to determine the required quality status |

## Authorization status

| Status | Meaning |
| --- | --- |
| `AUTHORIZED` | Named authority approved the identified candidate for the stated use |
| `AUTHORIZED WITH CONDITIONS` | Authority approved the candidate subject to explicit conditions |
| `NOT AUTHORIZED` | Authority rejected or withheld release |
| `AUTHORIZATION NOT VERIFIED` | No valid authorization evidence is available |

QA disposition never substitutes for authorization.

## Exception record

Each exception must include:

- exception ID;
- candidate and defect or requirement;
- exact deviation;
- reason a fix is not being made before release;
- affected audience and use;
- risk and consequence;
- compensating control;
- owner;
- accepting authority;
- effective and expiration dates;
- review trigger;
- rollback or containment;
- prohibited uses.

An exception is not valid merely because a deadline exists.

## Release decision rules

- Do not release a corrupt, incomplete, materially inaccurate, unsafe, inaccessible, insecure, or unauthorized candidate.
- Do not downgrade severity solely to obtain a pass.
- Do not accept an exception outside the authority’s scope.
- Do not reuse an exception for a different version, audience, channel, or use without review.
- Expired conditions reopen the release decision.
- A new candidate invalidates prior final-byte QA unless equivalence is proven.

## Release execution evidence

If release is performed, record:

- authorized candidate ID and fingerprint;
- release destination and audience;
- date and responsible person/system;
- access and publication settings;
- version and status displayed;
- successful retrieval or opening after publication;
- rollback location or prior baseline;
- support and monitoring owner.

Without execution evidence, report “authorized for release,” not “released.”
