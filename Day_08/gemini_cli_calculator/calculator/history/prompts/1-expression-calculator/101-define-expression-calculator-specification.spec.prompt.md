---
id: 101
title: Define Expression Calculator Specification
stage: spec
date: 2025-12-02
surface: agent
model: Gemini
feature: 1-expression-calculator
branch: 1-expression-calculator
user: user
command: /sp.specify "Calculator: input expr(string) -> output result(number)"
labels: [spec, calculator]
links:
  spec: specs/1-expression-calculator/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/1-expression-calculator/spec.md
  - specs/1-expression-calculator/checklists/requirements.md
tests:
  - none
---

## Prompt

/sp.specify "Calculator: input expr(string) -> output result(number)"

## Response snapshot

The specification for the 'Expression Calculator' is complete and located at `specs/1-expression-calculator/spec.md`.

## Outcome

- ✅ Impact: High. Defines the core feature of the project.
- 🧪 Tests: No tests were run.
- 📁 Files: 2 files were created, 1 was updated.
- 🔁 Next prompts: User can now proceed with `/sp.plan`.
- 🧠 Reflection: User interaction was required to clarify error handling. The initial git commands were skipped based on user feedback.

## Evaluation notes (flywheel)

- Failure modes observed: Initial assumption about git workflow was incorrect.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Confirm with user about git workflow at the beginning of a task.
