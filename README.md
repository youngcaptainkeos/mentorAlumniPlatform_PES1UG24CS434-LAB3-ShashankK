# MyProject_MentorAlumniPlatform

### Software Engineering Lab Individual Project Submission — Lab 3 & Full Project Overview
**Department of Computer Science and Engineering, PES University**

---

## 📌 Student & Project Details

* **Project Title**: Alumni Mentorship & Mock Interview Platform
* **Repository Name**: `mentorAlumniPlatform_PES1UG24CS434-LAB3-ShashankK`
* **Nomenclature**: `MyProject_MentorAlumniPlatform`
* **Student Name**: Shashank K
* **SRN**: PES1UG24CS434
* **Course**: Software Engineering (UE22CS351A / SE Lab)
* **Problem Statement**: #06 — Campus & Academic Operations

---

## 📖 Executive Summary & Problem Context

Connecting students with alumni working in specialized domains requires an intelligent matching mechanism, dynamic availability calendar booking, pre-interview goal/resume attachment, and structured post-interview scorecard recording.

### Key Stakeholders / Actors
1. **Student Mentee**: Searches verified alumni by domain, uploads resumes, schedules mock interview sessions, and receives structured evaluation feedback.
2. **Alumni Mentor**: Configures interview domain expertise, publishes availability calendar slots, reviews attached student portfolios, and submits standardized feedback scorecards.
3. **Calendar & Meeting Service**: External integration for dispatching calendar invitations and generating secure video conferencing URLs.

---

## 📁 Repository Folder Structure & Deliverables Index

As per the Software Engineering Lab submission guidelines specified in `Git Hub Project Submission Details.docx`, this repository is structured into 6 primary deliverable folders:

```
mentorAlumniPlatform_PES1UG24CS434-LAB3-ShashankK/
├── 1-RE/                                  # Requirements Engineering
│   ├── FR_NFR_Specification.md            # 5 FRs, 2 NFRs, RTM Table & Core Use Case Flow
│   ├── Deliverable_1_Requirements_Table.pdf
│   ├── Deliverable_2_Use_Case_Diagram.pdf
│   ├── Deliverable_3_Use_Case_Flow_Specification.pdf
│   └── 6_SE_Lab1_SE_Problem_Statements.pdf
│
├── 2-Architectural_Diagram/               # Architectural Patterns & UML Component Design
│   ├── Architecture_Justification_and_Component_Diagram.md  # Style Selection & Interface Specs
│   ├── Lab_3_Component_Diagram.drawio     # UML Component Diagram
│   └── Lab_3_Architecture_Student_handout.pdf
│
├── 3-Project_Creation_Screenshots/        # Agile Tooling (Jira & GitHub Setup)
│   ├── Jira_and_GitHub_Project_Setup.md   # Kanban, Scrum, Bug Tracking & Git Branching
│   ├── SHASHANK_KESHAVA_MURTHY_PES1UG24CS434_KANBAN_06.pdf
│   ├── SHASHANK_KESHAVA_MURTHY_PES1UG24CS434_SCRUM_06.pdf
│   └── SHASHANK_KESHAVA_MURTHY_PES1UG24CS434_BUG_REPORT_06.pdf
│
├── 4-SRS_and_Work_Breakdown/              # SRS & Work Breakdown Structure
│   └── SRS_and_WBS_Specification.md       # IEEE-style SRS & 5-Phase WBS
│
├── 5-Github_Copilot_Code/                 # AI Code Generation & Prompts
│   └── Copilot_Generated_Code_Summary.md  # Distributed Lock & Matching Algorithm Snippets
│
├── 6-Software_Testing_Tools/              # Software Testing & Vibe Coding Patching
│   └── Testing_Tools_and_Vibe_Coding_Report.md  # Test Suite Execution & Patch Logs
│
└── README.md                              # Main Repository Index & Project Documentation
```

---

## 🎯 Summary of Deliverable Folders

