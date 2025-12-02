# Research: Expression Calculator

**Purpose**: To document the technology choices for the Expression Calculator feature.

## Technology Stack Selection

### Decision: Python 3.11 with Standard Library

- **Rationale**: Python was chosen for its readability and the power of its standard library. For this feature, the built-in `eval()` function provides a direct and simple way to evaluate mathematical expressions, which perfectly aligns with the project's "Simplicity" principle. Using only the standard library avoids introducing external dependencies, further simplifying setup and maintenance.
- **Alternatives considered**:
    - **Manual Parsing**: Building a manual parser (e.g., using shunting-yard algorithm) was considered. This was rejected as it would add significant complexity for a problem that has a simple, secure-enough solution for this context, violating the "Simplicity" principle.
    - **JavaScript/Node.js**: Also has an `eval()` function, but Python was chosen for its clean syntax for a command-line tool.

### Decision: `pytest` for Testing

- **Rationale**: `pytest` is the de-facto standard for testing in Python. It has a simple, clean syntax for writing tests and powerful features for discovery, fixtures, and assertions. This choice supports the "Correctness" and "Test-Driven Development" principles.
- **Alternatives considered**:
    - **`unittest`**: Python's built-in testing framework. `pytest` was chosen over `unittest` due to its less verbose syntax and more powerful feature set, which improves developer productivity.
