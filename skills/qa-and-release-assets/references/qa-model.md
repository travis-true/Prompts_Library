# Common QA model

## Quality dimensions

| Dimension | Core question |
| --- | --- |
| Accuracy | Does the deliverable match authoritative sources and approved decisions? |
| Completeness | Are required content, files, states, alternatives, and metadata present? |
| Scope | Does it include only the approved audience, use, and content boundaries? |
| Structure | Can users find, follow, and understand the intended flow? |
| Usability | Can the intended audience complete the intended task in context? |
| Visual quality | Is hierarchy, fit, legibility, balance, and fidelity acceptable? |
| Accessibility | Is equivalent access supported and verified? |
| Technical integrity | Does the final format open, render, calculate, play, navigate, and export correctly? |
| Interoperability | Does it work in required platforms, versions, devices, and downstream systems? |
| Privacy/security | Is data, access, classification, retention, and permitted use controlled? |
| Brand/template | Does it preserve approved design and required repeated elements? |
| Source integrity | Are claims, assets, data, and citations traceable and permitted? |
| Cross-format consistency | Do related outputs preserve meaning and status? |
| Governance | Are owner, version, status, approval, review, support, and maintenance clear? |
| Package integrity | Are required files complete, clean, related, and reproducible? |

## Evidence classes

- `DIRECT`: Observed in the final candidate through rendering, parsing, playback, recalculation, or execution.
- `COMPARATIVE`: Verified against source, template, prior baseline, or related output.
- `AUTOMATED`: Produced by a checker, validator, linter, or test.
- `MANUAL`: Human or model inspection requiring judgment.
- `DECLARED`: Stated by a source or owner but not independently verified.
- `NOT AVAILABLE`: Required evidence could not be obtained.

Use more than one evidence class when the risk or construct requires it.

## Test record

Each test should contain:

- test ID;
- candidate ID;
- requirement;
- dimension;
- method and environment;
- expected result;
- observed result;
- evidence locator;
- result;
- limitation;
- defect ID when failed;
- reviewer and date.

Results:

- `PASS`
- `FAIL`
- `NOT APPLICABLE`
- `NOT VERIFIED`
- `BLOCKED`

## Risk-based depth

Increase depth when:

- consequences of error are high;
- the audience is large or external;
- content is regulated, controlled, contractual, safety-sensitive, or security-sensitive;
- the package contains automation, calculations, data, forms, or interactions;
- conversion or export can alter meaning;
- multiple formats must remain semantically equivalent;
- accessibility barriers would exclude intended users;
- changes affect approved baselines.
