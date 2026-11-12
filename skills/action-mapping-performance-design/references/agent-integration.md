# Agent integration and handoff boundaries

## General pattern

This is a **skill used by existing specialists**, not an orchestration agent. The project coordinator controls phases, scope, artifact registers, approvals, and handoffs. A skill invocation supplies analysis or a proposed draft, not permission to advance the project.

| Specialist/workstream | Intended use | Typical output | Never assume |
|---|---|---|---|
| Training Needs Discovery | Discover | Performance Discovery Gate, evidence ledger, barriers | Request for a class proves training need |
| Learning Solution Planning | Discover or Design | Intervention comparison, provisional action map | Non-training fix was approved |
| Detailed Learning Design | Design | Action-to-practice trace, prototype brief, performance evidence | Technical tests or learning architecture approvals are complete |
| Training Content Production | Review a brief or design | Production-alignment findings | Permission to rewrite approved content |
| PowerPoint/Word Builder | Review the approved content map | Alignment notes only | Authority to alter slides, workbook wording, activities, or IDs |
| Training Project Coordinator | Record-only handoff packet | Proposed revision and dependencies | Changes were automatically persisted |

## Portable project record expectations

- Existing IDs and exact revisions remain authoritative. Do not fabricate predecessors or approval references.
- Put proposed outputs in a separate register entry, such as `AM-001 v0.1 — PROPOSED`, and identify its exact source basis.
- If prior decisions conflict with a new recommendation, show a side-by-side change proposal and request explicit approval.
- Preserve unverified technical constraints, observation logistics, evidence provenance, and production holds.
- Never read unrelated projects by default, contact stakeholders, or call other plugins on behalf of a skill unless expressly authorized.
- Return the completed handoff in the conversation; state it is not externally saved.

## Example: controlled pilot

A user may authorize **review of an approved OneNote design** but not execution of technical validation. The skill can note that retrieval tasks may need a more authentic challenge, suggest a low-fidelity test, and propose a measurement hypothesis. It **cannot** infer learner success from a single timed retrieval anecdote, change all approved action goals, or claim the prototype is validated.
