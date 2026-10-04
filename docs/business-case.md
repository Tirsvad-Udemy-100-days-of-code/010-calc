# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [8ccefff] |

---

## Executive Summary

Day 10 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" asks for a console calculator that uses functions, a dictionary of functions, user input, a loop and recursion. This project delivers it as a small, tested and documented Python 3.13+ program with no runtime dependencies.

## Methodological and Standards Foundation

The SQA and QC framework in `framework/` (plan first, then code), ISO/IEC 25010:2023 for quality characteristics, and the Python conventions of the `coding-conventions` skill.

## Problem Statement

The assignment needs a finished, verifiable result with setup and run instructions, not a single untested script.

## Business Opportunity

A compact reference project that shows the lecture concepts and can serve as the template for later course days.

## Objectives

1. Add, subtract, multiply and divide two numbers from console input.
2. Store the operations as functions in a dictionary and call them through it.
3. Let the user continue with the previous result or start a new calculation, restarting by recursion.
4. Cover the behaviour with automated tests and document setup, run and tests in the README.

## Scope

### In Scope

Console program under `src/`, tests under `tests/`, `pyproject.toml`, `Doxyfile`, README, ASCII title and calculator, repository description and topics.

### Out of Scope

Graphical or web interface, further operations, packaging for PyPI, runtime dependencies.

## Expected Benefits

### Tangible Benefits

A working, tested calculator and a reproducible setup with a local `.venv`.

### Intangible Benefits

Practice with the plan-first process on a small project.

## Strategic Alignment

Supports completing the Python Pro Bootcamp with reviewed, portfolio-quality projects.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Operations and loop work | All tests pass | `python -m pytest` |
| 2 | Setup is reproducible | README steps work on a clean `.venv` | Manual run of the README |
| 3 | No runtime dependencies | Empty dependency list | `pyproject.toml` |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Doxygen is not installed locally | Docs build not checked | README names it as optional |
| Token in `.env` leaks | Account compromise | `.env` stays git-ignored and is never read by the project |

## Assumptions

- Python 3.13 or newer is installed.
- The git host is reachable for issues and pull requests.

## Constraints

- Python 3.13 or newer, `venv`, folders `src/`, `tests/`, `docs/`, constants in `constants.py`.
- No commit or push without the Product Owner's request.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| A few hours of the Product Owner's time | A finished, documented assignment and a reusable project skeleton |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns the assignment, does the work and accepts each milestone |

## Recommendation

Proceed — the scope is small, the cost is low and it completes the assignment.

---

[SA-001]: ./stakeholder-analysis.md
[8ccefff]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/010-calc/commit/8ccefffef7ec1f9ecbf548085a5c92fae75e1341
