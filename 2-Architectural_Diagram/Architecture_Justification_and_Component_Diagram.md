# Architectural Selection, Justification & Component Diagram

**System**: Alumni Mentorship & Mock Interview Platform (Problem Statement #06)  
**Student**: Shashank K (PES1UG24CS434)  
**Lab Assignment**: SE Lab 3 — Architectural Pattern & Component Modelling  

---

## 1. Architectural Style Selection

**Selected Architectural Pattern**: **Layered Modular Microservices Architecture**

### Justification & Evaluation
For the **Alumni Mentorship & Mock Interview Platform**, we evaluated three primary architectural styles:
1. **Layered Architecture (3-Tier)**: Simple separation of UI, business logic, and database, but limits independent scaling of heavy services (e.g. concurrent slot lock manager).
2. **Monolithic Architecture**: High risk of single points of failure under peak mock-interview scheduling traffic.
3. **Layered Microservices Architecture (Selected)**: Combines clean horizontal separation (Presentation, Application Service Layer, Persistence) with modular microservices for independent scalability and fault isolation.

---

## 2. Technical Justification & Specific Reasons

### Reason 1: High Concurrency Booking & Independent Scalability
The platform experiences burst traffic during university interview seasons when hundreds of students attempt to reserve limited mentor slots simultaneously. Decoupling the **Order/Session Manager** from the **Alumni Profile Service** allows the reservation concurrency engine to scale horizontally using Redis distributed locking without overhead on static profile rendering services.

### Reason 2: Fault Isolation Across Third-Party Integrations
The system heavily relies on external services (Google/Outlook Calendar APIs, Zoom/Teams video SDKs, and S3 file storage). Isolating the **Notification & Calendar Sync Service** inside its own microservice bounded context prevents external API rate-limiting or network timeouts from crashing core student browsing and mentor scorecard recording features.

---

## 3. Security Advantage
* **Isolated Security & Privacy Layer**: The **Data Privacy & Anonymization Engine** executes soft-deletions and PII scrub routines within an isolated data pipeline (NFR-001). Resume uploads are processed through an isolated microservice container that enforces virus scanning and strict IAM role-based access control (RBAC), preventing unauthorized access to confidential student evaluations or mentor contact information.

---

## 4. Performance Benefit
* **Sub-200ms Transaction Lock Latency**: By utilizing an in-memory caching and lock manager service within the **Order/Session Manager** component, booking slot validation (NFR-002) achieves sub-200ms response times and eliminates database deadlock conditions under peak concurrent booking loads.

---

## 5. System Component Specification

The system design comprises 5 core components with provided (ball) and required (socket) interfaces:

```
+-----------------------------------------------------------------------------------+
|                                 WEB CLIENT / UI                                   |
+-----------------------------------------------------------------------------------+
                                         |
                                         v (REST / HTTPS)
+-----------------------------------------------------------------------------------+
|                           ORDER / SESSION MANAGER                                 |
|  - Validates booking quotas                                                       |
|  - Executes pessimistic/distributed locks for slot reservation                   |
+-----------------------------------------------------------------------------------+
          |                                  |                              |
          v (gRPC / Internal API)            v (Database Query)             v (Event Bus / REST)
+-----------------------------------+  +--------------------------+  +--------------------------+
| ALUMNI PROFILE & AVAILABILITY SVC |  | RATING & SCORECARD SVC   |  | NOTIFICATION & SYNC SVC  |
| - Domain matching                 |  | - Rubric scoring         |  | - Calendar invite sync   |
| - Calendar slot publishing        |  | - Growth analytics       |  | - Video link generation  |
+-----------------------------------+  +--------------------------+  +--------------------------+
```

### Identified Core Components & Interfaces:
1. **Student & Mentor Web Interface Component** (`<<component>>`)
   - *Provided Interface*: Web UI Controls, Dashboard View
   - *Required Interface*: REST API endpoints provided by Order/Session Manager & Profile Service.
2. **Order & Session Manager Component** (`<<component>>`)
   - *Provided Interface*: `ISessionBookingAPI` (Slot reservation, quota checks)
   - *Required Interface*: `IProfileAvailability`, `ICalendarSync`, `IScorecardService`.
3. **Alumni Profile & Availability Service Component** (`<<component>>`)
   - *Provided Interface*: `IProfileAvailability` (Domain filtering, slot lookup)
   - *Required Interface*: Database persistence connector.
4. **Rating & Scorecard Service Component** (`<<component>>`)
   - *Provided Interface*: `IScorecardService` (Rubric submission, trend calculations)
   - *Required Interface*: Notification dispatcher.
5. **Notification & Calendar Sync Service Component** (`<<component>>`)
   - *Provided Interface*: `ICalendarSync` (Async event queue consumer)
   - *Required Interface*: Google/Outlook Calendar REST APIs, Email Gateway.

---
*Attached Diagram Files in `2-Architectural_Diagram/`:*
* [Lab_3_Component_Diagram.drawio](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/2-Architectural_Diagram/Lab_3_Component_Diagram.drawio)
* [Lab_3_Architecture_Student_handout.pdf](file:///media/shashank/Data1/Link%20to%20PDocuments/sem%205/SE/LAB%203/2-Architectural_Diagram/Lab_3_Architecture_Student_handout.pdf)
