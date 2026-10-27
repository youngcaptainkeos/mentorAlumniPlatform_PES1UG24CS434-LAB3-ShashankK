# Lab 5: Static Code Analysis — Student Scholarship Eligibility Screener

**Student Name:** Shashank Keshava Murthy  
**SRN:** PES1UG24CS434  
**Course:** Software Engineering (UE22CS351A / SE Lab)  
**Section:** Section 5H  
**Assigned Repository:** [SETAPESU26/L5_11_scholarship_screener](https://github.com/SETAPESU26/L5_11_scholarship_screener)  
**Main Portfolio Repository:** [youngcaptainkeos/mentorAlumniPlatform_PES1UG24CS434-LAB3-ShashankK](https://github.com/youngcaptainkeos/mentorAlumniPlatform_PES1UG24CS434-LAB3-ShashankK)

---

## 📌 Deliverables Summary

| Deliverable | Location / File | Description |
| :--- | :--- | :--- |
| **Cleaned & Fixed Python Code** | [`scholarship_system.py`](./scholarship_system.py) | Fully refactored script passing Bandit (0 issues), Flake8 (0 violations), and Pylint (**10.00 / 10**). |
| **Identified Issues Table** | [`issues.md`](./issues.md) | Exhaustive documentation of 15 security, defect, quality, and domain logic issues with remediation steps. |
| **Reflection Answers** | [`reflection.md`](./reflection.md) | In-depth answers to the 4 core reflection questions covering tool comparison, severity triage, dynamic testing, and CI/CD pipelines. |
| **Before Reports** | [`reports/bandit_report_before.txt`](./reports/bandit_report_before.txt)<br>[`reports/flake8_report_before.txt`](./reports/flake8_report_before.txt)<br>[`reports/pylint_report_before.txt`](./reports/pylint_report_before.txt) | Baseline diagnostic outputs generated directly from the starter repository. |
| **After Reports** | [`reports/bandit_report_after.txt`](./reports/bandit_report_after.txt)<br>[`reports/flake8_report_after.txt`](./reports/flake8_report_after.txt)<br>[`reports/pylint_report_after.txt`](./reports/pylint_report_after.txt) | Verification reports confirming clean runs across all three tools. |
| **Root Clean Reports** | [`bandit_report.txt`](./bandit_report.txt)<br>[`flake8_report.txt`](./flake8_report.txt)<br>[`pylint_report.txt`](./pylint_report.txt) | Standalone clean reports matching the standard lab grading path. |

---

## 📊 Before vs. After Quantitative Comparison

```
Metric                 Before Fixes          After Fixes           Improvement
----------------------------------------------------------------------------------
Bandit Security Issues  2 (1 Med, 1 Low)      0 (No issues)         100% Resolved
Flake8 Style Errors     12 Violations         0 Violations          100% Compliant
Pylint Score            4.69 / 10             10.00 / 10            +5.31 (+113.2%)
Prompt Injection Guard  Vulnerable (eval)     Protected (AST parse) Immune to RCE
Domain Input Validation None (U003 qualified) Strict Sanity Checks  U003 rejected
```

---

## 🛠️ Summary of Applied Fixes

### 1. Security Hardening (Bandit & OWASP)
- **Arbitrary Code Execution / Prompt Injection (`B307` / `CWE-78`):**  
  Eliminated `eval(MERIT_FORMULA)`. Replaced with `safe_eval_formula()`, an Abstract Syntax Tree (AST) evaluator that strictly parses and executes only arithmetic binary operators (`+`, `-`, `*`, `/`), unary signs, numbers, and allowed variables (`gpa`, `credits`). Function calls and dangerous attributes are rejected.
- **Bare Exception Suppression (`B110` / `CWE-703`):**  
  Replaced dangerous `except: pass` in `load_results()` with specific exception handling `(FileNotFoundError, json.JSONDecodeError, OSError)` and descriptive error logging.

### 2. Code Quality & Logic Integrity (Pylint)
- **Dangerous Mutable Default Argument (`W0102`):**  
  Changed `logs=[]` in `evaluate_applicant()` to `logs: Optional[List[str]] = None`, initializing a fresh list inside the function to eliminate cross-caller memory leakage.
- **Shadowing Built-in Identifier (`W0622`):**  
  Renamed parameter `credits` to `credit_hours` to avoid shadowing Python's built-in `credits`.
- **Global State Elimination (`W0603`):**  
  Replaced bare global rebinding (`global MERIT_FORMULA`, `global results`) with an internal state container `_STATE` avoiding global namespace pollution.
- **Resource Management & Encoding (`W1514`, `R1732`):**  
  Migrated all file I/O to context managers (`with open(..., encoding="utf-8")`) to prevent file descriptor leaks.
- **Modernized String Formatting (`C0209`):**  
  Converted legacy `%` string formatting to Python 3 f-strings.
- **Complete PEP 257 Docstrings (`C0114`, `C0116`):**  
  Authored thorough module and function docstrings with type annotations.

### 3. Style & Standards Compliance (Flake8 & PEP 8)
- Removed unused imports `math` and `sys` (`F401`).
- Enforced 2 blank lines between all top-level functions and classes (`E302`, `E305`).
- Replaced singleton comparison `== True` with idiomatic truthiness `if details.get("eligible"):` (`E712`, `C0121`).
- Renamed camelCase `printShortlist` to PEP 8 compliant `print_shortlist` (`C0103`).
- Kept all line lengths strictly within 79 characters (`E501`).

### 4. Domain Validation & Business Logic Bug Fix
- **Applicant U003 Anomaly:**  
  The original program permitted invalid data (`GPA 12.5`, `credits -3`, `income -1`) to achieve an impossible score of 119.0 and qualify for the shortlist.  
  Added `validate_application_data()` verifying:
  - $0.0 \le \text{GPA} \le 10.0$
  - $\text{Credits} \ge 0$
  - $\text{Family Income} \ge 0$  
  Invalid records are rejected and logged, leaving only genuine candidates (`U001` and `U005`) on the shortlist.

---

## 🚀 How to Run and Verify

```bash
# 1. Activate python virtual environment
source venv/bin/activate

# 2. Run the application
python Lab-5/scholarship_system.py

# 3. Verify with Bandit (Security)
bandit -r Lab-5/scholarship_system.py

# 4. Verify with Flake8 (PEP 8 Style)
flake8 Lab-5/scholarship_system.py

# 5. Verify with Pylint (Quality Score 10.00/10)
pylint Lab-5/scholarship_system.py
```
