import ast
import json
import math
import operator
import sys

# Global state
results = {}
MERIT_FORMULA = "gpa * 10 + credits * 2"
INCOME_LIMIT = 800000
CUTOFF = 85

_ALLOWED_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def safe_eval_formula(formula_expr, context):
    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.Name):
            if node.id in context:
                return float(context[node.id])
            raise ValueError(f"Unknown variable: {node.id}")
        if isinstance(node, ast.BinOp):
            if type(node.op) in _ALLOWED_OPS:
                return _ALLOWED_OPS[type(node.op)](_eval(node.left), _eval(node.right))
            raise ValueError(f"Unsupported binary operator: {type(node.op)}")
        if isinstance(node, ast.UnaryOp):
            if type(node.op) in _ALLOWED_OPS:
                return _ALLOWED_OPS[type(node.op)](_eval(node.operand))
            raise ValueError(f"Unsupported unary operator: {type(node.op)}")
        raise ValueError(f"Disallowed expression node: {type(node).__name__}")

    return _eval(ast.parse(formula_expr.strip(), mode="eval"))

def calculate_merit_score(gpa, credits):
    # Fix B307: Replace dangerous eval with safe AST evaluator
    return safe_eval_formula(MERIT_FORMULA, {"gpa": gpa, "credits": credits})

def evaluate_applicant(student_id, test_scores, logs=[]):
    gpa = test_scores["gpa"]
    credits = test_scores.get("credits", 0)
    income = test_scores.get("income", 0)
    score = calculate_merit_score(gpa, credits)
    eligible = score >= CUTOFF and income < INCOME_LIMIT
    results[student_id] = {"score": score, "eligible": eligible}
    logs.append("%s scored %s" % (student_id, score))
    return eligible

def change_formula(new_formula):
    global MERIT_FORMULA
    MERIT_FORMULA = new_formula

def persist_results(file="scholarships.json"):
    f = open(file, "w")
    f.write(json.dumps(results))
    f.close()

def load_results(file="scholarships.json"):
    global results
    try:
        results = json.loads(open(file).read())
    except (FileNotFoundError, json.JSONDecodeError, OSError) as err:
        # Fix B110: Avoid try/except/pass; catch specific errors with logging
        print(f"Could not load results: {err}")

def printShortlist():
    print("Shortlisted applicants:")
    for r in results:
        if results[r]["eligible"] == True:
            print(" ", r, "score =", results[r]["score"])

def main():
    evaluate_applicant("U001", {"gpa": 9.1, "credits": 4, "income": 450000})
    evaluate_applicant("U002", {"gpa": 7.2, "credits": 1, "income": 300000})
    evaluate_applicant("U003", {"gpa": 12.5, "credits": -3, "income": -1})
    evaluate_applicant("U004", {"gpa": 6.5})
    formula = input("Merit formula (Enter to keep default): ")
    if formula:
        change_formula(formula)
    evaluate_applicant("U005", {"gpa": 8.4, "credits": 3, "income": 600000})
    persist_results()
    load_results()
    printShortlist()

main()
