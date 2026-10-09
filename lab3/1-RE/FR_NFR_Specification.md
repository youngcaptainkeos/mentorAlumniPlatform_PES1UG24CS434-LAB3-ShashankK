# Requirements Engineering (RE) Specification & RTM Table

**Project Title**: Alumni Mentorship & Mock Interview Platform  
**Problem Statement**: #06 (Campus & Academic Operations)  
**Student Name**: Shashank K  
**SRN**: PES1UG24CS434  
**Course**: Software Engineering (SE Lab) — Department of Computer Science & Engineering, PES University  

---

## 1. Functional Requirements (FR)

| Req ID | Type | Description | Priority | Acceptance Criteria | Rationale / Justification | Comments |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-001** | Functional | The system shall recommend alumni mentors to students based on domain matching (e.g., Embedded Systems, Cloud Computing, AI/ML) and facilitate one-click session booking. | **High** | **Pass**: Mentorship session added to both calendars with meeting link.<br>**Fail**: Double-booking of mentor slots or unmatched domain listings. | Core discovery and booking mechanism connecting students with relevant alumni expertise seamlessly. | Base requirement from problem statement specification. |
| **FR-002** | Functional | The system shall allow Alumni Mentors to manage their profile, define interview domain specializations, and configure recurring/ad-hoc availability calendar slots. | **High** | **Pass**: Available slots publish dynamically to student catalog; sync in < 5s.<br>**Fail**: Overlapping slot creation or unverified mentor profiles enabled. | Gives mentors full autonomy over their time commitments and domain specializations. | Includes time-zone normalization and buffer management. |
| **FR-003** | Functional | The system shall provide Alumni Mentors with a structured rubric scorecard interface to submit quantitative ratings (technical, communication, problem solving) and qualitative feedback post-session. | **High** | **Pass**: Scorecard submitted and instantly visible in student dashboard; notification dispatched.<br>**Fail**: Incomplete mandatory rubric fields submitted. | Standardizes evaluation criteria, providing students with actionable, objective interview feedback. | Requires ratings on 1-5 scale across defined competencies. |
| **FR-004** | Functional | The system shall allow Student Mentees to upload and attach resumes/portfolios and specific interview focus topics during session booking for mentor pre-review. | **Medium** | **Pass**: Supported formats (PDF/DOCX ≤ 5MB) securely attached and accessible to mentor prior to call.<br>**Fail**: Corrupted files or unauthorized file access. | Enables mentors to review background details prior to the mock interview for targeted, realistic questions. | Automated anti-malware scanning upon file upload. |
| **FR-005** | Functional | The system shall track mentorship analytics, generate student performance growth reports across multiple mock interviews, and award alumni engagement badges. | **Medium** | **Pass**: Trend chart generated with historical rubric averages; badges visible on profile.<br>**Fail**: Data discrepancy in aggregated session scores. | Encourages continuous student improvement and incentivizes sustained alumni participation. | Supports PDF progress report export. |

---

## 2. Non-Functional Requirements (NFR)

| Req ID | Type | Description | Priority | Acceptance Criteria | Rationale / Justification | Comments |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **NFR-001** | Non-Functional (Privacy & Security) | All user profile data, resumes, and feedback scorecards shall adhere to privacy guidelines and support soft-deletion within 24 hours of request. | **High** | **Pass**: Data anonymization/soft deletion completed within 24 hours with audit log confirmation.<br>**Fail**: Retained PII or active profile data post 24-hour window. | Protects sensitive student evaluations, resumes, and alumni personal contact information. | Complies with institutional student data privacy regulations. |
| **NFR-002** | Non-Functional (Reliability & Performance) | The session scheduling and automated calendar sync service shall maintain 99.9% uptime and prevent concurrent double-booking with under 200ms transaction lock latency. | **High** | **Pass**: 100% of concurrent booking collisions rejected; meeting link generation latency < 2s.<br>**Fail**: Double-booking occurrence or calendar sync timeout. | Prevents scheduling conflicts and ensures reliable mentor-mentee interview appointments. | Tested with simulated concurrent booking attempts. |

---

## 3. Requirements Traceability Matrix (RTM)

| Requirement ID | Requirement Description | Use Case ID | Architecture Component | Jira Story ID | Test Case ID | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-001** | Domain Match & Mentor Recommendation | UC-01 | Order/Session Manager | KBPS-101 | TC-FR01-01 | Verified |
| **FR-002** | Mentor Profile & Availability Setup | UC-02 | Alumni Profile & Availability Service | KBPS-102 | TC-FR02-01 | Verified |
| **FR-003** | Structured Scorecard & Feedback | UC-04 | Rating & Feedback Service | KBPS-103 | TC-FR03-01 | Verified |
| **FR-004** | Resume Attachment & Goal Submission | UC-03 | Document & Storage Service | KBPS-104 | TC-FR04-01 | Verified |
| **FR-005** | Analytics & Engagement Badges | UC-05 | Analytics & Reporting Engine | KBPS-105 | TC-FR05-01 | Verified |
| **NFR-001** | Data Privacy & 24h Soft Deletion | UC-06 | Security & Data Privacy Layer | KBPS-106 | TC-NFR01-01 | Verified |
| **NFR-002** | High Availability & Lock Latency | UC-01 | Lock & Concurrency Manager | KBPS-107 | TC-NFR02-01 | Verified |

---

## 4. Core Use Case Flow Specification

### Use Case ID: UC-01 — Book Mock Interview Session
* **Primary Actor**: Student Mentee
* **Secondary Actors**: Alumni Mentor, Calendar & Video Meeting Service
* **Preconditions**:
  1. Student Mentee is authenticated via university OAuth2 SSO.
  2. Alumni Mentor has active profile and published calendar slots.
  3. Student has not exceeded active session limit (max 2 active bookings).
* **Postconditions**:
  1. Chosen slot status updated to `RESERVED` / `BOOKED`.
  2. Calendar invitation with conferencing link sent to both parties.
  3. Audit log entry recorded in database.

#### Main Success Scenario (MSS):
1. Student Mentee navigates to 'Find Alumni Mentors' page.
2. System presents searchable catalog of verified mentors filtered by domain (e.g., Cloud, Embedded Systems, AI/ML).
3. Student selects mentor profile and views open 45-minute calendar slots.
4. Student selects an available date/time slot.
5. Student inputs interview domain focus and target role goals.
6. System executes `UC-02: Validate Slot Concurrency` to acquire short-term transaction lock.
7. System executes `UC-03: Attach Resume` (optional PDF upload ≤ 5MB).
8. System commits session booking and updates slot status.
9. System invokes external Calendar & Video Conference API to generate video meeting link.
10. System displays booking confirmation banner and dispatches notification emails.

#### Alternate & Exception Flows:
* **4a. Booking Limit Reached**: System detects 2 existing active sessions, alerts student, and halts booking.
* **6a. Concurrent Booking Collision**: System detects lock collision, displays slot unavailable message, and prompts student to re-select.
* **7a. Invalid File Upload**: System rejects files > 5MB or non-PDF/DOCX formats.
* **9a. External API Timeout**: System saves booking with pending status and triggers background retry service.

---
*Attached Reference Files in `1-RE/`:*
* [Deliverable_1_Requirements_Table.pdf](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/1-RE/Deliverable_1_Requirements_Table.pdf)
* [Deliverable_2_Use_Case_Diagram.pdf](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/1-RE/Deliverable_2_Use_Case_Diagram.pdf)
* [Deliverable_3_Use_Case_Flow_Specification.pdf](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/1-RE/Deliverable_3_Use_Case_Flow_Specification.pdf)
