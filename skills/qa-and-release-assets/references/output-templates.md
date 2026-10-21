# QA and release templates

## Contents

1. QA contract
2. Candidate inventory
3. Test matrix
4. Evidence ledger
5. Defect register
6. Cross-format comparison
7. Exception record
8. QA disposition
9. Authorization and release

## 1. QA contract

- **Intended use and audience:**  
- **Candidate/package scope:**  
- **Source and requirements baseline:**  
- **Formats and environments:**  
- **QA level and mode:**  
- **Required checks:**  
- **Repair authorization:**  
- **QA owner, exception authority, and release authority:**  
- **Deadline, destination, rollback, and maintenance:**  

## 2. Candidate inventory

| Candidate ID | File | Format/size | Version/status | Fingerprint | Relationship | Intended use |
| --- | --- | --- | --- | --- | --- | --- |

## 3. Test matrix

| Test ID | Requirement | Candidate | Dimension | Method/environment | Blocking rule | Result |
| --- | --- | --- | --- | --- | --- | --- |

## 4. Evidence ledger

| Test ID | Expected | Observed | Evidence/locator | Evidence class | Limitation | Reviewer/date |
| --- | --- | --- | --- | --- | --- | --- |

## 5. Defect register

| Defect ID | Candidate/location | Expected/observed | Severity | Effect | Owner/disposition | Retest |
| --- | --- | --- | --- | --- | --- | --- |

## 6. Cross-format comparison

| Element | Authoritative value | Format A | Format B | Difference | Approved? | Defect |
| --- | --- | --- | --- | --- | --- | --- |

## 7. Exception record

| Exception ID | Deviation | Risk | Control | Owner/authority | Expiration | Restricted use |
| --- | --- | --- | --- | --- | --- | --- |

## 8. QA disposition

- **Candidate/package:**  
- **QA scope completed:**  
- **QA scope not verified:**  
- **Open defects and conditions:**  
- **Disposition:** `QA PASS`, `QA PASS WITH CONDITIONS`, `QA FAIL`, or `NOT VERIFIED`
- **Basis and limitations:**  
- **Recommended action:**  

## 9. Authorization and release

- **Authorization:** `AUTHORIZED`, `AUTHORIZED WITH CONDITIONS`, `NOT AUTHORIZED`, or `AUTHORIZATION NOT VERIFIED`
- **Authority and evidence:**  
- **Permitted audience/use:**  
- **Conditions and deadline:**  
- **Release execution evidence:**  
- **Rollback/containment:**  
- **Support and review triggers:**  

Never populate authority, approval, or execution evidence without support.

## 10. Advisory training-outline review and development handoff

For the outline mode, use the [review report](../templates/outline-review/comprehensive-review-report.md), [finding lifecycle record](../templates/outline-review/finding-record.md), [objective/change traceability](../templates/outline-review/detailed-traceability-matrix.md), [gap log](../templates/outline-review/evidence-gap-log.md), [proposed outline](../templates/outline-review/revised-outline-template.md) only when authorized, [development handoff](../templates/outline-review/development-handoff.md), and [twelve review-quality checks](../templates/outline-review/review-quality-check.md). Preserve F IDs alongside QA defect aliases; keep outline judgment, scoped QA result, authorization and actual execution distinct.
