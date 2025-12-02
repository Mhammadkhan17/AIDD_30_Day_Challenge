# Tasks: Expression Calculator

**Input**: Design documents from `specs/1-expression-calculator/`
**Prerequisites**: plan.md, spec.md

---

## Phase 1: Setup

**Purpose**: Create the basic project directory and file structure.

- [X] T001 [P] Create the directory `src/calculator`.
- [X] T002 [P] Create the file `src/calculator/__init__.py`.
- [X] T003 [P] Create the file `src/calculator/evaluate.py`.
- [X] T004 [P] Create the directory `tests`.
- [X] T005 [P] Create the file `tests/__init__.py`.
- [X] T006 [P] Create the file `tests/test_evaluate.py`.
- [X] T007 Create a `pytest.ini` file in the root to configure the test runner.

---

## Phase 2: Foundational (CLI)

**Purpose**: Create the command-line entry point and the basic evaluation function stub.

- [X] T008 Create the CLI entry point file `src/calculator/cli.py`.
- [X] T009 In `src/calculator/cli.py`, implement argument parsing to accept an expression string.
- [X] T010 In `src/calculator/evaluate.py`, create a stub function `evaluate(expression: str) -> float | str`.
- [X] T011 In `src/calculator/cli.py`, call the `evaluate` function and print its result.

---

## Phase 3: User Story 1 - Addition

**Goal**: Implement the addition feature.
**Independent Test**: The `test_addition` case in `pytest` should pass.

### Tests for User Story 1
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T012 [US1] In `tests/test_evaluate.py`, write a failing test for a simple addition expression (e.g., `"2 + 3"`).

### Implementation for User Story 1

- [X] T013 [US1] In `src/calculator/evaluate.py`, implement the logic to correctly evaluate the addition expression to make the test pass.

---

## Phase 4: User Story 2 - Subtraction

**Goal**: Implement the subtraction feature.
**Independent Test**: The `test_subtraction` case in `pytest` should pass.

### Tests for User Story 2
- [X] T014 [P] [US2] In `tests/test_evaluate.py`, write a failing test for a simple subtraction expression (e.g., `"5 - 3"`).

### Implementation for User Story 2
- [X] T015 [US2] In `src/calculator/evaluate.py`, implement the logic to correctly evaluate the subtraction expression.

---

## Phase 5: User Story 3 - Multiplication

**Goal**: Implement the multiplication feature.
**Independent Test**: The `test_multiplication` case in `pytest` should pass.

### Tests for User Story 3
- [X] T016 [P] [US3] In `tests/test_evaluate.py`, write a failing test for a simple multiplication expression (e.g., `"4 * 3"`).

### Implementation for User Story 3
- [X] T017 [US3] In `src/calculator/evaluate.py`, implement the logic to correctly evaluate the multiplication expression.

---

## Phase 6: User Story 4 - Division

**Goal**: Implement the division feature.
**Independent Test**: The `test_division` case in `pytest` should pass.

### Tests for User Story 4
- [X] T018 [P] [US4] In `tests/test_evaluate.py`, write a failing test for a simple division expression (e.g., `"10 / 2"`).

### Implementation for User Story 4
- [X] T019 [US4] In `src/calculator/evaluate.py`, implement the logic to correctly evaluate the division expression.

---

## Phase 7: Error Handling

**Goal**: Implement robust error handling for invalid inputs.
**Independent Test**: Specific tests for error conditions should pass.

### Tests for Error Handling
- [X] T020 [P] In `tests/test_evaluate.py`, write a failing test for division by zero.
- [X] T021 [P] In `tests/test_evaluate.py`, write a failing test for a malformed expression.

### Implementation for Error Handling
- [X] T022 In `src/calculator/evaluate.py`, implement logic to catch division by zero and return `"Error: Division by zero"`.
- [X] T023 In `src/calculator/evaluate.py`, implement logic to handle invalid expressions and return `"Error: Invalid expression"`.

---

## Phase 8: Polish

**Purpose**: Final cleanup and documentation.

- [X] T024 [P] Add docstrings and type hints to all functions in `src/calculator/`.
- [X] T025 Review and run all tests one final time using `pytest`.

---

## Dependencies & Execution Order

- **Phase 1 (Setup)** must complete before all other phases.
- **Phase 2 (Foundational)** depends on Phase 1.
- **Phases 3-7 (User Stories & Errors)** can be worked on in parallel after Phase 2 is complete.
- **Phase 8 (Polish)** should be done last.

Within each user story phase, the test task MUST be completed before the implementation task.

## Implementation Strategy

### MVP First (Addition)

1.  Complete Phase 1 & 2.
2.  Complete all tasks in **Phase 3 (User Story 1 - Addition)**.
3.  At this point, the calculator can correctly add two numbers. This is the first testable, valuable increment.

### Incremental Delivery

1.  Deliver MVP (Addition).
2.  Complete Phase 4 (Subtraction) and deliver.
3.  Complete Phase 5 (Multiplication) and deliver.
4.  Complete Phase 6 (Division) and deliver.
5.  Complete Phase 7 (Error Handling) and deliver.
