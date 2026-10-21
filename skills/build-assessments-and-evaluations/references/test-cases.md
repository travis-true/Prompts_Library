# Validation test cases

## Case 1: Practical software assessment

**Request:** Verify that new employees can independently complete an approved software workflow.

**Expected behavior:** Use a realistic performance task with permitted tools, observable evidence, source-grounded criteria, critical errors, rubric, accessibility, and remediation; do not rely on a quiz alone.

## Case 2: Formative knowledge checks

**Request:** Add unscored checks to a live session.

**Expected behavior:** Align each check to an outcome and instructional decision, provide feedback, keep stakes low, and avoid unnecessary learner-data collection.

## Case 3: Arbitrary pass score

**Request:** Create a mandatory assessment with an 80% pass score because that is the company standard, but no policy or competency basis is supplied.

**Expected behavior:** Mark the threshold unverified, request or identify the authority, protect critical criteria, and avoid claiming the score demonstrates competence.

## Case 4: Reaction survey

**Request:** Prove the training was effective using a satisfaction survey.

**Expected behavior:** Reject the unsupported interpretation, use the survey for experience or improvement questions, and recommend direct learning or performance evidence for effectiveness decisions.

## Case 5: High-risk certification

**Request:** Certify complex judgment using five multiple-choice questions.

**Expected behavior:** Challenge insufficient sampling and method, require scenario or performance evidence, human review, defensible standards, security, remediation, appeal, and validation.

## Case 6: Pre/post comparison

**Request:** Compare pre- and post-scores from different forms.

**Expected behavior:** Verify construct, coverage, demand, conditions, scoring, pairing, and missing data; avoid causal claims unsupported by design.

## Case 7: Observation

**Request:** Build a manager checklist for workplace transfer.

**Expected behavior:** Define observable behavior, opportunity to perform, not-observed handling, manager calibration, privacy, evidence, and action.

## Case 8: Operational result

**Request:** Determine whether training reduced errors.

**Expected behavior:** Define the error metric, baseline, population, period, comparison, concurrent changes, opportunity, limitations, and decision; do not attribute change automatically.

## Case 9: Accessibility

**Request:** Create an online timed assessment for a mixed audience.

**Expected behavior:** Examine whether speed is part of the construct, provide equivalent access and accommodations, verify keyboard/screen-reader behavior, and document any construct change.

## Case 10: No platform creation

**Request:** Build an LMS quiz when the host can produce only text.

**Expected behavior:** Produce an implementation-ready item bank, key, blueprint, feedback, import specification, and QA plan without claiming an LMS package exists.

## Blocking failures

The skill fails validation if it:

- starts with item writing before defining the decision and outcome;
- invents correct answers, standards, cut scores, validation, reliability, results, or approvals;
- uses knowledge items to claim performance without justification;
- treats reaction, confidence, attendance, or completion as competence;
- uses trick wording, trivia, or irrelevant complexity;
- ignores critical errors or lets total score compensate for non-compensable failures;
- omits accessibility, fairness, privacy, security, retention, or appeal where material;
- claims causation from simple pre/post change or operational trends;
- analyzes data without verifying definitions, denominators, missingness, and permitted use;
- releases a high-stakes instrument without appropriate authority and evidence.


## Engagement extension

Unknown-stakes case: a certificate program with unclear result use must trigger a decision/consequence question; if no questions are allowed, leave stakes unresolved. Fallback case: screenshot recognition cannot certify software operation. No standard means no global pass. Run the extension regression suite at repository path `tests/test_engagement_assessment.py` after changes.
