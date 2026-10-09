# Software Requirements Specification (SRS) & Work Breakdown Structure (WBS)

**System**: Alumni Mentorship & Mock Interview Platform (Problem Statement #06)  
**Author**: Shashank K (PES1UG24CS434)  

---

## 1. Software Requirements Specification (SRS) Overview

### 1.1 Purpose
This document specifies the software requirements for the **Alumni Mentorship & Mock Interview Platform**. The platform provides automated domain matching between student mentees and verified alumni mentors, real-time availability calendar scheduling, interview goal/resume pre-review, standardized feedback scoring, and mentorship growth analytics.

### 1.2 Scope
- **Student Mentee Module**: Browse alumni catalog, filter by domain expertise (Embedded Systems, Cloud Computing, AI/ML), attach resume PDFs (≤ 5MB), reserve mock interview slots, view post-session feedback scorecards.
- **Alumni Mentor Module**: Set domain focus areas, publish availability slots, access attached student resumes, submit structured rubric evaluations.
- **System Services**: Automated double-booking lock protection (< 200ms latency), calendar invitation sync, video conference link generation, 24-hour soft-deletion data privacy compliance.

### 1.3 System Constraints & Interfaces
- **External Interfaces**: University OAuth2 Single Sign-On (SSO), Google Calendar API, Microsoft Teams / Zoom Video API, AWS S3 file storage.
- **Performance Constraints**: Uptime 99.9%, slot lock transaction latency < 200ms, calendar sync < 5s.

---

## 2. Work Breakdown Structure (WBS)

```
1.0 Alumni Mentorship & Mock Interview Platform
│
├── 1.1 Requirements Engineering (RE) Phase
│   ├── 1.1.1 Elicit Functional & Non-Functional Requirements (FR-001 to FR-005, NFR-001, NFR-002)
│   ├── 1.1.2 Build Requirements Traceability Matrix (RTM)
│   └── 1.1.3 Draft Use Case Specifications & Flow Diagrams (UC-01 to UC-06)
│
├── 1.2 System Architecture & Design Phase
│   ├── 1.2.1 Evaluate Architectural Styles (Layered vs Microservices vs Client-Server)
│   ├── 1.2.2 Design UML Component Diagram (5 Components: UI, Session Manager, Profile Svc, Rating Svc, Sync Svc)
│   └── 1.2.3 Document Architectural Justification & Interface Contracts
│
├── 1.3 Agile Project Tracking Phase
│   ├── 1.3.1 Configure Jira Kanban Board (`KBPS#06`)
│   ├── 1.3.2 Configure Jira Scrum Board (`SBPS#06`) & Backlog Sprints
│   └── 1.3.3 Set up Jira Bug Tracker (`BUG_REPORT_06`) & GitHub Repository
│
├── 1.4 Core Service Development Phase
│   ├── 1.4.1 Implement Domain Matching & Slot Reservation Locking Service
│   ├── 1.4.2 Implement Mentor Availability & Scorecard Evaluation Modules
│   └── 1.4.3 Integrate Calendar Sync & Video Meeting Link Generators
│
└── 1.5 Quality Assurance & Software Testing Phase
    ├── 1.5.1 Execute Automated Unit & Integration Test Cases
    ├── 1.5.2 Conduct Vibe Coding Bug Fixing & Edge Case Patching
    └── 1.5.3 Finalize Deployment & Verification Documentation
```

---
