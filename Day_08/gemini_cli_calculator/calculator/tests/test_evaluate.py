from calculator.evaluate import evaluate

def test_addition():
    assert evaluate("2 + 3") == 5

def test_subtraction():
    assert evaluate("5 - 3") == 2

def test_multiplication():
    assert evaluate("4 * 3") == 12

def test_division():
    assert evaluate("10 / 2") == 5

def test_division_by_zero():
    assert evaluate("10 / 0") == "Error: Division by zero"

def test_malformed_expression():
    assert evaluate("5 + * 3") == "Error: Invalid expression"