<!--
Sync Impact Report

- Version change: 0.0.0 -> 1.0.0
- Added Principles:
  - I. Simplicity
  - II. Correctness
  - III. Test-Driven Development
- Removed Principles: None (template had placeholders)
- Added Sections:
  - Development Workflow
  - Quality Gates
- Templates requiring updates:
  - .specify/templates/plan-template.md (updated)
  - .specify/templates/spec-template.md (no changes needed)
  - .specify/templates/tasks-template.md (updated)
- Follow-up TODOs: None
-->
# Simple Calculator Constitution

## Core Principles

### I. Simplicity
The project must be kept simple, focusing only on basic arithmetic operations (add, subtract, multiply, divide). No feature creep.

### II. Correctness
All calculations must be 100% accurate. Floating point inaccuracies should be handled where possible.

### III. Test-Driven Development
Development must follow the TDD (Test-Driven Development) methodology. Write a failing test before writing implementation code.

## Development Workflow

1. Create a failing test case that captures the new requirement.
2. Write the minimal code to make the test pass.
3. Refactor the code for clarity and simplicity.

## Quality Gates

All code must pass linting and unit tests before being committed.

## Governance

All pull requests must be reviewed and approved by at least one other team member. The constitution can be amended via a pull request, which must be approved by the project lead.

**Version**: 1.0.0 | **Ratified**: 2025-12-02 | **Last Amended**: 2025-12-02