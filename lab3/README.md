# Lab 3: Component Modelling & Architectural Pattern Selection

**Project Title**: Alumni Mentorship & Mock Interview Platform  
**Problem Statement**: #06 (Campus & Academic Operations)  
**Student Name**: Shashank K  
**SRN**: PES1UG24CS434  
**Course**: Software Engineering (UE22CS351A / SE Lab) — Department of Computer Science & Engineering, PES University  

---

## 📌 Lab Overview & Objectives
Lab 3 focuses on evaluating software architectural styles (Layered, Microservices, Client-Server), selecting the optimal architecture for Problem Statement #06, designing a UML Component Diagram showing provided/required interfaces, and organizing the individual project submission deliverables into 6 standardized folders as outlined in `Git Hub Project Submission Details.docx`.

---

## 📁 Lab 3 Subfolder & Deliverables Structure

```
lab3/
├── 1-RE/                                  # 1-Folder for RE
│   └── FR_NFR_Specification.md            # Detailed FR/NFR Table & RTM Matrix
├── 2-Architectural_Diagram/               # 2-Folder for Architectural Diagram
│   ├── Architecture_Justification_and_Component_Diagram.md # Architectural pattern justification
│   └── Lab_3_Component_Diagram.drawio     # UML Component Diagram
├── 3-Project_Creation_Screenshots/        # 3-Folder for Project Creational Screenshots
│   └── Jira_and_GitHub_Project_Setup.md   # GitHub & Jira setup documentation
├── 4-SRS_and_Work_Breakdown/              # 4-Folder for SRS and Work Breakdown steps
│   └── SRS_and_WBS_Specification.md       # IEEE SRS & Work Breakdown Structure
├── 5-Github_Copilot_Code/                 # 5-Folder for GitHub Copilot generated code
│   └── Copilot_Generated_Code_Summary.md  # Copilot prompts & generated Redis locking code
├── 6-Software_Testing_Tools/              # 6-Folder for Practicing on Software Testing Tools
│   └── Testing_Tools_and_Vibe_Coding_Report.md # Vibe coding bug fixing report & test logs
├── Git Hub Project Submission Details.docx
├── Lab_3_Architecture_Student_handout.pdf
└── Lab_3_Component_Diagram.drawio
```

---

## 🏛️ Architectural Selection Summary
* **Selected Pattern**: **Layered Modular Microservices Architecture**
* **Justification**: Decouples the high-concurrency reservation lock engine from static profile rendering services and isolates third-party Google/Outlook calendar and video conferencing APIs.
* **Security & Performance**: Enforces isolated data privacy containers for 24-hour soft-deletion compliance (NFR-001) and achieves sub-200ms transaction lock latency (NFR-002).
