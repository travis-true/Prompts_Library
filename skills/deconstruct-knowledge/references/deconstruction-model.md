# Content deconstruction model

## Contents

- Core element types
- Workflow normalization
- Content atom rules
- Audience and moment-of-need model
- Risk and readiness
- Suitability for downstream uses

## Core element types

| Element | Capture |
| --- | --- |
| Purpose | Why the knowledge or process exists |
| Outcome | Observable end state or result |
| Scope | Included and excluded people, situations, systems, and work |
| Audience | Roles, proficiency, needs, constraints, and permissions |
| Trigger | Event or condition that starts use |
| Input | Information, material, access, approval, or prerequisite |
| Action | Observable behavior performed by an actor |
| Decision | Choice with supported criteria and routes |
| Rule | Mandatory condition, threshold, prohibition, or requirement |
| Definition | Controlled meaning of a term |
| Handoff | Transfer of work, information, authority, or evidence |
| Exception | Condition where the normal route does not apply |
| Escalation | Trigger, recipient, information, timing, and expected response |
| Completion | Evidence that the work is finished |
| Verification | Check that confirms quality, compliance, or performance |
| Failure mode | Known error, symptom, cause, consequence, and containment |
| Example | Illustrative application with stated limits |
| Dependency | Required system, role, policy, data, vendor, or upstream process |
| Measure | Evidence used to answer a defined performance or governance question |
| Maintenance trigger | Event requiring review, update, containment, or retirement |

## Workflow normalization

Represent each step with:

- step ID;
- actor;
- action;
- object or system;
- precondition;
- output or evidence;
- next step;
- exception or escalation;
- source and locator;
- validation status.

Do not:

- combine multiple actors into one ambiguous step;
- hide decisions inside action text;
- assume system states or permissions;
- omit failure or escalation routes found in the source;
- convert optional guidance into a mandatory rule;
- remove qualifiers such as “may,” “typically,” “unless,” or “only when.”

## Content atom rules

A strong atom:

- expresses one reusable idea;
- makes sense without the surrounding paragraph;
- retains conditions and exceptions;
- uses approved terminology;
- identifies its audience and context;
- has one or more source locators;
- can be updated without rewriting unrelated content.

Split content when a sentence contains independent rules, audiences, conditions, or decisions. Keep related condition and exception language with the claim it modifies.

## Audience and moment-of-need model

Classify the knowledge demand as one or more:

- learn for the first time;
- learn because something changed;
- apply during work;
- solve a problem or recover from error;
- decide among alternatives;
- verify completion or quality;
- teach, coach, approve, support, or maintain;
- recall later through search or retrieval.

Capture likely search terms, system labels, synonyms, acronyms, and user language without replacing controlled terminology.

## Risk and readiness

Assess:

- consequence of incorrect guidance;
- likelihood of misunderstanding or misuse;
- source-authority strength;
- change frequency;
- complexity and variability;
- detectability and reversibility of errors;
- population affected;
- regulatory, safety, financial, privacy, security, or reputational exposure.

Use qualitative levels unless the organization provides an approved scoring model:

- `LOW`
- `MODERATE`
- `HIGH`
- `CRITICAL`

Higher risk requires stronger source authority, validation, approval, versioning, and maintenance controls.

## Suitability for downstream uses

| Use | Minimum readiness |
| --- | --- |
| Brainstorming or discovery | Gaps and assumptions clearly labeled |
| Draft training or job aid | Applicable sources identified; material conflicts isolated |
| Controlled SOP or policy guidance | Governing content resolved and approved |
| Retrieval or knowledge base | Atoms traceable, searchable, scoped, and maintained |
| AI assistant response | Authority, scope, restrictions, uncertainty, and escalation encoded |
| Workflow automation | Deterministic rules, inputs, permissions, exceptions, evidence, and human controls validated |

Readiness for one use does not imply readiness for every use.
