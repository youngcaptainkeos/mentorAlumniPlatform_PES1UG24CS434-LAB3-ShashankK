# Lab 1: Requirements Engineering & Use Case Modelling

**Project Title**: Alumni Mentorship & Mock Interview Platform  
**Problem Statement**: #06 (Campus & Academic Operations)  
**Student Name**: Shashank K  
**SRN**: PES1UG24CS434  
**Course**: Software Engineering (UE22CS351A / SE Lab) — Department of Computer Science & Engineering, PES University  

---

## 📌 Lab Overview & Objectives
The primary goal of Lab 1 is to perform formal **Requirements Engineering (RE)** for Problem Statement #06, establishing 5 Functional Requirements (FR-001 to FR-005) and 2 Non-Functional Requirements (NFR-001 and NFR-002), modeling a complete UML Use-Case Diagram, and documenting a 1-page Use-Case Flow Specification for the core system workflow.

---

## 📁 Lab 1 Deliverables Index

* [**`Deliverable_1_Requirements_Table.pdf`**](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/lab1/Deliverable_1_Requirements_Table.pdf): Formal specification table defining FR-001 through FR-005 and NFR-001/NFR-002 with priorities, acceptance criteria, rationales, and comments.
* [**`Deliverable_2_Use_Case_Diagram.pdf`**](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/lab1/Deliverable_2_Use_Case_Diagram.pdf): Complete UML Use-Case diagram illustrating Student Mentee and Alumni Mentor actors, core use cases, and `«include»` / `«extend»` relationships.
* [**`Deliverable_3_Use_Case_Flow_Specification.pdf`**](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/lab1/Deliverable_3_Use_Case_Flow_Specification.pdf): Detailed specification for `UC-01: Book Mock Interview Session` covering preconditions, postconditions, main success scenario (MSS), and exception handling.
* [**`6_SE_Lab1_SE_Problem_Statements.pdf`**](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/lab1/6_SE_Lab1_SE_Problem_Statements.pdf): Official Problem Statement #06 guidelines from PES University.

---

## 📋 Requirements Summary

### Functional Requirements (FR)
1. **FR-001**: Domain-based Alumni Mentor Recommendation & 1-Click Booking [Priority: High]
2. **FR-002**: Mentor Profile Management & Dynamic Availability Slot Publishing [Priority: High]
3. **FR-003**: Structured Rubric Scorecard & Qualitative Evaluation Feedback [Priority: High]
4. **FR-004**: Student Resume/Portfolio Attachment (≤ 5MB PDF) & Focus Topic Submission [Priority: Medium]
5. **FR-005**: Mentorship Performance Analytics & Engagement Badging System [Priority: Medium]

### Non-Functional Requirements (NFR)
1. **NFR-001 (Privacy & Security)**: User profile, evaluation scorecard, and resume data privacy compliance with 24-hour soft-deletion support.
2. **NFR-002 (Reliability & Performance)**: Session scheduling service maintaining 99.9% uptime and sub-200ms transaction lock latency to prevent concurrent slot collisions.
