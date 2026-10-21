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
