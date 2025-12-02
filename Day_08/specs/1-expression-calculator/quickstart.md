# Quickstart: Expression Calculator

**Feature**: Expression Calculator

This guide provides instructions on how to set up and run the Expression Calculator.

## Prerequisites

-   Python 3.11 or later
-   `pytest` (for running tests)

## Setup

1.  **Clone the repository** (if you haven't already):
    ```bash
    # This step is a placeholder as repository interaction is currently skipped.
    # git clone <repository-url>
    # cd <repository-directory>
    ```

2.  **Install dependencies**:
    This project uses only the Python standard library, so no dependencies need to be installed. To run the tests, you will need `pytest`:
    ```bash
    pip install pytest
    ```

## Running the Calculator

The calculator is run as a Python module from the root of the project directory.

```bash
python -m calculator.cli "<expression>"
```

**Example:**
```bash
$ python -m calculator.cli "100 / ( 5 + 5 )"
10.0
```

## Running Tests

Tests are located in the `tests/` directory and can be run using `pytest`.

From the project root directory, run:
```bash
pytest
```
