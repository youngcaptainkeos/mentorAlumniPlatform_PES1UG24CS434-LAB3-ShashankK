"""Student Scholarship Eligibility Screener Module.

This module provides functionality to evaluate student scholarship applications
based on GPA, extracurricular credits, and family income thresholds.
It features safe arithmetic formula evaluation, applicant input validation,
and structured JSON persistence.
"""

import ast
import json
import operator
from typing import Any, Dict, List, Optional, Tuple

# Default application thresholds
DEFAULT_INCOME_LIMIT = 800000
DEFAULT_CUTOFF = 85.0
DEFAULT_FORMULA = "gpa * 10 + credits * 2"

# Global state container avoiding bare global variable rebinds
_STATE: Dict[str, Any] = {
    "results": {},
    "formula": DEFAULT_FORMULA,
}

_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def safe_eval_formula(formula_expr: str, context: Dict[str, float]) -> float:
    """Safely evaluate an arithmetic formula expression against a context.

    Prevents arbitrary code execution by strictly validating the AST against
    an allowlist of numeric constants, mathematical operators, and variables.

    Args:
        formula_expr: Expression string (e.g., 'gpa * 10 + credits * 2').
        context: Mapping of variable names to their numeric float values.

    Returns:
        Evaluated numeric float result.

    Raises:
        ValueError: If expression contains disallowed AST nodes or variables.
    """
    def _evaluate_node(node: ast.AST) -> float:
        if isinstance(node, ast.Expression):
            return _evaluate_node(node.body)
        if (
            isinstance(node, ast.Constant)
            and isinstance(node.value, (int, float))
        ):
            return float(node.value)
        if isinstance(node, ast.Name):
            if node.id in context:
                return float(context[node.id])
            raise ValueError(f"Unknown variable in formula: {node.id}")
        if isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type in _ALLOWED_OPERATORS:
                left_val = _evaluate_node(node.left)
                right_val = _evaluate_node(node.right)
                return _ALLOWED_OPERATORS[op_type](left_val, right_val)
            raise ValueError(
                f"Unsupported binary operator: {op_type.__name__}"
            )
        if isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type in _ALLOWED_OPERATORS:
                operand_val = _evaluate_node(node.operand)
                return _ALLOWED_OPERATORS[op_type](operand_val)
            raise ValueError(
                f"Unsupported unary operator: {op_type.__name__}"
            )
        raise ValueError(f"Disallowed expression node: {type(node).__name__}")

    try:
        parsed_ast = ast.parse(formula_expr.strip(), mode="eval")
        return _evaluate_node(parsed_ast)
    except SyntaxError as err:
        raise ValueError(f"Invalid formula syntax: {err}") from err


def validate_application_data(
    gpa: float, credit_hours: float, income: float
) -> Tuple[bool, str]:
    """Validate applicant data bounds to ensure realistic and legal values.

    Args:
        gpa: Grade Point Average (must be between 0.0 and 10.0).
        credit_hours: Extracurricular credits earned (must be non-negative).
        income: Annual family income in currency units (must be non-negative).

    Returns:
        Tuple of (is_valid, reason_message).
    """
    if not isinstance(gpa, (int, float)) or not 0.0 <= gpa <= 10.0:
        return False, f"GPA {gpa} out of valid bounds (0.0 - 10.0)"
    if not isinstance(credit_hours, (int, float)) or credit_hours < 0:
        return False, f"Credits {credit_hours} cannot be negative"
    if not isinstance(income, (int, float)) or income < 0:
        return False, f"Income {income} cannot be negative"
    return True, "Valid application data"


def calculate_merit_score(gpa: float, credit_hours: float) -> float:
    """Calculate the merit score using the active merit formula.

    Args:
        gpa: Grade point average.
        credit_hours: Extracurricular credits earned.

    Returns:
        Calculated merit score.
    """
    context = {"gpa": float(gpa), "credits": float(credit_hours)}
    active_formula = _STATE["formula"]
    return safe_eval_formula(active_formula, context)


