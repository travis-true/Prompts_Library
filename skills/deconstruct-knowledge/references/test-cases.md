# Validation test cases

Use these scenarios to test whether the skill preserves evidence and produces structured, usable knowledge.

## Case 1: One approved procedure

**Input:** A current approved procedure with clear roles, steps, exceptions, and owner.

**Expected behavior:** Produce traceable workflow steps and atoms, preserve terminology and qualifiers, identify any missing operational details, and mark readiness appropriately.

## Case 2: Policy and job aid conflict

**Input:** A current policy requires approval, while an older job aid omits it.

**Expected behavior:** Preserve the conflict, rank sources using authority and scope, prevent the old job aid from becoming governing content, and identify the resolution or retirement action.

## Case 3: SME interview only

**Input:** Detailed SME notes describe a working process, but no approved source exists.

**Expected behavior:** Attribute the statements to the SME, extract a provisional model, label it unverified, identify validation questions, and prevent controlled release.

## Case 4: Narrative document

**Input:** A long narrative explains a process without numbered steps.

**Expected behavior:** Infer a provisional sequence only where supported, label interpretation, preserve narrative qualifiers, and avoid inventing completion criteria or decision rules.

## Case 5: Mixed approved and historical sources

**Input:** Current documentation, superseded files, examples, tickets, and metrics.

**Expected behavior:** Register every relevant source, separate governing content from evidence and history, use operational evidence without treating it as policy, and retain provenance.

## Case 6: High-risk content with missing exception

**Input:** A controlled procedure lacks instructions for a known high-consequence exception.

**Expected behavior:** Create a critical gap and downstream restriction, identify the accountable decision owner, and block affected production or automation.

## Case 7: AI assistant preparation

**Input:** Approved workflow material will ground an internal assistant.

**Expected behavior:** Create scoped atoms, retrieval terms, permitted and prohibited uses, uncertainty and escalation rules, version controls, and an AI-ready handoff.

## Case 8: Automation request

**Input:** A user wants to automate a workflow described only at a high level.

**Expected behavior:** Identify missing deterministic rules, inputs, permissions, exceptions, evidence, and human controls; mark the package not ready for automation.

## Case 9: Immediate deconstruction with incomplete context

**Input:** The user prohibits questions and supplies one partial source.

**Expected behavior:** Produce a provisional rapid intake, label gaps and assumptions, state low or medium confidence, and avoid unsupported readiness claims.

## Case 10: Approved package must remain unchanged

**Input:** The user requests packaging only and prohibits reconciliation or correction.

**Expected behavior:** Preserve approved content exactly, log conflicts and gaps for decision, and avoid silent correction or expansion.

## Blocking failures

The skill fails validation if it:

- invents facts, steps, roles, rules, exceptions, approvals, or evidence;
- treats SME testimony, examples, tickets, or historical material as governing without support;
- silently resolves conflicting sources;
- loses source IDs or precise locators;
- strips conditions, qualifiers, exceptions, or scope;
- creates downstream assets before knowledge readiness is established;
- marks content approved, complete, validated, or ready without evidence;
- ignores classification, privacy, access, or permitted-use restrictions;
- converts narrative description into a mandatory workflow without labeling interpretation;
- treats readiness for drafting as readiness for controlled publication or automation.
