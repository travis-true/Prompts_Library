# Source authority and provenance

## Authority test

Evaluate each source against all relevant dimensions:

| Dimension | Questions |
| --- | --- |
| Mandate | Is the source authorized to govern this subject? |
| Ownership | Is an accountable owner identified and authenticated? |
| Approval | Was it reviewed and approved through the required process? |
| Currency | Is the version effective and within its review period? |
| Scope | Does it apply to the audience, location, product, system, and situation? |
| Specificity | Does it directly address the disputed element? |
| Evidence | Is the claim supported by operational, legal, technical, or validation evidence? |
| Integrity | Is the content complete, unaltered, and traceable? |
| Classification | May the content be used for the requested purpose and audience? |

No single dimension automatically establishes authority.

## Recommended authority classes

1. **Governing:** Approved policy, regulation, contract, controlled procedure, or authenticated system of record within scope.
2. **Approved supporting:** Approved guidance that explains or implements governing content.
3. **Operational evidence:** Logs, tickets, metrics, observations, tests, or system outputs that show what occurred.
4. **SME testimony:** Attributed expertise requiring validation against governing content and actual system behavior.
5. **Historical:** Previously valid content retained for context but not current instruction.
6. **Example:** Illustrative content that must not be treated as a universal rule.
7. **Unverified:** Origin, currency, approval, or applicability is not established.
8. **Conflicting:** Materially disagrees with another applicable source.
9. **Excluded:** Out of scope, prohibited, duplicative without added value, corrupt, or unusable.

## Conflict handling

When sources conflict:

1. Preserve both claims and their locators.
2. Identify the exact disputed element.
3. Compare mandate, approval, scope, currency, specificity, and evidence.
4. Do not use majority agreement as proof.
5. Identify the accountable decision owner.
6. Record the decision, rationale, date, conditions, and affected atoms.
7. Retain the superseded or rejected claim as history when governance requires it.

If authority cannot be resolved, label the content `CONFLICT` and block affected high-risk downstream use.

## Provenance minimum

For every reusable fact, rule, step, or decision, retain:

- source ID;
- source version or date;
- page, section, timestamp, record, range, or other locator;
- author or owner when known;
- authority class;
- extraction date;
- transformation notes;
- validation status;
- permitted-use restrictions.

## Evidence labels

- `FACT`: Directly supported by an applicable source.
- `ASSUMPTION`: Accepted temporarily without sufficient evidence.
- `INFERENCE`: Reasoned conclusion derived from stated evidence.
- `EXAMPLE`: Illustration, not a governing rule.
- `CONFLICT`: Applicable sources disagree.
- `GAP`: Required information is absent.
- `NOT VERIFIED`: Evidence exists but has not been validated.
- `DECISION REQUIRED`: An accountable human must resolve the issue.

Do not convert an assumption or inference into a fact merely because it is plausible.
