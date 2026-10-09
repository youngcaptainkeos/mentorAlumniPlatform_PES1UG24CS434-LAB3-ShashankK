# Jira & GitHub Project Creation & Setup Report

**Project Title**: Alumni Mentorship & Mock Interview Platform  
**Student Name**: Shashank K  
**SRN**: PES1UG24CS434  
**Problem Statement**: #06  

---

## 1. Overview of Project Management Tools Setup

As per the Software Engineering Lab guidelines, the project management tracking was configured using **Atlassian Jira Software** and **GitHub Repositories** to support Agile workflows (Kanban & Scrum) alongside Bug Tracking.

---

## 2. Jira Kanban Project Setup (`KBPS#06`)

* **Project Name**: `Kanban_BPS#06`
* **Project Key**: `KBPS06`
* **Board Configuration**:
  * Columns: `Backlog` -> `In Progress` -> `In Review` -> `Done`
  * Added Epics corresponding to core system modules (Mentorship Engine, Availability Engine, Rubric Engine).
  * Created 7 User Stories mapping directly to FR-001 through FR-005, NFR-001, and NFR-002.
  * Configured sub-tasks for API integration, unit testing, and UI wireframing.

---

## 3. Jira Scrum Project Setup (`SBPS#06`)

* **Project Name**: `Scrum_BPS#06`
* **Project Key**: `SBPS06`
* **Sprint Structure**:
  * **Sprint 1 (Requirements & Architecture)**: Finalizing FR/NFR table, Use-Case diagrams, and Component diagrams.
  * **Sprint 2 (Core Booking Engine)**: Implementing domain matching, slot locks, and calendar integrations.
  * **Sprint 3 (Testing & Bug Patching)**: Executing test suites, fixing concurrent reservation edge cases.

---

## 4. Jira Bug Tracking Setup (`BUG_REPORT_06`)

* **Project Key**: `BUG06`
* **Reported Defects**:
  * `BUG-01`: Concurrent slot double-booking race condition during high transaction spikes.
  * `BUG-02`: Soft-deletion 24-hour retention background job failing to purge attached PDF resumes.
  * `BUG-03`: Scorecard rating component throwing null pointer exception on empty qualitative feedback input.

---

## 5. GitHub Repository Workflow

* **Repo Name**: `mentorAlumniPlatform_PES1UG24CS434-LAB3-ShashankK`
* **Branch Strategy**:
  * `main`: Production-ready release code.
  * `development`: Active sprint integration branch.
  * `feature/*`: Specific feature implementation branches.
  * `fix/*`: Vibe coding bug patch branches.

---
*Attached Verification Documents in `3-Project_Creation_Screenshots/`:*
* [SHASHANK_KESHAVA_MURTHY_PES1UG24CS434_KANBAN_06.pdf](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/3-Project_Creation_Screenshots/SHASHANK_KESHAVA_MURTHY_PES1UG24CS434_KANBAN_06.pdf)
* [SHASHANK_KESHAVA_MURTHY_PES1UG24CS434_SCRUM_06.pdf](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/3-Project_Creation_Screenshots/SHASHANK_KESHAVA_MURTHY_PES1UG24CS434_SCRUM_06.pdf)
* [SHASHANK_KESHAVA_MURTHY_PES1UG24CS434_BUG_REPORT_06.pdf](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/3-Project_Creation_Screenshots/SHASHANK_KESHAVA_MURTHY_PES1UG24CS434_BUG_REPORT_06.pdf)
