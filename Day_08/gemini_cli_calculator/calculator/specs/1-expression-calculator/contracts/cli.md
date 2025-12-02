# Contract: Command-Line Interface

**Feature**: Expression Calculator

This document defines the public contract for the command-line interface (CLI).

## Command

The tool will be executed as a Python script.

```bash
python -m calculator.cli "<expression>"
```

## Input

-   **`<expression>`** (string, required): A string containing the mathematical expression to be evaluated. The expression must be enclosed in quotes to be treated as a single argument.

## Output

### On Success

-   The tool will print the numerical result of the calculation to `stdout`.
-   The tool will exit with code `0`.

**Example:**

```bash
$ python -m calculator.cli "5 + 3"
8
```

### On Failure

-   If the expression is invalid (e.g., malformed, division by zero), the tool will print a descriptive error message to `stderr`.
-   The tool will exit with code `1`.

**Example (Division by Zero):**

```bash
$ python -m calculator.cli "10 / 0"
Error: Division by zero
```

**Example (Invalid Expression):**

```bash
$ python -m calculator.cli "5 + * 3"
Error: Invalid expression
```
