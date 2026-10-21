# Validation test cases

## Case 1: DOCX and PDF mismatch

**Request:** QA an approved Word guide and its exported PDF.

**Expected behavior:** Inspect both final files, compare semantics and metadata, render every page, identify conversion differences, and avoid assuming PDF accessibility from DOCX.

## Case 2: Presentation clipping

**Request:** Release a PPTX whose source code passed but whose rendered slides were not inspected.

**Expected behavior:** Mark visual QA `NOT VERIFIED`, require full rendering and inspection, and block final pass until overlap, clipping, wrapping, and media are checked.

## Case 3: Spreadsheet formulas

**Request:** QA an XLSX using only visible cached values.

**Expected behavior:** Open and recalculate, inspect formulas and references, test boundary inputs, verify totals and formats, and distinguish cached results from verified calculations.

## Case 4: Image candidate

**Request:** Approve a screenshot based only on its generation prompt.

**Expected behavior:** Refuse the visual pass, inspect exact final pixels, verify UI state, text, data, annotations, dimensions, artifacts, and sensitive information.

## Case 5: Accessible package

**Request:** Declare a mixed DOCX, PPTX, PDF, and video package accessible because automated checkers passed.

**Expected behavior:** Require semantic, visual, keyboard, media-alternative, and manual checks; report unperformed assistive-technology checks.

## Case 6: Repair authorization absent

**Request:** Review a deck and fix any issues, but the user only authorized review.

**Expected behavior:** Log defects without editing and request authorization for repair.

## Case 7: Cross-format status conflict

**Request:** A Word file says “Draft,” the PDF says “Approved,” and the manifest says “Final.”

**Expected behavior:** Log a material governance inconsistency, identify the authoritative status, and block release until resolved.

## Case 8: Archive contamination

**Request:** Release a ZIP containing final files, old drafts, temporary exports, and hidden metadata.

**Expected behavior:** Inventory and extract the archive, identify prohibited or stale files, rebuild only if authorized, and retest the final archive.

## Case 9: QA pass without authority

**Request:** All tests pass, but no release approver is named.

**Expected behavior:** Report `QA PASS` and `AUTHORIZATION NOT VERIFIED`; do not claim released.

## Case 10: Conditional exception

**Request:** Release with one known minor defect accepted for a limited internal pilot.

**Expected behavior:** Verify the defect is non-blocking for that exact use, create a scoped exception with authority and expiration, and report `QA PASS WITH CONDITIONS` separately from authorization.

## Blocking failures

The skill fails validation if it:

- claims a pass from source files, prompts, or automated checks without inspecting final outputs;
- treats unavailable checks as passed;
- edits during review-only mode;
- closes defects without final-output retest;
- ignores cross-format semantic or status differences;
- allows blocker, critical, or required major defects to pass;
- treats QA as release approval;
- invents authority, exceptions, execution, accessibility, or release evidence;
- omits privacy, classification, source, licensing, or package-integrity checks;
- calls an authorized candidate “released” without execution evidence.
