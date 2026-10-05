# Software Testing Tools & Vibe Coding Bug Fix Report

**Project Title**: Alumni Mentorship & Mock Interview Platform  
**Student Name**: Shashank K (PES1UG24CS434)  

---

## 1. Overview of Software Testing Process

This module documents the testing workflow, execution of automated unit/integration test cases, and the application of **Vibe Coding** (AI-assisted rapid bug diagnosis and code patching) to fix identified software defects.

---

## 2. Test Suite Execution & Initial Results

The platform's core booking and data management modules were evaluated against 4 primary test cases:

| Test Case ID | Feature Under Test | Expected Behavior | Initial Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Mentor Domain Matching | Filters catalog by domain tag (e.g. Cloud) | Pass | **PASS** |
| **TC-02** | Concurrent Booking Lock | Blocks simultaneous double-booking of same slot | Fail (Race condition detected) | **FAIL** |
| **TC-03** | Scorecard Evaluation Submission | Rejects empty required rubric fields | Pass | **PASS** |
| **TC-04** | 24-Hour Soft Deletion | Purges/anonymizes user PII within 24 hours | Fail (Resume file retained) | **FAIL** |

---

## 3. Vibe Coding Bug Fixing & Patch Application

### Bug 1: Concurrent Slot Reservation Lock Collision (`TC-02`)
* **Root Cause Analysis**: The initial booking controller lacked distributed transaction isolation, allowing two asynchronous HTTP requests to write to the database simultaneously before checking slot availability.
* **Vibe Coding Prompt**: *"Fix the race condition in slot reservation controller by wrapping database writes in a Redis distributed lock (`SET NX PX`). Re-test under 10 concurrent requests."*
* **Applied Patch**: Integrated `reserveSlotLock` middleware to guarantee atomicity.

### Bug 2: Soft-Deletion File Orphan Error (`TC-04`)
* **Root Cause Analysis**: Soft-deletion flagged the user database record as `deleted`, but failed to send an asynchronous message to the object storage service to delete attached resume files.
* **Applied Patch**: Added an event listener on `USER_SOFT_DELETE` topic to trigger S3 object unlinking.

---

## 4. Re-Testing & Verification Log

Following the Vibe Coding patch deployment, the automated test suite was executed again:

```bash
$ npm test

  Alumni Mentorship Platform Test Suite
    ✓ TC-01: Domain Matching & Recommendation (12ms)
    ✓ TC-02: Concurrent Booking Slot Lock Collision Protection (45ms)
    ✓ TC-03: Scorecard Rubric Validation (8ms)
    ✓ TC-04: 24-Hour Soft-Deletion & File Orphan Cleanup (82ms)

  4 passing (147ms)
  0 failing
```

---

## 5. Repository Link

* **Fix & Patch Commit Repo**: [mentorAlumniPlatform_PES1UG24CS434-LAB3-ShashankK](https://github.com/youngcaptainkeos/mentorAlumniPlatform_PES1UG24CS434-LAB3-ShashankK.git)
---