def evaluate_applicant(
    student_id: str,
    test_scores: Dict[str, Any],
    logs: Optional[List[str]] = None,
) -> bool:
    """Evaluate an applicant's scholarship eligibility and record outcomes.

    Args:
        student_id: Unique identifier for the student.
        test_scores: Dict containing 'gpa', optional 'credits', and 'income'.
        logs: Optional list for appending execution trace logs.

    Returns:
        True if the applicant qualifies for scholarship, False otherwise.
    """
    if logs is None:
        logs = []

    gpa = test_scores.get("gpa")
    credit_hours = test_scores.get("credits", 0)
    income = test_scores.get("income", 0)

    # Perform domain sanity validation
    is_valid, reason = validate_application_data(gpa, credit_hours, income)
    if not is_valid:
        _STATE["results"][student_id] = {
            "score": None,
            "eligible": False,
            "status": f"Rejected: {reason}",
        }
        logs.append(f"{student_id} rejected: {reason}")
        return False

    score = calculate_merit_score(gpa, credit_hours)
    eligible = score >= DEFAULT_CUTOFF and income < DEFAULT_INCOME_LIMIT
    _STATE["results"][student_id] = {
        "score": score,
        "eligible": eligible,
        "status": "Eligible" if eligible else "Ineligible",
    }
    logs.append(f"{student_id} scored {score}")
    return eligible


def change_formula(new_formula: str) -> None:
    """Update the merit evaluation formula after validating its syntax.

    Args:
        new_formula: Expression string to evaluate merit scores.

    Raises:
        ValueError: If formula contains invalid syntax or unsafe operations.
    """
    test_context = {"gpa": 8.0, "credits": 2.0}
    safe_eval_formula(new_formula, test_context)
    _STATE["formula"] = new_formula


def persist_results(file: str = "scholarships.json") -> None:
    """Save evaluation results to a JSON file safely using a context manager.

    Args:
        file: Destination filepath string.
    """
    with open(file, "w", encoding="utf-8") as file_handle:
        json.dump(_STATE["results"], file_handle, indent=2)


def load_results(file: str = "scholarships.json") -> Dict[str, Any]:
    """Load evaluation results from a JSON file handling IO errors gracefully.

    Args:
        file: Source filepath string.

    Returns:
        Dictionary mapping student IDs to evaluation records.
    """
    try:
        with open(file, "r", encoding="utf-8") as file_handle:
            loaded_data = json.load(file_handle)
            if isinstance(loaded_data, dict):
                _STATE["results"] = loaded_data
    except (FileNotFoundError, json.JSONDecodeError, OSError) as err:
        print(f"Notice: Could not load results from {file} ({err})")
    return _STATE["results"]


def print_shortlist() -> None:
    """Display shortlisted applicants whose scholarship criteria were met."""
    print("Shortlisted applicants:")
    for student_id, details in _STATE["results"].items():
        if details.get("eligible"):
            print(f"  {student_id} score = {details.get('score')}")


def main() -> None:
    """Execute standard screening test cases and interactive input."""
    evaluate_applicant("U001", {"gpa": 9.1, "credits": 4, "income": 450000})
    evaluate_applicant("U002", {"gpa": 7.2, "credits": 1, "income": 300000})
    evaluate_applicant("U003", {"gpa": 12.5, "credits": -3, "income": -1})
    evaluate_applicant("U004", {"gpa": 6.5})

    formula = input("Merit formula (Enter to keep default): ")
    if formula.strip():
        try:
            change_formula(formula)
        except ValueError as err:
            print(f"Error in formula ({err}), retaining default formula.")

    evaluate_applicant("U005", {"gpa": 8.4, "credits": 3, "income": 600000})
    persist_results()
    load_results()
    print_shortlist()


if __name__ == "__main__":
    main()
