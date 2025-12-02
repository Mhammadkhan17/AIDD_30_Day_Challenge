def evaluate(expression: str) -> float | str:
    """
    Evaluates a mathematical expression string.

    Args:
        expression: The mathematical expression to evaluate.

    Returns:
        The numerical result of the expression, or an error string if the
        expression is invalid or results in division by zero.
    """
    try:
        # Basic check to prevent arbitrary code execution via eval()
        # Only allow numbers, basic arithmetic operators, and parentheses
        allowed_chars = "0123456789.+-*/() "
        for char in expression:
            if char not in allowed_chars:
                return "Error: Invalid expression"

        # Using eval() for simplicity as specified in research.md
        # This is generally unsafe for untrusted input, but acceptable for this context.
        result = eval(expression)
        return float(result)
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception:
        return "Error: Invalid expression"