# Validation and handoffs

Use [demo.json](../../examples/demo/demo.json) for schema 1.1. Paths resolve within the deliverable root. The standard-library validator reads local UTF-8 files, never executes demo operations, contacts services or grants approval.

```sh
python scripts/validate_demo.py --skill . --record examples/demo/demo.json --root .
```

The record contains version/document/state, source and objective IDs, operation states, complete scene fields, per-path timing, action success/retry rules, asset inventory, fallback-equivalence records, thirteen quality records, open items, learner/key separation, rehearsal records, release authorization and prepared handoffs. Use the example field structure; preserve IDs when adapting it. Record quotations locate declared evidence, not proof of source authority or actual reviewer work.

The validator checks arithmetic, identifiers, local assets/references, declared state transitions, mutation retry protections, evidence/claim limits and readiness consistency. It cannot discover every omitted step, judge semantic equivalence, authenticate approval, test a UI, observe rehearsal, establish proficiency or certify accessibility.

## Handoffs
Prepare production integration for **Live Training Session Design**, practice/evidence development for **Build Assessments and Evaluations**, and actual artifact/rehearsal/approval checks for **QA and Release Assets**. Use [the handoff template](../../templates/demo/development-qa-handoff.md). Preserve original finding IDs when supplied, source/objective/scene/action/asset IDs, versions, constraints, gaps, owners, dependencies and acceptance criteria. The receiving skill should reuse this demo as a component rather than create a competing course. Prepared; not executed means no external dispatch or invocation occurred.

## Quality and release
Structural success remains separate from all thirteen quality statuses and release authorization. Ready for delivery requires actual applicable evidence, verified required assets and rehearsals, resolved blocking work and documented authorization. Otherwise retain Draft complete; review required or Needs revision for known defects. Use Planning framework only when material inputs prevent a supported script. Unperformed tests stay Not checked. Fictional specifications can pass a written-design review but not environmental tests for an application that does not exist.
