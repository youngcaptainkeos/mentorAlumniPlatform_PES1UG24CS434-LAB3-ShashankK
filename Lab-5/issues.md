# Static Code Analysis Issues Report — Student Scholarship Eligibility Screener

**Student Name:** Shashank Keshava Murthy  
**SRN:** PES1UG24CS434  
**Course:** Software Engineering (UE22CS351A / SE Lab)  
**Assigned Repository:** [SETAPESU26/L5_11_scholarship_screener](https://github.com/SETAPESU26/L5_11_scholarship_screener)  
**Analyzed Script:** `scholarship_system.py`

---

## 1. Executive Summary

Static code analysis was performed on `scholarship_system.py` using three industry-standard tools:
- **Bandit (v1.9.4):** Security analysis detecting insecure patterns, dangerous function invocations, and exception suppression.
- **Flake8 (v7.4.1):** PEP 8 style, syntax, and formatting compliance.
- **Pylint (v4.1.3):** Deep semantic code quality, logic defects, dangerous defaults, and design standards.

### Initial vs. Final Metrics Overview

| Tool | Initial State (Before Fixes) | Final State (After Fixes) | Delta / Improvement |
| :--- | :--- | :--- | :--- |
| **Bandit** | 2 Issues (1 Medium severity, 1 Low severity) | **0 Issues Identified** | 100% resolved (0 High, 0 Med, 0 Low) |
| **Flake8** | 12 Violations (F401, E302, E305, E722, E712) | **0 Violations** | 100% PEP 8 compliant |
| **Pylint Score** | **4.69 / 10** (25 warnings/conventions/errors) | **10.00 / 10** | **+5.31 (+113.2% increase)** |

---

## 2. Comprehensive Issue Tracking Table

The following table documents all identified issues, categorized by tool, severity, location in original code, diagnostic description, and the remediation approach applied.

| Issue / Error Code | Tool | Type / Severity | Original Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **B307 / W0123** | Bandit / Pylint | Security (Medium Severity, CWE-78) | `scholarship_system.py:12` | **Dangerous `eval()` Invocation**: `calculate_merit_score` evaluated `MERIT_FORMULA` via `eval()`. Combined with `formula = input(...)`, an attacker can supply malicious Python code (e.g., `__import__('os').system(...)`), resulting in Arbitrary Remote Code Execution (RCE) / Prompt Injection. | Removed `eval()`. Implemented `safe_eval_formula()` using Python's `ast` parser with strict whitelist validation allowing only mathematical binary operations (`+`, `-`, `*`, `/`), unary signs, numeric constants, and approved identifiers (`gpa`, `credits`). Any function calls or unauthorized AST nodes raise `ValueError`. |
| **B110 / E722 / W0702** | Bandit / Flake8 / Pylint | Security & Reliability (Low Severity, CWE-703) | `scholarship_system.py:37-38` | **Bare `except:` with `pass`**: `load_results` caught all exceptions indiscriminately and suppressed them with `pass`. This silences critical runtime signals including `KeyboardInterrupt`, `MemoryError`, missing files, and JSON syntax corruption. | Replaced the bare `except:` clause with explicit expected exceptions `(FileNotFoundError, json.JSONDecodeError, OSError)` and informative non-fatal console diagnostics. |
| **W0102** | Pylint | Defect / Bug (Medium Severity) | `scholarship_system.py:14` | **Dangerous Mutable Default Argument**: `evaluate_applicant(..., logs=[])` used a mutable list as default argument. In Python, default arguments are evaluated once at function definition time, causing the list to be shared across all subsequent invocations. | Changed the function signature to `logs: Optional[List[str]] = None`, and initialized an independent list inside the function body (`if logs is None: logs = []`). |
| **F401 / W0611** | Flake8 / Pylint | Clean Code / Quality (Low) | `scholarship_system.py:2` | **Unused Import `math`**: The `math` module was imported at top of file but never referenced in any function or statement. | Removed `import math` to reduce memory overhead and eliminate namespace pollution. |
| **F401 / W0611** | Flake8 / Pylint | Clean Code / Quality (Low) | `scholarship_system.py:3` | **Unused Import `sys`**: The `sys` module was imported at top of file but never utilized. | Removed `import sys`. |
| **W0622** | Pylint | Code Quality / Naming (Low) | `scholarship_system.py:11, 16` | **Redefining Built-in Name `credits`**: The parameter `credits` shadowed Python's built-in `credits` constant in the builtins namespace. | Renamed parameter and local variable to `credit_hours` across function definitions and callers. |
| **W0603** | Pylint | Maintainability / Design (Low-Med) | `scholarship_system.py:25, 34` | **Global Statement Usage**: `global MERIT_FORMULA` and `global results` re-bound module-level variables directly from within function bodies, introducing hidden state mutations and tight coupling. | Replaced raw global variables with an internal module state dictionary `_STATE = {"results": {}, "formula": DEFAULT_FORMULA}`. State updates mutate dictionary keys rather than rebinding global identifiers. |
| **W1514 / R1732** | Pylint | Resource Management (Medium) | `scholarship_system.py:29-31, 36` | **Unmanaged File I/O & Missing Encoding**: `open(file, "w")` without context managers risks leaking file descriptors if an exception occurs before `f.close()`. Additionally, omitting `encoding` relies on platform-dependent defaults. | Refactored file operations to use `with open(file, "w", encoding="utf-8") as file_handle:` and direct serialization with `json.dump()` / `json.load()`. |
| **C0103** | Pylint | Naming Convention (Low) | `scholarship_system.py:40` | **Non-snake_case Function Name**: `printShortlist` violated PEP 8 naming conventions which mandate snake_case for functions. | Renamed function to `print_shortlist` adhering strictly to PEP 8 standards. |
| **E712 / C0121** | Flake8 / Pylint | Style & Idiomatic Python (Low) | `scholarship_system.py:43` | **Explicit Comparison to Boolean Literal**: `if results[r]["eligible"] == True:` violated PEP 8 guidance against comparing booleans to `True`. | Refactored to idiomatic truthiness evaluation: `if details.get("eligible"):`. |
| **C0209** | Pylint | Code Modernization (Low) | `scholarship_system.py:21` | **Legacy String Formatting**: Used old printf-style `%` string formatting `"%s scored %s" % (student_id, score)`. | Upgraded to modern Python 3 f-string formatting: `f"{student_id} scored {score}"`. |
| **C0114 / C0116** | Pylint | Documentation (Medium) | `scholarship_system.py:1, 11, 14, 24, 28, 33, 40, 46` | **Missing Module & Function Docstrings**: The module and all its functions lacked docstrings explaining functionality, parameters, return types, and exceptions. | Authored detailed PEP 257 docstrings for the module and every function, complete with argument specifications and type hints. |
| **E302 / E305** | Flake8 | Formatting / Whitespace (Low) | `scholarship_system.py:11, 14, 24, 28, 33, 40, 46, 59` | **PEP 8 Blank Line Violations**: Top-level function definitions had only 1 blank line preceding them instead of the mandatory 2 blank lines. Top-level call also lacked 2 preceding blank lines. | Added standard 2 blank lines between all top-level functions and classes in compliance with PEP 8. |
| **Semantic / Logic Bug** | Manual Audit & Execution | Business Logic Defect (High Severity) | `scholarship_system.py:15-19, 49` | **Missing Domain Input Validation (Applicant U003 Anomaly)**: Applicant `U003` has invalid data (`gpa: 12.5` > 10.0 max, `credits: -3` < 0, `income: -1` < 0). Due to lack of validation, the merit score was calculated as `12.5*10 + (-3)*2 = 119.0`, erroneously qualifying an invalid candidate for scholarship shortlist. | Created `validate_application_data(gpa, credit_hours, income)` enforcing `0.0 <= gpa <= 10.0`, `credit_hours >= 0`, and `income >= 0`. Applicants with invalid records are marked ineligible with clear rejection logs. |
| **Design Guard** | Architecture | Execution Safety (Low-Med) | `scholarship_system.py:59` | **Unprotected Script Execution**: `main()` was invoked directly at module level, executing interactive CLI code even when imported by automated test runners or external modules. | Protected module execution inside standard `if __name__ == "__main__":` entrypoint guard. |

---

## 3. High-Priority Issues Detailed Deep-Dive

### 3.1. Arbitrary Code Execution / Prompt Injection via `eval()` (Bandit B307 / CWE-78)
- **Vulnerability Mechanism:**  
  In the baseline code, `calculate_merit_score` computed scores via `eval(MERIT_FORMULA)`. The program additionally prompted the user:
  ```python
  formula = input("Merit formula (Enter to keep default): ")
  if formula:
      change_formula(formula)
  ```
  If a user or external prompt injected arbitrary Python code such as:
  ```python
  __import__('os').system('cat /etc/passwd')
  ```
  or malicious file exfiltration scripts, the `eval()` call executed it with the full privileges of the host process.
- **Remediation:**  
  Replaced dynamic string execution with an Abstract Syntax Tree (AST) evaluator `safe_eval_formula()`. The AST parser breaks down the mathematical string and recursively inspects each AST node against a strict whitelist (`ast.Add`, `ast.Sub`, `ast.Mult`, `ast.Div`, `ast.USub`, `ast.Constant`, `ast.Name`). Any invocation of `ast.Call`, `ast.Attribute`, or unauthorized names immediately triggers a `ValueError`, providing provable mathematical safety without executing arbitrary code.

### 3.2. Mutable Default Argument State Leak (Pylint W0102)
- **Vulnerability Mechanism:**  
  Python binds default argument expressions only once when the function definition is executed at load time. In the baseline code:
  ```python
  def evaluate_applicant(student_id, test_scores, logs=[]):
      ...
      logs.append("%s scored %s" % (student_id, score))
  ```
  Every caller that does not explicitly provide a `logs` argument shares the exact same list instance in memory. This introduces cross-applicant state pollution, memory leaks, and non-deterministic behavior during sequential calls.
- **Remediation:**  
  Adopted the standard Python sentinel pattern:
  ```python
  def evaluate_applicant(
      student_id: str,
      test_scores: Dict[str, Any],
      logs: Optional[List[str]] = None,
  ) -> bool:
      if logs is None:
          logs = []
      ...
  ```
  This guarantees every call defaults to a freshly allocated, isolated list.

### 3.3. Bare Exception Suppression (Bandit B110 / Flake8 E722 / Pylint W0702)
- **Vulnerability Mechanism:**  
  In `load_results()`:
  ```python
  try:
      results = json.loads(open(file).read())
  except:
      pass
  ```
  The bare `except:` caught `BaseException`, intercepting critical system signals such as `KeyboardInterrupt` (Ctrl+C), `SystemExit`, and memory exhaustion, while also silently swallowing corrupted JSON or I/O permission failures.
- **Remediation:**  
  Replaced with a targeted exception tuple:
  ```python
  try:
      with open(file, "r", encoding="utf-8") as file_handle:
          loaded_data = json.load(file_handle)
          if isinstance(loaded_data, dict):
              _STATE["results"] = loaded_data
  except (FileNotFoundError, json.JSONDecodeError, OSError) as err:
      print(f"Notice: Could not load results from {file} ({err})")
  ```
  This maintains application resilience while surfacing actionable diagnostics and respecting system interrupts.