### [1-RE/ — Requirements Engineering](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/1-RE/FR_NFR_Specification.md)
* **Functional Requirements (FR-001 to FR-005)**: Mentorship domain recommendations, profile & availability management, structured rubric scorecards, resume attachment handling, and growth analytics.
* **Non-Functional Requirements (NFR-001 & NFR-002)**: 24-hour soft-deletion privacy compliance and sub-200ms slot reservation lock latency with 99.9% uptime.
* **Requirements Traceability Matrix (RTM)**: Direct mapping between FR/NFR IDs, Use Cases, System Components, Jira User Stories, and Automated Test Cases.
* **Use-Case Specification**: Detailed step-by-step flow for `UC-01: Book Mock Interview Session` with include/extend relationships and alternate flows.

### [2-Architectural_Diagram/ — Architecture & Component Diagram](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/2-Architectural_Diagram/Architecture_Justification_and_Component_Diagram.md)
* **Architectural Style**: **Layered Modular Microservices Architecture**.
* **Justification**: Selected to enable independent horizontal scaling of high-concurrency booking lock managers and provide fault isolation across third-party video/calendar API integrations.
* **Security & Performance**: Enforces isolated data privacy boundaries (PII soft-deletion) and sub-200ms lock latency.
* **5 Key Components**: Client Web UI, Order/Session Manager, Alumni Profile & Availability Service, Rating & Scorecard Service, Notification & Calendar Sync Service.

### [3-Project_Creation_Screenshots/ — Agile Tracking (Jira & GitHub)](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/3-Project_Creation_Screenshots/Jira_and_GitHub_Project_Setup.md)
* **Kanban Project (`KBPS#06`)**: Configured backlog, in-progress, in-review, done states for rapid continuous flow.
* **Scrum Project (`SBPS#06`)**: Planned 3 Sprints covering RE/Architecture, Booking Engine, and QA/Testing.
* **Bug Tracking (`BUG_REPORT_06`)**: Tracked race condition locks, orphan resume files, and null scorecard parameters.

### [4-SRS_and_Work_Breakdown/ — SRS & WBS](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/4-SRS_and_Work_Breakdown/SRS_and_WBS_Specification.md)
* **IEEE SRS Overview**: Standardized specification of system constraints, user roles, security rules, and performance metrics.
* **WBS Hierarchy**: Structured breakdown spanning Requirements, System Architecture, Agile Tooling, Core Service Development, and Quality Assurance.

### [5-Github_Copilot_Code/ — Copilot Code Generation](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/5-Github_Copilot_Code/Copilot_Generated_Code_Summary.md)
* **AI Assistance**: Prompts and code snippets generated using GitHub Copilot for Redis distributed locking (`slotLockManager.js`) and domain ranking algorithms (`mentorMatcher.js`).

### [6-Software_Testing_Tools/ — Testing & Vibe Coding](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/6-Software_Testing_Tools/Testing_Tools_and_Vibe_Coding_Report.md)
* **Test Suite**: Automated execution of 4 primary test cases (Domain matching, Concurrent booking locks, Rubric validation, 24h soft-deletion).
* **Vibe Coding Bug Fixing**: Applied rapid AI patches to resolve concurrent reservation race conditions (`TC-02`) and unlinked S3 file deletion (`TC-04`), achieving 100% test suite pass rate upon re-testing.

---

## 🛠️ Software Stack & Technologies

* **Modelling & Diagramming**: Draw.io, StarUML
* **Project Management**: Atlassian Jira (Kanban, Scrum, Bug Tracking)
* **Version Control**: Git & GitHub
* **AI & Vibe Coding Tools**: GitHub Copilot, Anthropic/DeepMind AI Coding Assistants
* **Backend Runtime & Lock Engine**: Node.js / Express, Redis Distributed Locks

---

## 📜 Verification & Compliance Statement

This repository fulfills all requirements set forth in **Lab 3: Component Modelling & Architectural Pattern Selection** as well as the complete **Individual Project Submission Guidelines** (`Git Hub Project Submission Details.docx`) for Problem Statement #06 at PES University.
